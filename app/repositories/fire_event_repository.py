from sqlalchemy.orm import Session
from app.db.models import FireEvent

class FireEventRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(FireEvent).all()

    def get_by_id(self, event_id: int):
        return self.db.query(FireEvent).filter(FireEvent.fire_event_id == event_id).first()

    def create(self, dto):
        new_event = FireEvent(**dto.dict())
        self.db.add(new_event)
        self.db.commit()
        self.db.refresh(new_event)
        return new_event

    def update(self, event_id: int, dto):
        event = self.get_by_id(event_id)
        if event:
            for key, value in dto.dict().items():
                setattr(event, key, value)
            self.db.commit()
            self.db.refresh(event)
        return event

    def delete(self, event_id: int):
        event = self.get_by_id(event_id)
        if event:
            self.db.delete(event)
            self.db.commit()
            return True
        return False