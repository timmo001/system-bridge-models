# generated by datamodel-codegen:
#   filename:  sensors.json

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class Sensors(BaseModel):
    """
    Sensors
    """

    class Config:
        extra = Extra.allow

    id: str | None = Field(None, description="Event ID")
    last_updated: dict[str, float] | None = Field(None, description="Last updated")
