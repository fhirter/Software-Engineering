package Engineering

import (
	"github.com/google/uuid"
)

type Artikel struct {
	id           uuid.UUID // github.com/google/uuid
	name         string
	bezeichnung  string
	lagerbestand int
	gewicht      float32
}

func NewArticle(name string, bezeichnung string, gewicht float32) *Artikel {
	a := new(Artikel)
	a.id = uuid.New()
	a.name = name
	a.bezeichnung = bezeichnung
	a.gewicht = gewicht

	return a
}
