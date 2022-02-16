from db.models import engine, User, Team , Video, Game, Tag
from typing import Optional
from sqlalchemy.orm import sessionmaker
from random import randint
Session = sessionmaker(bind=engine)


def create_user(user_id: int, viewer_count: int, email: Optional[str], display_name: Optional[str] = "",
                login: Optional[str] = "", description: Optional[str] = "", team_id: Optional[int] = None) -> None:
    with Session() as session:
        try:
            user = User(id=user_id, viewer_count=viewer_count, email=email, display_name=display_name,
                        description=description, login=login, team_id=team_id)
            session.add(user)
            session.flush()
            for i in range(randint(1,5)):
                video = Video(video_type=f"{randint(1,100)}", view_count=randint(1,10000), title=f"govno{i}",
                              language=f"{randint(1,100)}", user_id=user_id, game_id=randint(1,5), description="description")
                session.add(video)

            session.commit()
        except Exception as e:
            session.rollback()
            raise e


def create_team(team_id: int, team_name: str, team_display_name: str, description: str = ""):
    with Session() as session:
        try:
            team = Team(id=team_id, team_name=team_name, team_display_name=team_display_name, description=description)
            session.add(team)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e


def create_video(video_type: str, view_count: int, title: str,
                 language: str, user_id: int, game_id: int, description: str = ""):
    with Session() as session:
        try:
            video = Video(video_type=video_type, view_count=view_count, title=title,
                          language=language, user_id=user_id, game_id=game_id, description=description)
            session.add(video)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e


def create_game(game_id: int, name: str, viewer_count: int, follower_count: int, tag_id: int, description: str = ""):
    with Session() as session:
        try:
            game = Game(id=game_id, name=name, viewer_count=viewer_count,
                        follower_count=follower_count, tag_id=tag_id, description=description)
            session.add(game)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e

def create_tag(tag_id: int, tag_name: str, is_auto: bool = "true"):
    with Session() as session:
        try:
            tag = Tag(id=tag_id, tag_name=tag_name, is_auto=is_auto)
            session.add(tag)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e