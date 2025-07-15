import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import io
import random

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


    
elm = list(element_colors.keys())

st.set_page_config(page_title="Random Regular Graph Generator", layout="centered")

st.title("🎲 Random Regular Graph Generator")

st.markdown("""
This app generates a **random regular graph** based on the number of nodes (`n`) and the degree (`d`).
- A *d*-regular graph is one where each node has exactly *d* connections.
""")

# User input
n = st.number_input("Number of nodes (n)", min_value=1, value=10)
d = st.number_input("Degree of each node (d)", min_value=0, value=2)
nsize = st.number_input("Degree of each node (d)", min_value=0, value=9000)

use_seed = st.sidebar.checkbox("Use seed")
seed_val = st.sidebar.number_input("Seed value", min_value=0, value=42, step=1, disabled=not use_seed)

# Button to generate graph
if st.button("Generate Graph"):
    # Check if a regular graph is possible
    if n * d % 2 != 0:
        st.error("❌ Invalid input: n * d must be even for a regular graph to exist.")
    elif d >= n:
        st.error("❌ Invalid input: Degree must be less than the number of nodes.")
    else:
        try:
            if use_seed:
                random.seed(seed_val)
                G = nx.random_regular_graph(d, n, seed=seed_val)
            else:
                G = nx.random_regular_graph(d, n)
    
            random.shuffle(elm)
            mapping =dict(zip(list(G.nodes), elm[0:n]))
            G = nx.relabel_nodes(G, mapping)

            node_colours = []

            for node in G.nodes:
                node_colours.append(element_colors[node])

            # Draw graph
            fig, ax = plt.subplots(figsize=(6, 6))
            nx.draw_circular(G, with_labels=True, node_color = node_colours, edge_color="gray", node_size=nsize, ax=ax)
            st.pyplot(fig)

            # Downloadable image
            buf = io.BytesIO()
            fig.savefig(buf, format="png")
            st.download_button("📥 Download Graph as PNG", buf.getvalue(), "regular_graph.png", "image/png")

        except Exception as e:
            st.error(f"❌ Error generating graph: {e}")
          
