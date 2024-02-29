#!/usr/bin/env python
# coding: utf-8

# In[6]:


while(1):
    print("-----------------------------------------")
    print("Simple Calculator")
    print("-----------------------------------------")
    print("Operations:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Power")
    print("6: Percentage")
    print("7: Exit")
    print("-----------------------------------------")
    operation=input("Enter Operation 1 or 2 or 3 or 4 or 5 or 6 or 7\n")
    if operation == '7':
        print("-----------------------------------------")
        print("🙋‍♂️SIGNING OFF🙋‍♂️")
        break    
    elif operation== '6':
        n1=float(input("Enter Percentage \n"))
        n2=float(input("Enter a Number \n"))
        result = (n1*n2)/100
        print("===============🔎ANSWER🔍===============")
        print(f"{n1} % of {n2} = {result}")
        continue
        
        
    n1=float(input("Enter a Number \n"))
    n2=float(input("Enter a Number \n"))
    if operation == '1':
        result = n1+n2
        print("===============🔎ANSWER🔍===============")
        print(f"{n1} + {n2} = {result}")
    elif operation == '2':
        result = n1-n2
        print("===============🔎ANSWER🔍===============")
        print(f"{n1} - {n2} = {result}")
    elif operation == '3':
        result = n1*n2
        print("===============🔎ANSWER🔍===============")
        print(f"{n1} * {n2} = {result}")
    elif operation == '4':
        result = n1/n2
        print("===============🔎ANSWER🔍===============")
        print(f"{n1} / {n2} = {result}")
    elif operation == '5':
        result = n1**n2
        print("===============🔎ANSWER🔍===============")
        print(f"{n1} power {n2} = {result}")
    else:
        print("Invalid operation. Please choose 1, 2, 3, 4, 5 or 6.")

        
    


# In[ ]:




