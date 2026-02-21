from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime, ForeignKey, Boolean, Date, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Building(Base):
    __tablename__ = 'building'
    building_id = Column(Integer, primary_key=True, autoincrement=True)
    building_name = Column(String, nullable=False)
    phone_number = Column(String)
    status = Column(Boolean, default=True)
    # Using UTC as per teacher's recommendation
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Employee(Base):
    __tablename__ = 'employee'
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    # This will now store the encrypted string
    password = Column(String, nullable=False)
    role = Column(String)

class MLModel(Base):
    __tablename__ = 'ML_model'
    model_id = Column(Integer, primary_key=True, autoincrement=True)
    version = Column(String)
    file_path = Column(String)
    trained_at = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String)
    employee_id = Column(Integer, ForeignKey('employee.employee_id'))

class Camera(Base):
    __tablename__ = 'camera'
    camera_id = Column(Integer, primary_key=True, autoincrement=True)
    camera_serial = Column(String, unique=True, nullable=False)
    location_name = Column(String)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    status = Column(String, default="Active")
    installed_at = Column(DateTime(timezone=True), server_default=func.now())
    building_id = Column(Integer, ForeignKey('building.building_id'))
    model_id = Column(Integer, ForeignKey('ML_model.model_id'))

class ModelDeployment(Base):
    __tablename__ = 'model_deployment'
    deployment_id = Column(Integer, primary_key=True, autoincrement=True)
    model_id = Column(Integer, ForeignKey('ML_model.model_id'))
    camera_id = Column(Integer, ForeignKey('camera.camera_id'))
    deployment_status = Column(String)
    error_message = Column(Text)
    deployed_at = Column(DateTime(timezone=True), server_default=func.now())
    employee_id = Column(Integer, ForeignKey('employee.employee_id'))

class FireEvent(Base):
    __tablename__ = 'fire_event'
    fire_event_id = Column(Integer, primary_key=True, autoincrement=True)
    confidence = Column(Numeric)
    detected_at = Column(DateTime(timezone=True), server_default=func.now())
    message = Column(Text)
    image_url = Column(Text)
    camera_id = Column(Integer, ForeignKey('camera.camera_id'))

class CameraAction(Base):
    __tablename__ = 'camera_action'
    action_id = Column(Integer, primary_key=True, autoincrement=True)
    camera_id = Column(Integer, ForeignKey('camera.camera_id'))
    employee_id = Column(Integer, ForeignKey('employee.employee_id'))
    action_type = Column(String)
    old_value = Column(Text)
    new_value = Column(Text)
    action_time = Column(DateTime(timezone=True), server_default=func.now())
    action_date = Column(Date, server_default=func.current_date())