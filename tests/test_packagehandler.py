import pytest

from packageManager.manager import packageManager

def test_install():
    App = packageManager()
    App.install('curl')
    pass