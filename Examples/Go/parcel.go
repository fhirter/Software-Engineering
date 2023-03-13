package main

type Parcel struct {
	weight     int
	dimensions Dimension
}

func (p Parcel) setWeight(weight int) {
	p.weight = weight
}

type Dimension struct {
	width  int
	height int
	depth  int
}
