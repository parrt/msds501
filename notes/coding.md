# Coding

*in progress*

## Computation model

Memory just holds data; all of the action happens in the processor, which has five principal operations:
 
* load chunks of data from memory into the processor
* perform arithmetic computations
* conditionally perform computations
* repeat steps
* store chunks of data back to memory

Processors execute low-level *machine instructions* that perform one or more of those principal operations. Each instruction does a tiny amount of work but the processor can do them extremely fast, on the order of billions a second.  A program then is just a sequence of these low-level instructions. Writing a program in these low-level machine instructions would be extremely tedious, so we typically use programming languages such as Python to make our lives easier. Each high-level instruction such as the following actually force the processor to execute multiple low-level instructions.

```
total = cost + tax
```

The processor must load `cost` and `tax` from memory, add the two values, then store the result in memory at the address associated with `total`.

Unless given instructions to the contrary, the processor keeps executing instructions one after the other.
 
## operations

First, what are you given? what's unknown? Ok, now write down the comp u expect to perform. Now give some samples,
 
Step one means getting a list of numbers, which we can assume is a given.

is this similar to something I've solved before?

 by starting at the last step in working our way backwards

 this highlights that you should start from the result, the last step, and work your way backwards

analogy with a food truck that picks up raw materials at one spot drives down the road chooses a fork in the road, prepares food en route, then delivers prepared food at a different location. This might circle back to get more  raw materials.
 
 At the other extreme there can be preprogrammed high-level operations that can, for example, display a bar chart given a list of numbers.