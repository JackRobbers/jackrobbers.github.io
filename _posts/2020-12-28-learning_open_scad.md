# Introduction

I'm going to try learning [https://www.openscad.org/](OpenSCAD). It's 3D CAD software that uses a domain specifc scripting language as the input. 

I think the first time I heard about OpenSCAD was in the description for an n by m lego brick model on . I've used some of the parametric features of 

# Learning

I started out by following the [https://en.wikibooks.org/wiki/OpenSCAD_Tutorial/](offical OpenSCAD tutorial).

Here's a few things I noticed while going through the tutorial. These are just some salient tips and quirks that stood out to me.

## Combining Objects 
    The tutorial stresses that in order for OpenSCAD to consider two objects the same thing, you need to subtract a small value (e.g 0.001) from the one of the objects along the edge they overlap so OpenSCAD knows that they are combined. This really doesn't seem like the cleanest solution to this problem, and I can see it leading to cumulative errors when you are combining many objects together in a stack.
## Program Style
    The tutorial uses a pattern where when single object that are modified by another function. They leave the semicolon off and indent

    I think it's much nicer to just always use the squiggly brackets.
## Scale vs Resize
    Scale takes the amounts to scale the object by in each direction.
    Resize takes the resulting dimensions