# ISDN 4002

## 1 Run the project

### 1.1 Backend

Please first install the dependency (conda):

```bash
conda create -n linking python=3.7
conda activate linking
pip install Flask==2.2.2, python-dotenv, flask-cors
```

Then, run the flask backend:

```bash
flask run
```

Note: .env file controls the environment config.

```python
FLASK_APP=backend  # Choose which flask module as backend entry: backend/demo ("demo" is for a simple test).
FLASK_DEBUG=True  # Decide development/production mode.
```