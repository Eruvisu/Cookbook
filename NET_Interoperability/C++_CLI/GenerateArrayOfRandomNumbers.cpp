using namespace System;
using namespace System::Linq;

int main(array<System::String ^> ^args)
{
	// Generate and display a random number.
	//Random^ rnd = gcnew Random;
	auto rnd = gcnew Random;
	Console::WriteLine(rnd->Next(1, 100));

	// Generate an array of random numbers,
	// and then display the sum and average of the
	// numbers contained in this array.
	array<int>^ numbers = gcnew array<int>(100);
	for (int i = 0; i < numbers->Length; i++)
		numbers[i] = rnd->Next(0, 100);
	int sum = Enumerable::Sum(numbers);
	double average = Enumerable::Average(numbers);

	Console::WriteLine(sum);
	Console::WriteLine(average);

	//auto ms = gcnew System::IO::MemoryStream(100);
	//delete ms;	// calling delete will not destroy the object,
	//				// it will just call Dispose().

	{
		System::IO::MemoryStream ms(100);	// using stack semantics; when 'ms' goes out of scope,
											// delete will be called automatically, that is Dispose()
											// will be called automatically.
		auto len = ms.Length;
	}

	return 0;
}