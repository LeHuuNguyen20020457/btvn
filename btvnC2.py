def App(app, date, price):
	Ship = 20
	if app == "Shopee":
		if date == "10/10":
			Ship = 0
			price = price - price*0.3
		elif price >= 500:
			price = price - price*0.2
		elif price < 500 and price >= 0:
			pass
		elif price < 0:
			return "không hợp lệ"
	else:
		return "sai app"
	price = price + Ship
	return price


