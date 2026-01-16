import tkinter as tk
import solver



def solve():
    output = ""
    #print("solving")
    #print(str(mode.get()))
    match str(mode.get()):
        case '1'|'2':
            output = solver.solve(int(mode.get()),str(question_text.get()),None)
            #print(output)
        case '3':
            output = solver.solve(int(mode.get()),str(question_text.get()),str(api_text.get()))
            #print(output)
        case '0':
            output = "Please change the mode"
        case _:
            output = "Mode selector error"
    txt_output.config(text=output)

def check_AI_use(sel_mode):
    if sel_mode == "3":
        api_txt_input.pack(padx=4,pady=4,fill="both")
    else:
        api_txt_input.pack_forget()


window = tk.Tk()
window.config(bg="CadetBlue3")

#title setup
frm_title = tk.Frame(width=256,height=96,relief="raised",borderwidth=5,padx=12,pady=12,bg="RoyalBlue4")
tk.Label(master=frm_title,text="O(1) Solver", font=("Helvetica",20),bg="RoyalBlue4").pack()
frm_title.pack(fill="x")

#input area setup
frm_input = tk.Frame(bg="RoyalBlue1",width=256,height=256)
tk.Label(master=frm_input,bg="RoyalBlue1",font=("Helvetica",15),text="Processor Input").pack()

#mode selector
frm_input_mode = tk.Frame(master=frm_input,bg="SlateBlue2",width=256,height=256,relief="ridge",borderwidth=4)

tk.Label(master=frm_input_mode,bg="SlateBlue2",font=("Helvetica",12),text="Processor Mode").pack()
mode = tk.StringVar(value="1")
opt_mode = tk.OptionMenu(frm_input_mode,mode,*["1","2","3"],command=lambda v: check_AI_use(v))
opt_mode.pack(padx=8,pady=8)

frm_input_mode.pack(fill="both",padx=12,pady=12)

#text input
frm_input_text = tk.Frame(master=frm_input,bg="DodgerBlue2",width=256,height=256,relief="ridge",borderwidth=4)
tk.Label(master=frm_input_text,bg = "DodgerBlue2",font=("Helvetica",12),text="Processor Text Input").pack()

question_text = tk.StringVar(value="Enter your question (also delete this)")
txt_input = tk.Entry(master=frm_input_text,bg="DodgerBlue2",borderwidth=4,textvariable=question_text)
txt_input.pack(padx=4,pady=4,fill="both")

api_text = tk.StringVar(value="Enter your api key (also delete this)")
api_txt_input = tk.Entry(master=frm_input_text,bg="DodgerBlue3",borderwidth=4,textvariable=api_text)

frm_input_text.pack(fill="both",padx=12,pady=12)

#solve button
btn_solve = tk.Button(master=frm_input,text="Solve",bg="orange3",font=("Helvetica",12), command=lambda : solve())
btn_solve.pack(padx=4,pady=4)

frm_input.pack(fill="both",padx=12,pady=12)


frm_output = tk.Frame(bg="OrangeRed3",)
tk.Label(master=frm_output,bg="OrangeRed3",font=("Helvetica",15),text="Processor Output").pack()

#output_text = tk.StringVar(value="")
txt_output = tk.Label(master=frm_output,bg="OrangeRed3", font=("Helvetica",12),relief="raised",borderwidth=4)#,textvariable=output_text)
txt_output.pack(fill="both",padx=12,pady=12)



frm_output.pack(fill="both",padx=12,pady=12)
#final closing stuff
window.minsize(512,768)
window.title("O(1) Solver")
window.mainloop()

