from stegano import lsb

input_image = "test_base.png"
output_image = "test_encoded.png"
ip_to_hide = "45.141.215.21"

lsb.hide(input_image, ip_to_hide).save(output_image)
print(f"✅ IP wurde eingebettet in: {output_image}")
