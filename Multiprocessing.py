import multiprocessing


class MultiprocessingPool():

    def __init__(self,numprocs=1):
        self.numprocs=numprocs

    def run(self, funcion, inputs):

        pool = multiprocessing.Pool(self.numprocs)
        mapping = pool.map
        mapping(funcion, inputs)
        pool.close()
        pool.join()

        return 1
