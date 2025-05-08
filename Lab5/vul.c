#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void start_level() {
  char buffer[64];
  gets(buffer);
}

int main(int argc, char **argv)
{
    start_level();
}