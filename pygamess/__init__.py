#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from .gamess import Gamess, GamessError, GamessFromInputFile

__version__ = "0.3.0"
__all__ = ["Gamess", "GamessFromInputFile"]


del gamess
