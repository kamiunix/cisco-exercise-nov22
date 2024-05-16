# Malware URL Lookup Service

This is a simple web service implemented in Python using Flask. It allows users to check if a given URL is known to contain malware.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/malware-url-lookup.git
    ```

2. Navigate to the project directory:

    ```bash
    cd malware-url-lookup
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

5. Install Flask inside the virtual environment:

    ```bash
    pip install flask
    ```

## Usage

1. Ensure you have Python installed on your machine.
2. Run the Flask application by executing the following command:

    ```bash
    python service.py
    ```

3. Once the service is running, you can access it through a web browser or make GET requests programmatically. Here's an example URL to check if `example.com` is safe:

    ```
    http://127.0.0.1:5000/v1/urlinfo/example.com
    ```

    This will return a JSON response indicating whether the URL is safe or not.

## Configuration

The list of malicious URLs is stored in a JSON file named `malicious_urls.json`. You can modify this file to add or remove malicious URLs as needed.

