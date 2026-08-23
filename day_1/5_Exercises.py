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