---
author: admin
categories:
- Instructional
comments: true
date: 2010-04-28 19:37:30+00:00
layout: post
slug: see-programming-abstractions-assignment-1
tags:
- Memory Allocation
- C
- Templates
- stanford
- CS106B
- E-learning
- see
- CS106A
- Letter Frequency Table
- Memory Diagramming
- Vectors
- Pointer Manipulation
- Function Pointers
- programming
- Structures
- String Manipulation
- Struct
- C++
- Graphics Card
- CUDA
- File Access
- cpp
- elearning
title: SEE, Programming Abstractions, Assignment 1
---


[SEE](http://see.stanford.edu/), or, Stanford Engineering Everywhere, has turned out to be my favourite E-learning resource; I've dipped into it a few times over the past few years but in light of my recent investment into a [CUDA](http://en.wikipedia.org/wiki/CUDA) enabled [Graphics Card](http://en.wikipedia.org/wiki/GeForce%209%20Series), I thought that it was coming high time to brush up on my [C++ programming](http://en.wikipedia.org/wiki/C%2B%2B), which I've basically left stagnant for two years after advancing no further than function pointers, structures, and templates.

So, in the spirit of openness that SEE tries to foster, I'll be blogging my work through their [CS106B course, Programming Abstractions](http://see.stanford.edu/see/courseinfo.aspx?coll=11f4f422-5670-4b4c-889c-008262e09e4e), the second of three programming courses. (I passed on [CS106A, Programming Methodology](http://see.stanford.edu/see/courseinfo.aspx?coll=824a47e1-135f-4508-a5aa-866adcae1111), since I've had enough Java shoved down my throat to last a lifetime...).

Now, I'll try not to repeat the lectures, and will focus mostly on the [Assignments](http://see.stanford.edu/see/materials/icspacs106b/assignments.aspx).

Straight into it, [Assignment 1](http://see.stanford.edu/materials/icspacs106b/H08-SectionHandout1.pdf) is split into several Problems, introducing String manipulation, Pointer manipulation, File access, Struct use, Vector templates, and Memory Diagramming.

### Problem 1:Pointers

Build two different functions to remove substrings from strings, one that returns a fresh 'new' string, and another that operates directly on an existing string in memory. Simple Enough (Well, there was one [Gotcha!](http://stackoverflow.com/questions/2709199/c-string-manipulation-isnt-making-sense-to-me) that I fell hook line and sinker for)

    
    string CensorString1(string text, string remove){
        string returned;
        size_t found=0, lastfound=0;
        found = text.find(remove);
        while (string::npos != found ){
            returned += text.substr(lastfound,found-lastfound);
            lastfound = found + remove.length();
            found = text.find(remove,lastfound);
        }
        returned += text.substr(lastfound);
        return returned;
    }

    
    void CensorString2(string& text, string remove){
        size_t found = text.find(remove);
        while ( string::npos != found){
            text.erase(found, remove.length());
            found = text.find(remove);
        } 
    
    }

### Problem 2: Struct

Build a structure definition to store statistical information about class grades read from a file, where each line is a mark between 0 and 100. Write a function to generate this structure with max/min/average, and return the structure. (I left some extra vestigial information in the structure such as the number of entries and the total total of marks for averaging purposes.

    
     struct gradestats {
         gradestats(){
             min=numeric_limits::max();
             max=numeric_limits::min();
             count=0;
             total=0;
             average=0;
         }
         int min,max,count,total;
         double average;
     };
    
    struct gradestats GradeStatistics(string filename){
        struct gradestats stats;
        int tempI;
        ifstream instream(filename.c_str());
        if(!instream.fail()){
            while(instream >> tempI){
                if(instream.fail || tempI < 0 || tempI > 100) continue;
                if(stats.min > tempI) stats.min = tempI;
                if(stats.max < tempI) stats.max = tempI;
                stats.total += tempI;
                stats.count++;
                stats.average = stats.total/stats.count;
            }
        } else {
            instream.clear();
            cout << "Something wicked this way comes!" << endl;
        }
        instream.close();
        return stats;
    }

### Problem 3: Vectors

Write a function that takes a filename and prints out a letter frequency table. (dont forget to include [fstream](http://en.wikipedia.org/wiki/Fstream))

    
    void CountLetters(string filename){
        int tempI;
        vector  counts(26,0);
        char tempC;
        ifstream instream(filename.c_str());
    
        if (!instream.fail()){
            do{
                tempC = std::tolower(tempC);
                if (!(tempC < 97 || tempC > 122)){
                    cout.put(tempC);
                    counts.at(tempC-97)++;
                }
                tempC = instream.get();
            }while ( tempC != EOF );
    
            cout < < endl;
    
            for (tempI=0;tempI < counts.size(); tempI++)
                cout << (char)(tempI + 97) << ":" << counts[tempI] << endl;
        } else {
            instream.clear();
            cout << "Something wicked this way comes!" << endl;
        }
    }

### Problem 4: Memory

I hate drawing diagrams, so I'll just hint; two structs 'exist' in the 'main' method stack, julie & tom. There's nothing in the heap, and the 'battle' method stack has one structure and one **reference** to a structure, and has a few internal variables (pos, level, name). The internal structure variables can be worked out easily enough (look out for the nasty character/integer modifications in the names).

### Conclusion

I could make a habit out of this! Interesting and useful challenges from a [world class CS department ](http://www-cs.stanford.edu/), all for free and accessible whenever you want / can.
