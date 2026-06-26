# LEAD INTAKE AUTOMATION

## CREATE YOUR DATABASE FIRST

download postgres(stable version)

create database (in the query tool run `CREATE DATABASE lead_intake_automation;`)
create table in the database created (`CREATE TABLE leads( id, name, email, message, status and time  );`)

## RUN WEBHOOK SCRIPT AND TEST SCRIPT
start venv and activate it (
    `python -m venv venv`,
    `venv/Scripts/activate`(on windows)
)

install requirements(`pip install -r requirement.txt`)

in one terminal run `python app.py`

in another terminal run `python testwebhook.py`


