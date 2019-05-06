graph =  {
          "tala"   : ["shebin"],
          "shebin" : ["tala","elsb3","quesna","minouf"],
          "elsb3"  : ["quesna","shebin"],
          "quesna" : ["elsb3","shebin"],
          "minouf" : ["shohda","shebin","sirs","sadat"],
          "shohda" : ["minouf"],
          "sirs"   : ["minouf","bagour"],
          "bagour" : ["sirs"],
          "sadat"  : ["minouf","ashmon"],
          "ashmon" : ["sadat"]
         }

dist =   {
          "tala"   : [0 , 16.3 , 19.7 , 32.8 , 32 , 13.7 , 31.5 , 31.9 , 77.5 , 56.6], 
          "shebin" : [16.3 , 0 , 15.2 , 18.3 , 17.9 , 14.3 , 16.2 , 16.2 , 67.5 , 39.1], 
          "elsb3"  : [19.7 , 14.3 , 0 , 17.1 , 31.6 , 28.9 , 30.1 , 29.2 , 82 , 51.5], 
          "quesna" : [32.8 , 18.3 , 17.1 , 0 , 33.7 , 30.8 , 32.5 , 33.7 , 87.7 , 50.1], 
          "minouf" : [32 , 17.9 , 31.6 , 33.7 , 0 , 22.8 , 7.2 , 17.1 , 57.6 , 24.1], 
          "shohda" : [13.7 , 14.3 , 28.9 , 30.8 , 22.8 , 0 , 27.1 , 30.7 , 78.9 , 41.6], 
          "sirs"   : [31.5 , 16.2 , 30.1 , 32.5 , 7.5 , 27.1 , 0 , 8.3 , 62.6 , 22.2], 
          "bagour" : [31.9 , 16.2 , 29.2 , 33.7 , 17.1 , 30.7 , 8.3 , 0 , 70.6 , 21], 
          "sadat"  : [77.5 , 67.5 , 82 , 87.7 , 57.7 , 78.9 , 62.6 , 70.6 , 0 , 75], 
          "ashmon" : [56.5 , 39.1 , 51.5 , 50.1 , 24.1 , 41.6 , 22.2 , 21 , 75 , 0]
         }

nodes = ["tala","shebin","elsb3","quesna","minouf","shohda","sirs","bagour","sadat","ashmon"]

#=============================
from collections import deque 
visited = []
queue = deque([])

newpath = []
path = list ( 20 * ' ' )
n = 0
flag = 0

H_Dist = {}
child_dist = {}
sorted_child_dist = {}

opened = []
closed = []
path1 = []

#==============================
def BFS(start,end):
    if (start == end):
        visited.append(end)
        return
    
    if ((not start in visited)and(not start in queue)):
        queue.append(start)
    for node in graph[start]:
        if( (not node in queue) and (not node in visited) ):
            queue.append(node)
    visited.append(queue.popleft())
    BFS(queue[0],end)
    
#==============================
def DFS(start,end):
    global flag
    global n
    if(flag == 0):
        path[n]=start
        if(start == end):
            flag=1
        n+=1
        visited.append(start)
        for cnt in graph[start]:
            if(not cnt in visited):
                DFS(cnt,end)
        n -= 1
        
#=================================
def Find_H_Dist(end):
    for i in range(10):
        H_Dist[nodes[i]] = dist[end][i]
        
#=================================
def Greedy_Search(start,end):

    global flag
    global n
    if(flag == 0):
        if(start == end):
            flag=1
            
        visited.append(start)
        for cnt in graph[start]:
            child_dist[cnt] = H_Dist[cnt]

        sorted_child_dist = sorted(child_dist.items(),key=lambda t:t[1])
        list8 = []
        for i in  sorted_child_dist:
            list8.append(i)
        for cnt in list8:
            if(not cnt[0] in visited):
                Greedy_Search(cnt[0],end)

#=================================
def get_distance(city1,city2):
    return dist[city1][nodes.index(city2)]
#=================================
def add(start,list1):
    global opened
    global closed
    global path1
    list3 =[]
    for c in list1:
        list3.append(c)
    list3.append(start)
    cost = 0
    list2 = []
    for i in range(len(list1)-1):
        cost += get_distance(list1[i],list1[i+1])
    
    list2.append(list3)
    list2.append(start)
    list2.append(cost)
    opened.append(list2)

#=================================    
def Asearch(start,end):
    global opened
    global closed
    global path1
    
    add(start,[])
    A_search(end)
    
#=================================
def A_search(goal):
    global opened
    global closed
    global path1
    min1 = opened[0]
    index = 0

    for i in range(1,len(opened),1):
        if ((min1[2]+get_distance(min1[1],goal))> ( opened[i][2]+get_distance(opened[i][1],goal) )):
            min1 = opened[i]
            index=i
    path1 = []
    for c in min1[0]:
        path1.append(c)
    closed.append(min1[1])
    opened.pop(index)
    for c in graph[min1[1]]:
        if( (not c in closed)and ( (c == goal) or (hasopenedchild(c)) ) ):
            add(c,path1)
        if( path1[-1] == goal ):
            return
    A_search(goal)
    
#================================
def hasopenedchild(c1):
    global opened
    global closed
    global path1
    global graph
    for i in graph[c1]:
        if(not i in closed):
            return True
    return False

#=================================        
def Take_In():
    while True:
        try:
            choice = input("Please Enter Your Choice : \n--------------------------\n(1) Breadth First Search Algorthim.\n(2) Depth First Search Algorthim.\n(3) Greedy Search Algorthim.\n(4) A* Search Algorthim.\n")
            if (choice != '1' and choice!= '2' and choice!= '3' and choice!= '4'):
                print("Error choice !! Try again\n")
                continue
        except(NameError):
            print("Error choice !! Try again\n")
            continue
        return choice
    
#================================

print ("                 ^_^ *** AI SEARCH ALGORTHIMS TASK *** ^_^ ")
print ("                 ----------------------------------------- \n")

input1 = Take_In()
if(input1 == '1'):
    start = input("Enter your Start City :")
    end = input("Enter Your End City :")
    BFS(start,end)
    print (visited)

elif(input1 == '2'):
    start = input("Enter your Start City :")
    end = input("Enter Your End City :")
    DFS(start,end)
    print (visited)

elif(input1 == '3'):
    start = input("Enter your Start City :")
    end = input("Enter Your End City :")
    Find_H_Dist(end)
    Greedy_Search(start,end)
    print (visited)

elif(input1 == '4'):
    start = input("Enter your Start City :")
    end = input("Enter Your End City :")
    Asearch(start,end)
    print (path1)
