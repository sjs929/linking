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

Note: .env file controls the environment config.

```python
FLASK_APP=backend  # Choose which flask module as backend entry: backend
FLASK_DEBUG=True  # Decide development/production mode.
```

### 1.3 API

#### 1.3.1 Simple Test

A simple test to verify whether Flask flamework is installed correctly. 

```cmd
URL: http://127.0.0.1:5000/hello
Return: HTML - "Linking! Hello, World!" 
```

```cmd
URL: http://127.0.0.1:5000/login
Return: HTML - A demo page for log in
```

```welcome
URL: http://127.0.0.1:5000/welcome
Return: JSON - {
            "Class": "ISDN 4002",
            "Project": "Linking"
        }
```