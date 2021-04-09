# Final Project
# Squirrel Tracker: an web-application based on Django

## introduction

An web-application that can import the 2018 Central Park Squirrel Census data and allows people to add, update, and view squirrel data, with the purpose of keeping track of all the known squirrels in Central Park. 

## DataSet
Source: [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) dataset published by [**Squirrel Census**](https://www.thesquirrelcensus.com/).  
Overall: Containing 3,023 sightings, including Location Coordinates, Squirrel Unique ID, Shift and so on. 

## Management commands:
Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 
```sh
$ python manage.py import_squirrel_data /path/to/file.csv
```

Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command. 
```sh
$ python manage.py export_squirrel_data /path/to/file.csv
```

## Views
### Map   
[Map](https://??????/map/): A view that shows a map that displays the location of the squirrel sightings on an [OpenStreets map](https://www.openstreetmap.org/about/).   
>Located at: /map   
Method Supported: GET   
Use the [leaflet](https://leafletjs.com/) library for plotting

### Squirrel List
[Squirrel List](https://??????/sightings/): A view that lists all squirrel sightings with links to view each sighting.
>Located at: /sightings   
Method Supported: GET   

### Squirrel Update
[Squirrel Update](https://??????/sightings/): A view to update a particular sighting.
>Located at: /sightings/<unique-squirrel-id>   
Method Supported: GET & POST

### Squirrel Add
[Squirrel Add](https://??????/sightings/add): A view to create a new sighting.
>Located at: /sightings/add   
Method Supported: GET & POST

### Squirrel Stats
[Squirrel Add](https://??????/sightings/stats): A view with general stats about the sightings.
>Located at: /sightings/stats   
Method Supported: GET


## Dependencies

## Background
Eccentric billionaire Joffrey Hosencratz just purchased the web development company you work for. You’ve met him once in an elevator and he was impressed with your skill in developing web applications with the Django framework. He also relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. See, he fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona has left him wanting. 

He would like to start keeping track of all the known squirrels and plans to start with Central Park. He’s asked you to build an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and view squirrel data. 

## Contributors

Group Name: Project Group 11

Section: 2

Contributors: Jiaxin Wu, Weishan Lu

UNIs: [**[jw3991]**](https://github.com/jw3991), [**[ws??]**](https://github.com/????)

Click [**Link**](https://github.com/jw3991/final_project_1/) for more information on our Squirrel Tracker Web-Application.
