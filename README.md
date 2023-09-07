# JollyMax Parser

JollyMax Parser is a Python utility for fetching user data from the JollyMax platform, specifically designed for **PUBG Mobile** users.

## Parser

The `JollyMaxParser` class allows you to retrieve user information by providing a user ID. It handles the process of obtaining an access token and querying user data from the JollyMax API.

### Dependencies

- `aiohttp`: Asynchronous HTTP client/server framework.

```python
from jollymax import JollyMaxParser

# Create a JollyMaxParser instance with a PUBGM ID
async with JollyMaxParser(user_id) as pubg_user:
    print(f"ID: {pubg_user.id}, Nick: {pubg_user.nick_name}")
```

## API

The JollyMax Parser API provides a simple endpoint to retrieve user data based on a user's PUBG Mobile ID.

### Endpoints

- `/get?pubg_id=1230`: Fetches user data for a given PUBG Mobile ID.

### Dependencies

- `FastAPI`: Modern, fast (high-performance) web framework for building APIs with Python.

## Demo

You can try the JollyMax Parser API with the following URL:

[Demo API](https://pubgjollymax-1-o0843426.deta.app/)

**Usage**:

https://pubgjollymax-1-o0843426.deta.app/get?pubg_id=5942485795

**Response**:

```json
{
  "id": 5942485795,
  "nickName": "hoosnick"
}
```

## License

This project is licensed under the [Apache License 2.0](LICENSE).
