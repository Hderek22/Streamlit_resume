"""About page shown when the user enters the application"""
import streamlit as st


# Used to write the about page in the app.py file
st.title("Derek Hall")
"""st.image('resources/images/me.jpg')"""
st.markdown(
    """

"_Focus on the success of your Teammates and amazing things will happen for you!_"

One thing you should know about me is...I don't dabble. It is simply not in my nature. If I set out to accomplish a goal, I'm all in, end of story.

I started bussing tables as a teenager and liked the business...at age 30 I owned 3 restaurants.

I pursued big box retail after selling my business of 14 years...within 3 years I was managing 150M annualy.

I took up running to get healthy and ended up running the NYC marathon twice.

Its safe to say I'm certainly not one to dabble.
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
