nigerian_dic = {
    "Igbo": {
        "Hello / Greetings": "Ndewo",
        "Thank you": "Daalụ",
        "Please": "Biko",
        "Yes": "Ee",
        "No": "Mba",
        "How are you?": "Kedu?",
        "I am fine": "Adị m mma",
        "Food": "Nri",
        "Water": "Mmiri",
        "Morning": "Ụtụtụ",
        "Afternoon": "Ehihie",
        "Evening": "Anyasị",
        "Name": "Aha",
        "Man / Male": "Nwoke",
        "Woman / Female": "Nwanyị",
        "House": "Ụlọ",
        "Cloth / Fabric": "Akwa",
        "Money": "Ego",
        "Time": "Oge",
        "Person": "Onye"
    },
    "Hausa": {
        "Hello / Greetings": "Sannu",
        "Thank you": "Na gode",
        "Please": "Don Allah",
        "Yes": "I",
        "No": "A'a",
        "How are you?": "Yaya kake? (M) / Yaya kike? (F)",
        "Fine / Peace (used as a reply to a greeting)": "Lafiya",
        "Food": "Abinci",
        "Water": "Ruwa",
        "Morning": "Safiya",
        "Day / Sun": "Rana",
        "Night": "Dare",
        "Name": "Suna",
        "Person / Human": "Mutum",
        "Man / Male": "Namiji",
        "Woman / Female": "Mace",
        "House": "Gida",
        "Money": "Kudi",
        "Blessing / Welcome": "Barka",
        "Near": "Kusa"
    },
    "Yoruba": {
        "Hello / Greetings (General)": "Ẹ ńlẹ́ o",
        "Thank you": "Ẹ ṣé",
        "Please": "Ẹ jọ̀ọ́",
        "Yes": "Bẹ́ẹ̀ni",
        "No": "Rárá",
        "How are you?": "Báwo ni?",
        "I am fine": "Mo wà dáadáa",
        "Food": "Oúnjẹ",
        "Water": "Omi",
        "Morning": "Òwúrọ̀",
        "Noon / Afternoon": "Ọsán",
        "Evening": "Ìrọ̀lẹ́",
        "Name": "Orúkọ",
        "Man / Male": "Ọkùnrin",
        "Woman / Female": "Obìnrin",
        "House": "Ilé",
        "Cloth / Clothing": "Aṣọ",
        "Money": "Owó",
        "Cold": "Tútù",
        "Hot": "Gbóná"
    },
    "Igala": {
        "Greetings (General)": "Ẹlẹ́",
        "Thank you": "Nagọ",
        "Please": "Ọchẹkẹlẹ",
        "Yes": "Hẹẹ",
        "No": "Mba",
        "How are you?": "Awẹlẹ",
        "I am fine": "Uch’ọlafia",
        "Food": "Ujẹnwu",
        "Water": "Omi",
        "Good Morning (Greeting)": "Ugwa",
        "Good Evening (Greeting)": "Ọlọ́rọka",
        "Night": "Anẹ",
        "Name": "Aha",
        "Husband / Man": "Ọkọ",
        "Wife / Woman": "Ọya",
        "House": "Unyi",
        "Child": "Akwọra",
        "Year": "Ọdọ",
        "Hand": "Ọwọ",
        "Head": "Oji"
    },
    "Edo": {
        "Hello / Good day (General greeting)": "Kóyo",
        "Thank you (more formal)": "Ó khian gbó",
        "Thank you (less formal)": "Ó ghíè ó",
        "Please": "Bí àgbọn",
        "Yes": "Éhèhè",
        "No": "Iháá",
        "How are you?": "Kóyo vbé óbò?",
        "I am fine": "Vbé óbò nà",
        "Food (specifically Pounded Yam/Swallow)": "Ìyán",
        "Water": "Ámá",
        "Morning / Day": "Ókhi",
        "Sun / Time": "Owèdè",
        "Name": "Éyè",
        "Woman / Female": "Ókhuó",
        "Man / Male": "Órèè",
        "House / Home": "Ówá",
        "Clothes / Wrapper": "Éwú",
        "Child": "Óvbé",
        "Day": "Édè",
        "Good Woman": "Ókhuó n'éyè"
    }
}

# --- Corrected Program Logic ---

print("Welcome to the language dictionary")
print("Choose a language to translate English words into:")
print("1. Igbo\n2. Yoruba\n3. Hausa\n4. Edo\n5. Igala")

# Use strip() and lower() to make input flexible
choice = input("Please choose the language number (1-5): ").strip()
language_map = {
    "1": "Igbo",
    "2": "Yoruba",
    "3": "Hausa",
    "4": "Edo",
    "5": "Igala"
}

if choice in language_map:
    language_key = language_map[choice]

    # Optional: Print available words to guide the user
    print(f"\n--- Available English Words for {language_key} ---")
    print(", ".join(nigerian_dic[language_key].keys()))
    print("--------------------------------------------------")

    # The word must exactly match a key in the dictionary
    word = input("Enter the English word or phrase: ").strip()

    # Look up the word in the chosen language's sub-dictionary
    # Use .get() to avoid crashing if the word is not found
    translation = nigerian_dic[language_key].get(word)

    if translation:
        print(f"\nThe {language_key} translation for '{word}' is: *{translation}*")
    else:
        # Provide a helpful error message if the word isn't found
        print(f"\nSorry, the word '{word}' was not found in the {language_key} dictionary. Please check the spelling.")

else:
    print("\nLanguage not currently in program, please try again later 😁😁")