from seleniumbase import SB


def scrape_jobs():
    jobs_data = []
    url = "https://realpython.github.io/fake-jobs/"

    with SB(headless=True) as sb:
        sb.open(url)
        sb.wait_for_element("div.column.is-half", timeout=15)

        job_cards = sb.find_elements("div.column.is-half")

        for card in job_cards:
            try:
                title = card.find_element("css selector", "h2.title").text.strip()
            except Exception:
                title = ""

            try:
                company = card.find_element("css selector", "h3.subtitle").text.strip()
            except Exception:
                company = ""

            try:
                location = card.find_element("css selector", "p.location").text.strip()
            except Exception:
                location = ""

            try:
                link_element = card.find_element("css selector", "a.card-footer-item")
                job_url = link_element.get_attribute("href")
            except Exception:
                job_url = ""

            if title and job_url:
                jobs_data.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "url": job_url,
                })

    return jobs_data