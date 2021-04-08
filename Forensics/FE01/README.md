# FE01 - 100pts

## Briefing

> Download the file and find a way to get the flag. Contents: fe01.ost

Challenge Files:

* [fe01.zip](./fe01.zip)

## Solution

1. We can run `file fe01.ost` to determine that `fe01.ost` is a Microsoft Outlook email folder.

2. Searching online for a program that can read this identifies `pffexport`, which can be installed with `sudo apt install pff-tools`.

3. We can extract the content with `pffexport fe01.ost` and `cd` into `fe01.ost.export`.

4. Run `find . -type d -empty -delete` **in `fe01.ost.export`** to delete all empty directories.

5. Searching the folder for `flag` shows that `Root - Mailbox/IPM_SUBTREE/Inbox/Message00018/Attachments` has a ZIP file called `1_flag.zip` (as an attachment to the `Message00018` email) that is password protected.

6. Looking around some more reveals that the calendar contains the key. `Root - Mailbox/IPM_SUBTREE/Calendar/Appointment00001/Appointment.txt` has the name `c]5p@S7K/z}Z!Q  -  11am meeting with Chris` so `c]5p@S7K/z}Z!Q` is the password.

7. Extracting the `1_flag.zip` with `c]5p@S7K/z}Z!Q` as the password shows an image `flag.jpg` with the flag in it.

### Flag

`pst_i'm_in_here!`
