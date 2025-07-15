import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import io


element_colors_named = {
    "Fire": "orangered",
    "Water": "dodgerblue",
    "Earth": "saddlebrown",
    "Air": "skyblue",
    "Light": "lightyellow",
    "Dark": "dimgray",
    "Metal": "lightsteelblue",
    "Crystal": "lightcyan",
    "Ice": "paleturquoise",
    "Lightning": "gold",
    "Steam": "lightgray",
    "Magma": "tomato",
    "Shadow": "gray",
    "Holy": "cornsilk",
    "Poison": "chartreuse",
    "Nature": "forestgreen",
    "Void": "indigo",
    "Chaos": "orchid",
    "Order": "beige",
    "Plasma": "hotpink",
    "Wood": "burlywood",
    "Glass": "lavender",
    "Sand": "sandybrown",
    "Ash": "darkgray",
    "Smoke": "slategray",
    "Aether": "mediumorchid",
    "Blood": "darkred",
    "Spirit": "mediumpurple",
    "Sound": "mediumseagreen",
    "Energy": "orange",
    "Radiance": "lemonchiffon",
    "Frost": "powderblue",
    "Corruption": "darkmagenta",
    "Dream": "thistle",
    "Gravity": "dimgray",
    "Echo": "silver",
    "Pulse": "deeppink",
    "Acid": "greenyellow",
    "Venom": "yellowgreen",
    "Flame": "tomato",
    "Mist": "whitesmoke",
    "Obsidian": "black",
    "Lava": "orangered",
    "Storm": "slategray",
    "Stone": "sienna",
    "Fog": "gainsboro",
    "Quake": "rosybrown",
    "Ink": "midnightblue",
    "Force": "mediumslateblue",
    "Moon": "khaki",
    "Sun": "gold",
    "Star": "lightgoldenrodyellow",
    "Dust": "tan",
    "Ether": "blueviolet",
    "Spark": "darkorange",
    "Chill": "paleturquoise",
    "Metallic": "lightsteelblue",
    "Gale": "lightblue",
    "Thorn": "darkolivegreen",
    "Toxin": "olivedrab",
    "Arcane": "mediumpurple",
    "Blessing": "lemonchiffon",
    "Curse": "indigo",
    "Fear": "gray",
    "Hope": "honeydew",
    "Glory": "gold",
}

    
elm = list(element_colors.values())

st.set_page_config(page_title="Random Regular Graph Generator", layout="centered")

st.title("🎲 Random Regular Graph Generator")

st.markdown("""
This app generates a **random regular graph** based on the number of nodes (`n`) and the degree (`d`).
- A *d*-regular graph is one where each node has exactly *d* connections.
""")

# User input
n = st.number_input("Number of nodes (n)", min_value=1, value=10)
d = st.number_input("Degree of each node (d)", min_value=0, value=2)

# Button to generate graph
if st.button("Generate Graph"):
    # Check if a regular graph is possible
    if n * d % 2 != 0:
        st.error("❌ Invalid input: n * d must be even for a regular graph to exist.")
    elif d >= n:
        st.error("❌ Invalid input: Degree must be less than the number of nodes.")
    else:
        try:
            G = nx.random_regular_graph(d, n)

            mapping =dict(zip(list(G.nodes), elm[0:n]))
            G = nx.relabel_nodes(G, mapping)

            node_colours = []

            for node in G.nodes:
                node_colours.append(element_colors[node])

            # Draw graph
            fig, ax = plt.subplots(figsize=(6, 6))
            nx.draw_circular(G, with_labels=True, node_color=node_colours, edge_color="gray", node_size=700, ax=ax)
            st.pyplot(fig)

            # Downloadable image
            buf = io.BytesIO()
            fig.savefig(buf, format="png")
            st.download_button("📥 Download Graph as PNG", buf.getvalue(), "regular_graph.png", "image/png")

        except Exception as e:
            st.error(f"❌ Error generating graph: {e}")
          
