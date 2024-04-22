# g_n={'A':[('B',2),('C',3)],'B':[('D',5)],'C':[('D',2)],'D':[]}
# h_n={'A':3,'B':4,'C':2,'D':0}
g_n={}
h_n={}

n=int(input("enter the value of n"))
for i in range(1,n+1):
    node=input("enter the node: ")
    neighbour=input("enter the neighbour: ")
    if neighbour=='':
        g_n[node]=[]
    else:
        list1=[]
        for i in list(neighbour.split(',')):
            cost=int(input("enter the estimated path cost: "))
            t=tuple([i,cost])
            list1.append(t)
        g_n[node]=list1
print(g_n)
def heuristic():
    for i in g_n:
        c=int(input(f"enter the heuristic cost{i}: "))
        h_n[i]=c
    print(h_n)

def a_search(start,goal,path):
    if start==goal:
        print(path)
        return
    min=10000000000
    node=start
    for i in g_n[start]:
        m=i[0]
        n=i[1]
        if(n+h_n[start]<=min):
            min=n+h_n[start]
            node=m
    path.append(node)
    a_search(node,goal,path)
heuristic()   
start=input("enter the start node: ")
goal=input("enter the goal node : ")
path=list()
path.append(start)
a_search(start,goal,path)
