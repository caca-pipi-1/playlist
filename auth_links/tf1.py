from streamlink import Streamlink
from streamlink.options import Options

import sys

options = Options({
    "email": sys.argv[1],
    "password": sys.argv[2],
    "purge-credentials": True
})

session = Streamlink(options)
streams = session.streams("https://www.tf1.fr/tf1/direct")

print(streams)

print(streams["best"].url)