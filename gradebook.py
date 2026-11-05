
def gradebook():
    student_gradebook = {"Max" == "90", "Peter" == "87", "Kid" == "67"}


    question = input("Give me a student name!")

 
 
 
    if student_gradebook.get(question):
        print(question, "grade = ", student_gradebook(question))

    else:
        print("Student not found")
 
 






gradebook()