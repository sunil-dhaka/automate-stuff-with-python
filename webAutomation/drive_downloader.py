# https://stackoverflow.com/questions/38511444/python-download-files-from-google-drive-using-url
import requests
from tqdm import tqdm

def download_file_from_google_drive(id):

    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    # very specific
    name=response.headers['Content-Disposition'].split(';')[1].split('=')[1].strip('"')

    total_size=int(response.headers.get('Content-Length'))
    # print(response.headers)
    inital_pos=0
    with open(name,'ab') as f:
        with tqdm(total=total_size,unit_scale=True,unit='B',desc=name,initial=inital_pos,ascii=True) as progress_bar:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)	
                    progress_bar.update(len(chunk))	


if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 2:
        print("Usage: python google_drive.py drive_file_id")
    else:
        file_id = sys.argv[1]

download_file_from_google_drive(file_id)
