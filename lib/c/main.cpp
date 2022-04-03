#include <iostream>
#include <WinHvPlatform.h>
#include <vector>
#include <Q

using namespace std;

int main(int argn, char** arg) {
  for (int i = 0; i < 10; ++i) 
    std::cout << "Hello" << i << "\n";
}
