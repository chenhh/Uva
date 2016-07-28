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


def cross_prod(v1, v2):
    """
    v1: tuple(int), size: 2
    v2: tuple(int), size: 2

    cross_prod(v1, v2) = |v1| * |v2| * sin(theta)
    if cross_prod(v1, v2) == 0, then v1 is parallel to v2
    (theta = 0 or pi).

    """
    return v1[0] * v2[1] - v1[1] * v2[0]


def dot_prod(v1, v2):
    """
    v1: tuple(int), size: 2
    v2: tuple(int), size: 2

    dot_prod(v1, v2) = |v1|* |v2| * cos(theta)
    if dot_prod(v1, v2) == 0 then v1 is orthogonal to v2
    (theta = pi/2 or 3/2 pi)
    """
    return v1[0] * v2[0] + v1[1] * v2[1]


def candidate_shape(points):
    """
    points: list((int, int)), size: 4
    (a, b, c, d)
    """
    vab = (points[1][0] - points[0][0], points[1][1] - points[0][1])
    vbc = (points[2][0] - points[1][0], points[2][1] - points[1][1])
    vcd = (points[3][0] - points[2][0], points[3][1] - points[2][1])
    vda = (points[0][0] - points[3][0], points[0][1] - points[3][1])

    vac = (points[2][0] - points[0][0], points[2][1] - points[0][1])
    vdb = (points[1][0] - points[3][0], points[1][1] - points[3][1])

    cross_abcd = cross_prod(vab, vcd)
    cross_dabc = cross_prod(vda, vbc)

    # "Ordinary Quadrilateral"
    ans = 0
    if cross_abcd == 0 or cross_dabc == 0:
        # ab is parallel to cd or da is parallel to bc
        # the shape can be a Trapezium
        ans = 1

    if cross_abcd == 0 and cross_dabc == 0:
        # both ab is parallel to cd and da is parallel to bc
        # the shape can be a Parallelogram
        ans = 2

        if dot_prod(vac, vdb) == 0:
            # ac is orthogonal to db, the shape can be Rhombus
            ans = 3

        if dot_prod(vab, vbc) == 0:
            # ab is orthogonal to bc, the shape can be Rectangle
            ans = 4

        if dot_prod(vac, vdb) == 0 and dot_prod(vab, vbc) == 0:
            ans = 5
    return ans


def four_points_shape(points):
    """ uva 11800 """
    a, b, c, d = points
    ans = candidate_shape(points)
    ans = max(ans, candidate_shape([a, c, b, d]))
    ans = max(ans, candidate_shape([a, b, d, c]))

    if ans == 0:
        # the general case
        return "Ordinary Quadrilateral"

    if ans == 1:
        return "Trapezium"

    if ans == 2:
        return "Parallelogram"

    if ans == 3:
        return "Rhombus"

    if ans == 4:
        return "Rectangle"

    if ans == 5:
        return "Square"
