from sqlalchemy import (
    Column, Integer, String, Text, Boolean,
    Date, DateTime, DECIMAL, ForeignKey
)
from sqlalchemy.orm import relationship
from database import Base

class Employee(Base):
    __tablename__ = "employee"

    employee_id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

    models = relationship("MLModel", back_populates="employee")
    deployments = relationship("ModelDeployment", back_populates="employee")
    camera_actions = relationship("CameraAction", back_populates="employee")


class Building(Base):
    __tablename__ = "building"

    building_id = Column(Integer, primary_key=True)
    building_name = Column(String, nullable=False)
    phone_number = Column(String)
    status = Column(Boolean)
    created_at = Column(DateTime)

    cameras = relationship("Camera", back_populates="building")

class MLModel(Base):
    __tablename__ = "ml_model"

    model_id = Column(Integer, primary_key=True)
    version = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    trained_at = Column(DateTime)
    status = Column(String)

    employee_id = Column(Integer, ForeignKey("employee.employee_id"))

    employee = relationship("Employee", back_populates="models")
    deployments = relationship("ModelDeployment", back_populates="model")
    cameras = relationship("Camera", back_populates="model")

class Camera(Base):
    __tablename__ = "camera"

    camera_id = Column(Integer, primary_key=True)
    camera_serial = Column(String, nullable=False)
    location_name = Column(String)
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)
    status = Column(String)
    installed_at = Column(DateTime)

    building_id = Column(Integer, ForeignKey("building.building_id"))
    model_id = Column(Integer, ForeignKey("ml_model.model_id"))

    building = relationship("Building", back_populates="cameras")
    model = relationship("MLModel", back_populates="cameras")
    fire_events = relationship("FireEvent", back_populates="camera")
    deployments = relationship("ModelDeployment", back_populates="camera")
    camera_actions = relationship("CameraAction", back_populates="camera")


class FireEvent(Base):
    __tablename__ = "fire_event"

    fire_event_id = Column(Integer, primary_key=True)
    confidence = Column(DECIMAL)
    detected_at = Column(DateTime)
    message = Column(Text)
    image_url = Column(Text)

    camera_id = Column(Integer, ForeignKey("camera.camera_id"))

    camera = relationship("Camera", back_populates="fire_events")

class CameraAction(Base):
    __tablename__ = "camera_action"

    action_id = Column(Integer, primary_key=True)

    camera_id = Column(Integer, ForeignKey("camera.camera_id"))
    employee_id = Column(Integer, ForeignKey("employee.employee_id"))

    action_type = Column(String)
    old_value = Column(Text)
    new_value = Column(Text)
    action_time = Column(DateTime)
    action_date = Column(Date)

    camera = relationship("Camera", back_populates="camera_actions")
    employee = relationship("Employee", back_populates="camera_actions")

class ModelDeployment(Base):
    __tablename__ = "model_deployment"

    deployment_id = Column(Integer, primary_key=True)

    model_id = Column(Integer, ForeignKey("ml_model.model_id"))
    camera_id = Column(Integer, ForeignKey("camera.camera_id"))
    employee_id = Column(Integer, ForeignKey("employee.employee_id"))

    deployment_status = Column(String)
    error_message = Column(Text)
    deployed_at = Column(DateTime)

    model = relationship("MLModel", back_populates="deployments")
    camera = relationship("Camera", back_populates="deployments")
    employee = relationship("Employee", back_populates="deployments")
