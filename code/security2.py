from tkinter import *
import MySQLdb
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

def show_frame(frame):
    frame.tkraise()

def search_row(user_name,password):
  
    connection=MySQLdb.connect(host='localhost',database='pythonlab', user='root',password='Mac2000@')
    cursor = connection.cursor()
    
    str="select * from data2 where user_name = '%s'"
    args=(user_name)
    args2 = (user_name,password)

    try:
        cursor.execute(str % args)
        row=cursor.fetchone()
        if row is None:
            return 0
        elif row[1] == args2[1] :
            return row[2]
        else:
            return 2
    
    except (Exception) as error :
        connection.rollback()
        print ("Error while using MySQL table", error)
    
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            
            
def insert_rows(user_name,password):
    
    connection=MySQLdb.connect(host='localhost',database='pythonlab', user='root',password='Mac2000@')

    cursor = connection.cursor()
    str="insert into data2(user_name,password) values('%s', '%s')"
    args=(user_name,password)

    
    try:
        cursor.execute(str % args)
        connection.commit()
        print("1 row inserted.. ")

    except (Exception) as error :
        connection.rollback()
        print ("Error while using MySQL table", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")  
                


class Login:
    
    def __init__(self,root):
        self.root = root
        self.root.title("RDBMS IA2")
        self.root.geometry("1199x600+100+100")
#         self.root.configure(bg = "tan1" )
        
        #=======================Login Frame=====================================================================
        my_frame = Frame(self.root,bg = "white")
        my_frame.place(height = 600, width = 1199)
        
        
        self.bg = ImageTk.PhotoImage(file = "rdbms_bg1.jpg")
        self.bg_image = Label(my_frame,image= self.bg).place(x=0,y=0,relwidth = 1,relheight = 1)
        Frame_login = Frame(my_frame,bg = "white")
        Frame_login.place(height = 375, width = 500,x = 150,y = 150)
        
        title = Label(Frame_login, text = "Login Here", font = ("Impact", 35, "bold"), fg = "#d77337", bg = "white" 
                 ).place(x = 90, y = 30)
        desc = Label(Frame_login, text = "legitimate user login", font = ("Goudy old style",15 ,"bold"), 
                     fg = "#d77337", bg = "white" ).place(x = 90, y = 100)
        
        username = Label(Frame_login,text = "Username", font = ("Goudy old style", 15, "bold"), fg = "gray", bg = "white", 
                        ).place(x=90, y=140)
        
        self.txt_userlogin = Entry(Frame_login, font = ("Times new roman",15),bg = "lightgray")
        self.txt_userlogin.place(x = 90, y = 170, height = 35 , width = 300)
        
        
        password = Label(Frame_login,text = "Password", font = ("Goudy old style", 15, "bold"), fg = "gray", bg = "white", 
                        ).place(x=90, y=210)
        self.txt_passlogin = Entry(Frame_login, font = ("Times new roman",15),bg = "lightgray")
        self.txt_passlogin.place(x = 90, y = 240, height = 35 , width = 300)
        
        signup_btn = Button(Frame_login, text = "Sign up?", fg = "#d77337", bg = "white" ,bd = 0,font = ("Times new roman",12),
                          command = lambda: show_frame(Frame_signup)).place(x = 90, y = 275)
        Login_btn = Button(Frame_login, text = "Login", bg = "#d77337", fg = "white" ,bd = 0,font = ("Times new roman",12),
                          command = self.login).place(x = 195, y = 320,height = 40,width = 150)
        
        
        
        #============================Sign up Frame================================================================
        
        
        Frame_signup = Frame(my_frame,bg = "white")
        Frame_signup.place(height = 375, width = 500,x = 150,y = 150)
    
        title = Label(Frame_signup, text = "Sign up here", font = ("Impact", 35, "bold"), fg = "#d77337", bg = "white" 
                 ).place(x = 90, y = 30)
        desc = Label(Frame_signup, text = "legitimate user sign up", font = ("Goudy old style",15 ,"bold"), 
                     fg = "#d77337", bg = "white" ).place(x = 90, y = 100)
        
        username = Label(Frame_signup,text = "Username", font = ("Goudy old style", 15, "bold"), fg = "gray", bg = "white", 
                        ).place(x=90, y=140)
        
        self.txt_usersignup = Entry(Frame_signup, font = ("Times new roman",15),bg = "lightgray")
        self.txt_usersignup.place(x = 90, y = 170, height = 35 , width = 300)
        
        
        password = Label(Frame_signup,text = "Password", font = ("Goudy old style", 15, "bold"), fg = "gray", bg = "white", 
                        ).place(x=90, y=210)
        self.txt_passsignup = Entry(Frame_signup, font = ("Times new roman",15),bg = "lightgray")
        self.txt_passsignup.place(x = 90, y = 240, height = 35 , width = 300)
        
        login_btn = Button(Frame_signup, text = "login?", fg = "#d77337", bg = "white" ,bd = 0,font = ("Times new roman",12),
                          command = lambda: show_frame(Frame_login)).place(x = 90, y = 275)
        signup_btn = Button(Frame_signup, text = "Sign up", bg = "#d77337", fg = "white" ,bd = 0,font = ("Times new roman",12),
                          command = self.signup).place(x = 195, y = 320,height = 40,width = 150)
        
        
        #============================Read only frame================================================================
        self.Frame_read = Frame(self.root,bg = "white")
        self.Frame_read.place(height = 600, width = 1199)
        
        titler = Label(self.Frame_read, text = "Read only view", font = ("Impact", 35, "bold"), fg = "#d77337", bg = "white" 
                 )
        
        text1 = Text(self.Frame_read,height = 30, width = 150,x = 10, y = 50)

        file1 = open('test_file.txt', 'r')
        Lines = file1.readlines()

        for line in Lines:
        #     print("{}".format(line.strip()))

            text1.config(state = "normal")
            text1.insert(INSERT,"{}\n".format(line.strip()))
            text1.config(state = "disabled")

        s=Scrollbar(self.Frame_read,orient=VERTICAL,command=text1.yview)
        
        #attach scroll bar to the text widget
        text1.configure(yscrollcommand=s.set)
        
        #attach the scroll bar to the root window
        s.pack(side=RIGHT,fill=Y)
        titler.pack()
        text1.pack()
        
        
          #============================write only frame================================================================
        self.Frame_write = Frame(self.root,bg = "white smoke")
        self.Frame_write.place(height = 600, width = 1199)
        
        titler = Label(self.Frame_write, text = "Write only view", font = ("Impact", 35, "bold"), fg = "#d77337",
                       bg = "white smoke" )
        
#         txtDisplay = Entry(self.Frame_write,font = ('arial',18,'bold'),bd = 10, width = 60,height = 60,
#                   bg = "gray", justify = RIGHT)
        self.my_text = Text(self.Frame_write, width = 60, height = 12,font = ('arial',18,'bold'),bg = "peach puff")
        
        
        clear_btn = Button(self.Frame_write, text = "clear", bg = "#d77337", fg = "white" ,bd = 0,font = ("Times new roman",12),
                          command = self.clear).place(x = 440, y = 510,height = 40,width = 150)
        add_btn = Button(self.Frame_write, text = "Add to file", bg = "#d77337", fg = "white" ,bd = 0,font = ("Times new roman",12),
                          command = self.get_text).place(x = 610, y = 510,height = 40,width = 150)
        
    
        titler.pack(pady = 25)
        self.my_text.pack(pady=20)
#         txtDisplay.pack()
        
        
        
        
          #============================Read and write frame================================================================
        
        
        self.Frame_both = Frame(self.root,bg = "white")
        self.Frame_both.place(height = 600, width = 1199)
        
        self.text2 = Text(self.Frame_both,height = 30, width = 150,x = 10, y = 50)

        file1 = open('test_file.txt', 'r')
        Lines = file1.readlines()

        for line in Lines:
        #     print("{}".format(line.strip()))
            self.text2.insert(INSERT,"{}\n".format(line.strip()))
        
        s=Scrollbar(self.Frame_both,orient=VERTICAL,command=self.text2.yview)
        
        #attach scroll bar to the text widget
        self.text2.configure(yscrollcommand=s.set)
        
        #attach the scroll bar to the root window
        s.pack(side=RIGHT,fill=Y)
        update_btn = Button(self.Frame_both, text = "Update", bg = "#d77337", fg = "white" ,bd = 0,font = ("Times new roman",12),
                          command = self.update,height = 2,width = 12) 
       
        
        self.text2.pack(pady = 10)
        update_btn.pack()
        show_frame(my_frame)
        

    def login(self):
        if self.txt_userlogin.get() == "" or self.txt_passlogin.get() == "":
            messagebox.showerror("Error","All fields are required",parent = self.root)
        else:
            result = search_row(self.txt_userlogin.get(),self.txt_passlogin.get())
            if result == 0:
                messagebox.showerror("Error","User doesn't exist",parent = self.root)
            elif result == "Student":
                messagebox.showinfo("Welcome",f"Welcome {self.txt_userlogin.get()}",parent = self.root)
                show_frame(self.Frame_read)
            elif result == "Assistant":
                messagebox.showinfo("Welcome",f"Welcome {self.txt_userlogin.get()}",parent = self.root)
                show_frame(self.Frame_write)
            elif result == "Teacher":
                messagebox.showinfo("Welcome",f"Welcome {self.txt_userlogin.get()}",parent = self.root)
                show_frame(self.Frame_both)
            else:
                messagebox.showwarning("Error","Wrong password",parent = self.root)
                
    def signup(self):
        username = self.txt_usersignup.get()
        password = self.txt_passsignup.get()
        lcase = ucase = ncase = charcase =flag = 0
        chars = ['@', '#', '$']
        for i in password:
            if i.islower():
                lcase = 1
        for j in password:
            if j.isupper():
                ucase = 1
        for k in password:
            if k.isdigit():
                ncase = 1
        for l in password:
            if l in chars:
                charcase = 1
        if (len(password) >= 8 and len(password) <= 15):
            if lcase == 1:
                if ucase == 1:
                    if ncase == 1:
                        if charcase == 1:
                            insert_rows(username,password)
                            messagebox.showinfo("Successful","User Registered",parent = self.root)
                            flag = 1
        if flag == 0:
            messagebox.showerror("Error","Password should contain one lowercase,\none uppercase,one number and one of ['@', '#', '$']")
        
        
    def clear(self):
        self.my_text.delete(1.0,END)
        
    def get_text(self):
        line = self.my_text.get(1.0,END)
        with open("test_file.txt","a+") as f:
            f.write("\n")
            for l in line:
                f.write(l)
            f.seek(0)
            self.clear()
            
    def update(self):
        line = self.text2.get(1.0,END)
        with open("test_file.txt","w") as f:
            f.write("\n")
            for l in line:
                f.write(l)
            f.seek(0)
            self.clear()
        
root = Tk()
obj = Login(root)
root.mainloop()