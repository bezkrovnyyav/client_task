# Project description

- This app get data from the site [jsonplaceholder](https://jsonplaceholder.typicode.com/).
- The data is saved in the variable api_response.
- The data is displayed in the console.
---
# Instructions for configuring and launching the project

**1.** Clone the repository:

    git clone https://github.com/bezkrovnyyav/client_task.git
   
**2.** Create a virtual environment and activate it in Windows:

    cd client_task
    python -m venv env
    env\Scripts\activate

**3.** Install dependencies:

    pip install -r requirements_dev.txt

**4.** Start the app:

    python main.py

# Instructions for testing the project

**1.** Clone the repository:

    git clone https://github.com/bezkrovnyyav/client_task.git
   
**2.** Create a virtual environment and activate it in Windows:

    cd client_task
    python -m venv env
    env\Scripts\activate

**3.** Install dependencies:

    pip install -r requirements_test.txt

**4.** Run linter:

    flake8 .
