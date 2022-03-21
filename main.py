from tkinter import *
import tkinter as tk
import random
import math


class Mental_Aritmetic_App:
    def __init__(self, root):
        self.root = root
        self.tasks_dictionary = {}
        # self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.geometry("1500x700")
        self.root.title("Алекс-Ментална Аритметика")
        self.root.resizable(width=True, height=True)
        self.WORK_MIN = 3
        self.reps = 0
        self.timer = None
        # Title Label
        self.label = Label(self.root, text='Алекс-Ментална Аритметика', bg="#d8f8f7", font=("Arial", 20, "bold"),
                           relief=GROOVE)
        self.label.grid(column=1, row=0)
        self.label.pack(ipadx=10, ipady=10)

        # Tasks positions
        self.l1 = Label(font=("Arial", 22), text="", justify='center')
        self.l1.place(x=70, y=100)
        self.l2 = Label(font=("Arial", 22), text="", justify='center')
        self.l2.place(x=230, y=100)
        self.l3 = Label(font=("Arial", 22), text="", justify='center')
        self.l3.place(x=430, y=100)
        self.l4 = Label(font=("Arial", 22), text="", justify='center')
        self.l4.place(x=630, y=100)
        self.l5 = Label(font=("Arial", 22), text="", justify='center')
        self.l5.place(x=830, y=100)
        self.l6 = Label(font=("Arial", 22), text="", justify='center')
        self.l6.place(x=1030, y=100)
        self.l7 = Label(font=("Arial", 22), text="", justify='center')
        self.l7.place(x=1230, y=100)
        self.l8 = Label(font=("Arial", 22), text="", justify='center')
        self.l8.place(x=1430, y=100)
        self.l9 = Label(font=("Arial", 22), text="", justify='center')
        self.l9.place(x=1630, y=100)
        self.l10 = Label(font=("Arial", 22), text="", justify='center')
        self.l10.place(x=1830, y=100)
        self.l11 = Label(font=("Arial", 22), text="", justify='center')
        self.l11.place(x=70, y=500)
        self.l12 = Label(font=("Arial", 22), text="", justify='center')
        self.l12.place(x=230, y=500)
        self.l13 = Label(font=("Arial", 22), text="", justify='center')
        self.l13.place(x=430, y=500)
        self.l14 = Label(font=("Arial", 22), text="", justify='center')
        self.l14.place(x=630, y=500)
        self.l15 = Label(font=("Arial", 22), text="", justify='center')
        self.l15.place(x=830, y=500)
        self.l16 = Label(font=("Arial", 22), text="", justify='center')
        self.l16.place(x=1030, y=500)
        self.l17 = Label(font=("Arial", 22), text="", justify='center')
        self.l17.place(x=1230, y=500)
        self.l18 = Label(font=("Arial", 22), text="", justify='center')
        self.l18.place(x=1430, y=500)
        self.l19 = Label(font=("Arial", 22), text="", justify='center')
        self.l19.place(x=1630, y=500)
        self.l20 = Label(font=("Arial", 22), text="", justify='center')
        self.l20.place(x=1830, y=500)

        # ---------------------------- ENTRY BUTTONS ------------------------------- #
        self.en1 = Entry(width=8, textvariable=self.l1, font='arial 15', bd=7, relief=GROOVE)
        self.en1.place(x=30, y=450)
        self.en2 = Entry(width=8, textvariable=self.l2, font='arial 15', bd=7, relief=GROOVE)
        self.en2.place(x=230, y=450)
        self.en3 = Entry(width=8, textvariable=self.l3, font='arial 15', bd=7, relief=GROOVE)
        self.en3.place(x=430, y=450)
        self.en4 = Entry(width=8, textvariable=self.l4, font='arial 15', bd=7, relief=GROOVE)
        self.en4.place(x=630, y=450)
        self.en5 = Entry(width=8, textvariable=self.l5, font='arial 15', bd=7, relief=GROOVE)
        self.en5.place(x=830, y=450)
        self.en6 = Entry(width=8, textvariable=self.l6, font='arial 15', bd=7, relief=GROOVE)
        self.en6.place(x=1030, y=450)
        self.en7 = Entry(width=8, textvariable=self.l7, font='arial 15', bd=7, relief=GROOVE)
        self.en7.place(x=1230, y=450)
        self.en8 = Entry(width=8, textvariable=self.l8, font='arial 15', bd=7, relief=GROOVE)
        self.en8.place(x=1430, y=450)
        self.en9 = Entry(width=8, textvariable=self.l9, font='arial 15', bd=7, relief=GROOVE)
        self.en9.place(x=1630, y=450)
        self.en10 = Entry(width=8, textvariable=self.l10, font='arial 15', bd=7, relief=GROOVE)
        self.en10.place(x=1780, y=450)
        self.en11 = Entry(width=8, textvariable=self.l11, font='arial 15', bd=7, relief=GROOVE)
        self.en11.place(x=30, y=840)
        self.en12 = Entry(width=8, textvariable=self.l12, font='arial 15', bd=7, relief=GROOVE)
        self.en12.place(x=230, y=840)
        self.en13 = Entry(width=8, textvariable=self.l13, font='arial 15', bd=7, relief=GROOVE)
        self.en13.place(x=430, y=840)
        self.en14 = Entry(width=8, textvariable=self.l14, font='arial 15', bd=7, relief=GROOVE)
        self.en14.place(x=630, y=840)
        self.en15 = Entry(width=8, textvariable=self.l15, font='arial 15', bd=7, relief=GROOVE)
        self.en15.place(x=830, y=840)
        self.en16 = Entry(width=8, textvariable=self.l16, font='arial 15', bd=7, relief=GROOVE)
        self.en16.place(x=1030, y=840)
        self.en17 = Entry(width=8, textvariable=self.l17, font='arial 15', bd=7, relief=GROOVE)
        self.en17.place(x=1230, y=840)
        self.en18 = Entry(width=8, textvariable=self.l18, font='arial 15', bd=7, relief=GROOVE)
        self.en18.place(x=1430, y=840)
        self.en19 = Entry(width=8, textvariable=self.l19, font='arial 15', bd=7, relief=GROOVE)
        self.en19.place(x=1630, y=840)
        self.en20 = Entry(width=8, textvariable=self.l20, font='arial 15', bd=7, relief=GROOVE)
        self.en20.place(x=1780, y=840)

        # ---------------------------- START BUTTON ------------------------------- #
        self.b1 = tk.Button(text="Start", font=("Arial", 18), bg="#c63d2b",
                            command=lambda: [self.nums_configurator(), self.start_timer()])
        self.b1.place(x=10, y=10)
        # ---------------------------- UI SETUP ------------------------------- #
        self.canvas = Canvas(width=100, height=50, bg='#00a200', highlightthickness=0)
        self.timer_text = self.canvas.create_text(50, 30, text="00:00", fill="black",
                                                  font=("", 20, "bold"))
        self.canvas.place(x=120, y=10)

        # ---------------------------- MOVE TO NEXT ENTRY BY ENTER CLICK ------------------------------- #
        entries = [child for child in root.winfo_children() if isinstance(child, Entry)]
        for idx, entry in enumerate(entries):
            entry.bind('<Return>', lambda e, idx=idx: self.go_to_next_entry(e, entries, idx))

    def num_generator(self):
        """ Function which generate random 10 numbers between -99 to 99"""
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

        nums_as_str = " \n".join(map(str, self.random_list))
        print(sum(map(int, self.random_list)), end=' ')

        return nums_as_str

    def nums_configurator(self):
        """Function to generate 20 random tasks"""

        for i in range(1, 21):
            self.key = i
            self.value = self.num_generator()
            self.tasks_dictionary[self.key] = self.value
            self.lst = [self.value]
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

        # ---------------------------- TIMER MECHANISM ------------------------------- #

    def start_timer(self):
        self.reps += 1
        self.work_sec = self.WORK_MIN * 60
        self.count_down(self.work_sec)

        # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    def count_down(self, count):

        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            self.timer = root.after(1000, self.count_down, count - 1)

    # ---------------------------- GO TO NEXT ENTRY TO FILL BY ENTER------------------------------- #
    def go_to_next_entry(self, event, entry_list, this_index):
        next_index = (this_index + 1) % len(entry_list)
        entry_list[next_index].focus_set()


root = Tk()
obj = Mental_Aritmetic_App(root)
root.mainloop()