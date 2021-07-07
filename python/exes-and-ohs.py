def xo(s):
    chars = list(s)
    x_count = 0
    o_count = 0
    for c in chars:
        if c.lower() == 'x':
            x_count += 1
        elif c.lower() == 'o':
            o_count += 1
    return x_count == o_count