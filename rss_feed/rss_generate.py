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
host='https://e86d-75-172-71-56.eu.ngrok.io'
proj_root = Path(__file__).parent.parent
for podcast in  session_orm.query(Podcast).all():
# for podcast in  [session_orm.query(Podcast).first()]:
    slug_name=slugify(podcast.name)
    root_dir = f'podcast-data/{slug_name}'
    podcast.root_url = f"{host}/{root_dir}/"
    podcast.feed_url = f"{podcast.root_url}rss.xml"
    rss_string = env.get_template('rss_feed.xml').render(pod=podcast, root_dir=root_dir)
    with open(proj_root/root_dir/'rss.xml', "w+") as file:
        file.write(rss_string)