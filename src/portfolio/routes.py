from uuid import UUID

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from portfolio.authn import UserSignup
from portfolio.database.db import get_conn

app = FastAPI()

templates = Jinja2Templates(directory="src/portfolio/templates")



@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse, tags=["Home"])
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/signup/", tags=["Authn"])
async def get_signup(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup/", response_class=HTMLResponse, tags=["Authn"])
async def signup(request: Request) -> HTMLResponse:
    conn = get_conn()
    form_data = await request.form()
    valid_user = UserSignup(**form_data)
    if valid_user.is_valid():
        with conn.cursor() as cur:
                user_id = UUID("your-uuid-here")
                cur.execute(
    "SELECT * FROM users WHERE id = %s",
    (user_id,),
)
        conn.commit()
        return templates.TemplateResponse("index.html", {"request": request, "message": "Signup successful!"}) #Ignore
    return templates.TemplateResponse("signup.html", {"request": request, "message": "Signup failed. Please try again."})

@app.post("/login", response_class=HTMLResponse, tags=["Authn"])
async def login(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("login.html", {"request": request})



































