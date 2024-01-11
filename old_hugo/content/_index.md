---
# Leave the homepage title empty to use the site title
title:
date: 2023-06-01
type: landing

sections:
  - block: markdown 
    content: 
      title: Welcome!
    design:
      columns: '1'
  - block: collection
    id: posts
    content:
      title: Recent Posts
      subtitle: ''
      text: ''
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        folders:
          - post
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: compact
      columns: '2'
  - block: collection
    id: featured
    content:
      title: Featured Publications
      filters:
        folders:
          - publication
        featured_only: true
    design:
      columns: '2'
      view: card

#
#  - block: portfolio
#    id: projects
#    content:
#      title: Projects
#      filters:
#        folders:
#          - project
#      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
#      default_button_index: 0
#      # Filter toolbar (optional).
#      # Add or remove as many filters (`filter_button` instances) as you like.
#      # To show all items, set `tag` to "*".
#      # To filter by a specific tag, set `tag` to an existing tag name.
#      # To remove the toolbar, delete the entire `filter_button` block.
#      buttons:
#        - name: All
#          tag: '*'
#        - name: Deep Learning
#          tag: Deep Learning
#        - name: Other
#          tag: Demo
#    design:
#      # Choose how many columns the section has. Valid values: '1' or '2'.
#      columns: '1'
#      view: showcase
#      # For Showcase view, flip alternate rows?
#      flip_alt_rows: false

  - block : people

# This file represents a page section.
    headless: true

# Order that this section appears on the page.
    weight: 40

    id: authors
    title: Meet the Team
    subtitle:

    content:

      text: Welcome to the NanoML team's website! Started in 2021 by Blake Wilson under the supervision of our PI's, we are a team of researchers at Purdue University and Oak Ridge National Lab working on the intersection of quantum computing, nanophotonics, and machine learning. Our team develops high quality machine learning code and we hope it is useful for your projects! We focus on speeding up the characterization of materials in laboratory settings, generation of unique nanophotonic and quantum devices, and fast algorithms written in Python. We take a first principles approach to develop new perspectives at the intersection of physics, computer science, and machine learning. 
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
        - Principal Investigators
        - Postdoctoral Fellows
        - Graduate Students
        - Undergraduate Students
        - Alumni
    design:
      show_interests: false
      show_role: true
      show_social: true

  - block: markdown
    content:
      title: Gallery
      subtitle: ''
      text: |-
        {{< gallery album="gallery" >}}
    design:
      columns: '1'
---
