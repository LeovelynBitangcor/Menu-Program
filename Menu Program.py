print("HELLO STUDENTS!")

print("""
What shift are you?

A. Shift A
B. Shift B
C. Shift C
""")

shift = input("=>")

if shift == "A":
    day = input("""  What day is today?
    A. Monday
    B. Tuesday
    C. Wednesday
    D. Thursday
    E. Friday
    F. Saturday
    G. Sunday
    
    =>""")
     
    if day == "A" or day == "B":
          b = input("DID YOU WEAR YOUR SCHOOL UNIFORM AND ID?                                         1. Yes  2. No              =>"  )
          if b == "1":
               print("You may now enter the School Campus.")
          else:
               print("You ARE NOT ALLOWED to enter the School Campus.")
    elif day == "C":
         c = input("DID YOU WEARu YOUR WASHING DAY OUTFIT AND ID?                                          1. Yes  2. No         => ")
         if c == "1":
              print("You may now enter the School Campus.")
         elif c == "2":
              print("You CAN STILL enter the School Campus.")
    else:
         print("You ARE NOT ALLOWED to enter the School Campus.") 

elif shift == "B":
    day = input(""" What day is today?
    A. Monday
    B. Tuesday
    C. Wednesday
    D. Thursday
    E. Friday
    F. Saturday
    G. Sunday
     

=>""")
     
    if day == "D" or day == "E" or day == "F":
         d = input("DID YOU WEAR YOUR SCHOOL UNIFORM AND ID?                            1. Yes   2. No  ")
         if d == "1":
              print("You may now enter the School Campus.")
         else:
              print("You ARE NOT ALLOWED to enter the School Campus.")
    else: 
         print("You ARE NOT ALLOWED to enter the School Campus.")

elif shift == "C":
    day = input(""" What day is today?
    A. Monday
    B. Tuesday
    C. Wednesday
    D. Thursday
    E. Friday
    F. Saturday
    G. Sunday
    
  =>""")
     
    if day == "A" or day == "B" or day == "G":
          b = input("DID YOU WEAR YOUR SCHOOL UNIFORM AND ID?                            1. Yes  2. No  ")
          if b == "1":
               print("You may now enter the School Campus.")
          else:
               print("You ARE NOT ALLOWED to enter the School Campus.")
    else: 
         print("You ARE NOT ALLOWED to enter the School Campus.")
else: 
     print("Invalid")