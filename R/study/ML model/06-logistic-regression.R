# R 내장 데이터셋 'mtcars'를 사용
data(mtcars)

# 32종의 자동차에 대한 속성을 포함하는 데이터
# 자동차의 연비와 성능관련정보를 담고 있고있음

# 데이터 확인
head(mtcars)

# 로지스틱 회귀 모델 생성
model <- glm(am ~ mpg + wt + hp, data = mtcars, family = binomial) # family = binomial은 로지스틱 회귀모델을 사용하겠다는 뜻

# 종속변수 : am (변속기 형태 : automatic = 0 , manual = 1)
# 10개의 독립변수 중에서 3개만 가지고 로지스틱 회귀모델을 생성함
# 독립변수가 많으면 모델이 복잡도가 증가해지므로 복잡도를 높이지 않으려고 처음부터 독립변수의 갯수를 작게 넣음

# 독립변수 포함시켜서 모델 생성하는 방법
#  1. 처음부터 모든 독립변수를 다 넣고 모델을 만든 다음에 불필요한 변수 빼는 방식
#   => 단계적 제거(backward elimination)
#  2. 처음부터 조금씩 독립변수를 추가하면서 모델의 성능을 확인하며 추가하는 방식
#   => 단계적 추가(foreward selection)

# 모델 요약
summary(model)

# 모델 계수 해석
coef(model)

# 예측값 계산
predicted_probabilities <- predict(model, type = "response")

# 예측값 확인
head(predicted_probabilities)

# 예측값을 바탕으로 실제 클래스를 예측
predicted_classes <- ifelse(predicted_probabilities > 0.5, 1, 0)

# 혼동 행렬(confusion matrix) 계산
table(Predicted = predicted_classes, Actual = mtcars$am)

# 모델 성능 평가 (정확도 계산)
accuracy <- mean(predicted_classes == mtcars$am)
accuracy # 0.9375


# 모델의 성능 올리기
model2 <- glm(am ~ mpg + wt + hp + cyl + drat + vs + gear + carb, data = mtcars, family = binomial)

# knn의 k값을 지정하는 것과 같은 하이퍼 파라미터가 없음
# 독립변수의 갯수를 늘려서 성능을 높이는 방법을 사용함

# model2 예측값 계산
predicted_probabilities <- predict(model2, type = "response")

# model2 예측값 확인
head(predicted_probabilities)

# 예측값을 바탕으로 실제 클래스를 예측
predicted_classes <- ifelse(predicted_probabilities > 0.5, 1, 0)

# 혼동 행렬(confusion matrix) 계산
table(Predicted = predicted_classes, Actual = mtcars$am)

# 모델 성능 평가 (정확도 계산)
accuracy <- mean(predicted_classes == mtcars$am)
accuracy # 1
