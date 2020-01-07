import re

result = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print('\bf[a-z]* => {result}')

result = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

print(f"r'(\b[a-z]+) \1' => {result}")

result = 'tea for too '.replace('too', 'two')
print(f"'tea for too '.replace('too', 'two') => {result}")
