from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TEXT_AREA_FONT = ("Arial", 20, "italic")
SCORE_LABEL_FONT = ("Arial", 15)


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        def get_next_question():
            if self.quiz.still_has_questions():
                self.score_label.config(text=f"Score: {self.quiz.score}")
                question_text = self.quiz.next_question()
                self.canvas.itemconfig(self.text_area, text=question_text)
            else:
                self.canvas.itemconfig(self.text_area, text="You've reached the end.")
                self.true_button.config(state="disabled")
                self.false_button.config(state="disabled")

        def is_correct():
            feedback_and_next(self.quiz.check_answer("True"))

        def is_incorrect():
            feedback_and_next(self.quiz.check_answer("False"))

        def feedback_and_next(user_is_right: bool):

            def default_and_next():
                self.canvas.config(bg="white")
                get_next_question()

            if user_is_right:
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")

            self.window.after(ms=1000, func=default_and_next)

        # Windows settings
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # File images
        self.false_button_img = PhotoImage(file="images/false.png")
        self.true_button_img = PhotoImage(file="images/true.png")

        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.text_area = self.canvas.create_text(
            150,
            125,
            text="",
            fill=THEME_COLOR,
            font=TEXT_AREA_FONT,
            width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        # Buttons and label
        self.false_button = Button(image=self.false_button_img, highlightthickness=0, command=is_incorrect)
        self.false_button.grid(row=2, column=0)

        self.true_button = Button(image=self.true_button_img, highlightthickness=0, command=is_correct)
        self.true_button.grid(row=2, column=1)

        self.score_label = Label(text=f"Score: {0}", bg=THEME_COLOR, fg="white", font=SCORE_LABEL_FONT)
        self.score_label.grid(row=0, column=0, columnspan=2)

        get_next_question()

        self.window.mainloop()
