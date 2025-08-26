from fastapi import FastAPI, UploadFile, File
from pdfparser import parse_pdf
from webscrapper import display_skills_summary
from database import DBConnection
from difference import Differences
import os

#db1 = DBConnection()
app = FastAPI()
os.makedirs('uploads', exist_ok=True)

@app.post("/api/parse-document")
async def get_skills(job_description: str, file: UploadFile = File(...)):
    #job_description = 'Kubernetes'
    # Save the uploaded file
    file_location = f"uploads/{file.filename}"
    print(file_location)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    try:
        # Send the file to affinda for parsing (pdfparser)
        result = parse_pdf(file_location)
    except Exception as e:
        print(e)
        return {"error": "Sorry, we could not parse your file"}

    # Save the results into the database
    #db1.insert_a_user(result)

    # Make a call to the difference.py method
    dif = Differences()
    skill_dict = dif.get_difference_in_skills(result, job_description)

    missing_skills = skill_dict['missing_skills']
    percentage_known = skill_dict['percentage_known']

    # Get summaries for missing skills
    skills_summary_dict = display_skills_summary(missing_skills)

    return {
        "skills_summary": skills_summary_dict,
        "percentage_known": percentage_known
    }