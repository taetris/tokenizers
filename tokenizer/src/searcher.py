from collections import defaultdict 

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

def create_index(blocks):
    field_dict = defaultdict(set)
    for blkidx, sents in enumerate(blocks):
        sent_list = sents.split(".")
        for lineidx, sent in enumerate( sent_list):
            word_list = sent.split(" ")
            [field_dict[word].add(f"{lineidx}") for word in word_list]

    return field_dict

index = {}
# Create an index for each field
def indexer(dict_list):
    
    for field in ['subject', 'content', 'footnote']:
        blocks = [dict_[field] for dict_ in dict_list]
        index[field] = create_index(blocks)
        
    return index

# Search for a term in a specific field
def search(term, field):
    return index[field][term]

# index = indexer(data)
# print(index)
# print(search('Some', 'footnote'))


