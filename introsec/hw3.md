# Homework 3

Due Date: 2024-05-05 23:59:59

* auto-gen TOC:
{:toc}

## Introduction

This homework lab will primarily cover password cracking. We will be using both `hashcat` and `john` to crack passwords and passphrases.

## What you must do

1. Join the following room on TryHackMe: [https://tryhackme.com/r/room/crackthehash](https://tryhackme.com/r/room/crackthehash). This room covers the basics of password cracking. Complete the exercise.

    Take a screenshot showing completion of the room. This should be included in your `hw3.md` file.

    Thoughts:
    * I strongly encourage you to make use of the hints. 
    * All passwords should make use of the `rockyou.txt` wordlist and `hashcat`. 
    * You may find `hashid` to be a useful tool. 
    * Please remember that the shell will interpret some characters, so you may need to escape them or wrap them in **single** quotes.

1. The previous exercise made use of `hashcat`. This will make use of `john`.  Redo the above room using `john`. Please record each hash and command used to crack it in your `hw3.md` file.

1. One of the best parts of `john` is the ability to convert many different things to a format that `john` can understand. This is done with one of the files `/usr/share/john/` on your kali VM.

    Use the following script to select 20 random lines from the `rockyou.txt` wordlist and save them to a file called `rockyou20.txt`:

    ```awk
   BEGIN {
       if (!n) {
           print "Usage: sample.awk -v n=[size]"
           exit
       }
       t = n
       srand()

   }

   NR <= n {
       pool[NR] = $0
       places[NR] = NR
       next

   }

   NR > n {
       t++
       M = int(rand()*t) + 1
       if (M <= n) {
           READ_NEXT_RECORD(M)
       }

   }

   END {
       if (NR < n) {
           print "sample.awk: Not enough records for sample" \
               > "/dev/stderr"
           exit
       }
       # gawk needs a numeric sort function
       # since it doesn't have one, zero-pad and sort alphabetically
       pad = length(NR)
       for (i in pool) {
           new_index = sprintf("%0" pad "d", i)
           newpool[new_index] = pool[i]
       }
       x = asorti(newpool, ordered)
       for (i = 1; i <= x; i++)
           print newpool[ordered[i]]

   }

   function READ_NEXT_RECORD(idx) {
       rec = places[idx]
       delete pool[rec]
       pool[NR] = $0
       places[idx] = NR  
   } 
     ```

   Run this script with `awk -f sample.awk -v n=20 /usr/share/wordlists/rockyou.txt > rockyou20.txt`

   * Use the script again on rockyou20.txt to select 3 random lines, combine those with spaces, and use that as the keyphrase for an ssh key of type ed25519. 
   * Use `python3 /usr/share/john/ssh2john.py` to convert the key to a format that `john` can understand.
   * Use hashcat to generate all possible 3-word passphrases from the `rockyou20.txt` wordlist and crack the key. You will need to look at the options for `hashcat` to generate all possible 3-word passphrases. Hints:
     * Look at the hashcat attack modes. One of them is 'combination'.
     * You will need to use the `--stdout` option to generate the passphrases.
     * You will likely need to run the command multiple times on incremental word lists to get all three-word combinations.
   * Use `john` to crack the key. You will need to look at the options for `john` to use a wordlist. 

   Record this whole process (commands used) in your `hw3.md` file.
1. You used `hashcat` to generate the combinations above. Write a `john` rule that will do the same thing.

## Submission

Once you have completed the above, you should have a markdown file in your repo called `hw3/hw3.md` that contains all the requested information. Commit and push this to your repo. Also commit and include any requested screenshots. Once you have done this, you can consider the assignment submitted.

In order to include output from your shell, see the [technical writing page](../technical_writing.md) for some basic instructions. For instance:

```sh
❯ ps -efH --no-header | awk '{print $1}' | grep -Ev $(python3 -c 'import sys; print("|".join(sys.argv[1:]))' $(cut -f1 -d':' /etc/passwd)) | sort | uniq -c | sort -rn | head -n 11
     30 USER01
     27 USER02
     24 USER03
     23 USER04
     23 USER05
     22 USER06
     22 USER07
     19 USER08
     19 USER09
     19 USER10
     18 USER11
```

Could be created with the following markdown:

````markdown
```sh
❯ ps -efH --no-header | awk '{print $1}' | grep -Ev $(python3 -c 'import sys; print("|".join(sys.argv[1:]))' $(cut -f1 -d':' /etc/passwd)) | sort | uniq -c | sort -rn | head -n 11
     30 USER01
     27 USER02
     24 USER03
     23 USER04
     23 USER05
     22 USER06
     22 USER07
     19 USER08
     19 USER09
     19 USER10
     18 USER11
```
````