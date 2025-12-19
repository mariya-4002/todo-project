from dataclasses import dataclass

@dataclass
class GetAllTodoRequest:
    page: int = 1
    limit: int = 10
