## Install and setup
Poetry is used as package managment system. You can find it and installation guide at [Poetry official site](https://python-poetry.org/docs/)

### Step 1. Initializing poetry
Installing from poetry is pretty simple. Just type
```
poetry install
```
at the project directory

### Step 2. Create configuration
Create file `config.yaml` in project directory and fill it as it shown in `config.yaml.example`

### Step 3. Initialize alembic
Go to poetry shell with command
```
poetry shell
```
and apply all migrations with command
```
alembic upgrade head
```

### Step 4. Launch the app!
Go to poetry shell if you are outside it as described in [step 3](#step-3-initialize-alembic)
and just type
```
python main.py
```
or
```
uvicorn main:app
```