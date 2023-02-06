### A Flask Api *TODO List*

#### Objective
>maintain a list of tasks

#### Technologies
>Flask

#### About
There are 5 api end points.
- add a task in the list using the url ``http://127.0.0.1:5000/add?task=&date=&month=&year=`` 
- update the status of the task using the url ``http://127.0.0.1:5000/update/status?id=``
- update the due date of the task using the url ``http://127.0.0.1:5000/update/date?id=&date=&month=&year=``
- remove a task from the list using the url ``http://127.0.0.1:5000/remove?id=``
- see the list of task using the url ``http://127.0.0.1:5000/todo``

##### *Note - while running the application, enter the values after ``=`` in the above mentioned urls in the respetive fields

#### Installation and Setup
- clone the repository 
- run the ``app.py`` file in any python IDE 
- use the above urls in Chrome or Thunder Client in vscode
