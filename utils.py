def writer(filex, data):f = open('{0}'.format(filex), "a+", encoding="utf-8");f.write('{}\n'.format(data));f.close()
def writer_mem(filex, data):f = open('{0}'.format(filex), "w+", encoding="utf-8");f.write('{}\n'.format(data));f.close()
def reader(file_n): f=open(file_n, 'rt'); return [n.strip('\n') for n in f.readlines()];f.close()