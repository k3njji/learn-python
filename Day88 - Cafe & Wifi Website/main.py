from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel
import csv

app = FastAPI()
templates = Jinja2Templates(directory="templates")

engine = create_engine(
    'sqlite:///C:/Python by Angela Yu/Day88 - Cafe & Wifi Website/instance/posts.db',
    connect_args = {'check_same_thread': False}
)


SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

class Cafe(Base):
    __tablename__ = 'cafes'
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    link = Column(String, nullable = False)
    open = Column(String, nullable = False)
    close = Column(String, nullable = False)
    coffee = Column(String, nullable = False)
    power = Column(String, nullable = False)
    wifi = Column(String, nullable = False)

Base.metadata.create_all(engine)

class CafeCreate(BaseModel):
    name: str
    link: str
    open: str
    close: str
    coffee: str
    wifi: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Add cafe (GET)
@app.get("/add", response_class=HTMLResponse)
def add_cafe_form(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})

# Add cafe (POST)
@app.post("/add")
def add_cafe(
    cafe: str = Form(...),
    link: str = Form(...),
    open: str = Form(...),
    close: str = Form(...),
    coffee: str = Form(...),
    wifi: str = Form(...),
    power: str = Form(...),
    db: Session = Depends(get_db)
):
    new_user = Cafe(
        name = cafe,
        link = link,
        open = open,
        close = close,
        coffee = coffee,
        power = power,
        wifi = wifi
    )
    print(new_user)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return RedirectResponse(url="/cafes", status_code=303)

@app.get("/cafes", response_class=HTMLResponse)
def cafes(request: Request, db: Session = Depends(get_db)):
    cafes_db = db.query(Cafe).all()

    return templates.TemplateResponse(
        "cafes.html",
        {"request": request, "cafes": cafes_db}
    )