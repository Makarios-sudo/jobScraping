from bs4 import BeautifulSoup
import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view

  
@api_view(["GET"])
def indeed(request):

    keywords = request.GET.get("keywords")
    location = request.GET.get("location")
    pageNum = request.GET.get("pageNum")

    param = {
        "keywords":keywords,
        "location":location,
        "pageNum":pageNum
    }
    
    URLs = ( 
        "https://www.linkedin.com/jobs/search/" 
    )

    response = requests.get(
        URLs, 
        params=param
    )
    
    soup = BeautifulSoup(
        response.content, 
        "html.parser"
    )
    
    jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    data_list = []

    while True:
        for job in jobs:
        
            job_title = job.find('h3', class_='base-search-card__title').text.strip()
            job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
            job_location = job.find('span', class_='job-search-card__location').text.strip()
            job_link = job.find('a', class_='base-card__full-link')['href']

            """  TODO  --> Getting when the jobs was posted """
            # job_posted = job.find('time', class_="job-search-card__listdate--new")['datetime'] 
            # time = datetime.strptime(job_posted, '%a, %d %b %Y %H:%M:%S %z')
            
            data = {
                "job_title": job_title,
                "job_company": job_company,
                "job_location": job_location,
                "job_link": job_link
            }

            data_list.append(data)
        return JsonResponse(data_list, safe=False)

