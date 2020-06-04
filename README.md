# Skype for rest house
*A solution to Skype your elderly loved ones stuck in their rest house during this isolation period.*

## Background
With the COVID crisis, it is sometimes hard to meet relatives, especially if they are not familiar with video-conferencing technologies.
It is also important for the most vulnerable ones not to stay isolated.

This small project proposes a solution which requires zero interaction from them to be able to receive a Skype call.
It only relies on Microsoft Skype, a Linux (Ubuntu) box and a bit of configuration.

## Concept
We rely on a Intel NUC running an Ubuntu Desktop edition.
The computer is connected to the TV via HDMI for video and sound.
A webcam filming your relative is connected over USB.
The computer is remotely controlled via SSH (command line) or [RealVNC](https://www.realvnc.com).
These interfaces are used to start and stop Skype.

Since it may be hard for your relative to control the TV, we also designed a Arduino-based IR remote control driven by the NUC: input source can be changed back and forth, the volume can be tuned if required, etc.

Skype is configured to accept all incoming calls from the address book.
To avoid privacy issues, Skype has to be manually started when convenient for your relative, and stopped afterwards.

## Note
The documentation is in French.
Translation can be done upon request :)
Feel free to open issues for requests, and feel free to contribute.

## Special Thanks
To Emilien Le Jamtel for the original inspiration ;)
