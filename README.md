# weather-api-rak-bank

## Description
FastAPI project for Weather outfit and activity recommendation along with Generative AI synopsis.

## Documentation to use endpoints
![swagger-docs](./docs)
![openapi-docs](./api/openapi.json)

##  🎉 Main Features:
● FastAPI Implementation: Utilizes FastAPI to build RESTful endpoints, adhering to REST architecture norms.
● Weather Data Fetching: Integrates real-time weather data using a third-party WeatherAPI.
● Generative Language Model Integration: Uses "meta/llama-2" model but have another option to use own LLM model to formulate a comical weather synopsis.
● Recommendations System: Provide recommendations for activities and outfits based on the weather data analysis.
● CRUD Operations: Offers CRUD endpoints for managing outfir & activity recommendation configurations.

## concept
1. Minimal functionality.
2. Convincing Clean architecture.
3. Easy to read.
4. Compatibility.
5. Versatility.

## tables/models
1. recommendation

## integrated with
1. Python 3.9+
2. Fastapi
3. Database
   1. MySQL
   2. Migration with alembic
   3. pytest with real DB
   4. Load with two ways (eager, lazy)
   5. Modeling with schema
4. dependency-injector
   1. service-repository pattern
5. Deployment
   1. container environment (docker)

## commands
1. db(alembic)
   1. `alembic upgrade head`: apply every migrations
   2. `alembic downgrade base`: rollback every migrations
   3. `alembic revision --autogenerate -m "revision_name"`: create new migration 
   4. `alembic history`: get alembic revision history
2. How to migration
   1. Create or modify models from `app/model/*.py`
   2. `alembic -x ENV=[dev|stage|prod] revision --autogenerate -m "revision_name"`
   3. Check auto generated migration file from `app/migrations/versions/*.py`
   4. `alembic -x ENV=[dev|stage|prod] upgrade head`  
      If ENV does not exist, it will be applied to the test.
3. server
   1. `uvicorn app.main:app --reload`: base
   2. options
      1. host: `--host 0.0.0.0`
      2. port: `--port 8000`
4. test
   1. `pytest`: base 
   2. `pytest --cov=app --cov-report=term-missing`: coverage with stdout
   3. `pytest --cov=app --cov-report=html`: coverage with html

## sample env
```dotenv
# mysql case
ENV=dev
DB=mysql
DB_USER=rakbank
DB_PASSWORD=rakbank123
DB_HOST=localhost
DB_PORT=3306

# postgres case
ENV=dev
DB=postgresql
DB_USER=rakbank
DB_PASSWORD=rakbank123
DB_HOST=localhost
DB_PORT=5432
```
