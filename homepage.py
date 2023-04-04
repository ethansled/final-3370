import tkinter as tk

# Create a new window
root = tk.Tk()
root.title("Homepage Workout App")
root.geometry("400x700")

# Define the function for button 1
def open_file1():
    import test1 # Import the other Tkinter file
    test1.main() # Call the main function from file1

# Define the function for button 2
def open_file2():
    import file2 # Import the other Tkinter file
    file2.main() # Call the main function from file2
    
# Define the function for button 3
def open_file3():
    import file3 # Import the other Tkinter file
    file3.main() # Call the main function from file2
    
# Define the function for button 4
def open_file4():
    import file4 # Import the other Tkinter file
    file4.main() # Call the main function from file2

# Create two buttons to access the other Tkinter files
button1 = tk.Button(root, text="Open File 1", command=open_file1)
button1.pack(padx=100)

button2 = tk.Button(root, text="Open File 2", command=open_file2)
button2.pack(pady=100)

button3 = tk.Button(root, text="Open File 3", command=open_file3)
button3.pack(padx=100)

button4 = tk.Button(root, text="Open File 4", command=open_file4)
button4.pack(pady=100)

# Run the window
root.mainloop()
