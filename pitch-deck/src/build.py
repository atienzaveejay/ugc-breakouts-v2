import re,pathlib
here=pathlib.Path(__file__).parent
src=here.parent.parent/"index.html"
L=src.read_text(encoding="utf-8").split("\n")
css="\n".join(L[11:727])      # lines 12..727
start=next(i for i,l in enumerate(L) if l.startswith('<svg width="0" height="0"'))
end=next(i for i in range(start,len(L)) if L[i].strip()=="</svg>")
sprite="\n".join(L[start:end])
extra='''  <symbol id="i-deck" viewBox="0 0 24 24"><rect class="i" x="3" y="5" width="18" height="12" rx="2"/><path class="i" d="M8 21h8M12 17v4M7 9h6M7 12h10"/></symbol>
  <symbol id="i-download" viewBox="0 0 24 24"><path class="i" d="M12 4v11M7.5 10.5 12 15l4.5-4.5M5 19h14"/></symbol>
  <symbol id="i-mail" viewBox="0 0 24 24"><rect class="i" x="3" y="5" width="18" height="14" rx="2"/><path class="i" d="m4 7 8 6 8-6"/></symbol>
</svg>'''
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Pitch Deck Generator</title>
<meta name="description" content="UGC Breakouts proposal: a creator builds a brand pitch deck from their own TikTok numbers and breakouts.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">
<style>
'''
out=head+css+"\n"+(here/"pd.css").read_text(encoding="utf-8")+"\n[hidden]{display:none!important}img{max-width:100%}\n</style>\n</head>\n<body>\n"+sprite+"\n"+extra+"\n"+(here/"body.html").read_text(encoding="utf-8")+"\n<script>\n"+(here/"app.js").read_text(encoding="utf-8")+"</script>\n</body>\n</html>\n"
dst=here.parent/"index.html"
dst.parent.mkdir(exist_ok=True)
dst.write_text(out,encoding="utf-8")
print(len(out))
