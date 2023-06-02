# Размах данных
from datetime import date, datetime
import sys

dateformat = '%Y-%m-%d'
dtl = []
for dt in sys.stdin:
    dtl.append(datetime.strptime(dt.strip(), dateformat).date())

print((max(dtl) - min(dtl)).days)
