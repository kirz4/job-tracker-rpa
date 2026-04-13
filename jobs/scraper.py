from seleniumbase import SB


def scrape_jobs():
    jobs_data = []

    url = "https://realpython.github.io/fake-jobs/"

    with SB(uc=True, headless=True) as sb:
        sb.open(url)
        sb.wait_for_element("div.card-content", timeout=15)

        cards = sb.find_elements("div.card-content")

        for card in cards:
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
                parent = card.find_element("xpath", "./ancestor::div[contains(@class, 'column')]")
                link_element = parent.find_element("css selector", "a.card-footer-item")
                job_url = link_element.get_attribute("href")
            except Exception:
                job_url = ""

            if title and job_url:
                jobs_data.append(
                    {
                        "title": title,
                        "company": company,
                        "location": location,
                        "url": job_url,
                    }
                )

    return jobs_data