from data import question_data
from question import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
  question_text = question["text"]
  question_answer = question["answer"]
  new_question = Question(text=question_text, answer=question_answer)
  question_bank.append(new_question)

brain = QuizBrain(question_bank)

while(brain.still_has_question()):
  brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {brain.score}/{brain.question_number}")







