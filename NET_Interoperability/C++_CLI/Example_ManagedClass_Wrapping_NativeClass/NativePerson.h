#pragma once

#include <atlstr.h>

class NativePerson
{
public:
	NativePerson(int age, LPCTSTR name);

	int GetAge() const { return m_Age; }
	void SetAge(int age)
	{
		m_Age = age;
	}

	LPCTSTR GetName() const
	{
		return m_Name;
	}

	CString SayHello(LPCTSTR greet);

private:
	int m_Age;
	CString m_Name;
};
