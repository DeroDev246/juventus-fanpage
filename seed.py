"""
Run once to populate the database with the initial Juventus squad and fixture data.
  python seed.py
"""
from database import SessionLocal, engine, Base
from models import (
    Player, CareerHighlight, RecentPerformance,
    Match, MatchScorer, MatchStatusEnum
)

Base.metadata.create_all(bind=engine)

PLAYERS = [
    dict(id=1,  name="Wojciech Szczęsny", position="Goalkeeper", age=33, nationality="Poland",  number=1,  image_initials="WS", goals=0,  assists=0, appearances=28, rating=7.2, market_value="€8M",  foot="Right", height="1.96m", joined="2017", contract_until="2025",
         bio="One of the most reliable goalkeepers in Serie A, Szczęsny joined Juventus in 2017 and has been a cornerstone of their defence ever since.",
         highlights=["3x Serie A Champion with Juventus","UEFA Champions League finalist 2017","Polish national team captain","Won Coppa Italia multiple times"],
         performances=[dict(opponent="AC Milan",date="Mar 2",result="W 1-0",rating=7.8,saves=5),dict(opponent="Lazio",date="Feb 24",result="D 1-1",rating=6.5,saves=3),dict(opponent="Frosinone",date="Feb 18",result="W 3-2",rating=7.0,saves=4)]),
    dict(id=2,  name="Bremer", position="Defender", age=27, nationality="Brazil", number=3, image_initials="BR", goals=3, assists=1, appearances=24, rating=7.5, market_value="€50M", foot="Right", height="1.88m", joined="2022", contract_until="2027",
         bio="The commanding Brazilian centre-back has been a revelation since joining from Torino, making him one of the best defenders in Italy.",
         highlights=["Best Defender in Serie A 2021/22 (Torino)","Juventus Player of the Season 2022/23","Consistent Brazil international","Commanding aerial presence"],
         performances=[dict(opponent="AC Milan",date="Mar 2",result="W 1-0",rating=8.0,saves=None),dict(opponent="Lazio",date="Feb 24",result="D 1-1",rating=7.2,saves=None),dict(opponent="Frosinone",date="Feb 18",result="W 3-2",rating=7.5,saves=None)]),
    dict(id=3,  name="Danilo", position="Defender", age=32, nationality="Brazil", number=6, image_initials="DN", goals=2, assists=4, appearances=26, rating=6.9, market_value="€5M", foot="Right", height="1.84m", joined="2019", contract_until="2024",
         bio="A veteran of the Juventus back line, Danilo brings experience and versatility, capable of playing right-back or centre-back.",
         highlights=["Serie A champion with Juventus","Coppa Italia winner","Champions League winner with Real Madrid","Brazil World Cup squad member"],
         performances=[dict(opponent="AC Milan",date="Mar 2",result="W 1-0",rating=7.0,saves=None),dict(opponent="Lazio",date="Feb 24",result="D 1-1",rating=6.5,saves=None),dict(opponent="Frosinone",date="Feb 18",result="W 3-2",rating=7.2,saves=None)]),
    dict(id=4,  name="Federico Gatti", position="Defender", age=25, nationality="Italy", number=4, image_initials="FG", goals=4, assists=1, appearances=22, rating=7.1, market_value="€18M", foot="Right", height="1.90m", joined="2022", contract_until="2027",
         bio="The remarkable story of Gatti — rising from the lower Italian leagues to Juventus and the national team — makes him a fan favourite.",
         highlights=["Rapid rise from Serie C to Serie A","Italy national team debut 2022","Key contributor in Juventus defence","Strong aerial ability"],
         performances=[dict(opponent="AC Milan",date="Mar 2",result="W 1-0",rating=7.5,saves=None),dict(opponent="Lazio",date="Feb 24",result="D 1-1",rating=7.0,saves=None),dict(opponent="Frosinone",date="Feb 18",result="W 3-2",rating=6.8,saves=None)]),
    dict(id=5,  name="Manuel Locatelli", position="Midfielder", age=26, nationality="Italy", number=5, image_initials="ML", goals=4, assists=7, appearances=30, rating=7.3, market_value="€35M", foot="Right", height="1.87m", joined="2021", contract_until="2026",
         bio="A Euro 2020 winner, Locatelli anchors the Juventus midfield with composure and vision, distributing play efficiently from deep.",
         highlights=["UEFA Euro 2020 winner with Italy","2 goals at Euro 2020","Serie A title with Juventus","Key midfield anchor for Italy"],
         performances=[dict(opponent="AC Milan",date="Mar 2",result="W 1-0",rating=7.8,saves=None),dict(opponent="Lazio",date="Feb 24",result="D 1-1",rating=7.0,saves=None),dict(opponent="Frosinone",date="Feb 18",result="W 3-2",rating=7.5,saves=None)]),
    dict(id=6,  name="Adrien Rabiot", position="Midfielder", age=28, nationality="France", number=25, image_initials="AR", goals=8, assists=5, appearances=29, rating=7.6, market_value="€25M", foot="Left", height="1.88m", joined="2019", contract_until="2024",
         bio="The tall, dynamic French midfielder has been one of Juventus's most consistent performers, combining physicality with technical quality.",
         highlights=["Ligue 1 champion with PSG (5x)","Champions League finalist 2020 (PSG)","Consistent top performer for Juventus","France World Cup squad 2022"],
         performances=[dict(opponent="AC Milan",date="Mar 2",result="W 1-0",rating=8.2,saves=None),dict(opponent="Lazio",date="Feb 24",result="D 1-1",rating=7.5,saves=None),dict(opponent="Frosinone",date="Feb 18",result="W 3-2",rating=7.8,saves=None)]),
    dict(id=7,  name="Federico Chiesa", position="Winger", age=26, nationality="Italy", number=7, image_initials="FC", goals=6, assists=4, appearances=18, rating=7.8, market_value="€60M", foot="Right", height="1.75m", joined="2020", contract_until="2025",
         bio="One of Italy's brightest talents, Chiesa is an electrifying winger capable of taking on any defender in Europe with explosive pace and skill.",
         highlights=["UEFA Euro 2020 winner & key player","Champion of Italy with Juventus","Son of legendary Enrico Chiesa","Outstanding dribbler and goal threat"],
         performances=[dict(opponent="AC Milan",date="Mar 2",result="W 1-0",rating=8.5,saves=None),dict(opponent="Frosinone",date="Feb 18",result="W 3-2",rating=8.0,saves=None),dict(opponent="Inter Milan",date="Feb 4",result="L 0-1",rating=7.0,saves=None)]),
    dict(id=8,  name="Dušan Vlahović", position="Forward", age=24, nationality="Serbia", number=9, image_initials="DV", goals=16, assists=3, appearances=31, rating=7.7, market_value="€80M", foot="Left", height="1.90m", joined="2022", contract_until="2026",
         bio="The powerful Serbian striker is Juventus's main goal threat — a physical, technically gifted forward who dominated Serie A at Fiorentina.",
         highlights=["Top scorer Serie A 2021/22 (Fiorentina)","Record signing for Juventus (€80M)","Serbian national team captain","30+ Serie A goals in a single calendar year"],
         performances=[dict(opponent="AC Milan",date="Mar 2",result="W 1-0",rating=7.5,saves=None),dict(opponent="Lazio",date="Feb 24",result="D 1-1",rating=8.0,saves=None),dict(opponent="Frosinone",date="Feb 18",result="W 3-2",rating=8.5,saves=None)]),
    dict(id=9,  name="Nicolo Fagioli", position="Midfielder", age=22, nationality="Italy", number=34, image_initials="NF", goals=3, assists=6, appearances=20, rating=7.2, market_value="€30M", foot="Right", height="1.75m", joined="2021", contract_until="2027",
         bio="A promising young talent from the Juventus academy, Fagioli brings creative flair and technical ability to the midfield.",
         highlights=["Juventus academy graduate","Italy U21 international","Breakthrough season 2022/23","Creative midfielder of the future"],
         performances=[dict(opponent="AC Milan",date="Mar 2",result="W 1-0",rating=7.0,saves=None),dict(opponent="Lazio",date="Feb 24",result="D 1-1",rating=6.8,saves=None),dict(opponent="Frosinone",date="Feb 18",result="W 3-2",rating=7.5,saves=None)]),
    dict(id=10, name="Moise Kean", position="Forward", age=24, nationality="Italy", number=18, image_initials="MK", goals=9, assists=2, appearances=28, rating=7.0, market_value="€28M", foot="Right", height="1.83m", joined="2023", contract_until="2025",
         bio="The powerful young Italian forward returned to Juventus after stints abroad, offering pace, power and a poacher's instinct.",
         highlights=["Italy international","Ligue 1 winner with PSG","Juventus academy product","Premier League experience with Everton"],
         performances=[dict(opponent="AC Milan",date="Mar 2",result="W 1-0",rating=6.5,saves=None),dict(opponent="Lazio",date="Feb 24",result="D 1-1",rating=7.2,saves=None),dict(opponent="Frosinone",date="Feb 18",result="W 3-2",rating=7.8,saves=None)]),
    dict(id=11, name="Weston McKennie", position="Midfielder", age=25, nationality="USA", number=16, image_initials="WM", goals=5, assists=4, appearances=25, rating=6.8, market_value="€20M", foot="Right", height="1.83m", joined="2020", contract_until="2025",
         bio="The energetic American midfielder brings intensity and work-rate to the Juventus engine room, a cult hero for fans worldwide.",
         highlights=["USA international & key player","Scored against Germany in the Bundesliga","Coppa Italia winner with Juventus","One of USA's biggest football exports"],
         performances=[dict(opponent="AC Milan",date="Mar 2",result="W 1-0",rating=6.8,saves=None),dict(opponent="Lazio",date="Feb 24",result="D 1-1",rating=6.5,saves=None),dict(opponent="Frosinone",date="Feb 18",result="W 3-2",rating=7.0,saves=None)]),
    dict(id=12, name="Alex Sandro", position="Defender", age=33, nationality="Brazil", number=12, image_initials="AS", goals=1, assists=3, appearances=15, rating=6.5, market_value="€4M", foot="Left", height="1.83m", joined="2015", contract_until="2024",
         bio="A long-serving left-back at Juventus, Alex Sandro has been a dependable presence on the left flank for nearly a decade.",
         highlights=["8 seasons at Juventus","Multiple Serie A titles","Champions League finalist","Brazil international"],
         performances=[dict(opponent="Frosinone",date="Feb 18",result="W 3-2",rating=6.5,saves=None),dict(opponent="Verona",date="Feb 10",result="W 2-1",rating=6.8,saves=None),dict(opponent="Napoli",date="Feb 3",result="D 1-1",rating=6.3,saves=None)]),
]

