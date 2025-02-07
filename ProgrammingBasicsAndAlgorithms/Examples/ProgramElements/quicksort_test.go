package ProgramElements

import (
	"reflect"
	"testing"
)

func TestQuicksort(t *testing.T) {
	var data = []int{4, 6, 3, 7}

	var sorted = quickSortStart(data)
	var expected = []int{3, 4, 6, 7}

	if !reflect.DeepEqual(sorted, expected) {
		t.Errorf("Quicksort failed. Got %v, expected %v", sorted, expected)
	}
}
