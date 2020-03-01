import numpy as np

def distanceCDfar(c):
    dist = 0
    chem_start, chem_end = c.chemical.get_word_start(), c.chemical.get_word_end()
    dis_start, dis_end = c.disease.get_word_start(), c.disease.get_word_end()
    if dis_start < chem_start:
        dist = chem_start - dis_end
    else:
        dist = dis_start - chem_end
    return dist/5000

def distanceCD(c):
    dist = 0
    chem_start, chem_end = c.chemical.get_word_start(), c.chemical.get_word_end()
    dis_start, dis_end = c.disease.get_word_start(), c.disease.get_word_end()
    if dis_start < chem_start:
        dist = chem_start - dis_end
    else:
        dist = dis_start - chem_end
    return (5000 - dist)/5000

def distanceCD_(c,l):
    dist = []
    for w in l:
        pattern = r'({{A}})(.*)('+w+r')(.*)({{B}})'
        matchObj = re.search(pattern, get_tagged_text(c), flags=re.I)
        if(matchObj):
            match_groups = matchObj.group(2,4)
            dist.append(min([len(mg) for mg in match_groups]))
    if(len(dist)>0):
        return (5000-max(dist))/5000
    return 0

def distanceDC_(c,l):
    dist = []
    for w in l:
        pattern = r'({{B}})(.*)('+w+r')(.*)({{A}})'
        matchObj = re.search(pattern, get_tagged_text(c), flags=re.I)
        if(matchObj):
            match_groups = matchObj.group(2,4)
            dist.append(min([len(mg) for mg in match_groups]))
    if(len(dist)>0):
        return (5000-max(dist))/5000
    return 0

def distanceDevFol(c):
    dist = 1000
    matchObj = re.search(r'(develop)(.*)({{B}})(.*)(following)(.*)({{A}})', get_tagged_text(c), flags=re.I)
    if(matchObj):
        match_groups = matchObj.group(2,4,6)
        dist = min([len(mg) for mg in match_groups])
    return (5000-dist)/5000
    