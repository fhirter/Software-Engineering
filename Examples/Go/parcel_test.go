package main

import "testing"

func TestIfNegativeWeightReturnsAnError(t *testing.T) {
	parcel := Eurobox{}

	err := parcel.setWeight(-1)

	if err == nil {
		t.Fail()
	}
}
