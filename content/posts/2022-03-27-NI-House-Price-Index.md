---
date: 2022-03-27T19:49:00+00:00
layout: post
tags:
- Government Open Data
- Data Analysis
- Data Wrangling
- NI House Price Index
title: Wrangling NI House Price Index Data
---


# Data Wrangling NI House Price Index Data

This is a 'messy' 'blog post' that's just a braindump of a notebook to step through [NI House Price Index](https://www.nisra.gov.uk/statistics/housing-community-and-regeneration/northern-ireland-house-price-index) datasets I was playing around with.

It's mostly code, so if you were here from some 'insight', feck aff.

There is **no** analysis here, this is **just** data wrangling.

TLDR As always, Government Open Data has over the years gone from 'non-existent' to 'garbeled' to 'inconsistent' and I feel is now in the stage of 'consistently inconsistent', which is progress in my eyes.

# Preamble Code, move on.


```python
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Pull the latest pages of https://www.finance-ni.gov.uk/publications/ni-house-price-index-statistical-reports and extract links

base_url= 'https://www.finance-ni.gov.uk/publications/ni-house-price-index-statistical-reports'
base_content = requests.get(base_url).content
base_soup = BeautifulSoup(base_content)
```


```python
for a in base_soup.find_all('a'):
    if a.attrs.get('href','').endswith('xlsx'):
        source_name, source_url = a.contents[1],a.attrs['href']

source_df = pd.read_excel(source_url, sheet_name = None) # Load all worksheets in

```


```python
source_df.keys()
```




    dict_keys(['Cover Sheet', 'Contents', 'Table 1', 'Table 2', 'Table 2a', 'Table 2b', 'Table 2c', 'Table 2d', 'Table 3', 'Table 3a', 'Table 3b', 'Table 3c', 'Table 4', 'Fig 5', 'Table 5', 'Table 5a', 'Fig 6', 'Table 6', 'Table 7', 'Table 8', 'Table 9', 'Table 9a', 'Table 9b', 'Table 9c', 'Table 9d', 'Table 10a', 'Table 10b', 'Table 10c', 'Table 10d', 'Table 10e', 'Table 10f', 'Table 10g', 'Table 10h', 'Table 10i', 'Table 10j', 'Table 10k'])




```python
source_df['Contents']
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
      <th>Table of Contents</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Worksheet Name</td>
      <td>Frequency</td>
      <td>House Price Index - Quarter 4 2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Table 1</td>
      <td>Quarterly</td>
      <td>Table 1: NI HPI Trends Q1 2005 - Q4 2021</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figure 1</td>
      <td>Quarterly</td>
      <td>Figure 1: Graph of NI HPI Q1 2005 - Q4 2021</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Figure 1a</td>
      <td>Quarterly</td>
      <td>Figure 1a: Graph of Percentage Quarterly Chang...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Figure 1b</td>
      <td>Quarterly</td>
      <td>Figure 1b: Graph of Percentage Annual Change Q...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Table 10h</td>
      <td>Quarterly</td>
      <td>Table 10h: Number of Verified Residential Prop...</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Table 10i</td>
      <td>Quarterly</td>
      <td>Table 10i: Number of Verified Residential Prop...</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Table 10j</td>
      <td>Quarterly</td>
      <td>Table 10j: Number of Verified Residential Prop...</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Table 10k</td>
      <td>Quarterly</td>
      <td>Table 10k: Number of Verified Residential Prop...</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Figure 11</td>
      <td>Quarterly</td>
      <td>Figure 11: Number of Verified Residential Prop...</td>
    </tr>
  </tbody>
</table>
<p>63 rows × 3 columns</p>
</div>



### Fix the Contents sheet to correctly reflect the Worksheet names
And fix the table headers and sheet-titles while we're at it.


```python
new_header = source_df['Contents'].iloc[0]
source_df['Contents'] = source_df['Contents'][1:]
source_df['Contents'].columns = new_header
```


```python
source_df['Contents'].columns = [*new_header[:-1],'Title']
```


```python
[t for t in source_df['Contents']['Title'].values if t.startswith('Table')]
```




    ['Table 1: NI HPI Trends Q1 2005 - Q4 2021',
     'Table 2: NI HPI & Standardised Price Statistics by Property Type Q4 2021',
     'Table 2a: NI Detached Property Price Index Q1 2005 - Q4 2021',
     'Table 2b: NI Semi-Detached Property Price Index Q1 2005 - Q4 2021',
     'Table 2c: NI Terrace Property Price Index Q1 2005 - Q4 2021',
     'Table 2d: NI Apartment Price Index Q1 2005 - Q4 2021',
     'Table 3: NI HPI & Standardised Price Statistics by New/Existing Resold Dwelling Type Q4 2021',
     'Table 3a: NI New Dwelling Price Index Q1 2005 - Q4 2021',
     'Table 3b: NI Existing Resold Dwellings Price Index Q1 2005 - Q4 2021',
     'Table 3c: Number of Verified Residential Property Sales by New/Existing Resold Dwellings Q1 2005 - Q2 2021',
     'Table 4: Number of Verified Residential Property Sales Q1 2005 - Q4 2021',
     'Table 5: HPI & Standardised Price for each Local Government District in NI',
     'Table 5a: Number of Verified Residential Property Sales by Local Government District Q1 2005 - Q4 2021',
     'Table 6: NI HPI & Standardised Price by Urban and Rural areas of Northern Ireland',
     'Table 7: Standardised House Price & Index for Rural Areas of Northern Ireland by drive times',
     'Table 8: Number of Verified Residential Property Sales for Urban and Rural Areas of NI (Q1 2005 - Q4 2021) and Rural Areas of NI by drive times (Q1 2015 - Q4 2021)',
     'Table 9: NI Average Sale Prices All Properties Q1 2005 - Q4 2021',
     'Table 9a: NI Average Sale Prices Detached Properties Q1 2005 - Q4 2021',
     'Table 9b: NI Average Sale Prices Semi-Detached Properties Q1 2005 - Q4 2021',
     'Table 9c: NI Average Sale Prices Terrace Properties Q1 2005 - Q4 2021',
     'Table 9d: NI Average Sale Prices Apartments Q1 2005 - Q4 2021',
     'Table 10a: Number of Verified Residential Property Sales by Type in Antrim and Newtownabbey Council Q1 2005 - Q4 2021',
     'Table 10b: Number of Verified Residential Property Sales by Type in Ards and North Down Council Q1 2005 - Q4 2021',
     'Table 10c: Number of Verified Residential Property Sales by Type in Armagh City, Banbridge and Craigavon Council Q1 2005 - Q4 2021',
     'Table 10d: Number of Verified Residential Property Sales by Type in Belfast Council Q1 2005 - Q4 2021',
     'Table 10e: Number of Verified Residential Property Sales by Type in Causeway Coast and Glens Council Q1 2005 - Q4 2021',
     'Table 10f: Number of Verified Residential Property Sales by Type in Derry City and Strabane Council Q1 2005 - Q4 2021',
     'Table 10g: Number of Verified Residential Property Sales by Type in Fermanagh and Omagh Council Q1 2005 - Q4 2021',
     'Table 10h: Number of Verified Residential Property Sales by Type in Lisburn and Castlereagh Council Q1 2005 - Q4 2021',
     'Table 10i: Number of Verified Residential Property Sales by Type in Mid and East Antrim Council Q1 2005 - Q4 2021',
     'Table 10j: Number of Verified Residential Property Sales by Type in Mid Ulster Council Q1 2005 - Q4 2021',
     'Table 10k: Number of Verified Residential Property Sales by Type in Newry, Mourne and Down Council Q1 2005 - Q4 2021']




```python
# Replace 'Figure' with 'Fig' in 'Worksheet Name'
with pd.option_context('mode.chained_assignment',None):
    source_df['Contents']['Worksheet Name'] = source_df['Contents']['Worksheet Name'].str.replace('Figure','Fig')
```

## Tidy up Data

### General Methodology

Ignore figure data (pretty much completly....)

Tables have more or less the same structure; a header on row 3(1), a year and quarter 'index' (on time series; otherwise categorical index, see Table 2, Table 3).

Some TS tables _also_ have totals subsections so these should be a) validated and b) ignored.

Any columns with no header in row 3(1) should be ignored (usually text notes)

_Operate Sequentially_ (i.e. Table 1, Table 2, Table 2a; don't skip, even if it's tempting)

Use keys from 'Contents' to describe data, but **may be suffixed by the date which could change between data sets!**

There's also some really columns that look like checksums, so if there is an 'NI' column, or a data column that all valid values are '100', delete it.

### Table 1: NI HPI Trends Q1 2005 - Q4 2021

**TODO: Regexy way to get rid of the '\QX-YYYY -\QX YYYY' tail**



```python
source_df['Table 1']
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
      <th>Table 1: NI House Price Index, Standardised Price and Quarterly and Annual Change</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Back to contents</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Year</td>
      <td>Quarter</td>
      <td>NI House Price Index</td>
      <td>NI House Standardised Price</td>
      <td>Quarterly Change</td>
      <td>Annual Change</td>
      <td>NI</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005</td>
      <td>Q1</td>
      <td>100.883607</td>
      <td>111920.268199</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>Q2</td>
      <td>104.564663</td>
      <td>116004.031639</td>
      <td>0.036488</td>
      <td>NaN</td>
      <td>100</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>Q3</td>
      <td>111.219</td>
      <td>123386.352673</td>
      <td>0.063638</td>
      <td>NaN</td>
      <td>100</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>89</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>90</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>92</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>93</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>94 rows × 8 columns</p>
</div>




