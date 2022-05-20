from stegano import exifHeader

result = exifHeader.reveal("img/2_secret.jpg")
result = result.decode()
print(result)
