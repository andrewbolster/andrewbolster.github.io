---
date: 2024-01-17 13:50 +0000
layout: post
tags:
- Kernel Management
- JupyterLab
- Environment Setup
- conda
- Notebook
- Python
title: Jupyter Environment Management for Dummies
---

This is another one of those "I kept googling the same thing over and over again" things that needed a post, except this time I made an [issue to make a post](https://github.com/andrewbolster/andrewbolster.github.io/issues/8) and then started to repeatedly refer to that.

## TL;DR

When you want to spin up an experimental environment and get it tied in to your Jupyter environment of choice (I actually quite like [JupyterLab Desktop these days...](https://github.com/jupyterlab/jupyterlab-desktop)), you need two steps.

```bash
# Create the conda environment with $NAME and ipykernel as the main dependency
conda create --name $NAME ipykernel && conda activate

# Once you're in the new environment, add it to the _global_ (There may be a better `kernelspec` way to do this but I haven't done it yet.)
ipython kernel install --name=$CONDA_DEFAULT_ENV --user

... Do real work here ...

# If you messed up and need to nuke it from orbit without wiping out the rest of your env;
jupyter kernelspec uninstall $NAME
```

BTW it can sometimes take a few minutes/interactions to coax Jupyterlab into identifying the new kernel.

## Aside on Kernel Names

There's also a trick to getting the current kernel name in a Notebook that doesn't abuse any magic functions

```py
import sys
import os
kernel_name = os.path.basename(sys.executable.replace("/bin/python",""))
```

But what _does_ abuse the magic string is then using that in-kernel python variable to do the _out_ of kernel invocation of the 'correct' install incantation;

**Reminder**:
* `!command` runs the command in shell of the jupyterlab runner (so you _can_ install jupyter extensions etc from a running notebook.)
  * e.g. `!which python` which give you the system python of the runtime the _jupyterlab runner_ is executing in, not the notebook kernel
* `%command` are a small subset of [magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html) for interacting with the _notebook_ kernel
  * e,g. `%conda install -y -q <requirement>` or `%pip install -yq <requirement>` **DON'T COPY PASTE THESE YET**

_However_ some environment setups (particularly `conda` related ones) cause a bit of mayhem, so for instance when you run the magic of `%conda env list`, you may get a response back that has a * beside the 'base' environment, which is a bit wrong coming from a notebook we just created above.

To be _sure_ that you're actually installing things in the right environment, this works;

```py
import sys
import os
kernel_name = os.path.basename(sys.executable.replace("/bin/python",""))
```

```py
%conda install -y -n $kernel_name magicalpackagenamethatsdefinitelynotahallucination
```
