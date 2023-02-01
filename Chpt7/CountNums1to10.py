current_num=0
## jumps all the even numbers and prints only the odd numbers.
while current_num <10:
    current_num+=1
    if(current_num%2)==0:
        continue
    print(current_num)