from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from lib.models.employee import session, Employee

app = FastAPI()


class EmployeeSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    age: int
    gender: str
    phone_number: str
    salary: int
    designation: str


@app.get("/employees")
def get_employees():
    employees = session.query(Employee).all()
    return employees


@app.get("/employee/{id}")
def get_employee(id: int):
    employee = session.query(Employee).filter(Employee.id == id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee does not exist in our databse")
    return employee


@app.get("/employees/salary/asc")
def get_employees_by_salary():
    employees = session.query(Employee).order_by(Employee.salary.asc()).all()
    return employees


@app.get("/employees/age/old")
def get_oldest_employee():
    employee = session.query(Employee).order_by(Employee.age.desc()).first()
    return employee
