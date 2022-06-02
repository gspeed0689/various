# various
Random IPYNBs and Python files

This is a collection of little things I've written to practice python, some are useful, some are silly, some are things. 

## eXtended Unique IDentifier (XUID)

Do you think to yourself that UUID doesn't provide enough random unique values to fit your application, or storing things like time and MAC addresses is too useful, and you don't want to be as crazy as AWS with internal 420-bit URNs, then have I got a package for you. 
XUID uses the whole alphanumeric space to create a unique string that you can use to uniquely identify all of your digital objects.

## Dynamic Salt

I read an article on how to allegedly store passwords, as in don't store the password but store a salted hash of the password, and compare a salted hash of the current password attempt to the one in the database. 
So I tried implementing something like that in python, but with different salt for different characters. 
