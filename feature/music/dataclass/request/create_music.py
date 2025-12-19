from dataclasses import dataclass

@dataclass
class CreateMusicRequest:
    title: str
    artist: str
