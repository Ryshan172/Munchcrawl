"""
Holds functionality for modelling of food, ingredient and flavour relationships. 

Since it is difficult to map food ingredients to tastes, the idea is to:
- Use a probabilistic graphical model (PGM) like a Logical Credal Network (LCN)
- Using an LCN would allow for graphical modelling of tastes and also have a range of probabilities, since it isn't an exact science
- Research does exist on using LCNs for modelling relationships and running inference so these established procedures can be used 

"""


