from fastapi import FastAPI
import uvicorn
from dotenv import dotenv_values
from pymongo import MongoClient
from routes.api import router as api_router
config = dotenv_values(".env")

app = FastAPI()

@app.on_event('startup')
async def startup_db_client():
    app.mongo_client = MongoClient(config['URI'])
    app.database = app.mongo_client[config['DB_NAME']]
    print("Project Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(api_router)



