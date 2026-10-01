# === Exercise 1: The Smart Sensor ===
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

# === Exercise 3: The Playlist A ===

class Song:
    # Write __init__
    def __init__(self, title: str, artist: str, duration_minutes: float) -> None:
        self.title = title
        self.artist = artist
        self.duration_minutes = duration_minutes
    # Write is_long_song
    def is_long_song(self) -> bool:
        return self.duration_minutes > 4

    # Add the __str__ method here!
    # It should return: f"{self.title} by {self.artist}"
    def __str__(self) -> str:
        return f"{self.title} by {self.artist}"

# --- Test Step 1 ---
song1 = Song("Bohemian Rhapsody", "Queen", 5.5)
song2 = Song("Blinding Lights", "The Weeknd", 3.2)

print("\nExercise 3: The Playlist A")
print(song1.is_long_song()) # Should be True
print(song2.is_long_song()) # Should be False

# === Exercise 4: The Playlist B ===
class Playlist:
    # Write __init__
    def __init__(self, name: str) -> None:
        self.name = name
        self.songs = []
    # Write add_song
    def add_song(self, song: Song) -> None:
        self.songs.append(song)

    # Write get_long_songs
    def get_long_songs(self) -> list[str]:
        long_titles = []
        for song in self.songs:
            if song.is_long_song():
                long_titles.append(song.title)
        return long_titles

    # Add the __len__ method here!
    # It should return the length of self.songs
    def __len__(self) -> int:
        return len(self.songs)

# --- Test Step 2 ---
# 1. Create the playlist
my_playlist = Playlist("My Road Trip")

# 2. Create songs (using your class from Step 1)
s1 = Song("Bohemian Rhapsody", "Queen", 5.5)
s2 = Song("Blinding Lights", "The Weeknd", 3.2)
s3 = Song("Stairway to Heaven", "Led Zeppelin", 8.0)

# 3. Add them to the playlist
my_playlist.add_song(s1)
my_playlist.add_song(s2)
my_playlist.add_song(s3)

# 4. Get the long songs
print("\nExercise 4: The Playlist B")
print(f"Long songs in '{my_playlist.name}': {my_playlist.get_long_songs()}")

print("Printing the song object directly:")
print(s1)  # This will automatically call s1.__str__()!

print(f"\nNumber of songs in the playlist: {len(my_playlist)}") # This calls my_playlist.__len__()

# Expected Output:
# Long songs in 'My Road Trip': ['Bohemian Rhapsody', 'Stairway to Heaven']

# === Exercise 5: The Premium Playlist (Inheritance) ===
"""
The Goal: Create a PremiumPlaylist class that inherits from your existing Playlist class, but restricts the number of songs it can hold.
Requirements:
1. Create a class named PremiumPlaylist that inherits from Playlist. The syntax is:
   class PremiumPlaylist(Playlist):
2. Write the __init__ method. It should take name (str) and max_songs (int).
    - Crucial Step: Inside __init__, call the parent's initializer using super().__init__(name). This sets up self.name and self.songs automatically!
    - Then, save the limit: self.max_songs = max_songs.
3. Override the add_song method.
    - Before adding the song, check if the current number of songs (len(self)) is less than self.max_songs.
    - If it is, call the parent's add_song method using super().add_song(song).
    - If it is not, print a warning message: "Playlist is full! Cannot add more songs."
"""

# (Assume your Playlist class from the previous exercise is already defined above)

print("\nExercise 5: The Premium Playlist")
class PremiumPlaylist(Playlist):
    # Write your __init__ method here
    def __init__(self, name: str, max_songs: int) -> None:        
    # Hint: Use super().__init__(name)
        super().__init__(name)
        self.max_songs = max_songs
    
    # Write your add_song method here
    # Hint: Use len(self) to check the limit, and super().add_song(song) to add it
    def add_song(self, song: Song) -> None:
        if (len(self)) < self.max_songs:
            super().add_song(song)
        else:
            print("Playlist is full! Cannot add more songs.")


