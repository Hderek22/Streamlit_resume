"""Home page: hero, impact metrics, summary, and background."""
import content as c
import ui

ui.html(f"""
<div class="hero">
<div>
<div class="status"><span class="dot"></span>open to remote roles · {c.LOCATION.split(' · ')[0]}</div>
<h1>{c.NAME}</h1>
<p class="role grad">{c.HEADLINE}</p>
<p class="tag">&gt; {c.TAGLINE}</p>
{ui.contact_buttons()}
</div>
<div class="photo"><img src="{ui.image_data_uri('resources/images/me.jpg')}" alt="{c.NAME}"></div>
</div>
""")

ui.html('<div class="grid k4">' + "".join(f"""
<div class="card metric">
<div class="v grad">{value}</div>
<div class="l">{label}</div>
<div class="c">{context}</div>
</div>""" for value, label, context in c.METRICS) + "</div>")

ui.section("01", "Summary")
ui.html(f'<div class="card"><p class="summary" style="margin:0">{c.SUMMARY}</p></div>')

ui.section("02", "Beyond the resume")
story = "".join(f"<p>{line}</p>" for line in c.STORY)
ui.html(f"""
<div class="card story">
<p class="quote">"{c.QUOTE}"</p>
{story}
<p style="margin:0"><b>I don't dabble.</b> If I set out to accomplish a goal, I'm all in.</p>
</div>
""")

ui.footer()
