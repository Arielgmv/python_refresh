priority = "low"

print("\nFirst if example")
if priority == "high":
    print("Do this today.")
elif priority == "medium":
    print("Schedule this for this week.")
else:
    print("Can wait.")

# === 1. Mini exercise ===
note = """
Today:
- review Python functions
- finish FastAPI healt check
"""
print("\nExercise 1 - Print lines with bucle For:")
for line in note.splitlines():
    line = line.strip()
    if line.startswith("-"):
        print("Task line:", line)

# === 2. The Tag Sorter (if / elif / else) ===
task = "Draft the weekly report for the boss @work"

# Python checks these from top to bottom
print("\nExercise 2 - The Tag Sorter (if / elif / else)")
if "@work" in task:
    print("📂 Filed under: Work")
elif "@home" in task:
    print("🏠 Filed under: Personal")
elif "@urgent" in task:
    print("🚨 Filed under: DO THIS NOW")
else:
    print("📥 Filed under: Inbox (Uncategorized)")

# === 3. The Priority Filter (for loop + if statement) ===

database = [
    {"text": "Buy groceries", "priority": 1, "done": False},
    {"text": "Renew passport", "priority": 3, "done": False},
    {"text": "Call mom", "priority": 1, "done": True},
    {"text": "Fix server bug", "priority": 1, "done": False}
]

print("\nExercise 3 - The Priority Filter (for loop + if statement)")

print("\nShow all tasks")
for item in database:
    print(f"text: {item['text']}, priority: {item['priority']}, done: {item['done']}")

print("\n🔥 URGENT PENDING TASKS 🔥")
for item in database:
    # We only care if priority is 1 AND it is not done
    if item["priority"] == 1 and item["done"] == False:
        print(f"- {item['text']}")

# === 4. The Command Line Interface (while loop) ===
print("\nExercise 4 - The Command Line Interface (while loop)")

print("\nWelcome to Second Brain Lite!")

while True:
    # input() pauses the loop and waits for the user to type something
    command = input("Enter a command ('add', 'view', or 'quit'): ").lower()

    if command == "quit":
        print("Saving brain... Goodbye! 👋")
        break # This is the escape hatch! It stops the while loop entirely.

    elif command == "add":
        new_task = input("What do you want to remember? ")
        print(f"✅ Added: '{new_task}'")

    elif command == "view":
        print("👀 Viewing your tasks... (Imagine tasks here)")

    else:
        print("❌ Unknown command. Try again")