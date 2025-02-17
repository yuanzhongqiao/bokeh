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

# Standard library imports
import re
import warnings

# Bokeh imports
from bokeh.util.warnings import BokehDeprecationWarning, BokehUserWarning
from tests.support.util.api import verify_all
from tests.support.util.types import Capture

# Module under test
import bokeh as b # isort:skip

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

ALL =  (
    '__version__',
    'license',
    'sampledata',
)

_LICENSE = """\
Copyright (c) 2012 - 2024, Anaconda, Inc., and Bokeh Contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

Neither the name of Anaconda nor the names of any contributors
may be used to endorse or promote products derived from this software
without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
THE POSSIBILITY OF SUCH DAMAGE.

"""

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

Test___all__ = verify_all(b, ALL)

def test___version___type() -> None:
    assert isinstance(b.__version__, str)

def test___version___defined() -> None:
    VERSION_PAT = re.compile(r"^(\d+\.\d+\.\d+)((?:\.dev|\.rc).*)?")
    assert VERSION_PAT.match(b.__version__.strip(".dirty"))

def test_license(capsys: Capture) -> None:
    b.license()
    out, err = capsys.readouterr()
    assert out == _LICENSE

class TestWarnings:
    @pytest.mark.parametrize('cat', (BokehDeprecationWarning, BokehUserWarning))
    def test_bokeh_custom(self, cat) -> None:
        r = warnings.formatwarning("message", cat, "line", "lineno")
        assert r == f"{cat.__name__}: message\n"

    def test_general_default(self) -> None:
        r = warnings.formatwarning("message", RuntimeWarning, "line", "lineno")
        assert r == "line:lineno: RuntimeWarning: message\n"

    # TODO (bev) issue with this one test and 3.9 support PR
    @pytest.mark.skip
    def test_filters(self) -> None:
        assert ('always', None, BokehUserWarning, None, 0) in warnings.filters
        assert ('always', None, BokehDeprecationWarning, None, 0) in warnings.filters

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
