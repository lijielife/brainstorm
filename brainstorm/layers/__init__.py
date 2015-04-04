#!/usr/bin/env python
# coding=utf-8
from __future__ import division, print_function, unicode_literals
from functools import partial

from brainstorm.structure.construction import ConstructionWrapper
from brainstorm.layers.input_layer import InputLayerImpl
from brainstorm.layers.noop_layer import NoOpLayerImpl
from brainstorm.layers.fully_connected_layer import FullyConnectedLayerImpl
from brainstorm.layers.squared_difference_layer import SquaredDifferenceLayerImpl
from brainstorm.layers.binomial_cross_entropy import BinomialCrossEntropyLayerImpl
from brainstorm.layers.loss_layer import LossLayerImpl

# somehow this construction is needed because in __all__ unicode does not work
__all__ = [str(a) for a in [
    'InputLayer', 'NoOpLayer', 'FullyConnectedLayer', 'SquaredDifferenceLayer',
    'LossLayer', 'BinomialCrossEntropyLayer'
]]

InputLayer = partial(ConstructionWrapper.create, "InputLayer")
NoOpLayer = partial(ConstructionWrapper.create, "NoOpLayer")
FullyConnectedLayer = partial(ConstructionWrapper.create, "FullyConnectedLayer")
SquaredDifferenceLayer = partial(ConstructionWrapper.create, "SquaredDifferenceLayer")
BinomialCrossEntropyLayer = partial(ConstructionWrapper.create, "BinomialCrossEntropyLayer")
LossLayer = partial(ConstructionWrapper.create, "LossLayer")