```python
def basic_cleanup(df:pd.DataFrame, offset=1)->pd.DataFrame:
    df = df.copy()
    # Re-header from row 1 (which was row 3 in excel)
    new_header = df.iloc[offset]
    df = df.iloc[offset+1:]
    df.columns = new_header

    # remove 'NaN' trailing columns
    df = df[df.columns[pd.notna(df.columns)]]

    # 'NI' is a usually hidden column that appears to be a checksum;
    #if it's all there and all 100, remove it, otherwise, complain.
    # (Note, need to change this 'if' logic to just 'if there's a
    # column with all 100's, but cross that bridge later)
    if 'NI' in df:
        assert df['NI'].all() and df['NI'].mean() == 100, "Not all values in df['NI'] == 100"
        df = df.drop('NI', axis=1)

    # Strip rows below the first all-nan row, if there is one
    # (Otherwise this truncates the tables as there is no
    # idxmax in the table of all 'false's)
    if any(df.isna().all(axis=1)):
        idx_first_bad_row = df.isna().all(axis=1).idxmax()
        df = df.loc[:idx_first_bad_row-1]

    # By Inspection, other tables use 'Sale Year' and 'Sale Quarter'
    if set(df.keys()).issuperset({'Sale Year','Sale Quarter'}):
        df = df.rename(columns = {
            'Sale Year':'Year',
            'Sale Quarter': 'Quarter'
        })

    # For 'Year','Quarter' indexed pages, there is an implied Year
    # in Q2/4, so fill it downwards
    if set(df.keys()).issuperset({'Year','Quarter'}):
        df['Year'] = df['Year'].astype(float).fillna(method='ffill').astype(int)

        # In Pandas we can represent Y/Q combinations as proper datetimes
        #https://stackoverflow.com/questions/53898482/clean-way-to-convert-quarterly-periods-to-datetime-in-pandas
        df.insert(loc=0,
                  column='Period',
                  value=pd.PeriodIndex(df.apply(lambda r:f'{r.Year}-{r.Quarter}', axis=1), freq='Q')
        )

    # reset index, try to fix dtypes, etc, (this should be the last
    # operation before returning!
    df = df.reset_index(drop=True).infer_objects()  

    return df

df = basic_cleanup(source_df['Table 1'])
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
      <th>1</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>NI House Price Index</th>
      <th>NI House Standardised Price</th>
      <th>Quarterly Change</th>
      <th>Annual Change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>100.883607</td>
      <td>111920.268199</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>104.564663</td>
      <td>116004.031639</td>
      <td>0.036488</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>111.219000</td>
      <td>123386.352673</td>
      <td>0.063638</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>115.083964</td>
      <td>127674.143865</td>
      <td>0.034751</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>118.354129</td>
      <td>131302.064422</td>
      <td>0.028415</td>
      <td>0.173175</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>132.931827</td>
      <td>147474.561707</td>
      <td>0.026103</td>
      <td>0.052326</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>134.382831</td>
      <td>149084.306040</td>
      <td>0.010915</td>
      <td>0.059421</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>139.105050</td>
      <td>154323.134643</td>
      <td>0.035140</td>
      <td>0.095724</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>143.346066</td>
      <td>159028.118093</td>
      <td>0.030488</td>
      <td>0.106491</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>143.456594</td>
      <td>159150.737832</td>
      <td>0.000771</td>
      <td>0.079174</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 7 columns</p>
</div>




```python
dest_df = {
    'Table 1': basic_cleanup(source_df['Table 1'])
}
```


```python
len([k for k in source_df.keys() if k.startswith('Table')])
```




    32



One down, 31 to go...

### Table 2: NI HPI & Standardised Price Statistics by Property Type Q4 2021'


```python
df = basic_cleanup(source_df['Table 2'])
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
      <th>1</th>
      <th>Property Type</th>
      <th>Index\n(Quarter 4 2021)</th>
      <th>Percentage Change on Previous Quarter</th>
      <th>Percentage Change over 12 months</th>
      <th>Standardised Price\n(Quarter 4 2021)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Detached</td>
      <td>143.488806</td>
      <td>0.008491</td>
      <td>0.093110</td>
      <td>241131.373512</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Semi-Detached</td>
      <td>140.680694</td>
      <td>0.004211</td>
      <td>0.076953</td>
      <td>153718.543755</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Terrace</td>
      <td>149.564169</td>
      <td>-0.009577</td>
      <td>0.078758</td>
      <td>112831.710806</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Apartment</td>
      <td>133.376791</td>
      <td>-0.014732</td>
      <td>0.032761</td>
      <td>116554.228620</td>
    </tr>
    <tr>
      <th>4</th>
      <td>All</td>
      <td>143.456594</td>
      <td>0.000771</td>
      <td>0.079174</td>
      <td>159150.737832</td>
    </tr>
  </tbody>
</table>
</div>



Those '\n (Quarter 4 2021)' entries are unnecessary, so _for this table_, lets clear them


```python
df.columns = [c.split('\n')[0] for c in df.columns]
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
      <th>Property Type</th>
      <th>Index</th>
      <th>Percentage Change on Previous Quarter</th>
      <th>Percentage Change over 12 months</th>
      <th>Standardised Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Detached</td>
      <td>143.488806</td>
      <td>0.008491</td>
      <td>0.093110</td>
      <td>241131.373512</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Semi-Detached</td>
      <td>140.680694</td>
      <td>0.004211</td>
      <td>0.076953</td>
      <td>153718.543755</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Terrace</td>
      <td>149.564169</td>
      <td>-0.009577</td>
      <td>0.078758</td>
      <td>112831.710806</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Apartment</td>
      <td>133.376791</td>
      <td>-0.014732</td>
      <td>0.032761</td>
      <td>116554.228620</td>
    </tr>
    <tr>
      <th>4</th>
      <td>All</td>
      <td>143.456594</td>
      <td>0.000771</td>
      <td>0.079174</td>
      <td>159150.737832</td>
    </tr>
  </tbody>
</table>
</div>




```python
dest_df['Table 2'] = df
```

### Table 2a: NI Detached Property Price Index Q1 2005 - Q4 2021



```python
df = basic_cleanup(source_df['Table 2a'])
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
      <th>1</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>NI Detached Property Price Index</th>
      <th>NI Detached Property Standardised Price</th>
      <th>Quarterly Change</th>
      <th>Annual Change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>95.465560</td>
      <td>160428.832662</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>100.974498</td>
      <td>169686.542965</td>
      <td>0.057706</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>107.526236</td>
      <td>180696.666810</td>
      <td>0.064885</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>110.279730</td>
      <td>185323.883533</td>
      <td>0.025608</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>112.270506</td>
      <td>188669.361197</td>
      <td>0.018052</td>
      <td>0.176032</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>131.266614</td>
      <td>220592.113069</td>
      <td>0.026393</td>
      <td>0.055357</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>133.814014</td>
      <td>224872.989982</td>
      <td>0.019406</td>
      <td>0.071429</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>139.682380</td>
      <td>234734.715703</td>
      <td>0.043855</td>
      <td>0.129844</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>142.280745</td>
      <td>239101.239764</td>
      <td>0.018602</td>
      <td>0.112515</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>143.488806</td>
      <td>241131.373512</td>
      <td>0.008491</td>
      <td>0.093110</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 7 columns</p>
</div>



### Table 2x: NI XXX Property Price Index Q1 2005 - Q4 2021

This table structure is consistent against the rest of the Table 2x cohort; mapping to the Property Types listed in Table 2.

For the time being, we can ignore these, but this will probably become a pain later on...


```python
dest_df['Table 2']['Property Type']
```




    0         Detached
    1    Semi-Detached
    2          Terrace
    3        Apartment
    4              All
    Name: Property Type, dtype: object




```python
import re

table2s = re.compile('Table 2[a-z]')
assert table2s.match('Table 2') is None, 'Table 2 is matching itself!'
assert table2s.match('Table 20') is None, 'Table 2 is greedy!'
assert table2s.match('Table 2z') is not None, 'Table 2 is matching incorrectly!'
```


```python
table2s = re.compile('Table 2[a-z]')
for table in source_df:
    if table2s.match(table):
        dest_df[table] = basic_cleanup(source_df[table])
```


```python
len(dest_df), len([k for k in source_df.keys() if k.startswith('Table') and k not in dest_df])
```




    (6, 26)



6 down, 26 to go.

### Table 3: NI HPI & Standardised Price Statistics by New/Existing Resold Dwelling Type Q4 2021

These appear to be a similar structure of the Table 2's... hopefully


```python
df = basic_cleanup(source_df['Table 3'])
df.columns = [c.split('\n')[0] for c in df.columns] # Stolen from Table 2 Treatment
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
      <th>Property Type</th>
      <th>Index</th>
      <th>Percentage Change on Previous Quarter</th>
      <th>Percentage Change over 12 months</th>
      <th>Standardised Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>New</td>
      <td>141.769973</td>
      <td>0.024877</td>
      <td>0.072609</td>
      <td>185966.524090</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Existing Resold</td>
      <td>143.518977</td>
      <td>-0.004918</td>
      <td>0.080771</td>
      <td>152275.828046</td>
    </tr>
    <tr>
      <th>2</th>
      <td>All</td>
      <td>143.456594</td>
      <td>0.000771</td>
      <td>0.079174</td>
      <td>159150.737832</td>
    </tr>
  </tbody>
</table>
</div>




```python
dest_df['Table 3'] = df
```


```python
df = basic_cleanup(source_df['Table 3a'])
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
      <th>1</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>NI New Dwellings Price Index</th>
      <th>NI New Dwellings Standardised Price</th>
      <th>Quarterly Change</th>
      <th>Annual Change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>95.804706</td>
      <td>125671.662611</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>101.229223</td>
      <td>132787.263460</td>
      <td>0.056621</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>106.243580</td>
      <td>139364.837967</td>
      <td>0.049535</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>110.118105</td>
      <td>144447.239874</td>
      <td>0.036468</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>113.624410</td>
      <td>149046.629634</td>
      <td>0.031841</td>
      <td>0.186000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>132.173052</td>
      <td>173377.779440</td>
      <td>0.004103</td>
      <td>0.036125</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>133.772562</td>
      <td>175475.933612</td>
      <td>0.012102</td>
      <td>0.027916</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>136.969311</td>
      <td>179669.264190</td>
      <td>0.023897</td>
      <td>0.046474</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>138.328776</td>
      <td>181452.540106</td>
      <td>0.009925</td>
      <td>0.050867</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>141.769973</td>
      <td>185966.524090</td>
      <td>0.024877</td>
      <td>0.072609</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 7 columns</p>
</div>




```python
table3s = re.compile('Table 3[a-z]')
for table in source_df:
    if table3s.match(table):
        dest_df[table] = basic_cleanup(source_df[table])
len(dest_df), len([k for k in source_df.keys() if k.startswith('Table') and k not in dest_df])
```




    (10, 22)



### Table 4: Number of Verified Residential Property Sales Q1 2005 - Q4 2021

Table 4 is not looking great


```python
df = source_df['Table 4']
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
      <th>Table 4: Number of Verified Residential Property Sales</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Verified Sales = Sales matched to a property i...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Please note figures for the 2 most recent quar...</td>
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
      <td>Back to contents</td>
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
      <td>Sale Year</td>
      <td>Sale Quarter</td>
      <td>Detached</td>
      <td>Semi-Detached</td>
      <td>Terrace</td>
      <td>Apartment</td>
      <td>Total</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005\n</td>
      <td>Quarter 1</td>
      <td>809</td>
      <td>894</td>
      <td>1035</td>
      <td>198</td>
      <td>2936</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>84</th>
      <td>2021</td>
      <td>Quarter 1</td>
      <td>2509</td>
      <td>2477</td>
      <td>1962</td>
      <td>561</td>
      <td>7509</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>85</th>
      <td>NaN</td>
      <td>Quarter 2</td>
      <td>2668</td>
      <td>2613</td>
      <td>2056</td>
      <td>604</td>
      <td>7941</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>86</th>
      <td>NaN</td>
      <td>Quarter 3</td>
      <td>2519</td>
      <td>2797</td>
      <td>2220</td>
      <td>633</td>
      <td>8169</td>
      <td>Please note this figure is provisional and wil...</td>
    </tr>
    <tr>
      <th>87</th>
      <td>NaN</td>
      <td>Quarter 4</td>
      <td>1478</td>
      <td>2100</td>
      <td>2057</td>
      <td>515</td>
      <td>6150</td>
      <td>and new dwellings sold in this quarter being a...</td>
    </tr>
    <tr>
      <th>88</th>
      <td>NaN</td>
      <td>2021 Total</td>
      <td>9174</td>
      <td>9987</td>
      <td>8295</td>
      <td>2313</td>
      <td>29769</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>89 rows × 8 columns</p>
</div>



Of note; new offset for the header row at index 3 instead of index 1, due to lots of fluff at the start that is probably not going to be consistent between reports so that will almost certainly mess up my day in a few months.

Also, **Quarter dates** have now been shifted into 'Quarter 1' instead of 'Q1', which ... meh 🤷‍♂️. More Egrigiously, it looks like **'\n' has leaked into some Sales Year values**. Funtimes.

Finally, and possibly most annoying, the introduction of **partial total lines** is going to throw things off, and this isn't a validation study, to stuff-em

In an effort not to over-complicate `basic_cleanup`, we can try and clean these table specific issues first;


```python
df.iloc[:,1]=df.iloc[:,1].str.replace('Quarter ([1-4])',r'Q\1', regex=True)
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
      <th>Table 4: Number of Verified Residential Property Sales</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Verified Sales = Sales matched to a property i...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Please note figures for the 2 most recent quar...</td>
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
      <td>Back to contents</td>
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
      <td>Sale Year</td>
      <td>Sale Quarter</td>
      <td>Detached</td>
      <td>Semi-Detached</td>
      <td>Terrace</td>
      <td>Apartment</td>
      <td>Total</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005\n</td>
      <td>Q1</td>
      <td>809</td>
      <td>894</td>
      <td>1035</td>
      <td>198</td>
      <td>2936</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>84</th>
      <td>2021</td>
      <td>Q1</td>
      <td>2509</td>
      <td>2477</td>
      <td>1962</td>
      <td>561</td>
      <td>7509</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>85</th>
      <td>NaN</td>
      <td>Q2</td>
      <td>2668</td>
      <td>2613</td>
      <td>2056</td>
      <td>604</td>
      <td>7941</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>86</th>
      <td>NaN</td>
      <td>Q3</td>
      <td>2519</td>
      <td>2797</td>
      <td>2220</td>
      <td>633</td>
      <td>8169</td>
      <td>Please note this figure is provisional and wil...</td>
    </tr>
    <tr>
      <th>87</th>
      <td>NaN</td>
      <td>Q4</td>
      <td>1478</td>
      <td>2100</td>
      <td>2057</td>
      <td>515</td>
      <td>6150</td>
      <td>and new dwellings sold in this quarter being a...</td>
    </tr>
    <tr>
      <th>88</th>
      <td>NaN</td>
      <td>2021 Total</td>
      <td>9174</td>
      <td>9987</td>
      <td>8295</td>
      <td>2313</td>
      <td>29769</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>89 rows × 8 columns</p>
