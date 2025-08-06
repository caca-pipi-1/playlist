from streamlink import Streamlink
from streamlink.options import Options

import sys

options = Options({
    "email": sys.argv[1],
    "password": sys.argv[2]
})

session = Streamlink(options)
streams = session.streams("https://www.tf1.fr/tf1/direct")

print(streams["best"].url)