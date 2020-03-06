b = []
for i in range(3):
  a = []
  for j in range(4):
    a.append(0)
  b.append(a)

b[0][1] = 1
print(b)