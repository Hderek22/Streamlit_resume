"""Career page shown when the user enters the application"""
import streamlit as st


# Used to write the page in the app.py file
st.title("Career")
st.markdown(
    """### Houchens Food Group

**Total Loss Specialist**
- Lead total loss (shrink) reduction initiatives across stores, analyzing inventory, sales, and shrink data to identify root causes and drive corrective action.
- Partner with store leadership and loss prevention teams to design and implement controls, audits, and training that reduce shrink and improve inventory accuracy.
- Build reporting and analytics tools to track loss trends and measure the impact of loss-prevention initiatives.
- Collaborate cross-functionally on process improvements that protect margin and profitability.

### Earth Fare Organic Markets

**Director of Operations**
- Directly responsible for overall financial performance and operations of a region spanning from Charlotte, NC to Fairfax, VA with an annual revenue of $150M
- Created, implemented and spearheaded multiple projects within the region which were adopted throughout the entire chain
- Oversaw openings and remodels throughout the region while ensuring compliance with local governmental policies and procedures
- Supervised new store opening human resources, including job fairs, training syllabi and orientations

### Stanley Rd. QSR

**President & CEO, Multi-Unit Quiznos Franchise**
- Led the startup of a multi-unit franchise business which operated profitably from startup to sale
- Developed and executed a business plan covering financing, commercial leasing, local/corporate operating regulations, recruiting and vendor procurement
- Planned and executed local store marketing that achieved double-digit same-store sales growth every year of operations
- Managed payroll, benefits, quality control, customer satisfaction and team building
- Earned Certified Corporate Trainer designation from the franchisor, assisting new franchisees with initial setup and launch
- Negotiated and closed the sale of a national franchise unit

""",
    unsafe_allow_html=True,
)
