# ! program to divide two number without using / or bitwise operator
def divison(D,d):
  if D < d:
    return 0
  return 1 + divison(D-d,d)

print(divison(122,3))
