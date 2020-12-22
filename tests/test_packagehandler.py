import pytest

from packageManager.manager import packageManager

class Test():
    _app = packageManager()

    def setup_method(self, test_method):
        pass

    def teardown_method(self, test_method):
        pass

    def test_update_os(self):
        self._app.update()

    def test_install(self):
        self._app.install('ntpdate')
