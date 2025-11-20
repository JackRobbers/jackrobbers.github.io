---
layout: default
---

<!-- TODO / IDEAS

photos

auto milestones. years, number of rides, daylight savings

stats


 -->

Thick/Thicc Thigh Thursday is a weekly bike ride.

We always meet at 6pm at Redfern Park.

We've ridden {{ site.ttt | size }} times and swum at least {{  site.ttt | where:"swim","true" | size  }} times.

# Ride Archive 

<div class="flex-container" markdown=1>


{% for ride in site.ttt reversed %}

<div markdown=1>


{{ forloop.rindex }} **{{ ride.route }}{% if ride.venue %} + {% endif %}{{ ride.venue }}** {% if ride.swim == true %}🏊{% endif %} 

{{ ride.path | date: '%d/%m/%Y' }}

{% assign date = ride.path | split: "/" | last | split: "."  | first %}
{% assign jpg_path = "/images/ttt/" | append: date | append: ".jpg" %}
{% assign jpg = site.static_files | where: "path", jpg_path | first %}
{% assign png_path = "/images/ttt/" | append: date | append: ".png" %}
{% assign png = site.static_files | where: "path", png_path | first %}
{% if jpg %}
![](..{{jpg_path}})
{% elsif png %}
![](..{{png_path}})
{% else %}
## ...
{% endif %}

{{ ride.content}}

</div>

{% endfor %}

</div>