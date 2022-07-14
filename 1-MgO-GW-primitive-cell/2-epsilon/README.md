
# 1. Copy wavefunctions and weights from SCF calculations

    cp ../1-paratec/2-WFN/weight.dat .
    cp ../1-paratec/2-WFN/GWR WFN
    cp ../1-paratec/2-WFNq/GWR WFNq

or just create links to those files

    ln -s ../1-paratec/2-WFN/weight.dat weight.dat

and so on

# 2. Submit calculations

    sbatch job.epsilon


