#parseXL.py
"""
****** if it is just a data table, then the first row
will have numerous non empty cells.

Execution Report - The main demand signal.
Use MRP report for long range planning.
SNR report - what is in transit. Shipped, not received.
pick list - items that can be shipped now. once a pack slip is printed, no changes can be made

******  Execution report structure
1 or more blank rows up top.  In 2016 there were two rows
Merged columns.  text string - 'Execution Report for Supplier - XXXXXX  (XXXXXX - Supplier Code)
Merged columns. text string - supplier name associated with supplier code
One or more blank rows
merged columns. text string - 'Report Date: dddddd ttttttt
one or more blank rows
data set.  First row is header row.

*******    SNR Report stucture
merged rows on top of data.  Three rows.  But this can change.
    Row 1  -  text string   Supplier code dash Supplier Name   008445 -TIMKEN COMPANY NEW PHILADELPHIA
    Row 2 - text string - Day of Week, date MMM, ddd, yyyy
    Row 3 - text string - SNR Maintenance Report
the order, the content, etc. can all change
data set - first row is header row,  first cell is "Date Shipped"

****************    Pick List structure
these are the items and quantities required to ship that are not SNR
The cells are not merged.
Data in Column A
1 or more blank rows.  My sample has three blank rows.
Row 1 - text string - 'Production Pick List'
Row 2 - text string - Supplier code  Supplier Name   008445 TIMKEN COMPANY NEW PHILADELPHIA
one or more blank rows
Row 3 - text string - 'Ship Horizon: dd Days.   This is good to know. chronic 1-2 days late can mean this needs to be increased
one or more blank rows
Row 4 - text string merged cells - 'Report Date : ' +  day/month/year  ttttt time
Row 5 - text string - 'Production / Repair'
one or more blank rows
data set - header row - starts with 'Material Number'
!!!!!!   For this report extract supplier code and add as a field to the data set.
!!!!!!!!!  might also be a good idea to add Ship Horizon to data set.
"""

import re
import pandas as pd
from typing import cast

MAX_ROWS = 20  #max rows for title search

