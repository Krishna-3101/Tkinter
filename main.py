import tkinter
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch 
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter, A4
import psycopg2



window=tkinter.Tk()
window.title("Grid View")
window.configure(bg='light blue')

frame=tkinter.Frame(window)
frame.configure(bg='yellow')
frame.pack(padx=20,pady=10)




def update_database():
    conn=None
    cur=None
    try:
        conn = psycopg2.connect(
                dbname="kck",
                user="postgres",
                password="admin123",
                host="localhost",
                port="5432"
            )
        cur=conn.cursor()
        name=name_entry.get()
        
        insert_values='INSERT INTO tkinter (s_no, name, template, date ) VALUES (%s, %s, %s, %s)'
        insert_data=(count,name, template_dropdown.get(), date_entry.get_date())
        cur.execute(insert_values, insert_data)
        #data=cur.fetchone()
        conn.commit()
    
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def clear_item():
    #name_entry.delete(0, tkinter.END)
    manual_wt_entry.delete(0,tkinter.END)
    item_code_entry.delete(0, tkinter.END)
    item_name_entry.delete(0, tkinter.END)
    gross_wt_entry.delete(0, tkinter.END)
    tree.delete(*tree.get_children())

def add_item():
    #global count
    #count=count+1
    name=name_entry.get()
    manual_weight=int(manual_wt_entry.get())
    item_code=int(item_code_entry.get())
    item_name=item_name_entry.get()
    gross_weight=int(gross_wt_entry.get())
    
    items=[name, manual_weight, item_code, item_name, gross_weight]
    tree.insert('',0,values=items)
    
    
def check():
    conn=None
    cur=None
    global template_details
    try:
        conn = psycopg2.connect(
                dbname="kck",
                user="postgres",
                password="admin123",
                host="localhost",
                port="5432"
            )
        cur=conn.cursor()
        cur.execute('SELECT * FROM tkinter WHERE name = %s', (name_entry.get(),))
        rows = cur.fetchall()
        if rows:
            cur.execute('SELECT template FROM tkinter WHERE name = %s ORDER BY date DESC LIMIT 1', (name_entry.get(),))
            template_details = cur.fetchone()
            #template_label.destroy()
            #template_dropdown.destroy()
            
            template_labeluser=tkinter.Label(frame, text= template_details )
            template_labeluser.grid(row=7, column=0)
            

       
            for row in rows:
                tree.insert('', 0, values=row)
        else:
             print("no")    
    
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
    return template_details

def refresh():
    name_entry.delete(0, tkinter.END)
    clear_item()
    tree.delete(*tree.get_children())
      
 
def generate_pdf_temp1():
    global details
    details=tree.item(tree.selection())    
    width = 80
    height = 210
    pdf='D:\\Krishna sai\\Ktinker\\receipt.pdf'#'recieptttttttt.pdf'
    

    c=canvas.Canvas(pdf,pagesize=(width,height))
    c.setStrokeColor('Black')
    c.rect(0.1*inch,0.1*inch,0.9*inch,2.7*inch,fill=0)
    c.setFillColor('Black')
    c.setFont("Helvetica", 4)
    c.drawRightString(0.8*inch, 2.7*inch, (details.get("values")[0]))
    c.drawString(0.8*inch, 2*inch, 'template 1')
    c.save()
    #print(pdf)
    
    #c.showPage()
    #c.save()

def generate_pdf_temp2():
    global details
    details=tree.item(tree.selection())
    width = 80
    height = 210
    pdf='D:\\Krishna sai\\Ktinker\\receipt.pdf'#'recieptttttttt.pdf'

    c=canvas.Canvas(pdf,pagesize=(width,height))
    c.setStrokeColor('Black')
    c.rect(0.1*inch,0.1*inch,0.9*inch,2.7*inch,fill=0)
    c.setFillColor('Black')
    c.setFont("Helvetica", 4)
    c.drawRightString(0.8*inch, 2.7*inch, (details.get("values")[0]))
    c.drawRightString(0.8*inch, 2*inch, 'template 2')
    c.save()

def generate_pdf_temp3():
    global details
    details=tree.item(tree.selection())
    width = 80
    height = 210
    pdf='D:\\Krishna sai\\Ktinker\\receipt.pdf'#'recieptttttttt.pdf'

    c=canvas.Canvas(pdf,pagesize=(width,height))
    c.setStrokeColor('Black')
    c.rect(0.1*inch,0.1*inch,0.9*inch,2.7*inch,fill=0)
    c.setFillColor('Black')
    c.setFont("Helvetica", 4)
    c.drawRightString(0.8*inch, 2.7*inch, (details.get("values")[0]))
    c.drawRightString(0.8*inch, 2*inch, 'template 3')
    c.save()

