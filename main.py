from fastapi import FastAPI
from routes import router as users_router  # Update the import to the new file name

app = FastAPI()

app.include_router(users_router)
