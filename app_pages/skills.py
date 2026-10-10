"""Skills page: skill groups, certifications, and technical coursework."""
import content as c
import ui

ui.page_header(
    "skills",
    'Operator first. <span class="grad">Builder too.</span>',
    "Inventory and shrink know-how from the store floor, backed by the analytics and "
    "software skills to find loss drivers and fix them.",
)

ui.html('<div class="grid k2">' + "".join(f"""
<div class="card skill">
<h3><span class="ico">{group['icon']}</span>{group['title']}</h3>
{ui.chips(group['items'])}
</div>""" for group in c.SKILLS) + "</div>")

ui.section("01", "Certifications")
certs = "".join(f'<div class="cert"><span>{name}</span><span>{when}</span></div>'
                for name, when in c.CERTIFICATIONS)
ui.html(f"""
<div class="grid k2">
<div class="card">{certs}</div>
<div class="card" style="display:flex;gap:1.2rem;align-items:center">
<img src="{ui.image_data_uri('resources/images/badge.png')}" alt="Credential badge"
style="width:110px;height:110px;flex-shrink:0">
<div>
<div style="font-weight:700;margin-bottom:0.3rem">Technical credential</div>
<div style="color:var(--muted);font-size:0.9rem;margin-bottom:0.7rem">
Python, SQL, Amazon Web Services, machine learning in finance, APIs and databases.</div>
<a class="btn" href="{c.CREDENTIAL_URL}" target="_blank">Verify on Credly ↗</a>
</div>
</div>
</div>
""")

ui.section("02", "Technical coursework")
ui.html(f'<div class="card">{ui.chips(c.COURSEWORK, "dim")}</div>')

ui.footer()
