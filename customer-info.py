import tkinter as tk

# Define the main window of the application
root = tk.Tk()
root.title("User Information")

# Set window size
root.geometry("800x800")

# Set background color
root.configure(bg="#e4f5ec")

# Create a frame to contain the input fields
input_frame = tk.Frame(root)
input_frame.config(bg=root["bg"])
input_frame.pack()

title_label = tk.Label(input_frame, text="User Registration Form", font=("arial bold", 20), bg=root["bg"])  

# Create labels and entry fields for each piece of information
fname_label = tk.Label(input_frame, text="First Name: ", font=("arial", 12), bg=root["bg"])
fname_entry = tk.Entry(input_frame)

lname_label = tk.Label(input_frame, text="Last Name: ", font=("arial", 12), bg=root["bg"])
lname_entry = tk.Entry(input_frame)

phone_label = tk.Label(input_frame, text="Phone Number: ", font=("arial", 12), bg=root["bg"])
phone_entry = tk.Entry(input_frame)

email_label = tk.Label(input_frame, text="Email Address: ", font=("arial", 12), bg=root["bg"])
email_entry = tk.Entry(input_frame)

gender_label = tk.Label(input_frame, text="Gender: ", font=("arial", 12), bg=root["bg"])
gender_entry = tk.Entry(input_frame)

address_label = tk.Label(input_frame, text="Address: ", font=("arial", 12), bg=root["bg"])
address_entry = tk.Entry(input_frame)

weight_label = tk.Label(input_frame, text="Weight (lbs):", font=("arial", 12), bg=root["bg"])
weight_entry = tk.Entry(input_frame)

height_label = tk.Label(input_frame, text="Height (cm):", font=("arial", 12), bg=root["bg"])
height_entry = tk.Entry(input_frame)

age_label = tk.Label(input_frame, text="Age: ", font=("arial", 12), bg=root["bg"])
age_entry = tk.Entry(input_frame)



# Add the labels and entry fields to the frame
title_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
fname_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
fname_entry.grid(row=1, column=1, padx=5, pady=5)

lname_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
lname_entry.grid(row=2, column=1, padx=5, pady=5)

phone_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
phone_entry.grid(row=3, column=1, padx=5, pady=5)

email_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
email_entry.grid(row=4, column=1, padx=5, pady=5)

gender_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
gender_entry.grid(row=5, column=1, padx=5, pady=5)

address_label.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
address_entry.grid(row=1, column=3, padx=5, pady=5)

weight_label.grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)
weight_entry.grid(row=2, column=3, padx=5, pady=5)

height_label.grid(row=3, column=2, padx=5, pady=5, sticky=tk.W)
height_entry.grid(row=3, column=3, padx=5, pady=5)

age_label.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)
age_entry.grid(row=4, column=3, padx=5, pady=5)

# Create a function to handle the button click event
def submit_info():
    if not fname_entry.get() or not lname_entry.get() or not phone_entry.get() or not gender_entry.get() or not address_entry.get() or not weight_entry.get() or not height_entry.get() or not age_entry.get():
        error_label.config(text="Please Ensure All Fields Are Filled", fg="red")
        return
    
    try:
        customer_weight = int(weight_entry.get())
    except ValueError:
        error_label.config(text="Enter A Valid Weight In Pounds", fg="red")
        return
    
    try:
        customer_height = int(height_entry.get())
    except ValueError:
        error_label.config(text="Enter A Valid Height In Centimeters", fg="red")
        return
    
    try:
        customer_age = int(age_entry.get())
    except ValueError:
        error_label.config(text="Enter a Valid Age", fg="red")
        return
    
    customer_phone = phone_entry.get()
    if not customer_phone.isdigit():
        error_label.config(text="Please Enter a Valid Phone Number", fg="red")
        return
    
    customer_email = email_entry.get()
    if "@" not in customer_email or "." not in customer_email:
        error_label.config(text="Please Enter a Valid Email Address", fg="red")
        return
    
    # All entries are valid, submit form
    customer_fname = fname_entry.get()
    customer_lname = lname_entry.get()
    customer_phone = phone_entry.get()
    customer_email = email_entry.get()
    customer_gender = gender_entry.get()
    customer_address = address_entry.get()
    customer_weight = int(weight_entry.get())
    customer_height = int(height_entry.get())
    customer_age = int(age_entry.get())
    
    # Do something with the user's information (Print to console)
    print(f"First Name: {customer_fname}")
    print(f"Last Name: {customer_lname}")
    print(f"Phone: {customer_phone}")
    print(f"Email: {customer_email}")
    print(f"Gender: {customer_gender}")
    print(f"Address: {customer_address}")
    print(f"Weight (lbs): {customer_weight}")
    print(f"Height (cm): {customer_height}")
    print(f"Age: {customer_age}")

    # Clear entries and error label updated
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    error_label.config(text="Form Successfully Submitted. Closing Window...", fg="green")
    #close the screen 4 seconds after the button is pressed
    root.after(4000, root.destroy)
    #Write to text doc. 
    with open("customers.txt", "a") as f:
        f.write(f"\nFirst Name: {customer_fname}\nLast Name: {customer_lname}\nPhone: {customer_phone}\nGender: {customer_gender}\nAddress: {customer_address}\nWeight: {customer_weight}\nHeight: {customer_height}\nAge: {customer_age}\n---------------")



# Add a label to display errors to the user
error_label = tk.Label(root, text="", fg="red", font=("arial",12), bg=root["bg"])
error_label.pack()

# Add a button to submit the information
submit_button = tk.Button(root, text="Submit", font=("arial",10), command=submit_info, relief="raised", borderwidth=5, fg="white", bg="grey", padx=5, pady=5)
submit_button.pack(pady=10)

# Start the application
root.mainloop()