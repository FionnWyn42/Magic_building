import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import io
import random
from math import gcd

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

def generate_coprime_cycles_graph(n, unique=True):
    G = nx.DiGraph()
    G.add_nodes_from(range(n))

    used_ks = set()

    cycles = []

    for k in range(1, n):
        cycle = [0]
        if gcd(k, n) == 1:
            if unique and n - k in used_ks:
                continue  # skip mirrored version
            used_ks.add(k)

            # Connect nodes in a cycle with step size k
            a = 0
            for i in range(n):
                b = (a + k) % n
                G.add_edge(a, b)
                cycle.append(b)
                a = b
            cycles.append(cycle)

    return G, cycles

    


st.set_page_config(page_title="Random Regular Graph Generator", layout="centered")

st.title("🎲 Random Regular Graph Generator")

st.markdown("""
This app generates a **random regular graph** based on the number of nodes (`n`) and the degree (`d`).
- A *d*-regular graph is one where each node has exactly *d* connections.
""")

method = st.radio("Choose how to define elements:", ["Random", "Custom Input"])

if method == 'Random':

# User input
    n = st.number_input("Number of nodes (n)", min_value=1, value=10)
    elm = list(element_colors.keys())

else:
    element_input = st.text_input("Enter elements (comma-separated)", "Fire,Water,Earth,Air")
    color_input = st.text_input("Enter colors (comma-separated or leave blank for random)", "")

    elements = [e.strip().title() for e in element_input.split(",")]
    
    if color_input.strip() == "":
        available_colors = list(element_colors.values())
        colors = random.sample(available_colors, len(elements))
    else:
        colors = [c.strip().lower() for c in color_input.split(",")]

    if len(elements) != len(colors):
        st.error("Please ensure the number of elements matches the number of colors.")
        st.stop()

    elm = elements
    element_colors = dict(zip(elm, colors))
    n = len(elm)

nsize = st.number_input("Degree of each node (d)", min_value=0, value=2000)

use_seed = st.sidebar.checkbox("Use seed")
seed_val = st.sidebar.number_input("Seed value", min_value=0, value=42, step=1, disabled=not use_seed)

# Button to generate graph
if st.button("Generate Graph"):
    
        try:
            if use_seed:
                seed_used = seed_val 
            else:
                seed_used = random.randint(0, 10**7)
            
            random.seed(seed_used)
            G, cycles = generate_coprime_cycles_graph(n)
            
            random.shuffle(elm)
            mapping =dict(zip(list(G.nodes), elm[0:n]))
            G = nx.relabel_nodes(G, mapping)

            node_colours = []

            for node in G.nodes:
                node_colours.append(element_colors[node])

            # Draw graph
            fig, ax = plt.subplots(figsize=(6, 6))
            nx.draw_circular(G, with_labels=True, node_color = node_colours, edge_color="gray", node_size=nsize, ax=ax, arrows = True)
            st.pyplot(fig)

            st.success(f"Seed used: `{seed_used}`")
            st.code(f"{seed_used}", language="python")

            # Downloadable image
            buf = io.BytesIO()
            fig.savefig(buf, format="png")
            st.download_button("📥 Download Graph as PNG", buf.getvalue(), "regular_graph.png", "image/pn")
            cycle_names = [
           "generating",
           "overcoming",
           "absorbing",
           "balancing",
           "draining",
           "transforming"
             ]
            for j, cycle in enumerate(cycles):
                map_c = [mapping[c] for c in cycle]
                
                cycle_text = ' ->  '.join(map_c)
                st.text(cycle_names[j%len(cycle_names)])
                st.text(cycle_text)
                               
        except Exception as e:
            st.error(f"❌ Error generating graph: {e}")
          
