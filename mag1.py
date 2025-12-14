import streamlit as st

# --- KRYTYCZNA ZMIANA: Inicjalizacja Magazynu w Stanie Sesji ---
# To jest jedyny sposób, aby Streamlit 'zapamiętał' listę
# pomiędzy kliknięciami przycisków i wprowadzaniem danych.
if 'magazyn_items' not in st.session_state:
    st.session_state['magazyn_items'] = [
        {"nazwa": "Laptop", "ilosc": 5},
        {"nazwa": "Kabel USB", "ilosc": 20}
    ]

# Przypisanie listy z sesji do zmiennej dla łatwiejszego dostępu
magazyn_items = st.session_state['magazyn_items']
# ----------------------------------------------------------------

# --- Konfiguracja Strony ---
st.title("✅ Poprawiony Magazyn Streamlit")
st.markdown("Aplikacja używa stanu sesji (`st.session_state`), aby **zachować wszystkie** dodane produkty.")

# --- Funkcje Logiki Magazynu ---

def dodaj_towar(nazwa, ilosc):
    """Dodaje nowy towar do magazynu w sesji."""
    if nazwa and ilosc > 0:
        magazyn_items.append({
            "nazwa": nazwa,
            "ilosc": ilosc
        })
        st.success(f"Dodano: {nazwa} (Ilość: {ilosc})")

def usun_towar(indeks):
    """Usuwa towar z magazynu w sesji i wymusza odświeżenie."""
    if 0 <= indeks < len(magazyn_items):
        usuniety_towar = magazyn_items.pop(indeks)
        st.warning(f"Usunięto: {usuniety_towar['nazwa']}")
        st.rerun() # Wymuszenie odświeżenia, aby lista natychmiast się zaktualizowała


# --- Sekcja Dodawania Towaru ---
st.header("➕ Dodaj Nowy Towar")
col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    # Używamy st.text_input z kluczem, ale dane pobieramy bezpośrednio
    nowa_nazwa = st.text_input("Nazwa Towaru", key="simple_input_nazwa")
with col2:
    nowa_ilosc = st.number_input("Ilość", min_value=1, step=1, value=1, key="simple_input_ilosc")
with col3:
    st.write(" ")
    # Przycisk dodawania
    if st.button("Dodaj do Magazynu", use_container_width=True):
        dodaj_towar(nowa_nazwa, nowa_ilosc)
        # Opcjonalne: Wyczyszczenie pól, aby uniknąć przypadkowego ponownego dodania
        st.session_state.simple_input_nazwa = ""
        st.session_state.simple_input_ilosc = 1


# --- Sekcja Wyświetlania i Usuwania Towarów ---
st.header("📋 Aktualny Stan Listy")

if not magazyn_items:
    st.info("Lista jest pusta. Dodaj pierwszy towar powyżej!")
else:
    # Wyświetlanie listy jako tabeli
    st.table(magazyn_items)

    # --- Sekcja Usuwania ---
    st.header("➖ Usuń Towar")

    # Tworzenie listy opcji do usunięcia
    opcje_usuwania = [f"{i+1}. {item['nazwa']} (Ilość: {item['ilosc']})" for i, item in enumerate(magazyn_items)]
    
    # Używamy selectbox do wyboru, który element usunąć
    wybor_indeksu = st.selectbox(
        "Wybierz towar do usunięcia",
        options=list(range(len(magazyn_items))),
        format_func=lambda x: opcje_usuwania[x],
        key="usun_selectbox"
    )
    
    # Przycisk usuwania
    if st.button("Usuń Wybrany Towar"):
        usun_towar(wybor_indeksu)
