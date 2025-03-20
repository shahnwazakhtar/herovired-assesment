
def main():
   
    input_string = input("Please enter a list of numbers, separated by spaces: ") 
    numbers = [int(num) for num in input_string.split()]  
    if not numbers:
        print("You didn't enter any numbers!")
        return
    largest_number = max(numbers)
    print(f"The largest number in the list is: {largest_number}")
if __name__ == "__main__":
    main()
