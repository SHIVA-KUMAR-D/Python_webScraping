import requests
import json

def fetch_url(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url


    try:

        response=requests.get(url)

        report ={
            "Original URL": url,
            "Final URL": response.url,
            "Status Code": response.status_code,
            "Reason": response.reason,
            "Response Time": response.elapsed.total_seconds(),
            "Response Size": convert_size(len(response.content)),
            "Headers": dict(response.headers),
            "Redirects": redirects(response.history),
        }
        return report
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def redirects(history):
    if not history:
        return "No redirects"
    else:
        redirect_list = []
        for resp in history:
            redirect_list.append({
                "URL": resp.url,
                "Status Code": resp.status_code,
                "Reason": resp.reason
            })
        return redirect_list

def convert_size(content_length):
    if content_length < 1024:
        return f"{content_length} Bytes"
    elif content_length < 1024 ** 2:
        return f"{content_length / 1024:.2f} KB"    
    else:
        return f"{content_length / (1024 ** 2):.2f} MB"

def display_report(report):
    print("=" * 60)
    print("HTTP EXPLORER")
    print("=" * 60)

    for key, value in report.items():

        if key == "Headers":
            print("\nHeaders")
            print("-" * 60)

            for h, v in value.items():
                print(f"{h:<20}: {v}")

        else:
            print(f"{key:<20}: {value}")


def save_report(report):
    with open("report.json","w") as f:
        json.dump(report,f,indent=4)

def main():
    url =input("Enter the URL :")
    report = fetch_url(url)

    if report:
        display_report(report)
        save_report(report)
        print("\nReport saved successfully.")






if __name__ == "__main__":
    main()