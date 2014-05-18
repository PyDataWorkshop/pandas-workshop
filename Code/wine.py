
# http://blog.yhathq.com/posts/comparing-random-forests-in-python-and-r.html

import pandas as pd
import pylab as pl
import numpy as np
 
df = pd.read_csv("./wine.csv")
df['is_red'] = np.where(df.color=='red', 1, 0)
df['high_quality'] = np.where(df.quality > 6.0, 1, 0)

#################################################################

cols = train.columns[:11]
clf = RandomForestClassifier(n_estimators=20, max_features=9, min_samples_split=5)
start = time.time()
clf.fit(train[cols], train.quality)
print "training time:", time.time() - start
# training time: 0.935894012451

##################################################################
 
print pd.crosstab(test.quality, clf.predict(test[cols]), rownames=["Actual"], colnames=["Pred"])

# Pred    3  4    5    6    7   8
# Actual
# 3       0  0    5    3    1   0
# 4       2  1   36   16    2   1
# 5       0  0  381  132    5   1
# 6       0  1  123  531   57   2
# 7       0  0   14  106  157   1
# 8       0  0    0   21   12  17
# 9       0  0    1    2    0   0

print np.sum(test.quality==clf.predict(test[cols])) / float(len(test))
# 0.666462293072
