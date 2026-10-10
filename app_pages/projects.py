"""Projects page: featured builds and earlier work."""
import content as c
import ui

ui.page_header(
    "projects",
    'Tools I <span class="grad">build and ship</span>',
    "Software I design and maintain myself, starting with the store tools used by operators "
    "every day.",
)


def project_card(p: dict) -> str:
    link = (f'<a class="more" href="{p["link"]}" target="_blank">view code ↗</a>'
            if p["link"] else "")
    return f"""
<div class="card proj">
<div class="meta"><span class="live">{p['status']}</span><span>{p['year']}</span></div>
<h3>{p['name']}</h3>
<p>{p['desc']}</p>
{ui.chips(p['stack'], 'alt')}
{link}
</div>"""


ui.html('<div class="grid k3">' + "".join(project_card(p) for p in c.PROJECTS) + "</div>")

ui.section("01", "Earlier builds")
rows = "".join(f"""
<div class="row">
<div><div class="n">{p['name']}</div><div class="d">{p['desc']}</div></div>
<div style="text-align:right"><div class="y">{p['year']}</div>
{f'<a href="{p["link"]}" target="_blank">code ↗</a>' if p['link'] else ''}</div>
</div>""" for p in c.EARLIER_PROJECTS)
ui.html(f'<div class="card">{rows}</div>')

ui.footer()
