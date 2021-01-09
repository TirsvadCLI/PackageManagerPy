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
import subprocess
process=subprocess.Popen('DEBIAN_FRONTEND=noninteractive apt-get install ntpdate', shell=True)
process.communicate()[0]
if process.returncode != 0:
    print('some error')
