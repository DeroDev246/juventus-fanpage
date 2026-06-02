from pydantic import BaseModel
from typing import List, Optional
from models import PositionEnum, MatchStatusEnum


# PLAYER SCHEMAS

class CareerHighlightOut(BaseModel):
    id: int
    highlight: str
    
    class Config:
        from_attributes = True


class RecentPerformanceOut(BaseModel):
    id: int
    opponent: str
    date: str
    result: str
    rating: float
    saves: Optional[int]=None

    class Config:
        from_attributes = True


class PlayerSummary(BaseModel):
    id: int
    name: str
    position: PositionEnum
    age: int
    nationality: str
    number: int
    image_initials: str
    goals: int
    assists: int
    appearances: int
    rating: float
    market_value: Optional[str]

    class Config:
        from_attributes = True


class PlayerDetail(PlayerSummary):
    foot: Optional[str]
    height: Optional[str]
    joined: Optional[str]
    contract_until: Optional[str]
    bio: Optional[str]
    career_highlights: List[CareerHighlightOut] = []
    recent_performances: List[RecentPerformanceOut] = []

    class Config:
        from_attributes= True


class PlayerCreate(BaseModel):
    name: str
    position: PositionEnum
    age: int
    nationality: str
    number: int
    image_initials: str
    goals: int = 0
    assists: int = 0
    appearances: int = 0
    rating: float = 0.0
    market_value: Optional[str] = None
    foot: Optional[str] = None
    height: Optional[str] = None
    joined: Optional[str] = None
    contract_until: Optional[str] = None
    bio: Optional[str] = None


class PlayerUpdate(BaseModel):
    name: Optional[str] = None
    position: Optional[PositionEnum] = None
    age: Optional[int] = None
    nationality: Optional[str] = None
    number: Optional[int] = None
    goals: Optional[int] = None
    assists: Optional[int] = None
    appearances: Optional[int] = None
    rating: Optional[float] = None
    market_value: Optional[str] = None
    foot: Optional[str] = None
    height: Optional[str] = None
    joined: Optional[str] = None
    contract_until: Optional[str] = None
    bio: Optional[str] = None

# MATCH SCHEMAS 

class ScorerOut(BaseModel):
    id: int
    player: str
    minute: int
    team: str

    class Config:
        from_attributes = True


class MatchOut(BaseModel):
    id: int
    home: str
    away: str
    home_score: Optional[int]
    away_score: Optional[int]
    date: str
    time: Optional[str]
    competition: str
    matchday: Optional[str]
    venue: Optional[str]
    status: MatchStatusEnum
    minute: Optional[int]
    scorers: List[ScorerOut] = []

    class Config:
        from_attributes = True


class MatchCreate(BaseModel):
    home: str
    away: str
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    date: str
    time: Optional[str] = None
    competition: str
    matchday: Optional[str] = None
    venue: Optional[str] = None
    status: MatchStatusEnum = MatchStatusEnum.upcoming
    minute: Optional[int] = None