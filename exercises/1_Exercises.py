# === Smart Greenhouse: Exercise 1 ===
"""
Context: Your smart greenhouse has dozens of sensors sending data every minute. However, cheap sensors sometimes send garbage data (negative temperatures, missing keys, or humidity over 100%). Before we can feed this data into an AI model to predict plant growth, we need to clean it.
The Goal: Write a function clean_sensor_data(raw_data: list[dict]) -> list[dict] that processes a messy list of sensor readings.
Requirements:
1. Create an empty list called clean_data = [].
2. Loop through each reading in raw_data.
3. Filter: Check if the reading is valid. A reading is valid ONLY if:
    - It has a "temperature" key.
    - It has a "humidity" key.
    - The temperature is greater than 0.
    - The humidity is between 0 and 100 (inclusive).
      (Hint: Use .get() to safely check for keys without crashing).
4. Transform: If the reading is valid, convert the temperature from Celsius to Fahrenheit.
    - Formula: F = (C * 9/5) + 32
    - Update the dictionary's "temperature" key to the new Fahrenheit value.
5. Append: Add the cleaned and transformed dictionary to your clean_data list.
6. Return clean_data.
"""

def clean_sensor_data(raw_data: list[dict]) -> list[dict]:
    clean_data = []
    
    # Write your loop and logic here
    # Remember to use .get() for safety!
    for reading in raw_data:        
        temperature = reading.get("temperature")
        humidity = reading.get("humidity")
        # 1. Check if keys exist (is not None) to avoid the "Falsy Zero" trap
        if temperature is not None and humidity is not None:
            if temperature > 0 and 0 <= humidity <= 100:
                # 2. Calculate the new value
                fahrenheit_value = (temperature * 9/5) + 32
                # 3. Update the dictionary directly!
                reading["temperature"] = fahrenheit_value
                # 4. Append INSIDE the if block so it only adds valid data
                clean_data.append(reading)
    return clean_data


# --- Test your function ---
messy_readings = [
    {"sensor_id": 1, "temperature": 20.0, "humidity": 60},     # Valid
    {"sensor_id": 2, "temperature": -5.0, "humidity": 50},     # Invalid (Negative temp)
    {"sensor_id": 3, "humidity": 80},                          # Invalid (Missing temp)
    {"sensor_id": 4, "temperature": 25.0, "humidity": 120},    # Invalid (Humidity > 100)
    {"sensor_id": 5, "temperature": 30.0, "humidity": 45},     # Valid
    {"sensor_id": 6, "temperature": 15.0, "humidity": 90}      # Valid
]

cleaned = clean_sensor_data(messy_readings)

print("\nSmart Greenhouse: Exercise 1")

for reading in cleaned:
      
    print(f"Sensor {reading['sensor_id']}: {reading['temperature']}°F, {reading['humidity']}% Humidity")

# Expected Output:
# Sensor 1: 68.0°F, 60% Humidity
# Sensor 5: 86.0°F, 45% Humidity
# Sensor 6: 59.0°F, 90% Humidity

# === Smart Greenhouse: Exercise 2 ===
"""
Context: Now that we can clean sensor data, we need a "Controller" object that represents the physical greenhouse. This object will keep track of the current environment and raise alerts if things get dangerous for the plants.
The Goal: Create a Greenhouse class that stores the current temperature and humidity, updates them with new readings, and checks for dangerous conditions.
Requirements:
1. The Constructor (__init__):
    - It should take a name (string).
    - Initialize self.current_temp to 0.0.
    - Initialize self.current_humidity to 0.0.
    - Initialize self.is_active to True.
2. The Updater (update_environment):
    - This method takes a reading (a cleaned dictionary from Exercise 1).
    - It updates self.current_temp and self.current_humidity using the values from the dictionary.
3. The Safety Check (check_alerts):
    - Create an empty list called alerts = [].
    - If self.current_temp is greater than 90.0, append "Warning: Temperature too high!" to the list.
    - If self.current_humidity is less than 20.0, append "Warning: Humidity too low!" to the list.
    - Return the alerts list.
4. The Magic Method (__str__):
    - Return a nice string showing the status, like: "Greenhouse 'Main': Temp: 75.0°F, Humidity: 60%".
"""

