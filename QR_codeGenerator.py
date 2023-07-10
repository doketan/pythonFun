import qrcode
#from PIL import Image

# data to encode
data = "https://yourdata.com";

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

#
image = qr.make_image(fill_color="black", back_color = "white")

#
image.save("qr_code.png")
#image.open("qr_code.png")

# import qrcode
#
# # Generate a QR code
# data = "Hello, World!"  # Data to be encoded in the QR code
# filename = "qrcode.png"  # Output file name
#
# qr = qrcode.QRCode(
#     version=1,  # QR code version (adjust as needed)
#     error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
#     box_size=10,  # Size of each box in pixels
#     border=4,  # Border size in boxes
# )
# qr.add_data(data)
# qr.make(fit=True)
#
# # Create an image from the QR code data
# img = qr.make_image(fill_color="black", back_color="white")
#
# # Save the image to a file
# img.save(filename)
