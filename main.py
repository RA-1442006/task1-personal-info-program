"""
Personal Information Program
Task 1: Python Internship
Description: Collects user information via console input, validates numeric values,
computes additional metrics, and displays a clean formatted profile card.
"""

def main():
    print("=" * 58)
    print(f"{'WELCOME TO THE PERSONAL INFO SYSTEM':^58}")
    print("=" * 58)
    print("Please answer the following questions to build your profile.\n")

    # ---------------------------------------------------------
    # Section 1: Collecting User Inputs
    # ---------------------------------------------------------

    # 1. Full Name (String)
    while True:
        full_name = input("Enter your full name: ").strip()
        if full_name:
            break
        print("Error: Full name cannot be empty. Please try again.")

    # 2. Age (Integer with error handling)
    while True:
        try:
            age_input = input("Enter your age (in years): ").strip()
            age = int(age_input)
            if age <= 0:
                print("Error: Age must be a positive number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid whole number for age (e.g., 21).")

    # 3. Height in cm (Float with error handling)
    while True:
        try:
            height_input = input("Enter your height in centimeters (cm): ").strip()
            height_cm = float(height_input)
            if height_cm <= 0:
                print("Error: Height must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid decimal number for height (e.g., 175.5).")

    # 4. City (String)
    while True:
        city = input("Enter your city of residence: ").strip()
        if city:
            break
        print("Error: City cannot be empty. Please try again.")

    # 5. Email (String)
    while True:
        email = input("Enter your email address: ").strip()
        if "@" in email and "." in email.split("@")[-1] and " " not in email:
            break
        print("Error: Please enter a valid email address (e.g., name@example.com).")

    # 6. Favorite Programming Language (String)
    while True:
        fav_language = input("Enter your favorite programming language: ").strip()
        if fav_language:
            break
        print("Error: Favorite programming language cannot be empty. Please try again.")

    # 7. Hobby (String)
    while True:
        hobby = input("Enter your primary hobby: ").strip()
        if hobby:
            break
        print("Error: Hobby cannot be empty. Please try again.")

    # 8. Short Goal (String)
    while True:
        career_goal = input("Enter your short one-line goal: ").strip()
        if career_goal:
            break
        print("Error: Goal cannot be empty. Please try again.")

    # ---------------------------------------------------------
    # Section 2: Calculated Fields (Data Processing)
    # ---------------------------------------------------------

    # Calculation 1: Age in 5 years
    age_in_5_years = age + 5

    # Calculation 2: Convert height in cm to feet and inches
    # 1 inch = 2.54 cm, 1 foot = 12 inches
    total_inches = round(height_cm / 2.54)
    height_feet, height_inches = divmod(total_inches, 12)

    # ---------------------------------------------------------
    # Section 3: Formatted Output (Profile Card)
    # ---------------------------------------------------------

    card_width = 58
    border_thick = "=" * card_width
    border_thin = "-" * card_width

    print("\n" + border_thick)
    print(f"{'USER PROFILE CARD':^{card_width}}")
    print(border_thick)

    # Personal Information
    print(f"  {'Field':<24} | {'Details'}")
    print(border_thin)
    print(f"  {'Full Name':<24} | {full_name}")
    print(f"  {'Current Age':<24} | {age} years")
    print(f"  {'Age in 5 Years':<24} | {age_in_5_years} years")
    print(f"  {'Height':<24} | {height_cm:.1f} cm ({height_feet} ft {height_inches} in)")
    print(border_thin)

    # Contact & Location
    print(f"  {'City':<24} | {city}")
    print(f"  {'Email':<24} | {email}")
    print(border_thin)

    # Interests & Ambitions
    print(f"  {'Favorite Language':<24} | {fav_language}")
    print(f"  {'Primary Hobby':<24} | {hobby}")
    print(f"  {'One-Line Goal':<24} | {career_goal}")
    print(border_thick)
    print(f"{'Profile generated successfully!':^{card_width}}")
    print(border_thick + "\n")


if __name__ == "__main__":
    main()
