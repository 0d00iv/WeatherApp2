def kthLargest(arr,N,K):

    #Sort the given array
     arr.sort()




     return arr[K-1]


#driver code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    N = len(arr)
    K = 2

    #Function Call
    print("K'th largest element is",
          kthLargest(arr, N, K))
 