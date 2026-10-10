"""Shared styling and HTML building blocks for every page."""
import base64
from functools import lru_cache
from html import escape
from pathlib import Path

import streamlit as st

import content as c

ROOT = Path(__file__).parent

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

:root {
  --bg: #07090f;
  --panel: rgba(17, 24, 39, 0.72);
  --panel-solid: #0f1521;
  --line: rgba(148, 163, 184, 0.14);
  --line-hi: rgba(45, 212, 191, 0.45);
  --text: #e6edf6;
  --muted: #8b98ab;
  --accent: #2dd4bf;
  --accent-2: #38bdf8;
  --accent-3: #a78bfa;
  --mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  --sans: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
}

/* ---------- canvas ---------- */
.stApp {
  background:
    radial-gradient(900px 500px at 85% -10%, rgba(56, 189, 248, 0.12), transparent 60%),
    radial-gradient(700px 400px at -10% 20%, rgba(45, 212, 191, 0.10), transparent 60%),
    linear-gradient(rgba(148, 163, 184, 0.045) 1px, transparent 1px) 0 0 / 44px 44px,
    linear-gradient(90deg, rgba(148, 163, 184, 0.045) 1px, transparent 1px) 0 0 / 44px 44px,
    var(--bg);
  color: var(--text);
}
.stApp, [data-testid="stMarkdownContainer"] * { font-family: var(--sans); }
[data-testid="stHeader"] { background: rgba(7, 9, 15, 0.75); backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line); }
[data-testid="stMainBlockContainer"], .block-container { max-width: 1120px; padding-top: 4.5rem; }
#MainMenu, footer, [data-testid="stDecoration"] { visibility: hidden; }
[data-testid="stMarkdownContainer"] a { color: var(--accent); }

/* top nav links */
[data-testid="stTopNavLink"] p {
  font-family: var(--mono) !important; font-size: 0.85rem; letter-spacing: 0.02em; }

/* ---------- type ---------- */
.eyebrow { font-family: var(--mono); font-size: 0.78rem; color: var(--accent);
  letter-spacing: 0.08em; text-transform: lowercase; margin: 0 0 0.6rem; }
.eyebrow::before { content: '// '; color: var(--muted); }
.page-title { font-size: clamp(2rem, 5vw, 3rem); font-weight: 800; line-height: 1.08;
  letter-spacing: -0.03em; margin: 0 0 0.6rem; color: var(--text); }
.page-sub { color: var(--muted); font-size: 1.05rem; max-width: 46rem; margin: 0 0 2rem; line-height: 1.6; }
.grad { background: linear-gradient(90deg, var(--accent), var(--accent-2) 55%, var(--accent-3));
  -webkit-background-clip: text; background-clip: text; color: transparent; }
.section-h { display: flex; align-items: center; gap: 0.9rem; margin: 2.8rem 0 1.2rem; }
.section-h h2 { font-size: 1.35rem; font-weight: 700; margin: 0; padding: 0; color: var(--text);
  letter-spacing: -0.01em; }
.section-h .num { font-family: var(--mono); color: var(--accent); font-size: 0.85rem; }
.section-h .rule { flex: 1; height: 1px; background: linear-gradient(90deg, var(--line), transparent); }

/* ---------- hero ---------- */
.hero { display: grid; grid-template-columns: 1fr 230px; gap: 2.5rem; align-items: center;
  margin-bottom: 2rem; }
.hero h1 { font-size: clamp(2.4rem, 6vw, 3.8rem); font-weight: 800; letter-spacing: -0.04em;
  line-height: 1.02; margin: 0 0 0.8rem; padding: 0; color: var(--text); }
.hero .role { font-size: clamp(1.15rem, 2.4vw, 1.5rem); font-weight: 600; margin: 0 0 0.5rem; }
.hero .tag { font-family: var(--mono); color: var(--muted); font-size: 0.9rem; margin: 0 0 1.4rem; }
.status { display: inline-flex; align-items: center; gap: 0.5rem; font-family: var(--mono);
  font-size: 0.78rem; color: var(--text); border: 1px solid var(--line); background: var(--panel);
  padding: 0.35rem 0.75rem; border-radius: 999px; margin-bottom: 1.4rem; }
.dot { width: 8px; height: 8px; border-radius: 50%; background: #22c55e;
  box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.6); animation: pulse 2s infinite; }
@keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(34,197,94,.55); }
  70% { box-shadow: 0 0 0 8px rgba(34,197,94,0); } 100% { box-shadow: 0 0 0 0 rgba(34,197,94,0); } }
.photo { position: relative; width: 230px; height: 270px; border-radius: 18px; padding: 2px;
  background: linear-gradient(140deg, var(--accent), var(--accent-2) 50%, var(--accent-3)); }
.photo img { width: 100%; height: 100%; object-fit: cover; object-position: 50% 15%;
  border-radius: 16px; display: block; background: var(--panel-solid); }
