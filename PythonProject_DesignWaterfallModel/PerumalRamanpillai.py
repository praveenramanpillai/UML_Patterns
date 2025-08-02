# PerumalRamanpillai.py
# This program receives and displays a custom Waterfall Model with user input

# Define the main class
class RamanapillaiModel:
    def __init__(self):
        # This will store a list of (phase, phase_activities) pairs
        self.model = []

    # Builds the model by getting input from the user
    def build_model(self):
        print("Welcome to the Waterfall Model Builder\n")
        print("Enter a phase name like: Communication, Planning, Modelling, Development, Testing, Deployment and Maintenance")
        print("Type 'complete' once you are done.\n")

        while True:
            # Prompts the user for a phase name
            phase = input("Enter phase name (or 'complete' to finish): ").strip()
            if phase.lower() == 'complete':
                break

            # Prompts the user for activities in that phase
            activities = input(f"Enter activities for '{phase}' (comma separated): ").strip()

            # Convert the comma-separated string into a list of activities
            activities_list = [a.strip() for a in activities.split(",") if a.strip()]
            self.model.append((phase, activities_list))
            print(f"{phase} phase added/updated with new activity\n")

    # Displays the final model in a readable format
    def display_model(self):
        print("\nRamanapillai's Waterfall Model:\n")
        for phase, phase_activities in self.model:
            print(f"{phase}:")
            for act in phase_activities:
                print(f"  - {act}")
            print()

# Run the program
if __name__ == "__main__":
    model = RamanapillaiModel()
    model.build_model()
    model.display_model()
