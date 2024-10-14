package main

import "fmt"

func main() {
	fmt.Println("Hello, World!")

	parcel := Eurobox{}

	setup(parcel)
}

func setup(parcel Parcel) {
	err := parcel.setWeight(5)
	if err != nil {
		panic("Weight could not be set!")
	}
}
