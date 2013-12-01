---
author: admin
comments: false
date: 2008-05-12 13:10:00+00:00
layout: post
slug: embedded-c-gps-project
title: Embedded C GPS Project
categories:
- Instructional
tags:
- C
- code
- Embedded
- GPS
- LCD
---

Afternoon folks, I'm supposed to be studying but dont have the heart to, so I'm documenting a recent project from Uni.  
  
The remit was to be able to parse RS232 data coming in from a GPS unit and reformat it for a LCD display. I dont have the part numbers handy but I was programming on a 18F series PIC that supported C.  
  
Most of the ancillary code is more platform dependant, such as working with the PIC interrupts etc, so for the purposes of this code snippit, assumme that a [NMEA](http://gpsinformation.org/dale/nmea.htm) sentence (I used RMC and some RMB, but never really finished that bit) stored as a character buffer, and a structure, as defined, to store relevent data in.  
  
PLEASE read up about NMEA sentence structure before continuing  
  
{% highlight Cpp %}
typedef    struct message  
   {  
       //date  
       int day, month, year;  
     
       //Time  
       int hour, min, sec;  
  
       //lat  
       int lat_deg;  
       float lat_min;  
       char lat_ref;  
         
       //lng  
       int lng_deg;  
       float lng_min;  
       char lng_ref;  
           
   }message;  
{%endhighlight%}
  
Since NMEA sentences are comma separated values, I kinda cheated and iterated thru the string, replacing the commas with terminating characters and recording the next positions as character pointers.  
  
{% highlight Cpp %}
for(i=0;i<BUFFERSIZE;i++){  
 if(end)buffer[i]=0;        //wipe the rest of the sentence        
  
 if(buffer[i]==42&&check==1){        //asterix  
  check=0;  
  if(checksum==chr2hex(&buffer[i+1])) valid=1;  
  else valid=0;  
  
  i+=2;          //get to the end of the checksum  
  
  end=1;          //this is the end of the current sentence  
 }  
 if(check)checksum^=buffer[i];  
 if(buffer[i]==36){        //dollarsign  
  
  buffer[i]=0;  
  
  check=1;  
  
  AddToList(&(buffer[i+1]));     //ignore first character  
  
 }  
 if(buffer[i]==44){  
  buffer[i]=0;     //replace all commas with nulls  
  AddToList(&(buffer[i+1]));   //add next position to list of words  
 }  
}  
  
{%endhighlight%}
  
The first character(dollar sign) is ignored because it is never needed beyond this point.  
  
The NMEA sentence structure includes a asterix delimited checksum, i.e everything after the dollarsign and before the asterix is progressivly XOR'd and the hex value representation of this result is concatenated on the end of the sentence before transmission.  
  
the chr2 hex function simply converts two ASCII characters to their Hex value equivalent.  
  
AddToList, strangly enough, adds the pointer passed to it to a wordlist, which is an array of character pointers.  
  
Now we have a list of pointers, because i used a character pointer array, and ended all the strings with nulls, we essentially now have individual strings for each part of the NMEA sentence, that can be addressed directly. eg:  
{% highlight Cpp %}
{        //GPRMC  
           getTime(words[1],&incoming);  
           getDate(words[9],&incoming);  
           getLat(words[3],&incoming,*words[3+1]);  
           getLng(words[5],&incoming,*words[5+1]);  
}  
  
{%endhighlight%}
In this instance, the get functions all take two arguments, what to read from, and where to put it.  
  
For anyone whos interested the full code is [here](http://bolster.homelinux.net:81/projects/gps/GPS.c)  
  
I guess i better do some work then.  
  
  

Please at least pretend to click my ads. I know they're a joke, but still, it dont cost ya anything!
