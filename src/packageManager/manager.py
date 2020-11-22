import distro
import logging
import os
import subprocess

class packageManager(object):
    _log = logging.getLogger(__name__)
    _distro: tuple
    _packageManager: str

    def __init__(self):
        self._distro = distro.linux_distribution(full_distribution_name=False)
        if (self._distro[0] in ('debian', 'ubuntu')):
            self._packageManager = "apt"
        elif (self._distro[0] in ('fedora', 'cenots')):
            if (self._distro[0] == 'Fedora') and ( int(self._distro[1]) >= 22 ):
                self._packageManager = "dnf"
            else:
                self._packageManager = 'yum'
        else:
            self._log.error("Failed to detect PackageManager for OS "+self._distro[0]+" "+self._distro[1])

    def _install(self, package):
        if(self._packageManager=='apt'):
            proc = subprocess.Popen('DEBIAN_FRONTEND=noninteractive apt-get install -qq '+package, shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        if (not proc.wait()):
            self._log.error('Install failed for package '+package)

    def install(self, packages):
        if isinstance(packages,str):
            self._install(packages)
        for p in packages:
            self._install(p)

    def update(self):
        if(self._packageManager=='apt'):
            proc = subprocess.Popen('DEBIAN_FRONTEND=noninteractive apt-get update -qq ', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        elif (self._packageManager=='dnf'):
            proc = subprocess.Popen('dnf upgrade --refresh', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        elif (self._packageManager=='yum'):
            proc = subprocess.Popen('yum update', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")

        if (not proc.wait()):
            self._log.error('System update failed ')

    def upgrade(self):
        if(self._packageManager=='apt'):
            proc = subprocess.Popen('DEBIAN_FRONTEND=noninteractive apt-get upgrade -qq ', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        elif (self._packageManager=='dnf'):
            proc = subprocess.Popen('dnf upgrade', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        elif (self._packageManager=='yum'):
            proc = subprocess.Popen('yum upgrade', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")

        if (not proc.wait()):
            self._log.error('System upgrade failed ')

if __name__ == "__main__":
	pass