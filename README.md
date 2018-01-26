# KMC_scripts
Various python scripts to analyze Zacros kinetic Monte Carlo output files.

1) count_reactions.py: Running count_reactions.py in the Zacros output folder, it scans the general_output file and returns the number of all elementary reactions that occurred during the simulation. The elementary reactions list is obtained from mechanism_input file.

2) lattice_plot.py: Plots the lattice from the lattice_output file, linking points which are defined as neighbours in the lattice_input file
