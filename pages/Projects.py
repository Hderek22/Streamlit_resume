"""Projects page shown when the user enters the application"""
import streamlit as st


# Used to write the page in the app.py file
st.title("Projects")
st.markdown(
    """
Check out more on [**GitHub**](https://github.com/hderek22)

**Retail Operations Management Suite (2026)**
- Design, build, ship and maintain retail management tools for in-store operators, including native iPhone and Android apps
- Own the tools end-to-end, from initial build through ongoing releases and maintenance in production

**HERMES – Multi-Agent Assistant (2026)**
- Built a multi-agent assistant from scratch without relying on existing agent frameworks, as a hands-on learning project
- Added a web interface on top of the core agent system for interacting with it outside the command line

**GemGrooves – Music Platform (2026)**
- Built a music platform that uses blockchain technology under the hood, designed so the underlying tech stays invisible and the experience feels seamless to listeners and artists
- Built out the Studio flow, including minting functionality

**Machine Learning Crypto Trading Algorithm/Bot (2022) [(Code)](https://github.com/Hderek22/machine_learning_crypto_algo.git)**
- Built a logistic regression model using Sklearn
- Connected to Alpaca Finance API's with trading signals based on market movement

**Blockchain Payment Processing Tool (2022) [(Code)](https://github.com/Hderek22/blockchain_payment_processing_tool.git)**
- Created a blockchain currency and built a Streamlit app for making payments with the new currency

**Crowdsale KaseiCoin (2022) [(Code)](https://github.com/Hderek22/CrowdsaleKaseiCoin.git)**
- Created an ERC20 token - KaseiCoin
- Coded crowdsale for the ERC20 token

""",
    unsafe_allow_html=True,
)
