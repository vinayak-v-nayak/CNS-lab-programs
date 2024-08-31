import ftplib
import os

def ftp_client():
    # Get user input for server, username, and password
    server = input("Enter FTP server: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(server)
        ftp.login(user=username, passwd=password)
        print(f"Connected to {server}")

        # List directory contents
        print("Directory list:")
        ftp.retrlines('LIST')

        # Upload a file
        def upload_file():
            file_path = input("Enter the path of the file to upload: ")
            file_name = os.path.basename(file_path)
            with open(file_path, 'rb') as file:
                ftp.storbinary(f'STOR {file_name}', file)
            print(f"Uploaded {file_name}")

        # Download a file
        def download_file():
            file_name = input("Enter the name of the file to download: ")
            local_path = input("Enter the local path to save the file: ")
            with open(local_path + '/' + file_name, 'wb') as file:
                ftp.retrbinary('RETR ' + file_name, file.write)
            print(f"Downloaded {file_name} to {local_path}")

        while True:
            print("\nOptions:")
            print("1. List directory")
            print("2. Upload file")
            print("3. Download file")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                print("Directory list:")
                ftp.retrlines('LIST')
            elif choice == '2':
                upload_file()
            elif choice == '3':
                download_file()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

        # Close the connection
        ftp.quit()
        print("Disconnected from server")

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

if __name__ == "__main__":
    ftp_client()
