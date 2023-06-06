class solution:
    def selection_sort(self,arr):
        for i in range(len(arr)):
        # initializing an variable for storing minimum element
            min_idx = i

            # Finding the index of the minimum element from the unsorted part
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            # Swap the minimum element with the current element
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
if __name__=='__main__':
    arr = [12, 11, 13, 5, 6, 7]
    s=solution()
    print(s.selection_sort(arr))
    # print(selection_sort(arr))