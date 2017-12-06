import tkinter

#creating the windows
window = tkinter.Tk()

def homePage():
    #editing the layout of the window
    window.title("Mathematical education tool")
    window.geometry("500x400")
    window.wm_iconbitmap("schoolLogo.ico")
    window.configure(background="red")

    #adding the school logo and name
    photo = tkinter.PhotoImage(file="schoolNameLogo.png")
    schoolName = tkinter.Label(window, image=photo)
    schoolName.pack()

    #creating the username label and entry point
    studentAndStaff = tkinter.Label(window, text="Student and Staff:", fg="white", bg="red", font="calibri")
    studentAndStaff.pack()
    usernameLabel = tkinter.Label(window, text="Enter username here:", fg="white", bg="red")
    usernameLabel.pack()
    usernameEntry = tkinter.Entry(window)
    usernameEntry.pack()

    #creating the password label and entry point
    passwordLabel = tkinter.Label(window, text="Enter password here:", fg="white", bg="red")
    passwordLabel.pack()
    passwordEntry = tkinter.Entry(window)
    passwordEntry.pack()

    #creating the login buttons
    staffLoginButton = tkinter.Button(window, text="Staff login", fg="red", bg="white", command=staffWindow)
    studentLoginButton = tkinter.Button(window, text = "Student login", fg="red", bg="white",  command=studentWindow)
    staffLoginButton.pack()
    studentLoginButton.pack()

    #creating an exit button
    def closeApplication():
        window.destroy()
    
    exitButton = tkinter.Button(window, text="Quit", width=3, height=1,command= closeApplication)
    exitButton.pack()
    #start the application
    window.mainloop()


#creating the staff window
def staffWindow():
    #cling the homePage
    window.destroy()
    #creating and editing the layout of the staff window
    global windowStaff
    windowStaff = tkinter.Tk()
    windowStaff.title("Staff")
    windowStaff.geometry("500x350")
    windowStaff.wm_iconbitmap("staffIcon.ico")
    windowStaff.configure(background="green")


def studentWindow():
    #closing the homePage
    window.destroy()
    #creating and editing the layout of the student window
    global windowStudent
    windowStudent = tkinter.Tk()
    windowStudent.title("Student")
    windowStudent.geometry("800x1000")
    windowStudent.wm_iconbitmap("studentIcon.ico")
    windowStudent.configure(background="black")

    #adding different media to the student window
    quizTitle = tkinter.Label(windowStudent, text="Welcome to the space quiz!", bg="black", fg="white", font=("impact", 50))
    quizTitle.pack()
    backG = tkinter.Canvas(windowStudent, width=800, height=500)
    backG.pack()
    spaceBackground = tkinter.PhotoImage(file = "spaceBG.png")
    backG.create_image(0,0,image=spaceBackground)

    #creating the different buttons for each topic
    algebraTopicButton = tkinter.Button(windowStudent, text="Algebra", activebackground="yellow", activeforeground="blue", bg="grey", fg="white", height= 3, width=10, font=("times", 20), command=algebraWindow)
    algebraTopicButton.pack()
    algebraTopicButton.place(x=100,y=100)

    shapesTopicButton = tkinter.Button(windowStudent, text="Shapes", activebackground="yellow", activeforeground="blue", bg="grey", fg="white", height= 3, width=10, font=("times", 20), command=shapesWindow)
    shapesTopicButton.pack()
    shapesTopicButton.place(x=100,y=250)
    windowStudent.mainloop()

def algebraWindow():
    algebraQuestions = open("algebraQuestions.py", "r")
    #closing the studentWindow
    windowStudent.destroy()
    #creating the new algebra window
    global windowAlgebra #setting it as a global variable
    windowAlgebra = tkinter.Tk()
    windowAlgebra.title("Algebra") #naming the webpage banner

def shapesWindow():
    shapesQuestions = open("shapesQuestions.txt", "r+")
    windowStudent.destroy()
    global windowShapes
    windowShapes = tkinter.Tk()
    windowShapes.title("Shapes")
    windowShapes.geometry("500x500")
    windowShapes.configure(background = "turquoise1")
    def submit():
        print (answerEntryBox.get())
    questionNumberShapes = 1 #Set as a number so othe other questions can be used
    questionOnScreenShapes = shapesQuestions.readlines(10)
    userInput = tkinter.StringVar()
    var = userInput
    #questionNumberShapes += 1 #Increasing the question number by 1
    
    question = tkinter.Label(windowShapes, textvariable= var, fg="grey", bg= "turquoise1")
    question.pack()
    var.set(questionOnScreenShapes)
    enterAnswer = tkinter.Label(windowShapes, text="Enter your answer here:", fg="grey", bg="turquoise1")
    enterAnswer.pack()
    answerEntryBox = tkinter.Entry(windowShapes) #Creating an entry box allowing the user to type in their answer
    answerEntryBox.pack()
    answerSubmitButton = tkinter.Button(windowShapes, text="Submit", width = 5, command = submit)
    answerSubmitButton.pack()
    
    windowShapes.mainloop()

#running the function called homePage
homePage()
