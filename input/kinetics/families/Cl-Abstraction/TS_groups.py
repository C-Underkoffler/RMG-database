#!/usr/bin/env python
# encoding: utf-8

name = "Cl-Abstraction/TS_groups"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "X_Cl_or_Xrad_Cl_Xbirad_Cl_Xtrirad_Cl",
    group = "OR{HCl, C_Cl, O_Cl, Cl2, Si_Cl, N_Cl, S_Cl}",
    distances = DistanceData(distances={}),
)

entry(
    index = 2,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Hrad, Orad, Crad, Clrad, Sirad, Srad, Nrad}",
    distances = DistanceData(distances={}),
)

entry(
    index = 3,
    label = "HCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 H  u0 {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 4,
    label = "C_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C  ux {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 9,
    label = "Cs_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs ux {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 21,
    label = "Csnorad_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 43,
    label = "C_H3Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cl u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 44,
    label = "CsRHHCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cl  u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 45,
    label = "CsRRHCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cl  u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,S}
5    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 46,
    label = "CsRRRCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cl  u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
5    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 22,
    label = "Csrad_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 47,
    label = "C_H2Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Cl u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 48,
    label = "CsradRHCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs  u1 {2,S} {3,S} {4,S}
2 *2 Cl  u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 49,
    label = "CsradRRCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs  u1 {2,S} {3,S} {4,S}
2 *2 Cl  u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 23,
    label = "CsbiradCl",
    group = "OR{Cs_singletCl, Cs_tripletCl}",
    distances = DistanceData(distances={}),
)

entry(
    index = 50,
    label = "Cs_singletCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    R  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 51,
    label = "Cs_tripletCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    R  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 24,
    label = "CstriradCl",
    group = "OR{Cdoublet_Cl, Cquartet_Cl}",
    distances = DistanceData(distances={}),
)

