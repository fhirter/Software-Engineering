#!/usr/bin/env bash
plantuml Images/plantuml/*.puml
mv Images/plantuml/*.png Images/
marp --pdf Slides.md --allow-local-files