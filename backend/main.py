from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.chat_routes import router as chat_router
from endpoints.database_routes import router as database_router


app = FastAPI()

# Cors Settings
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True, # For CORS between internal API calls,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include routes
app.include_router(chat_router)
app.include_router(database_router)