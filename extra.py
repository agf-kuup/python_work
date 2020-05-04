
def parseDate(s):
    D={ 'Jan':'01',
        'Feb':'02',
        'Mar':'03',
        'Apr':'04',
        'May':'05',
        'Jun':'06',
        'Jul':'07',
        'Aug':'08',
        'Sep':'09',
        'Oct':'10',
        'Nov':'11',
        'Dec':'12',
        }
    A=s.split()
    if len(A[3])==1:
        A[3]='0'+A[3]
    return A[-2]+'-'+D[A[2]]+'-'+A[3]

def getDate(s):
    s=s.decode("utf-8").split('\n')
    for i in s:
        if 'Date' in i:
            break
    return parseDate(i)