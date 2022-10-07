from bs4 import BeautifulSoup
import requests

print("put some skill that are not familiar with")
unfamiliar_skill = input("> ")
print(f"Filtering out {unfamiliar_skill}")


def find_jobs():
    r = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")

    content = r.content

    soup = BeautifulSoup(content, 'html.parser')

    jobs = soup.find_all(name="li", class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):

        publish_date = job.select_one(selector=".sim-posted span").get_text().strip()

        if "few" in publish_date:

            company_name = job.find(name="h3", class_="joblist-comp-name").get_text().strip()
            skill = job.select_one(".srp-skills").get_text().replace(" ", "")
            more_info = job.select_one(selector=".list-job-dtl li a").get("href")

            # print(company_name)
            # print(skill)
            # print(more_info)

            if unfamiliar_skill not in skill:

                with open(f"jobs/{index}.txt", mode="w") as file:
                    file.write(f"Company Name : {company_name}\n")
                    file.write(f"Skills : {skill.strip()}\n")
                    file.write(f"Link : {more_info}\n")
                    print(f"File Saved : {index}")


if __name__ == "__main__":
    find_jobs()

    # while True:
    #     find_jobs()
    #     wait_time = 10
    #     print(f"waiting for {wait_time} seconds...")
    #     time.sleep(wait_time)
