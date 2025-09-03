import requests
import json

# The URL of your running FastAPI server
API_URL = "http://127.0.0.1:8000/analyze-url"

# The target URL you want to analyze
TARGET_URL = "http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster"
# Alternative URL for testing: a clean news article
# TARGET_URL = "http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/"
TARGET_URL="http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/"

def run_test():
    print(f"Sending request to analyze: {TARGET_URL}")
    headers = {'Content-Type': 'application/json'}
    json_data = {'url': TARGET_URL}

    try:
        response = requests.post(API_URL, headers=headers, json=json_data)
        response.raise_for_status()  # This will raise an error for bad responses (4xx or 5xx)

        print("\n--- ✅ Success! ---")
        print("Response JSON:")
        # Pretty-print the JSON response
        print(json.dumps(response.json(), indent=2))

    except requests.exceptions.HTTPError as err:
        print(f"\n--- ❌ HTTP Error ---")
        print(f"Status Code: {err.response.status_code}")
        print("Response Body:")
        print(err.response.text)
    except requests.exceptions.RequestException as e:
        print(f"\n--- ❌ Request Failed ---")
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_test()




# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# # Load environment variables from a .env file
# load_dotenv()

# # --- Configuration ---
# # The model we want to test
# MODEL_NAME = "gemini-1.5-flash-latest"

# # A simple question to ask the model
# PROMPT = "What is the capital of France?"

# def run_gemini_test():
#     """
#     A simple, isolated test to check the connection to the Google Gemini API
#     using an API key and the ChatGoogleGenerativeAI class.
#     """
#     print("--- Google Gemini Connection Test ---")

#     # Check if the API key is available in the environment
#     if not os.getenv("GOOGLE_API_KEY"):
#         print("\n--- ❌ FAILURE ---")
#         print("Error: GOOGLE_API_KEY environment variable not found.")
#         print("Please create a .env file and add your key, or export the variable.")
#         return

#     try:
#         print(f"1. Initializing ChatGoogleGenerativeAI with model: '{MODEL_NAME}'...")
#         llm = ChatGoogleGenerativeAI(model=MODEL_NAME, temperature=0)
#         print("   ✅ Model initialized successfully.")

#         print(f"\n2. Sending prompt to the model: '{PROMPT}'...")
#         response = llm.invoke(PROMPT)
        
#         print("\n--- ✅ SUCCESS! ---")
#         print("Received a valid response from the model.")
#         print(f"\nPrompt: {PROMPT}")
#         # The response from this class is an AIMessage object, so we access its content
#         print(f"Response: {response.content}")

#     except Exception as e:
#         print("\n--- ❌ FAILURE ---")
#         print("An error occurred while trying to connect to the Google Gemini API.")
#         print(f"Error Type: {type(e).__name__}")
#         print(f"Error Details: {repr(e)}")
#         print("\nPossible causes:")
#         print("- The API key might be invalid or not enabled for the Gemini API.")
#         print("- There might be a network issue blocking the connection to Google's servers.")

# if __name__ == "__main__":
#     run_gemini_test()


# import requests

