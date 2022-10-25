#define WINVER 0x0500
#include <windows.h>

int main()
{
    // This structure will be used to create the keyboard
    // input event.
    // windows key- ip, printscreen - ip1
    INPUT ip;
    INPUT ip1;

    // Set up a generic keyboard event for windows key
    ip.type = INPUT_KEYBOARD;
    ip.ki.wScan = 0; // hardware scan code for key
    ip.ki.time = 0;
    ip.ki.dwExtraInfo = 0;

    // Set up a generic keyboard event for printscreen key
    ip1.type = INPUT_KEYBOARD;
    ip1.ki.wScan = 0; // hardware scan code for key
    ip1.ki.time = 0;
    ip1.ki.dwExtraInfo = 0;


    // Press the windows key
    ip.ki.wVk = 0x5B; // virtual-key code for the "a" key
    ip.ki.dwFlags = 0; // 0 for key press
    SendInput(1, &ip, sizeof(INPUT));


    // press the print screen key
    ip1.ki.wVk = 0x2C; // virtual-key code for the "a" key
    ip1.ki.dwFlags = 0; // 0 for key press
    SendInput(1, &ip1, sizeof(INPUT));

    // Release the printscreen key
    ip1.ki.dwFlags = KEYEVENTF_KEYUP; // KEYEVENTF_KEYUP for key release
    SendInput(1, &ip1, sizeof(INPUT));

    // Release the windows key
    ip.ki.dwFlags = KEYEVENTF_KEYUP; // KEYEVENTF_KEYUP for key release
    SendInput(1, &ip, sizeof(INPUT));

    // Exit normally
    return 0;
}