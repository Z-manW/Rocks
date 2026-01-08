from core.rock import Rock
import time

rock = Rock("Pebble")

while True:
    message = rock.check_neglect()
    if message:
        print(message)


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

    choice = input("> ").strip()

    if choice == "1":
        print(rock.observe())
    elif choice == "2":
        print(rock.affirm())
    elif choice == "3":
        print(rock.disturb())
    elif choice == "4":
        print("You leave the rock alone.")
    elif choice == "5":
        print(rock.attempt_wake())
    elif choice == "6":
        break

    print("-" * 50)
    time.sleep(4)
