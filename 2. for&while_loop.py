## for loop
def sum_any(x):
  result = 0
  for i in range(1,x+1,2):
    result = result+i
    print(i)
  return result
print(sum_any(10))

### for loop - dictinary and numpy array
# dictionary uses method; numpy array uses function;
for key, value in my_dict.items():

for value in np.nditer(my_array):


## while loop
result = 0
while result < 100: #statement is usually boolean
  result = result + 1
print(result)


## while loop in a function
def sum_any(x):
  result = 0
  i = 0
  while i < x:
    i = i+1
    result = result+i
    print(i)
  return result
print(sum_any(10))



## while + break
result = 0
while result < 100:
  result = result + 1
  if result == 25:
    break #break the running outside while loop 
print(result)


## while vs if --- WHILE LOOP keeps excuting until it reaches to the boolen statement; IF only runs once and stops. 
def sum_any(x):
  result = 0
  i = 0
  if i < x:
    i = i+1
    result = result+i
    print(i)
  return result
print(sum_any(10))