.photo::after { content: ''; position: absolute; inset: -18px; z-index: -1; border-radius: 30px;
  background: radial-gradient(closest-side, rgba(45, 212, 191, 0.28), transparent); }

/* ---------- buttons ---------- */
.btns { display: flex; flex-wrap: wrap; gap: 0.6rem; }
.btn { display: inline-flex; align-items: center; gap: 0.45rem; text-decoration: none !important;
  font-family: var(--mono); font-size: 0.85rem; font-weight: 500; padding: 0.6rem 1rem;
  border-radius: 10px; border: 1px solid var(--line); color: var(--text) !important;
  background: var(--panel); transition: all 0.18s ease; }
.btn:hover { border-color: var(--line-hi); transform: translateY(-1px);
  box-shadow: 0 6px 24px -10px rgba(45, 212, 191, 0.6); }
.btn.primary { background: linear-gradient(90deg, var(--accent), var(--accent-2));
  color: #04111a !important; border-color: transparent; font-weight: 700; }

/* ---------- cards ---------- */
.card { background: var(--panel); border: 1px solid var(--line); border-radius: 16px;
  padding: 1.4rem 1.5rem; backdrop-filter: blur(6px); transition: border-color .2s, transform .2s; }
.card:hover { border-color: var(--line-hi); }
.grid { display: grid; gap: 1rem; }
.grid.k4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.grid.k3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid.k2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }

.metric .v { font-size: clamp(1.9rem, 3.6vw, 2.4rem); font-weight: 800; letter-spacing: -0.03em;
  line-height: 1; margin-bottom: 0.55rem; }
.metric .l { font-weight: 600; font-size: 0.95rem; color: var(--text); }
.metric .c { font-family: var(--mono); font-size: 0.72rem; color: var(--muted); margin-top: 0.3rem; }
.metric { position: relative; overflow: hidden; }
.metric::before { content: ''; position: absolute; left: 0; top: 0; height: 2px; width: 100%;
  background: linear-gradient(90deg, var(--accent), transparent); }

