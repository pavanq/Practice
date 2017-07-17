from datetime import datetime
from pytz import timezone
tz = timezone('US/Eastern')
print datetime.now(tz)
