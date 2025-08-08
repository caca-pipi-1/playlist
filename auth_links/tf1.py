from streamlink import Streamlink
from streamlink.options import Options
import sys
import utilities

options = Options({
    "email": sys.argv[1],
    "password": sys.argv[2],
    "purge-credentials": True
})

session = Streamlink()
stream = session.streams("https://www.tf1.fr/tf1/direct", options)["best"].url

utilities.replace_url("TF1", stream)

print(stream)