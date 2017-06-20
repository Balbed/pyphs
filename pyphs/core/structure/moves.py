#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 14:59:02 2017

@author: Falaize
"""
from pyphs.misc.tools import myrange


# ======================== MOVE ELEMENTS ==================================== #
def movesquarematrixcolnrow(M, indi, indf):
    """
Move row and col of a square matrix from index i to index j

Parameters
----------

M: 2D array like
    A square matrix.

indi, indf: intergers
    Indices.

Return
------
A: same type as :code:`M`.
    :code:`A[j, :] == M[i, :]` and :code:`A[:, j] == M[:, i]`.

Example
-------
>>> import numpy as np
>>> M = np.eye(3)
>>> print(M)
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
>>> from pyphs.core.structure.moves import movesquarematrixcolnrow
>>> A = movesquarematrixcolnrow(M, 0, 2)
>>> print(A)
    """
    n = M.shape[0]
    new_indices = myrange(n, indi, indf)
    return M[new_indices, new_indices]


def movematrixcols(matrix, indi, indf):
    n = matrix.shape[1]
    new_indices = myrange(n, indi, indf)
    return matrix[:, new_indices]


def moveCoreMcolnrow(core, indi, indf):
    if not core.M.is_zero:
        core.M = movesquarematrixcolnrow(core.M, indi, indf)


def move_stor(core, indi, indf):
    new_indices = myrange(core.dims.x(), indi, indf)
    core.x = [core.x[el] for el in new_indices]
    if core._dxH is not None:
        core._dxH = [core._dxH[el] for el in new_indices]
    moveCoreMcolnrow(core, indi, indf)


def move_diss(core, indi, indf):
    new_indices = myrange(core.dims.w(), indi, indf)
    core.w = [core.w[el] for el in new_indices]
    core.z = [core.z[el] for el in new_indices]
    moveCoreMcolnrow(core, core.dims.x()+indi, core.dims.x()+indf)
    if not core.Zl.is_zero:
        core.Zl = movesquarematrixcolnrow(core.Zl, indi, indf)


def move_port(core, indi, indf):
    new_indices = myrange(core.dims.y(), indi, indf)
    core.u = [core.u[el] for el in new_indices]
    core.y = [core.y[el] for el in new_indices]
    moveCoreMcolnrow(core, core.dims.x()+core.dims.w()+indi,
                     core.dims.x()+core.dims.w()+indf)


def move_connector(core, indi, indf):
    new_indices = myrange(core.dims.cy(), indi, indf)
    core.cu = [core.cu[el] for el in new_indices]
    core.cy = [core.cy[el] for el in new_indices]
    moveCoreMcolnrow(core, core.dims.x()+core.dims.w()+core.dims.y()+indi,
                     core.dims.x()+core.dims.w()+core.dims.y()+indf)