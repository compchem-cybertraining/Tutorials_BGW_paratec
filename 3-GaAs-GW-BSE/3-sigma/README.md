
# 1. Copy necessary files from the SCF calculations

    cp ../1-paratec/1-SCF/CD95 RHO
    cp ../1-paratec/1-SCF/VXC VXC
    cp ../1-paratec/2-WFN0-GW/weight.dat weight.dat
    cp ../1-paratec/2-WFN0-GW/GWC WFN_inner
  

# 2. Copy necessary files from the epsilon calculations

    cp ../2-epsilon/eps0mat eps0mat
    cp ../2-epsilon/epsmat epsmat


or just create links to those files, e.g.

    ln -s ../1-paratec/2-WFN0-GW/weight.dat weight.dat

and so on

# 3. Submit calculations

    sbatch job.sigma


