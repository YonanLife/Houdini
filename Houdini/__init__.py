import logging
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s %(levelname)s:%(name)s:%(message)s", datefmt="%Y-%m-%d %H:%M:%S")

logging.getLogger("beaker.container").setLevel(logging.INFO)
