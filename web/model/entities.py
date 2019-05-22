from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

# Table Student
class Student(connector.Manager.Base):
	__tablename__ = 'students'
	id = Column(Integer, Sequence('student_id'), primary_key = True)
	name = Column(String(50))
	lname = Column(String(50))
	uname = Column(String(50))
	password = Column(String(50))