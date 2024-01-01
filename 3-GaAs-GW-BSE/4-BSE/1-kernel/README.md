
# 1. Copy necessary files from the SCF calculations

    cp ../../1-paratec/2-WFN0-GW/GWC WFN_co
  

# 2. Copy necessary files from the epsilon calculations

    cp ../../2-epsilon/eps0mat eps0mat
    cp ../../2-epsilon/epsmat epsmat


or just create links to those files

    ln -s ../../1-paratec/2-WFN0-GW/GWC WFN_co

and so on

# 3. Submit calculations

    sbatch job.kernel


