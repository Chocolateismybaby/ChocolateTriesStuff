import random
import time
print("Encrypter/Decrypter.\n\n")
nb_of_wrong = 0
time.sleep(1)

#Function to check if password is valid
def pass_isallowed(passw):
    unallowed = [" ", "\\", "\'", "\"", "{", "}"]
    for char in unallowed:
        if char in passw:
            print("Password has invalid characters. Try again.\nInvalid characters: " + str(unallowed))
            return False

#Function to derive the Usable Key (with extra spaces) from the raw key by using a password
def keywithspaces(key, passw, pass_keys):

#Seeing how many spaces need to be added
    add_key = 0
    for text in passw:
        add_key += pass_keys[text]

#Creating the string of spaces
    add_space = ""
    for x in range(add_key):
        add_space += " "

#Cutting it in half
    half1 = add_space[0:(int((add_key / 2)))]
    half2 = add_space[(int((add_key / 2)))::]

#Adding one half to beginning and end of key
    key = half1 + key + half2
    return key

#Start
while True:
    choice = input("""Do you want to:
    a. Encrypt
    b. Decrypt\n>""")

#Encrypter Part
#=================================================================

    if choice.lower() == "a" or choice == "1":
        raw = input("Text or filename: \n")

        #Getting password
        while True:
            passw = input("Password (if any): ")
            if pass_isallowed(passw) != False: break

        #Checking if user wants to encrypt Raw Text or File Content
        if raw.endswith(".txt"):
            input_file = open(raw, "r", encoding="utf-8")
            raw_text = input_file.read()
        else:
            raw_text = raw

        #What should the output file name be?
        out_name = input("Output filename: ")
        if out_name == "": out_name = "file"

        #Now to create a randomly generated key of a random size between 750,000 and 1,000,000
        print("Generating Key...")
        chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                 "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F",
                 "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!",
                 "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[",
                 "]", "^", "_", "`", "{", "|", "}", "~", " ", "\n", "\'", "\""]

        pwd_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                 "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F",
                 "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!",
                 "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[",
                 "]", "^", "_", "`", "|", "~"]


        #Getting random Key Length
        key_len = random.randint(750000, 1000000)

        #Making the key
        rand = 0
        key = ""
        for step in range(key_len):
            rand = random.randint(0, 95)
            key += chars[rand]

        #Checking if the key contains all characters
        for char in key:
            if char in chars:
                """ """
            else:
                input("Wtf this wasn\'t supposed to happen. Exit and try again.")

        #Writing the key to the Key File
        keyname = str(out_name) + "_key"
        key_file = open(keyname, "w")
        key_file.write(key)
        key_file.close()


        pwd_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F",
                     "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!",
                     "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[",
                     "]", "^", "_", "`", "|", "~"]



        #Creating a dictionary where each possible character has a random but unique value
        pass_keys = {}
        used_nbs = []
        rand_nb = 0
        for i in pwd_chars:
            used = False
            while used == False:
                rand_nb = random.randint(0, 95)
                if rand_nb in used_nbs:
                    continue
                else:
                    pass_keys[i] = rand_nb
                    used_nbs.append(rand_nb)
                    used = True

        #Getting the Key with spaces at beginning and end
        key = keywithspaces(key, passw, pass_keys)
        key_len2 = len(key)

        print("Working...")

        #Analyzing the key and saving the indexes where every character exists into the index_dict
        #The dictionary entries look like this   "character":[list of indexes where it exists]
        index_dict = {}
        ind = 0
        for letter in key:
            if letter in index_dict:
                index_dict[letter].append((ind + key_len2))
            else:
                index_dict[letter] = [(ind + key_len2)]
            ind += 1
        if ind == (key_len2):
            """ """
        else:
            input("Wtf this wasn\'t supposed to happen. Exit and try again.")


        #Start encrypting by replacing every character of the string to be encrypted by one of its indexes in the Key With Spaces, and separating them by "l"
        final_output = ""
        length = 0
        lind = 0
        invs = 0
        refreshes = 0
        dict_backup = index_dict
        for character in raw_text:
            try:
                length = len(index_dict[character])
                if len(index_dict[character]) == 0:
                    index_dict = dict_backup
                    length = len(index_dict[character])
                    refreshes += 1
                lind = random.randint(0, (length - 1))
                final_output = final_output + str(index_dict[character][lind]) + "l"
                del index_dict[character][lind]

            except:
                invs += 1

        #Writing the dictionary of random values assigned to the letters
        added = str(pass_keys).replace(", ", "\n")
        added = added.replace("{", "\n{\n")
        added = added.replace("}", "\n}")

        #Writing the output
        final_output += added
        final_file = open(out_name, "w")
        final_file.write(final_output)
        final_file.close()

        #Stuff that doesn't really matter
        if invs == 0 and refreshes == 0:
            input("Done")
        elif invs != 0 and refreshes == 0:
            input("Done with " + str(invs) + " errors.")
        elif invs == 0 and refreshes != 0:
            input("Done with " + str(refreshes) + " dictionary refreshes.")
        elif invs != 0 and refreshes != 0:
            input("Done with " + str(invs) + " errors and " + str(refreshes) + " dictionary refreshes.")
        nb_of_wrong = 0


