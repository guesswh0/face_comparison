# Face comparison micro-service

## Installation

#### Requirements

* Python 3.6+

#### Clone

    git clone https://github.com/guesswh0/compare_faces.git
    
#### Install dependencies
    pip3 install -r requirements.txt
    
#### Development server

    flask run

#### Deployment

To _deploy_ see flask [deployment options](https://flask.palletsprojects.com/en/1.1.x/deploying/)  


##
 **Sample Call:**
  ```
    curl -X POST [host:port]/api/faces/compare \
        -F source=@face_image1.jpg \
        -F target=@face_image2.jpg
  ```