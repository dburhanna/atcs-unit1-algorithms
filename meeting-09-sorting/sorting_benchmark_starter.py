import time
def benchmark(sort_function,data):
    start=time.perf_counter()
    sort_function(data)
    return time.perf_counter()-start
# TODO: compare algorithms and input arrangements.
