/home/sunild/Downloads/CS771-Vids/PPTs

## Motivation:
---
I needed to convert some `pptx` files that were not being `correctly`(images and text were not rendered completely as I wished) converted into `pdf` format using LibreOffice. So I went online and serched for `ppt-to-pdf` converter, found adobe does that and also correctly, but only 1 convert was allowed free then you have buy a plan, make an account and all that. Dang it. But there is a cache; we can delete cache and cookies for this site and then can do the one free convert again and again, but this is ineffective, boring repeat work that wastes time. Then I automated this task(as it is excat repeat) using `selenium-with-helium`. 

## Use:
---
Although this project only focuses on `pptx-to-pdf`; but it can be changed with just 2-3 tweaks; just give appropriate adobe converter link and tell programme to look for those specific files that you want to convert. 

## Issues and Solutions:
---
Currently it does not work headlessly with both firefox and chrome webdrivers. Chrome does not support dragging files and all that headlessly, I think not sure. 

But firefox does support. And I am working on that.  