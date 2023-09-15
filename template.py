import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep" ,#-----deployent yaml file
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]


#----logic to create this template

for filepath in list_of_files:
    filepath = Path(filepath) #----it will take of path differences in mac and windows

    filedir,filename = os.path.split(filepath) #----seperating filepath and files 

    #check my file directory is empty

    if filedir != "":
        os.makedirs(filedir,exist_ok=True) #----creating directory if it does not exist
        logging.info(f"creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (not os.path.getsize(filepath)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file:{filepath}")
    else:
        logging.info(f"file already exists:{filepath}")
    
