package ProgramElements

func quickSortStart(arr []int) []int {
	return quickSort(arr, 0, len(arr)-1)
}

func quickSort(arr []int, low, high int) []int {
	if low < high {
		var p int
		arr, p = partition(arr, low, high)
		arr = quickSort(arr, low, p-1)  // lower
		arr = quickSort(arr, p+1, high) // upper
	}
	return arr
}

func partition(arr []int, low, high int) ([]int, int) {
	var pivot = arr[high]
	var i = low
	for j := low; j < high; j++ {
		if arr[j] < pivot {
			arr[i], arr[j] = arr[j], arr[i]
			i++
		}
	}
	arr[i], arr[high] = arr[high], arr[i]
	return arr, i
}
