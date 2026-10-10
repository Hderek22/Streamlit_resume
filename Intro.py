### Entry point for the streamlit resume: sets up the theme and top navigation
import streamlit as st

import ui

st.set_page_config(
    page_title="Derek Hall | Retail Inventory Operations",
    page_icon="📦",
    layout="wide",
)


def main():
    """Main function of App"""
    ui.setup()
    nav = st.navigation(
        [
            st.Page("app_pages/home.py", title="Home", default=True),
            st.Page("app_pages/experience.py", title="Experience"),
            st.Page("app_pages/skills.py", title="Skills"),
            st.Page("app_pages/projects.py", title="Projects"),
        ],
        position="top",
    )
    nav.run()


if __name__ == "__main__":
    main()
