import pytest
from throwpillow.history import History, HistoryException
from throwpillow.message import ClaudeMessage, UserMessage, Message
from typing import List

# Empty History Tests

def test_history_creation():
    history = History()
    assert history is not None

def test_history_is_empty():
    history = History()
    assert history.messages == []

def test_history_has_0_len():
    history = History()
    assert len(history) == 0

def test_history_iter_does_nothing():
    history = History()
    result = True
    for _ in history:
        result = False
    assert result

def test_history_get_item_fails():
    history = History()
    with pytest.raises(IndexError):
        history[0]

def test_history_append_works_for_user():
    message = UserMessage("This should work")
    history = History()
    history.append(message)
    assert True

def test_history_append_fails_for_claude():
    message = ClaudeMessage("This should not work")
    history = History()
    with pytest.raises(HistoryException):
        history.append(message)

# Initial User Message
def test_history_creation_one_message_good():
    message = UserMessage("This should work")
    items: List[Message] = [message]
    history = History(items)
    assert len(history) == 1
    
def test_history_creation_one_message_bad():
    message = ClaudeMessage("This should not work")
    items: List[Message] = [message]
    with pytest.raises(HistoryException):
        History(items)

def test_history_creation_two_messages_good():
    message1 = UserMessage("This should work")
    message2 = ClaudeMessage("So should this")
    items: List[Message] = [message1, message2]
    history = History(items)
    assert len(history) == 2

def test_history_creation_two_messages_bad():
    message1 = UserMessage("This should work")
    message2 = UserMessage("This should not")
    items: List[Message] = [message1, message2]
    with pytest.raises(HistoryException):
        History(items)

# Conversion

def test_history_empty_as_strings():
    history = History()
    result = history.as_strings()
    assert result == []

def test_history_multiple_as_strings():
    message1 = UserMessage("Something here")
    message2 = ClaudeMessage("Another thing")
    messages = [message1, message2]
    history = History(messages)
    result = history.as_strings()
    assert len(result) == 2
    assert result[0] == repr(message1)
    assert result[1] == repr(message2)

