import sys
from datetime import datetime
for line in sys.stdin.readlines(): 
    boolVal = “false” 
    line = line.strip() 
    DATETIME = datetime.strptime(line, “%m/%d/%Y”) 
    print DATETIME
