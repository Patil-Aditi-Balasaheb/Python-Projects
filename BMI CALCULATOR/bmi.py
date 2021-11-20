"""BMI calculator"""

from tkinter import *
from tkinter .font import Font
from PIL import ImageTk,Image  
import tkinter as tk
import time
from tkinter.messagebox import showinfo
from datetime import date
from tkinter import ttk


class Patient:
    """Creating patient class to model patient details for BMI calculation."""
    def __init__(self, name="UNKNOWN", gender="UNKNOWN", age="UNKNOWN", ppsn="TESTING", weight=0.0, height=0.0):
        """Setting class attributes."""
        self.name = name
        self.gender = gender
        self.age = age
        self.ppsn = ppsn
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        """creating method to calculate body mass index, returns float
        BMI= weight(kg) / ( height(m)*height(m) )
        Example:
        >>> Patient(weight=75, height=1.7).calculate_bmi()
        25.95155709342561
        """
        return float(self.weight / (self.height * self.height))

    def bmi_analysis(self):
        """Analyse the patient's BMI:
        < 15 very severly underweight, < 18.5 underweight, < 25 healthy, < 30 overweight, 30+ obese
        >>> Patient(height=1.83, weight=89).bmi_analysis()
        'overweight'
        """
        bmi = self.calculate_bmi()
        if bmi < 16:
            analysis = "very severely underweight"
            b = "severly_underweight"
            exercise = "\nYoga Poses such as:\n1) Camel Pose\n2) Plow Pose\n3) Boat Pose\n4) Tree Pose\n5) Triangle Pose\n6) Belly breathing\n7) Cobra Pose\n8) Warrior Pose\n9) Down dog Pose"
            diet = "\n1) Follow a high calorie, high protein and high calcium diet plan.\n2) Include more of milk and milk products e.g. milk and protein shakes, yogurt, smoothies, cottage cheese etc.\n3) Include peanut butter, walnuts, almonds, raisins and other dry fruits in your diet.\n4) Include potatoes, sweet potatoes, yam, colocasia, white rice, sago and other high calorie items.\n5) If prefer non vegetarian, include red meat, chicken Fish, Eggs.\n6) Eat more of vegetables and fruits especially bananas, mangoes, watermelon, pomegranate, carrots, beans, broccoli, spinach, grapes, beetroot etc.\n7) Include good quality MUFA & PUFA rich oils.\n8) Drink plenty of water.\n9) Follow a small frequent meal pattern.\n10) Remember eating junk food only adds to your calories not to the nutrition. So be wise to yourself and choose healthy."
        elif bmi < 18.5:
            analysis = "underweight"
            b = "underweight"
            exercise = "\n1) Running\n2) Weight lifting\n3) Cycling\n4) Up Up Down Down\n5) Squats\n6) Bench Up and Down\n7) Press Shoulder\n8) Bench Dips\n9) Sage Twist Pose\n10) Seated Side Stretch\n11) Pushups\n12) Pullups\n13) Hula Hopping\n14) Superman\n15) Skipping\n16) Tree Pose"
            diet = "\n1) Drink plenty of water.\n2) High calorie high protein diet is recommended.\n3) Consume your food in frequent small meals and eat at a regular interval of 2 hours.\n4) Include nuts like almons, walnuts, cashews, raisins, coconut etc.\n5) Use high calorie items eg. peanut butter cheese, coconut chutney.\n6) Increase consumption of potatoes, sweet potatoes, colocasia beans, and other vegetables.\n7) If you are anemic include pomegranate, watermelon, spinach and beetroot in your diet.\n8) Include high calorie fruits like banana, mango, grapes, custard apple etc.\n9) Include eggs, Chicken, Fish."
        elif bmi < 25:
            analysis = "healthy"
            b = "healthy"
            exercise = "\n1) Skipping\n2) Running\n3) Swimming\n4) Anulom-Vilom\n5) Suryanamaskar\n6) Pranayam"
            diet = "\n1) Eat a variety of nutrient-rich foods.\n2) Match food intake with physical activity.\n3) Avoid fried, salty and spicy foods.\n4) Consume adequate water to avoid dehydration.\n5) Avoid smoking, chewing of tobacco and tobacco products (Khaini, Zarda, Paan masala) and consumption of alcohol.\n6) Fruits, vegetables, legumes (e.g. lentils, beans), nuts and whole grains.\n7) Green leafy vegetables, other vegetables, fruits, eggs, milk and milk products and flesh foods."
        elif bmi < 30:
            analysis = "overweight"
            b = "overweight"
            exercise = "\n1) Lunges 2x15\n2) Single Leg Bridge 2x15\n3) Squats 2x15\n4) Push Ups 2x15\n5) Mountain Climber 2x15\n6) Bicycle Crunches 2x15\n7) Dumbell Bench Press\n8) V-bar pulldowns\n9) Deadlifts\n10) Triceps Pushdown\n11) Leg Press\n12) Walking\n13) Jogging\n14) Jumping Rope\n15) Swimming\n16) Anything else you can think of to keep you moving"
            diet = "\n1) Whole wheat bread\n2) Oatmeal\n3) Whole wheat pasta\n4) Brown rice\n5) Fish, Chicken\n6) Eggs (but don't eat too many yolks)\n7) Fat free cottage cheese, fat free peanut butter, fat free yogurt\n8) Any fruits or vegetables\n9) Avoid eating junk food and oily stuff"
        else:
            analysis = "obese"
            b = "obese"
            exercise = "\nYoga Poses such as:\n1) Bridge Pose\n2) Camel Pose\n3) Warrior I, II and III Pose\n4) Upward and Downward facing dog\n5) Lord of the Dance Pose\n6) Intense Side stretch Pose\n7) Plank and Reverse Plank Pose\n8) Lotus, Cow, Child, Cat, Bow, Chair Pose\n9) Shoulderstand\n10) Thunderbolt and Extended Triangle Pose"
            diet = "\n1) Whole wheat bread\n2) Oatmeal\n3) Whole wheat pasta\n4) Brown rice\n5) Fish, Chicken\n6) Eggs (but don't eat too many yolks)\n7) Fat free cottage cheese, fat free peanut butter, fat free yogurt\n8) Any fruits or vegetables\n9) Avoid eating junk food and oily stuff\n10) A good multivitamin"
        return analysis,b,exercise,diet

    def generate_report(self):
        """Creating method to generate report to file containing patient details and BMI results."""
        report_file = open(self.ppsn, "w")
        print("-" * 100, file=report_file)
        print("\t\tPATIENT REPORT", file=report_file)
        print("-" * 100, "\n", file=report_file)
        self.today = date.today()
        print("Date:\t",self.today,file=report_file)
        print("\nPatient name:\t", self.name, file=report_file)
        print("Patient gender:\t", self.gender, file=report_file)
        print("Patient age: \t", self.age, file=report_file)
        print("Patient PPSN:\t", self.ppsn, file=report_file)
        print("Patient weight:\t", self.weight, "kg", file=report_file)
        print("Patient height:\t", self.height, "m", file=report_file)
        print("Patient BMI: \t", round(self.calculate_bmi(), 1), file=report_file)
        self.b = self.bmi_analysis()
        print("BMI Analysis: \t", self.b[0].upper(), file=report_file)
        print("\nExercise Suggested:", self.b[2], file=report_file)
        print("\nDiet Suggested:", self.b[3], file=report_file)
        print("\n\n\n", file=report_file)
        report_file.close()
        
        #self.onClick()
    
    def onClick(self):
        tk.messagebox.showinfo("Generate Report","Report has been downloaded in your folder.")


