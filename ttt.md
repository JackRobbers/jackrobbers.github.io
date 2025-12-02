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

<div markdown=1 id="{{date}}">


{{ forloop.rindex }} **{{ ride.route }}{% if ride.venue %} + {% endif %}{{ ride.venue }}** {% if ride.swim == true %}🏊{% endif %} 

{{ ride.path | date: '%d/%m/%Y' }}

{% assign date = ride.path | split: "/" | last | split: "."  | first %}
{% assign image_path = "/images/ttt/" | append: date %}
{{ png_path}}
{% assign images = site.static_files | where_exp: "file", "file.path contains image_path" | sort: "path" | reverse %}
{% if images %}

<div markdown=1 class="horizontal-images" >

{% for i in images  %}
![](..{{i.path}})
{% endfor %}

</div>

{% else %}
## ...
{% endif %}

{{ ride.content}}

</div>

{% endfor %}

</div>