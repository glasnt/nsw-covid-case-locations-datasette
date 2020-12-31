# NSW Covid Case Locations - Datasette Visualisation

This service visualises the [NSW Ministry of Health - NSW COVID-19 case locations (CC)](https://data.nsw.gov.au/data/dataset/nsw-covid-19-case-locations) data using [Datasette](https://datasette.io/)

Uses the `combo-branch` branch of a [fork of datasette-cluster-map](https://github.com/glasnt/datasette-cluster-map) for:

  - rich HTML popups (isolated: html-popup branch)
  - map hash implementation (from [pending feature](https://github.com/simonw/datasette-cluster-map/tree/map-hash/datasette_cluster_map) in datasette) (allows for saving the current zoom/location on the map)

# Deploy

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

# Methodology

Any time the service starts, a new set of data is downloaded from the source URL. The source data is slightly appended (for rich popup information), then served with datasette. 

The data is then able to be analysed ad-hoc. 

# Warranty

This service does not take into account data integreity or other issues with the changing of the format of the incoming data. It may break at any time. Always refer to the source. 
