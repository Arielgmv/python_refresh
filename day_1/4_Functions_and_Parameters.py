# === Practice 1: Basic Parameters (The Math Blender) ===
# 'hours_a' and 'hours_b' are our parameters (the ingredients)
def calculate_total_study(hours_a: int, hours_b: int) -> int:
    total = hours_a + hours_b
    return total 

# Now we "call" the function and pass in our actual data
tech_hours = calculate_total_study(2, 2)
english_hours = calculate_total_study(2, 1)
leetcode_hours = calculate_total_study(1, 1)

print("\nPractice 1: Basic Parameters (The Math Blender)")
print(f"Tech study today: {tech_hours}")
print(f"English study today: {english_hours}")
print(f"Leet Code study today: {leetcode_hours}")

# === Practice 2: Passing Lists into Functions ===
# 'my_list' is the parameter. Python expects a list to be passed here.
def print_all_items(my_list: list):
    print("\n--- Here is your list ---")
    for item in my_list:
        print(f"👉 {item}")
    # Notice there is no 'return' here. Functions can just DO things, 
    # like printing, without giving data back!

# Let's test it with different lists
morning_routine = ["wake up", "drink coffee", "write code"]
groceries = ["apples", "milk", "bread"]

print("\nPractice 2: Passing Lists into Functions")
print_all_items(morning_routine)
print_all_items(groceries)

# === Practice 3: Parameters + Control Flow ===
def get_category_emoji(task_text: str) -> str:
    # We check the parameter 'task_text' for specific words
    if "@work" in task_text:
        return "📁"
    elif "@home" in task_text:
        return "🏠"
    elif "@urgent" in task_text:
        return "🚨"
    else:
        return "📥"
    
# Testing the function
task1 = "Finish the API endpoint @work"
task2 = "Call mom @home"

# We pass the tasks in, and save the returned emoji into a variable
emoji1 = get_category_emoji(task1)
emoji2 = get_category_emoji(task2)

print("\nPractice 3: Parameters + Control Flow")
print(f"{emoji1} {task1}")
print(f"{emoji2} {task2}")

# === Training 1: Returning Calculated Data ===
# Write a function that takes your total_goal and subtracts your completed_hours, returning the remaining hours.
def calculate_remaining_hours(total_goal: int, completed_hours: int) -> int:
    remaining_hours = total_goal - completed_hours
    return remaining_hours

left_to_study = calculate_remaining_hours(4, 2)

print("\nTraining 1: Returning Calculated Data")
print(f"You have {left_to_study} hours left to study today.")

# === Training 2: Passing Lists into Functions ===
# Loop through the provided list and use an if statement to print the task only if the word "urgent" is inside it.
def get_urgent_tasks(my_list: list):    
    for item in my_list:
        if "@urgent" in item:            
            print(f"{item}")

python_tasks = ["functions, @urgent", "lists", "control flow, @urgent"]
sql_tasks = ["selects, @urgent", "order by"]

print("\nTraining 2: Passing Lists into Functions")
print("--- Here is your list with urgent activities ---")
get_urgent_tasks(sql_tasks)

# === Training 3: Parameters + Control Flow ===
# Take a string representing a priority level and return a number (1 for high, 2 for medium, 3 for low)
def get_priority(priority_text: str) -> int:
    if "@high" in priority_text:
        return 1
    elif "@medium" in priority_text:
        return 2
    elif "@low" in priority_text:
        return 3
    else:
        return 4 # A fallback number for untagged tasks

text1 = "Finish the Python basics @high"
text2 = "Start with the Leetcode @medium"

priority1 = get_priority(text1)
priority2 = get_priority(text2)

print("\nTraining 3: Parameters + Control Flow")
print(f"Priority {priority1}: {text1}")
print(f"Priority {priority2}: {text2}")


# === 1. Mini exercise ===
print("\nExercise 1 - Mini exercise:")
def count_done_tasks(tasks):
    done = 0
    for t in tasks:
        if t["done"]:
            done +=1
    return done

tasks = [
    {"text": "review Python", "done": True},
    {"text": "practice SQL", "done": False},
    {"text": "practice English", "done": True},
]
print("Completed tasks:", count_done_tasks(tasks))

# === Exercise 2. The Factory (Multiple parameters & returning a dict)===
# The ': str' and '-> dict' are Type Hints. They don't change how the code runs, 
# but they help your code editor auto-complete and catch bugs!
def create_task(text: str, priority: str = "normal") -> dict:
    new_task = {
        "text": text,
        "priority": priority,
        "done": False # New tasks are never done by default
    }
    return new_task

# Using the default priority
task1 = create_task("Read FastAPI docs")

# Overriding the default priority
task2 = create_task("Fix server crash", priority="urgent")

print("\nExercise 2. The Factory (Multiple parameters & returning a dict")
print(task1)
print(task2)

# Loop over actual task objects (not the function!)
for task in [task1, task2]: # ✅ Now iterating over a list of tasks
    print(f"{task['text']} - Priority: {task['priority']}, Done: {task['done']}")

# === Exercise 3. The Filter (List in -> List out) ===
def get_pending_tasks(task_list: list) -> list:
    pending_tasks = [] # Create an empty bucket

    for t in task_list:
        if t["done"] == False: # Or simply: if not t["done"]:
            pending_tasks.append(t) # Toss it in the bucket
    
    return pending_tasks

database = [
    {"text": "review Python", "done": True},
    {"text": "practice SQL", "done": False},
    {"text": "write endpoints", "done": False},
    {"text": "practice English", "done": False}
]

# Save the returned list into a new variable
to_do_list = get_pending_tasks(database)
print("\nExercise 3: The Filter (List in -> List out) - Pending tasks")
print(f"You have {len(to_do_list)} tasks left to do.")

# === Exercise 4. The Target Level (parse_note_to_tasks) ===
def parse_note_to_tasks(raw_note: str) -> list:
    extracted_tasks = []

    for line in raw_note.splitlines():
        line = line.strip()

        if line.startswith("-"):
            # line[2:] chops off the first two characters ("- ") so we just get the text
            clean_text = line[2:].strip()

            # Use our factory logic from Example 1!
            task_dict = {"text": clean_text, "done": False}
            extracted_tasks.append(task_dict)
    return extracted_tasks

# --- Let's test it ---
my_daily_note = """
Brain dump for today:
- finish the python regresh
- read about FastAPI routing
Remember to drink water!
"""

parsed_data = parse_note_to_tasks(my_daily_note)
print("\nExercise 4. The Target Level (parse_note_to_tasks)")
print(parsed_data)