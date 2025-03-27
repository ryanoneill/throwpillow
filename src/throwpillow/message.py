from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def __repr__(self) -> str:
        return f'{{"role": "{self.role}", "content": "{self.content}"}}'

class UserMessage(Message):
    def __init__(self, content: str):
        super().__init__("user", content)

class ClaudeMessage(Message):
    def __init__(self, content: str):
        super().__init__("assistant", content)
