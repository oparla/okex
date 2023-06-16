from geopy.geocoders import Nominatim

# Koordinat latitude dan longitude
latitude = -2.9760735
longitude = 104.7754307

# Membuat objek geocoder
geolocator = Nominatim(user_agent="my-app")

# Mendapatkan informasi lokasi berdasarkan koordinat
location = geolocator.reverse((latitude, longitude))

# Menampilkan hasil lokasi
print(location.address)
