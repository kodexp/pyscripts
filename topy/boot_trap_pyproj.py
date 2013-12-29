__author__ = 'fzhang'

import subprocess
import os
import sys


class BootTrapper:
    """
    Boottrap a python project, setup common dirs and files
    """
    def __init__(self, rootdir, pname):
        self.root_dir = rootdir
        self.project_name = pname

    def create_dirs(self):
        path2proj=os.path.join(self.root_dir,self.project_name)

        subprocess.check_call( ["mkdir","-p", path2proj] )

        os.chdir(path2proj)

        for adir in (self.project_name, "tests", "doc", "apidoc","bin","config","resource"):

            if not os.path.exists(adir):
                subprocess.check_call(["mkdir", adir] )
            else:
                pass  #dir exists already

    def create_init_files(self):
        pass

    def create_setup(self):
        """ make a setup.py
        """
    def create_tox_conf(self):
        """
        create a sample tox.ini
        """

    def create_readme_(self):
        """
        create a README.txt"
        """
    def create_virtualenv(self):
        """
        create a virtual environment
        """
    def create_hello_module(self):
        """
        create a sample program hello world
        """

    def create_test_hello(self):
        """
        create a test program
        """

#####################################################################################
if __name__ == "__main__":
    # Usage thisprog rootdir projname

    if len(sys.argv)<3:
        print "Usage: %s  rootdir projname" %(sys.argv[0])
        sys.exit(1)


    rootd=sys.argv[1]
    pname=sys.argv[2]

    #boot=BootTrapper("/tmp", "pyname")
    boot = BootTrapper(rootd, pname)

    boot.create_dirs()