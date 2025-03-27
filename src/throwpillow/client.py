from anthropic import Anthropic

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