MATCHES = [
    dict(home="Juventus", away="Napoli",     date="Mar 9, 2024",  time="20:45", competition="Serie A",         matchday="Matchday 28",       venue="Allianz Stadium",              status="upcoming", scorers=[]),
    dict(home="Fiorentina",away="Juventus",  date="Mar 17, 2024", time="15:00", competition="Serie A",         matchday="Matchday 29",       venue="Stadio Artemio Franchi",       status="upcoming", scorers=[]),
    dict(home="Juventus", away="Genoa",      date="Mar 30, 2024", time="18:00", competition="Serie A",         matchday="Matchday 30",       venue="Allianz Stadium",              status="upcoming", scorers=[]),
    dict(home="Cagliari", away="Juventus",   date="Apr 7, 2024",  time="20:45", competition="Serie A",         matchday="Matchday 31",       venue="Unipol Domus",                 status="upcoming", scorers=[]),
    dict(home="Juventus", away="Fiorentina", date="Apr 10, 2024", time="21:00", competition="Coppa Italia",    matchday="Semi-Final 2nd Leg",venue="Allianz Stadium",              status="upcoming", scorers=[]),
    dict(home="Juventus", away="AC Milan",   date="Mar 2, 2024",  time=None,    competition="Serie A",         matchday="Matchday 27",       venue="Allianz Stadium",              status="result",   home_score=1, away_score=0, scorers=[dict(player="Vlahović",  minute=23, team="Juventus")]),
    dict(home="Lazio",    away="Juventus",   date="Feb 24, 2024", time=None,    competition="Serie A",         matchday="Matchday 26",       venue="Stadio Olimpico",              status="result",   home_score=1, away_score=1, scorers=[dict(player="Immobile",  minute=35, team="Lazio"), dict(player="Vlahović", minute=67, team="Juventus")]),
    dict(home="Juventus", away="Frosinone",  date="Feb 18, 2024", time=None,    competition="Serie A",         matchday="Matchday 25",       venue="Allianz Stadium",              status="result",   home_score=3, away_score=2, scorers=[dict(player="Chiesa",    minute=12, team="Juventus"), dict(player="Kean", minute=38, team="Juventus"), dict(player="Vlahović", minute=72, team="Juventus")]),
    dict(home="Juventus", away="Inter Milan",date="Feb 4, 2024",  time=None,    competition="Serie A",         matchday="Matchday 23",       venue="Allianz Stadium",              status="result",   home_score=0, away_score=1, scorers=[dict(player="Thuram",    minute=55, team="Inter Milan")]),
    dict(home="Verona",   away="Juventus",   date="Feb 10, 2024", time=None,    competition="Serie A",         matchday="Matchday 24",       venue="Stadio Bentegodi",             status="result",   home_score=1, away_score=2, scorers=[dict(player="Kean",      minute=29, team="Juventus"), dict(player="Fagioli", minute=80, team="Juventus")]),
]


