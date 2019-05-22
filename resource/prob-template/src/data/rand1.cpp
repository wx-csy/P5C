#include <bits/stdc++.h>
using namespace std;

long long seed;
int n;

int main(int argc, char *argv[]) {
  seed = atoll(argv[1]);
  n = atoi(argv[2]);
  mt19937 gen(seed);
  printf("%d\n", n);
  while (n--) {
    printf("%d %d\n", int(gen() % 1000000), int(gen() % 1000000));
  }
  return 0;
}