</div>




```python
df=df[~df.iloc[:,1].str.contains('Total').fillna(False)]
```


```python
# Lose the year new-lines (needs astype because non str lines are
# correctly inferred to be ints, so .str methods nan-out
with pd.option_context('mode.chained_assignment',None):
    df.iloc[:,0]=df.iloc[:,0].astype(str).str.replace('\n','')
```


```python
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
      <th>Table 4: Number of Verified Residential Property Sales</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Verified Sales = Sales matched to a property i...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Please note figures for the 2 most recent quar...</td>
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
      <td>Back to contents</td>
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
      <td>Sale Year</td>
      <td>Sale Quarter</td>
      <td>Detached</td>
      <td>Semi-Detached</td>
      <td>Terrace</td>
      <td>Apartment</td>
      <td>Total</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005</td>
      <td>Q1</td>
      <td>809</td>
      <td>894</td>
      <td>1035</td>
      <td>198</td>
      <td>2936</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>82</th>
      <td>nan</td>
      <td>Q4</td>
      <td>2808</td>
      <td>2944</td>
      <td>2170</td>
      <td>555</td>
      <td>8477</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>84</th>
      <td>2021</td>
      <td>Q1</td>
      <td>2509</td>
      <td>2477</td>
      <td>1962</td>
      <td>561</td>
      <td>7509</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>85</th>
      <td>nan</td>
      <td>Q2</td>
      <td>2668</td>
      <td>2613</td>
      <td>2056</td>
      <td>604</td>
      <td>7941</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>86</th>
      <td>nan</td>
      <td>Q3</td>
      <td>2519</td>
      <td>2797</td>
      <td>2220</td>
      <td>633</td>
      <td>8169</td>
      <td>Please note this figure is provisional and wil...</td>
    </tr>
    <tr>
      <th>87</th>
      <td>nan</td>
      <td>Q4</td>
      <td>1478</td>
      <td>2100</td>
      <td>2057</td>
      <td>515</td>
      <td>6150</td>
      <td>and new dwellings sold in this quarter being a...</td>
    </tr>
  </tbody>
</table>
<p>72 rows × 8 columns</p>
</div>




```python
basic_cleanup(df, offset=3)
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
      <th>3</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Detached</th>
      <th>Semi-Detached</th>
      <th>Terrace</th>
      <th>Apartment</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>809</td>
      <td>894</td>
      <td>1035</td>
      <td>198</td>
      <td>2936</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>2208</td>
      <td>2474</td>
      <td>2808</td>
      <td>483</td>
      <td>7973</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>2297</td>
      <td>2655</td>
      <td>2952</td>
      <td>539</td>
      <td>8443</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>2498</td>
      <td>3003</td>
      <td>3492</td>
      <td>631</td>
      <td>9624</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>2185</td>
      <td>2650</td>
      <td>3158</td>
      <td>594</td>
      <td>8587</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>2808</td>
      <td>2944</td>
      <td>2170</td>
      <td>555</td>
      <td>8477</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>2509</td>
      <td>2477</td>
      <td>1962</td>
      <td>561</td>
      <td>7509</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>2668</td>
      <td>2613</td>
      <td>2056</td>
      <td>604</td>
      <td>7941</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>2519</td>
      <td>2797</td>
      <td>2220</td>
      <td>633</td>
      <td>8169</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>1478</td>
      <td>2100</td>
      <td>2057</td>
      <td>515</td>
      <td>6150</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 8 columns</p>
</div>



Thats awkward enough to get it's own function...



```python
def cleanup_table_4(df):
    """
    Table 4: Number of Verified Residential Property Sales
    * Regex 'Quarter X' to 'QX' in future 'Sales Quarter' column
    * Drop Year Total rows
    * Clear any Newlines from the future 'Sales Year' column
    * call `basic_cleanup` with offset=3
    """
    df.iloc[:,1]=df.iloc[:,1].str.replace('Quarter ([1-4])',r'Q\1', regex=True)
    df=df[~df.iloc[:,1].str.contains('Total').fillna(False)]
    # Lose the year new-lines (needs astype because non str lines are
    # correctly inferred to be ints, so .str methods nan-out
    with pd.option_context('mode.chained_assignment',None):
        df.iloc[:,0]=df.iloc[:,0].astype(str).str.replace('\n','')
    return basic_cleanup(df, offset=3)

cleanup_table_4(source_df['Table 4'].copy())
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
      <th>3</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Detached</th>
      <th>Semi-Detached</th>
      <th>Terrace</th>
      <th>Apartment</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>809</td>
      <td>894</td>
      <td>1035</td>
      <td>198</td>
      <td>2936</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>2208</td>
      <td>2474</td>
      <td>2808</td>
      <td>483</td>
      <td>7973</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>2297</td>
      <td>2655</td>
      <td>2952</td>
      <td>539</td>
      <td>8443</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>2498</td>
      <td>3003</td>
      <td>3492</td>
      <td>631</td>
      <td>9624</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>2185</td>
      <td>2650</td>
      <td>3158</td>
      <td>594</td>
      <td>8587</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>2808</td>
      <td>2944</td>
      <td>2170</td>
      <td>555</td>
      <td>8477</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>2509</td>
      <td>2477</td>
      <td>1962</td>
      <td>561</td>
      <td>7509</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>2668</td>
      <td>2613</td>
      <td>2056</td>
      <td>604</td>
      <td>7941</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>2519</td>
      <td>2797</td>
      <td>2220</td>
      <td>633</td>
      <td>8169</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>1478</td>
      <td>2100</td>
      <td>2057</td>
      <td>515</td>
      <td>6150</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 8 columns</p>
</div>




```python
dest_df['Table 4'] = cleanup_table_4(source_df['Table 4'])
len(dest_df), len([k for k in source_df.keys() if k.startswith('Table') and k not in dest_df])
```




    (11, 21)



### Table 5: HPI & Standardised Price for each Local Government District in NI

This _nearly works_ but structurally requires a multi-index column to make sense....


```python
df = basic_cleanup(source_df['Table 5'])
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
      <th>1</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Antrim and Newtownabbey HPI</th>
      <th>Antrim and Newtownabbey Standardised Price</th>
      <th>Ards and North Down HPI</th>
      <th>Ards and North Down Standardised Price</th>
      <th>Armagh City, Banbridge and Craigavon HPI</th>
      <th>Armagh City, Banbridge and Craigavon Standardised Price</th>
      <th>Belfast HPI</th>
      <th>...</th>
      <th>Fermanagh and Omagh HPI</th>
      <th>Fermanagh and Omagh Standardised Price</th>
      <th>Lisburn and Castlereagh HPI</th>
      <th>Lisburn and Castlereagh Standardised Price</th>
      <th>Mid and East Antrim HPI</th>
      <th>Mid and East Antrim Standardised Price</th>
      <th>Mid Ulster Standardised HPI</th>
      <th>Mid Ulster Standardised Price</th>
      <th>Newry, Mourne and Down HPI</th>
      <th>Newry, Mourne and Down Standardised Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>99.903277</td>
      <td>114851.528270</td>
      <td>97.150602</td>
      <td>130398.569667</td>
      <td>102.245597</td>
      <td>100785.145986</td>
      <td>99.839849</td>
      <td>...</td>
      <td>109.429237</td>
      <td>104874.980231</td>
      <td>95.958322</td>
      <td>128828.327513</td>
      <td>102.246427</td>
      <td>105865.408901</td>
      <td>102.714778</td>
      <td>114882.211239</td>
      <td>100.810773</td>
      <td>113420.880186</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>99.723509</td>
      <td>114644.862732</td>
      <td>100.794472</td>
      <td>137133.037807</td>
      <td>106.325843</td>
      <td>104807.109982</td>
      <td>100.589870</td>
      <td>...</td>
      <td>117.239850</td>
      <td>112360.529330</td>
      <td>100.164437</td>
      <td>134475.225477</td>
      <td>104.443325</td>
      <td>108140.065924</td>
      <td>110.386311</td>
      <td>123462.501283</td>
      <td>111.965743</td>
      <td>125971.191415</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>107.940849</td>
      <td>124091.740608</td>
      <td>102.167971</td>
      <td>137133.037807</td>
      <td>110.006212</td>
      <td>108434.910333</td>
      <td>109.614861</td>
      <td>...</td>
      <td>125.900145</td>
      <td>120660.397585</td>
      <td>106.757895</td>
      <td>143327.237126</td>
      <td>112.748278</td>
      <td>116738.970434</td>
      <td>117.595723</td>
      <td>131525.929577</td>
      <td>117.235685</td>
      <td>131900.333698</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>111.934696</td>
      <td>128683.175719</td>
      <td>106.396379</td>
      <td>142808.538807</td>
      <td>116.073031</td>
      <td>114415.072260</td>
      <td>110.728237</td>
      <td>...</td>
      <td>130.781315</td>
      <td>125338.422216</td>
      <td>111.307116</td>
      <td>149434.769200</td>
      <td>114.584090</td>
      <td>118639.759900</td>
      <td>121.851999</td>
      <td>136286.397473</td>
      <td>123.628047</td>
      <td>139092.296651</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>113.494351</td>
      <td>130476.197845</td>
      <td>109.206160</td>
      <td>146579.915492</td>
      <td>121.831058</td>
      <td>120090.852733</td>
      <td>112.326582</td>
      <td>...</td>
      <td>135.555749</td>
      <td>129914.152078</td>
      <td>110.539212</td>
      <td>148403.823796</td>
      <td>115.878975</td>
      <td>119980.477260</td>
      <td>129.544702</td>
      <td>144890.365875</td>
      <td>127.449613</td>
      <td>143391.890242</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>131.045293</td>
      <td>150653.238745</td>
      <td>123.824862</td>
      <td>166201.593253</td>
      <td>130.857866</td>
      <td>128988.723586</td>
      <td>133.525177</td>
      <td>...</td>
      <td>142.381814</td>
      <td>136456.127817</td>
      <td>129.797418</td>
      <td>174258.823716</td>
      <td>130.813697</td>
      <td>135443.809729</td>
      <td>124.617456</td>
      <td>139379.446212</td>
      <td>138.815696</td>
      <td>156179.721555</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>133.481101</td>
      <td>153453.510344</td>
      <td>128.398202</td>
      <td>172340.072904</td>
      <td>130.382658</td>
      <td>128520.303209</td>
      <td>135.257679</td>
      <td>...</td>
      <td>141.464114</td>
      <td>135576.621629</td>
      <td>131.166305</td>
      <td>176096.615474</td>
      <td>131.268719</td>
      <td>135914.936888</td>
      <td>127.657615</td>
      <td>142779.737045</td>
      <td>138.481347</td>
      <td>155803.549899</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>137.827568</td>
      <td>158450.326506</td>
      <td>130.543464</td>
      <td>175219.510303</td>
      <td>137.439265</td>
      <td>135476.115278</td>
      <td>138.558752</td>
      <td>...</td>
      <td>146.059468</td>
      <td>139980.724158</td>
      <td>134.815374</td>
      <td>180995.654429</td>
      <td>138.663140</td>
      <td>143571.081234</td>
      <td>129.231669</td>
      <td>144540.250870</td>
      <td>145.000829</td>
      <td>163138.533592</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>141.167257</td>
      <td>162289.724156</td>
      <td>134.116570</td>
      <td>180015.444071</td>
      <td>143.522521</td>
      <td>141472.480114</td>
      <td>142.250634</td>
      <td>...</td>
      <td>149.743153</td>
      <td>143511.101233</td>
      <td>136.178634</td>
      <td>182825.891020</td>
      <td>140.051373</td>
      <td>145008.450168</td>
      <td>135.759680</td>
      <td>151841.560426</td>
      <td>152.177814</td>
      <td>171213.265699</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>141.900751</td>
      <td>163132.969278</td>
      <td>134.883745</td>
      <td>181045.170599</td>
      <td>140.957739</td>
      <td>138944.332704</td>
      <td>140.072076</td>
      <td>...</td>
      <td>156.033991</td>
      <td>149540.124905</td>
      <td>137.683726</td>
      <td>184846.544332</td>
      <td>141.311289</td>
      <td>146312.960523</td>
      <td>136.847809</td>
      <td>153058.587031</td>
      <td>152.044892</td>
      <td>171063.717288</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 25 columns</p>
