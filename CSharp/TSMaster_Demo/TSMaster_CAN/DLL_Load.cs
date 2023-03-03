using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace TSMaster_CAN
{
    public class DLL_Load
    {
        [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
        public unsafe delegate int seed_key(byte* ipSeedArray, uint iSeedArraySize, uint iSecurityLevel, string ipVariant, byte* iopKeyArray, uint iMaxKeyArraySize, ref int oActualKeyArraySize);

        [DllImport("kernel32.dll")]
        public extern static IntPtr LoadLibrary(string path);

        [DllImport("kernel32", EntryPoint = "FreeLibrary", SetLastError = true)]
        public static extern bool FreeLibrary(IntPtr hModule);

        [DllImport("Kernel32.dll")]
        private static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

        public static Delegate LoadFunction<T>(IntPtr hModule, string functionName)
        {
            IntPtr functionAddress = GetProcAddress(hModule, functionName);
            if (functionAddress.ToInt64() == 0)
            {
                return null;
            }
            return Marshal.GetDelegateForFunctionPointer(functionAddress, typeof(T));
        }
        public static IntPtr Handle;
        public static seed_key key_handle;
        public static void load_seed_key(string dllname)
        {
            FreeLibrary(Handle);
            Handle = LoadLibrary(dllname);
            if (Handle.ToInt64() != 0)
            {
                key_handle = (seed_key)LoadFunction<seed_key>(Handle, "GenerateKeyEx");
                if (key_handle != null)
                {
                    
                }
            }

        }
    }
}
