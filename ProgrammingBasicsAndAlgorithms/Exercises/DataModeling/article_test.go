package Engineering

import "testing"

func TestConstructor(t *testing.T) {
	var name string = "Foo"
	var bezeichnung string = "Bar Bazl"
	var gewicht float32 = 4.5

	article := NewArticle(name, bezeichnung, gewicht)

	if article.name != name {
		t.Fatalf(`name is not as expected! expected %s, got %s`, name, article.name)
	}
}
