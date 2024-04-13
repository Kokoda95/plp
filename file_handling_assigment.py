# Open the new file and write on it
with open("my_file.txt", "w") as file:
    file.write("Hello! \n")
    file.write("My name is Kokoda. \n")
    file.write("I am 5.5ft tall.\n")

# Append some contents and then read the file.   
with open("my_file.txt", "a") as file:
    file.write("I like travelling. \n")
    file.write("I also like listening stories. \n")
    file.write("My goal is to create application. \n")
    # Move the cursor to the beginning of the file.
    file.seek(0)
    # Get the file mode
    mode = file.mode
    # Read all lines of the file.
    try:
       lines = file.readlines()
    except:
        print(f"Error! occured, the mode of the file is: {mode}.")
    # Print each line
    else:
        for line in lines:
            print(line.strip())
    finally:
        # List of modes allow reading
        modes = ['r', 'r+', 'w+', 'a+']
        # Check if mode of file exists in the list
        if mode in modes:
            print("Thank you for reading the file!!!")        
        else:
            print("The file mode does not allow reading.")
