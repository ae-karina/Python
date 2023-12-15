import time

sj = time.strftime("%Y.%m.%d %H.&M.%S", time.localtime(time.time()))

f = open(sj + '.txt', 'x')
