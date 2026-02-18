# Import variables from zaj01
from python1course.zaj01 import ja, rok

# Import classes from zaj04 (Ambulance System)
from python1course.zaj04 import Driver, Incident


def main():
    print("--- START: Testing Package python1course ---")

    # 1. Testing zaj01 variables
    print("\n[TEST] Data from zaj01:")
    print(f"Student: {ja.get('imie', 'Unknown')} {ja.get('nazwisko', '')}")
    print(f"Course Year: {rok}")

    # 2. Testing zaj04 classes
    print("\n[TEST] Classes from zaj04 (Fleet/Personnel/Operations):")

    try:
        # Creating Driver object
        # Arguments: name, surname, rate, license_number, qualifications
        driver1 = Driver(
            "Jan",
            "Kowalski",
            15.0,
            "LIC-12345",  # Added license number
            ["First Aid", "Driving"],  # Added qualifications list
        )
        print(f" -> Created Driver: {driver1}")

        # Creating Incident object
        # Arguments: type, address, priority
        incident1 = Incident("Accident", "Main Street 1", 1)
        print(f" -> Created Incident: {incident1}")

    except TypeError as e:
        print(f"ERROR creating objects: {e}")
        print("Tip: Check __init__ in your class files for required arguments.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("\n--- END: Package works! ---")


if __name__ == "__main__":
    main()
