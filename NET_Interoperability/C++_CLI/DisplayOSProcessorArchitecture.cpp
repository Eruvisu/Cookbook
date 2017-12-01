#include<Windows.h>

using namespace System;

int main(array<System::String ^> ^args)
{
	SYSTEM_INFO si;
	GetNativeSystemInfo(&si);
	if (si.wProcessorArchitecture == PROCESSOR_ARCHITECTURE_AMD64)
		Console::WriteLine(L"64 bit system!");
	else
		Console::WriteLine(L"32 bit system!");

	return 0;
}