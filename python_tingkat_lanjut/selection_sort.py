def selectionSort(nums):
    for i in range(len(nums)):
        lowestValueIndex = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowestValueIndex]:
                lowestValueIndex = j

        nums[i], nums[lowestValueIndex] = nums[lowestValueIndex], nums[i]



randomListOfNums = [12, 8, 3, 20, 11]
selectionSort(randomListOfNums)
print(randomListOfNums)
