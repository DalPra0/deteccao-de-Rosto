import cv2
import os

output_folder = 'dataset'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cap = cv2.VideoCapture(0)

image_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame")
        break

    cv2.imshow('Capturando Imagens - Pressione s para salvar, q para sair', frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        image_count += 1
        image_path = os.path.join(output_folder, f'imagem_{image_count}.jpg')
        cv2.imwrite(image_path, frame)
        print(f"Imagem salva: {image_path}")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
