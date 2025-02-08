import os
import requests
import wget
import ctypes
import time

SPI_SETDESKWALLPAPER = 0x0014
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDCHANGE = 0x02
def get_wallpaper():

    access_key = os.environ.get('UNSPLASH_ACCESS_KEY')
    url = 'https://api.unsplash.com/photos/random/?client_id='+access_key
    params = {
		"query": "HD Wallpapers",
		"orientation": "landscape"
	}
    response = requests.get(url,params=params).json()
    image_url = response['urls']['full']
    wallpaper = wget.download(image_url, 'C:\\Users\\arsha\\OneDrive\\Desktop\\Python Projects')
    return wallpaper

def change_wallpaper():
    """
    Sets the downloaded wallpaper as the desktop background on Windows.
    """
    wallpaper = get_wallpaper()

    # Use the Windows API to set the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, wallpaper, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
    )

def main():
	try:
		while True:
			change_wallpaper()
			time.sleep(10)

	except KeyboardInterrupt:
		print("\nHope you like this one! Quitting.")
	except Exception as e:
		pass
	

if __name__ == "__main__":
	main()
