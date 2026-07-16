# === 1. Mini exercise ===
print("Exercise 1 - Mini exercise:")
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
