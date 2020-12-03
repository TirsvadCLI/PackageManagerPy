import distro
import logging
import os
import subprocess

class packageManager(object):
    _log = object
    _distro: tuple
    _packageManager: str

    def __init__(self):
        self._log = logging.getLogger(__name__)
        self._distro = distro.linux_distribution(full_distribution_name=False)
        if (self._distro[0] in ('debian', 'ubuntu')):
            self._packageManager = "apt"
        elif (self._distro[0] in ('fedora', 'cenots')):
            if (self._distro[0] == 'fedora') and ( int(self._distro[1]) >= 22 ):
                self._packageManager = "dnf"
            else:
                self._packageManager = 'yum'
        else:
            self._log.error("Failed to detect PackageManager for OS "+self._distro[0]+" "+self._distro[1])

    def _install(self, package):
        if(self._packageManager=='apt'):
            process = subprocess.Popen('DEBIAN_FRONTEND=noninteractive apt-get install -qq '+package, shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        elif (self._packageManager=='dnf'):
            process = subprocess.Popen('dnf --assumeyes --quiet install '+package, shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        elif (self._packageManager=='yum'):
            process = subprocess.Popen('yum install '+package, shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        if (process.wait()):
            self._log.error('Install failed for package '+package)
        else:
            self._log.debug('Installed package '+package)

    def install(self, packages):
        if isinstance(packages, str):
            self._install(packages)
        for p in packages:
            self._install(p)

    def update(self):
        if(self._packageManager=='apt'):
            process = subprocess.Popen('DEBIAN_FRONTEND=noninteractive apt-get update -qq', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        elif (self._packageManager=='dnf'):
            process = subprocess.Popen('dnf --assumeyes --quiet  upgrade --refresh', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        elif (self._packageManager=='yum'):
            process = subprocess.Popen('yum update', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        if (process.wait()):
            self._log.error('System update failed ')

    def upgrade(self):
        if(self._packageManager=='apt'):
            process = subprocess.Popen('DEBIAN_FRONTEND=noninteractive apt-get upgrade -qq ', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        elif (self._packageManager=='dnf'):
            process = subprocess.Popen('dnf  --assumeyes --quiet  upgrade', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        elif (self._packageManager=='yum'):
            process = subprocess.Popen('yum upgrade', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
        if (process.wait()):
            self._log.error('System upgrade failed ')

    def system_upgrade(self):
        self.update()
        if (self._packageManager=='dnf'):
            self.install('dnf-plugin-system-upgrade')
            process = subprocess.Popen('dnf system-upgrade', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=subprocess.STDOUT, executable="/bin/bash")
            if (process.wait()):
                self._log.error('System upgrade failed ')
        self.upgrade()

if __name__ == "__main__":
    exit('Cannot be run directly')
