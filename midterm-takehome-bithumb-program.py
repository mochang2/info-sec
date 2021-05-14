# midterm-takehome-2021.py
#
# XCoin API-call related functions
#

import sys
import time
import math
import base64
import hmac, hashlib
import urllib.parse
import json
import pprint
import certifi


class XCoinAPI:
        # attributes
	api_url = "https://api.bithumb.com" #bithumb url
	api_key = ""
	api_secret = ""

	def __init__(self, api_key, api_secret):  #Constructor
		self.api_key = api_key
		self.api_secret = api_secret

	def body_callback(self, buf):
		self.contents = buf
		
	def usecTime(self) : # used to generate nonce
		mt = self.microtime(False)
		mt_array = mt.split(" ")[:2]
		return mt_array[1] + mt_array[0][2:5]
	def microtime(self, get_as_float = False): 
		if get_as_float:
			return time.time()
		else:
			return '%f %d' % math.modf(time.time())

	def xcoinApiCall(self, endpoint, rgParams):
		# 1. Api-Sign and Api-Nonce information generation.
		# 2. Request related information from the Bithumb API server.
		#
		# - nonce: it is an arbitrary number that may only be used once.
		# - api_sign: API signature information created in various combinations values.

                         #key encoding
		endpoint_item_array = {
			"endpoint" : endpoint
		}

		uri_array = dict(endpoint_item_array, **rgParams) # Concatenate the two arrays.

		str_data = urllib.parse.urlencode(uri_array)

		nonce = self.usecTime()  #nonce: time value

		data = endpoint + chr(0) + str_data + chr(0) + nonce
		utf8_data = data.encode('utf-8')

		key = self.api_secret
		utf8_key = key.encode('utf-8')

                         # hash mac with integrity
		h = hmac.new(bytes(utf8_key), utf8_data, hashlib.sha512)
		hex_output = h.hexdigest()
		utf8_hex_output = hex_output.encode('utf-8')

		api_sign = base64.b64encode(utf8_hex_output)
		utf8_api_sign = api_sign.decode('utf-8')

                         
                         # set curl options
		curl_handle = pycurl.Curl()
		curl_handle.setopt(pycurl.POST, 1)
		curl_handle.setopt(pycurl.POSTFIELDS, str_data)
		curl_handle.setopt(pycurl.CAINFO, certifi.where().encode('utf-8')) # encoded to avoid UnicodeEncodeError
                         # SSL certificate

		url = self.api_url + endpoint
		curl_handle.setopt(curl_handle.URL, url)
		curl_handle.setopt(curl_handle.HTTPHEADER, ['Api-Key: ' + self.api_key, 'Api-Sign: ' + utf8_api_sign, 'Api-Nonce: ' + nonce])
		curl_handle.setopt(curl_handle.WRITEFUNCTION, self.body_callback)
		curl_handle.perform()

		#response_code = curl_handle.getinfo(pycurl.RESPONSE_CODE) # Get http response status code.

		curl_handle.close()

		return (json.loads(self.contents)) #return with dict format


# 21.04.24 기준 disable 시킴
api_key = "071583fd0c535168b4847d15ee610bf6" # connect_key
api_secret = "ccb369583890cc374116b0c678e86724"

api = XCoinAPI(api_key, api_secret);

rgParams = {
	"order_currency" : "BTC",
	"payment_currency" : "KRW"
};



#
# private api
#
# endpoint		=> parameters
# /info/current
# /info/account
# /info/balance
# /info/wallet_address

# A. Balance
resultA = api.xcoinApiCall("/info/balance", rgParams)
print("""
{{
        status :  {}
        data : {{
                total_btc : {}
                total_krw : {}
                in_use_btc : {}
                in_use_krw : {}
                available_btc : {}
                available_krw : {}
                xcoin_last_btc : {}
        }}
}}""".format(resultA["status"], resultA["data"]["total_btc"], 
            resultA["data"]["total_krw"], resultA["data"]["in_use_btc"], 
            resultA["data"]["in_use_krw"], resultA["data"]["available_btc"], 
            resultA["data"]["available_krw"], resultA["data"]["xcoin_last_btc"]))



# B. Orders
resultB = api.xcoinApiCall("/info/orders", rgParams)
print(resultB)
print("""
{{
        status :  {}
        message : {}
}}""".format(resultB["status"], resultB["message"]))
"""  #no have orders
            resultB["data"]["payment_currency"], resultB["data"]["order_id"], 
            resultB["data"]["order_date"], resultB["data"]["type"], 
            resultB["data"]["units"], resultB["data"]["units_remaining"],
             resultB["data"]["price"]))"""
