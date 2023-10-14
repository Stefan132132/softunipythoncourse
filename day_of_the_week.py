days_of_week = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
day = int(input())

if day in days_of_week:
    print(f"{days_of_week[day]}")
else:
    print("Error")













# a = int(input())

# if(a >= 1 and a <= 7):
#     if(a == 1):
#         print("Monday")
#     elif(a == 2):
#         print("Tuesday")
#     elif(a == 3):
#         print("Wednesday")
#     elif(a == 4):
#         print("Thursday")
#     elif(a == 5):
#         print("Friday")
#     elif(a == 6):
#         print("Saturday")
#     elif(a == 7):
#         print("Sunday")
# else:
#     print("Error")