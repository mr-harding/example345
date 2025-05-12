from tkinter import *
from tkinter import messagebox

class User:
    def __init__(self, first_name, age, mobile_question):
        self.first_name = first_name
        self.age = age
        self.mobile_question = mobile_question

class GatherInfo:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Gather Information")
        self.page = 0

        #Configuring rows and columns
        #...

        self.users = []
        firstname = StringVar()
        age = IntVar()
        mobile_question = BooleanVar()

        self.title_frame = Frame(self.parent, bg="magenta")
        self.title_frame.grid(row=0, column=0, columnspan=2, sticky="nesw")
        self.title_label = Label(self.title_frame, text="Collecting person data", bg="magenta", fg="black")

        self.title_label.grid(row=0, column=0, sticky="nesw", pady=20)
        self.show_all_button = Button(self.title_frame, text="Show All", command=self.show_all)
        self.show_all_button.grid(row=0, column=1, sticky="e", padx=10)

        self.info_frame = Frame(self.parent)
        self.info_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=50)

        #First name and age labels
        self.first_name_label = Label(self.info_frame, text="First Name:")
        self.first_name_entry = Entry(self.info_frame, textvariable=firstname)

        self.age_label = Label(self.info_frame, text="Age:")
        self.age_entry = Entry(self.info_frame, textvariable=age, text="")


        self.first_name_label.grid(row=1, column=0, sticky="w")
        self.first_name_entry.grid(row=1, column=1, sticky="ew")
        self.age_label.grid(row=2, column=0, sticky="w")
        self.age_entry.grid(row=2, column=1, sticky="ew")

        self.mobile_question_label = Label(self.info_frame, text="Do you have a mobile phone?")
        self.mobile_question_label.grid(row=3, column=0, sticky="w")

        #Radiobuttons
        self.mobile_question_var = StringVar()
        self.mobile_question_var.set("No")

        self.mobile_question_yes = Radiobutton(self.info_frame, text="Yes", variable=self.mobile_question_var, value="Yes")
        self.mobile_question_no = Radiobutton(self.info_frame, text="No", variable=self.mobile_question_var, value="No")
        self.mobile_question_yes.grid(row=4, column=1, sticky="w")
        self.mobile_question_no.grid(row=4, column=2, sticky="w")

        self.data_control = Frame(self.parent)
        self.data_control.grid(row=4, column=0, padx=10, pady=50, columnspan=2, sticky="nesw")
        self.data_control.columnconfigure(0, weight=1)
        self.data_control.columnconfigure(1, weight=1)
        self.data_control.columnconfigure(2, weight=1)


        self.enter_data_button = Button(self.data_control, text="Enter Data", command=self.enter_data)
        self.enter_data_button.grid(row=4, column=1, sticky="ns")




    def show_all(self):
        '''Show all the data entered by the user'''

        #If the user has not entered any data, show a message box
        if self.users == []:
            messagebox.showinfo("Information", "No data entered yet.")
            return

        #Otherwise, show the data

        #Title frame
        self.title_label.configure(text="Displaying person data")
        self.show_all_button.configure(text="Add New Person", command=self.add_new_person)

        #Input boxes
        self.first_name_entry.grid_remove()
        self.age_entry.grid_remove()
        self.mobile_question_label.grid_remove()
        self.mobile_question_yes.grid_remove()
        self.mobile_question_no.grid_remove()

        if self.users[0] == "Yes":
            has_phone = "The user has a mobile phone."
        else:
            has_phone = "The user does not have a mobile phone."

        self.display_first_name_label = Label(self.info_frame, text=self.users[0].first_name)
        self.display_age_label = Label(self.info_frame, text=self.users[0].age)
        self.display_mobile_label = Label(self.info_frame, text=has_phone)

        self.display_first_name_label.grid(row=1, column=1, sticky="w", padx=10)
        self.display_age_label.grid(row=2, column=1, sticky="w", padx=10)
        self.display_mobile_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=10)



        #Buttons at the bottom
        self.enter_data_button.grid_remove()

        self.next_button = Button(self.data_control, text="Next", command=self.next_page)
        self.previous_button = Button(self.data_control, text="Previous", command=self.previous_page)

        self.previous_button.grid(row=4, column=0, sticky="w")
        self.next_button.grid(row=4, column=2, sticky="e")

        
    def add_new_person(self):
        '''Back to original page to add new person'''

        # Title change
        self.title_label.configure(text="Collecting person data")
        self.show_all_button.configure(text="Show All", command=self.show_all)

        # Bring back entry boxes and mobile phone question
        self.first_name_entry.grid()
        self.age_entry.grid()
        self.mobile_question_label.grid()
        self.mobile_question_yes.grid()
        self.mobile_question_no.grid()

        # Hide display labels
        self.display_first_name_label.grid_remove()
        self.display_age_label.grid_remove()
        self.display_mobile_label.grid_remove()

        # Show enter data button again
        self.enter_data_button.grid(row=4, column=1, sticky="ns")

        # Hide next and previous buttons
        self.next_button.grid_remove()
        self.previous_button.grid_remove()



    def enter_data(self):
        '''Enter the data entered by the user into the list of users'''
        user_name = self.first_name_entry.get().lower().capitalize()

        if user_name == "":
            messagebox.showerror("Error", "Please enter a valid first name.")
            self.first_name_entry.focus_set()
            return
        
        elif user_name in [user.first_name for user in self.users]:
            messagebox.showerror("Error", "This name already exists.")
            self.first_name_entry.delete(0, END)
            self.first_name_entry.focus_set()
            return
        
        elif self.age_entry.get() == "" or not self.age_entry.get().isdigit() or int(self.age_entry.get()) not in range(0, 121):
            messagebox.showerror("Error", "Please enter a valid age.")
            self.age_entry.focus_set()
            return



        
        user_name = User(user_name, self.age_entry.get(), self.mobile_question_var.get())
        self.users.append(user_name)
        messagebox.showinfo("Information", "Data entered successfully.")

        self.first_name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.first_name_entry.focus_set()


    def next_page(self):
        '''Go to the next page'''
        if self.page == len(self.users) - 1:
            self.page = 0
        else:
            self.page += 1

        self.display_first_name_label.configure(text=self.users[self.page].first_name)
        self.display_age_label.configure(text=self.users[self.page].age)
        if self.users[self.page].mobile_question == "Yes":
            has_phone = "The user has a mobile phone."
        else:
            has_phone = "The user does not have a mobile phone."
        self.display_mobile_label.configure(text=has_phone)

    def previous_page(self):
        '''Go back to to the previous page'''
        if self.page == 0:
            self.page = len(self.users) - 1
        else:
            self.page -= 1

        self.display_first_name_label.configure(text=self.users[self.page].first_name)
        self.display_age_label.configure(text=self.users[self.page].age)
        if self.users[self.page].mobile_question == "Yes":
            has_phone = "The user has a mobile phone."
        else:
            has_phone = "The user does not have a mobile phone."
        self.display_mobile_label.configure(text=has_phone)

if __name__ == "__main__":
    root = Tk()
    gui = GatherInfo(root)
    #Original size of the window but cant be bothered resizing every object so it looks clean
    # root.geometry("351x375")
    root.mainloop()