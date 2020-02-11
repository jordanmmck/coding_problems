# OS

## Process vs Thread

`Process`: a "program" that has a state (scheduling, data, stack, etc.) within the OS that isn't shared, processes can only communicate through interprocess communication facilities

`Thread`: threads are typically spawned by a process and multiple threads can be attached to one process, they share the process's data/address space and can interact with other threads from the same process. This sharing of "global" information makes it easier to threads to work on the same data than processes. Also, creating a thread is less expensive than creating a new process (through fork or whatever).
