import os
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy.pool import QueuePool