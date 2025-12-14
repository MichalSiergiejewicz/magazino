import streamlit as st

# --- Definicja Magazynu (GLOBALNA LISTA) ---
# Ostrzeżenie: Ta lista jest resetowana do stanu początkowego przy każdej interakcji.
magazyn_items = [
    {"nazwa": "Laptop", "ilosc": 5},
    {"nazwa": "Kabel USB", "ilosc": 20},
    {"nazwa": "Myszka bezprzewodowa", "ilosc": 15}
]

# --- Konfiguracja Strony ---
st.set_page_config(page_title="Nietrwały Magazyn Streamlit", layout="centered")
st.title("💡 Nietrwały Magazyn - Demo Listy Pythona")
st.error("UWAGA: Dane są resetowane po każdym kliknięciu przycisku 'Dodaj' lub 'Usuń', ponieważ kod nie używa st.session_state.")


# --- Sekcja Dodawania Towaru ---
st.header("➕ Dodaj Towar (Tymczasowo)")
col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    nowa_nazwa = st.text_input("Nazwa Towaru", key="input_nazwa")
with col2:
    nowa_ilosc = st.number_input("Ilość", min_value=1, step=1, value=1, key="input_ilosc")
with col3:
    st.write(" ")
    
    if st.button("Dodaj do Magazynu"):
        if nowa_nazwa and nowa_ilosc > 0:
            # Towar zostaje dodany DO BIEŻĄCEJ KOPII listy w tym jednym przebiegu skryptu
            magazyn_items.append({"nazwa": nowa_nazwa, "ilosc": nowa_ilosc})
            
            st.success(f"Tymczasowo dodano: {nowa_nazwa}. Lista poniżej jest zaktualizowana, ale po kolejnym kliknięciu wróci do stanu początkowego.")
        else:
            st.warning("Wprowadź poprawną nazwę i ilość.")

# --- Sekcja Wyświetlania ---
st.header("📋 Aktualny Stan Listy")

if not magazyn_items:
    st.info("Lista jest pusta.")
else:
    # Wyświetlanie listy jako tabeli
    st.table(magazyn_items)

    # --- Sekcja Usuwania ---
    st.header("➖ Usuń Towar (Tymczasowo)")
    
    # Tworzenie listy opcji do usunięcia
    opcje_usuwania = [f"{i+1}. {item['nazwa']} (Ilość: {item['ilosc']})" for i, item in enumerate(magazyn_items)]
    
    # Wybór indeksu elementu do usunięcia
    wybor_indeksu = st.selectbox(
        "Wybierz element do usunięcia (wybór bazuje na aktualnej, tymczasowej liście)",
        options=list(range(len(magazyn_items))),
        format_func=lambda x: opcje_usuwania[x]
    )
    
    if st.button("Usuń Wybrany Towar"):
        # Towar zostaje usunięty z BIEŻĄCEJ KOPII listy
        usuniety = magazyn_items.pop(wybor_indeksu)
        st.error(f"Tymczasowo usunięto: {usuniety['nazwa']}. Lista zaraz wróci do stanu początkowego.")


# --- Sekcja Instrukcji ---
st.markdown("---")
st.info("Aby stworzyć **działający** magazyn, który pamięta zmiany, zamień logikę na użycie `st.session_state`.")
