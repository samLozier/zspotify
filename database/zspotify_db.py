from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import BigInteger
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from pathlib import Path

Base = declarative_base()

engine = create_engine(f"sqlite:///{Path(__file__).parents[0]}/zspotify_db.db")


class Podcast(Base):
    __tablename__ = "podcast"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    slug_name = Column(String, nullable=False)
    description = Column(String)
    explicit = Column(Boolean)
    href = Column(String, nullable=False)
    html_description = Column(String)
    is_externally_hosted = Column(Boolean)
    # languages = Column(String, nullable=True)
    # available_markets = Column(String, nullable=True)
    # copyrights = Column(String, nullable=True)
    media_type = Column(String)
    publisher = Column(String)
    total_episodes = Column(Integer)
    type = Column(String)
    uri = Column(String)
    episodes = relationship("Episode", backref="podcast")


class Episode(Base):
    __tablename__ = "episode"

    id = Column(String, primary_key=True)
    podcast_id = Column(Integer, ForeignKey("podcast.id"), nullable=True)
    # podcast = relationship("Podcast", back_populates='episode')
    audio_preview_url = Column(String)
    content_type = Column(String)
    description = Column(String)
    duration_ms = Column(BigInteger)
    explicit = Column(String)
    external_urls = Column(String)
    href = Column(String)
    html_description = Column(String)

    # images <class 'list'>
    is_externally_hosted = Column(Boolean)
    is_paywall_content = Column(Boolean)
    is_playable = Column(Boolean)
    language = Column(String)
    # languages <class 'list'>
    name = Column(String)
    slug_name = Column(String, nullable=False)
    release_date = Column(String)
    release_date_precision = Column(String)
    type = Column(String)
    uri = Column(String)
    is_downloaded = Column(Boolean)
    file_path = Column(String)
    file_size = Column(Integer)


# if __name__ == "__main__":
# #     # meta = MetaData()
# #     # meta.create_all(engine)
# #     # Podcast.__table__.drop(engine)
#     Podcast.__table__.create(engine)
# #     # Podcast.__table__.update(engine)
# #     # Episode.__table__.drop(engine)
#     Episode.__table__.create(engine)
# #     # Episode.__table__.update(engine)
