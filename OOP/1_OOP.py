# === Exercise 1: The Smart Sensor (My First Class) ===
"""
The Goal: Create a Sensor class that monitors a value and knows if it's in danger.
Requirements:
1. Create a class named Sensor.
2. Write the __init__ method. It should take name (string) and threshold (float).
    - Save them as self.name and self.threshold.
    - Also create a self.current_reading attribute and set it to 0.0.
3. Write a method called update_reading(self, new_value). It should update self.current_reading to the new_value.
4. Write a method called is_alert_triggered(self). It should return True if self.current_reading is greater than self.threshold, otherwise return False.
"""
# === Exercise 9: The Smart Sensor ===

class Sensor:
    # Write your __init__ method here
    def __init__(self, string, threshold):
        self.name = string
        self.threshold = threshold
        self.current_reading = 0.0
    # Write your update_reading method here
    def update_reading(self, new_value):
        self.current_reading = new_value        
    # Write your is_alert_triggered method here
    def is_alert_triggered(self):
        if self.current_reading > self.threshold:
            return True
        else:
            return False

# --- Test your Class ---
# Create two different sensors from the same blueprint
temp_sensor = Sensor("Server Room Temp", threshold=80.0)
cpu_sensor = Sensor("CPU Usage", threshold=95.0)

# Update the readings
temp_sensor.update_reading(75.0)
cpu_sensor.update_reading(98.0)

print("\nExercise 1: The Smart Sensor")
print(f"{temp_sensor.name}: {temp_sensor.current_reading} (Alert? {temp_sensor.is_alert_triggered()})")
print(f"{cpu_sensor.name}: {cpu_sensor.current_reading} (Alert? {cpu_sensor.is_alert_triggered()})")

# Expected Output:
# Server Room Temp: 75.0 (Alert? False)
# CPU Usage: 98.0 (Alert? True)