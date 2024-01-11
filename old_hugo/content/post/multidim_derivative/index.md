---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Multidim_derivative"
subtitle: ""
summary: ""
authors: []
tags: []
categories: []
date: 2023-06-14T06:10:43-07:00
lastmod: 2023-06-14T06:10:43-07:00
featured: false
draft: true

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---


## What is the gradient?

In machine learning, we use gradients all the time. But, what is it?

$\lim_{\Delta x \rightarrow 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}$

This is the definition in one dimension. But, in multiple dimensions we work with vectors $\hat{r}$. The analagous definition is:

$\lim_{\Delta \hat{r} \rightarrow 0} \frac{f(\hat{r} + \Delta \hat{r}) - f(\hat{r})}{\Delta \hat{r}}$

In one dimension, $\Delta x$ was well defined. However, in multiple dimensions, $\Delta \hat{r}$ could take several values because all directions are valid. For simplicity, we define.. 
