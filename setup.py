import os, urllib

def main():
	filename = "index.html"
	new_index = open(filename, 'w')
	index_content = '<!doctype html>\n\n<html lang="en">\n<head>\n\t<meta charset="utf-8">\n\n\t<title>Your New Website</title>\n\n\t<link rel="stylesheet" href="css/styles.css">\n\n</head>\n\n<body>\nHello, world!\n\t<script src="js/scripts.js"></script>\n</body>\n</html>\n'
	new_index.write(index_content)
	new_index.close()

	if not os.path.exists("js"):
		os.makedirs("js")
		new_js = open("js/scripts.js", 'w')
		new_js.close()

	if not os.path.exists("css"):
		os.makedirs("css")
		new_css = open("css/styles.css", 'w')
		new_css.close()

if __name__ == "__main__":
	main()


