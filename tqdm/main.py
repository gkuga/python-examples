from tqdm import tqdm
import time
import pandas as pd


def basic_example():
    print("Basic example:")
    for i in tqdm(range(20), desc="Processing"):
        time.sleep(0.1)  # Simulate some processing

def list_processing_example():
    print("Date range processing example:")
    for t in tqdm(pd.date_range(start='2025-04-14 01:05:00', end='2025-04-14 01:40:00', freq='15s')):
        time.sleep(0.1)  # Simulate some processing

if __name__ == "__main__":
    basic_example()
    list_processing_example()
    print("\nAll examples completed!")