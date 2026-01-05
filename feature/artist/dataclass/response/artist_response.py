from dataclasses import dataclass
from typing import List

@dataclass
class ArtistResponse:
    id: int
    name: str
    bio: str
    genre: str


@dataclass
class ArtistListResponse:
    page: int
    limit: int
    total: int
    results: List[ArtistResponse]
