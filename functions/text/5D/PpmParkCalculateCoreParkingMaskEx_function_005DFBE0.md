# PpmParkCalculateCoreParkingMaskEx

- RVA: `0x005DFBE0`–`0x005E05D7` (길이 `2,551` bytes)
- VA: `0x00000001405DFBE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CD9D8`
- 디코드: `623`개 명령, `2,551/2,551` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **63**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **24**

### Outgoing calls
- `0x005DFC38` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFC8C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFCA8` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFCC9` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFCE1` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFCFD` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFD1A` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFD35` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFD4C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFD69` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFDC5` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFE0E` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005DFE41` → [PpmParkFindOverUtilizedProcessorsEx](../4F/PpmParkFindOverUtilizedProcessorsEx_function_004F1394.md) (function, `0x004F1394`)
- `0x005DFEBC` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005DFEC4` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005DFEFC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFF1F` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x005DFF35` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x005DFF42` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005DFF58` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005DFF66` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005DFF6E` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005DFF7F` → [KeCountSetBitsAffinityEx](../2C/KeCountSetBitsAffinityEx_function_002CE6E0.md) (function, `0x002CE6E0`)
- `0x005DFFA6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DFFCD` → [KeCheckProcessorAffinityEx](../30/KeCheckProcessorAffinityEx_function_00305150.md) (function, `0x00305150`)
- `0x005DFFDF` → [KeCheckProcessorAffinityEx](../30/KeCheckProcessorAffinityEx_function_00305150.md) (function, `0x00305150`)
- `0x005DFFEA` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x005E000E` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x005E0017` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x005E0024` → [KeCountSetBitsAffinityEx](../2C/KeCountSetBitsAffinityEx_function_002CE6E0.md) (function, `0x002CE6E0`)
- `0x005E0041` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0055` → [KeCpuSetQueryUnparkRecommendationEx](../4F/KeCpuSetQueryUnparkRecommendationEx_function_004F22B0.md) (function, `0x004F22B0`)
- `0x005E0098` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005E00A4` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x005E00BA` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x005E00C7` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005E00DA` → [KeCountSetBitsAffinityEx](../2C/KeCountSetBitsAffinityEx_function_002CE6E0.md) (function, `0x002CE6E0`)
- `0x005E00FC` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005E0115` → [KeCheckProcessorAffinityEx](../30/KeCheckProcessorAffinityEx_function_00305150.md) (function, `0x00305150`)
- `0x005E0120` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x005E013F` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x005E0148` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x005E0154` → [KeCountSetBitsAffinityEx](../2C/KeCountSetBitsAffinityEx_function_002CE6E0.md) (function, `0x002CE6E0`)
- `0x005E0164` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005E017D` → [Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline](Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline_function_005DFB8C.md) (function, `0x005DFB8C`)
- `0x005E018F` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005E01B9` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E01DF` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E01EB` → [KeIsSubsetAffinityEx](../2C/KeIsSubsetAffinityEx_function_002CDC80.md) (function, `0x002CDC80`)
- `0x005E0397` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E0415` → [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) (function, `0x005E05E0`)
- `0x005E041A` → [Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline](Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline_function_005DFB8C.md) (function, `0x005DFB8C`)
- `0x005E0448` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E045E` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E0477` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E0489` → [KeOrAffinityEx2](../2C/KeOrAffinityEx2_function_002CF930.md) (function, `0x002CF930`)
- `0x005E049B` → [KeOrAffinityEx2](../2C/KeOrAffinityEx2_function_002CF930.md) (function, `0x002CF930`)
- `0x005E04B4` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E04C6` → [KeOrAffinityEx2](../2C/KeOrAffinityEx2_function_002CF930.md) (function, `0x002CF930`)
- `0x005E0518` → [PpmEventTraceSoftCoreParkingSelectionEx](../4F/PpmEventTraceSoftCoreParkingSelectionEx_function_004F2424.md) (function, `0x004F2424`)
- `0x005E056A` → [PpmParkComputeDiff](../4A/PpmParkComputeDiff_function_004ADCAC.md) (function, `0x004ADCAC`)
- `0x005E059E` → [PpmEventLPICoreParking](PpmEventLPICoreParking_function_005DAE1C.md) (function, `0x005DAE1C`)
- `0x005E05B0` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmParkCalculateCoreParkingMask](../48/PpmParkCalculateCoreParkingMask_function_0048E5F0.md) at `0x0048E63A`

### Static image references
- `0x005DFC06` → RVA `0x00E0A740` (`.data`; read)
- `0x005DFC3D` → RVA `0x00F083D0` (`.data`; read)
- `0x005DFC4C` → RVA `0x00E67A80` (`.data`; read)
- `0x005DFD73` → RVA `0x00E08380` (`.data`; read)
- `0x005DFD7A` → RVA `0x00F0CE0C` (`.data`; read)
- `0x005DFD81` → RVA `0x00F083C8` (`.data`; read)
- `0x005DFD8F` → RVA `0x00F083B0` (`.data`; write)
- `0x005DFD98` → RVA `0x00F083C0` (`.data`; write)
- `0x005DFDB5` → RVA `0x00FC6AE8` (`ALMOSTRO`; read)
- `0x005DFDCA` → RVA `0x00F083E0` (`.data`; read)
- `0x005DFDE4` → RVA `0x00F083D8` (`.data`; read)
- `0x005DFE54` → RVA `0x00FC50B8` (`ALMOSTRO`; read)
- `0x005DFEDD` → RVA `0x00F083A2` (`.data`; read)
- `0x005DFFAB` → RVA `0x00FC6ABF` (`ALMOSTRO`; read)
- `0x005DFFBB` → RVA `0x00F21FB0` (`.data`; read)
- `0x005E019A` → RVA `0x00FC501C` (`ALMOSTRO`; read)
- `0x005E028F` → RVA `0x00F0B24C` (`.data`; read)
- `0x005E0330` → RVA `0x00FC6AF1` (`ALMOSTRO`; read)
- `0x005E035B` → RVA `0x00FC6A86` (`ALMOSTRO`; read)
- `0x005E056F` → RVA `0x00E67A40` (`.data`; read)
- `0x005E057A` → RVA `0x00E67A3C` (`.data`; read)
- `0x005E0582` → RVA `0x00E67A48` (`.data`; read)
- `0x005E058E` → RVA `0x00E67A3C` (`.data`; write)
- `0x005E0594` → RVA `0x00E67A48` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DFBE0  48 8B C4                        mov rax, rsp
005DFBE3  48 89 58 08                     mov qword ptr [rax + 8], rbx
005DFBE7  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
005DFBEB  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
005DFBEF  55                              push rbp
005DFBF0  41 54                           push r12
005DFBF2  41 55                           push r13
005DFBF4  41 56                           push r14
005DFBF6  41 57                           push r15
005DFBF8  48 8D A8 D8 FE FF FF            lea rbp, [rax - 0x128]
005DFBFF  48 81 EC 00 02 00 00            sub rsp, 0x200
005DFC06  48 8B 05 33 AB 82 00            mov rax, qword ptr [rip + 0x82ab33]
005DFC0D  48 33 C4                        xor rax, rsp
005DFC10  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
005DFC17  0F 57 C0                        xorps xmm0, xmm0
005DFC1A  48 8D 4D E0                     lea rcx, [rbp - 0x20]
005DFC1E  33 C0                           xor eax, eax
005DFC20  33 DB                           xor ebx, ebx
005DFC22  33 D2                           xor edx, edx
005DFC24  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
005DFC28  41 B8 08 01 00 00               mov r8d, 0x108
005DFC2E  89 5D 88                        mov dword ptr [rbp - 0x78], ebx
005DFC31  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
005DFC35  89 5D 80                        mov dword ptr [rbp - 0x80], ebx
005DFC38  E8 03 70 0E 00                  call 0x1406c6c40
005DFC3D  39 1D 8D 87 92 00               cmp dword ptr [rip + 0x92878d], ebx
005DFC43  8D 7B 01                        lea edi, [rbx + 1]
005DFC46  0F 84 57 09 00 00               je 0x1405e05a3
005DFC4C  4C 8B 2D 2D 7E 88 00            mov r13, qword ptr [rip + 0x887e2d]
005DFC53  33 D2                           xor edx, edx
005DFC55  45 0F B7 45 00                  movzx r8d, word ptr [r13]
005DFC5A  49 8D 4D 08                     lea rcx, [r13 + 8]
005DFC5E  49 C1 E0 03                     shl r8, 3
005DFC62  4D 8D A5 08 01 00 00            lea r12, [r13 + 0x108]
005DFC69  49 8D 9D 10 02 00 00            lea rbx, [r13 + 0x210]
005DFC70  4D 8D BD 18 03 00 00            lea r15, [r13 + 0x318]
005DFC77  49 8D BD 20 04 00 00            lea rdi, [r13 + 0x420]
005DFC7E  4D 8D B5 30 06 00 00            lea r14, [r13 + 0x630]
005DFC85  49 8D B5 38 07 00 00            lea rsi, [r13 + 0x738]
005DFC8C  E8 AF 6F 0E 00                  call 0x1406c6c40
005DFC91  66 41 C7 45 00 01 00            mov word ptr [r13], 1
005DFC98  49 8D 4C 24 08                  lea rcx, [r12 + 8]
005DFC9D  45 0F B7 04 24                  movzx r8d, word ptr [r12]
005DFCA2  33 D2                           xor edx, edx
005DFCA4  49 C1 E0 03                     shl r8, 3
005DFCA8  E8 93 6F 0E 00                  call 0x1406c6c40
005DFCAD  48 8D 43 08                     lea rax, [rbx + 8]
005DFCB1  66 41 C7 04 24 01 00            mov word ptr [r12], 1
005DFCB8  44 0F B7 03                     movzx r8d, word ptr [rbx]
005DFCBC  48 8B C8                        mov rcx, rax
005DFCBF  49 C1 E0 03                     shl r8, 3
005DFCC3  33 D2                           xor edx, edx
005DFCC5  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
005DFCC9  E8 72 6F 0E 00                  call 0x1406c6c40
005DFCCE  66 C7 03 01 00                  mov word ptr [rbx], 1
005DFCD3  49 8D 4F 08                     lea rcx, [r15 + 8]
005DFCD7  45 0F B7 07                     movzx r8d, word ptr [r15]
005DFCDB  33 D2                           xor edx, edx
005DFCDD  49 C1 E0 03                     shl r8, 3
005DFCE1  E8 5A 6F 0E 00                  call 0x1406c6c40
005DFCE6  BB 01 00 00 00                  mov ebx, 1
005DFCEB  48 8D 4F 08                     lea rcx, [rdi + 8]
005DFCEF  66 41 89 1F                     mov word ptr [r15], bx
005DFCF3  33 D2                           xor edx, edx
005DFCF5  44 0F B7 07                     movzx r8d, word ptr [rdi]
005DFCF9  49 C1 E0 03                     shl r8, 3
005DFCFD  E8 3E 6F 0E 00                  call 0x1406c6c40
005DFD02  66 89 1F                        mov word ptr [rdi], bx
005DFD05  33 D2                           xor edx, edx
005DFD07  49 8D 9D 28 05 00 00            lea rbx, [r13 + 0x528]
005DFD0E  44 0F B7 03                     movzx r8d, word ptr [rbx]
005DFD12  48 8D 4B 08                     lea rcx, [rbx + 8]
005DFD16  49 C1 E0 03                     shl r8, 3
005DFD1A  E8 21 6F 0E 00                  call 0x1406c6c40
005DFD1F  BF 01 00 00 00                  mov edi, 1
005DFD24  49 8D 4E 08                     lea rcx, [r14 + 8]
005DFD28  66 89 3B                        mov word ptr [rbx], di
005DFD2B  33 D2                           xor edx, edx
005DFD2D  45 0F B7 06                     movzx r8d, word ptr [r14]
005DFD31  49 C1 E0 03                     shl r8, 3
005DFD35  E8 06 6F 0E 00                  call 0x1406c6c40
005DFD3A  66 41 89 3E                     mov word ptr [r14], di
005DFD3E  48 8D 4E 08                     lea rcx, [rsi + 8]
005DFD42  44 0F B7 06                     movzx r8d, word ptr [rsi]
005DFD46  33 D2                           xor edx, edx
005DFD48  49 C1 E0 03                     shl r8, 3
005DFD4C  E8 EF 6E 0E 00                  call 0x1406c6c40
005DFD51  49 8D 9D 40 08 00 00            lea rbx, [r13 + 0x840]
005DFD58  66 89 3E                        mov word ptr [rsi], di
005DFD5B  44 0F B7 03                     movzx r8d, word ptr [rbx]
005DFD5F  48 8D 4B 08                     lea rcx, [rbx + 8]
005DFD63  49 C1 E0 03                     shl r8, 3
005DFD67  33 D2                           xor edx, edx
005DFD69  E8 D2 6E 0E 00                  call 0x1406c6c40
005DFD6E  66 89 3B                        mov word ptr [rbx], di
005DFD71  33 F6                           xor esi, esi
005DFD73  48 8B 15 06 86 82 00            mov rdx, qword ptr [rip + 0x828606]
005DFD7A  48 63 05 8B D0 92 00            movsxd rax, dword ptr [rip + 0x92d08b]
005DFD81  48 8B 0D 40 86 92 00            mov rcx, qword ptr [rip + 0x928640]
005DFD88  48 69 C0 E8 01 00 00            imul rax, rax, 0x1e8
005DFD8F  89 35 1B 86 92 00               mov dword ptr [rip + 0x92861b], esi
005DFD95  48 03 C2                        add rax, rdx
005DFD98  40 88 35 21 86 92 00            mov byte ptr [rip + 0x928621], sil
005DFD9F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
005DFDA3  0F B6 80 B4 00 00 00            movzx eax, byte ptr [rax + 0xb4]
005DFDAA  6B C0 64                        imul eax, eax, 0x64
005DFDAD  89 45 B8                        mov dword ptr [rbp - 0x48], eax
005DFDB0  48 85 C9                        test rcx, rcx
005DFDB3  74 15                           je 0x1405dfdca
005DFDB5  44 8B 05 2C 6D 9E 00            mov r8d, dword ptr [rip + 0x9e6d2c]
005DFDBC  BA FF 00 00 00                  mov edx, 0xff
005DFDC1  49 C1 E0 02                     shl r8, 2
005DFDC5  E8 76 6E 0E 00                  call 0x1406c6c40
005DFDCA  39 35 10 86 92 00               cmp dword ptr [rip + 0x928610], esi
005DFDD0  8B DE                           mov ebx, esi
005DFDD2  89 5D 9C                        mov dword ptr [rbp - 0x64], ebx
005DFDD5  0F 84 8F 07 00 00               je 0x1405e056a
005DFDDB  8B C3                           mov eax, ebx
005DFDDD  48 69 F8 10 05 00 00            imul rdi, rax, 0x510
005DFDE4  48 03 3D ED 85 92 00            add rdi, qword ptr [rip + 0x9285ed]
005DFDEB  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
005DFDEF  F6 87 A0 04 00 00 01            test byte ptr [rdi + 0x4a0], 1
005DFDF6  0F 85 58 07 00 00               jne 0x1405e0554
005DFDFC  48 8D 8F 40 02 00 00            lea rcx, [rdi + 0x240]
005DFE03  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
005DFE07  4C 8D 87 38 01 00 00            lea r8, [rdi + 0x138]
005DFE0E  E8 4D EA CE FF                  call 0x1402ce860
005DFE13  0F B7 87 96 04 00 00            movzx eax, word ptr [rdi + 0x496]
005DFE1A  4D 8B C7                        mov r8, r15
005DFE1D  8B 55 B8                        mov edx, dword ptr [rbp - 0x48]
005DFE20  48 8B CF                        mov rcx, rdi
005DFE23  66 89 B7 E4 04 00 00            mov word ptr [rdi + 0x4e4], si
005DFE2A  40 88 B7 E6 04 00 00            mov byte ptr [rdi + 0x4e6], sil
005DFE31  0F B7 B7 92 04 00 00            movzx esi, word ptr [rdi + 0x492]
005DFE38  66 3B F0                        cmp si, ax
005DFE3B  0F 43 F0                        cmovae esi, eax
005DFE3E  89 75 90                        mov dword ptr [rbp - 0x70], esi
005DFE41  E8 4E 15 F1 FF                  call 0x1404f1394
005DFE46  45 33 C9                        xor r9d, r9d
005DFE49  4C 8D 87 B8 04 00 00            lea r8, [rdi + 0x4b8]
005DFE50  45 88 48 10                     mov byte ptr [r8 + 0x10], r9b
005DFE54  8B 05 5E 52 9E 00               mov eax, dword ptr [rip + 0x9e525e]
005DFE5A  85 C0                           test eax, eax
005DFE5C  74 2B                           je 0x1405dfe89
005DFE5E  48 69 C8 10 27 00 00            imul rcx, rax, 0x2710
005DFE65  33 D2                           xor edx, edx
005DFE67  48 B8 08 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000008
005DFE71  48 8B 00                        mov rax, qword ptr [rax]
005DFE74  48 F7 F1                        div rcx
005DFE77  49 89 00                        mov qword ptr [r8], rax
005DFE7A  49 3B 40 08                     cmp rax, qword ptr [r8 + 8]
005DFE7E  74 09                           je 0x1405dfe89
005DFE80  41 C6 40 10 01                  mov byte ptr [r8 + 0x10], 1
005DFE85  49 89 40 08                     mov qword ptr [r8 + 8], rax
005DFE89  45 8B F9                        mov r15d, r9d
005DFE8C  44 89 4D 8C                     mov dword ptr [rbp - 0x74], r9d
005DFE90  44 38 4F 0C                     cmp byte ptr [rdi + 0xc], r9b
005DFE94  0F 86 B1 06 00 00               jbe 0x1405e054b
005DFE9A  41 0F B7 56 02                  movzx edx, word ptr [r14 + 2]
005DFE9F  49 8B CE                        mov rcx, r14
005DFEA2  41 8B C7                        mov eax, r15d
005DFEA5  4C 8D 3C 80                     lea r15, [rax + rax*4]
005DFEA9  49 C1 E7 07                     shl r15, 7
005DFEAD  4C 03 BF 08 05 00 00            add r15, qword ptr [rdi + 0x508]
005DFEB4  44 89 4D 80                     mov dword ptr [rbp - 0x80], r9d
005DFEB8  4D 8D 47 28                     lea r8, [r15 + 0x28]
005DFEBC  E8 9F E9 CE FF                  call 0x1402ce860
005DFEC1  49 8B CE                        mov rcx, r14
005DFEC4  E8 B7 16 CF FF                  call 0x1402d1580
005DFEC9  85 C0                           test eax, eax
005DFECB  0F 85 77 06 00 00               jne 0x1405e0548
005DFED1  B8 01 00 00 00                  mov eax, 1
005DFED6  C7 45 80 00 00 10 00            mov dword ptr [rbp - 0x80], 0x100000
005DFEDD  66 39 05 BE 84 92 00            cmp word ptr [rip + 0x9284be], ax
005DFEE4  49 8D 9F 30 01 00 00            lea rbx, [r15 + 0x130]
005DFEEB  76 60                           jbe 0x1405dff4d
005DFEED  45 0F B7 45 00                  movzx r8d, word ptr [r13]
005DFEF2  49 8D 4D 08                     lea rcx, [r13 + 8]
005DFEF6  49 C1 E0 03                     shl r8, 3
005DFEFA  33 D2                           xor edx, edx
005DFEFC  E8 3F 6D 0E 00                  call 0x1406c6c40
005DFF01  33 C0                           xor eax, eax
005DFF03  66 41 C7 45 00 01 00            mov word ptr [r13], 1
005DFF0A  66 89 45 B0                     mov word ptr [rbp - 0x50], ax
005DFF0E  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
005DFF12  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
005DFF16  48 89 5D A0                     mov qword ptr [rbp - 0x60], rbx
005DFF1A  EB 1E                           jmp 0x1405dff3a
005DFF1C  8B 4D 88                        mov ecx, dword ptr [rbp - 0x78]
005DFF1F  E8 AC 86 CF FF                  call 0x1402d85d0
005DFF24  49 8B CD                        mov rcx, r13
005DFF27  0F B6 90 D0 00 00 00            movzx edx, byte ptr [rax + 0xd0]
005DFF2E  4C 8B 80 60 8E 00 00            mov r8, qword ptr [rax + 0x8e60]
005DFF35  E8 86 B7 C7 FF                  call 0x14025b6c0
005DFF3A  48 8D 55 A0                     lea rdx, [rbp - 0x60]
005DFF3E  48 8D 4D 88                     lea rcx, [rbp - 0x78]
005DFF42  E8 39 55 E3 FF                  call 0x140415480
005DFF47  85 C0                           test eax, eax
005DFF49  74 D1                           je 0x1405dff1c
005DFF4B  EB 10                           jmp 0x1405dff5d
005DFF4D  41 0F B7 55 02                  movzx edx, word ptr [r13 + 2]
005DFF52  4C 8B C3                        mov r8, rbx
005DFF55  49 8B CD                        mov rcx, r13
005DFF58  E8 03 E9 CE FF                  call 0x1402ce860
005DFF5D  4D 8B C5                        mov r8, r13
005DFF60  49 8B D6                        mov rdx, r14
005DFF63  49 8B CD                        mov rcx, r13
005DFF66  E8 D5 07 DE FF                  call 0x1403c0740
005DFF6B  49 8B CD                        mov rcx, r13
005DFF6E  E8 0D 16 CF FF                  call 0x1402d1580
005DFF73  85 C0                           test eax, eax
005DFF75  75 05                           jne 0x1405dff7c
005DFF77  0F BA 6D 80 10                  bts dword ptr [rbp - 0x80], 0x10
005DFF7C  49 8B CD                        mov rcx, r13
005DFF7F  E8 5C E7 CE FF                  call 0x1402ce6e0
005DFF84  41 0F B7 0F                     movzx ecx, word ptr [r15]
005DFF88  8B DE                           mov ebx, esi
005DFF8A  45 0F B7 04 24                  movzx r8d, word ptr [r12]
005DFF8F  2B C8                           sub ecx, eax
005DFF91  3B CE                           cmp ecx, esi
005DFF93  0F 46 D9                        cmovbe ebx, ecx
005DFF96  33 F6                           xor esi, esi
005DFF98  49 C1 E0 03                     shl r8, 3
005DFF9C  49 8D 4C 24 08                  lea rcx, [r12 + 8]
005DFFA1  33 D2                           xor edx, edx
005DFFA3  44 8B F6                        mov r14d, esi
005DFFA6  E8 95 6C 0E 00                  call 0x1406c6c40
005DFFAB  40 38 35 0D 6B 9E 00            cmp byte ptr [rip + 0x9e6b0d], sil
005DFFB2  66 41 C7 04 24 01 00            mov word ptr [r12], 1
005DFFB9  75 71                           jne 0x1405e002c
005DFFBB  8B 35 EF 1F 94 00               mov esi, dword ptr [rip + 0x941fef]
005DFFC1  49 8D 8D 30 06 00 00            lea rcx, [r13 + 0x630]
005DFFC8  8B D6                           mov edx, esi
005DFFCA  89 75 88                        mov dword ptr [rbp - 0x78], esi
005DFFCD  E8 7E 51 D2 FF                  call 0x140305150
005DFFD2  85 C0                           test eax, eax
005DFFD4  74 56                           je 0x1405e002c
005DFFD6  85 DB                           test ebx, ebx
005DFFD8  74 52                           je 0x1405e002c
005DFFDA  8B D6                           mov edx, esi
005DFFDC  49 8B CD                        mov rcx, r13
005DFFDF  E8 6C 51 D2 FF                  call 0x140305150
005DFFE4  85 C0                           test eax, eax
005DFFE6  75 44                           jne 0x1405e002c
005DFFE8  8B CE                           mov ecx, esi
005DFFEA  E8 E1 85 CF FF                  call 0x1402d85d0
005DFFEF  B9 01 00 00 00                  mov ecx, 1
005DFFF4  66 39 0D A7 83 92 00            cmp word ptr [rip + 0x9283a7], cx
005DFFFB  49 8B CC                        mov rcx, r12
005DFFFE  76 15                           jbe 0x1405e0015
005E0000  0F B6 90 D0 00 00 00            movzx edx, byte ptr [rax + 0xd0]
005E0007  4C 8B 80 60 8E 00 00            mov r8, qword ptr [rax + 0x8e60]
005E000E  E8 AD B6 C7 FF                  call 0x14025b6c0
005E0013  EB 07                           jmp 0x1405e001c
005E0015  8B D6                           mov edx, esi
005E0017  E8 D4 B6 C7 FF                  call 0x14025b6f0
005E001C  0F BA 6D 80 08                  bts dword ptr [rbp - 0x80], 8
005E0021  49 8B CC                        mov rcx, r12
005E0024  E8 B7 E6 CE FF                  call 0x1402ce6e0
005E0029  44 8B F0                        mov r14d, eax
005E002C  49 8D B5 10 02 00 00            lea rsi, [r13 + 0x210]
005E0033  33 D2                           xor edx, edx
005E0035  44 0F B7 06                     movzx r8d, word ptr [rsi]
005E0039  48 8D 4E 08                     lea rcx, [rsi + 8]
005E003D  49 C1 E0 03                     shl r8, 3
005E0041  E8 FA 6B 0E 00                  call 0x1406c6c40
005E0046  48 8B D6                        mov rdx, rsi
005E0049  66 C7 06 01 00                  mov word ptr [rsi], 1
005E004E  49 8D 8D 30 06 00 00            lea rcx, [r13 + 0x630]
005E0055  E8 56 22 F1 FF                  call 0x1404f22b0
005E005A  0F B7 F0                        movzx esi, ax
005E005D  33 C0                           xor eax, eax
005E005F  89 75 94                        mov dword ptr [rbp - 0x6c], esi
005E0062  85 F6                           test esi, esi
005E0064  0F 84 09 01 00 00               je 0x1405e0173
005E006A  8D 48 01                        lea ecx, [rax + 1]
005E006D  66 39 0D 2E 83 92 00            cmp word ptr [rip + 0x92832e], cx
005E0074  49 8D B5 10 02 00 00            lea rsi, [r13 + 0x210]
005E007B  76 67                           jbe 0x1405e00e4
005E007D  66 89 45 B0                     mov word ptr [rbp - 0x50], ax
005E0081  48 8D 55 A0                     lea rdx, [rbp - 0x60]
005E0085  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
005E0089  48 8D 4D 88                     lea rcx, [rbp - 0x78]
005E008D  48 8B 00                        mov rax, qword ptr [rax]
005E0090  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
005E0094  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
005E0098  E8 E3 53 E3 FF                  call 0x140415480
005E009D  85 C0                           test eax, eax
005E009F  75 36                           jne 0x1405e00d7
005E00A1  8B 4D 88                        mov ecx, dword ptr [rbp - 0x78]
005E00A4  E8 27 85 CF FF                  call 0x1402d85d0
005E00A9  48 8B CE                        mov rcx, rsi
005E00AC  0F B6 90 D0 00 00 00            movzx edx, byte ptr [rax + 0xd0]
005E00B3  4C 8B 80 60 8E 00 00            mov r8, qword ptr [rax + 0x8e60]
005E00BA  E8 01 B6 C7 FF                  call 0x14025b6c0
005E00BF  48 8D 55 A0                     lea rdx, [rbp - 0x60]
005E00C3  48 8D 4D 88                     lea rcx, [rbp - 0x78]
005E00C7  E8 B4 53 E3 FF                  call 0x140415480
005E00CC  85 C0                           test eax, eax
005E00CE  74 D1                           je 0x1405e00a1
005E00D0  4D 8D A5 08 01 00 00            lea r12, [r13 + 0x108]
005E00D7  48 8B CE                        mov rcx, rsi
005E00DA  E8 01 E6 CE FF                  call 0x1402ce6e0
005E00DF  89 45 94                        mov dword ptr [rbp - 0x6c], eax
005E00E2  33 C0                           xor eax, eax
005E00E4  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
005E00E8  48 8D 55 A0                     lea rdx, [rbp - 0x60]
005E00EC  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
005E00F0  48 8D 4D 88                     lea rcx, [rbp - 0x78]
005E00F4  66 89 45 B0                     mov word ptr [rbp - 0x50], ax
005E00F8  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
005E00FC  E8 7F 53 E3 FF                  call 0x140415480
005E0101  85 C0                           test eax, eax
005E0103  75 6C                           jne 0x1405e0171
005E0105  8D 78 01                        lea edi, [rax + 1]
005E0108  44 3B F3                        cmp r14d, ebx
005E010B  73 4F                           jae 0x1405e015c
005E010D  8B 75 88                        mov esi, dword ptr [rbp - 0x78]
005E0110  49 8B CD                        mov rcx, r13
005E0113  8B D6                           mov edx, esi
005E0115  E8 36 50 D2 FF                  call 0x140305150
005E011A  85 C0                           test eax, eax
005E011C  75 3E                           jne 0x1405e015c
005E011E  8B CE                           mov ecx, esi
005E0120  E8 AB 84 CF FF                  call 0x1402d85d0
005E0125  66 39 3D 76 82 92 00            cmp word ptr [rip + 0x928276], di
005E012C  49 8B CC                        mov rcx, r12
005E012F  76 15                           jbe 0x1405e0146
005E0131  0F B6 90 D0 00 00 00            movzx edx, byte ptr [rax + 0xd0]
005E0138  4C 8B 80 60 8E 00 00            mov r8, qword ptr [rax + 0x8e60]
005E013F  E8 7C B5 C7 FF                  call 0x14025b6c0
005E0144  EB 07                           jmp 0x1405e014d
005E0146  8B D6                           mov edx, esi
005E0148  E8 A3 B5 C7 FF                  call 0x14025b6f0
005E014D  83 4D 80 10                     or dword ptr [rbp - 0x80], 0x10
005E0151  49 8B CC                        mov rcx, r12
005E0154  E8 87 E5 CE FF                  call 0x1402ce6e0
005E0159  44 8B F0                        mov r14d, eax
005E015C  48 8D 55 A0                     lea rdx, [rbp - 0x60]
005E0160  48 8D 4D 88                     lea rcx, [rbp - 0x78]
005E0164  E8 17 53 E3 FF                  call 0x140415480
005E0169  85 C0                           test eax, eax
005E016B  74 9B                           je 0x1405e0108
005E016D  48 8B 7D C8                     mov rdi, qword ptr [rbp - 0x38]
005E0171  33 C0                           xor eax, eax
005E0173  88 45 85                        mov byte ptr [rbp - 0x7b], al
005E0176  C7 45 98 03 00 00 00            mov dword ptr [rbp - 0x68], 3
005E017D  E8 0A FA FF FF                  call 0x1405dfb8c
005E0182  33 D2                           xor edx, edx
005E0184  85 C0                           test eax, eax
005E0186  0F 84 87 00 00 00               je 0x1405e0213
005E018C  49 8B CC                        mov rcx, r12
005E018F  E8 EC 13 CF FF                  call 0x1402d1580
005E0194  33 D2                           xor edx, edx
005E0196  85 C0                           test eax, eax
005E0198  75 79                           jne 0x1405e0213
005E019A  8B 05 7C 4E 9E 00               mov eax, dword ptr [rip + 0x9e4e7c]
005E01A0  A8 08                           test al, 8
005E01A2  74 6F                           je 0x1405e0213
005E01A4  41 B8 00 01 00 00               mov r8d, 0x100
005E01AA  48 C7 45 E0 01 00 20 00         mov qword ptr [rbp - 0x20], 0x200001
005E01B2  48 8D 4D E8                     lea rcx, [rbp - 0x18]
005E01B6  8D 72 01                        lea esi, [rdx + 1]
005E01B9  E8 82 6A 0E 00                  call 0x1406c6c40
005E01BE  48 8B 97 00 05 00 00            mov rdx, qword ptr [rdi + 0x500]
005E01C5  48 8D 4D E0                     lea rcx, [rbp - 0x20]
005E01C9  48 63 42 04                     movsxd rax, dword ptr [rdx + 4]
005E01CD  4C 69 C0 08 01 00 00            imul r8, rax, 0x108
005E01D4  49 83 C0 10                     add r8, 0x10
005E01D8  4C 03 C2                        add r8, rdx
005E01DB  0F B7 55 E2                     movzx edx, word ptr [rbp - 0x1e]
005E01DF  E8 7C E6 CE FF                  call 0x1402ce860
005E01E4  48 8D 55 E0                     lea rdx, [rbp - 0x20]
005E01E8  49 8B CC                        mov rcx, r12
005E01EB  E8 90 DA CE FF                  call 0x1402cdc80
005E01F0  33 D2                           xor edx, edx
005E01F2  85 C0                           test eax, eax
005E01F4  75 1D                           jne 0x1405e0213
005E01F6  0F BA 6D 80 19                  bts dword ptr [rbp - 0x80], 0x19
005E01FB  48 8B 87 00 05 00 00            mov rax, qword ptr [rdi + 0x500]
005E0202  40 88 75 85                     mov byte ptr [rbp - 0x7b], sil
005E0206  8B 48 04                        mov ecx, dword ptr [rax + 4]
005E0209  89 4D 98                        mov dword ptr [rbp - 0x68], ecx
005E020C  C7 40 04 02 00 00 00            mov dword ptr [rax + 4], 2
005E0213  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
005E0218  44 3B F0                        cmp r14d, eax
005E021B  73 1C                           jae 0x1405e0239
005E021D  44 3B F3                        cmp r14d, ebx
005E0220  73 17                           jae 0x1405e0239
005E0222  44 8B 45 80                     mov r8d, dword ptr [rbp - 0x80]
005E0226  3B C3                           cmp eax, ebx
005E0228  44 8B F3                        mov r14d, ebx
005E022B  44 0F 42 F0                     cmovb r14d, eax
005E022F  41 83 C8 04                     or r8d, 4
005E0233  44 89 45 80                     mov dword ptr [rbp - 0x80], r8d
005E0237  EB 04                           jmp 0x1405e023d
005E0239  44 8B 45 80                     mov r8d, dword ptr [rbp - 0x80]
005E023D  41 0F B7 47 04                  movzx eax, word ptr [r15 + 4]
005E0242  8B F3                           mov esi, ebx
005E0244  3B D8                           cmp ebx, eax
005E0246  76 16                           jbe 0x1405e025e
005E0248  44 3B F3                        cmp r14d, ebx
005E024B  73 11                           jae 0x1405e025e
005E024D  41 83 C8 08                     or r8d, 8
005E0251  8B F0                           mov esi, eax
005E0253  41 3B C6                        cmp eax, r14d
005E0256  44 89 45 80                     mov dword ptr [rbp - 0x80], r8d
005E025A  41 0F 46 F6                     cmovbe esi, r14d
005E025E  8B 1D B8 4D 9E 00               mov ebx, dword ptr [rip + 0x9e4db8]
005E0264  44 0F B7 DA                     movzx r11d, dx
005E0268  83 E3 08                        and ebx, 8
005E026B  74 11                           je 0x1405e027e
005E026D  48 8B 8F 00 05 00 00            mov rcx, qword ptr [rdi + 0x500]
005E0274  48 63 41 04                     movsxd rax, dword ptr [rcx + 4]
005E0278  44 0F B7 5C 41 08               movzx r11d, word ptr [rcx + rax*2 + 8]
005E027E  45 0F B7 57 06                  movzx r10d, word ptr [r15 + 6]
005E0283  45 0F B7 27                     movzx r12d, word ptr [r15]
005E0287  66 45 3B D4                     cmp r10w, r12w
005E028B  45 0F 43 D4                     cmovae r10d, r12d
005E028F  39 15 B7 AF 92 00               cmp dword ptr [rip + 0x92afb7], edx
005E0295  45 8B CA                        mov r9d, r10d
005E0298  74 38                           je 0x1405e02d2
005E029A  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
005E029D  F7 D8                           neg eax
005E029F  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
005E02A3  48 1B C9                        sbb rcx, rcx
005E02A6  48 F7 D9                        neg rcx
005E02A9  0F B6 94 01 89 00 00 00         movzx edx, byte ptr [rcx + rax + 0x89]
005E02B1  B8 1F 85 EB 51                  mov eax, 0x51eb851f
005E02B6  41 0F AF D4                     imul edx, r12d
005E02BA  83 C2 32                        add edx, 0x32
005E02BD  F7 E2                           mul edx
005E02BF  C1 EA 05                        shr edx, 5
005E02C2  41 3B D2                        cmp edx, r10d
005E02C5  76 0B                           jbe 0x1405e02d2
005E02C7  41 83 C8 40                     or r8d, 0x40
005E02CB  44 8B CA                        mov r9d, edx
005E02CE  44 89 45 80                     mov dword ptr [rbp - 0x80], r8d
005E02D2  0F B7 05 C9 80 92 00            movzx eax, word ptr [rip + 0x9280c9]
005E02D9  B9 01 00 00 00                  mov ecx, 1
005E02DE  66 3B C1                        cmp ax, cx
005E02E1  76 11                           jbe 0x1405e02f4
005E02E3  8B C8                           mov ecx, eax
005E02E5  33 D2                           xor edx, edx
005E02E7  FF C8                           dec eax
005E02E9  44 03 C8                        add r9d, eax
005E02EC  41 8B C1                        mov eax, r9d
005E02EF  F7 F1                           div ecx
005E02F1  44 2B CA                        sub r9d, edx
005E02F4  33 C9                           xor ecx, ecx
005E02F6  85 DB                           test ebx, ebx
005E02F8  74 19                           je 0x1405e0313
005E02FA  66 45 85 DB                     test r11w, r11w
005E02FE  74 13                           je 0x1405e0313
005E0300  66 45 3B D9                     cmp r11w, r9w
005E0304  73 0D                           jae 0x1405e0313
005E0306  41 0F BA E8 16                  bts r8d, 0x16
005E030B  45 0F B7 CB                     movzx r9d, r11w
005E030F  44 89 45 80                     mov dword ptr [rbp - 0x80], r8d
005E0313  8B 45 94                        mov eax, dword ptr [rbp - 0x6c]
005E0316  45 8B E6                        mov r12d, r14d
005E0319  41 03 C1                        add eax, r9d
005E031C  66 45 89 4F 08                  mov word ptr [r15 + 8], r9w
005E0321  3B C6                           cmp eax, esi
005E0323  0F 43 C6                        cmovae eax, esi
005E0326  41 3B C6                        cmp eax, r14d
005E0329  44 0F 47 E0                     cmova r12d, eax
005E032D  29 75 90                        sub dword ptr [rbp - 0x70], esi
005E0330  38 0D BB 67 9E 00               cmp byte ptr [rip + 0x9e67bb], cl
005E0336  66 45 89 67 0A                  mov word ptr [r15 + 0xa], r12w
005E033B  75 0A                           jne 0x1405e0347
005E033D  0F BA 6D 80 15                  bts dword ptr [rbp - 0x80], 0x15
005E0342  41 8B F4                        mov esi, r12d
005E0345  EB 14                           jmp 0x1405e035b
005E0347  85 DB                           test ebx, ebx
005E0349  74 10                           je 0x1405e035b
005E034B  0F BA 6D 80 17                  bts dword ptr [rbp - 0x80], 0x17
005E0350  41 0F B7 C3                     movzx eax, r11w
005E0354  3B F0                           cmp esi, eax
005E0356  0F 42 C6                        cmovb eax, esi
005E0359  8B F0                           mov esi, eax
005E035B  38 0D 25 67 9E 00               cmp byte ptr [rip + 0x9e6725], cl
005E0361  44 8B F9                        mov r15d, ecx
005E0364  8A D9                           mov bl, cl
005E0366  88 4D 84                        mov byte ptr [rbp - 0x7c], cl
005E0369  74 17                           je 0x1405e0382
005E036B  8A 87 F6 04 00 00               mov al, byte ptr [rdi + 0x4f6]
005E0371  44 0F B7 BF F0 04 00 00         movzx r15d, word ptr [rdi + 0x4f0]
005E0379  8A 9F F7 04 00 00               mov bl, byte ptr [rdi + 0x4f7]
005E037F  88 45 84                        mov byte ptr [rbp - 0x7c], al
005E0382  4D 8D 85 20 04 00 00            lea r8, [r13 + 0x420]
005E0389  49 8D 95 18 03 00 00            lea rdx, [r13 + 0x318]
005E0390  49 8D 8D 30 06 00 00            lea rcx, [r13 + 0x630]
005E0397  E8 A4 03 DE FF                  call 0x1403c0740
005E039C  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
005E039F  4D 8D 8D 20 04 00 00            lea r9, [r13 + 0x420]
005E03A6  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
005E03AA  4C 8D 87 40 02 00 00            lea r8, [rdi + 0x240]
005E03B1  8A 45 84                        mov al, byte ptr [rbp - 0x7c]
005E03B4  48 8B CF                        mov rcx, rdi
005E03B7  88 5C 24 70                     mov byte ptr [rsp + 0x70], bl
005E03BB  49 8D 9D 30 06 00 00            lea rbx, [r13 + 0x630]
005E03C2  88 44 24 68                     mov byte ptr [rsp + 0x68], al
005E03C6  48 8B D3                        mov rdx, rbx
005E03C9  44 89 7C 24 60                  mov dword ptr [rsp + 0x60], r15d
005E03CE  48 8D 87 B8 04 00 00            lea rax, [rdi + 0x4b8]
005E03D5  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
005E03DA  48 8D 45 80                     lea rax, [rbp - 0x80]
005E03DE  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
005E03E3  49 8D 85 38 07 00 00            lea rax, [r13 + 0x738]
005E03EA  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
005E03EF  49 8D 85 28 05 00 00            lea rax, [r13 + 0x528]
005E03F6  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
005E03FB  49 8D 85 08 01 00 00            lea rax, [r13 + 0x108]
005E0402  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005E0407  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
005E040C  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
005E0410  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
005E0415  E8 C6 01 00 00                  call 0x1405e05e0
005E041A  E8 6D F7 FF FF                  call 0x1405dfb8c
005E041F  33 C9                           xor ecx, ecx
005E0421  85 C0                           test eax, eax
005E0423  74 12                           je 0x1405e0437
005E0425  38 4D 85                        cmp byte ptr [rbp - 0x7b], cl
005E0428  74 0D                           je 0x1405e0437
005E042A  48 8B 87 00 05 00 00            mov rax, qword ptr [rdi + 0x500]
005E0431  8B 4D 98                        mov ecx, dword ptr [rbp - 0x68]
005E0434  89 48 04                        mov dword ptr [rax + 4], ecx
005E0437  4D 8D 85 40 08 00 00            lea r8, [r13 + 0x840]
005E043E  48 8B CB                        mov rcx, rbx
005E0441  49 8D 95 28 05 00 00            lea rdx, [r13 + 0x528]
005E0448  E8 53 57 CF FF                  call 0x1402d5ba0
005E044D  49 8D 8D 40 08 00 00            lea rcx, [r13 + 0x840]
005E0454  4C 8B C1                        mov r8, rcx
005E0457  49 8D 95 38 07 00 00            lea rdx, [r13 + 0x738]
005E045E  E8 3D 57 CF FF                  call 0x1402d5ba0
005E0463  48 8B D3                        mov rdx, rbx
005E0466  4C 8D 87 38 01 00 00            lea r8, [rdi + 0x138]
005E046D  48 8D 9F 38 01 00 00            lea rbx, [rdi + 0x138]
005E0474  48 8B CB                        mov rcx, rbx
005E0477  E8 24 57 CF FF                  call 0x1402d5ba0
005E047C  4C 8B C3                        mov r8, rbx
005E047F  49 8D 95 28 05 00 00            lea rdx, [r13 + 0x528]
005E0486  48 8B CB                        mov rcx, rbx
005E0489  E8 A2 F4 CE FF                  call 0x1402cf930
005E048E  4C 8B C3                        mov r8, rbx
005E0491  49 8D 95 38 07 00 00            lea rdx, [r13 + 0x738]
005E0498  48 8B CB                        mov rcx, rbx
005E049B  E8 90 F4 CE FF                  call 0x1402cf930
005E04A0  48 8D 9F 48 03 00 00            lea rbx, [rdi + 0x348]
005E04A7  4C 8B C3                        mov r8, rbx
005E04AA  49 8D 95 30 06 00 00            lea rdx, [r13 + 0x630]
005E04B1  48 8B CB                        mov rcx, rbx
005E04B4  E8 E7 56 CF FF                  call 0x1402d5ba0
005E04B9  4C 8B C3                        mov r8, rbx
005E04BC  49 8D 95 38 07 00 00            lea rdx, [r13 + 0x738]
005E04C3  48 8B CB                        mov rcx, rbx
005E04C6  E8 65 F4 CE FF                  call 0x1402cf930
005E04CB  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
005E04CE  44 0F B7 CE                     movzx r9d, si
005E04D2  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
005E04D7  45 0F B7 C4                     movzx r8d, r12w
005E04DB  44 8B 7D 8C                     mov r15d, dword ptr [rbp - 0x74]
005E04DF  48 8B CF                        mov rcx, rdi
005E04E2  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
005E04E6  41 8B D7                        mov edx, r15d
005E04E9  49 8D 85 10 02 00 00            lea rax, [r13 + 0x210]
005E04F0  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
005E04F5  49 8D 85 20 04 00 00            lea rax, [r13 + 0x420]
005E04FC  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005E0501  49 8D 85 08 01 00 00            lea rax, [r13 + 0x108]
005E0508  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
005E050D  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
005E0512  66 44 89 74 24 20               mov word ptr [rsp + 0x20], r14w
005E0518  E8 07 1F F1 FF                  call 0x1404f2424
005E051D  0F B6 47 0C                     movzx eax, byte ptr [rdi + 0xc]
005E0521  4D 8D A5 08 01 00 00            lea r12, [r13 + 0x108]
005E0528  8B 75 90                        mov esi, dword ptr [rbp - 0x70]
005E052B  4D 8D B5 30 06 00 00            lea r14, [r13 + 0x630]
005E0532  41 FF C7                        inc r15d
005E0535  41 B9 00 00 00 00               mov r9d, 0
005E053B  44 89 7D 8C                     mov dword ptr [rbp - 0x74], r15d
005E053F  44 3B F8                        cmp r15d, eax
005E0542  0F 82 52 F9 FF FF               jb 0x1405dfe9a
005E0548  8B 5D 9C                        mov ebx, dword ptr [rbp - 0x64]
005E054B  33 F6                           xor esi, esi
005E054D  4D 8D BD 18 03 00 00            lea r15, [r13 + 0x318]
005E0554  BF 01 00 00 00                  mov edi, 1
005E0559  03 DF                           add ebx, edi
005E055B  3B 1D 7F 7E 92 00               cmp ebx, dword ptr [rip + 0x927e7f]
005E0561  89 5D 9C                        mov dword ptr [rbp - 0x64], ebx
005E0564  0F 82 71 F8 FF FF               jb 0x1405dfddb
005E056A  E8 3D D7 EC FF                  call 0x1404adcac
005E056F  39 35 CB 74 88 00               cmp dword ptr [rip + 0x8874cb], esi
005E0575  8B D6                           mov edx, esi
005E0577  0F 97 C2                        seta dl
005E057A  39 15 BC 74 88 00               cmp dword ptr [rip + 0x8874bc], edx
005E0580  75 0A                           jne 0x1405e058c
005E0582  39 35 C0 74 88 00               cmp dword ptr [rip + 0x8874c0], esi
005E0588  8B C6                           mov eax, esi
005E058A  74 02                           je 0x1405e058e
005E058C  8B C7                           mov eax, edi
005E058E  89 15 A8 74 88 00               mov dword ptr [rip + 0x8874a8], edx
005E0594  89 35 AE 74 88 00               mov dword ptr [rip + 0x8874ae], esi
005E059A  85 C0                           test eax, eax
005E059C  74 05                           je 0x1405e05a3
005E059E  E8 79 A8 FF FF                  call 0x1405dae1c
005E05A3  40 8A C7                        mov al, dil
005E05A6  48 8B 8D F0 00 00 00            mov rcx, qword ptr [rbp + 0xf0]
005E05AD  48 33 CC                        xor rcx, rsp
005E05B0  E8 8B C0 0C 00                  call 0x1406ac640
005E05B5  4C 8D 9C 24 00 02 00 00         lea r11, [rsp + 0x200]
005E05BD  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
005E05C1  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
005E05C5  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
005E05C9  49 8B E3                        mov rsp, r11
005E05CC  41 5F                           pop r15
005E05CE  41 5E                           pop r14
005E05D0  41 5D                           pop r13
005E05D2  41 5C                           pop r12
005E05D4  5D                              pop rbp
005E05D5  C3                              ret
005E05D6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmParkCalculateCoreParkingMaskEx(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m1B0;
    unsigned __int8 v_stack_m1B8;
    unsigned __int8 v_stack_m1C0;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned int v_stack_m200;
    unsigned int v_stack_m208;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (512);
    result = (*(unsigned __int64 *)(v_rip + 8563507)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 296 + 240) = result;
    result = 0;
    v_rbx = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 296 - 80) = 0;
    *(unsigned int *)(v_rsp - 296 - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 296 - 96) = v_xmm0;
    *(unsigned int *)(v_rsp - 296 - 128) = 0;
    result = memset(v_rsp - 296 - 32, a2, 264, a4);
    if ((*(unsigned int *)(v_rip + 9602957)) == 0) goto loc_005E05A3;
    a2 = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197))) << (3);
    result = memset(*(unsigned __int64 *)(v_rip + 8945197) + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197)) = 1;
    a2 = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 264)) << (3);
    result = memset(*(unsigned __int64 *)(v_rip + 8945197) + 264 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 264) = 1;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 528)) << (3);
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 296 - 64) = *(unsigned __int64 *)(v_rip + 8945197) + 528 + 8;
    result = memset(*(unsigned __int64 *)(v_rip + 8945197) + 528 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 528) = 1;
    a2 = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 792)) << (3);
    result = memset(*(unsigned __int64 *)(v_rip + 8945197) + 792 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 792) = 1;
    a2 = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 1056)) << (3);
    result = memset(*(unsigned __int64 *)(v_rip + 8945197) + 1056 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 1056) = 1;
    a2 = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 1320)) << (3);
    result = memset(*(unsigned __int64 *)(v_rip + 8945197) + 1320 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 1320) = 1;
    a2 = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 1584)) << (3);
    result = memset(*(unsigned __int64 *)(v_rip + 8945197) + 1584 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 1584) = 1;
    a2 = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 1848)) << (3);
    result = memset(*(unsigned __int64 *)(v_rip + 8945197) + 1848 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 1848) = 1;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 2112)) << (3);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_rip + 8945197) + 2112 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 2112) = 1;
    v_rsi = 0;
    result = ((int)(*(unsigned int *)(v_rip + 9621643))) * ((int)(*(unsigned int *)(v_rip + 9621643)));
    *(unsigned int *)(v_rip + 9602587) = 0;
    result = (result) + (*(unsigned __int64 *)(v_rip + 8553990));
    *(unsigned __int8 *)(v_rip + 9602593) = 0;
    *(unsigned __int64 *)(v_rsp - 296 - 48) = result;
    result = (unsigned int)((*(unsigned __int8 *)(result + 180)) * ((unsigned int)(*(unsigned __int8 *)(result + 180))));
    *(unsigned int *)(v_rsp - 296 - 72) = (unsigned int)(result);
    if (*(unsigned __int64 *)(v_rip + 9602624) != 0) {
        a3 = *(unsigned int *)(v_rip + 10382636);
        a2 = 255;
        a3 = (a3) << (2);
        result = memset(*(unsigned __int64 *)(v_rip + 9602624), a2, a3, a4);
    }
    *(unsigned int *)(v_rsp - 296 - 100) = 0;
    if ((*(unsigned int *)(v_rip + 9602576)) == 0) goto loc_005E056A;
loc_005DFDDB:
    v_rdi = (1) * (0);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rip + 9602541));
    *(unsigned __int64 *)(v_rsp - 296 - 56) = v_rdi;
    if (((*(unsigned __int8 *)(v_rdi + 1184)) & (1)) != 0) goto loc_005E0554;
    result = KiCopyAffinityEx(v_rdi + 576, *(unsigned __int16 *)(v_rdi + 576 + 2), v_rdi + 312, a4);
    *(unsigned __int16 *)(v_rdi + 1252) = 0;
    *(unsigned __int8 *)(v_rdi + 1254) = 0;
    v_rsi = *(unsigned __int16 *)(v_rdi + 1170);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 1170))) >= ((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 1174)))) { v_rsi = (unsigned int)(*(unsigned __int16 *)(v_rdi + 1174)); }
    *(unsigned int *)(v_rsp - 296 - 112) = (unsigned int)(v_rsi);
    result = PpmParkFindOverUtilizedProcessorsEx(v_rdi, (unsigned int)(*(unsigned int *)(v_rsp - 296 - 72)), *(unsigned __int64 *)(v_rip + 8945197) + 792, a4);
    a4 = 0;
    *(unsigned __int8 *)(v_rdi + 1208 + 16) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10375774))) == 0) goto loc_005DFE89;
    a1 = (v_rdi) * ((unsigned int)(*(unsigned int *)(v_rip + 10375774)));
    a2 = 0;
    *(unsigned __int64 *)(v_rdi + 1208) = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rip + 10375774)));
    if ((*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rip + 10375774)))) != (*(unsigned __int64 *)(v_rdi + 1208 + 8))) {
        *(unsigned __int8 *)(v_rdi + 1208 + 16) = 1;
        *(unsigned __int64 *)(v_rdi + 1208 + 8) = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rip + 10375774)));
    }
    *(unsigned int *)(v_rsp - 296 - 116) = 0;
    if ((*(unsigned __int8 *)(v_rdi + 12)) <= 0) goto loc_005E054B;
loc_005DFE9A:
    v_r15 = (0 + 0 * 4) << (7);
    v_r15 = (v_r15) + (*(unsigned __int64 *)(v_rdi + 1288));
    *(unsigned int *)(v_rsp - 296 - 128) = 0;
    result = KiCopyAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 1584, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 1584 + 2), v_r15 + 40, a4);
    result = KeIsEmptyAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 1584, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 1584 + 2), v_r15 + 40, a4);
    if ((unsigned int)(result) != 0) goto loc_005E0548;
    *(unsigned int *)(v_rsp - 296 - 128) = 0x100000ULL;
    if ((*(unsigned __int16 *)(v_rip + 9602238)) <= 1) goto loc_005DFF4D;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197))) << (3);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_rip + 8945197) + 8, a2, a3, a4);
    result = 0;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197)) = 1;
    *(unsigned __int16 *)(v_rsp - 296 - 80) = 0;
    *(unsigned __int64 *)(v_rsp - 296 - 88) = *(unsigned __int64 *)(v_r15 + 304 + 8);
    *(unsigned __int64 *)(v_rsp - 296 - 96) = v_r15 + 304;
    goto loc_005DFF3A;
loc_005DFF1C:
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(v_rsp - 296 - 120)), a2, a3, a4);
    result = KeAddGroupAffinityEx(*(unsigned __int64 *)(v_rip + 8945197), *(unsigned __int8 *)(result + 208), *(unsigned __int64 *)(result + 36448), a4);
loc_005DFF3A:
    result = KeEnumerateNextProcessor(v_rsp - 296 - 120, v_rsp - 296 - 96, *(unsigned __int64 *)(result + 36448), a4);
    if ((unsigned int)(result) == 0) goto loc_005DFF1C;
    goto loc_005DFF5D;
loc_005DFF4D:
    result = KiCopyAffinityEx(*(unsigned __int64 *)(v_rip + 8945197), *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 2), v_r15 + 304, a4);
loc_005DFF5D:
    result = KeAndAffinityEx2(*(unsigned __int64 *)(v_rip + 8945197), *(unsigned __int64 *)(v_rip + 8945197) + 1584, *(unsigned __int64 *)(v_rip + 8945197), a4);
    result = KeIsEmptyAffinityEx(*(unsigned __int64 *)(v_rip + 8945197), *(unsigned __int64 *)(v_rip + 8945197) + 1584, *(unsigned __int64 *)(v_rip + 8945197), a4);
    if ((unsigned int)(result) == 0) {
    }
    result = KeCountSetBitsAffinityEx(*(unsigned __int64 *)(v_rip + 8945197), *(unsigned __int64 *)(v_rip + 8945197) + 1584, *(unsigned __int64 *)(v_rip + 8945197), a4);
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r15)) - ((unsigned int)(result)));
    v_rbx = (unsigned int)((unsigned int)(v_rsi));
    if (((unsigned int)(a1)) <= ((unsigned int)(v_rsi))) { v_rbx = (unsigned int)(a1); }
    v_rsi = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 264)) << (3);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_rip + 8945197) + 264 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 264) = 1;
    if ((*(unsigned __int8 *)(v_rip + 10382093)) != 0) goto loc_005E002C;
    *(unsigned int *)(v_rsp - 296 - 120) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9707503)));
    result = KeCheckProcessorAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 1584, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9707503)))), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_005E002C;
    if ((unsigned int)(v_rbx) == 0) goto loc_005E002C;
    result = KeCheckProcessorAffinityEx(*(unsigned __int64 *)(v_rip + 8945197), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9707503)))), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_005E002C;
    result = KeGetPrcb((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9707503)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9707503)))), a3, a4);
    if ((*(unsigned __int16 *)(v_rip + 9601959)) <= 1) goto loc_005E0015;
    result = KeAddGroupAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 264, *(unsigned __int8 *)(result + 208), *(unsigned __int64 *)(result + 36448), a4);
    goto loc_005E001C;
loc_005E0015:
    result = KeAddProcessorAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 264, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9707503)))), *(unsigned __int64 *)(result + 36448), a4);
loc_005E001C:
    result = KeCountSetBitsAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 264, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9707503)))), *(unsigned __int64 *)(result + 36448), a4);
loc_005E002C:
    a2 = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 528)) << (3);
    result = memset(*(unsigned __int64 *)(v_rip + 8945197) + 528 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8945197) + 528) = 1;
    result = KeCpuSetQueryUnparkRecommendationEx(*(unsigned __int64 *)(v_rip + 8945197) + 1584, *(unsigned __int64 *)(v_rip + 8945197) + 528, a3, a4);
    result = 0;
    *(unsigned int *)(v_rsp - 296 - 108) = (unsigned int)((unsigned __int16)(result));
    if ((unsigned int)((unsigned __int16)(result)) == 0) goto loc_005E0173;
    if ((*(unsigned __int16 *)(v_rip + 9601838)) <= ((unsigned __int16)(result + 1))) goto loc_005E00E4;
    *(unsigned __int16 *)(v_rsp - 296 - 80) = 0;
    *(unsigned __int64 *)(v_rsp - 296 - 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 296 - 64));
    *(unsigned __int64 *)(v_rsp - 296 - 96) = *(unsigned __int64 *)(v_rip + 8945197) + 528;
    result = KeEnumerateNextProcessor(v_rsp - 296 - 120, v_rsp - 296 - 96, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_005E00D7;
loc_005E00A1:
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(v_rsp - 296 - 120)), v_rsp - 296 - 96, a3, a4);
    result = KeAddGroupAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 528, *(unsigned __int8 *)(result + 208), *(unsigned __int64 *)(result + 36448), a4);
    result = KeEnumerateNextProcessor(v_rsp - 296 - 120, v_rsp - 296 - 96, *(unsigned __int64 *)(result + 36448), a4);
    if ((unsigned int)(result) == 0) goto loc_005E00A1;
loc_005E00D7:
    result = KeCountSetBitsAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 528, v_rsp - 296 - 96, *(unsigned __int64 *)(result + 36448), a4);
    *(unsigned int *)(v_rsp - 296 - 108) = (unsigned int)(result);
    result = 0;
loc_005E00E4:
    *(unsigned __int64 *)(v_rsp - 296 - 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8945197) + 528 + 8);
    *(unsigned __int16 *)(v_rsp - 296 - 80) = 0;
    *(unsigned __int64 *)(v_rsp - 296 - 96) = *(unsigned __int64 *)(v_rip + 8945197) + 528;
    result = KeEnumerateNextProcessor(v_rsp - 296 - 120, v_rsp - 296 - 96, *(unsigned __int64 *)(result + 36448), a4);
    if ((unsigned int)(result) != 0) goto loc_005E0171;
loc_005E0108:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) >= ((unsigned int)(v_rbx))) goto loc_005E015C;
    result = KeCheckProcessorAffinityEx(*(unsigned __int64 *)(v_rip + 8945197), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 296 - 120)))), *(unsigned __int64 *)(result + 36448), a4);
    if ((unsigned int)(result) != 0) goto loc_005E015C;
    result = KeGetPrcb((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 296 - 120)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 296 - 120)))), *(unsigned __int64 *)(result + 36448), a4);
    if ((*(unsigned __int16 *)(v_rip + 9601654)) <= ((unsigned __int16)(result + 1))) goto loc_005E0146;
    result = KeAddGroupAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 264, *(unsigned __int8 *)(result + 208), *(unsigned __int64 *)(result + 36448), a4);
    goto loc_005E014D;
loc_005E0146:
    result = KeAddProcessorAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 264, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 296 - 120)))), *(unsigned __int64 *)(result + 36448), a4);
loc_005E014D:
    result = KeCountSetBitsAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 264, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 296 - 120)))), *(unsigned __int64 *)(result + 36448), a4);
loc_005E015C:
    result = KeEnumerateNextProcessor(v_rsp - 296 - 120, v_rsp - 296 - 96, *(unsigned __int64 *)(result + 36448), a4);
    if ((unsigned int)(result) == 0) goto loc_005E0108;
loc_005E0171:
    result = 0;
loc_005E0173:
    *(unsigned __int8 *)(v_rsp - 296 - 123) = 0;
    *(unsigned int *)(v_rsp - 296 - 104) = 3;
    result = Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline(v_rsp - 296 - 120, v_rsp - 296 - 96, *(unsigned __int64 *)(result + 36448), a4);
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_005E0213;
    result = KeIsEmptyAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 264, a2, *(unsigned __int64 *)(result + 36448), a4);
    a2 = 0;
    if ((unsigned int)(result) != 0) goto loc_005E0213;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10374780)))) & (8)) == 0) goto loc_005E0213;
    *(unsigned __int64 *)(v_rsp - 296 - 32) = 0x200001ULL;
    result = memset(v_rsp - 296 - 24, a2, 256, a4);
    a3 = (256) * ((int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 296 - 56) + 1280) + 4)));
    a3 = (a3) + (16);
    a3 = (a3) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 296 - 56) + 1280));
    result = KiCopyAffinityEx(v_rsp - 296 - 32, *(unsigned __int16 *)(v_rsp - 296 - 30), a3, a4);
    result = KeIsSubsetAffinityEx(*(unsigned __int64 *)(v_rip + 8945197) + 264, v_rsp - 296 - 32, a3, a4);
    a2 = 0;
    if ((unsigned int)(result) == 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 296 - 56) + 1280);
        *(unsigned __int8 *)(v_rsp - 296 - 123) = (unsigned __int8)(a2 + 1);
        a1 = *(unsigned int *)(result + 4);
        *(unsigned int *)(v_rsp - 296 - 104) = (unsigned int)(a1);
        *(unsigned int *)(result + 4) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) >= ((unsigned int)(*(unsigned __int16 *)(v_r15 + 2)))) goto loc_005E0239;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) >= ((unsigned int)(v_rbx))) goto loc_005E0239;
    v_r14 = (unsigned int)((unsigned int)(v_rbx));
    if (((unsigned int)(*(unsigned __int16 *)(v_r15 + 2))) < ((unsigned int)(v_rbx))) { v_r14 = (unsigned int)(*(unsigned __int16 *)(v_r15 + 2)); }
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 296 - 128))) | (4));
    *(unsigned int *)(v_rsp - 296 - 128) = (unsigned int)(a3);
    goto loc_005E023D;
loc_005E0239:
loc_005E023D:
    if (((unsigned int)(v_rbx)) <= ((unsigned int)(*(unsigned __int16 *)(v_r15 + 4)))) goto loc_005E025E;
    v_rsi = (unsigned int)((unsigned int)(v_rbx));
    if (((unsigned int)(v_r14)) < ((unsigned int)(v_rbx))) {
        a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 296 - 128))) | (8));
        v_rsi = (unsigned int)(*(unsigned __int16 *)(v_r15 + 4));
        *(unsigned int *)(v_rsp - 296 - 128) = (unsigned int)(a3);
        if (((unsigned int)(*(unsigned __int16 *)(v_r15 + 4))) <= ((unsigned int)(v_r14))) { v_rsi = (unsigned int)(v_r14); }
    }
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10374584))) & (8));
    result = *(unsigned __int16 *)(v_r15 + 4);
    v_r11 = 0;
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 296 - 56) + 1280);
        result = (int)(*(unsigned int *)(a1 + 4));
        v_r11 = *(unsigned __int16 *)(a1 + result * 2 + 8);
    }
    v_r10 = *(unsigned __int16 *)(v_r15 + 6);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r15 + 6))) >= ((unsigned __int16)(*(unsigned __int16 *)(v_r15)))) { v_r10 = (unsigned int)(*(unsigned __int16 *)(v_r15)); }
    if ((*(unsigned int *)(v_rip + 9613239)) == 0) goto loc_005E02D2;
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rsp - 296 - 116))));
    a1 = -(a1);
    a2 = (unsigned int)((*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_rsp - 296 - 48) * 1 + 137)) * ((unsigned int)(*(unsigned __int16 *)(v_r15))));
    a2 = (unsigned int)((a2) + (50));
    a2 = (unsigned int)((a2) >> (5));
    if (a2 >= = ((unsigned int)(v_r10))) {
        a3 = (unsigned int)((a3) | (64));
        a4 = a2;
        *(unsigned int *)(v_rsp - 296 - 128) = (unsigned int)(a3);
    }
    result = *(unsigned __int16 *)(v_rip + 9601225);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 9601225))) >= = 1) {
        a1 = (unsigned int)(*(unsigned __int16 *)(v_rip + 9601225));
        a2 = 0;
        result = (unsigned int)((*(unsigned __int16 *)(v_rip + 9601225)) - 1);
        a4 = (unsigned int)((a4) + ((unsigned int)(result)));
        result = a4;
        a4 = (unsigned int)((a4) - (0));
    }
    a1 = 0;
    if ((unsigned int)(v_rbx) == 0) goto loc_005E0313;
    if ((unsigned __int16)(v_r11) == 0) goto loc_005E0313;
    if (((unsigned __int16)(v_r11)) < ((unsigned __int16)(a4))) {
        a4 = (unsigned __int16)(v_r11);
        *(unsigned int *)(v_rsp - 296 - 128) = (unsigned int)(a3);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 296 - 108))) + (a4));
    *(unsigned __int16 *)(v_r15 + 8) = (unsigned __int16)(a4);
    if (((unsigned int)(result)) >= ((unsigned int)(v_rsi))) { result = (unsigned int)(v_rsi); }
    v_r12 = (unsigned int)((unsigned int)(v_r14));
    if (((unsigned int)(result)) > ((unsigned int)(v_r14))) { v_r12 = (unsigned int)(result); }
    *(unsigned __int16 *)(v_r15 + 10) = (unsigned __int16)(v_r12);
    if ((*(unsigned __int8 *)(v_rip + 10381243)) != 0) goto loc_005E0347;
    goto loc_005E035B;
loc_005E0347:
    v_rsi = (unsigned int)((unsigned int)(v_r12));
    if ((unsigned int)(v_rbx) != 0) {
        result = (unsigned __int16)(v_r11);
        if (((unsigned int)((unsigned int)((unsigned int)(v_r12)))) < ((unsigned int)(result))) { result = (unsigned int)((unsigned int)((unsigned int)(v_r12))); }
        v_rsi = (unsigned int)(result);
    }
    *(unsigned __int8 *)(v_rsp - 296 - 124) = 0;
    v_rbx = 0;
    v_r15 = 0;
    if ((*(unsigned __int8 *)(v_rip + 10381093)) != 0) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 296 - 56) + 1270);
        v_r15 = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 296 - 56) + 1264);
        v_rbx = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 296 - 56) + 1271);
        *(unsigned __int8 *)(v_rsp - 296 - 124) = (unsigned __int8)(result);
    }
    result = KeAndAffinityEx2(*(unsigned __int64 *)(v_rip + 8945197) + 1584, *(unsigned __int64 *)(v_rip + 8945197) + 792, *(unsigned __int64 *)(v_rip + 8945197) + 1056, a4);
    v_stack_m1B0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 296 - 116)));
    v_stack_m1B8 = (unsigned __int8)(v_rbx);
    v_stack_m1C0 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 296 - 124));
    v_stack_m1C8 = (unsigned int)(v_r15);
    v_stack_m1D0 = *(unsigned __int64 *)(v_rsp - 296 - 56) + 1208;
    v_stack_m1D8 = v_rsp - 296 - 128;
    v_stack_m1E0 = *(unsigned __int64 *)(v_rip + 8945197) + 1848;
    v_stack_m1E8 = *(unsigned __int64 *)(v_rip + 8945197) + 1320;
    v_stack_m1F0 = *(unsigned __int64 *)(v_rip + 8945197) + 264;
    v_stack_m1F8 = *(unsigned __int64 *)(v_rip + 8945197);
    v_stack_m200 = (unsigned int)(v_rsi);
    v_stack_m208 = (unsigned int)(v_r12);
    result = PpmParkComputeUnparkMaskEx(*(unsigned __int64 *)(v_rsp - 296 - 56), *(unsigned __int64 *)(v_rip + 8945197) + 1584, *(unsigned __int64 *)(v_rsp - 296 - 56) + 576, *(unsigned __int64 *)(v_rip + 8945197) + 1056);
    result = Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_rsp - 296 - 56), *(unsigned __int64 *)(v_rip + 8945197) + 1584, *(unsigned __int64 *)(v_rsp - 296 - 56) + 576, *(unsigned __int64 *)(v_rip + 8945197) + 1056);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_005E0437;
    if ((*(unsigned __int8 *)(v_rsp - 296 - 123)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 296 - 56) + 1280);
        a1 = *(unsigned int *)(v_rsp - 296 - 104);
        *(unsigned int *)(result + 4) = (unsigned int)(a1);
    }
    result = KeSubtractAffinityEx2(*(unsigned __int64 *)(v_rip + 8945197) + 1584, *(unsigned __int64 *)(v_rip + 8945197) + 1320, *(unsigned __int64 *)(v_rip + 8945197) + 2112, *(unsigned __int64 *)(v_rip + 8945197) + 1056);
    result = KeSubtractAffinityEx2(*(unsigned __int64 *)(v_rip + 8945197) + 2112, *(unsigned __int64 *)(v_rip + 8945197) + 1848, *(unsigned __int64 *)(v_rip + 8945197) + 2112, *(unsigned __int64 *)(v_rip + 8945197) + 1056);
    result = KeSubtractAffinityEx2(*(unsigned __int64 *)(v_rsp - 296 - 56) + 312, *(unsigned __int64 *)(v_rip + 8945197) + 1584, *(unsigned __int64 *)(v_rsp - 296 - 56) + 312, *(unsigned __int64 *)(v_rip + 8945197) + 1056);
    result = KeOrAffinityEx2(*(unsigned __int64 *)(v_rsp - 296 - 56) + 312, *(unsigned __int64 *)(v_rip + 8945197) + 1320, *(unsigned __int64 *)(v_rsp - 296 - 56) + 312, *(unsigned __int64 *)(v_rip + 8945197) + 1056);
    result = KeOrAffinityEx2(*(unsigned __int64 *)(v_rsp - 296 - 56) + 312, *(unsigned __int64 *)(v_rip + 8945197) + 1848, *(unsigned __int64 *)(v_rsp - 296 - 56) + 312, *(unsigned __int64 *)(v_rip + 8945197) + 1056);
    result = KeSubtractAffinityEx2(*(unsigned __int64 *)(v_rsp - 296 - 56) + 840, *(unsigned __int64 *)(v_rip + 8945197) + 1584, *(unsigned __int64 *)(v_rsp - 296 - 56) + 840, *(unsigned __int64 *)(v_rip + 8945197) + 1056);
    result = KeOrAffinityEx2(*(unsigned __int64 *)(v_rsp - 296 - 56) + 840, *(unsigned __int64 *)(v_rip + 8945197) + 1848, *(unsigned __int64 *)(v_rsp - 296 - 56) + 840, *(unsigned __int64 *)(v_rip + 8945197) + 1056);
    v_stack_m1D8 = (unsigned int)(v_r15);
    v_stack_m1E0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 296 - 128)));
    v_stack_m1E8 = *(unsigned __int64 *)(v_rip + 8945197) + 528;
    v_stack_m1F0 = *(unsigned __int64 *)(v_rip + 8945197) + 1056;
    v_stack_m1F8 = *(unsigned __int64 *)(v_rip + 8945197) + 264;
    v_stack_m200 = *(unsigned __int64 *)(v_rip + 8945197);
    v_stack_m208 = (unsigned __int16)(v_r14);
    result = PpmEventTraceSoftCoreParkingSelectionEx(*(unsigned __int64 *)(v_rsp - 296 - 56), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 296 - 116)))), (unsigned __int16)(v_r12), (unsigned __int16)(v_rsi));
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 296 - 116))) + 1);
    *(unsigned int *)(v_rsp - 296 - 116) = (unsigned int)(v_r15);
    if (((unsigned int)(v_r15)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 296 - 56) + 12)))) goto loc_005DFE9A;
loc_005E0548:
loc_005E054B:
    v_rsi = 0;
loc_005E0554:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 296 - 100))) + (1));
    *(unsigned int *)(v_rsp - 296 - 100) = (unsigned int)(v_rbx);
    if (((unsigned int)(v_rbx)) < (*(unsigned int *)(v_rip + 9600639))) goto loc_005DFDDB;
loc_005E056A:
    result = PpmParkComputeDiff(*(unsigned __int64 *)(v_rsp - 296 - 56), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 296 - 116)))), (unsigned __int16)(v_r12), 0);
    a2 = ((*(unsigned int *)(v_rip + 8942795)) > 0) ? 1 : 0;
    if ((*(unsigned int *)(v_rip + 8942780)) != a2) goto loc_005E058C;
    result = 0;
    if ((*(unsigned int *)(v_rip + 8942784)) != 0) {
        result = 1;
    }
    *(unsigned int *)(v_rip + 8942760) = a2;
    *(unsigned int *)(v_rip + 8942766) = 0;
    if ((unsigned int)(result) != 0) {
        result = PpmEventLPICoreParking(*(unsigned __int64 *)(v_rsp - 296 - 56), a2, (unsigned __int16)(v_r12), 0);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 296 + 240)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned __int16)(v_r12), 0);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmParkCalculateCoreParkingMaskEx(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m1B0;
    uint8_t v_stack_m1B8;
    uint8_t v_stack_m1C0;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint32_t v_stack_m200;
    uint32_t v_stack_m208;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (512);
    result = (*(uint64_t *)(v_rip + 0x82AB33)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x128 + 0xF0) = result;
    result = 0;
    local_rbx = 0;
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x128 - 0x50) = 0;
    *(uint32_t *)(local_rsp - 0x128 - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0x128 - 0x60) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x128 - 0x80) = 0;
    result = memset(local_rsp - 296 - 32, Arg2, 264, Arg4);
    if ((*(uint32_t *)(v_rip + 0x92878D)) == 0) goto loc_005E05A3;
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D))) << (3);
    result = memset(*(uint64_t *)(v_rip + 0x887E2D) + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D)) = 1;
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x108)) << (3);
    result = memset(*(uint64_t *)(v_rip + 0x887E2D) + 264 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x108) = 1;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x210)) << (3);
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x128 - 0x40) = *(uint64_t *)(v_rip + 0x887E2D) + 528 + 8;
    result = memset(*(uint64_t *)(v_rip + 0x887E2D) + 528 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x210) = 1;
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x318)) << (3);
    result = memset(*(uint64_t *)(v_rip + 0x887E2D) + 792 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x318) = 1;
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x420)) << (3);
    result = memset(*(uint64_t *)(v_rip + 0x887E2D) + 1056 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x420) = 1;
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x528)) << (3);
    result = memset(*(uint64_t *)(v_rip + 0x887E2D) + 1320 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x528) = 1;
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x630)) << (3);
    result = memset(*(uint64_t *)(v_rip + 0x887E2D) + 1584 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x630) = 1;
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x738)) << (3);
    result = memset(*(uint64_t *)(v_rip + 0x887E2D) + 1848 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x738) = 1;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x840)) << (3);
    Arg2 = 0;
    result = memset(*(uint64_t *)(v_rip + 0x887E2D) + 2112 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x840) = 1;
    local_rsi = 0;
    result = ((int32_t)(*(uint32_t *)(v_rip + 0x92D08B))) * ((int32_t)(*(uint32_t *)(v_rip + 0x92D08B)));
    *(uint32_t *)(v_rip + 0x92861B) = 0;
    result = (result) + (*(uint64_t *)(v_rip + 0x828606));
    *(uint8_t *)(v_rip + 0x928621) = 0;
    *(uint64_t *)(local_rsp - 0x128 - 0x30) = result;
    result = (uint32_t)((*(uint8_t *)(result + 0xB4)) * ((uint32_t)(*(uint8_t *)(result + 0xB4))));
    *(uint32_t *)(local_rsp - 0x128 - 0x48) = (uint32_t)(result);
    if (*(uint64_t *)(v_rip + 0x928640) != 0) {
        Arg3 = *(uint32_t *)(v_rip + 0x9E6D2C);
        Arg2 = 255;
        Arg3 = (Arg3) << (2);
        result = memset(*(uint64_t *)(v_rip + 0x928640), Arg2, Arg3, Arg4);
    }
    *(uint32_t *)(local_rsp - 0x128 - 0x64) = 0;
    if ((*(uint32_t *)(v_rip + 0x928610)) == 0) goto loc_005E056A;
loc_005DFDDB:
    local_rdi = (1) * (0);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_rip + 0x9285ED));
    *(uint64_t *)(local_rsp - 0x128 - 0x38) = local_rdi;
    if (((*(uint8_t *)(local_rdi + 0x4A0)) & (1)) != 0) goto loc_005E0554;
    result = KiCopyAffinityEx(local_rdi + 576, *(uint16_t *)(local_rdi + 0x240 + 0x2), local_rdi + 312, Arg4);
    *(uint16_t *)(local_rdi + 0x4E4) = 0;
    *(uint8_t *)(local_rdi + 0x4E6) = 0;
    local_rsi = *(uint16_t *)(local_rdi + 0x492);
    if (((uint16_t)(*(uint16_t *)(local_rdi + 0x492))) >= ((uint16_t)(*(uint16_t *)(local_rdi + 0x496)))) { local_rsi = (uint32_t)(*(uint16_t *)(local_rdi + 0x496)); }
    *(uint32_t *)(local_rsp - 0x128 - 0x70) = (uint32_t)(local_rsi);
    result = PpmParkFindOverUtilizedProcessorsEx(local_rdi, (uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x48)), *(uint64_t *)(v_rip + 0x887E2D) + 792, Arg4);
    Arg4 = 0;
    *(uint8_t *)(local_rdi + 0x4B8 + 0x10) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9E525E))) == 0) goto loc_005DFE89;
    Arg1 = (local_rdi) * ((uint32_t)(*(uint32_t *)(v_rip + 0x9E525E)));
    Arg2 = 0;
    *(uint64_t *)(local_rdi + 0x4B8) = *(uint64_t *)((uint32_t)(*(uint32_t *)(v_rip + 0x9E525E)));
    if ((*(uint64_t *)((uint32_t)(*(uint32_t *)(v_rip + 0x9E525E)))) != (*(uint64_t *)(local_rdi + 0x4B8 + 0x8))) {
        *(uint8_t *)(local_rdi + 0x4B8 + 0x10) = 1;
        *(uint64_t *)(local_rdi + 0x4B8 + 0x8) = *(uint64_t *)((uint32_t)(*(uint32_t *)(v_rip + 0x9E525E)));
    }
    *(uint32_t *)(local_rsp - 0x128 - 0x74) = 0;
    if ((*(uint8_t *)(local_rdi + 0xC)) <= 0) goto loc_005E054B;
loc_005DFE9A:
    local_r15 = (0 + 0 * 4) << (7);
    local_r15 = (local_r15) + (*(uint64_t *)(local_rdi + 0x508));
    *(uint32_t *)(local_rsp - 0x128 - 0x80) = 0;
    result = KiCopyAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 1584, *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x630 + 0x2), local_r15 + 40, Arg4);
    result = KeIsEmptyAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 1584, *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x630 + 0x2), local_r15 + 40, Arg4);
    if ((uint32_t)(result) != 0) goto loc_005E0548;
    *(uint32_t *)(local_rsp - 0x128 - 0x80) = 0x100000ULL;
    if ((*(uint16_t *)(v_rip + 0x9284BE)) <= 1) goto loc_005DFF4D;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D))) << (3);
    Arg2 = 0;
    result = memset(*(uint64_t *)(v_rip + 0x887E2D) + 8, Arg2, Arg3, Arg4);
    result = 0;
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D)) = 1;
    *(uint16_t *)(local_rsp - 0x128 - 0x50) = 0;
    *(uint64_t *)(local_rsp - 0x128 - 0x58) = *(uint64_t *)(local_r15 + 0x130 + 0x8);
    *(uint64_t *)(local_rsp - 0x128 - 0x60) = local_r15 + 304;
    goto loc_005DFF3A;
loc_005DFF1C:
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x78)), Arg2, Arg3, Arg4);
    result = KeAddGroupAffinityEx(*(uint64_t *)(v_rip + 0x887E2D), *(uint8_t *)(result + 0xD0), *(uint64_t *)(result + 0x8E60), Arg4);
loc_005DFF3A:
    result = KeEnumerateNextProcessor(local_rsp - 296 - 120, local_rsp - 296 - 96, *(uint64_t *)(result + 0x8E60), Arg4);
    if ((uint32_t)(result) == 0) goto loc_005DFF1C;
    goto loc_005DFF5D;
loc_005DFF4D:
    result = KiCopyAffinityEx(*(uint64_t *)(v_rip + 0x887E2D), *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x2), local_r15 + 304, Arg4);
loc_005DFF5D:
    result = KeAndAffinityEx2(*(uint64_t *)(v_rip + 0x887E2D), *(uint64_t *)(v_rip + 0x887E2D) + 1584, *(uint64_t *)(v_rip + 0x887E2D), Arg4);
    result = KeIsEmptyAffinityEx(*(uint64_t *)(v_rip + 0x887E2D), *(uint64_t *)(v_rip + 0x887E2D) + 1584, *(uint64_t *)(v_rip + 0x887E2D), Arg4);
    if ((uint32_t)(result) == 0) {
    }
    result = KeCountSetBitsAffinityEx(*(uint64_t *)(v_rip + 0x887E2D), *(uint64_t *)(v_rip + 0x887E2D) + 1584, *(uint64_t *)(v_rip + 0x887E2D), Arg4);
    Arg1 = (uint32_t)((*(uint16_t *)(local_r15)) - ((uint32_t)(result)));
    local_rbx = (uint32_t)((uint32_t)(local_rsi));
    if (((uint32_t)(Arg1)) <= ((uint32_t)(local_rsi))) { local_rbx = (uint32_t)(Arg1); }
    local_rsi = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x108)) << (3);
    Arg2 = 0;
    result = memset(*(uint64_t *)(v_rip + 0x887E2D) + 264 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x108) = 1;
    if ((*(uint8_t *)(v_rip + 0x9E6B0D)) != 0) goto loc_005E002C;
    *(uint32_t *)(local_rsp - 0x128 - 0x78) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x941FEF)));
    result = KeCheckProcessorAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 1584, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x941FEF)))), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_005E002C;
    if ((uint32_t)(local_rbx) == 0) goto loc_005E002C;
    result = KeCheckProcessorAffinityEx(*(uint64_t *)(v_rip + 0x887E2D), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x941FEF)))), Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_005E002C;
    result = KeGetPrcb((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x941FEF)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x941FEF)))), Arg3, Arg4);
    if ((*(uint16_t *)(v_rip + 0x9283A7)) <= 1) goto loc_005E0015;
    result = KeAddGroupAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 264, *(uint8_t *)(result + 0xD0), *(uint64_t *)(result + 0x8E60), Arg4);
    goto loc_005E001C;
loc_005E0015:
    result = KeAddProcessorAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 264, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x941FEF)))), *(uint64_t *)(result + 0x8E60), Arg4);
loc_005E001C:
    result = KeCountSetBitsAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 264, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x941FEF)))), *(uint64_t *)(result + 0x8E60), Arg4);
loc_005E002C:
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x210)) << (3);
    result = memset(*(uint64_t *)(v_rip + 0x887E2D) + 528 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x210) = 1;
    result = KeCpuSetQueryUnparkRecommendationEx(*(uint64_t *)(v_rip + 0x887E2D) + 1584, *(uint64_t *)(v_rip + 0x887E2D) + 528, Arg3, Arg4);
    result = 0;
    *(uint32_t *)(local_rsp - 0x128 - 0x6C) = (uint32_t)((uint16_t)(result));
    if ((uint32_t)((uint16_t)(result)) == 0) goto loc_005E0173;
    if ((*(uint16_t *)(v_rip + 0x92832E)) <= ((uint16_t)(result + 1))) goto loc_005E00E4;
    *(uint16_t *)(local_rsp - 0x128 - 0x50) = 0;
    *(uint64_t *)(local_rsp - 0x128 - 0x58) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x128 - 0x40));
    *(uint64_t *)(local_rsp - 0x128 - 0x60) = *(uint64_t *)(v_rip + 0x887E2D) + 528;
    result = KeEnumerateNextProcessor(local_rsp - 296 - 120, local_rsp - 296 - 96, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_005E00D7;
loc_005E00A1:
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x78)), local_rsp - 296 - 96, Arg3, Arg4);
    result = KeAddGroupAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 528, *(uint8_t *)(result + 0xD0), *(uint64_t *)(result + 0x8E60), Arg4);
    result = KeEnumerateNextProcessor(local_rsp - 296 - 120, local_rsp - 296 - 96, *(uint64_t *)(result + 0x8E60), Arg4);
    if ((uint32_t)(result) == 0) goto loc_005E00A1;
loc_005E00D7:
    result = KeCountSetBitsAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 528, local_rsp - 296 - 96, *(uint64_t *)(result + 0x8E60), Arg4);
    *(uint32_t *)(local_rsp - 0x128 - 0x6C) = (uint32_t)(result);
    result = 0;
loc_005E00E4:
    *(uint64_t *)(local_rsp - 0x128 - 0x58) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x887E2D) + 0x210 + 0x8);
    *(uint16_t *)(local_rsp - 0x128 - 0x50) = 0;
    *(uint64_t *)(local_rsp - 0x128 - 0x60) = *(uint64_t *)(v_rip + 0x887E2D) + 528;
    result = KeEnumerateNextProcessor(local_rsp - 296 - 120, local_rsp - 296 - 96, *(uint64_t *)(result + 0x8E60), Arg4);
    if ((uint32_t)(result) != 0) goto loc_005E0171;
loc_005E0108:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) >= ((uint32_t)(local_rbx))) goto loc_005E015C;
    result = KeCheckProcessorAffinityEx(*(uint64_t *)(v_rip + 0x887E2D), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x78)))), *(uint64_t *)(result + 0x8E60), Arg4);
    if ((uint32_t)(result) != 0) goto loc_005E015C;
    result = KeGetPrcb((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x78)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x78)))), *(uint64_t *)(result + 0x8E60), Arg4);
    if ((*(uint16_t *)(v_rip + 0x928276)) <= ((uint16_t)(result + 1))) goto loc_005E0146;
    result = KeAddGroupAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 264, *(uint8_t *)(result + 0xD0), *(uint64_t *)(result + 0x8E60), Arg4);
    goto loc_005E014D;
loc_005E0146:
    result = KeAddProcessorAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 264, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x78)))), *(uint64_t *)(result + 0x8E60), Arg4);
loc_005E014D:
    result = KeCountSetBitsAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 264, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x78)))), *(uint64_t *)(result + 0x8E60), Arg4);
loc_005E015C:
    result = KeEnumerateNextProcessor(local_rsp - 296 - 120, local_rsp - 296 - 96, *(uint64_t *)(result + 0x8E60), Arg4);
    if ((uint32_t)(result) == 0) goto loc_005E0108;
loc_005E0171:
    result = 0;
loc_005E0173:
    *(uint8_t *)(local_rsp - 0x128 - 0x7B) = 0;
    *(uint32_t *)(local_rsp - 0x128 - 0x68) = 3;
    result = Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline(local_rsp - 296 - 120, local_rsp - 296 - 96, *(uint64_t *)(result + 0x8E60), Arg4);
    Arg2 = 0;
    if ((uint32_t)(result) == 0) goto loc_005E0213;
    result = KeIsEmptyAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 264, Arg2, *(uint64_t *)(result + 0x8E60), Arg4);
    Arg2 = 0;
    if ((uint32_t)(result) != 0) goto loc_005E0213;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9E4E7C)))) & (8)) == 0) goto loc_005E0213;
    *(uint64_t *)(local_rsp - 0x128 - 0x20) = 0x200001ULL;
    result = memset(local_rsp - 296 - 24, Arg2, 256, Arg4);
    Arg3 = (256) * ((int32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 0x500) + 0x4)));
    Arg3 = (Arg3) + (16);
    Arg3 = (Arg3) + (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 0x500));
    result = KiCopyAffinityEx(local_rsp - 296 - 32, *(uint16_t *)(local_rsp - 0x128 - 0x1E), Arg3, Arg4);
    result = KeIsSubsetAffinityEx(*(uint64_t *)(v_rip + 0x887E2D) + 264, local_rsp - 296 - 32, Arg3, Arg4);
    Arg2 = 0;
    if ((uint32_t)(result) == 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 0x500);
        *(uint8_t *)(local_rsp - 0x128 - 0x7B) = (uint8_t)(Arg2 + 1);
        Arg1 = *(uint32_t *)(result + 0x4);
        *(uint32_t *)(local_rsp - 0x128 - 0x68) = (uint32_t)(Arg1);
        *(uint32_t *)(result + 0x4) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) >= ((uint32_t)(*(uint16_t *)(local_r15 + 0x2)))) goto loc_005E0239;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) >= ((uint32_t)(local_rbx))) goto loc_005E0239;
    local_r14 = (uint32_t)((uint32_t)(local_rbx));
    if (((uint32_t)(*(uint16_t *)(local_r15 + 0x2))) < ((uint32_t)(local_rbx))) { local_r14 = (uint32_t)(*(uint16_t *)(local_r15 + 0x2)); }
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x80))) | (4));
    *(uint32_t *)(local_rsp - 0x128 - 0x80) = (uint32_t)(Arg3);
    goto loc_005E023D;
loc_005E0239:
loc_005E023D:
    if (((uint32_t)(local_rbx)) <= ((uint32_t)(*(uint16_t *)(local_r15 + 0x4)))) goto loc_005E025E;
    local_rsi = (uint32_t)((uint32_t)(local_rbx));
    if (((uint32_t)(local_r14)) < ((uint32_t)(local_rbx))) {
        Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x80))) | (8));
        local_rsi = (uint32_t)(*(uint16_t *)(local_r15 + 0x4));
        *(uint32_t *)(local_rsp - 0x128 - 0x80) = (uint32_t)(Arg3);
        if (((uint32_t)(*(uint16_t *)(local_r15 + 0x4))) <= ((uint32_t)(local_r14))) { local_rsi = (uint32_t)(local_r14); }
    }
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9E4DB8))) & (8));
    result = *(uint16_t *)(local_r15 + 0x4);
    local_r11 = 0;
    if (!(condition_is_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 0x500);
        result = (int32_t)(*(uint32_t *)(Arg1 + 0x4));
        local_r11 = *(uint16_t *)(Arg1 + result * 2 + 0x8);
    }
    local_r10 = *(uint16_t *)(local_r15 + 0x6);
    if (((uint16_t)(*(uint16_t *)(local_r15 + 0x6))) >= ((uint16_t)(*(uint16_t *)(local_r15)))) { local_r10 = (uint32_t)(*(uint16_t *)(local_r15)); }
    if ((*(uint32_t *)(v_rip + 0x92AFB7)) == 0) goto loc_005E02D2;
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x74))));
    Arg1 = -(Arg1);
    Arg2 = (uint32_t)((*(uint8_t *)(Arg1 + *(uint64_t *)(local_rsp - 0x128 - 0x30) * 1 + 0x89)) * ((uint32_t)(*(uint16_t *)(local_r15))));
    Arg2 = (uint32_t)((Arg2) + (50));
    Arg2 = (uint32_t)((Arg2) >> (5));
    if (Arg2 >= = ((uint32_t)(local_r10))) {
        Arg3 = (uint32_t)((Arg3) | (64));
        Arg4 = Arg2;
        *(uint32_t *)(local_rsp - 0x128 - 0x80) = (uint32_t)(Arg3);
    }
    result = *(uint16_t *)(v_rip + 0x9280C9);
    if (((uint16_t)(*(uint16_t *)(v_rip + 0x9280C9))) >= = 1) {
        Arg1 = (uint32_t)(*(uint16_t *)(v_rip + 0x9280C9));
        Arg2 = 0;
        result = (uint32_t)((*(uint16_t *)(v_rip + 0x9280C9)) - 1);
        Arg4 = (uint32_t)((Arg4) + ((uint32_t)(result)));
        result = Arg4;
        Arg4 = (uint32_t)((Arg4) - (0));
    }
    Arg1 = 0;
    if ((uint32_t)(local_rbx) == 0) goto loc_005E0313;
    if ((uint16_t)(local_r11) == 0) goto loc_005E0313;
    if (((uint16_t)(local_r11)) < ((uint16_t)(Arg4))) {
        Arg4 = (uint16_t)(local_r11);
        *(uint32_t *)(local_rsp - 0x128 - 0x80) = (uint32_t)(Arg3);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x6C))) + (Arg4));
    *(uint16_t *)(local_r15 + 0x8) = (uint16_t)(Arg4);
    if (((uint32_t)(result)) >= ((uint32_t)(local_rsi))) { result = (uint32_t)(local_rsi); }
    local_r12 = (uint32_t)((uint32_t)(local_r14));
    if (((uint32_t)(result)) > ((uint32_t)(local_r14))) { local_r12 = (uint32_t)(result); }
    *(uint16_t *)(local_r15 + 0xA) = (uint16_t)(local_r12);
    if ((*(uint8_t *)(v_rip + 0x9E67BB)) != 0) goto loc_005E0347;
    goto loc_005E035B;
loc_005E0347:
    local_rsi = (uint32_t)((uint32_t)(local_r12));
    if ((uint32_t)(local_rbx) != 0) {
        result = (uint16_t)(local_r11);
        if (((uint32_t)((uint32_t)((uint32_t)(local_r12)))) < ((uint32_t)(result))) { result = (uint32_t)((uint32_t)((uint32_t)(local_r12))); }
        local_rsi = (uint32_t)(result);
    }
    *(uint8_t *)(local_rsp - 0x128 - 0x7C) = 0;
    local_rbx = 0;
    local_r15 = 0;
    if ((*(uint8_t *)(v_rip + 0x9E6725)) != 0) {
        result = *(uint8_t *)(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 0x4F6);
        local_r15 = *(uint16_t *)(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 0x4F0);
        local_rbx = *(uint8_t *)(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 0x4F7);
        *(uint8_t *)(local_rsp - 0x128 - 0x7C) = (uint8_t)(result);
    }
    result = KeAndAffinityEx2(*(uint64_t *)(v_rip + 0x887E2D) + 1584, *(uint64_t *)(v_rip + 0x887E2D) + 792, *(uint64_t *)(v_rip + 0x887E2D) + 1056, Arg4);
    v_stack_m1B0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x74)));
    v_stack_m1B8 = (uint8_t)(local_rbx);
    v_stack_m1C0 = (uint8_t)(*(uint8_t *)(local_rsp - 0x128 - 0x7C));
    v_stack_m1C8 = (uint32_t)(local_r15);
    v_stack_m1D0 = *(uint64_t *)(local_rsp - 0x128 - 0x38) + 1208;
    v_stack_m1D8 = local_rsp - 296 - 128;
    v_stack_m1E0 = *(uint64_t *)(v_rip + 0x887E2D) + 1848;
    v_stack_m1E8 = *(uint64_t *)(v_rip + 0x887E2D) + 1320;
    v_stack_m1F0 = *(uint64_t *)(v_rip + 0x887E2D) + 264;
    v_stack_m1F8 = *(uint64_t *)(v_rip + 0x887E2D);
    v_stack_m200 = (uint32_t)(local_rsi);
    v_stack_m208 = (uint32_t)(local_r12);
    result = PpmParkComputeUnparkMaskEx(*(uint64_t *)(local_rsp - 0x128 - 0x38), *(uint64_t *)(v_rip + 0x887E2D) + 1584, *(uint64_t *)(local_rsp - 0x128 - 0x38) + 576, *(uint64_t *)(v_rip + 0x887E2D) + 1056);
    result = Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(local_rsp - 0x128 - 0x38), *(uint64_t *)(v_rip + 0x887E2D) + 1584, *(uint64_t *)(local_rsp - 0x128 - 0x38) + 576, *(uint64_t *)(v_rip + 0x887E2D) + 1056);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_005E0437;
    if ((*(uint8_t *)(local_rsp - 0x128 - 0x7B)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 0x500);
        Arg1 = *(uint32_t *)(local_rsp - 0x128 - 0x68);
        *(uint32_t *)(result + 0x4) = (uint32_t)(Arg1);
    }
    result = KeSubtractAffinityEx2(*(uint64_t *)(v_rip + 0x887E2D) + 1584, *(uint64_t *)(v_rip + 0x887E2D) + 1320, *(uint64_t *)(v_rip + 0x887E2D) + 2112, *(uint64_t *)(v_rip + 0x887E2D) + 1056);
    result = KeSubtractAffinityEx2(*(uint64_t *)(v_rip + 0x887E2D) + 2112, *(uint64_t *)(v_rip + 0x887E2D) + 1848, *(uint64_t *)(v_rip + 0x887E2D) + 2112, *(uint64_t *)(v_rip + 0x887E2D) + 1056);
    result = KeSubtractAffinityEx2(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 312, *(uint64_t *)(v_rip + 0x887E2D) + 1584, *(uint64_t *)(local_rsp - 0x128 - 0x38) + 312, *(uint64_t *)(v_rip + 0x887E2D) + 1056);
    result = KeOrAffinityEx2(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 312, *(uint64_t *)(v_rip + 0x887E2D) + 1320, *(uint64_t *)(local_rsp - 0x128 - 0x38) + 312, *(uint64_t *)(v_rip + 0x887E2D) + 1056);
    result = KeOrAffinityEx2(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 312, *(uint64_t *)(v_rip + 0x887E2D) + 1848, *(uint64_t *)(local_rsp - 0x128 - 0x38) + 312, *(uint64_t *)(v_rip + 0x887E2D) + 1056);
    result = KeSubtractAffinityEx2(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 840, *(uint64_t *)(v_rip + 0x887E2D) + 1584, *(uint64_t *)(local_rsp - 0x128 - 0x38) + 840, *(uint64_t *)(v_rip + 0x887E2D) + 1056);
    result = KeOrAffinityEx2(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 840, *(uint64_t *)(v_rip + 0x887E2D) + 1848, *(uint64_t *)(local_rsp - 0x128 - 0x38) + 840, *(uint64_t *)(v_rip + 0x887E2D) + 1056);
    v_stack_m1D8 = (uint32_t)(local_r15);
    v_stack_m1E0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x80)));
    v_stack_m1E8 = *(uint64_t *)(v_rip + 0x887E2D) + 528;
    v_stack_m1F0 = *(uint64_t *)(v_rip + 0x887E2D) + 1056;
    v_stack_m1F8 = *(uint64_t *)(v_rip + 0x887E2D) + 264;
    v_stack_m200 = *(uint64_t *)(v_rip + 0x887E2D);
    v_stack_m208 = (uint16_t)(local_r14);
    result = PpmEventTraceSoftCoreParkingSelectionEx(*(uint64_t *)(local_rsp - 0x128 - 0x38), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x74)))), (uint16_t)(local_r12), (uint16_t)(local_rsi));
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x74))) + 1);
    *(uint32_t *)(local_rsp - 0x128 - 0x74) = (uint32_t)(local_r15);
    if (((uint32_t)(local_r15)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x128 - 0x38) + 0xC)))) goto loc_005DFE9A;
loc_005E0548:
loc_005E054B:
    local_rsi = 0;
loc_005E0554:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x64))) + (1));
    *(uint32_t *)(local_rsp - 0x128 - 0x64) = (uint32_t)(local_rbx);
    if (((uint32_t)(local_rbx)) < (*(uint32_t *)(v_rip + 0x927E7F))) goto loc_005DFDDB;
loc_005E056A:
    result = PpmParkComputeDiff(*(uint64_t *)(local_rsp - 0x128 - 0x38), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x128 - 0x74)))), (uint16_t)(local_r12), 0);
    Arg2 = ((*(uint32_t *)(v_rip + 0x8874CB)) > 0) ? 1 : 0;
    if ((*(uint32_t *)(v_rip + 0x8874BC)) != Arg2) goto loc_005E058C;
    result = 0;
    if ((*(uint32_t *)(v_rip + 0x8874C0)) != 0) {
        result = 1;
    }
    *(uint32_t *)(v_rip + 0x8874A8) = Arg2;
    *(uint32_t *)(v_rip + 0x8874AE) = 0;
    if ((uint32_t)(result) != 0) {
        result = PpmEventLPICoreParking(*(uint64_t *)(local_rsp - 0x128 - 0x38), Arg2, (uint16_t)(local_r12), 0);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x128 + 0xF0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint16_t)(local_r12), 0);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DFBE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
