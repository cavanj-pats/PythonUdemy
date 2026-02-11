#challenge_StudentDetails.py
#                              The only twist is saving to a file is required.
#                              using a process called pickle which is a serialization technique

import string
import pickle


class Student():
    
    def __init__(self, stud_id, name, grades):
        self.studentID = stud_id
        self.name = name
        self.grades = (grades)   #just to make certain it is a dictionary


    def __repr__(self):
        #print the object

        str = (self.studentID) + " " + (self.name) +"\n"
        for key, grade in self.grades.items():
            str += f"{key} Grade: {grade} \n"

        return str


def save(student):
    #pickle is saving  
    with open('Student.data', 'wb') as file:
        pickle.dump(student, file)

def load():
    #unpickle
    with open('Student.data', 'rb') as file:
        return pickle.load(file)

if __name__ == "__main__":
    #pass  #complete details later
    joe = Student('S001', 'Jim', {'Math': 90, 'Fluids': 78})

    save(joe)
  
    jim = load()  
    
    print(jim.__repr__())