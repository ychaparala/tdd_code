#!/usr/bin/env python
#
###########################################
#
# File: text_parsing.py
# Author: Ra Inta
# Description:
# Created: July 18, 2019
# Last Modified: July 18, 2019
#
###########################################

import os
import json

import pandas as pd

data_dir = "/home/ra/host/BH_Analytics/Discover/DataEngineering/data/"


##################################################
### 1) JSON parsing - currency data     ##########
##################################################

json_name = os.path.join(data_dir, "USD_comparison.json")

# Note the encoding specification is often necessary
with open(json_name, encoding='utf-8', errors='ignore') as json_file:
     usd_data = json.load(json_file, strict=False)

usd_data

usd_data.keys()

usd_data["date"]

usd_data["rates"]["BGN"]

# These codes aren't all that descriptive on their own.
# Let's join with some more information

curr_codes_file = os.path.join(data_dir, "XE_ISO4217_CurrencyCodes.csv")

curr_codes_df = pd.read_csv(curr_codes_file)

usd_df = pd.DataFrame({"code": [x for x in usd_data['rates'].keys()]})

usd_df["rate"] = [usd_data['rates'][x] for x in usd_df["code"]]

usd_df = pd.merge(usd_df, curr_codes_df, left_on="code", right_on="Code", how="left")

# Print out the countries and their rates, compared to USD
for Idx in usd_df.index.values:
    print(f"The {usd_df.loc[Idx, 'Country Name']} is at {usd_df.loc[Idx, 'rate']} USD")

# Or, more succinct -- and performant -- broadcasting:
print("The " + usd_df['Country Name'] + " is at " + usd_df['rate'].astype('str') + " USD")


##################################################
### 2) Parsing XML documents            ##########
##################################################

import xml.etree.ElementTree as ET
import bz2

xml_dir = "/home/ra/code/botr/collate/"

input_file = bz2.BZ2File(os.path.join(xml_dir, 'search_bands.xml.bz2.bak.bz2'),
                                      'rb')

tree = ET.parse( input_file )
root = tree.getroot()

twoF = []
freq = []
jobId = []
num_templates = []

# Walk through the XML tree for 2F and f0; don't pick up the vetoed bands. Have
# to keep jobId label to produce topJobs list.
for jobNumber in root.iter('job'):
    nodeInfo = root[int(jobNumber.text)].find('loudest_nonvetoed_template')
    if nodeInfo.find('twoF') is not None:
        twoF.append( float( nodeInfo.find('twoF').text ) )
        freq.append( float( nodeInfo.find('freq').text ) )
        jobId.append( jobNumber.text )

# Get number of templates in each band
for nTempl in root.iter('num_templates'):
   num_templates.append( float( nTempl.text ) )

# The hallowed function for pretty-printing
# From http://effbot.org/zone/element-lib.htm#prettyprint
# Note that lxml, an external library, has a pretty-print option
# but it breaks for a lot of corner-casees
def indent(elem, level=0):
    """This is a function to make the XML output pretty, with the right level
    of indentation. See
    http://effbot.org/zone/element-lib.htm#prettyprint
    for the original version"""
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i



indent(search_root)
search_bands_xml = ET.ElementTree(search_root)
search_bands_xml.write(searchBandsOutputFileName, xml_declaration=True, encoding='UTF-8', method='xml')



##################################################
### 3) Parsing HDF5 files               ##########
##################################################

# ## The HDF5 Format

# A popular data format for representing out of memory data (on disk) in Pandas is the HDF5 format. HDF5 is a data model and format that can store multiple data frames, as well as different data types. This format has been used extensively outside of Python, long before Pandas was written. However, Pandas has adopted it as well and it is a popular format.

# From the website:
#
# >HDF5 is a data model, library, and file format for storing and managing data. It supports an unlimited variety of datatypes, and is designed for flexible and efficient I/O and for high volume and complex data.
#
# https://support.hdfgroup.org/HDF5/

# Pandas has documentation for the HDF5 format under the Data I/O section of the documentation:
#
# https://pandas.pydata.org/pandas-docs/stable/io.html
#
# In this documentation, Pandas goes through a series of functions that allow basic I/O, along with some subsetting capability. You can review the documentation there, it is quite good. However, since that was developed, there has been another package called `Dask` that does a better job of the same sort of thing. We will go through the Dask package in this lecture set. However, if you find it a bit overwhelming, you could use the more basic Pandas functions detailed in the links above.

# ## Creating an HDF5 data store using Pandas functions

# You can create tables that are static, that is read-only that do not support querying using this file format like so:

# In[6]:


## First read in a dataset
transactions = pd.read_csv(r'../data/retail_sales/transactions.csv')
## Establish an HDF file connection
store = pd.HDFStore('temp/store.h5')
store


# In[7]:


## Write the table as static
store['transact'] = transactions


# In[8]:


store ## note the transact frame now is part of the store.


# You can then retrieve items like so:

# In[9]:


transaction2 = store['transact']
transaction2.head()


# Behind the scenes, pandas is leveraging the PyTables library to interact with HDF5 data. Pytables uses some C code and 'Cython' to accomplish fast performance and friendly implementation.
#
# Here, the store is acting like a dict and we can store or retrieve data items via their name (key). By using this syntax (`store['name']`), we are using the HDF `put` method which creates a fixed array format. Fixed stores are not appendable once written (although they can be replaced). This format is specified by default when using `put` or `to_hdf` or by `format='fixed'` or `format='f'`

# ## Speed gains
#
# Note the difference in speed between retrieving the HDF store and reading in the CSV file. On our system, it took $\frac{1}{5}$ the time to bring in the HDF5 data.

# In[10]:


get_ipython().run_line_magic('time', "df2 = pd.read_csv(r'../data/retail_sales/transactions.csv')")


# In[11]:


get_ipython().run_line_magic('time', "df1 = store['transact']")


# However, the typical use case for HDF5 involves saving a large amount of data to a single data store (on disk dataframe), so you can later query or add to the data (append).

# ## Appending to the data store

# Let's show how to add to an existing store of data. First, we will delete the static table:

# In[12]:


del store['transact']


# Now we can create a non-static dataframe in the store, using the table format (or 't'). For this table format, delete & query type operations are supported-- tables are specified by `format='table'` or `format='t'` to `append` or `put` or `to_hdf`, or by using the `append` method to create the table.
#
# For example:
# `store.put('tabl1', t1, format='table')`
# or
# `store.put('tabl1', t1, format='t')`
# or
# `df.to_hdf(format='table')`

# In[13]:


store


# In[14]:


t1 = transactions[0:100]
t2 = transactions[100:200]
# Append creates the table, but also appends if exists
store.append('transact_all',t1,min_itemsize = 50)


# In[15]:


store.append('transact_all',t2)


# Strings are a fixed width in the underlying data store. Therefore, we must decide on the width of the column when writing the table. You can pass an argument when creating the table to establish the minimum length for a given column (or all columns). In the above code I set a width of 50 for all strings. You could alternatively pass a dict of variable names as key and widths as values to set it by column.

# The data store is not threadsafe, and does not support concurrent reading/writing.

# Unicode data types are not compatible, and will fail to write!

# A data table in PyTable is defined as a collection of records whose values are stored in fixed-length fields. All records have the same structure and all values in each field have the same data type. We can specify the size of the fields and their datatypes explicitly- but pandas provides a high-level interface that takes care of these aspects for us.

# In[16]:


get_ipython().run_line_magic('time', "df2 = store['transact_all'] ## great performance.")


# For more advanced useage, review the excellent Pandas documentation linked above. On to dask!

###########################################
# End of text_parsing.py
###########################################
