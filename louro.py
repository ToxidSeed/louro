#!/home/alone/projects/venv/bin/python
import os
from config import app_path
os.chdir(app_path)

from gui.principal import init
init()