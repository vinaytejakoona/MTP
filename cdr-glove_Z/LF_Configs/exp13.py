# def LF_induce(c):
#     return (1,1) if re.search(r'{{A}}.{0,20}induc.{0,20}{{B}}', get_tagged_text(c), flags=re.I) else (0,0)


def LF_induce(c):
    return (1,distanceCD_(c,['induc'])) if re.search(r'{{A}}.*induc.*{{B}}', get_tagged_text(c), flags=re.I) else (0,0)

causal_past = ['induced', 'caused', 'due']
# def LF_d_induced_by_c(c):
#     return (rule_regex_search_btw_BA(c, '.{0,50}' + ltp(causal_past) + '.{0,9}(by|to).{0,50}', 1),1)

def LF_d_induced_by_c(c):
    sc = 0
    word_vectors = get_word_vectors(get_between_tokens(c))
    for w in causal_past:
        sc=max(sc,get_similarity(word_vectors,w))
    return (1,sc)

# def LF_d_induced_by_c_tight(c):
#     return (rule_regex_search_btw_BA(c, '.{0,50}' + ltp(causal_past) + ' (by|to) ', 1),1)

def LF_d_induced_by_c_tight(c):
    return (rule_regex_search_btw_BA(c, '.*' + ltp(causal_past) + ' (by|to) ', 1),distanceCD_(c,causal_past))

def LF_induce_name(c):
    return (1,1) if 'induc' in c.chemical.get_span().lower() else (0,0)     

causal = ['cause[sd]?', 'induce[sd]?', 'associated with']
# def LF_c_cause_d(c):
#     return (1,1) if (
#         re.search(r'{{A}}.{0,50} ' + ltp(causal) + '.{0,50}{{B}}', get_tagged_text(c), re.I)
#         and not re.search('{{A}}.{0,50}(not|no).{0,20}' + ltp(causal) + '.{0,50}{{B}}', get_tagged_text(c), re.I)
#     ) else (0,0)

def LF_c_cause_d(c):
    return (1,distanceCD_(c,causal)) if (
        re.search(r'{{A}}.* ' + ltp(causal) + '.*{{B}}', get_tagged_text(c), re.I)
        and not re.search('{{A}}.{0,50}(not|no).{0,20}' + ltp(causal) + '.{0,50}{{B}}', get_tagged_text(c), re.I)
    ) else (0,0)


treat = ['treat', 'effective', 'prevent', 'resistant', 'slow', 'promise', 'therap']

def LF_d_treat_c(c):
    return (rule_regex_search_btw_BA(c, '.{0,50}' + ltp(treat) + '.{0,50}', -1),1)

# def LF_d_treat_c(c):
#     return (rule_regex_search_btw_BA(c, '.*' + ltp(treat) + '.*', -1),1)

def LF_c_treat_d(c):
    return (rule_regex_search_btw_AB(c, '.{0,50}' + ltp(treat) + '.{0,50}', -1),1)

# def LF_c_treat_d(c):
#     return (rule_regex_search_btw_AB(c, '.*' + ltp(treat) + '.*', -1),1)

# def LF_treat_d(c):
#     return (rule_regex_search_before_B(c, ltp(treat) + '.{0,50}', -1),1)


def LF_treat_d(c):
    sc = 0
    word_vectors = get_word_vectors(get_left_tokens(c[1],5))
    for w in treat:
        sc=max(sc,get_similarity(word_vectors,w))
    if(re.search('(not|no|none) .* {{B}}', get_tagged_text(c), re.I)):
        return (0,0)
    else:
        return (-1,sc)
    
# def LF_c_treat_d_wide(c):
#     return (rule_regex_search_btw_AB(c, '.*' + ltp(treat) + '.*', -1),1)

def LF_c_treat_d_wide(c):
    return (rule_regex_search_btw_AB(c, '.{0,200}' + ltp(treat) + '.{0,200}', -1),1)


def LF_c_d(c):
    return (1,1) if ('{{A}} {{B}}' in get_tagged_text(c)) else (0,0)

def LF_c_induced_d(c):
    return (1,1) if (
        ('{{A}} {{B}}' in get_tagged_text(c)) and 
        (('-induc' in c[0].get_span().lower()) or ('-assoc' in c[0].get_span().lower()))
        ) else (0,0)

