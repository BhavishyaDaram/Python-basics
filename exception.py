# a=int(input("tell your number :- "))
# try:
#     print(10/a)
# except Exception as err:
#     print("Sorry you cannot divide by zero")
# else:
#     print("good there is no exception")
# finally:
#     print("I will run no matter what ")

# print("ok I have done the division")

a=int(input("tell your number :- "))
try:
    if age < 10 or age >18:
     raise ValueError("your agemust be between 10 and 18")
    else:
     print("welcome to the club")
except Exception as err:
  print(f"an error occured as {err}")
print("the club will start soon")