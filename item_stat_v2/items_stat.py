import pdfplumber
import pandas as pd
with pdfplumber.open("items.pdf") as temp:
    first_page = temp.pages[0]
    first_page_txt = first_page.extract_text()

# print(first_page_txt)

txt_line_split = first_page_txt.split("\n")

stat = dict()
for txt in txt_line_split:
    if '1 本' in txt:
        # print(txt)
        book_name = txt.split(" ")[1]
        if book_name not in stat:
            stat[book_name] = 1
        else:
            stat[book_name] +=1
#print(stat) 
df = pd.DataFrame()

bookname = pd.Series(list(stat.keys()))
#bookname = bookname.str.encode(encoding='utf-8')

number = pd.Series(list(stat.values()))
#number = number.str.encode(encoding='utf-8')

df['bookname'] = bookname
df['number'] = number


# print(list(stat.keys()))
# print(list(stat.values()))

print(df)
df.to_excel("book_number.xlsx",encoding='utf-8',index=None)
