# Instruction set
* Set of native operations
* Programmer's view of machine
* Each opcode has two representations:
	* Machine readable binary number
	* Human-readable mnemonic
* A compiler converts code into machine-readable binary format

## Types

### Complex instruciton set/computer (CISC)
* Intel/AMD
* Rich instructions

### Reduced instruction set/computer (RISC)
* ARM/SPARC/MIPS/PowerPC
* Simple instructions
* Typically refer to "load/store" architectures

Modern CISC CPUs have RISC cores.

## Programming methodology
* Functional programming: what
* Imperative programming: what and how
* Assembly language: what, how and where (The resources available must be understood)

## MIPS architecture
![MIPS architecture](img/mips.png)

* 32-bit machine
	* Instructions are 32-bit
	* Data stored in 32-bit words
	* Addresses are 32-bit
	* Memory is byte-addressed
* 32 general purpose registers
* Most operations only use registers
* Core ste of around 60 instructions

### MIPS instruction types
* I-type: Requires 1+ registers and a constant
![I-Type instruction](img/i-type.png)
* R-type: Requires 3 registers and a constant
![R-Type instruction](img/r-type.png)
* J-type: Requires a constant
![J-Type instruction](img/j-type.png)