.summary { font-size: 1.08rem; line-height: 1.75; color: #c9d3e0; }
.quote { font-size: 1.05rem; font-style: italic; color: var(--text); border-left: 2px solid var(--accent);
  padding-left: 1rem; margin: 0 0 1rem; }
.story p { color: #c9d3e0; line-height: 1.65; margin: 0 0 0.7rem; }

.chips { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.chip { font-family: var(--mono); font-size: 0.74rem; padding: 0.28rem 0.6rem; border-radius: 6px;
  color: #b8f5ea; background: rgba(45, 212, 191, 0.08); border: 1px solid rgba(45, 212, 191, 0.22); }
.chip.alt { color: #cfe7ff; background: rgba(56, 189, 248, 0.08); border-color: rgba(56, 189, 248, 0.22); }
.chip.dim { color: var(--muted); background: transparent; border-color: var(--line); }

/* ---------- timeline ---------- */
.timeline { position: relative; padding-left: 1.8rem; }
.timeline::before { content: ''; position: absolute; left: 6px; top: 8px; bottom: 8px; width: 2px;
  background: linear-gradient(var(--accent), var(--accent-2) 40%, var(--line)); }
.job { position: relative; margin-bottom: 1.1rem; }
.job::before { content: ''; position: absolute; left: calc(-1.8rem + 1px); top: 1.65rem; width: 12px;
  height: 12px; border-radius: 50%; background: var(--bg); border: 2px solid var(--accent); }
.job.current::before { background: var(--accent); box-shadow: 0 0 14px var(--accent); }
.job-top { display: flex; justify-content: space-between; align-items: baseline; gap: 1rem;
  flex-wrap: wrap; margin-bottom: 0.25rem; }
.job h3 { font-size: 1.15rem; font-weight: 700; margin: 0; padding: 0; color: var(--text); }
.job .dates { font-family: var(--mono); font-size: 0.78rem; color: var(--accent); white-space: nowrap; }
.job .co { color: var(--muted); font-size: 0.92rem; margin-bottom: 0.8rem; }
.job .co b { color: #c9d3e0; font-weight: 600; }
.job ul { margin: 0 0 0.9rem; padding-left: 1.1rem; }
.job li { color: #c9d3e0; line-height: 1.6; margin-bottom: 0.35rem; font-size: 0.95rem; }
.job li::marker { color: var(--accent); }
.badge-now { font-family: var(--mono); font-size: 0.68rem; color: #04111a; background: var(--accent);
  border-radius: 4px; padding: 0.1rem 0.4rem; margin-left: 0.5rem; vertical-align: middle; }

/* ---------- skills / projects ---------- */
.skill h3, .proj h3 { font-size: 1.05rem; font-weight: 700; margin: 0 0 0.9rem; padding: 0; color: var(--text); }
.skill .ico { font-size: 1.3rem; margin-right: 0.45rem; }
.proj { display: flex; flex-direction: column; height: 100%; }
.proj .meta { display: flex; justify-content: space-between; font-family: var(--mono);
  font-size: 0.74rem; color: var(--muted); margin-bottom: 0.8rem; }
.proj .meta span, .chip, .dates, .y, .eyebrow, .tag, .btn { font-family: var(--mono) !important; }
.proj .meta .live { color: #4ade80; }
.proj .meta .live::before { content: '● '; }
.proj p { color: #c9d3e0; line-height: 1.6; font-size: 0.94rem; margin: 0 0 1rem; flex: 1; }
.proj a.more { font-family: var(--mono); font-size: 0.8rem; text-decoration: none; margin-top: 0.8rem; }
.row { display: flex; justify-content: space-between; align-items: baseline; gap: 1rem;
  padding: 0.85rem 0; border-bottom: 1px dashed var(--line); }
.row:last-child { border-bottom: 0; }
.row .n { font-weight: 600; color: var(--text); }
.row .d { color: var(--muted); font-size: 0.9rem; margin-top: 0.2rem; }
.row .y { font-family: var(--mono); font-size: 0.75rem; color: var(--muted); white-space: nowrap; }
.row a { font-family: var(--mono); font-size: 0.78rem; text-decoration: none; white-space: nowrap; }
.cert { display: flex; justify-content: space-between; gap: 1rem; padding: 0.6rem 0;
  border-bottom: 1px dashed var(--line); }
.cert:last-child { border-bottom: 0; }
.cert span:last-child { font-family: var(--mono); font-size: 0.75rem; color: var(--muted); }

.cta { text-align: center; padding: 2.2rem 1.5rem; margin-top: 3rem;
  background: linear-gradient(135deg, rgba(45,212,191,0.10), rgba(56,189,248,0.06) 50%, rgba(167,139,250,0.08)); }
.cta h2 { font-size: 1.6rem; font-weight: 800; margin: 0 0 0.5rem; padding: 0; color: var(--text); letter-spacing: -0.02em; }
.cta p { color: var(--muted); margin: 0 0 1.3rem; }
.cta .btns { justify-content: center; }
.foot { text-align: center; font-family: var(--mono); font-size: 0.72rem; color: var(--muted);
  margin: 2.5rem 0 1rem; }
.foot a { color: var(--muted) !important; }

/* ---------- responsive ---------- */
@media (max-width: 900px) {
  .grid.k4 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .grid.k3 { grid-template-columns: 1fr; }
}
@media (max-width: 640px) {
  .hero { grid-template-columns: 1fr; gap: 1.5rem; }
  .photo { width: 150px; height: 175px; order: -1; }
  .grid.k2 { grid-template-columns: 1fr; }
  .grid.k4 { gap: 0.7rem; }
  .card { padding: 1.1rem 1.15rem; }
  .row { flex-direction: column; gap: 0.3rem; }
}
</style>
"""


def html(markup: str) -> None:
    """Render raw HTML. Indents and blank lines are dropped so Markdown never breaks it up,
    and "$" is encoded so dollar amounts are not read as LaTeX math."""
    lines = (line.strip() for line in markup.splitlines())
    body = "\n".join(line for line in lines if line).replace("$", "&#36;")
    st.markdown(body, unsafe_allow_html=True)


def setup() -> None:
    html(CSS)


@lru_cache
def image_data_uri(rel_path: str) -> str:
    path = ROOT / rel_path
    mime = "image/png" if path.suffix == ".png" else "image/jpeg"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def chips(items, kind: str = "") -> str:
    return '<div class="chips">' + "".join(
        f'<span class="chip {kind}">{escape(i)}</span>' for i in items) + "</div>"


def page_header(eyebrow: str, title: str, sub: str = "") -> None:
    html(f"""
<p class="eyebrow">{eyebrow}</p>
<h1 class="page-title">{title}</h1>
{f'<p class="page-sub">{sub}</p>' if sub else ''}
""")


def section(num: str, title: str) -> None:
    html(f'<div class="section-h"><span class="num">{num}</span><h2>{title}</h2>'
         '<span class="rule"></span></div>')


def contact_buttons() -> str:
    return f"""
<div class="btns">
<a class="btn primary" href="mailto:{c.EMAIL}">✉ Email me</a>
<a class="btn" href="{c.LINKEDIN}" target="_blank">in&nbsp; LinkedIn</a>
<a class="btn" href="{c.GITHUB}" target="_blank">&lt;/&gt; GitHub</a>
</div>"""


def footer() -> None:
    html(f"""
<div class="card cta">
<h2>Let's get your inventory right.</h2>
<p>Open to remote Retail Inventory Operations roles.</p>
{contact_buttons()}
</div>
<p class="foot">built with python + streamlit · <a href="{c.SOURCE}" target="_blank">view source</a></p>
""")
