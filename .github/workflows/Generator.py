import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import io
import random
from math import gcd
physical_elements = {
    "Fire": "red",
    "Water": "blue",
    "Earth": "saddlebrown",
    "Air": "skyblue",
    "Metal": "lightgray",
    "Crystal": "cyan",
    "Ice": "lightblue",
    "Lightning": "gold",
    "Steam": "gainsboro",
    "Magma": "tomato",
    "Shadow": "dimgray",
    "Wood": "peru",
    "Stone": "sienna",
    "Sand": "tan",
    "Ash": "darkgray",
    "Smoke": "slategray",
    "Lava": "orangered",
    "Obsidian": "black",
    "Flame": "darkorange",
    "Snow": "mintcream",
    "Glass": "lavender",
    "Clay": "rosybrown",
    "Mud": "burlywood",
    "Salt": "ghostwhite",
    "Iron": "silver",
    "Steel": "lightsteelblue",
    "Copper": "chocolate",
    "Bronze": "darkgoldenrod",
    "Lead": "gray",
    "Gold": "gold",
    "Silver": "lightgray",
    "Platinum": "whitesmoke",
    "Diamond": "aliceblue",
    "Pearl": "ivory",
    "Coal": "black",
    "Sulfur": "khaki",
    "Blood": "darkred",
    "Quicksilver": "lightblue",
    "Ether": "blueviolet",
    "Star": "lightyellow",
    "Sun": "goldenrod",
    "Moon": "lightgray",
    "Galaxy": "midnightblue",
    "Nebula": "mediumpurple",
    "Plasma": "deeppink",
    "Dust": "navajowhite",
    "Fog": "lightgray",
    "Mist": "honeydew",
    "Gale": "lightcyan",
    "Tide": "steelblue",
    "Current": "cornflowerblue",
    "Whirlwind": "lightblue",
    "Tornado": "slategray",
    "Quake": "tan",
    "Boulder": "brown",
    "Rock": "saddlebrown",
    "Spark": "orange",
    "Pulse": "hotpink",
    "Drift": "beige",
    "Haze": "seashell",
    "Frost": "powderblue",
    "Glacier": "azure",
    "Storm": "lightslategray",
    "Meteor": "darkslategray",
    "Asteroid": "gray",
    "Comet": "lavenderblush",
    "Volcano": "firebrick",
    "Cinder": "dimgrey",
    "Wave": "dodgerblue",
    "Rain": "paleturquoise",
    "Bubble": "lightcyan",
    "Mudslide": "peru",
    "Pebble": "wheat",
    "Crater": "lightgoldenrodyellow",
    "Thermal": "orange",
    "Aurora": "orchid",
    "Smokecloud": "lightgray",
    "Ember": "indianred",
    "Blizzard": "lightsteelblue",
    "Icicle": "lightcyan",
    "Shale": "slategray",
    "Echo": "silver",
    "Wisp": "aliceblue",
    "Beam": "lightyellow",
    "Root": "darkolivegreen",
    "Petal": "pink",
    "Seed": "yellowgreen",
    "Branch": "sienna",
    "Thorn": "darkseagreen",
    "Vine": "olivedrab",
    "Bark": "saddlebrown",
    "Sap": "goldenrod",
    "Pollen": "lemonchiffon",
    "Field": "mediumseagreen",
    "Forest": "darkgreen",
    "Jungle": "green",
    "River": "deepskyblue",
    "Lake": "royalblue",
    "Ocean": "teal",
    "Cave": "dimgray",
    "Tundra": "lightblue",
    "Savanna": "darkkhaki",
    "Desert": "moccasin",
    "Marsh": "olive",
    "Reef": "mediumaquamarine"
}

