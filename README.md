# Generalized Hand Gesture Recognition System

## Overview

This project presents a hand gesture recognition system designed for adaptability across various applications. Utilizing advanced machine learning, the system accurately interprets hand gestures for natural and efficient user interaction. Optimized for edge-based inference, it ensures real-time responsiveness suitable for applications like video conferencing, sign language communication, and smart home control. This system aims to advance human-computer interaction and promote inclusivity.

## Applications

### 1. Video Conference and Communication Systems
Integrates gesture-based controls into video conferencing, enabling natural navigation and expressive communication in remote collaboration environments.

### 2. American Sign Language (ASL) Communication
Translates hand gestures into spoken words, facilitating communication for individuals who are deaf or hard of hearing, promoting inclusivity in diverse settings.

### 3. Media Control
Enables intuitive hand gesture control over media playback, enhancing user experience in entertainment, presentations, and smart home environments.

## Running the Applications

To launch the unified application interface, execute:
python app.py


### Video Conference and Communication Systems
To run the video conference application:
python gesture_detection.py


### American Sign Language (ASL) Communication
To run the sign language communication application:
python sign_language.py


To train the ASL alphabet model:
1. Collect alphabet images:
    ```
    python collect_imgs.py
    ```
2. Create dataset:
    ```
    python create_dataset.py
    ```
3. Train classifier:
    ```
    python train_classifer.py
    ```
4. Utilize trained model:
    ```
    model.p
    ```

### Media Control
To run the media control application:
python media_control.py


## Project Resources

- **Project Presentation:** [Presentation.pdf](Presentation.pdf)
