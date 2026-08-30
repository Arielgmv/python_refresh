# === Exercise 5.8: The Data Grouping ===
"""
The Goal:
You have a list of task dictionaries, and each task has a "category" (like "Work" or "Personal"). Write a function that groups these tasks into a new dictionary.
The keys of the new dictionary should be the category names.
The values should be a list of the tasks that belong to that category.
Rules:
1. Do NOT use any advanced Python tools. Just standard loops and dictionaries.
2. Create an empty dictionary at the start: grouped_tasks = {}.
3. Loop through the task_list.
4. Get the "category" from the task using .get(). If it's missing, default to "Other".
5. The tricky part: Before you append the task to the list for that category, you must check if the category already exists in your grouped_tasks dictionary. If it doesn't exist yet, you need to create an empty list for it first!
6. Append the task to the correct list.
7. Return the grouped_tasks dictionary.
"""
def list_task_dictionaries(task_list: list[dict]) -> dict:
    grouped_tasks = {}
    for task in task_list:
        category = task.get("category", "Other")
        if category not in grouped_tasks:
            grouped_tasks[category] = []
        grouped_tasks[category].append(task)
    return grouped_tasks

# --- Test your function ---
my_tasks = [
    {"text": "Fix bug", "category": "Work"},
    {"text": "Buy milk", "category": "Personal"},
    {"text": "Write email", "category": "Work"},
    {"text": "Walk the dog", "category": "Personal"},
    {"text": "Mystery task"}
]

grouped = list_task_dictionaries(my_tasks)

print ("\n Exercise 5.8: The Data Grouping")
for category, tasks in grouped.items():
    print(f"\n{category}")
    for t in tasks:
        #print(t)
        print(f" - {t["text"]}")

# === Exercise 5.9: The Mini Data Pipeline ===
"""
The Goal:
Write a single function process_task_pipeline(raw_tasks: list[dict]) -> dict[str, list[str]] that does three things in order:
1. Filter: Ignore any task that doesn't have a "text" key (invalid data).
2. Transform: Convert the task's "category" to lowercase (e.g., "Work" becomes "work") so they group nicely. If it has no category, default to "other".
3. Group: Group the valid, transformed tasks by their new lowercase category. Instead of returning the whole dictionary, just return a list of the task texts for each category.
Rules:
Use standard for loops and if statements.
Use .get() to safely check for keys.
Return a dictionary where keys are categories and values are lists of strings (task texts).
"""


# --- Test your function ---
messy_raw_data = [
    {"text": "Fix bug", "category": "Work"},
    {"text": "Buy milk", "category": "PERSONAL"}, # Uppercase!
    {"category": "Work"}, # Missing text! (Should be filtered out)
    {"text": "Write email", "category": "work"},
    {"text": "Walk the dog", "category": "Personal"},
    {"text": "Mystery task"} # Missing category! (Should become "other")
]

print("\nExercise 5.9: The Mini Data Pipeline")
grouped_tasks = {}
for task in messy_raw_data:    
    if "text" in task:
        category = task.get("category", "other").lower()
        if category not in grouped_tasks:
            grouped_tasks[category] = []
        grouped_tasks[category].append(task)

print(grouped_tasks)
for category, tasks in grouped_tasks.items():
    print(f"\n{category}:")
    for t in tasks:
        print(f" - {t["text"]}")