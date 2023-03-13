package main

import "fmt"

func main() {
	fmt.Println("Hello, World!")

	parcel := Eurobox{}

	setup(parcel)
}

func setup(parcel Parcel) {
	parcel.setWeight(5)
}
