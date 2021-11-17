import os
from openpyxl import Workbook, load_workbook
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string

def createTargetIfNotExists(tgt_workbook, tgt_worksheet):

  targetW = Workbook()
  try:
    targetW = load_workbook(tgt_workbook)
  except:
    targetW.save(tgt_workbook)
    targetW = load_workbook(tgt_workbook)

  sheets = targetW.sheetnames

  if tgt_worksheet not in sheets:
    print("Creating sheet: ", tgt_worksheet)
    targetW.create_sheet(tgt_worksheet)
    targetW.save(tgt_workbook)

def getRangeOfRowCols(xlRange):

  rangeTuples = []

  start,end = xlRange.split(":")

  startCoord = coordinate_from_string(start)

  startCol, startRow = column_index_from_string(startCoord[0]), startCoord[1]

  endCoord = coordinate_from_string(end)

  endCol, endRow =  column_index_from_string(endCoord[0]), endCoord[1]

  rangeTuples.append((startRow, endRow))
  rangeTuples.append((startCol, endCol))

  return rangeTuples

#Copy range of cells as a nested list
#Takes: start cell, end cell, and sheet you want to copy from.
def copyRange(startCol, startRow, endCol, endRow, sheet):
    rangeSelected = []
    #Loops through selected Rows
    for i in range(startRow,endRow + 1,1):
        #Appends the row to a RowSelected list
        rowSelected = []
        for j in range(startCol,endCol+1,1):
            rowSelected.append(sheet.cell(row = i, column = j).value)
        #Adds the RowSelected List and nests inside the rangeSelected
        rangeSelected.append(rowSelected)

    return rangeSelected

#Paste range
#Paste data from copyRange into template sheet
def pasteRange(startCol, startRow, endCol, endRow, sheetReceiving,copiedData):
    countRow = 0
    for i in range(startRow,endRow+1,1):
        countCol = 0
        for j in range(startCol,endCol+1,1):
            
            sheetReceiving.cell(row = i, column = j).value = copiedData[countRow][countCol]
            countCol += 1
        countRow += 1

def copyCellsFromSrcToTgt(sw, sws, sr, tw, tws, tr):

  sWb = load_workbook(sw)
  tWb = load_workbook(tw)

  srcSheet = sWb[sws]
  tgtSheet = tWb[tws]

  srcRangeDetails = getRangeOfRowCols(sr)
  tgtRangeDetails = getRangeOfRowCols(tr)

  rangeSelected = copyRange(srcRangeDetails[1][0], srcRangeDetails[0][0], srcRangeDetails[1][1], srcRangeDetails[0][1], srcSheet)
  pasteRange(tgtRangeDetails[1][0], tgtRangeDetails[0][0], tgtRangeDetails[1][1], tgtRangeDetails[0][1], tgtSheet, rangeSelected)
  
  tWb.save(tw)

if __name__ == "__main__":
  src_workbook = input("Enter path and name of src workbook: ")
  src_worksheet = input("Enter name of the src sheet: ")
  src_range = input("Enter the range of src cells: ")

  tgt_workbook = input("Enter path and name of target workbook: ")
  tgt_worksheet = input("Enter name of the target sheet: ")
  tgt_range = input("Enter the range of target cells: ")

  createTargetIfNotExists(tgt_workbook, tgt_worksheet)

  copyCellsFromSrcToTgt(src_workbook, src_worksheet, src_range, tgt_workbook, tgt_worksheet, tgt_range)