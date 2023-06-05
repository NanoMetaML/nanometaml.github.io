---
title: 'Machine learning framework for quantum sampling of highly constrained, continuous optimization problems'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - blake_wilson 
  - zhaxylyk_kudyshev 
  - alex_kildishev
  - vlad_shalaev
  - sasha_boltasseva

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

date: '2013-07-01T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2021-12-29T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# Publication name and optional abbreviated publication name.
publication: In *Applied Physics Reviews*
publication_short: In *APR*

abstract: In recent years, there is growing interest in using quantum computers for solving combinatorial optimization problems. In this work, we developed a generic, machine learning-based framework for mapping continuous-space inverse design problems into surrogate quadratic unconstrained binary optimization (QUBO) problems by employing a binary variational autoencoder and a factorization machine. The factorization machine is trained as a low-dimensional, binary surrogate model for the continuous design space and sampled using various QUBO samplers. Using the D-Wave Advantage hybrid sampler and simulated annealing, we demonstrate that by repeated resampling and retraining of the factorization machine, our framework finds designs that exhibit figures of merit exceeding those of its training set. We showcase the framework's performance on two inverse design problems by optimizing (i) thermal emitter topologies for thermophotovoltaic applications and (ii) diffractive meta-gratings for highly efficient beam steering. This technique can be further scaled to leverage future developments in quantum optimization to solve advanced inverse design problems for science and engineering applications.

# Summary. An optional shortened abstract.
summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
links:
- name: arXiv 
  url: https://arxiv.org/abs/2105.02396

url_pdf: 'https://engineering.purdue.edu/~shalaev/Publication_list_files/APR21-AR-00462.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: "" 
---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the _Slides_ button to check out the example.
{{% /callout %}}

Supplementary notes can be added here, including [code, math, and images](https://wowchemy.com/docs/writing-markdown-latex/).
