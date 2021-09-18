## for loop
def sum_any(x):
  result = 0
  for i in range(1,x+1,2):
    result = result+i
    print(i)
  return result
print(sum_any(10))


## while loop
result = 0
while result < 100: #statement is usually boolean
  result = result + 1

print(result)


## while + break
result = 0
while result < 100:
  result = result + 1
  if result == 25:
    break #break the running outside while loop 

print(result)
