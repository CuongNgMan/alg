
SAMPLE_DATA_DIR = '../sampledata'
def write(filename:str,numbs:list) -> None:
    path = str('{0}/{1}.txt').format(SAMPLE_DATA_DIR,filename)
    writer = open(path,'w')
    for n in numbs:
        writer.write(str('{} ').format(n))
    writer.close()
    return None