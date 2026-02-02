---
categories:
- Uni
comments: true
date: 2010-03-10 09:49:40+00:00
slug: so-what-can-you-do-with-32-million-passwords
tags:
- 'Application Security'
- Cybersecurity
- 'Data Security'
- Education
- EeePC
- Hacking
- Linux
- Networking
- QUB
- cybersecurity
title: So what can you do with 32 Million Passwords...
---


So I have a piece of coursework for a [CS module](http://www.qub.ac.uk/schools/eeecs/Education/Undergraduates/ModuleSummaries/ModuleInformation/?CrsCode=CSC3048) I'm taking at [Queen's University Belfast](http://www.qub.ac.uk/schools/eeecs/) and one of the focal points of it is the recent [RockYou! SQL-injection breach](http://techcrunch.com/2009/12/14/rockyou-hack-security-myspace-facebook-passwords/) that released 32million passwords into the internet, and I thought I'd have a closer look at that list.

I 'acquired' the password list from your regular neighbourhood tracker, and thought I could walk through the process of getting a probability-sorted password dictionary.

(The '-S 2048K' memory restriction on the 'sort' program is to avoid Dreamhost locking out my process for being over-memory)

> tar -xvzf UserAccount-passwords.tgz

Having a look at the head of the resultant 'UserAccount-passwords.txt' file shows:

>

>
> $ head UserAccount-passwords.txt
>
>

>
> password
>
>

>
> mekster11
>
>

>
> mekster11
>
>

>
> mekster11
>
>

>
> progr4sm
>
>

>
> khas8950
>
>

>
> emilio1
>
>

>
> holiday2
>
>

>
> caitlin1
>
>

>
> purblanca

32million entries in arbitrary order arn't really that useful, so I sorted them alphabetically first (-d)

> sort -d -S 2048K UserAccount-passwords.txt -o UserAccount-passwords.sorted.txt

And getting a head again gave a whole pile of blank lines, so to get rid of them use [this handy sed expression](http://www.cyberciti.biz/faq/howto-linux-unix-command-remove-all-blank-lines/)

> $ sed '/^$/d' UserAccount-passwords.sorted.txt > UserAccount-passwords.sorted.unblanked.txt

So our first ten passwords are now:

> $ head UserAccount-passwords.sorted.unblanked.txt

!

!!!!

!!!!!

!!!!!

!!!!!

!!!!!

!!!!!

!!!!!

!!!!!

!!!!!

Loooots of duplicates, so we'll get rid of them

> uniq -cd UserAccount-passwords.sorted.unblanked.txt UserAccount-passwords.uniq.txt

The -d flag means that we only want to know about entries that appear at least twice, and  the -c means we only want one line for each password and a count for how often it appears (This reduced the number of lines in the list from 32,603,048 non-blank entries to 2,459,759), giving a first ten of:

> $head UserAccount-passwords.uniq.txt

12 !!!!!

67 !!!!!!

3 !!!!!!!

3 !!!!!!!!

8 !!!!!!!!!!

2 !!!"""Â£Â£Â£

2 !!!$$$

2 !!!???

2 !!!@@@

2 !!""Â£Â£

Still sorted alphabetically, so sort reverse-numerically to get most popular entries at the top.

>

>
> sort -nr -S 2048K UserAccount-passwords.uniq.txt -o UserAccount-passwords.uniq.sorted.txt

Giving our top 20 most popular passwords (sorry guys, but this is really depressing)

> $ head -20 UserAccount-passwords.uniq.sorted.txt

290729 123456

79076 12345

76789 123456789

59462 password

49952 iloveyou

33291 princess

21725 1234567

20901 rockyou

20553 12345678

16648 abc123

16227 nicole

15308 daniel

15163 babygirl

14726 monkey

14331 lovely

14103 jessica

13984 654321

13981 michael

13488 ashley

13456 qwerty

There really is no hope for us...

More analysis to come when I can be bothered, and potentially some attempts at breaking into a VM with simulated user accounts.
