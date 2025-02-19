# Architecture Decision Records Review

## Vorbereitung

Konvertiere mit folgendem Befehl die Architecture Decision Records Markdown Dateien in PDFs:

```shell
$filename_noext="example"

pandoc "$filename_noext.md" \
    --output "$filename_noext.pdf" \
    --pdf-engine=xelatex \
    -H "header.sty"
```

```latex
% header.sty
\usepackage[a4paper, top=1.5cm, bottom=2cm, left=1.5cm, right=1.5cm]{geometry}
\renewcommand{\arraystretch}{2}

\RequirePackage{titlesec}
\RequirePackage{titling}
\RequirePackage{fontspec}

\defaultfontfeatures{Mapping=tex-text,Scale=MatchLowercase}
\setmainfont{Open Sans}
\setmonofont{Courier}

\newfontfamily\headingfont[
 UprightFont = *-Regular,
 BoldFont = *-Bold
]{Verdana}

\newfontfamily{\emojifont}{Symbola}

\titleformat{\section}
    {\Huge\bfseries\headingfont}{\thesection}{1em}{}
\titleformat{\subsection}
    {\Large\bfseries\headingfont}{\thesubsection}{1em}{}
\titleformat{\subsubsection}
    {\large\bfseries\headingfont}{\thesubsubsection}{1em}{}
\titleformat{\paragraph}
    {\normalsize\bfseries\headingfont}{\theparagraph}{1em}{}
```

Tausche die Ausgedruckten ADR mit den anderen Gruppen aus.

## Review

Beurteile die Qualität der ADR der anderen Gruppe. Achte dich auf Verständlichkeit und Nachvollziehbarkeit.
Halte sowohl positive als auch verbesserungswürdige Punkte fest.