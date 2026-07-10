
# a=0
# while a<=10:
#     print(a)
#     a+=1
user_input=int(input("Enter a Positive number : "))#taking input from user to print range of numbers
if user_input>=0:#this this checking user input is positive or negative
    a=0
    while a<=user_input:
        print(a)
        a+=1
else:#if the numbber is negavative this condition will be execute
    print("Enter valid number and only positive number")
