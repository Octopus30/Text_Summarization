#python function we use multiple times

import os
from box.exceptions import BoxValueError #for the exceptions instead of 
#custom exception we use box exceptions
import yaml #to handle yaml files

from textSummarizer.logging import logger 


from box import ConfigBox 
"""
about config box
d  = {'key':"value"}
d = ConfigBox(d)
print(d.key)

this is more convinient to read instead of d['key'] so 
without getting the error and to read this we use configBox 
    """
from pathlib import Path #to handle path in both mac and windows
from typing import Any

from ensure import ensure_annotations
"""
why ensure_annotations? 

def get_product(x: int,y:int)->int:
    return x*y

get_product(10,20) o/p :200
get_product(2,'10') o/p: "1010"

to reduce these type of errors we use ensure_annotations

It is a good practice to use ensure_annotations to ensure that the
corrects arguments are passed to the function.
else it results in errors when the function is called.

"""


# to read the information inside the yaml files
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns
    Args:
        path_to_yaml (str): Path like input

    Raises:
        ValueError :if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe.load(yaml_file)
            logger.info(f"yaml file{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list, verbose =True):
    """Create list of directories.
    Args:
        path_to_directories (list): list of directories
        ignore_log (bool, optional): [ignore multiple directories to be created]. Defaults to False."""
    
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok = True)
        if verbose:
            logger.info(f"created directory at : {directory} ")

@ensure_annotations
def get_size(path :Path) -> str:
    """
    get size in KB

    Args:
        path (str): path to file

    Returns:
        str: size in KB
    """
    size_in_Kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_Kb} KB"


    
    

