using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace SimpleInterop
    {
    class PlayMessageBeep
    {
        [DllImport("user32")]
        extern static bool MessageBeep(uint sound);     //native C function from WinAPI

        static void Main (string[] args)
        {
            // Plays a message beep
            MessageBeep(0x10);
        }
        }
    }
