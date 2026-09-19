"""Minimal, dependency-free Markdown -> HTML converter tuned for the ThesHit study guides.
Handles: ATX headings, bold/italic/code, links, blockquotes (nested), ordered/unordered
lists with continuation lines, fenced code blocks, horizontal rules, paragraphs."""
import re, html as _html

_HR = re.compile(r'^(-{3,}|\*{3,}|_{3,}|—{1,})$')
_H = re.compile(r'^(#{1,6})\s+(.*)$')
_LI = re.compile(r'^(\s*)([-*+]|\d+[.)])\s+(.*)$')


def slugify(s: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-') or 'x'


def _inline(t: str) -> str:
    t = _html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'__([^_]+?)__', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*(?!\s)([^*]+?)(?<!\s)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(
        r'\[([^\]]+)\]\(([^)\s]+)\)',
        lambda m: f'<a href="{_html.escape(m.group(2), quote=True)}" target="_blank" rel="noopener">{m.group(1)}</a>',
        t,
    )
    return t


def convert(md: str) -> str:
    lines = md.replace('\r\n', '\n').replace('\r', '\n').split('\n')
    out, para = [], []
    i, n = 0, len(lines)

    def flush():
        if para:
            out.append('<p>' + _inline(' '.join(x.strip() for x in para).strip()) + '</p>')
            para.clear()

    while i < n:
        raw = lines[i]
        s = raw.strip()

        if s.startswith('```'):
            flush()
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith('```'):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append('<pre><code>' + _html.escape('\n'.join(buf)) + '</code></pre>')
            continue

        if not s:
            flush()
            i += 1
            continue

        if _HR.match(s):
            flush()
            out.append('<hr>')
            i += 1
            continue

        m = _H.match(s)
        if m:
            flush()
            lvl, txt = len(m.group(1)), m.group(2).strip()
            out.append(f'<h{lvl} id="{slugify(txt)}">{_inline(txt)}</h{lvl}>')
            i += 1
            continue

        if s.startswith('>'):
            flush()
            q = []
            while i < n and lines[i].strip().startswith('>'):
                q.append(re.sub(r'^\s*>\s?', '', lines[i]))
                i += 1
            out.append('<blockquote>' + convert('\n'.join(q)) + '</blockquote>')
            continue

        if _LI.match(raw):
            flush()
            ordered = bool(re.match(r'^\s*\d+[.)]\s+', raw))
            tag = 'ol' if ordered else 'ul'
            items = []
            while i < n and _LI.match(lines[i]):
                mm = _LI.match(lines[i])
                text = mm.group(3)
                i += 1
                cont = []
                while i < n and lines[i].strip() and not _LI.match(lines[i]):
                    cont.append(lines[i].strip())
                    i += 1
                if cont:
                    text += ' ' + ' '.join(cont)
                items.append('<li>' + _inline(text) + '</li>')
            out.append(f'<{tag}>' + ''.join(items) + f'</{tag}>')
            continue

        para.append(s)
        i += 1

    flush()
    return '\n'.join(out)


if __name__ == '__main__':
    import sys
    print(convert(open(sys.argv[1], encoding='utf-8-sig').read()))
