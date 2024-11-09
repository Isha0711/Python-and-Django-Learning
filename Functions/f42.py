# Write a recursive function sum_all_recursive(*args) that sums all  numbers passed as arguments (including nested tuples or lists)
def sum_all_recursive(*args):
  total = 0
  for item in args:
    if type(item) in [list, tuple]:  
      total += sum_all_recursive(*item)
    else:
      total += item
  return total