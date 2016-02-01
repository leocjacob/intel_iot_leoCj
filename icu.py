import argparse
import base64
import httplib2
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
API_DISCOVERY_FILE = 'v_d_f.json'
def main(photo_file):
  credentials = GoogleCredentials.get_application_default()
  with open(API_DISCOVERY_FILE, 'r') as f:
    doc = f.read()
  service = discovery.build_from_document(doc, credentials=credentials, http=httplib2.Http())

  with open(photo_file, 'rb') as image:
    image_content = base64.b64encode(image.read())
    service_request = service.images().annotate(
      body={
        'requests': [{
          'image': {
            'content': image_content
           },
          'features': [{
            'type': 'LABEL_DETECTION',
            'maxResults': 1,
           }]
         }]
      })
    response = service_request.execute()
    label = response['responses'][0]['labelAnnotations'][0]['description']
    print('Found label: %s for %s' % (label, photo_file))
    return 0

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('image_file', help='The image you\'d like to label.')
  args = parser.parse_args()
  main(args.image_file)
