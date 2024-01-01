
# 1. Copy wavefunctions and weights from SCF calculations

    cp ../1-paratec/2-WFN-GW/weight.dat .
    cp ../1-paratec/2-WFN-GW/GWC WFN
    cp ../1-paratec/2-WFNq-GW/GWC WFNq

or just create links to those files, e.g.

    ln -s ../1-paratec/2-WFN-GW/weight.dat weight.dat

and so on

# 2. Submit calculations

    sbatch job.epsilon


