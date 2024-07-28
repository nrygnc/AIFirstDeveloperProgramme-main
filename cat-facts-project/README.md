**Cat Facts Application**

This Streamlit application fetches cat facts from an API, stores them in a SQLite database, and allows users to view the saved facts.

**Features:**
:arrow_down_small:
1. Fetches cat facts from a public API.
2. Saves retrieved facts to a SQLite database.
3. Displays all stored cat facts.

****Getting Started****
:arrow_down_small:
1. **Install dependencies:**

 **Bash**
 _pip install streamlit requests sqlalchemy_

2. **Run the application:**

**Bash**
_python cat_facts_app.py_ (or your script name)


****Using the Application****

The application has two buttons:

* **Fetch and Save New Cat Facts:** This button retrieves new cat facts from the API and saves them to the database. In case of any errors during the API call, an error message will be displayed.
* **Display Cat Facts from Database:** This button displays all the cat facts currently stored in the database.

**Code Structure**


**_fetch_cat_facts_ function:** Fetches JSON data containing cat facts from the API.
**_save_cat_facts_ function:** Saves retrieved cat facts (text) to the SQLite database.
**_display_cat_facts_ function:** Queries the database and displays all stored cat facts.
**_main_ function**: Builds the Streamlit application layout and handles button clicks.

**Technologies Used**

* Streamlit: A Python library for building web apps.
* Requests: A library for making HTTP requests.
* SQLAlchemy: A library for interacting with relational databases.


**Database**

The application uses a SQLite database named `cat_facts.db` to store the retrieved cat facts.

**Further Development**

* Implement functionalities to:
Delete specific cat facts.
Search for cat facts based on keywords.
* Add visual enhancements to the application.

**Note:**
:astonished:
This is a basic example showcasing data fetching, database interaction, and a user interface using Streamlit. You can customize and extend it further based on your requirements.

:+1::+1::+1:

**Screenshots**

:camera_flash:


**Application Output **

![Cat fact](Ekran Resmi 2021-09-29 14.52.52.png)

<img width="1132" alt="Ekran Resmi 2024-07-28 18 13 36" src="https://github.com/user-attachments/assets/5614405e-acb4-4f18-8997-4b957a2c7541">


:point_right: [View the application](http://localhost:8501/)

****
```

# Create the README.md file
with open('README.md', 'w') as file:
    file.write(readme_content)
```

Finally, we can create a new repository on GitHub and push the code to it.

# Push the code to GitHub
!git init
!git add .
!git commit -m "Initial commit"
!git branch -M main
!git remote add origin
