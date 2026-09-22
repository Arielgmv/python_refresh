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
    def __init__(self, name: str, threshold: float) -> None:
        self.name = name
        self.threshold = threshold
        self.current_reading = 0.0
    # Write your update_reading method here
    def update_reading(self, new_value: float) -> None:
        self.current_reading = new_value        
    # Write your is_alert_triggered method here
    def is_alert_triggered(self) -> bool:
        return self.current_reading > self.threshold
    
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

# === Exercise 2: The Sensor Network (Composition) ===
"""
The Goal: Create a SensorNetwork class that holds a list of Sensor objects and can check all of them at once.
Requirements:
1. Create a class named SensorNetwork.
2. Write the __init__ method. It should take a name (string).
 - Save it as self.name.
 - Create an empty list called self.sensors = [].
3. Write a method called add_sensor(self, sensor). It should append the passed sensor object to self.sensors.
4. Write a method called get_triggered_alarms(self).
 - Loop through self.sensors.
 - If a sensor's alarm is triggered (use the method you built in Exercise 1!), add the sensor's name to a new list.
 - Return the list of triggered sensor names.
"""
# === Exercise 2: The Sensor Network ===

class SensorNetwork:
    # Write your __init__ method here
    def __init__(self, name: str) -> None:
        self.name = name
        self.sensors = []
    # Write your add_sensor method here
    def add_sensor(self, sensor: Sensor) -> None:
        self.sensors.append(sensor)
    
    # Write your get_triggered_alarms method here
    def get_triggered_alarms(self) -> list[str]:
        triggered_alarms = []
        for sensor in self.sensors:
            if sensor.is_alert_triggered():
                triggered_alarms.append(sensor.name)
        return triggered_alarms


# --- Test your Classes ---
# 1. Create the network
network = SensorNetwork("Data Center Alpha")

# 2. Create individual sensors (using your class from Exercise 1)
temp_sensor = Sensor("Server Room Temp", threshold=80.0)
cpu_sensor = Sensor("CPU Usage", threshold=95.0)
humidity_sensor = Sensor("Humidity", threshold=60.0)

# 3. Add them to the network
network.add_sensor(temp_sensor)
network.add_sensor(cpu_sensor)
network.add_sensor(humidity_sensor)

# 4. Update their readings
temp_sensor.update_reading(85.0)   # Will trigger
cpu_sensor.update_reading(50.0)    # Will NOT trigger
humidity_sensor.update_reading(70.0) # Will trigger

# 5. Check the network
print("\nExercise 2: The Sensor Network")
alarms = network.get_triggered_alarms()
print(f"Network '{network.name}' has triggered alarms in: {alarms}")

# Expected Output:
# Network 'Data Center Alpha' has triggered alarms in: ['Server Room Temp', 'Humidity']