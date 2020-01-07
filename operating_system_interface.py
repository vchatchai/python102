import os

value = os.getcwd()

print(f'os.getcmd() => {os.getcwd()}')
print(f'os.cpucount() => {os.cpu_count()}')
print(f'dir(os) => {dir(os)}')
# print(f'help(os) => {help(os)}')


import shutil

value = shutil.disk_usage('e:\workspace')
print(value)