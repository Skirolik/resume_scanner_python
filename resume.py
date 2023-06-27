

import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resume= docx2txt.process("Naukri_NateshKumarS[2y_2m].docx")
job_description = docx2txt.process("Manav Hardware Engineer JD (1).docx")
# print(job_description)

## making a varible for both text
text=[resume,job_description]

##count of words
cv=CountVectorizer()
count_matrix= cv.fit_transform(text)

##to see the similatiry

# print("\n Similarity Score")
# print(cosine_similarity(count_matrix))

## the match percentage
matchpercentage= cosine_similarity(count_matrix)[0][1]*100
matchpercentage= round(matchpercentage,2)
print("Resume Match about:"+ str(matchpercentage)+"% of the job description")