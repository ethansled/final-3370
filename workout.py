import tkinter as tk
from tkinter import ttk
from workout import Workout


# Define the main window
root = tk.Tk()
root.title("Workout Manager")
root.geometry("400x700")
#Set the background color
root.configure(bg = "#e4f5ec")
#Configuring the background color
input_frame = tk.Frame(root)
input_frame.config(bg=root["bg"])
input_frame.pack()

# Define a function to log the workout
def log_workout():
    exercise = exercise_entry.get()
    reps = reps_entry.get()
    weight = weight_entry.get()
    #workout1 = Workout(exercise, reps, weight)
    workout_text.insert(tk.END, f"Exercise Name: {exercise}, Amount of Reps: {reps}, Weight (if applicable): {weight}")
    #------ For writing the workouts to a txt file, could help when we want to make a database. 
    with open("workouts.txt", "a") as f:
        f.write(f"Exercise: {exercise}, Reps: {reps}, Weight: {weight}\n")
    exercise_entry.delete(0, tk.END)
    reps_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
#Function to generate workout that is pre made 
#--------This will have to access the database when it is created------------
def generate_workout():
    return 


# Define the input fields for the exercise, reps, and weight
exercise_label = ttk.Label(root, text="Exercise:")
exercise_entry = ttk.Entry(root, width=30)
reps_label = ttk.Label(root, text="Reps:")
reps_entry = ttk.Entry(root, width=30)
weight_label = ttk.Label(root, text="Weight (lbs):")
weight_entry = ttk.Entry(root, width=30)
workout_title_text = ttk.Label(root, text = "Current Workout:")


# Define the log button and its functionality
log_button = ttk.Button(root, text="Add Workout", command=log_workout)
generate_button = ttk.Button(root, text= "Generate Pre-Made Workout", command = generate_workout())
#To generate the text for workouts 
workout_text = tk.Text(root, height=20, width=100)

# Pack the input fields and log button onto the window
exercise_label.pack(pady=10)
exercise_entry.pack(pady=10)
reps_label.pack(pady=10)
reps_entry.pack(pady=10)
weight_label.pack(pady=10)
weight_entry.pack(pady=10)
log_button.pack(pady=20)
generate_button.pack(pady = 20)
workout_title_text.pack(pady = 20)
workout_text.pack(pady=10)
#Trying to interact with the class
#print(workout1.get_workout_info())

# Run the main loop
root.mainloop()