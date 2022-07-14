"""Projects page shown when the user enters the application"""
import streamlit as st


# Used to write the page in the app.py file
st.title("Projects[(GitHub)](https://github.com/hderek22)")
st.markdown(
    """

**Machine Learning Crypto Trading Algorithm/Bot[(Code)](https://github.com/Hderek22/machine_learning_crypto_algo.git)**
- Built a logistic regression model using Sklearn
- Connected to Alpaca Finance API's with trading signals based on market movement.

**Blockchain Payment Processing Tool[(Code)](https://github.com/Hderek22/blockchain_payment_processing_tool.git)**
- Created a blockchain currency and built a Streamlit app for making payments with the new currency.

**Crowdsale KaseiCoin[(Code)](https://github.com/Hderek22/CrowdsaleKaseiCoin.git)**
- Created ab ERC20 token - KasaiCoin
- Coded crowdsale for ERC20 Token

        

""",
    unsafe_allow_html=True,
)
