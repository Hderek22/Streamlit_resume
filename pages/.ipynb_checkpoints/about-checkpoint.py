"""About page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the about page in the app.py file"""
    st.title("My name is Derek Hall")
    st.markdown(
            """## Who Am I?
"_Focus on the success of your Teammates and your life will change_"

One thing you should know about me is...I don't dabble. Its simply not in my nature. If I set out to accomplish a goal, I'm all in, end of story.

I started bussing tables as a teenager and liked the business...at age 30 I owned 3 restaurants.

I joined retail after selling my business of 14 years...within 3 years I was managing 150M annualy.

I took up running to get healthy and relieve stress...ended up running the NY marathon twice.

Its safe to say I'm certainly not one to dabble.

------

de·ci·sion
/dəˈsiZHən/

I like to think of a decision being the opposite of an 'incision'. instead of cutting in...you are cutting off. Cutting off any other option and deciding on one outcome.

## Experiences

**Business Development | Leadership | Team Building**
 
## Skills

**Python | Solidity | Machine Learning | API's | SQL | AWS**

[**LinkedIn**](https://www.linkedin.com/in/hderek22) | [**Email**](mailto:Hderek22@gmail.com)

## My Goals

-----

Check out my [**GitHub**](https://github.com/Hderek22/Streamlit_resume.git) for the implementation. Reach out to me for any project or a simple discussion on Streamlit.
Built Streamlit [**page**](https://www.streamlit.io/) for more more information and updates.


""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
