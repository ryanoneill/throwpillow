from throwpillow import Message, ClaudeMessage, UserMessage

def test_user_message_creation():
    message = UserMessage("content")
    assert message is not None

def test_claude_message_creation():
    message = ClaudeMessage("content")
    assert message is not None

def test_user_message_is_message():
    message: Message = UserMessage("hello")
    assert message is not None

def test_claude_message_is_message():
    message: Message = ClaudeMessage("hello")
    assert message is not None

def test_user_message_role_is_user():
    message: Message = UserMessage("goodbye")
    assert message.role == "user"

def test_claude_message_role_is_assistant():
    message: Message = ClaudeMessage("goodbye")
    assert message.role == "assistant"

def test_user_message_content_is_accessible():
    message: Message = UserMessage("some content")
    assert message.content == "some content"

def test_claude_message_content_is_accessible():
    message: Message = ClaudeMessage("some content")
    assert message.content == "some content"

def test_user_message_repr_matches_format():
    message: Message = UserMessage("whatever")
    assert repr(message) == '{"role": "user", "content": "whatever"}'

def test_claude_message_repr_matches_format():
    message: Message = ClaudeMessage("whatever")
    assert repr(message) == '{"role": "assistant", "content": "whatever"}'
