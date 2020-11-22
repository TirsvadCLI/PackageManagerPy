import pytest

from packageManager.manager import packageManager

def test_install():
    App = packageManager()
    App.update()
    App.upgrade()
    App.install('curl')
    pass