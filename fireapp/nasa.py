import requests

# Set your NASA FIRMS API key
API_KEY = "eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6ImFiaGlfMjMyMzMiLCJleHAiOjE3MDE5MjA0MzIsImlhdCI6MTY5NjczNjQzMiwiaXNzIjoiRWFydGhkYXRhIExvZ2luIn0.L68bzF3PrAWhJpkH8ty1KlZ6Gj_-_LBGP2ZpXmVWAHOuTM5z2rI6EmsZ1jgv2-LSEjD1va9-YR8VtAn1dUUhewt_V7Gvw1p4GQOe-2CGYLmd-tU_gGZ0WrwGgTuk2v-GhA1DWS1YTDggravUWePRzxj86wIGSgeNBh2JSoCVMpfI7Amv3YpYiaHAtkoBGGQiZ7frvzu5GmhSXGJoSpRBLa8B333jXzb5h-DuTvkiu5gprM9n1coVdbv7qQ9UBVroxXI2ovXI4LO-T_dpznV_MVSw97ZWe-oIQzuplAudmtRaoh_lLdZl1ywY3zJqoZ_U0h2WXTOTirlqDE8qdNd1rg"

# Make a request to the FIRMS API
response = requests.get(
    "https://nrt3.modaps.eosdis.nasa.gov/api/v1/firehubs/firepoints/latest.json",
    params={"apiKey": API_KEY},
)

# Check the response status code
if response.status_code == 200:
    # Success!
    data = response.json()

    # Print the number of fire footprints
    print("Number of fire footprints:", len(data["firepoints"]))

    # Print the first fire footprint
    print(data["firepoints"][0])

else:
    # Something went wrong
    print("Error:", response.status_code)
