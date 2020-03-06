def solution(Board):

  path = []
  flag = []
  for i in range(int(rows)):
    a = []
    for j in range(len(Board[0])):
      a.append(0)
    flag.append(a)
  m = max(max(Board))
  for i in range(int(rows)):
    for j in range(len(Board[0])):
      if Board[i][j] == m:
        flag1 = flag.copy()
        flag1[i][j] = 1
        print(flag,"AAA")
        path.append(genpath(i, j, 4, flag1)) 
  return max(path)
  
# Return the n-digit number started from [a, b] in the Board
def genpath(a, b, n, f):
  val = B[a][b]
  print(a, b, f)
  #print(val,"v")
  if (n == 1):
    return val
  else:
    if (a-1>-1 and f[a-1][b]==0):
      f1 = f.copy()
      f1[a-1][b] = 1
      val1 = 10**(n-1)*val + genpath(a-1,b,n-1,f1)
    #  print(val1,"a")
      val_list.append(val1)
    if (a+1<int(rows) and f[a+1][b]==0):
      f1 = f.copy()
      f1[a+1][b] = 1
      val1 = 10**(n-1)*val + genpath(a+1,b,n-1,f1)
    #  print(val1,"b")
      val_list.append(val1)
    if (b-1>-1 and f[a][b-1]==0):
      f1 = f.copy()
      f1[a][b-1] = 1
      val1 = 10**(n-1)*val + genpath(a,b-1,n-1,f1)
     # print(val1,"c")
      val_list.append(val1)
    if (b+1<len(B[0]) and f[a][b+1]==0):
      f1 = f.copy()
      f1[a][b+1] = 1
      val1 = 10**(n-1)*val + genpath(a,b+1,n-1,f1)
      val_list.append(val1)
    #  print(val1,"d")
    val = max(val_list)
    return val

rows = input("The number of the rows: ")
B = []
val_list = []
for i in range(int(rows)):
  Bi = input("Input the numbers of row " + str(i) + " :")
  bi = Bi.split(",")
  b = [int(item) for item in bi]
  B.append(b)

print(solution(B))