root=""
user=""
report_win=""
severly_underweight_win=""
exercise_su_win=""
diet_su_win=""
underweight_win=""
exercise_u_win=""
diet_u_win=""
healthy_win=""
exercise_h_win=""
diet_h_win=""
overweight_win=""
exercise_o_win=""
diet_o_win=""
obese_win=""
exercise_ob_win=""
diet_ob_win=""

new_font=""
my_font=""
height=0
width=0
    
class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("BMI Calculator")
        self.config(bg="black")
        
        #getting screen width and height of display
        width= self.winfo_screenwidth() 
        height= self.winfo_screenheight()
        #setting tkinter window size
        self.geometry("%dx%d" % (width, height))
        
        #background image
        im = Image.open('bmi1.png')
        im = im.resize((width, height), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(im)
        tk.Label(self,image = tkimage).pack(pady=0)
        
        #required to make window show before the program gets to the mainloop
        self.update()
        
def main():
    global root
    global height
    global width
    global new_font,my_font
    
    root=Tk()
    #getting screen width and height of display
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    
    #setting tkinter window size
    root.geometry("%dx%d" % (width, height))
    root.config(bg="black")
    
    #setup stuff goes here
    root.title("BMI Calculator")
    
    #tk.Tk.__init__(root)
    root.withdraw()

    #ssplash(root)
    splash=Splash(root)
    
    ## simulate a delay while loading
    time.sleep(3)

    ## finished loading so destroy splash
    splash.destroy()
    
    # show window again
    root.deiconify()
    
    #background image
    im = Image.open('main.png')
    im = im.resize((width, height), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(im)
    tk.Label(root,image = tkimage).pack(pady=0)
    
    def calculate():
        global user
        user = Patient(name=(name_entry.get()),
                       gender=(gender_entry.get()),
                       age=(age_entry.get()),
                       weight=float(weight_entry.get()),
                       height=float(height_entry.get()))

        b=user.bmi_analysis()
        bmi_label.configure(text="Your BMI is " +
                                 str(round(user.calculate_bmi(), 2))
                                 + " which is "
                                 + b[0] + ".",)
        #bmi label
        bmi_label.pack()
        bmi_label.place(x=500,y=400) #grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        #Diet and Exercise Buttons
        if (b[1]=='severly_underweight'):
            btn_1=tk.Button(text="Diet and Exercise",command=severly_underweight,font=new_font,borderwidth=20)
        elif (b[1]=='underweight'):
            btn_1=tk.Button(text="Diet and Exercise",command=underweight,font=new_font,borderwidth=20,)
        elif (b[1]=='healthy'):
            btn_1=tk.Button(text="Diet and Exercise",command=healthy,font=new_font,borderwidth=20,)
        elif (b[1]=='overweight'):
            btn_1=tk.Button(text="Diet and Exercise",command=overweight,font=new_font,borderwidth=20)
        else:
            btn_1=tk.Button(text="Diet and Exercise",command=obese,font=new_font,borderwidth=20,)
        btn_1.place(x=800,y=600)
        btn_1.config(width=15,relief=RAISED,compound=tk.CENTER,bg="white",activeforeground="purple",activebackground="white",borderwidth=15)
        
        #Generate Report Button
        report = tk.Button(text="Generate Report",command=report_func,font=new_font, width=15,relief=RAISED,compound=tk.CENTER,bg="white",activeforeground="green",activebackground="white",borderwidth=15)
        report.place(x=500,y=600)
        
 
    new_font=Font(weight="bold",size=20)
    my_font=Font(family="Times New Roman",size=25,weight="bold",slant="italic")
    label_font=Font(weight="bold",size=25)
    
    # declare labels
    name_label = tk.Label(text="Name",font=new_font,bg="black",fg="white")
    gender_label = tk.Label(text="Gender",font=new_font,bg="black",fg="white")
    age_label = tk.Label(text="Age",font=new_font,bg="black",fg="white")
    height_label = tk.Label(text="Height (m)",font=new_font,bg="black",fg="white")
    weight_label = tk.Label(text="Weight (Kg)",font=new_font,bg="black",fg="white")
    bmi_label = tk.Label(font=label_font,bg="black",fg="white")

    # declare entry boxes
    name_entry = tk.Entry(justify="left",font=new_font)
    gender_entry = tk.Entry(justify="left",font=new_font)
    age_entry = tk.Entry(justify="left",font=new_font)
    height_entry = tk.Entry(justify="right",font=new_font)
    weight_entry = tk.Entry(justify="right",font=new_font)

    # declare buttons
    calculate_button = tk.Button(text="Calculate", command=calculate,font=new_font, width=15,relief=RAISED,compound=tk.CENTER,bg="white",activeforeground="blue",activebackground="white",borderwidth=15)
    quit = tk.Button(text="Quit",command=root.destroy,font=new_font, width=15,relief=RAISED,compound=tk.CENTER,bg="white",activeforeground="red",activebackground="white",borderwidth=15)

    # place widgets on grid
    # name
    name_label.pack()
    name_label.place(x=500,y=100)   #grid(row=0, column=0, padx=10, pady=10)
    name_entry.pack()
    name_entry.place(x=700,y=100)   #grid(row=0, column=1, padx=10, pady=10)

    #gender
    gender_label.pack()
    gender_label.place(x=500,y=150) #grid(row=1, column=0, padx=10, pady=10)
    gender_entry.pack()
    gender_entry.place(x=700,y=150) #grid(row=1, column=1, padx=10, pady=10)

    #age
    age_label.pack()
    age_label.place(x=500,y=200) #grid(row=2, column=0, padx=10, pady=10)
    age_entry.pack()
    age_entry.place(x=700,y=200)  #grid(row=2, column=1, padx=10, pady=10)

    #height
    height_label.pack()
    height_label.place(x=500,y=250) #grid(row=3, column=0, padx=10, pady=10)
    height_entry.pack()
    height_entry.place(x=700,y=250) #grid(row=3, column=1, padx=10, pady=10)

    #weight
    weight_label.pack()
    weight_label.place(x=500,y=300) #grid(row=4, column=0, padx=10, pady=10)
    weight_entry.pack()
    weight_entry.place(x=700,y=300) #grid(row=4, column=1, padx=10, pady=10)

    #Calculate button
    calculate_button.pack()
    calculate_button.place(x=500,y=500) #grid(row=6, column=1, padx=10, pady=10)
    
    #Quit button
    quit.pack()
    quit.place(x=800,y=500)
    
    root.mainloop()

def report_func():
    global report_win
    report_win=Toplevel(root)
    report_win.geometry("%dx%d" % (width, height))
    report_win.title("Report")
    report_win.config(bg='black')
    
    user.generate_report()
    
    scrollbar = Scrollbar(report_win)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(report_win, yscrollcommand = scrollbar.set ,font=("Times",16),fg="white",bg="black")

    with open('TESTING','r') as file:
        lines = file.readlines()
        #xval=50
        #yval=50
        for l in lines:
            mylist.insert(END,l)
            #Label2 = Label(report_win,text=l,font=("Times",15),bg="black",fg="white")
            #Label2.place(x=xval,y=yval)
            #xval+=50
            #yval+=50
        mylist.pack( side = LEFT, fill = BOTH ,expand=True)
    report_win.mainloop()


#Severly Underweight 
def severly_underweight():
    global severly_underweight_win
    severly_underweight_win=Toplevel(root)
    severly_underweight_win.geometry("%dx%d" % (width, height))
    severly_underweight_win.title("Diet and Exercise")
    severly_underweight_win.config(bg='black')
    img1 = Image.open('exe_diet1.png')
    img1 = img1.resize((width, height), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(severly_underweight_win,image = tkimage1,bd=0)
    Label1.pack()
    Label2 = Label(severly_underweight_win,text="Severely Underweight",font=("Times",40),bg="black",fg="white")
    Label2.place(x=500,y=300)
    btn_exer = Button(severly_underweight_win, text='Exercise',font=new_font,command=exercise_su,fg="black",bg="white",borderwidth=30)
    btn_exer.pack()
    btn_exer.place(x=500,y=400)
    btn_diet = Button(severly_underweight_win, text='Diet',font=new_font,command=diet_su,fg="black",bg="white",borderwidth=30)      
    btn_diet.pack()
    btn_diet.place(x=800,y=400)
    severly_underweight_win.mainloop()

def exercise_su():
    global exercise_su_win
    exercise_su_win=Toplevel(severly_underweight_win)
    exercise_su_win.geometry("%dx%d" % (width, height))
    exercise_su_win.title("Exercise/Yogasana")
    exercise_su_win.config(bg='black')
    img1 = Image.open('given.png')
    img1 = img1.resize((900, 700), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(exercise_su_win,image = tkimage1,bd=0)
    Label1.pack()
    btn_back = Button(exercise_su_win, text='Back',font=new_font,command=exercise_su_win.destroy,fg="black",bg="white")      
    btn_back.pack()
    btn_back.place(x=1200,y=650)
    exercise_su_win.mainloop()

def diet_su():
    global diet_su_win
    diet_su_win=Toplevel(severly_underweight_win)
    diet_su_win.geometry("%dx%d" % (width, height))
    diet_su_win.title("Exercise/Yogasana")
    diet_su_win.config(bg='black')
    img1 = Image.open('SeverPD.png')
    #img1.save("SeverPD",quality=95)
    img1 = img1.resize((900, 700), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(diet_su_win,image = tkimage1,bd=0)
    Label1.pack()
    btn_back = Button(diet_su_win, text='Back',font=new_font,command=diet_su_win.destroy,fg="black",bg="white")      
    btn_back.pack()
    btn_back.place(x=1200,y=650)
    diet_su_win.mainloop()


#Underweight
def underweight():      
    global underweight_win
    underweight_win=Toplevel(root)
    underweight_win.geometry("%dx%d" % (width, height))
    underweight_win.title("Diet and Exercise")
    underweight_win.config(bg="black")
    img1 = Image.open('exe_diet2.png')
    img1 = img1.resize((width, height), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(underweight_win,image = tkimage1,bd=0)
    Label1.pack()
    Label2 = Label(underweight_win,text="Underweight",font=("Times",40),bg="black",fg="white")
    Label2.place(x=600,y=200)
    btn_exer = Button(underweight_win, text='Exercise',font=new_font,command=exercise_u,fg="black",bg="white",borderwidth=25)
    btn_exer.pack()
    btn_exer.place(x=600,y=300)
    btn_diet = Button(underweight_win, text='Diet',font=new_font,command=diet_u,fg="black",bg="white",borderwidth=25)      
    btn_diet.pack()
    btn_diet.place(x=850,y=300)
    underweight_win.mainloop()

def exercise_u():
    global exercise_u_win
    exercise_u_win=Toplevel(underweight_win)
    exercise_u_win.geometry("%dx%d" % (width, height))
    exercise_u_win.title("Exercise/Yogasana")
    exercise_u_win.config(bg='black')
    img1 = Image.open('rutuja.png')
    img1 = img1.resize((900, 700), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(exercise_u_win,image = tkimage1,bd=0)
    Label1.pack()
    btn_back = Button(exercise_u_win, text='Back',font=new_font,command=exercise_u_win.destroy,fg="black",bg="white")      
    btn_back.pack()
    btn_back.place(x=1200,y=650)
    exercise_u_win.mainloop()

def diet_u():
    global diet_u_win
    diet_u_win=Toplevel(underweight_win)
    diet_u_win.geometry("%dx%d" % (width, height))
    diet_u_win.title("Diet")
    diet_u_win.config(bg='black')
    img1 = Image.open('UnderweightPD.png')
    img1 = img1.resize((900, 700), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(diet_u_win,image = tkimage1,bd=0)
    Label1.pack()
    btn_back = Button(diet_u_win, text='Back',font=new_font,command=diet_u_win.destroy,fg="black",bg="white")      
    btn_back.pack()
    btn_back.place(x=1200,y=650)
    diet_u_win.mainloop()


#Healthy
def healthy():   
    global healthy_win
    healthy_win=Toplevel(root)
    healthy_win.geometry("%dx%d" % (width, height))
    healthy_win.title("Diet and Exercise")
    img1 = Image.open('exe_diet3.png')
    img1 = img1.resize((width, height), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(healthy_win,image = tkimage1,bd=0)
    Label1.pack()
    Label2 = Label(healthy_win,text="Healthy",font=("Times",40),bg="black",fg="white")
    Label2.place(x=500,y=300)
    btn_exer = Button(healthy_win, text='Exercise',font=new_font,command=exercise_h,fg="black",bg="white",borderwidth=30,)
    btn_exer.pack()
    btn_exer.place(x=500,y=400)
    btn_diet = Button(healthy_win, text='Diet',font=new_font,command=diet_h,fg="black",bg="white",borderwidth=30)      
    btn_diet.pack()
    btn_diet.place(x=800,y=400)
    healthy_win.mainloop()

def exercise_h():
    global exercise_h_win
    exercise_h_win=Toplevel(healthy_win)
    exercise_h_win.geometry("%dx%d" % (width, height))
    exercise_h_win.title("Exercise/Yogasana")
    exercise_h_win.config(bg='black')
    img1 = Image.open('new1.png')
    img1 = img1.resize((900,700), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(exercise_h_win,image = tkimage1,bd=0)
    Label1.pack()
    btn_back = Button(exercise_h_win, text='Back',font=new_font,command=exercise_h_win.destroy,fg="black",bg="white")      
    btn_back.pack()
    btn_back.place(x=1200,y=650)
    exercise_h_win.mainloop()

def diet_h():
    global diet_h_win
    diet_h_win=Toplevel(healthy_win)
    diet_h_win.geometry("%dx%d" % (width, height))
    diet_h_win.title("Diet")
    diet_h_win.config(bg='black')
    img1 = Image.open('NewNormPD.png')
    img1 = img1.resize((900, 700), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(diet_h_win,image = tkimage1,bd=0)
    Label1.pack()
    btn_back = Button(diet_h_win, text='Back',font=new_font,command=diet_h_win.destroy,fg="black",bg="white")      
    btn_back.pack()
    btn_back.place(x=1000,y=650)
    diet_h_win.mainloop()


#Overweight
def overweight(): 
    global overweight_win
    overweight_win=Toplevel(root)
    overweight_win.geometry("%dx%d" % (width, height))
    overweight_win.title("Diet and Exercise")
    img1 = Image.open('exe_diet4.png')
    img1 = img1.resize((width, height), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(overweight_win,image = tkimage1,bd=0)
    Label1.pack()
    Label2 = Label(overweight_win,text="Overweight",font=("Times",40),bg="black",fg="white")
    Label2.place(x=100,y=200)
    btn_exer = Button(overweight_win, text='Exercise',font=new_font,command=exercise_o,fg="black",bg="white",borderwidth=25)
    btn_exer.pack()
    btn_exer.place(x=100,y=300)
    btn_diet = Button(overweight_win, text='Diet',font=new_font,command=diet_o,fg="black",bg="white",borderwidth=25)      
    btn_diet.pack()
    btn_diet.place(x=400,y=300)
    overweight_win.mainloop()

def exercise_o():
    global exercise_o_win
    exercise_o_win=Toplevel(overweight_win)
    exercise_o_win.geometry("%dx%d" % (width, height))
    exercise_o_win.title("Exercise/Yogasana")
    exercise_o_win.config(bg='black')
    img1 = Image.open('workout1.png')
    img1 = img1.resize((900,700), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(exercise_o_win,image = tkimage1,bd=0)
    Label1.pack()
    btn_back = Button(exercise_o_win, text='Back',font=new_font,command=exercise_o_win.destroy,fg="black",bg="white")      
    btn_back.pack()
    btn_back.place(x=1200,y=650)
    exercise_o_win.mainloop()

def diet_o():
    global diet_o_win
    diet_o_win=Toplevel(overweight_win)
    diet_o_win.geometry("%dx%d" % (width, height))
    diet_o_win.title("Diet")
    diet_o_win.config(bg='black')
    img1 = Image.open('OverPD.png')
    img1 = img1.resize((900,700), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(diet_o_win,image = tkimage1,bd=0)
    Label1.pack()
    btn_back = Button(diet_o_win, text='Back',font=new_font,command=diet_o_win.destroy,fg="black",bg="white")      
    btn_back.pack()
    btn_back.place(x=1200,y=650)
    diet_o_win.mainloop()


#Obese
def obese():
    global obese_win
    obese_win=Toplevel(root)
    obese_win.geometry("%dx%d" % (width, height))
    obese_win.title("Diet and Exercise")
    img1 = Image.open('exe_diet5.png')
    img1 = img1.resize((width, height), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(obese_win,image = tkimage1,bd=0)
    Label1.pack()
    Label2 = Label(obese_win,text="Obese",font=("Times",50),bg="black",fg="white")
    Label2.place(x=500,y=300)
    btn_exer = Button(obese_win, text='Exercise',font=new_font,command=exercise_ob,fg="black",bg="white",borderwidth=25)
    btn_exer.pack()
    btn_exer.place(x=400,y=400)
    btn_diet = Button(obese_win, text='Diet',font=new_font,command=diet_ob,fg="black",bg="white",borderwidth=25)      
    btn_diet.pack()
    btn_diet.place(x=700,y=400)
    obese_win.mainloop()

def exercise_ob():
    global exercise_ob_win
    exercise_ob_win=Toplevel(obese_win)
    exercise_ob_win.geometry("%dx%d" % (width, height))
    exercise_ob_win.title("Exercise/Yogasana")
    exercise_ob_win.config(bg='black')
    img1 = Image.open('vaishali.png')
    img1 = img1.resize((900,700), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(exercise_ob_win,image = tkimage1,bd=0)
    Label1.pack()
    btn_back = Button(exercise_ob_win, text='Back',font=new_font,command=exercise_ob_win.destroy,fg="black",bg="white")      
    btn_back.pack()
    btn_back.place(x=1200,y=650)
    exercise_ob_win.mainloop()

def diet_ob():
    global diet_ob_win
    diet_ob_win=Toplevel(obese_win)
    diet_ob_win.geometry("%dx%d" % (width, height))
    diet_ob_win.title("Diet")
    diet_ob_win.config(bg='black')
    img1 = Image.open('obesePD.png')
    img1 = img1.resize((900,700), Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(img1)
    Label1 = Label(diet_ob_win,image = tkimage1,bd=0)
    Label1.pack()
    btn_back = Button(diet_ob_win, text='Back',font=new_font,command=diet_ob_win.destroy,fg="black",bg="white")      
    btn_back.pack()
    btn_back.place(x=1200,y=650)
    diet_ob_win.mainloop()
    
    
if __name__ == "__main__":
    main()