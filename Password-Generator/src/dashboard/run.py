import streamlit as st
from src.oop_approach.main import PinPassword, RandomPasswordGenerator, RememberablePasswordGenerator

# Create a sidebar
st.sidebar.title("Sidebar Menu")

# Add options to the sidebar menu
selected_option = st.sidebar.radio(
    ":red[Select an option]",
    ("Pin Password", "Random Password", "Rememberable Password")
)

if selected_option == "Pin Password":
    length = st.slider(":blue[select the length of the password]", 4, 16, value=8)
    pass_generator = PinPassword(length=length)

elif selected_option == "Random Password":
    length = st.slider(":blue[select the length of the password]", 8, 16, value=12)
    include_number = st.checkbox("Include number")
    include_symbol = st.checkbox("Include symbol")

    pass_generator = RandomPasswordGenerator(length, include_number, include_symbol)

elif selected_option == "Rememberable Password":
    length = st.slider(":blue[select count of words for the password]", 2, 10, value=4)
    # word_list
    word_list = []
    include_word_list = st.toggle("Include user defined word-list?")
    if include_word_list :
        user_input = st.text_input("Enter a comma-separated list of items:")
        word_list = [item.strip() for item in user_input.split(',')]
    separator = st.text_input("Separator")

    pass_generator = RememberablePasswordGenerator(length, word_list=word_list, separator=separator)


if st.button("Get Password") :
    password = pass_generator.generate_password()
    st.write(f"```{password}```")


