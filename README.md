# weather-api

## Description
FastAPI project for Weather outfit and activity recommendation along with Generative AI synopsis.

## Documentation to use endpoints
![swagger-docs](./docs)
![openapi-docs](./api/openapi.json)

##  🎉 Main Features:
1. FastAPI Implementation: Utilizes FastAPI to build RESTful endpoints, adhering to REST architecture norms.
2. Weather Data Fetching: Integrates real-time weather data using a third-party WeatherAPI.
3. Generative Language Model Integration: Uses "meta/llama-2" model but have another option to use own LLM model to formulate a comical weather synopsis.
4. Recommendations System: Provide recommendations for activities and outfits based on the weather data analysis.
5. CRUD Operations: Offers CRUD endpoints for managing outfir & activity recommendation configurations.

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
DB_USER=<your db user>
DB_PASSWORD=<your db password>
DB_HOST=localhost
DB_PORT=3306
PROJECT_NAME="<Project Name>"
REPLICATE_API_TOKEN="<please use Replicate Token>"

# postgres case
ENV=dev
DB=postgresql
DB_USER=<your db user>
DB_PASSWORD=<your db password>
DB_HOST=localhost
DB_PORT=5432
PROJECT_NAME="<Project Name>"
REPLICATE_API_TOKEN="<please use Replicate Token>"
```

![image](https://github.com/akramwarsi/Weather-Recommendation-API/assets/50487227/a83c192d-71be-4072-af30-4e18a51862ae)
![image](https://github.com/akramwarsi/Weather-Recommendation-API/assets/50487227/3fefb361-1ae6-49fa-b64f-8f6a9c31ee88)
![image](https://github.com/akramwarsi/Weather-Recommendation-API/assets/50487227/11d928ae-d4f8-41c1-a959-b634717eaf60)

