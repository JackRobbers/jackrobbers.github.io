---
layout: default
---

Thick/Thicc Thigh Thursday is a weekly bike ride.

We always meet at 6pm at Redfern Park

# Ride Archive

{% for ride in site.ttt %}
{{ ride.date }} {{ ride.name }}

{{ ride.collection }}

{% endfor %}