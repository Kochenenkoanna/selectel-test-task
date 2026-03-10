from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class VacancyBase(BaseModel):
    title: str = Field(..., min_length=1) 
    timetable_mode_name: str = Field(..., min_length=1)
    tag_name: str = Field(..., min_length=1)
    city_name: Optional[str] = None
    published_at: datetime
    is_remote_available: bool
    is_hot: bool
    external_id: Optional[int] = Field(None, ge=1) 


class VacancyCreate(VacancyBase):
    pass


class VacancyUpdate(VacancyBase):
    pass


class VacancyRead(VacancyBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
