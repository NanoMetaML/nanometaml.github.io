---
title: Editing our Website 
subtitle: Welcome 👋 we know building an academic website can be intimidating, so we built this tutorial to help you maintain and add onto this website!

# Summary for listings and search engines
subtitle: Welcome 👋 we know building an academic website can be intimidating, so we built this tutorial to help you maintain and add onto this website!

# Link this post with a project
projects: []

# Date published
date: '2023-07-30T00:00:00Z'

# Date updated
lastmod: '2023-08-13T00:00:00Z'

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/CpkOjOcXdUY)'
  focal_point: ''
  placement: 2
  preview_only: false

authors:
  - blake_wilson

tags:
  - Academic

categories:
  - Demo
---

## Overview
If you don't have an academic website, you can't further your career! Or at least, that's how we see it. So, to help you build your academic hugo website, we'll give you free access to ours. It's pretty simple to setup and use. First thing is you'll need to clone our website source code.

```bash
mkdir my-website
cd my-website
git clone https://github.com/NanoMetaML/nanometaml.github.io.git
```

Great! Now you'll need to install [hugo](https://gohugo.io/) and [go-lang](https://go.dev/).
```bash
hugo server
```

Finally, open up your internet browser to localhost:<port> to the port given by the hugo server output and you should see your website!

Next, we recommend pushing your website to a github repo and adding a github action to build the website on every push. These are standard practice and can be found in the hugo documentation. We recommend using the github.io pages for hosting your website because it's free and integrates well with github.

