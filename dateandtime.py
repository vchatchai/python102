from datetime import date

now = date.today()
print(f'date.today() => {now} ')
print(f'now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.") => {now.strftime("%d-%m-%y. %d %b %Y is a %A on the %d day of %B")}')
birthday = date(1982, 11, 15)
print(f'birthday => {birthday}')
print( f'age = now - birthday =>{now - birthday}')