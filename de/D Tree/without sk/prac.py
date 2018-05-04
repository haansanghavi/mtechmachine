import math
"""
col1 = ["blonde","blonde","brown","blonde","red","brown","brown","blonde"]
col2 = ["avg","tall","short","short","avg","tall","avg","short"]
col3 = [""]
"""

#Hair = [0,0,1,0,2,1,1,0]
Hair = ['Bl','Bl','Br','Bl','Red','Br','Br','Bl']
Height = ['a','t','s','s','a','t','a','s']
Weight = ['l','a','a','a','h','h','h','l']
Lotion = [1,0,0,1,1,1,1,0]
Sunburn = [0,1,1,0,0,1,1,1]
all_list = [Hair,Height,Weight,Lotion]
all_index = []

for _ in range(len(all_list)):
    all_index.append(_)


#print(hair_ele)

def truefalse(a):
    yes=no=0
    for _ in range(len(a)):
        if a[_] == 1:
            yes+=1
        else:
            no+=1
    return yes,no


def similar(a,b):
    n=0
    yes=no=0
    #print(a,b)
    #print(Sunburn)
    for i in range(len(a)):
        if a[i] == b:
            n=n+1
            if Sunburn[i] == 0:
                yes+=1
            else:
                no+=1        
    #print(yes,no)
    return n,yes,no

def entropy(pos,neg,tot):
    #print("Pos:",pos)
    #print("Neg:",neg)
    #print("Tot:",tot)
    
    if pos == 0:
        return 0
    elif neg == 0:
        return 0
    elif pos == neg:
        return 1
    else:
        entropy = -((pos/tot)*math.log((pos/tot),2))-((neg/tot)*math.log((neg/tot),2))
        #print("\nEn",entropy,"\n")
        return entropy


def infogain(a,f_ent,lenb):
    tot = len(a)
    a_set = set(a)
    a_list = []
    values = []
    info_gain = 0
    in_entropy = 0
    fin=0
    
    for i in range(len(a_set)):
        a_list.append(a_set.pop())
        temp,yes,no = similar(a,a_list[i])
        values.append(temp)
        in_entropy = entropy(yes,no,tot)
        #print("Entropy:",in_entropy)
        info_gain += in_entropy
        total=yes+no
        #print("YesNo",yes,no)
        #print("fdghsdfhgsdf",total)
        #yes,no = truefalse(b)
        #sun_ent = entropy(yes,no,len(b))
        fin += total/lenb*in_entropy
    info_gain = f_ent-fin
    return info_gain



#print(entropy())
    
#print("Info Gain(Hair):", infogain(Hair))

yes,no = truefalse(Sunburn)
sun_ent = entropy(yes,no,len(Sunburn))
print("\n\n\nSS:",Sunburn,"\n\n\n")

tree = []
for _ in range(len(all_list)):
	tree.append(infogain(all_list[_],sun_ent,len(Sunburn)))
	print("Info Gain(",all_list[_],"):", infogain(all_list[_],sun_ent,len(Sunburn)))

print(tree)
#sorted(tree,all_list, reverse=True)
Z = [x for _,x in sorted(zip(tree,all_index), reverse=True)]

print("all_index",Z)
for _ in range(len(all_index)):
    print("\ntree",tree[Z[_]],"\nlist",all_list[Z[_]])


print("\n\n\nTree:",tree)



print("all list:",all_list)
print("\n\n\n")
	

temp_pop = all_list.pop(0)

yes,no = truefalse(temp_pop)
sun_ent = entropy(yes,no,len(temp_pop))

print("\naaaaaaaaaa",temp_pop,sun_ent,"\n")

tree = []
for _ in range(len(all_list)):
	tree.append(infogain(all_list[_],sun_ent,len(temp_pop)))
	print("Info Gain(",all_list[_],"):", infogain(all_list[_],sun_ent,len(temp_pop)))

print(tree)
#sorted(tree,all_list, reverse=True)
Z = [x for _,x in sorted(zip(tree,all_index), reverse=True)]

print("all_index",Z)
"""for _ in range(len(all_index)):
    print("\ntree",tree[Z[_]],"\nlist",all_list[Z[_]])
"""

print("\n\n\nTree:",tree)




print("all list:",all_list)
print("\n\n\n")


def finalinfogain(val1,attr):
    setAttr = set(attr)
    valAttr = []
    count = 0
    totalBl = 0
    for i in Hair:
        if i == 'bl':
            totalBl+=1
           
    for i in setAttr:
        valAttr.insert(count,i)
        count+= 1
    
    entropylist = []
    totalList = []
    #print(valAttr)
    #when hair is bl
    j = 0
    for i in range(len(valAttr)):
        pos = 0
        neg = 0
        for j in range(len(Sunburn)):
            if Hair[j] == 'Bl':
                #print('bl')
                if attr[j] == valAttr[i]:
                    #print(attr[j],valAttr[i])
                    if Sunburn[j] == 1:
                        pos += 1
                    elif Sunburn[j] == 0:
                        neg += 1
                   
       
        #print("pos",pos)
        totalList.insert(i,pos+neg)
        entropylist.insert(i,entropy(pos,neg,pos+neg))
   
           
    print("\n\n",entropylist,"\n")
   
    i = 0
    sum = 1
    for i in range(len(entropylist)):
        sum = sum - ((totalList[i]/4)*entropylist[i])
       
    print("\n",sum)
    return sum               

"""
yes,no = truefalse(Sunburn)
sun_ent = entropy(yes,no,len(Sunburn))


tree.append(infogain(all_list[Z[0]],tree[Z[0]],len(all_list[Z[0]])))
print("Info Gain(",all_list[_],"):", infogain(all_list[Z[0]],tree[Z[0]],len(all_list[Z[0]])))

print(tree)
#sorted(tree,all_list, reverse=True)
Z = [x for _,x in sorted(zip(tree,all_index), reverse=True)]

print("all_index",Z)
for _ in range(len(all_index)):
    print("\ntree",tree[Z[_]],"\nlist",all_list[Z[_]])
    
"""





finalinfogain('bl',Height)
finalinfogain('bl',Lotion)



