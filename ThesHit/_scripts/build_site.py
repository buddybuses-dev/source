"""Build a single-file offline site (_site/index.html) mirroring the whole ThesHit repo:
every study guide, exam, notes, ship deliverable, plus per-module audio, per-space
audiobooks, community/resources/reference docs, search, and progress tracking.

Run:  python _scripts/build_site.py
Serve: python -m http.server 8080   (from the repo root)  ->  http://localhost:8080/_site/
"""
import os, re, json, sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from md_to_html import convert

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "_site")
SPACES = ["01_the-foundation", "02_the-mastery", "03_the-industry",
          "04_the-vault", "05_the-launchpad", "06_the-frontier"]
PART_FILES = [("Study Guide", "study-guide.md"), ("Notes", "notes.md"),
              ("Exam", "exam.md"), ("Ship Deliverable", "ship-deliverable.md")]

PAGES = {}          # id -> {title, kind, crumb, parts:[{label,html}], audio, audiobook}
NAV = []            # sidebar model
ORDER = []          # flat list of module ids for prev/next


def read(p):
    with open(p, encoding="utf-8-sig") as f:
        return f.read()


def url_for(abs_path):
    rel = os.path.relpath(abs_path, ROOT).replace(os.sep, "/")
    return "/" + quote(rel)


def pid(abs_path):
    rel = os.path.relpath(abs_path, ROOT).replace(os.sep, "/")
    return re.sub(r'[^a-z0-9]+', '-', rel.lower()).strip('-')


def space_title(folder):
    return re.sub(r'^\d+_', '', folder).replace('-', ' ').title()


def group_title(folder):
    m = re.match(r'(layer|course|vertical)-(\d+)_(.+)', folder)
    if m:
        return f"{m.group(1).title()} {int(m.group(2))} · {m.group(3).replace('-', ' ').title()}"
    return re.sub(r'^\d+[_-]', '', folder).replace('-', ' ').replace('_', ' ').title()


def first_h1(md, fallback):
    for ln in md.splitlines():
        m = re.match(r'^#\s+(.*)', ln.strip())
        if m:
            return m.group(1).strip()
    return fallback


def is_module(d):
    return os.path.isfile(os.path.join(d, "study-guide.md"))


def add_module(moddir, crumb):
    sg = read(os.path.join(moddir, "study-guide.md"))
    title = first_h1(sg, group_title(os.path.basename(moddir)))
    parts = []
    for label, fn in PART_FILES:
        p = os.path.join(moddir, fn)
        if os.path.isfile(p):
            parts.append({"label": label, "html": convert(read(p))})
    mp3 = os.path.join(moddir, "study-guide.mp3")
    _id = pid(moddir)
    PAGES[_id] = {"title": title, "kind": "module", "crumb": crumb, "parts": parts,
                  "audio": url_for(mp3) if os.path.isfile(mp3) else None, "audiobook": None}
    ORDER.append(_id)
    return {"id": _id, "title": title}


def add_doc(mdfile, crumb, title=None):
    md = read(mdfile)
    t = title or first_h1(md, os.path.splitext(os.path.basename(mdfile))[0].replace('-', ' ').title())
    _id = pid(mdfile)
    PAGES[_id] = {"title": t, "kind": "doc", "crumb": crumb,
                  "parts": [{"label": "", "html": convert(md)}], "audio": None, "audiobook": None}
    return {"id": _id, "title": t}


def space_audiobook(space_dir):
    ad = os.path.join(ROOT, space_dir, "_audio")
    if os.path.isdir(ad):
        for f in sorted(os.listdir(ad)):
            if f.lower().endswith(".mp3"):
                return url_for(os.path.join(ad, f))
    return None


