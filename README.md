# Face comparison micro-service

## Installation

#### Clone

    $ git clone https://github.com/guesswh0/face_comparison.git
    
#### Install dependencies

    $ pip3 install -r requirements.txt
    
#### Set up models

To use default models:
1. Install dlib (requires cmake): `$ pip install dlib`
2. Fetch model pre-trained files: `$ fetch_models`

To use custom models, configure `.env`.
        
    
#### Development server

    flask run

#### Deployment

To _deploy_ see flask [deployment options](https://flask.palletsprojects.com/en/1.1.x/deploying/)  


##
 **Sample Call:**
  ```
    curl -X POST [host:port]/api/compare_faces \
        -F source=@face_image1.jpg \
        -F target=@face_image2.jpg
  ```