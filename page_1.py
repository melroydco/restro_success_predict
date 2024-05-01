import streamlit as st

def main():
    st.title("Page with Two Buttons")

    # Button 1
    if st.button("Button 1"):
        st.write("Button 1 Clicked!")

    # Button 2 positioned at the bottom right corner
    if st.button("Button 2", key="button_2"):
        st.write("Button 2 Clicked!")

    st.markdown(
        """
        <style>
            div[data-testid="stButton_button_2"] > button {
                position: fixed;
                bottom: 10px;
                right: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
