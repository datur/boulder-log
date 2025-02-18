# Boulder Log

A web application allowing users to upload photos of the boulders they have climbed. Users can also view photos of boulders uploaded by other users.

## How to run the application

1. Clone the repository

2. Install project tooling
 - [uv](https://arc.net/l/quote/mbjdcymf) for requirements management

2. Configure virtual environment
```bash
# Create a virtual environment
uv uv python install 3.12
uv venv --python 3.12.7

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
uv sync
```

3. Create application state
```bash
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

```

4. Run the application
```bash
python manage.py runserver
```

## Database modeling

The initial database model for the application is shown below:

https://drawsql.app/teams/dave-1/diagrams/boulder-log