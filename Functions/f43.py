# Write a recursive function flatten_recursive(*args) that flattens any number of nested lists passed as arguments.
def flatten_recursive(*args):
  flat_list = []
  for item in args:
    if type(item) in [list, tuple]:  
      flat_list.extend(flatten_recursive(*item))  
    else:
      flat_list.append(item) 
  return flat_list
