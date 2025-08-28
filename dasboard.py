import streamlit as st

# Page configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Title
st.title("📊 Sales Dashboard")

# Main Filter
main_filter = st.radio("Select Sales Type:", ["Primary Sales", "Secondary Sales"])

# Primary Sales Selected
if main_filter == "Primary Sales":
    primary_type = st.radio("Select Type:", ["Incoming", "Outgoing"])

    # Incoming Selected
    if primary_type == "Incoming":
        st.subheader("🔽 Select Details for Incoming:")

        # 2 Columns layout for dropdowns
        col1, col2 = st.columns(2)

        with col1:
            gsp = st.selectbox("GSP", ["Select", "Option 1", "Option 2", "Option 3"])
            mechnova = st.selectbox("Mechnova", ["Select", "Option A", "Option B"])

        with col2:
            stronwell1 = st.selectbox("Stronwell 1", ["Select", "Alpha", "Beta"])
            stronwell2 = st.selectbox("Stronwell 2", ["Select", "Gamma", "Delta"])
            gardening = st.selectbox("Gardening", ["Select", "Item X", "Item Y"])

        # Display selected values
        st.markdown("---")
        st.write("### ✅ Your Selections:")
        st.write(f"**GSP:** {gsp}")
        st.write(f"**Mechnova:** {mechnova}")
        st.write(f"**Stronwell 1:** {stronwell1}")
        st.write(f"**Stronwell 2:** {stronwell2}")
        st.write(f"**Gardening:** {gardening}")

    elif primary_type == "Outgoing":
        st.warning("⚠️ Outgoing data UI is under construction.")

# Secondary Sales Selected
elif main_filter == "Secondary Sales":
    st.info("ℹ️ Secondary Sales filter functionality coming soon.")
