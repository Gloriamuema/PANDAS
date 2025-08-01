for number in range(1, 11):
    print(number)
    
   # infinite loop
while True:
    numbers = input("Enter a number: ")
    
    if numbers.lower() == 'stop':
        print("Stopped.")
        # Exit the loop
        break  
    
    print("You entered:", numbers) 
    
    
    