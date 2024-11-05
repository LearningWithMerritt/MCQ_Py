import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

from config import *





class App(tk.Tk):

    quizzes = [
        "Operators",
        "Strings",
        "Conditionals", 
        "Functions"
    ]

    def __init__(self):
        super().__init__()
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title(TITLE)
        self.minsize(WIDTH,HEIGHT)
        self.configure(bg= WINDOW_BG)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0,weight=1)


        self.title_screen = TitleScreen(self)
        self.quiz_screen = QuizView(self)
        # self.quiz_select_screen = QuizSelectPage(self)

     
    

        self.show_frame(self.quiz_screen)
        self.mainloop()


    def show_frame(self, frame):
        frame.tkraise()




class TitleScreen(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        
        self.configure(bg=BG_COLOR)


        self.bind_events()

        self.create_widgets()
        self.draw_widgets()

        self.grid(row=0, column=0, sticky="nsew")
    
    def create_widgets(self):
        self.container = tk.Frame(self, bg=BG_COLOR 
        )
        self.title = tk.Label(self.container, 
            text=TITLE, font=("Courier", 50),
            fg="#ffd43b", bg=BG_COLOR
        )


        self.b_frame=tk.Frame(self.container, bg=BG_COLOR)

        self.start = tk.Button(
            self.b_frame, text="START", height=2, command= lambda: print("START QUIZ")  #lambda : self.parent.show_frame(self.parent.quiz_select_screen)
        )

        self.settings = tk.Button(
            self.b_frame, text="SETTINGS", height=2, command= lambda: print("OPEN SETTINGS")
        )

        self.stop = tk.Button(
            self.b_frame, text="EXIT", height=2,command=self.exit_app
        )

        self.frame2 = tk.Frame(self.container, bg=BG_COLOR)

        self.dropdown = ttk.Combobox(self.frame2, values = App.quizzes)
        self.dropdown.set("Select a Quiz")

    def draw_widgets(self):
        # self.container.place(
        #     relx=0.5, rely=0.25, relheight=.75, 
        #     relwidth=.80, anchor="center"
        # )

        self.container.pack(fill="both", expand=1, padx=20, pady=20)

        self.title.pack(fill="both")

        self.frame2.pack(fill="x")
        self.dropdown.pack(pady=10)


        self.b_frame.pack(fill="x")
        self.start.pack(side="left", fill="both", expand=1)
        self.settings.pack(side="left", fill="both", expand=1,padx=5)
        self.stop.pack(side="left", fill="both", expand=1 )





    def bind_events(self):
        self.parent.protocol("WM_DELETE_WINDOW", self.exit_app)

    def exit_app(self):
        # self.update_idletasks()
        # if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        #     self.parent.destroy()
        self.parent.destroy()




class QuizView(tk.Frame):

    testq = (
    "What is the output of the following code segment?\n\n"
    "def foo(num):\n"
    "   vals = []\n"
    "   for x in range(num):\n"
    "       if x % 10 == 0:\n"
    "           vals.append(x)\n"
    "   return vals\n\n\n"
    "print(foo(100))\n\n"

    )

    test_choices = [
        "[0,10,20,30,40,50,60,70,80,90]",
        "[0,10,20,30,40,50,60,70,80,90,100]",
        "[10,20,30,40,50,60,70,80,90]",
        "[10,20,30,40,50,60,70,80,90,100]"
    ]

    def __init__(self, parent):
        super().__init__(parent)

        self.q_num = tk.IntVar(value=1)
        self.score =tk.IntVar(value=23)            # set later
        self.num_of_questions = tk.IntVar(value=30) # set later
        self.percent = tk.IntVar(value=round(self.score.get() / self.num_of_questions.get() * 100))

        self.parent = parent
        self.configure(
            bg=BG_COLOR
        )


        self.create()
        self.layout()

        self.grid(row=0, column=0, sticky="nsew")

    def create(self):
        self.frame1 = tk.Frame(self, width=800,height=800, bg=BG_COLOR)
        self.quiz_name = tk.Label(self.frame1, text="QUIZ NAME", bg=HIGHLIGHT, font=("Courier", QUESTION_FONT_SIZE, "bold"))

        self.frame2 = tk.Frame(self.frame1, bg=HIGHLIGHT)
        self.score_frame = tk.Frame(self.frame2, bg=HIGHLIGHT)
        self.q_num_label = tk.Label(self.score_frame, text=f"QUESTION: {self.q_num.get()}", bg=HIGHLIGHT, font=("Courier", QUESTION_FONT_SIZE, "bold"))
        self.score = tk.Label(self.score_frame, text=f"SCORE: {self.score.get()}/{self.num_of_questions.get()}", bg=HIGHLIGHT, font=("Courier", QUESTION_FONT_SIZE, "bold"))
        self.percent_label = tk.Label(self.score_frame,text=f"PERCENT: {self.percent.get()}%", bg=HIGHLIGHT, font=("Courier", QUESTION_FONT_SIZE, "bold"))



        
        self.textbox = tk.Text(self.frame1,height=10, width=80, font=("Courier", QUESTION_FONT_SIZE))
        self.textbox.insert(tk.END, QuizView.testq)
        self.textbox.configure(
            state="disabled"
        )

        self.choice_buttons = []
        for e in QuizView.test_choices:
            self.choice_buttons.append(tk.Button(self.frame1,height=2, text=e, font=("Courier", QUESTION_FONT_SIZE, "bold")))
            


    def layout(self):
        self.frame1.pack(padx=50)
        self.quiz_name.pack(fill="x", expand=1)

        self.frame2.pack(fill="x")
        self.score_frame.pack(side="left", fill="x", expand=1)
        self.q_num_label.pack(side="left", fill="x", expand=1)
        self.score.pack(side="left", fill="x",expand=1)
        self.percent_label.pack(side="left", fill="x",expand=1)

        
        self.textbox.pack(pady=10)
        self.resize_text_widget()

        


        for e in self.choice_buttons:
            e.pack(fill="x",pady=5)


    def resize_text_widget(self, event=None):
        num_lines = int(self.textbox.index('end-1c').split('.')[0])

        self.textbox.config(height=max(num_lines, 10))

# class QuizSelectPage(tk.Frame):

#     def __init__(self, parent):
#         super().__init__(parent)
#         self.parent = parent
#         self.configure(bg = BG_COLOR)

#         # self.buttons =[]
#         self.options = [
#             "Operators",
#             "Strings",
#             "Conditionals", 
#             "Functions"
#         ]



#         self.create()
#         self.layout()



#         self.grid(row=0, column=0, sticky="nsew")

    
#     def create(self):
#         self.label = tk.Label(self, text = "SELECT A QUIZ TO TAKE.", font=("Courier", 36), bg = BG_COLOR)
        
#         self.dropdown = ttk.Combobox(self, values=self.options)
#         self.dropdown.set("Select a Quiz")

#     def layout(self):
#         self.label.pack(fill="x")
#         self.dropdown.pack()


    
    # def create_widgets(self):
    #     self.label = tk.Label(self, text = "SELECT A QUIZ TO TAKE.", font=("Courier", 36), bg = BG_COLOR)
    #     self.btnframe = tk.Frame(self, bg=BG_COLOR)
    #     for n in range(57):
    #         self.buttons.append(tk.Button(self.btnframe, text=f"Button{n+1}", height=2))
                

    # def draw_widgets(self):
    #     self.label.pack(fill="x", expand = 1)
    #     self.btnframe.pack(fill="both", expand = 1)


    #     for i in range(len(self.buttons)//5 + 1):
    #         self.btnframe.grid_rowconfigure(i, weight=1)
    #         for j in range(5):
    #             if i * 5 + j >= len(self.buttons):
    #                 return
    #             self.buttons[i*5+j].grid(row=i, column=j,sticky="nsew", padx=5,pady=5)
    #             self.btnframe.grid_columnconfigure(j, weight=1)
        


    

if __name__ == "__main__":
    App()


