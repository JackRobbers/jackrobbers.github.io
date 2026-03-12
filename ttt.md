---
layout: default
---

Thick/Thicc Thigh Thursday is a weekly bike ride.

We always meet at 6pm at Redfern Park.

We've ridden {{ site.ttt | size }} times and swum at least {{  site.ttt | where:"swim","true" | size }} times.


{% assign imageCount = 0 %}

# Upcoming Rides (subject to change)

{%  assign today = 'now' | date: '%s' %}

# Ride Archive 
{{ today }}

<div class="flex-container" markdown=1>

{% for ride in site.ttt reversed %}
{% assign date_unix = ride.path | date: '%s'}

<div markdown=1 id="{{date}}">

{{ forloop.rindex }}
**{{ ride.route }}{% if ride.venue %} + {% endif %}{{ ride.venue }}** {% if ride.swim == true %}🏊{% endif %} 

{{ ride.path | date: '%d/%m/%Y' }}
{% assign date = ride.path | split: "/" | last | split: "."  | first %}
{% assign image_path = "/images/ttt/" | append: date %}
{{ png_path}}
{% assign images = site.static_files | where_exp: "file", "file.path contains image_path" | sort: "path" | reverse %}
{% if images.size > 0 %}

<div>
{% for i in images  %}
<img src="..{{i.path}}">
{% endfor %}
</div>

{% else %}
## ...
{% assign imageCount = imageCount | plus: 1 %}
{% endif %}

{{ ride.content}}

</div>

{% endfor %}

</div>

This archive is incomplete. {{ site.ttt | where:"route","???" | size }} rides are missing details and {{ imageCount }} rides are missing posters. If you remember where a ride went or have a poster please let me know!