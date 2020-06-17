---
title: Lecturing data analysis online
author: ~
date: '2020-06-17'
slug: teaching-during-a-pandemic
categories: []
tags: [education, teaching-statistics, corrupting-the-youth]
---

_Warning: a long-winded reflection on lecturing (for the first time ever) and having to suddenly do it online; skip to the end to see the cool interactive dashboards produced by the students in my class._

For the last twelve weeks I have been lecturing an [introductory data analysis
course](mida.numbat.space) for Monash's Masters of Business Analytics program. 
The before times format for the course is what has been dubbed 'lectorial'style, 
which is a ~~fancy~~ ugly  way of saying the classroom is flipped: students work
through lab based exercises while the lecturer and teaching assistants roam
through the class guiding the students through any issues. Occasionally
the class stops while the lecturer explains some tricky concept or reveals
a solution to the class. This semester we managed to do one traditional
lectorial during which a university wide email was sent detailing that 
live-action classes were cancelled (a most sensible action). 

Switching to a fully online class, presented many challenges to the 'lectorial' 
format, however I was fortunate enough that the syllabus and content of the course
was well established by my supervisor Di Cook and colleague Nick Tierney [^1].
It was also at this time that Greg Wilson did a very timely seminar titled
[Teaching Online On Short Notice](https://education.rstudio.com/blog/2020/03/teaching-online-on-short-notice/)
that provided useful tips (with some that I should have definitely followed
more closely!). I learnt a lot from lecturing and was lucky that the
students were so motivated and thoughtful, if you don't read the rest of the
post please take some time to look at some of the really creative projects
they put together [^2]. 

As we move to the new normal of learning and teaching online, I wanted
to take some time to reflect on what I thought worked and areas for improvement [^3].

## The good and not so good parts

I tried following the keep everything as simple as possible principle, however
there were two big parts of the course that needed to be adapted:
the running of lectorials and assessments.

Each lectorial consists of students learning a few new concepts and
putting those concepts into practice via working through lab exercises
contained in R markdown documents. I ended up splitting this up into a
pre-recorded lecture and having ordinary class time be an interactive 
walk-through of lab exercises on Zoom. I think the latter approach worked well. 
Students could ask questions on the chat to me and other students, 
make predictions on the output based (what will this code produce), see that 
I make mistakes when coding and call them out. I tried to get
students actively engaged by via the "What questions do you have?" framing
but I found that it was consistently the same students who would unmute and 
answer my questions or have questions. I felt uncomfortable calling
out a specific student. Perhaps this problem would have been mitigated through the use
of breakout rooms which I had tried early on but found awkward as no one 
really know each other yet and all the rooms were eerily quiet. I think I could've
also made better use of the poll feature in Zoom. What is 
a good way of getting to know and engage students and for students to get to know each other 
during an online class? I missed that aspect most when compared to the online 
class.

In hindsight, it was a mistake to pre-record the conceptual parts
of the lectorials too. I had polled the students about having pre-recorded 
lectures instead of a live stream and the overwhelming majority said they 
preferred having a pre-recorded video. I'm not sure if they were right in this 
case, as I would often have to remind them of the content during the live 
stream, as not everyone got around to watching the video. A selfish reason for 
not pre-recording is that it ended up being a lot of work. It was always 
tempting to keep editing the videos or do another take. It was tricky trying to 
work out whether the explanations I came up with made sense when you're talking
to a computer. I definitely should have listened to the advice of Greg Wilson
here!

The three big assessments for the course were the mid-semester test, a 
data analysis practical exam, and a group project. The test and exam
were ordinarily done during class time, which makes preventing cheating
question modifications much simpler. I wrote a new online test using the
excellent [exams](http://www.r-exams.org/) R package which allowed us to 
template questions using (R)markdown and upload them directly to the units 
learning management system. This was one of those tasks that could be mostly 
automated but did require a lot of tweaking and testing and showed me that it's
really hard to write good exam questions. Hopefully it'll be useful for 
future iterations of the course to start building up a question bank. 

The data analysis practical exam was written by Nick and Di, and is meant to 
emulate a real data analysis. This year the students analysed Australia's 
covid19 data, with the goal of submitting a reproducible report (HTML + Rmd) 
that answered the questions we posed. The expectation was to produce the output 
within 24 hours of the exam being  posted and I relied on our tutors hand-marking 
the results to pick up things like cheating and plagiarism. 

The group project is challenging (but also fun) assessment for the class [^4]. Students
work in teams to create a digital artefact that summarises some interesting
findings from a 'real world' dataset they've found or collected.
I personally think this is the most valuable component of the course, in that
it shows students how messy working with data can be and emphasises the 
importance some of the stuff that I harked on and on about during the course
(like analysis workflow, looking at your data and thinking about its 
limitations). It's also great as they have a piece of work they can show 
off to the world. I had the most fun in the classes where we worked on the
projects (I used break out-rooms here!), it was fun seeing what everyone 
had come up with and having a discussion about their aims. In the final
presentations it was really great seeing how proud everyone was of their work.

## Letting students shiny

I want to end by showing off some of my favourite group projects for
the semester (they were made using `shiny` or `flexdashboard` or a 
combination of both!).  If you click on the image under each description 
you'll be redirected to our department's shiny server, they might
take a little while to load but I reckon it's worth the wait!

### Group Pompous Assets: Happiness Around the World

This dashboard was created by 
[Priya Ravindra Dingorkar](https://twitter.com/DingorkarPriya), 
[Dewi Amaliah](https://twitter.com/dlamaliah), Brenwin Ang and Davide Signor.
It pulls together some metrics for happiness around the world and explores
what things are important for different regions happiness. 

{{% figure src="./happiness.png" width="75%" link="https://ebsmonash.shinyapps.io/ETC5510-group-pompous-assets" class="center" %}}


### Group ggplot2: A Tale of Two Presidents

This dashboard was created by [Dilinie Seimon](https://twitter.com/dilinie_seimon) and 
Emily Sheehan and explores twitter data (that they collected) and approval
ratings of the past two US presidents. I really liked the presentation and
narrative flow of this analysis. 

{{% figure src="./pres.png" width="75%" link="https://ebsmonash.shinyapps.io/ETC5510-group-ggplot2/" class="center" %}}

### Group VHS: That's What The PM Said

This dashboard was created by [Hahn Ngo](https://twitter.com/HaiHanhNgo), 
[Varsha Ujjinni Vijay Kumar](https://twitter.com/uv_varsha) and Sam Lyubic.
They scraped all of the Australian PMs recent media releases, speeches, and 
so on, performed a tidy-text analysis on them and related them to current events.

{{% figure src="./vhs.png" width="75%" link="https://ebsmonash.shinyapps.io/ETC5510-group-vhs/" class="center" %}}

## Acknowledgements

It is challenging teaching a modern data analysis course that gives students
somewhat of an insight in the realities of working with data. I think this 
kind of course would not be possible without the tooling available from
Rstudio that let's students get up and running really quickly and producing
interesting stuff in the first class. I would also like to thank Nick and Di
again for all the work they've put into designing this course, I wish I had
one like it when I was at uni! Finally, a big thank you to all my students
and all the hard work you've put in, especially during these very uncertain times!

[^1]: who was also in the same boat running the undergrad stream of this course. A big thank you to Nick, Di,  and the TAs Steff Kobakian and Sherry Zhang for providing so much support and being there when it felt like everything was falling apart. 

[^2]: The dashboards below are just a few of my favourites! It's really impressive, the creativity and scope of the projects and even more so when you note that most students had no prior R or programming (and very little stats) experience.

[^3]: If you're one of my 5510 students reading this, please send me an email if you think I've got this wrong :wink:.

[^4]: A minor problem for the online format is coordinating and rearranging groups. If there is a better solution than sending long email chains, contact me!
