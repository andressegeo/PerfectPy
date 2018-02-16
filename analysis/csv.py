import os
import logging as lg
lg.basicConfig(level=lg.DEBUG)

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data", data_file)
    
    try:
        with open(path_to_file, "r") as f:
            preview = f.readline()
            lg.debug("great it works: {}".format(preview))
    except FileNotFoundError as e:
        lg.critical("fichier no found: {}".format(e))
    

    

if __name__ == "__main__":
    launch_analysis('current_mps.csv')