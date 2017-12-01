#include<Windows.h>

using namespace System;

// In order for this to work, go to Project properties->Linker->Advanced->Entry Point and add Program::Main
// or the name of some other function that you wish to serve as the program entry point.
public ref class Program
{
	static int Main(array<System::String^>^ args)
	{
		SYSTEM_INFO si;
		GetNativeSystemInfo(&si);
		if (si.wProcessorArchitecture == PROCESSOR_ARCHITECTURE_AMD64)
			Console::WriteLine(L"64 bit system!");
		else
			Console::WriteLine(L"32 bit system");

		return 0;
	}
};