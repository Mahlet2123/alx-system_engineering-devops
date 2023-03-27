# 0x0B. SSH
By: Sylvain Kalache

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using #!/usr/bin/env bash instead of /bin/bash

## Tasks
### 0. Use a private key
- mandatory
- Score: 100.0% (Checks completed: 100.0%)

Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

	Requirements:

	Only use ssh single-character flags
	You cannot use -l
	You do not need to handle the case of a private key protected by a passphrase

---

	sylvain@ubuntu$ ./0-use_a_private_key
	ubuntu@server01:~$ exit
	Connection to 8.8.8.8 closed.
	sylvain@ubuntu$ 

### 1. Create an SSH key pair
- mandatory
- Score: 100.0% (Checks completed: 100.0%)

Write a Bash script that creates an RSA key pair.

Requirements:

Name of the created private key must be school
Number of bits in the created key to be created 4096
The created key must be protected by the passphrase betty

Example:

sylvain@ubuntu$ ls
1-create_ssh_key_pair
sylvain@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
sylvain@ubuntu$ ls
1-create_ssh_key_pair school  school.pub
sylvain@ubuntu$ 
