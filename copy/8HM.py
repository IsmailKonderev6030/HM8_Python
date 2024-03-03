with open("p1.txt",'r',encoding='utf-8') as p1:
    first = []
    i = 1
    for line in p1:
        first.append(line)
        print(i,'.',line,sep='',end='')
        i+=1
    
print()
index = int(input("Enter index line for copy: "))

with open("p2.txt",'a',encoding='utf-8') as p2:
    p2.write(first[index-1])