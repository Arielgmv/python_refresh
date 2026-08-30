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

# === Exercise 5.5: The Data Filter ===
"""
Exercise 5.5: The Data Filter (The Long Way)
In AI and Data Science, 80% of your job is filtering out bad data. Before we learn the "one-line" shortcut, you need to be completely comfortable writing the "long way."
The Goal:
You have a list of raw sensor readings (numbers). Some are negative (errors), and some are too high (outliers).
Write a function that loops through the list, keeps only the valid readings (between 10 and 50, inclusive), and returns a new list with just those valid numbers.
Rules:
1. Do NOT use list comprehensions.
2. Do NOT use filter() or lambda.
3. Create an empty list at the start (the "accumulator").
4. Use a standard for loop.
5. Use an if statement to check the condition.
6. Use .append() to add the valid numbers to your empty list.
"""

def filter_sensor_readings(readings: list[int]) -> list[int]:
    # 1. Create an empty list to hold our good data
    valid_readings = []
    
    # 2. Write a standard for loop to look at each 'reading' in 'readings'
    for reading in readings:
    # 3. Inside the loop, write an if statement:
    #    If the reading is >= 10 AND the reading is <= 50:
        if reading >=10 and reading <=50:
    # 4. If it is valid, append it to 'valid_readings'
            valid_readings.append(reading)
    # 5. Return the 'valid_readings' list
    return valid_readings

# --- Test your function ---
raw_data = [5, 12, 45, 99, -3, 22, 50, 10, 8]

good_data = filter_sensor_readings(raw_data)

print("\nExercise 5.5: The Data Filter")
print(f"Raw data: {raw_data}")
print(f"Filtered data: {good_data}")
# Expected Output: [12, 45, 22, 50, 10]

# === Exercise 5.6: The Data Transformer ===
"""
The Goal:
You have a list of temperatures in Celsius. Write a function that loops through the list, converts each temperature to Fahrenheit, and returns a new list with the converted numbers.
Formula: Fahrenheit = (Celsius * 9/5) + 32
Rules:
1. Do NOT use list comprehensions.
2. Create an empty list at the start.
3. Use a standard for loop.
4. Calculate the new value, and use .append() to add it to your empty list.
5. Return the new list.
"""
def convert_celsius_to_fahrenheit(celsius_list: list[float]) -> list[float]:
    # 1. Create an empty list to hold the converted temperatures
    fahrenheit_list = []
    
    # 2. Write a standard for loop to look at each 'temp' in 'celsius_list'
    for temp in celsius_list:
    
    # 3. Inside the loop, calculate the fahrenheit value
    #    Formula: (temp * 9/5) + 32
        fahrenheit_value = (temp * 9/5) + 32
    
    # 4. Append the new fahrenheit value to 'fahrenheit_list'
        fahrenheit_list.append(fahrenheit_value)
    # 5. Return the 'fahrenheit_list'
    return fahrenheit_list

# --- Test your function ---
celsius_data = [0, 20, 37, 100]

fahrenheit_data = convert_celsius_to_fahrenheit([float(temp) for temp in celsius_data])

print("\nExercise 5.6: The Data Transformer")
print(f"Celsius: {celsius_data}")
print(f"Fahrenheit: {fahrenheit_data}")
# Expected Output: [32.0, 68.0, 98.6, 212.0]

# === Exercise 5.7: The Data Aggregator ===
"""
The Goal:
Write a function that calculates the average of a list of numbers.
Rules:
1. Do NOT use the built-in sum() or len() functions for this exercise. We want to practice the loop!
2. Create two variables at the start: total (set to 0) and count (set to 0).
3. Use a standard for loop.
4. Inside the loop, add the current number to total, and add 1 to count.
5. After the loop finishes, divide total by count and return the result.
"""

def calculate_average(numbers: list[float]) -> float:
    # 1. Create variables to hold the running total and the count
    total = 0.0
    count = 0
    
    # 2. Write a standard for loop to look at each 'num' in 'numbers'
    for num in numbers:
    # 3. Inside the loop, add 'num' to 'total'
        total += num
    # 4. Inside the loop, add 1 to 'count'
        count += 1
    # 5. After the loop, calculate the average (total / count) and return it
    average = (total / count)
    return average

# --- Test your function ---
sensor_readings = [10.0, 20.0, 30.0, 40.0, 50.0]

average = calculate_average(sensor_readings)

print("\nExercise 5.7: The Data Aggregator")
print(f"Readings: {sensor_readings}")
print(f"Average: {average}")
# Expected Output: 30.0

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

def group_tasks_by_category(task_list: list[dict]) -> dict[str, list[dict]]:
    # 1. Create an empty dictionary to hold our grouped data
    grouped_tasks = {}
    
    # 2. Write a standard for loop to look at each 'task' in 'task_list'
    for task in task_list:
    # 3. Inside the loop, get the 'category' from the task. 
    #    Default to "Other" if it's missing.
        category = task.get("category", "Other")
    # 4. Check if the 'category' is already a key in 'grouped_tasks'.
        if category in grouped_tasks:
            pass
    #    If it is NOT in the dictionary, set grouped_tasks[category] = []
        else:
            grouped_tasks[category] = []
    # 5. Append the 'task' to the list at grouped_tasks[category]
        grouped_tasks[category].append(task)
    # 6. Return the 'grouped_tasks' dictionary
    return grouped_tasks

