import random as ran  # Import the random module with alias 'ran'

wh = int(input("number of password ? "))  # Ask the user how many characters the password should have
wha = input("Password difficulty ?   easy / normal / difficult / very difficult ")  # Ask the user for password difficulty

# Lists for storing different parts of password
rando_num_ans = []  # List to store random numbers
rando_password = []  # List to store the final password characters
rando_word_ans = []  # List to store random special characters
rando_word_en_ans = []  # List to store random uppercase letters
rando_word_en_ans_s = []  # List to store random lowercase letters

# Lists of characters to choose from
rando_word = ['@','!','#','$','%','&','*','+','/','-','.','_','=']  # Special symbols
rando_word_en = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']  # Uppercase letters
rando_word_en_s = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  # Lowercase letters
items = [1,2,3,4,5,6,7,8,9,0]  # Numbers from 0 to 9

# Create easy password (only numbers)
if wha == "easy":
    for i in range(wh):  # Loop for the number of characters
        rando_d = ran.sample(items,1)  # Pick one random number
        ans = rando_d[0]  # Get the number from list
        rando_num_ans.append(ans)  # Add number to list

    for i in range(wh):  # Print the password numbers
        for j in range(1):  
            print(rando_num_ans[i], end='')  # Print each number without newline
    print("")  # Print newline after password
    print("your password is : ⬆ ⬆")  # Print message

# Create normal password (numbers + special characters)
elif wha == "normal":
    whaa = wh - 4  # Subtract 4 for special characters
    for i in range(whaa):
        rando_d = ran.sample(items, 1)  # Pick random numbers
        ans = rando_d[0]
        rando_num_ans.append(ans)
    for i in range(4):  # Add 4 special characters
        rrr = ran.choice(rando_word)
        rando_word_ans.append(rrr)
    rando_password.extend(rando_num_ans)  # Add numbers to final password
    rando_password.extend(rando_word_ans)  # Add special characters
    ran.shuffle(rando_password)  # Shuffle the password to mix numbers and symbols

    for i in range(wh):  # Print the password
        for j in range(1):
            print(rando_password[i], end='')
    print("")
    print("your password is : ⬆ ⬆")

# Create difficult password (numbers + symbols + uppercase letters)
elif wha == "difficult":
    whaa = wh - 9  # Subtract 9 for letters and symbols
    for i in range(whaa):
        rando_d = ran.sample(items, 1)
        ans = rando_d[0]
        rando_num_ans.append(ans)
    for i in range(4):  # Add 4 special characters
        rrr = ran.choice(rando_word)
        rando_word_ans.append(rrr)
    for i in range(5):  # Add 5 uppercase letters
        rrr_en_w = ran.choice(rando_word_en)
        rando_word_en_ans.append(rrr_en_w)

    rando_password.extend(rando_word_en_ans)  # Add uppercase letters
    rando_password.extend(rando_num_ans)  # Add numbers
    rando_password.extend(rando_word_ans)  # Add symbols
    ran.shuffle(rando_password)  # Shuffle all characters

    for i in range(wh):
        for j in range(1):
            print(rando_password[i], end='')
    print("")
    print("your password is : ⬆ ⬆")

# Create very difficult password (numbers + symbols + uppercase + lowercase letters)
elif wha == "very difficult":
    whaa = wh - 11  # Subtract 11 for letters and symbols
    for i in range(whaa):
        rando_d = ran.sample(items, 1)
        ans = rando_d[0]
        rando_num_ans.append(ans)
    for i in range(4):  # Add 4 special characters
        rrr = ran.choice(rando_word)
        rando_word_ans.append(rrr)
    for i in range(5):  # Add 5 uppercase letters
        rrr_en_w = ran.choice(rando_word_en)
        rando_word_en_ans.append(rrr_en_w)
    for i in range(2):  # Add 2 lowercase letters
        rrr_en_w_s = ran.choice(rando_word_en_s)
        rando_word_en_ans_s.append(rrr_en_w_s)

    rando_password.extend(rando_word_en_ans_s)  # Add lowercase letters
    rando_password.extend(rando_word_en_ans)  # Add uppercase letters
    rando_password.extend(rando_num_ans)  # Add numbers
    rando_password.extend(rando_word_ans)  # Add symbols
    ran.shuffle(rando_password)  # Shuffle all characters

    for i in range(wh):
        for j in range(1):
            print(rando_password[i], end='')
    print("")
    print("your password is : ⬆ ⬆")

else:
    print("what???!?!")  # Print error if difficulty not recognized

# Mohammad Reza Mokhtari Kia
