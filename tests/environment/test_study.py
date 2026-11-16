"""Offline smoke checks for the study environment; never imports old exercises."""

import pytest

from tools.check_environment import study_checks


@pytest.mark.parametrize(
    "name,function", list(study_checks().items()), ids=list(study_checks())
)
def test_study_package_behavior(name, function):
    function()
