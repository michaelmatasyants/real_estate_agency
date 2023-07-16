# Website of real estate agency

The website is under development, so only the page with the list of flats and admin for filling the database are available.

### How to run

1. Firstly, you have to install python and pip (package-management system) if they haven't been already installed.

2. Create a virtual environment with its own independent set of packages using [virtualenv/venv](https://docs.python.org/3/library/venv.html). It'll help you to isolate the project from the packages located in the base environment.

3. Install all the packages used in this project, in your virtual environment which you've created on the step 2. Use the `requirements.txt` file to install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Create a database file and apply all migrations at once:
    ```sh
    python3 manage.py migrate
    ```
   
5. Run the server for development and 
    ```sh
    python3 manage.py runserver
    ```

6. Create superuser to see/edit the data on admin page:
    Input
    ```sh
    python3 manage.py createsuperuser
    ```

7. Open admin page and login in with password, you've entered on previous step:
   `http://127.0.0.1:8000/admin/`

### Environment variables

Some of the project settings come from environment variables. To define them, create a file `.env` next to `manage.py` and write data in this format: `VARIABLE=value`.

Three variables are available:
- `DEBUG` — debug mode. Set it to True to see debugging information in case of an error.
- `SECRET_KEY` — project secret key
- `ALLOWED_HOSTS` — see [Django docs](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).


## Project Objectives

The code is written for educational purposes
