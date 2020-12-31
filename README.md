# NSW Covid Case Locations Datasette

This service visualises the [NSW Ministry of Health - NSW COVID-19 case locations (CC)](https://data.nsw.gov.au/data/dataset/nsw-covid-19-case-locations) data using [Datasette](https://datasette.io/)

Uses a [fork of datasette-cluster-map](https://github.com/glasnt/datasette-cluster-map) for the rich HTML popups. 

# Deploy

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

# Methodology

Any time the service starts, a new set of data is downloaded from the source URL. The source data is slightly appended (for rich popup information), then served with datasette. 

The data is then able to be analysed ad-hoc. 

# Warranty

This service does not take into account data integreity or other issues with the changing of the format of the incoming data. It may break at any time. Always refer to the source. 
