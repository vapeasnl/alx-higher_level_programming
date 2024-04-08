■ Done?  Get a sandbox
13. Add file mandatory
Write a function that returns the addition of 2 integers.
The function must be visible from outside
The name of the function must be add
You are not allowed to use var
Tip (/rltoken/1k6VPdLchwtGubOfPyGL1Q)
guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$
■ Done?  Get a sandbox
14. Const or not const #advanced
Write a file that modifies the value of myVar to 333
guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
