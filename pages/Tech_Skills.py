"""Edu page shown when the user enters the application"""
import streamlit as st

# Used to write the page in the app.py file
st.title("Tech Skills")
st.image("resources/images/badge.png", width=250)
st.markdown(
    """
**[**Credential**](https://www.credly.com/badges/0e89d302-0f91-4ec7-8589-f60f857bf798?source=linked_in_profile)**\n

**Courses Completed** \n
- Python \n
- Solidity \n
- Blockchain and Cryptocurrency \n
- SQL \n
- Amazon Web Services \n
- Algorithmic Trading \n
- Financial Fundamentals \n
- Machine Learning Applications in Finance \n
- Api's & Databases \n
- Matplotlib \n
- Natural Language Processing \n
- Numpy \n
- Pandas \n
""",
    unsafe_allow_html=True,
)
