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

{% for ride in site.ttt reversed %}

{{ forloop.rindex }} **{{ ride.route }}{% if ride.venue %} + {% endif %}{{ ride.venue }}** {% if ride.swim == true %}🏊{% endif %} 

{{ ride.path | date: '%d/%m/%Y'}}

{{ ride.content }}

---
{% endfor %}