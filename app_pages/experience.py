"""Experience page: career timeline, newest first."""
import content as c
import ui

ui.page_header(
    "experience",
    'Store floor to <span class="grad">regional ops</span>',
    "30 years in grocery and multi-unit retail. Now pairing that operating experience "
    "with software and data to cut shrink and inventory.",
)


def job_card(job: dict) -> str:
    place = f" · {job['place']}" if job["place"] else ""
    now = '<span class="badge-now">NOW</span>' if job.get("current") else ""
    bullets = "".join(f"<li>{b}</li>" for b in job["bullets"])
    return f"""
<div class="job{' current' if job.get('current') else ''}">
<div class="card">
<div class="job-top"><h3>{job['role']}{now}</h3><span class="dates">{job['dates']}</span></div>
<div class="co"><b>{job['company']}</b>{place}</div>
<ul>{bullets}</ul>
{ui.chips(job['tags'], 'alt')}
</div>
</div>"""


ui.html('<div class="timeline">' + "".join(job_card(j) for j in c.EXPERIENCE) + "</div>")

ui.footer()
