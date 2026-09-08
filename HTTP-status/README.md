An API doesn't just return data. It should also tell the client what happened.

That's what HTTP status codes are for.


| Code  | Meaning               | Common Use                     |
| ----- | --------------------- | ------------------------------ |
| `200` | OK                    | Successful GET/PUT/PATCH       |
| `201` | Created               | Successful POST                |
| `204` | No Content            | Successful DELETE              |
| `400` | Bad Request           | Invalid client request         |
| `401` | Unauthorized          | Authentication required/failed |
| `403` | Forbidden             | Authenticated but not allowed  |
| `404` | Not Found             | Resource doesn't exist         |
| `422` | Unprocessable Content | Validation error               |
| `500` | Internal Server Error | Server-side failure            |


**Remember:**
```text
2xx → Success
4xx → Client error
5xx → Server error
```