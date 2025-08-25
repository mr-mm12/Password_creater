import random as ran
wh=int(input("number of password ? "))
wha=input("Password difficulty ?   easy / normal / difficult / very difficult ")
# for add lists
rando_num_ans=[]
rando_password=[]
rando_word_ans=[]
rando_word_en_ans=[]
rando_word_en_ans_s=[]
rando_word=['@','!','#','$','%','&','*','+','/','-','.','_','=']
rando_word_en=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rando_word_en_s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
items=[1,2,3,4,5,6,7,8,9,0]
#for create easy password
if wha == "easy":
    for i in range(wh):
        rando_d=ran.sample(items,1)
        ans=rando_d[0]
        rando_num_ans.append(ans)
    for i in range(wh):
        for j in range(1):
            print(rando_num_ans[i], end='')
    print("")
    print("your password is : ⬆ ⬆")
#for create normal password
elif wha == "normal":
    whaa=wh - 4
    for i in range(whaa):
        rando_d = ran.sample(items, 1)
        ans = rando_d[0]
        rando_num_ans.append(ans)
    for i in range(4):
        rrr = ran.choice(rando_word)
        rando_word_ans.append(rrr)
    rando_password.extend(rando_num_ans)
    rando_password.extend(rando_word_ans)
    ran.shuffle(rando_password)
    for i in range(wh):
        for j in range(1):
            print(rando_password[i], end='')
    print("")
    print("your password is : ⬆ ⬆")
#for create difficult password
elif wha == "difficult":
    whaa=wh - 9
    for i in range(whaa):
        rando_d = ran.sample(items, 1)
        ans = rando_d[0]
        rando_num_ans.append(ans)
    for i in range(4):
        rrr = ran.choice(rando_word)
        rando_word_ans.append(rrr)
    for i in range(5):
        rrr_en_w=ran.choice(rando_word_en)
        rando_word_en_ans.append(rrr_en_w)
    rando_password.extend(rando_word_en_ans)
    rando_password.extend(rando_num_ans)
    rando_password.extend(rando_word_ans)
    ran.shuffle(rando_password)
    for i in range(wh):
        for j in range(1):
            print(rando_password[i], end='')
    print("")
    print("your password is : ⬆ ⬆")
#for create very difficult password
elif wha == "very difficult":
    whaa=wh - 11
    for i in range(whaa):
        rando_d = ran.sample(items, 1)
        ans = rando_d[0]
        rando_num_ans.append(ans)
    for i in range(4):
        rrr = ran.choice(rando_word)
        rando_word_ans.append(rrr)
    for i in range(5):
        rrr_en_w=ran.choice(rando_word_en)
        rando_word_en_ans.append(rrr_en_w)
    for i in range(2):
        rrr_en_w_s=ran.choice(rando_word_en)
        rando_word_en_ans_s.append(rrr_en_w_s)
    rando_password.extend(rando_word_en_ans_s)
    rando_password.extend(rando_word_en_ans)
    rando_password.extend(rando_num_ans)
    rando_password.extend(rando_word_ans)
    ran.shuffle(rando_password)
    for i in range(wh):
        for j in range(1):
            print(rando_password[i], end='')
    print("")
    print("your password is : ⬆ ⬆")
else:
    print("what???!?!")