import timeit

# Function to generate a histogram (for demonstration purposes)
def hundred_hgram():
    # Your histogram code here
    # For example, generating a histogram of 100 random numbers
    import random
    histogram = {}
    for _ in range(100):
        value = random.randint(1, 10)
        if value in histogram:
            histogram[value] += 1
        else:
            histogram[value] = 1
    return histogram

# Function to benchmark the histogram generation
def benchmark_histogram():
    # Set the number of iterations for benchmarking
    iterations = 1000
    # Create a Timer object for benchmarking the hundred_hgram function
    timer = timeit.Timer('hundred_hgram()', globals=globals())
    # Get the result of the benchmark
    result_100 = timer.timeit(number=iterations)
    # Print the benchmark result
    print(f"Benchmark result for {iterations} iterations: {result_100} seconds")

# Run the benchmark only if this script is executed directly
if __name__ == '__main__':
    benchmark_histogram()
