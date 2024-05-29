# QR Code Utility

The QR Code Utility is a command-line tool for generating and decoding QR codes. It provides functionalities for creating QR codes from text data/file, decoding QR codes from images, and scanning QR codes using a webcam.






## Installation

clone/download qrutility and run/test/update on your local machine.

```cmd
  git clone https://github.com/h4jack/qrutil.git qrutil
  cd ./qrutil
  pip install -r requirements.txt
```
## Running Tests

To run tests, run the following command

```cmd
PS C:\qrutil> py .\main.py generate -q "This is test 
>> And this is Line 2." -f test
QR Code Generated.
Saved as test.png
Program End.
```
## Features

- Generate QR codes from text data.
- Generate QR codes from text files.
- Decode QR codes from image files.
- Decode QR codes in real-time using a webcam.

## Usage/Examples


#### Generate QR-Code from a text file.
```cmd
PS C:\qrutil> py .\main.py generate -r test.txt -f test1.png
File Content:
This is a test file to encode the text into qr coede.
This is the second line to test if takes multiple line
QR Code Generated.
Saved as test1.png.png
Program End.
```

#### Decode QR-Code 
```cmd
PS C:\qrutil> py .\main.py decode -f .\test1.png    
QRCode data:
This is a test file to encode the text into qr coede.
This is the second line to test if takes multiple line
Program End.
PS S:\WorkSpace\Projects\QR-Code> 
```

#### Scan QR-Code using WebCam.
```cmd
PS C:\qrutil> py .\main.py webcam       
QR Code Scanner is opened look for new window.
Press CTRL-C to Exit.
Closed the QR Code Scanner..
Program End.
```
## Authors

- [@h4jack](https://www.github.com/h4jack)


## License

[MIT](https://github.com/h4jack/qrutil/blob/main/LICENSE/)


## Feedback

If you have any feedback, please reach out to us at ig: @0x07da