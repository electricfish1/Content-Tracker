from typing import TypedDict, Literal
from typing_extensions import NotRequired, Required

class Model(TypedDict, total=False):
    id: Required[int]
    name: str
    total_scenes: int
    downloaded_scenes: int
    first_scrape: str
    last_scrape: str
    url: str

class Scene(TypedDict, total=False):
    id: Required[int]
    title: str
    category: str
    date: str
    quality: str
    duration: int
    size: float
    downloaded: bool
    model_id: int
    tags: list[str]