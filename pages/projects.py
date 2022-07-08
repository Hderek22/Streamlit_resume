"""Projects page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Career")
    st.markdown(
            """### Earth Fare Organic Markets
            
**Director of Operations 9 years**
- Directly responsible for overall financial performance and operations of region spanning from Charlotte, NC to Fairfax, VA
- Created, implemented and spearheaded multiple projects within region which were adopted throughout entire chain
- Oversaw openings and remodels throughout region while insuring compliance with local governmental policies and procedures.
- Supervised new store opening human resources.
- Job Fairs, training syllabus’s and orientations.

            
### Stanley Rd. QSR - 12 Years
**President & CEO of a Multi-Unit Quiznos Franchise- 14 years**
- Led the startup of a multi-unit franchise business which operated profitably from startup to sale.
- Developed an executed business plan to include financing, commercial leasing, local/corporate operating regulations, recruiting and vendor procurement.
- Planned and executed local store marketing plan that achieved double-digit same store sales growth during every year of operations. 
- Managed payroll, benefits, quality control, customer satisfaction and team building.
- Certified Corporate Trainer designation earned from franchisor assisting in new franchisee initial setup and launch.
- Negotiated and closed the sale of a national franchise unit.



### Projects [(GitHub)](https://github.com/hderek22)

**Machine Learning Crypto Trading Algorithm/Bot[(Code)](https://github.com/Hderek22/machine_learning_crypto_algo.git)**
- Built a logistic regression model using Sklearn
- Connected to Alpaca Finance API's with trading signals based on market movement.

**Blockchain Payment Processing Tool[(Code)](https://github.com/Hderek22/blockchain_payment_processing_tool.git)**
- Coded a blockchain currency and built a Streamlit app for making payments with the new currency.

**Crowdsale KaseiCoin[(Code)](https://github.com/Hderek22/CrowdsaleKaseiCoin.git)**
- Created ab ERC20 token - KasaiCoin
- Coded crowdsale for ERC20 Token

            

""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
