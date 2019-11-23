# How to use each tool

- pos-to-json.py
	This tool is used to convert json from bus station pos API: http://weixin.qianhaixing.cn/weixin/traffic/line/detail/data/13, and convert the json format to Google map format.
	Then replace spots and show them on Google map.
	Usage: python pos-to-json.py <file>

- site-to-json.py
	Convert station position to Google map json format
	Usage: python site-to-json.py <file>

- format.py
	Convert position in specific format directly into json file, input file is example.dat, and output file is example.js.
	The format of example.dat is:
	<lng> <lat>
	Those data is split by space.
	Usage: python format.py