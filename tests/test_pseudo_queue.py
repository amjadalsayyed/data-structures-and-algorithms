import pytest
from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue

def test_PS_1 (AA):
    assert AA.dequeue() == 'A'

def test__PS_2():
    PQ = PseudoQueue()
    assert PQ.dequeue() == "Pseude Queue is Empty!"

def test_PS_3(AA):
    
    assert str(AA.inbox) == "C --> B --> A -->  None"

def test_PS_4(AA):
    AA.dequeue()
    assert str(AA.outbox) ==  "B --> C -->  None"   

@pytest.fixture
def AA():
    AA = PseudoQueue()
    AA.enqueue('A')
    AA.enqueue('B')
    AA.enqueue('C')
    return AA