---
aliases:
- /2011/02/bolsters-code-related-rants-an-ongoing-collection.html
categories:
- Commentary
comments: true
date: 2011-02-12 18:21:53+00:00
slug: bolsters-code-related-rants-an-ongoing-collection
tags:
- Opinion
- Programming
- Rant
- development
- file management
- version control
title: Bolsters Code-Related Rants (An ongoing collection)
---
![FFFFFFUUUUUUUU](http://kissmyalas.com/wp-content/uploads/2010/05/RageFace.jpg)


  * Logging functions being called with just a variable and no comment as to **what the hell it is**


  * _logging_ has functions more than logging.info, **use them!**


    * _Debug_ = **useful** information if something **breaks** but isn't interesting during normal operation


    * _info_ = useful and generally **interesting** information


    * _warn_ = something went **wrong**, indicating something should probably be refactored / fixed,_ but the system could recover from it._


    * _error_ = **oh dear jesus fuck the entire site evaporated into a swarm of zombie locusts, I better put something in the error log.**


  * Commented out historical code! Using a version control system means you can go back to **any** point in the history of the codebase and see how we used to do something; you don't need dozens of lines of extraneous code 'just in case'


  * **Checking in inoperable code to the default branch** (I know I'm guilty of this sometimes too). If major changes to one section are being made, do it in a **branch**, that's what branches are there for. Then, when the new functionality is stable, update **your** local code with respect to the default branch, then make sure** all the functionality still works** and **only** **then** commit and check it in to default


  * Non existent or orphan files; if you add a new file,`hg add $filename` before updating or committing, otherwise noone has any idea whats going on. Ditto removals of files, its `hg remove $filename ; rm $filename`, not the other way around.

You guys got any to add? I'll be adding to this as I think of them... / come across them...
