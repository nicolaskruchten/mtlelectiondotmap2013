#Montreal Election Dotmap 2013

*(Inspired by the [Census Dotmap](http://bmander.com/dotmap/index.html))*

This script creates a large graphic ([1000 DPI original](http://nicolaskruchten.github.io/mtlelectiondotmap2013/mtlelectiondotmap2013.png), [Zoom.it zoomable](http://zoom.it/rVnM)) showing one coloured dot per vote cast for the top three candidates in the election for the mayoralty of Montreal in 2013: 

![image](http://nicolaskruchten.github.io/mtlelectiondotmap2013/mtlelectiondotmap2013-small.png)

Each dot is randomly positioned within the catchment area for the polling station it was recorded in.

This map was generated using two datasets (exact links in the code) from the [City of Montreal Open Data portal](http://donnees.ville.montreal.qc.ca/group/election-referendum) and so the following notice is required: *Contient des données reproduites, modifiées, traduites ou distribuées « telles quelles » avec la permission de la Ville de Montréal.*

Depends on `matplotlib` and `shapely`.