# --- Test your Inheritance ---
# 1. Create a premium playlist with a limit of 2 songs
premium_mix = PremiumPlaylist("Top Hits", max_songs=2)

# 2. Create songs
s1 = Song("Bohemian Rhapsody", "Queen", 5.5)
s2 = Song("Blinding Lights", "The Weeknd", 3.2)
s3 = Song("Stairway to Heaven", "Led Zeppelin", 8.0)

# 3. Add songs (The first two should work, the third should trigger the warning)
premium_mix.add_song(s1)
premium_mix.add_song(s2)
premium_mix.add_song(s3) 

print(f"Songs in '{premium_mix.name}': {len(premium_mix)}")
print(f"Long songs: {premium_mix.get_long_songs()}") # Notice how you get this method for free!

# === Exercise 6: The AI Experiment Tracker (Dataclasses) ===
"""
The Goal: Rewrite a class using the @dataclass decorator, and add default values.
Context: In Machine Learning, we run "Experiments" with different settings (hyperparameters) and track the results.
Requirements:
1. Import the dataclass tool: from dataclasses import dataclass
2. Add @dataclass right above your class definition.
3. Define your variables with type hints. Do not write an __init__ method!
4. Notice how you can set default values (like accuracy = 0.0).
"""
from dataclasses import dataclass

# === Exercise 6: The AI Experiment Tracker ===

#Add the @dataclass decorator here
@dataclass
class MLExperiment:
    # TODO: Define the attributes using type hints. 
    # No __init__ needed!
    name: str
    learning_rate: float
    epochs: int
    accuracy: float = 0.0  # Default value

    # You can still add custom methods!
    def print_summary(self):
        print(f"Experiment '{self.name}' ran for {self.epochs} epochs with LR={self.learning_rate}. Final Accuracy: {self.accuracy}")


# --- Test your Dataclass ---
# Notice how clean and fast it is to create objects now!
exp1 = MLExperiment(name="Baseline Model", learning_rate=0.01, epochs=10)
exp2 = MLExperiment(name="High LR Test", learning_rate=0.1, epochs=5, accuracy=0.85)

print("\nExercise 6: The AI Experiment Tracker")
exp1.print_summary()
exp2.print_summary()

# Bonus: Dataclasses also automatically create a nice __str__ (called __repr__) for you!
print("\nRaw object print:")
print(exp1) 

# === Exercise 7: Encapsulation ===
"""
The Goal: Create a NeuralNetwork class that uses Python's @property decorator to validate data before it is saved.
Requirements:
1. Create a class NeuralNetwork.
2. In __init__, take a learning_rate. But instead of saving it as self.learning_rate, save it as self._learning_rate (the underscore indicates it's "private" or protected).
3. Create a getter method using @property. It should just return self._learning_rate.
4. Create a setter method using @learning_rate.setter.
    - It should check if the value is greater than 0.
    - If it is, set self._learning_rate = value.
    - If it is NOT, print a warning: "Error: Learning rate must be positive!" and do not change the value.
"""
class NeuralNetwork:
    def __init__(self, learning_rate: float):
        # We assign it using the setter we are about to create!
        self.learning_rate = learning_rate 

    # Write the @property getter for learning_rate
    @property
    def learning_rate(self):
        return self._learning_rate
    
    # Write the @learning_rate.setter to validate the value
    @learning_rate.setter
    def learning_rate(self, value):
        if value > 0:
            self._learning_rate = value
        else:
            print("Error: Learning rate must be positive!")


# --- Test your Encapsulation ---
print("\nExercise 7: Encapsulation")

# 1. Create a valid network
my_nn = NeuralNetwork(0.01)
print(f"Initial learning rate: {my_nn.learning_rate}")

# 2. Try to update it with a valid number
my_nn.learning_rate = 0.05
print(f"Updated learning rate: {my_nn.learning_rate}")

# 3. Try to update it with an INVALID number (This should trigger your setter's warning!)
my_nn.learning_rate = -0.5 
print(f"Learning rate after bad update: {my_nn.learning_rate}") # Should still be 0.05!