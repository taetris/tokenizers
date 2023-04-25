from collections import defaultdict 

data = [
    {
        'subject': 'Frankenstein', 
        'content': 'This is my name.',
        'footnote': 'Some text. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tempus magna id eleifend bibendum. Curabitur at orci dui. Aenean dapibus enim sit amet enim posuere, blandit egestas mi rutrum. Phasellus suscipit consequat sodales. Vivamus vulputate porta est quis consequat. Sed aliquet sodales nibh, nec mattis eros fermentum at. Quisque et mauris nec purus iaculis porta. Maecenas euismod enim sed lobortis gravida.'
    },
    {
        'subject': 'Benjamin Button',
        'content': 'That is your name.',
        'footnote': 'Some more text. and Some more text hereInteger et dignissim velit. Sed quis viverra nunc. Curabitur id pellentesque lectus metus, non commodo nisi imperdiet at. Nulla sed justo ex. Maecenas pulvinar libero eu purus rutrum, vitae varius lorem pharetra. Nunc at semper justo. Aliquam erat volutpat. Proin suscipit turpis eget velit ultrices tempor. Maecenas blandit risus id justo auctor interdum.'
    }
]

def create_index(blocks):
    field_dict = defaultdict(set)
    for blkidx, sents in enumerate(blocks):
        sent_list = sents.split(".")
        for lineidx, sent in enumerate( sent_list):
            word_list = sent.split(" ")
            [field_dict[word].add(f"{blkidx}.{lineidx}") for word in word_list]

    return field_dict

index = {}
# Create an index for each field
def indexer(dict_list):
    
    for field in ['subject', 'content', 'footnote']:
        blocks = [dict_[field] for dict_ in dict_list]
        index[field] = create_index(blocks)
        
    return index

# Search for a term in a specific field
def search(term):
    # found_list = {}
    for field in ['subject', 'content', 'footnote']:
        
        if index[field][term]:
            print(f"FOund at {index[field][term]}")
            [print(data[int(num.split('.')[0])]['content']) for i, num in enumerate(index[field][term])]
            # found_list[field] = (index[field][term])
    # return found_list
    return index[field][term]

index = indexer(data)
# print(index)
search('Benjamin')

# print('Benjami' in index['subject'])
