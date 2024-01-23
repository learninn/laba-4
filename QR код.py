data = "слыш 200 рублей где?"
import qrcode
qr = qrcode.make(data)
qr.save('qrcode.png')