import requests
import csv
import json
url = "https://www.naukri.com/jobapi/v3/search"


def getAndSaveJobData(department,searchKeyList):
    print(f"Executing search scraping for {department}")
    print("--------------------------------------------")
    for searchKey in searchKeyList:
        print("-------------------------------")
        print(f"Search keyword {searchKey}")
        print("-------------------------------")
        j=16
        for i in range(1,j):
            n = str(i)
            params = {
                "noOfResults": "20",
                "urlType": "search_by_keyword",
                "searchType": "adv",
                "keyword": searchKey,
                "pageNo": n,
                "cityTypeGid": "183",
                "k": searchKey,
                "cityTypeGid": "183",
                "seoKey": "web-developer-jobs",
                "src": "directSearch",
                "latLong": ""
            }

            headers = {
                "Host": "www.naukri.com",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
                "Accept": "application/json",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Referer": "https://www.naukri.com/web-developer-jobs?k=web+developer&cityTypeGid=183",
                "clientid": "d3skt0p",
                "appid": "109",
                "systemid": "Naukri",
                "Content-Type": "application/json",
                "gid": "LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE",
                "Connection": "keep-alive",
                "Cookie": ("test=naukri.com; _t_ds=242589551720077706-5524258955-024258955; _t_us=66864D89; _t_s=seo; _t_sd=google; _t_r=1030%2F%2F; "
                        "persona=default; J=0; ak_bmsc=45F498BC794595C4D45298E4F0EB1FEC~000000000000000000000000000000~YAAQhM8uF+DMy3OQAQAAY86ffBjQMv2pfdslO0FWHJe4VlSU1Ta8GSYeuqPdENjY6T3YpVlnTP0WWbUOYrw6QqNAKydYgR9gNRktP3I1SAHrvYaUepuqSGMw3vVHU9Mb0wI+uea0Vrbwor6I3pFLHT0q97w1IUimhs+ALKbGme+cl23vpofsjl4xB4tWoqoQfPXraoaHuOm1StT9WyxRkLTyFl9qtUpEp0l7lJM2usiwQKpk+uylfCo0jn2UiYVjgqRdAO1KP839cleef+3ZblJamOyq1zpeXJyLSu1CxGwJZLza9ggcpevtGVrdXC6Py72irgEMoVmikpfXR1Dp1D/ox47/Cd8HZIYtHoZdjkyMDSADDuQpPWiiUAkmvOruuTe2/vm41T/Cf/G9fORBQSkQd8IuNWHQ/FFczchUFIkbPD6tBeoVvlnAFBv2hPkSmbeN; bm_sv=9FB0FAF067763ECD82E2963134A666ED~YAAQhM8uF+7Jy3OQAQAA57affBiF1uRGGHxdIxgVS5Oko4srMtx0u4fQVUe6Ee/uZZqlISTkLTcOieo18MGmGFiBZXXo/2aEVrkiYr9+DZbkpGwo4/he3JCOC+6swownl08ZQXjWCigFo0ehdS+Szxp26PBIW/gXxvJokAeKvQxDmGClZrc1OwbKFwNCs/y56yklhZu/+AudD1leAu29Ibp+XiGddN3HdYsZGDKZkwdzasMQrt+nMYax3oi31RRM3Q==~1; bm_mi=2321BEA968F04A19F34B92C49C455E62~YAAQhM8uF9PEy3OQAQAA5oeffBgHv98gQRhimeSjYURBnL4MSSUjSzQoWVgW1jFRfpdJ2NiXqp8C9mn0qJEpulkDUiHT4UwbKVk+kKaflmLEqA6H6sdeTy1fVZj0Wf7iza9SmTnnbOBteyBxPSSWdWRb34cSFZ1Rzzj/4VacHV2Hgwq6QDDQEp3bZMHL94rM28tnQ9WRDDVZ+Y2zmKFOjQNxLkZvcR3QFTuAr1K0egDewrR/LHeIZEyQsEovlILef39hf24uDfIWwFsJQeWwPosz4GpsXMlsPfQKKLPwsDXLjThGXDjwlPMVZ0LomrhoghY6fsMS5omlXR1y+7Zm~1; "
                        "HOWTORT=ul=1720078063709&r=https%3A%2F%2Fwww.naukri.com%2Fweb-developer-jobs%3Fk%3Dweb%2Bdeveloper%26cityTypeGid%3D183&hd=1720078064775"),
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Priority": "u=4",
                "TE": "trailers"
            }

            
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                print(response.status_code)
                print("successfully fetched job data")
                data = response.json()
                
                noOfJobs = data.get("noOfJobs")
                j = (noOfJobs % 20) + 1

                job_details = data.get("jobDetails", [])
                
                # Define the CSV file name
                csv_file = "scraped_jobs/"+department + ".csv"
                
                # Define the CSV headers
                csv_headers = ["title", "jobId", "currency", "footerPlaceholderLabel", "footerPlaceholderColor", "companyName", "isSaved", "tagsAndSkills", "experience", "salary", "location", "companyId", "jdURL", "staticUrl", "jobDescription", "showMultipleApply", "groupId", "isTopGroup", "createdDate", "mode", "board"]

                # Write data to CSV
                with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=csv_headers)
                    if i==1:
                        writer.writeheader()
                    
                    for job in job_details:
                        # Extract placeholders
                        placeholders = job.get("placeholders", [])
                        experience = next((item["label"] for item in placeholders if item["type"] == "experience"), None)
                        salary = next((item["label"] for item in placeholders if item["type"] == "salary"), None)
                        location = next((item["label"] for item in placeholders if item["type"] == "location"), None)
                        
                        # Write job details to CSV
                        writer.writerow({
                            "title": job.get("title"),
                            "jobId": job.get("jobId"),
                            "currency": job.get("currency"),
                            "footerPlaceholderLabel": job.get("footerPlaceholderLabel"),
                            "footerPlaceholderColor": job.get("footerPlaceholderColor"),
                            "companyName": job.get("companyName"),
                            "isSaved": job.get("isSaved"),
                            "tagsAndSkills": job.get("tagsAndSkills"),
                            "experience": experience,
                            "salary": salary,
                            "location": location,
                            "companyId": job.get("companyId"),
                            "jdURL": job.get("jdURL"),
                            "staticUrl": job.get("staticUrl"),
                            "jobDescription": job.get("jobDescription"),
                            "showMultipleApply": job.get("showMultipleApply"),
                            "groupId": job.get("groupId"),
                            "isTopGroup": job.get("isTopGroup"),
                            "createdDate": job.get("createdDate"),
                            "mode": job.get("mode"),
                            "board": job.get("board")
                        })
                print(f"Job details have been saved to {csv_file}")
            else:
                print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")

        