</div>




```python
# Two inner-columns per LGD
lgds = df.columns[3:].str.replace(' HPI','').str.replace(' Standardised Price','').unique()
lgds
```




    Index(['Antrim and Newtownabbey', 'Ards and North Down',
           'Armagh City, Banbridge and Craigavon', 'Belfast',
           'Causeway Coast and Glens', 'Derry City and Strabane',
           'Fermanagh and Omagh', 'Lisburn and Castlereagh', 'Mid and East Antrim',
           'Mid Ulster Standardised', 'Mid Ulster', 'Newry, Mourne and Down'],
          dtype='object', name=1)



For some reason; Mid-ulster has a 'Standardised HPI' which throws off the above trick, so we gotta make it ugly...


```python
lgds = df.columns[3:].str.replace(' Standardised HPI',' HPI')\
    .str.replace(' HPI','')\
    .str.replace(' Standardised Price','').unique()
lgds
```




    Index(['Antrim and Newtownabbey', 'Ards and North Down',
           'Armagh City, Banbridge and Craigavon', 'Belfast',
           'Causeway Coast and Glens', 'Derry City and Strabane',
           'Fermanagh and Omagh', 'Lisburn and Castlereagh', 'Mid and East Antrim',
           'Mid Ulster', 'Newry, Mourne and Down'],
          dtype='object', name=1)




```python
df.columns = [*df.columns[:3], *pd.MultiIndex.from_product([lgds,['Index','Price']], names=['LGD','Metric'])]
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
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>(Antrim and Newtownabbey, Index)</th>
      <th>(Antrim and Newtownabbey, Price)</th>
      <th>(Ards and North Down, Index)</th>
      <th>(Ards and North Down, Price)</th>
      <th>(Armagh City, Banbridge and Craigavon, Index)</th>
      <th>(Armagh City, Banbridge and Craigavon, Price)</th>
      <th>(Belfast, Index)</th>
      <th>...</th>
      <th>(Fermanagh and Omagh, Index)</th>
      <th>(Fermanagh and Omagh, Price)</th>
      <th>(Lisburn and Castlereagh, Index)</th>
      <th>(Lisburn and Castlereagh, Price)</th>
      <th>(Mid and East Antrim, Index)</th>
      <th>(Mid and East Antrim, Price)</th>
      <th>(Mid Ulster, Index)</th>
      <th>(Mid Ulster, Price)</th>
      <th>(Newry, Mourne and Down, Index)</th>
      <th>(Newry, Mourne and Down, Price)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>99.903277</td>
      <td>114851.528270</td>
      <td>97.150602</td>
      <td>130398.569667</td>
      <td>102.245597</td>
      <td>100785.145986</td>
      <td>99.839849</td>
      <td>...</td>
      <td>109.429237</td>
      <td>104874.980231</td>
      <td>95.958322</td>
      <td>128828.327513</td>
      <td>102.246427</td>
      <td>105865.408901</td>
      <td>102.714778</td>
      <td>114882.211239</td>
      <td>100.810773</td>
      <td>113420.880186</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>99.723509</td>
      <td>114644.862732</td>
      <td>100.794472</td>
      <td>137133.037807</td>
      <td>106.325843</td>
      <td>104807.109982</td>
      <td>100.589870</td>
      <td>...</td>
      <td>117.239850</td>
      <td>112360.529330</td>
      <td>100.164437</td>
      <td>134475.225477</td>
      <td>104.443325</td>
      <td>108140.065924</td>
      <td>110.386311</td>
      <td>123462.501283</td>
      <td>111.965743</td>
      <td>125971.191415</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>107.940849</td>
      <td>124091.740608</td>
      <td>102.167971</td>
      <td>137133.037807</td>
      <td>110.006212</td>
      <td>108434.910333</td>
      <td>109.614861</td>
      <td>...</td>
      <td>125.900145</td>
      <td>120660.397585</td>
      <td>106.757895</td>
      <td>143327.237126</td>
      <td>112.748278</td>
      <td>116738.970434</td>
      <td>117.595723</td>
      <td>131525.929577</td>
      <td>117.235685</td>
      <td>131900.333698</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>111.934696</td>
      <td>128683.175719</td>
      <td>106.396379</td>
      <td>142808.538807</td>
      <td>116.073031</td>
      <td>114415.072260</td>
      <td>110.728237</td>
      <td>...</td>
      <td>130.781315</td>
      <td>125338.422216</td>
      <td>111.307116</td>
      <td>149434.769200</td>
      <td>114.584090</td>
      <td>118639.759900</td>
      <td>121.851999</td>
      <td>136286.397473</td>
      <td>123.628047</td>
      <td>139092.296651</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>113.494351</td>
      <td>130476.197845</td>
      <td>109.206160</td>
      <td>146579.915492</td>
      <td>121.831058</td>
      <td>120090.852733</td>
      <td>112.326582</td>
      <td>...</td>
      <td>135.555749</td>
      <td>129914.152078</td>
      <td>110.539212</td>
      <td>148403.823796</td>
      <td>115.878975</td>
      <td>119980.477260</td>
      <td>129.544702</td>
      <td>144890.365875</td>
      <td>127.449613</td>
      <td>143391.890242</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>131.045293</td>
      <td>150653.238745</td>
      <td>123.824862</td>
      <td>166201.593253</td>
      <td>130.857866</td>
      <td>128988.723586</td>
      <td>133.525177</td>
      <td>...</td>
      <td>142.381814</td>
      <td>136456.127817</td>
      <td>129.797418</td>
      <td>174258.823716</td>
      <td>130.813697</td>
      <td>135443.809729</td>
      <td>124.617456</td>
      <td>139379.446212</td>
      <td>138.815696</td>
      <td>156179.721555</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>133.481101</td>
      <td>153453.510344</td>
      <td>128.398202</td>
      <td>172340.072904</td>
      <td>130.382658</td>
      <td>128520.303209</td>
      <td>135.257679</td>
      <td>...</td>
      <td>141.464114</td>
      <td>135576.621629</td>
      <td>131.166305</td>
      <td>176096.615474</td>
      <td>131.268719</td>
      <td>135914.936888</td>
      <td>127.657615</td>
      <td>142779.737045</td>
      <td>138.481347</td>
      <td>155803.549899</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>137.827568</td>
      <td>158450.326506</td>
      <td>130.543464</td>
      <td>175219.510303</td>
      <td>137.439265</td>
      <td>135476.115278</td>
      <td>138.558752</td>
      <td>...</td>
      <td>146.059468</td>
      <td>139980.724158</td>
      <td>134.815374</td>
      <td>180995.654429</td>
      <td>138.663140</td>
      <td>143571.081234</td>
      <td>129.231669</td>
      <td>144540.250870</td>
      <td>145.000829</td>
      <td>163138.533592</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>141.167257</td>
      <td>162289.724156</td>
      <td>134.116570</td>
      <td>180015.444071</td>
      <td>143.522521</td>
      <td>141472.480114</td>
      <td>142.250634</td>
      <td>...</td>
      <td>149.743153</td>
      <td>143511.101233</td>
      <td>136.178634</td>
      <td>182825.891020</td>
      <td>140.051373</td>
      <td>145008.450168</td>
      <td>135.759680</td>
      <td>151841.560426</td>
      <td>152.177814</td>
      <td>171213.265699</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>141.900751</td>
      <td>163132.969278</td>
      <td>134.883745</td>
      <td>181045.170599</td>
      <td>140.957739</td>
      <td>138944.332704</td>
      <td>140.072076</td>
      <td>...</td>
      <td>156.033991</td>
      <td>149540.124905</td>
      <td>137.683726</td>
      <td>184846.544332</td>
      <td>141.311289</td>
      <td>146312.960523</td>
      <td>136.847809</td>
      <td>153058.587031</td>
      <td>152.044892</td>
      <td>171063.717288</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 25 columns</p>
</div>



We _could_ turn this into a proper multiindex but it would mean pushing the Period/Year/Quarter columns into keys which would be inconsistent behaviour with the rest of the 'cleaned' dataset, so that can be a downstream problem; at least we've got the relevant metrics consistent!


```python
def cleanup_table_5(df):
    """
    Table 5: Standardised House Price & Index for each Local Government District Northern Ireland
    *
    """
    # Basic Cleanup first
    df = basic_cleanup(df)
    # Build multi-index of LGD / Metric [Index,Price]
    # Two inner-columns per LGD
    lgds = df.columns[3:].str.replace(' Standardised HPI',' HPI')\
        .str.replace(' HPI','')\
        .str.replace(' Standardised Price','')\
        .unique()
    df.columns = [*df.columns[:3], *pd.MultiIndex.from_product([lgds,['Index','Price']], names=['LGD','Metric'])]
    return df

