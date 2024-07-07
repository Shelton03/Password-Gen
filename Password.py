import customtkinter,tkinter,random,emoji

letters = ['a','q','w','e','r','t','y','u','i','o','p','s','d','f','g','h','j','k','l',
           'z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G',
           'H','J','K','L','Z','X','C','V','B','N','M']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','^','&','*','(',')',':','?','/','|','{','}','~']

def save():

    global notificationText
   
    filename = desiredName.get() + ".txt"

    try:
        
        f = open(filename,"w")
        f.write(passStorage)
        f.close
        desiredName.forget()
        notificationText = customtkinter.CTkTextbox(app,font=("Arial",14),height=10,width=325)
        notificationText.pack(pady=10)
        notificationString = emoji.emojize(":check_mark_button:") + "Password Saved Successfuly in " + filename
        notificationText.insert(1.0,notificationString)
            
 
    except:

        notificationText= customtkinter.CTkTextbox(app,font=("Arial",14),height=10,width=325)
        notificationText.pack()
        errorString = emoji.emojize(":cross_mark:") + "Oops, Save Failed! An error occurred."
        notificationText.insert(1.0,errorString)
   

def generatePassword():

    global desiredName
    global passStorage
    password_list = []
    password = ""

    try:
        for char in range(1,int(numLtrs.get())+1):
            password_list.append(random.choice(letters))
            
        for char in range(1,int(numNums.get())+1):
            password_list.append(random.choice(numbers))
    
        for char in range(1,int(numSyms.get())+1):
            password_list.append(random.choice(symbols))

        random.shuffle(password_list)
        
        for char in password_list:
            password += char
    
        def clear():

            passwordText.delete(1.0,"end")
            genButton.pack(padx=10,pady=10)
            SaveButton.forget()
            clrButton.forget()
            passwordText.forget()
            notificationText.forget()
            desiredName.forget()

        SaveButton = customtkinter.CTkButton(app,text="Save",command=save)
        SaveButton.pack(padx=10,pady=10)

        clrButton = customtkinter.CTkButton(app,text="Clear",command=clear)
        clrButton.pack(padx=10,pady=10)
    
        passwordText = customtkinter.CTkTextbox(app,font=("Arial",14),height=10,width=325)
        passwordText.pack()

        passwordText.insert(1.0,password)

        desiredName = customtkinter.CTkEntry(app,width=325,height= 10,placeholder_text="Name of file where you want password to be saved")
        desiredName.pack(pady=10)


        genButton.forget()

        passStorage = password
        password=""
    
    except:
        errorText = customtkinter.CTkTextbox(app,font=("Arial",14),height=10,width=325)
        errorText.pack()
        errorString = emoji.emojize(":cross_mark:") + "Oops! An error occurred."
        errorText.insert(1.0,errorString)
    
    
#App Window
app = customtkinter.CTk()
app.geometry("350x525")
app.title("Password Generator")

#labels and Entry Boxes

welcomeLabel = customtkinter.CTkLabel(app,text="Welcome to Karma's password generator",text_color="grey")
welcomeLabel.pack(padx=10,pady=10)

ltrsLabel = customtkinter.CTkLabel(app,text="How many letters would you like in your password?", text_color="grey")
ltrsLabel.pack(padx=10,pady=10)

numLtrs = customtkinter.CTkEntry(app,width=325,height= 10,placeholder_text="Number of letters")
numLtrs.pack()

numsLabel = customtkinter.CTkLabel(app,text="How many numbers would you like in your password?", text_color="grey",)
numsLabel.pack(padx=10,pady=10)

numNums = customtkinter.CTkEntry(app, width=325,height=10,placeholder_text="Number of numbers")
numNums.pack()

symLabel = customtkinter.CTkLabel(app,text="How many symbols would you like in your password?", text_color="grey")
symLabel.pack(padx=10,pady=10)

numSyms = customtkinter.CTkEntry(app,width=325,height=10,placeholder_text="Number of Symbols")
numSyms.pack()

genButton = customtkinter.CTkButton(app,text="generate",command=generatePassword)
genButton.pack(padx=10,pady=10)

app.mainloop()