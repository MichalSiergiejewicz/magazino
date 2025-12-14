import streamlit as st

# --- Definicja Magazynu (Globalna Lista) ---
# Uwaga: Ta lista jest resetowana za każdym razem, gdy użytkownik kliknie przycisk
# lub wprowadzi zmianę w interfejsie Streamlit.
magazyn_items = [
    {"nazwa": "Laptop", "ilosc": 5},
    {"nazwa": "Kabel USB", "ilosc": 20}
]

# --- Konfiguracja Strony ---
st.title("💡 Najprostszy Magazyn Streamlit")
st.markdown("**(Ostrzeżenie: Dane nie są trwałe i znikają po każdej interakcji!)**")

# --- Sekcja Dodawania Towaru ---
st.header("➕ Dodaj Towar (Tylko Wyświetlanie)")
col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    nowa_nazwa = st.text_input("Nazwa Towaru", key="simple_input_nazwa")
with col2:
    nowa_ilosc = st.number_input("Ilość", min_value=1, step=1, value=1, key="simple_input_ilosc")
with col3:
    st.write(" ")
    # Przycisk dodawania
    if st.button("Dodaj do Listy", use_container_width=True):
        if nowa_nazwa and nowa_ilosc > 0:
            # W tym miejscu towar zostałby dodany do listy 'magazyn_items'
            # ale ponieważ skrypt zaraz się zrestartuje, to dodanie jest chwilowe.
            magazyn_items.append({"nazwa": nowa_nazwa, "ilosc": nowa_ilosc})
            st.success(f"Dodano: {nowa_nazwa}. Sprawdź listę poniżej (będzie zawierać dodany element TYLKO w tym przebiegu skryptu).")
        else:
            st.error("Wprowadź poprawne dane.")


# --- Sekcja Wyświetlania ---
st.header("📋 Aktualny Stan Listy")

if not magazyn_items:
    st.info("Lista jest pusta.")
else:
    # Wyświetlanie listy jako tabeli
    st.table(magazyn_items)

    # --- Sekcja Usuwania ---
    st.header("➖ Usuń Towar (Tylko Wyświetlanie)")
    
    # Tworzenie listy opcji do usunięcia
    opcje_usuwania = [f"{i+1}. {item['nazwa']} (Ilość: {item['ilosc']})" for i, item in enumerate(magazyn_items)]
    
    wybor_indeksu = st.selectbox(
        "Wybierz towar do usunięcia",
        options=list(range(len(magazyn_items))),
        format_func=lambda x: opcje_usuwania[x]
    )
    
    if st.button("Usuń Wybrany Towar"):
        # W tym miejscu towar zostałby usunięty z listy 'magazyn_items'
        # ale ponieważ skrypt zaraz się zrestartuje, to usunięcie jest chwilowe.
        usuniety = magazyn_items.pop(wybor_indeksu)
        st.warning(f"Usunięto: {usuniety['nazwa']}. Sprawdź listę poniżej (będzie pusta po interakcji).")
