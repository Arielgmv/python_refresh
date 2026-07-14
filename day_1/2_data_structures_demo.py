# === 1. Simple list operations ===
# Creating a list of tasks
tasks = ["wake up", "drink coffe", "write code"]
print("Initial tasks:", tasks)

# Accessing an item by its index
print(tasks[0])

# Adding a new item to the end of the list
tasks.append("take a break")
print("After appending:", tasks)

# Iterate and print
print("\nAll tasks:")
for task in tasks:
    print(task)

# === 2. Dictionaries: The Key-Value Store ===
# Creating a dictionary for a specific user
user = {"name": "Alice", "role": "Admin", "active": True}

print("\nValues in the dictionary")
print("Initial Values:", user)

# Accessing data using the key
print("\nAccessing data using the key")
print(f"The user is {user["name"]}, role: {user["role"]}, active status: {user["active"]}")

# Updating an existing value or adding a new one
user["active"] = False
user["last_login"] = "Today"

print("\nUpdated values in the dictionary")
print("Updated values:", user)

# === 3. For Loops: The Iteration Engine ===
fruits = ["apple", "banana", "cherry"]

print("\nThe For loop")
for item in fruits:
    print(item)

# === 4. List of dictionaries (structured tasks) ===
# Data structures: lists & dictionaries
# tasks is a list ([]) that acts as a container
# Inside that container, each individual item is a dictionary ({}), which stores the specific metadata ("text" and "done") for a single task
task_list = [
    {"text": "review functions", "done": True},
    {"text": "run FastAPI health check", "done": False},
]

print("\nStructured tasks:")
for t in task_list:
    status = "✅" if t["done"] else "⏳"
    print(f"{status} {t['text']}")

# === 5. The List of Dictionaries (other example) ===
# A list containing multiple dictionaries
project_tasks = [
    {"title": "Design database", "status":"Done"},
    {"title": "Write API", "status":"In Progress"},
    {"title": "Deploy to server", "status":"Pending"}
]

# Looping through the list
print("\nAnother Structured tasks")
for task in project_tasks:
    print(f"Task: {task['title']} | Current Status: {task['status']}")

# Adding boolean done status to project_tasks dictionary
for task in project_tasks:
    task["done"] = (task["status"] == "Done")

# Looping through the updated list
print("\nAnother updated Structured tasks")
for task in project_tasks:
    print(f"Task: {task['title']} | Current Status: {task['status']} | Done: {task['done']}")

print("\nProject tasks with boolean 'done':")
for t in project_tasks:
    emoji = "✅" if t["done"] else "⏳"
    print(f"{emoji} {t['title']} - Status: {t['status']}")