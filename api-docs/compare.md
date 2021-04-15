**Face Comparison**
----
  Returns json

* **URL**

  /api/compare_faces

* **Method:**

  `POST`

* **Data Params**

  `source = *.jpg|jpeg|png`<br/>
  `target = *.jpg|jpeg|png`<br/>

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
    `{
        "FaceMatches": bool,
        "Similarity": float[0, 100] 
    }`
 
* **Error Responses:**
    
  * **Condition:** if '__source__' or  '__target__' not in request files<br />
  * **Code:** 404 <br />
    **Content:** 
    `{
        "error": "bad request", 
        "message": "no source|target file"
    }`

  * **Condition:** if '__source__' or  '__target__' image file extension is not supported <br/>
  * **Code:** 415 <br />
    **Content:** 
    `{
        "error": "unsupported media type",
        "message": "'source|target' image file type is not supported"
    }`
  
  * **Condition:** if there is no face in '__source__' or  '__target__' image<br/>
  * **Code:** 422 <br />
    **Content:** 
    `{
        "error": "unprocessable entity",
        "message": "Face not found"
    }`
    
* **Sample Call:**

```bash
curl -X POST [host:port]/api/compare_faces 
    -F source=@face_image1.jpg 
    -F target=@face_image2.jpg
```