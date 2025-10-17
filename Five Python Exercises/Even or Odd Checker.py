def check_even_odd(number): #define function
    if number % 2 ==0: #if else statement
        return 'even'
    else:
        return 'odd'
    
num = int(input("Enter an integer: ")) #Get the input from user

result = check_even_odd(num) #calling the function
print(f"The number {num} is {result}. ") #print the result