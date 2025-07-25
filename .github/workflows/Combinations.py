import streamlit as st
import numpy as np
import networkx as nx
import math
from itertools import combinations
from pyvis.network import Network
import tempfile

# Example element colors (add more if needed)
element_colors = {
    "Fire": "red",
    "Water": "blue",
    "Earth": "saddlebrown",
    "Air": "skyblue",
    "Light": "lightyellow",
    "Dark": "gray",
    "Metal": "lightgray",
    "Crystal": "cyan",
    "Ice": "lightblue",
    "Lightning": "gold",
    "Steam": "gainsboro",
    "Magma": "tomato",
    "Shadow": "dimgray",
    "Holy": "ivory",
    "Poison": "yellowgreen",
    "Nature": "green",
    "Void": "purple",
    "Chaos": "orchid",
    "Order": "beige",
    "Plasma": "deeppink",
    "Wood": "peru",
    "Glass": "lavender",
    "Sand": "tan",
    "Ash": "darkgray",
    "Smoke": "slategray",
    "Aether": "mediumorchid",
    "Blood": "darkred",
    "Spirit": "mediumpurple",
    "Sound": "mediumseagreen",
    "Energy": "orange",
    "Radiance": "lightgoldenrodyellow",
    "Frost": "powderblue",
    "Corruption": "darkmagenta",
    "Dream": "thistle",
    "Gravity": "dimgray",
    "Echo": "silver",
    "Pulse": "hotpink",
    "Acid": "greenyellow",
    "Venom": "olivedrab",
    "Flame": "darkorange",
    "Mist": "whitesmoke",
    "Obsidian": "black",
    "Lava": "orangered",  # Not allowed! → change to "tomato"
    "Storm": "slategray",
    "Stone": "sienna",
    "Fog": "lightgray",
    "Quake": "rosybrown",
    "Ink": "navy",
    "Force": "slateblue",
    "Moon": "khaki",
    "Sun": "gold",
    "Star": "lightyellow",
    "Dust": "burlywood",
    "Ether": "blueviolet",
    "Spark": "darkorange",
    "Chill": "paleturquoise",
    "Metallic": "lightsteelblue",
    "Gale": "lightblue",
    "Thorn": "darkolivegreen",
    "Toxin": "yellowgreen",
    "Arcane": "mediumslateblue",
    "Blessing": "lemonchiffon",
    "Curse": "indigo",
    "Fear": "dimgray",
    "Hope": "honeydew",
    "Glory": "gold",
    "Decay": "sienna",
    "Silence": "lightgray",
    "Illusion": "lavender",
    "Reality": "beige",
    "Time": "darkgray",
    "Space": "midnightblue",
    "Memory": "mistyrose",
    "Glow": "cornsilk",
    "Rift": "blueviolet",
    "Nether": "darkslategray",
    "Specter": "lightslategray",
    "Flare": "coral",
    "Breeze": "lightcyan",
    "Haze": "lightgray",
    "Blight": "darkolivegreen",
    "Wisp": "aliceblue",
    "Tide": "steelblue",
    "Tempest": "slategray",
    "Whirlwind": "lightblue",
    "Charm": "lightpink",
    "Envy": "limegreen",
    "Greed": "darkseagreen",
    "Wrath": "firebrick",
    "Lust": "crimson",
    "Serenity": "azure",
    "Unity": "mintcream",
    "Balance": "ghostwhite",
    "Fate": "plum",
    "Truth": "ivory",
    "Myth": "thistle",
    "Shatter": "gainsboro"
}

def generate_elemental_combinations_pyvis(pos_elms_colors, p, l, seed=None):
    if seed is not None:
        np.random.seed(seed)

    pos_elms = list(pos_elms_colors.keys())

    N = p
    n = p
    levels = [0]

    for q in range(l):
        new_v = math.comb(n, 2)
        levels.append(N)
        N += new_v
        n = new_v

    levels.append(N)
    elms = np.random.choice(pos_elms, N, replace=False)
    elms_split = []

    for j in range(l + 1):
        elms_l = elms[levels[j]: levels[j + 1]]
        elms_split.append(elms_l)

    edges = []
    for ind in range(l):
        elm_combs = list(combinations(elms_split[ind], 2))
        elms_res = elms_split[ind + 1]
        for k, el in enumerate(elm_combs):
            edges.append([el[0], elms_res[k]])
            edges.append([el[1], elms_res[k]])

    G = nx.DiGraph()
    G.add_edges_from(edges)

    net = Network(height="600px", directed=True)
    net.from_nx(G)

    for n in net.nodes:
        n['color'] = pos_elms_colors.get(n['label'], 'lightgray')
        n['border'] = 'black'

    for e in net.edges:
        e['color'] = pos_elms_colors.get(e['from'], 'gray')

    return net


# --- Streamlit App Interface ---
st.set_page_config("Elemental Combinations", layout="centered")
st.title("🧪 Elemental Combination Graph")

p = st.number_input("Number of base elements (p)", min_value=2, value=4)
l = st.number_input("Number of levels (l)", min_value=1, value=2)

use_seed = st.checkbox("Use random seed")
seed_val = st.number_input("Seed value", min_value=0, value=42) if use_seed else None

if st.button("Generate Graph"):
    try:
        net = generate_elemental_combinations_pyvis(element_colors, p, l, seed=seed_val)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as f:
            net.show(f.name)
            html = open(f.name, 'r', encoding='utf-8').read()
            st.components.v1.html(html, height=650, scrolling=True)
    except Exception as e:
        st.error(f"Error generating graph: {e}")
      
