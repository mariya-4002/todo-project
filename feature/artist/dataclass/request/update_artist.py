from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateArtistRequest:
    id: int
    name: Optional[str] = None
    bio: Optional[str] = None
    genre: Optional[str] = None
