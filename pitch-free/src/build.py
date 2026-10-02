import pathlib
here=pathlib.Path(__file__).parent
src=here.parent.parent/"index.html"
L=src.read_text(encoding="utf-8").split("\n")
# shell, rail and notes CSS from the v2 prototype (lines 12..97); the story world is our own
css="\n".join(L[11:97])
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Profile Analyzer Story</title>
<meta name="description" content="UGC Breakouts proposal: a free public page where a creator types their TikTok handle and taps through a story of their own breakouts.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">
<style>
'''
out=head+css+"\n"+(here/"pf.css").read_text(encoding="utf-8")+"\n</style>\n</head>\n<body>\n"+(here/"body.html").read_text(encoding="utf-8")+"\n<script>\n"+(here/"app.js").read_text(encoding="utf-8")+"</script>\n</body>\n</html>\n"
(here.parent/"index.html").write_text(out,encoding="utf-8")
print(len(out))
