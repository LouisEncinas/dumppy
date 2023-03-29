import subprocess
import pkg_resources
import sys

ver = sys.version[:4]
if ver[-1] == '.': ver = ver[:-1]
for module in pkg_resources.working_set:
    subprocess.call(f'py -{ver} -m pip install --upgrade {module.project_name}', shell=True)