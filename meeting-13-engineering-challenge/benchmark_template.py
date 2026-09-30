import time
def benchmark(function,*args,repetitions=5):
    times=[]
    for _ in range(repetitions):
        start=time.perf_counter()
        function(*args)
        times.append(time.perf_counter()-start)
    return {"min":min(times),"max":max(times),"average":sum(times)/len(times),"runs":times}
# TODO: benchmark controlled datasets at increasing sizes.
