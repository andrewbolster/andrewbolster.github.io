---
aliases:
- /2014/04/generating-a-unit-3-vector-in-python-uniform-spherical-projection/
- /2014/04/generating-a-unit-3-vector-in-python-uniform-spherical-projection.html
cover:
  image: img/generating-a-unit-3-vector-in-python-uniform-spherical-projection.generated.png
date: 2014-04-09 00:00:00+00:00
tags:
- NumPy
- Python
title: Generating a unit 3 vector in Python (Uniform Spherical Projection)
---
Quick one more as a reminder to me than anything else.

As part of my PhD work I'm building different behaviours for virtual submarines. I'll be explaining some parts of my work in a separate post, but basically, I needed to random walk. Random walk in 2 dimensions is easy; pick two random numbers, go that way. Unfortunately [doesn't work that way on a spherical surface](http://hbfs.wordpress.com/2010/10/12/random-points-on-a-sphere-generating-random-sequences-iii/)

So to make things easier, I stole [this StackOverflow answer from dmckee](http://stackoverflow.com/a/5408843/252556) and tidied it up a bit for my purposes. (Assuming everyone else is like me and does `import numpy as np`)

```python
def random_three_vector():
    """
    Generates a random 3D unit vector (direction) with a uniform spherical distribution
    Algo from http://stackoverflow.com/questions/5408276/python-uniform-spherical-distribution
    :return:
    """
    phi = np.random.uniform(0,np.pi*2)
    costheta = np.random.uniform(-1,1)

    theta = np.arccos( costheta )
    x = np.sin( theta) * np.cos( phi )
    y = np.sin( theta) * np.sin( phi )
    z = np.cos( theta )
    return (x,y,z)

# Example IPython code to test the uniformity of the distribution
from pylab import scatter
threetups = []
for _ in range(1000):
    threetups.append(random_three_vector())
zipped = zip(*threetups)
scatter(*zipped[0:2])
```