entry(
    index = 52,
    label = "Cdoublet_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C  u1 p1 {2,S}
2 *2 Cl u0 p0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 53,
    label = "Cquartet_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C  u3 p0 {2,S}
2 *2 Cl u0 p0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 10,
    label = "Cd_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd ux {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 25,
    label = "Cdnorad_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 54,
    label = "Cd_C/R/Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,S} {3,D}
2 *2 Cl u0 {1,S}
3    C  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 55,
    label = "Cd_O/R/Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,S} {3,D}
2 *2 Cl u0 {1,S}
3    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 26,
    label = "Cdrad_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 56,
    label = "Cdrad_C/Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,S} {3,D}
2 *2 Cl u0 {1,S}
3    C  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 57,
    label = "Cdrad_O/Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,S} {3,D}
2 *2 Cl u0 {1,S}
3    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 11,
    label = "Ct_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Ct u0 {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 12,
    label = "Cb_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cb u0 {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 5,
    label = "O_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  ux {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 13,
    label = "OradCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u1 {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 14,
    label = "ORCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u0 {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 27,
    label = "OHCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 28,
    label = "OCCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 58,
    label = "O/Cs/Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 59,
    label = "O/Cd/Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 60,
    label = "O/Ct/Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 61,
    label = "O/Cb/Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 29,
    label = "OOCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 340,
    label = "Cl2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cl u0 {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 341,
    label = "Si_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Si ux {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 342,
    label = "N_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 N  ux {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 344,
    label = "N3_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 [N3s,N3d] ux {2,S}
2 *2 Cl        u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 348,
    label = "N3s_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 N3s ux {2,S}
2 *2 Cl  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 359,
    label = "NH2Cl",
    group = 
"""
1 *1 N3s ux {2,S} {3,S} {4,S}
2 *2 Cl  u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 360,
    label = "N3s/Cl/H/R",
    group = 
"""
1 *1 N3s ux {2,S} {3,S} {4,S}
2 *2 Cl  u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 361,
    label = "N3s/Cl/R/R",
    group = 
"""
1 *1 N3s ux {2,S} {3,S} {4,S}
2 *2 Cl  u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 349,
    label = "N3d_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 N3d ux {2,S}
2 *2 Cl  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 345,
    label = "N5_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 [N5s,N5d,N5dd,N5t,N5b] ux {2,S}
2 *2 Cl                     u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 350,
    label = "N5s_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 N5s ux {2,S}
2 *2 Cl  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 351,
    label = "N5d_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 [N5d,N5dd] ux {2,S}
2 *2 Cl         u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 343,
    label = "S_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 S  ux {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 346,
    label = "SradCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 S  u1 {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 347,
    label = "SRCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 S  u0 {2,S}
2 *2 Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 352,
    label = "SHCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 S  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 353,
    label = "SCl2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 S  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    Cl u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 354,
    label = "SOCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 S  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 355,
    label = "SCCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 S  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 356,
    label = "SSCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 S  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    S  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 357,
    label = "SNCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 S  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    N  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 358,
    label = "SSiCl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 S  u0 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    Si ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 6,
    label = "Hrad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 H u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 7,
    label = "Orad",
    group = "OR{OjR, O_atom_triplet}",
    distances = DistanceData(distances={}),
)

entry(
    index = 15,
    label = "OjR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O u1 {2,S}
2    R ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 30,
    label = "OjH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 31,
    label = "OjC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O u1 {2,S}
2    C ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 62,
    label = "OjCs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O  u1 {2,S}
2    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 63,
    label = "OjCd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O  u1 {2,S}
2    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 64,
    label = "OjCt",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O  u1 {2,S}
2    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 65,
    label = "OjCb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O  u1 {2,S}
2    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 32,
    label = "OjO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O u1 {2,S}
2    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 16,
    label = "O_atom_triplet",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O u2
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 8,
    label = "Crad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 C u[1,2,3,4]
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 17,
    label = "Cj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 C u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 33,
    label = "Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 66,
    label = "Cs_methyl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 67,
    label = "CsjRH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 103,
    label = "CsjCH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 208,
    label = "Csj/Cs/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 209,
    label = "Csj/Cd/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 210,
    label = "Csj/Ct/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 211,
    label = "Csj/Cb/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 104,
    label = "CsjOH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 68,
    label = "CsjRRH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 105,
    label = "CsjCCH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 212,
    label = "Csj/Cs/Cs/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 213,
    label = "Csj/Cs/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 214,
    label = "Csj/Cs/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 215,
    label = "Csj/Cs/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 216,
    label = "Csj/Cd/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 217,
    label = "Csj/Cd/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 218,
    label = "Csj/Cd/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 219,
    label = "Csj/Ct/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 220,
    label = "Csj/Ct/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 221,
    label = "Csj/Cb/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 106,
    label = "CsjCOH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 222,
    label = "Csj/Cs/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 223,
    label = "Csj/Cd/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 224,
    label = "Csj/Ct/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 225,
    label = "Csj/Cb/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 107,
    label = "CsjOOH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 69,
    label = "CsjRRR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 108,
    label = "CsjCCC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 226,
    label = "Csj/Cs/Cs/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 227,
    label = "Csj/Cs/Cs/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 228,
    label = "Csj/Cs/Cs/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 229,
    label = "Csj/Cs/Cs/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 230,
    label = "Csj/Cs/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 231,
    label = "Csj/Cs/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 232,
    label = "Csj/Cs/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 233,
    label = "Csj/Cs/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 234,
    label = "Csj/Cs/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 235,
    label = "Csj/Cs/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 236,
    label = "Csj/Cd/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 237,
    label = "Csj/Cd/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 238,
    label = "Csj/Cd/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 239,
    label = "Csj/Cd/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 240,
    label = "Csj/Cd/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 241,
    label = "Csj/Cd/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 242,
    label = "Csj/Ct/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 243,
    label = "Csj/Ct/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 244,
    label = "Csj/Ct/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 245,
    label = "Csj/Cb/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 109,
    label = "CsjCCO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 246,
    label = "Csj/Cs/Cs/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 247,
    label = "Csj/Cs/Cd/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 248,
    label = "Csj/Cs/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 249,
    label = "Csj/Cs/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 250,
    label = "Csj/Cd/Cd/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 251,
    label = "Csj/Cd/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 252,
    label = "Csj/Cd/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 253,
    label = "Csj/Ct/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 254,
    label = "Csj/Ct/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 255,
    label = "Csj/Cb/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 110,
    label = "CsjCOO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 256,
    label = "Csj/Cs/O/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 257,
    label = "Csj/Cd/O/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 258,
    label = "Csj/Ct/O/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 259,
    label = "Csj/Cb/O/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 111,
    label = "CsjOOO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    O  ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 34,
    label = "Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 70,
    label = "Cdj_CR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D}
2    C  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 112,
    label = "Cdj_CH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 260,
    label = "Cdj_CdsH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 261,
    label = "Cdj_CddH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 113,
    label = "Cdj_CC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 262,
    label = "Cdj_CdsCs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 263,
    label = "Cdj_CdsCd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 264,
    label = "Cdj_CdsCt",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 265,
    label = "Cdj_CdsCb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 266,
    label = "Cdj_CddCs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cs  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 267,
    label = "Cdj_CddCd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cd  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 268,
    label = "Cdj_CddCt",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Ct  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 269,
    label = "Cdj_CddCb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 114,
    label = "Cdj_CO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 270,
    label = "Cdj_CdsO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 271,
    label = "Cdj_CddO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    O   ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 71,
    label = "Cdj_OR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D}
2    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 115,
    label = "Cdj_OH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 116,
    label = "Cdj_OC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 272,
    label = "Cdj_OCs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 273,
    label = "Cdj_OCd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 274,
    label = "Cdj_OCt",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 275,
    label = "Cdj_OCb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 117,
    label = "Cdj_OO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 35,
    label = "Ctj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Ct u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 72,
    label = "CtjC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Ct u1 {2,T}
2    C  ux {1,T}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 36,
    label = "Cbj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cb u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 18,
    label = "Cjj",
    group = "OR{Csjj, Cdjj}",
    distances = DistanceData(distances={}),
)

entry(
    index = 37,
    label = "Csjj",
    group = "OR{Cs_sing, Cs_trip}",
    distances = DistanceData(distances={}),
)

entry(
    index = 73,
    label = "Cs_sing",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 284,
    label = "Cs_singH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 285,
    label = "Cs_singRH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs  u0 p1 {2,S} {3,S}
2    H   u0 {1,S}
3    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 294,
    label = "Cs_singCH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 304,
    label = "Cs_sing/Cs/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 305,
    label = "Cs_sing/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 306,
    label = "Cs_sing/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 307,
    label = "Cs_sing/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 295,
    label = "Cs_singOH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 286,
    label = "Cs_singRR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs  u0 p1 {2,S} {3,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 296,
    label = "Cs_singCC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    C  ux {1,S}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 308,
    label = "Cs_sing/Cs/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 309,
    label = "Cs_sing/Cs/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 310,
    label = "Cs_sing/Cs/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 311,
    label = "Cs_sing/Cs/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 312,
    label = "Cs_sing/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 313,
    label = "Cs_sing/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 314,
    label = "Cs_sing/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 315,
    label = "Cs_sing/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 316,
    label = "Cs_sing/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 317,
    label = "Cs_sing/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 297,
    label = "Cs_singCO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    C  ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 318,
    label = "Cs_sing/Cs/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Cs ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 319,
    label = "Cs_sing/Cd/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Cd ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 320,
    label = "Cs_sing/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Ct u0 {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 321,
    label = "Cs_sing/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    Cb u0 {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 298,
    label = "Cs_singOO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u0 p1 {2,S} {3,S}
2    O  ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 74,
    label = "Cs_trip",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 287,
    label = "Cs_tripH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 288,
    label = "Cs_tripRH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs  u2 p0 {2,S} {3,S}
2    R!H ux {1,S}
3    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 299,
    label = "Cs_tripCH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    C  ux {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 322,
    label = "Cs_trip/Cs/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cs ux {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 323,
    label = "Cs_trip/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cd ux {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 324,
    label = "Cs_trip/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Ct u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 325,
    label = "Cs_trip/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cb u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 300,
    label = "Cs_tripOH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    O  ux {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 289,
    label = "Cs_tripRR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs  u2 p0 {2,S} {3,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 301,
    label = "Cs_tripCC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    C  ux {1,S}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 326,
    label = "Cs_trip/Cs/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 327,
    label = "Cs_trip/Cs/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 328,
    label = "Cs_trip/Cs/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 329,
    label = "Cs_trip/Cs/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 330,
    label = "Cs_trip/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 331,
    label = "Cs_trip/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 332,
    label = "Cs_trip/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 333,
    label = "Cs_trip/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 334,
    label = "Cs_trip/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 335,
    label = "Cs_trip/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 302,
    label = "Cs_tripCO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    C  ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 336,
    label = "Cs_trip/Cs/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cs ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 337,
    label = "Cs_trip/Cd/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cd ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 338,
    label = "Cs_trip/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Ct ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 339,
    label = "Cs_trip/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    Cb ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 303,
    label = "Cs_tripOO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u2 p0 {2,S} {3,S}
2    O  ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 38,
    label = "Cdjj",
    group = "OR{Cd_singletR, Cd_tripletR}",
    distances = DistanceData(distances={}),
)

entry(
    index = 75,
    label = "Cd_singletR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u0 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 290,
    label = "Cd_singletC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u0 p1 {2,D}
2    C  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 291,
    label = "Cd_singletO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u0 p1 {2,D}
2    O  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 76,
    label = "Cd_tripletR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u2 p0
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 292,
    label = "Cd_tripletC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u2 p0 {2,D}
2    C  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 293,
    label = "Cd_tripletO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u2 p0 {2,D}
2    O  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 19,
    label = "Cjjj",
    group = "OR{C_doubletR, C_quartetR}",
    distances = DistanceData(distances={}),
)

entry(
    index = 39,
    label = "C_doubletR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 C u1 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 40,
    label = "C_quartetR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 C u3
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 20,
    label = "Cjjjj",
    group = "OR{C_quintet, C_triplet}",
    distances = DistanceData(distances={}),
)

entry(
    index = 41,
    label = "C_quintet",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 C u4 p0
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 42,
    label = "C_triplet",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 C u2 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 394,
    label = "Clrad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cl u[1,2,3,4]
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 395,
    label = "Sirad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Si u[1,2,3,4]
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 396,
    label = "Srad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 S u[1,2,3,4]
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 398,
    label = "Srad_H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 S u[1,2,3,4] {2,S}
2    H u0         {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 399,
    label = "Srad_R",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 S   u[1,2,3,4] {2,S}
2    R!H u0         {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 402,
    label = "Srad_C",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 S u[1,2,3,4] {2,S}
2    C u0         {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 403,
    label = "Srad_N",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 S u[1,2,3,4] {2,S}
2    N u0         {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 404,
    label = "Srad_O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 S u[1,2,3,4] {2,S}
2    O u0         {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 405,
    label = "Srad_Si",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 S  u[1,2,3,4] {2,S}
2    Si u0         {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 406,
    label = "Srad_S",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 S u[1,2,3,4] {2,S}
2    S u0         {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 407,
    label = "Srad_Cl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 S  u[1,2,3,4] {2,S}
2    Cl u0         {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 397,
    label = "Nrad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 N u[1,2,3,4]
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 400,
    label = "N3_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 [N3s,N3d] u[1,2,3,4]
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 408,
    label = "N3s_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 N3s u[1,2,3,4]
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 411,
    label = "NH2",
    group = 
"""
1 *3 N3s u1 {2,S} {3,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 412,
    label = "N3s/H/R",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 N3s u1 {2,S} {3,S}
2    H   u0 {1,S}
3    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 413,
    label = "N3s/R/R",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 N3s u1 {2,S} {3,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 400,
    label = "N3d_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 N3d u[1,2,3,4]
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 401,
    label = "N5_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 [N5s,N5d,N5dd,N5t,N5b] u[1,2,3,4]
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 409,
    label = "N5s_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 N5s u[1,2,3,4]
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 410,
    label = "N5d_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 [N5d,N5dd] u[1,2,3,4]
""",
    distances = DistanceData(distances={}),
)

tree(
"""
L1: X_Cl_or_Xrad_Cl_Xbirad_Cl_Xtrirad_Cl
    L2: HCl
    L2: C_Cl
        L3: Cs_Cl
            L4: Csnorad_Cl
                L5: C_H3Cl
                L5: CsRHHCl
                L5: CsRRHCl
                L5: CsRRRCl
            L4: Csrad_Cl
                L5: C_H2Cl
                L5: CsradRHCl
                L5: CsradRRCl
            L4: CsbiradCl
                L5: Cs_singletCl
                L5: Cs_tripletCl
            L4: CstriradCl
                L5: Cdoublet_Cl
                L5: Cquartet_Cl
        L3: Cd_Cl
            L4: Cdnorad_Cl
                L5: Cd_C/R/Cl
                L5: Cd_O/R/Cl
            L4: Cdrad_Cl
                L5: Cdrad_C/Cl
                L5: Cdrad_O/Cl
        L3: Ct_Cl
        L3: Cb_Cl
    L2: O_Cl
        L3: OradCl
        L3: ORCl
            L4: OHCl
            L4: OCCl
                L5: O/Cs/Cl
                L5: O/Cd/Cl
                L5: O/Ct/Cl
                L5: O/Cb/Cl
            L4: OOCl
    L2: Cl2
    L2: Si_Cl
    L2: N_Cl
        L3: N3_Cl
            L4: N3s_Cl
                L5: NH2Cl
                L5: N3s/Cl/H/R
                L5: N3s/Cl/R/R
            L4: N3d_Cl
        L3: N5_Cl
            L4: N5s_Cl
            L4: N5d_Cl
    L2: S_Cl
        L3: SradCl
        L3: SRCl
            L4: SHCl
            L4: SCl2
            L4: SOCl
            L4: SCCl
            L4: SSCl
            L4: SNCl
            L4: SSiCl
L1: Y_rad_birad_trirad_quadrad
    L2: Hrad
    L2: Orad
        L3: OjR
            L4: OjH
            L4: OjC
                L5: OjCs
                L5: OjCd
                L5: OjCt
                L5: OjCb
            L4: OjO
        L3: O_atom_triplet
    L2: Crad
        L3: Cj
            L4: Csj
                L5: Cs_methyl
                L5: CsjRH2
                    L6: CsjCH2
                        L7: Csj/Cs/H2
                        L7: Csj/Cd/H2
                        L7: Csj/Ct/H2
                        L7: Csj/Cb/H2
                    L6: CsjOH2
                L5: CsjRRH
                    L6: CsjCCH
                        L7: Csj/Cs/Cs/H
                        L7: Csj/Cs/Cd/H
                        L7: Csj/Cs/Ct/H
                        L7: Csj/Cs/Cb/H
                        L7: Csj/Cd/Cd/H
                        L7: Csj/Cd/Ct/H
                        L7: Csj/Cd/Cb/H
                        L7: Csj/Ct/Ct/H
                        L7: Csj/Ct/Cb/H
                        L7: Csj/Cb/Cb/H
                    L6: CsjCOH
                        L7: Csj/Cs/O/H
                        L7: Csj/Cd/O/H
                        L7: Csj/Ct/O/H
                        L7: Csj/Cb/O/H
                    L6: CsjOOH
                L5: CsjRRR
                    L6: CsjCCC
                        L7: Csj/Cs/Cs/Cs
                        L7: Csj/Cs/Cs/Cd
                        L7: Csj/Cs/Cs/Ct
                        L7: Csj/Cs/Cs/Cb
                        L7: Csj/Cs/Cd/Cd
                        L7: Csj/Cs/Cd/Ct
                        L7: Csj/Cs/Cd/Cb
                        L7: Csj/Cs/Ct/Ct
                        L7: Csj/Cs/Ct/Cb
                        L7: Csj/Cs/Cb/Cb
                        L7: Csj/Cd/Cd/Cd
                        L7: Csj/Cd/Cd/Ct
                        L7: Csj/Cd/Cd/Cb
                        L7: Csj/Cd/Ct/Ct
                        L7: Csj/Cd/Ct/Cb
                        L7: Csj/Cd/Cb/Cb
                        L7: Csj/Ct/Ct/Ct
                        L7: Csj/Ct/Ct/Cb
                        L7: Csj/Ct/Cb/Cb
                        L7: Csj/Cb/Cb/Cb
                    L6: CsjCCO
                        L7: Csj/Cs/Cs/O
                        L7: Csj/Cs/Cd/O
                        L7: Csj/Cs/Ct/O
                        L7: Csj/Cs/Cb/O
                        L7: Csj/Cd/Cd/O
                        L7: Csj/Cd/Ct/O
                        L7: Csj/Cd/Cb/O
                        L7: Csj/Ct/Ct/O
                        L7: Csj/Ct/Cb/O
                        L7: Csj/Cb/Cb/O
                    L6: CsjCOO
                        L7: Csj/Cs/O/O
                        L7: Csj/Cd/O/O
                        L7: Csj/Ct/O/O
                        L7: Csj/Cb/O/O
                    L6: CsjOOO
            L4: Cdj
                L5: Cdj_CR
                    L6: Cdj_CH
                        L7: Cdj_CdsH
                        L7: Cdj_CddH
                    L6: Cdj_CC
                        L7: Cdj_CdsCs
                        L7: Cdj_CdsCd
                        L7: Cdj_CdsCt
                        L7: Cdj_CdsCb
                        L7: Cdj_CddCs
                        L7: Cdj_CddCd
                        L7: Cdj_CddCt
                        L7: Cdj_CddCb
                    L6: Cdj_CO
                        L7: Cdj_CdsO
                        L7: Cdj_CddO
                L5: Cdj_OR
                    L6: Cdj_OH
                    L6: Cdj_OC
                        L7: Cdj_OCs
                        L7: Cdj_OCd
                        L7: Cdj_OCt
                        L7: Cdj_OCb
                    L6: Cdj_OO
            L4: Ctj
                L5: CtjC
            L4: Cbj
        L3: Cjj
            L4: Csjj
                L5: Cs_sing
                    L6: Cs_singH2
                    L6: Cs_singRH
                        L7: Cs_singCH
                            L8: Cs_sing/Cs/H
                            L8: Cs_sing/Cd/H
                            L8: Cs_sing/Ct/H
                            L8: Cs_sing/Cb/H
                        L7: Cs_singOH
                    L6: Cs_singRR
                        L7: Cs_singCC
                            L8: Cs_sing/Cs/Cs
                            L8: Cs_sing/Cs/Cd
                            L8: Cs_sing/Cs/Ct
                            L8: Cs_sing/Cs/Cb
                            L8: Cs_sing/Cd/Cd
                            L8: Cs_sing/Cd/Ct
                            L8: Cs_sing/Cd/Cb
                            L8: Cs_sing/Ct/Ct
                            L8: Cs_sing/Ct/Cb
                            L8: Cs_sing/Cb/Cb
                        L7: Cs_singCO
                            L8: Cs_sing/Cs/O
                            L8: Cs_sing/Cd/O
                            L8: Cs_sing/Ct/O
                            L8: Cs_sing/Cb/O
                        L7: Cs_singOO
                L5: Cs_trip
                    L6: Cs_tripH2
                    L6: Cs_tripRH
                        L7: Cs_tripCH
                            L8: Cs_trip/Cs/H
                            L8: Cs_trip/Cd/H
                            L8: Cs_trip/Ct/H
                            L8: Cs_trip/Cb/H
                        L7: Cs_tripOH
                    L6: Cs_tripRR
                        L7: Cs_tripCC
                            L8: Cs_trip/Cs/Cs
                            L8: Cs_trip/Cs/Cd
                            L8: Cs_trip/Cs/Ct
                            L8: Cs_trip/Cs/Cb
                            L8: Cs_trip/Cd/Cd
                            L8: Cs_trip/Cd/Ct
                            L8: Cs_trip/Cd/Cb
                            L8: Cs_trip/Ct/Ct
                            L8: Cs_trip/Ct/Cb
                            L8: Cs_trip/Cb/Cb
                        L7: Cs_tripCO
                            L8: Cs_trip/Cs/O
                            L8: Cs_trip/Cd/O
                            L8: Cs_trip/Ct/O
                            L8: Cs_trip/Cb/O
                        L7: Cs_tripOO
            L4: Cdjj
                L5: Cd_singletR
                    L6: Cd_singletC
                    L6: Cd_singletO
                L5: Cd_tripletR
                    L6: Cd_tripletC
                    L6: Cd_tripletO
        L3: Cjjj
            L4: C_doubletR
            L4: C_quartetR
        L3: Cjjjj
            L4: C_quintet
            L4: C_triplet
    L2: Clrad
    L2: Sirad
    L2: Srad
        L3: Srad_H
        L3: Srad_R
            L4: Srad_C
            L4: Srad_N
            L4: Srad_O
            L4: Srad_Si
            L4: Srad_S
            L4: Srad_Cl
    L2: Nrad
        L3: N3_rad
            L4: N3s_rad
            L4: NH2
            L4: N3s/H/R
            L4: N3s/R/R
            L4: N3d_rad
        L3: N5_rad
            L4: N5s_rad
            L4: N5d_rad
"""
)