def parse_excel_report(file_path, sheet_name=0):
  # 1. Read everything into a raw DataFrame to inspect the layout
  # header=None prevents pandas from guessing headers incorrectly at the start
  df_raw = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

  # 1. Replace '\xa0' with a normal space across the entire DataFrame
  df_raw = df_raw.replace(r'\xa0', ' ', regex=True)

  # 2. Trim leading and trailing spaces from all text columns
  df_raw = df_raw.replace(r'^\s+|\s+$', '', regex=True)

  report_name = None
  report_date = None
  supplier_code = None
  supplier_name = None
  header_row_index = None
  has_known_column = None
  is_title_row = None

  # Keywords to watch out for
  name_pattern = re.compile(r'(execution|snr\s*report|snr|pick\s*list)', re.IGNORECASE)
  # Simple regex to catch dates like 08/20/2026 or 2026-08-20
  date_pattern = re.compile(r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})')
  supplier_code_pattern = re.compile(r'^\d{6}|\d{6}$') #anchors at beginning or end of string

  #known columns
  known_columns = {'material no', 'reqd qty', 'material number', 'quantity', 
                   'required date', 'date shipped', 'snr number'}  #this is case sensitive

   # 2. Extract Metadata First  Iterate through rows to trap the metadata strings
  for idx, row in df_raw.iterrows():
    #first check if first row is start of a table
    first_row_table_cells = [str(val).strip().lower() for val in row if pd.notna(val) 
                             and str(val).strip() != ""]
            
        # Sift out empty rows or merged single-cell metadata rows
    clean_idx = cast(int, idx)   #remove error.  code was running fine
    if clean_idx==0 and len(first_row_table_cells) >= 3:    #guess that 3 is a good value
      #this is a s/s with a table of data
      report_name = 'Supplier Table'
      header_row_index = 0
      break


    # Combine cell strings in the row to safely handle merged cells
    row_text = " ".join([str(val) for val in row if pd.notna(val)])
        
        # Extract name if found and not yet set
    if not report_name and name_pattern.search(row_text):
      name_match = name_pattern.search(row_text)
      #might not even need to raise error.  just ignore andlet report_name be none
      if name_match:
        report_name = name_match.group(0)
      else:
        raise ValueError ('No Report Name found when expected at top dataset.')
      report_name_idx = idx
            
        # Extract date if found and not yet set
    if not report_date and date_pattern.search(row_text):
      date_match = date_pattern.search(row_text)
      if date_match:
        report_date = date_match.group(0)
      else:
        raise ValueError('No Date to match when expected.')
      report_date_idx = idx

    if not supplier_code and supplier_code_pattern.search(row_text):
      supplier_code_match = supplier_code_pattern.search(row_text)
      if supplier_code_match:
        supplier_code = supplier_code_match.group(0)
      else:
        raise ValueError('No Supplier Code Match when match was expected')
      supplier_code_idx = cast(int, idx)

    if report_name is not None and report_date is not None and supplier_code is not None:
      if report_name.lower() == 'execution':
        supplier_name = df_raw.iloc[supplier_code_idx+1,0]
      elif report_name.lower() == 'pick list':
        supplier_name_text= str(df_raw.iloc[supplier_code_idx,0])  # row idx and col - 0
        #if i do above, there are no extra rows and no extra columns.  so no NaN.
        #supplier_name_pattern= r'(?i)^[nan\d\s_\n\r])+ | [nan\d\s_\n\r]+$'
        supplier_name_pattern = r'^[\d\s_\n\r]+ | [\d\s_\s\r]+$'
        supplier_name = re.sub(supplier_name_pattern, "", supplier_name_text)
        supplier_name = supplier_name.strip()  #leading and trailing spaces
        #dDate = report_date[14:].strip().split(' ')  #split on space
        day, month, year = report_date.split('/')
        dDate = f"{month}/{day}/{year}"
        report_date = f"{dDate}"

      elif report_name.lower() == 'snr':
        supplier_name_text= str(df_raw.iloc[supplier_code_idx,0])  # row idx and col - 0
        supplier_name_pattern = r'(^[0-9-]+)'
        supplier_name = re.sub(supplier_name_pattern,'',supplier_name_text)

      break
    elif cast(int,idx) >= MAX_ROWS:
      raise ValueError('Unable to find title information')

  #3. Dynamic Table Finder
  for idx, row in df_raw.iterrows():
    # Get cells that actually contain data, stripped of whitespace
    non_empty_cells = [str(val).strip().lower() for val in row if pd.notna(val) 
                         and str(val).strip() != ""]
        
    # Sift out empty rows or merged single-cell metadata rows
    if len(non_empty_cells) <= 1:
      continue

    # Strategy A: Check if any of your known database column terms exist in this row
    has_known_column = any(col in known_columns for col in non_empty_cells)
      
    # Strategy B: Ensure this row doesn't accidentally contain the main title text keywords
    row_text_lower = " ".join(non_empty_cells)
    is_title_row = name_pattern.search(row_text_lower) or date_pattern.search(row_text_lower)

    #if (has_known_column or len(non_empty_cells) >= 3) and not is_title_row:
    if (has_known_column):
      header_row_index = cast(int, idx)
      break

    """
    
   
    # 3. Dynamic Dataset Identification
    # Skip the metadata rows we just verified
    if idx > 1:
      # Drop empty columns. If columns remain populated, this is our start row!
      non_empty_cells = row.dropna().tolist()
      if len(non_empty_cells) > 1:  # Header row will have multiple columns
        header_row_index = idx
        break

    """
  if header_row_index is None:
    raise ValueError("Could not find the dataset header row dynamically.")

  # 4. Re-read or slice the dataframe starting exactly at the discovered dataset row
  clean_df = pd.read_excel(file_path, skiprows=header_row_index)
    
    # Drop completely blank padding lines if any trail below the table
  clean_df = clean_df.dropna(how='all')
  

  print(f"Discovered Report Name: {report_name}")
  print(f"Discovered Report Date: {report_date}")
  print(f"Discovered Supplier Code: {supplier_code}")
  print(f"Discovered Supplier Name: {supplier_name}")
  
    
  #return clean_df, report_name, report_date
  return clean_df


# --- How to use it ---
#data_df = parse_excel_report("ExecutionReport_Dummy.xlsx")
#data_df = parse_excel_report("8445 EXE 20160323.xlsx")
#data_df = parse_excel_report("8445 SNR 20160323.xlsx")
data_df = parse_excel_report("8445 PL 20160323.xlsx")
#data_df = parse_excel_report("SAC OSR 20160323.xlsx")
print(data_df.head())
print(len(data_df))
