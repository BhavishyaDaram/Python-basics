def palindrome(st):
 rev=""
 for i in range(len(st)-1,-1,-1):
    rev = rev + st[i]
 if rev ==st:
  print ("palindrome")
 else:
   print ("not a palindrome")

palindrome("NAMAN")
palindrome("cursor")