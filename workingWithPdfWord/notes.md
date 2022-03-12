**The Problematic PDF Format**

While PDF files are great for laying out text in a way that’s easy for people to
print and read, they’re not straightforward for software to parse into plaintext.
As such, PyPDF2 might make mistakes when extracting text from a PDF and
may even be unable to open some PDFs at all. There isn’t much you can do
about this, unfortunately. PyPDF2 may simply be unable to work with some of
your particular PDF files. That said, I haven’t found any PDF files so far that
can’t be opened with PyPDF2.

## points

- PyPDF2 uses a zero-based index for getting pages: The first page is page 0,
the second is page 1, and so on. This is always the case, even if pages are
numbered differently within the document.

- Exercise: Create a PDF from only those pages that have some specific text, identi-
fied by extractText().

- Many of the limitations that come with working with PDFs and Word
documents are because these formats are meant to be nicely displayed for
human readers, rather than easy to parse by software.

## docx
- document object
    - paragraph objects
        - run objects

- The text in a Word document is more than just a string. It has font, size,
color, and other styling information associated with it. A style in Word is a
collection of these attributes. A Run object is a contiguous run of text with
the same style. A new Run object is needed whenever the text style changes.

- With Python-Docx, your Python programs will now be able to read the
text from a .docx file and use it just like any other string value.

- Keep in mind that as of Python-Docx version 0.5.3, new Paragraph objects
can be added only to the end of the document, and new Run objects can be
added only to the end of a Paragraph object.

## concepts
- style paragraphs
- style runs
- add_paragraph
- add_run
- add_heading[0,1,2,3,4]
- add_picture
- add_break
- add_picture