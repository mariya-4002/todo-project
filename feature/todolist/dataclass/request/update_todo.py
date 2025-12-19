from dataclasses import dataclass

@dataclass
class UpdateTodoRequest:
    id: int
    title: str
    description: str
