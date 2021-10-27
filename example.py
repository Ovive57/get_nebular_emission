import get_nebular_emission.eml as eml
#from preparenovonix.compare import plot_vct

# The r" " are needed to handle Windows paths
# otherwise ' ' can be enough to include the path.
infile = r"example_data/example_data.dat"

# Calculate the nebular emission lines
# The columns where the stellar mass, SFR and Zcold=Mzcold/Mcold are
# to be found in the input file, should be specified within the argument:
# m_sfr_z
# Several components are allowed (e.g. disk and bulge).
#eml.eml(infile, m_sfr_z=[[11,6,2]],h0=0.6777, verbose=True, Testing=True)

eml.eml(infile, m_sfr_z=[[11,0,2],[11,0,2]], h0=0.6777, LC2sfr=True, verbose=True, Testing=True) #(e.g. LC photons)
#eml.eml(infile, m_sfr_z=[[11,13,2],[11,13,2]], h0=0.6777, LC2sfr=False, verbose=True, Testing=True) #(e.g. SFR)

## Compare the prepared file with the original one
#plot_vct(infile, first_loop=0, plot_type='png', plot_show=True)

