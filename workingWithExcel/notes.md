## definitions
- workbooks
    - worksheets
    - activesheet
    - cell

## reading
The first row or column integer is 1 , not 0.

You can determine the size of the sheet with the Worksheet object’s
`max_row()` and `max_column()` methods.

`cell.column_letter()` method can be used to convert col numbers into col letter.

## writing
The remove_sheet() method takes a Worksheet object, not a string of the
sheet name, as its argument. 

## formulas
You can also read the formula in a cell just as you would any value.
However, if you want to see the result of the calculation for the formula
instead of the literal formula, you must pass True for the data_only keyword
argument to load_workbook(). This means a Workbook object can show either
the formulas or the result of the formulas but not both. (But you can have
multiple Workbook objects loaded for the same spreadsheet file.)

```py
>>> import openpyxl
>>> wbFormulas = openpyxl.load_workbook('writeFormula.xlsx')
>>> sheet = wbFormulas.get_active_sheet()
>>> sheet['A3'].value
# '=SUM(A1:A2)'
>>> wbDataOnly = openpyxl.load_workbook('writeFormula.xlsx', data_only=True)
>>> sheet = wbDataOnly.get_active_sheet()
>>> sheet['A3'].value
# 500
```

**NOTE:**
    
Excel formulas offer a level of programmability for spreadsheets but can
quickly become unmanageable for complicated tasks. For example, even if
you’re deeply familiar with Excel formulas, it’s a headache to try to decipher
what =`IFERROR(TRIM(IF(LEN(VLOOKUP(F7, Sheet2!$A$1:$B$10000, 2,
FALSE))>0,SUBSTITUTE(VLOOKUP(F7, Sheet2!$A$1:$B$10000, 2, FALSE),
" ", ""),"")), "")` actually does. Python code is much more readable.

**conepts**
- charts
- formulas
- freeze panes
- set width-height of cell
- merge and unmerge cells
- fonts and styles
## Important
As openpyxl has changed quite a bit in how it creates charts etc. Try to visit [official docs](https://openpyxl.readthedocs.io/).
For [openpyxl charts](https://openpyxl.readthedocs.io/en/stable/charts/chart_layout.html#size-and-position) 