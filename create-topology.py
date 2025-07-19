# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "toml",
#   "diskcache",
#   "platformdirs",
#
#   "hypernetx", "fastjsonschema",
#   "matplotlib", "PyQt5",
# ]
# ///

import os
import sys

import diskcache
import platformdirs

cache = diskcache.Cache(platformdirs.user_cache_dir('sectop-1'))
CACHE_EXPIRE_S = 60 * 60

def lcache(key, expensive_call, expire=CACHE_EXPIRE_S):
    global cache
    value = cache.get(key, None)
    if value is None:
        value = expensive_call()
    cache.set(key, value, expire=expire)
    return value

import hypernetx
import matplotlib
import matplotlib.pyplot

# Hello world from https://colab.research.google.com/github/pnnl/HyperNetX/blob/master/tutorials/basic/Basic%202%20-%20Visualization%20Methods.ipynb#scrollTo=eee46b55-04fa-4aee-961c-fbdaa14b3322

scenes = {
    0: ('FN', 'TH'),
    1: ('TH', 'JV'),
    2: ('BM', 'FN', 'JA'),
    3: ('JV', 'JU', 'CH', 'BM'),
    4: ('JU', 'CH', 'BR', 'CN', 'CC', 'JV', 'BM'),
    5: ('TH', 'GP'),
    6: ('GP', 'MP'),
    7: ('MA', 'GP')
}

H = hypernetx.Hypergraph(scenes)
hypernetx.draw(H)

matplotlib.use('Qt5Agg') # Allows UI to be drawn
#matplotlib.pyplot.figure(figsize=(8, 6)) # Unnecessary
hypernetx.drawing.draw(H, with_node_labels=True, with_edge_labels=True)
matplotlib.pyplot.show()

