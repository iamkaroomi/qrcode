import qrcode

# Function to generate QR code
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)

# Example usage
data_to_encode = input("Enter What You Want As QR Code:")
output_filename = input("Name Your File name(example.png):")
generate_qr_code(data_to_encode, output_filename)
print(f"QR Code generated and saved as {output_filename}")
