Advancing to the next stage:  
As previously instructed, proceed to the `challenge` directory, then execute the `embryogdb_level5` file. Subsequently, utilize the `run` command to execute the program.  

```bash
We write code in order to express an idea which can be reproduced and refined.  
We can think of our analysis as a program which injests the target to be analyzed as data.  
As the saying goes, code is data and data is code.

While using gdb interactively as we have done with the past levels is incredibly powerful, another powerful tool is gdb scripting.  
By scripting gdb, you can very quickly create a custom-tailored program analysis tool.  
If you know how to interact with gdb, you already know how to write a gdb script--the syntax is exactly the same.  
You can write your commands to some file, for example `x.gdb`, and then launch gdb using the flag `-x <PATH_TO_SCRIPT>`.  
This file will execute all of the gdb commands after gdb launches.  
Alternatively, you can execute individual commands with `-ex '<COMMAND>'`.  
You can pass multiple commands with multiple `-ex` arguments.  
Finally, you can have some commands be always executed for any gdb session by putting them in `~/.gdbinit`.  
You probably want to put `set disassembly-flavor intel` in there.  

Within gdb scripting, a very powerful construct is breakpoint commands. 
Consider the following gdb script:
  start
  break *main+42
  commands
    x/gx $rbp-0x32
    continue
  end
  continue

In this case, whenever we hit the instruction at `main+42`, we will output a particular local variable and then continue execution.

Now consider a similar, but slightly more advanced script using some commands you have not seen yet:
  start
  break *main+42
  commands
    silent
    set $local_variable = *(unsigned long long*)($rbp-0x32)
    printf "Current value: %llx\n", $local_variable
    continue
  end
  continue

In this case, the `silent` indicates that we want gdb to not report that we have hit a breakpoint, to make the output a bit cleaner.  
Then we use the `set` command to define a variable within our gdb session, whose value is our local variable.  
Finally, we output the current value using a formatted string.
```

Now, let's write our first gdb scripting file.

```gdb
run
break *main+721
display/6gx $rsp
continue
```

To run this `.gdb` extension file, use this command: `gdb ./<executable_file> -x <.gdb_file>`  

The above script starts the program, sets the breakpoint, and displays the values of the stack.  
Using this information, we can copy the respective value, continue, and paste it into the program. 

After repeating this process a few times, you will obtain the flag.  
<!-- Flag: ~pwn.college{wrYITQuz-p33ii1_1asyBMnJDIt.0FO0IDL4UDOzQzW}~ -->
Let's proceed to the next level.  
