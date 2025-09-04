import qrcode
print()
print('Welcome to the QR code generator!')
print()
print('You can enter any data to generate a QR code this data can be a link, text, image etc.')
print()
user_input = input("Enter the data to encode in the QR code : ").title().strip()

data_img = qrcode.make(user_input)
print()
image_save = input('what is the name of the file you want to save the QR code as (with .png extension) : ').replace(' ', '_').strip()
print()

data_img.save(f"{image_save}.png")
print()

print(f"QR code generated and saved as {image_save}")