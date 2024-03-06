#Forensic CTF
- The goal of this ctf is to simulate as  close to real life a scenarion in which you are given a drive on which you must operate to obtain forensic evidence.
- Skills needed for this are:
   - Imaging a drive in a write-blocked manner using FTK, Autopsy, Sleuthkit or some other industry tool.
   - Recovering deleted files
   - Knowledge of a stegonography tool like steghide
   - Ability to interact with a DB like sqlite
   - File structure knowledge as it relates to finding browser history
   - Ability to read metadata from photos
 
## Step 1
 - Obtain the files that you will need off the babbage server, located at @babbage.cs.pdx.edu:/disk/scratch/dmcgrath
 - The two files are extra_drive.zip and windows_11.zip
 - Unzip the files
 - Create the vm using the .vhdx image from the windows 11 folder
 - attach the extra_dive to it using the .vhdx from the extra_drive folder

## Step 2
- Look around on the vm. See if there is anything that looks interesting, use the tools mentioned above
