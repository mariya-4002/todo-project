from dataclasses import dataclass

@dataclass
class CreateArtistRequest:
    name: str
    bio: str
    genre: str
