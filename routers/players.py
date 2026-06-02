from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List

from database import get_db
from models import Player
from schemas import PlayerSummary, PlayerDetail


router=APIRouter()

@router.get("/", response_model=List[PlayerSummary])
def get_players(db: Session= Depends(get_db)):
    return db.query(Player).order_by(Player.position, Player.name).all()

@router.get("/{player_id}", response_model=PlayerDetail)
def get_player(player_id: int, db: Session = Depends(get_db)):
    player=(
        db.query(Player)
        .options(
            joinedload(Player.career_highlights),
            joinedload(Player.recent_performances)
        )
        .filter(Player.id == player_id)
        .first()
    )

    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
