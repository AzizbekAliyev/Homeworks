a = list(map(int, input().split()))  
s = int(input())  

if s < sum(a):
  print(0)

print(s - sum(a))