# Virtual-CPU
It takes instructions and executes them.

Guide:

0000
Function: Sets memory values.
Usage: Enter 0000, followed by the binary data followed by the binary address of the desired memory cell.

0001
Function: Loads a value from memory to a register.
Usage: Enter 0001, followed by the binary address of the data in memory followed by the binary address of the desired register.

0010
Function: Stores the result in memory.
Usage: Enter 0011, then the address of the memory where the data willl be stored.

0011
Function: Adds two numbers and outputs it to the ALU
Usage: Enter 0010, then the register number containing the first number, then the register number containing the second number.

0100
Function: Subtracts two numbers and outputs it to the ALU
Usage: Enter 0010, then the register number containing the first number, then the register number containing the second number.

0101
Function: Multiplies two numbers and outputs it to the ALU.
Usage: Enter 0100, then the register number containing the first number, then the register number containing the second number.

0110
Function: Divides two numbers and outputs it to the ALU.
Usage: Enter 0100, then the register number containing the first number, then the register number containing the second number.
