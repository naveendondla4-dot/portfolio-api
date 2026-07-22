from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Contact(BaseModel):
    name: str
    email: str
    subject: str
    message: str


@app.get("/")
def home():
    return {"message": "Portfolio API Running"}


@app.post("/contact")
def contact(data: Contact):
    print(data)
    return {"message": "Message Sent Successfully"}
