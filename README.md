# Notable Health Take Home Project

## Technologies used
- Serverless Framework
- API Gateway
- AWS Lambda
- MongoDB Atlas
- Written in Python

## Instructions
The following are links to each of the endpoints, although the only endpoint that is currently functional is the "Get a list of all doctors" endpoint.
The portions of the paths that are in curly braces are parameters that would change depending on which physician you are looking for, and on what date.
- Get a list of all doctors
  - GET - https://gu0x2vwy93.execute-api.us-east-1.amazonaws.com/dev/physicians
- Get a list of all appointments for a particular doctor and particular day
  - GET - https://gu0x2vwy93.execute-api.us-east-1.amazonaws.com/dev/physicians/{physicianId}/appointments/{date}
- Delete an existing appointment from a doctor's calendar
  - DELETE - https://gu0x2vwy93.execute-api.us-east-1.amazonaws.com/dev/physicians/{physicianId}/appointments/delete
- Add a new appointment to a doctor's calendar
  - POST - https://gu0x2vwy93.execute-api.us-east-1.amazonaws.com/dev/physicians/{physicianId}/appointments/new
  
## A huge thank you to Notable Health for this opporunity!
