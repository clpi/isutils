import numpy as np
import cv2

def main():
    a = ['-', '-', '-', 1, '-', '-', '-']
    n = len(a)  # length of the array
    for i in range(2*n):
        print(a[(i % n):]+a[:(i % n)])


if __name__ == "__main__":
    main()
