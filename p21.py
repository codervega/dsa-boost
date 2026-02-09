def toachievegoal(start,goal):
  num = start ^ goal
  count = 0
  while(num):
    count = count + 1
    num = num >> 2
  
  return count


start = int(input("enter the start"))
goal = int(input("enter the goal"))

ans = toachievegoal(start,goal)
print(ans)