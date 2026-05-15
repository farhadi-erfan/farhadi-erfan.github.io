---
layout: about
title: about
permalink: /
subtitle: Writer, Programmer, Designer
nav: false

profile:
  align: right
  image: "https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/photo_2023-01-03_19-46-23.jpg"
  image_circular: false
  more_info: >
    University of Rochester<br>
    Computer Science<br>
    Rochester, NY

selected_papers: false
social: true

announcements:
  enabled: false
  scrollable: false
  limit: 10
latest_posts:
  enabled: false
---

<style>
  html { scroll-behavior: smooth; }
  h2 { scroll-margin-top: 5rem; }
  .page-nav { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.25rem 0 2rem 0; }
  .page-nav a { border: 1px solid var(--global-divider-color); border-radius: 999px; padding: 0.35rem 0.75rem; font-size: 0.9rem; text-decoration: none; }
  .portfolio-img { display: block; max-width: 100%; width: min(100%, 760px); max-height: 460px; object-fit: contain; margin: 1rem auto 1.75rem auto; border-radius: 0.5rem; }
  .portfolio-img.poster { width: min(100%, 420px); max-height: 640px; }
  .soft-highlight { background: rgba(255, 230, 120, 0.35); border-radius: 0.2rem; padding: 0 0.15rem; font-size: 1em; }
</style>

<nav class="page-nav">
  <a href="#about">About</a>
  <a href="#news">News</a>
  <a href="#publications">Publications</a>
  <a href="#projects">Projects</a>
</nav>

## About {#about}

I am a PhD student in Computer Science at the University of Rochester, advised by Prof. Zhen Bai. I design and study <span class="soft-highlight">embodied agents</span> and <span class="soft-highlight">interactive AI literacy experiences</span>, especially learning systems where students encounter AI through games, spatial interaction, tangible metaphors, and exploratory environments.

My background moves between engineering, cinema, and education. I studied Computer Engineering at Sharif University of Technology and Cinema Studies at Soore University of Arts, and that mix still shapes my work: I often think of technology not only as software, but also as a medium for narrative, culture, learning, and imagination. This thread also appears in my cinema/AI work, from movie-scene search and narrative pattern mining to VLM-based analysis of cinematic style.

Along the way, I contributed to SSC, co-founded the educational NGO [Rasta](https://rastaiha.ir), taught programming and creative writing at NODET schools, published short stories, directed podcasts and radio plays, and designed and curated the exhibition and curriculum for [Iran's Computer Museum](https://computermuseum.ir/). For me, research, software, games, and film are different ways of asking the same question: how can we build experiences that help people <span class="soft-highlight">see the world differently</span>?

## News {#news}

{% include news.liquid limit=true %}

## Selected Publications {#publications}

{% include selected_papers.liquid %}

## Projects {#projects}

### 2024--2026 · BeeCurious

BeeCurious brings together my Minecraft-based AI literacy and embodied peer-agent research. It includes **BeeTrap-MC**, which teaches filter bubbles and recommendation systems through gameplay, and **Meet Bip**, an embodied bee agent designed to support learners through spatially grounded dialogue, bounded knowledge, and exploratory scaffolding.

### 2023--2025 · Computational Cinema & Narrative Intelligence

My work at the intersection of cinema, AI, and computational narrative analysis. It includes movie-scene search with large language models, computer vision, and information retrieval; narrative pattern mining over plot structures; and VLM-based analysis of cinematic style through lighting, color, framing, spatial organization, atmosphere, and genre-level visual patterns.

### 2023--2024 · Watching Others Sleep

A 22-minute short film screened at Tehran Short Film Week in May 2024.

<img class="portfolio-img poster" src="/assets/img/watching-others-sleep-poster.jpg" alt="Watching Others Sleep poster">

### 2020--2023 · Iran Computer Museum

Lead Designer and Content Curator. I designed the museum's main exhibit narrative, educational tours, interactive installations, and learning materials. The museum opened to the public in December 2023.

[Website](https://computermuseum.ir/)  
[Tree of AI](https://ai-tree.darkube.app/)  
[Calculus of Words](https://word2vec.darkube.app/?show_colors=true&show_relations=true)

<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/screenshot1.png" alt="AI Tree screenshot">
<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/screenshot2.png" alt="Calculus of Words screenshot">

### 2022--2023 · RoboLamb

A 2D RPG adventure game developed with Godot to introduce teenagers to computer science and programming concepts through gameplay.

<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/robolamb.png" alt="RoboLamb screenshot">

### 2022 · CoColor: Interactive Exploration of Color Designs

An interactive system for AI-assisted color design workflows. I contributed to literature review, interaction design, implementation, and user testing with professional UX designers.

<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/screenshot3.png" alt="CoColor screenshot">

### 2022 · Goldoone

A drag-and-drop 2D game developed with Godot to help elementary students improve literacy skills through gameplay.

[Download](https://drive.google.com/file/d/1gCJd__aOALFLNJTAFOp15BsaLpOo0Tal/view?usp=sharing)  
[Video](https://vimeo.com/787343192)

<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/goldoone.png" alt="Goldoone screenshot">

### 2022 · Intro-GD

An easy-to-use Godot add-on for creating tutorials and introduction sections inside Godot scenes.

[Godot Asset Library](https://godotengine.org/asset-library/asset/1403)  
[GitHub](https://github.com/farhadi-erfan/intro-gd)

<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/godot.png" alt="Intro-GD screenshot">

### 2021 · Fifteen

A simple multiplayer online game, developed with Django Channels and Godot, where players compete to collect three cards that add up to 15.

[Cafe Bazaar](https://cafebazaar.ir/app/ir.alefedu.fifteen)

<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/fif.jpg" alt="Fifteen screenshot">

### 2020--2022 · Kamva

My thesis project, later developed into a gamified platform for online workshops and semi-personalized educational content. Built with Django, Docker, and React.

[Website](https://kamva.academy)  
[GitHub](https://github.com/rastaiha)  
[Video](https://www.youtube.com/watch?v=5UeoLFCX45c)

<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/kamva.png" alt="Kamva screenshot">

### 2020 · Kabarama Dalapeste

An online gamified contest designed during the early days of Covid-19 to support connection and interaction during the transition to e-learning.

[GitHub](https://github.com/Rastaiha/KabaramadalaPeste)

<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/kabar%20(1).png" alt="Kabarama Dalapeste screenshot 1">
<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/kabar%20(2).png" alt="Kabarama Dalapeste screenshot 2">
<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/kabar%20(3).png" alt="Kabarama Dalapeste screenshot 3">

### 2020 · Clash of Civilizations

An unfinished realtime online strategy game where players balanced civilization-building, science, and conflict through cards, battles, and educational quizzes.

<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/cards.jpg" alt="Clash of Civilizations screenshot">

### 2016--2019 · Shined Brightly, Though...

A 75-minute documentary based on my memories from school years and Iran's educational system.

[Watch on Vimeo](https://vimeo.com/414334902)

<img class="portfolio-img" src="https://raw.githubusercontent.com/farhadi-erfan/farhadi-erfan-old/master/images/shined.png" alt="Shined Brightly Though screenshot">
