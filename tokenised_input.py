import io
import sys
import json, os, re
import token
import numpy as np
import editdistance
from collections import defaultdict, OrderedDict, Counter
from copy import deepcopy

sys.path.insert(0, 'utils')
from code_tokenizer import tokenize
from fairseq_utils import *

vocab_file = '/content/drive/MyDrive/syscan_final/token_vocab.txt'
vocab = set([line.split()[0] for line in open(vocab_file)])

def tokenize_python_code(code_string):
    try:
        tokens = tokenize(io.BytesIO(code_string.encode('utf8')).readline)
        toks = [t for t in tokens]
    except Exception as e:
        print (e)
        return 1
    SPECIAL = {'STRING', 'COMMENT', 'INDENT', 'DEDENT', 'NEWLINE', 'NL'}
    IGNORE = {'ENCODING', 'ENDMARKER'}
    toks_raw = []
    anonymize_dict = defaultdict(list)
    for tok in toks:
        tok_type_name = token.tok_name[tok.type]
        if tok_type_name in IGNORE:
            continue
        elif tok_type_name in SPECIAL:
            toks_raw.append(f'<{tok_type_name}>')
            if tok_type_name in {'STRING', 'COMMENT'}:
                anonymize_dict[f'<{tok_type_name}>'].append(tok.string)
        else:
            toks_raw.append(tok.string)
    assert len(toks_raw) == len(toks)-2
    print(str(toks_raw))
    print(str(anonymize_dict))
    return toks_raw, anonymize_dict

f = open("/content/drive/MyDrive/syscan_final/check.py", "r")
Lines = f.readlines()
string1=""
for line in Lines:
    string1 = string1+line
tokenize_python_code(string1)

