# Launching a Virtual Machine at Amazon Web Services

The goal of this lecture-lab is to teach you to create a Linux machine at *Amazon Web Services*, login and copy some data to that machine.

##  Discussion

Login to AWS and go to your [AWS console](http://aws.amazon.com/console) and click on the "EC2" link.

<img src=images/console_snippet.png width=200>

Click "Launch Instance", which will start the process to create a virtual machine in the cloud. An instance is just a virtual machine.

<img src=images/launch.png width=400>

Select the "Amazon Linux AMI" entry, which should be the first one.  This is a commonly-used "image" that results in a Linux machine that contains lots of useful goodies as you can see from that list, such as Python and MySQL. An image is just a snapshot of the disk after someone carefully installs software properly on a Linux machine. This means we don't have to install software every time we create a new machine.

<img src=images/ami.png width=600>

Select instance type "t2.micro," which should be the first machine type listed. This machine is very low powered but is sufficient for playing around. Click "Review and launch"

<img src=images/selectvm.png width=600>

This will bring up a screen describing the details about the instance we are launching. ignore all of it for now and just click "Launch" at the bottom right.

This will bring a dialog box up to select a key pair. A key pair is what allows you to securely access the server and prevent unauthorized access. The *first time*, you will need to create a new key pair. Name it as your user ID then click on "Download key pair."  It will download a *userid*.pem file, which are your security credentials for getting into the machine. Save that file in a safe spot. If you lose it you will not be able to get into the machine that you create. From now on, you can reuse this existing key.

<img src=images/keypair.png width=600>

Click on the "I acknowledge that I have ..." checkbox then "Launch instance." You should see something like:

<img src=images/launched.png width=600>

Click on the `i-...` link to go to the EC2 console showing your instance.

<img src=images/ec2-instance.png width=600>

Click on your instance and you should see a description box at the bottom. Look for the "Public IP" address, which is 54.196.174.210 in this case:

<img src=images/publicIP.png width=600>

Click on the "Connect" button at the top of the page and it will bring up a dialog box that tells you how to connect to the server.  You want to connect with "A standalone SSH client" link (Java is now a security risk in the browser so we can't use that choice.)  Inside you will see the `ssh` command necessary to connect to your machine. If you have Windows, there is a link to show you how to use an SSH client called PuTTY. 

<img src=images/connect.png width=550>

 Before we can connect, we have to make sure that the security file is not visible to everyone on the computer (other users). Otherwise ssh will not let us connect because the security file is not secure:

```bash@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for '/Users/parrt/Dropbox/licenses/parrt.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
bad permissions: ignore key: /Users/parrt/Dropbox/licenses/parrt.pem
Permission denied (publickey).
```

Whoa!  Do this:

```bash
$ cd ~/Dropbox/licenses
$ ls -l parrt.pem
-rw-r--r--@ 1 parrt  parrt  1696 Aug  4 15:15 /Users/parrt/Dropbox/licences/parrt.pem
```

To fix the permissions, we can use whatever "show information about file" GUI your operating system has or, from the command line, do this:

```bash
$ cd ~/Dropbox/licenses
$ chmod 400 parrt.pem
```

which changes the permissions like this:

```bash
$ ls -l parrt.pem
-rw-------@ 1 parrt  501  1696 Aug  1 12:12 /Users/parrt/Dropbox/licenses/parrt.pem
```

Don't worry if you don't understand exactly what's going on there. It's basically saying that the file is only read-write for me, the current user, with no permissions to anybody else.

For mac and linux users, we will use the direct `ssh` command from the command line. It will be something like:

```bash
ssh -i parrt.pem ec2-user@54.196.174.210
```

Naturally, you will have to provide the full pathname to your *userid*.pem file.

 Try to connect again and it will now warn you that you have never connected to that machine before. Again, this is a security measure. You can simply say "yes" here.

```bash
$ ssh -i parrt.pem ec2-user@54.196.174.210
The authenticity of host '54.196.174.210 (54.196.174.210)' can't be established.
ECDSA key fingerprint is SHA256:BYGiV2qRthhw52HQni5vnoRtiT16cplmdbXAuXqQdqc.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '54.196.174.210' (ECDSA) to the list of known hosts.
Last login: Thu Aug  4 20:04:07 2016 from sentinel.cs.usfca.edu

       __|  __|_  )
       _|  (     /   Amazon Linux AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-ami/2016.03-release-notes/
8 package(s) needed for security, out of 17 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-30-0-97 ~]$ 
```

The `$` is your prompt just like you have on your local machine using the terminal / shell, but you are giving commands to a remote server not your local machine.

To get data up to the server, you can cut-and-paste if the file is small. For example,  cut-and-paste the following data into a file called `coffee` in your home directory. First copy this data from the PDF:

```bash
3 parrt
2 jcoker
8 tombu
```

then type these commands and paste the data in the sequence:

```bash
[ec2-user@ip-172-30-0-97 ~]$ cd ~ # get to my home directory
[ec2-user@ip-172-30-0-97 ~]$ cat > coffee
3 parrt
2 jcoker
8 tombu
^D
[ec2-user@ip-172-30-0-97 ~]$ cat coffee # print it back out
3 parrt
2 jcoker
8 tombu
$ 
```

The `^D` means control-D, which means end of file.  `cat` is reading from standard input and writing to the file because of the redirection operator `>`. The way it knows we are done is when we signal in the file with control-D *on a line by itself*.

For larger files, we need to use the secure copy `scp` command that has the same argument structure as secure shell `ssh`. Get another shell up on your laptop. From the directory where you have the `coffee` file *on your laptop*, use the following similar command:

```bash
$ scp -i parrt.pem access.log ec2-user@54.196.174.210:~ec2-user
access.log                                    100% 1363KB   1.3MB/s   00:00
$ 
```

Do not forget the `~ec2-user` on the end of that line. The `access.log` file is at github under `msan501` repo in `data`.  From the shell that is connected to the remote server, ask for the directory listing and you will see the new file:

```bash
[ec2-user@ip-172-30-0-97 ~]$ ls
access.log  coffee
[ec2-user@ip-172-30-0-97 ~]$ head access.log # print the first few lines of file
64.221.136.91 - - [02/Sep/2003:00:00:09 -0700] "GET / HTTP/1.1" 200 11690 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Win 9x 4.90; Q312461)"
64.221.136.91 - - [02/Sep/2003:00:00:10 -0700] "GET /images/shim.gif HTTP/1.1" 200 43 "http://www.antlr.org/" "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Win 9x 4.90; Q312461)"
...
```

To exit the remote server, type `exit` or use `^D` from the `$` prompt. The machine will still be running but you're no longer connected to it from your laptop.

Play around with your instance and then **TERMINATE YOUR INSTANCE WHEN YOU ARE DONE**, otherwise you will continue to get charged for the use of that machine. Right-click on the instance from your AWS console and select "instance state" then submenu "terminate". It will warn you that all of your local storage will go away. Hit the "yes, terminate" button. It should look like this when done:

<img src=images/terminated.png width=450>

If you say "stop" instead, it will stop the machine, but you still get charged. On the other hand, this is useful because you can restart that machine without having to go through this whole procedure. All of your data will be intact. If you say "Terminate", it will toss the machine out and you will have to go through this procedure again to get a new machine.
