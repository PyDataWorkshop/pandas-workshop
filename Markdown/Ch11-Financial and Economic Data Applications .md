Chapter 11 Financial and Economic Data Applications
=======================================================
- Data Munging Topics
- Group Transforms and Analysis
- More Example Applications

<hr>
<pre><code>
aapl = pd.io.data.get_data_yahoo('AAPL', 
                                 start=datetime.datetime(2006, 10, 1), 
                                 end=datetime.datetime(2012, 1, 1))
aapl.head()
</code></pre>
<hr>
