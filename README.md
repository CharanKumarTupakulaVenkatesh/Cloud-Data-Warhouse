# Cloud-Data-Warhouse

## Project Overview
Divvy is a bike sharing program in Chicago, Illinois USA that allows riders to purchase a pass at a kiosk or use a mobile application to unlock a bike at stations around the city and use the bike for a specified amount of time. The bikes can be returned to the same station or to another station. The City of Chicago makes the anonymized bike trip data publicly available for projects like this where we can analyze the data.

Since the data from Divvy are anonymous, we have created fake rider and account profiles along with fake payment data to go along with the data from Divvy. The dataset looks like this:

 ![](Bike_ERD.png?raw=True)

The goal of this project is to develop a data warehouse solution using Azure Synapse Analytics. We will:

**Design a star schema based on the business outcomes listed below;**
>
>**.Import the data into Synapse;**
>
>**.Transform the data into the star schema;**
>
>**.and finally, view the reports from Analytics.**
>
> ### The business outcomes you are designing for are as follows:**
>
 ### 1.Analyze how much time is spent per ride
   >
   >**.Based on date and time factors such as day of week and time of day**
   >
   >**.Based on which station is the starting and / or ending station**
   >
   >**.Based on age of the rider at time of the ride**
   >
   >**.Based on whether the rider is a member or a casual rider**
   >
### 2.Analyze how much money is spent
>
  >**.Per month, quarter, year**
  >
  >**.Per member, based on the age of the rider at account start**
  >
### 3.EXTRA CREDIT - Analyze how much money is spent per member
  >
  >**.Based on how many rides the rider averages per month**
  >
  >**.Based on how many minutes the rider spends on a bike per month**
  >
On the next page are instructions for logging in to an Azure account where we can configure the resources, Azure Synapse Workspace, and data storage to complete the project.

## Project Environment
In order to complete this project, you'll need to use these tools:

>**1.Access to Microsoft Azure. Instructions for accessing an Azure account where we can create the resources necessary for the project.**
>
>**2.Python to run the script to load data into a PostgreSQL database on Azure to simulate your OLTP data source**
>
>**3.An editor to work with the Python and SQL scripts, we recommend Visual Studio Code**

## Project Instructions
## Task 1: Create your Azure resources
>
.Create an Azure **PostgreSQL** database
>
.Create an Azure Synapse workspace
>
.Create a Dedicated SQL Pool and database within the Synapse workspace

## Task 2: Design a star schema
We are being provided a relational schema that describes the data as it exists in **PostgreSQL**. 
In addition, We have been given a set of business requirements related to the data warehouse. 
We are being asked to design a star schema using fact and dimension tables.

## Task 3: Create the data in **PostgreSQL**
To prepare your environment for this project, We first must create the data in **PostgreSQL**. 
This will simulate the production environment where the data is being used in the OLTP system. 
This can be done using the Python script provided for us in Github: ProjectDataToPostgres.py

Download the script file and place it in a folder where We can run a Python script
Download the data files from the classroom resources
Open the script file in VS Code and add the host, username, and password information for your **PostgreSQL** database
Run the script and verify that all four data files are copied/uploaded into **PostgreSQL**
We can verify this data exists by using pgAdmin or a similar **PostgreSQL** data tool.

## Task 4: EXTRACT the data from **PostgreSQL**
In your Azure Synapse workspace, We will use the ingest wizard to create a one-time pipeline that ingests the data from **PostgreSQL** into Azure Blob Storage. This will result in all four tables being represented as text files in Blob Storage, ready for loading into the data warehouse.

## Task 5: LOAD the data into external tables in the data warehouse
Once in Blob storage, the files will be shown in the data lake node in the Synapse Workspace. From here, We can use the script generating function to load the data from blob storage into external staging tables in the data warehouse We created using the Dedicated SQL Pool.

## Task 6: TRANSFORM the data to the star schema
We will write SQL scripts to transform the data from the staging tables to the final star schema We designed.

## Helpful Hints
When We use the ingest wizard, it uses the copy tool to EXTRACT into Blob storage. During this process, Azure Synapse automatically creates links for the data lake. When We start the SQL script wizard to LOAD data into external tables, start the wizard from the data lake node, not the blob storage node.
When using the external table wizard, We may need to modify the script to put dates into a varchar field in staging rather than using the datetime data type. We can convert them during the transform step.
When using the external table wizard, if We rename the columns in your script, it will help We when writing transform scripts. By default, they are named [C1], [C2], etc. which are not useful column names in staging.