def build():
    # --- Start Here ---
    sh = os.path.join(ROOT, "00_start-here")
    if os.path.isdir(sh):
        items = [add_doc(os.path.join(sh, f), "Start Here")
                 for f in sorted(os.listdir(sh)) if f.endswith(".md")]
        NAV.append({"title": "Start Here", "items": items})

    # --- The six spaces ---
    for sp in SPACES:
        spdir = os.path.join(ROOT, sp)
        if not os.path.isdir(spdir):
            continue
        st = space_title(sp)
        book = space_audiobook(sp)
        children = sorted(d for d in os.listdir(spdir)
                          if os.path.isdir(os.path.join(spdir, d)) and not d.startswith("_"))
        sec = {"title": st, "audiobook": book}
        if children and is_module(os.path.join(spdir, children[0])):
            # flat: modules directly under the space (The Foundation)
            sec["items"] = [add_module(os.path.join(spdir, c), st) for c in children]
        else:
            groups = []
            for c in children:
                cdir = os.path.join(spdir, c)
                mods = sorted(d for d in os.listdir(cdir)
                              if is_module(os.path.join(cdir, d)))
                if not mods:
                    continue
                gt = group_title(c)
                groups.append({"title": gt,
                               "items": [add_module(os.path.join(cdir, m), f"{st}  /  {gt}") for m in mods]})
            sec["groups"] = groups
        # attach audiobook id to every module page in this space
        if book:
            NAV_ids = []
            if "items" in sec:
                NAV_ids += [it["id"] for it in sec["items"]]
            for g in sec.get("groups", []):
                NAV_ids += [it["id"] for it in g["items"]]
            for mid in NAV_ids:
                PAGES[mid]["audiobook"] = book
        NAV.append(sec)

    # --- Community ---
    cm = os.path.join(ROOT, "07_community")
    if os.path.isdir(cm):
        items = [add_doc(os.path.join(cm, f), "Community")
                 for f in sorted(os.listdir(cm)) if f.endswith(".md")]
        NAV.append({"title": "Community", "items": items})

    # --- Resources ---
    rs = os.path.join(ROOT, "_resources")
    if os.path.isdir(rs):
        items = []
        for sub in sorted(os.listdir(rs)):
            sd = os.path.join(rs, sub)
            if not os.path.isdir(sd):
                continue
            for fn in sorted(os.listdir(sd)):
                if not fn.endswith(".md"):
                    continue
                p = os.path.join(sd, fn)
                if fn == "README.md":
                    items.append(add_doc(p, "Resources", title=sub.replace('-', ' ').title()))
                else:
                    items.append(add_doc(p, "Resources / " + sub.replace('-', ' ').title()))
        if items:
            NAV.append({"title": "Resources", "items": items})

    # --- Reference docs (top-level) ---
    ref = []
    for fn in ["README.md", "badges.md", "progress-tracker.md"]:
        p = os.path.join(ROOT, fn)
        if os.path.isfile(p):
            ref.append(add_doc(p, "Reference"))
    tmpl = os.path.join(ROOT, "_templates")
    if os.path.isdir(tmpl):
        for fn in sorted(os.listdir(tmpl)):
            if fn.endswith(".md"):
                ref.append(add_doc(os.path.join(tmpl, fn), "Reference / Templates"))
    if ref:
        NAV.append({"title": "Reference", "items": ref})


