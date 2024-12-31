from fastapi import FastAPI
from feature.main import app as feature_app
from campus.main import app as campus_app 
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(feature_app, prefix="/feature", tags=["feature"])
app.include_router(campus_app, prefix="/campus", tags=["campus"]) 
