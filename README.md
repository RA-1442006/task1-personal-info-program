# Personal Information Program

Task 1 — Python Internship Project

---

## 📌 Project Overview

The **Personal Information Program** is a beginner-friendly command-line application developed in Python. It prompts users to enter their personal and professional details, validates numeric and textual inputs, performs basic calculations, and outputs a formatted, aligned profile card using Python f-strings.

---

## 🚀 Key Concepts Covered

- **Variables & Meaningful Naming**: Storing user information with descriptive, clean variable names (`full_name`, `age`, `height_cm`, `career_goal`).
- **User Input (`input()`)**: Interactively collecting strings from the terminal.
- **Type Conversion (Casting)**: Converting string inputs into integers (`int()`) and floating-point numbers (`float()`) for numeric operations.
- **Error Handling (`try / except` & loops)**: Gracefully handling invalid inputs (such as entering letters for age or height) and re-prompting the user until valid data is entered.
- **Data Computation**: Calculating derived values such as future age (`age + 5`) and unit conversion (centimeters to feet & inches).
- **Formatted Output (`f-strings`)**: Structuring and aligning text into a clean console profile card using width specifiers, alignment operators (`<`, `^`), and custom character borders (`=`, `-`).

---

## 🛠️ How to Run the Program

### Prerequisites
- Python 3.6 or newer installed on your machine.
- A terminal, command prompt, or code editor (like VS Code).

### Steps
1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd personal-info-program
   ```
3. Run the Python script:
   ```bash
   python main.py
   ```
4. Follow the interactive prompts in the terminal to enter your information.

---

## 📋 Input Specifications

| Field Name | Data Type | Example Value | Description / Validation |
| :--- | :--- | :--- | :--- |
| `Full Name` | `str` | `Alex Morgan` | User's full name (cannot be empty) |
| `Age` | `int` | `22` | Whole positive number (validated with `try/except`) |
| `Height` | `float` | `175.0` | Height in centimeters (validated with `try/except`) |
| `City` | `str` | `Seattle` | City of residence |
| `Email` | `str` | `alex.morgan@example.com` | User email address (checked for basic `@` and `.`) |
| `Favorite Language` | `str` | `Python` | Favorite programming language |
| `Hobby` | `str` | `Photography` | Primary hobby / leisure activity |
| `Goal` | `str` | `Become a proficient Python developer` | One-line learning or career goal |

### Output Format
The output displays two sections:
1. **Interactive Prompt Section**: Where the user responds to terminal prompts.
2. **Profile Card**: A fixed-width (58 characters), neatly aligned card with:
   - Header with centered title
   - Two-column table (`Field` and `Details`)
   - Calculated fields (`Age in 5 Years` and height in `ft / in`)
   - Thick (`=`) and thin (`-`) character borders

---

## 💻 Sample Output

```text
==========================================================
           WELCOME TO THE PERSONAL INFO SYSTEM            
==========================================================
Please answer the following questions to build your profile.

Enter your full name: Alex Morgan
Enter your age (in years): 22
Enter your height in centimeters (cm): 175.0
Enter your city of residence: Seattle
Enter your email address: alex.morgan@example.com
Enter your favorite programming language: Python
Enter your primary hobby: Photography
Enter your short one-line goal: Become a proficient Python developer and build impactful applications.

==========================================================
                    USER PROFILE CARD                     
==========================================================
  Field                    | Details
----------------------------------------------------------
  Full Name                | Alex Morgan
  Current Age              | 22 years
  Age in 5 Years           | 27 years
  Height                   | 175.0 cm (5 ft 9 in)
----------------------------------------------------------
  City                     | Seattle
  Email                    | alex.morgan@example.com
----------------------------------------------------------
  Favorite Language        | Python
  Primary Hobby            | Photography
  One-Line Goal            | Become a proficient Python developer and build impactful applications.
==========================================================
             Profile generated successfully!              
==========================================================
```

---

## 💡 What I Learned

During this project, I gained hands-on experience with core Python basics:
- Understanding how programs communicate with users through terminal input and output.
- Writing defensive code that anticipates user typing mistakes using `while` loops and `try/except` blocks instead of letting the program crash.
- Performing arithmetic and conversions with multiple data types.
- Controlling text presentation using string formatting syntax instead of messy manual spacing.

---

## ❓ Concept Q&A

### 1. What is a variable in Python?
A **variable** is a named container or reference used in a program to store data in the computer's memory. Once stored, you can reuse, read, or modify that data throughout your code by referring to the variable name (e.g., `age = 22`).

### 2. What is the difference between `input()` and `print()`?
- `input()` is used to **receive data from the user**. It pauses program execution, displays an optional prompt message, waits for the user to type something into the terminal, and returns whatever they typed as a string (`str`).
- `print()` is used to **send data to the screen**. It outputs text, variables, or expressions to the console so the user can read the results.

### 3. What is an f-string?
An **f-string** (Formatted String Literal, introduced in Python 3.6) is a syntax prefixing a string with `f` or `F` (e.g., `f"Hello, {name}"`). It allows embedding Python variables and expressions directly inside curly braces `{}`. F-strings also support format specifiers for width, alignment (`<`, `>`, `^`), and decimal precision (e.g., `{height_cm:.1f}`).

### 4. Why is type conversion required for user input?
In Python, the `input()` function **always returns user data as a string (`str`)**, even if the user enters digits like `"22"`. If you try to perform mathematical operations on strings (such as `"22" + 5`), Python either performs string concatenation or throws a `TypeError`. Converting the string to an integer with `int()` or a float with `float()` is necessary so Python treats the value as a real number for mathematical calculations.
