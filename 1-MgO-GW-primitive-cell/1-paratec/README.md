

# 1. Run the SCF calculations to obtain the converged charge density 

    cd 1-SCF
    sbatch job.scf
    cd ../


# 2a. Prepare the wavefunction at other the k-points and for more bands, these are non-self-consistent calculations

    cd 2-WFN
    cp ../1-SCF/CD .
    sbatch job.wfn
    cd ../

# 2b. Prepare the wavefunction around the q=0 point using slightly-shifted k-points

    cd 2-WFNq
    cp ../1-SCF/CD .
    sbatch job.wfnq 
    cd ../

