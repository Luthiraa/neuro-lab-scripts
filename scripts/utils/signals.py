def mono(x, v):
    return v[x-1, :]  

def bi(x, y, v):
    return mono(x, v) - mono(y, v)

def tri(x, y, z, v):
    return mono(y, v) - ((mono(x, v) + mono(z, v)) / 2)

def tetra(x, y, z, w, v):
    return tri(x, y, z, v) - tri(y, z, w, v)

def vpp(v):
    return np.max(v) - np.min(v)