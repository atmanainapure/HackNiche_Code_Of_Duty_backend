
from pyresparser import ResumeParser

def resume_parser(link):
    #Read the resume file
    file_name = link
    resume_data = ResumeParser(file_name).get_extracted_data()
    print(resume_data.values)
    #Evaluate the resume
    total_score = 0

    #Check for education
    if 'education' in resume_data.keys():
        total_score += 10

    #Check for experience
    if 'experience' in resume_data.keys():
        total_score += 20

    #Check for skills
    if 'skills' in resume_data.keys():
        total_score += 30

    #Check for certifications
    if 'certifications' in resume_data.keys():
        total_score += 40

    #Check for awards
    if 'awards' in resume_data.keys():
        total_score += 50

    if 'no_of_pages' in resume_data.keys():
        total_score += 30

    #Calculate the resume score
    resume_score = total_score

    return resume_score