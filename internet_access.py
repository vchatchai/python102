from urllib.request import urlopen

with urlopen('https://www.bred-it.com/') as response : 
    for line in response :
        line = line.decode('utf-8')
        print(line)
        # if 'EST' in line  or 'EDT' in line :
            # print(line)