cleanup_table_5(source_df['Table 5'])
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
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>(Antrim and Newtownabbey, Index)</th>
      <th>(Antrim and Newtownabbey, Price)</th>
      <th>(Ards and North Down, Index)</th>
      <th>(Ards and North Down, Price)</th>
      <th>(Armagh City, Banbridge and Craigavon, Index)</th>
      <th>(Armagh City, Banbridge and Craigavon, Price)</th>
      <th>(Belfast, Index)</th>
      <th>...</th>
      <th>(Fermanagh and Omagh, Index)</th>
      <th>(Fermanagh and Omagh, Price)</th>
      <th>(Lisburn and Castlereagh, Index)</th>
      <th>(Lisburn and Castlereagh, Price)</th>
      <th>(Mid and East Antrim, Index)</th>
      <th>(Mid and East Antrim, Price)</th>
      <th>(Mid Ulster, Index)</th>
      <th>(Mid Ulster, Price)</th>
      <th>(Newry, Mourne and Down, Index)</th>
      <th>(Newry, Mourne and Down, Price)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>99.903277</td>
      <td>114851.528270</td>
      <td>97.150602</td>
      <td>130398.569667</td>
      <td>102.245597</td>
      <td>100785.145986</td>
      <td>99.839849</td>
      <td>...</td>
      <td>109.429237</td>
      <td>104874.980231</td>
      <td>95.958322</td>
      <td>128828.327513</td>
      <td>102.246427</td>
      <td>105865.408901</td>
      <td>102.714778</td>
      <td>114882.211239</td>
      <td>100.810773</td>
      <td>113420.880186</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>99.723509</td>
      <td>114644.862732</td>
      <td>100.794472</td>
      <td>137133.037807</td>
      <td>106.325843</td>
      <td>104807.109982</td>
      <td>100.589870</td>
      <td>...</td>
      <td>117.239850</td>
      <td>112360.529330</td>
      <td>100.164437</td>
      <td>134475.225477</td>
      <td>104.443325</td>
      <td>108140.065924</td>
      <td>110.386311</td>
      <td>123462.501283</td>
      <td>111.965743</td>
      <td>125971.191415</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>107.940849</td>
      <td>124091.740608</td>
      <td>102.167971</td>
      <td>137133.037807</td>
      <td>110.006212</td>
      <td>108434.910333</td>
      <td>109.614861</td>
      <td>...</td>
      <td>125.900145</td>
      <td>120660.397585</td>
      <td>106.757895</td>
      <td>143327.237126</td>
      <td>112.748278</td>
      <td>116738.970434</td>
      <td>117.595723</td>
      <td>131525.929577</td>
      <td>117.235685</td>
      <td>131900.333698</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>111.934696</td>
      <td>128683.175719</td>
      <td>106.396379</td>
      <td>142808.538807</td>
      <td>116.073031</td>
      <td>114415.072260</td>
      <td>110.728237</td>
      <td>...</td>
      <td>130.781315</td>
      <td>125338.422216</td>
      <td>111.307116</td>
      <td>149434.769200</td>
      <td>114.584090</td>
      <td>118639.759900</td>
      <td>121.851999</td>
      <td>136286.397473</td>
      <td>123.628047</td>
      <td>139092.296651</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>113.494351</td>
      <td>130476.197845</td>
      <td>109.206160</td>
      <td>146579.915492</td>
      <td>121.831058</td>
      <td>120090.852733</td>
      <td>112.326582</td>
      <td>...</td>
      <td>135.555749</td>
      <td>129914.152078</td>
      <td>110.539212</td>
      <td>148403.823796</td>
      <td>115.878975</td>
      <td>119980.477260</td>
      <td>129.544702</td>
      <td>144890.365875</td>
      <td>127.449613</td>
      <td>143391.890242</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>131.045293</td>
      <td>150653.238745</td>
      <td>123.824862</td>
      <td>166201.593253</td>
      <td>130.857866</td>
      <td>128988.723586</td>
      <td>133.525177</td>
      <td>...</td>
      <td>142.381814</td>
      <td>136456.127817</td>
      <td>129.797418</td>
      <td>174258.823716</td>
      <td>130.813697</td>
      <td>135443.809729</td>
      <td>124.617456</td>
      <td>139379.446212</td>
      <td>138.815696</td>
      <td>156179.721555</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>133.481101</td>
      <td>153453.510344</td>
      <td>128.398202</td>
      <td>172340.072904</td>
      <td>130.382658</td>
      <td>128520.303209</td>
      <td>135.257679</td>
      <td>...</td>
      <td>141.464114</td>
      <td>135576.621629</td>
      <td>131.166305</td>
      <td>176096.615474</td>
      <td>131.268719</td>
      <td>135914.936888</td>
      <td>127.657615</td>
      <td>142779.737045</td>
      <td>138.481347</td>
      <td>155803.549899</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>137.827568</td>
      <td>158450.326506</td>
      <td>130.543464</td>
      <td>175219.510303</td>
      <td>137.439265</td>
      <td>135476.115278</td>
      <td>138.558752</td>
      <td>...</td>
      <td>146.059468</td>
      <td>139980.724158</td>
      <td>134.815374</td>
      <td>180995.654429</td>
      <td>138.663140</td>
      <td>143571.081234</td>
      <td>129.231669</td>
      <td>144540.250870</td>
      <td>145.000829</td>
      <td>163138.533592</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>141.167257</td>
      <td>162289.724156</td>
      <td>134.116570</td>
      <td>180015.444071</td>
      <td>143.522521</td>
      <td>141472.480114</td>
      <td>142.250634</td>
      <td>...</td>
      <td>149.743153</td>
      <td>143511.101233</td>
      <td>136.178634</td>
      <td>182825.891020</td>
      <td>140.051373</td>
      <td>145008.450168</td>
      <td>135.759680</td>
      <td>151841.560426</td>
      <td>152.177814</td>
      <td>171213.265699</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>141.900751</td>
      <td>163132.969278</td>
      <td>134.883745</td>
      <td>181045.170599</td>
      <td>140.957739</td>
      <td>138944.332704</td>
      <td>140.072076</td>
      <td>...</td>
      <td>156.033991</td>
      <td>149540.124905</td>
      <td>137.683726</td>
      <td>184846.544332</td>
      <td>141.311289</td>
      <td>146312.960523</td>
      <td>136.847809</td>
      <td>153058.587031</td>
      <td>152.044892</td>
      <td>171063.717288</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 25 columns</p>
</div>




```python
dest_df['Table 5']=cleanup_table_5(source_df['Table 5'])
len(dest_df), len([k for k in source_df.keys() if k.startswith('Table') and k not in dest_df])
```




    (12, 20)



### Table 5a: Number of Verified Residential Property Sales by Local Government District

This one has a new problem; the Sale Year/Quarter is now squished together. This will do a few terrible things to our `basic_cleanup` so this needs to be done ahead of cleanup.
Also has annual total lines.


```python
df = source_df['Table 5a'].copy()
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
      <th>Table 5a: Number of Verified Residential Property Sales by Local Government District</th>
      <th>Unnamed: 1</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Please note figures for the 2 most recent quar...</td>
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
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Back to contents</td>
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
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sale Year/Quarter</td>
      <td>Antrim and Newtownabbey</td>
      <td>Ards and North Down</td>
      <td>Armagh City, Banbridge and Craigavon</td>
      <td>Belfast</td>
      <td>Causeway Coast and Glens</td>
      <td>Derry City and Strabane</td>
      <td>Fermanagh and Omagh</td>
      <td>Lisburn and Castlereagh</td>
      <td>Mid and East Antrim</td>
      <td>Mid Ulster</td>
      <td>Newry, Mourne and Down</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Q1 2005</td>
      <td>236</td>
      <td>320</td>
      <td>333</td>
      <td>623</td>
      <td>236</td>
      <td>226</td>
      <td>138</td>
      <td>219</td>
      <td>188</td>
      <td>176</td>
      <td>241</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Q2 2005</td>
      <td>735</td>
      <td>857</td>
      <td>961</td>
      <td>1549</td>
      <td>712</td>
      <td>637</td>
      <td>316</td>
      <td>655</td>
      <td>618</td>
      <td>428</td>
      <td>505</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Q3 2021</td>
      <td>739</td>
      <td>989</td>
      <td>931</td>
      <td>1584</td>
      <td>625</td>
      <td>485</td>
      <td>325</td>
      <td>869</td>
      <td>671</td>
      <td>377</td>
      <td>574</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Q4 2021</td>
      <td>532</td>
      <td>702</td>
      <td>730</td>
      <td>1272</td>
      <td>417</td>
      <td>405</td>
      <td>250</td>
      <td>572</td>
      <td>474</td>
      <td>359</td>
      <td>437</td>
    </tr>
    <tr>
      <th>87</th>
      <td>2021 Total</td>
      <td>2647</td>
      <td>3685</td>
      <td>3333</td>
      <td>5934</td>
      <td>2327</td>
      <td>1803</td>
      <td>1181</td>
      <td>3053</td>
      <td>2346</td>
      <td>1460</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>88</th>
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
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Please note figures for the 2 most recent quar...</td>
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
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>90 rows × 12 columns</p>
</div>




```python
dates = df.iloc[:,0].str.extract('(Q[1-4]) ([0-9]{4})').rename(columns={0:'Quarter',1:'Year'})
for c in ['Quarter','Year']:# insert the dates in order, so they come out in reverse in the insert
    df.insert(1,c,dates[c])
    df.iloc[2,1]=c # Need to have the right colname for when `basic_cleanup` is called.

```


```python
df.iloc[2,1]=c
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
      <th>Table 5a: Number of Verified Residential Property Sales by Local Government District</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Unnamed: 1</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Please note figures for the 2 most recent quar...</td>
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
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Back to contents</td>
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
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sale Year/Quarter</td>
      <td>Year</td>
      <td>Quarter</td>
      <td>Antrim and Newtownabbey</td>
      <td>Ards and North Down</td>
      <td>Armagh City, Banbridge and Craigavon</td>
      <td>Belfast</td>
      <td>Causeway Coast and Glens</td>
      <td>Derry City and Strabane</td>
      <td>Fermanagh and Omagh</td>
      <td>Lisburn and Castlereagh</td>
      <td>Mid and East Antrim</td>
      <td>Mid Ulster</td>
      <td>Newry, Mourne and Down</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Q1 2005</td>
      <td>2005</td>
      <td>Q1</td>
      <td>236</td>
      <td>320</td>
      <td>333</td>
      <td>623</td>
      <td>236</td>
      <td>226</td>
      <td>138</td>
      <td>219</td>
      <td>188</td>
      <td>176</td>
      <td>241</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Q2 2005</td>
      <td>2005</td>
      <td>Q2</td>
      <td>735</td>
      <td>857</td>
      <td>961</td>
      <td>1549</td>
      <td>712</td>
      <td>637</td>
      <td>316</td>
      <td>655</td>
      <td>618</td>
      <td>428</td>
      <td>505</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Q3 2021</td>
      <td>2021</td>
      <td>Q3</td>
      <td>739</td>
      <td>989</td>
      <td>931</td>
      <td>1584</td>
      <td>625</td>
      <td>485</td>
      <td>325</td>
      <td>869</td>
      <td>671</td>
      <td>377</td>
      <td>574</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Q4 2021</td>
      <td>2021</td>
      <td>Q4</td>
      <td>532</td>
      <td>702</td>
      <td>730</td>
      <td>1272</td>
      <td>417</td>
      <td>405</td>
      <td>250</td>
      <td>572</td>
      <td>474</td>
      <td>359</td>
      <td>437</td>
    </tr>
    <tr>
      <th>87</th>
      <td>2021 Total</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2647</td>
      <td>3685</td>
      <td>3333</td>
      <td>5934</td>
      <td>2327</td>
      <td>1803</td>
      <td>1181</td>
      <td>3053</td>
      <td>2346</td>
      <td>1460</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>88</th>
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
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Please note figures for the 2 most recent quar...</td>
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
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>90 rows × 14 columns</p>
</div>




```python
df=df[~df.iloc[:,0].str.contains('Total').fillna(False)]
```

df.iloc[1,2]=c


