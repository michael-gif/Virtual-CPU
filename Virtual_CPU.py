import tkinter as tk
instructions = []
registers = [0,0,0,0,0,0]
memory = [1,0,0,0,0,0,0,0]
instructioncount = 0
accumulator = 0
app = tk.Tk()
app.title("Virtual CPU")
app.geometry('1365x525')
app.configure(background='gray25')
app.iconbitmap(r'cpuicon.ico')
app.resizable(0,0)

def updateregisters():
    registervalue1.set("0: " + str(registers[0]))
    registervalue2.set("1: " + str(registers[1]))
    registervalue3.set("2: " + str(registers[2]))
    registervalue4.set("3: " + str(registers[3]))
    registervalue5.set("4: " + str(registers[4]))
    registervalue6.set("5: " + str(registers[5]))
    memoryvalue1.set("0: " + str(memory[0]))
    memoryvalue2.set("1: " + str(memory[1]))
    memoryvalue3.set("2: " + str(memory[2]))
    memoryvalue4.set("3: " + str(memory[3]))
    memoryvalue5.set("4: " + str(memory[4]))
    memoryvalue6.set("5: " + str(memory[5]))
    memoryvalue7.set("6: " + str(memory[6]))
    memoryvalue8.set("7: " + str(memory[7]))

def clearsequence():
    global instructions, instructioncount
    listbox1.delete(0,'end')
    instructions = []
    instructioncount = 0

def clearprevious():
    global instructions, instructioncount
    listbox1.delete('end')
    instructioncount -= 1
    instructions.pop(len(instructions)-1)

def decodebinary(value):
    total = 0
    if value[0] == "1":
        total += 8
    if value[1] == "1":
        total += 4
    if value[2] == "1":
        total += 2
    if value[3] == "1":
        total += 1
    return total

def changelabelvalue():
    global instructions, instructioncount
    change = entryvalue.get()
    if change.isalpha() == False:
        instructioncount += 1
        if len(change) > 4:
            print("Error:entry length max exceeded")
            change = change[:4]
            listbox1.insert('end', str(instructioncount) + ": " + change)
            instructions.append(change)
        elif len(change) < 4:
            print("Error:entry length insufficient")
            change = change + "0"*(4-len(change))
            listbox1.insert('end', str(instructioncount) + ": " + change)
            instructions.append(change)
        else:
            listbox1.insert('end', str(instructioncount) + ": " + change)
            instructions.append(change)
    else:
        print("Error:entry type invalid")

def startprogram():
    global registers, memory, accumulator
    x = 0
    reg1 = 0
    reg2 = 0
    while x < len(instructions):
        if instructions[x] == "0000":
            listbox2.insert('end',"Executing " + str(x+1) + ": " + instructions[x] + "\n")
            command = instructions[x+1]
            data = decodebinary(command)
            command = instructions[x+2]
            address = decodebinary(command)
            memory[address] = data
            updateregisters()
            x += 3            
        elif instructions[x] == "0001":
            listbox2.insert('end',"Executing " + str(x+1) + ": " + instructions[x] + "\n")
            command = instructions[x+1]
            address = decodebinary(command)
            data = memory[address]
            command = instructions[x+2]
            register = decodebinary(command)
            registers[register] = data
            updateregisters()
            x += 3
        elif instructions[x] == "0010":
            listbox2.insert('end',"Executing " + str(x+1) + ": " + instructions[x] + "\n")
            command = instructions[x+1]
            storelocation = decodebinary(command)
            memory[storelocation] = accumulator
            updateregisters()
            x += 2
        elif instructions[x] == "0011":
            listbox2.insert('end',"Executing " + str(x+1) + ": " + instructions[x] + "\n")
            command = instructions[x+1]
            reg1 = decodebinary(command)
            command = instructions[x+2]
            reg2 = decodebinary(command)
            accumulator = registers[reg1] + registers[reg2]
            accumulatorvalue.set(accumulator)
            updateregisters()
            x += 3
        elif instructions[x] == "0100":
            listbox2.insert('end',"Executing " + str(x+1) + ": " + instructions[x] + "\n")
            command = instructions[x+1]
            reg1 = decodebinary(command)
            command = instructions[x+2]
            reg2 = decodebinary(command)
            accumulator = registers[reg1] - registers[reg2]
            accumulatorvalue.set(accumulator)
            x += 3
        elif instructions[x] == "0101":
            listbox2.insert('end',"Executing " + str(x+1) + ": " + instructions[x] + "\n")
            command = instructions[x+1]
            reg1 = decodebinary(command)
            command = instructions[x+2]
            reg2 = decodebinary(command)
            accumulator = registers[reg1] * registers[reg2]
            accumulatorvalue.set(accumulator)
            x += 3
        elif instructions[x] == "0110":
            listbox2.insert('end',"Executing " + str(x+1) + ": " + instructions[x] + "\n")
            command = instructions[x+1]
            reg1 = decodebinary(command)
            command = instructions[x+2]
            reg2 = decodebinary(command)
            accumulator = registers[reg1] / registers[reg2]
            accumulatorvalue.set(accumulator)
            x += 3
        else:
            print("Error:entry invalid")
            x = len(instructions)

