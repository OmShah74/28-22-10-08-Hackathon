# urgency in scale 1 to 10
# importance in profit
# completion time in units
# we introduce a new parameter called S parameter by adding urgency and profit and subtracting by the duration required. 
# the entire thing is then divided by 3.
# We sort the jobs according to decreasing order of the above obtained parameter
def rank(l):
    for i in l:
        i.append((i[1]+i[2]-i[3])/3)
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if l[j][4]>l[i][4]:
                temp=l[j]
                l[j]=l[i]
                l[i]=temp
    for i in l:
        print(i[0],end=" ")

n=int(input("Enter number of jobs are there\n"))
l=[]
for i in range(n):
    k=[]
    k.append(i+1)
    k.append(int(input("Enter profit for job\n")))
    k.append(int(input("Enter importance in the scale of 1 to 10 for job\n")))
    k.append(int(input("Enter duration of completion of job\n")))
    l.append(k)
print(l)
rank(l)