from ultralytics import YOLO
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
from gtts import gTTS
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips
import tempfile
import os

# YOLOv8 모델 로드
model = YOLO("/Users/eden/Desktop/python/assistant/1108_finetuned.pt")  # 경로 구글 드라이브로 변경

# 입력 및 출력 동영상 경로 설정
input_video_path = "/Users/eden/Desktop/python/assistant/IMG_4111.MOV"  # 경로 구글 드라이브로 변경
temp_video_path = "/Users/eden/Desktop/python/assistant/temp1112_b.mp4"  # 경로 구글 드라이브로 변경
output_video_path = "/Users/eden/Desktop/python/assistant/1112_boutput.mp4"  # 경로 구글 드라이브로 변경
# 임시 오디오 파일 경로 설정
temp_audio_path = "/Users/eden/Desktop/python/assistant/temp_audio_1112_b.mp4"  # 경로 구글 드라이브로 변경

# 세 개의 ROI 이미지 경로 설정
roi_paths = [
    "/Users/eden/Desktop/python/assistant/ROI/roi-right.png",  # 오른쪽 영역  # 경로 구글 드라이브로 변경
    "/Users/eden/Desktop/python/assistant/ROI/roi-left.png",   # 왼쪽 영역  # 경로 구글 드라이브로 변경
    "/Users/eden/Desktop/python/assistant/ROI/roi-center.png"  # 중앙 영역  # 경로 구글 드라이브로 변경
]

# 폰트 파일 경로 설정 (Pretendard 또는 다른 한글 지원 폰트)
font_path = "/Users/eden/Desktop/python/assistant/font/Pretendard-SemiBold.ttf"  # 경로 구글 드라이브로 변경
font_size = 38
font = ImageFont.truetype(font_path, font_size)

# 클래스 이름 한국어 번역 딕셔너리
class_translations = {  
    'traffic_light_controller': '신호 조절기', 
    'power_controller': '전기 조절기', 
    'wheelchair': '휠체어',
    'truck': '트럭', 
    'tree_trunk': '나무', 
    'traffic_sign': '교통 표지판', 
    'table': '테이블', 
    'stroller': '유모차', 
    'stop': '정지신호', 
    'scooter': '스쿠터', 
    'potted_plant': '화분', 
    'pole': '막대기둥', 
    'person': '사람', 
    'parking_meter': '주차장 미터기', 
    'movable_signage': '표지판', 
    'motorcycle': '오토바이',
    'kiosk': '키오스크', 
    'fire_hydrant': '소화기', 
    'dog': '강아지',
    'chair': '의자', 
    'cat': '고양이', 
    'carrier': '캐리어', 
    'car': '차', 
    'bus': '버스', 
    'bollard': '기둥', 
    'bicycle': '자전거', 
    'bench': '벤치', 
    'barricade': '바리케이드', 
    'kickboard': '킥보드', 
    'light': '신호등'
}

# 한글 종성 확인 함수
def get_particle(word, subject_particle="이", topic_particle="은"):
    if (ord(word[-1]) - 44032) % 28 != 0:
        return subject_particle, topic_particle  # 받침이 있는 경우
    else:
        return "가", "는"  # 받침이 없는 경우

# 음성 파일 생성 함수
def save_text_to_audio(text, lang='ko'):
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        tts.save(f.name)
        return f.name

