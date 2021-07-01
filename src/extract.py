# -*- coding: utf-8 -*-

import re
import sys
import json
from nltk.tokenize import sent_tokenize

sentences = []

with open(sys.argv[1], 'r') as f:
    for line in f:
        record = json.loads(line)
        title = re.sub('\s+', ' ', record['title'].strip())
        abstract = re.sub('\s+', ' ', record['abstract'].strip())
        sentences.extend(sent_tokenize(title))
        sentences.extend(sent_tokenize(abstract))

with open(sys.argv[2], 'w') as o:
    o.write('\n'.join(sentences))
