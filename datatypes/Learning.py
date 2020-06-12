#!/usr/bin/env python3

import sys,argparse,re, time
from datetime import datetime




ln = '31.184.238.128 - - [02/Jun/2015:17:00:12 -0700] "GET /logs/access.log HTTP/1.1" 200 2145998 "http://kmprograf.forumcircle.com" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36" "redlug.com"'


x = re.search("^\[(?!END).*]", ln)

x = re.search(r'\[(.*)\]', ln)

ts = x[1].split()[0][:-3]


print(ts)

datetimeObj = datetime.strptime(ts, '%d/%b/%Y:%H:%M')

print('Out',datetimeObj, type(datetimeObj))

ep = datetimeObj.timestamp()

print(ep)

tm = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ep))

print(tm)





















# #parser = argparse.ArgumentParser(add_help=False)
# parser = argparse.ArgumentParser(prog=sys.argv[0], \
#                                  description='Program to extract log lines where ' + 
#                                  'the source IP address matches the --ip [address] passed')
# 
# parser.add_argument('--ip', type=str, required=True, 
#                     help='Usage example: %(prog)s --ip 111.222.111.222')
# 
# if len(sys.argv) != 3:
#     parser.print_help(sys.stderr)
#     sys.exit(1)
# 
# args = parser.parse_args()
# 
# print('Doing something', args.ip)









