#!/usr/bin/env python
# encoding: utf-8

name = "Cl_Abstraction/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "X_Cl_or_Xrad_Cl_Xbirad_Cl_Xtrirad_Cl;Y_rad_birad_trirad_quadrad",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""
If a biradical CH2JJ can abstract from RCH4 to make RCH3J and CH3J 
then a Y_rad CH3J should be able to abstract from RCH3J which means X_H needs 
to include Xrad_H. I.e. you can abstract from a radical. To make this possible
a head node has been created X_H_or_Xrad_H which is a union of X_H and Xrad_H.
The kinetics for it have just been copied from X_H and are only defined for 
abstraction by Y_rad_birad. I.e. the top level very approximate guess.

Do better kinetics for this exist? Do we in fact use the reverse kinetics anyway?
""",
)

entry(
    index = 1,
    label = "X_Cl;Y_rad_birad_trirad_quadrad",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)



