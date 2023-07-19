import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format = '[%(asctime)s]:%(message)s:')

project_name = "TextVortex"

list_of_files = [
    ".github/workflows/.gitkeep"  ,
    # whenever we commit the code and push it in the repo , it will automatically deploy it into the cloud 
    # empty folder wont we uploaded into the cloud so we are storing an hidden folder '.gitkeep' later we'll delete it
    f"src/{project_name}/__init__.py",
    # when ever constructor package is created it will consider the folder where the __init__.py file as the package folder
      f"src/{project_name}/components/__init__.py",
      f"src/{project_name}/utils/__init__.py",
      f"src/{project_name}/utils/common.py",
      f"src/{project_name}/logging/__init__.py",
      f"src/{project_name}/config/__init__.py",
      f"src/{project_name}/config/configuration.py",
      f"src/{project_name}/pipeline/__init__.py",
      f"src/{project_name}/entity/__init__.py",
      f"src/{project_name}/constants/__init__.py",
      'config/config.yaml',
      'params.yaml',
      'app.py',
      'main.py',
      'Dockerfile',
      'requirements.txt',
      'setup.py',
      'research/trails.ipynb',
]

for filepath in list_of_files:
    filepath = Path(filepath)
    f_dir , f_name = os.path.split(filepath)
    if f_dir != "":
        os.makedirs(f_dir,exist_ok=True)
        logging.info(f"creating directory : {f_dir}, for the file{f_name}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"created a file {filepath}")
    else:
        logging.info(f"{f_name} already existsl")
