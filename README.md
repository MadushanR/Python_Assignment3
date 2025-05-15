# Basic Python Bank App

A simple command-line banking application built in Python that lets users manage Savings and Chequing accounts.

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Contributing](#contributing)

## Features

* **Account Management**: Create and view Savings and Chequing accounts.
* **Transactions**: Deposit to and withdraw from accounts.
* **Transfers**: Move money between Savings and Chequing.
* **Balance Inquiry**: Check current balances.
* **Transaction History**: View a simple log of recent transactions.
* **Command-Line Interface**: Interactive text-based menu system.

## Tech Stack

* **Language**: Python 3.6+

## Prerequisites

* Python 3.6 or higher installed.
* (Optional) Virtual environment tool (`venv` or `virtualenv`).

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MadushanR/Python_Assignment3.git
   cd Python_Assignment3
   ```
2. **(Optional) Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\\Scripts\\activate
   ```
3. **Install dependencies** (if any are listed in `requirements.txt`):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main application:

   ```bash
   python bank_app.py
   ```
2. Follow on-screen prompts to:

   * Create a user and select account type (Savings or Chequing)
   * Deposit or withdraw funds
   * Transfer between accounts
   * View balances and transaction history
3. Exit the application by choosing the **Exit** option from the menu.

## Project Structure

```plaintext
basic-python-bank-app/
├── bank_app.py         # Main program with CLI menu
├── accounts.py         # Account classes (Savings, Chequing)
├── transactions.py     # Transaction and transfer logic
├── data/               # (Optional) Persistent data files
├── requirements.txt    # Project dependencies
└── README.md # This file
```

## Contributing

1. ⭐️ Fork the repo.
2. 🔀 Create a branch (`git checkout -b feature/YourFeature`).
3. 🛠️ Make your changes.
4. 📄 Commit (`git commit -m "Add feature"`).
5. 🚀 Push (`git push origin feature/YourFeature`).
6. 🔎 Open a Pull Request.


---

> *Built with 🏦 and 🐍 in Python*
