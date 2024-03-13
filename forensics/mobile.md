## Introduction

Gavin Heartthrob is a celebrity arrested by the Urbana, Illinois police department. After his arrest, Tabitha Paparazzi published details of the investigation in the local newspaper, The News-Gazette. These details were clearly from the sealed police report, though Tabitha denies contacting anyone within the police department. Investigators found some pages of the report left in Crystal Lake Park, though they were unable to determine how they got there. Officer David Leeks has reportedly been behaving strangely by his fellow officers, and an extra cellular phone was retrieved from his patrol car.

Tabitha’s phone number is 217-550-3657.

## Android backup forensics
Files to use:

* mob.dd.bz2

## Rooted device forensics

An Android backup file does not contain much sensitive user data. This data is accessible in the /data folder on the device, which is only viewable by the root user on the device. To obtain access to this data, we needed to root the device. Rooting a device is the process of gaining root access to the device. This is a form of privilege escalation attack against the device firmware, so it shouldn't be taken lightly. We are altering the device, which is dangerous in a forensics context. It also isn't always easy.

With a rooted Android device, the Android Debug Bridge can be used to open a shell on the device using the command abd shell. This opens a Unix shell on the device. We used this shell to issue commands to change to the root user, locate the /data partition, and invoke dd to create an image of the /data partition on a SIM card. We then recovered this image file from the SIM card (mob.dd) Mount the image with the following commands.

```sh
mkdir ~/mobile
sudo mount -t ext4 -o loop,noexec mob.dd ~/mobile
```

You now have access to a Unix ext4 partition. All of the forensic techniques you have learned in previous labs can now be applied to this device (including file carving.) Most Android data is stored in SQLite databases. Here are a few databases of interest.

* ~/mobile/data/com.android.providers.telephony/databases/mmssms.db
* ~/mobile/data/com.android.providers.contacts/databases/contacts2.db
* ~/mobile/data/com.android.browser/databases/browser2.db

The files in this directory might also be of interest:

* ~/mobile/data/com.google.android.apps.maps/cache/http/

The rest of this investigation is up to you. Build the strongest case you can. Some useful information you should look for: the owner of the device, its phone number, and IMEI. You might also try to find the call records and look for any geolocation data cached on the device.
