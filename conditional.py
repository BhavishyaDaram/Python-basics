# #ACCEPT TWO NUMBERS PRINT GREATEST BTW THEM
# num1=int(input("please tell your first number: "))
# num2=int(input("please tell your second number: "))
# if(num1>num2):
#     print(num1)
# elif(num2>num1):
#     print(num2)
# else:
#     print("both the numbers are same")
year = int(input("tell your year:"))
if year%100==0 and year%400==0:
    print("its a leap year")
elif year%100!=0 and year%4==0:
    print("its a leap year")
else:
    print("Normal year")

    