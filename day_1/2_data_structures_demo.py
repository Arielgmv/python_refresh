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

# === 2. List of dictionaries (structured tasks) ===
# Data structures: lists & dictionaries
# tasks is a list ([]) that acts as a container
# Inside that container, each individual item is a dictionary ({}), which stores the specific metadata ("text" and "done") for a single task
task_list = [
    {"text": "review functions", "done": False},
    {"text": "run FastAPI health check", "done": True},
]

print("\nStructured tasks:")
for t in task_list:
    status = "✅" if t["done"] else "⏳"
    print(f"{status} {t['text']}")



# Estoy en Gemini - Python Chat - 2. Dictionaries: The Key-Value Store