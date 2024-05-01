# import cv2
# import numpy as np
# import cv2_imshow

# # Open the video file
# video_capture = cv2.VideoCapture('/content/2024-04-23 22-18-40.mkv')

# # Get the frames per second (fps), width, and height of the video
# fps = video_capture.get(cv2.CAP_PROP_FPS)
# width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Create VideoWriter object to save the modulated video
# output_video = cv2.VideoWriter('pcm_modulated_video.mp4',
#                                cv2.VideoWriter_fourcc(*'mp4v'),
#                                fps, (width, height))

# # Define the number of quantization levels (bit depth)
# num_levels = 8  # Example: 8-bit depth (256 levels)

# while True:
#     # Read a frame from the video
#     ret, frame = video_capture.read()

#     # Break the loop if there are no more frames
#     if not ret:
#         break

#     # Convert the frame to grayscale
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Perform PCM modulation
#     quantized_frame = np.round(gray_frame / 255 * (2 ** num_levels - 1)) * (255 / (2 ** num_levels - 1))
#     quantized_frame = quantized_frame.astype(np.uint8)

#     # Write the modulated frame to the output video
#     output_video.write(cv2.cvtColor(quantized_frame, cv2.COLOR_GRAY2BGR))


#     cv2_imshow(quantized_frame)


#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# video_capture.release()
# output_video.release()
import cv2
import numpy as np

# Open the video file
video_capture = cv2.VideoCapture('carPark.mp4')

# Get the frames per second (fps), width, and height of the video
fps = video_capture.get(cv2.CAP_PROP_FPS)
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create VideoWriter object to save the modulated video
output_video = cv2.VideoWriter('pcm_modulated_video.mp4',
                               cv2.VideoWriter_fourcc(*'mp4v'),
                               fps, (width, height))

# Define the number of quantization levels (bit depth)
num_levels = 8  # Example: 8-bit depth (256 levels)

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()

    # Break the loop if there are no more frames
    if not ret:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform PCM modulation
    quantized_frame = np.round(gray_frame / 255 * (2 ** num_levels - 1)) * (255 / (2 ** num_levels - 1))
    quantized_frame = quantized_frame.astype(np.uint8)

    # Write the modulated frame to the output video
    output_video.write(cv2.cvtColor(quantized_frame, cv2.COLOR_GRAY2BGR))

    # Display the quantized frame (optional)
    cv2.imshow('Quantized Frame', quantized_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and writer objects
video_capture.release()
output_video.release()
# Close all OpenCV windows
cv2.destroyAllWindows()
