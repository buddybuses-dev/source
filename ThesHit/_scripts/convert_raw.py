import re, sys, io

BULLET_SECTIONS = {"your toolkit", "common pitfalls", "self-assessment checklist"}
NUMBERED_KEEP = {"exam topics"}  # keep as plain paragraphs already separated by blank lines -> bullets too

def convert(raw_body, title):
    lines = raw_body.split("\n")
    # drop leading nav/author lines up to and including the "T4 ... |" course line and the "This is the study guide" line
    # find first "N. " numbered heading
    out = ["# " + title, ""]
    i = 0
    n = len(lines)
    # Find course tagline line (contains " | ") before first numbered heading, and the "This is the study guide" line
    preamble = []
    while i < n and not re.match(r"^\d+\.\s+\S", lines[i]):
        preamble.append(lines[i])
        i += 1
    # from preamble, find the "X | Y" tagline and the "This is the study guide..." sentence
    tagline = None
    intro = None
    for ln in preamble:
        s = ln.strip()
        if not s or s == title.split(" — ")[0] or s.lower() in ("matt murphy", "🏅"):
            continue
        if tagline is None and "|" in s:
            tagline = s
            continue
        if s.lower().startswith("this is the study guide"):
            intro = s
            continue
    if tagline:
        out.append("## " + tagline)
        out.append("")
    if intro:
        out.append(intro)
        out.append("")

    section = None
    para_buf = []

    def flush_para():
        nonlocal para_buf
        if not para_buf:
            return
        text = " ".join(p.strip() for p in para_buf if p.strip())
        para_buf = []
        if not text:
            return
        if section in BULLET_SECTIONS or section in NUMBERED_KEEP:
            out.append("- " + text)
        else:
            out.append(text)
        out.append("")

    while i < n:
        line = lines[i]
        m = re.match(r"^\d+\.\s+(.*)$", line.strip())
        if m and line.strip()[0].isdigit():
            flush_para()
            section = m.group(1).strip().lower()
            out.append("## " + m.group(1).strip())
            out.append("")
            i += 1
            continue
        if line.strip() == "":
            flush_para()
            i += 1
            continue
        para_buf.append(line)
        i += 1
    flush_para()

    # trim trailing boilerplate after "Ready to move on to the next Lesson?"
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text

def main():
    path = sys.argv[1]
    raw = io.open(path, encoding="utf-8").read()
    # split header
    header, body = raw.split("---\n", 1)
    title_line = [l for l in header.split("\n") if l.startswith("Title:")][0]
    title = title_line[len("Title: "):].split(" | ")[0].strip()
    # cut body at "Ready to move on to the next Lesson?"
    cut = body.find("Ready to move on to the next Lesson?")
    if cut != -1:
        body = body[:cut]
    md = convert(body, title)
    sys.stdout.write(md)

if __name__ == "__main__":
    main()
