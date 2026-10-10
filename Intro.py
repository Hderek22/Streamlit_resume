### Main page for streamlit resume
import streamlit as st

st.set_page_config()


def main():
    """Main function of App"""
    st.title("Hire Me")
    st.info(
        """
        If you are looking to hire an Operations and Inventory Control leader
        who builds his own software and data tools,
        [email me](mailto:hderek22@gmail.com) or reach out
        to me on [LinkedIn](https://www.linkedin.com/in/hderek22)\n
        I build the tools that cut loss and make operations run tighter.
"""
    )
    st.title("Additional Info")
    st.info(
        "This is an interactive Streamlit app built with Python's **streamlit** library. "
        "Do reach out to me on [LinkedIn](https://www.linkedin.com/in/hderek22) or "
        "at [mail me](mailto:hderek22@gmail.com) to know more. "
        "Also check the [source code](https://github.com/Hderek22/Streamlit_resume.git) here. "
    )


if __name__ == "__main__":
    main()