class Greenhouse:
    # Write your __init__ method here
    def __init__(self, name: str) -> None:
        self.name = name
        self.current_temp = 0.0
        self.current_humidity = 0.0
        self.is_active = True
    # Write your update_environment method here
    def update_environment(self, reading: dict) -> None:
        self.current_temp = reading['temperature']
        self.current_humidity = reading['humidity']    
    # Write your check_alerts method here
    def check_alerts(self) -> list[str]:
        alerts = []
        if self.current_temp > 90.0:
            alerts.append("Warning: Temperature too high!")
        if self.current_humidity < 20.0:
            alerts.append("Warning: Humidity too low!")
        return alerts
    # Write your __str__ method here
    def __str__(self) -> str:
        return f"Greenhouse '{self.name}': Temp: {self.current_temp}°F, Humidity: {self.current_humidity}%"
    
# --- Test your Class ---
# 1. Create the greenhouse
my_greenhouse = Greenhouse("Main")

# 2. Simulate receiving cleaned data from Exercise 1
safe_reading = {"sensor_id": 1, "temperature": 75.0, "humidity": 60.0}
danger_reading = {"sensor_id": 2, "temperature": 95.0, "humidity": 15.0}

# 3. Update with safe data
my_greenhouse.update_environment(safe_reading)
print("\nSmart Greenhouse: Exercise 2 - Safe Status")
print(my_greenhouse) # This will use your __str__ method!
print("Alerts:", my_greenhouse.check_alerts())

# 4. Update with dangerous data
my_greenhouse.update_environment(danger_reading)
print("\nSmart Greenhouse: Exercise 2 - Danger Status")
print(my_greenhouse)
print("Alerts:", my_greenhouse.check_alerts())

# Expected Output for Danger Status:
# Greenhouse 'Main': Temp: 95.0°F, Humidity: 15.0%
# Alerts: ['Warning: Temperature too high!', 'Warning: Humidity too low!']

# === Smart Greenhouse: Exercise 3 ===
"""
The Goal: Create a SmartFarm class that holds multiple Greenhouse objects and can check all of them for alerts at once.
Requirements:
1. Create a class named SmartFarm.
2. Write the __init__ method. It should take a farm_name (string).
    - Save it as self.farm_name.
    - Create an empty list called self.greenhouses = [].
3. Write a method called add_greenhouse(self, greenhouse: Greenhouse). It should append the passed greenhouse object to self.greenhouses.
4. Write a method called get_farm_alerts(self) -> dict[str, list[str]].
    - Create an empty dictionary called all_alerts = {}.
    - Loop through self.greenhouses.
    - For each greenhouse, call its .check_alerts() method.
    - If the list of alerts is not empty, add it to the all_alerts dictionary. The key should be the greenhouse's name, and the value should be the list of alerts.
    - Return the all_alerts dictionary.
"""
class SmartFarm:
    # Write your __init__ method here
    def __init__(self, farm_name: str) -> None:
        self.farm_name = farm_name
        self.greenhouses = []
    # Write your add_greenhouse method here
    def add_greenhouse(self, greenhouse: Greenhouse) -> None:
        self.greenhouses.append(greenhouse)
    
    # Write your get_farm_alerts method here
    def get_farm_alerts(self) -> dict[str, list[str]]:
        all_alerts = {}
        for greenhouse in self.greenhouses:
            alerts = greenhouse.check_alerts()
            if alerts:
                all_alerts[greenhouse.name] = alerts
        return all_alerts

# --- Test your Classes ---
# 1. Create the farm
my_farm = SmartFarm("Ariel's Organic Farm")

# 2. Create individual greenhouses (using your class from Exercise 2)
gh1 = Greenhouse("Tomato House")
gh2 = Greenhouse("Cucumber House")
gh3 = Greenhouse("Strawberry House")

# 3. Add them to the farm
my_farm.add_greenhouse(gh1)
my_farm.add_greenhouse(gh2)
my_farm.add_greenhouse(gh3)

# 4. Simulate updating their environments
gh1.update_environment({"temperature": 75.0, "humidity": 60.0}) # Safe
gh2.update_environment({"temperature": 95.0, "humidity": 15.0}) # DANGER!
gh3.update_environment({"temperature": 80.0, "humidity": 50.0}) # Safe

# 5. Check the whole farm for alerts
print("\nSmart Greenhouse: Exercise 3")
farm_alerts = my_farm.get_farm_alerts()

if farm_alerts:
    print("ALERTS DETECTED ON FARM:")
    for name, alerts in farm_alerts.items():
        print(f" - {name}: {alerts}")
else:
    print("All greenhouses are operating normally.")

# Expected Output:
# ALERTS DETECTED ON FARM:
#  - Cucumber House: ['Warning: Temperature too high!', 'Warning: Humidity too low!']