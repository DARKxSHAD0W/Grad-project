from sqlalchemy import Column, Integer, String, Numeric, Text, TIMESTAMP, ForeignKey, Boolean, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Building(Base):
    __tablename__ = 'building'
    building_id = Column(Integer, primary_key=True)
    building_name = Column(String)
    phone_number = Column(String)
    status = Column(Boolean)
    created_at = Column(TIMESTAMP)

class Employee(Base):
    __tablename__ = 'employee'
    employee_id = Column(Integer, primary_key=True)
    full_name = Column(String)
    username = Column(String)
    password = Column(String)
    role = Column(String)

class MLModel(Base):
    __tablename__ = 'ML_model'
    model_id = Column(Integer, primary_key=True)
    version = Column(String)
    file_path = Column(String)
    employee_id = Column(Integer, ForeignKey('employee.employee_id'))

class Camera(Base):
    __tablename__ = 'camera'
    camera_id = Column(Integer, primary_key=True)
    camera_serial = Column(String)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    building_id = Column(Integer, ForeignKey('building.building_id'))
    model_id = Column(Integer, ForeignKey('ML_model.model_id'))

class ModelDeployment(Base):
    __tablename__ = 'model_deployment'
    deployment_id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('ML_model.model_id'))
    camera_id = Column(Integer, ForeignKey('camera.camera_id'))
    employee_id = Column(Integer, ForeignKey('employee.employee_id'))

class FireEvent(Base):
    __tablename__ = 'fire_event'
    fire_event_id = Column(Integer, primary_key=True)
    confidence = Column(Numeric)
    detected_at = Column(TIMESTAMP)
    camera_id = Column(Integer, ForeignKey('camera.camera_id'))

class CameraAction(Base):
    __tablename__ = 'camera_action'
    action_id = Column(Integer, primary_key=True)
    camera_id = Column(Integer, ForeignKey('camera.camera_id'))
    employee_id = Column(Integer, ForeignKey('employee.employee_id'))
    action_type = Column(String)