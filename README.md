FaceRecognition for KETI with openCV, python
===================

- 전자부품연구원 콘텐츠응용연구센터 첫번째 개발 과제
- **openCV**와 **python**을 활용한 **얼굴 인식(Recognition)** 프로그램

----------


#### <i class="icon-file"></i> 사용 라이브러리
> - [openCV](http://opencv.org/)
> - [tkinter](https://docs.python.org/2/library/tkinter.html)(python interface to Tck/Tk)
> - [PIL](http://www.pythonware.com/products/pil/) (Python Imaging Library)
>


#### <i class="icon-file"></i> 얼굴 인식 과정
![enter image description here](https://raw.githubusercontent.com/cmusatyalab/openface/master/images/summary.jpg)
 >1. DataSet 만들기 
 >2. 만들어진 Data들을 재료로 trainging 시키기(TrainingData.yml)
 >3. detect하기 == 얼굴 인식!


#### <i class="icon-file"></i>FaceRecog 동작 방식
> **func dataSetCreate()** 
>- 웹캠의 화면을 읽어와서 화면 안에서 인식되는 얼굴들을 얼굴부분만 잘라 이미지형태로 저장한다.
> 
> 
>**func training()** 
>-  저장된 이미지 파일들을 userID가 같은 것들끼리 그룹화하여 trainingData.yml이라는 파일로 저장해둔다.
>
> **func detect()** 
>-  trainingData.yml에 저장된 정보들을 바탕으로 recognizer는 인식한 얼굴이 누구의 얼굴인지 predict하여 나타내준다. 
>
