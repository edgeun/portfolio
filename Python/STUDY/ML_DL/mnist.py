# mnist 필기체 데이터 불러오기
from tensorflow.keras.datasets.mnist import load_data
( x_train, y_train ), ( x_test, y_test ) = load_data( 'mnist.npz' )

print(x_train.shape)  # (60000, 28, 28)

# 차원 축소하기
x_train = x_train.reshape((x_train.shape[0], -1))
x_test =  x_test.reshape((x_test.shape[0], -1) )  # 차원 축소 코드
print(x_train.shape)  # (60000, 784)

# 설명: 필기체 사진을 신경망에 넣으려면 다음과 같이 차원을 축소해야합니다.

# ( 60000, 28, 28 ) --> 차원 축소 코드 --> ( 60000, 784 ) 
# -1 이라고 쓰면 28x28 을 알아서 계산해서 784로 해주는것입니다.

# 신경망 구성에 필요한 모듈 불러오기
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential  # 신경망 모델 구성
from tensorflow.keras.layers import Dense       # 완전 연결 계층 
from tensorflow.keras.optimizers import SGD     # 경사감소법
from tensorflow.keras.losses import mse         # 오차 함수

# 모델 생성하기
model = Sequential()

# 층 구성하기(2층 신경망)
model.add( Dense( 10, input_shape=( 784,  ),  activation='sigmoid') )  # 은닉층
model.add( Dense( 10, activation='softmax') )  # 출력층 

# 모델 학습 방법 지정하기
model.compile( optimizer=SGD(),  # 경사하강법
               loss= 'sparse_categorical_crossentropy',  # 오차함수
               metrics=['acc'] )  # 정확도를 높이는 방법으로 학습 시키겠다.

# 학습 시키기
model.fit( x_train, y_train, batch_size=100, epochs=200 )

# 테스트 데이터 예측하기
test_loss, test_acc = model.evaluate( x_test, y_test )
print( test_acc )  # 0.8845999836921692

####

## 3층 신경망 구성
# 층 구성하기
model.add( Dense( 50, input_shape=( 784,  ),  activation='sigmoid') )  # 은닉1층
model.add( Dense( 100, activation='sigmoid') )  # 은닉2층
model.add( Dense( 10, activation='softmax') )   # 출력층 

# 모델 학습 방법 지정하기
model.compile( optimizer=SGD(),  # 경사하강법
               loss= 'sparse_categorical_crossentropy',  # 오차함수
               metrics=['acc'] )  # 정확도를 높이는 방법으로 학습 시키겠다.

# 학습 시키기
model.fit( x_train, y_train, batch_size=100, epochs=200 )

# 테스트 데이터 예측하기
test_loss, test_acc = model.evaluate( x_test, y_test )
print( test_acc )  # 0.9580000042915344

####
## 패션 데이터
from tensorflow.keras.datasets.fashion_mnist import load_data
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = load_data()

target_dict = {
 0: 'T-shirt/top',
 1: 'Trouser',
 2: 'Pullover',
 3: 'Dress',
 4: 'Coat',
 5: 'Sandal',
 6: 'Shirt',
 7: 'Sneaker',
 8: 'Bag',
 9: 'Ankle boot',
}

plt.figure(figsize=(10,10))

for i in range(0,20):
    plt.subplot(5,5, i+1)
    plt.imshow(x_train[i] )
    plt.title( target_dict[(y_train[i]) ])
    plt.xticks([])
    plt.yticks([])

# mnist 데이터를 불러오기
import tensorflow as tf
from tensorflow.keras.datasets.fashion_mnist import load_data

(x_train, y_train), (x_test, y_test) = load_data() 

# 28x28 의 shape 를 1 x 784 로 변경
x_train = x_train.reshape(60000, 28*28)
x_test  = x_test.reshape(10000, 28*28)

# min-max 정규화 진행
x_train = x_train/255.0
x_test = x_test/255.0

# 정답 데이터를 준비하기 (p98)
# 원 핫 인코딩을 하는 이유? 신경망에 정답 데이터를 넣어줄 땐 원 핫 인코딩을 거쳐야 됨
# 3 -> 원 핫 인코딩 -> [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ]
# 이런식으로 정답을 3에 해당되는 값만 1로 나머지는 0으로(원 핫 인코딩)
# 변경해서 신경망에 넣어줘야 됨
from tensorflow.keras.utils import to_categorical

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
print ( y_train.shape)  # (60000, 10)

# 모델 구성하기
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(784, ) ) ) # 은닉1층
model.add(Dense(128, activation='relu' ) ) # 은닉1층
model.add(Dense( 10, activation='softmax') ) 

# 모델 설정하기 (경사하강법과 오차 함수를 정의)
model.compile(optimizer='adam',  # 경사하강법 
              loss='categorical_crossentropy',  #오차 함수
              metrics=['acc'] )  # 학습과정에서 정확도를 보려고 지정

# 모델 훈련하기
model.fit( x_train, y_train, epochs=30, batch_size=100)

# model.fit( 훈련데이터, 정답, 에폭수, 배치사이즈 ) 
# 에폭수 : 학습 횟수 (책을 몇 번 볼건지)
# 배치사이즈 : 한번에 학습할 양 (사람은 책을 한 번에 한 페이지 밖에 못 보지만
# 컴퓨터는 한 번에 여러 페이지를 볼 수 있다)

# 모델 평가
model.evaluate(x_test, y_test)

# 생성한 모델 저장하기
model.save('fashion_model.h5')

####
## 위에서 저장한 모델 불러오기
from tensorflow.keras.models import load_model

new_model = load_model('fashion_model.h5')

# 모델 평가
new_model.evaluate(x_test, y_test)  # [0.3909059464931488, 0.8880000114440918]

## 새 이미지 파일로 테스트해보기
## 이미지 불러와서 전처리
# 모듈 불러오기
import tensorflow as tf
import cv2  # 이미지를 전문으로 전처리하는 모듈

# 이미지 경로 설정
img_path = '~\dress.jpg'

# 색 반전 시키는 코드
img = cv2.imread(img_path)  # 이미지 읽어서 숫자로 변환
img = cv2.bitwise_not(img)  # 색 반전시키는 코드 (흰 <-> 검 / 검 <-> 흰)
print(img.shape)  # (683, 427, 3) => 컬러 사진이라서 흑백 사진으로 변경해야 됨
                  # 흑백 사진을 학습한 신경망이기 때문에

# TensorFlow 2.X 버전으로 변경된 코드
# 이미지 크기를 28x28로 조정
resized_images = tf.image.resize( img, (28, 28) )

# RGB 이미지를 그레이스케일로 변환
a = tf.image.rgb_to_grayscale(resized_images)
print(a.shape)  # (28, 28, 1) => 흑백 사진(1채널)으로 변경 됨

## 전처리한 이미지 모델에 넣어보기
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# TensorFlow 2.X 즉시 실행 모드로 실행
# a 이미지를 [ 28,28 ]로 변환
x = tf.reshape( a, [ 28, 28 ] )

# 신경망에 넣기 좋도록 [ 1, 784 ]로 변환
x2 = tf.reshape( x, [ 1, 784 ] )

# NumPy 배열로 변환
x2 = x2.numpy()  # 즉시 실행 모드에서 사용 가능

# 모델 불러오기
new_model = load_model('c:\\data\\fashion_model.h5')

# 예측
results = new_model.predict(x2)
predicted_class = np.argmax(results)

print(predicted_class)  # 3: dress
