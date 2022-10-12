from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
from database.zspotify_db import engine, Podcast, Episode
from sqlalchemy.orm import sessionmaker
from pprint import pprint
from slugify import slugify

session = sessionmaker(bind = engine)
session_orm = session()

env = Environment(
    loader=FileSystemLoader(Path(__file__).parent/'templates/'),
autoescape=select_autoescape()
)
podcast = session_orm.query(Podcast).first()
host='https://7f07-75-172-71-56.eu.ngrok.io'
slug_name=slugify(podcast.name)
root_dir = f'podcast_data/{slug_name}'
podcast.root_url = f"{host}/{root_dir}/"
podcast.feed_url = f"{podcast.root_url}rss.xml"
test_out = env.get_template('rss_feed.xml').render(pod=podcast, root_dir=root_dir)
pprint(test_out)