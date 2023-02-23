import requests,re,sys,os

# Userid By @Xenzi-XN1 & @Aldi098 
# tanggal buat : 23/02/2023
# Open source code >_<

def getuserid(url):
	with requests.Session() as ses:
		ses.get(
			"https://commentpicker.com/find-facebook-id.php",
			headers={
				"Host": "commentpicker.com",
				"upgrade-insecure-requests": "1",
				"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 2007 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"dnt": "1",
				"x-requested-with": "mark.via.gp",
				"sec-fetch-site": "none",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?",
				"sec-fetch-dest": "document"
			}
		)
		cookie = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		respon = ses.get(
			"https://commentpicker.com/actions/token.php?id=whoknows",
			headers={
				"Host": "commentpicker.com",
				"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 2007 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
				"accept": "*/*",
				"x-requested-with": "mark.via.gp",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"referer": "https://commentpicker.com/find-facebook-id.php"
			},
			cookies={
				"cookie": cookie
			}
		)
		cookiee = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		getid = ses.get(
			f"https://commentpicker.com/actions/facebook-id.php?url={url}&token={respon.text}",
			headers={
				"Host": "commentpicker.com",
				"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 2007 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
				"accept": "*/*",
				"x-requested-with": "mark.via.gp",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"referer": "https://commentpicker.com/find-facebook-id.php"
			},
			cookies={
				"cookie": cookiee
			}
		)
		try:
			id = re.search('"entity_id":"(.*?)"', str(getid.text)).group(1)
			print (f"[Respon] Url : {url}\n         Userid : {id}")
		except AttributeError as e:
			exit(f"[Eror] url private")
		except requests.exceptions.ConnectionError:
			exit(f"[Eror] tidak ada koneksi internet")

if __name__ == "__main__":
	home = os.getenv("HOME")
	arg = sys.argv
	try:
		arg[1]
	except:
		exit(f"[Usage] python {arg[0]} <url>")
	getuserid(arg[1])
