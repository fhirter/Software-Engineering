package main

import "errors"

type Parcel interface {
	setWeight(weight int) error
	getWeight() int
	setDimensions(dimensions Dimensions) error
	getDimensions() Dimensions
}

type Eurobox struct {
	weight     int
	dimensions Dimensions
}

func (p Eurobox) getWeight() int {
	return p.weight
}

func (p Eurobox) setWeight(weight int) error {
	if weight <= 0 {
		return errors.New("Weight must be greater than zero")
	}
	p.weight = weight
	return nil
}

func (p Eurobox) setDimensions(dimension Dimensions) error {
	p.dimensions = dimension
	return nil
}

func (p Eurobox) getDimensions() Dimensions {
	return p.dimensions
}

type Dimensions struct {
	width  int
	height int
	depth  int
}
