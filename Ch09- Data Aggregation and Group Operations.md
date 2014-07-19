Chapter 9 Data Aggregation and Group Operations
===============================================
- GroupBy Mechanics
- Data Aggregation
- Group-wise Operations and Transformations
- Pivot Tables and Cross-Tabulation
- Example: 2012 Federal Election Commission Database

<hr>
Categorizing a data set and applying a function to each group, whether an aggregation
or transformation, is often a critical component of a data analysis workflow. 

After
loading, merging, and preparing a data set, a familiar task is to compute group statistics
or possibly pivot tables for reporting or visualization purposes. 

pandas provides a flexible
and high-performance groupby facility, enabling you to slice and dice, and summarize
data sets in a natural way.

One reason for the popularity of relational databases and SQL (which stands for
“structured query language”) is the ease with which data can be joined, filtered, transformed,
and aggregated. However, query languages like SQL are rather limited in the
kinds of group operations that can be performed. 

As you will see, with the expressiveness and power of Python and pandas, we can perform much more complex grouped
operations by utilizing any function that accepts a pandas object or NumPy array. In
this chapter, you will learn how to:

- Split a pandas object into pieces using one or more keys (in the form of functions,
arrays, or DataFrame column names)
- Computing group summary statistics, like count, mean, or standard deviation, or
a user-defined function
- Apply a varying set of functions to each column of a DataFrame
- Apply within-group transformations or other manipulations, like normalization,
linear regression, rank, or subset selection
- Compute pivot tables and cross-tabulations
- Perform quantile analysis and other data-derived group analyses

<hr>
