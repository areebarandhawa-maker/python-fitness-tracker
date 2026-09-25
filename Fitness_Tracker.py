from abc import ABC, abstractmethod

# ABSTRACT BASE CLASS

class Workout(ABC):

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.__completed = False   # Private attribute

    @abstractmethod
    def calculate_calories(self):
        pass

    def mark_completed(self):
        self.__completed = True

    def is_completed(self):
        return self.__completed

    def __str__(self):
        status = "Completed" if self.__completed else "Not Completed"
        return f"{self.name} | {self.__class__.__name__} | {self.duration} min | {status}"

# RUN SUBCLASS

class Run(Workout):
    
    def __init__(self, name, duration, distance):
        super().__init__(name, duration)
        self.distance = distance

    def calculate_calories(self):
        # Simple project-based formula:
        # 10 calories per minute + 5 calories per km
        return (self.duration * 10) + (self.distance * 5)

# SWIM SUBCLASS

class Swim(Workout):
   
    def __init__(self, name, duration, laps):
        super().__init__(name, duration)
        self.laps = laps

    def calculate_calories(self):
        # Simple project-based formula:
        # 8 calories per minute + 2 calories per lap
        return (self.duration * 8) + (self.laps * 2)

# FUNCTION WITH DEFAULT ARGUMENT

def display_workouts(workouts, limit=5):
    
    print(f"\nShowing up to {limit} workouts:")

    for workout in workouts[:limit]:
        print(workout)

# FUNCTION USING *ARGS

def total_calories(*calories):
   
    return sum(calories)

# MAIN PROGRAM
# Create workout objects

run1 = Run("Morning Run", 30, 5)
run2 = Run("Evening Run", 45, 7)

swim1 = Swim("Morning Swim", 40, 20)
swim2 = Swim("Weekend Swim", 60, 30)


workouts = [run1, run2, swim1, swim2]

run1.mark_completed()
swim1.mark_completed()

print("========== WORKOUTS ==========")

for workout in workouts:
    print(workout)


print("\n========== CALORIE CALCULATIONS ==========")

for workout in workouts:
    calories = workout.calculate_calories()

    print(
        f"{workout.name}: "
        f"{calories} calories"
    )

calorie_summary = {
    workout.name: workout.calculate_calories()
    for workout in workouts
}

print("\n========== CALORIE SUMMARY ==========")
print(calorie_summary)

workout_types = {
    workout.__class__.__name__
    for workout in workouts
}

print("\n========== UNIQUE WORKOUT TYPES ==========")
print(workout_types)

high_calorie_workouts = [
    workout.name
    for workout in workouts
    if workout.calculate_calories() > 400
]

print("\n========== HIGH-CALORIE WORKOUTS ==========")
print(high_calorie_workouts)

display_workouts(workouts)


# Also demonstrate changing the default
display_workouts(workouts, 2)

calorie_values = [
    workout.calculate_calories()
    for workout in workouts
]

total = total_calories(*calorie_values)

print("\n========== TOTAL CALORIES ==========")
print(f"Total calories burned: {total}")

sorted_workouts = sorted(
    workouts,
    key=lambda workout: workout.calculate_calories(),
    reverse=True
)

print("\n========== WORKOUTS SORTED BY CALORIES ==========")

for workout in sorted_workouts:
    print(
        f"{workout.name}: "
        f"{workout.calculate_calories()} calories"
    )


print("\n========== COMPLETION STATUS ==========")

for workout in workouts:
    print(
        f"{workout.name}: "
        f"{workout.is_completed()}"
    )

print("\n========== REQUIREMENTS COMPLETED ==========")

print("1. Dictionary and Set: Completed")
print("2. List comprehension: Completed")
print("3. Function with default argument: Completed")
print("4. Function with *args: Completed")
print("5. sorted() with lambda key: Completed")
print("6. Abstract class with @abstractmethod: Completed")
print("7. Two subclasses with different implementations: Completed")
print("8. Polymorphism: Completed")
print("9. Private attribute with controlled access: Completed")
print("10. __str__ method: Completed")


# ============================================================
# REFLECTION
# ============================================================

"""
Reflection:

I made Workout an abstract class because Run and Swim share common
workout information, while their calorie calculations are different.
I made the completion status private so that it cannot be changed
directly from outside the class and can only be controlled through
methods. The trickiest part was understanding how polymorphism works
with different workout subclasses, so I used the same
calculate_calories() call inside a loop and allowed each subclass
to provide its own implementation.
"""