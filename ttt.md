---
layout: default
---
<!-- compute some stats -->
{% assign today = 'now' | date: '%s' %}
{% assign missingImageCount = 0 %}
{% assign rides = 0 %}
{% for ride in site.ttt %}
{% assign date_unix = ride.path | date: '%s' %}
{% if date_unix < today %}
{% assign rides = rides | plus: 1 %}
{% endif %}
{% assign date = ride.path | split: "/" | last | split: "."  | first %}
{% assign image_path = "/images/ttt/" | append: date %}
{% assign images = site.static_files | where_exp: "file", "file.path contains image_path" | sort: "path" | reverse %}
{% if images.size == 0 %}
{% assign missingImageCount = missingImageCount | plus: 1 %}
{% endif %}
{% endfor %}

Thick/Thicc Thigh Thursday is a weekly bike ride.

We always meet at 6pm at Redfern Park.

We've ridden {{ rides }} times and swum at least {{  site.ttt | where:"swim","true" | size }} times.



# Upcoming Rides
<div class="flex-container" markdown=1>

{% for ride in site.ttt %}
{% assign date_unix = ride.path | date: '%s' %}
{% if date_unix > today %}

<div markdown=1 id="{{date}}">

{{ ride.path | date: '%U' | plus: 114}}
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

{% endif %}
{% endfor %}

</div>

# Ride Archive 
This archive is incomplete. {{ site.ttt | where:"route","???" | size }} rides are missing details and {{ missingImageCount }} rides are missing posters. If you remember where a ride went or have a poster please let me know!

<div class="flex-container" markdown=1>

{% for ride in site.ttt reversed %}
{% assign date_unix = ride.path | date: '%s' %}
{% assign a = date_unix | minus: today %}
{% if date_unix < today %}

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

{% endif %}
{% endfor %}

</div>