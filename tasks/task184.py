def p(d):
    F=lambda d:[[*dict.fromkeys([c for c in r if c])]for r in d if any(r)]
    return[*zip(*F(zip(*F(d))))]