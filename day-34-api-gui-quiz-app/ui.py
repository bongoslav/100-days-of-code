from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # passing the QuizBrain object - expecting QuizBrain data type
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,  # a bit less than 300
                                                     font=("Arial", 20, "italic"),
                                                     text="Text",
                                                     fill=THEME_COLOR)
        self.canvas.grid(columnspan=2, column=0, row=1, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.pressed_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.pressed_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            # updating the score
            self.score_label.config(text=f"Score: {self.quiz.score}")  # .quiz - the quizbrain (line 8);
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.true_button.config(state="disabled")  # disabling the buttons at the end of the game
            self.false_button.config(state="disabled")

    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def pressed_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)  # the same as pressed true

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")  # we can't use time module bc window.mainloop()
        else:
            self.canvas.config(bg="red")
        self.window.after(300, self.get_next_question)