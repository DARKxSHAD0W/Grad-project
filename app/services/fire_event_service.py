from fastapi import HTTPException, status
from app.repositories.fire_event_repository import FireEventRepository

class FireEventService:
    def __init__(self, db):
        self.repository = FireEventRepository(db)

    def get_all_events(self):
        return self.repository.get_all()

    def log_detection(self, dto):
        # Using 'confidence' to match your DTO/Model
        if dto.confidence < 20:
            return {"status": "ignored", "message": "Confidence level too low."}
        return self.repository.create(dto)

    def get_event_by_id(self, event_id: int):
        event = self.repository.get_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Fire event not found")
        return event

    def update_event(self, event_id: int, dto):
        event = self.repository.update(event_id, dto)
        if not event:
            raise HTTPException(status_code=404, detail="Fire event not found")
        return event

    def delete_event(self, event_id: int):
        if not self.repository.delete(event_id):
            raise HTTPException(status_code=404, detail="Fire event not found")
        return {"detail": "Fire event deleted successfully"}