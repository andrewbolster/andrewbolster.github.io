---
category: ''
description: ''
layout: post
tags:
- 'Data Science'
- Python
- Statistics
- UK
- 'data visualization'
- notebook
title: Data Wrangling for UK Internet Usage
---

This post is a little different from my usual fare;

Basically, there was a tweet from [MATRIX NI](http://matrixni.org) that caught
my eye; the latest Office of National Statistics
[report](http://www.ons.gov.uk/ons/dcp171778_404497.pdf) on Internet Use in the
UK.

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/MATRIX_NI">@MATRIX_NI</a> <a href="https://twitter.com/ONS">@ONS</a> And the tables show Northern Ireland being around 7% behind the Avg and 2% behind the next-worst-region...</p>&mdash; Andrew Bolster (@Bolster) <a href="https://twitter.com/Bolster/status/601689626496135168">May 22, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Basically, NI "lost". So I thought it was a good opportunity to play around with
the data a little bit instead of [my usual
stuff](http://andrewbolster.info/2014/05/so-what-is-it-you-do-again/).

As such this sent me on two main thrusts;

1. Demonstrating a little sample of my normal workflow with data wrangling using
[Python](https://www.python.org/), [Pandas](http://pandas.pydata.org),
[Plot.ly](https://plot.ly/) and a few other tools. This is not clean code and
it's not pretty.
2. NI Sucks at the internet and I believe this statistic is the more realistic,
reliable, and impactful metric to target economic and cultural
growth/stability/recovery/happiness/whatever.

Unfortuately the data massage, both in terms of dealing with the Excel data and then massaging the outputs into something
the blog could safely handle took longer than I'd expected so the follow up will have to wait for another time.

Until then, well, here's some data to play with.



## "Open Data" sucks

When I'm working on something like this, I usually end up spending about 80% of
my time just getting the data into a format that can be used reasonably; Excel
documents are NOT accessible open data standards and they should all go die in a
fire... But this is what we've got.

Lets kick things off with a few 'preambles'.

**In [1]:**

```python
import pandas as pd
import plotly.plotly as py
import statsmodels as sm

from sklearn.linear_model import LinearRegression
import scipy, scipy.stats

import cufflinks as cf # Awesome Pandas/Plot.ly integration module https://github.com/santosjorge/cufflinks

py.sign_in('bolster', 'XXXXXXX')

```

![png](/notebooks/data-wrangling-for-uk-internet-usage_files/data-wrangling-for-uk-internet-usage_2_0.png)



Pandas has the relatively intelligent `read_excel` method that... well... does
what it says on the tin.

Since every gov department appears to use Excel as a formatting and layout tool
rather than a data management platform, there are lots of pointlessly empty rows
and columns that we can drop, so we end up with the top of a data structure like
this.

As you can see, Pandas has "guessed" that the top row is a set of column
headers... this is incorrect...

**In [3]:**

```python
df = pd.read_excel("/home/bolster/Downloads/rftiatables152015q1_tcm77-405031.xls", sheetname="4b")
df=df.dropna(axis=1,how="all")
df=df.dropna(axis=0,how="all")
df.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Table 4B: Recent and lapsed internet users and internet non-users, by geographical location, UK</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 10</th>
      <th>Unnamed: 12</th>
      <th>Unnamed: 13</th>
      <th>Unnamed: 14</th>
      <th>Unnamed: 15</th>
      <th>Unnamed: 16</th>
      <th>Unnamed: 18</th>
      <th>Unnamed: 20</th>
      <th>Unnamed: 21</th>
      <th>Unnamed: 22</th>
      <th>Unnamed: 23</th>
      <th>Unnamed: 24</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> Persons aged 16 years and over</td>
      <td>                       NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>                    NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>        NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>       %</td>
    </tr>
    <tr>
      <th>1</th>
      <td>                            NaN</td>
      <td> Used in the last 3 months</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td> Used over 3 months ago</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td> Never used</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>                            NaN</td>
      <td>                   2013 Q1</td>
      <td> 2014 Q1</td>
      <td> 2014 Q2</td>
      <td> 2014 Q3</td>
      <td> 2014 Q4</td>
      <td> 2015 Q1</td>
      <td>                2013 Q1</td>
      <td> 2014 Q1</td>
      <td> 2014 Q2</td>
      <td> 2014 Q3</td>
      <td> 2014 Q4</td>
      <td> 2015 Q1</td>
      <td>    2013 Q1</td>
      <td> 2014 Q1</td>
      <td> 2014 Q2</td>
      <td> 2014 Q3</td>
      <td> 2014 Q4</td>
      <td> 2015 Q1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>                             UK</td>
      <td>                      83.3</td>
      <td>      85</td>
      <td>    85.6</td>
      <td>    85.8</td>
      <td>      86</td>
      <td>    86.2</td>
      <td>                    2.5</td>
      <td>     2.2</td>
      <td>     2.3</td>
      <td>     2.2</td>
      <td>     2.2</td>
      <td>     2.2</td>
      <td>         14</td>
      <td>    12.6</td>
      <td>      12</td>
      <td>    11.8</td>
      <td>    11.6</td>
      <td>    11.4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>                     North East</td>
      <td>                      79.4</td>
      <td>    81.3</td>
      <td>    81.2</td>
      <td>    81.9</td>
      <td>    80.8</td>
      <td>    81.6</td>
      <td>                    2.6</td>
      <td>     2.4</td>
      <td>     2.9</td>
      <td>     2.5</td>
      <td>     2.5</td>
      <td>     3.6</td>
      <td>       16.8</td>
      <td>    14.3</td>
      <td>    14.1</td>
      <td>    12.9</td>
      <td>    14.1</td>
      <td>      13</td>
    </tr>
  </tbody>
</table>
</div>



Remove pointless rows (Note that the index on the right hand side isn't
automatically updated)

**In [4]:**

```python
df.drop(df.index[[0, -3,-2,-1]], inplace=True)
df.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Table 4B: Recent and lapsed internet users and internet non-users, by geographical location, UK</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 10</th>
      <th>Unnamed: 12</th>
      <th>Unnamed: 13</th>
      <th>Unnamed: 14</th>
      <th>Unnamed: 15</th>
      <th>Unnamed: 16</th>
      <th>Unnamed: 18</th>
      <th>Unnamed: 20</th>
      <th>Unnamed: 21</th>
      <th>Unnamed: 22</th>
      <th>Unnamed: 23</th>
      <th>Unnamed: 24</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>                    NaN</td>
      <td> Used in the last 3 months</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td> Used over 3 months ago</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td> Never used</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
      <td>     NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>                    NaN</td>
      <td>                   2013 Q1</td>
      <td> 2014 Q1</td>
      <td> 2014 Q2</td>
      <td> 2014 Q3</td>
      <td> 2014 Q4</td>
      <td> 2015 Q1</td>
      <td>                2013 Q1</td>
      <td> 2014 Q1</td>
      <td> 2014 Q2</td>
      <td> 2014 Q3</td>
      <td> 2014 Q4</td>
      <td> 2015 Q1</td>
      <td>    2013 Q1</td>
      <td> 2014 Q1</td>
      <td> 2014 Q2</td>
      <td> 2014 Q3</td>
      <td> 2014 Q4</td>
      <td> 2015 Q1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>                     UK</td>
      <td>                      83.3</td>
      <td>      85</td>
      <td>    85.6</td>
      <td>    85.8</td>
      <td>      86</td>
      <td>    86.2</td>
      <td>                    2.5</td>
      <td>     2.2</td>
      <td>     2.3</td>
      <td>     2.2</td>
      <td>     2.2</td>
      <td>     2.2</td>
      <td>         14</td>
      <td>    12.6</td>
      <td>      12</td>
      <td>    11.8</td>
      <td>    11.6</td>
      <td>    11.4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>             North East</td>
      <td>                      79.4</td>
      <td>    81.3</td>
      <td>    81.2</td>
      <td>    81.9</td>
      <td>    80.8</td>
      <td>    81.6</td>
      <td>                    2.6</td>
      <td>     2.4</td>
      <td>     2.9</td>
      <td>     2.5</td>
      <td>     2.5</td>
      <td>     3.6</td>
      <td>       16.8</td>
      <td>    14.3</td>
      <td>    14.1</td>
      <td>    12.9</td>
      <td>    14.1</td>
      <td>      13</td>
    </tr>
    <tr>
      <th>7</th>
      <td> Tees Valley and Durham</td>
      <td>                      78.5</td>
      <td>      81</td>
      <td>    80.3</td>
      <td>    81.4</td>
      <td>    79.6</td>
      <td>    83.5</td>
      <td>                    2.3</td>
      <td>     2.1</td>
      <td>     2.8</td>
      <td>     3.1</td>
      <td>       2</td>
      <td>     2.3</td>
      <td>       16.5</td>
      <td>      13</td>
      <td>    14.2</td>
      <td>      12</td>
      <td>    15.2</td>
      <td>    12.9</td>
    </tr>
  </tbody>
</table>
</div>



Fill in the 'headings' for the "Used in the last" section to wipe out those
NaN's

**In [5]:**

```python
df.iloc[0].fillna(method="ffill", inplace=True)
df.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Table 4B: Recent and lapsed internet users and internet non-users, by geographical location, UK</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 10</th>
      <th>Unnamed: 12</th>
      <th>Unnamed: 13</th>
      <th>Unnamed: 14</th>
      <th>Unnamed: 15</th>
      <th>Unnamed: 16</th>
      <th>Unnamed: 18</th>
      <th>Unnamed: 20</th>
      <th>Unnamed: 21</th>
      <th>Unnamed: 22</th>
      <th>Unnamed: 23</th>
      <th>Unnamed: 24</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>                    NaN</td>
      <td> Used in the last 3 months</td>
      <td> Used in the last 3 months</td>
      <td> Used in the last 3 months</td>
      <td> Used in the last 3 months</td>
      <td> Used in the last 3 months</td>
      <td> Used in the last 3 months</td>
      <td> Used over 3 months ago</td>
      <td> Used over 3 months ago</td>
      <td> Used over 3 months ago</td>
      <td> Used over 3 months ago</td>
      <td> Used over 3 months ago</td>
      <td> Used over 3 months ago</td>
      <td> Never used</td>
      <td> Never used</td>
      <td> Never used</td>
      <td> Never used</td>
      <td> Never used</td>
      <td> Never used</td>
    </tr>
    <tr>
      <th>2</th>
      <td>                    NaN</td>
      <td>                   2013 Q1</td>
      <td>                   2014 Q1</td>
      <td>                   2014 Q2</td>
      <td>                   2014 Q3</td>
      <td>                   2014 Q4</td>
      <td>                   2015 Q1</td>
      <td>                2013 Q1</td>
      <td>                2014 Q1</td>
      <td>                2014 Q2</td>
      <td>                2014 Q3</td>
      <td>                2014 Q4</td>
      <td>                2015 Q1</td>
      <td>    2013 Q1</td>
      <td>    2014 Q1</td>
      <td>    2014 Q2</td>
      <td>    2014 Q3</td>
      <td>    2014 Q4</td>
      <td>    2015 Q1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>                     UK</td>
      <td>                      83.3</td>
      <td>                        85</td>
      <td>                      85.6</td>
      <td>                      85.8</td>
      <td>                        86</td>
      <td>                      86.2</td>
      <td>                    2.5</td>
      <td>                    2.2</td>
      <td>                    2.3</td>
      <td>                    2.2</td>
      <td>                    2.2</td>
      <td>                    2.2</td>
      <td>         14</td>
      <td>       12.6</td>
      <td>         12</td>
      <td>       11.8</td>
      <td>       11.6</td>
      <td>       11.4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>             North East</td>
      <td>                      79.4</td>
      <td>                      81.3</td>
      <td>                      81.2</td>
      <td>                      81.9</td>
      <td>                      80.8</td>
      <td>                      81.6</td>
      <td>                    2.6</td>
      <td>                    2.4</td>
      <td>                    2.9</td>
      <td>                    2.5</td>
      <td>                    2.5</td>
      <td>                    3.6</td>
      <td>       16.8</td>
      <td>       14.3</td>
      <td>       14.1</td>
      <td>       12.9</td>
      <td>       14.1</td>
      <td>         13</td>
    </tr>
    <tr>
      <th>7</th>
      <td> Tees Valley and Durham</td>
      <td>                      78.5</td>
      <td>                        81</td>
      <td>                      80.3</td>
      <td>                      81.4</td>
      <td>                      79.6</td>
      <td>                      83.5</td>
      <td>                    2.3</td>
      <td>                    2.1</td>
      <td>                    2.8</td>
      <td>                    3.1</td>
      <td>                      2</td>
      <td>                    2.3</td>
      <td>       16.5</td>
      <td>         13</td>
      <td>       14.2</td>
      <td>         12</td>
      <td>       15.2</td>
      <td>       12.9</td>
    </tr>
  </tbody>
</table>
</div>



This ones a bit complicated so we'll split it up; first off transpose the frame
(rows become columns, etc), and then set the new column headers to be the row
currently containing the region names. Then drop that row since we don't need it
any more, and finally update the columns to give the first two columns useful
names.

**In [6]:**

```python
df = df.T
df.columns = df.iloc[0]
df.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Table 4B: Recent and lapsed internet users and internet non-users, by geographical location, UK</th>
      <th>nan</th>
      <th>nan</th>
      <th>UK</th>
      <th>North East</th>
      <th>Tees Valley and Durham</th>
      <th>Northumberland and Tyne and Wear</th>
      <th>North West</th>
      <th>Cumbria</th>
      <th>Cheshire</th>
      <th>Greater Manchester</th>
      <th>...</th>
      <th>Devon</th>
      <th>Wales</th>
      <th>West Wales and the Valleys</th>
      <th>East Wales</th>
      <th>Scotland</th>
      <th>North Eastern Scotland</th>
      <th>Eastern Scotland</th>
      <th>South Western Scotland</th>
      <th>Highlands and Islands</th>
      <th>Northern Ireland</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Table 4B: Recent and lapsed internet users and internet non-users, by geographical location, UK</th>
      <td>                       NaN</td>
      <td>     NaN</td>
      <td>   UK</td>
      <td> North East</td>
      <td> Tees Valley and Durham</td>
      <td> Northumberland and Tyne and Wear</td>
      <td> North West</td>
      <td> Cumbria</td>
      <td> Cheshire</td>
      <td> Greater Manchester</td>
      <td>...</td>
      <td> Devon</td>
      <td> Wales</td>
      <td> West Wales and the Valleys</td>
      <td> East Wales</td>
      <td> Scotland</td>
      <td> North Eastern Scotland</td>
      <td> Eastern Scotland</td>
      <td> South Western Scotland</td>
      <td> Highlands and Islands</td>
      <td> Northern Ireland</td>
    </tr>
    <tr>
      <th>Unnamed: 2</th>
      <td> Used in the last 3 months</td>
      <td> 2013 Q1</td>
      <td> 83.3</td>
      <td>       79.4</td>
      <td>                   78.5</td>
      <td>                             80.1</td>
      <td>       81.9</td>
      <td>      79</td>
      <td>     84.1</td>
      <td>               83.5</td>
      <td>...</td>
      <td>  83.8</td>
      <td>  79.1</td>
      <td>                       76.8</td>
      <td>       83.1</td>
      <td>     82.6</td>
      <td>                   83.8</td>
      <td>             84.9</td>
      <td>                   80.6</td>
      <td>                  80.5</td>
      <td>             77.3</td>
    </tr>
    <tr>
      <th>Unnamed: 4</th>
      <td> Used in the last 3 months</td>
      <td> 2014 Q1</td>
      <td>   85</td>
      <td>       81.3</td>
      <td>                     81</td>
      <td>                             81.5</td>
      <td>       83.7</td>
      <td>    84.9</td>
      <td>     85.4</td>
      <td>                 85</td>
      <td>...</td>
      <td>  83.9</td>
      <td>  81.7</td>
      <td>                       79.4</td>
      <td>       85.4</td>
      <td>     85.1</td>
      <td>                   89.2</td>
      <td>             87.1</td>
      <td>                   82.2</td>
      <td>                    86</td>
      <td>             77.4</td>
    </tr>
    <tr>
      <th>Unnamed: 5</th>
      <td> Used in the last 3 months</td>
      <td> 2014 Q2</td>
      <td> 85.6</td>
      <td>       81.2</td>
      <td>                   80.3</td>
      <td>                               82</td>
      <td>       84.1</td>
      <td>    82.5</td>
      <td>     85.5</td>
      <td>                 86</td>
      <td>...</td>
      <td>  83.1</td>
      <td>  81.8</td>
      <td>                       80.4</td>
      <td>         84</td>
      <td>     85.1</td>
      <td>                   89.3</td>
      <td>             86.7</td>
      <td>                   82.3</td>
      <td>                  87.9</td>
      <td>               79</td>
    </tr>
    <tr>
      <th>Unnamed: 6</th>
      <td> Used in the last 3 months</td>
      <td> 2014 Q3</td>
      <td> 85.8</td>
      <td>       81.9</td>
      <td>                   81.4</td>
      <td>                             82.3</td>
      <td>       84.5</td>
      <td>      80</td>
      <td>     86.9</td>
      <td>               86.1</td>
      <td>...</td>
      <td>  85.2</td>
      <td>  82.8</td>
      <td>                       81.7</td>
      <td>       84.6</td>
      <td>     85.1</td>
      <td>                   87.7</td>
      <td>             87.6</td>
      <td>                   83.3</td>
      <td>                  79.1</td>
      <td>             78.3</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 51 columns</p>
</div>



**In [7]:**

```python
df.drop(df.index[[0]], inplace=True)
df.columns = ["Internet Use","Date"] + [s.strip() for s in df.columns[2:].tolist()] # Some idiots put spaces at the end of their cells
df.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Internet Use</th>
      <th>Date</th>
      <th>UK</th>
      <th>North East</th>
      <th>Tees Valley and Durham</th>
      <th>Northumberland and Tyne and Wear</th>
      <th>North West</th>
      <th>Cumbria</th>
      <th>Cheshire</th>
      <th>Greater Manchester</th>
      <th>...</th>
      <th>Devon</th>
      <th>Wales</th>
      <th>West Wales and the Valleys</th>
      <th>East Wales</th>
      <th>Scotland</th>
      <th>North Eastern Scotland</th>
      <th>Eastern Scotland</th>
      <th>South Western Scotland</th>
      <th>Highlands and Islands</th>
      <th>Northern Ireland</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Unnamed: 2</th>
      <td> Used in the last 3 months</td>
      <td> 2013 Q1</td>
      <td> 83.3</td>
      <td> 79.4</td>
      <td> 78.5</td>
      <td> 80.1</td>
      <td> 81.9</td>
      <td>   79</td>
      <td> 84.1</td>
      <td> 83.5</td>
      <td>...</td>
      <td> 83.8</td>
      <td> 79.1</td>
      <td> 76.8</td>
      <td> 83.1</td>
      <td> 82.6</td>
      <td> 83.8</td>
      <td> 84.9</td>
      <td> 80.6</td>
      <td> 80.5</td>
      <td> 77.3</td>
    </tr>
    <tr>
      <th>Unnamed: 4</th>
      <td> Used in the last 3 months</td>
      <td> 2014 Q1</td>
      <td>   85</td>
      <td> 81.3</td>
      <td>   81</td>
      <td> 81.5</td>
      <td> 83.7</td>
      <td> 84.9</td>
      <td> 85.4</td>
      <td>   85</td>
      <td>...</td>
      <td> 83.9</td>
      <td> 81.7</td>
      <td> 79.4</td>
      <td> 85.4</td>
      <td> 85.1</td>
      <td> 89.2</td>
      <td> 87.1</td>
      <td> 82.2</td>
      <td>   86</td>
      <td> 77.4</td>
    </tr>
    <tr>
      <th>Unnamed: 5</th>
      <td> Used in the last 3 months</td>
      <td> 2014 Q2</td>
      <td> 85.6</td>
      <td> 81.2</td>
      <td> 80.3</td>
      <td>   82</td>
      <td> 84.1</td>
      <td> 82.5</td>
      <td> 85.5</td>
      <td>   86</td>
      <td>...</td>
      <td> 83.1</td>
      <td> 81.8</td>
      <td> 80.4</td>
      <td>   84</td>
      <td> 85.1</td>
      <td> 89.3</td>
      <td> 86.7</td>
      <td> 82.3</td>
      <td> 87.9</td>
      <td>   79</td>
    </tr>
    <tr>
      <th>Unnamed: 6</th>
      <td> Used in the last 3 months</td>
      <td> 2014 Q3</td>
      <td> 85.8</td>
      <td> 81.9</td>
      <td> 81.4</td>
      <td> 82.3</td>
      <td> 84.5</td>
      <td>   80</td>
      <td> 86.9</td>
      <td> 86.1</td>
      <td>...</td>
      <td> 85.2</td>
      <td> 82.8</td>
      <td> 81.7</td>
      <td> 84.6</td>
      <td> 85.1</td>
      <td> 87.7</td>
      <td> 87.6</td>
      <td> 83.3</td>
      <td> 79.1</td>
      <td> 78.3</td>
    </tr>
    <tr>
      <th>Unnamed: 7</th>
      <td> Used in the last 3 months</td>
      <td> 2014 Q4</td>
      <td>   86</td>
      <td> 80.8</td>
      <td> 79.6</td>
      <td> 81.7</td>
      <td> 85.1</td>
      <td> 80.4</td>
      <td> 86.5</td>
      <td> 86.4</td>
      <td>...</td>
      <td> 82.6</td>
      <td> 82.1</td>
      <td>   81</td>
      <td>   84</td>
      <td> 84.8</td>
      <td> 87.9</td>
      <td> 86.2</td>
      <td> 83.3</td>
      <td> 82.7</td>
      <td> 78.1</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 51 columns</p>
</div>



**In [8]:**

```python
q_map = {"Q1":"March","Q2":"June","Q3":"September","Q4":"December"}
def _yr_q_parse(yq): return yq[0], q_map[yq[1]]
def _yr_q_join(s): return " ".join(_yr_q_parse(s.split(" ")))
df['Date'] = pd.to_datetime(df['Date'].apply(_yr_q_join))
```

Finally, set the Date to be the primary index (i.e. the row identifier), convert
all the values from boring "objects" to "floats", give the column range a name
(for when we're manipulating the data later), and for play, lets just look at
the average internet use statistics between 2013 and 2015

**In [9]:**

```python
df.set_index(['Date','Internet Use'],inplace=True)
df.sortlevel(inplace=True)
df=df.astype(float)
df.columns.name="Region"
df.groupby(level='Internet Use').mean().T
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Internet Use</th>
      <th>Never used</th>
      <th>Used in the last 3 months</th>
      <th>Used over 3 months ago</th>
    </tr>
    <tr>
      <th>Region</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>UK</th>
      <td> 12.233333</td>
      <td> 85.316667</td>
      <td> 2.266667</td>
    </tr>
    <tr>
      <th>North East</th>
      <td> 14.200000</td>
      <td> 81.033333</td>
      <td> 2.750000</td>
    </tr>
    <tr>
      <th>Tees Valley and Durham</th>
      <td> 13.966667</td>
      <td> 80.716667</td>
      <td> 2.433333</td>
    </tr>
    <tr>
      <th>Northumberland and Tyne and Wear</th>
      <td> 14.383333</td>
      <td> 81.266667</td>
      <td> 2.983333</td>
    </tr>
    <tr>
      <th>North West</th>
      <td> 13.250000</td>
      <td> 83.950000</td>
      <td> 2.666667</td>
    </tr>
    <tr>
      <th>Cumbria</th>
      <td> 15.433333</td>
      <td> 82.216667</td>
      <td> 2.200000</td>
    </tr>
    <tr>
      <th>Cheshire</th>
      <td> 11.550000</td>
      <td> 86.050000</td>
      <td> 2.316667</td>
    </tr>
    <tr>
      <th>Greater Manchester</th>
      <td> 12.050000</td>
      <td> 85.316667</td>
      <td> 2.483333</td>
    </tr>
    <tr>
      <th>Lancashire</th>
      <td> 13.066667</td>
      <td> 83.783333</td>
      <td> 3.050000</td>
    </tr>
    <tr>
      <th>Merseyside</th>
      <td> 16.383333</td>
      <td> 80.483333</td>
      <td> 3.016667</td>
    </tr>
    <tr>
      <th>Yorkshire and the Humber</th>
      <td> 13.416667</td>
      <td> 84.033333</td>
      <td> 2.383333</td>
    </tr>
    <tr>
      <th>East Yorkshire and Northern Lincolnshire</th>
      <td> 13.916667</td>
      <td> 83.416667</td>
      <td> 2.616667</td>
    </tr>
    <tr>
      <th>North Yorkshire</th>
      <td> 11.216667</td>
      <td> 86.483333</td>
      <td> 1.900000</td>
    </tr>
    <tr>
      <th>South Yorkshire</th>
      <td> 15.250000</td>
      <td> 82.116667</td>
      <td> 2.416667</td>
    </tr>
    <tr>
      <th>West Yorkshire</th>
      <td> 12.916667</td>
      <td> 84.533333</td>
      <td> 2.400000</td>
    </tr>
    <tr>
      <th>East Midlands</th>
      <td> 12.783333</td>
      <td> 84.366667</td>
      <td> 2.733333</td>
    </tr>
    <tr>
      <th>Derbyshire and Nottinghamshire</th>
      <td> 12.916667</td>
      <td> 83.833333</td>
      <td> 3.083333</td>
    </tr>
    <tr>
      <th>Leicestershire, Rutland and Northamptonshire</th>
      <td> 11.633333</td>
      <td> 85.750000</td>
      <td> 2.516667</td>
    </tr>
    <tr>
      <th>Lincolnshire</th>
      <td> 14.933333</td>
      <td> 82.666667</td>
      <td> 2.166667</td>
    </tr>
    <tr>
      <th>West Midlands</th>
      <td> 14.450000</td>
      <td> 82.916667</td>
      <td> 2.483333</td>
    </tr>
    <tr>
      <th>Herefordshire, Worcestershire and Warwickshire</th>
      <td> 12.083333</td>
      <td> 85.050000</td>
      <td> 2.600000</td>
    </tr>
    <tr>
      <th>Shropshire and Staffordshire</th>
      <td> 13.350000</td>
      <td> 84.316667</td>
      <td> 2.266667</td>
    </tr>
    <tr>
      <th>West Midlands</th>
      <td> 16.266667</td>
      <td> 81.116667</td>
      <td> 2.550000</td>
    </tr>
    <tr>
      <th>East of England</th>
      <td> 10.900000</td>
      <td> 86.900000</td>
      <td> 2.100000</td>
    </tr>
    <tr>
      <th>East Anglia</th>
      <td> 12.133333</td>
      <td> 85.400000</td>
      <td> 2.383333</td>
    </tr>
    <tr>
      <th>Bedfordshire and Hertfordshire</th>
      <td>  8.916667</td>
      <td> 89.216667</td>
      <td> 1.850000</td>
    </tr>
    <tr>
      <th>Essex</th>
      <td> 11.216667</td>
      <td> 86.716667</td>
      <td> 1.950000</td>
    </tr>
    <tr>
      <th>London</th>
      <td>  9.116667</td>
      <td> 88.950000</td>
      <td> 1.816667</td>
    </tr>
    <tr>
      <th>Inner London</th>
      <td>  8.000000</td>
      <td> 90.083333</td>
      <td> 1.650000</td>
    </tr>
    <tr>
      <th>Outer London</th>
      <td>  9.850000</td>
      <td> 88.150000</td>
      <td> 1.933333</td>
    </tr>
    <tr>
      <th>South East</th>
      <td>  9.450000</td>
      <td> 88.600000</td>
      <td> 1.916667</td>
    </tr>
    <tr>
      <th>Berkshire, Buckinghamshire and Oxfordshire</th>
      <td>  7.700000</td>
      <td> 90.566667</td>
      <td> 1.700000</td>
    </tr>
    <tr>
      <th>Surrey, East and West Sussex</th>
      <td>  9.100000</td>
      <td> 88.916667</td>
      <td> 1.900000</td>
    </tr>
    <tr>
      <th>Hampshire and Isle of Wight</th>
      <td> 10.516667</td>
      <td> 87.683333</td>
      <td> 1.716667</td>
    </tr>
    <tr>
      <th>Kent</th>
      <td> 11.183333</td>
      <td> 86.466667</td>
      <td> 2.333333</td>
    </tr>
    <tr>
      <th>South West</th>
      <td> 11.500000</td>
      <td> 86.100000</td>
      <td> 2.333333</td>
    </tr>
    <tr>
      <th>Gloucestershire, Wiltshire and Bristol/Bath area</th>
      <td> 10.016667</td>
      <td> 88.050000</td>
      <td> 1.883333</td>
    </tr>
    <tr>
      <th>Dorset and Somerset</th>
      <td> 11.333333</td>
      <td> 85.900000</td>
      <td> 2.616667</td>
    </tr>
    <tr>
      <th>Cornwall and Isles of Scilly</th>
      <td> 13.966667</td>
      <td> 82.566667</td>
      <td> 3.466667</td>
    </tr>
    <tr>
      <th>Devon</th>
      <td> 13.566667</td>
      <td> 84.116667</td>
      <td> 2.283333</td>
    </tr>
    <tr>
      <th>Wales</th>
      <td> 15.333333</td>
      <td> 81.666667</td>
      <td> 2.816667</td>
    </tr>
    <tr>
      <th>West Wales and the Valleys</th>
      <td> 16.800000</td>
      <td> 79.983333</td>
      <td> 3.000000</td>
    </tr>
    <tr>
      <th>East Wales</th>
      <td> 12.850000</td>
      <td> 84.450000</td>
      <td> 2.500000</td>
    </tr>
    <tr>
      <th>Scotland</th>
      <td> 13.033333</td>
      <td> 84.683333</td>
      <td> 2.183333</td>
    </tr>
    <tr>
      <th>North Eastern Scotland</th>
      <td> 10.183333</td>
      <td> 88.050000</td>
      <td> 1.733333</td>
    </tr>
    <tr>
      <th>Eastern Scotland</th>
      <td> 11.350000</td>
      <td> 86.533333</td>
      <td> 2.016667</td>
    </tr>
    <tr>
      <th>South Western Scotland</th>
      <td> 14.933333</td>
      <td> 82.550000</td>
      <td> 2.400000</td>
    </tr>
    <tr>
      <th>Highlands and Islands</th>
      <td> 14.500000</td>
      <td> 83.050000</td>
      <td> 2.416667</td>
    </tr>
    <tr>
      <th>Northern Ireland</th>
      <td> 19.666667</td>
      <td> 78.283333</td>
      <td> 1.816667</td>
    </tr>
  </tbody>
</table>
</div>



Now that everythings tidy, we can start to play.

First thing to have a look at is the regional breakdown, so we select the
Regional records and make a fresh dataframe just with those values. We can also
forget about the "Used in the last 3 months" records because they're not
particularly interesting and make the graphs look weird...

As you can see, there are two "West Midlands"; this is a pain, as one is the
'Region' and the other is to [NUTS level 2](http://www.ons.gov.uk/ons/guide-
method/geography/beginner-s-guide/eurostat/index.html) Region, obviously.... So
we drop the local authority region. This was not as easy as I expected to do
programmatically, and if someone has a cleverer way to do this, lemme know.

**In [10]:**

```python
def last_index_of(li, val):
    return (len(li) - 1) - li[::-1].index(val)

def non_dup_indexes_of_columns(df, dupkey):
    col_ids = range(len(df.columns.tolist()))
    col_ids.remove(last_index_of(df.columns.tolist(),dupkey))
    return col_ids


regions = ["UK",
           "North East","North West",
           "Yorkshire and the Humber",
           "East Midlands", "West Midlands",
           "East of England", "London",
           "South East", "South West",
           "Wales", "Scotland",
           "Northern Ireland"
]

df_regional_use = df[regions]
df_regional_use = df_regional_use[non_dup_indexes_of_columns(df_regional_use,"West Midlands")]# Dammit West Midlands...
```

Now we can plot the regional internet uses using Plot.ly, meaning that these
graphs both look good in my IPython Notebook where I'm editing this, and
hopefully on the blog when this goes up....

**In [11]:**

```python
df_regional_use_means = df_regional_use.groupby(level='Internet Use').mean().T

cols = ['Never used','Used over 3 months ago']

df_regional_use_means[cols].sort(columns=cols).iplot(kind="bar",
    filename='Internet Region Use Means Bar',world_readable=True, theme="pearl",
    title="Average Digital Illiteracy by Region (2013-2015)", xTitle="Region", yTitle="%")
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~bolster/49.embed" height="525" width="100%"></iframe>



Now that doesn't look too good; Northern Ireland has the highest proportion of
"Never Used", at just below 20%.

"But!" you might say, "What about all the great programs and processes put in
place recently? We're rapidly recovering from a troubles, and we're on the up
and up!"

Alright then, lets look at the standard deviation of these results (i.e. the
volativility)

**In [12]:**

```python
df_regional_use_stddevs = df_regional_use.groupby(level='Internet Use').std().T

df_regional_use_stddevs[cols].sort(columns=cols).iplot(kind="bar",
    filename='Internet Region Use Std Bar',world_readable=True, theme="pearl",
    title="Standard Deviation in UK Digital Illiteracy since 2013", xTitle="Period", yTitle="Std Dev (Variability)")
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~bolster/50.embed" height="525" width="100%"></iframe>



Nope, we still suck. So we've got the highest amount of "Digital Illiteracy" and
the lowest change in Digital Literacy of any region. Lets take a look at that;
std dev is a terrible measure for time series data and doesn't give a reliable
sense of 'trend'

**In [13]:**

```python
df_regional_never = df_regional_use.xs("Never used", level="Internet Use")
df_regional_never_pct_change = ((df_regional_never/df_regional_never.iloc[0])-1)

#fig,ax = my_chart_factory()

#df_regional_never_pct_change.plot(ax=ax, legend=False, color=tableau20)
df_regional_never_pct_change.iplot(filename='Internet Region Never Pct Change',world_readable=True, theme="pearl",
                                   title="Reduction in UK Digital Illiteracy since 2013",
                                   xTitle="Period", yTitle="%")
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~bolster/48.embed" height="525" width="100%"></iframe>



Remember this is the number of people who said that they *never* use the
internet...

Ok that's a nice interactive graph that you can poke around with, but it's very
noisy.... Lets see if we can clean that up a bit with a [Hodrick-Prescott
filter](http://en.wikipedia.org/wiki/Hodrick%E2%80%93Prescott_filter) (we could
have just done a linear regression but that's not really that interesting.

**In [25]:**

```python
cycle,trend = sm.tsa.filters.hp_filter.hpfilter(df_regional_never_pct_change)

trend.iplot(filename='Internet Region Never Pct Change Reg',world_readable=True, theme="pearl",
                                   title="Reduction in UK Digital Illiteracy since 2013",
                                   xTitle="Period", yTitle="%")
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~bolster/52.embed" height="525" width="100%"></iframe>



Note that because of the big gap at the beginning of the data (i.e. there's no
information between Q1 2013 and Q1 2014), the regression has a kink in it.
Looking at the results, and the "knee" in the data, it's highly likely that this
is just a mistake in the accounting and that it's actually 2013 Q4 data.

Either way, Northern Ireland is not only bottom of the Digital Literacy Table,
but it's also accomplished the least progress in this area of any region across
the UK.

# Why worry about Digital Illiteracy?

I'll save that particular rant for another time...
