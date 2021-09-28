# cse416

## TODO for Initial Build

### GUI
* "Buttons don't look like buttons" - get rid of full-div-width buttons
* Change default font - set in .css file
* Change values of "Compactness" dropdown - should reflect values in UML enum
* Sidebar should be always visible, but certain controls should be hidden until a state is selected (Use Case 17)
* Dropdown menu for selection of state (initially visible) should allow state selection (needs to be added), as well as clicking on a state (already exists)
* Add a function that will request a "global history" of all plans on initial page load (called in a document.onready/onload?). This function should also be fired periodically based on a timer (every 5 minutes or so?) to check for new entries
* Get rid of "Fetch" button - functionality changed to server side polling
* Change Abort button to only be shown for a job which is selected from the "global history" which is in a PENDING/RUNNING state (replaces DELETE button in these cases)
* Remove hardcoded values (except for state boundaries) - Client should begin dynamically requesting content from server
* XMLHttpRequest calls/responses in appropriate locations so that they can be tied to the server quickly
  (url endpoint should be the same name as the method call in the UML, eg. call for creating a job should be for url /createJob)
  
XMLHttpRequest example:
```
  var params = {
    "range":"Sheet1!A4:C4",
    "majorDimension": "ROWS",
    "values": [
      ["Hello World","123", "456"]
    ],
  }
  
  var xhr = new XMLHttpRequest();
  xhr.open(method, url);
  xhr.setRequestHeader('Authorization', 'Bearer ' + access_token);
  xhr.onload = requestComplete; // function called on success
  xhr.onerror =  requestFailed; // function called on failure
  xhr.send(JSON.stringify(params));
  ```
  
### Server
* Set up initial endpoint functionality (endpoints should be reachable by the name of the method call, eg. call for creating a job should be mapped to /createJob)
* Don't really have to worry about DB stuff yet (no data stored or to be stored in the DB so far), but connection capability should be implemented

### Preprocessing
* "Smooth" geometry to limit # of vertices using QGIS
* Limit decimal precision for geoJSON
* Identify neighbors of each precinct
* Produce a JSON which combines precinct geometry data with precinct metadata (name, id, populations, neighbors)
* geoJSON files for state's currently enacted districting plans
