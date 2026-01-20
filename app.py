import streamlit as st


dictionary_data = {
    "Hello": {
        "Hausa": "Sannu",
        "Yoruba": "Pẹlẹ o",
        "Igbo": "Nnọọ",
        "Igala": "Agba",
        "Edo": "Kóyo"
    },
    "Thank you": {
        "Hausa": "Nagode",
        "Yoruba": "E ṣe",
        "Igbo": "Imela",
        "Igala": "Agba",
        "Edo": "Uruese"
    },
    "Water": {
        "Hausa": "Ruwa",
        "Yoruba": "Omi",
        "Igbo": "Mmiri",
        "Igala": "Ami",
        "Edo": "Amen"
    },
    "Come": {
        "Hausa": "Zo",
        "Yoruba": "Wa",
        "Igbo": "Bịa",
        "Igala": "Lia",
        "Edo": "Khian"
    },
    "Eat": {
        "Hausa": "Ci",
        "Yoruba": "Jẹ",
        "Igbo": "Rie",
        "Igala": "Je",
        "Edo": "Re"
    },
    "Eye": {
        "Hausa": "Ido",
        "Yoruba": "Oju",
        "Igbo": "Anya",
        "Igala": "Éjū",
        "Edo": "Aró"
    },
    "Good morning": {
        "Hausa": "ina kwana",
        "Igbo": "Ututu oma",
        "Yoruba": "E ku aaro",
        "Igala": "Oludu",
        "Edo": "Obie owie"

    },
}


st.set_page_config(page_title="Nigerian Multi-Lang Dictionary", page_icon="🇳🇬")

st.title("🇳🇬 Nigerian Languages Dictionary")
st.write("Translate English words into **Hausa, Yoruba, Igbo, Igala, and Edo**.")


languages = ["Hausa", "Yoruba", "Igbo", "Igala", "Edo"]
selected_lang = st.sidebar.selectbox("Select Target Language", languages)

# 4. Search Functionality
search_term = st.text_input("Enter an English word (e.g., Hello, Good morning, Eat):").capitalize().strip()

if search_term:
    if search_term in dictionary_data:
        translation = dictionary_data[search_term][selected_lang]

        st.success(f"### {selected_lang} Translation:")
        st.header(translation)

        # Show all versions in a table for comparison
        with st.expander("See comparison in all languages"):
            st.table(dictionary_data[search_term])
    else:
        st.error("Word not found in the dictionary. Try 'Water' or 'Hello'.")

st.divider()
st.info("Tip: You can expand the dataset by adding more entries to the `dictionary_data` variable in the code.")

