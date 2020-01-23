from timeit import Timer

print(f"Timer('t=a; a=b; b=t', 'a=1; b=2') => {Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()}")
print(f"Timer('a,b = b,a', 'a=1; b=2').time.it() => {Timer('a,b = b,a', 'a=1; b=2').timeit()}")