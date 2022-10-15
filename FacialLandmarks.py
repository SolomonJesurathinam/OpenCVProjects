'''import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
facemesh = mp_face_mesh.FaceMesh(max_num_faces=2)

image = cv2.imread("test.jpg")
imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = facemesh.process(imgRGB)

for face_landmarks in results.multi_face_landmarks:
    #print('face_landmarks:', face_landmarks)
    mp_draw.draw_landmarks(image=image,landmark_list=face_landmarks)

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