```python
basic_cleanup(df,offset=2)
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
      <th>2</th>
      <th>Period</th>
      <th>Sale Year/Quarter</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Antrim and Newtownabbey</th>
      <th>Ards and North Down</th>
      <th>Armagh City, Banbridge and Craigavon</th>
      <th>Belfast</th>
      <th>Causeway Coast and Glens</th>
      <th>Derry City and Strabane</th>
      <th>Fermanagh and Omagh</th>
      <th>Lisburn and Castlereagh</th>
      <th>Mid and East Antrim</th>
      <th>Mid Ulster</th>
      <th>Newry, Mourne and Down</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>Q1 2005</td>
      <td>2005</td>
      <td>Q1</td>
      <td>236</td>
      <td>320</td>
      <td>333</td>
      <td>623</td>
      <td>236</td>
      <td>226</td>
      <td>138</td>
      <td>219</td>
      <td>188</td>
      <td>176</td>
      <td>241</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>Q2 2005</td>
      <td>2005</td>
      <td>Q2</td>
      <td>735</td>
      <td>857</td>
      <td>961</td>
      <td>1549</td>
      <td>712</td>
      <td>637</td>
      <td>316</td>
      <td>655</td>
      <td>618</td>
      <td>428</td>
      <td>505</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>Q3 2005</td>
      <td>2005</td>
      <td>Q3</td>
      <td>757</td>
      <td>960</td>
      <td>968</td>
      <td>1722</td>
      <td>714</td>
      <td>632</td>
      <td>365</td>
      <td>654</td>
      <td>686</td>
      <td>403</td>
      <td>582</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>Q4 2005</td>
      <td>2005</td>
      <td>Q4</td>
      <td>893</td>
      <td>995</td>
      <td>1199</td>
      <td>1943</td>
      <td>834</td>
      <td>746</td>
      <td>385</td>
      <td>670</td>
      <td>759</td>
      <td>489</td>
      <td>711</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>Q1 2006</td>
      <td>2006</td>
      <td>Q1</td>
      <td>761</td>
      <td>933</td>
      <td>1038</td>
      <td>1686</td>
      <td>763</td>
      <td>708</td>
      <td>348</td>
      <td>600</td>
      <td>668</td>
      <td>515</td>
      <td>567</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>Q4 2020</td>
      <td>2020</td>
      <td>Q4</td>
      <td>756</td>
      <td>1052</td>
      <td>974</td>
      <td>1565</td>
      <td>728</td>
      <td>496</td>
      <td>336</td>
      <td>830</td>
      <td>685</td>
      <td>419</td>
      <td>636</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>Q1 2021</td>
      <td>2021</td>
      <td>Q1</td>
      <td>652</td>
      <td>976</td>
      <td>849</td>
      <td>1497</td>
      <td>610</td>
      <td>466</td>
      <td>290</td>
      <td>762</td>
      <td>572</td>
      <td>349</td>
      <td>486</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>Q2 2021</td>
      <td>2021</td>
      <td>Q2</td>
      <td>724</td>
      <td>1018</td>
      <td>823</td>
      <td>1581</td>
      <td>675</td>
      <td>447</td>
      <td>316</td>
      <td>850</td>
      <td>629</td>
      <td>375</td>
      <td>503</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>Q3 2021</td>
      <td>2021</td>
      <td>Q3</td>
      <td>739</td>
      <td>989</td>
      <td>931</td>
      <td>1584</td>
      <td>625</td>
      <td>485</td>
      <td>325</td>
      <td>869</td>
      <td>671</td>
      <td>377</td>
      <td>574</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>Q4 2021</td>
      <td>2021</td>
      <td>Q4</td>
      <td>532</td>
      <td>702</td>
      <td>730</td>
      <td>1272</td>
      <td>417</td>
      <td>405</td>
      <td>250</td>
      <td>572</td>
      <td>474</td>
      <td>359</td>
      <td>437</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 15 columns</p>
</div>




```python
def cleanup_table_5a(df):
    """
    Table 5a: Number of Verified Residential Property Sales by Local Government District
    * Parse the 'Sale Year/Quarter' to two separate cols
    * Insert future-headers for Quarter and Year cols
    * Remove rows with 'total' in the first column
    * Disregard the 'Sale Year/Quarter' column
    * perform `basic_cleanup` with offset=2
    """
    # Safety first
    df=df.copy()

    # Extract 'Quarter' and 'Year' columns from the future 'Sale Year/Quarter' column
    dates = df.iloc[:,0].str.extract('(Q[1-4]) ([0-9]{4})').rename(columns={0:'Quarter',1:'Year'})
    for c in ['Quarter','Year']:# insert the dates in order, so they come out in reverse in the insert
        df.insert(1,c,dates[c])
        df.iloc[2,1]=c # Need to have the right colname for when `basic_cleanup` is called.

    # Remove 'total' rows from the future 'Sale Year/Quarter' column
    df=df[~df.iloc[:,0].str.contains('Total').fillna(False)]

    # Remove the 'Sale Year/Quarter' column all together
    df = df.iloc[:,1:]

    # Standard cleanup
    df = basic_cleanup(df, offset=2)

    return df

cleanup_table_5a(source_df['Table 5a'])
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
      <th>2</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Antrim and Newtownabbey</th>
      <th>Ards and North Down</th>
      <th>Armagh City, Banbridge and Craigavon</th>
      <th>Belfast</th>
      <th>Causeway Coast and Glens</th>
      <th>Derry City and Strabane</th>
      <th>Fermanagh and Omagh</th>
      <th>Lisburn and Castlereagh</th>
      <th>Mid and East Antrim</th>
      <th>Mid Ulster</th>
      <th>Newry, Mourne and Down</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>236</td>
      <td>320</td>
      <td>333</td>
      <td>623</td>
      <td>236</td>
      <td>226</td>
      <td>138</td>
      <td>219</td>
      <td>188</td>
      <td>176</td>
      <td>241</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>735</td>
      <td>857</td>
      <td>961</td>
      <td>1549</td>
      <td>712</td>
      <td>637</td>
      <td>316</td>
      <td>655</td>
      <td>618</td>
      <td>428</td>
      <td>505</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>757</td>
      <td>960</td>
      <td>968</td>
      <td>1722</td>
      <td>714</td>
      <td>632</td>
      <td>365</td>
      <td>654</td>
      <td>686</td>
      <td>403</td>
      <td>582</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>893</td>
      <td>995</td>
      <td>1199</td>
      <td>1943</td>
      <td>834</td>
      <td>746</td>
      <td>385</td>
      <td>670</td>
      <td>759</td>
      <td>489</td>
      <td>711</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>761</td>
      <td>933</td>
      <td>1038</td>
      <td>1686</td>
      <td>763</td>
      <td>708</td>
      <td>348</td>
      <td>600</td>
      <td>668</td>
      <td>515</td>
      <td>567</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>756</td>
      <td>1052</td>
      <td>974</td>
      <td>1565</td>
      <td>728</td>
      <td>496</td>
      <td>336</td>
      <td>830</td>
      <td>685</td>
      <td>419</td>
      <td>636</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>652</td>
      <td>976</td>
      <td>849</td>
      <td>1497</td>
      <td>610</td>
      <td>466</td>
      <td>290</td>
      <td>762</td>
      <td>572</td>
      <td>349</td>
      <td>486</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>724</td>
      <td>1018</td>
      <td>823</td>
      <td>1581</td>
      <td>675</td>
      <td>447</td>
      <td>316</td>
      <td>850</td>
      <td>629</td>
      <td>375</td>
      <td>503</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>739</td>
      <td>989</td>
      <td>931</td>
      <td>1584</td>
      <td>625</td>
      <td>485</td>
      <td>325</td>
      <td>869</td>
      <td>671</td>
      <td>377</td>
      <td>574</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>532</td>
      <td>702</td>
      <td>730</td>
      <td>1272</td>
      <td>417</td>
      <td>405</td>
      <td>250</td>
      <td>572</td>
      <td>474</td>
      <td>359</td>
      <td>437</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 14 columns</p>
</div>




```python
dest_df['Table 5a']=cleanup_table_5a(source_df['Table 5a'])
len(dest_df), len([k for k in source_df.keys() if k.startswith('Table') and k not in dest_df])
```




    (13, 19)



### Table 6: Standardised House Price & Index for all Urban and Rural areas in NI

Wee buns, thankfully. Still mixing the 'HPI' vs 'Index', but that's a downstream problem


