# developerTraits.py

class Trait:
    def __init__(self, name, brief):
        self.name = name
        self.brief = brief

    def __str__(self):
        return f"{self.name}: {self.brief}"

class DeveloperProfile:
    def __init__(self):
        self.problemSolving = None
        self.technicalSkills = None
        self.teamwork = None

    def describe(self):
        return "\n".join([
            str(self.problemSolving),
            str(self.technicalSkills),
            str(self.teamwork)
        ])

class TraitBuilder:

    def reset(self):
        self.profile = DeveloperProfile()
        self.steps = []

    def setProblemSolving(self):
        self.profile.problemSolving = Trait(
            "Problem Solving & Analytical Skills",
            "Breaks down complex problems, applies logical reasoning, and devises innovative solutions."
        )
        self.steps.append("Set Problem Solving & Analytical Skills")

    def setTechnicalSkills(self):
        self.profile.technicalSkills = Trait(
            "Strong Technical Skills",
            "Demonstrates expertise in programming languages, frameworks, and system design."
        )
        self.steps.append("Set Strong Technical Skills")

    def setTeamwork(self):
        self.profile.teamwork = Trait(
            "Teamwork & Communication",
            "Collaborates effectively, communicates clearly, and supports collective team goals."
        )
        self.steps.append("Set Teamwork & Communication")

    def getResult(self):
        return self.profile, self.steps


class Director:
    def construct(self, builder: TraitBuilder):
        builder.reset()
        builder.setProblemSolving()
        builder.setTechnicalSkills()
        builder.setTeamwork()
        return builder.getResult()


if __name__ == "__main__":
    print("=== The Essential traits for excellent software developers ===\n")

    director = Director()
    builder = TraitBuilder()
    profile, steps = director.construct(builder)

    # Brief description
    print("Developer Profile Description:\n")
    print(profile.describe())

    # Names of steps
    print("\nImportant Steps Executed:")
    for step in steps:
        print(f"- {step}")

    # Number of steps
    print(f"\nNumber of Steps: {len(steps)}")
