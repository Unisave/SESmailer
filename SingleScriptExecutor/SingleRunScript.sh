#!/bin/bash

echo -n "Input reciever name: "
read recipientName
echo -n "Input reciever mail ID: "
read RECIPIENT
echo -n "Input mail subject: "
read SUBJECT

python templateEngineMail.py -r "$recipientName"
sleep 2
python3 MailTerminalInterfaceable.py -s "$SUBJECT" -r "$RECIPIENT" -m output.html