#sequence box
labeltext = tk.StringVar(app)
labeltext.set("")
label1=tk.Label(app,bg='black',fg='white',textvariable=labeltext,anchor='nw').place(x=10,y=30,width=150,height=250)
listbox1 = tk.Listbox(app,bg="black",fg="white")
listbox1.place(x=10,y=30,width=150,height=250)
listbox1.yview()

#program counter box
listbox2 = tk.Listbox(app,bg="black",fg="white")
listbox2.place(x=170,y=30,width=150,height=250)
listbox2.yview()

#register boxes
registervalue1 = tk.StringVar(app)
registervalue2 = tk.StringVar(app)
registervalue3 = tk.StringVar(app)
registervalue4 = tk.StringVar(app)
registervalue5 = tk.StringVar(app)
registervalue6 = tk.StringVar(app)
registerlabel1 = tk.Label(app,bg="black",fg='white',textvariable=registervalue1,anchor='w').place(x=330,y=30,width=100)
registerlabel2 = tk.Label(app,bg="black",fg='white',textvariable=registervalue2,anchor='w').place(x=330,y=60,width=100)
registerlabel3 = tk.Label(app,bg="black",fg='white',textvariable=registervalue3,anchor='w').place(x=330,y=90,width=100)
registerlabel4 = tk.Label(app,bg="black",fg='white',textvariable=registervalue4,anchor='w').place(x=330,y=120,width=100)
registerlabel5 = tk.Label(app,bg="black",fg='white',textvariable=registervalue5,anchor='w').place(x=330,y=150,width=100)
registerlabel6 = tk.Label(app,bg="black",fg='white',textvariable=registervalue6,anchor='w').place(x=330,y=180,width=100)

#memory boxes
memoryvalue1 = tk.StringVar(app)
memoryvalue2 = tk.StringVar(app)
memoryvalue3 = tk.StringVar(app)
memoryvalue4 = tk.StringVar(app)
memoryvalue5 = tk.StringVar(app)
memoryvalue6 = tk.StringVar(app)
memoryvalue7 = tk.StringVar(app)
memoryvalue8 = tk.StringVar(app)
memorylabel1 = tk.Label(app,bg="black",fg='white',textvariable=memoryvalue1,anchor='w').place(x=440,y=30,width=100)
memorylabel2 = tk.Label(app,bg="black",fg='white',textvariable=memoryvalue2,anchor='w').place(x=440,y=60,width=100)
memorylabel3 = tk.Label(app,bg="black",fg='white',textvariable=memoryvalue3,anchor='w').place(x=440,y=90,width=100)
memorylabel4 = tk.Label(app,bg="black",fg='white',textvariable=memoryvalue4,anchor='w').place(x=440,y=120,width=100)
memorylabel5 = tk.Label(app,bg="black",fg='white',textvariable=memoryvalue5,anchor='w').place(x=440,y=150,width=100)
memorylabel6 = tk.Label(app,bg="black",fg='white',textvariable=memoryvalue6,anchor='w').place(x=440,y=180,width=100)
memorylabel7 = tk.Label(app,bg="black",fg='white',textvariable=memoryvalue7,anchor='w').place(x=440,y=210,width=100)
memorylabel8 = tk.Label(app,bg="black",fg='white',textvariable=memoryvalue8,anchor='w').place(x=440,y=240,width=100)

