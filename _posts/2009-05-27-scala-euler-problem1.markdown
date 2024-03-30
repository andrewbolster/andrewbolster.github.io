---
author: admin
categories:
- Commentary
comments: false
date: 2009-05-27 13:44:10+00:00
layout: post
slug: scala-euler-problem1
tags:
- code
- algorithms
- github
- project-euler
- scala
- mathematics
- programming
title: Scala-Euler Problem1
---


Finished my approach to [Euler Problem 1 ](http://projecteuler.net/index.php?section=problems&id=1)last night and checked everything into [github](http://github.com/andrewbolster/Scala-Euler/blob/bc53f88a481354e65370e68d317219e9839e60ea/src/euler/Problem1.scala).

> 

> 
> 

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Was not happy with limiting the specific factors of 3 and 5, and limit of 1000 so i implemented a generalised solution.

> 

>     
>     def solution(fs: List[Int], max: Int ) = ( 1 until max ).filter( f => fs.exists( n => f % n == 0)).foldLeft(0)(_+_)
> 
> 

Where fs is a List of integer factors and max is obv the highest limit. eg(Answer is in white font, so select the line "Answer" to see it

> 

>     
>     print("Answer: ",solution(List(3,5),1000))
>     >Answer: <span style="color: #ffffff;"><strong>233168</strong></span>
> 
> 

Thanks to [@lichtsprung ](http://twitter.com/lichtsprung)for the testing help.

The general aim is to complete a few dozen of these in [Scala](http://www.scala-lang.org/), then switch to [Java](http://www.java.com/en/), or[ C/C++](http://www.cprogramming.com/), or something else, and loop around until i have a[ complete library of euler problems](http://projecteuler.net/index.php?section=view_all) for all of the languages i end up using; Nothing like having long term goals!
