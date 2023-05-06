"""About page shown when the user enters the application"""
import streamlit as st


# Used to write the about page in the app.py file
st.title("Derek Hall")
st.image("resources/images/me.jpg")
st.markdown(
    """

"_Focus on the success of your Teammates and amazing things will happen for you!_"

## Experiences

**Business Development | Leadership | Team Building | Finance**

## Skills

**Python | Solidity | Machine Learning | API's | SQL | AWS**

[**LinkedIn**](https://www.linkedin.com/in/hderek22) | [**Email**](mailto:Hderek22@gmail.com)

## My Goals

**Join a team with likeminded 'can do' teammates and build a 4 star business!**

-----

*Built with [**Streamlit**](https://www.streamlit.io/)*

*Check out my [**GitHub**](https://github.com/Hderek22/Streamlit_resume.git) for the implementation details of this page.* 




""",
    unsafe_allow_html=True,
)