def seed():
    db = SessionLocal()
    try:
        if db.query(Player).count() > 0:
            print("Database already seeded. Skipping.")
            return

        print("Seeding players...")
        for p in PLAYERS:
            player = Player(
                id=p["id"], name=p["name"], position=p["position"],
                age=p["age"], nationality=p["nationality"], number=p["number"],
                image_initials=p["image_initials"], goals=p["goals"],
                assists=p["assists"], appearances=p["appearances"],
                rating=p["rating"], market_value=p["market_value"],
                foot=p["foot"], height=p["height"], joined=p["joined"],
                contract_until=p["contract_until"], bio=p["bio"],
            )
            db.add(player)
            db.flush()
            for h in p["highlights"]:
                db.add(CareerHighlight(player_id=player.id, highlight=h))
            for perf in p["performances"]:
                db.add(RecentPerformance(player_id=player.id, **perf))

        print("Seeding matches...")
        for m in MATCHES:
            scorers = m.pop("scorers", [])
            match = Match(
                home=m["home"], away=m["away"], date=m["date"],
                time=m.get("time"), competition=m["competition"],
                matchday=m.get("matchday"), venue=m.get("venue"),
                status=m["status"],
                home_score=m.get("home_score"), away_score=m.get("away_score"),
            )
            db.add(match)
            db.flush()
            for s in scorers:
                db.add(MatchScorer(match_id=match.id, **s))

        db.commit()
        print("Seed complete.")
    except Exception as e:
        db.rollback()
        print(f"Seed failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
