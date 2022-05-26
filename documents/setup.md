# On local

1. Install virtual environment: `python3 -m venv venv && source venv/bin/activate`

2. Install all packages: `pip install -r requirements.txt`

3. Clone file ` cp .env.example .env` and config `.env`

4. Clone file ` cp ./tests/.env.example ./tests/.env` and config `.env`

5. Testing: `python -m pytest tests/`

6. Start dev server `export FLASK_APP=flaskr && export FLASK_ENV=development && flask run --port 5001`. You can use SQLite if running at local

# On docker

1. Clone file `cp .env.example .env` and config `.env`

2. Clone file ` cp ./tests/.env.example ./tests/.env` and config `.env`

3. Run docker compose: `docker-compose up -d` 

4. Generate MySQL schema: `docker exec pythonflask flask init-db`

5. Testing: `docker exec pythonflask python -m pytest tests/`
