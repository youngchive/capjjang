# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import os
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
from numba.pycc import export

# 이미지 폴더 경로 설정
image_folder_path = "image224/a"  # 스펙트로그램 이미지가 있는 폴더 경로 지정

# 폴더 내의 모든 이미지 파일 로드
for file_name in os.listdir(image_folder_path):
    if file_name.endswith(".png") or file_name.endswith(".jpg"):  # 이미지 파일 확장자에 따라 수정
        image_file_path = os.path.join(image_folder_path, file_name)
        spec_image = plt.imread(image_file_path)

        # 스펙트로그램 이미지에 랜덤 마스킹 적용
        masked_spec_image = np.copy(spec_image)
        mask = np.random.rand(*spec_image.shape) < 0.5  # 50%의 확률로 픽셀을 마스킹
        masked_spec_image[mask] = 0  # 마스킹된 픽셀을 0으로 설정

        # 마스킹된 이미지 로컬에 적용
        # 이미지 처리 코드 추가
        # 예시로 matplotlib를 사용하여 이미지를 로컬에 저장하는 코드를 추가합니다.
        masked_image_file_path = os.path.join(image_folder_path, "masked_" + file_name)  # 저장할 이미지 파일 경로 지정
        plt.imsave(masked_image_file_path, masked_spec_image)

        # 이미지 처리 작업 예시: 마스킹된 이미지를 화면에 출력
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(spec_image)
        plt.title("Original Spectrogram")
        plt.subplot(1, 2, 2)
        plt.imshow(masked_spec_image)
        plt.title("Masked Spectrogram")
        plt.show()
        #file_handle = export(masked_spec_image, format='jpg')