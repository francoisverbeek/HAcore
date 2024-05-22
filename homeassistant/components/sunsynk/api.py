"""stub and constants for api accessm."""

BASE_URL = "https://api.sunsynk.net"
BASE_API = BASE_URL + "/api/v1"
BASE_HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "accept-language": "en-US,en;q=0.5",
    "accept-encoding": "gzip, deflate, br",
}


async def get_bearer_token(session, username, password):
    """Get the bearer token for the sunsynk api."""
    params = {
        "username": username,
        "password": password,
        "grant_type": "password",
        "client_id": "csp-web",
        "source": "sunsynk",
        "areaCode": "sunsynk",
    }
    returned = await session.post(
        BASE_URL + "/oauth/token", json=params, headers=BASE_HEADERS
    )

    returned = await returned.json()
    return returned["data"]["access_token"]
