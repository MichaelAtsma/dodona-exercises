import time

# Sample functions to be tested

def equal(n):
    return n == 1

def greater(n):
    return n > 1

test_functions = [equal, greater]




# Testing environment implementation below. Don't change this.

def time_functions(funcs, runs=3, inputs=None, print_each_input=False, print_cold_start=True):
    if inputs is None:
        inputs = [1000000]

    results = {func.__name__: {} for func in funcs}
    for inp in inputs:
        if print_each_input:
            print(f"\nTesting input: {inp}")
        for func in funcs:
            # Cold start
            start_cold = time.time()
            func(inp)
            end_cold = time.time()
            cold_start_time = end_cold - start_cold
            if print_each_input and print_cold_start:
                print(f"{func.__name__} cold start: {format_time(cold_start_time)}")

            # Timed runs
            start = time.time()
            for i in range(runs):
                func(inp)
            end = time.time()
            elapsed = end - start
            avg_time = elapsed / runs
            results[func.__name__][inp] = {"total": elapsed, "avg": avg_time}
            if print_each_input:
                print(f"{func.__name__} avg over {runs} runs: {format_time(avg_time)}")

    print("\nSummary:")
    for func in funcs:
        avg_times = [(inp, data["avg"]) for inp, data in results[func.__name__].items()]
        total_times = [(inp, data["total"]) for inp, data in results[func.__name__].items()]
        fastest = min(avg_times, key=lambda x: x[1])
        slowest = max(avg_times, key=lambda x: x[1])
        total_avg = sum(t for _, t in avg_times) / len(avg_times)
        print(f"{func.__name__}:")
        print(f"  Fastest input: {fastest[0]} (avg {format_time(fastest[1])})")
        print(f"  Slowest input: {slowest[0]} (avg {format_time(slowest[1])})")
        print(f"  Total average time per call: {format_time(total_avg)}")
        print(f"  Total time for all {runs * len(total_times)} calls: {format_time(sum(t for _, t in total_times))}")

def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.6f} seconds"
    else:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes:02d}:{secs:06.3f} minutes"

if __name__ == "__main__":
    test_inputs = range(-1000000, 1000001)
    time_functions(test_functions, runs=3, inputs=test_inputs, print_each_input=False, print_cold_start=False)
