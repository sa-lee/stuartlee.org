---
title: Theories of Data Analysis
author: Stuart Lee
date: '2017-03-21'
categories: 
  - EDA
  - graphics 
  - data analysis
  - statistical practice
  - uncertainty
---

In my reading of the literature on interactive graphics and exploratory data
analysis (a fair chunk of which was produced in the 70s and 80s) I have come
across many interesting papers that are still relevant to current issues
in science. The paper *Theories of Data Analysis from Magical Thinking Through Classical Statistics*
by Persi Diaconis ([link](https://doi.org/10.1002/9781118150702.ch1)) 
describes and explores the act of doing 'data analysis'. The paper
outlines ways in which the every practice of data analysis's different from 
the methods taught in classical statistics (i.e. analysts are humans that have their own
theories and biases), and the relationship between magical thinking and scientific thinking. 

Diaconis says that magical thinking is the tendency to see patterns in the noise and to persist believing false statements despite evidence to the contrary. Diaconis elaborates on this by drawing examples from from the experiments of Kahneman, Slovic and Tversky on judgement under uncertainty and William Cleveland's experiments on rescaling scatterplots. In the latter case, subjects believed there was a stronger linear association between two variables, when the axes were zoomed out even though they were looking at the same data. Diaconis concludes that,

> Once we note a pattern or take hold of an idea, it can be harder than seems normatively warranted to revise our belief. 

Diaconis provides examples of magical thinking in research (a familiar example is that of studies
from extrasensory perception studies, [heavily](http://andrewgelman.com/2011/01/06/that_silly_esp/) [discussed](http://andrewgelman.com/2011/01/11/one_more_time_o/) by Andrew Gelman.) and common ways an analyst can mislead themselves. Diaconis details examples of the garden of forking paths, multiple comparisons and 'peeking' at the data. 

Several practical 'remedies' are given to  control magical thinking. Diaconis understands the importance exploratory data analysis for generating new hypotheses and revealing the unexpected. He gives examples of data analyses of exploratory studies that avoid the use of P-values to generate insight. Of particular interest to me was using interactive 3D scatter plots of diabetes data using orthogonal projections.  Other remedies suggested including correcting for multiple comparisons, bootstrapping, cross-validation,  modelling the data generating process, replication and 'borrowing strength'. 

Diaconis finishes by discussing probability-free and Bayesian approaches to statistics, as well as the importance of using mathematics and computation to guide statistical practice. 

The paper provides a lot of thought-provoking examples and convincingly argues 
of the need for exploratory data analysis. I particularly liked this quote
about how statisticians can play a role in science:

> Once the statistician gives up the hubris of being "the decider", he or she can seize a vital role , helping to make science and technology function better, because groups and people now understand the quantitative aspects of the strengths of each other's results more clearly. 

