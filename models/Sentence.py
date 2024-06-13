from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Sentence(Base):
    __tablename__ = 'sentences'
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True, index=True, nullable=False)
    pdf_url = Column(String, unique=True, index=True)
    sentence_title = Column(String)
    full_text = Column(Text)
    summary_text = Column(Text)
    date_created = Column(DateTime, default=datetime.utcnow)
