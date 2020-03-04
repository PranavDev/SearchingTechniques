#Binary Search and Linear Search

def Linear_Search(Elements):
  print("\n------### LINEAR SEARCH ###------")
  e = int(input("  #Enter element to search : "))
  flag = 0
  computations = 0
  for i in range(0,len(Elements)):
    computations = computations + 1
    if(e==Elements[i]):
      print("      ~ELEMENT ",e," FOUND AT INDEX:",(i+1))
      flag = 1
  if(flag==0):
    print("      ~ELEMENT ",e," NOT FOUND")
  print("### COMPUTATIONS : ",computations)


def Binary_Search(Elements):
  low = 0
  high = len(Elements)
  mid = int((low+high)/2)
  flag = 0
  computations = 0
  print("\n------### BINARY SEARCH ###------")
  e = int(input("  #Enter element to search : "))
  while(mid>=0 or mid<=len(Elements)-1):
    computations = computations + 1
    if(mid==low and low==high):
      break
    if(e<Elements[mid]):
      high = mid
    elif(e>Elements[mid]):
      low = mid
    else:
      flag = 1
      break
    mid = int((low+high)/2)
  if(flag==1):
    print("      ~ELEMENT ",e," FOUND AT INDEX:",(mid+1))
  else:
    print("      ~ELEMENT ",e," NOT FOUND")
  print("### COMPUTATIONS : ",computations)

#MAIN
Elements = []
n = int(input(">Enter the Number of elements : "))

i = 0
for i in range(0,n):
  ele = int(input("  #Enter Element : "))
  Elements.append(ele)

print("\nList : ",Elements)

flag = 0
while(flag!=9):
  ch = int(input("\n\n>Enter 1.Linear Search   2.Binary Search   3.Exit : "))
  if(ch==1):
    Linear_Search(Elements)
  elif(ch==2):
    Binary_Search(Elements)
  else:
    flag=9
