package main

import (
	"reflect"
	"testing"
)

func TestMean(t *testing.T) {
	var data = []int{4, 4, 5, 5}
	var window = 2

	var given = mean(data, window)
	var expected = []float32{4, 5}

	if !reflect.DeepEqual(given, expected) {
		t.Fatalf(`Arrays not equal! expected %v, got %v`, expected, given)
	}
}
