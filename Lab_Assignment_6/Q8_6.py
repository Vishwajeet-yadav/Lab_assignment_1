def fun(v):
  g=v.split(',')
  l=[]
#   l= [-25, -10, -7, -3, 2, 4, 8, 10]
  output = []
  for i in g:
      l.append(int(i))
  for i in l:
      for j in l:
          for k in l:
              if i+j+k == 0 and i<j<k:
                  output.append([i,j,k])
  print(output)
v=input('Enter the numbers seperated by ",": ')
fun(v)