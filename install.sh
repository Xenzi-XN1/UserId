#! /usr/bin/bash

null="> /dev/null 2>&1"
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
echo -e $b">"$w" UserId - Tool to retrieve Facebook "$g"Userid"
echo -e $b" >"$w" installing modules: "$g"requests"$w
pip3 install requests
echo -e $b" >"$w" successfully installing "$g"modules"
echo -e $b" >"$w" installing Tool: "$g"UserId"$w
wget -q https://raw.githubusercontent.com/Xenzi-XN1/UserId/main/userid.py -O $PREFIX/bin/userid && chmod +x $PREFIX/bin/userid
echo -e $b" >"$w" successfully installing "$g"UserId"
echo -e $b">"$w" use command "$g"userid"$w" for start the console"