```python
df = basic_cleanup(source_df['Table 6'])
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
      <th>1</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Urban Areas HPI</th>
      <th>Urban Areas Standardised Price</th>
      <th>Rural Areas HPI</th>
      <th>Rural Areas Standardised Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>101.309947</td>
      <td>107723.320891</td>
      <td>100.109860</td>
      <td>124292.601178</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>104.402908</td>
      <td>111012.079786</td>
      <td>105.467951</td>
      <td>138865.721275</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>111.163485</td>
      <td>118200.631818</td>
      <td>111.847591</td>
      <td>138865.721275</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>114.871996</td>
      <td>122143.908606</td>
      <td>116.175119</td>
      <td>144238.615701</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>118.187559</td>
      <td>125669.361667</td>
      <td>119.329374</td>
      <td>148154.818847</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>132.610763</td>
      <td>141005.619094</td>
      <td>133.854953</td>
      <td>166189.226014</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>134.077654</td>
      <td>142565.370205</td>
      <td>135.267264</td>
      <td>167942.698911</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>138.575881</td>
      <td>147348.355880</td>
      <td>140.501443</td>
      <td>174441.256673</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>142.840470</td>
      <td>151882.912133</td>
      <td>144.695321</td>
      <td>179648.216283</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>142.375033</td>
      <td>151388.010443</td>
      <td>146.115278</td>
      <td>181411.180623</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 7 columns</p>
</div>




```python
dest_df['Table 6']=basic_cleanup(source_df['Table 6'])
len(dest_df), len([k for k in source_df.keys() if k.startswith('Table') and k not in dest_df])
```




    (14, 18)



### Table 7: Standardised House Price & Index for Rural Areas of Northern Ireland by drive times

Nearly-wee-buns; but this one doesn't have Year or Quarter headers, and the extra `\n (Ref: Q1 2015)` added, which will complicate downstream analysis if that changes over time...


```python
df = source_df['Table 7'].copy()
df.head()
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
      <th>Table 7: Standardised House Price &amp; Index for Rural Areas of Northern Ireland by drive times</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>Unnamed: 10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Back to contents</td>
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
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Drive time within 20mins of town of 10,000 or ...</td>
      <td>Drive time within 20mins of town of 10,000 or ...</td>
      <td>Drive time outside 20mins of town of 10,000 or...</td>
      <td>Drive time outside 20mins of town of 10,000 or...</td>
      <td>Drive time within 1hr of Belfast Index</td>
      <td>Drive time within 1hr of Belfast  Price\n(Ref:...</td>
      <td>Drive time outside 1hr of Belfast Index</td>
      <td>Drive time outside 1hr of Belfast  Price\n(Ref...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>Q1</td>
      <td>100</td>
      <td>124898.676844</td>
      <td>100</td>
      <td>122528.427865</td>
      <td>100</td>
      <td>128955.274996</td>
      <td>100</td>
      <td>111866.40498</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>Q2</td>
      <td>103.166882</td>
      <td>128854.070701</td>
      <td>103.003978</td>
      <td>126209.155363</td>
      <td>103.025069</td>
      <td>132856.260679</td>
      <td>103.349406</td>
      <td>115613.265107</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>Q3</td>
      <td>105.851629</td>
      <td>132207.28391</td>
      <td>105.619893</td>
      <td>129414.394046</td>
      <td>105.031061</td>
      <td>135443.093443</td>
      <td>107.811831</td>
      <td>120605.219276</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[1,0] = 'Year'
df.iloc[1,1] = 'Quarter'
df.head()
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
      <th>Table 7: Standardised House Price &amp; Index for Rural Areas of Northern Ireland by drive times</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>Unnamed: 10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Back to contents</td>
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
      <th>1</th>
      <td>Year</td>
      <td>Quarter</td>
      <td>Drive time within 20mins of town of 10,000 or ...</td>
      <td>Drive time within 20mins of town of 10,000 or ...</td>
      <td>Drive time outside 20mins of town of 10,000 or...</td>
      <td>Drive time outside 20mins of town of 10,000 or...</td>
      <td>Drive time within 1hr of Belfast Index</td>
      <td>Drive time within 1hr of Belfast  Price\n(Ref:...</td>
      <td>Drive time outside 1hr of Belfast Index</td>
      <td>Drive time outside 1hr of Belfast  Price\n(Ref...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>Q1</td>
      <td>100</td>
      <td>124898.676844</td>
      <td>100</td>
      <td>122528.427865</td>
      <td>100</td>
      <td>128955.274996</td>
      <td>100</td>
      <td>111866.40498</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>Q2</td>
      <td>103.166882</td>
      <td>128854.070701</td>
      <td>103.003978</td>
      <td>126209.155363</td>
      <td>103.025069</td>
      <td>132856.260679</td>
      <td>103.349406</td>
      <td>115613.265107</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>Q3</td>
      <td>105.851629</td>
      <td>132207.28391</td>
      <td>105.619893</td>
      <td>129414.394046</td>
      <td>105.031061</td>
      <td>135443.093443</td>
      <td>107.811831</td>
      <td>120605.219276</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
basic_cleanup(df).head()
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
      <th>1</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Drive time within 20mins of town of 10,000 or more Index</th>
      <th>Drive time within 20mins of town of 10,000 or more  Price\n(Ref: Q1 2015)</th>
      <th>Drive time outside 20mins of town of 10,000 or more Index</th>
      <th>Drive time outside 20mins of town of 10,000 or more  Price\n(Ref: Q1 2015)</th>
      <th>Drive time within 1hr of Belfast Index</th>
      <th>Drive time within 1hr of Belfast  Price\n(Ref: Q1 2015)</th>
      <th>Drive time outside 1hr of Belfast Index</th>
      <th>Drive time outside 1hr of Belfast  Price\n(Ref: Q1 2015)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015Q1</td>
      <td>2015</td>
      <td>Q1</td>
      <td>100.000000</td>
      <td>124898.676844</td>
      <td>100.000000</td>
      <td>122528.427865</td>
      <td>100.000000</td>
      <td>128955.274996</td>
      <td>100.000000</td>
      <td>111866.404980</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015Q2</td>
      <td>2015</td>
      <td>Q2</td>
      <td>103.166882</td>
      <td>128854.070701</td>
      <td>103.003978</td>
      <td>126209.155363</td>
      <td>103.025069</td>
      <td>132856.260679</td>
      <td>103.349406</td>
      <td>115613.265107</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015Q3</td>
      <td>2015</td>
      <td>Q3</td>
      <td>105.851629</td>
      <td>132207.283910</td>
      <td>105.619893</td>
      <td>129414.394046</td>
      <td>105.031061</td>
      <td>135443.093443</td>
      <td>107.811831</td>
      <td>120605.219276</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015Q4</td>
      <td>2015</td>
      <td>Q4</td>
      <td>107.430656</td>
      <td>134179.467306</td>
      <td>106.924715</td>
      <td>131013.172436</td>
      <td>106.240145</td>
      <td>137002.270924</td>
      <td>110.075053</td>
      <td>123137.004353</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016Q1</td>
      <td>2016</td>
      <td>Q1</td>
      <td>108.909364</td>
      <td>136026.354775</td>
      <td>108.368772</td>
      <td>132782.552750</td>
      <td>107.604887</td>
      <td>138762.178070</td>
      <td>111.828874</td>
      <td>125098.941485</td>
    </tr>
  </tbody>
</table>
</div>




```python
def cleanup_table_7(df):
    """
    Table 7: Standardised House Price & Index for Rural Areas of Northern Ireland by drive times
    * Insert Year/Quarter future-headers
    * Clean normally
    # TODO THIS MIGHT BE VALID FOR MULTIINDEXING ON DRIVETIME/[Index/Price]
    """
    df = df.copy()
    df.iloc[1,0] = 'Year'
    df.iloc[1,1] = 'Quarter'
    df = basic_cleanup(df)
    return df

cleanup_table_7(source_df['Table 7'])
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
      <th>1</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Drive time within 20mins of town of 10,000 or more Index</th>
      <th>Drive time within 20mins of town of 10,000 or more  Price\n(Ref: Q1 2015)</th>
      <th>Drive time outside 20mins of town of 10,000 or more Index</th>
      <th>Drive time outside 20mins of town of 10,000 or more  Price\n(Ref: Q1 2015)</th>
      <th>Drive time within 1hr of Belfast Index</th>
      <th>Drive time within 1hr of Belfast  Price\n(Ref: Q1 2015)</th>
      <th>Drive time outside 1hr of Belfast Index</th>
      <th>Drive time outside 1hr of Belfast  Price\n(Ref: Q1 2015)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015Q1</td>
      <td>2015</td>
      <td>Q1</td>
      <td>100.000000</td>
      <td>124898.676844</td>
      <td>100.000000</td>
      <td>122528.427865</td>
      <td>100.000000</td>
      <td>128955.274996</td>
      <td>100.000000</td>
      <td>111866.404980</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015Q2</td>
      <td>2015</td>
      <td>Q2</td>
      <td>103.166882</td>
      <td>128854.070701</td>
      <td>103.003978</td>
      <td>126209.155363</td>
      <td>103.025069</td>
      <td>132856.260679</td>
      <td>103.349406</td>
      <td>115613.265107</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015Q3</td>
      <td>2015</td>
      <td>Q3</td>
      <td>105.851629</td>
      <td>132207.283910</td>
      <td>105.619893</td>
      <td>129414.394046</td>
      <td>105.031061</td>
      <td>135443.093443</td>
      <td>107.811831</td>
      <td>120605.219276</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015Q4</td>
      <td>2015</td>
      <td>Q4</td>
      <td>107.430656</td>
      <td>134179.467306</td>
      <td>106.924715</td>
      <td>131013.172436</td>
      <td>106.240145</td>
      <td>137002.270924</td>
      <td>110.075053</td>
      <td>123137.004353</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016Q1</td>
      <td>2016</td>
      <td>Q1</td>
      <td>108.909364</td>
      <td>136026.354775</td>
      <td>108.368772</td>
      <td>132782.552750</td>
      <td>107.604887</td>
      <td>138762.178070</td>
      <td>111.828874</td>
      <td>125098.941485</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016Q2</td>
      <td>2016</td>
      <td>Q2</td>
      <td>111.263396</td>
      <td>138966.509219</td>
      <td>109.739250</td>
      <td>134461.778232</td>
      <td>110.208116</td>
      <td>142119.179594</td>
      <td>111.991819</td>
      <td>125281.221326</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016Q3</td>
      <td>2016</td>
      <td>Q3</td>
      <td>113.419541</td>
      <td>141659.506269</td>
      <td>112.426034</td>
      <td>137753.851946</td>
      <td>112.202571</td>
      <td>144691.133778</td>
      <td>115.398242</td>
      <td>129091.864904</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016Q4</td>
      <td>2016</td>
      <td>Q4</td>
      <td>113.928074</td>
      <td>142294.657346</td>
      <td>113.219995</td>
      <td>138726.680412</td>
      <td>112.508660</td>
      <td>145085.851672</td>
      <td>116.952798</td>
      <td>130830.890712</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2017Q1</td>
      <td>2017</td>
      <td>Q1</td>
      <td>114.262386</td>
      <td>142712.207695</td>
      <td>113.549623</td>
      <td>139130.567598</td>
      <td>112.823330</td>
      <td>145491.635911</td>
      <td>117.341538</td>
      <td>131265.759778</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2017Q2</td>
      <td>2017</td>
      <td>Q2</td>
      <td>115.566592</td>
      <td>144341.144812</td>
      <td>115.829688</td>
      <td>141924.295411</td>
      <td>114.288862</td>
      <td>147381.515712</td>
      <td>119.397027</td>
      <td>133565.161466</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2017Q3</td>
      <td>2017</td>
      <td>Q3</td>
      <td>116.716428</td>
      <td>145777.273752</td>
      <td>117.061832</td>
      <td>143434.022704</td>
      <td>115.192251</td>
      <td>148546.484147</td>
      <td>121.273582</td>
      <td>135664.395891</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2017Q4</td>
      <td>2017</td>
      <td>Q4</td>
      <td>117.925340</td>
      <td>147287.189812</td>
      <td>118.541541</td>
      <td>145247.086931</td>
      <td>116.101165</td>
      <td>149718.576638</td>
      <td>123.577530</td>
      <td>138241.740123</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2018Q1</td>
      <td>2018</td>
      <td>Q1</td>
      <td>118.482802</td>
      <td>147983.452250</td>
      <td>120.184585</td>
      <td>147260.282195</td>
      <td>117.972698</td>
      <td>152132.017714</td>
      <td>122.075418</td>
      <td>136561.381608</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2018Q2</td>
      <td>2018</td>
      <td>Q2</td>
      <td>119.443631</td>
      <td>149183.514842</td>
      <td>120.710551</td>
      <td>147904.740501</td>
      <td>117.686726</td>
      <td>151763.241043</td>
      <td>125.603705</td>
      <td>140508.349303</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2018Q3</td>
      <td>2018</td>
      <td>Q3</td>
      <td>121.408923</td>
      <td>151638.138779</td>
      <td>122.222994</td>
      <td>149757.912837</td>
      <td>119.614730</td>
      <td>154249.503782</td>
      <td>127.210974</td>
      <td>142306.342946</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2018Q4</td>
      <td>2018</td>
      <td>Q4</td>
      <td>123.531419</td>
      <td>154289.108214</td>
      <td>125.254013</td>
      <td>153471.772944</td>
      <td>121.462721</td>
      <td>156632.586327</td>
      <td>130.953652</td>
      <td>146493.143086</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2019Q1</td>
      <td>2019</td>
      <td>Q1</td>
      <td>122.499375</td>
      <td>153000.098716</td>
      <td>123.207618</td>
      <td>150964.357154</td>
      <td>120.087144</td>
      <td>154858.706540</td>
      <td>129.712835</td>
      <td>145105.085124</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2019Q2</td>
      <td>2019</td>
      <td>Q2</td>
      <td>124.397722</td>
      <td>155371.109292</td>
      <td>125.151589</td>
      <td>153346.274193</td>
      <td>122.486275</td>
      <td>157952.513361</td>
      <td>130.480634</td>
      <td>145963.994647</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2019Q3</td>
      <td>2019</td>
      <td>Q3</td>
      <td>126.533407</td>
      <td>158038.551430</td>
      <td>128.647747</td>
      <td>157630.061642</td>
      <td>124.978137</td>
      <td>161165.900455</td>
      <td>133.258945</td>
      <td>149071.990904</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2019Q4</td>
      <td>2019</td>
      <td>Q4</td>
      <td>127.126748</td>
      <td>158779.626458</td>
      <td>127.784267</td>
      <td>156572.053236</td>
      <td>124.547746</td>
      <td>160610.887802</td>
      <td>134.709059</td>
      <td>150694.181735</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2020Q1</td>
      <td>2020</td>
      <td>Q1</td>
      <td>127.090324</td>
      <td>158734.133127</td>
      <td>128.619521</td>
      <td>157595.476721</td>
      <td>124.744271</td>
      <td>160864.317472</td>
      <td>135.068006</td>
      <td>151095.722593</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2020Q2</td>
      <td>2020</td>
      <td>Q2</td>
      <td>127.200617</td>
      <td>158871.887068</td>
      <td>127.231209</td>
      <td>155894.400318</td>
      <td>125.021931</td>
      <td>161222.374474</td>
      <td>132.935126</td>
      <td>148709.746207</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2020Q3</td>
      <td>2020</td>
      <td>Q3</td>
      <td>129.627870</td>
      <td>161903.493901</td>
      <td>131.083667</td>
      <td>160614.756005</td>
      <td>127.873046</td>
      <td>164899.037745</td>
      <td>135.952621</td>
      <td>152085.309777</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>132.853240</td>
      <td>165931.938294</td>
      <td>135.873737</td>
      <td>166483.954356</td>
      <td>130.725554</td>
      <td>168577.497418</td>
      <td>142.032974</td>
      <td>158887.182045</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>134.414458</td>
      <td>167881.879606</td>
      <td>136.978231</td>
      <td>167837.272586</td>
      <td>132.479831</td>
      <td>170839.730568</td>
      <td>142.532053</td>
      <td>159445.483290</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>139.417605</td>
      <td>174130.744141</td>
      <td>142.727536</td>
      <td>174881.805508</td>
      <td>137.737680</td>
      <td>177620.004609</td>
      <td>147.652942</td>
      <td>165174.037638</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>143.303934</td>
      <td>178984.717757</td>
      <td>147.615067</td>
      <td>180870.420630</td>
      <td>141.482937</td>
      <td>182449.710341</td>
      <td>153.161532</td>
      <td>171336.300173</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>144.731984</td>
      <td>180768.332630</td>
      <td>149.013971</td>
      <td>182584.475980</td>
      <td>142.365385</td>
      <td>183587.673223</td>
      <td>156.204293</td>
      <td>174740.127539</td>
    </tr>
  </tbody>
</table>
</div>




```python
dest_df['Table 7'] = cleanup_table_7(source_df['Table 7'])
len(dest_df), len([k for k in source_df.keys() if k.startswith('Table') and k not in dest_df])
```




    (15, 17)



### Table 8: Number of Verified Residential Property Sales of properties in urban and rural areas and properties in rural areas by drive times witihn towns of 10,000 or more and within 1 hour of Belfast

We're now getting into the swing of this!

This one has two similar problems we've already seen; Munged Quarters/Years (this time with no header on that column...), and annual Total rows.

> Vee must deeel with it


```python
cleanup_table_5a(source_df['Table 8']).head()
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
      <th>2</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Urban</th>
      <th>Rural</th>
      <th>Drive time within 20mins of town of 10,000 or more</th>
      <th>Drive time outside 20mins of town of 10,000 or more</th>
      <th>Drive time within 1hr of Belfast</th>
      <th>Drive time outside 1hr of Belfast</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015Q1</td>
      <td>2015</td>
      <td>Q1</td>
      <td>3294</td>
      <td>1322</td>
      <td>898</td>
      <td>424</td>
      <td>976</td>
      <td>346</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015Q2</td>
      <td>2015</td>
      <td>Q2</td>
      <td>3789</td>
      <td>1500</td>
      <td>1034</td>
      <td>466</td>
      <td>1142</td>
      <td>358</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015Q3</td>
      <td>2015</td>
      <td>Q3</td>
      <td>4199</td>
      <td>1640</td>
      <td>1145</td>
      <td>495</td>
      <td>1250</td>
      <td>390</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015Q4</td>
      <td>2015</td>
      <td>Q4</td>
      <td>4396</td>
      <td>1780</td>
      <td>1223</td>
      <td>557</td>
      <td>1342</td>
      <td>438</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016Q1</td>
      <td>2016</td>
      <td>Q1</td>
      <td>4424</td>
      <td>1731</td>
      <td>1171</td>
      <td>560</td>
      <td>1263</td>
      <td>468</td>
    </tr>
  </tbody>
</table>
</div>




```python
cleanup_table_8 = cleanup_table_5a
```


```python
dest_df['Table 8'] = cleanup_table_8(source_df['Table 8'])
len(dest_df), len([k for k in source_df.keys() if k.startswith('Table') and k not in dest_df])
```




    (16, 16)



### Table 9: NI Average Sales Prices Q1 2005 - Q4 2021

Wee buns


```python
basic_cleanup(source_df['Table 9'])
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
      <th>1</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Simple Mean</th>
      <th>Simple Median</th>
      <th>Standardised Price (HPI)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>115912.942222</td>
      <td>100000</td>
      <td>111920.268199</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>120481.290591</td>
      <td>105000</td>
      <td>116004.031639</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>128866.225917</td>
      <td>115000</td>
      <td>123386.352673</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>129649.092074</td>
      <td>117000</td>
      <td>127674.143865</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>132972.115070</td>
      <td>120000</td>
      <td>131302.064422</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>171803.199843</td>
      <td>150000</td>
      <td>147474.561707</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>176218.214924</td>
      <td>150000</td>
      <td>149084.306040</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>184144.458946</td>
      <td>154950</td>
      <td>154323.134643</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>173490.230508</td>
      <td>155000</td>
      <td>159028.118093</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>159965.154863</td>
      <td>141000</td>
      <td>159150.737832</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 6 columns</p>
</div>




```python
dest_df['Table 9'] = basic_cleanup(source_df['Table 9'])
len(dest_df), len([k for k in source_df.keys() if k.startswith('Table') and k not in dest_df])
```




    (17, 15)



### Table 9x: NI Average Sale Prices XXXXX Property Q1 2005 - Q4 2021

These are very similar to Tables 2x; i.e. they're broken down by property type.

Annoyingly, they don't follow the same structure as Tables 2x or Table 9 because they don't include the Year/Quarter headers.

If that reminds you of anything, it's because Table 7 was the same...



```python
cleanup_table_7(source_df['Table 9a'])
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
      <th>1</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Simple Mean</th>
      <th>Simple Median</th>
      <th>Standardised Price (HPI)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>166314.816092</td>
      <td>149972.5</td>
      <td>160428.832662</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>173370.669076</td>
      <td>155000.0</td>
      <td>169686.542965</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>185397.896739</td>
      <td>165000.0</td>
      <td>180696.666810</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>186545.119355</td>
      <td>165000.0</td>
      <td>185323.883533</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>191328.398119</td>
      <td>173000.0</td>
      <td>188669.361197</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>243712.512641</td>
      <td>220000.0</td>
      <td>220592.113069</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>254182.439174</td>
      <td>225000.0</td>
      <td>224872.989982</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>268755.621299</td>
      <td>235000.0</td>
      <td>234734.715703</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>245860.399289</td>
      <td>225000.0</td>
      <td>239101.239764</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>244468.040738</td>
      <td>219000.0</td>
      <td>241131.373512</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 6 columns</p>
</div>




```python
cleanup_table_9x = cleanup_table_7
```


```python
table9s = re.compile('Table 9[a-z]')
for table in source_df:
    if table9s.match(table):
        dest_df[table] = cleanup_table_9x(source_df[table])
len(dest_df), len([k for k in source_df.keys() if k.startswith('Table') and k not in dest_df])
```




    (21, 11)



### Table 10x: Number of Verified Residential Property Sales by Type in XXXXX
Surprisingly, we're in the home straight; the remaining tables are all of the same structure, with familiar awkwardness.,,

* Annual-Total Rows
* Munged Year/Quarter Column
* That column having a silly (but contextual) name
* a different offset

Fortunately, we already have something like that from dealing with Table 5a!



```python
source_df['Table 10a']
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
      <th>Table 10a: Number of Verified Residential Property Sales by Type in Antrim and Newtownabbey Council</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Please note figures for the 2 most recent quar...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Back to contents</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ANTRIM AND NEWTOWNABBEY</td>
      <td>Apartments</td>
      <td>Detached</td>
      <td>Semi-Detached</td>
      <td>Terrace</td>
      <td>Total</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Q1 2005</td>
      <td>10</td>
      <td>61</td>
      <td>78</td>
      <td>87</td>
      <td>236</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Q2 2005</td>
      <td>46</td>
      <td>213</td>
      <td>216</td>
      <td>260</td>
      <td>735</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Q1 2021</td>
      <td>52</td>
      <td>222</td>
      <td>212</td>
      <td>166</td>
      <td>652</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Q2 2021</td>
      <td>56</td>
      <td>217</td>
      <td>275</td>
      <td>176</td>
      <td>724</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Q3 2021</td>
      <td>47</td>
      <td>222</td>
      <td>268</td>
      <td>202</td>
      <td>739</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Q4 2021</td>
      <td>50</td>
      <td>117</td>
      <td>176</td>
      <td>189</td>
      <td>532</td>
    </tr>
    <tr>
      <th>87</th>
      <td>2021 Total</td>
      <td>205</td>
      <td>778</td>
      <td>931</td>
      <td>733</td>
      <td>2647</td>
    </tr>
  </tbody>
</table>
<p>88 rows × 6 columns</p>
</div>




```python
cleanup_table_5a(source_df['Table 10a'])
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
      <th>2</th>
      <th>Period</th>
      <th>Year</th>
      <th>Quarter</th>
      <th>Apartments</th>
      <th>Detached</th>
      <th>Semi-Detached</th>
      <th>Terrace</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005Q1</td>
      <td>2005</td>
      <td>Q1</td>
      <td>10</td>
      <td>61</td>
      <td>78</td>
      <td>87</td>
      <td>236</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005Q2</td>
      <td>2005</td>
      <td>Q2</td>
      <td>46</td>
      <td>213</td>
      <td>216</td>
      <td>260</td>
      <td>735</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005Q3</td>
      <td>2005</td>
      <td>Q3</td>
      <td>46</td>
      <td>214</td>
      <td>238</td>
      <td>259</td>
      <td>757</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005Q4</td>
      <td>2005</td>
      <td>Q4</td>
      <td>65</td>
      <td>227</td>
      <td>270</td>
      <td>331</td>
      <td>893</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006Q1</td>
      <td>2006</td>
      <td>Q1</td>
      <td>48</td>
      <td>186</td>
      <td>231</td>
      <td>296</td>
      <td>761</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2020Q4</td>
      <td>2020</td>
      <td>Q4</td>
      <td>53</td>
      <td>248</td>
      <td>268</td>
      <td>187</td>
      <td>756</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2021Q1</td>
      <td>2021</td>
      <td>Q1</td>
      <td>52</td>
      <td>222</td>
      <td>212</td>
      <td>166</td>
      <td>652</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2021Q2</td>
      <td>2021</td>
      <td>Q2</td>
      <td>56</td>
      <td>217</td>
      <td>275</td>
      <td>176</td>
      <td>724</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2021Q3</td>
      <td>2021</td>
      <td>Q3</td>
      <td>47</td>
      <td>222</td>
      <td>268</td>
      <td>202</td>
      <td>739</td>
    </tr>
    <tr>
      <th>67</th>
      <td>2021Q4</td>
      <td>2021</td>
      <td>Q4</td>
      <td>50</td>
      <td>117</td>
      <td>176</td>
      <td>189</td>
      <td>532</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 8 columns</p>
</div>




```python
cleanup_table_10x = cleanup_table_5a
```


```python
table10s = re.compile('Table 10[a-z]')
for table in source_df:
    if table10s.match(table):
        dest_df[table] = cleanup_table_10x(source_df[table])
len(dest_df), len([k for k in source_df.keys() if k.startswith('Table') and k not in dest_df])
```




    (32, 0)



## And We're Done!

So, we can see that while government open data is a pain, at least it's a ... consistently inconsistent pain?

I hope this was helpful to someone else.



```python
dest_df['Contents'] = source_df['Contents'][source_df['Contents']['Worksheet Name'].str.startswith('Table')]
```


```python
with pd.ExcelWriter('NI Housing Price Index.xlsx') as writer:
    # Thankfully these are semantically sortable otherwise this would be a _massive_ pain
    for k,df in sorted(dest_df.items()):
        df.to_excel(writer, sheet_name=k)

```

* [Notebook Here](/assets/2022-03-27-NI-House-Price-Index.ipynb)
* [Resulting Excel File Here](/assets/2022-03-27-NI-House-Price-Index.xlsx)
