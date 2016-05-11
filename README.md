# VBAandLDAP
System/Applications Used
Outlook 2013
VBA 7.1
Linux (RHEL 5)
Python 2.7.9
Assumption you understand how to use a bash script

This repository contains the files you will need to have in place to parse a string of text from an email or multiple emails in a folder 
and save it to an excel file and then running that file on an LDAP query for each record line and convert output to csv format and email the file which is then used as a mail merge (hence the csv need).

This is a 3 step process, which can be adjusted but I'd gone in a different direction but felt that maybe somewhere this might be useful for someone. The VB script, pulls a string of text, determined by RegEx, and puts it into an excel file and saves that file. This was used on automatic notifaction emails where the string of text we needed came in the same format every time. The string we grabbed was a UID that was resided in the users AD record. The string was being pulled from the emails and put into an excel file because VB script was friendlier within the Microsoft Office suite than out, but this would be better if the string was saved to a text file rather than excel since the final format of the data pulled from the email needed is text. 

1. Run VB script to creat Excel file. 
2. Save contents to a text file. 
3. Run bash script on Command line

The bash script will run the file, line by line, on LDAP and print the output to a file in LDIF format. You will use the LDIFtoCSV by https://github.com/tachang/ldiftocsv.git to convert LDIF to csv 

Using mutt to send the email as an attachment to person who needs this csv file for the mail merge. 
