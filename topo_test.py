import frontrunner.geo.topo_filter as topo_filter
from creds import GOOGLE_API_KEY as key

def get_open_pixels():
    return topo_filter.main(key)