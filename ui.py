import tkinter

THEME_COLOR = "#375362"


class QuizInterface:
    '''
    Quiz interface class

    Models the graphical user interface
    of the software
    '''

    def __init__(self):
        self. window = tkinter.Tk()
        self.window.title('Quizzle')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = tkinter.Label(
            text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = tkinter.Canvas(width=300, height=250, bg='white')

        self.question_text = self.canvas.create_text(150, 125, text='Some question text', fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.window.mainloop()
