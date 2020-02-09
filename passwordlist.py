import sys

m = list(sys.argv[1]) # letter list to be used
n = int(sys.argv[2])  # number of const strings use 0,1,2,3,4 ...
t = sys.argv[3]       # name of file DONT PUT .txt  
c = open(t+ ".txt","a")
k = sys.argv[4]       # string which will generate and is the format
def mul(la,lb):
    c = []
    for i in la:
        for j in lb:
            c.append(i+j)    
    return c

def add(la,strr):
    lb = []
    for j in la  :
        lb.append(j+strr)
    return lb

log_level = 2

def log(text, level=1):
    if log_level >= level:
        print(text)
l = m
l = ['']
wl = {'I':['0','1','2','3','4','5','6','7','8','9'],'a':['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']}
'''
UNCOMMENT TO USE IN IDLE ELSE USE IN CMD
m = list(input("enter combination of alpha numeric if specific:  "))
n = int(input("enter number of constant strings :"))
t = input("enter name of file : ")   
c = open(n+ ".txt","a")
k = input("enter parse string : ")
'''
for j in range(n):
#    wl[str(j)] = str(input('enter string ' + str(j) + ' : '))  # UNCOMMENT FOR IDLE COMMENT LINE BELOW INSTEAD
    wl[str(j)] = str(sys.argv[5+j])
    l1.append(str(j))

wl['S'] = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=',':',';','<',',','.','?','/','<','>','~','`',"'",'"','{','}']
wl['A'] = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
wl['q'] = m


with open(t+".txt","a") as f :
    print(k)
    for j in k:
        if (ord(j) >= 48 ) and (ord(j) < 58):
            l= add(l,wl[j])
        else:
            l = mul(l,wl[j])
    for m in l :
        f.write(m)
        f.write("\n")
        log(m)
            
