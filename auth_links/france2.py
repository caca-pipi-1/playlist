import requests
import streamlink
import urllib.parse
import utilities

manifest = requests.post("https://api.ssai.ftven.fr/v1/session/c6f323e65336fbba9ea766d582216fd61ed74452/SSAIFrance2OTTEMTConfiguration/out/v1/3f5d86a548454a27ab9a06078aa68a03/index.m3u8").json()["manifestUrl"]

url = "https://live-ssai-v2.ftven.fr/dai" + manifest

m3u8 = requests.get("https://hdfauth.ftven.fr/esi/TA?format=json&url=" + urllib.parse.quote(url, safe="")).json()["url"]

stream = streamlink.streams(m3u8)["best"].url

utilities.replace_url("FRANCE 2", stream)

print(stream)