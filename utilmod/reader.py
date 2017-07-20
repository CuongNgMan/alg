SAMPLE_DATA_DIR = '../sampledata'

def read(filename:str='unique') -> None:
	path = str('{0}/{1}.txt').format(SAMPLE_DATA_DIR,filename)
	try:
		with open(path,'r') as reader:
			res = reader.read().strip().split(' ')
		return list(map(int,res))
	except OSError as err:
		print("OS errors : {}".format(err))
	except:
		print("Unexpected errors")