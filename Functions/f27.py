# Write a recursive function flatten(lst) that flattens a nested list structure. 
def flatten(lst):
  flat_list = []
  for item in lst:
    if type(item) in [list]:
      flat_list.extend(flatten(item))  
    else:
      flat_list.append(item)
  return flat_list