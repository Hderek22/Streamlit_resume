"""All resume copy for the app lives here, so pages only handle layout."""

NAME = "Derek Hall"
HEADLINE = "Retail Inventory Operations Leader"
TAGLINE = "Shrink Reduction · In-Store Technology · Analytics"
LOCATION = "Henderson, KY · Open to remote"
EMAIL = "hderek22@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/hderek22"
GITHUB = "https://github.com/hderek22"
SOURCE = "https://github.com/Hderek22/Streamlit_resume"

SUMMARY = (
    "Retail inventory and operations leader with 30 years in grocery and multi-unit retail. "
    "Cut regional shrink 0.4% and inventory $1.2M with a truck-to-shelf initiative, then built "
    "native iPhone and Android tools that helped reduce inventory $3M in four months and "
    "contributed to $1M+ in shrink reduction across ~30 units. Pairs store-level operating "
    "experience and financial discipline with hands-on Python, SQL, and Excel analytics, and "
    "trains store teams to execute new processes and technology."
)

# value, label, context
METRICS = [
    ("$3M", "Inventory decrease", "in four months, Houchens"),
    ("$1M+", "Shrink reduction", "store tools contributed"),
    ("$1.2M", "Regional inventory cut", "truck-to-shelf, Earth Fare"),
    ("30 yrs", "Grocery & multi-unit retail", "store floor to region"),
]

STORY = [
    "I started bussing tables as a teenager and liked the business. At 30 I owned 3 restaurants.",
    "After selling my business of 14 years I moved into big box retail, and within a few years "
    "I was running a $150M region.",
    "I took up running to get healthy and ended up running the NYC Marathon twice.",
]
QUOTE = "Focus on the success of your teammates and amazing things will happen for you."

EXPERIENCE = [
    {
        "role": "Total Loss Specialist",
        "company": "Houchens Food Group",
        "place": "KY, IN, IL, OH",
        "dates": "Dec 2025 – Present",
        "current": True,
        "bullets": [
            "Own inventory loss and markdown reduction for ~30 retail units across four states, "
            "partnering with store leadership on controls, audits, and training.",
            "Designed, built, shipped, and maintain native iPhone and Android tools for in-store "
            "operators; they contributed to $1M+ in shrink reduction and a $3M inventory decrease "
            "in four months.",
            "Build weekly reporting on ground beef markdown, grind production, and grocery "
            "inventory days-on-hand to find loss drivers by store and day of week.",
        ],
        "tags": ["~30 units", "$1M+ shrink", "$3M inventory", "iOS + Android"],
    },
    {
        "role": "Store Manager",
        "company": "The Fresh Market",
        "place": "Winston-Salem, NC",
        "dates": "Dec 2021 – Dec 2025",
        "bullets": [
            "Led a team of 45 employees.",
            "Decreased hourly payroll 3% by streamlining processes.",
            "Improved shrink performance.",
        ],
        "tags": ["45-person team", "-3% payroll"],
    },
    {
        "role": "Director of Operations",
        "company": "Earth Fare, Inc.",
        "place": "Asheville, NC",
        "dates": "Mar 2012 – Dec 2021",
        "bullets": [
            "Ran financial performance and operations for a 12-store, $150M region spanning "
            "Charlotte, NC to Fairfax, VA.",
            "Created the truck-to-shelf initiative, which cut region inventory by $1.2M and "
            "reduced total shrink by 0.4%.",
            "Delivered positive comp growth across the region while the company average declined; "
            "the only region with positive comps in every unit for an entire period.",
            "Created region programs adopted chain-wide: POG Integrity Sweep, Operation In Stock "
            "Condition Blitz, and Shrink Action Plan Protocols.",
            "Oversaw store openings and remodels, including permit compliance, new-store hiring, "
            "job fairs, and training syllabi.",
        ],
        "tags": ["12 stores", "$150M region", "-$1.2M inventory", "-0.4% shrink"],
    },
    {
        "role": "Owner/Operator, Multi-Unit Franchise",
        "company": "Quiznos",
        "place": "Greensboro, NC",
        "dates": "Feb 1998 – Oct 2012",
        "bullets": [
            "Launched a multi-unit franchise that was profitable from startup; built the "
            "financing, leasing, hiring, and vendor plan.",
            "Grew same-store sales by double digits every year of operation.",
            "Earned Certified Corporate Trainer designation and trained new franchisees; "
            "negotiated the sale of a franchise unit.",
        ],
        "tags": ["Profitable from startup", "Double-digit comps"],
    },
    {
        "role": "Market Training Manager / Multi-Unit Manager",
        "company": "Taco Bell Corporation",
        "place": "",
        "dates": "Feb 2004 – Feb 2006",
        "bullets": [
            "Trained 250+ employees across a region and led rollout of new products and procedures.",
            "Ran three units with $2.2M combined annual sales; improved profitability, retention, "
            "and sales growth.",
        ],
        "tags": ["250+ trained", "$2.2M sales"],
    },
]

