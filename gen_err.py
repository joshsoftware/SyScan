import numpy as np
import random
import re

action_pattern_map = {
    'delete(': ("\(", ""),
    'delete)': ("\)", ""),
    'delete,': (",", ""),
    'delete:': (":", ""),
    'delete{': ("\{", ""),
    'delete}': ("\}", ""),
    'delete[': ("\[", ""),
    'delete]': ("\]", ""),
    'delete+': ("\+", ""),
    'delete-': ("-", ""),
    'delete=': ("=", ""),
    'delete<': ("<", ""),
    'delete>': ("\*", ""),
    'duplicate(': ("\(", "( ("),
    'duplicate)': ("\)", ") )"),
    'duplicate,': (",", ", ,"),
    'duplicate{': ("\{", "{ {"),
    'duplicate}': ("\}", "} }"),
    'duplicate[': ("\[", "[ ["),
    'duplicate]': ("\]", "] ]"),
    'replace,with;': (",", ";"),
}

action_pattern_map_kw = {
    'deleteWhile': ("while", ""),
    'deleteElif': ("elif", ""),
    'deleteIf': ("if", ""),
    'deleteIf': ("for", ""),
    'replaceDefWithDf': ("def", "df"),
    'replaceElseWithEles': ("else", "eles"),
    'replaceWhileWithFor': ("while", "for"),
    'replaceForWithWhile': ("for", "while"),
    'replaceWhileWithWhil': ("while", "whil"),
    'replaceClassWithCls': ("class", "cls"),    
    'replacePandasWithPanda': ("pandas", "panda"),
    'replace<INDENT>With<DEDENT>': ("<INDENT>", "<DEDENT>"),
    'replaceNumpyWithNump': ("numpy", "nump"),
    'replaceRandomWithRandm': ("random", "randm"),
    'replaceImportWithImport': ("import", "Import"),
    'replaceIfWithElse': ("if", "else"),
    'replaceElseWithElif': ("else", "elif"),
    'replaceElifwithElseif': ("elif", "elseif"),
}

actions = list(action_pattern_map.keys())
actions_kw = list(action_pattern_map_kw.keys())

def corrupt_syntax(line):
    err_cnt = random.randint(0, 2)
    cnt = 0
    np.random.shuffle(actions)
    
    for act in actions:
        if cnt > err_cnt:
            break
        else:
            patt = action_pattern_map[act]   #value patt[0], patt[1]
            positions = [m.span() for m in re.finditer(patt[0], line)]            
            if(len(positions) == 0):
                continue
            else:
                if len(positions) > 1: 
                    to_corrupt = np.random.randint(len(positions))
                else: 
                    to_corrupt = 0
                line = line[:positions[to_corrupt][0]] + patt[1] + line[positions[to_corrupt][1]:]
        return line

def corrupt_kw_typo(line):
    err_cnt = random.randint(0, 2)
    cnt = 0
    np.random.shuffle(actions_kw)
    
    for act in actions_kw:
        if cnt > err_cnt:
            break
        else:
            patt = action_pattern_map_kw[act]   #value patt[0], patt[1]
            positions = [m.span() for m in re.finditer(patt[0], line)]
            if(len(positions) == 0):
                continue
            else:
                if len(positions) > 1: 
                    to_corrupt = np.random.randint(len(positions))
                else: 
                    to_corrupt = 0
                line = line[:positions[to_corrupt][0]] + patt[1] + line[positions[to_corrupt][1]:]
    return line

file1 = open('good.txt', 'r')
file2 = open('bad.txt', 'w')

for line in file1:
    new_line = corrupt_syntax(line)
    final_line = corrupt_kw_typo(new_line)
    file2.write(final_line)

file1.close()
file2.close()
