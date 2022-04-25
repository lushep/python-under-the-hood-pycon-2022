# Python under the hood: What so special about Python Objects?

## Abstract

Become a stronger and more confident Python programmer by learning the fundamentals of Python objects. 

If you've ever asked:

- Why do I have to pass a `string` in the function `len(string)` as an argumnet, when if I want to convert the string to upper case I use `string.upper()`?
- With a pandas dataframe why do I sometimes need brackets for example `df.describe()` as opposed to `df.shape`?
- What do people really mean when they say "everything in Python is an object?"

Then this tutorial is for you!

By the end of this tutorial, you will be able to build Python objects from scratch, leverage the magic of Python dunder methods (double underscore, like `__len__`) and extend existing classes to add functionality. These skills will expand your understanding of Python objects (and afterall, everything in Python is an object) so that you become more confident in writing Python programs. 

***Please note:*** this tutorial will not cover:
- Advanced object oriented principles
- Object oriented design patterns

### Technical Requirements / Training Materials

A laptop with Python installed is required for this workshop.

The tutorial will be delivered using Jupyter Notebooks; students will get a copy of all materials with which they can edit and complete exercises. 

## Audience

This tutorial is for Python programmers who have been using Python in their day to day and don't necessarily have a formal education or background in computer science. Students may have already heard of object oriented programming and even implemented their own classes, though this is not a requirement. 

To make the most out of this tutorial it is recommended that students already:
- Are able to write simple functions in Python, including those with default parameters, as you will use the same methodology to write methods
- Have Foundational knowledge of commonly used built-in Python objects: strings, lists, tuples and dictionaries

By the end of the tutorial students will be able to write simple classes with attributes and methods, use pythonic structures like dunder methods and extend existing class. This will improve students' intuition of Python objects enhancing their ability to read and write Python code which means that this subject is applicable to students working in any field where Python is used. 

## Format

The ratio of presentation to exercise will be 1:2*:
- Presentation & Demos (~1 hour): trainer-led. Student participation will be included (through polls, questioning and discussion) every 5-10 mins to increase student engagement and ownership of learning. 
- Exercises (~2 hours): Students will be in breakout groups and the trainer will move about giving support where necessary. After each exercise students will share ideas and discuss best practice.

*Introduction of the group and course is included in timing for the presentations.

### Outline

1. Intros including intro to Python objects (15 mins)
    - Introductions to get to know the group
    - Presentation: What are Python objects and why should we learn them?
2. The fundamentals of object oriented programming (40 mins)
    - Presentation/demo: Build a simple class and explain the method `__init__`
    - Exercise: Defining methods/attributes
    - Exercise: Add methods and attributes, instantiate the class and call the method
    - *Bonus** exercise: Changing the object from immutable to mutable - where do we see this in built-in Python objects?

**Break 10 mins**

3. Dunder methods (45 mins)
    - Demo: Add the dunder method `__len__`
    - Exercise: Add more dunder methods
    - *Bonus** Discussion: which objects can we deduce use dunder methods and why is this useful?
    - *Bonus** Exercise: Including protected and private variables in the class

**Break 10 mins**

4. Parent / Child classes (30 mins)
    - Demo: Add a child class to inherit methods/attributes from parent
    - Exercise: Add new child classes, including ones that overwrite parent methods
5. OOP in the wild (30 mins)
    - Exercise: Example exerts from typically used Python code. Groups will interpret and explain what is happening in the code, including why certain syntax is used and design choices were made.

### Outline notes

This is a 3-hour tutorial, including 2x 10 min breaks. To adapt to a 2 hour tutorial:
- only one break would take place
- the section on parent/child class would be removed

Other things to take into account
- *Bonus** sessions are included and will only be covered where suitable and would benefit the group, eg. if the group work particularly fast or already have a good understand on a certain topic
- **Presentations and demos** have participatory tasks every 5-10 mins in the form of polls, questioning or whiteboard responses, to increase engagement and develop ownership of own learning
- **Exercises** are differented by increasing in difficulty giving students the option to do the whole exercise or start from a mid-way point depending on their own ability

## Past Experience

I have worked as an instructor in Python for 2.5 years in two different trainer specific roles:

Apr 2019 - Nov 2020 | Global Data Technical Trainer at Bloomberg LP (London)
- Responsible for organising technical training for the Global Data team (~1000 people in AMER, APAC and EMEA) to improve data literacy through the adoption of Python. 
- Designed and delivered entire technical curriculum, particularly focusing on Data Analysis in Python.

Nov 2020 - Present | Data Science Educator at GoDataDriven (the Netherlands)
- Responsible for the Data Science with Python curriculum which includes designing and delivering training to companies and colleagues based all over the world. Trainings include data analysis/science with Python, advanced Python (including object oriented programming) and Python best practices as well as other courses such as data visualisation and storytelling and working with dbt Labs to deliver dbt Learn. 


## Delivering this topic
I already have the material as I designed this topic to be delivered for many of the courses I run, particularly those that generally focus on advanced python and python best practice. I have now delivered this topic in courses online over 10 times this year in public/open training that GoDataDriven offer as well as to particular companies/clients. 

What I have learned from this is that often Python programmers (especially those who are self-taught to a degree) have limited experience with this style of coding. It's often an area that gets neglected since a lot of code will not be written in this style, which may cause programmers to think it's not necessary. I argue otherwise as the subject generates many "lightbulb" moments for students when they see some of the concepts of Python that are often taken for granted. This is actually my own experience when I attended a course on this topic 3 years ago, and overall I believe it improves confident when writing and interpreting Python code.

Below is a link to the material I have used in the past which is based on the Deck example in Fluent Python. The material will be adapted to be made suitable for PyCon, which will include condensing the topics into one notebook and including a bonus directory for the bonus sections seen in the tutorial outline.
https://gdd.li/pycon-tutorial-python-objects