def write_site():
    os.makedirs(OUT_DIR, exist_ok=True)
    full_audio = os.path.join(ROOT, "_audio_all", "ThesHit__complete-course.mp3")
    payload = {
        "nav": NAV,
        "pages": PAGES,
        "order": ORDER,
        "fullAudio": url_for(full_audio) if os.path.isfile(full_audio) else None,
        "spaceBooks": [{"title": s["title"], "url": s.get("audiobook")} for s in NAV if s.get("audiobook")],
        "moduleCount": len(ORDER),
    }
    data = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    html = HTML_TEMPLATE.replace("/*__DATA__*/", data)
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {os.path.join(OUT_DIR, 'index.html')}  ({len(html)/1024:.0f} KB)")
    print(f"Modules: {len(ORDER)}   Total pages: {len(PAGES)}")


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ThesHit — Offline Course Mirror</title>
<style>
  :root{
    --bg:#faf9f7; --panel:#fff; --ink:#1c1b19; --muted:#6b6863; --line:#e6e3de;
    --accent:#b5471f; --accent-soft:#f4e6df; --ok:#2f7d3a;
  }
  @media (prefers-color-scheme:dark){:root{
    --bg:#17171a; --panel:#1f1f23; --ink:#e9e7e3; --muted:#9b968e; --line:#33323a;
    --accent:#e0794f; --accent-soft:#3a2a22; --ok:#5cc76d;
  }}
  *{box-sizing:border-box}
  html,body{margin:0;height:100%}
  body{background:var(--bg);color:var(--ink);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;display:flex}
  a{color:var(--accent)}
  #sidebar{width:320px;flex:0 0 320px;height:100vh;overflow-y:auto;background:var(--panel);border-right:1px solid var(--line);padding:0 0 40px}
  #sidebar h1{font-size:15px;letter-spacing:.08em;text-transform:uppercase;margin:0;padding:18px 20px 6px;color:var(--muted)}
  #brand{padding:18px 20px 10px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--panel);z-index:2}
  #brand strong{font-size:18px;display:block}
  #brand small{color:var(--muted)}
  #search{width:100%;margin-top:10px;padding:8px 10px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--ink);font-size:14px}
  .sec{margin-top:8px}
  .sec>.sec-t{font-weight:700;padding:12px 20px 6px;font-size:14px;letter-spacing:.02em}
  .grp>.grp-t{color:var(--muted);padding:8px 20px 4px;font-size:12px;text-transform:uppercase;letter-spacing:.06em}
  .navlink{display:flex;gap:8px;align-items:flex-start;padding:6px 20px 6px 24px;cursor:pointer;font-size:14px;color:var(--ink);text-decoration:none}
  .navlink:hover{background:var(--accent-soft)}
  .navlink.active{background:var(--accent-soft);border-left:3px solid var(--accent);padding-left:21px;font-weight:600}
  .navlink .tick{color:var(--ok);flex:0 0 14px;font-weight:700;visibility:hidden}
  .navlink.done .tick{visibility:visible}
  .booklink{display:block;padding:4px 20px 8px 24px;font-size:12px}
  #main{flex:1;height:100vh;overflow-y:auto}
  #wrap{max-width:860px;margin:0 auto;padding:28px 40px 120px}
  #crumb{color:var(--muted);font-size:13px;margin-bottom:4px}
  #ptitle{font-size:30px;line-height:1.2;margin:.1em 0 .5em}
  .audiobar{position:sticky;top:0;background:var(--bg);padding:10px 0 12px;border-bottom:1px solid var(--line);margin-bottom:18px;z-index:1}
  .audiobar audio{width:100%}
  .audiobar .row{display:flex;gap:14px;flex-wrap:wrap;align-items:center;font-size:13px;margin-top:6px}
  .tabs{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0 18px}
  .tab{padding:6px 12px;border:1px solid var(--line);border-radius:999px;cursor:pointer;font-size:13px;background:var(--panel)}
  .tab.active{background:var(--accent);color:#fff;border-color:var(--accent)}
  .content h1{font-size:26px;margin:1.2em 0 .4em}
  .content h2{font-size:21px;margin:1.4em 0 .4em;padding-bottom:.2em;border-bottom:1px solid var(--line)}
  .content h3{font-size:17px;margin:1.2em 0 .3em}
  .content blockquote{margin:1em 0;padding:.4em 1em;border-left:3px solid var(--accent);background:var(--accent-soft);border-radius:0 6px 6px 0}
  .content code{background:var(--accent-soft);padding:.1em .35em;border-radius:4px;font-size:.9em}
  .content pre{background:var(--panel);border:1px solid var(--line);padding:12px;border-radius:8px;overflow-x:auto}
  .content pre code{background:none;padding:0}
  .content hr{border:none;border-top:1px solid var(--line);margin:2em 0}
  .content ul,.content ol{padding-left:1.4em}
  .content li{margin:.25em 0}
  .pager{display:flex;justify-content:space-between;margin-top:40px;gap:12px}
  .pager button{flex:1;padding:12px;border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:10px;cursor:pointer;font-size:13px}
  .pager button:disabled{opacity:.35;cursor:default}
  .donebtn{display:inline-flex;gap:8px;align-items:center;margin:18px 0 0;padding:10px 16px;border-radius:10px;border:1px solid var(--ok);background:transparent;color:var(--ok);cursor:pointer;font-size:14px;font-weight:600}
  .donebtn.on{background:var(--ok);color:#fff}
  #home .card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:18px 20px;margin:14px 0}
  #home audio{width:100%;margin-top:8px}
  .progwrap{background:var(--panel);border:1px solid var(--line);border-radius:999px;height:12px;overflow:hidden;margin:8px 0}
  .progbar{height:100%;background:var(--ok);width:0}
  #menuBtn{display:none}
  @media (max-width:880px){
    body{display:block}
    #sidebar{position:fixed;left:0;top:0;z-index:20;transform:translateX(-100%);transition:transform .2s}
    #sidebar.open{transform:none}
    #menuBtn{display:block;position:fixed;left:12px;top:12px;z-index:30;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:10px 14px;font-size:14px}
    #wrap{padding-top:64px}
  }
</style>
</head>
<body>
<button id="menuBtn">☰ Menu</button>
<nav id="sidebar">
  <div id="brand">
    <strong>ThesHit</strong>
    <small>offline course mirror</small>
    <input id="search" placeholder="Filter modules…" autocomplete="off">
  </div>
  <div id="navtree"></div>
</nav>
<main id="main"><div id="wrap"><div id="page"></div></div></main>

<script>
const D = /*__DATA__*/;
const $ = s => document.querySelector(s);
const nav = $('#navtree'), page = $('#page');
const LS_DONE = 'theshit.done', LS_LAST = 'theshit.last';
let done = new Set(JSON.parse(localStorage.getItem(LS_DONE) || '[]'));

function saveDone(){ localStorage.setItem(LS_DONE, JSON.stringify([...done])); }

function navItem(it){
  const a = document.createElement('a');
  a.className = 'navlink'; a.dataset.id = it.id; a.href = '#' + it.id;
  a.innerHTML = '<span class="tick">✓</span><span>' + it.title + '</span>';
  return a;
}
function buildNav(){
  nav.innerHTML = '';
  const homeA = navItem({id:'home', title:'⌂  Home & audiobooks'});
  homeA.querySelector('.tick').remove();
  nav.appendChild(homeA);
  D.nav.forEach(sec => {
    const box = document.createElement('div'); box.className = 'sec';
    const t = document.createElement('div'); t.className = 'sec-t'; t.textContent = sec.title;
    box.appendChild(t);
    if (sec.audiobook){
      const b = document.createElement('a'); b.className = 'booklink'; b.href = sec.audiobook;
      b.target = '_blank'; b.textContent = '▶ Play ' + sec.title + ' audiobook';
      box.appendChild(b);
    }
    (sec.items || []).forEach(it => box.appendChild(navItem(it)));
    (sec.groups || []).forEach(g => {
      const gb = document.createElement('div'); gb.className = 'grp';
      const gt = document.createElement('div'); gt.className = 'grp-t'; gt.textContent = g.title;
      gb.appendChild(gt);
      g.items.forEach(it => gb.appendChild(navItem(it)));
      box.appendChild(gb);
    });
    nav.appendChild(box);
  });
  refreshTicks();
}
function refreshTicks(){
  document.querySelectorAll('.navlink').forEach(a => {
    a.classList.toggle('done', done.has(a.dataset.id));
    a.classList.toggle('active', a.dataset.id === current);
  });
}

let current = null;
function renderHome(){
  current = 'home'; refreshTicks();
  const pct = Math.round(done.size / D.moduleCount * 100);
  let books = D.spaceBooks.map(b => b.url
    ? `<div class="card"><strong>${b.title}</strong><audio controls preload="none" src="${b.url}"></audio></div>` : '').join('');
  page.innerHTML = `
    <div id="home">
      <div id="crumb">Offline mirror</div>
      <h1 id="ptitle">ThesHit — your full course, offline</h1>
      <p>Every module's study guide, notes, exam, and ship brief — plus narrated audio for all ${D.moduleCount} modules. Progress is saved in this browser.</p>
      <div class="card">
        <strong>Progress</strong>
        <div class="progwrap"><div class="progbar" style="width:${pct}%"></div></div>
        <div>${done.size} / ${D.moduleCount} modules marked complete (${pct}%)</div>
      </div>
      ${D.fullAudio ? `<div class="card"><strong>▶ Complete course — one file</strong><audio controls preload="none" src="${D.fullAudio}"></audio></div>` : ''}
      <h2 style="border-bottom:1px solid var(--line);padding-bottom:.2em">Space audiobooks</h2>
      ${books}
    </div>`;
}

function renderPage(id){
  const p = D.pages[id];
  if (!id || id === 'home' || !p){ renderHome(); localStorage.setItem(LS_LAST,'home'); return; }
  current = id; localStorage.setItem(LS_LAST, id); refreshTicks();
  const idx = D.order.indexOf(id);
  const prev = idx > 0 ? D.order[idx-1] : null;
  const next = idx >= 0 && idx < D.order.length-1 ? D.order[idx+1] : null;
  const parts = p.parts.filter(x => x.html.trim());
  const audio = p.audio ? `<div class="audiobar">
      <audio controls preload="none" src="${p.audio}"></audio>
      <div class="row">
        ${p.audiobook ? `<a href="${p.audiobook}" target="_blank">▶ Full space audiobook</a>` : ''}
        <span>Module ${idx+1} of ${D.order.length}</span>
      </div></div>` : '';
  const tabs = parts.length > 1
    ? `<div class="tabs">${parts.map((x,i)=>`<span class="tab${i?'':' active'}" data-i="${i}">${x.label}</span>`).join('')}</div>` : '';
  const bodies = parts.map((x,i)=>`<div class="content" data-body="${i}" ${i?'hidden':''}>${x.html}</div>`).join('');
  const isMod = p.kind === 'module';
  page.innerHTML = `
    <div id="crumb">${p.crumb || ''}</div>
    <h1 id="ptitle">${p.title}</h1>
    ${audio}${tabs}${bodies}
    ${isMod ? `<button class="donebtn${done.has(id)?' on':''}" id="doneBtn">${done.has(id)?'✓ Completed':'Mark module complete'}</button>` : ''}
    <div class="pager">
      <button ${prev?'':'disabled'} data-go="${prev||''}">← Previous</button>
      <button ${next?'':'disabled'} data-go="${next||''}">Next →</button>
    </div>`;
  page.querySelectorAll('.tab').forEach(t => t.onclick = () => {
    page.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));
    t.classList.add('active');
    const i = t.dataset.i;
    page.querySelectorAll('[data-body]').forEach(b => b.hidden = b.dataset.body !== i);
  });
  const db = $('#doneBtn');
  if (db) db.onclick = () => {
    if (done.has(id)) done.delete(id); else done.add(id);
    saveDone(); renderPage(id);
  };
  page.querySelectorAll('[data-go]').forEach(b => b.onclick = () => {
    if (b.dataset.go){ location.hash = b.dataset.go; }
  });
  $('#main').scrollTop = 0;
  $('#sidebar').classList.remove('open');
}

function route(){
  const id = location.hash.replace(/^#/, '') || localStorage.getItem(LS_LAST) || 'home';
  renderPage(id);
}
window.addEventListener('hashchange', route);
$('#search').addEventListener('input', e => {
  const q = e.target.value.toLowerCase().trim();
  document.querySelectorAll('.navlink').forEach(a => {
    if (a.dataset.id === 'home'){ return; }
    a.style.display = !q || a.textContent.toLowerCase().includes(q) ? '' : 'none';
  });
  document.querySelectorAll('.sec, .grp').forEach(s => {
    const any = [...s.querySelectorAll('.navlink')].some(a => a.style.display !== 'none');
    s.style.display = any ? '' : 'none';
  });
});
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT') return;
  if (e.key === '[' ) { const b = page.querySelector('[data-go]:not([disabled])'); if(b&&b.textContent[0]==='←') b.click(); }
  if (e.key === ']' ) { const bs = page.querySelectorAll('[data-go]:not([disabled])'); const b=bs[bs.length-1]; if(b&&b.textContent.includes('Next')) b.click(); }
});
$('#menuBtn').onclick = () => $('#sidebar').classList.toggle('open');

buildNav();
route();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
    write_site()
