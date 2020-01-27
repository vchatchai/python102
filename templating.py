from string import Template

t = Template('${village}folk send $$10 to $cause.')
result = t.substitute(village='Nottingham', cause='the ditch fund')

print(result)


result = t.safe_substitute()
print(result)

import time, os.path

photofiles = ['image_1074.jpg', 'img_1076.jp', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
t = BatchRename(fmt)

date = time.strftime('%d%b%y')

for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n = i, f=ext)
    print('{0} --> {1}'.format(filename, newname))