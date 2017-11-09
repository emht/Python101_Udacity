Take A Break
============

Take a break is a python script used to notify the user who is using his computer longer than s/he should.  The script will open the selected playlist of songs for the user to relax and enjoy his health.

How To Run
==========

1. 
2. 
3.

Requirements
============
* webbrowser: To open the webbrowser to play the songs from youtube, change it for spotify app or something in future.
*
*

Implementation
==============
The pseudocode for the program would be like the following:

1. Read the time at which system starts and save it somewhere.
2. Keep the track of time passing by.
3. After a certain interval of Time (set by the user), screen goes total blank, blocking every mouse and keyboard interrupt except a control kill switch (just in case), and a set of user-defined song playlist starts to play for a certain period of time (as defined by the user).
4. The start time for the next session is reset and this whole cycle repeats itself.


repeat three times:
	* Wait "x" hours.
	* Open Web Browser

1. Add functionality for every 20 minutes, short breaks.
2. After every one hour, long breaks of 10 minutes.
