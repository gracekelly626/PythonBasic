def get_circle_area(local_radius):
  local_area = 3.14*local_radius**2
  return local_area ##return local result; need a container to receive it while outside the function itself; print does not need it 

def check_circle_area(local_area):
  if local_area <= 0:
    print('this is not valid:', local_area) 
  elif local_area >= 50:
    print('this is such a big circle:', local_area)
  elif 50> local_area >= 40:
    print('this is such a medium circle:', local_area)
  else:
    print('this is such a small circle:', local_area)

area1 = get_circle_area(1)
area2 = get_circle_area(5)
area3 = get_circle_area(10)
check_circle_area(area1)
check_circle_area(area2)
check_circle_area(area3)

print('------')

def return_circle_area(local_area):
  if local_area <= 0:
    return 'this is not valid:'+ str(local_area) 
  elif local_area >= 50:
    return 'this is such a big circle:' + str(local_area)
  elif 50> local_area >= 40:
    return 'this is such a medium circle:'+ str(local_area)
  else:
    return 'this is such a small circle:'+ str(local_area)

result1 = return_circle_area(area1)
print(result1)


## concept of parameter
## parameter aka argument 
## like local_area in return_circle_area(local_area)
