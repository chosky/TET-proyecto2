# Installation manual to execute the mpi project on the DCA
Operative System: Centos 7

Follow the next steps: 

Install Open MPI
1. $ wget https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/m/mpi4py-common-1.3.1-2.el7.noarch.rpm 
2. $ rpm -i mpi4py-common-1.3.1-2.el7.noarch.rpm
3. $ wget https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/m/mpi4py-openmpi-1.3.1-2.el7.x86_64.rpm
4. $ rpm -i mpi4py-openmpi-1.3.1-2.el7.x86_64.rpm
  // we have to load the module of openmpi
5. $ module load mpi/openmpi-x86_64

Install and Exec Virtual-env
1. $ yum install python2
2. $ yum install epel-release
3. $ yum install python-pip
4. $ pip install virtualenv 
5. $ virtualenv entorno
 //entorno is the name of our virtual enviroment
 //This command is to activate the virtual-env
6. $ source entorno/bin/activate 

Install libraries
1. $ pip install mpi4py
2. $ pip install matplotlib
3. $ pip install numpy

To deactive the Virtual enviroment

1. $ deactivate

