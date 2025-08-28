num_list=[]
result={}
count=int(input("How many names do you need to enter?"))
for _ in range(count):
    name=input("Name:").lower()
    num_list.append(name)    
    result.setdefault(name,0)
    if name in result:
        result[name]+=1
    if name not in result:
        result.setdefault(name)
max_count=max(result.values())
most_count=[name for name,v in result.items() if v==max_count]
print("Your result is:",most_count,"/// That much -->",max_count)
