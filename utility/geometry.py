# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""


def is_triangle(values, debug=False):
    """
    uva 194
    :param values: list[float], length : 6
    :return: True if the parameters can form a triangle else False
    """
    from math import pi, sin, cos
    EPS = 1e-6

    a, alpha, b, beta, c, gamma = values
    if a <= 0 or b <= 0 or c <= 0 or alpha <= 0 or beta <= 0 or gamma <= 0:
        if debug:
            print("some negative values.")
            print(values)
        return False

    if alpha + beta + gamma - pi > EPS:
        if debug:
            print("the sum of angles not equal to pi.",
                  sum(alpha + beta + gamma))
        return False

    if a + b <= c or a + c <= b or b + c <= a:
        # triangle inequality
        if debug:
            print("not satisfying triangle inequality.")
        return False

    a2 = a * a
    b2 = b * b
    c2 = c * c
    ab = a * b
    ac = a * c
    bc = b * c
    sin_alpha = sin(alpha)
    sin_beta = sin(beta)
    sin_gamma = sin(gamma)

    sine1 = a * sin_beta - b * sin_alpha
    sine2 = a * sin_gamma - c * sin_alpha
    sine3 = b * sin_gamma - c * sin_beta

    if (sine1 > EPS or sine2 > EPS or sine3 > EPS):
        if debug:
            print("not satisfying law of sine.")
            print(sine1, sine2, sine3)
        return False

    cosine1 = a2 - b2 - c2 + 2 * bc * cos(alpha)
    cosine2 = b2 - a2 - c2 + 2 * ac * cos(beta)
    cosine3 = c2 - a2 - b2 + 2 * ab * cos(gamma)

    if (cosine1 > EPS or cosine2 > EPS or cosine3 > EPS):
        if debug:
            print("not satisfying law of cosine.")
            print(cosine1, cosine2, cosine3)
        return False

    return True


def main():
    pass


if __name__ == '__main__':
    main()
