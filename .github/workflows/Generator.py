import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import io
import random
from math import gcd

physical_elements = {
    "Fire": "red", "Water": "blue", "Earth": "saddlebrown", "Air": "skyblue", "Metal": "gray",
    "Crystal": "cyan", "Ice": "lightblue", "Lava": "orangered", "Sand": "tan", "Mud": "burlywood",
    "Wood": "peru", "Lightning": "gold", "Steam": "lightgray", "Smoke": "dimgray", "Ash": "darkgray",
    "Stone": "slategray", "Salt": "whitesmoke", "Clay": "chocolate", "Dust": "lightgrey", "Snow": "azure"
}
conceptual_elements = {
    "Hope": "lightyellow", "Fear": "darkred", "Love": "deeppink", "Hate": "black", "Wisdom": "navy",
    "Madness": "purple", "Peace": "lightblue", "Chaos": "orange", "Order": "lightgray", "Science": "green"
}
combined_elements = {**physical_elements, **conceptual_elements}
physical_living_elements = {
    "Fire": "red", "Water": "blue", "Earth": "saddlebrown", "Air": "skyblue", "Metal": "gray",
    "Tree": "forestgreen", "Leaf": "mediumseagreen", "Blood": "crimson", "Bone": "ivory", "Fur": "lightgray",
    "Feather": "lavender", "Wing": "skyblue", "Eye": "blue", "Heart": "firebrick", "Skin": "navajowhite",
    "Hair": "gray", "Seed": "wheat", "Vine": "olivedrab", "Moss": "lightgreen", "Flower": "orchid",
    "Petal": "pink"
}
random_weird_elements = {
    "Christmas": "red", "Box": "saddlebrown", "Engine": "dimgray", "Basement": "gray", "Constitution": "gold",
    "WiFi": "blue", "Homework": "lightpink", "Alarm": "crimson", "Pillow": "ivory", "Mustache": "sienna",
    "Caffeine": "darkorange", "Toilet": "gainsboro", "Meme": "hotpink", "Cringe": "plum", "Lecture": "slategray",
    "Printer": "silver", "Cupcake": "lightyellow", "Boredom": "gray", "Treadmill": "lightslategray", "Banana": "gold"
}

# --- Element Sets ---
element_sets = {
    "Physical Elements": physical_elements,
    "Conceptual Elements": conceptual_elements,
    "Combined Elements": combined_elements,
    "Physical + Living Elements": physical_living_elements,
    "Random Weird Elements": random_weird_elements
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

st.title("🎲 Elemental Cycles Generator")

st.markdown("""
This app generates a random set of elemental cycles
""")
set_choice = st.selectbox("Choose an element set", list(element_sets.keys()))
element_colors = element_sets[set_choice]
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

nsize = st.number_input("Size of Node", min_value=0, value=2000)

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

            if method == 'Random':
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
           "transforming",
           "refining",
           "obliterating"
           "despising",
           "hatred"
        
             ]
            for j, cycle in enumerate(cycles):
                map_c = [mapping[c] for c in cycle]
                
                cycle_text = ' ->  '.join(map_c)
                st.text(cycle_names[j%len(cycle_names)])
                st.text(cycle_text)
                               
        except Exception as e:
            st.error(f"❌ Error generating graph: {e}")
          
