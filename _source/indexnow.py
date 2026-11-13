"""Ping IndexNow (Bing, Yandex, Seznam, Naver...) with every URL in sitemap.xml.
Run after each deploy:  python3 _source/indexnow.py  [optional: specific URLs]"""
import json, re, sys, urllib.request
HOST = "www.inspectandprotect.net"
KEY = "bc4134a152736a86c3f7ac0cd286e2d6"
def urls():
    if len(sys.argv) > 1:
        return sys.argv[1:]
    xml = urllib.request.urlopen(f"https://{HOST}/sitemap.xml").read().decode()
    return re.findall(r"<loc>([^<]+)</loc>", xml)
u = urls()
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": u}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
r = urllib.request.urlopen(req)
print(r.status, len(u), "URLs submitted")
