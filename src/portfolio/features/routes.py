from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from src.portfolio.features.authn import UserSignup
from src.portfolio.database.integretion import get_connection
from passlib.context import CryptContext

app = FastAPI()

templates = Jinja2Templates(directory="src/portfolio/templates")



@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse, tags=["Home"])
async def home(request: Request,) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})
    

@app.get("/signup/", tags=["Authn"])
async def get_signup(request: Request,) -> HTMLResponse:
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup/", response_class=HTMLResponse, tags=["Authn"])
async def signup(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
):
    conn = get_connection()
    #pswd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    #hashed_password = pswd_context.hash()
    valid_user = UserSignup(
         username=username,
         email=email,
         password=password
    )
    if valid_user:
        with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                    (username, email, password)
                )
        conn.commit()
        return templates.TemplateResponse("index.html", {"request": request, "message": "Signup successful!"})
    else:
        return templates.TemplateResponse("signup.html", {"request": request, "message": "Signup failed. Please try again."})
    
@app.post("/login", response_class=HTMLResponse, tags=["Authn"])
async def login(request: Request,) -> HTMLResponse:
    return templates.TemplateResponse("login.html", {"request": request})



































