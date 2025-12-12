from dataclasses import dataclass

@dataclass
class TodoDataClass:
    id: int = None
    title: str = None
    description: str = None
    created_at: str = None

@dataclass
class TodoCreateDataClass:
    title: str
    description: str

@dataclass
class TodoUpdateDataClass:
    title: str
    description: str
