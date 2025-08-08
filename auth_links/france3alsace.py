import requests
import streamlink
import utilities

m3u8 = requests.get("https://hdfauth.ftven.fr/esi/TA?format=json&url=https%3A%2F%2Fsimulcast-fr3regions-p.ftven.fr%2Fsimulcast%2Falsace%2Fhls_francedomtom_alsace%2Fmaster.m3u8").json()["url"]

stream = streamlink.streams(m3u8)["best"].url

utilities.replace_url("FRANCE 3 ALSACE", stream)

print(stream)