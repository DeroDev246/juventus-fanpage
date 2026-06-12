from sqlalchemy import (
    Column, Integer, String, Float, Text,
    ForeignKey, DateTime, Enum
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import enum


class PositionEnum(str, enum.Enum):
    Goalkeeper = "Goalkeeper"
    Defender   = "Defender"
    Midfielder = "Midfielder"
    Winger     = "Winger"
    Forward    = "Forward"


class MatchStatusEnum(str, enum.Enum):
    upcoming = "upcoming"
    live     = "live"
    results   = "results"


# PLAYERS

class Player(Base):
    __tablename__ = "players"

    id             = Column(Integer, primary_key=True, index=True)
    name           = Column(String(100), nullable=False)
    position       = Column(Enum(PositionEnum), nullable=False)
    age            = Column(Integer, nullable=False)
    nationality    = Column(String(60), nullable=False)
    number         = Column(Integer, nullable=False)
    image_initials = Column(String(4), nullable=False)
    goals          = Column(Integer, default=0)
    assists        = Column(Integer, default=0)
    appearances    = Column(Integer, default=0)
    rating         = Column(Float, default=0.0)
    market_value   = Column(String(20))
    foot           = Column(String(10))
    height         = Column(String(10))
    joined         = Column(String(10))
    contract_until = Column(String(10))
    bio            = Column(Text)

    
    career_highlights    = relationship("CareerHighlight",     back_populates="player", cascade="all, delete-orphan")
    recent_performances  = relationship("RecentPerformance",   back_populates="player", cascade="all, delete-orphan")


class CareerHighlight(Base):
    __tablename__ = "career_highlights"

    id        = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id", ondelete="CASCADE"), nullable=False)
    highlight = Column(String(255), nullable=False)

    player = relationship("Player", back_populates="career_highlights")


class RecentPerformance(Base):
    __tablename__ = "recent_performances"

    id        = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id", ondelete="CASCADE"), nullable=False)
    opponent  = Column(String(100), nullable=False)
    date      = Column(String(30), nullable=False)
    result    = Column(String(10), nullable=False)   
    rating    = Column(Float, nullable=False)
    saves     = Column(Integer, nullable=True)        

    player = relationship("Player", back_populates="recent_performances")


# MATCHES

class Match(Base):
    __tablename__ = "matches"

    id          = Column(Integer, primary_key=True, index=True)
    home        = Column(String(100), nullable=False)
    away        = Column(String(100), nullable=False)
    home_score  = Column(Integer, nullable=True)   
    away_score  = Column(Integer, nullable=True)
    date        = Column(String(30), nullable=False)
    time        = Column(String(10), nullable=True)
    competition = Column(String(100), nullable=False)
    matchday    = Column(String(60))
    venue       = Column(String(150))
    status      = Column(Enum(MatchStatusEnum), nullable=False, default=MatchStatusEnum.upcoming)
    minute      = Column(Integer, nullable=True)   

    scorers = relationship("MatchScorer", back_populates="match", cascade="all, delete-orphan")


class MatchScorer(Base):
    __tablename__ = "match_scorers"

    id       = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id", ondelete="CASCADE"), nullable=False)
    player   = Column(String(100), nullable=False)
    minute   = Column(Integer, nullable=False)
    team     = Column(String(100), nullable=False)

    match = relationship("Match", back_populates="scorers")
