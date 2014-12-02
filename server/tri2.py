import numpy as np
import scipy.optimize as opt

#Returns the distance from a point to the list of spheres
def calc_distance(point):
    return np.power(np.sum(np.power(centers-point,2),axis=1),.5)-rad

#Latitude/longitude to carteisan
def geo2cart(lat,lon):
    lat=np.deg2rad(lat)
    lon=np.deg2rad(lon)
    points=np.vstack((earth_radius*np.cos(lat)*np.cos(lon),
           earth_radius*np.cos(lat)*np.sin(lon),
           earth_radius*np.sin(lat))).T
    return points

#Cartesian to lat/lon
def cart2geo(xyz):
    if xyz.ndim==1: xyz=xyz[None,:]
    lat=np.arcsin(xyz[:,2]/earth_radius)
    lon=np.arctan2(xyz[:,1],xyz[:,0])
    return np.rad2deg(lat),np.rad2deg(lon)

#Minimization function. 
def minimize(point):
    dist= calc_distance(point)
    #Here you can change the minimization parameter, here the distances
    #from a sphere to a point is divided by its radius for linear weighting.
    err=np.linalg.norm(dist/rad)
    return err

earth_radius = 1
p1 = (0, 0, 1)
p2 = (0, 1, 1)
p3 = (1, 0, 1)
p4 = (0, 0.5, 1)

points = np.vstack((p1,p2,p3,p4))
lat    = points[:,0]
lon    = points[:,1]
rad    = points[:,2]

centers = geo2cart(lat,lon)

out=[]
for x in range(30):
    latrand=np.average(lat/rad)*np.random.rand(1)*np.sum(rad)
    lonrand=np.average(lon/rad)*np.random.rand(1)*np.sum(rad)
    start=geo2cart(latrand,lonrand)
    end_pos=opt.fmin_powell(minimize,start)
    out.append([cart2geo(end_pos),np.linalg.norm(end_pos-geo2cart(36.989,91464))])


out = sorted(out, key=lambda x: x[1])
print 'Latitude:',out[0][0][0],'Longitude:',out[0][0][1],'Distance:',out[0][1]