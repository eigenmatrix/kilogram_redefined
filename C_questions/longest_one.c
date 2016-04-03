/*
 * This program finds the longest string of 1s with
 * two inclusive 0s
 */
#include <stdlib.h>
int longest_one (char *input, int size)
{
  int *zeros, *zero_start;
  int i, zero_count, left, right;
  int max_len, max_pos;

  zeros = (int*) malloc(sizeof(*zeros) * size);
  zero_start = zeros;
  for (i = 0; i < size; i++) {
    if (input[i] == 0) {
      *zeros = i;
      zeros++;
      zero_count++;
    }
  }
  zeros = zero_start;
  if (zero_count <= 2) {
    //Too few zeros
    return (size);
  }

  //Start at the third zero.
  max_len = 0;
  max_pos = 0;
  if (zeros[2]) {
    max_len = zeros[2];
  }

  for (i = 3; i < zero_count; i++) {
    int len;
    right = zeros[i];
    left = zeros[i-3];

    len = (right) - (left);
    if (len > max_len) {
      max_len = len - 1;
      max_pos = i - 3;
    }
  }
  printf("longest start is %d\n", max_pos);
  return (max_len);
}

int main()
{
  int size;
  char data[] = {0,0,1,1,0,1,0,1,1,1,1,0,1,1,1,0,0};

  size = sizeof(data);
  printf("longest is %d", longest_one(data,size));
  return 0;
}