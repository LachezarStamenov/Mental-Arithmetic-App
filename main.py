import tkinter.messagebox
from tkinter import *
import tkinter as tk
import random
import math


class Mental_Aritmetic_App:
    def __init__(self, root):
        self.root = root
        self.sum_total = []
        self.tasks_dictionary = {}
        self.root.geometry("1200x800+0+0")
        self.root.title("Mental Arithmetic")
        self.root.resizable(width=True, height=True)
        self.WORK_MIN = 3
        self.reps = 0
        self.timer = None
        # ----------------------------- TITLE LABEL ------------------------------- #
        self.label = Label(self.root, text='Summation of two-digit numbers - mix ', bg="#e0e0df",
                           font=("Arial", 20, "bold"),
                           relief=GROOVE)
        self.label.grid(column=0, row=0, columnspan=16)

        # ---------------------------- TASKS POSITIONS ------------------------------- #

        self.row_label1 = Label(font=("Arial", 18), text="1\n2\n3\n4\n5\n6\n7\n8\n9\n10", justify='center')
        self.row_label1.grid(column=0, row=2)
        self.l1 = Label(font=("Arial", 18), text="", justify='center')
        self.l1.grid(column=1, row=2)
        self.l2 = Label(font=("Arial", 18), text="", justify='center')
        self.l2.grid(column=2, row=2)
        self.l3 = Label(font=("Arial", 18), text="", justify='center')
        self.l3.grid(column=3, row=2)
        self.l4 = Label(font=("Arial", 18), text="", justify='center')
        self.l4.grid(column=4, row=2)
        self.l5 = Label(font=("Arial", 18), text="", justify='center')
        self.l5.grid(column=5, row=2)
        self.l6 = Label(font=("Arial", 18), text="", justify='center')
        self.l6.grid(column=6, row=2)
        self.l7 = Label(font=("Arial", 18), text="", justify='center')
        self.l7.grid(column=7, row=2)
        self.l8 = Label(font=("Arial", 18), text="", justify='center')
        self.l8.grid(column=8, row=2)
        self.l9 = Label(font=("Arial", 18), text="", justify='center')
        self.l9.grid(column=9, row=2)
        self.l10 = Label(font=("Arial", 18), text="", justify='center')
        self.l10.grid(column=10, row=2)
        self.row_label2 = Label(font=("Arial", 18), text="1\n2\n3\n4\n5\n6\n7\n8\n9\n10", justify='center')
        self.row_label2.grid(column=0, row=4)
        self.l11 = Label(font=("Arial", 18), text="", justify='center')
        self.l11.grid(column=1, row=4)
        self.l12 = Label(font=("Arial", 18), text="", justify='center')
        self.l12.grid(column=2, row=4)
        self.l13 = Label(font=("Arial", 18), text="", justify='center')
        self.l13.grid(column=3, row=4)
        self.l14 = Label(font=("Arial", 18), text="", justify='center')
        self.l14.grid(column=4, row=4)
        self.l15 = Label(font=("Arial", 18), text="", justify='center')
        self.l15.grid(column=5, row=4)
        self.l16 = Label(font=("Arial", 18), text="", justify='center')
        self.l16.grid(column=6, row=4)
        self.l17 = Label(font=("Arial", 18), text="", justify='center')
        self.l17.grid(column=7, row=4)
        self.l18 = Label(font=("Arial", 18), text="", justify='center')
        self.l18.grid(column=8, row=4)
        self.l19 = Label(font=("Arial", 18), text="", justify='center')
        self.l19.grid(column=9, row=4)
        self.l20 = Label(font=("Arial", 18), text="", justify='center')
        self.l20.grid(column=10, row=4)

        # ---------------------------- ENTRY BUTTONS ------------------------------- #
        self.en1 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en1.grid(column=1, row=3)
        self.en2 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en2.grid(column=2, row=3)
        self.en3 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en3.grid(column=3, row=3)
        self.en4 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en4.grid(column=4, row=3)
        self.en5 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en5.grid(column=5, row=3)
        self.en6 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en6.grid(column=6, row=3)
        self.en7 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en7.grid(column=7, row=3)
        self.en8 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en8.grid(column=8, row=3)
        self.en9 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en9.grid(column=9, row=3)
        self.en10 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en10.grid(column=10, row=3)
        self.en11 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en11.grid(column=1, row=5)
        self.en12 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en12.grid(column=2, row=5)
        self.en13 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en13.grid(column=3, row=5)
        self.en14 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en14.grid(column=4, row=5)
        self.en15 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en15.grid(column=5, row=5)
        self.en16 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en16.grid(column=6, row=5)
        self.en17 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en17.grid(column=7, row=5)
        self.en18 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en18.grid(column=8, row=5)
        self.en19 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en19.grid(column=9, row=5)
        self.en20 = Entry(width=8, font='arial 15', bd=7, relief=GROOVE)
        self.en20.grid(column=10, row=5)

        # ------------------------------- BUTTONS -------------------------------------- #
        self.btn_start = tk.Button(text="Start", font=("Arial", 14), bg="#f4f2f4",
                                   command=lambda: [self.nums_configurator(), self.start_timer()])
        self.btn_start.grid(column=1, row=6)

        self.btn_validate = tk.Button(text="Check\nanswers", font=("Arial", 12), bg="#f4f2f4", command=self.validator)
        self.btn_validate.grid(column=9, row=6)

        self.btn_exit = tk.Button(text="Exit", font=("Arial", 14), bg="#f4f2f4", command=self.exit)
        self.btn_exit.grid(column=10, row=6)

        self.btn_help = tk.Button(text="Help", font=("Arial", 14), bg="#f4f2f4", command=self.help)
        self.btn_help.grid(column=8, row=6)

        self.canvas = Canvas(width=70, height=40, bg='#9ccd28', highlightthickness=0)
        self.timer_text = self.canvas.create_text(35, 20, text="00:00", fill="black", font=("", 15, "bold"))
        self.canvas.grid(column=10, row=1)

        # ---------------------------- MOVE TO NEXT ENTRY BY ENTER CLICK ------------------------------- #
        entries = [child for child in root.winfo_children() if isinstance(child, Entry)]
        for idx, entry in enumerate(entries):
            entry.bind('<Return>', lambda e, idx=idx: self.go_to_next_entry(e, entries, idx))

        # ---------------------------- NUMBERS GENERATOR ----------------------------------- #
    def num_generator(self):
        """ Generate  10 random numbers between -99 to 99"""
        self.random_list = []
        while len(self.random_list) < 10:
            self.n = random.randint(-85, 99)
            self.random_list.append(self.n)
            if sum(self.random_list) > 0:
                continue
            else:
                self.random_list.remove(self.n)
                self.n = random.randint(-85, 99)
                self.random_list.append(self.n)
                if sum(self.random_list) < 0:
                    self.random_list.remove(self.n)

        print((sum(map(int, self.random_list))), end=" ")
        self.sum_total.append(sum(map(int, self.random_list)))
        return self.random_list

    # ---------------------------- TASKS GENERATOR ----------------------------------- #
    def nums_configurator(self):
        for i in range(1, 21):
            self.key = i
            self.value = self.num_generator()
            self.value_as_str = " \n".join(map(str, self.value))
            self.tasks_dictionary[self.key] = self.value_as_str
        self.l1.config(text=self.tasks_dictionary[1])
        self.l2.config(text=self.tasks_dictionary[2])
        self.l3.config(text=self.tasks_dictionary[3])
        self.l4.config(text=self.tasks_dictionary[4])
        self.l5.config(text=self.tasks_dictionary[5])
        self.l6.config(text=self.tasks_dictionary[6])
        self.l7.config(text=self.tasks_dictionary[7])
        self.l8.config(text=self.tasks_dictionary[8])
        self.l9.config(text=self.tasks_dictionary[9])
        self.l10.config(text=self.tasks_dictionary[10])
        self.l11.config(text=self.tasks_dictionary[11])
        self.l12.config(text=self.tasks_dictionary[12])
        self.l13.config(text=self.tasks_dictionary[13])
        self.l14.config(text=self.tasks_dictionary[14])
        self.l15.config(text=self.tasks_dictionary[15])
        self.l16.config(text=self.tasks_dictionary[16])
        self.l17.config(text=self.tasks_dictionary[17])
        self.l18.config(text=self.tasks_dictionary[18])
        self.l19.config(text=self.tasks_dictionary[19])
        self.l20.config(text=self.tasks_dictionary[20])

        return self.tasks_dictionary

    # ---------------------------- ANSWERS VALIDATION ----------------------------------- #
    def validator(self):
        entries = {
            1: self.en1.get(), 2: self.en2.get(), 3: self.en3.get(), 4: self.en4.get(), 5: self.en5.get(),
            6: self.en6.get(), 7: self.en7.get(), 8: self.en8.get(), 9: self.en9.get(), 10: self.en10.get(),
            11: self.en11.get(), 12: self.en12.get(), 13: self.en13.get(), 14: self.en14.get(), 15: self.en15.get(),
            16: self.en16.get(), 17: self.en17.get(), 18: self.en18.get(), 19: self.en19.get(), 20: self.en20.get(),
        }
        answers = {
            1: self.sum_total[0], 2: self.sum_total[1], 3: self.sum_total[2], 4: self.sum_total[3],
            5: self.sum_total[4], 6: self.sum_total[5], 7: self.sum_total[6], 8: self.sum_total[7],
            9: self.sum_total[8], 10: self.sum_total[9], 11: self.sum_total[10], 12: self.sum_total[11],
            13: self.sum_total[12], 14: self.sum_total[13], 15: self.sum_total[14], 16: self.sum_total[15],
            17: self.sum_total[16], 18: self.sum_total[17], 19: self.sum_total[18], 20: self.sum_total[19],
        }
        try:
            if int(entries[1]) == answers[1]:
                self.en1.config(fg='green')
            else:
                self.en1.config(fg='red')
            if int(entries[2]) == answers[2]:
                self.en2.config(fg='green')
            else:
                self.en2.config(fg='red')
            if int(entries[3]) == answers[3]:
                self.en3.config(fg='green')
            else:
                self.en3.config(fg='red')
            if int(entries[4]) == answers[4]:
                self.en4.config(fg='green')
            else:
                self.en4.config(fg='red')
            if int(entries[5]) == answers[5]:
                self.en5.config(fg='green')
            else:
                self.en5.config(fg='red')
            if int(entries[6]) == answers[6]:
                self.en6.config(fg='green')
            else:
                self.en6.config(fg='red')
            if int(entries[7]) == answers[7]:
                self.en7.config(fg='green')
            else:
                self.en7.config(fg='red')
            if int(entries[8]) == answers[8]:
                self.en8.config(fg='green')
            else:
                self.en8.config(fg='red')
            if int(entries[9]) == answers[9]:
                self.en9.config(fg='green')
            else:
                self.en9.config(fg='red')
            if int(entries[10]) == answers[10]:
                self.en10.config(fg='green')
            else:
                self.en10.config(fg='red')
            if int(entries[11]) == answers[11]:
                self.en11.config(fg='green')
            else:
                self.en11.config(fg='red')
            if int(entries[12]) == answers[12]:
                self.en12.config(fg='green')
            else:
                self.en12.config(fg='red')
            if int(entries[13]) == answers[13]:
                self.en13.config(fg='green')
            else:
                self.en13.config(fg='red')
            if int(entries[14]) == answers[14]:
                self.en14.config(fg='green')
            else:
                self.en14.config(fg='red')
            if int(entries[15]) == answers[15]:
                self.en15.config(fg='green')
            else:
                self.en15.config(fg='red')
            if int(entries[16]) == answers[16]:
                self.en16.config(fg='green')
            else:
                self.en16.config(fg='red')
            if int(entries[17]) == answers[17]:
                self.en17.config(fg='green')
            else:
                self.en17.config(fg='red')
            if int(entries[18]) == answers[18]:
                self.en18.config(fg='green')
            else:
                self.en18.config(fg='red')
            if int(entries[19]) == answers[19]:
                self.en19.config(fg='green')
            else:
                self.en19.config(fg='red')
            if int(entries[20]) == answers[20]:
                self.en20.config(fg='green')
            else:
                self.en20.config(fg='red')
        except:
            print("error")

        # ---------------------------- TIMER ----------------------------------- #

    def start_timer(self):
        self.reps += 1
        self.work_sec = self.WORK_MIN * 60
        self.count_down(self.work_sec)

    def count_down(self, count):

        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            self.timer = root.after(1000, self.count_down, count - 1)

        # ------------------------- GO TO NEXT ENTRY BY ENTER---------------------------- #

    def go_to_next_entry(self, event, entry_list, this_index):
        next_index = (this_index + 1) % len(entry_list)
        entry_list[next_index].focus_set()

        # ------------------------------------ EXIT-------------------------------------- #

    def exit(self):
        exit = tkinter.messagebox.askyesno('', 'Do you really want to exit?')
        if exit > 0:
            root.destroy()
            return
    # -------------------------------- HELP INFORMATION---------------------------------- #

    def help(self):
        text = "USER INSTRUCTIONS\n\n" \
               "1. Use the start button to generate 20 tasks.\n\n " \
               "2. The timer on the left corner will start counting 3 minutes.\n\n" \
               "3. Fill your answers in the empty cells and click Enter to move to next.\n\n" \
               "4. When you are ready with your answers, click 'Check answers' and if \n\n" \
               "your answer is correct it will be colored in green, else it will be red!\n\n" \
               "5. Exit the App with 'Exit' button."
        text = tkinter.messagebox.showinfo("", text)
        return


root = Tk()
obj = Mental_Aritmetic_App(root)
root.mainloop()