'''def selected():
    details=tree.item(tree.selection())
    
    print(details.get("values")[1])'''

def generate_pdf():
    #print(template_details)
    update_database()
    if (str(template_dropdown.get()))==template1 or (str(template_details)) == template1:
        if (str(template_dropdown.get())) and (str(template_details)):
            if (str(template_dropdown.get()))==template1:
                generate_pdf_temp1()
                clear_item()
            elif (str(template_dropdown.get()))==template2:
                generate_pdf_temp2()
                clear_item()
            else:
                generate_pdf_temp3()
                clear_item()
        else:
              generate_pdf_temp1  
              clear_item
        
    elif (str(template_dropdown.get()))==template2 or (str(template_details))== template2:
        if (str(template_dropdown.get())) and (str(template_details)):
            if (str(template_dropdown.get()))==template1:
                generate_pdf_temp1()
                clear_item()
            elif (str(template_dropdown.get()))==template2:
                generate_pdf_temp2()
                clear_item()
            else:
                generate_pdf_temp3()
                clear_item()
        else:
              generate_pdf_temp2
              clear_item
    else:
        if (str(template_dropdown.get())) and (str(template_details)):
            if (str(template_dropdown.get()))==template1:
                generate_pdf_temp1()
                clear_item()
            elif (str(template_dropdown.get()))==template2:
                generate_pdf_temp2()
                clear_item()
            else:
                generate_pdf_temp3()
                clear_item()
        else:
              generate_pdf_temp3
              clear_item       
    

template1="('template1',)"
template2="('template2',)"
template3="('template3',)"
#template_details= None
details=None
template_details= None


count=0




name_label=tkinter.Label(frame, text="Name", bg='yellow')
name_label.grid(row=0, column=0)

name_entry=tkinter.Entry(frame)
name_entry.grid(row=1, column=0)



check_button=tkinter.Button(frame, text="Check user", command= check)
check_button.grid(row=3, column=2)



manual_wt=tkinter.Label(frame, text="Manual Weight")
manual_wt.grid(row=0, column=2)
manual_wt_entry=tkinter.Entry(frame)
manual_wt_entry.grid(row=1,column=2)

item_code_label=tkinter.Label(frame, text="Item Code")
item_code_label.grid(row=2, column=0)
item_code_entry=tkinter.Entry(frame)
item_code_entry.grid(row=3,column=0)

item_name_label=tkinter.Label(frame, text="Item Name")
item_name_label.grid(row=2, column=1)
item_name_entry=tkinter.Entry(frame)
item_name_entry.grid(row=3, column=1)

check_button=tkinter.Button(frame, text="Check user", command= check)
check_button.grid(row=3, column=2)



gross_wt=tkinter.Label(frame, text="Gross Weight")
gross_wt.grid(row=0, column=1)
gross_wt_entry=tkinter.Entry(frame)
gross_wt_entry.grid(row=1, column=1)

add_new=tkinter.Button(frame, text="Add New", command=add_item)
add_new.grid(row=4, column=2, pady=5)

columns=('name', 'manual_weight', 'item_name', 'item_code', 'gross_weight')
tree=ttk.Treeview(frame, columns=columns, show="headings")
tree.heading('name', text='First Name')
tree.heading('manual_weight', text='Manual Weight')
tree.heading('item_name', text='Item Name')
tree.heading('item_code', text='Item code')
tree.heading('gross_weight', text='Gross Weight')
#tree.heading('s_no', text='S.No')
tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)



choices=['template1', 'template2', 'template3']
template_label=tkinter.Label(frame, text='Select template')
template_label.grid(row=6, column=1)
template_dropdown=ttk.Combobox(frame, values=choices)
template_dropdown.grid(row=7, column=1)

date_label=tkinter.Label(frame, text="Enter Date")
date_label.grid(row=6, column=3)
date_entry=DateEntry(frame)
date_entry.grid(row=7, column=3)

generate_print_button=tkinter.Button(frame, text="Generate Print", command=generate_pdf)
generate_print_button.grid(row=7, column=2,  padx=20, pady=5)
refresh_button=tkinter.Button(frame,text="Refresh", command=refresh)
refresh_button.grid(row=8, column=0, columnspan=3, sticky="news", padx=20, pady=5)
window.mainloop()








'''from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch 
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter, A4
import psycopg2

page_width=80
page_height=400
pdf='"D:\Krishna sai\Payment reciept\receipt.pdf"'
c=canvas.Canvas(pdf,pagesize=landscape((page_height*mm, page_width*mm)))

c.setFillColor('Black')
c.setFont("Helvetica", 29)
c.drawRightString(4.7*inch, 9.2*inch,'Metal Receipt Slip')'''