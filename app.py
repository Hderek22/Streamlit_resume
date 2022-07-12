### Main page for streamlit resume
import streamlit as st
import pages.about
import pages.projects
import pages.edu
import pages.career
import resources.ast as ast

st.set_page_config()

PAGES = {
    "About": pages.about,  
    "Tech Skills": pages.edu,
    "Career" : pages.career,
    "Projects" : pages.projects
}

def main():
    """Main function of App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)

    st.sidebar.title("Hire Me")
    st.sidebar.info(
        """
        If you are looking to hire a Business Development Expert with tech skills, 
        [email me](mailto:Hderek22@icloud.com) or reach out 
        to me on [LinkedIn](https://www.linkedin.com/in/hderek22)\n
        I will help your business grow!
""")
    st.sidebar.title("Additional Info")
    st.sidebar.info(
        "This an interactive streamlit app completely created with Python's latest library **streamlit** "
        "Do reach out to me on [LinkedIn](https://www.linkedin.com/in/hderek22) or "
        "at [Mail me](mailto:hderek22@icloud.com) to know more. "
        "Also check the [source code](https://github.com/Hderek22/Streamlit_resume.git) here. "  

)

if __name__ == "__main__":
    main()
