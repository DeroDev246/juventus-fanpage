from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List

from database import get_db
from models import Match, MatchStatusEnum
from schemas import MatchOut

router=APIRouter()

def _load_matches(db:Session, status: MatchStatusEnum = None):
    q = db.query(Match).options(joinedload(Match.scorers))
    if status:
        q = q.filter(Match.status == status)

    return q.order_by(Match.id.desc()).all()

@router.get("/", response_model=dict)
def get_all_matches(db: Session = Depends(get_db)):
    def serialize (matches):
        return [MatchOut.model_validate(m) for m in matches]
    return{
        "upcoming" : serialize(_load_matches(db, MatchStatusEnum.upcoming)),
        "result" : serialize(_load_matches(db, MatchStatusEnum.result)),
        "live" : serialize(_load_matches(db, MatchStatusEnum.live)),
    }

@router.get("/upcoming", response_model=List[MatchOut])
def get_upcoming(db: Session = Depends(get_db)):
    return _load_matches(db, MatchStatusEnum.upcoming)

@router.get("/results", response_model=List[MatchOut])
def get_results(db: Session = Depends(get_db)):
    return _load_matches(db, MatchStatusEnum.results)

@router.get("/live", response_model=List[MatchOut])
def get_live(db: Session = Depends(get_db)):
    return _load_matches(db, MatchStatusEnum.live)

@router.get("/{match_id}", response_model=MatchOut)
def get_match(match_id: int, db: Session = Depends(get_db)):
    match = (
        db.query(Match)
        .options(joinedload(Match.scorers))
        .filter(Match.id == match_id)
        .first()
    )

    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    
    return match