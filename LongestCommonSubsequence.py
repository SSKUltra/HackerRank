#handle input

ins = input()
n = int(ins.split()[0])
m = int(ins.split()[1])

in_a = input()
in_b = input()

a = []
b = []

for i in range(n):
    a.append(int(in_a.split()[i]))
    
for j in range(m):
    b.append(int(in_b.split()[j]))

#C is a multidimensional list
#C is the table that stores Longest common subsequence values
w, h = m+1 , n+1 ;
C = [[0 for x in range(w)] for y in range(h)] 

#Stores one of the Longest common subsequence
out = []

#recursive equation used to solve problem in a bottom up iterative approach
for i in range(1,n+1,1):
    for j in range(1,m+1,1):
        if a[i-1] == b[j-1]:
            C[i][j] = C[i-1][j-1] + 1
            
        else:
            C[i][j] = max(C[i-1][j], C[i][j-1])

#Tracing back Longest common subsequence
while(1):
    if i <=0 or j<=0:
        break
    if a[i-1] == b[j-1]:
        out.append(a[i-1])
        i = i-1
        j = j-1
  
    else:
        if C[i-1][j] > C[i][j-1]:
            i = i-1
        else:
            j = j-1

#output
print(*reversed(out))
