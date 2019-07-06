# Print Hello World! on console

.data                                   # Data declaration section
message: .asciiz "Hello World!\n";    

.text                                   # Start of code section
main:                
        la $a0, message                 # Load the address of the message into the $a0 register
        li $v0, 4                       # Load 4 into the $v0 register to tell the processor that you want to print a string
        syscall
        
        li $v0, 10                      # Load 10 into the $v0 register
        syscall

