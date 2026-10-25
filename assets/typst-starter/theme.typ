#let ink = rgb("203443")
#let accent = rgb("087f8c")

#let source-note(file, pages) = block(above: 3pt, below: 6pt)[
  #text(size: 8.5pt, fill: accent)[Source: #raw(file), PDF #pages.]
]

#let teaching-note(title, body) = block(
  width: 100%, inset: 9pt, radius: 2pt,
  fill: rgb("eef8f8"), stroke: 0.5pt + accent,
  breakable: true,
)[
  #text(weight: "bold", fill: ink)[#title]
  #parbreak()
  #body
]

#let teaching-figure(path, caption, source: none, width: 100%, height: auto, alt: none) = figure(
  image(path, width: width, height: height, fit: "contain", alt: alt),
  caption: if source == none { caption } else { [#caption #text(style: "italic")[#source]] },
)

#let textbook(title: "Study Notes", subtitle: "", language: "en", body) = {
  set document(title: title)
  set page(
    paper: "a4", margin: (x: 23mm, y: 23mm), numbering: "1",
    header: align(right, text(size: 8pt, fill: accent)[STUDY NOTES]),
  )
  set text(font: "Libertinus Serif", size: 11pt, lang: language, fill: ink)
  set par(justify: true, leading: 0.65em, first-line-indent: 0pt, spacing: 0.7em)
  set heading(numbering: "1.1")
  set figure(gap: 7pt)
  show figure.caption: set text(size: 9pt)
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    block(above: 10pt, below: 16pt)[#text(size: 23pt, weight: "bold", fill: ink)[#it]]
  }
  show heading.where(level: 2): set text(size: 15pt, weight: "bold", fill: ink)
  show heading.where(level: 3): set text(size: 12pt, weight: "bold", fill: accent)
  page(header: none, footer: none)[
    #v(20%)
    #text(size: 12pt, fill: accent)[TEXTBOOK STUDY NOTES]
    #v(12pt)
    #text(size: 32pt, weight: "bold")[#title]
    #v(10pt)
    #text(size: 17pt)[#subtitle]
    #v(1fr)
    #text(size: 10pt)[Explanations · worked examples · visual learning]
  ]
  outline(depth: 2)
  pagebreak()
  body
}
