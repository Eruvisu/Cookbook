#include "NativePerson.h"

NativePerson::NativePerson(int age, LPCTSTR name)
{
	m_Age = age;
	m_Name = name;
}

CString NativePerson::SayHello(LPCTSTR greet)
{
	return greet + m_Name;
}
