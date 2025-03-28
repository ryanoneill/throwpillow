from typing import List
from .message import Message, ClaudeMessage, UserMessage

class HistoryException(Exception):
    def __init__(self, message: str):
        self.message = message

class History:
    def __init__(self, items: List[Message] = []):
        self.messages: List[Message] = []

        for item in items:
            self.append(item)

    def append(self, message: Message) -> None:
        n = len(self.messages)
        is_user = n % 2 == 0

        if is_user:
            if isinstance(message, UserMessage):
                self.messages.append(message)
            else:
                value = "It is the user's turn, and this is not a `UserMessage`"
                raise HistoryException(value)
        else:
            if isinstance(message, ClaudeMessage):
                self.messages.append(message)
            else:
                value = "It is Claude's turn, and this is not a `ClaudeMessage`"
                raise HistoryException(value)

    def __iter__(self):
        return iter(self.messages)

    def __len__(self) -> int:
        return len(self.messages)

    def __getitem__(self, index: int) -> Message:
        return self.messages[index]

    def as_strings(self) -> List[str]:
        return list(map(repr, self.messages))
