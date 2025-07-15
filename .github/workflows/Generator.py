import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import io

element_colors = {
    "Fire": "#FF4500",       # orange-red
    "Water": "#1E90FF",      # dodger blue
    "Earth": "#8B4513",      # saddle brown
    "Air": "#87CEEB",        # sky blue
    "Light": "#FFFFE0",      # light yellow
    "Dark": "#2F4F4F",       # dark slate gray
    "Metal": "#B0C4DE",      # light steel blue
    "Crystal": "#E0FFFF",    # light cyan
    "Ice": "#AFEEEE",        # pale turquoise
    "Lightning": "#FFD700",  # gold
    "Steam": "#D3D3D3",      # light gray
    "Magma": "#FF6347",      # tomato red
    "Shadow": "#696969",     # dim gray
    "Holy": "#FFF8DC",       # cornsilk
    "Poison": "#7FFF00",     # chartreuse
    "Nature": "#228B22",     # forest green
    "Void": "#4B0082",       # indigo
    "Chaos": "#DA70D6",      # orchid
    "Order": "#F5F5DC",      # beige
    "Plasma": "#FF69B4",     # hot pink
    "Wood": "#DEB887",       # burlywood
    "Glass": "#E6E6FA",      # lavender
    "Sand": "#F4A460",       # sandy brown
    "Ash": "#A9A9A9",        # dark gray
    "Smoke": "#708090",      # slate gray
    "Aether": "#BA55D3",     # medium orchid
    "Blood": "#8B0000",      # dark red
    "Spirit": "#9370DB",     # medium purple
    "Sound": "#20B2AA",      # light sea green
    "Energy": "#FFA500",     # orange
    "Radiance": "#FFFACD",   # lemon chiffon
    "Frost": "#E0FFFF",      # light cyan
    "Corruption": "#8B008B", # dark magenta
    "Dream": "#D8BFD8",      # thistle
    "Gravity": "#696969",    # dim gray
    "Echo": "#C0C0C0",       # silver
    "Pulse": "#FF1493",      # deep pink
    "Acid": "#ADFF2F",       # green yellow
    "Venom": "#9ACD32",      # yellow green
    "Flame": "#FF6347",      # tomato
    "Mist": "#F5F5F5",       # white smoke
    "Obsidian": "#2E2E2E",   # dark charcoal
    "Lava": "#FF4500",       # orange red
    "Storm": "#708090",      # slate gray
    "Stone": "#A0522D",      # sienna
    "Fog": "#DCDCDC",        # gainsboro
    "Quake": "#BC8F8F",      # rosy brown
    "Ink": "#191970",        # midnight blue
    "Force": "#7B68EE",      # medium slate blue
    "Moon": "#F0E68C",       # khaki
    "Sun": "#FFD700",        # gold
    "Star": "#FFFACD",       # lemon chiffon
    "Dust": "#D2B48C",       # tan
    "Ether": "#8A2BE2",      # blue violet
    "Spark": "#FF8C00",      # dark orange
    "Chill": "#AFEEEE",      # pale turquoise
    "Metallic": "#B0C4DE",   # light steel blue
    "Gale": "#ADD8E6",       # light blue
    "Thorn": "#556B2F",      # dark olive green
    "Toxin": "#6B8E23",      # olive drab
    "Arcane": "#9370DB",     # medium purple
    "Blessing": "#FFFACD",   # lemon chiffon
    "Curse": "#4B0082",      # indigo
    "Fear": "#696969",       # dim gray
    "Hope": "#F0FFF0",       # honeydew
    "Glory": "#FFD700",      # gold
    "Decay": "#8B4513",      # brown
    "Silence": "#C0C0C0",    # silver
    "Illusion": "#E6E6FA",   # lavender
    "Reality": "#F5F5DC",    # beige
    "Time": "#A9A9A9",       # dark gray
    "Space": "#483D8B",      # dark slate blue
    "Memory": "#FFE4E1",     # misty rose
    "Glow": "#FFF8DC",       # cornsilk
    "Rift": "#8A2BE2",       # blue violet
    "Nether": "#2F4F4F",     # dark slate gray
    "Specter": "#778899",    # light slate gray
    "Flare": "#FF7F50",      # coral
    "Breeze": "#AFEEEE",     # pale turquoise
    "Haze": "#D3D3D3",       # light gray
    "Blight": "#556B2F",     # dark olive green
    "Wisp": "#F0F8FF",       # alice blue
    "Tide": "#4682B4",       # steel blue
    "Tempest": "#708090",    # slate gray
    "Whirlwind": "#ADD8E6",  # light blue
    "Charm": "#FFB6C1",      # light pink
    "Envy": "#7FFF00",       # chartreuse
    "Greed": "#9ACD32",      # yellow green
    "Wrath": "#B22222",      # firebrick
    "Lust": "#DC143C",       # crimson
    "Serenity": "#E0FFFF",   # light cyan
    "Unity": "#F0FFF0",      # honeydew
    "Balance": "#F5F5F5",    # white smoke
    "Fate": "#DDA0DD",       # plum
    "Truth": "#FFFFF0",      # ivory
    "Myth": "#E6E6FA",       # lavender
    "Shatter": "#DCDCDC"     # gainsboro
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
          
