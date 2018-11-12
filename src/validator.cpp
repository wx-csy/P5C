#include "testlib.h"
using namespace std;

int main(int argc, char* argv[]) {
  registerValidation(argc, argv);
  int n = inf.readInt(1, 100000, "n"); inf.readEoln();
  while (n--) {
    inf.readInt(-1000000, 1000000, "x"); inf.readSpace();
    inf.readInt(-1000000, 1000000, "y"); inf.readEoln();
  }
  inf.readEof();
  return 0;
}
