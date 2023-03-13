package main

type Parcel interface {
	setWeight(weight int)
	getWeight() int
	setDimensions(dimensions Dimensions)
	getDimensions() Dimensions
}

type Eurobox struct {
	weight     int
	dimensions Dimensions
}

func (p Eurobox) getWeight() int {
	return p.weight
}

func (p Eurobox) setWeight(weight int) {
	p.weight = weight
}

func (p Eurobox) setDimensions(dimension Dimensions) {
	p.dimensions = dimension
}

func (p Eurobox) getDimensions() Dimensions {
	return p.dimensions
}

type Dimensions struct {
	width  int
	height int
	depth  int
}
