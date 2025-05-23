import streamlit as st
from astropy.io import fits


st.title("Convert FITS Timestamp to Decimal Day")
uploaded_file = st.file_uploader("Upload your FIT or FITS file here: ", type=["fits","fit"])

if uploaded_file:
	with fits.open(uploaded_file) as opened_file:
		header = opened_file[0].header
		timestamp = header.get("DATE-AVG", None)

		if timestamp:
			year = timestamp[:4]
			month = timestamp[5:7]
			day = timestamp[8:10]
			date = year + " " + month + " " + day

			hours = int(timestamp[11:13])
			mins = int(timestamp[14:16])
			secs = float(timestamp[17:])

			tot_hours = hours + mins/60 + (secs/60)/60

			fraction_of_day = round(tot_hours/24,5)

			str_frac = str(fraction_of_day)

			while len(str_frac) < 7:
				str_frac += "0"

			final_time = date + str_frac[1:]
			st.write(final_time)
		
		else:
			st.write("No valid timestamp found in file.")









