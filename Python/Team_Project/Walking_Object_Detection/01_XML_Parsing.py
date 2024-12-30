### Class만 추출하기

import xml.etree.ElementTree as ET
import os

# XML 파일 경로 설정
xml_file = 'C:\\Users\\boeun\\Downloads\\Bbox10.zip\\Bbox_0725'

# XML 파일 파싱 함수
def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # 각 라벨 정보 저장
    labels = []
    for label in root.findall(".//label"):
        labels.append(label.find("name").text)
    
    return labels

# 파싱 결과 출력
labels = parse_xml(xml_file)
print(labels)

### XML 파싱하기

import os
import xml.etree.ElementTree as ET

# 클래스 이름 목록
class_names = [
    'traffic_light_controller', 'power_controller', 'wheelchair', 'truck', 
    'tree_trunk', 'traffic_sign', 'traffic_light', 'table', 'stroller', 
    'stop', 'scooter', 'potted_plant', 'pole', 'person', 'parking_meter', 
    'movable_signage', 'motorcycle', 'kiosk', 'fire_hydrant', 'dog', 
    'chair', 'cat', 'carrier', 'car', 'bus', 'bollard', 'bicycle', 
    'bench', 'barricade'
]

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 모든 이미지 정보 가져오기
    images_data = []
    for image_elem in root.findall('image'):
        image_name = image_elem.get('name')
        image_width = int(image_elem.get('width'))
        image_height = int(image_elem.get('height'))

        # 바운딩 박스 정보 가져오기
        objects = []
        for box in image_elem.findall('box'):
            class_name = box.get('label')
            xtl = float(box.get('xtl'))
            ytl = float(box.get('ytl'))
            xbr = float(box.get('xbr'))
            ybr = float(box.get('ybr'))
            objects.append((class_name, xtl, ytl, xbr, ybr))
        
        images_data.append((image_name, image_width, image_height, objects))
    
    return images_data

def convert_to_yolo_format(objects, image_width, image_height):
    yolo_data = []
    for obj in objects:
        class_name, xtl, ytl, xbr, ybr = obj
        # 클래스 ID 가져오기
        class_id = class_names.index(class_name)
        
        # 바운딩 박스를 정규화
        center_x = (xtl + xbr) / 2 / image_width
        center_y = (ytl + ybr) / 2 / image_height
        width = (xbr - xtl) / image_width
        height = (ybr - ytl) / image_height
        
        yolo_data.append(f"{class_id} {center_x} {center_y} {width} {height}")
    
    return yolo_data

def save_yolo_format(yolo_data, output_dir, image_name):
    output_file = os.path.join(output_dir, image_name.replace('.jpg', '.txt'))
    with open(output_file, 'w') as f:
        for line in yolo_data:
            f.write(line + '\n')

def convert_voc_to_yolo(xml_file, output_dir):
    images_data = parse_xml(xml_file)

    for image_name, image_width, image_height, objects in images_data:
        # YOLO 형식으로 변환
        yolo_data = convert_to_yolo_format(objects, image_width, image_height)
        
        # YOLO 형식 저장
        save_yolo_format(yolo_data, output_dir, image_name)

# XML 파일 경로와 출력 디렉토리 설정
xml_file = 'C:\\data\\bbox\\bbox_sample.xml'  # XML 파일 경로 수정
output_dir = "C:\\data\\bbox"     # 출력 디렉토리 수정

# 변환 실행
convert_voc_to_yolo(xml_file, output_dir)

### classes.txt 파일 생성 코드

import os

# 클래스 이름 목록
class_names = [
    'traffic_light_controller', 'power_controller', 'wheelchair', 'truck', 
    'tree_trunk', 'traffic_sign', 'traffic_light', 'table', 'stroller', 
    'stop', 'scooter', 'potted_plant', 'pole', 'person', 'parking_meter', 
    'movable_signage', 'motorcycle', 'kiosk', 'fire_hydrant', 'dog', 
    'chair', 'cat', 'carrier', 'car', 'bus', 'bollard', 'bicycle', 
    'bench', 'barricade', 'kickboard', 'red', 'green', 'crosswalk'
]

def save_class_mapping(output_dir):
    class_mapping_file = os.path.join(output_dir, "classes.txt")
    with open(class_mapping_file, "w") as f:
        for class_id, class_name in enumerate(class_names):
            f.write(f"{class_id} {class_name}\n")
    print("classes.txt 파일 생성 완료!")

# 출력 디렉토리 설정
output_dir = "C:\\data\\bbox"  # 출력 디렉토리 수정

# classes.txt 파일 생성
save_class_mapping(output_dir)

### XML 파싱 및 YOLO 형식으로 변환

import xml.etree.ElementTree as ET

# 클래스 이름을 ID로 매핑하는 함수
def create_class_id_mapping(classes):
    return {class_name: idx for idx, class_name in enumerate(classes)}

# XML 파싱 및 YOLO 형식 변환 함수
def parse_and_convert_to_yolo(xml_file, output_dir):
    # XML 파일 파싱
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # 모든 클래스 이름을 추출하여 ID 매핑 생성
    classes = set()
    for image in root.findall("image"):
        for box in image.findall("box"):
            label = box.attrib.get("label")
            if label:
                classes.add(label)
    class_id_mapping = create_class_id_mapping(classes)
    
    # 각 이미지에 대해 YOLO 형식으로 변환하여 텍스트 파일로 저장
    for image in root.findall("image"):
        image_name = image.attrib["name"]
        width = int(image.attrib["width"])
        height = int(image.attrib["height"])
        
        # YOLO 형식의 텍스트 파일명
        yolo_txt_file = f"{output_dir}/{image_name.split('.')[0]}.txt"
        
        with open(yolo_txt_file, "w") as f:
            for box in image.findall("box"):
                label = box.attrib.get("label")
                xtl = float(box.attrib.get("xtl"))
                ytl = float(box.attrib.get("ytl"))
                xbr = float(box.attrib.get("xbr"))
                ybr = float(box.attrib.get("ybr"))
                
                # 클래스 ID 가져오기
                class_id = class_id_mapping[label]
                
                # 중심 좌표와 폭, 높이 계산 후 정규화
                x_center = ((xtl + xbr) / 2) / width
                y_center = ((ytl + ybr) / 2) / height
                bbox_width = (xbr - xtl) / width
                bbox_height = (ybr - ytl) / height
                
                # YOLO 형식으로 파일에 쓰기
                f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n")
    
    # 클래스 ID 매핑 저장
    class_mapping_file = f"{output_dir}/classes.txt"
    with open(class_mapping_file, "w") as f:
        for class_name, class_id in class_id_mapping.items():
            f.write(f"{class_id} {class_name}\n")

    print("YOLO 형식 파일 생성 완료!")

# XML 파일 경로와 YOLO 텍스트 파일을 저장할 디렉토리 경로 지정
xml_path = "C:\\deeplearing_project\\bbox_sample.xml"
output_dir = "C:\\deeplearing_project\\yolo_labels"

# 변환 실행
parse_and_convert_to_yolo(xml_path, output_dir)
