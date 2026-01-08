import random
import time


class Rock:
    def _init_(self, name: str):
        self.name = name

        # Core identity
        self.temperament = random.choice([
            "Agreeable",
            "Narcissistic",
            "Hectic",
            "Honorable",
            "Argumentative"
            ])

        self.mood = random.choice([
            "Happy",
            "Stressed",
            "Sad",
            "Mad",
            "Agitated",
            "Content",
            "Bored"
            ])

        # Hidden stats (players never sees numbers)
        self.bond = random.radint(30, 70)
        self.stability = random.randint(30, 70)

        # Time tracking
        self.last_interaction = time.time()
        self.is_hibernating = False

    def describe(self):
        description = f"{self.name} is feeling {self.mood.lower()}."

        if self.temperament == "Narcissistic":
            description += " It seems deeply aware of its own existence."

        elif self.temperament == "Honorable":
            description += " It carries itself with quiet dignity."
        elif self.temperament == "Hectic":
            description += " There's a restless energy about it."
        elif self.temperament == "Argumentative":
            description += " It looks like it has something to prove."
        elif self.temperament == "Agreeable":
            description += " It seems content to be here with you."

        return description
