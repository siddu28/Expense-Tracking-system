from fastapi import FastAPI,HTTPException
from datetime import date 
import db_helper
from typing import List
from pydantic import BaseModel

class Expense(BaseModel):
    amount:float
    category:str
    notes:str

    
class Date_range(BaseModel):
    start_date:date
    end_date:date


app=FastAPI()


@app.get("/expences/{expence_date}",response_model=List[Expense])
def get_expences(expence_date: date):
    expences=db_helper.fetch_expenses_for_date(expence_date)
    if expences is None:
        raise HTTPException(status_code=500,detail="Failed to retrieve expense summary from the database")

    return expences

@app.post("/expences/{expence_date}")
def add_or_update_expense(expence_date:date,expenses:List[Expense]):
    db_helper.delete_expenses_for_date(expence_date)
    for expense in expenses:
        db_helper.insert_expense(expence_date,expense.amount,expense.category,expense.notes)

    return {"Message":"Expences updated sucessfully"}


@app.post("/analytics")
def get_analytics(date_range:Date_range):
    data=db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)

    if data is None:
        raise HTTPException(status_code=500,detail="Failed to retrieve expense summary from the database")
    
    total=sum([row['total'] for row in data])

    breakdown={}
    for row in data:
        percentage=(row['total']/total)*100 if total!=0 else 0
        breakdown[row['category']]={
            'total':row['total'],
            'percentage':percentage
        }

    return breakdown

@app.get("/monthly_summary")
def get_analytics_monthly():
    monthly_summary=db_helper.fetch_expense_summary_by_month()
    if monthly_summary is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve monthly expense summary from the database.")

    return monthly_summary

















