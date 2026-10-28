import json, sys, os
src, data_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
html = open(src, encoding="utf-8").read()
data = json.load(open(data_path, encoding="utf-8"))
seed = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
assert "/*SEED*/" in html
open(out, "w", encoding="utf-8").write(html.replace("/*SEED*/", seed))
print("ok", os.path.getsize(out), "bytes")
