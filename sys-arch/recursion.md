# Recursion
Return address must be preserved across each recursive call.

```c
int fact(n) {
	if(n == 1) return 1;
	else return n * fact(n-1);
}
```
Assembles to
```assembly_mips
FACT:
	# If n > 1 then recurse
	subi $t0, $a0, 1
	bgtz $t0, REC 
	# Else return 1
	li $v0, 1
	j RET

REC: 
	# Allocate space on stack for argument and return address
	sw $a0, 4($sp)
	sw $ra, 0($sp)
	subi $a0, $a0, 1
	jal FACT
	# Pop off argument and return address
	lw $a0, 4($sp)
	lw $ra, 0($sp)
	addi $sp, $sp, 8
	# Return n*fact(n-1)
	$mul $v0, $v0, $a0

RET:
	jr $ra
```
