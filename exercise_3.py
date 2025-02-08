ls1 = [
    "How many World Cups does Brazil have?", ["A. 3", "B. 4", "C. 5", "D. 6"],
    "What is the capital of Canada?", ["A. Toronto", "B. Ottawa", "C. Vancouver", "D. Montreal"],
    "Which planet is known as the Red Planet?", ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    "Who wrote 'Romeo and Juliet'?", ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
    "What is the chemical symbol for gold?", ["A. Au", "B. Ag", "C. Pb", "D. Fe"],
    "Which programming language is known for web development?", ["A. Java", "B. C++", "C. Python", "D. JavaScript"],
    "Who painted the Mona Lisa?", ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
    "What is the largest ocean on Earth?", ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
    "Which country invented the pizza?", ["A. France", "B. Italy", "C. Greece", "D. USA"],
    "What is the square root of 144?", ["A. 10", "B. 12", "C. 14", "D. 16"]]


ls2 = ["C", "B", "B", "B", "A", "D", "C", "D", "B", "B"]

print("Welcome to KBC")
name=str(input("Enter your name: "))
age=int(input("Enter your age: "))
n=str(input("Enter S to start: "))

res=0

if(n=="S"):
    for i in range(0,20,2):
        print(ls1[i])
        print(ls1[i+1])
        ans=input()
        k=int(i/2)
        if(ans==ls2[k]):
            res=res+1
        else :
            break
else :
    print("Invalid Input!!")        

print("Your Total Income : ", res*1000000)