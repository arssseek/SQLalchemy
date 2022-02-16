from sqlalchemy.orm import sessionmaker,Session ,join
from db.crud import create_team, create_user,create_tag,create_game
from random import randint, choice
from db.models import engine, User , Team , Game ,Tag, Video
from sqlalchemy import delete
from tqdm import tqdm
import time
#for m in tqdm(range(100)):
#    for i  in range(20):
#        create_team(team_id=i, team_name=f"team-{i}", team_display_name=f"dis_name_{i}",
#              description="blalba")
#    for i in range(11):
#        create_tag(tag_id=i, tag_name=f"team-{i}", is_auto=True)
#   for i in range(6):
#        create_game(game_id=i, name=f"team-{i}", viewer_count=randint(1,10000),follower_count=randint(1,10000), tag_id=randint(1,10),description="blalba")
#    for i in range(1000000):
#        create_user(user_id=i, viewer_count=randint(1000, 2000), display_name=f"dis_name_{i}", login=f"login{i}",
#                    description="lolkek", email="pohui", team_id=randint(1,19))
x = time.time()
Session = sessionmaker(bind=engine)
session = Session()
m = session.query(User).filter(User.team_id == '5').count()
print(m)
m = session.query(User).filter(User.team_id == '5').all()
print(m)
m = session.query(User).get(f"{randint(1,1000000)}")
print(m)
m = session.query(User).join(Team, User.team_id == Team.id).all()
print(m)
print(time.time() - x)



