#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void stringToMorse(const char *str, char *morse, size_t morseSize) {
    const char *morseCode[] = {
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", 
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", 
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    };
    while (*str) {
        if (*str >= 'a' && *str <= 'z') {
            strncat(morse, morseCode[*str - 'a'], morseSize - strlen(morse) - 1);
        } else if (*str >= 'A' && *str <= 'Z') {
            strncat(morse, morseCode[*str - 'A'], morseSize - strlen(morse) - 1);
        } else if (*str == ' ') {
            strncat(morse, " / ", morseSize - strlen(morse) - 1);
        }
        strncat(morse, " ", morseSize - strlen(morse) - 1);
        str++;
    }
}

int main(void) {
    FILE *file = fopen("input.txt", "r");
    if (file == NULL) {
        perror("Failed to open file");
        return 1;
    }

    char line[256];
    char morse[2048] = "";  // Increase size for larger output

    while (fgets(line, sizeof(line), file)) {
        stringToMorse(line, morse, sizeof(morse));
    }

    fclose(file);

    // Remove trailing space
    size_t len = strlen(morse);
    if (len > 0 && morse[len - 1] == ' ') {
        morse[len - 1] = '\0';
    }

    printf("Morse Code: %s\n", morse);

    return 0;
}
