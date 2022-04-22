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
        self.question_text = self.canvas.create_text(
            150, 125, text='Some question text', fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tkinter.PhotoImage(
            file='projects/trivia-quiz-app/images/true.png')
        false_image = tkinter.PhotoImage(
            file='projects/trivia-quiz-app/images/false.png')
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0)
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
