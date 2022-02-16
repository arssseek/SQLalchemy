from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table
from sqlalchemy.sql import func
from settings import POSTGRES_URL

Base = declarative_base()
engine = create_engine(POSTGRES_URL, echo=False)

GameTag = Table('game_tag', Base.metadata,
                Column("game_id", String, ForeignKey("game.id"), primary_key=True),
                Column("tag_id", String, ForeignKey("tag.id"), primary_key=True))


class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, onupdate=func.now())
    display_name = Column(String)
    login = Column(String)
    description = Column(String)
    viewer_count = Column(Integer)
    follower_count = Column(Integer)
    email = Column(String)
    user_created_at = Column(DateTime)

    team_id = Column(ForeignKey("team.id"))

    # streams? uselist false?
    team = relationship("Team", back_populates="users")
    videos = relationship("Video", back_populates="user")
    def __repr__(self):
        return f"<{self.id},{self.viewer_count},{self.team_id}>"


class Team(Base):
    __tablename__ = 'team'
    id = Column(String, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, onupdate=func.now())
    team_name = Column(String)
    team_display_name = Column(String)
    description = Column(String)

    users = relationship("User", back_populates="team")

    def __repr__(self):
        return f"<Product({self.id})>"


class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, onupdate=func.now())
    video_type = Column(String)  # past_broadcast, highlight, upload
    title = Column(String)
    description = Column(String)
    video_created_at = Column(DateTime)
    video_published_at = Column(DateTime)
    view_count = Column(Integer)
    language = Column(String)
    duration = Column(DateTime)

    user_id = Column(String, ForeignKey('user.id'))
    game_id = Column(String, ForeignKey('game.id'))

    user = relationship("User", back_populates="videos")
    game = relationship("Game", back_populates='videos')


    def __repr__(self):
        return f"<Video({self.id})>"


class Game(Base):
    __tablename__ = "game"

    id = Column(String, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, onupdate=func.now())
    name = Column(String)
    description = Column(String)
    viewer_count = Column(Integer)
    follower_count = Column(Integer)

    tag_id = Column(ForeignKey("tag.id"))

    tags = relationship("Tag", back_populates="games")
    videos = relationship("Video", back_populates="game")


class Tag(Base):
    __tablename__ = "tag"

    id = Column(String, primary_key=True)
    tag_name = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, onupdate=func.now())
    is_auto = Column(Boolean)  # true if auto-generated


    games = relationship("Game", secondary=GameTag, back_populates="tags")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
