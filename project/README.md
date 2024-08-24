## BANKING SYSTEM

Name: Aayush Singh
Github username: aayush3692
edx username: aayushsingh1239

Video overview: <https://youtu.be/CvMfmo_qTfs>

### Project Overview

Welcome to the **BANK!!** application, a simple command-line banking system that allows users to manage accounts, deposit and withdraw funds, and transfer money between accounts. This program is designed to provide a basic simulation of banking operations using Python. It leverages file I/O to store customer information in a text file, making it accessible for basic operations like viewing balances, depositing, withdrawing, and transferring money.

The application is intended to demonstrate basic programming concepts such as input/output operations, conditionals, loops, file handling, and simple error handling. It's a useful educational tool for those learning Python and trying to understand how banking operations might be implemented in a simple console-based environment.

### Project Structure

The project consists of the following main Python files:

1. **`bank_program.py`**: This is the main program file. It contains all the functions needed to perform banking operations such as adding an account, showing the balance, depositing money, withdrawing money, and transferring money between accounts. The program runs in a loop, allowing users to perform multiple operations until they choose to exit.

2. **`customers.txt`**: This text file acts as a simple database for storing customer information. Each line represents a customer and contains the customer's name, account number, and current balance, separated by commas. The program reads from and writes to this file to update account balances and other information as needed.

### Features and Functions

The **BANK!!** application includes the following functionalities:

- **Show Balance**: Displays the balance of a specified account. The user is prompted to enter their account number, and if it exists, the program retrieves and displays the balance.

- **Deposit Money**: Allows the user to deposit a specified amount into their account. The program checks if the account exists and updates the balance accordingly. Invalid or negative deposit amounts are rejected.

- **Withdraw Money**: Enables the user to withdraw a specified amount from their account. The program ensures there are sufficient funds before processing the withdrawal.

- **Add Account**: Allows the user to add a new account by entering the customer’s name, account number, and initial balance. This information is appended to the `customers.txt` file.

- **Transfer Money**: Facilitates transferring funds between two accounts. The program checks for sufficient funds in the sender's account and updates both accounts upon a successful transfer.

- **Exit**: Exits the program after thanking the user for using the banking service.

### Design Choices

- **File-Based Storage**: The program uses a simple text file (`customers.txt`) to store customer data. This choice was made for simplicity and ease of use, as it allows users to manually inspect and edit account data. However, this method is not suitable for large-scale applications or those needing high security or efficiency.

- **Error Handling**: The program includes basic error handling for file operations and input validation. For example, it checks for file existence before reading or writing and validates user input to ensure it is numeric where required. This approach prevents common runtime errors and improves user experience by providing feedback on invalid input.

- **Global Variable Usage**: The program uses global variables minimally (e.g., `amount`), preferring to pass parameters and return values directly to reduce dependencies and increase code clarity. This design decision promotes modularity and makes the code easier to understand and maintain.

### Future Improvements

While the current implementation is functional and meets basic requirements, several improvements could be made:

- **Data Persistence and Security**: Migrating from a text file to a database system such as SQLite or MySQL would enhance data security and performance, particularly for larger datasets.

- **User Authentication**: Adding a feature for user authentication (e.g., usernames and passwords) would make the application more secure by restricting access to personal financial data.

- **Error Handling and Logging**: Enhancing error handling and incorporating logging mechanisms would make the application more robust and easier to debug and maintain.

- **GUI Development**: Developing a graphical user interface (GUI) would make the application more user-friendly and accessible to users who are not comfortable with command-line interfaces.

By implementing these improvements, the application could evolve into a more sophisticated and user-friendly tool, potentially serving as a foundation for more advanced projects in the future.

---

This README.md file provides a comprehensive overview of your project, including its purpose, functionality, design decisions, and potential areas for enhancement.
