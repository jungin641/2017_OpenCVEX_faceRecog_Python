FaceRecognition for KETI with openCV, python
===================

- 전자부품연구원 콘텐츠응용연구센터 유정인 첫번째 개발 과제
- **openCV**와 **python**을 활용한 **얼굴 인식(Recognition)** 프로그램

----------
	
#### <i class="icon-file"></i> 프로그램 개요
>- 기능 : 웹캠에서 인식한 얼굴들을 id 로 분류하여 저장하고, 그것을 바탕으로 누구의 얼굴인지 판별해주는 프로그램
>- 개발 기간 : 2017.03.07 ~ 2017. 03.17
>- 개발 언어 및 환경 : [python2.7.6](https://www.python.org/download/releases/2.7.6/)
>- 사용 IDE : [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)
>- 해당 툴과 언어 사용 이전에 C++ / openCV 를 사용하여 개발을 진행하였으나, C++ / openCV를 사용한 자료들은 4~5년 전이 최신이기 때문에 운영체제 버전 등의 여러가지 요인으로 인해 실행이 안 되는 문제 발생
>- 그 대안으로 python은 최근 4~5년 내에 그 사용이 급증하여 왠만한 얼굴 인식 프로그램은 python을 사용하는 추세를 보임,  os독립적으로 어디서든 호환성이 뛰어나며 추후 확장성이 더 뛰어날것이라고 판단하여 python을 사용하는 것으로 개발 방향을 수정.

#### <i class="icon-file"></i> 사용 모듈
> - [cv2](https://github.com/opencv/opencv/blob/master/modules/python/src2/cv2.cpp) (python에서 [openCV](http://opencv.org/)를 사용하기 위해 쓰는 모듈)
> - [tkinter](https://docs.python.org/2/library/tkinter.html)(python interface to Tck/Tk)
> - [PIL](http://www.pythonware.com/products/pil/) (python Imaging Library)
>


#### <i class="icon-file"></i> 얼굴 인식 과정

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

실행 파일 링크 : https://goo.gl/UYMrxe

참고 링크 : http://thecodacus.com/opencv-face-recognition-python-part1/#.WMoeAjuLTRY