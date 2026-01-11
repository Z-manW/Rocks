from core.rock import Rock
import time

rock = Rock("Pebble")

while True:
    # Check neglect and print any state changes
    message = rock.check_neglect()
    if message:
        print(message)

    # Ambient thoughts
    thought = rock.ambient_thought()
    if thought:
        print(f"[ambient] {thought}")

    print("\nChooose an action:")
    print("1. observe")
    print("2. affirm")
    print("3. disturb")
    print("4. wait")
    print("5. wake")
    print("6. quit")

    choice = input("> ").strip().lower()

    if choice in ("1", "observe"):
        print(rock.observe())
    elif choice in ("2", "affirm"):
        print(rock.affirm())
    elif choice in ("3", "disturb"):
        print(rock.disturb())
    elif choice in ("4", "wait"):
        print("You leave the rock alone.")
    elif choice in ("5", "wake"):
        print(rock.attempt_wake())
    elif choice in ("6", "quit"):
        break
    else:
        print ("Invalid choice.")

    print("-" * 50)
    time.sleep(3)
