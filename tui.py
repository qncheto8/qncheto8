def display_main_menu():
    """Display the main menu and return the user's choice."""
    print("Main Menu")
    print("A. View data")
    print("B. Visualize data")
    print("C. Export Park Data")
    print("D. Exit")
    choice = input("Enter your choice: ")
    return choice.upper()


def display_sub_menu_a():
    """Display sub-menu for viewing data and return the user's choice."""
    print("\nSub-Menu A: View Data")
    print("1. View all reviews for a specific park")
    print("2. Count reviews from a specific location")
    print("3. Average rating for a park in a given year")
    print("4. Display average score per park by reviewer location")
    print("5. Return to main menu")
    return input("Enter your choice: ").strip()


def display_sub_menu_b():
    """Display sub-menu for visualizing data and return the user's choice."""
    print("\nSub-Menu B: Visualize Data")
    print("1. Pie chart of reviews by park")
    print("2. Bar chart of average review scores")
    print("3. Top 10 locations for a park")
    print("4. Average rating by month")
    print("5. Return to main menu")
    return input("Enter your choice: ").strip()


def display_message(message):
    """Display a message to the user."""
    print(message)


def display_error(message):
    """Display an error message to the user."""
    print(f"Error: {message}")


def get_park_name():
    """Prompt the user to enter a park name."""
    return input("Enter park name: ").strip()


def get_location_name():
    """Prompt the user to enter a reviewer location."""
    return input("Enter reviewer location: ").strip()


def get_year():
    """Prompt the user to enter a year."""
    return input("Enter year (e.g., 2023): ").strip()


def get_export_format():
    """Prompt the user to enter the export format."""
    return input("Enter the format (txt, csv, json): ").lower()


def get_filename():
    """Prompt the user to enter the filename."""
    return input("Enter the filename: ")
