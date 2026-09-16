# === Exercise 1: The AI Label Encoder ===
"""
The Goal: Write a function that takes a list of unique category names and returns a dictionary mapping each name to its index number.
Hint: Python has a built-in function called enumerate(). When you loop through a list with it, it gives you both the index and the item: for index, item in enumerate(my_list):.
"""
# === Exercise 1: The AI Label Encoder ===
def create_label_encoder(categories: list[str]) -> dict[str, int]:
    return {animal: index for index, animal in enumerate(categories)}
    
# --- Test your function ---
animal_classes = ["cat", "dog", "bird", "fish"]

encoder = create_label_encoder(animal_classes)
print("\nExercise 1: The AI Label Encoder")
print(encoder)

# === Exercise 2: The Robust Calculator (Try/Except Error Handling) ===
"""
Context: In data pipelines, bad data will crash your program if you aren't careful. For example, dividing by zero.
The Goal: Write a function that calculates a "task score" using the formula: score = estimated_hours / priority.
If the calculation fails (e.g., priority is 0), catch the error, print a warning message, and do not add it to the final list.
Hint: You need to catch ZeroDivisionError.
"""
print("\nExercise 2: The Robust Calculator (Try/Except Error Handling)")
def calculate_task_scores(tasks: list[dict]) -> list[float]:
    valid_scores = []
    for task in tasks:
        hours = task.get("estimated_hours", 0)
        priority = task.get("priority", 1)
        try:
            score = float(hours/priority)
            valid_scores.append(score)
        except ZeroDivisionError:
            print("Divided by Zero")
    return(valid_scores)

# --- Test your function ---
task_data = [
    {"text": "Fix bug", "estimated_hours": 4, "priority": 2},
    {"text": "Write docs", "estimated_hours": 2, "priority": 0}, # Will cause ZeroDivisionError!
    {"text": "Deploy app", "estimated_hours": 5, "priority": 1}
]

scores = calculate_task_scores(task_data)
print(f"Valid scores: {scores}")

# === Exercise 3: The Data Saver (Reading and Writing JSON) ===
"""
The Goal: Write two functions. One to save a dictionary to a .json file, and one to read it back.
Hint: You will need to import json at the top of your file. Use the with open(...) as file: syntax (Context Managers) to safely handle files.
"""
import json

def save_data_to_json(data: dict, filename: str):
    # Open the file in write mode ('w') and use json.dump() to save the data.
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)   

def load_data_from_json(filename: str) -> dict:
    # Open the file in read mode ('r') and use json.load() to return the data.
    with open(filename, "r", encoding="utf-8") as file:        
        return json.load(file)

# --- Test your functions ---
my_config = {
    "model_name": "fastapi-ai",
    "version": 1.0,
    "features": ["text", "image"]
}

# 1. Save the data
save_data_to_json(my_config, "config.json")
print("\nExercise 3: The Data Saver")
print("Data saved successfully!")

# 2. Load the data back
loaded_config = load_data_from_json("config.json")
print("Data loaded successfully!")
print(loaded_config)