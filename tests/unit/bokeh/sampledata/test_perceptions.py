#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2024, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations # isort:skip

import pytest ; pytest

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# External imports
import pandas as pd

# Bokeh imports
from tests.support.util.api import verify_all

# Module under test
#import bokeh.sampledata.perceptions as bsp # isort:skip

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

ALL = (
    'numberly',
    'probly',
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

Test___all__ = pytest.mark.sampledata(verify_all("bokeh.sampledata.perceptions", ALL))

@pytest.mark.sampledata
def test_numberly() -> None:
    import bokeh.sampledata.perceptions as bsp
    assert isinstance(bsp.numberly, pd.DataFrame)

    # check detail for package data
    assert len(bsp.numberly) == 46

@pytest.mark.sampledata
def test_probly() -> None:
    import bokeh.sampledata.perceptions as bsp
    assert isinstance(bsp.probly, pd.DataFrame)

    # check detail for package data
    assert len(bsp.probly) == 46

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
