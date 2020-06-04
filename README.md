# Skype for rest house
A solution to Skype your grandma/ grandpa in their rest house under confinment

Note: this will be filled in ;).

## Background
With the COVID crisis it could be hard to meet your relatives and if they are not familiar with some video-conferencing technologies, it could be very hard for them not to stay isolated.

This small project build a solution which require zero interaction for them to be able to receive a Skype call.  It only relies on Microsoft Skype, a Linux (ubuntu) box and some configuration.

## Concept
We rely on a Intel NUC running a Ubuntu Desktop edition. The computer is connected via HDMI to the TV for video and sound while a USB webcam offer a video stream from your relative.  The computer is remotelly controlled via SSH (command line) and RealVNC which give a user interface access to start and stop Skype.

As it could be hard for your relative to control the TV, we also create a Arduino based remote controlled driven by the NUC.  We therefore can change the input source back and forth and tune the volume if required.

Skype is configured to accept all incoming call from the adress book.  To avoid privacy issue, Skype as to be started when convenient for your relative and stopped afterward.

## Note
The documentation is in French :).  We might translate if there is a request or need for it :).
Feel free to open an issue on this project to request translation or feel free to contribute.

## Special Thanks
To Emilien Le Jamtel for the idea to use Skype ;).
