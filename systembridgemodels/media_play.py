# generated by datamodel-codegen:
#   filename:  media_play.json

from __future__ import annotations

from pydantic import BaseModel


class MediaPlay(BaseModel):
    """
    Media Play
    """

    album: str | None = None
    artist: str | None = None
    autoplay: bool | None = False
    cover: str | None = None
    title: str | None = None
    url: str
    volume: float | None = 40
