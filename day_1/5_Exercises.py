# === Exercise 1: The Task Completer ===
# Right now, you can create tasks, but you need a way to automatically check them off.
#The Goal: Write a function that takes a list of task dictionaries and a specific task name. It should loop through the list, find the task that matches the name, and change its "done" status to True.
def complete_task(task_list: list[dict], target_task_name: str) -> bool:
    for task in task_list: #Loop through 'task_list'
        if task["text"] == target_task_name: #Check if the dictionary's "text" key matches 'target_task_name'
            task["done"] = True #If it matches, set the dictionary's "done" key to True
            return True # Exit the function after updating the task
    return False # Return False if the task was not found

# --- Test your function ---
my_tasks = [
    {"text": "Read FastAPI docs", "done": False},
    {"text": "Write code", "done": False}
]

# Call the function to modify the list
success = complete_task(my_tasks, "Read FastAPI docs")
print("\nExercise 1: The Task Completer")
print("Updated tasks:", my_tasks) # "Read FastAPI docs" should now show "done": True!
print("Success:", success) # Should print True if the task was found and updated

# === Exercise 2: The form Completer ===
# You are a secretary with a stack of paper forms (the list). Each form has a title ("text") and a "Completed" checkbox ("done"). Your boss says: “Find the form with the title ‘Read FastAPI docs’ and check the box.” You flip through the forms. When you find the right one, you check the box (set done=True). You shout back “Done!” (return True).
# If you flip through all forms and don’t find it, you shout “Not found!” (return False). Because you changed the actual form (the dictionary), when your boss looks at the stack later, they see the checkbox is ticked. That's the mutation effect.
def complete_form(form_list: list[dict], target_form_title: str) -> bool:
    for form in form_list:
        if form["text"] == target_form_title:
            form["done"] = True
            return True
    return False

my_forms = [
    {"text": "Read FastAPI docs", "done": False},
    {"text": "Write code", "done": False}
]

success = complete_form(my_forms, "Read FastAPI docs")
print("\nExercise 2: The form completer")
print("Updated forms:", my_forms)
print("Success:", success)

# === Exercise 3: The Task Organizer ===
"""Instead of just filtering one type of task, let's separate a master list into two distinct buckets based on priority. The Goal: Pass a list of task dictionaries into a function. Return a new dictionary containing two lists: one for urgent tasks (priority 1) and one for everything else."""
def organize_tasks(task_list: list[dict]) -> dict[str, list[dict]]:
    """Separates tasks into 'high' and 'low' priority buckets."""
    urgent_bucket = []
    regular_bucket = []
    
    for task in task_list: # Loop through 'task_list'
        priority = task.get("priority") # .get() returns None if the key doesn't exist, preventing a crash
        if priority == 1: # If the dictionary's "priority" is 1, append it to 'urgent_bucket'
            urgent_bucket.append(task)
        else: #Else, append it to 'regular_bucket'
            regular_bucket.append(task)
    # TODO: Return a dictionary structured exactly like this: 
    # {"high": urgent_bucket, "low": regular_bucket}
    return {"high": urgent_bucket, "low": regular_bucket}

# --- Test your function ---
master_tasks = [
    {"text": "Fix crash", "priority": 1},
    {"text": "Learn Python", "priority": 2},
    {"text": "Call mom", "priority": 1},
    {"text": "Mystery task"} #Added to test the .get() safety!
]

organized = organize_tasks(master_tasks)
print("\nExercise 3 The Task Organizer")
# Using a loop to print it cleanly, or just print(organized)
for category, tasks in organized.items():
    print(f"\n{category.upper()} priority tasks:")
    for t in tasks:
        print(f" - {t['text']} (Priority: {t.get('priority', 'N/A')})")

# === Exercise 4: The Data Enricher (Feature Engineering) ===
"""
Context: You have a raw list of tasks. Before sending this data to your FastAPI backend or an AI model, you need to calculate some extra metadata for each task.
The Goal: Write a function enrich_tasks(task_list: list[dict]) -> list[dict] that loops through the list and adds two new keys to every dictionary:
"estimated_hours":
If priority is 1, it takes 4 hours.
If priority is 2, it takes 2 hours.
For any other priority (or if priority is missing), it takes 1 hour.
"is_urgent": A boolean that is True if the priority is 1 or 2, and False otherwise.
Rules:
You must use .get() to safely check the priority.
Return the modified list of dictionaries.
"""
def enrich_tasks(task_list: list[dict]) -> list[dict]:
    for task in task_list:
        priority = task.get("priority")
        if priority == 1:        
            task.update({"estimated_hours": 4, "is_urgent": True})
        elif priority == 2:
            task.update({"estimated_hours": 2, "is_urgent": True})
        else:
            task.update({"estimated_hours": 1, "is_urgent": False})
    return task_list

# --- Test your function ---
raw_tasks = [
    {"text": "Fix server crash", "priority": 1},
    {"text": "Write documentation", "priority": 2},
    {"text": "Brainstorm ideas", "priority": 3},
    {"text": "Mystery task without priority"} # Test your .get() safety!
]

enriched_tasks = enrich_tasks(raw_tasks)

print ("\nExercise 4: The Data Enricher")
for task in enriched_tasks:
    print(f"- {task['text']}")
    print(f" Est. Hours: {task['estimated_hours']} | Urgent: {task['is_urgent']}")

# === Exercise 5: The Pythonic Way (List Comprehensions) ===
"""
The Goal:
Using your enriched_tasks list from Exercise 4, write a function get_urgent_task_names(task_list: list[dict]) -> list[str] that does the following:
Filters the list to keep only the tasks where is_urgent is True.
Extracts only the "text" (the name) of those tasks.
Returns a simple list of strings.
Hint: A list comprehension looks like this:
[expression for item in iterable if condition]
"""
# === Exercise 5: The Pythonic Way ===
def get_urgent_task_names(task_list: list[dict]) -> list[str]:
    return [task["text"] for task in task_list if task.get("is_urgent") is True]

# --- Test your function ---
# (Assume enriched_tasks is already populated from Exercise 4)
enriched_tasks = [
    {"text": "Fix server crash", "priority": 1, "estimated_hours": 4, "is_urgent": True},
    {"text": "Write documentation", "priority": 2, "estimated_hours": 2, "is_urgent": True},
    {"text": "Brainstorm ideas", "priority": 3, "estimated_hours": 1, "is_urgent": False},
    {"text": "Mystery task", "estimated_hours": 1, "is_urgent": False}
]

urgent_names = get_urgent_task_names(enriched_tasks)

print("\nExercise 5: The Pythonic Way")
print(f"Urgent tasks to do: {urgent_names}")
# Expected Output: ['Fix server crash', 'Write documentation']