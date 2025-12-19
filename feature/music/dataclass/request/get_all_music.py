from dataclasses import dataclass

@dataclass
class GetAllMusicRequest:
    page: int = 1
    limit: int = 10
