import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import date
import time
import mysql.connector
import string
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
import mysql.connector
import random
from datetime import datetime, timedelta
#admin-userlogin   done
#storebooks-books   done
#studentsdata-students,teachers  done

# Connection for admin database


class MainApp:
    def __init__(self, root):
        self.root = root
        self.var1 = "Admin Name"  # Initialize var1 with a default value or pass it as a parameter
        self.fm3 = tk.Frame(self.root)  # Initialize fm as a Frame
        # Initialize main frame
        self.init_main_frame()

    def init_main_frame(self):
        # Load and set the background image
        self.bg_image = Image.open(r"C:\Users\Admin\Downloads\Designer.png").resize((900, 500))  # Adjust path as necessary
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, height=500, width=900)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        # Create a semi-transparent overlay
        overlay_image = Image.new('RGBA', (900, 500), (0, 0, 0, 180))
        self.overlay = ImageTk.PhotoImage(overlay_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.overlay)

        # Enchanted opening quote
        self.enchanted_quote = tk.Label(self.canvas, text="Unlock the gates to the library of wonders, \nwhere 'The Hobbit' meets 'Harry Potter', and 'Pride and Prejudice' dances with 'The Great Gatsby'.\n Step through the portals of wisdom where 'Verity' uncovers truths, 'Percy Jackson' wields mythical powers,\n beckoning you to explore realms beyond imagination.", 
                                     fg='white', bg='black', font=('Arial', 10, 'italic'))
        self.enchanted_quote.place(x=60, y=60)

        # Let's Go Button
        self.lets_go_button = tk.Button(self.canvas, text="Let's Go", fg='black', bg='yellow', width=15, font=('Arial', 12, 'bold'),
                                     activebackground='black', activeforeground='yellow', command=self.show_dashboard, bd=3, relief='flat', cursor='hand2')
        self.lets_go_button.place(x=340, y=380)  # Adjusted x position slightly to the left

    def show_dashboard(self):
        # Hide elements not needed anymore
        self.lets_go_button.destroy()
        self.enchanted_quote.destroy()

        # Load and set the background image again
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        # User ID
        self.user_label = tk.Label(self.canvas, text='User ID', bg='black', font=('Arial', 12, 'bold'), fg='white')
        self.user_label.place(x=200, y=100)

        self.user_entry = tk.Entry(self.canvas, width=22, font=('Arial', 12, 'bold'), bd=4, relief='groove')
        self.user_entry.place(x=320, y=100)

        # Password
        self.password_label = tk.Label(self.canvas, text='Password', bg='black', font=('Arial', 12, 'bold'), fg='white')
        self.password_label.place(x=200, y=150)

        self.password_entry = tk.Entry(self.canvas, width=22, show='*', font=('Arial', 12, 'bold'), bd=4, relief='groove')
        self.password_entry.place(x=320, y=150)

        # Login Button
        self.login_button = tk.Button(self.canvas, text='Login', fg='black', bg='yellow', width=10, font=('Arial', 12, 'bold'),
                                   activebackground='black', activeforeground='yellow', command=self.process_login, bd=3, relief='flat', cursor='hand2')
        self.login_button.place(x=220, y=250)

        # Clear Button
        self.clear_button = tk.Button(self.canvas, text='Clear', fg='black', bg='yellow', width=10, font=('Arial', 12, 'bold'),
                                   activebackground='black', activeforeground='yellow', bd=3, relief='flat', cursor='hand2',
                                   command=self.clear_entries)
        self.clear_button.place(x=360, y=250)

        # Right Side Image (250x400)
        self.right_image = Image.open(r"C:\Users\Admin\Downloads\right.png").resize((250, 400))  # Adjust path and size as necessary
        self.right_image = ImageTk.PhotoImage(self.right_image)
        self.right_image_label = tk.Label(self.canvas, image=self.right_image, bg='white')
        self.right_image_label.image = self.right_image
        self.right_image_label.place(x=600, y=50)

        # User Type (Radio Buttons)
        self.user_type_var = tk.StringVar()
        self.user_type_label = tk.Label(self.canvas, text='User Type', bg='black', font=('Arial', 12, 'bold'), fg='white')
        self.user_type_label.place(x=180, y=200)

        self.user_type_student = tk.Radiobutton(self.canvas, text='Student', variable=self.user_type_var, value='Student',
                                             bg='grey33', fg='white', font=('Arial', 12, 'bold'),
                                             activebackground='black', activeforeground='white',
                                             selectcolor='purple1')
        self.user_type_student.place(x=300, y=200)

        self.user_type_teacher = tk.Radiobutton(self.canvas, text='Teacher', variable=self.user_type_var, value='Teacher',
                                             bg='grey33', fg='white', font=('Arial', 12, 'bold'),
                                             activebackground='black', activeforeground='white',
                                             selectcolor='purple1')
        self.user_type_teacher.place(x=400, y=200)
        
        self.user_type_admin = tk.Radiobutton(self.canvas, text='Admin', variable=self.user_type_var, value='Admin',
                                           bg='grey33', fg='white', font=('Arial', 12, 'bold'),
                                           activebackground='black', activeforeground='white',
                                           selectcolor='purple1')
        self.user_type_admin.place(x=500, y=200)

        # Sign Up Button
        self.btn3 = tk.Button(self.canvas, text='Sign Up', fg='black', bg='yellow', width=10, font=('Arial', 12, 'bold'),
                           activebackground='black', activeforeground='yellow', bd=3, relief='flat', cursor='hand2',
                           command=self.signup)
        self.btn3.place(x=220, y=300)

        # Donation Button
        self.btn4 = tk.Button(self.canvas, text='Donation', fg='black', bg='yellow', width=10, font=('Arial', 12, 'bold'),
                           activebackground='black', activeforeground='yellow', bd=3, relief='flat', cursor='hand2',
                           command=self.donation)
        self.btn4.place(x=360, y=300)

        # Forgot Password Button
        self.forgot_password_button = tk.Button(self.canvas, text='Forgot Password', fg='black', bg='orchid1', width=15, font=('Arial', 10, 'bold'),
                                             activebackground='purple', activeforeground='yellow', bd=3, relief='flat', cursor='hand2',
                                             command=self.forgot_password)
        self.forgot_password_button.place(x=320, y=350)



    def show_dialog(self, title):
        pass




    def signup(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign Up")
        signup_window.geometry("400x400")  # Set the sign-up window size to 400x400

        tk.Label(signup_window, text="UserID").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(signup_window, text="Password").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(signup_window, text="Type (Student/Teacher/Admin)").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(signup_window, text="Name").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(signup_window, text="Roll No").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(signup_window, text="Email").grid(row=5, column=0, padx=10, pady=10)
        tk.Label(signup_window, text="Contact No").grid(row=6, column=0, padx=10, pady=10)

        user_id_entry = tk.Entry(signup_window)
        password_entry = tk.Entry(signup_window, show='*')
        type_entry = tk.Entry(signup_window)
        name_entry = tk.Entry(signup_window)
        rollno_entry = tk.Entry(signup_window)
        email_entry = tk.Entry(signup_window)
        contactno_entry = tk.Entry(signup_window)

        user_id_entry.grid(row=0, column=1, padx=10, pady=10)
        password_entry.grid(row=1, column=1, padx=10, pady=10)
        type_entry.grid(row=2, column=1, padx=10, pady=10)
        name_entry.grid(row=3, column=1, padx=10, pady=10)
        rollno_entry.grid(row=4, column=1, padx=10, pady=10)
        email_entry.grid(row=5, column=1, padx=10, pady=10)
        contactno_entry.grid(row=6, column=1, padx=10, pady=10)

        def generate_id():
            return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        def add_user_to_db():
            user_id = user_id_entry.get()
            password = password_entry.get()
            user_type = type_entry.get().capitalize()
            name = name_entry.get()
            roll_no = rollno_entry.get()
            email = email_entry.get()
            contact_no = contactno_entry.get()

            if not (user_id and password and user_type and name and roll_no and email and contact_no):
                messagebox.showerror("Error", "All fields are required!")
                return

            if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
                messagebox.showerror("Error", "Password must include both numbers and letters!")
                return

            if user_type not in ["Student", "Teacher", "Admin"]:
                messagebox.showerror("Error", "Type must be Student, Teacher, or Admin!")
                return

            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="welcome123", database="admin")
                cursor = conn.cursor()

                cursor.execute("INSERT INTO userlogin (UserID, Password, Type) VALUES (%s, %s, %s)", 
                               (user_id, password, user_type))
                conn.commit()
                cursor.close()
                conn.close()

                stud_id = tea_id = None
                studentsdata_conn = mysql.connector.connect(host="localhost", user="root", password="welcome123", database="studentsdata")
                studentsdata_cursor = studentsdata_conn.cursor()

                if user_type == "Student":
                    stud_id = generate_id()
                    studentsdata_cursor.execute("INSERT INTO students (stud_id, Name, RollNo, Email, ContactNo) VALUES (%s, %s, %s, %s, %s)", 
                                                (stud_id, name, roll_no, email, contact_no))
                elif user_type == "Teacher":
                    tea_id = generate_id()
                    studentsdata_cursor.execute("INSERT INTO teachers (tea_id, Name, Email, Contact) VALUES (%s, %s, %s, %s)", 
                                                (tea_id, name, email, contact_no))

                studentsdata_conn.commit()
                studentsdata_cursor.close()
                studentsdata_conn.close()

                messagebox.showinfo("Success", f"{user_type} signed up successfully! ID: {stud_id or tea_id}")

            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

        signup_button = tk.Button(signup_window, text="Sign Up", command=add_user_to_db)
        signup_button.grid(row=7, columnspan=2, pady=10)



                

        
        # Donation Button
        self.btn4 = tk.Button(self.canvas, text='Donation', fg='black', bg='yellow', width=10, font=('Arial', 12, 'bold'),
                           activebackground='black', activeforeground='yellow', bd=3, relief='flat', cursor='hand2',
                           command=self.donation)
        self.btn4.place(x=360, y=300)

        # Forgot Password Button
        self.forgot_password_button = tk.Button(self.canvas, text='Forgot Password', fg='black', bg='orchid1', width=15, font=('Arial', 10, 'bold'),
                                             activebackground='purple', activeforeground='yellow', bd=3, relief='flat', cursor='hand2',
                                             command=self.forgot_password)
        self.forgot_password_button.place(x=320, y=350)

        # Add sign up button
        self.signup_button = tk.Button(root, text="Sign Up", command=self.signup)
        self.signup_button.pack(pady=20)

        # Add forgot password button
        self.forgot_password_button = tk.Button(root, text="Forgot Password", command=self.forgot_password)
        self.forgot_password_button.pack(pady=20)

    def signup(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign Up")
        signup_window.geometry("500x500")  # Set the sign-up window size to 500x500

        tk.Label(signup_window, text="UserID").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(signup_window, text="Password").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(signup_window, text="Type (Student/Teacher/Admin)").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(signup_window, text="Name").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(signup_window, text="Roll No").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(signup_window, text="Email").grid(row=5, column=0, padx=10, pady=10)
        tk.Label(signup_window, text="Contact No").grid(row=6, column=0, padx=10, pady=10)

        user_id_entry = tk.Entry(signup_window)
        password_entry = tk.Entry(signup_window, show='*')
        type_entry = tk.Entry(signup_window)
        name_entry = tk.Entry(signup_window)
        rollno_entry = tk.Entry(signup_window)
        email_entry = tk.Entry(signup_window)
        contactno_entry = tk.Entry(signup_window)

        user_id_entry.grid(row=0, column=1, padx=10, pady=10)
        password_entry.grid(row=1, column=1, padx=10, pady=10)
        type_entry.grid(row=2, column=1, padx=10, pady=10)
        name_entry.grid(row=3, column=1, padx=10, pady=10)
        rollno_entry.grid(row=4, column=1, padx=10, pady=10)
        email_entry.grid(row=5, column=1, padx=10, pady=10)
        contactno_entry.grid(row=6, column=1, padx=10, pady=10)

        def generate_id():
            return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        def add_user_to_db():
            user_id = user_id_entry.get()
            password = password_entry.get()
            user_type = type_entry.get().capitalize()
            name = name_entry.get()
            roll_no = rollno_entry.get()
            email = email_entry.get()
            contact_no = contactno_entry.get()

            if not (user_id and password and user_type and name and roll_no and email and contact_no):
                messagebox.showerror("Error", "All fields are required!")
                return

            if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
                messagebox.showerror("Error", "Password must include both numbers and letters!")
                return

            if user_type not in ["Student", "Teacher", "Admin"]:
                messagebox.showerror("Error", "Type must be Student, Teacher, or Admin!")
                return

            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="welcome123", database="admin")
                cursor = conn.cursor()

                cursor.execute("INSERT INTO userlogin (UserID, Password, Type) VALUES (%s, %s, %s)", 
                               (user_id, password, user_type))
                conn.commit()
                cursor.close()
                conn.close()

                stud_id = tea_id = None
                studentsdata_conn = mysql.connector.connect(host="localhost", user="root", password="welcome123", database="studentsdata")
                studentsdata_cursor = studentsdata_conn.cursor()

                if user_type == "Student":
                    stud_id = generate_id()
                    studentsdata_cursor.execute("INSERT INTO students (stud_id, Name, RollNo, Email, ContactNo) VALUES (%s, %s, %s, %s, %s)", 
                                                (stud_id, name, roll_no, email, contact_no))
                elif user_type == "Teacher":
                    tea_id = generate_id()
                    studentsdata_cursor.execute("INSERT INTO teachers (tea_id, Name, Email, Contact) VALUES (%s, %s, %s, %s)", 
                                                (tea_id, name, email, contact_no))

                studentsdata_conn.commit()
                studentsdata_cursor.close()
                studentsdata_conn.close()

                messagebox.showinfo("Success", f"{user_type} signed up successfully! ID: {stud_id or tea_id}")

            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

        signup_button = tk.Button(signup_window, text="Sign Up", command=add_user_to_db)
        signup_button.grid(row=7, columnspan=2, pady=10)

    def clear_entries(self):
        self.user_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)


    def donation(self):
        self.show_dialog("Donation")

    def forgot_password(self):
        self.show_dialog("Forgot Password")

    def show_dialog(self, title):
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("300x200")
        dialog.resizable(0, 0)

        tk.Label(dialog, text=title, font=("Arial", 14)).pack(pady=20)
        tk.Button(dialog, text="Close", command=dialog.destroy, font=("Arial", 12)).pack(pady=10)

    def process_login(self):
        user_type = self.user_type_var.get()
        user_id = self.user_entry.get()
        password = self.password_entry.get()
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="welcome123",
                database="admin"
            )
            cursor = mydb.cursor()

            if user_type == "Student":
                cursor.execute("SELECT * FROM userlogin WHERE UserID=%s AND Password=%s AND Type='Student'", (user_id, password))
            else:
                cursor.execute("SELECT * FROM userlogin WHERE UserID=%s AND Password=%s AND Type='Teacher'", (user_id, password))

            result = cursor.fetchone()
            if result!=None:

                self.var1 = user_id  # Set var1 to the logged-in user's ID

                self.under_fm=tk.Frame(root,height=500,width=900,bg='#fff')
                self.under_fm.place(x=0,y=0)
            
                self.fm2=tk.Frame(root,bg='#012727',height=80,width=900)
                self.fm2.place(x=0,y=0)
            
                self.lbb=tk.Label(self.fm2,bg='#012727')
                self.lbb.place(x=15,y=5)            
    # Set up student dashboard
                self.dashboard_label = tk.Label(self.canvas, text=f"Welcome, {self.var1}!", bg='black', fg='white',
                                                font=('Arial', 16, 'bold'))
                self.dashboard_label.place(x=200, y=100)
                self.lb3=tk.Label(self.fm2,text='DASHBOARD',fg='White',bg='#012727',font=('times new roman',30,'bold'))
                self.lb3.place(x=325,y=17)
            
            #Name of the logged in admin
                #self.name=tk.Label(root,text="Name :{user_id}",bg='#fff',fg="black",font=('Calibri',12,'bold'))
                #self.name.place(x=5,y=83)
                #self.name1=tk.Label(root,text=self.ab[0],fg='black',bg='#fff',font=('Calibri',12,'bold'))
                #self.name1.place(x=60,y=83)
            
            #Display Date
                self.today=date.today()
                self.dat=tk.Label(root,text='Date : ',bg='#fff',fg='black',font=('Calibri',12,'bold'))
                self.dat.place(x=750,y=83)
                self.dat2 = tk.Label(root, text=self.today, bg='#fff', fg='black', font=('Calibri', 12, 'bold'))
                self.dat2.place(x=800, y=83)
            
            #For Head part

 
            else:
                messagebox.showerror('Library System', 'Your ID or Password is invalid!')


            if result:
                self.var1 = user_id  # Set var1 to the logged-in user's ID
                self.dashboard(user_type)
            else:
                messagebox.showerror('Library System', 'Your ID or Password is invalid!')

        except mysql.connector.Error as err:
            messagebox.showerror('Library System', f"Error: {err}")

        finally:
            if mydb.is_connected():
                cursor.close()
                mydb.close()

    def dashboard(self, user_type):
        if user_type == "Student":
            self.show_student_dashboard()
        elif user_type == "Teacher":
            self.show_teacher_dashboard()
        elif user_type == "Admin":
            self.show_admin_dashboard()

    def show_student_dashboard(self):
    # Clear previous elements
        self.user_label.destroy()
        self.user_entry.destroy()
        self.password_label.destroy()
        self.password_entry.destroy()
        self.login_button.destroy()
        self.clear_button.destroy()
        self.right_image_label.destroy()
        self.user_type_label.destroy()
        self.user_type_student.destroy()
        self.user_type_teacher.destroy()
        self.user_type_admin.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.forgot_password_button.destroy()

        self.fm3 = tk.Frame(self.root, bg='#fff', width=900, height=390)
        self.fm3.place(x=0, y=110)
  
    # Example of student dashboard elements
    # Replace with actual student dashboard elements as need
        


        # Clock Widget
        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))
            if int(h) >=12 and int(m) >=0:
                    self.lb7_hr.config(text="PM")

            #if int(h) > 12:
                    #h = str(int(h) // 12)
            self.lb1_hr.config(text=h)
            self.lb3_hr.config(text=m)
            self.lb5_hr.config(text=s)
            self.lb1_hr.after(200, clock)

        # Clock Widgets Placement
        self.lb1_hr = tk.Label(self.fm3, text='12', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb1_hr.place(x=607, y=0, width=60, height=30)

        self.lb3_hr = tk.Label(self.fm3, text='05', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb3_hr.place(x=677, y=0, width=60, height=30)

        self.lb5_hr = tk.Label(self.fm3, text='37', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb5_hr.place(x=747, y=0, width=60, height=30)

        self.lb7_hr = tk.Label(self.fm3, text='AM', font=('times new roman', 17, 'bold'), bg='#581845', fg='white')
        self.lb7_hr.place(x=817, y=0, width=60, height=30)

        # Clock
        clock() 



    # Right Side Image (250x400


        self.canvas8 = tk.Canvas(self.fm3, bg='black', width=400, height=300)
        self.canvas8.place(x=475, y=40)
        image_path = r"C:\Users\Admin\Downloads\stud.png"  # Adjust path as necessary
        self.photo9 = tk.PhotoImage(file=image_path)
        self.canvas8.create_image(0, 0, image=self.photo9, anchor="nw")

    # Developer Info
        self.develop = tk.Label(self.fm3, text='Developed By-JK x AH', bg='#fff', fg='#d7837f',
                             font=('Candara', 12, 'bold'))
        self.develop.place(x=732, y=350)
        button_config = {
            'fg': '#fff',
            'bg': '#581845',
            'font': ('Candara', 15, 'bold'),
            'width': 15,
            'bd': 7,
            'relief': 'flat',
            'cursor': 'hand2',
            'activebackground': 'black',
            'activeforeground': '#581845'
        }

    # Buttons
    # Add Book Button
        self.bt1 = tk.Button(self.fm3, text=' Add Books', command=self.addbook, **button_config)
        self.bt1.place(x=40, y=40)

    # Issue Book Button
        self.bt2 = tk.Button(self.fm3, text='  Issue Books', command=self.issuebook, **button_config)
        self.bt2.place(x=250, y=40)

    # Edit Book Button
        self.bt3 = tk.Button(self.fm3, text='  Edit Books', command=self.edit, **button_config)
        self.bt3.place(x=40, y=120)

    # Return Book Button
        self.bt4 = tk.Button(self.fm3, text='  Return Books', command=self.returnbook, **button_config)
        self.bt4.place(x=250, y=120)

    # Delete Book Button
        self.bt5 = tk.Button(self.fm3, text=' Delete Books', command=self.delete, **button_config)
        self.bt5.place(x=40, y=200)

    # Show Book Button
        self.bt6 = tk.Button(self.fm3, text=' Show Books', command=self.show, **button_config)
        self.bt6.place(x=250, y=280)

    # Search Book Button
        self.bt7 = tk.Button(self.fm3, text='  Search Books', command=self.search, **button_config)
        self.bt7.place(x=250, y=200)

    # Log Out Button
        self.bt8 = tk.Button(self.fm3, text='  Log Out', command=self.logout, **button_config)
        self.bt8.place(x=40, y=280)    



    # Add your additional buttons or functionality here as needed

    # Example placeholders for additional buttons:
    # self.btn9 = Button(self.fm3, text='Button 9', fg='#fff', bg='#581845', font=('Candara', 15, 'bold'), width=170,
    #                   height=0, bd=7, relief='flat', cursor='hand2', command=self.function9, activebackground='black',
    #                   activeforeground='#581845')
    # self.btn9.place(x=40, y=360)

    # self.btn10 = Button(self.fm3, text='Button 10', fg='#fff', bg='#581845', font=('Candara', 15, 'bold'), width=170,
    #                    height=0, bd=7, relief='flat', cursor='hand2', command=self.function10, activebackground='black',
    #                    activeforeground='#581845')
    # self.btn10.place(x=250, y=360)
    
    def show_teacher_dashboard(self):
    # Clear previous elements
        self.user_label.destroy()
        self.user_entry.destroy()
        self.password_label.destroy()
        self.password_entry.destroy()
        self.login_button.destroy()
        self.clear_button.destroy()
        self.right_image_label.destroy()
        self.user_type_label.destroy()
        self.user_type_student.destroy()
        self.user_type_teacher.destroy()
        self.user_type_admin.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.forgot_password_button.destroy()

        self.fm3 = tk.Frame(self.root, bg='#fff', width=900, height=390)
        self.fm3.place(x=0, y=110)
  
    # Example of student dashboard elements
    # Replace with actual student dashboard elements as need
        


        # Clock Widget
        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))
            if int(h) >=12 and int(m) >=0:
                    self.lb7_hr.config(text="PM")

            #if int(h) > 12:
                    #h = str(int(h) // 12)
            self.lb1_hr.config(text=h)
            self.lb3_hr.config(text=m)
            self.lb5_hr.config(text=s)
            self.lb1_hr.after(200, clock)

        # Clock Widgets Placement
        self.lb1_hr = tk.Label(self.fm3, text='12', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb1_hr.place(x=607, y=0, width=60, height=30)

        self.lb3_hr = tk.Label(self.fm3, text='05', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb3_hr.place(x=677, y=0, width=60, height=30)

        self.lb5_hr = tk.Label(self.fm3, text='37', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb5_hr.place(x=747, y=0, width=60, height=30)

        self.lb7_hr = tk.Label(self.fm3, text='AM', font=('times new roman', 17, 'bold'), bg='#581845', fg='white')
        self.lb7_hr.place(x=817, y=0, width=60, height=30)

        # Clock
        clock() 



    # Right Side Image (250x400


        self.canvas8 = tk.Canvas(self.fm3, bg='black', width=400, height=300)
        self.canvas8.place(x=475, y=40)
        image_path = r"C:\Users\Admin\Downloads\stud.png"  # Adjust path as necessary
        self.photo9 = tk.PhotoImage(file=image_path)
        self.canvas8.create_image(0, 0, image=self.photo9, anchor="nw")

    # Developer Info
        self.develop = tk.Label(self.fm3, text='Developed By-JK x AH', bg='#fff', fg='#d7837f',
                             font=('Candara', 12, 'bold'))
        self.develop.place(x=732, y=350)
        button_config = {
            'fg': '#fff',
            'bg': '#581845',
            'font': ('Candara', 15, 'bold'),
            'width': 15,
            'bd': 7,
            'relief': 'flat',
            'cursor': 'hand2',
            'activebackground': 'black',
            'activeforeground': '#581845'
        }

    # Buttons
    # Add Book Button
        self.bt1 = tk.Button(self.fm3, text=' Add Books', command=self.addbook, **button_config)
        self.bt1.place(x=40, y=40)

    # Issue Book Button
        self.bt2 = tk.Button(self.fm3, text='  Issue Books', command=self.issuebook, **button_config)
        self.bt2.place(x=250, y=40)

    # Edit Book Button
        self.bt3 = tk.Button(self.fm3, text='  Edit Books', command=self.edit, **button_config)
        self.bt3.place(x=40, y=120)

    # Return Book Button
        self.bt4 = tk.Button(self.fm3, text='  Return Books', command=self.returnbook, **button_config)
        self.bt4.place(x=250, y=120)

    # Delete Book Button
        self.bt5 = tk.Button(self.fm3, text=' Delete Books', command=self.delete, **button_config)
        self.bt5.place(x=40, y=200)

    # Show Book Button
        self.bt6 = tk.Button(self.fm3, text=' Show Books', command=self.show, **button_config)
        self.bt6.place(x=250, y=280)

    # Search Book Button
        self.bt7 = tk.Button(self.fm3, text='  Search Books', command=self.search, **button_config)
        self.bt7.place(x=250, y=200)

    # Log Out Button
        self.bt8 = tk.Button(self.fm3, text='  Log Out', command=self.logout, **button_config)
        self.bt8.place(x=40, y=280)    




    def show_admin_dashboard(self):
    # Clear previous elements
        self.user_label.destroy()
        self.user_entry.destroy()
        self.password_label.destroy()
        self.password_entry.destroy()
        self.login_button.destroy()
        self.clear_button.destroy()
        self.right_image_label.destroy()
        self.user_type_label.destroy()
        self.user_type_student.destroy()
        self.user_type_teacher.destroy()
        self.user_type_admin.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.forgot_password_button.destroy()

        self.fm3 = tk.Frame(self.root, bg='#fff', width=900, height=390)
        self.fm3.place(x=0, y=110)
  

        


        # Clock Widget
        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))
            if int(h) >=12 and int(m) >=0:
                    self.lb7_hr.config(text="PM")

            #if int(h) > 12:
                    #h = str(int(h) // 12)
            self.lb1_hr.config(text=h)
            self.lb3_hr.config(text=m)
            self.lb5_hr.config(text=s)
            self.lb1_hr.after(200, clock)

        # Clock Widgets Placement
        self.lb1_hr = tk.Label(self.fm3, text='12', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb1_hr.place(x=607, y=0, width=60, height=30)

        self.lb3_hr = tk.Label(self.fm3, text='05', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb3_hr.place(x=677, y=0, width=60, height=30)

        self.lb5_hr = tk.Label(self.fm3, text='37', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb5_hr.place(x=747, y=0, width=60, height=30)

        self.lb7_hr = tk.Label(self.fm3, text='AM', font=('times new roman', 17, 'bold'), bg='#581845', fg='white')
        self.lb7_hr.place(x=817, y=0, width=60, height=30)

        # Clock
        clock() 



    # Right Side Image (250x400


        self.canvas8 = tk.Canvas(self.fm3, bg='black', width=400, height=300)
        self.canvas8.place(x=475, y=40)
        image_path = r"C:\Users\Admin\Downloads\stud.png"  # Adjust path as necessary
        self.photo9 = tk.PhotoImage(file=image_path)
        self.canvas8.create_image(0, 0, image=self.photo9, anchor="nw")

    # Developer Info
        self.develop = tk.Label(self.fm3, text='Developed By-JK x AH', bg='#fff', fg='#d7837f',
                             font=('Candara', 12, 'bold'))
        self.develop.place(x=732, y=350)
        button_config = {
            'fg': '#fff',
            'bg': '#581845',
            'font': ('Candara', 15, 'bold'),
            'width': 15,
            'bd': 7,
            'relief': 'flat',
            'cursor': 'hand2',
            'activebackground': 'black',
            'activeforeground': '#581845'
        }

    # Buttons
    # Add Book Button
        self.bt1 = tk.Button(self.fm3, text=' Show Books', command=self.addbook, **button_config)
        self.bt1.place(x=40, y=40)

    # Issue Book Button
        self.bt2 = tk.Button(self.fm3, text=' Manage students', command=self.issuebook, **button_config)
        self.bt2.place(x=250, y=40)

    # Edit Book Button
        self.bt3 = tk.Button(self.fm3, text='  Edit Books', command=self.edit, **button_config)
        self.bt3.place(x=40, y=120)
    # Return Book Button
        self.bt4 = tk.Button(self.fm3, text='  Manage Teachers', command=self.returnbook, **button_config)
        self.bt4.place(x=250, y=120)

    # Delete Book Button
        self.bt5 = tk.Button(self.fm3, text=' Delete Books', command=self.delete, **button_config)
        self.bt5.place(x=40, y=200)

    # Show Book Button
        self.bt6 = tk.Button(self.fm3, text=' Show Books', command=self.show, **button_config)
        self.bt6.place(x=250, y=280)

    # Search Book Button
        self.bt7 = tk.Button(self.fm3, text='  Search Books', command=self.search, **button_config)
        self.bt7.place(x=250, y=200)

    # Log Out Button
        self.bt8 = tk.Button(self.fm3, text='  Log Out', command=self.logout, **button_config)
        self.bt8.place(x=40, y=280)    








    def addbook(self):
        pass
    def issuebook(self):
        def __init__(self):
            self.root = Toplevel()
            self.root.title("Issue Book")
            self.issue()
            self.root.mainloop()
        def issue(self):
            self.f = Frame(self.root, bg='#ffe8ec', width=900, height=390)
            self.f.place(x=0, y=110)

            self.fmi = Canvas(self.f, bg='#ffe8ec', width=900, height=390, bd=0, relief='flat')
            self.fmi.place(x=0, y=0)
    
            self.fc = Frame(self.fmi, bg='#ffe8ec', width=338, height=230, bd=4, relief='flat')
            self.fc.place(x=70, y=20)

            self.ffbll = Frame(self.fc, bg='#00203f', bd=2, relief='flat', width=210, height=40)
            self.ffbll.place(x=50, y=0)

            self.lc = Label(self.ffbll, text='STUDENT INFORMATION', bg='#00203f', fg='#adefd1', font=('Arial', 12, 'bold'))
            self.lc.place(x=0, y=6)

        # ERP ID of student
            self.lb = Label(self.fc, text='ERP ID', bg='#ffe8ec', fg='black', font=('times new roman', 11, 'bold'))
            self.lb.place(x=15, y=90)

            self.em2 = Entry(self.fc, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
            self.em2.place(x=105, y=90)

        # Submit Button for ERP ID
            self.bt = Button(self.fc, text='SUBMIT', width=8, bg='#00203f', fg='#adefd1', font=('Canara', 12, 'bold'),
                             bd=5, relief='flat', command=self.check, activeforeground='#00203f', activebackground='#adefd1')
            self.bt.place(x=15, y=160)

        # Back Button (commented out image related code)
            self.backbt = Button(self.fmi, width=60, bg='#ffe8ec', activebackground='#ffe8ec', bd=0, relief='flat',
                                 command=self.issueback)
            self.backbt.place(x=5, y=5)
        # self.log = PhotoImage(file='filename.png')
        # self.backbt.config(image=self.log, compound=LEFT)
        # self.small_log = self.log.subsample(2, 2)
        # self.backbt.config(image=self.small_log)
        def check(self):
            self.b = self.em2.get()
            cursor = dbstudents.cursor()
            cursor.execute("SELECT * FROM Students WHERE ERP=%s", (self.b,))
            self.var = cursor.fetchone()
            if self.var is not None:
                self.fmii = Canvas(self.f, bg='#ffe8ec', width=338, height=90, bd=0, relief='flat')
                self.fmii.place(x=70, y=255)

            # Name
                self.lb1 = Label(self.fmii, text='Name :', fg='black', bg='#ffe8ec', font=('Calibri', 12, 'bold'))
                self.lb1.place(x=5, y=5)
                self.lb2 = Label(self.fmii, text=self.var[1], fg='black', bg='#ffe8ec', font=('Calibri', 12, 'bold'))
                self.lb2.place(x=70, y=5)

            # Course
                self.lb3 = Label(self.fmii, text='Course :', fg='black', bg='#ffe8ec', font=('Calibri', 12, 'bold'))
                self.lb3.place(x=5, y=25)
                self.lb4 = Label(self.fmii, text=self.var[2], fg='black', bg='#ffe8ec', font=('Calibri', 12, 'bold'))
                self.lb4.place(x=70, y=25)

            # Year
                self.lb5 = Label(self.fmii, text='Year :', fg='black', bg='#ffe8ec', font=('Calibri', 12, 'bold'))
                self.lb5.place(x=5, y=45)
                self.lb6 = Label(self.fmii, text=self.var[3], fg='black', bg='#ffe8ec', font=('Calibri', 12, 'bold'))
                self.lb6.place(x=70, y=45)

            # Contact
                self.lb7 = Label(self.fmii, text='Contact :', fg='black', bg='#ffe8ec', font=('Calibri', 12, 'bold'))
                self.lb7.place(x=5, y=65)
                self.lb8 = Label(self.fmii, text=self.var[6], fg='black', bg='#ffe8ec', font=('Calibri', 12, 'bold'))
                self.lb8.place(x=70, y=65)

            # IssueBooks
                self.fr = Frame(self.fmi, bg='#ffe8ec', bd=5, relief='flat', width=338, height=250)
                self.fr.place(x=420, y=20)
                self.ff = Frame(self.fr, bg='#adefd1', bd=2, relief='flat', width=140, height=40)
                self.ff.place(x=80, y=0)

                self.lb = Label(self.ff, text='ISSUE BOOK', bg='#adefd1', fg='#00203f', font=('Arial', 12, 'bold'))
                self.lb.place(x=13, y=5)

            # Book ID
                self.tt = Label(self.fr, text='BOOK ID', bg='#ffe8ec', fg='#00203f', font=('times new roman', 11, 'bold'))
                self.tt.place(x=30, y=90)
                self.e1 = Entry(self.fr, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                self.e1.place(x=130, y=90)

            # Submit Button for BookID
                self.bt1 = Button(self.fr, text='SUBMIT', width=8, bg='#adefd1', fg='#00203f', font=('Canara', 12, 'bold'),
                                  bd=5, relief='flat', command=self.data, activeforeground='#adefd1',
                                  activebackground='#00203f')
                self.bt1.place(x=15, y=160)
            else:
                messagebox.showwarning('Warning', 'This student is not registered !')
        
        def issueback(self):
            try:
                self.boot.destroy()
                self.cur()
            except Exception as e:
                self.cur()

        repeat = 0
        def data(self):
            self.b = self.em2.get()
            cursor = dbstudents.cursor()
            cursor.execute("SELECT * FROM Students WHERE ERP=%s", (self.b,))
            self.var = cursor.fetchone()
            self.flag = 0
            if int(self.var[11]) >= 3:
                try:
                    self.boot.destroy()
                    messagebox.showerror("Unable to process request", "You exceed the limit of Books per student!")
                    self.flag = 1
                    self.cur()
                except Exception as e:
                    messagebox.showerror("Unable to process request", "You exceed the limit of Books per student!")
                    self.flag = 1
                    self.cur()

            self.vva = self.e1.get()
            cursor = dbstore.cursor()
            cursor.execute("SELECT * FROM Books WHERE BookID=%s", (self.vva,))
            dbstore.commit()
            self.value = cursor.fetchone()

            if self.value is not None:
                if self.flag != 1:
                    self.boot = Tk()
                    self.boot.title("Issue Books")
                # self.boot.iconbitmap("filename.ico")
                    self.boot.configure(bg='#ffe8ec')
                    self.boot.geometry("370x450+880+30")
                    self.boot.resizable(0, 0)
                    IssueBook.repeat = 1

                    self.lb = Label(self.boot, text='Title:', bg='#ffe8ec', fg='black', font=('Calibri', 12, 'bold'))
                    self.lb.place(x=30, y=30)
                    self.lbn = Label(self.boot, text=self.value[1], bg='#ffe8ec', fg='black', font=('Calibri', 12, 'bold'))
                    self.lbn.place(x=120, y=30)
                    self.lb = Label(self.boot, text='Author:', bg='#ffe8ec', fg='black', font=('Calibri', 12, 'bold'))
                    self.lb.place(x=30, y=60)
                    self.lbn = Label(self.boot, text=self.value[2], bg='#ffe8ec', fg='black', font=('Calibri', 12, 'bold'))
                    self.lbn.place(x=120, y=60)
                    self.lb = Label(self.boot, text='Edition:', bg='#ffe8ec', fg='black', font=('Calibri', 12, 'bold'))
                    self.lb.place(x=30, y=90)
                    self.lbn = Label(self.boot, text=self.value[3], bg='#ffe8ec', fg='black', font=('Calibri', 12, 'bold'))
                    self.lbn.place(x=120, y=90)

                    self.label = Label(self.fr, text='ADD MORE BOOKS ', bg='#ffe8ec', fg='black',
                                       font=('times new roman', 11, 'bold'))
                    self.label.place(x=15, y=220)

                # Radio Button
                    self.it1 = Radiobutton(self.fr, text='YES', bg='#ffe8ec', variable='radio', value=1, command=self.yes)
                    self.it1.place(x=170, y=220)

                    self.it2 = Radiobutton(self.fr, text='NO', bg='#ffe8ec', variable='radio', value=2, command=self.no)
                    self.it2.place(x=240, y=220)

                # ISSUED button
                    self.button1 = Button(self.boot, text='ISSUE', bg='#adefd1', fg='#00203f', width=10, height=0,
                                          font=('Canara', 11, 'bold'), activebackground='#00203f',
                                          activeforeground='#adefd1', command=self.issued)
                    self.button1.place(x=30, y=400)

                    self.btn = Button(self.boot, text='SEND MAIL', bg='#adefd1', fg='#00203f', width=10, height=0,
                                      font=('Canara', 11, 'bold'), activebackground='#00203f', activeforeground='#adefd1',
                                      command=self.mail)
                    self.btn.place(x=160, y=400)

                # Date - Calendar
                    self.x = date.today()

                    self.cal = Calendar(self.boot, selectmode="day", bg='black', year=2022, month=3, day=30)
                    self.cal.place(x=20, y=150)

                    btn1 = Button(self.boot, text="CONFIRM DATE", command=self.get_data, bg='#343148',
                                  font=('Canara', 11, 'bold'),
                                  fg='#d7c49e', activebackground='black', activeforeground='#d7c49e', relief='flat')
                    btn1.place(x=90, y=350)

                    self.boot.mainloop()

            else:
                messagebox.showerror('Book Not Found', 'No such book exists!')
                self.e1.delete(0, tk.END)

        def get_data(self):
            self.datecon = self.cal.selection_get()

        def yes(self):
            self.n = self.n + 1

            self.bt1 = Button(self.fr, text='SUBMIT', width=8, bg='#adefd1', fg='#00203f', font=('Canara', 12, 'bold'),
                              bd=5, relief='flat', command=self.data, activeforeground='#adefd1', activebackground='#00203f',
                              state=tk.ACTIVE)
            self.bt1.place(x=15, y=160)

            self.e1.delete(0, tk.END)
            self.max = self.max - 1

        def no(self):
            self.bt1 = Button(self.fr, text='SUBMIT', width=8, bg='#adefd1', fg='#00203f', font=('Canara', 12, 'bold'),
                              bd=5, relief='flat', command=self.data, activeforeground='#adefd1', activebackground='#00203f',
                              state=tk.DISABLED)
            self.bt1.place(x=15, y=160)

        def issued(self):
            self.datecon = self.cal.selection_get()

            self.ac = self.e1.get()
            cursor = dbstore.cursor()

            cursor.execute("UPDATE Books SET Issue='Issued', ID=%s WHERE BookID=%s", (self.b, self.ac))
            dbstore.commit()

            if self.n <= 3:
                book = dbstudents.cursor()
                self.erpid1 = self.em2.get()
                book.execute("SELECT * FROM Students WHERE ERP=%s", (self.erpid1,))
                self.issuevar = book.fetchone()
                self.sum = self.issuevar[11] + 1
                book.execute("UPDATE Students SET NoBook=%s WHERE ERP=%s", (str(self.sum), self.b))
                dbstudents.commit()

            comm = dbstudents.cursor()
            comm.execute("UPDATE Students SET FromDate=%s, ToDate=%s, SubmitDate='' WHERE ERP=%s",
                         (str(self.x), str(self.datecon), self.b))
            dbstudents.commit()

            messagebox.showinfo('Library Management System', 'YOUR BOOK HAS BEEN ISSUED')
            self.boot.destroy()
            self.e1.delete(0, tk.END)

        def mail(self):
            self.erpid = self.em2.get()
            cursor = dbstudents.cursor()
            cursor.execute("SELECT * FROM Students WHERE ERP=%s", (self.erpid,))
            self.var = cursor.fetchone()
            sender = "libraryauthority@gmail.com"
            reciever = self.var[5]
            with open("passwordfilename.txt", 'r') as file:
                password = file.read()
            message = """FROM: LIBRARY DEPARTMENT
                            TO : Library Issued Books Department
                            Subject: Hello Student! Your book has been Issued"""
            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login(sender, password)
                server.sendmail(sender, reciever, message)
                print("ok")
                messagebox.showinfo("Library System", "Send mail Successfully !")
            except Exception as e:
                pass


    def issuebook():
        IssueBook()




        
    def edit(self):
        pass
    
    def returnbook(self):
        pass
    
    def delete(self):
        pass
    
    def show(self):
        pass
        
    def search(self):
        pass
        
    def logout(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("900x500")
    app = MainApp(root)
    root.mainloop()
    





