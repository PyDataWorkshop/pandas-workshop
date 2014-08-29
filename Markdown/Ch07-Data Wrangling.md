Chapter 7 Data Wrangling: Clean, Transform, Merge, Reshape
============================================================
- Combining and Merging Data Sets
- Reshaping and Pivoting
- Data Transformation
- String Manipulation
- Example: USDA Food Database

<hr>
- Much of the programming work in data analysis and modeling is spent on data preparation:
loading, cleaning, transforming, and rearranging. Sometimes the way that data
is stored in files or databases is not the way you need it for a data processing application.
- Many people choose to do ad hoc processing of data from one form to another using
a general purpose programming, like Python, Perl, R, or Java, or UNIX text processing
tools like sed or awk. Fortunately, pandas along with the Python standard library provide
you with a high-level, flexible, and high-performance set of core manipulations
and algorithms to enable you to wrangle data into the right form without much trouble.
- If you identify a type of data manipulation that isn’t anywhere in this book or elsewhere
in the pandas library, feel free to suggest it on the mailing list or GitHub site. Indeed,
much of the design and implementation of pandas has been driven by the needs of real
world applications.
