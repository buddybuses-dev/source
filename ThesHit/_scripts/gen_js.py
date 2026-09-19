import json, sys, io, os

ROOT = r"C:\Users\Mizgin2\ThesHit"

TEMPLATE = r"""
function htmlToMd(title, html) {
  const root = document.createElement('div');
  root.innerHTML = html;
  function inline(node) {
    let out = '';
    for (const child of node.childNodes) {
      if (child.nodeType === 3) { out += child.textContent; continue; }
      const tag = child.tagName ? child.tagName.toLowerCase() : '';
      if (tag === 'strong' || tag === 'b') out += '**' + inline(child).trim() + '**';
      else if (tag === 'em' || tag === 'i') out += '*' + inline(child).trim() + '*';
      else if (tag === 'br') out += '\n';
      else if (tag === 'code') out += '`' + inline(child) + '`';
      else out += inline(child);
    }
    return out;
  }
  const lines = ['# ' + title, ''];
  const kids = Array.from(root.children);
  let skipNextHr = false;
  kids.forEach((el, i) => {
    const tag = el.tagName.toLowerCase();
    if (tag === 'p' && i === 0) {
      const onlyStrong = el.children.length === 1 && el.children[0].tagName === 'STRONG';
      if (onlyStrong) {
        lines.push('## ' + inline(el).trim().replace(/\*\*/g, ''));
        lines.push('');
        skipNextHr = true;
        return;
      }
    }
    if (tag === 'hr') {
      if (skipNextHr) { skipNextHr = false; return; }
      lines.push('———'); lines.push(''); return;
    }
    skipNextHr = false;
    if (tag === 'h1' || tag === 'h2') lines.push('## ' + inline(el).trim().replace(/^\d+\.\s+/, ''));
    else if (tag === 'h3') lines.push('### ' + inline(el).trim().replace(/^\d+\.\s+/, ''));
    else if (tag === 'p') lines.push(inline(el).trim());
    else if (tag === 'blockquote') lines.push('> ' + inline(el).trim());
    else if (tag === 'ul' || tag === 'ol') {
      let n = 1;
      for (const li of el.children) {
        const prefix = tag === 'ul' ? '- ' : (n++ + '. ');
        lines.push(prefix + inline(li).trim());
      }
    }
    else lines.push(inline(el).trim());
    lines.push('');
  });
  return lines.join('\n').replace(/\n{3,}/g, '\n\n').trim() + '\n';
}

async function fetchOne(slug) {
  const res = await fetch('https://the-faction.mn.co/api/web/v1/spaces/23776511/posts/' + slug, {credentials: 'include'});
  if (!res.ok) return {error: 'HTTP ' + res.status};
  const json = await res.json();
  return {title: json.title, md: htmlToMd(json.title, json.description)};
}

const batch = __BATCH__;

const parts = [];
const report = [];
for (const b of batch) {
  const r = await fetchOne(b.slug);
  if (r.error) { report.push({idx: b.idx, err: r.error}); continue; }
  parts.push('@@@MODULE ' + b.idx + '@@@\n' + r.md);
  report.push({idx: b.idx, len: r.md.length});
}
document.body.innerHTML = '';
const pre = document.createElement('pre');
pre.textContent = parts.join('\n');
document.body.appendChild(pre);
JSON.stringify(report)
"""

def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    m = json.load(io.open(os.path.join(ROOT, "_scripts", "manifest.json"), encoding="utf-8"))
    batch = [{"idx": i, "slug": m[i]["url"].rsplit("/", 1)[-1]} for i in range(lo, hi)]
    js = TEMPLATE.replace("__BATCH__", json.dumps(batch))
    out_path = os.path.join(ROOT, "_scripts", "_gen.js.txt")
    with io.open(out_path, "w", encoding="utf-8") as f:
        f.write(js)
    print(f"wrote {out_path} for indices [{lo},{hi})")

if __name__ == "__main__":
    main()
