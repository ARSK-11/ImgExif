import os
import sys
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS
import csv

print(""" welcome in tools imgexif versin 0.1v
	=======================================================================
	wewsdfs qeqweqwqweoqwe                 34eleordfkoeortofogoe
	sfsfsfe qweqweqoowqeoww               p34pp34ppp44erpeprperp
	5600560 qweqweqoqweoowoqw            34ppfpp34pre oroeoroeor
		wqeqweq  qweqweqwe          34ppdpppfpep  rpperpeprp
	weroweo qeqweqw   qweqwewew        o34oodoo3oer   eprpeprpep
	werwerw qweqwew    qweqweqwe      3400d0kkfof     peprpeprpe
	werwrwe qweqwew     oeodfooeo    oe9934kd933      eorjnacokw 
	werwerw wqeqwew      iertigfie  erooerooero       kampretkdf
	werwerw 023992k       idfmvieri eroeroeoro        elwlelwlel
	werwerw 82838ji        irfiri93npweppeero              
	werwerw 0kiiidf                                       IMGExif
	werwerw 934oe99
	werwerw 03kld30
	werwere 2300020
tools imgExif scan information img:
pilihan
1. scan img
2. help
	""")


def create_google_maps_url(gps_coords):
	dec_deg_lat = convert_decimal_degrees(
		float(gps_coords["lat"][0]), 
		float(gps_coords["lat"][1]), 
		float(gps_coords["lat"][2]), 
		gps_coords["lat_ref"])

	dec_deg_lon = convert_decimal_degrees(
		float(gps_coords["lon"][0]), 
		float(gps_coords["lon"][1]), 
		float(gps_coords["lon"][2]), 
		gps_coords["lon_ref"])
	return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"

def convert_decimal_degrees(degree, minutes, seconds, direction):
	decimal_degrees = degree + minutes / 60 + seconds / 3600

	if direction == "S" or direction == "W":
		decimal_degrees*=-1
	return decimal_degrees


while True:
	output_choice = input("otpions>>>>: ")
	try:
		conv_val = int(output_choice)
		if conv_val==1:
			sys.stdout = open("exifdata.txt", "w")
			break
		elif conv_val==2:
			break
		else:
			print("you enter anincorrect option, please try again.")

	except:
		print("""You entered an invalid option, please try again.
			======================================================


			nomer satu options untuk mensecan img 
			options no 2 untuk bantuan



			""")




#add file to the folder ./images
cwd=os.getcwd()
#Change the current working directory to the one where you keep your images.
os.chdir(os.path.join(cwd, "images"))
files=os.listdir()

if len(files)==0:
	print("You don't have have file in the ./images folder.")
	exit()

for file in files:
	try:
		image = Image.open(file)
		print(f"---------------------------------------------{file}--------------------------------------------")
		gps_coords={}
		if image._getexif()==None:
			print(f"{file} contain no exif data")

		else:
			for tag, value in image._getexif().items():
				tag_name =TAGS.get(tag)
				if tag_name == "GPSInfo":
					for key, val in value.items():
						print(f"{GPSTAGS.get(key)} - {val}")
						if GPSTAGS.get(key) == "GPSLatitude":
							gps_coords["lat"] = val

						elif GPSTAGS.get(key) == "GPSLongitude":
							gps_coords["lon"] = val

						elif GPSTAGS.get(key) == "GPSLatitudeRef":
							gps_coords["lat_ref"] = val

						elif GPSTAGS.get(key) == "GPSLongitudeRef":
							gps_coords["lon_ref"] = val

				else:
					print(f"{tag_name} - {value}")


		if gps_coords:
			print(create_google_maps_url(gps_coords))
	except IOError:
		print("File format not supported.")
if output_choice == "1":
	sys.stdout.close()
os.chdir(cwd)