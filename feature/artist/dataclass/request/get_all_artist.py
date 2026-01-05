from dataclasses import dataclass

@dataclass
class GetAllArtistRequest:
    page: int = 1
    limit: int = 10