# Decrypter Part
# =================================================================

    elif choice.lower() == "b" or choice == "2":
        #Asking for the name of the encrypted file and opening it
        while True:
            try:
                fname = input("Encrypted file name: ")
                kname = fname + "_key"
                input_file = open(fname, "r")
                txt = input_file.read()
                input_file_data = txt.split("\n")
                input_file.close()
                key_file = open(kname, "r")
                key = key_file.read()
                key_file.close()

                #Asking for the password used when encrypting and checking if it's valid
                while True:
                    passw_dec = input("Enter password (if any): ")
                    if pass_isallowed(passw_dec) != False: break
            except:
                print("Invalid file.")
            break

        #Extracting the first line of the encrypted file which contains the list of indexes separated by "l"
        txtdata = txt[0:(txt.index("l\n") + 1)] + "l"

        #Reading the dictionary of random value for every letter and writing it into pass_keys_dec
        line_nb = 0
        pass_keys_dec = {}

        for line in input_file_data:
            line_nb += 1
            if line_nb < 3: continue
            else:
                line = line.rstrip()
                line = line.lstrip()
                try:
                    pass_keys_dec[line[1]] = int(line[4::])
                except: """ """


        #Adding spaces to the beginning and end of the key according to the password. If the password was incorrect the number of spaces will also
        #be incorrect so so the entire indexes will mess up and the output will be wrong
        key = keywithspaces(key, passw_dec, pass_keys_dec)

        #Separating the indexes
        output = ""
        key_len = len(key)
        txtdata = txtdata.split("l")

        #Replacing each index with its letter from the Key With Spaces
        for ind in txtdata:
            try:
                ind = int(ind)
                output += key[(ind - key_len)]
            except:
                """ """

        #Checking if the output is large and writing it to a file if it is
        if len(output) > 1000:
            final_name = fname + "_decrypted.txt"
            ff = open(final_name, "w")
            ff.write(output)
            ff.close()
            input("Output is large, wrote to file.")
        else:
            input(output)


# If user enters invalid command
# =================================================================
#This part doesn't matter at all :D I was bored and didn't know what to do

        nb_of_wrong = 0
    else:
        if nb_of_wrong < 2:
            print("\nChoose either A or B.\n")
        elif nb_of_wrong == 2:
            print("\nYou're starting to piss me off. Be careful.\n")
            time.sleep(3)
        elif nb_of_wrong == 3:
            print("That's it I'm done with you.")
            sec = 60
            while sec != 0:
                print(sec)
                time.sleep(1)
                sec = sec - 1
            print("\nWow you waited. How lifeless.\n")
            nb_of_wrong = 1
        nb_of_wrong += 1