def LF_improve_before_disease(c):
    return (rule_regex_search_before_B(c, 'improv.*', -1),1)

pat_terms = ['in a patient with ', 'in patients with']
def LF_in_patient_with(c):
    return (-1,1) if re.search(ltp(pat_terms) + '{{B}}', get_tagged_text(c), flags=re.I) else (0,0)

uncertain = ['combin', 'possible', 'unlikely']
# def LF_uncertain(c):
#     return (rule_regex_search_before_A(c, ltp(uncertain) + '.*', -1),1)

def LF_uncertain(c):
    sc = 0
    word_vectors = get_word_vectors(get_left_tokens(c[1],5))
    for w in uncertain:
        sc=max(sc,get_similarity(word_vectors,w))
    if(re.search('(not|no|none) .* {{B}}', get_tagged_text(c), re.I)):
        return (0,0)
    else:
        return (-1,sc)
    
# def LF_induced_other(c):
#     return (rule_regex_search_tagged_text(c, '{{A}}.{20,1000}-induced {{B}}', -1),1)

def LF_induced_other(c):
    return (rule_regex_search_tagged_text(c, '{{A}}.*-induced {{B}}', -1),1)

# def LF_far_c_d(c):
#     return (rule_regex_search_btw_AB(c, '.{100,5000}', -1),1)

def LF_far_c_d(c):
    return (rule_regex_search_btw_AB(c, '.*', -1),distanceCDn1(c))

# def LF_far_d_c(c):
#     return (rule_regex_search_btw_BA(c, '.{100,5000}', -1),1)

def LF_far_d_c(c):
    return (rule_regex_search_btw_BA(c, '.*', -1),distanceCD(c))

# def LF_risk_d(c):
#     return (rule_regex_search_before_B(c, 'risk of ', 1),1)


def LF_risk_d(c):
    sc = 0
    word_vectors = get_word_vectors(get_left_tokens(c[1],5))
    sc=max(sc,get_similarity(word_vectors,'risk'))
    return (1,sc)

# def LF_develop_d_following_c(c):
#     return (1,1) if re.search(r'develop.{0,25}{{B}}.{0,25}following.{0,25}{{A}}', get_tagged_text(c), flags=re.I) else (0,0)

def LF_develop_d_following_c(c):
    return (1,distanceDevFol(c)) if re.search(r'develop.*{{B}}.*following.*{{A}}', get_tagged_text(c), flags=re.I) else (0,0)

procedure, following = ['inject', 'administrat'], ['following']
# def LF_d_following_c(c):
#     return (1,1) if re.search('{{B}}.{0,50}' + ltp(following) + '.{0,20}{{A}}.{0,50}' + ltp(procedure), get_tagged_text(c), flags=re.I) else (0,0)

def LF_d_following_c(c):
    return (1,distanceDC_(c,following)) if re.search('{{B}}.*' + ltp(following) + '.*{{A}}.*' + ltp(procedure), get_tagged_text(c), flags=re.I) else (0,0)

def LF_measure(c):
    return (-1,1) if re.search('measur.{0,75}{{A}}', get_tagged_text(c), flags=re.I) else (0,0)

# def LF_measure(c):
#     return (-1,1) if re.search('measur.*{{A}}', get_tagged_text(c), flags=re.I) else (0,0)

def LF_level(c):
    return (-1,1) if re.search('{{A}}.{0,25} level', get_tagged_text(c), flags=re.I) else (0,0)


# def LF_level(c):
#     return (-1,1) if re.search('{{A}}.* level', get_tagged_text(c), flags=re.I) else (0,0)


def LF_neg_d(c):
    return (-1,1) if re.search('(none|not|no) .{0,25}{{B}}', get_tagged_text(c), flags=re.I) else (0,0)

# def LF_neg_d(c):
#     return (-1,1) if re.search('(none|not|no) .*{{B}}', get_tagged_text(c), flags=re.I) else (0,0)


WEAK_PHRASES = ['none', 'although', 'was carried out', 'was conducted',
                'seems', 'suggests', 'risk', 'implicated',
               'the aim', 'to (investigate|assess|study)']

WEAK_RGX = r'|'.join(WEAK_PHRASES)

def LF_weak_assertions(c):
    return (-1,1) if re.search(WEAK_RGX, get_tagged_text(c), flags=re.I) else (0,0)
