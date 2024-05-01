import streamlit as st
from main import main
from page_2 import page2
from page3 import page3
# from page4 import page4

def main_app():
    # Get the current page from the query parameters
    page = st.experimental_get_query_params().get("page", ["main"])[0]

    # Show content based on the current page
    if page == "main":
        main()

    elif page == "page2":
        page2()

    elif page == "page3":
        page3()



if __name__ == "__main__":
    main_app()
