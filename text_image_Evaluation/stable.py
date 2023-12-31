# LIST
import os
import requests
import config

api_host = os.getenv('API_HOST', 'https://api.stability.ai')
url = f"{api_host}/v1/engines/list"

api_key = config.api_key

# if api_key is None:
#     raise Exception("Missing Stability API key.")

response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})

if response.status_code != 200:
    payload = response.json()
    print(payload)


# TEXT-IMAGE
# import base64
# import os
# import requests
# import config

# engine_id = "stable-diffusion-xl-1024-v1-0"
# api_host = os.getenv('API_HOST', 'https://api.stability.ai')
# api_key = config.api_key

# if api_key is None:
#     raise Exception("Missing Stability API key.")

# response = requests.post(
#     f"{api_host}/v1/generation/{engine_id}/text-to-image",
#     headers={
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#         "Authorization": f"Bearer {api_key}"
#     },
#     json={
#         "text_prompts": [
#             {
#                 "text": "A lighthouse on a cliff"
#             }
#         ],
#         "cfg_scale": 7,
#         "height": 1024,
#         "width": 1024,
#         "samples": 1,
#         "steps": 30,
#     },
# )

# if response.status_code != 200:
#     raise Exception("Non-200 response: " + str(response.text))

# data = response.json()

# for i, image in enumerate(data["artifacts"]):
#     with open(f"./out/v1_txt2img_{i}.png", "wb") as f:
#         f.write(base64.b64decode(image["base64"]))

