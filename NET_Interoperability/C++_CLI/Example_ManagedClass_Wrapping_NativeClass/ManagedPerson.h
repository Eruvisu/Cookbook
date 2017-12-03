#pragma once

#include "NativePerson.h"

namespace PeopleLibrary
{
	using namespace System;

	public ref class ManagedPerson
	{
	public:
		ManagedPerson(int age, String^ name);
		~ManagedPerson();

		property int Age
		{
			int get()
			{
				return m_pNative->GetAge();
			}
			void set(int age)
			{
				m_pNative->SetAge(age);
			}
		}

		property String^ Name
		{
			String^ get();
		}

		String^ SayHello(String^ greet);

	private:
		NativePerson* m_pNative;
	};
}