
# 1. Copy necessary files from the SCF calculations

    cp ../1-paratec/1-SCF/CD95 RHO
    cp ../1-paratec/1-SCF/VXC VXC
    cp ../1-paratec/2-WFN/weight.dat weight.dat
    cp ../1-paratec/2-WFN/GWR WFN_inner
  

# 2. Copy necessary files from the epsilon calculations

    cp ../2-epsilon/eps0mat .
    cp ../2-epsilon/epsmat .


or just create links to those files

    ln -s ../1-paratec/2-WFN/weight.dat weight.dat

and so on

# 3. Submit calculations

    sbatch job.sigma


