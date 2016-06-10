# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 13:53:43 2016

@author: Falaize
"""
import numpy


def norm(lis):
    """
    return the norm of a vector given as a list
    """
    return numpy.sqrt(numpy.matrix(lis)*numpy.matrix(lis).T)[0, 0]


def myrange(N, indi, indf):
    """
    return 'range(N)' with index 'indi' at position 'indf'
    """
    lis = range(N)
    if indi < indf:
        deb = lis[:indi] + lis[indi+1:indf+1]
        end = lis[indf+1:]
        eli = [lis[indi], ]
        lis = deb + eli + end
    elif indi > indf:
        deb = lis[:indf]
        end = lis[indf:indi] + lis[indi+1:]
        eli = [lis[indi], ]
        lis = deb + eli + end
    return lis


def progressbar(progress):
    """
     progressbar() : Displays or updates a console progress bar
     Accepts a float between 0 and 1. Any int will be converted to a float.
     A value under 0 represents a 'halt'.
     A value at 1 or bigger represents 100%
     """
    import sys
    barLength = 10  # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format("#"*block+"-"*(barLength-block),
                                              progress*100, status)
    print text
#    sys.stdout.write(text)
#    sys.stdout.flush()


def splitlist(lis, len_out):
    """
    Split the 'lis' in a list1 of list2 with max(len(list(2)))='len_out'
    """
    lis.reverse()
    lis_out = list()
    while lis:
        temp = list()
        for _ in range(len_out):
            try:
                temp.append(lis.pop())
            except IndexError:
                pass
        lis_out.append(temp)
    return lis_out


def matrix2list(mat):
    assert 1 in mat.shape
    return [e[0, 0] for e in mat]


def decimate(it, nd=10):
    """
    Return first then each 'nd' elements from iterable 'it'.

    Parameters
    -----------

    it : iterable
        Input data.

    nd : int
        Decimation factor

    Returns
    -------

    l : list
        One in 'nd' values from 'it'.

    """
    assert (isinstance(nd, int) and nd > 0), "'nd' is not an integer: {0!r}".format(nd)
    l = list()
    n = 0
    for el in it:
        if not n % nd:
            l.append(el)
        n += 1
    return l
