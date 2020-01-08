import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

print( f'data => {data}')
mean = statistics.mean(data)
print(f'statistics.mean(data) => {mean}')
median = statistics.median(data)
print(f'statistics.median(data) => {median}')
variance = statistics.variance(data)
print(f'statistics.variance(data) => {variance}')