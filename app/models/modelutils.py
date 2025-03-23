from  datetime import datetime
from sqlmodel import Field, SQLModel
from pydantic import model_validator


def current_utc_time() -> datetime:
    return datetime.now()


class TimestampMixin(SQLModel):
    created_at: datetime = Field(default_factory=current_utc_time)
    updated_at: datetime = Field(default_factory=current_utc_time)

    @model_validator(mode='after')
    def set_updated_at(self):
        self.updated_at = datetime.now()
        return self