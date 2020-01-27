import reprlib
setvalue = set('supercalifragilisticexpialidocious')
print(f'setvalue => {setvalue}')
value = reprlib.repr(setvalue)
print(f'reprlib.repr(set("supercalifragilisticexpialidocious")) => {value}')

import pprint

t = [[[['black', 'cyan'], 'white', ['green','red']],[['magenta'],'yello'], 'blue']]

pprint.pprint(t, width=30)

import textwrap

doc = """The warp() method is just like fill() except that it returns 
a list of string instead of one big string with newlines to separate 
the wrapped lines"""

print(textwrap.fill(doc, width=40))

import locale

locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv()
x = 1234567.8


print(f'locale.format_string("%d", x, grouping=True) => {locale.format_string("%d", x, grouping=True)}')