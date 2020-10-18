Select round (long_w , 4) from station where lat_n = (Select min(lat_n) from station where lat_n > 38.7780);
