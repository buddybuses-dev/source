# 2.1 Why Remote Access

Kilde: https://www.skool.com/cliefnotes/classroom/2a86a1d1?md=b0db9033a43540578f305e5bb936a371

**Claude Code har nå Remote Control innebygd.** Start en økt ved pulten, skann en QR-kode,
fortsett fra telefonen. **Det lokale miljøet blir lokalt** — filer, MCP-servere, workspace;
ingenting flyttes til skyen, du bare aksesserer økten fra et annet sted. Erstatter tidligere
workarounds (SSH-tunneler, web-grensesnitt, custom front-ends) med én kommando + QR.
Muliggjør: **async workflows** (start et langt build, lukk lokket, sjekk telefonen, send en
justering) og **mobil monitoring** (renders, stor kodegenerering, multi-steg-pipelines — se
progresjon, grip inn når det trengs). Relevant for vår Tailscale/VPS-plan i `operations/vps-deploy.md`.

**Kategori:** Building Your Stack — Remote Access
