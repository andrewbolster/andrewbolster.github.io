---
layout: post
title: Daily Dated Untitled Jupyter Notebooks
date: 2018-09-26 12:29 +0100
tags: python jupyter data notebook
category: hotfix
---

I am a *heavy* user of [Jupyter Notebook](http://jupyter.org/), both personally for wrapping my head around Open Data, professionally for analysis and reporting, and for education/presentations.

So am very comfortable with just spinning up new notebooks all over the show. However, this ends up looking like this...

![](/img/untitled_hell.png)

Less than informative and impossible to work out WTF I was doing. 

Helpfully, there's a way to change it. 

In your `jupyter_notebook_config.py` file ([Normally in `~/.jupyter`](https://jupyter-notebook.readthedocs.io/en/stable/config.html)), add the following somewhere sensible

```python
import datetime #Somewhere near the top 
...
# around line 450, in the ContentsManager section
c.ContentsManager.untitled_notebook = datetime.date.today().strftime("%Y%m%d")
```

Now when you create a new notebook, it'll be pre-named with the date, i.e. '20180926.ipynb'

Note: This date will be the date that the notebook server was *started*, not necessarily the date that the notebook is created. If anyone can think of a clever way of doing that, let me know!