#ALU box
accumulatorvalue = tk.StringVar(app)
accumulatorlabel = tk.Label(app,bg="black",fg='white',textvariable=accumulatorvalue).place(x=550,y=30,width=100)

#titles
tk.Label(app,text="Sequence:",bg='grey25',fg='snow').place(x=10,y=5)
tk.Label(app,text="Instruction:",bg='grey25',fg='snow').place(x=10,y=285)
tk.Label(app,text="Program Counter Output:",bg='grey25',fg='snow').place(x=170,y=5)
tk.Label(app,text="Register Values:",bg='grey25',fg='snow').place(x=330,y=5)
tk.Label(app,text="Memory Values:",bg='grey25',fg='snow').place(x=440,y=5)
tk.Label(app,text="ALU Output:",bg='grey25',fg='snow').place(x=550,y=5)

#Guide text
tk.Label(app,text="Guide:",bg='grey25',fg='snow').place(x=660,y=5)

tk.Label(app,text="0000",bg='grey25',fg='snow').place(x=660,y=25)
tk.Label(app,text="Function: Sets memory values.",bg='grey25',fg='snow').place(x=660,y=45)
tk.Label(app,text="Usage: Enter 0000, followed by the binary data followed by the binary address of the desired memory cell.",bg='grey25',fg='snow').place(x=660,y=65)

tk.Label(app,text="0001",bg='grey25',fg='snow').place(x=660,y=95)
tk.Label(app,text="Function: Loads a value from memory to a register.",bg='grey25',fg='snow').place(x=660,y=115)
tk.Label(app,text="Usage: Enter 0001, followed by the binary address of the data in memory followed by the binary address of the desired register.",bg='grey25',fg='snow').place(x=660,y=135)

tk.Label(app,text="0010",bg='grey25',fg='snow').place(x=660,y=165)
tk.Label(app,text="Function: Stores the result in memory.",bg='grey25',fg='snow').place(x=660,y=185)
tk.Label(app,text="Usage: Enter 0011, then the address of the memory where the data willl be stored.",bg='grey25',fg='snow').place(x=660,y=205)

tk.Label(app,text="0011",bg='grey25',fg='snow').place(x=660,y=235)
tk.Label(app,text="Function: Adds two registers.",bg='grey25',fg='snow').place(x=660,y=255)
tk.Label(app,text="Usage: Enter 0010, then the register number containing the first number, then the register number containing the second number.",bg='grey25',fg='snow').place(x=660,y=275)

tk.Label(app,text="0100",bg='grey25',fg='snow').place(x=660,y=305)
tk.Label(app,text="Function: Subtracts two registers.",bg='grey25',fg='snow').place(x=660,y=325)
tk.Label(app,text="Usage: Enter 0100, then the register number containing the first number, then the register number containing the second number.",bg='grey25',fg='snow').place(x=660,y=345)

tk.Label(app,text="0101",bg='grey25',fg='snow').place(x=660,y=375)
tk.Label(app,text="Function: Multiplies two registers.",bg='grey25',fg='snow').place(x=660,y=395)
tk.Label(app,text="Usage: Enter 0101, then the register number containing the first number, then the register number containing the second number.",bg='grey25',fg='snow').place(x=660,y=415)

tk.Label(app,text="0110",bg='grey25',fg='snow').place(x=660,y=445)
tk.Label(app,text="Function: Divides two registers.",bg='grey25',fg='snow').place(x=660,y=465)
tk.Label(app,text="Usage: Enter 0110, then the register number containing the first number, then the register number containing the second number.",bg='grey25',fg='snow').place(x=660,y=485)

#instruction input box
entryvalue = tk.StringVar(app)
entry1 = tk.Entry(app,textvariable=entryvalue).place(x=75,y=285,width=85)

#buttons
button = tk.Button(app,text="Add Instruction",bg='grey40',command=changelabelvalue).place(x=10,y=310,width=150)
button2 = tk.Button(app,text="Run Program",bg='grey40',command=startprogram).place(x=170,y=310,width=150)
button3 = tk.Button(app,text="Clear Sequence",bg='grey40',command=clearsequence).place(x=10,y=340,width = 150)
button3 = tk.Button(app,text="Clear Previous",bg='grey40',command=clearprevious).place(x=10,y=370,width = 150)

#set intial register and memory values
updateregisters()

tk.mainloop()
