import argparse
import qrcode
import cv2

MAX_QR_DATA_LENGTH = 1000

MAX_QR_DATA_LENGTH = 1000

def encodeQr(qrdata, qrfilename):
    if len(qrdata) > MAX_QR_DATA_LENGTH:
        print(f"QR data length exceeds the maximum limit of {MAX_QR_DATA_LENGTH} characters. Only the first {MAX_QR_DATA_LENGTH} characters will be encoded.")
        qrdata = qrdata[:MAX_QR_DATA_LENGTH]
    qrimg = qrcode.make(qrdata)
    qrimg.save(f"{qrfilename}.png")
    print("QR Code Generated.")
    print(f"Saved as {qrfilename}.png")

def readAndEncodeFile(filename, qrfilename):
    try:
        with open(filename, 'rb') as file:  # Open file in binary mode
            # Read the first few bytes to detect the encoding
            data = file.read(4)
            file_encoding = None
            
            if data.startswith(b'\xff\xfe'):  # UTF-16 little endian BOM
                file_encoding = 'utf-16'
            elif data.startswith(b'\xfe\xff'):  # UTF-16 big endian BOM
                file_encoding = 'utf-16'
            elif data.startswith(b'\xef\xbb\xbf'):  # UTF-8 BOM
                file_encoding = 'utf-8'

            # Reset file pointer to beginning
            file.seek(0)

            # Read file content using detected encoding
            if file_encoding:
                with open(filename, 'r', encoding=file_encoding) as f:
                    qrdata = f.read()
                    print("File Content:")
                    print(qrdata)
                    if len(qrdata) > MAX_QR_DATA_LENGTH:
                        print(f"File content length exceeds the maximum limit of {MAX_QR_DATA_LENGTH} characters. Only the first {MAX_QR_DATA_LENGTH} characters will be encoded.")
                        qrdata = qrdata[:MAX_QR_DATA_LENGTH]
                    encodeQr(qrdata, qrfilename)
            else:
                print("Unsupported encoding detected.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")




def wcamQrDecode():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Initialize the OpenCV QRCode detector
    detector = cv2.QRCodeDetector()

    try:
        while True:
            _, img = cap.read()

            # Detect and decode QR codes
            data, vertices_array, _ = detector.detectAndDecode(img)

            # Check if there is a QR code in the image
            if vertices_array is not None:
                if data:
                    print("QR Code detected, data:", data)

            # Display the result
            cv2.imshow("Webcam QR Code Detection", img)

            # Wait for a key press (with a delay of 1 millisecond)
            key = cv2.waitKey(1)

            # Press 'q' to quit
            if key == ord("q"):
                break

    except KeyboardInterrupt:
        # Handle CTRL-C (keyboard interrupt)
        print("Closed the QR Code Scanner..")

    finally:
        # Release the camera and close the OpenCV window
        cap.release()
        cv2.destroyAllWindows()

def decodeQr(qrfilename):
    image = cv2.imread(qrfilename)
    detector = cv2.QRCodeDetector()
    try:
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    except:
        print("Error Detected. (Not Exist/Unsupported File format).")
        return
    if vertices_array is not None:
        print("QRCode data:")
        print(data)
    else:
        print("There was some error")

def main():
    parser = argparse.ArgumentParser(description='QR Code Generator and Decoder')
    subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands', dest='subcommand')

    # Generate QR Code
    parser_generate = subparsers.add_parser('generate', help='Generate QR Code')
    parser_generate.add_argument('-q', '--qrdata', type=str, help='QR data to encode')
    parser_generate.add_argument('-r', '--read-file', type=str, help='Read content from file and encode it to QR code')
    parser_generate.add_argument('-f', '--file', type=str, help='File name')

    # Decode QR Code
    parser_decode = subparsers.add_parser('decode', help='Decode QR Code')
    parser_decode.add_argument('-f', '--file', type=str, help='File name')

    # Webcam QR Code Decoder
    parser_webcam = subparsers.add_parser('webcam', help='Webcam QR Code Decoder')

    args = parser.parse_args()

    if args.subcommand == 'generate':
        if args.qrdata is None and args.read_file is None:
            args.qrdata = input("Enter the qr data: ")
        if args.file is None:
            args.file = input("Enter the file name: ")
        if args.read_file:
            readAndEncodeFile(args.read_file, args.file)
        else:
            encodeQr(args.qrdata, args.file)
    elif args.subcommand == 'decode':
        if args.file is None:
            args.file = input("Enter the file name: ")
        decodeQr(args.file)
    elif args.subcommand == 'webcam':
        print("QR Code Scanner is opened look for new window.")
        print("Press CTRL-C to Exit.")
        wcamQrDecode()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
    print("Program End.")
