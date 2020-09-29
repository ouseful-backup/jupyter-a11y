import pkg_resources

#__version__ = pkg_resources.require("nbreader")[0].version
#version_info = pkg_resources.parse_version(__version__)

def _jupyter_nbextension_paths():
    return [dict(section="notebook",
                 src="static",
                 dest="nbreader",
                 require="nbreader/index")]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("nbreader enabled!")
