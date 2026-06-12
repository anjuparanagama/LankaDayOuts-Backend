from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.package import router as package_router

app = FastAPI(title="TiDB FastAPI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(package_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Lanka Day Outs Backend"}   
