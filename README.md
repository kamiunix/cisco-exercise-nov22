# Malware URL Lookup Service

This is a simple web service implemented in Python using Flask. It allows users to check if a given URL is known to contain malware.

## Installation

1. Clone this repository to your local machine:

    ```bash
   https://github.com/kamiunix/cisco-exercise-nov22.git
   ```

2. Navigate to the project directory:

    ```bash
    cd cisco-exercise-nov22
    ```

3. Create a virtual environment named `venv`:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    On Windows:
    ```bash
    venv\Scripts\activate
    ```

    On Unix or MacOS:
    ```bash
    source venv/bin/activate
    ```

    You should see `(venv)` appear at the beginning of your terminal prompt, indicating that the virtual environment is active.

5. Install Dependencies inside the virtual environment:

    ```bash
   pip install Flask Flask-SQLAlchemy Flask-BasicAuth
    ```

## Usage

1. Ensure you have Python installed on your machine.
2. Initialize the database by running the following command:

    ```bash
    python init_db.py
    ```

    This will create a SQLite database file named `malicious_urls.db` and populate it with the list of malicious URLs.
3. Run the Flask application by executing the following command:

    ```bash
    python service.py
    ```
4. Update the default username and password in the `service.py` file:

    ```python
    app.config['BASIC_AUTH_USERNAME'] = 'username'
    app.config['BASIC_AUTH_PASSWORD'] = 'password'
    ```
   
5. Once the service is running, you can access it through a web browser or make GET requests programmatically. Here's an example URL to check if `example.com` is safe:

    ```
    http://127.0.0.1:5000/v1/urlinfo/example.com
    ```

    This will return a JSON response indicating whether the URL is safe or not.

## Configuration

The list of malicious URLs is stored in a JSON file named `malicious_urls.json`. You can modify this file to add or remove malicious URLs as needed.

## Future Improvements

- Implemented a database to store the list of malicious URLs and check against it. This solves the potential problem of having a large list of URLs that would be inefficient to search through in a JSON file or that could not be handled in memory due to size constraints.
- If the number of requests is expected to be high, we could consider implementing caching mechanisms to reduce the load on the database and improve response times. Simplistically, we could cache the results of previous lookups for a certain period of time. Alternatively, we could use a more sophisticated caching mechanism like Redis or Memcached or make this into a scalable microservice using AWS Lambda, Google Cloud Functions, or containerization with Docker.
- If we need to update the list of malicious URLs frequently, we could implement an admin interface to add or remove URLs from the database. This would require authentication and authorization mechanisms to ensure that only authorized users can make changes. We could also consider implementing a more sophisticated access control mechanism using OAuth or JWT tokens. As for the actual upload method, we could allow users to upload a file with a list of URLs and process it in bulk asynchronously to avoid blocking the main service.
