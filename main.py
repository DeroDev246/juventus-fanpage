from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from database import engine, Base
from routers import players, matches

# Create all tables on startup (safe — skips existing tables)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Juventus Fan Page", version="2.0.0")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(players.router, prefix="/api/players", tags=["players"])
app.include_router(matches.router, prefix="/api/matches", tags=["matches"])


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/players", response_class=HTMLResponse)
async def players_page(request: Request):
    return templates.TemplateResponse("players.html", {"request": request})

@app.get("/players/{player_id}", response_class=HTMLResponse)
async def player_detail(request: Request, player_id: int):
    return templates.TemplateResponse("player_detail.html", {"request": request, "player_id": player_id})

@app.get("/matches", response_class=HTMLResponse)
async def matches_page(request: Request):
    return templates.TemplateResponse("matches.html", {"request": request})