# 자막 표시 함수
# 자막 표시 함수 (PIL을 사용하여 한글 표시)
def put_text_with_background(frame, text):
    img_pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(img_pil)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    margin = 10
    # 텍스트 배경 박스 그리기
    box_x_start = (frame.shape[1] - text_width) // 2 - margin
    box_x_end = (frame.shape[1] + text_width) // 2 + margin
    box_y_start = frame.shape[0] - text_height - 50 - margin
    box_y_end = frame.shape[0] - 50 + margin
    draw.rectangle([(box_x_start, box_y_start), (box_x_end, box_y_end)], fill=(0, 0, 0, 200))
    text_position = ((frame.shape[1] - text_width) // 2, box_y_start + margin)
    draw.text(text_position, text, font=font, fill=(255, 255, 255, 255))
    frame[:] = np.array(img_pil)

# 신호등 텍스트 
# 신호등 바운딩 박스 위에 텍스트를 표시하는 함수 정의
def put_text_on_traffic_light(frame, text, x, y):
    img_pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(img_pil)
    # font = ImageFont.truetype("arial.ttf", 20)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    margin = 5
    # 텍스트 배경 박스 그리기
    box_x_start = x - margin
    box_x_end = x + text_width + margin
    box_y_start = y - text_height - margin
    box_y_end = y + margin
    draw.rectangle([(box_x_start, box_y_start), (box_x_end, box_y_end)], fill=(0, 0, 0, 200))
    text_position = (x, y - text_height)
    draw.text(text_position, text, font=font, fill=(255, 255, 255, 255))
    frame[:] = np.array(img_pil)

# 자막과 음성을 위한 변수 초기화
last_text = None
last_text_frame_count = 0  # 프레임 카운트를 통해 자막 표시 시간 제어
center_audio_files = []  # 중앙(빨간) 영역의 음성 파일들
detection_status = {}
display_duration_frames = 60  # 자막을 60프레임 동안 유지
# audio_played = False  # 오디오가 이미 재생되었는지 확인하는 변수

# ROI 이미지 로드 및 오류 확인
rois = []
for path in roi_paths:
    roi_img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if roi_img is None:
        print(f"오류: '{path}' 파일을 불러올 수 없습니다. 경로를 확인하세요.")
        continue
    rois.append(roi_img)

if len(rois) != 3:
    print("필요한 ROI 이미지를 모두 불러오지 못했습니다. 경로를 확인 후 다시 시도하세요.")
else:
    cap = cv2.VideoCapture(input_video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(temp_video_path, fourcc, fps, (width, height))

    resized_rois = []
    for roi_img in rois:
        if roi_img.shape[:2] != (height, width):
            roi_img = cv2.resize(roi_img, (width, height))
        resized_rois.append(roi_img)

    colors = {
        "default": (0, 255, 0),  # 기본: 초록색
        "yellow": (0, 255, 255),  # 왼쪽 또는 오른쪽: 노란색
        "red": (0, 0, 255)  # 중앙: 빨간색
    }

    
    # 추가된 신호등 색상 탐지 함수
    def detect_traffic_light_color(frame, x1, y1, x2, y2):
        # 해당 영역을 잘라내어 색상 분석
        roi = frame[y1:y2, x1:x2]
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
        # 빨간불 범위 (HSV 색 공간에서)
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        
        # 초록불 범위 (HSV 색 공간에서)
        lower_green = np.array([35, 50, 70])
        upper_green = np.array([85, 255, 255])
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        
        # 빨간불과 초록불 비율 계산
        red_ratio = np.sum(mask_red) / (mask_red.shape[0] * mask_red.shape[1])
        green_ratio = np.sum(mask_green) / (mask_green.shape[0] * mask_green.shape[1])
        
        # 신호등 색상 판단
        if red_ratio > 0.5:
            return "red"  # 빨간불
        elif green_ratio > 0.5:
            return "green"  # 초록불
        else:
            return "none"  # 불확실한 상태
    
    frame_count = 0

# 오디오 재생 여부 확인을 위한 변수
audio_played = False  # 오디오가 이미 재생되었는지 확인하는 변수

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    # 각 ROI 이미지의 알파 채널을 사용하여 프레임에 추가
    for roi in resized_rois:
        if roi.shape[2] == 4:
            bgr = roi[:, :, :3]
            alpha = roi[:, :, 3] / 255.0
            combined_alpha = alpha * 0.2  # 투명도 설정 (20%)
            for c in range(3):
                frame[:, :, c] = (1 - combined_alpha) * frame[:, :, c] + combined_alpha * bgr[:, :, c]

    # 관심 영역 마스크 생성
    mask_right = cv2.inRange(resized_rois[0][:, :, :3], np.array([0, 255, 255]), np.array([0, 255, 255]))
    mask_left = cv2.inRange(resized_rois[1][:, :, :3], np.array([0, 255, 255]), np.array([0, 255, 255]))
    mask_center = cv2.inRange(resized_rois[2][:, :, :3], np.array([0, 0, 255]), np.array([0, 0, 255]))

    # 검출 정보 저장
    text_to_display = None
    detection_status.clear()

    # 객체 탐지 및 바운딩 박스 그리기
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        confidence = box.conf[0]
        if confidence >= 0.3:  # 신뢰도 필터 추가
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            translated_class = class_translations.get(class_name, class_name)

            # 신호등(29번 클래스) 색상 탐지 추가
            if class_id == 29:  
                light_color = detect_traffic_light_color(frame, x1, y1, x2, y2)

                if light_color == "red":
                    color = (0, 0, 255)  # 빨간색
                    detection_status[translated_class] = ("건너지마세요", "light")

                    # 신호등이 빨간색일 경우 "건너지마세요" 음성 출력
                    if not audio_played:  # 오디오가 재생되지 않았다면
                        audio_path = save_text_to_audio("건너지마세요")  # 음성 생성
                        center_audio_files.append(audio_path)  # 빨간 영역 음성 대기열에 추가
                        audio_played = True  # 오디오가 재생되었음을 표시

                elif light_color == "green":
                    color = (0, 255, 0)  # 초록색
                    detection_status[translated_class] = ("건너세요!", "light")

                    # 신호등이 초록색일 경우 "건너세요" 음성 출력
                    if audio_played:  # 이미 "건너지마세요" 음성이 출력된 경우
                        audio_played = False  # 오디오 재생 상태 리셋

                    if not audio_played:  # 오디오가 재생되지 않았다면
                        audio_path = save_text_to_audio("건너세요")  # 음성 생성
                        center_audio_files.append(audio_path)  # 초록 영역 음성 대기열에 추가
                        audio_played = True  # 오디오가 재생되었음을 표시

                else:
                    color = (0, 255, 0)  # 기본 초록색 (불확실한 경우)
                    detection_status[translated_class] = (f"{translated_class} 신호를 확인하세요.", "light")

                # 신호등에 대한 텍스트 표시 (confidence 표시 제외)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                put_text_on_traffic_light(frame, detection_status[translated_class][0], x1, y1)


            # 다른 객체들 처리 (사람, 자동차 등)
            else:
                detection_region = np.zeros_like(mask_right)
                detection_region[y1:y2, x1:x2] = 255
                center_overlap = cv2.bitwise_and(mask_center, detection_region)
                left_overlap = cv2.bitwise_and(mask_left, detection_region)
                right_overlap = cv2.bitwise_and(mask_right, detection_region)

                # 기본 색상
                color = colors["default"]
                subject_particle, _ = get_particle(translated_class)

                # 중앙(빨간색) 우선 처리
                if np.sum(center_overlap) / np.sum(mask_center) > 1/3:
                    color = colors["red"]
                    detection_status[translated_class] = (f"{translated_class}{subject_particle} 중앙 가까이에 있습니다.", "center")
                        
                elif np.sum(left_overlap) > 0 and np.sum(right_overlap) > 0:
                    color = colors["yellow"]
                    detection_status[translated_class] = (f"{translated_class}{subject_particle} 양쪽에 있습니다.", "side")
                elif np.sum(left_overlap) > 0:
                    color = colors["yellow"]
                    detection_status[translated_class] = (f"{translated_class}{subject_particle} 왼쪽에 있습니다.", "side")
                elif np.sum(right_overlap) > 0:
                    color = colors["yellow"]
                    detection_status[translated_class] = (f"{translated_class}{subject_particle} 오른쪽에 있습니다.", "side")

                # 바운딩 박스와 클래스 이름 표시
                label = f"{class_name} {confidence:.2f}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # 자막 및 음성 설정
    prioritized_status = sorted(detection_status.values(), key=lambda x: x[1] == "center", reverse=True)
    text_to_display = " ".join([status[0] for status in prioritized_status])

    if text_to_display and text_to_display != last_text:
        last_text = text_to_display
        last_text_frame_count = frame_count  # 자막 표시 시작 프레임 기록
        put_text_with_background(frame, last_text)

        # 음성 파일 생성 및 저장
        for status_text, priority in prioritized_status:
            audio_path = save_text_to_audio(status_text)
            if priority == "center":
                center_audio_files.append(audio_path)  # 빨간 영역 음성 대기열에 추가

    # 자막 유지: 설정된 프레임 수 동안 유지하고 이후에 제거
    if last_text and (frame_count - last_text_frame_count < display_duration_frames):
        put_text_with_background(frame, last_text)
    elif frame_count - last_text_frame_count >= display_duration_frames:
        last_text = None  # 자막 제거

    # 동영상 출력
    out.write(frame)
    frame_count += 1


cap.release()
out.release()

# 음성 파일 경로 리스트를 AudioFileClip 객체로 변환
center_audio_clips = [AudioFileClip(file) for file in center_audio_files]

# 모든 오디오 클립 결합
final_audio = concatenate_audioclips(center_audio_clips)

# 결합된 오디오의 길이 확인
print(f"결합된 오디오 길이: {final_audio.duration}초")

# final_audio가 None이 아니고 duration이 유효한지 확인
if final_audio.duration is not None:
    # 비디오 길이에 맞추기
    video_clip = VideoFileClip(temp_video_path)

    # 오디오 길이가 비디오 길이에 맞지 않으면 잘라내기
    if final_audio.duration > video_clip.duration:
        final_audio = final_audio.subclip(0, video_clip.duration)

    # 비디오에 오디오 설정
    final_video = video_clip.set_audio(final_audio)

    # 최종 비디오 파일 저장
    final_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
else:
    print("오디오의 길이가 유효하지 않습니다. 확인해주세요.")

# 임시 파일 삭제
os.remove(temp_video_path)
for file in center_audio_files:
    os.remove(file)
