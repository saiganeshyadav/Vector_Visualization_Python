import matplotlib.pyplot as plt
from matplotlib import style
print("-----vector addition-----")
print("Enter 1st vector(ai^+bj^)")
a=int(input("a:"))
b=int(input("b:"))
plt.plot((0,a),(0,b),label="vector 1",linewidth=3)
print("Enter 2nd vector(ci^+dj^ )")
c=int(input("c:"))
d=int(input("d:"))
e=a+c
f=b+d
plt.plot((0,c),(0,d),label="vector 2",linewidth=3)
plt.plot((0,e),(0,f),label="Resultant vector",linewidth=3)
plt.legend()
plt.title("vector addition and scalar multiplication")
plt.xlabel("X-axis")
plt.ylabel("y-axis")
style.use("ggplot")
plt.grid(True,color='k')
slope=d/c
g=a+1
k=1
for i in range(g,e+1,1):
    plt.plot((a,i),(b,(slope*k)+b))
    k+=1
    
slope1=b/a
s=c+1
j=1
for i in range(s,e+1,1):
    plt.plot((c,i),(d,(slope1*j)+d))
    j+=1

print("-----scalar multiplication------")
print("Enter vector(xi^+yj^)")
x=int(input("x:"))
y=int(input("y:"))
scalar=int(input("Enter scalar:"))
x1=scalar*x
y1=scalar*y
plt.plot((0,x),(0,y),label="normal vector",linewidth=3)
plt.plot((0,x1),(0,y1),label="scalar nvector",linewidth=3)
plt.legend()
plt.show()