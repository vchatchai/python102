import glob
import os
import shutil


print(os.getcwd())
# glob.glob("*.py", recursive=True)
print(f'glob.glob(\'python102/*.py\') =>  {glob.glob("*py*", recursive=True)}')
