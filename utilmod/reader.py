SAMPLE_DATA_DIR = '../sampledata'

def read(filename:str='unique') -> None:
    path = str('{0}/{1}.txt').format(SAMPLE_DATA_DIR,filename)
    reader = open(path,'r')
    res = reader.read().strip().split(' ')
    reader.close()
    return list(map(int,res))
