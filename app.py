import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, Field
from resume_dataset import resumes_dataset

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API KEY not found!")

client = Groq(api_key=my_api_key)
model = "qwen/qwen3.8-27b"

# Candidtes' resume as input
class CandidateAssessment(BaseModel):
    name: str = Field(description="The full name of candidate extracted from the Resume.")
    email: str = Field(description="The email of candidate extracted from the Resume.")
    socials: str = Field(description= "The linkedin profile of candidate extracted from the Resume. 'null' if not specified")
    gap: str = Field(description="If candidate have taken a gap year, value=0 if no gap year.")
    ats_score: int = Field(description="ATS score (0-100) of the candidate's Resume.")
    percentage: float = Field(description="Percentage of how relavent is the candidate for the listed job profile.")
    
# Top 2 candidates as out for interview
class HRInterviewList(BaseModel):
    job_title: str = Field(description="The job title they are getting assessed for.")
    interview_list: list[CandidateAssessment] = Field(description="Fill in exactly two candidates in this list with their 'name', 'email' as json object. Keys must be consistent as it is already defined ('name', 'email')")

schema = HRInterviewList.model_json_schema()

target_job_title = "Junior Python & AI automation Engineer"


system_instruction = {
    "role": "system",
    "content": f"""
    You are an expert HR Applicant Tracking System (ATS) evaluator. 
Your task is to review the provided list of candidate resumes, calculate a strict objective compatibility score out of 100 based on the target Job Title, rank them, and select exactly the top two (2) best-suited candidates.

Guidelines:
- Evaluate skills matching the target role parameters strictly.
- Completely ignore personal metadata noise or extraneous background stories.
- You MUST output your final selection strictly as a single valid json object conforming to this json schema format layout: {schema}
    """
}
prompt_content = f"""
Target job title: {target_job_title}
List of candidates to assess:
{chr(10).join([f"Resume #{i}, {resume}" for i, resume in enumerate(resumes_dataset)])}
"""
message = {
    "role": "user",
    "content":prompt_content
}
message = [system_instruction, message]

print(f"Parsing {len(resumes_dataset)} for HR interview...")
response = client.chat.completions.create(
    model = model,
    messages=message,
    temperature=0,
    max_tokens= 1000,
    response_format={"type": "json_object"}
)
hr_report = response.choices[0].message.content
print(hr_report)