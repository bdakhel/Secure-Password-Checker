# Secure-Password-Checker
A program that checks if your password is secure and has not been detected in a leak using "have i been pwned?"'s API. To make it more secure, using the concept of hashing you can check your password locally without providing "have i been pwned?" your password.
# Requirements
Before using the program, ensure you have python3 is downloaded as well as the requests, sys and hashlib python libraries
# Usage
Open your terminal and perform a git clone: 
``` 
git clone https://github.com/bdakhel/Secure-Password-Checker.git
```
Type into the terminal:
```
cd Secure-Password-Checker
```
Type into the terminal: 
```
python3 checkmypass.py "password"
```
where "password" is the password you would like to check. The program should print if your password is secure.
