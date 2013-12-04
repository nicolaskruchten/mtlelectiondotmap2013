# Copyright (c) 2013 Nicolas Kruchten.
# All rights reserved.
# 
# Redistribution and use in source and binary forms are permitted
# provided that the above copyright notice and this paragraph are
# duplicated in all such forms and that any documentation,
# advertising materials, and other materials related to such
# distribution and use acknowledge that the software was developed
# by the <organization>.  The name of the
# <organization> may not be used to endorse or promote products derived
# from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED ``AS IS'' AND WITHOUT ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

from matplotlib import pyplot as plt
from shapely.geometry import Point, shape
from random import uniform, shuffle
import json, csv

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


def getVotes():
    votes = csv.DictReader(open("elections-2013-resultats-detailles.csv", "r"))

    sectionVotes = {}

    for v in votes:
        if not v["Poste"] == "0": #mayoralty
            continue 

        #need a section key in the form XXX-YYY to match the JSON file below
        section = v["District"].split("-")[0].zfill(3) + "-" + v["Bureau"].zfill(3)
        if section not in sectionVotes:
            sectionVotes[section] = []
        numVotes = int(v["Votes"])
        color = None
        if "BERGERON" in v["Candidat"]: #green
            color = 'g'#78BE20'
        elif "CODERRE" in v["Candidat"]: #red
            color = 'r'#662d91'
        elif "JOLY" in v["Candidat"]: #blue
            color = 'b'#fdb813'
        else: #blue
            color = '#888888'
        if color:
            sectionVotes[section].append( (numVotes, color) )
    return sectionVotes

def getPoints(sectionVotes):
    with open ("sectionelect.json", "r") as f:
        sections=json.loads(f.read())

    points = []
    for feature in sections["features"]:
        section = shape(feature["geometry"])
        (minx, miny, maxx, maxy) = section.bounds
        sectionName = feature["properties"]["NOM_SECTION"]
        if sectionName not in sectionVotes:
            print sectionName + " not found!"
            continue

        for (numVotes, color) in sectionVotes[sectionName]:
            for i in range(numVotes):
                while True:
                    samplepoint = Point( uniform(minx,maxx), uniform(miny,maxy) )
                    if section.contains( samplepoint ):
                        points.append((samplepoint, color))
                        break
    shuffle(points) #otherwise they show up in party order!
    print len(points)
    return points


def saveScatter(points, fileName):
    fig     = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    patches = []
    with open ("districts.json", "r") as f:
        districts=json.loads(f.read())
        for x in districts['features']:
            for coordlist in x['geometry']['coordinates']:
                if len(coordlist) == 1:
                    coords = coordlist[0]
                else:
                    coords = coordlist
                twod = [[x,y] for [x,y,z] in coords]
                patches.append(Polygon(twod, True))

    p = PatchCollection(patches, facecolor='#ffffff',edgecolor="#ffffff", linewidths=0.1)
    ax.add_collection(p)

    patches = []
    with open ("districtelect.json", "r") as f:
        districts=json.loads(f.read())
        for x in districts['features']:
            for coordlist in x['geometry']['coordinates']:
                if len(coordlist) == 1:
                    coords = coordlist[0]
                else:
                    coords = coordlist
                patches.append(Polygon(coords, True))

    p = PatchCollection(patches, facecolor='#ffffff',edgecolor="#bbbbbb", linewidths=0.1)
    ax.add_collection(p)

    xcoords = [p.x for (p,c) in points]
    ycoords = [p.y for (p,c) in points]
    colors = [c for (p,c) in points]
    plt.scatter(xcoords, ycoords, c = colors, marker='.', s=0.3, alpha=0.5, lw = 0)
    ax.axis('off')
    fig.savefig(fileName, facecolor="#bbbbbb", dpi=1000, pad_inches=0)

sectionVotes = getVotes()
points = getPoints(sectionVotes)
saveScatter(points, "mtlelectiondotmap2013.png")

