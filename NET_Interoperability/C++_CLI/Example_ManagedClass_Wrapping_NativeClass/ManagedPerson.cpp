#include "ManagedPerson.h"
#include <msclr/marshal.h>

using namespace msclr::interop;
using namespace PeopleLibrary;
using namespace System;

ManagedPerson::ManagedPerson(int age, String^ name)
{
	marshal_context ctx;
	m_pNative = new NativePerson(age, ctx.marshal_as<LPCTSTR>(name));
}


ManagedPerson::~ManagedPerson()
{
	delete m_pNative;
}

String^ ManagedPerson::Name::get()
{
	return gcnew String(m_pNative->GetName());
}

String^ ManagedPerson::SayHello(String^ greet)
{
	marshal_context ctx;
	return gcnew String(m_pNative->SayHello(ctx.marshal_as<LPCTSTR>(greet)));
}