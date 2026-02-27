import cv2


def removeHair(img_org, img_gray, kernel_size=5, threshold=10, radius=3):

    kernel = cv2.getStructuringElement(
        cv2.MORPH_CROSS,
        (kernel_size, kernel_size)
    )

    blackhat = cv2.morphologyEx(
        img_gray,
        cv2.MORPH_BLACKHAT,
        kernel
    )

    _, thresh = cv2.threshold(
        blackhat,
        threshold,
        255,
        cv2.THRESH_BINARY
    )

    img_out = cv2.inpaint(
        img_org,
        thresh,
        radius,
        cv2.INPAINT_TELEA
    )

    return blackhat, thresh, img_out