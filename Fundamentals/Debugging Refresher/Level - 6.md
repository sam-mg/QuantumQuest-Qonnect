Ok, lets now begin with the next level.
As previously instructed, proceed to the `challenge` directory, then execute the `embryogdb_level5` file. Subsequently, utilize the `run` command to execute the program.  

```bash
As it turns out, gdb has FULL control over the target process. Not only can you analyze the program's state, but you can
also modify it. While gdb probably isn't the best tool for doing long term maintenance on a program, sometimes it can be
useful to quickly modify the behavior of your target process in order to more easily analyze it.

You can modify the state of your target program with the `set` command. For example, you can use `set $rdi = 0` to zero
out $rdi. You can use `set *((uint64_t *) $rsp) = 0x1234` to set the first value on the stack to 0x1234. You can use
`set *((uint16_t *) 0x31337000) = 0x1337` to set 2 bytes at 0x31337000 to 0x1337.

Suppose your target is some networked application which reads from some socket on fd 42. Maybe it would be easier for
the purposes of your analysis if the target instead read from stdin. You could achieve something like that with the
following gdb script:

  start
  catch syscall read
  commands
    silent
    if ($rdi == 42)
      set $rdi = 0
    end
    continue
  end
  continue

This example gdb script demonstrates how you can automatically break on system calls, and how you can use conditions
within your commands to conditionally perform gdb commands.
```

```sh
```

We have to write our own script to solve this level.
<!-- Flag: ~pwn.college{MUmuZOepSOT2ANvKPLEmx311MP7.0VO0IDL4UDOzQzW}~ -->
<!-- I got this flag using the command `call (void)win()`. -->