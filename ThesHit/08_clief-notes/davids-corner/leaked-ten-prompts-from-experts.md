# LEAKED: Ten Prompts from Experts

Kilde: https://www.skool.com/cliefnotes/classroom/c7f102c7?md=3efb754483f44f3990c57f3d6656bcad

**Prompt-mønstre.** Ti prompt-maler presentert som «lekket av en eks-Anthropic-forsker», med påstand om målbar kvalitetsøkning. De to første (representative for resten):

1. **Context Brief** — hopp aldri rett på spørsmålet. Start med: «Du hjelper meg med [konkret mål]. Bakgrunn: [rolle + prosjekt + begrensninger]. Jeg har allerede prøvd [X og Y]. Jeg står fast på [Z]. Bekreft først at du forstår hele konteksten før du foreslår noe.» (Hevdet +41 % output-kvalitet.) «Claude er ikke synsk — gi den hele kartet.»
2. **Force Visible Reasoning** — be ikke om svaret, krev prosessen: vis fullt steg-for-steg-resonnement, list eksplisitt hver antakelse, flagg usikkerheter med konfidensnivå (lav/medium/høy).

Resten følger samme ånd: gi rik kontekst, tving frem synlig tenkning, be om antakelser og usikkerhet.

**Relevans for oss:** «Context Brief» ER vår 5-delte `agent.md`-mal og `operations/DISPATCH.md` Mission Brief Builder. «Force Visible Reasoning» = `/verify` og `/redteam`-kommandoene + `VERIFICATION.md`. Foundation 1.3 «How to Structure Any Prompt» sier det samme.

**Kategori:** David's Corner — Developer Resources
