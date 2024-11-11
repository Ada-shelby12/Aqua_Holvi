
import qrcodefrom PIL 
import Image

# Get input data from the user
data = input("Enter the data you want to encode in the QR code: ")

# Create a QRCode object with customization options
qr = qrcode.QRCode(
version=2,  # Adjust version for data size
box_size=10,  # Pixel size of each box in the QR code
border=4  # Number of white borders around the QR code
)

# Add the data to the QR code object
qr.add_data(data)
qr.make(fit=True)  # Ensure data fits within the QR code

# Generate the QR code image with color options
image = qr.make_image(fill_color="black", back_color="white")  # Black foreground, white background

# Save the QR code image
image.save("qr_code.png")

# Display the saved QR code image (optional)
try:
    image = Image.open("qr_code.png")
    image.show()  # Display the image using the default image viewer
except FileNotFoundError:
    print("Error: QR code image not found. Check the file path or try generating it again.")
