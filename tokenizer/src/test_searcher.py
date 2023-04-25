# Tests for searcher.search.py
from . import searcher

data = [
    {
        'subject': 'Frankenstein', 
        'content': 'This is my name.',
        'footnote': 'Some text'
    },
    {
        'subject': 'Benjamin Button',
        'content': 'That is your name.',
        'footnote': 'Some more text. and Some more text here'
    }
]

def test_indexer():
    index = searcher.indexer(data)
    assert set(index.keys()) == {'subject', 'content', 'footnote'}
    

def test_search():
    index = searcher.indexer(data)
    
    assert 'Benjamin' in index['subject']
    assert 'name' in index['content']
    assert 'more' in index['footnote']
    
