---
layout: post
title: My Basic (Python) Data Science Setup
---

So, I've been largely silent for a long long time. Thought it was time to do something vaguely useful (and actually talk about it) so I'm tidying up a few meetup sessions I've presented at into a series of Basic Data Science stuff. This is the first one and covers my Python environment, the Jupyternotebook environments I use for analysis, and some  on the Plot.ly graphs and RISE / Reveal.js methods I use to turn those notebooks into presentations. 

This section will be "Light" on the data science, maths, politics and everything else outside of the setup of this wee environment. 

# What to Ass(u)me

* Basic Linux/OSX familiarity
* Basic Programming familiarity in a hybrid language like Python, R, Bash, Go, Rust, Julia, Node.JS, Matlab, etc.
* That when I use the phrases 'High Performance','Large','Big','Parallel', etc, this is in the context of a single, small, machine processing small amounts of interesting derived data. Yes, we can go big, but for now lets start up small... 

# TLDR
* Install [Anaconda](https://www.anaconda.com/download/) Python 3.X
* [_OPTIONAL_] Set up a `conda` environment to play in;
  * `conda create -n datasci`
  * `source activate datasci`
* `conda config --add channels conda-forge`
* `conda install numpy scipy pandas jupyter_nbextensions_configurator nbpresent nbbrowserconf nbbrowserpdf plotly seaborn`



# Full Stack/Monty Python

If you're using something else to do Data Science, [good for you](http://www.kdnuggets.com/2017/08/python-overtakes-r-leader-analytics-data-science.html), but in terms of flexibility, developer/analyst velocity and portability, Python is hard to beat. R still has Python beat in some of the depths of it's Statistics expertise, but IMO Python gets you 99% of the way there.

My environment of choice uses the [Anaconda distribution](https://docs.continuum.io/anaconda/). It's largely pre-built and optimised modules, as well as strong environment maintence capabilites make it hard to beat for exploratory analysis  / product design without the overheads of containerization, the pain of virtualenvs or the mess that comes from `sudo pip install`

I'll skip past the installation instructions since [Anaconda's installation guides are pretty spot on](https://www.anaconda.com/download/), and we'll swing on to some tasty packages.

If you want to keep all your datascience environments tidy, or you just want to minimise cross-bloat, `conda` makes environment creation and management [extremely easy](https://conda.io/docs/user-guide/tasks/manage-environments.html)

```shell
conda create -n datasci
source activate datasci
```

Once the base distribution is installed, it's also worthwhile adding in the [`conda-forge` channel](https://conda-forge.org/), which gives you access to community built and tested versions of most major Python packages (and can be more up to date than Anaconda's pre-built versions)

```shell
conda config --add channels conda-forge
```

## Numpy and Pandas and Scipy, oh, my!

There are a few fundamental challenges in Data Science that can be loosely grouped as:

* Extraction, Collection and Structured Storage of Mixed Value/Format Data
* Slicing, Dicing Grouping and Applying
* Extraction of Meaning/Context

The first two of these are made massively more comfortable with the addition of 3 (large) Python packages; `numpy`,`scipy` and `pandas`. 

`numpy` and `scipy` specialise in highly optimised vector-based computation and processing, allowing the application of single functions across large amounts of data in one go. They're both very tightly integrated with eachother but in general, `numpy` focuses on dense, fast, data storage and iteration, with a certain amount of statistical power under the hood (most of it from `scipy`), and then `scipy` focuses on slightly more 'esoteric' maths from the scientific, engineering and academic fields.

Without a doubt, `pandas` is my favourite Python module; it makes the conversion, collection, normalisation and output of complex datasets a breeze. It's a little bit heavy once you hit a few million rows, but at that point you should be thinking very carefully about what questions you're trying ask (and why you're not using Postgres/Spark/Mongo/Elasticsearch depending on where you are).

So, enough introductions;

```shell
conda install numpy scipy pandas
```

## Drops of Jupyter

While `pandas` is still my favourite module, `jupyter` probably makes the biggest difference in my day to day life. Oftentimes you will either be living in a text editor / IDE and executing those scripts from the command line, or running through a command line interpreter directly like IDLE or ipython. `jupyter` presents a "middle-way" of a block-based approach hosted through a local web server. Go play with it, you'll thank me.

Best of all it is packaged as part of Anaconda's Python distribution.

```shell
jupyter notebook
```

For presentationy stuff later though, I like to add in a few extras

```shell
conda install jupyter_nbextensions_configurator nbpresent nbbrowserconf nbbrowserpdf
```

## Graph all the things

One of the key parts of interrogating and analysing a dataset is visualisation. Python has a pile of fantastic visualisation libraries, with [`matplotlib`](https://matplotlib.org/) being the granddaddy of them all (and is a dependency of most numerical libraries because it's handy as hell). [But that's not our only option by a long shot.](https://wiki.python.org/moin/NumericAndScientific/Plotting)

Personally, I'm a fan of [Seaborn](https://seaborn.pydata.org/tutorial.html) for `pandas` aware static plots, and [Plotly](https://plot.ly/) for generating rich, interactive, shareable visualisations (like [this one](https://plot.ly/~bolster/217), presented with no context)

```shell
conda install plotly seaborn
```

# Conclusion

And that's about it!

I'll try to keep this page updated with "my 'best' practice" setup and workflow. Slap me around if I've messed anything up in these instructions, or to comment on how I'm totally wrong!


