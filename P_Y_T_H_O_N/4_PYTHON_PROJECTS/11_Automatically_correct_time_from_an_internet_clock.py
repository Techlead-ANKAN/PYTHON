# Automatically correct time from an internet clock


# import time
# import os

# try:
#     import ntplib
#     client = ntplib.NTPClient()
#     response = client.request('pool.ntp.org')
#     os.system('date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
# except:
#     print('Could not sync with time server.')

# print('Done.')

