#! /usr/bin/env python

#Determine Andromeda location in ra/decs

# convert to decimal degrees

from math import cos, pi
from random import uniform

NSRC = 1_000_000

def clip_to_radius[(ra, dec, ras, decs)]:
    output_ras = []
    output_decs = []
    for ra_i, dec_i in zip(ras, decs):
        if ra_i**2 + dec_i**2 <1:
            output_ras.append(ra_i)
            output_decs.append(dec_i)
    return output_ras, output_decs

def get_radec():
    pass

def generate_sky_pos():
        
    # from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'

    d, m, s = DEC.split(':')
    DEC = int(d)+int(m)/60+float(s)/3600

    h, m, s = RA.split(':')
    RA = 15*(int(h)+int(m)/60+float(s)/3600)
    RA = RA/cos(DEC*pi/180)

    

    # make 1000 stars within 1 degree of Andromeda
    ras = []
    decs = []
    for i in range(NSRC):
        ras.append(RA + uniform(-1,1))
        decs.append(DEC + uniform(-1,1))


# now write these to a csv file for use by my other program
    with open('catalog.csv','w') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)