# --- Test your function ---
my_tasks = [
    {"text": "Fix bug", "category": "Work"},
    {"text": "Buy milk", "category": "Personal"},
    {"text": "Write email", "category": "Work"},
    {"text": "Walk the dog", "category": "Personal"},
    {"text": "Mystery task"} # Test your default "Other" logic!
]

grouped = group_tasks_by_category(my_tasks)

print("\nExercise 5.8: The Data Grouping")
for category, tasks in grouped.items():
    print(f"\n{category}:")
    for t in tasks:
        print(f" - {t['text']}")


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
def process_task_pipeline(raw_tasks: list[dict]) -> dict[str, list[str]]:
    # 1. Create an empty dictionary for our final grouped data
    pipeline_output = {}
    
    # 2. Loop through each 'task' in 'raw_tasks'
    for task in raw_tasks:
    # 3. FILTER: If the task doesn't have a "text" key, skip it. 
    #    (Hint: use `if "text" not in task: continue`)
        if "text" in task:
    # 4. TRANSFORM: Get the category, default to "other", and make it lowercase.
            category = task.get("category", "other").lower()
    # 5. GROUP: Check if the category is in pipeline_output. 
    #    If not, create an empty list for it.
            if category not in pipeline_output:
                pipeline_output[category] = []
    # 6. Append the task's "text" to the correct category list.
            pipeline_output[category].append(task["text"])
    # 7. Return pipeline_output
    return pipeline_output

# --- Test your function ---
messy_raw_data = [
    {"text": "Fix bug", "category": "Work"},
    {"text": "Buy milk", "category": "PERSONAL"}, # Uppercase!
    {"category": "Work"}, # Missing text! (Should be filtered out)
    {"text": "Write email", "category": "work"},
    {"text": "Walk the dog", "category": "Personal"},
    {"text": "Mystery task"} # Missing category! (Should become "other")
]

final_output = process_task_pipeline(messy_raw_data)

print("\nExercise 5.9: The Mini Data Pipeline")
for category, texts in final_output.items():
    print(f"\n{category.upper()}: {texts}")


# === Exercise 6: The Data Sorter ===
"""
The Goal: Write a function that takes the enriched_tasks list and returns a new list sorted by estimated_hours in descending order (longest tasks first).
Hint: The syntax for sorted() with a lambda looks like this:
sorted(iterable, key=lambda item: item["some_key"], reverse=True)
"""
# === Exercise 6: The Data Sorter ===
def sort_tasks_by_time(task_list: list[dict]) -> list[dict]:
    #Return the sorted list using sorted() and a lambda function.
    # Sort by 'estimated_hours' in descending order (highest hours first).
    return sorted(task_list, key=lambda item: item["estimated_hours"], reverse=True) 
        

# --- Test your function ---
enriched_tasks = [
    {"text": "Fix server crash", "priority": 1, "estimated_hours": 4, "is_urgent": True},
    {"text": "Write documentation", "priority": 2, "estimated_hours": 2, "is_urgent": True},
    {"text": "Brainstorm ideas", "priority": 3, "estimated_hours": 1, "is_urgent": False},
    {"text": "Mystery task", "estimated_hours": 1, "is_urgent": False}
]

sorted_tasks = sort_tasks_by_time(enriched_tasks)

print("\nExercise 6: The Data Sorter")
for task in sorted_tasks:
    print(f"- {task['text']} ({task['estimated_hours']} hours)")

# === Exercise 7: The Lookup Map ===
"""
The Goal: Write a function create_task_lookup(task_list: list[dict]) -> dict[str, int] that takes your list of tasks and converts it into a dictionary where:
- The Key is the task's "text".
- The Value is the task's "estimated_hours".
Hint: A dictionary comprehension looks very similar to a list comprehension, but uses curly braces {} and a colon : to define the key and value:
{key: value for item in iterable}
"""
# === Exercise 7: The Lookup Map ===
def create_task_lookup(task_list: list[dict]) -> dict[str, int]:
    # Write this in ONE line using a dictionary comprehension!
    return {task["text"]: task.get("estimated_hours", 0) for task in task_list}

# --- Test your function ---
enriched_tasks = [
    {"text": "Fix server crash", "priority": 1, "estimated_hours": 4, "is_urgent": True},
    {"text": "Write documentation", "priority": 2, "estimated_hours": 2, "is_urgent": True},
    {"text": "Brainstorm ideas", "priority": 3, "estimated_hours": 1, "is_urgent": False}
]

task_map = create_task_lookup(enriched_tasks)

print("\nExercise 7: The Lookup Map")
print(task_map)
# Expected Output: {'Fix server crash': 4, 'Write documentation': 2, 'Brainstorm ideas': 1}

# Proving it works as a lookup:
print(f"\nHours needed for 'Fix server crash': {task_map['Fix server crash']}")