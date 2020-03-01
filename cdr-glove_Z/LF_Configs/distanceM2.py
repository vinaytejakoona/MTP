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
            dist.append(max([len(mg) for mg in match_groups]))
    if(len(dist)>0):
        return (5000-min(dist))/5000
    return 0

def distanceDC_(c,l):
    dist = []
    for w in l:
        pattern = r'({{B}})(.*)('+w+r')(.*)({{A}})'
        matchObj = re.search(pattern, get_tagged_text(c), flags=re.I)
        if(matchObj):
            match_groups = matchObj.group(2,4)
            dist.append(max([len(mg) for mg in match_groups]))
    if(len(dist)>0):
        return (5000-min(dist))/5000
    return 0

def distanceDevFol(c):
    dist = 1000
    matchObj = re.search(r'(develop)(.*)({{B}})(.*)(following)(.*)({{A}})', get_tagged_text(c), flags=re.I)
    if(matchObj):
        match_groups = matchObj.group(2,4,6)
        dist = max([len(mg) for mg in match_groups])
    return (5000-dist)/5000
    

def levenshtein(source, target):
    if len(source) < len(target):
        return levenshtein(target, source)

    # So now we have len(source) >= len(target).
    if len(target) == 0:
        return len(source)

    # We call tuple() to force strings to be used as sequences
    # ('c', 'a', 't', 's') - numpy uses them as values by default.
    source = np.array(tuple(source))
    target = np.array(tuple(target))

    # We use a dynamic programming algorithm, but with the
    # added optimization that we only need the last two rows
    # of the matrix.
    previous_row = np.arange(target.size + 1)
    for s in source:
        # Insertion (target grows longer than source):
        current_row = previous_row + 1

        # Substitution or matching:
        # Target and source items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))

        # Deletion (target grows shorter than source):
        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)

        previous_row = current_row

    return previous_row[-1]