conceptual_elements = {
    "Hope": "honeydew",
    "Fear": "dimgray",
    "Love": "pink",
    "Hate": "maroon",
    "Peace": "lightgreen",
    "War": "crimson",
    "Truth": "ivory",
    "Lies": "darkslategray",
    "Order": "beige",
    "Chaos": "orchid",
    "Joy": "gold",
    "Sorrow": "slateblue",
    "Wisdom": "cornsilk",
    "Ignorance": "lightgray",
    "Faith": "linen",
    "Doubt": "darkgray",
    "Honor": "navajowhite",
    "Betrayal": "firebrick",
    "Freedom": "skyblue",
    "Control": "gray",
    "Justice": "lightsteelblue",
    "Corruption": "darkmagenta",
    "Patience": "mintcream",
    "Anger": "indianred",
    "Kindness": "lightpink",
    "Jealousy": "yellowgreen",
    "Greed": "darkseagreen",
    "Pride": "mediumorchid",
    "Humility": "ghostwhite",
    "Dream": "thistle",
    "Nightmare": "black",
    "Memory": "mistyrose",
    "Amnesia": "slategrey",
    "Unity": "lightyellow",
    "Division": "purple",
    "Compassion": "lightcoral",
    "Apathy": "lightslategrey",
    "Logic": "lightblue",
    "Emotion": "deeppink",
    "Science": "steelblue",
    "Magic": "blueviolet",
    "Time": "darkgray",
    "Eternity": "azure",
    "Mortality": "darkred",
    "Immortality": "lavender",
    "Purpose": "khaki",
    "Despair": "darkslateblue",
    "Glory": "lightgoldenrodyellow",
    "Failure": "rosybrown",
    "Envy": "greenyellow",
    "Lust": "crimson",
    "Wrath": "firebrick",
    "Virtue": "mintcream",
    "Sin": "darkolivegreen",
    "Fate": "plum",
    "Chance": "tan",
    "Destiny": "wheat",
    "Silence": "lightgray",
    "Sound": "mediumseagreen",
    "Vision": "lightcyan",
    "Blindness": "slategray",
    "Revelation": "lightyellow",
    "Illusion": "lavender",
    "Truthfulness": "floralwhite",
    "Deceit": "darkslategrey",
    "Trust": "cornflowerblue",
    "Suspicion": "darkgray",
    "Balance": "ghostwhite",
    "Disorder": "indigo",
    "Memory": "mistyrose",
    "Forgetfulness": "lightgray",
    "Tradition": "antiquewhite",
    "Innovation": "lightblue",
    "Curiosity": "lightseagreen",
    "Fearlessness": "goldenrod",
    "Awareness": "lightyellow",
    "Neglect": "lightslategrey",
    "Rebirth": "palegreen",
    "Decay": "sienna",
    "Calm": "lightcyan",
    "Anxiety": "tomato",
    "Security": "seashell",
    "Risk": "salmon",
    "Honor": "papayawhip",
    "Dishonor": "brown",
    "Grace": "lavenderblush",
    "Burden": "grey",
    "Clarity": "aliceblue",
    "Confusion": "mediumpurple",
    "Inspiration": "lightgoldenrodyellow",
    "Oppression": "slategray",
    "Sanity": "lightgreen",
    "Madness": "darkorchid",
    "Light": "lemonchiffon",
    "Darkness": "black",
    "Memory": "mistyrose",
    "Knowledge": "beige",
    "Belief": "lightblue",
    "Imagination": "orchid",
    "Spirituality": "mediumslateblue"
}


combined_elements = {**physical_elements, **conceptual_elements}
physical_living_elements = {
    "Fire": "red",
    "Water": "blue",
    "Earth": "saddlebrown",
    "Air": "skyblue",
    "Metal": "lightgray",
    "Crystal": "cyan",
    "Stone": "sienna",
    "Sand": "tan",
    "Mud": "burlywood",
    "Ice": "lightblue",
    "Lava": "orangered",
    "Lightning": "gold",
    "Wood": "peru",
    "Grass": "yellowgreen",
    "Leaf": "mediumseagreen",
    "Tree": "forestgreen",
    "Root": "darkolivegreen",
    "Flower": "orchid",
    "Petal": "pink",
    "Fruit": "coral",
    "Seed": "wheat",
    "Vine": "olivedrab",
    "Thorn": "darkseagreen",
    "Branch": "sienna",
    "Bark": "chocolate",
    "Sap": "goldenrod",
    "Soil": "saddlebrown",
    "Moss": "lightgreen",
    "Fungus": "plum",
    "Bacteria": "slateblue",
    "Virus": "indianred",
    "Cell": "beige",
    "Organ": "rosybrown",
    "Blood": "crimson",
    "Bone": "ivory",
    "Flesh": "salmon",
    "Muscle": "tomato",
    "Heart": "firebrick",
    "Brain": "lightcoral",
    "Nerve": "lightpink",
    "Lung": "peachpuff",
    "Skin": "navajowhite",
    "Hair": "gray",
    "Feather": "lavender",
    "Fur": "lightgray",
    "Shell": "papayawhip",
    "Claw": "sienna",
    "Horn": "tan",
    "Tail": "burlywood",
    "Beak": "gold",
    "Wing": "skyblue",
    "Eye": "blue",
    "Ear": "mistyrose",
    "Voice": "lightsteelblue",
    "Roar": "orange",
    "Scent": "lemonchiffon",
    "Paw": "sandybrown",
    "Hoof": "peru",
    "Scale": "seagreen",
    "Fin": "aqua",
    "Tentacle": "mediumorchid",
    "Web": "lightcyan",
    "Hive": "khaki",
    "Nest": "beige",
    "Egg": "ivory",
    "Larva": "palegreen",
    "Cocoon": "linen",
    "Beetle": "black",
    "Butterfly": "violet",
    "Ant": "brown",
    "Bee": "goldenrod",
    "Bird": "lightblue",
    "Fish": "deepskyblue",
    "Lizard": "darkolivegreen",
    "Snake": "darkseagreen",
    "Spider": "darkgray",
    "Frog": "mediumseagreen",
    "Wolf": "gray",
    "Bear": "saddlebrown",
    "Lion": "darkgoldenrod",
    "Tiger": "orangered",
    "Fox": "chocolate",
    "Rabbit": "white",
    "Mouse": "gainsboro",
    "Deer": "peru",
    "Horse": "sienna",
    "Cow": "cornsilk",
    "Dog": "sandybrown",
    "Cat": "lightgray",
    "Human": "bisque",
    "Spirit": "mintcream",
    "Ghost": "aliceblue",
    "Soul": "lavenderblush",
    "Breath": "honeydew",
    "Heartbeat": "lightpink",
    "Instinct": "thistle",
    "Symbiosis": "lightgreen",
    "Adaptation": "lightblue",
    "Evolution": "palegoldenrod"
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
          
