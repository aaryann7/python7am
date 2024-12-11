student1 = input("Enter your name: ").capitalize()
st1Maths= int(input("Enter your marks in Maths "))
st1Science= int(input("Enter your marks in Science "))
st1English= int(input("Enter your marks in English "))

student2 = input("Enter your name: ").capitalize()
st2Maths= int(input("Enter your marks in Maths "))
st2Science= int(input("Enter your marks in Science "))
st2English= int(input("Enter your marks in English "))

student3 = input("Enter your name: ").capitalize()
st3Maths= int(input("Enter your marks in Maths"))
st3Science= int(input("Enter your marks in Science"))
st3English= int(input("Enter your marks in English"))

student4 = input("Enter your name: ").capitalize()
st4Maths= int(input("Enter your marks in Maths"))
st4Science= int(input("Enter your marks in Science"))
st4English= int(input("Enter your marks in English"))

student5 = input("Enter your name: ").capitalize()
st5Maths= int(input("Enter your marks in Maths"))
st5Science= int(input("Enter your marks in Science"))
st5English= int(input("Enter your marks in English"))



details = {
    student1 : {'Maths' : st1Maths, 'Science' : st1Science,  'English': st1English},
    student2 : {'Maths' : st2Maths, 'Science' : st2Science,  'English': st2English},
    student3 : {'Maths' : st3Maths, 'Science' : st3Science,  'English': st3English},
    student4 : {'Maths' : st4Maths, 'Science' : st4Science,  'English': st4English},
    student5 : {'Maths' : st5Maths, 'Science' : st5Science,  'English': st5English}

    
    }



choice = input("\nEnter name to see marks ").capitalize()

while choice != student1 or choice!= student2:
    print("Enter a valid name")
    choice = input("\nEnter name to see marks ").capitalize()
    


    if choice == student1:
        print(f"\nThe marks obtained by {choice} are  \nMaths = {details[student1]['Maths']}\nScience = {details[student1]['Science']}\nEnglish = {details[student1]['English']}")
        total_marks = details[student1]['Maths'] +  details[student1]['Science'] +  details[student1]['English']
        print(f"Total marks = {total_marks}")

    elif choice == student2:
        print(f"\nThe marks obtained by {choice} are  \nMaths = {details[student2]['Maths']}\nScience = {details[student2]['Science']}\nEnglish = {details[student2]['English']}")
        total_marks = details[student2]['Maths'] +  details[student2]['Science'] +  details[student2]['English']
        print(f"Total marks = {total_marks}")

    elif choice == student3:
        print(f"\nThe marks obtained by {choice} are  \nMaths = {details[student3]['Maths']}\nScience = {details[student3]['Science']}\nEnglish = {details[student3]['English']}")
        total_marks = details[student3]['Maths'] +  details[student3]['Science'] +  details[student3]['English']
        print(f"Total marks = {total_marks}")

    elif choice == student4:
        print(f"\nThe marks obtained by {choice} are  \nMaths = {details[student4]['Maths']}\nScience = {details[student4]['Science']}\nEnglish = {details[student4]['English']}")
        total_marks = details[student4]['Maths'] +  details[student4]['Science'] +  details[student4]['English']
        print(f"Total marks = {total_marks}")

    elif choice == student5:
        print(f"\nThe marks obtained by {choice} are  \nMaths = {details[student5]['Maths']}\nScience = {details[student5]['Science']}\nEnglish = {details[student5]['English']}")
        total_marks = details[student5]['Maths'] +  details[student5]['Science'] +  details[student5]['English']
        print(f"Total marks = {total_marks}")



    break