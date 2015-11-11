# Simple plantms
Project for plant maintenance system

Introduction
I was taked with implementing a plant maintenance solution at my previous job. After much investigation I found that most of the option available are paid and over priced or free and sevrely lacking in functionality. So I have undertaken to create such a system myself. Please note this is my first project on Github so please be kind.

Description
The system I will be building will be able to create various technical departments for a plant environment as well as multiple physical locations. The users will then be able to add equipment to the system and define types of maintenance tasks which will be linked to the equipment. These tasks will be given an interval. The maintenance tasks will then be executed by the techincal teams and recorded on the system. I will look to get core functionality up and running quickly and then work on future functionality such as providing a method to import old paperbased maintenance records and integration into ticket system like osTicket.

Detail
The system version 1.0 will have the following functionality
	1. User/Group permission based viewing of app.
	2. Ability to create sites at which equipment will live and be maintained.
	3. Ability to create technical departments, which can belong to just one or span many sites.
	4. Ability to create equipment, which will live at a site and belong to a department.
	5. Create multiple maintenance jobs for a piece of equipment
	6. Schedule the maintenance tasks according to the jobs.
	7. Print out works order for technical teams to complete.
	8. Record the maintenance tasks.
	9. Run reports on the various equipment.

Technologies
I will be developing the system in Django, using a MySQL database backend.

Notes
While the project is still in development I will be using the default Django implementation of SQLite for the database backend and will move over to MySQL closer to version 1.0 release.

PIP Packages used
- django 1.8
- django-extensions
- django-audit-log
- django-crispy-forms
