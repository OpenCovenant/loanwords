import collections
import json

def detect_duplicate_keys(list_of_pairs):
    key_count = collections.Counter(k for k,v in list_of_pairs)
    duplicate_keys = ', '.join(k for k,v in key_count.items() if v > 1)

    if len(duplicate_keys) != 0:
        raise ValueError('Duplicate key(s) found: {}'.format(duplicate_keys))

    return dict(list_of_pairs)

with open('skdr.json', 'r', encoding='utf-8') as r_file:
  a = json.load(r_file, object_pairs_hook=detect_duplicate_keys)
