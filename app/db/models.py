from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime, ForeignKey, Boolean, Date, func
from sqlalchemy.orm import declarative_base
from datetime import datetime
import pytz # Run 'pip install pytz' in your terminal

Base = declarative_base()

# 1. Helper function for Iraq Time
def get_local_time():
    return datetime.now(pytz.timezone('Asia/Baghdad'))

# 2. Building Table
class Building(Base):
    __tablename__ = 'building'
    building_id = Column(Integer, primary_key=True, autoincrement=True)
    building_name = Column(String, nullable=False)
    phone_number = Column(String)
    status = Column(Boolean, default=True)
    # Using 'default' instead of 'server_default' ensures Python sends the right time
    created_at = Column(DateTime(timezone=True), default=get_local_time)

# 3. Employee Table
class Employee(Base):
    __tablename__ = 'employee'
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String)

# 4. ML Model Table
class MLModel(Base):
    __tablename__ = 'ML_model'
    model_id = Column(Integer, primary_key=True, autoincrement=True)
    version = Column(String)
    file_path = Column(String)
    trained_at = Column(DateTime(timezone=True), default=get_local_time)
    status = Column(String)
    employee_id = Column(Integer, ForeignKey('employee.employee_id'))

# 5. Camera Table
class Camera(Base):
    __tablename__ = 'camera'
    camera_id = Column(Integer, primary_key=True, autoincrement=True)
    camera_serial = Column(String, unique=True, nullable=False)
    location_name = Column(String)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    status = Column(String, default="Active")
    installed_at = Column(DateTime(timezone=True), default=get_local_time)
    building_id = Column(Integer, ForeignKey('building.building_id'))
    model_id = Column(Integer, ForeignKey('ML_model.model_id'))

# 6. Model Deployment Table
class ModelDeployment(Base):
    __tablename__ = 'model_deployment'
    deployment_id = Column(Integer, primary_key=True, autoincrement=True)
    model_id = Column(Integer, ForeignKey('ML_model.model_id'))
    camera_id = Column(Integer, ForeignKey('camera.camera_id'))
    deployment_status = Column(String)
    error_message = Column(Text)
    deployed_at = Column(DateTime(timezone=True), default=get_local_time)
    employee_id = Column(Integer, ForeignKey('employee.employee_id'))

# 7. Fire Event Table
class FireEvent(Base):
    __tablename__ = 'fire_event'
    fire_event_id = Column(Integer, primary_key=True, autoincrement=True)
    confidence = Column(Numeric)
    detected_at = Column(DateTime(timezone=True), default=get_local_time)
    message = Column(Text)
    image_url = Column(Text)
    camera_id = Column(Integer, ForeignKey('camera.camera_id'))

# 8. Camera Action Table
class CameraAction(Base):
    __tablename__ = 'camera_action'
    action_id = Column(Integer, primary_key=True, autoincrement=True)
    camera_id = Column(Integer, ForeignKey('camera.camera_id'))
    employee_id = Column(Integer, ForeignKey('employee.employee_id'))
    action_type = Column(String)
    old_value = Column(Text)
    new_value = Column(Text)
    action_time = Column(DateTime(timezone=True), default=get_local_time)
    action_date = Column(Date, default=lambda: get_local_time().date())