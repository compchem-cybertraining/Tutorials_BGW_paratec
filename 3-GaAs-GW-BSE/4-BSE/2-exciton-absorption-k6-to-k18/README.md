
# 1. Copy necessary files from the SCF calculations

    cp ../../1-paratec/2-WFN0-GW/GWC WFN_co
    cp ../../1-paratec/3-WFN0-fine-grid-18-BSE/GWC WFN_fi

# 2. Copy necessary files from the epsilon calculations

    cp ../../2-epsilon/eps0mat eps0mat
    cp ../../2-epsilon/epsmat epsmat

# 4. Copy necessary files from sigma calculations

    cp ../../3-sigma/sigma_hp.dat sigma_hp.dat
    cp ../../3-sigma/eqp_co.dat eqp_co.dat

# 5. Copy necessary files from the BSE kernel calculaitons

    cp ../1-kernel/bsexmat bsexmat
    cp ../1-kernel/bsedmat bsedmat

or just create links to those files, e.g.

    ln -s ../../1-paratec/2-WFN0-GW/GWC WFN_co

and so on

# 6. Submit calculations

    sbatch job.absorption

# 7. Plot the absorption spectray using Python

    python BSE_RPA_plot.py



