from dataclasses import dataclass
from dotenv import load_dotenv
import os
from services.filesystem import get_parent_dir

env_file = os.path.join(get_parent_dir(__file__), '.env')

@dataclass
class AppSettings:

    dbname: str = None
    dbuser: str = None
    dbport: int = 5432
    dbhost: str = "localhost"
    dbpassword: str = None
    dburl: str = None
    project_name: str = None

    def __init__(self):

        if os.getenv("IS.CONTAINER") is not None:
            self.dbhost = os.getenv("DB.CONTAINER.HOST")

        self.dbname = os.getenv("DB.NAME")
        self.dbport = int(os.getenv("DB.PORT"))
        self.dbuser = os.getenv("DB.USER")
        self.dbpassword = os.getenv("DB.PASSWORD")
        self.dburl = f'postgresql+psycopg2://{self.dbuser}:{self.dbpassword}@{self.dbhost}:{self.dbport}/{self.dbname}'
        self.project_name = os.getenv("PROJECT.NAME")