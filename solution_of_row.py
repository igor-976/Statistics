import math as m


def i(a):
    n = 0
    row = 0
    while n <= 100:
        row += (m.pow(a, 2*n+1)*m.pow(-1, n))/(m.pow(2, n-1)*m.factorial(n)*(2*n+1))
        n += 1
    return row


def p(b):
    n = 0
    row = 0
    while n <= 100:
        row += (m.pow(b, 2*n+1)*m.pow(-1, n))/(m.pow(2, n-1)*m.factorial(n)*(2*n+1))
        n += 1
    return row


def d(a):
    n = 0
    row = 0
    while n <= 100:
        row += (m.pow(a, 2*n+3)*m.pow(-1, n))/(m.pow(2, n-1)*m.factorial(n)*(2*n+3))
        n += 1
    return row


def graph_d(ranged, step):
    dispersion = [[], []]
    j = 0
    n = 0
    while n <= ranged:
        n += step
        dispersion[0].append(round(n, 3))
        dispersion[1].append(round(d(n)/i(n), 4))
        j += 1

    return dispersion


def graph_p(ranged, step):
    probability = [[], []]
    boundary = 0
    chance = 0
    while boundary <= ranged:
        boundary += step
        probability[0].append(round(boundary, 4))
        if boundary >= 8:
            probability[1].append(0.6829)
        else:
            chance = p(m.sqrt(d(boundary)/i(boundary)))/i(boundary)
            probability[1].append(round(chance, 4))
    return probability


def graph_p2(step, boundary):
    probability = [[], []]
    values = 0
    chance = 0
    bound = boundary
    if boundary >= 8:
        bound = 8

    while values <= boundary:
        values += step
        probability[0].append(round(values, 4))
        if values > 8:
            probability[1].append(1.0)
        else:
            chance = p(values)/i(bound)
            probability[1].append(round(chance, 4))
    return probability



