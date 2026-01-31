---
date: 2023-05-18T14:43:00+01:00
layout: post
categories: [Data Science, Politics]
tags:
- Elections
- Google Sheets
- Data Visualization
- Web Development
- Data Analysis
- Python
- Northern Ireland
- democracy
- civic data
title: Pulling Election Count data out of Google Sheets for fun and democracy
---

# Messing around with Elections NI data

Sources:

* [Live Data (for 2023)](https://docs.google.com/spreadsheets/d/11o0rbI-NVcPJhkBZxInN4qn55rm0TCJT9ERitaiN1fk/edit?usp=sharing)
* [2022 Assembly Elections](https://docs.google.com/spreadsheets/d/1AazeIZwfflJJoTiYNil3RprIOXcNy8yyzfZ4ImVlETA/edit#gid=264660014)


## Creating your own Google Sheet and referencing the crowdsourced data

The above linked spreadsheets are naturally not editable by everyone; this is great for reliable data but isn't so great when you want to make pretty graphs.

Google Sheets supports the live referencing of external sheets in your own sheets, so you can 'import' the data from the read-only sheets as they evolve over the count, and then reference those data in your own visualisations.

This is done using the [IMPORTRANGE](https://support.google.com/docs/answer/3093340?hl=en&ref_topic=9199554&sjid=4812370886125323989-EU) function in Google Sheets, so like this;

`=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1AazeIZwfflJJoTiYNil3RprIOXcNy8yyzfZ4ImVlETA/edit#gid=372848906","Belfast South/West!A2:Q24")`

![Image of Imported Spreadsheet showing separated results for the Belfast South Assembly Election in 2022](/img/eni_sheet_1.png)

Using this and the [Google QUERY language](https://support.google.com/docs/answer/3093343?hl=en), you can easily create some pretty dynamic graphs in a couple of lines/cells across your own sheets, all while being 'fed' by the main collaborative work.

![Image of PieChart of First Preference Votes in Belfast South in 2022](/img/eni_sheet_2.png)

For instance, this is generated from the following formula;

`=query('Basic IMPORTRANGE'!A2:Q16, "select B, sum(C) group by B order by sum(C) desc")`;

In this case the first argument to the `query` is a reference to my own sheet that just has 'IMPORTRANGE' in it; the interesting bit is the second argument which gives a list of the values in column B (The Party Names in the count sheet) sorted by the sum of the matching rows in column C (the first preference votes), with that 'sum' being defined across the groups with the same values in column B, and finally, these all sorted in a descending fashion by the total of those first preference votes.

So now we've easily set up a aggregation with two 'cells' of formula and a fairly basic chart.

## Doing the real work with Python

Python is really powerful for this kind of stuff, particularly the `pandas` data management library; we can get the above referenced sheet into a 'raw' python format with just a 'few lines of code'.


```python
import pandas as pd
from urllib.parse import quote

sheet_id = "1AazeIZwfflJJoTiYNil3RprIOXcNy8yyzfZ4ImVlETA" # This is the bit taken from the URL above, like IMPORTRANGE above
tab_id = 372848906
# https://docs.google.com/spreadsheets/d/1AazeIZwfflJJoTiYNil3RprIOXcNy8yyzfZ4ImVlETA/edit#gid=372848906

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={tab_id}"
pd.read_csv(url)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>...</th>
      <th>Unnamed: 17</th>
      <th>Unnamed: 18</th>
      <th>Unnamed: 19</th>
      <th>Unnamed: 20</th>
      <th>Unnamed: 21</th>
      <th>Unnamed: 22</th>
      <th>Unnamed: 23</th>
      <th>Unnamed: 24</th>
      <th>Unnamed: 25</th>
      <th>Unnamed: 26</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Belfast South</td>
      <td>NaN</td>
      <td>Stage 1</td>
      <td>Surplus Hargey</td>
      <td>2.00</td>
      <td>Exclude &lt;500</td>
      <td>3.00</td>
      <td>Exclude McCann Sibanda</td>
      <td>4.00</td>
      <td>Exclude Girvin</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11.00</td>
      <td>12.0</td>
      <td>13.0</td>
      <td>14.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Deirdre Hargey</td>
      <td>Sinn Féin</td>
      <td>9511</td>
      <td>-1687</td>
      <td>7824.00</td>
      <td>NaN</td>
      <td>7824.00</td>
      <td>NaN</td>
      <td>7824.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Edwin Poots</td>
      <td>Democratic Unionist Party</td>
      <td>7211</td>
      <td>6.12</td>
      <td>7217.12</td>
      <td>6.08</td>
      <td>7223.20</td>
      <td>117.72</td>
      <td>7340.92</td>
      <td>1134</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Matthew O'Toole</td>
      <td>Social Democratic and Labour Party</td>
      <td>5394</td>
      <td>664.92</td>
      <td>6058.92</td>
      <td>68.18</td>
      <td>6127.10</td>
      <td>322.04</td>
      <td>6449.14</td>
      <td>10.18</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paula Bradshaw</td>
      <td>Alliance Party</td>
      <td>6503</td>
      <td>265.14</td>
      <td>6768.14</td>
      <td>59.5</td>
      <td>6827.64</td>
      <td>135.82</td>
      <td>6963.46</td>
      <td>31</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kate Nicholl</td>
      <td>Alliance Party</td>
      <td>5201</td>
      <td>145.98</td>
      <td>5346.98</td>
      <td>57.52</td>
      <td>5404.50</td>
      <td>131.28</td>
      <td>5535.78</td>
      <td>17</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Clare Bailey</td>
      <td>Green Party</td>
      <td>4058</td>
      <td>167.4</td>
      <td>4225.40</td>
      <td>169.82</td>
      <td>4395.22</td>
      <td>490.54</td>
      <td>4885.76</td>
      <td>48.36</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Stephen McCarthy</td>
      <td>Ulster Unionist Party</td>
      <td>3061</td>
      <td>6.12</td>
      <td>3067.12</td>
      <td>17.72</td>
      <td>3084.84</td>
      <td>25.18</td>
      <td>3110.02</td>
      <td>643.36</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Elsie Trainor</td>
      <td>Social Democratic and Labour Party</td>
      <td>2030</td>
      <td>181.8</td>
      <td>2211.80</td>
      <td>18.52</td>
      <td>2230.32</td>
      <td>132.94</td>
      <td>2363.26</td>
      <td>4</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Andrew Girvin</td>
      <td>Traditional Unionist Voice</td>
      <td>1935</td>
      <td>0.36</td>
      <td>1935.36</td>
      <td>9</td>
      <td>1944.36</td>
      <td>35.54</td>
      <td>1979.90</td>
      <td>-1979.9</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Luke McCann</td>
      <td>Aontú</td>
      <td>806</td>
      <td>70.92</td>
      <td>876.92</td>
      <td>15.16</td>
      <td>892.08</td>
      <td>-892.08</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Sipho Sibanda</td>
      <td>People Before Profit</td>
      <td>629</td>
      <td>40.5</td>
      <td>669.50</td>
      <td>172.66</td>
      <td>842.16</td>
      <td>-842.16</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Neil Moore</td>
      <td>Socialist Party</td>
      <td>353</td>
      <td>18</td>
      <td>371.00</td>
      <td>-371</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Paddy Lynn</td>
      <td>The Workers Party</td>
      <td>139</td>
      <td>24.48</td>
      <td>163.48</td>
      <td>-163.48</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Elly Odhiambo</td>
      <td>Independent</td>
      <td>107</td>
      <td>6.84</td>
      <td>113.84</td>
      <td>-113.84</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Exhausted</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>88.42</td>
      <td>88.42</td>
      <td>54.16</td>
      <td>142.58</td>
      <td>343.18</td>
      <td>485.76</td>
      <td>92</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Eligible Voters</td>
      <td>73497</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Turnout</td>
      <td>47306</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>% Turnout</td>
      <td>64.36%</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Valid Ballots</td>
      <td>46938</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>invalid ballots</td>
      <td>368</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>quota</td>
      <td>7824</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Belfast West</td>
      <td>NaN</td>
      <td>Stage 1</td>
      <td>Surplus Baker</td>
      <td>2.00</td>
      <td>Exclude Hill Mallon</td>
      <td>3.00</td>
      <td>Exclude Crossan</td>
      <td>4.00</td>
      <td>Exclude Burns</td>
      <td>...</td>
      <td>Exclude Doran</td>
      <td>9.00</td>
      <td>Exclude Murphy Higgins</td>
      <td>10.00</td>
      <td>Exclude Doherty</td>
      <td>11.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Danny Baker</td>
      <td>Sinn Féin</td>
      <td>9011</td>
      <td>-1733</td>
      <td>7278.00</td>
      <td>NaN</td>
      <td>7278.00</td>
      <td>NaN</td>
      <td>7278.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>7278.00</td>
      <td>NaN</td>
      <td>7278.00</td>
      <td>NaN</td>
      <td>7278.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Órlaithí Flynn</td>
      <td>Sinn Féin</td>
      <td>6743</td>
      <td>344.47</td>
      <td>7087.47</td>
      <td>5.38</td>
      <td>7092.85</td>
      <td>16.09</td>
      <td>7108.94</td>
      <td>27.37</td>
      <td>...</td>
      <td>68.37</td>
      <td>7228.63</td>
      <td>179</td>
      <td>7407.63</td>
      <td>NaN</td>
      <td>7407.63</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Aisling Reilly</td>
      <td>Sinn Féin</td>
      <td>5681</td>
      <td>1028.47</td>
      <td>6709.47</td>
      <td>10.19</td>
      <td>6719.66</td>
      <td>7.76</td>
      <td>6727.42</td>
      <td>17.09</td>
      <td>...</td>
      <td>50.52</td>
      <td>6811.98</td>
      <td>318.98</td>
      <td>7130.96</td>
      <td>533</td>
      <td>7663.96</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Pat Sheehan</td>
      <td>Sinn Féin</td>
      <td>6370</td>
      <td>52.44</td>
      <td>6422.44</td>
      <td>4</td>
      <td>6426.44</td>
      <td>5</td>
      <td>6431.44</td>
      <td>8.38</td>
      <td>...</td>
      <td>26.71</td>
      <td>6477.10</td>
      <td>258.18</td>
      <td>6735.28</td>
      <td>451.13</td>
      <td>7186.41</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Gerry Carroll</td>
      <td>People Before Profit</td>
      <td>3279</td>
      <td>115.33</td>
      <td>3394.33</td>
      <td>19.76</td>
      <td>3414.09</td>
      <td>78.38</td>
      <td>3492.47</td>
      <td>70.08</td>
      <td>...</td>
      <td>238.23</td>
      <td>3936.16</td>
      <td>542.99</td>
      <td>4479.15</td>
      <td>1543.46</td>
      <td>6022.61</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Frank McCoubrey</td>
      <td>Democratic Unionist Party</td>
      <td>4166</td>
      <td>0.57</td>
      <td>4166.57</td>
      <td>7.19</td>
      <td>4173.76</td>
      <td>0</td>
      <td>4173.76</td>
      <td>2</td>
      <td>...</td>
      <td>76.19</td>
      <td>5275.14</td>
      <td>154</td>
      <td>5429.14</td>
      <td>60.57</td>
      <td>5489.71</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Paul Doherty</td>
      <td>Social Democratic and Labour Party</td>
      <td>2528</td>
      <td>88.35</td>
      <td>2616.35</td>
      <td>2.19</td>
      <td>2618.54</td>
      <td>29.14</td>
      <td>2647.68</td>
      <td>36.28</td>
      <td>...</td>
      <td>478.51</td>
      <td>3232.66</td>
      <td>404.28</td>
      <td>3636.94</td>
      <td>-3636.94</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Gerard Herdman</td>
      <td>Aontú</td>
      <td>1753</td>
      <td>8.17</td>
      <td>1761.17</td>
      <td>32</td>
      <td>1793.17</td>
      <td>9.19</td>
      <td>1802.36</td>
      <td>17.19</td>
      <td>...</td>
      <td>35.19</td>
      <td>1871.74</td>
      <td>-1871.74</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Dan Murphy</td>
      <td>Irish Republican Socialist Party</td>
      <td>1103</td>
      <td>12.16</td>
      <td>1115.16</td>
      <td>8</td>
      <td>1123.16</td>
      <td>7</td>
      <td>1130.16</td>
      <td>14</td>
      <td>...</td>
      <td>7</td>
      <td>1159.16</td>
      <td>-1159.16</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Donnamarie Higgins</td>
      <td>Alliance Party</td>
      <td>907</td>
      <td>17.48</td>
      <td>924.48</td>
      <td>2</td>
      <td>926.48</td>
      <td>6</td>
      <td>932.48</td>
      <td>7.19</td>
      <td>...</td>
      <td>-1134.81</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Jordan Doran</td>
      <td>Traditional Unionist Voice</td>
      <td>802</td>
      <td>0.38</td>
      <td>802.38</td>
      <td>3</td>
      <td>805.38</td>
      <td>1</td>
      <td>806.38</td>
      <td>3</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Linsey Gibson</td>
      <td>Ulster Unionist Party</td>
      <td>474</td>
      <td>0.76</td>
      <td>474.76</td>
      <td>2</td>
      <td>476.76</td>
      <td>1.19</td>
      <td>477.95</td>
      <td>2</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Stevie Maginn</td>
      <td>Green Party</td>
      <td>307</td>
      <td>3.04</td>
      <td>310.04</td>
      <td>3</td>
      <td>313.04</td>
      <td>10</td>
      <td>323.04</td>
      <td>10.19</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Gerard Burns</td>
      <td>Independent</td>
      <td>192</td>
      <td>16.91</td>
      <td>208.91</td>
      <td>28.19</td>
      <td>237.10</td>
      <td>7</td>
      <td>244.10</td>
      <td>-244.1</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Patrick Crossan</td>
      <td>The Workers Party</td>
      <td>193</td>
      <td>4.75</td>
      <td>197.75</td>
      <td>6.76</td>
      <td>204.51</td>
      <td>-204.51</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Tony Mallon</td>
      <td>Independent</td>
      <td>129</td>
      <td>2.28</td>
      <td>131.28</td>
      <td>-131.28</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Declan Hill</td>
      <td>Independent</td>
      <td>26</td>
      <td>0.38</td>
      <td>26.38</td>
      <td>-26.38</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Exhausted</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>37.06</td>
      <td>37.06</td>
      <td>24</td>
      <td>61.06</td>
      <td>26.76</td>
      <td>87.82</td>
      <td>29.33</td>
      <td>...</td>
      <td>154.09</td>
      <td>393.43</td>
      <td>1173.47</td>
      <td>1566.90</td>
      <td>1048.78</td>
      <td>2615.68</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>44</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Eligible Voters</td>
      <td>68727</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Turnout</td>
      <td>44440</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>47</th>
      <td>% Turnout</td>
      <td>64.66%</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Valid Ballots</td>
      <td>43664</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>49</th>
      <td>invalid ballots</td>
      <td>776</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50</th>
      <td>quota</td>
      <td>7278</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>51 rows × 27 columns</p>
</div>



This is a little bit more complicated than other google foo would have you believe but it looks like Google updated their API's over the years to remove the 'happy path' for this call.

Additionally, note that as in the `IMPORTRANGE` example, there are no usable 'headers' in the underlying data so we may have to create these ourselves for more complex analysis.

Also, we have to manually 'tidy up' the 'range' ourselves, as the Belfast South range only goes to row 24, and then Belfast West appears.

While we could get fancy, for simplicity, this is a manual example. And we'll also exclude the 'metadata' such as the Turnout statistics and Quota from the bottom of the section, so in this case trimming the data from to run between rows 3 and 17 for just candidates and transfer statistics.


```python
df = pd.read_csv(url)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>...</th>
      <th>Unnamed: 17</th>
      <th>Unnamed: 18</th>
      <th>Unnamed: 19</th>
      <th>Unnamed: 20</th>
      <th>Unnamed: 21</th>
      <th>Unnamed: 22</th>
      <th>Unnamed: 23</th>
      <th>Unnamed: 24</th>
      <th>Unnamed: 25</th>
      <th>Unnamed: 26</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Belfast South</td>
      <td>NaN</td>
      <td>Stage 1</td>
      <td>Surplus Hargey</td>
      <td>2.00</td>
      <td>Exclude &lt;500</td>
      <td>3.00</td>
      <td>Exclude McCann Sibanda</td>
      <td>4.00</td>
      <td>Exclude Girvin</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11.00</td>
      <td>12.0</td>
      <td>13.0</td>
      <td>14.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Deirdre Hargey</td>
      <td>Sinn Féin</td>
      <td>9511</td>
      <td>-1687</td>
      <td>7824.00</td>
      <td>NaN</td>
      <td>7824.00</td>
      <td>NaN</td>
      <td>7824.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Edwin Poots</td>
      <td>Democratic Unionist Party</td>
      <td>7211</td>
      <td>6.12</td>
      <td>7217.12</td>
      <td>6.08</td>
      <td>7223.20</td>
      <td>117.72</td>
      <td>7340.92</td>
      <td>1134</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Matthew O'Toole</td>
      <td>Social Democratic and Labour Party</td>
      <td>5394</td>
      <td>664.92</td>
      <td>6058.92</td>
      <td>68.18</td>
      <td>6127.10</td>
      <td>322.04</td>
      <td>6449.14</td>
      <td>10.18</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paula Bradshaw</td>
      <td>Alliance Party</td>
      <td>6503</td>
      <td>265.14</td>
      <td>6768.14</td>
      <td>59.5</td>
      <td>6827.64</td>
      <td>135.82</td>
      <td>6963.46</td>
      <td>31</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kate Nicholl</td>
      <td>Alliance Party</td>
      <td>5201</td>
      <td>145.98</td>
      <td>5346.98</td>
      <td>57.52</td>
      <td>5404.50</td>
      <td>131.28</td>
      <td>5535.78</td>
      <td>17</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Clare Bailey</td>
      <td>Green Party</td>
      <td>4058</td>
      <td>167.4</td>
      <td>4225.40</td>
      <td>169.82</td>
      <td>4395.22</td>
      <td>490.54</td>
      <td>4885.76</td>
      <td>48.36</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Stephen McCarthy</td>
      <td>Ulster Unionist Party</td>
      <td>3061</td>
      <td>6.12</td>
      <td>3067.12</td>
      <td>17.72</td>
      <td>3084.84</td>
      <td>25.18</td>
      <td>3110.02</td>
      <td>643.36</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Elsie Trainor</td>
      <td>Social Democratic and Labour Party</td>
      <td>2030</td>
      <td>181.8</td>
      <td>2211.80</td>
      <td>18.52</td>
      <td>2230.32</td>
      <td>132.94</td>
      <td>2363.26</td>
      <td>4</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Andrew Girvin</td>
      <td>Traditional Unionist Voice</td>
      <td>1935</td>
      <td>0.36</td>
      <td>1935.36</td>
      <td>9</td>
      <td>1944.36</td>
      <td>35.54</td>
      <td>1979.90</td>
      <td>-1979.9</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Luke McCann</td>
      <td>Aontú</td>
      <td>806</td>
      <td>70.92</td>
      <td>876.92</td>
      <td>15.16</td>
      <td>892.08</td>
      <td>-892.08</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Sipho Sibanda</td>
      <td>People Before Profit</td>
      <td>629</td>
      <td>40.5</td>
      <td>669.50</td>
      <td>172.66</td>
      <td>842.16</td>
      <td>-842.16</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Neil Moore</td>
      <td>Socialist Party</td>
      <td>353</td>
      <td>18</td>
      <td>371.00</td>
      <td>-371</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Paddy Lynn</td>
      <td>The Workers Party</td>
      <td>139</td>
      <td>24.48</td>
      <td>163.48</td>
      <td>-163.48</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Elly Odhiambo</td>
      <td>Independent</td>
      <td>107</td>
      <td>6.84</td>
      <td>113.84</td>
      <td>-113.84</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Exhausted</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>88.42</td>
      <td>88.42</td>
      <td>54.16</td>
      <td>142.58</td>
      <td>343.18</td>
      <td>485.76</td>
      <td>92</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Eligible Voters</td>
      <td>73497</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Turnout</td>
      <td>47306</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>% Turnout</td>
      <td>64.36%</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Valid Ballots</td>
      <td>46938</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>invalid ballots</td>
      <td>368</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>quota</td>
      <td>7824</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Belfast West</td>
      <td>NaN</td>
      <td>Stage 1</td>
      <td>Surplus Baker</td>
      <td>2.00</td>
      <td>Exclude Hill Mallon</td>
      <td>3.00</td>
      <td>Exclude Crossan</td>
      <td>4.00</td>
      <td>Exclude Burns</td>
      <td>...</td>
      <td>Exclude Doran</td>
      <td>9.00</td>
      <td>Exclude Murphy Higgins</td>
      <td>10.00</td>
      <td>Exclude Doherty</td>
      <td>11.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Danny Baker</td>
      <td>Sinn Féin</td>
      <td>9011</td>
      <td>-1733</td>
      <td>7278.00</td>
      <td>NaN</td>
      <td>7278.00</td>
      <td>NaN</td>
      <td>7278.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>7278.00</td>
      <td>NaN</td>
      <td>7278.00</td>
      <td>NaN</td>
      <td>7278.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Órlaithí Flynn</td>
      <td>Sinn Féin</td>
      <td>6743</td>
      <td>344.47</td>
      <td>7087.47</td>
      <td>5.38</td>
      <td>7092.85</td>
      <td>16.09</td>
      <td>7108.94</td>
      <td>27.37</td>
      <td>...</td>
      <td>68.37</td>
      <td>7228.63</td>
      <td>179</td>
      <td>7407.63</td>
      <td>NaN</td>
      <td>7407.63</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Aisling Reilly</td>
      <td>Sinn Féin</td>
      <td>5681</td>
      <td>1028.47</td>
      <td>6709.47</td>
      <td>10.19</td>
      <td>6719.66</td>
      <td>7.76</td>
      <td>6727.42</td>
      <td>17.09</td>
      <td>...</td>
      <td>50.52</td>
      <td>6811.98</td>
      <td>318.98</td>
      <td>7130.96</td>
      <td>533</td>
      <td>7663.96</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Pat Sheehan</td>
      <td>Sinn Féin</td>
      <td>6370</td>
      <td>52.44</td>
      <td>6422.44</td>
      <td>4</td>
      <td>6426.44</td>
      <td>5</td>
      <td>6431.44</td>
      <td>8.38</td>
      <td>...</td>
      <td>26.71</td>
      <td>6477.10</td>
      <td>258.18</td>
      <td>6735.28</td>
      <td>451.13</td>
      <td>7186.41</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Gerry Carroll</td>
      <td>People Before Profit</td>
      <td>3279</td>
      <td>115.33</td>
      <td>3394.33</td>
      <td>19.76</td>
      <td>3414.09</td>
      <td>78.38</td>
      <td>3492.47</td>
      <td>70.08</td>
      <td>...</td>
      <td>238.23</td>
      <td>3936.16</td>
      <td>542.99</td>
      <td>4479.15</td>
      <td>1543.46</td>
      <td>6022.61</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Frank McCoubrey</td>
      <td>Democratic Unionist Party</td>
      <td>4166</td>
      <td>0.57</td>
      <td>4166.57</td>
      <td>7.19</td>
      <td>4173.76</td>
      <td>0</td>
      <td>4173.76</td>
      <td>2</td>
      <td>...</td>
      <td>76.19</td>
      <td>5275.14</td>
      <td>154</td>
      <td>5429.14</td>
      <td>60.57</td>
      <td>5489.71</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Paul Doherty</td>
      <td>Social Democratic and Labour Party</td>
      <td>2528</td>
      <td>88.35</td>
      <td>2616.35</td>
      <td>2.19</td>
      <td>2618.54</td>
      <td>29.14</td>
      <td>2647.68</td>
      <td>36.28</td>
      <td>...</td>
      <td>478.51</td>
      <td>3232.66</td>
      <td>404.28</td>
      <td>3636.94</td>
      <td>-3636.94</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Gerard Herdman</td>
      <td>Aontú</td>
      <td>1753</td>
      <td>8.17</td>
      <td>1761.17</td>
      <td>32</td>
      <td>1793.17</td>
      <td>9.19</td>
      <td>1802.36</td>
      <td>17.19</td>
      <td>...</td>
      <td>35.19</td>
      <td>1871.74</td>
      <td>-1871.74</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Dan Murphy</td>
      <td>Irish Republican Socialist Party</td>
      <td>1103</td>
      <td>12.16</td>
      <td>1115.16</td>
      <td>8</td>
      <td>1123.16</td>
      <td>7</td>
      <td>1130.16</td>
      <td>14</td>
      <td>...</td>
      <td>7</td>
      <td>1159.16</td>
      <td>-1159.16</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Donnamarie Higgins</td>
      <td>Alliance Party</td>
      <td>907</td>
      <td>17.48</td>
      <td>924.48</td>
      <td>2</td>
      <td>926.48</td>
      <td>6</td>
      <td>932.48</td>
      <td>7.19</td>
      <td>...</td>
      <td>-1134.81</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Jordan Doran</td>
      <td>Traditional Unionist Voice</td>
      <td>802</td>
      <td>0.38</td>
      <td>802.38</td>
      <td>3</td>
      <td>805.38</td>
      <td>1</td>
      <td>806.38</td>
      <td>3</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Linsey Gibson</td>
      <td>Ulster Unionist Party</td>
      <td>474</td>
      <td>0.76</td>
      <td>474.76</td>
      <td>2</td>
      <td>476.76</td>
      <td>1.19</td>
      <td>477.95</td>
      <td>2</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Stevie Maginn</td>
      <td>Green Party</td>
      <td>307</td>
      <td>3.04</td>
      <td>310.04</td>
      <td>3</td>
      <td>313.04</td>
      <td>10</td>
      <td>323.04</td>
      <td>10.19</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Gerard Burns</td>
      <td>Independent</td>
      <td>192</td>
      <td>16.91</td>
      <td>208.91</td>
      <td>28.19</td>
      <td>237.10</td>
      <td>7</td>
      <td>244.10</td>
      <td>-244.1</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Patrick Crossan</td>
      <td>The Workers Party</td>
      <td>193</td>
      <td>4.75</td>
      <td>197.75</td>
      <td>6.76</td>
      <td>204.51</td>
      <td>-204.51</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Tony Mallon</td>
      <td>Independent</td>
      <td>129</td>
      <td>2.28</td>
      <td>131.28</td>
      <td>-131.28</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Declan Hill</td>
      <td>Independent</td>
      <td>26</td>
      <td>0.38</td>
      <td>26.38</td>
      <td>-26.38</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Exhausted</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>37.06</td>
      <td>37.06</td>
      <td>24</td>
      <td>61.06</td>
      <td>26.76</td>
      <td>87.82</td>
      <td>29.33</td>
      <td>...</td>
      <td>154.09</td>
      <td>393.43</td>
      <td>1173.47</td>
      <td>1566.90</td>
      <td>1048.78</td>
      <td>2615.68</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>44</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Eligible Voters</td>
      <td>68727</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Turnout</td>
      <td>44440</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>47</th>
      <td>% Turnout</td>
      <td>64.66%</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Valid Ballots</td>
      <td>43664</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>49</th>
      <td>invalid ballots</td>
      <td>776</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50</th>
      <td>quota</td>
      <td>7278</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>51 rows × 27 columns</p>
</div>




```python
df.iloc[1:16]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>...</th>
      <th>Unnamed: 17</th>
      <th>Unnamed: 18</th>
      <th>Unnamed: 19</th>
      <th>Unnamed: 20</th>
      <th>Unnamed: 21</th>
      <th>Unnamed: 22</th>
      <th>Unnamed: 23</th>
      <th>Unnamed: 24</th>
      <th>Unnamed: 25</th>
      <th>Unnamed: 26</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Deirdre Hargey</td>
      <td>Sinn Féin</td>
      <td>9511</td>
      <td>-1687</td>
      <td>7824.00</td>
      <td>NaN</td>
      <td>7824.00</td>
      <td>NaN</td>
      <td>7824.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Edwin Poots</td>
      <td>Democratic Unionist Party</td>
      <td>7211</td>
      <td>6.12</td>
      <td>7217.12</td>
      <td>6.08</td>
      <td>7223.20</td>
      <td>117.72</td>
      <td>7340.92</td>
      <td>1134</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Matthew O'Toole</td>
      <td>Social Democratic and Labour Party</td>
      <td>5394</td>
      <td>664.92</td>
      <td>6058.92</td>
      <td>68.18</td>
      <td>6127.10</td>
      <td>322.04</td>
      <td>6449.14</td>
      <td>10.18</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paula Bradshaw</td>
      <td>Alliance Party</td>
      <td>6503</td>
      <td>265.14</td>
      <td>6768.14</td>
      <td>59.5</td>
      <td>6827.64</td>
      <td>135.82</td>
      <td>6963.46</td>
      <td>31</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kate Nicholl</td>
      <td>Alliance Party</td>
      <td>5201</td>
      <td>145.98</td>
      <td>5346.98</td>
      <td>57.52</td>
      <td>5404.50</td>
      <td>131.28</td>
      <td>5535.78</td>
      <td>17</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Clare Bailey</td>
      <td>Green Party</td>
      <td>4058</td>
      <td>167.4</td>
      <td>4225.40</td>
      <td>169.82</td>
      <td>4395.22</td>
      <td>490.54</td>
      <td>4885.76</td>
      <td>48.36</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Stephen McCarthy</td>
      <td>Ulster Unionist Party</td>
      <td>3061</td>
      <td>6.12</td>
      <td>3067.12</td>
      <td>17.72</td>
      <td>3084.84</td>
      <td>25.18</td>
      <td>3110.02</td>
      <td>643.36</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Elsie Trainor</td>
      <td>Social Democratic and Labour Party</td>
      <td>2030</td>
      <td>181.8</td>
      <td>2211.80</td>
      <td>18.52</td>
      <td>2230.32</td>
      <td>132.94</td>
      <td>2363.26</td>
      <td>4</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Andrew Girvin</td>
      <td>Traditional Unionist Voice</td>
      <td>1935</td>
      <td>0.36</td>
      <td>1935.36</td>
      <td>9</td>
      <td>1944.36</td>
      <td>35.54</td>
      <td>1979.90</td>
      <td>-1979.9</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Luke McCann</td>
      <td>Aontú</td>
      <td>806</td>
      <td>70.92</td>
      <td>876.92</td>
      <td>15.16</td>
      <td>892.08</td>
      <td>-892.08</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Sipho Sibanda</td>
      <td>People Before Profit</td>
      <td>629</td>
      <td>40.5</td>
      <td>669.50</td>
      <td>172.66</td>
      <td>842.16</td>
      <td>-842.16</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Neil Moore</td>
      <td>Socialist Party</td>
      <td>353</td>
      <td>18</td>
      <td>371.00</td>
      <td>-371</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Paddy Lynn</td>
      <td>The Workers Party</td>
      <td>139</td>
      <td>24.48</td>
      <td>163.48</td>
      <td>-163.48</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Elly Odhiambo</td>
      <td>Independent</td>
      <td>107</td>
      <td>6.84</td>
      <td>113.84</td>
      <td>-113.84</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Exhausted</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>88.42</td>
      <td>88.42</td>
      <td>54.16</td>
      <td>142.58</td>
      <td>343.18</td>
      <td>485.76</td>
      <td>92</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>15 rows × 27 columns</p>
</div>



There are a few ways to tidy up this stage/transfer setup, so for simplicity we'll take the 'index' off the left of the table (consisting of the candidate and party names) and try and construct a new column index based on those.

Sounds fancy.


```python
df.iloc[1:16]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>...</th>
      <th>Unnamed: 17</th>
      <th>Unnamed: 18</th>
      <th>Unnamed: 19</th>
      <th>Unnamed: 20</th>
      <th>Unnamed: 21</th>
      <th>Unnamed: 22</th>
      <th>Unnamed: 23</th>
      <th>Unnamed: 24</th>
      <th>Unnamed: 25</th>
      <th>Unnamed: 26</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Deirdre Hargey</td>
      <td>Sinn Féin</td>
      <td>9511</td>
      <td>-1687</td>
      <td>7824.00</td>
      <td>NaN</td>
      <td>7824.00</td>
      <td>NaN</td>
      <td>7824.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Edwin Poots</td>
      <td>Democratic Unionist Party</td>
      <td>7211</td>
      <td>6.12</td>
      <td>7217.12</td>
      <td>6.08</td>
      <td>7223.20</td>
      <td>117.72</td>
      <td>7340.92</td>
      <td>1134</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Matthew O'Toole</td>
      <td>Social Democratic and Labour Party</td>
      <td>5394</td>
      <td>664.92</td>
      <td>6058.92</td>
      <td>68.18</td>
      <td>6127.10</td>
      <td>322.04</td>
      <td>6449.14</td>
      <td>10.18</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paula Bradshaw</td>
      <td>Alliance Party</td>
      <td>6503</td>
      <td>265.14</td>
      <td>6768.14</td>
      <td>59.5</td>
      <td>6827.64</td>
      <td>135.82</td>
      <td>6963.46</td>
      <td>31</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kate Nicholl</td>
      <td>Alliance Party</td>
      <td>5201</td>
      <td>145.98</td>
      <td>5346.98</td>
      <td>57.52</td>
      <td>5404.50</td>
      <td>131.28</td>
      <td>5535.78</td>
      <td>17</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Clare Bailey</td>
      <td>Green Party</td>
      <td>4058</td>
      <td>167.4</td>
      <td>4225.40</td>
      <td>169.82</td>
      <td>4395.22</td>
      <td>490.54</td>
      <td>4885.76</td>
      <td>48.36</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Stephen McCarthy</td>
      <td>Ulster Unionist Party</td>
      <td>3061</td>
      <td>6.12</td>
      <td>3067.12</td>
      <td>17.72</td>
      <td>3084.84</td>
      <td>25.18</td>
      <td>3110.02</td>
      <td>643.36</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Elsie Trainor</td>
      <td>Social Democratic and Labour Party</td>
      <td>2030</td>
      <td>181.8</td>
      <td>2211.80</td>
      <td>18.52</td>
      <td>2230.32</td>
      <td>132.94</td>
      <td>2363.26</td>
      <td>4</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Andrew Girvin</td>
      <td>Traditional Unionist Voice</td>
      <td>1935</td>
      <td>0.36</td>
      <td>1935.36</td>
      <td>9</td>
      <td>1944.36</td>
      <td>35.54</td>
      <td>1979.90</td>
      <td>-1979.9</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Luke McCann</td>
      <td>Aontú</td>
      <td>806</td>
      <td>70.92</td>
      <td>876.92</td>
      <td>15.16</td>
      <td>892.08</td>
      <td>-892.08</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Sipho Sibanda</td>
      <td>People Before Profit</td>
      <td>629</td>
      <td>40.5</td>
      <td>669.50</td>
      <td>172.66</td>
      <td>842.16</td>
      <td>-842.16</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Neil Moore</td>
      <td>Socialist Party</td>
      <td>353</td>
      <td>18</td>
      <td>371.00</td>
      <td>-371</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Paddy Lynn</td>
      <td>The Workers Party</td>
      <td>139</td>
      <td>24.48</td>
      <td>163.48</td>
      <td>-163.48</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Elly Odhiambo</td>
      <td>Independent</td>
      <td>107</td>
      <td>6.84</td>
      <td>113.84</td>
      <td>-113.84</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Exhausted</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>88.42</td>
      <td>88.42</td>
      <td>54.16</td>
      <td>142.58</td>
      <td>343.18</td>
      <td>485.76</td>
      <td>92</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>15 rows × 27 columns</p>
</div>




```python
_table = df.iloc[1:16]
_table = _table.dropna(how='all', axis=1)
_table = _table.set_index(_table.columns.tolist()[0:2])
_table = _table.fillna(0)
_table = _table.astype(float)
_table.index=_table.index.set_names(['Candidate','Party'])
_table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>Unnamed: 10</th>
      <th>Unnamed: 11</th>
      <th>Unnamed: 12</th>
      <th>Unnamed: 13</th>
      <th>Unnamed: 14</th>
      <th>Unnamed: 15</th>
      <th>Unnamed: 16</th>
    </tr>
    <tr>
      <th>Candidate</th>
      <th>Party</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Deirdre Hargey</th>
      <th>Sinn Féin</th>
      <td>9511.0</td>
      <td>-1687.00</td>
      <td>7824.00</td>
      <td>0.00</td>
      <td>7824.00</td>
      <td>0.00</td>
      <td>7824.00</td>
      <td>0.00</td>
      <td>7824.00</td>
      <td>0.00</td>
      <td>7824.00</td>
      <td>0.00</td>
      <td>7824.00</td>
      <td>0.00</td>
      <td>7824.00</td>
    </tr>
    <tr>
      <th>Edwin Poots</th>
      <th>Democratic Unionist Party</th>
      <td>7211.0</td>
      <td>6.12</td>
      <td>7217.12</td>
      <td>6.08</td>
      <td>7223.20</td>
      <td>117.72</td>
      <td>7340.92</td>
      <td>1134.00</td>
      <td>8474.92</td>
      <td>0.00</td>
      <td>8474.92</td>
      <td>0.00</td>
      <td>8474.92</td>
      <td>-650.92</td>
      <td>7824.00</td>
    </tr>
    <tr>
      <th>Matthew O'Toole</th>
      <th>Social Democratic and Labour Party</th>
      <td>5394.0</td>
      <td>664.92</td>
      <td>6058.92</td>
      <td>68.18</td>
      <td>6127.10</td>
      <td>322.04</td>
      <td>6449.14</td>
      <td>10.18</td>
      <td>6459.32</td>
      <td>1630.00</td>
      <td>8089.32</td>
      <td>0.00</td>
      <td>8089.32</td>
      <td>0.00</td>
      <td>8089.32</td>
    </tr>
    <tr>
      <th>Paula Bradshaw</th>
      <th>Alliance Party</th>
      <td>6503.0</td>
      <td>265.14</td>
      <td>6768.14</td>
      <td>59.50</td>
      <td>6827.64</td>
      <td>135.82</td>
      <td>6963.46</td>
      <td>31.00</td>
      <td>6994.46</td>
      <td>214.68</td>
      <td>7209.14</td>
      <td>1114.00</td>
      <td>8323.14</td>
      <td>0.00</td>
      <td>8323.14</td>
    </tr>
    <tr>
      <th>Kate Nicholl</th>
      <th>Alliance Party</th>
      <td>5201.0</td>
      <td>145.98</td>
      <td>5346.98</td>
      <td>57.52</td>
      <td>5404.50</td>
      <td>131.28</td>
      <td>5535.78</td>
      <td>17.00</td>
      <td>5552.78</td>
      <td>244.90</td>
      <td>5797.68</td>
      <td>858.42</td>
      <td>6656.10</td>
      <td>81.00</td>
      <td>6737.10</td>
    </tr>
    <tr>
      <th>Clare Bailey</th>
      <th>Green Party</th>
      <td>4058.0</td>
      <td>167.40</td>
      <td>4225.40</td>
      <td>169.82</td>
      <td>4395.22</td>
      <td>490.54</td>
      <td>4885.76</td>
      <td>48.36</td>
      <td>4934.12</td>
      <td>164.02</td>
      <td>5098.14</td>
      <td>600.96</td>
      <td>5699.10</td>
      <td>127.00</td>
      <td>5826.10</td>
    </tr>
    <tr>
      <th>Stephen McCarthy</th>
      <th>Ulster Unionist Party</th>
      <td>3061.0</td>
      <td>6.12</td>
      <td>3067.12</td>
      <td>17.72</td>
      <td>3084.84</td>
      <td>25.18</td>
      <td>3110.02</td>
      <td>643.36</td>
      <td>3753.38</td>
      <td>16.90</td>
      <td>3770.28</td>
      <td>-3770.28</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Elsie Trainor</th>
      <th>Social Democratic and Labour Party</th>
      <td>2030.0</td>
      <td>181.80</td>
      <td>2211.80</td>
      <td>18.52</td>
      <td>2230.32</td>
      <td>132.94</td>
      <td>2363.26</td>
      <td>4.00</td>
      <td>2367.26</td>
      <td>-2367.26</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Andrew Girvin</th>
      <th>Traditional Unionist Voice</th>
      <td>1935.0</td>
      <td>0.36</td>
      <td>1935.36</td>
      <td>9.00</td>
      <td>1944.36</td>
      <td>35.54</td>
      <td>1979.90</td>
      <td>-1979.90</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Luke McCann</th>
      <th>Aontú</th>
      <td>806.0</td>
      <td>70.92</td>
      <td>876.92</td>
      <td>15.16</td>
      <td>892.08</td>
      <td>-892.08</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Sipho Sibanda</th>
      <th>People Before Profit</th>
      <td>629.0</td>
      <td>40.50</td>
      <td>669.50</td>
      <td>172.66</td>
      <td>842.16</td>
      <td>-842.16</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Neil Moore</th>
      <th>Socialist Party</th>
      <td>353.0</td>
      <td>18.00</td>
      <td>371.00</td>
      <td>-371.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Paddy Lynn</th>
      <th>The Workers Party</th>
      <td>139.0</td>
      <td>24.48</td>
      <td>163.48</td>
      <td>-163.48</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Elly Odhiambo</th>
      <th>Independent</th>
      <td>107.0</td>
      <td>6.84</td>
      <td>113.84</td>
      <td>-113.84</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Exhausted</th>
      <th>NaN</th>
      <td>0.0</td>
      <td>88.42</td>
      <td>88.42</td>
      <td>54.16</td>
      <td>142.58</td>
      <td>343.18</td>
      <td>485.76</td>
      <td>92.00</td>
      <td>577.76</td>
      <td>96.76</td>
      <td>674.52</td>
      <td>1196.90</td>
      <td>1871.42</td>
      <td>442.92</td>
      <td>2314.34</td>
    </tr>
  </tbody>
</table>
</div>



Now to do the same thing with the stage counts and transfers;

There are many ways to do this, either leaving it as is and just naming the columns by Stage and Transfer, but a 'better' way to do it is to create a multiindex on the column. Which probably means nothing.


```python
_table.columns
```




    Index(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6',
           'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11',
           'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15',
           'Unnamed: 16'],
          dtype='object')




```python
stage = ['Count','Transfers']
stages = range(1,_table.shape[1]//2+2)
pd.MultiIndex.from_product([stages,stage])[:-1]
```




    MultiIndex([(1,     'Count'),
                (1, 'Transfers'),
                (2,     'Count'),
                (2, 'Transfers'),
                (3,     'Count'),
                (3, 'Transfers'),
                (4,     'Count'),
                (4, 'Transfers'),
                (5,     'Count'),
                (5, 'Transfers'),
                (6,     'Count'),
                (6, 'Transfers'),
                (7,     'Count'),
                (7, 'Transfers'),
                (8,     'Count')],
               )




```python
_table.columns=pd.MultiIndex.from_product([stages,stage], names=['Stage','Step'])[:-1]
```


```python
_table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>Stage</th>
      <th colspan="2" halign="left">1</th>
      <th colspan="2" halign="left">2</th>
      <th colspan="2" halign="left">3</th>
      <th colspan="2" halign="left">4</th>
      <th colspan="2" halign="left">5</th>
      <th colspan="2" halign="left">6</th>
      <th colspan="2" halign="left">7</th>
      <th>8</th>
    </tr>
    <tr>
      <th></th>
      <th>Step</th>
      <th>Count</th>
      <th>Transfers</th>
      <th>Count</th>
      <th>Transfers</th>
      <th>Count</th>
      <th>Transfers</th>
      <th>Count</th>
      <th>Transfers</th>
      <th>Count</th>
      <th>Transfers</th>
      <th>Count</th>
      <th>Transfers</th>
      <th>Count</th>
      <th>Transfers</th>
      <th>Count</th>
    </tr>
    <tr>
      <th>Candidate</th>
      <th>Party</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Deirdre Hargey</th>
      <th>Sinn Féin</th>
      <td>9511.0</td>
      <td>-1687.00</td>
      <td>7824.00</td>
      <td>0.00</td>
      <td>7824.00</td>
      <td>0.00</td>
      <td>7824.00</td>
      <td>0.00</td>
      <td>7824.00</td>
      <td>0.00</td>
      <td>7824.00</td>
      <td>0.00</td>
      <td>7824.00</td>
      <td>0.00</td>
      <td>7824.00</td>
    </tr>
    <tr>
      <th>Edwin Poots</th>
      <th>Democratic Unionist Party</th>
      <td>7211.0</td>
      <td>6.12</td>
      <td>7217.12</td>
      <td>6.08</td>
      <td>7223.20</td>
      <td>117.72</td>
      <td>7340.92</td>
      <td>1134.00</td>
      <td>8474.92</td>
      <td>0.00</td>
      <td>8474.92</td>
      <td>0.00</td>
      <td>8474.92</td>
      <td>-650.92</td>
      <td>7824.00</td>
    </tr>
    <tr>
      <th>Matthew O'Toole</th>
      <th>Social Democratic and Labour Party</th>
      <td>5394.0</td>
      <td>664.92</td>
      <td>6058.92</td>
      <td>68.18</td>
      <td>6127.10</td>
      <td>322.04</td>
      <td>6449.14</td>
      <td>10.18</td>
      <td>6459.32</td>
      <td>1630.00</td>
      <td>8089.32</td>
      <td>0.00</td>
      <td>8089.32</td>
      <td>0.00</td>
      <td>8089.32</td>
    </tr>
    <tr>
      <th>Paula Bradshaw</th>
      <th>Alliance Party</th>
      <td>6503.0</td>
      <td>265.14</td>
      <td>6768.14</td>
      <td>59.50</td>
      <td>6827.64</td>
      <td>135.82</td>
      <td>6963.46</td>
      <td>31.00</td>
      <td>6994.46</td>
      <td>214.68</td>
      <td>7209.14</td>
      <td>1114.00</td>
      <td>8323.14</td>
      <td>0.00</td>
      <td>8323.14</td>
    </tr>
    <tr>
      <th>Kate Nicholl</th>
      <th>Alliance Party</th>
      <td>5201.0</td>
      <td>145.98</td>
      <td>5346.98</td>
      <td>57.52</td>
      <td>5404.50</td>
      <td>131.28</td>
      <td>5535.78</td>
      <td>17.00</td>
      <td>5552.78</td>
      <td>244.90</td>
      <td>5797.68</td>
      <td>858.42</td>
      <td>6656.10</td>
      <td>81.00</td>
      <td>6737.10</td>
    </tr>
    <tr>
      <th>Clare Bailey</th>
      <th>Green Party</th>
      <td>4058.0</td>
      <td>167.40</td>
      <td>4225.40</td>
      <td>169.82</td>
      <td>4395.22</td>
      <td>490.54</td>
      <td>4885.76</td>
      <td>48.36</td>
      <td>4934.12</td>
      <td>164.02</td>
      <td>5098.14</td>
      <td>600.96</td>
      <td>5699.10</td>
      <td>127.00</td>
      <td>5826.10</td>
    </tr>
    <tr>
      <th>Stephen McCarthy</th>
      <th>Ulster Unionist Party</th>
      <td>3061.0</td>
      <td>6.12</td>
      <td>3067.12</td>
      <td>17.72</td>
      <td>3084.84</td>
      <td>25.18</td>
      <td>3110.02</td>
      <td>643.36</td>
      <td>3753.38</td>
      <td>16.90</td>
      <td>3770.28</td>
      <td>-3770.28</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Elsie Trainor</th>
      <th>Social Democratic and Labour Party</th>
      <td>2030.0</td>
      <td>181.80</td>
      <td>2211.80</td>
      <td>18.52</td>
      <td>2230.32</td>
      <td>132.94</td>
      <td>2363.26</td>
      <td>4.00</td>
      <td>2367.26</td>
      <td>-2367.26</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Andrew Girvin</th>
      <th>Traditional Unionist Voice</th>
      <td>1935.0</td>
      <td>0.36</td>
      <td>1935.36</td>
      <td>9.00</td>
      <td>1944.36</td>
      <td>35.54</td>
      <td>1979.90</td>
      <td>-1979.90</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Luke McCann</th>
      <th>Aontú</th>
      <td>806.0</td>
      <td>70.92</td>
      <td>876.92</td>
      <td>15.16</td>
      <td>892.08</td>
      <td>-892.08</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Sipho Sibanda</th>
      <th>People Before Profit</th>
      <td>629.0</td>
      <td>40.50</td>
      <td>669.50</td>
      <td>172.66</td>
      <td>842.16</td>
      <td>-842.16</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Neil Moore</th>
      <th>Socialist Party</th>
      <td>353.0</td>
      <td>18.00</td>
      <td>371.00</td>
      <td>-371.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Paddy Lynn</th>
      <th>The Workers Party</th>
      <td>139.0</td>
      <td>24.48</td>
      <td>163.48</td>
      <td>-163.48</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Elly Odhiambo</th>
      <th>Independent</th>
      <td>107.0</td>
      <td>6.84</td>
      <td>113.84</td>
      <td>-113.84</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Exhausted</th>
      <th>NaN</th>
      <td>0.0</td>
      <td>88.42</td>
      <td>88.42</td>
      <td>54.16</td>
      <td>142.58</td>
      <td>343.18</td>
      <td>485.76</td>
      <td>92.00</td>
      <td>577.76</td>
      <td>96.76</td>
      <td>674.52</td>
      <td>1196.90</td>
      <td>1871.42</td>
      <td>442.92</td>
      <td>2314.34</td>
    </tr>
  </tbody>
</table>
</div>



Now we can do some interesting queries really easily;


```python
_table.xs("Count", level='Step', axis=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Stage</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
    </tr>
    <tr>
      <th>Candidate</th>
      <th>Party</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Deirdre Hargey</th>
      <th>Sinn Féin</th>
      <td>9511.0</td>
      <td>7824.00</td>
      <td>7824.00</td>
      <td>7824.00</td>
      <td>7824.00</td>
      <td>7824.00</td>
      <td>7824.00</td>
      <td>7824.00</td>
    </tr>
    <tr>
      <th>Edwin Poots</th>
      <th>Democratic Unionist Party</th>
      <td>7211.0</td>
      <td>7217.12</td>
      <td>7223.20</td>
      <td>7340.92</td>
      <td>8474.92</td>
      <td>8474.92</td>
      <td>8474.92</td>
      <td>7824.00</td>
    </tr>
    <tr>
      <th>Matthew O'Toole</th>
      <th>Social Democratic and Labour Party</th>
      <td>5394.0</td>
      <td>6058.92</td>
      <td>6127.10</td>
      <td>6449.14</td>
      <td>6459.32</td>
      <td>8089.32</td>
      <td>8089.32</td>
      <td>8089.32</td>
    </tr>
    <tr>
      <th>Paula Bradshaw</th>
      <th>Alliance Party</th>
      <td>6503.0</td>
      <td>6768.14</td>
      <td>6827.64</td>
      <td>6963.46</td>
      <td>6994.46</td>
      <td>7209.14</td>
      <td>8323.14</td>
      <td>8323.14</td>
    </tr>
    <tr>
      <th>Kate Nicholl</th>
      <th>Alliance Party</th>
      <td>5201.0</td>
      <td>5346.98</td>
      <td>5404.50</td>
      <td>5535.78</td>
      <td>5552.78</td>
      <td>5797.68</td>
      <td>6656.10</td>
      <td>6737.10</td>
    </tr>
    <tr>
      <th>Clare Bailey</th>
      <th>Green Party</th>
      <td>4058.0</td>
      <td>4225.40</td>
      <td>4395.22</td>
      <td>4885.76</td>
      <td>4934.12</td>
      <td>5098.14</td>
      <td>5699.10</td>
      <td>5826.10</td>
    </tr>
    <tr>
      <th>Stephen McCarthy</th>
      <th>Ulster Unionist Party</th>
      <td>3061.0</td>
      <td>3067.12</td>
      <td>3084.84</td>
      <td>3110.02</td>
      <td>3753.38</td>
      <td>3770.28</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Elsie Trainor</th>
      <th>Social Democratic and Labour Party</th>
      <td>2030.0</td>
      <td>2211.80</td>
      <td>2230.32</td>
      <td>2363.26</td>
      <td>2367.26</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Andrew Girvin</th>
      <th>Traditional Unionist Voice</th>
      <td>1935.0</td>
      <td>1935.36</td>
      <td>1944.36</td>
      <td>1979.90</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Luke McCann</th>
      <th>Aontú</th>
      <td>806.0</td>
      <td>876.92</td>
      <td>892.08</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Sipho Sibanda</th>
      <th>People Before Profit</th>
      <td>629.0</td>
      <td>669.50</td>
      <td>842.16</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Neil Moore</th>
      <th>Socialist Party</th>
      <td>353.0</td>
      <td>371.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Paddy Lynn</th>
      <th>The Workers Party</th>
      <td>139.0</td>
      <td>163.48</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Elly Odhiambo</th>
      <th>Independent</th>
      <td>107.0</td>
      <td>113.84</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>Exhausted</th>
      <th>NaN</th>
      <td>0.0</td>
      <td>88.42</td>
      <td>142.58</td>
      <td>485.76</td>
      <td>577.76</td>
      <td>674.52</td>
      <td>1871.42</td>
      <td>2314.34</td>
    </tr>
  </tbody>
</table>
</div>



This makes plotting quite simple; which then makes the queries you can express much more complex...


```python
_table.xs("Count", level='Step', axis=1).groupby('Party').sum().T.plot()
```




    <Axes: xlabel='Stage'>





![png](/img/eni_output_16_1.png)




```python
_table.xs("Transfers", level='Step', axis=1)\
    .groupby('Party').sum().cumsum().T.plot(
        title='Net Cumulative Transfers'
    )\
    .legend(loc='right', bbox_to_anchor=(1.6,0.5))
```




    <matplotlib.legend.Legend at 0x17b555a50>




![png](/img/eni_output_17_1.png)



## Conclusion

Considering it's election day today in Northern Ireland, I wanted to bash this out to help other election observers have a play with the fantastic work the likes of [@colm_burns](https://twitter.com/colm_burns) and the rest of the [@electionsni](https://twitter.com/electionsni) team are doing.

More than happy to help anyone else answer interesting electoral questions, and remember; vote early, vote often, and #votetillyouboke
