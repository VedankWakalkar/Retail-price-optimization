import os
from dotenv import load_dotenv
from sqlalchemy import (
    Column, 
    DateTime, 
    Integer, 
    Numeric, 
    Sequence, 
    SmallInteger, 
    String, 
    create_engine
)
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy.pool import QueuePool

load_dotenv()

engine=create_engine(
    os.getenv("DATABASE_URL"),    # storing data
    echo=True,
    pool_size=5,        #to keep a track 
    max_overflow=1,     #if there is more data then it is kept in waiting area
    pool_recycle=3600,  #Every hour it is checked for maintenance
    pool_pre_ping=True, #Checks the condition of the data 
    connect_args={
        "connect_timeout":60,
        "keepalives":1,
        "keepalives_idle":30,
        "keepalives_interval":10,
        "keepalives_count":5,
    }
)

Session= sessionmaker(bind=engine)
connection = engine.connect()
connection.close()

Base =declarative_base()

class RetailPrices(Base):
    __tablename__ = 'retail_prices'
    id = Column(SmallInteger, Sequence("retail_prices_id_seq"), primary_key=True)
    product_id = Column(String)
    product_category_name = Column(String)
    month_year = Column(DateTime)
    qty = Column(SmallInteger)
    total_price = Column(Numeric(precision=23, scale=15))
    freight_price = Column(Numeric(precision=23, scale=15))
    unit_price = Column(Numeric(precision=23, scale=15))
    product_name_length = Column(SmallInteger)
    product_photos_qty = Column(SmallInteger)
    product_description_length = Column(SmallInteger)
    product_weight_g = Column(SmallInteger)
    customers_product_score = Column(Numeric(precision=5, scale=3))
    weekday = Column(SmallInteger)
    weekend = Column(SmallInteger)
    year = Column(SmallInteger)
    month = Column(SmallInteger)
    holiday = Column(SmallInteger)
    volume = Column(Integer)
    fp1 = Column(Numeric(precision=23, scale=15))
    comp_2 = Column(Numeric(precision=23, scale=15))
    comp_1 = Column(Numeric(precision=23, scale=15))
    ps1 = Column(Numeric(precision=5, scale=3))
    ps2 = Column(Numeric(precision=5, scale=3))
    fp2 = Column(Numeric(precision=23, scale=15))
    comp_3 = Column(Numeric(precision=23, scale=15))
    ps3 = Column(Numeric(precision=5, scale=3))
    fp3 = Column(Numeric(precision=23, scale=15))
    lag_price = Column(Numeric(precision=23, scale=15))