# cookies = {
#     'akamai_session': '23.63.108.77.20909461756816876333',
#     'PHPSESSID': '45e073e6e88a6809504979e93549742e',
#     'wordpress_test_cookie': 'WP%20Cookie%20check',
#     'EdgeLocation': '28.60,77.20',
#     'PIM-SESSION-ID': 'tNlyrEtlE2OsenC3',
#     '_ntv_uid': 'ddbfhbgfynbhebg2ngdvajj3haiiff1756816877799',
#     'AMCVS_F0A65E09512D2C440A490D4D%40AdobeOrg': '1',
#     's_ecid': 'MCMID%7C23499472635433907691354921466440391014',
#     'qualtricsSwimlaneCookie': '64',
#     's_cc': 'true',
#     '_fbp': 'fb.1.1756816880332.545584050994168135',
#     'QSI_HistorySession': 'https%3A%2F%2Fwww.rei.com%2Fblog%2Fcamp%2Fhow-to-introduce-your-indoorsy-friend-to-the-outdoors%2F~1756816880546',
#     '_gcl_au': '1.1.1034985597.1756816881',
#     'bluecoreNV': 'false',
#     'bm_ss': 'ab8e18ef4e',
#     'bm_so': '9086E5FD35B1BED742ADF6CCA15CD8F0BABD75777FE96FE12E698BAE186DF9BA~YAAQTWw/F2BZLvGYAQAAdk4mDgRPPVnO+cYexUGEnX0cXOChVHv3G0flnrolkPNj4h7AquE74DsZ26NTHjoyJkGkXVQNqo6hrzJE/kl399E0tDEcrZptApoZBjnEjEO4KnQbzG8omG+QLARdETxVHmNkvrj3Cuggg1okghTLI/Fd4tUfQRrmXpMOHxn6YzetyZCEh3d/WlrDNePcjhy2BALfA9YD/Lbt/XqtNmuou6qCbFWplLbfLbE6uu+wCctdIDXAvKewXYcECN/OdoTNM0JxYPy/gaTGlgBWeVQhbFuVwqMVzB36eVaL+44pdfmHDuJT9EtrDSksy3JJpjJ26wUZ0X8bXT55YLJN1GpMyJ1IJxUlh4rvOhahjEyGyA2blU6d2QHOSSgByoJzoimFjwB7CdAVBPyUjshLyCrjWDXk2v/rcfhXcmZjPXEmzu5U5oesEWu6UWRyrw==',
#     'bm_sz': '261E127A3A07E87997BD4C54B5428B03~YAAQTWw/F2FZLvGYAQAAdk4mDhxReso3mOE1Vjsun5gJt9ehviU97VW+4LAAnGYwg6XqzdYWKFIQ8W7tClylt16LbdpQPZToW86CLLMCSIzfOlEzoMPaimMg5MMA7KLCdOHEu2nNGuVpS4215iIGWkFKmGI/QZsjSiTX67mdZoIUMMR4nPkXRTgvV8+LIUf/BgKeBk4kT+6eanDQ9wqYNRu8K28ib3nQQEbA0klbiSKnnJm6XBtYskQiYVgQXgeCr8UcKF9F3LERnobXOXJ1/i/zcWS2Nl29DdGYkv7aSixaWLmX0b3g1dEOIRZljHxvlUITFwTDBm73WENHqf+AT3BAfm+x/J5ClVdcJmWfrvBn5YG7VnWDj4Fod29anyUKC+w+EM8=~3355202~3619126',
#     '_abck': '4ACDA0DAC1A926B3EB289E7052835B17~0~YAAQTWw/F35ZLvGYAQAA1U4mDg4UvDqYErFvMiOG7vstB7PGEYc+7uK976AajIiqVjZV9dB48RXNskMNp0qfB+vlNK1whaI0fZ3WMunyNSlGlPIsRcLcXUFGCg1K1nrLVsQjNtOvTC3ES8IVtPghmnsmH7b/zP3S5C0cs3Ozs6UWxhkpnjYxQRO7L4p7HDtQK9MEAWnXIH1d5wW4E15Me277ln6OE3TVR0KXGhyZK2YyqzIwwqDByKIyIEpxKbb0v45jRYKzGhK6+IZQB0nVwml4DMZp64W+0BNNuEypYU7VjHcja8s3YfBbrwFCinU1Y7E96zf8YCNKTt6guS4XTiiAfumHqB6LyD9rJu3SmJEaGsTT1SnAEbdVrB9ZCRyzs7mxMv2O01V+0I35U4iRO6D9/BaqX6Gi8zOZ3LrABpPp2WAnMYEpUNDvenoSwqzrvIEEjSIoWPGz2h4zKcud9hJjyRtjeDJNNwoLBI6BwFvGRXPOkIJj2d2KTonOUEGa2487vLPe7NWmsCKR1hSRFcZtOgTQnZvNsh486AIJbIgXRtrfbLBEYRmt7pCpB6YHvNxcMB+z/jpxs68AU7+tHomH/ANiqvG7D+El3cdGv+seEAnnDZSYd2L02+a093zuTPB1uQ==~-1~-1~-1~~',
#     'bm_mi': '83FE06F9FB982EB9B575BBBF23D6DA6C~YAAQTWw/F7lZLvGYAQAA+VAmDhy0Xf+9oxkuT+yIvXW2tqqK57stdJpnUFuAjnC8sBCOdx/n2eVNq+JV++tmA4R3D7CRvI4LUvVmHKPR0Ur5T/hS3wspYqCN2Z4hdfrxL7yEzP+WKrsy4LCI8gqREDKxdIUdaZ+2VIAlTXuJwu1hgPS6t2BdXFnYE1KYT5b0P5A38gt8YF2qBMir8n4x/lN0oP/UcnxqdVLp/N2QeNPtvOjwYjTNEOoSJm1FhARIHv/Tb3XMV1i7MHEX2gYdZDYxpo5VN4FI7VvHeHXY3Ei5NEYW+tTEuB/cqeHrs4OiL8tNZW+oDMKOKd69IXArofbunXQR7jdATut61OLB7nTH1TV2YsYZABNwBdHE/q38Pcre/VRKrUZtnc6z8R3Wix1s5MKFO4aNgN8S6Ruio4Wo7Q8Z2SZxtvk2kTncadPEP/XVygvH7jghbLYxmoUeWqiyb6ABFx+VL4J9pmHImhZEh0+bpZSmn/XiTBtwpEqq/4OjZZSzSEK5JAlbZrbh9epI~1',
#     'AMCV_F0A65E09512D2C440A490D4D%40AdobeOrg': '1585540135%7CMCIDTS%7C20334%7CMCMID%7C23499472635433907691354921466440391014%7CMCAAMLH-1757483817%7C12%7CMCAAMB-1757483817%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1756886217s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-20341%7CvVersion%7C4.4.0%7CMCCIDH%7C-568361799',
#     'mp_rei_us_mixpanel': '%7B%22distinct_id%22%3A%20%221990a72334e543-0bcec325910073-1f462c6e-1fa400-1990a72334f111%22%2C%22bc_persist_updated%22%3A%201756816880985%2C%22bc_last_opaque_id%22%3A%202091690384%7D',
#     'bc_invalidateUrlCache_targeting': '1756879017785',
#     's_ppvl': 'blog%253AHow%2520to%2520Introduce%2520Your%2520Indoorsy%2520Friend%2520to%2520the%2520Outdoors%2C23%2C23%2C1288%2C1536%2C732%2C1920%2C1080%2C1.25%2CP',
#     'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Sep+03+2025+11%3A26%3A57+GMT%2B0530+(India+Standard+Time)&version=202504.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=9672c5f2-4d65-4f9a-8145-38c8344ac15b&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.rei.com%2Fblog%2Fcamp%2Fhow-to-introduce-your-indoorsy-friend-to-the-outdoors%2F&groups=C0004%3A1%2CC0001%3A1%2CC0005%3A1%2CC0002%3A1%2CC0003%3A1',
#     'bm_lso': '9086E5FD35B1BED742ADF6CCA15CD8F0BABD75777FE96FE12E698BAE186DF9BA~YAAQTWw/F2BZLvGYAQAAdk4mDgRPPVnO+cYexUGEnX0cXOChVHv3G0flnrolkPNj4h7AquE74DsZ26NTHjoyJkGkXVQNqo6hrzJE/kl399E0tDEcrZptApoZBjnEjEO4KnQbzG8omG+QLARdETxVHmNkvrj3Cuggg1okghTLI/Fd4tUfQRrmXpMOHxn6YzetyZCEh3d/WlrDNePcjhy2BALfA9YD/Lbt/XqtNmuou6qCbFWplLbfLbE6uu+wCctdIDXAvKewXYcECN/OdoTNM0JxYPy/gaTGlgBWeVQhbFuVwqMVzB36eVaL+44pdfmHDuJT9EtrDSksy3JJpjJ26wUZ0X8bXT55YLJN1GpMyJ1IJxUlh4rvOhahjEyGyA2blU6d2QHOSSgByoJzoimFjwB7CdAVBPyUjshLyCrjWDXk2v/rcfhXcmZjPXEmzu5U5oesEWu6UWRyrw==^1756879018052',
#     'utag_main': 'v_id:01990a722eb90042cc149c07e3e405065005405d00bd0$_sn:4$_se:1$_ss:1$_st:1756880816847$vapi_domain:rei.com$dc_visit:4$ses_id:1756879016847%3Bexp-session$_pn:1%3Bexp-session$_prevpage:blog%3AHow%20to%20Introduce%20Your%20Indoorsy%20Friend%20to%20the%20Outdoors%3Bexp-1756882617527$dc_event:1%3Bexp-session$dc_region:me-central-1%3Bexp-session',
#     'bm_s': 'YAAQTWw/Fx5bLvGYAQAACFsmDgSsWvuXECsIG4+BJswvNldDVKEc4zq/GQygeyr/Cjad6K5w/Pr52FNWmuz44hSxTjQogPhHYkYhaSGOilBGQzWhywh3oj3UqdTOCFJrHoD9byJIcRGR2LJQZfYkSr1YbVRsJwCv//qX8SttBrAQuz55eJFf7wbbeI6RSMJbUhx500VFAdq0q7LiqIvWrX7PO8V8D9MYKqYiyj6NXD5gtqRAq0YpHFaaKmpExREiCPWwOrjxsVvZgb4ooAvOEWg1k+M3TiqqPcQCmVBsGyop6gLTCqaMWUwufD0sp04U6B635jee7F/COqnrdwLcyjNaZrkCBcllIsftFDktmQSMOmvj9sG5MW3fqjYJcjVzreJvDv52MSUiBZASWSLYEHN3WVpgFARx8y28+hte1hMROeYMRwpJlYvLU3RvX4bUhzP+fhTHcN5N3amBLdcZC3IMiGk0bjGQ48+6pqjPkg+0Wlinvfj+ccAxNY0N/fcnsXHXkOYSCaL/MjQdi+SZ+ehU5Vkw5qmT176zM4vGxHhEthMppYXiTG1w4Q==',
#     's_ppv': 'blog%253AHow%2520to%2520Introduce%2520Your%2520Indoorsy%2520Friend%2520to%2520the%2520Outdoors%2C29%2C24%2C1632%2C830%2C732%2C1920%2C1080%2C1.25%2CP',
#     'bm_sv': '622923CB5BC3EF52F064B2BEAC5B47E1~YAAQTWw/F9JcLvGYAQAAQ2UmDhzEAgQk9PWjY0k4TH1eH6N+YopOYU2UTsnmUqxrW6kQt31hgbxrcIybauIrstrAuy3wECpsOFxqe6WU/OwhYIzp0sFH8nbLkktTUjsYJ9f1eIU6B49OY9ZxXOBwnmLz+Ys4Fg6YKNgKqJedg6oJmxiSdB4w3rDFzRfv1/ALvmVp+YoLJ4duOHfhtwYK0UYhDl+FqOVdpAzH7Uu905lP66tYMTPGy3AWeuln~1',
#     'ak_bmsc': 'E1162D36AE661B4E9B69A6FD152C0E8B~000000000000000000000000000000~YAAQTWw/F+pcLvGYAQAAOWYmDhwo038MIzsjQZQaqO96s8MDc9Ao53ee9PJV/5gDriW/FFtDpgEKIVQ5LFMwOAn+JmOV7h7McUyGE8I/HMwAuUxAfPzsHtWd92bts8+Sqs4xySjlPauBoiHKx7JUpkwlAigzPQ64IAzTrPyJ5sGB+bDRQnl3prin/eZh7YmRbY5C8p+JBgfbtIRbmD2poEs3eKt9WXj0t/0nVVxf+kxN0uQI/kG01XGyv33bvskJx6r6GGMBCj9mJ6s9V802IiHDlgkU9HlE47+TvHGEWZv7mJWM0OkezjssoMQGem1Mr/18aWxcK3qo83SnPaMGTuLBfGCFdYBq7orVg6OwAoKQmCm9KMbFX3fVkPPA4UiryKej1Lt2YwVhFB8DDk9cinZlUiXEVQDJxlMIp+mSDkGhHnmMUcLDeyUC+xyt0izFysF0LgjAj9l1mWH1xSKO5k5PPiEE/KTftIkFb6GESfG9MhJ+Pxi25Ee5Q8RZTg+3dBI5olUTki4y9d0nFnPiVii7J/0awtX8/Oa5wbMCnE+HgCuw7o0nPgv6RerelA3Wr/hHlxi60+yuO5rd+6LuAoHoboqZ4OK54J5eGK02dpwtjL4fUg7Gzsf6adR8IafjcMbNWbnjRRoah2BstMwJSfa9oa9ZWGuL0bv19HzAY3o0EgOFKc3/',
# }

# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
#     'cache-control': 'max-age=0',
#     'priority': 'u=0, i',
#     'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
#     # 'sec-ch-ua-mobile': '?0',
#     # 'sec-ch-ua-platform': '"Linux"',
#     # 'sec-fetch-dest': 'document',
#     # 'sec-fetch-mode': 'navigate',
#     # 'sec-fetch-site': 'none',
#     # 'sec-fetch-user': '?1',
#     # 'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
#     # 'cookie': 'akamai_session=23.63.108.77.20909461756816876333; PHPSESSID=45e073e6e88a6809504979e93549742e; wordpress_test_cookie=WP%20Cookie%20check; EdgeLocation=28.60,77.20; PIM-SESSION-ID=tNlyrEtlE2OsenC3; _ntv_uid=ddbfhbgfynbhebg2ngdvajj3haiiff1756816877799; AMCVS_F0A65E09512D2C440A490D4D%40AdobeOrg=1; s_ecid=MCMID%7C23499472635433907691354921466440391014; qualtricsSwimlaneCookie=64; s_cc=true; _fbp=fb.1.1756816880332.545584050994168135; QSI_HistorySession=https%3A%2F%2Fwww.rei.com%2Fblog%2Fcamp%2Fhow-to-introduce-your-indoorsy-friend-to-the-outdoors%2F~1756816880546; _gcl_au=1.1.1034985597.1756816881; bluecoreNV=false; bm_ss=ab8e18ef4e; bm_so=9086E5FD35B1BED742ADF6CCA15CD8F0BABD75777FE96FE12E698BAE186DF9BA~YAAQTWw/F2BZLvGYAQAAdk4mDgRPPVnO+cYexUGEnX0cXOChVHv3G0flnrolkPNj4h7AquE74DsZ26NTHjoyJkGkXVQNqo6hrzJE/kl399E0tDEcrZptApoZBjnEjEO4KnQbzG8omG+QLARdETxVHmNkvrj3Cuggg1okghTLI/Fd4tUfQRrmXpMOHxn6YzetyZCEh3d/WlrDNePcjhy2BALfA9YD/Lbt/XqtNmuou6qCbFWplLbfLbE6uu+wCctdIDXAvKewXYcECN/OdoTNM0JxYPy/gaTGlgBWeVQhbFuVwqMVzB36eVaL+44pdfmHDuJT9EtrDSksy3JJpjJ26wUZ0X8bXT55YLJN1GpMyJ1IJxUlh4rvOhahjEyGyA2blU6d2QHOSSgByoJzoimFjwB7CdAVBPyUjshLyCrjWDXk2v/rcfhXcmZjPXEmzu5U5oesEWu6UWRyrw==; bm_sz=261E127A3A07E87997BD4C54B5428B03~YAAQTWw/F2FZLvGYAQAAdk4mDhxReso3mOE1Vjsun5gJt9ehviU97VW+4LAAnGYwg6XqzdYWKFIQ8W7tClylt16LbdpQPZToW86CLLMCSIzfOlEzoMPaimMg5MMA7KLCdOHEu2nNGuVpS4215iIGWkFKmGI/QZsjSiTX67mdZoIUMMR4nPkXRTgvV8+LIUf/BgKeBk4kT+6eanDQ9wqYNRu8K28ib3nQQEbA0klbiSKnnJm6XBtYskQiYVgQXgeCr8UcKF9F3LERnobXOXJ1/i/zcWS2Nl29DdGYkv7aSixaWLmX0b3g1dEOIRZljHxvlUITFwTDBm73WENHqf+AT3BAfm+x/J5ClVdcJmWfrvBn5YG7VnWDj4Fod29anyUKC+w+EM8=~3355202~3619126; _abck=4ACDA0DAC1A926B3EB289E7052835B17~0~YAAQTWw/F35ZLvGYAQAA1U4mDg4UvDqYErFvMiOG7vstB7PGEYc+7uK976AajIiqVjZV9dB48RXNskMNp0qfB+vlNK1whaI0fZ3WMunyNSlGlPIsRcLcXUFGCg1K1nrLVsQjNtOvTC3ES8IVtPghmnsmH7b/zP3S5C0cs3Ozs6UWxhkpnjYxQRO7L4p7HDtQK9MEAWnXIH1d5wW4E15Me277ln6OE3TVR0KXGhyZK2YyqzIwwqDByKIyIEpxKbb0v45jRYKzGhK6+IZQB0nVwml4DMZp64W+0BNNuEypYU7VjHcja8s3YfBbrwFCinU1Y7E96zf8YCNKTt6guS4XTiiAfumHqB6LyD9rJu3SmJEaGsTT1SnAEbdVrB9ZCRyzs7mxMv2O01V+0I35U4iRO6D9/BaqX6Gi8zOZ3LrABpPp2WAnMYEpUNDvenoSwqzrvIEEjSIoWPGz2h4zKcud9hJjyRtjeDJNNwoLBI6BwFvGRXPOkIJj2d2KTonOUEGa2487vLPe7NWmsCKR1hSRFcZtOgTQnZvNsh486AIJbIgXRtrfbLBEYRmt7pCpB6YHvNxcMB+z/jpxs68AU7+tHomH/ANiqvG7D+El3cdGv+seEAnnDZSYd2L02+a093zuTPB1uQ==~-1~-1~-1~~; bm_mi=83FE06F9FB982EB9B575BBBF23D6DA6C~YAAQTWw/F7lZLvGYAQAA+VAmDhy0Xf+9oxkuT+yIvXW2tqqK57stdJpnUFuAjnC8sBCOdx/n2eVNq+JV++tmA4R3D7CRvI4LUvVmHKPR0Ur5T/hS3wspYqCN2Z4hdfrxL7yEzP+WKrsy4LCI8gqREDKxdIUdaZ+2VIAlTXuJwu1hgPS6t2BdXFnYE1KYT5b0P5A38gt8YF2qBMir8n4x/lN0oP/UcnxqdVLp/N2QeNPtvOjwYjTNEOoSJm1FhARIHv/Tb3XMV1i7MHEX2gYdZDYxpo5VN4FI7VvHeHXY3Ei5NEYW+tTEuB/cqeHrs4OiL8tNZW+oDMKOKd69IXArofbunXQR7jdATut61OLB7nTH1TV2YsYZABNwBdHE/q38Pcre/VRKrUZtnc6z8R3Wix1s5MKFO4aNgN8S6Ruio4Wo7Q8Z2SZxtvk2kTncadPEP/XVygvH7jghbLYxmoUeWqiyb6ABFx+VL4J9pmHImhZEh0+bpZSmn/XiTBtwpEqq/4OjZZSzSEK5JAlbZrbh9epI~1; AMCV_F0A65E09512D2C440A490D4D%40AdobeOrg=1585540135%7CMCIDTS%7C20334%7CMCMID%7C23499472635433907691354921466440391014%7CMCAAMLH-1757483817%7C12%7CMCAAMB-1757483817%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1756886217s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-20341%7CvVersion%7C4.4.0%7CMCCIDH%7C-568361799; mp_rei_us_mixpanel=%7B%22distinct_id%22%3A%20%221990a72334e543-0bcec325910073-1f462c6e-1fa400-1990a72334f111%22%2C%22bc_persist_updated%22%3A%201756816880985%2C%22bc_last_opaque_id%22%3A%202091690384%7D; bc_invalidateUrlCache_targeting=1756879017785; s_ppvl=blog%253AHow%2520to%2520Introduce%2520Your%2520Indoorsy%2520Friend%2520to%2520the%2520Outdoors%2C23%2C23%2C1288%2C1536%2C732%2C1920%2C1080%2C1.25%2CP; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Sep+03+2025+11%3A26%3A57+GMT%2B0530+(India+Standard+Time)&version=202504.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=9672c5f2-4d65-4f9a-8145-38c8344ac15b&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.rei.com%2Fblog%2Fcamp%2Fhow-to-introduce-your-indoorsy-friend-to-the-outdoors%2F&groups=C0004%3A1%2CC0001%3A1%2CC0005%3A1%2CC0002%3A1%2CC0003%3A1; bm_lso=9086E5FD35B1BED742ADF6CCA15CD8F0BABD75777FE96FE12E698BAE186DF9BA~YAAQTWw/F2BZLvGYAQAAdk4mDgRPPVnO+cYexUGEnX0cXOChVHv3G0flnrolkPNj4h7AquE74DsZ26NTHjoyJkGkXVQNqo6hrzJE/kl399E0tDEcrZptApoZBjnEjEO4KnQbzG8omG+QLARdETxVHmNkvrj3Cuggg1okghTLI/Fd4tUfQRrmXpMOHxn6YzetyZCEh3d/WlrDNePcjhy2BALfA9YD/Lbt/XqtNmuou6qCbFWplLbfLbE6uu+wCctdIDXAvKewXYcECN/OdoTNM0JxYPy/gaTGlgBWeVQhbFuVwqMVzB36eVaL+44pdfmHDuJT9EtrDSksy3JJpjJ26wUZ0X8bXT55YLJN1GpMyJ1IJxUlh4rvOhahjEyGyA2blU6d2QHOSSgByoJzoimFjwB7CdAVBPyUjshLyCrjWDXk2v/rcfhXcmZjPXEmzu5U5oesEWu6UWRyrw==^1756879018052; utag_main=v_id:01990a722eb90042cc149c07e3e405065005405d00bd0$_sn:4$_se:1$_ss:1$_st:1756880816847$vapi_domain:rei.com$dc_visit:4$ses_id:1756879016847%3Bexp-session$_pn:1%3Bexp-session$_prevpage:blog%3AHow%20to%20Introduce%20Your%20Indoorsy%20Friend%20to%20the%20Outdoors%3Bexp-1756882617527$dc_event:1%3Bexp-session$dc_region:me-central-1%3Bexp-session; bm_s=YAAQTWw/Fx5bLvGYAQAACFsmDgSsWvuXECsIG4+BJswvNldDVKEc4zq/GQygeyr/Cjad6K5w/Pr52FNWmuz44hSxTjQogPhHYkYhaSGOilBGQzWhywh3oj3UqdTOCFJrHoD9byJIcRGR2LJQZfYkSr1YbVRsJwCv//qX8SttBrAQuz55eJFf7wbbeI6RSMJbUhx500VFAdq0q7LiqIvWrX7PO8V8D9MYKqYiyj6NXD5gtqRAq0YpHFaaKmpExREiCPWwOrjxsVvZgb4ooAvOEWg1k+M3TiqqPcQCmVBsGyop6gLTCqaMWUwufD0sp04U6B635jee7F/COqnrdwLcyjNaZrkCBcllIsftFDktmQSMOmvj9sG5MW3fqjYJcjVzreJvDv52MSUiBZASWSLYEHN3WVpgFARx8y28+hte1hMROeYMRwpJlYvLU3RvX4bUhzP+fhTHcN5N3amBLdcZC3IMiGk0bjGQ48+6pqjPkg+0Wlinvfj+ccAxNY0N/fcnsXHXkOYSCaL/MjQdi+SZ+ehU5Vkw5qmT176zM4vGxHhEthMppYXiTG1w4Q==; s_ppv=blog%253AHow%2520to%2520Introduce%2520Your%2520Indoorsy%2520Friend%2520to%2520the%2520Outdoors%2C29%2C24%2C1632%2C830%2C732%2C1920%2C1080%2C1.25%2CP; bm_sv=622923CB5BC3EF52F064B2BEAC5B47E1~YAAQTWw/F9JcLvGYAQAAQ2UmDhzEAgQk9PWjY0k4TH1eH6N+YopOYU2UTsnmUqxrW6kQt31hgbxrcIybauIrstrAuy3wECpsOFxqe6WU/OwhYIzp0sFH8nbLkktTUjsYJ9f1eIU6B49OY9ZxXOBwnmLz+Ys4Fg6YKNgKqJedg6oJmxiSdB4w3rDFzRfv1/ALvmVp+YoLJ4duOHfhtwYK0UYhDl+FqOVdpAzH7Uu905lP66tYMTPGy3AWeuln~1; ak_bmsc=E1162D36AE661B4E9B69A6FD152C0E8B~000000000000000000000000000000~YAAQTWw/F+pcLvGYAQAAOWYmDhwo038MIzsjQZQaqO96s8MDc9Ao53ee9PJV/5gDriW/FFtDpgEKIVQ5LFMwOAn+JmOV7h7McUyGE8I/HMwAuUxAfPzsHtWd92bts8+Sqs4xySjlPauBoiHKx7JUpkwlAigzPQ64IAzTrPyJ5sGB+bDRQnl3prin/eZh7YmRbY5C8p+JBgfbtIRbmD2poEs3eKt9WXj0t/0nVVxf+kxN0uQI/kG01XGyv33bvskJx6r6GGMBCj9mJ6s9V802IiHDlgkU9HlE47+TvHGEWZv7mJWM0OkezjssoMQGem1Mr/18aWxcK3qo83SnPaMGTuLBfGCFdYBq7orVg6OwAoKQmCm9KMbFX3fVkPPA4UiryKej1Lt2YwVhFB8DDk9cinZlUiXEVQDJxlMIp+mSDkGhHnmMUcLDeyUC+xyt0izFysF0LgjAj9l1mWH1xSKO5k5PPiEE/KTftIkFb6GESfG9MhJ+Pxi25Ee5Q8RZTg+3dBI5olUTki4y9d0nFnPiVii7J/0awtX8/Oa5wbMCnE+HgCuw7o0nPgv6RerelA3Wr/hHlxi60+yuO5rd+6LuAoHoboqZ4OK54J5eGK02dpwtjL4fUg7Gzsf6adR8IafjcMbNWbnjRRoah2BstMwJSfa9oa9ZWGuL0bv19HzAY3o0EgOFKc3/',
# }

# response = requests.get(
#     'https://www.rei.com/blog/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/',
#     # cookies=cookies,
#     headers=headers,
# )

# print("Status Code:", response.status_code)
# print("Content Length:", len(response.text))

