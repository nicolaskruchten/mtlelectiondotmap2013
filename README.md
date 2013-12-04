#Montreal Election Dotmap 2009

*(Inspired by the [Census Dotmap](http://bmander.com/dotmap/index.html))*

This script creates a large graphic ([original](http://nicolaskruchten.github.io/mtlelectiondotmap2009/mtlelectiondotmap2009.png), [zoomable](http://zoom.it/Ghss)) showing one coloured dot per vote cast for the top three candidates in the election for the mayoralty of Montreal in 2009: 

* red for Tremblay
* blue for Harel
* green for Bergeron

Each dot is randomly positioned within the catchment area for the polling station it was recorded in.

This map was generated using two datasets (exact links in the code) from the [City of Montreal Open Data portal](http://donnees.ville.montreal.qc.ca/group/election-referendum) and so the following notice is required: *Contient des données reproduites, modifiées, traduites ou distribuées « telles quelles » avec la permission de la Ville de Montréal.*

Depends on `matplotlib` and `shapely`.
