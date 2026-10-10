"""Career page shown when the user enters the application"""
import streamlit as st


# Used to write the page in the app.py file
st.title("Career")
st.markdown(
    """### Houchens Food Group

**Total Loss Specialist (Dec 2025 – Present)**
- Own inventory loss and markdown reduction for about 30 retail units across KY, IN, IL, and OH, partnering with store leadership on controls, audits, and training.
- Designed, built, and maintain native iPhone and Android tools for in-store operators; they contributed to $1M+ in shrink reduction and a $3M inventory decrease in four months.
- Build weekly reporting on ground beef markdown, grind production, and grocery inventory days-on-hand to find loss drivers by store and day of week.

### The Fresh Market

**Store Manager, Winston-Salem, NC (Dec 2021 – Dec 2025)**
- Led a team of 45 employees.
- Decreased hourly payroll 3% by streamlining processes.
- Improved shrink performance.

### Earth Fare Organic Markets

**Director of Operations (Mar 2012 – Dec 2021)**
- Ran financial performance and operations for a 12-store, $150M region from Charlotte, NC to Fairfax, VA.
- Created the truck-to-shelf initiative, which cut region inventory by $1.2M and reduced total shrink by 0.4%.
- Delivered positive comp growth while the company average declined; the only region with positive comps in every unit for an entire period.
- Created programs adopted chain-wide: POG Integrity Sweep, Operation In Stock Condition Blitz, and Shrink Action Plan Protocols.
- Oversaw openings and remodels, new-store hiring, and training.

### Stanley Rd. QSR

**President & CEO, Multi-Unit Quiznos Franchise (Feb 1998 – Oct 2012)**
- Led a multi-unit franchise that was profitable from startup to sale, with double-digit same-store sales growth every year.
- Earned the Certified Corporate Trainer designation from the franchisor and negotiated the sale of a franchise unit.

""",
    unsafe_allow_html=True,
)
