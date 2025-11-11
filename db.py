import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from models import Base, MetalPriceGold, MetalPriceSilverAndPlatinum

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.user = os.getenv("user")
        self.password = quote_plus(os.getenv("password"))
        self.host = os.getenv("host")
        self.database = os.getenv("database")
        self.db_url = f"mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database}"
        self.engine = sa.create_engine(
            self.db_url,
            echo= False
        )
        self.session = sessionmaker(bind= self.engine)

        Base.metadata.create_all(self.engine)

    def get_all_gold_records(self):
        with self.session() as session:
            gold_records = session.query(MetalPriceGold).all()
            if not gold_records:
                return None
            return gold_records
        
    def get_all_silver_and_platinum_records(self):
        with self.session() as session:
            records = session.query(MetalPriceSilverAndPlatinum).all()
            if not records:
                return None
            return records
     