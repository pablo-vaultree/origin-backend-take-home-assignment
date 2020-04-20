import pytest

from api.risk_analysis_service import Profile


def test():
    x = Profile("a")
    assert x.name == "a"
