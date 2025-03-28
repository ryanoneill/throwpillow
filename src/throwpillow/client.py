from typing import TypedDict, cast
from anthropic import Anthropic
from anthropic.types import MessageParam
from .history import History
from .message import Message

class Client:
    def __init__(self):
        # TODO: Be able to change the model fully
        # TODO: Be able to change the max tokens fully
        # TODO: Be able to handle when the API Key has not been loaded.
        self.inner = Anthropic()
        self.model = "claude-3-haiku-20240307"
        self.max_tokens = 1000

    def send(self, content: str) -> str:
        # TODO: Be able to change the model per request
        # TODO: Be able to change the max tokens per request
        # TODO: Be able to make an asynchronous request
        response = self.inner.messages.create(
            model = self.model,
            max_tokens = self.max_tokens,
            messages = [
                {"role": "user", "content": content}
            ]
        )
        # TODO: Deal with errors
        # TODO: Deal with different types of ContentBlocks.
        return response.content[0].text

    # Experimental
    def converse(self, history: History) -> str:
        def convert(message: Message) -> MessageParam:
            result: MessageParam = cast(MessageParam, message.as_dict())
            return result
        messages = list(map(convert, history))
        response = self.inner.messages.create(
            model = self.model,
            max_tokens = self.max_tokens,
            messages = messages
        )

        return response.content[0].text

