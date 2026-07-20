import requests

# print(requests.__version__)

url=input("Enter the URL:")
print("=" * 50)
print("HTTP EXPLORER")
print("=" * 50)

response = requests.get(url)
print(f"final URL     :{response.url}")
print(f"status code   :{response.status_code}")
print(f"Reason        :{response.reason}")
print(f"Response time :{response.elapsed.total_seconds()} seconds")
print(f"Response size :{len(response.content)} Bytes")

print("\n HEADERS")
print("-" * 50)
for key,value in response.headers.items():
    print(f"{key:<20}:{value}")

print("\n REDIRECT HISTORY")
if response.history:
    for redirects in response.history:
        print(f"{redirects.status_code}->{redirects.headers.get('location','unknown')}")
else:
    print("No Redirects")




# print(response)
# print(response.status_code)
# print(response.reason)
# print(response.url)
# print(response.elapsed.total_seconds())
# print(len(response.content))
# # print(response.text)
# # print(response.headers)
# print(response.headers["Server"])