SKILLS = [
    {
        "icon": "📦",
        "title": "Inventory operations",
        "items": ["Inventory accuracy", "Shrink & markdown reduction", "Truck-to-shelf",
                  "Receiving flow", "Store audits & controls", "Cycle counts",
                  "Physical inventory"],
    },
    {
        "icon": "📊",
        "title": "Analytics",
        "items": ["Advanced Excel (pivot tables)", "SQL", "Python", "pandas", "NumPy",
                  "Matplotlib", "Tableau", "QlikView", "Periscope", "KPI & trend reporting"],
    },
    {
        "icon": "📱",
        "title": "In-store technology",
        "items": ["Native iPhone apps", "Native Android apps", "Process & tech rollouts",
                  "GitHub"],
    },
    {
        "icon": "💵",
        "title": "Financial acumen",
        "items": ["P&L management", "Payroll & workforce management", "Budgeting",
                  "Cost control", "Financial analysis"],
    },
    {
        "icon": "🧭",
        "title": "Leadership",
        "items": ["Team coaching", "Training & orientation",
                  "Cross-functional influence: store leadership, loss prevention, finance"],
    },
]

CERTIFICATIONS = [
    ("Forklift Certified Trainer", "May 2020 – Present"),
    ("ServSafe Certified", ""),
    ("Food Handler Certification", ""),
    ("High school diploma", ""),
]
CREDENTIAL_URL = (
    "https://www.credly.com/badges/0e89d302-0f91-4ec7-8589-f60f857bf798"
    "?source=linked_in_profile"
)
COURSEWORK = ["Python", "SQL", "Amazon Web Services", "Machine learning in finance",
              "APIs & databases", "pandas", "NumPy", "Matplotlib", "Natural language processing",
              "Algorithmic trading", "Solidity", "Blockchain & cryptocurrency",
              "Financial fundamentals"]

PROJECTS = [
    {
        "name": "Retail Operations Management Suite",
        "year": "2026",
        "status": "In production",
        "desc": "Native iPhone and Android tools for in-store operators, owned end to end from "
                "first build through production releases and maintenance. Built to help store "
                "teams improve inventory accuracy and cut shrink.",
        "stack": ["iOS", "Android", "Store operations"],
        "link": None,
    },
    {
        "name": "HERMES Multi-Agent Assistant",
        "year": "2026",
        "status": "Active",
        "desc": "A multi-agent assistant built from scratch without agent frameworks, with a "
                "web interface on top of the core agent system.",
        "stack": ["Python", "Multi-agent AI", "Web UI"],
        "link": GITHUB,
    },
    {
        "name": "Interactive Resume",
        "year": "2026",
        "status": "Live",
        "desc": "This site. A multipage Streamlit app in Python with a custom theme and "
                "data-driven pages.",
        "stack": ["Python", "Streamlit", "CSS"],
        "link": SOURCE,
    },
]

EARLIER_PROJECTS = [
    {
        "name": "GemGrooves Music Platform",
        "year": "2026",
        "desc": "Music platform with blockchain under the hood, designed so the tech stays "
                "invisible to listeners and artists. Built the Studio flow, including minting.",
        "link": None,
    },
    {
        "name": "ML Crypto Trading Bot",
        "year": "2022",
        "desc": "Logistic regression model in scikit-learn, wired to the Alpaca API with "
                "trading signals based on market movement.",
        "link": "https://github.com/Hderek22/machine_learning_crypto_algo.git",
    },
    {
        "name": "Blockchain Payment Processing Tool",
        "year": "2022",
        "desc": "Created a blockchain currency and a Streamlit app for making payments with it.",
        "link": "https://github.com/Hderek22/blockchain_payment_processing_tool.git",
    },
    {
        "name": "Crowdsale KaseiCoin",
        "year": "2022",
        "desc": "ERC20 token with a coded crowdsale contract.",
        "link": "https://github.com/Hderek22/CrowdsaleKaseiCoin.git",
    },
]
