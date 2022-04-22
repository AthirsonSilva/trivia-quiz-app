import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    '''
    Quiz interface class

    Models the graphical user interface
    of the software
    '''

    def __init__(self, quiz_brain: QuizBrain) -> None:
        '''
        Attributes

        Class attributes
        '''

        self.quiz = quiz_brain
        self. window = tkinter.Tk()
        self.window.title('Quizzle')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = tkinter.Label(
            text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125, width=200, text='Some question text', fill=THEME_COLOR, font=('Arial', 20, 'bold'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tkinter.PhotoImage(
            file='projects/trivia-quiz-app/images/true.png')
        false_image = tkinter.PhotoImage(
            file='projects/trivia-quiz-app/images/false.png')
        self.true_button = tkinter.Button(
            image=true_image, highlightthickness=0, command=self.check_true)
        self.false_button = tkinter.Button(
            image=false_image, highlightthickness=0, command=self.check_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def check_true(self) -> None:
        '''
        Calls the check_answer function

        Gets the True input from the user through
        the buttons on the UI and calls the QuizBrain class
        function with the True argument
        '''
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def check_false(self) -> None:
        '''
        Calls the check_answer function

        Gets the False input from the user through
        the buttons on the UI and calls the QuizBrain class
        function with the False argument
        '''

        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool) -> None:
        '''
        Feedback giving

        Gives the user a graphical feedback based
        if they get the answer right or wrong

        Args:
            is_right (bool): The return of the QuizBrain check_answer function
        '''

        if is_right:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')

        self.window.after(500, self.get_next_question())

    def get_next_question(self) -> None:
        '''
        Next question getter

        Get's the next question from he quiz brain class
        '''
        # self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.config(bg='white')
            self.canvas.itemconfig(self.question_text, text='You have reached the of the quiz')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')