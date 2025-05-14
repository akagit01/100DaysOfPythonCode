import qrcode

# Wi-Fi details
ssid = "VM4227284"  # Replace with your Wi-Fi network name
password = "4fEecbrthsVeanan"  # Replace with your Wi-Fi password
encryption = "WPA2"  # Replace with your encryption type (e.g., WPA, WPA2, or WEP)

# Format Wi-Fi QR code data
wifi_data = f"WIFI:T:{encryption};S:{ssid};P:{password};;"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is the smallest, 40 is the largest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Border size (minimum is 4)
)
qr.add_data(wifi_data)
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("wifi_qr_code.png")

print("Wi-Fi QR code generated and saved as 'wifi_qr_code.png'")
