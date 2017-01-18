# Interview question: Using only two comparisons, how can you tell if two date windows overlap?

import datetime
d1 = datetime.date(2016,1,5)
d2 = datetime.date(2016,1,15)
e1 = datetime.date(2016,1,15)
e2 = datetime.date(2016,1,25)

if (d1 <= e2) and (e1 <= d2):
    print 'overlap'
else:
    print 'no overlap'


