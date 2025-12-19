from dataclasses import dataclass

@dataclass
class UpdateMusicRequest:
    id: int
    title: str
    artist: str
