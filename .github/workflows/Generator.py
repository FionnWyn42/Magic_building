import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import io

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

            # Draw graph
            fig, ax = plt.subplots(figsize=(6, 6))
            nx.draw_circular(G, with_labels=True, node_color="skyblue", edge_color="gray", node_size=700, ax=ax)
            st.pyplot(fig)

            # Downloadable image
            buf = io.BytesIO()
            fig.savefig(buf, format="png")
            st.download_button("📥 Download Graph as PNG", buf.getvalue(), "regular_graph.png", "image/png")

        except Exception as e:
            st.error(f"❌ Error generating graph: {e}")
          
