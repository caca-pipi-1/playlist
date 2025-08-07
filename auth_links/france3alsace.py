import requests

stream = requests.get("https://hdfauth.ftven.fr/esi/TA?format=json&url=https%3A%2F%2Fsimulcast-fr3regions-p.ftven.fr%2Fsimulcast%2Falsace%2Fhls_francedomtom_alsace%2Fmaster.m3u8").json()["url"]

print(stream)