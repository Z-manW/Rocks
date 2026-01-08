import random
import time


class Rock:
    def __init__(self, name: str):
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
        self.bond = random.randint(30, 70)
        self.stability = random.randint(30, 70)

        # Time tracking
        self.last_interaction = time.time()
        self.is_hibernating = False

    def describe(self):

        if self.is_hibernating:
            return f"{self.name} is hibernating. The rock's face is gone. Come back later."

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

    def interact(self):
        self.last_interaction = time.time()

        # Bond grows slowly
        self.bond = min(100, self.bond + random.randint(1, 3,))

        # Calm effect
        if self.mood in ["Agitated", "Mad", "Stressed"]:
            if random.random() < (self.bond / 150):
                self.mood = "Content"

    
    def check_neglect(self):
        time_ignored = time.time() - self.last_interaction

        # 30 seconds = noticeable neglect (for testing)
        if time_ignored > 30 and not self.is_hibernating:

            if random.random() < (1 - self.stability / 100):
                self.mood = random.choice(["Bored", "Agitated", "Stressed"])

            # Extreme neglect -> hibernating
            if time_ignored > 90 and not self.is_hibernating:
                self.is_hibernating = True
                return "Pebble withdraws completely adn enters hibernation."

    def ambient_thought(self):
        if self.is_hibernating:
            return None

        chance = random.random()

        if chance < 0.3:
            return None # silence is intentional

        if self.mood == "Bored":
            return "The rock seems aware of the passing time."
        elif self.mood == "Agitated":
            return "Pebble radiates a faint, uncomfortable tension."
        elif self.mood == "Happy":
            return "Pebble feels pleasantly grounded."
        elif self.mood == "Stressed":
            return "Pebble feels compressed, like it's carrying weight."
        elif self.mood == "Content":
            return "Pebble rests calmly, unbothered."
        else:
            return "Pebble is hard to read right now."

    def observe(self):
        if self.is_hibernating:
            return "Pebble does not respond. The rock is hibernating."

        self.last_interaction = time.time()
        return self.describe()

    def affirm(self):
        if self.is_hibernating:
            return "Pebble does not respond The rock is hibernating."

        self. last_interaction = time.time()
        
        if self.temperament == "Narcissistic":
            self.bond += random.randint(3, 6)
            return "Pebble seems pleased by the attention."
        elif self.temperament == "Argumentative":
            if random.random() < 0.4:
                self.mood = "Agitated"
                return "Pebble bristles at your attempt."
            else:
                self.bond += 2
                return "Pebble reluctantly accepts your affirmation."

        else:
            self.bond += random.randint(1, 4)
            return "Pebble seems to appreciate the gesture."

    def disturb(self):
        if self.is_hibernating:
            return "Pebble does not respond. The rock is hibernating."

        self.last_interaction = time.time()

        if random.random() < (self.stability / 120):
            return "Pebble remains unmoved."
        else:
            self.mood = random.choice (["Mad", "Agitated", "Stressed"])
            return "Pebble reacts negatively to the disturbance."

    def attempt_wake(self):
        if not self.is_hibernating:
            return "Pebble is already awake."

        if random.random() < (self.bond / 200):
            self.is_hibernating = False
            self.mood = "Content"
            self.last_interaction = time.time()
            return "Pebble slowly stirs and regains awareness."
        else:
            return "The rock remains unresponsive."
