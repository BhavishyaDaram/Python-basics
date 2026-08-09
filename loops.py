#for loop to print 1 to 11
# for i in range(1,12,1):
#     print(i);
#
#to print 5 table
# for i in range(5,51,5):
#     print(i)
# to print any table 
# n=int(input("Which table you want?"))
# for i in range(n,(n*10)+1,n):
#     print(i);
# #LOOPS ON STRINGS
# a="Bhavishya"
# for i in range(len(a)):
#       print(a[i])
# while loop
# a=1
# while a<=30:
#     print(a)
#     a+=1  
# to extract last digits inorder
# a=256
# while a>0:
#     print(a%10)
#     a=a//10
# to extract reverse digits 
a=int(input("enter a number: "))
rev=0;
while a>0:
    reb=rev*10 +a%10
    a=a//10
if(rev==a):
        print("palindrome")
else:
        print("not a palindrome")