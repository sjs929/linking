# ISDN 4002

An application to notify about the detailed content of the sound, such as whether the sound is “watch out”, “excuse me” or their name and the direction with a history list on their phone.
## 1 Backend

### 1.1 Build

Please first install the dependency (conda):

```bash
conda create -n linking python=3.7
conda activate linking
pip install Flask==2.2.2 python-dotenv flask-cors
```

### 1.2 Run

Then, run the flask backend:

```bash
flask run
```

Note: .env file controls the environment configuration.

```python
FLASK_APP=backend  # Choose which flask module as entry: backend
FLASK_DEBUG=True  # Decide development/production mode.
FLASK_RUN_HOST = '0.0.0.0'  # Backend IP Address
FLASK_RUN_PORT = '8081'  # Backend Port
```

### 1.3 API

#### 1.3.1 Simple Test

A simple test to verify whether Flask flamework is installed correctly. 

```cmd
URL: http://<ip_address>/hello
Return: String - "Linking! Hello, World!" 
```

```cmd
URL: http://<ip_address>/login
Return: HTML - A demo page for log in
```

```cmd
URL: http://<ip_address>/welcome
Return: JSON - {
            "Class": "ISDN 4002",
            "Project": "Linking"
        }
```

```cmd
URL: http://<ip_address>/request?inputstr="<text>"
Return: String - <text>
```