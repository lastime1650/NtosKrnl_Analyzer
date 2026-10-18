# CmGetDeviceInterfaceSubkeyPath

- RVA: `0x008F1010`–`0x008F1797` (길이 `1,927` bytes)
- VA: `0x00000001408F1010`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00087248`
- 디코드: `492`개 명령, `1,927/1,927` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x008F1078` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x008F1097` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x008F10BA` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x008F1126` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008F11C8` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x008F124D` → [ScanHexFormat](ScanHexFormat_function_008F29C0.md) (function, `0x008F29C0`)
- `0x008F128C` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x008F1372` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x008F13F7` → [ScanHexFormat](ScanHexFormat_function_008F29C0.md) (function, `0x008F29C0`)
- `0x008F1565` → [RtlStringExHandleOtherFlagsW](../../text/41/RtlStringExHandleOtherFlagsW_function_0041E3F0.md) (function, `0x0041E3F0`)
- `0x008F1746` → [RtlStringExHandleOtherFlagsW](../../text/41/RtlStringExHandleOtherFlagsW_function_0041E3F0.md) (function, `0x0041E3F0`)
- `0x008F176D` → [RtlStringExHandleOtherFlagsW](../../text/41/RtlStringExHandleOtherFlagsW_function_0041E3F0.md) (function, `0x0041E3F0`)

### Direct callers
- [CmGetDeviceInterfaceClassGuid](CmGetDeviceInterfaceClassGuid_function_008F3380.md) at `0x008F33BD`
- [CmCreateDeviceInterfaceWorker](../90/CmCreateDeviceInterfaceWorker_function_009016E4.md) at `0x00901746`

### Static image references
- `0x008F102C` → RVA `0x00E0A740` (`.data`; read)
- `0x008F10AB` → RVA `0x00001A30` (`.rdata`; read)
- `0x008F10C5` → RVA `0x00001A40` (`.rdata`; read)
- `0x008F11EC` → RVA `0x00B4D0B0` (`GuidFormat`; read)
- `0x008F15B7` → RVA `0x00B0D4D0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x008F1078` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x008F1097` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x008F10BA` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x008F1126` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008F11C8` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x008F128C` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x008F1372` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x008F1565` → [RtlStringExHandleOtherFlagsW](../../text/41/RtlStringExHandleOtherFlagsW_function_0041E3F0.md) (`PAGE` → `.text`)
  - `0x008F1746` → [RtlStringExHandleOtherFlagsW](../../text/41/RtlStringExHandleOtherFlagsW_function_0041E3F0.md) (`PAGE` → `.text`)
  - `0x008F176D` → [RtlStringExHandleOtherFlagsW](../../text/41/RtlStringExHandleOtherFlagsW_function_0041E3F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008F1010  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008F1015  55                              push rbp
008F1016  56                              push rsi
008F1017  57                              push rdi
008F1018  41 54                           push r12
008F101A  41 55                           push r13
008F101C  41 56                           push r14
008F101E  41 57                           push r15
008F1020  48 8D 6C 24 B0                  lea rbp, [rsp - 0x50]
008F1025  48 81 EC 50 01 00 00            sub rsp, 0x150
008F102C  48 8B 05 0D 97 51 00            mov rax, qword ptr [rip + 0x51970d]
008F1033  48 33 C4                        xor rax, rsp
008F1036  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
008F103A  48 8B 85 B0 00 00 00            mov rax, qword ptr [rbp + 0xb0]
008F1041  48 8D 4D 98                     lea rcx, [rbp - 0x68]
008F1045  0F 57 C0                        xorps xmm0, xmm0
008F1048  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008F104D  45 33 F6                        xor r14d, r14d
008F1050  4C 89 4D 80                     mov qword ptr [rbp - 0x80], r9
008F1054  0F 57 C9                        xorps xmm1, xmm1
008F1057  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
008F105B  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
008F105F  41 8B FE                        mov edi, r14d
008F1062  41 8B DE                        mov ebx, r14d
008F1065  0F 11 4D A8                     movups xmmword ptr [rbp - 0x58], xmm1
008F1069  45 0F B6 E8                     movzx r13d, r8b
008F106D  4C 8B E2                        mov r12, rdx
008F1070  0F 11 45 98                     movups xmmword ptr [rbp - 0x68], xmm0
008F1074  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
008F1078  E8 E3 28 B7 FF                  call 0x140463960
008F107D  85 C0                           test eax, eax
008F107F  0F 88 8C 00 00 00               js 0x1408f1111
008F1085  0F B7 45 9A                     movzx eax, word ptr [rbp - 0x66]
008F1089  B9 FE FF 00 00                  mov ecx, 0xfffe
008F108E  66 23 C1                        and ax, cx
008F1091  66 83 F8 62                     cmp ax, 0x62
008F1095  72 7A                           jb 0x1408f1111
008F1097  E8 54 D1 A0 FF                  call 0x1402fe1f0
008F109C  44 0F B7 45 98                  movzx r8d, word ptr [rbp - 0x68]
008F10A1  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
008F10A5  41 83 F8 08                     cmp r8d, 8
008F10A9  72 0F                           jb 0x1408f10ba
008F10AB  48 8B 05 7E 09 71 FF            mov rax, qword ptr [rip - 0x8ef682]
008F10B2  48 8B 08                        mov rcx, qword ptr [rax]
008F10B5  48 3B 0A                        cmp rcx, qword ptr [rdx]
008F10B8  74 1A                           je 0x1408f10d4
008F10BA  E8 31 D1 A0 FF                  call 0x1402fe1f0
008F10BF  41 83 F8 08                     cmp r8d, 8
008F10C3  72 4C                           jb 0x1408f1111
008F10C5  48 8B 05 74 09 71 FF            mov rax, qword ptr [rip - 0x8ef68c]
008F10CC  48 8B 08                        mov rcx, qword ptr [rax]
008F10CF  48 3B 0A                        cmp rcx, qword ptr [rdx]
008F10D2  75 3D                           jne 0x1408f1111
008F10D4  49 8D 44 24 08                  lea rax, [r12 + 8]
008F10D9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
008F10E0  0F B7 08                        movzx ecx, word ptr [rax]
008F10E3  66 85 C9                        test cx, cx
008F10E6  74 10                           je 0x1408f10f8
008F10E8  66 83 F9 5C                     cmp cx, 0x5c
008F10EC  0F 84 9D 00 00 00               je 0x1408f118f
008F10F2  48 83 C0 02                     add rax, 2
008F10F6  EB E8                           jmp 0x1408f10e0
008F10F8  48 85 DB                        test rbx, rbx
008F10FB  0F 84 3E 02 00 00               je 0x1408f133f
008F1101  49 2B DC                        sub rbx, r12
008F1104  48 D1 FB                        sar rbx, 1
008F1107  BE FF FF FF FF                  mov esi, 0xffffffff
008F110C  48 3B DE                        cmp rbx, rsi
008F110F  76 36                           jbe 0x1408f1147
008F1111  BF 33 00 00 C0                  mov edi, 0xc0000033
008F1116  EB 05                           jmp 0x1408f111d
008F1118  BF 95 00 00 C0                  mov edi, 0xc0000095
008F111D  8B C7                           mov eax, edi
008F111F  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
008F1123  48 33 CC                        xor rcx, rsp
008F1126  E8 15 B5 DB FF                  call 0x1406ac640
008F112B  48 8B 9C 24 90 01 00 00         mov rbx, qword ptr [rsp + 0x190]
008F1133  48 81 C4 50 01 00 00            add rsp, 0x150
008F113A  41 5F                           pop r15
008F113C  41 5E                           pop r14
008F113E  41 5D                           pop r13
008F1140  41 5C                           pop r12
008F1142  5F                              pop rdi
008F1143  5E                              pop rsi
008F1144  5D                              pop rbp
008F1145  C3                              ret
008F1146  CC                              int3
008F1147  83 FB 30                        cmp ebx, 0x30
008F114A  72 C5                           jb 0x1408f1111
008F114C  8B C3                           mov eax, ebx
008F114E  48 8D 4D F0                     lea rcx, [rbp - 0x10]
008F1152  48 83 C0 DA                     add rax, -0x26
008F1156  41 BF 27 00 00 00               mov r15d, 0x27
008F115C  45 8B C7                        mov r8d, r15d
008F115F  4D 8D 0C 44                     lea r9, [r12 + rax*2]
008F1163  48 8D 45 F0                     lea rax, [rbp - 0x10]
008F1167  4C 2B C8                        sub r9, rax
008F116A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
008F1170  49 8D 50 FF                     lea rdx, [r8 - 1]
008F1174  48 85 D2                        test rdx, rdx
008F1177  74 29                           je 0x1408f11a2
008F1179  41 0F B7 04 09                  movzx eax, word ptr [r9 + rcx]
008F117E  66 85 C0                        test ax, ax
008F1181  74 1F                           je 0x1408f11a2
008F1183  66 89 01                        mov word ptr [rcx], ax
008F1186  4C 8B C2                        mov r8, rdx
008F1189  48 83 C1 02                     add rcx, 2
008F118D  EB E1                           jmp 0x1408f1170
008F118F  FF C7                           inc edi
008F1191  83 FF 01                        cmp edi, 1
008F1194  0F 87 77 FF FF FF               ja 0x1408f1111
008F119A  48 8B D8                        mov rbx, rax
008F119D  E9 50 FF FF FF                  jmp 0x1408f10f2
008F11A2  4D 85 C0                        test r8, r8
008F11A5  48 8D 41 FE                     lea rax, [rcx - 2]
008F11A9  BF 05 00 00 80                  mov edi, 0x80000005
008F11AE  48 0F 45 C1                     cmovne rax, rcx
008F11B2  41 0F 45 FE                     cmovne edi, r14d
008F11B6  66 44 89 30                     mov word ptr [rax], r14w
008F11BA  0F 84 68 05 00 00               je 0x1408f1728
008F11C0  48 8D 55 F0                     lea rdx, [rbp - 0x10]
008F11C4  48 8D 4D 98                     lea rcx, [rbp - 0x68]
008F11C8  E8 93 27 B7 FF                  call 0x140463960
008F11CD  8B F8                           mov edi, eax
008F11CF  85 C0                           test eax, eax
008F11D1  0F 88 46 FF FF FF               js 0x1408f111d
008F11D7  0F B7 55 98                     movzx edx, word ptr [rbp - 0x68]
008F11DB  48 8D 45 E6                     lea rax, [rbp - 0x1a]
008F11DF  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
008F11E3  4C 8D 4D B8                     lea r9, [rbp - 0x48]
008F11E7  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008F11EC  4C 8D 05 BD BE 25 00            lea r8, [rip + 0x25bebd]
008F11F3  48 8D 45 E4                     lea rax, [rbp - 0x1c]
008F11F7  D1 EA                           shr edx, 1
008F11F9  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008F11FE  0F 57 C0                        xorps xmm0, xmm0
008F1201  48 8D 45 E2                     lea rax, [rbp - 0x1e]
008F1205  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008F120A  48 8D 45 E0                     lea rax, [rbp - 0x20]
008F120E  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008F1213  48 8D 45 DE                     lea rax, [rbp - 0x22]
008F1217  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008F121C  48 8D 45 DC                     lea rax, [rbp - 0x24]
008F1220  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008F1225  48 8D 45 DA                     lea rax, [rbp - 0x26]
008F1229  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008F122E  48 8D 45 D8                     lea rax, [rbp - 0x28]
008F1232  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F1237  48 8D 45 BE                     lea rax, [rbp - 0x42]
008F123B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008F1240  48 8D 45 BC                     lea rax, [rbp - 0x44]
008F1244  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F1249  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
008F124D  E8 6E 17 00 00                  call 0x1408f29c0
008F1252  83 F8 FF                        cmp eax, -1
008F1255  0F 84 B6 FE FF FF               je 0x1408f1111
008F125B  45 8B C6                        mov r8d, r14d
008F125E  48 8D 4D C1                     lea rcx, [rbp - 0x3f]
008F1262  48 8D 55 DA                     lea rdx, [rbp - 0x26]
008F1266  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
008F1270  41 83 C0 08                     add r8d, 8
008F1274  48 8D 49 08                     lea rcx, [rcx + 8]
008F1278  48 8D 52 10                     lea rdx, [rdx + 0x10]
008F127C  41 83 F8 08                     cmp r8d, 8
008F1280  72 EE                           jb 0x1408f1270
008F1282  BA 5C 00 00 00                  mov edx, 0x5c
008F1287  49 8D 4C 24 08                  lea rcx, [r12 + 8]
008F128C  E8 CF 07 C1 FF                  call 0x140501a60
008F1291  48 8B D8                        mov rbx, rax
008F1294  48 C7 C1 FF FF FF FF            mov rcx, 0xffffffffffffffff
008F129B  48 85 C0                        test rax, rax
008F129E  0F 85 7E 02 00 00               jne 0x1408f1522
008F12A4  48 8B D9                        mov rbx, rcx
008F12A7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
008F12B0  48 FF C3                        inc rbx
008F12B3  66 45 39 34 5C                  cmp word ptr [r12 + rbx*2], r14w
008F12B8  75 F6                           jne 0x1408f12b0
008F12BA  48 3B DE                        cmp rbx, rsi
008F12BD  0F 87 55 FE FF FF               ja 0x1408f1118
008F12C3  83 FB 30                        cmp ebx, 0x30
008F12C6  0F 82 45 FE FF FF               jb 0x1408f1111
008F12CC  8D 73 01                        lea esi, [rbx + 1]
008F12CF  45 84 ED                        test r13b, r13b
008F12D2  74 1A                           je 0x1408f12ee
008F12D4  48 83 C6 02                     add rsi, 2
008F12D8  4D 85 F6                        test r14, r14
008F12DB  74 11                           je 0x1408f12ee
008F12DD  0F 1F 00                        nop dword ptr [rax]
008F12E0  48 FF C1                        inc rcx
008F12E3  66 41 83 3C 4E 00               cmp word ptr [r14 + rcx*2], 0
008F12E9  75 F5                           jne 0x1408f12e0
008F12EB  48 03 F1                        add rsi, rcx
008F12EE  B8 FF FF FF FF                  mov eax, 0xffffffff
008F12F3  48 3B F0                        cmp rsi, rax
008F12F6  0F 87 1C FE FF FF               ja 0x1408f1118
008F12FC  4C 8B 55 80                     mov r10, qword ptr [rbp - 0x80]
008F1300  4D 85 D2                        test r10, r10
008F1303  0F 84 62 01 00 00               je 0x1408f146b
008F1309  44 8B C3                        mov r8d, ebx
008F130C  49 8B CA                        mov rcx, r10
008F130F  49 83 C0 DA                     add r8, -0x26
008F1313  4F 8D 04 44                     lea r8, [r12 + r8*2]
008F1317  4D 2B C2                        sub r8, r10
008F131A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
008F1320  49 8D 57 FF                     lea rdx, [r15 - 1]
008F1324  48 85 D2                        test rdx, rdx
008F1327  74 21                           je 0x1408f134a
008F1329  41 0F B7 04 08                  movzx eax, word ptr [r8 + rcx]
008F132E  66 85 C0                        test ax, ax
008F1331  74 17                           je 0x1408f134a
008F1333  66 89 01                        mov word ptr [rcx], ax
008F1336  4C 8B FA                        mov r15, rdx
008F1339  48 83 C1 02                     add rcx, 2
008F133D  EB E1                           jmp 0x1408f1320
008F133F  49 8B D8                        mov rbx, r8
008F1342  48 D1 EB                        shr rbx, 1
008F1345  E9 BD FD FF FF                  jmp 0x1408f1107
008F134A  4D 85 FF                        test r15, r15
008F134D  48 8D 41 FE                     lea rax, [rcx - 2]
008F1351  BF 05 00 00 80                  mov edi, 0x80000005
008F1356  48 0F 45 C1                     cmovne rax, rcx
008F135A  33 C9                           xor ecx, ecx
008F135C  4D 85 FF                        test r15, r15
008F135F  0F 45 F9                        cmovne edi, ecx
008F1362  66 89 08                        mov word ptr [rax], cx
008F1365  0F 84 E5 03 00 00               je 0x1408f1750
008F136B  49 8B D2                        mov rdx, r10
008F136E  48 8D 4D A8                     lea rcx, [rbp - 0x58]
008F1372  E8 E9 25 B7 FF                  call 0x140463960
008F1377  8B F8                           mov edi, eax
008F1379  85 C0                           test eax, eax
008F137B  0F 88 9C FD FF FF               js 0x1408f111d
008F1381  0F B7 55 A8                     movzx edx, word ptr [rbp - 0x58]
008F1385  48 8D 45 E6                     lea rax, [rbp - 0x1a]
008F1389  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
008F138D  4C 8D 4D C8                     lea r9, [rbp - 0x38]
008F1391  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008F1396  4C 8D 05 13 BD 25 00            lea r8, [rip + 0x25bd13]
008F139D  48 8D 45 E4                     lea rax, [rbp - 0x1c]
008F13A1  D1 EA                           shr edx, 1
008F13A3  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008F13A8  0F 57 C0                        xorps xmm0, xmm0
008F13AB  48 8D 45 E2                     lea rax, [rbp - 0x1e]
008F13AF  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008F13B4  48 8D 45 E0                     lea rax, [rbp - 0x20]
008F13B8  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008F13BD  48 8D 45 DE                     lea rax, [rbp - 0x22]
008F13C1  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008F13C6  48 8D 45 DC                     lea rax, [rbp - 0x24]
008F13CA  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008F13CF  48 8D 45 DA                     lea rax, [rbp - 0x26]
008F13D3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008F13D8  48 8D 45 D8                     lea rax, [rbp - 0x28]
008F13DC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008F13E1  48 8D 45 CE                     lea rax, [rbp - 0x32]
008F13E5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008F13EA  48 8D 45 CC                     lea rax, [rbp - 0x34]
008F13EE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F13F3  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
008F13F7  E8 C4 15 00 00                  call 0x1408f29c0
008F13FC  83 F8 FF                        cmp eax, -1
008F13FF  0F 84 72 03 00 00               je 0x1408f1777
008F1405  45 33 DB                        xor r11d, r11d
008F1408  48 8D 4D D1                     lea rcx, [rbp - 0x2f]
008F140C  45 8B C3                        mov r8d, r11d
008F140F  48 8D 55 DA                     lea rdx, [rbp - 0x26]
008F1413  0F 1F 40 00                     nop dword ptr [rax]
008F1417  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
008F1420  0F B6 42 FE                     movzx eax, byte ptr [rdx - 2]
008F1424  41 83 C0 08                     add r8d, 8
008F1428  88 41 FF                        mov byte ptr [rcx - 1], al
008F142B  48 8D 49 08                     lea rcx, [rcx + 8]
008F142F  0F B6 02                        movzx eax, byte ptr [rdx]
008F1432  48 8D 52 10                     lea rdx, [rdx + 0x10]
008F1436  88 41 F8                        mov byte ptr [rcx - 8], al
008F1439  0F B6 42 F2                     movzx eax, byte ptr [rdx - 0xe]
008F143D  88 41 F9                        mov byte ptr [rcx - 7], al
008F1440  0F B6 42 F4                     movzx eax, byte ptr [rdx - 0xc]
008F1444  88 41 FA                        mov byte ptr [rcx - 6], al
008F1447  0F B6 42 F6                     movzx eax, byte ptr [rdx - 0xa]
008F144B  88 41 FB                        mov byte ptr [rcx - 5], al
008F144E  0F B6 42 F8                     movzx eax, byte ptr [rdx - 8]
008F1452  88 41 FC                        mov byte ptr [rcx - 4], al
008F1455  0F B6 42 FA                     movzx eax, byte ptr [rdx - 6]
008F1459  88 41 FD                        mov byte ptr [rcx - 3], al
008F145C  0F B6 42 FC                     movzx eax, byte ptr [rdx - 4]
008F1460  88 41 FE                        mov byte ptr [rcx - 2], al
008F1463  41 83 F8 08                     cmp r8d, 8
008F1467  72 B7                           jb 0x1408f1420
008F1469  EB 03                           jmp 0x1408f146e
008F146B  45 33 DB                        xor r11d, r11d
008F146E  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
008F1474  3B F0                           cmp esi, eax
008F1476  0F 87 B5 00 00 00               ja 0x1408f1531
008F147C  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
008F1481  44 8B D0                        mov r10d, eax
008F1484  44 8B CB                        mov r9d, ebx
008F1487  48 FF C8                        dec rax
008F148A  BB FE FF FF 7F                  mov ebx, 0x7ffffffe
008F148F  48 3B C3                        cmp rax, rbx
008F1492  0F 87 27 02 00 00               ja 0x1408f16bf
008F1498  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
008F149C  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
008F14A1  49 81 F9 FF FF FF 7F            cmp r9, 0x7fffffff
008F14A8  0F 83 8D 00 00 00               jae 0x1408f153b
008F14AE  4D 2B CA                        sub r9, r10
008F14B1  41 8B CA                        mov ecx, r10d
008F14B4  4D 2B E7                        sub r12, r15
008F14B7  49 8B D7                        mov rdx, r15
008F14BA  4D 8B C3                        mov r8, r11
008F14BD  0F 1F 00                        nop dword ptr [rax]
008F14C0  49 8D 04 09                     lea rax, [r9 + rcx]
008F14C4  48 85 C0                        test rax, rax
008F14C7  74 1A                           je 0x1408f14e3
008F14C9  41 0F B7 04 14                  movzx eax, word ptr [r12 + rdx]
008F14CE  66 85 C0                        test ax, ax
008F14D1  74 10                           je 0x1408f14e3
008F14D3  66 89 02                        mov word ptr [rdx], ax
008F14D6  49 FF C0                        inc r8
008F14D9  48 83 C2 02                     add rdx, 2
008F14DD  48 83 E9 01                     sub rcx, 1
008F14E1  75 DD                           jne 0x1408f14c0
008F14E3  48 85 C9                        test rcx, rcx
008F14E6  48 8D 42 FE                     lea rax, [rdx - 2]
008F14EA  BE 05 00 00 80                  mov esi, 0x80000005
008F14EF  49 8B CA                        mov rcx, r10
008F14F2  48 0F 45 C2                     cmovne rax, rdx
008F14F6  41 0F 45 F3                     cmovne esi, r11d
008F14FA  66 44 89 18                     mov word ptr [rax], r11w
008F14FE  49 8D 40 FF                     lea rax, [r8 - 1]
008F1502  49 0F 45 C0                     cmovne rax, r8
008F1506  48 2B C8                        sub rcx, rax
008F1509  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
008F150E  49 8D 14 47                     lea rdx, [r15 + rax*2]
008F1512  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
008F1516  85 F6                           test esi, esi
008F1518  78 2E                           js 0x1408f1548
008F151A  4C 8B E2                        mov r12, rdx
008F151D  4C 8B D9                        mov r11, rcx
008F1520  EB 5B                           jmp 0x1408f157d
008F1522  49 2B DC                        sub rbx, r12
008F1525  4C 8D 70 02                     lea r14, [rax + 2]
008F1529  48 D1 FB                        sar rbx, 1
008F152C  E9 89 FD FF FF                  jmp 0x1408f12ba
008F1531  BF 23 00 00 C0                  mov edi, 0xc0000023
008F1536  E9 E2 FB FF FF                  jmp 0x1408f111d
008F153B  BE 0D 00 00 C0                  mov esi, 0xc000000d
008F1540  66 45 89 1F                     mov word ptr [r15], r11w
008F1544  41 0F 42 F3                     cmovb esi, r11d
008F1548  48 8D 44 24 70                  lea rax, [rsp + 0x70]
008F154D  C7 44 24 28 00 08 00 00         mov dword ptr [rsp + 0x28], 0x800
008F1555  4B 8D 14 12                     lea rdx, [r10 + r10]
008F1559  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F155E  4C 8D 4D 80                     lea r9, [rbp - 0x80]
008F1562  49 8B CF                        mov rcx, r15
008F1565  E8 86 CE B2 FF                  call 0x14041e3f0
008F156A  81 FE 05 00 00 80               cmp esi, 0x80000005
008F1570  0F 84 0B 02 00 00               je 0x1408f1781
008F1576  4C 8B 5D 90                     mov r11, qword ptr [rbp - 0x70]
008F157A  4D 8B E3                        mov r12, r11
008F157D  8B FE                           mov edi, esi
008F157F  85 F6                           test esi, esi
008F1581  0F 88 96 FB FF FF               js 0x1408f111d
008F1587  48 B8 23 00 23 00 3F 00 23 00   movabs rax, 0x23003f00230023
008F1591  49 89 07                        mov qword ptr [r15], rax
008F1594  45 84 ED                        test r13b, r13b
008F1597  0F 84 80 FB FF FF               je 0x1408f111d
008F159D  49 8D 43 FF                     lea rax, [r11 - 1]
008F15A1  48 BE FF FF FF FF FF FF FF 7F   movabs rsi, 0x7fffffffffffffff
008F15AB  48 3B C3                        cmp rax, rbx
008F15AE  0F 87 40 01 00 00               ja 0x1408f16f4
008F15B4  45 33 FF                        xor r15d, r15d
008F15B7  4C 8D 15 12 BF 21 00            lea r10, [rip + 0x21bf12]
008F15BE  4C 8B CB                        mov r9, rbx
008F15C1  49 8B CB                        mov rcx, r11
008F15C4  4D 2B CB                        sub r9, r11
008F15C7  49 8B D4                        mov rdx, r12
008F15CA  4D 2B D4                        sub r10, r12
008F15CD  45 8B C7                        mov r8d, r15d
008F15D0  49 8D 04 09                     lea rax, [r9 + rcx]
008F15D4  48 85 C0                        test rax, rax
008F15D7  74 1A                           je 0x1408f15f3
008F15D9  41 0F B7 04 12                  movzx eax, word ptr [r10 + rdx]
008F15DE  66 85 C0                        test ax, ax
008F15E1  74 10                           je 0x1408f15f3
008F15E3  66 89 02                        mov word ptr [rdx], ax
008F15E6  49 FF C0                        inc r8
008F15E9  48 83 C2 02                     add rdx, 2
008F15ED  48 83 E9 01                     sub rcx, 1
008F15F1  75 DD                           jne 0x1408f15d0
008F15F3  48 85 C9                        test rcx, rcx
008F15F6  48 8D 42 FE                     lea rax, [rdx - 2]
008F15FA  48 0F 45 C2                     cmovne rax, rdx
008F15FE  BA 05 00 00 80                  mov edx, 0x80000005
008F1603  41 0F 45 D7                     cmovne edx, r15d
008F1607  66 44 89 38                     mov word ptr [rax], r15w
008F160B  49 8D 40 FF                     lea rax, [r8 - 1]
008F160F  49 0F 45 C0                     cmovne rax, r8
008F1613  4D 8B C3                        mov r8, r11
008F1616  4C 2B C0                        sub r8, rax
008F1619  4D 8D 0C 44                     lea r9, [r12 + rax*2]
008F161D  48 85 C9                        test rcx, rcx
008F1620  0F 84 B2 00 00 00               je 0x1408f16d8
008F1626  8B C2                           mov eax, edx
008F1628  85 D2                           test edx, edx
008F162A  0F 89 84 00 00 00               jns 0x1408f16b4
008F1630  3D 05 00 00 80                  cmp eax, 0x80000005
008F1635  74 7D                           je 0x1408f16b4
008F1637  8B FA                           mov edi, edx
008F1639  85 D2                           test edx, edx
008F163B  0F 88 DC FA FF FF               js 0x1408f111d
008F1641  4D 85 F6                        test r14, r14
008F1644  0F 84 D3 FA FF FF               je 0x1408f111d
008F164A  49 8D 43 FF                     lea rax, [r11 - 1]
008F164E  48 3B C3                        cmp rax, rbx
008F1651  0F 87 B9 00 00 00               ja 0x1408f1710
008F1657  49 2B DB                        sub rbx, r11
008F165A  49 8B D3                        mov rdx, r11
008F165D  4D 2B F4                        sub r14, r12
008F1660  49 8B CC                        mov rcx, r12
008F1663  48 8D 04 13                     lea rax, [rbx + rdx]
008F1667  48 85 C0                        test rax, rax
008F166A  74 17                           je 0x1408f1683
008F166C  41 0F B7 04 0E                  movzx eax, word ptr [r14 + rcx]
008F1671  66 85 C0                        test ax, ax
008F1674  74 0D                           je 0x1408f1683
008F1676  66 89 01                        mov word ptr [rcx], ax
008F1679  48 83 C1 02                     add rcx, 2
008F167D  48 83 EA 01                     sub rdx, 1
008F1681  75 E0                           jne 0x1408f1663
008F1683  48 85 D2                        test rdx, rdx
008F1686  48 8D 41 FE                     lea rax, [rcx - 2]
008F168A  BF 05 00 00 80                  mov edi, 0x80000005
008F168F  48 0F 45 C1                     cmovne rax, rcx
008F1693  41 0F 45 FF                     cmovne edi, r15d
008F1697  66 44 89 38                     mov word ptr [rax], r15w
008F169B  0F 85 7C FA FF FF               jne 0x1408f111d
008F16A1  4C 85 DE                        test rsi, r11
008F16A4  0F 86 73 FA FF FF               jbe 0x1408f111d
008F16AA  66 45 89 3C 24                  mov word ptr [r12], r15w
008F16AF  E9 69 FA FF FF                  jmp 0x1408f111d
008F16B4  4D 8B E1                        mov r12, r9
008F16B7  4D 8B D8                        mov r11, r8
008F16BA  E9 78 FF FF FF                  jmp 0x1408f1637
008F16BF  BE 0D 00 00 C0                  mov esi, 0xc000000d
008F16C4  8B FE                           mov edi, esi
008F16C6  4D 85 D2                        test r10, r10
008F16C9  0F 84 A7 FE FF FF               je 0x1408f1576
008F16CF  66 45 89 1F                     mov word ptr [r15], r11w
008F16D3  E9 45 FA FF FF                  jmp 0x1408f111d
008F16D8  49 8B C3                        mov rax, r11
008F16DB  48 23 C6                        and rax, rsi
008F16DE  0F 86 42 FF FF FF               jbe 0x1408f1626
008F16E4  4D 8B CC                        mov r9, r12
008F16E7  66 45 89 3C 24                  mov word ptr [r12], r15w
008F16EC  4C 8B C0                        mov r8, rax
008F16EF  E9 32 FF FF FF                  jmp 0x1408f1626
008F16F4  BA 0D 00 00 C0                  mov edx, 0xc000000d
008F16F9  8B FA                           mov edi, edx
008F16FB  4D 85 DB                        test r11, r11
008F16FE  0F 84 8B 00 00 00               je 0x1408f178f
008F1704  33 C9                           xor ecx, ecx
008F1706  66 41 89 0C 24                  mov word ptr [r12], cx
008F170B  E9 0D FA FF FF                  jmp 0x1408f111d
008F1710  BF 0D 00 00 C0                  mov edi, 0xc000000d
008F1715  4D 85 DB                        test r11, r11
008F1718  0F 84 FF F9 FF FF               je 0x1408f111d
008F171E  66 45 89 3C 24                  mov word ptr [r12], r15w
008F1723  E9 F5 F9 FF FF                  jmp 0x1408f111d
008F1728  48 8D 45 88                     lea rax, [rbp - 0x78]
008F172C  C7 44 24 28 00 08 00 00         mov dword ptr [rsp + 0x28], 0x800
008F1734  4C 8D 4D 90                     lea r9, [rbp - 0x70]
008F1738  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F173D  BA 4E 00 00 00                  mov edx, 0x4e
008F1742  48 8D 4D F0                     lea rcx, [rbp - 0x10]
008F1746  E8 A5 CC B2 FF                  call 0x14041e3f0
008F174B  E9 CD F9 FF FF                  jmp 0x1408f111d
008F1750  48 8D 45 88                     lea rax, [rbp - 0x78]
008F1754  C7 44 24 28 00 08 00 00         mov dword ptr [rsp + 0x28], 0x800
008F175C  4C 8D 4D 90                     lea r9, [rbp - 0x70]
008F1760  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008F1765  BA 4E 00 00 00                  mov edx, 0x4e
008F176A  49 8B CA                        mov rcx, r10
008F176D  E8 7E CC B2 FF                  call 0x14041e3f0
008F1772  E9 A6 F9 FF FF                  jmp 0x1408f111d
008F1777  BF 0D 00 00 C0                  mov edi, 0xc000000d
008F177C  E9 9C F9 FF FF                  jmp 0x1408f111d
008F1781  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
008F1785  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008F178A  E9 8B FD FF FF                  jmp 0x1408f151a
008F178F  45 33 FF                        xor r15d, r15d
008F1792  E9 A0 FE FF FF                  jmp 0x1408f1637
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmGetDeviceInterfaceSubkeyPath(__int64 a1, __int64 a2, unsigned __int8 a3, __int64 a4, __int64 a5, unsigned int a6)
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
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA2;
    unsigned __int64 v_stack_mA4;
    unsigned __int64 v_stack_mA6;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mAA;
    unsigned __int64 v_stack_mAC;
    unsigned __int64 v_stack_mAE;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB7;
    unsigned __int64 v_stack_mBA;
    unsigned __int64 v_stack_mBC;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC7;
    unsigned __int64 v_stack_mCA;
    unsigned __int64 v_stack_mCC;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int16 v_stack_mEE;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (336);
    result = (*(unsigned __int64 *)(v_rip + 5347085)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m118 = a5;
    v_r14 = 0;
    v_stack_m108 = a4;
    v_stack_mF8 = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    v_stack_mF0 = v_xmm0;
    v_stack_mD0 = v_xmm0;
    result = RtlInitUnicodeStringEx(v_stack_mF0, a2, a3, a4);
    if (sign_flag) goto loc_008F1111;
    result = (unsigned __int16)((v_stack_mEE) & ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    if (((unsigned __int16)(result)) < 98) goto loc_008F1111;
    result = PsGetCurrentServerSiloGlobals((unsigned int)(0xFFFEULL), a2, a3, a4);
    if (((unsigned int)(v_stack_mF0)) < 8) goto loc_008F10BA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9369218))) == (*(unsigned __int64 *)(v_stack_mE8))) goto loc_008F10D4;
loc_008F10BA:
    result = PsGetCurrentServerSiloGlobals(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9369218)), v_stack_mE8, v_stack_mF0, a4);
    if (((unsigned int)(v_stack_mF0)) < 8) goto loc_008F1111;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9369228))) != (*(unsigned __int64 *)(v_stack_mE8))) goto loc_008F1111;
loc_008F10D4:
loc_008F10E0:
    if ((unsigned __int16)(*(unsigned __int16 *)(a2 + 8)) == 0) goto loc_008F10F8;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 8))) == 92) goto loc_008F118F;
loc_008F10F2:
    result = (a2 + 8) + (2);
    goto loc_008F10E0;
loc_008F10F8:
    if (0 == 0) goto loc_008F133F;
    v_rbx = (0) - (a2);
    v_rbx = (v_rbx) >> (1);
loc_008F1107:
    if (v_rbx <= ((unsigned int)(0xFFFFFFFFULL))) goto loc_008F1147;
loc_008F1111:
    goto loc_008F111D;
loc_008F1118:
loc_008F111D:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_mE8, v_stack_mF0, a4);
    v_rsp = (v_rsp) + (336);
    return result;
loc_008F1147:
    if (((unsigned int)(v_stack_p8)) < 48) goto loc_008F1111;
    result = ((unsigned int)((unsigned int)(v_stack_p8))) + (-38);
    a4 = (a2 + result * 2) - (v_stack_m98);
loc_008F1170:
    if (39 - 1 == 0) goto loc_008F11A2;
    if ((unsigned __int16)(*(unsigned __int16 *)(a4 + v_stack_m98 * 1)) == 0) goto loc_008F11A2;
    *(unsigned __int16 *)(v_stack_m98) = (unsigned __int16)(*(unsigned __int16 *)(a4 + v_stack_m98 * 1));
    a1 = (v_stack_m98) + (2);
    goto loc_008F1170;
loc_008F118F:
    v_rdi = (unsigned int)(((unsigned int)(0xC0000095ULL)) + 1);
    if (((unsigned int)(v_rdi)) > 1) goto loc_008F1111;
    goto loc_008F10F2;
loc_008F11A2:
    result = a1 - 2;
    if (39 - 1 != 0) { result = a1; }
    v_rdi = (unsigned int)(0x80000005ULL);
    if (39 - 1 != 0) { v_rdi = 0; }
    *(unsigned __int16 *)(result) = 0;
    if (39 - 1 == 0) goto loc_008F1728;
    result = RtlInitUnicodeStringEx(v_stack_mF0, v_stack_m98, 39 - 1, a4);
    if (sign_flag) goto loc_008F111D;
    v_stack_p68 = v_stack_mA2;
    a2 = (unsigned int)((v_stack_mF0) >> (1));
    v_stack_p60 = v_stack_mA4;
    v_stack_p58 = v_stack_mA6;
    v_stack_p50 = v_stack_mA8;
    v_stack_p48 = v_stack_mAA;
    v_stack_p40 = v_stack_mAC;
    v_stack_p38 = v_stack_mAE;
    v_stack_p30 = v_stack_mB0;
    v_stack_p28 = v_stack_mCA;
    v_stack_p20 = v_stack_mCC;
    v_stack_mB0 = v_xmm0;
    result = ScanHexFormat(v_stack_mE8, a2, v_rip + 2473661, v_stack_mD0);
    if (((unsigned int)(result)) == -1) goto loc_008F1111;
loc_008F1270:
    a3 = (unsigned int)((0) + (8));
    if (a3 < 8) goto loc_008F1270;
    result = wcschr(a2 + 8, 92, a3, v_stack_mD0);
    if (result != 0) goto loc_008F1522;
loc_008F12B0:
    v_rbx = (-1) + 1;
    if ((*(unsigned __int16 *)(a2 + v_rbx * 2)) != 0) goto loc_008F12B0;
loc_008F12BA:
    if (v_rbx > ((unsigned int)(0xFFFFFFFFULL))) goto loc_008F1118;
    if (((unsigned int)(v_rbx)) < 48) goto loc_008F1111;
    if (a3 == 0) goto loc_008F12EE;
    v_rsi = (v_rbx + 1) + (2);
    if (0 == 0) goto loc_008F12EE;
loc_008F12E0:
    a1 = (-1) + 1;
    if ((*(unsigned __int16 *)(v_r14 + a1 * 2)) != 0) goto loc_008F12E0;
    v_rsi = (v_rsi) + (a1);
loc_008F12EE:
    if (v_rsi > ((unsigned int)(0xFFFFFFFFULL))) goto loc_008F1118;
    if (v_stack_m108 == 0) goto loc_008F146B;
    a3 = ((unsigned int)((unsigned int)(v_rbx))) + (-38);
    a3 = (a2 + a3 * 2) - (v_stack_m108);
loc_008F1320:
    if (39 - 1 == 0) goto loc_008F134A;
    if ((unsigned __int16)(*(unsigned __int16 *)(a3 + v_stack_m108 * 1)) == 0) goto loc_008F134A;
    *(unsigned __int16 *)(v_stack_m108) = (unsigned __int16)(*(unsigned __int16 *)(a3 + v_stack_m108 * 1));
    a1 = (v_stack_m108) + (2);
    goto loc_008F1320;
loc_008F133F:
    v_rbx = (a3) >> (1);
    goto loc_008F1107;
loc_008F134A:
    result = a1 - 2;
    if (39 - 1 != 0) { result = a1; }
    a1 = 0;
    v_rdi = (unsigned int)(0x80000005ULL);
    if (39 - 1 != 0) { v_rdi = 0; }
    *(unsigned __int16 *)(result) = 0;
    if (39 - 1 == 0) goto loc_008F1750;
    result = RtlInitUnicodeStringEx(v_stack_mE0, v_stack_m108, a3, v_stack_mD0);
    if (sign_flag) goto loc_008F111D;
    v_stack_p68 = v_stack_mA2;
    a2 = (unsigned int)((v_stack_mE0) >> (1));
    v_stack_p60 = v_stack_mA4;
    v_stack_p58 = v_stack_mA6;
    v_stack_p50 = v_stack_mA8;
    v_stack_p48 = v_stack_mAA;
    v_stack_p40 = v_stack_mAC;
    v_stack_p38 = v_stack_mAE;
    v_stack_p30 = v_stack_mB0;
    v_stack_p28 = v_stack_mBA;
    v_stack_p20 = v_stack_mBC;
    v_stack_mB0 = v_xmm0;
    result = ScanHexFormat(v_stack_mD8, a2, v_rip + 2473235, v_stack_mC0);
    if (((unsigned int)(result)) == -1) goto loc_008F1777;
    v_r11 = 0;
loc_008F1420:
    a3 = (unsigned int)((0) + (8));
    *(unsigned __int8 *)(v_stack_mB7 - 1) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mAE - 2));
    *(unsigned __int8 *)(v_stack_mB7 + 8 - 8) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mAE));
    *(unsigned __int8 *)(v_stack_mB7 + 8 - 7) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mAE + 16 - 14));
    *(unsigned __int8 *)(v_stack_mB7 + 8 - 6) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mAE + 16 - 12));
    *(unsigned __int8 *)(v_stack_mB7 + 8 - 5) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mAE + 16 - 10));
    *(unsigned __int8 *)(v_stack_mB7 + 8 - 4) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mAE + 16 - 8));
    *(unsigned __int8 *)(v_stack_mB7 + 8 - 3) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mAE + 16 - 6));
    *(unsigned __int8 *)(v_stack_mB7 + 8 - 2) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mAE + 16 - 4));
    if (a3 < 8) goto loc_008F1420;
    goto loc_008F146E;
loc_008F146B:
    v_r11 = 0;
loc_008F146E:
    if (((unsigned int)(v_rsi)) > ((unsigned int)((unsigned int)(a6)))) goto loc_008F1531;
    result = ((unsigned int)(a6)) - 1;
    if (result > ((unsigned int)(0x7FFFFFFEULL))) goto loc_008F16BF;
    v_stack_m108 = v_stack_p70;
    v_stack_p70 = (unsigned int)((unsigned int)((unsigned int)(a6)));
    if (((unsigned int)((unsigned int)(v_rbx))) >= 0x7FFFFFFFULL) goto loc_008F153B;
    a4 = ((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)((unsigned int)((unsigned int)(a6))));
    v_r12 = (a2) - (v_stack_p70);
loc_008F14C0:
    if (a4 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a6))))) * 1 == 0) goto loc_008F14E3;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r12 + v_stack_p70 * 1)) == 0) goto loc_008F14E3;
    *(unsigned __int16 *)(v_stack_p70) = (unsigned __int16)(*(unsigned __int16 *)(v_r12 + v_stack_p70 * 1));
    a3 = (0) + 1;
    a2 = (v_stack_p70) + (2);
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a6)))))) - (1);
    if (condition_is_not_equal) goto loc_008F14C0;
loc_008F14E3:
    result = a2 - 2;
    if (a1 != 0) { result = a2; }
    v_rsi = (unsigned int)(0x80000005ULL);
    if (a1 != 0) { v_rsi = 0; }
    *(unsigned __int16 *)(result) = 0;
    result = a3 - 1;
    if (a1 != 0) { result = a3; }
    a1 = ((unsigned int)((unsigned int)((unsigned int)(a6)))) - (result);
    v_stack_p70 = a1;
    v_stack_m108 = v_stack_p70 + result * 2;
    if (sign_flag) goto loc_008F1548;
loc_008F151A:
    goto loc_008F157D;
loc_008F1522:
    v_rbx = ((unsigned int)(0x7FFFFFFEULL)) - (v_stack_p70 + result * 2);
    v_rbx = (v_rbx) >> (1);
    goto loc_008F12BA;
loc_008F1531:
    goto loc_008F111D;
loc_008F153B:
    *(unsigned __int16 *)(v_stack_p70) = (unsigned __int16)(a1);
    v_rsi = (unsigned int)(0xC000000DULL);
    if (condition_is_below) { v_rsi = (unsigned int)(a1); }
loc_008F1548:
    v_stack_p28 = 0x800ULL;
    v_stack_p20 = v_stack_p70;
    result = RtlStringExHandleOtherFlagsW(v_stack_p70, (unsigned int)((unsigned int)((unsigned int)(a6))) + (unsigned int)((unsigned int)((unsigned int)(a6))) * 1, a3, v_stack_m108);
    if (((unsigned int)(v_rsi)) == 0x80000005ULL) goto loc_008F1781;
loc_008F1576:
loc_008F157D:
    if (sign_flag) goto loc_008F111D;
    *(unsigned __int64 *)(v_stack_p70) = result;
    if (a3 == 0) goto loc_008F111D;
    if ((v_stack_mF8 - 1) > v_rbx) goto loc_008F16F4;
    v_r15 = 0;
    a4 = (v_rbx) - (v_stack_mF8);
    v_r10 = (v_rip + 2211602) - (v_stack_mF8);
loc_008F15D0:
    if (a4 + v_stack_mF8 * 1 == 0) goto loc_008F15F3;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r10 + v_stack_mF8 * 1)) == 0) goto loc_008F15F3;
    *(unsigned __int16 *)(v_stack_mF8) = (unsigned __int16)(*(unsigned __int16 *)(v_r10 + v_stack_mF8 * 1));
    a3 = (0) + 1;
    a2 = (v_stack_mF8) + (2);
    a1 = (v_stack_mF8) - (1);
    if (condition_is_not_equal) goto loc_008F15D0;
loc_008F15F3:
    result = a2 - 2;
    if (a1 != 0) { result = a2; }
    a2 = (unsigned int)(0x80000005ULL);
    if (a1 != 0) { a2 = 0; }
    *(unsigned __int16 *)(result) = 0;
    result = a3 - 1;
    if (a1 != 0) { result = a3; }
    a3 = (v_stack_mF8) - (result);
    if (a1 == 0) goto loc_008F16D8;
loc_008F1626:
    if (!sign_flag) goto loc_008F16B4;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) == 0x80000005ULL) goto loc_008F16B4;
loc_008F1637:
    if (sign_flag) goto loc_008F111D;
    if (result + 2 == 0) goto loc_008F111D;
    if ((v_stack_mF8 - 1) > v_rbx) goto loc_008F1710;
    v_rbx = (v_rbx) - (v_stack_mF8);
    v_r14 = (result + 2) - (v_stack_mF8);
loc_008F1663:
    if (v_rbx + v_stack_mF8 * 1 == 0) goto loc_008F1683;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r14 + v_stack_mF8 * 1)) == 0) goto loc_008F1683;
    *(unsigned __int16 *)(v_stack_mF8) = (unsigned __int16)(*(unsigned __int16 *)(v_r14 + v_stack_mF8 * 1));
    a1 = (v_stack_mF8) + (2);
    a2 = (v_stack_mF8) - (1);
    if (condition_is_not_equal) goto loc_008F1663;
loc_008F1683:
    result = a1 - 2;
    if (a2 != 0) { result = a1; }
    v_rdi = (unsigned int)(0x80000005ULL);
    if (a2 != 0) { v_rdi = 0; }
    *(unsigned __int16 *)(result) = 0;
    if (a2 != 0) goto loc_008F111D;
    if (condition_is_below_or_equal) goto loc_008F111D;
    *(unsigned __int16 *)(v_stack_mF8) = 0;
    goto loc_008F111D;
loc_008F16B4:
    goto loc_008F1637;
loc_008F16BF:
    if (v_r10 == 0) goto loc_008F1576;
    *(unsigned __int16 *)(v_r15) = a3;
    goto loc_008F111D;
loc_008F16D8:
    result = (a3) & ((unsigned int)(0xC000000DULL));
    if (condition_is_below_or_equal) goto loc_008F1626;
    *(unsigned __int16 *)(v_stack_mF8 + result * 2) = 0;
    goto loc_008F1626;
loc_008F16F4:
    if (a3 == 0) goto loc_008F178F;
    a1 = 0;
    *(unsigned __int16 *)(v_stack_mF8 + result * 2) = 0;
    goto loc_008F111D;
loc_008F1710:
    if (a3 == 0) goto loc_008F111D;
    *(unsigned __int16 *)(v_stack_mF8 + result * 2) = 0;
    goto loc_008F111D;
loc_008F1728:
    v_stack_p28 = 0x800ULL;
    v_stack_p20 = v_stack_m100;
    result = RtlStringExHandleOtherFlagsW(v_stack_m98, 78, result, v_stack_mF8);
    goto loc_008F111D;
loc_008F1750:
    v_stack_p28 = 0x800ULL;
    v_stack_p20 = v_stack_m100;
    result = RtlStringExHandleOtherFlagsW(v_r10, 78, result, v_stack_mF8);
    goto loc_008F111D;
loc_008F1777:
    goto loc_008F111D;
loc_008F1781:
    goto loc_008F151A;
loc_008F178F:
    v_r15 = 0;
    goto loc_008F1637;
}
```

## 5. (Beta) C Style

```c
int64_t CmGetDeviceInterfaceSubkeyPath(int64_t Arg1, void *Arg2, uint8_t Arg3, int64_t Arg4, int64_t Arg5, void *Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg6 = (uint8_t *)Arg6;

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
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m48;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA2;
    uint64_t v_stack_mA4;
    uint64_t v_stack_mA6;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mAA;
    uint64_t v_stack_mAC;
    uint64_t v_stack_mAE;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB7;
    uint64_t v_stack_mBA;
    uint64_t v_stack_mBC;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC7;
    uint64_t v_stack_mCA;
    uint64_t v_stack_mCC;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint16_t v_stack_mEE;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (336);
    result = (*(uint64_t *)(v_rip + 0x51970D)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m118 = Arg5;
    local_r14 = 0;
    v_stack_m108 = Arg4;
    v_stack_mF8 = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    v_stack_mF0 = v_xmm0;
    v_stack_mD0 = v_xmm0;
    result = RtlInitUnicodeStringEx(v_stack_mF0, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_008F1111;
    result = (uint16_t)((v_stack_mEE) & ((uint16_t)((uint32_t)(0xFFFEULL))));
    if (((uint16_t)(result)) < 98) goto loc_008F1111;
    result = PsGetCurrentServerSiloGlobals((uint32_t)(0xFFFEULL), Arg2, Arg3, Arg4);
    if (((uint32_t)(v_stack_mF0)) < 8) goto loc_008F10BA;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x8EF682))) == (*(uint64_t *)(v_stack_mE8))) goto loc_008F10D4;
loc_008F10BA:
    result = PsGetCurrentServerSiloGlobals(*(uint64_t *)(*(uint64_t *)(v_rip - 0x8EF682)), v_stack_mE8, v_stack_mF0, Arg4);
    if (((uint32_t)(v_stack_mF0)) < 8) goto loc_008F1111;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x8EF68C))) != (*(uint64_t *)(v_stack_mE8))) goto loc_008F1111;
loc_008F10D4:
loc_008F10E0:
    if ((uint16_t)(*(uint16_t *)(arg2 + 0x8)) == 0) goto loc_008F10F8;
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x8))) == 92) goto loc_008F118F;
loc_008F10F2:
    result = (Arg2 + 8) + (2);
    goto loc_008F10E0;
loc_008F10F8:
    if (0 == 0) goto loc_008F133F;
    local_rbx = (0) - (Arg2);
    local_rbx = (local_rbx) >> (1);
loc_008F1107:
    if (local_rbx <= ((uint32_t)(0xFFFFFFFFULL))) goto loc_008F1147;
loc_008F1111:
    goto loc_008F111D;
loc_008F1118:
loc_008F111D:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_mE8, v_stack_mF0, Arg4);
    local_rsp = (local_rsp) + (336);
    return result;
loc_008F1147:
    if (((uint32_t)(v_stack_p8)) < 48) goto loc_008F1111;
    result = ((uint32_t)((uint32_t)(v_stack_p8))) + (-38);
    Arg4 = (Arg2 + result * 2) - (v_stack_m98);
loc_008F1170:
    if (39 - 1 == 0) goto loc_008F11A2;
    if ((uint16_t)(*(uint16_t *)(Arg4 + v_stack_m98 * 1)) == 0) goto loc_008F11A2;
    *(uint16_t *)(v_stack_m98) = (uint16_t)(*(uint16_t *)(Arg4 + v_stack_m98 * 1));
    Arg1 = (v_stack_m98) + (2);
    goto loc_008F1170;
loc_008F118F:
    local_rdi = (uint32_t)(((uint32_t)(0xC0000095ULL)) + 1);
    if (((uint32_t)(local_rdi)) > 1) goto loc_008F1111;
    goto loc_008F10F2;
loc_008F11A2:
    result = Arg1 - 2;
    if (39 - 1 != 0) { result = Arg1; }
    local_rdi = (uint32_t)(0x80000005ULL);
    if (39 - 1 != 0) { local_rdi = 0; }
    *(uint16_t *)(result) = 0;
    if (39 - 1 == 0) goto loc_008F1728;
    result = RtlInitUnicodeStringEx(v_stack_mF0, v_stack_m98, 39 - 1, Arg4);
    if (sign_flag) goto loc_008F111D;
    v_stack_p68 = v_stack_mA2;
    Arg2 = (uint32_t)((v_stack_mF0) >> (1));
    v_stack_p60 = v_stack_mA4;
    v_stack_p58 = v_stack_mA6;
    v_stack_p50 = v_stack_mA8;
    v_stack_p48 = v_stack_mAA;
    v_stack_p40 = v_stack_mAC;
    v_stack_p38 = v_stack_mAE;
    v_stack_p30 = v_stack_mB0;
    v_stack_p28 = v_stack_mCA;
    v_stack_p20 = v_stack_mCC;
    v_stack_mB0 = v_xmm0;
    result = ScanHexFormat(v_stack_mE8, Arg2, v_rip + 2473661, v_stack_mD0);
    if (((uint32_t)(result)) == -1) goto loc_008F1111;
loc_008F1270:
    Arg3 = (uint32_t)((0) + (8));
    if (Arg3 < 8) goto loc_008F1270;
    result = wcschr(Arg2 + 8, 92, Arg3, v_stack_mD0);
    if (result != 0) goto loc_008F1522;
loc_008F12B0:
    local_rbx = (-1) + 1;
    if ((*(uint16_t *)(arg2 + local_rbx * 2)) != 0) goto loc_008F12B0;
loc_008F12BA:
    if (local_rbx > ((uint32_t)(0xFFFFFFFFULL))) goto loc_008F1118;
    if (((uint32_t)(local_rbx)) < 48) goto loc_008F1111;
    if (Arg3 == 0) goto loc_008F12EE;
    local_rsi = (local_rbx + 1) + (2);
    if (0 == 0) goto loc_008F12EE;
loc_008F12E0:
    Arg1 = (-1) + 1;
    if ((*(uint16_t *)(local_r14 + Arg1 * 2)) != 0) goto loc_008F12E0;
    local_rsi = (local_rsi) + (Arg1);
loc_008F12EE:
    if (local_rsi > ((uint32_t)(0xFFFFFFFFULL))) goto loc_008F1118;
    if (v_stack_m108 == 0) goto loc_008F146B;
    Arg3 = ((uint32_t)((uint32_t)(local_rbx))) + (-38);
    Arg3 = (Arg2 + Arg3 * 2) - (v_stack_m108);
loc_008F1320:
    if (39 - 1 == 0) goto loc_008F134A;
    if ((uint16_t)(*(uint16_t *)(Arg3 + v_stack_m108 * 1)) == 0) goto loc_008F134A;
    *(uint16_t *)(v_stack_m108) = (uint16_t)(*(uint16_t *)(Arg3 + v_stack_m108 * 1));
    Arg1 = (v_stack_m108) + (2);
    goto loc_008F1320;
loc_008F133F:
    local_rbx = (Arg3) >> (1);
    goto loc_008F1107;
loc_008F134A:
    result = Arg1 - 2;
    if (39 - 1 != 0) { result = Arg1; }
    Arg1 = 0;
    local_rdi = (uint32_t)(0x80000005ULL);
    if (39 - 1 != 0) { local_rdi = 0; }
    *(uint16_t *)(result) = 0;
    if (39 - 1 == 0) goto loc_008F1750;
    result = RtlInitUnicodeStringEx(v_stack_mE0, v_stack_m108, Arg3, v_stack_mD0);
    if (sign_flag) goto loc_008F111D;
    v_stack_p68 = v_stack_mA2;
    Arg2 = (uint32_t)((v_stack_mE0) >> (1));
    v_stack_p60 = v_stack_mA4;
    v_stack_p58 = v_stack_mA6;
    v_stack_p50 = v_stack_mA8;
    v_stack_p48 = v_stack_mAA;
    v_stack_p40 = v_stack_mAC;
    v_stack_p38 = v_stack_mAE;
    v_stack_p30 = v_stack_mB0;
    v_stack_p28 = v_stack_mBA;
    v_stack_p20 = v_stack_mBC;
    v_stack_mB0 = v_xmm0;
    result = ScanHexFormat(v_stack_mD8, Arg2, v_rip + 2473235, v_stack_mC0);
    if (((uint32_t)(result)) == -1) goto loc_008F1777;
    local_r11 = 0;
loc_008F1420:
    Arg3 = (uint32_t)((0) + (8));
    *(uint8_t *)(v_stack_mB7 - 0x1) = (uint8_t)(*(uint8_t *)(v_stack_mAE - 0x2));
    *(uint8_t *)(v_stack_mB7 + 0x8 - 0x8) = (uint8_t)(*(uint8_t *)(v_stack_mAE));
    *(uint8_t *)(v_stack_mB7 + 0x8 - 0x7) = (uint8_t)(*(uint8_t *)(v_stack_mAE + 0x10 - 0xE));
    *(uint8_t *)(v_stack_mB7 + 0x8 - 0x6) = (uint8_t)(*(uint8_t *)(v_stack_mAE + 0x10 - 0xC));
    *(uint8_t *)(v_stack_mB7 + 0x8 - 0x5) = (uint8_t)(*(uint8_t *)(v_stack_mAE + 0x10 - 0xA));
    *(uint8_t *)(v_stack_mB7 + 0x8 - 0x4) = (uint8_t)(*(uint8_t *)(v_stack_mAE + 0x10 - 0x8));
    *(uint8_t *)(v_stack_mB7 + 0x8 - 0x3) = (uint8_t)(*(uint8_t *)(v_stack_mAE + 0x10 - 0x6));
    *(uint8_t *)(v_stack_mB7 + 0x8 - 0x2) = (uint8_t)(*(uint8_t *)(v_stack_mAE + 0x10 - 0x4));
    if (Arg3 < 8) goto loc_008F1420;
    goto loc_008F146E;
loc_008F146B:
    local_r11 = 0;
loc_008F146E:
    if (((uint32_t)(local_rsi)) > ((uint32_t)((uint32_t)(Arg6)))) goto loc_008F1531;
    result = ((uint32_t)(Arg6)) - 1;
    if (result > ((uint32_t)(0x7FFFFFFEULL))) goto loc_008F16BF;
    v_stack_m108 = v_stack_p70;
    v_stack_p70 = (uint32_t)((uint32_t)((uint32_t)(Arg6)));
    if (((uint32_t)((uint32_t)(local_rbx))) >= 0x7FFFFFFFULL) goto loc_008F153B;
    Arg4 = ((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)((uint32_t)((uint32_t)(Arg6))));
    local_r12 = (Arg2) - (v_stack_p70);
loc_008F14C0:
    if (Arg4 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg6))))) * 1 == 0) goto loc_008F14E3;
    if ((uint16_t)(*(uint16_t *)(local_r12 + v_stack_p70 * 1)) == 0) goto loc_008F14E3;
    *(uint16_t *)(v_stack_p70) = (uint16_t)(*(uint16_t *)(local_r12 + v_stack_p70 * 1));
    Arg3 = (0) + 1;
    Arg2 = (v_stack_p70) + (2);
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg6)))))) - (1);
    if (condition_is_not_equal) goto loc_008F14C0;
loc_008F14E3:
    result = Arg2 - 2;
    if (Arg1 != 0) { result = Arg2; }
    local_rsi = (uint32_t)(0x80000005ULL);
    if (Arg1 != 0) { local_rsi = 0; }
    *(uint16_t *)(result) = 0;
    result = Arg3 - 1;
    if (Arg1 != 0) { result = Arg3; }
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(Arg6)))) - (result);
    v_stack_p70 = Arg1;
    v_stack_m108 = v_stack_p70 + result * 2;
    if (sign_flag) goto loc_008F1548;
loc_008F151A:
    goto loc_008F157D;
loc_008F1522:
    local_rbx = ((uint32_t)(0x7FFFFFFEULL)) - (v_stack_p70 + result * 2);
    local_rbx = (local_rbx) >> (1);
    goto loc_008F12BA;
loc_008F1531:
    goto loc_008F111D;
loc_008F153B:
    *(uint16_t *)(v_stack_p70) = (uint16_t)(Arg1);
    local_rsi = (uint32_t)(0xC000000DULL);
    if (condition_is_below) { local_rsi = (uint32_t)(Arg1); }
loc_008F1548:
    v_stack_p28 = 0x800ULL;
    v_stack_p20 = v_stack_p70;
    result = RtlStringExHandleOtherFlagsW(v_stack_p70, (uint32_t)((uint32_t)((uint32_t)(Arg6))) + (uint32_t)((uint32_t)((uint32_t)(Arg6))) * 1, Arg3, v_stack_m108);
    if (((uint32_t)(local_rsi)) == 0x80000005ULL) goto loc_008F1781;
loc_008F1576:
loc_008F157D:
    if (sign_flag) goto loc_008F111D;
    *(uint64_t *)(v_stack_p70) = result;
    if (Arg3 == 0) goto loc_008F111D;
    if ((v_stack_mF8 - 1) > local_rbx) goto loc_008F16F4;
    local_r15 = 0;
    Arg4 = (local_rbx) - (v_stack_mF8);
    local_r10 = (v_rip + 2211602) - (v_stack_mF8);
loc_008F15D0:
    if (Arg4 + v_stack_mF8 * 1 == 0) goto loc_008F15F3;
    if ((uint16_t)(*(uint16_t *)(local_r10 + v_stack_mF8 * 1)) == 0) goto loc_008F15F3;
    *(uint16_t *)(v_stack_mF8) = (uint16_t)(*(uint16_t *)(local_r10 + v_stack_mF8 * 1));
    Arg3 = (0) + 1;
    Arg2 = (v_stack_mF8) + (2);
    Arg1 = (v_stack_mF8) - (1);
    if (condition_is_not_equal) goto loc_008F15D0;
loc_008F15F3:
    result = Arg2 - 2;
    if (Arg1 != 0) { result = Arg2; }
    Arg2 = (uint32_t)(0x80000005ULL);
    if (Arg1 != 0) { Arg2 = 0; }
    *(uint16_t *)(result) = 0;
    result = Arg3 - 1;
    if (Arg1 != 0) { result = Arg3; }
    Arg3 = (v_stack_mF8) - (result);
    if (Arg1 == 0) goto loc_008F16D8;
loc_008F1626:
    if (!sign_flag) goto loc_008F16B4;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) == 0x80000005ULL) goto loc_008F16B4;
loc_008F1637:
    if (sign_flag) goto loc_008F111D;
    if (result + 2 == 0) goto loc_008F111D;
    if ((v_stack_mF8 - 1) > local_rbx) goto loc_008F1710;
    local_rbx = (local_rbx) - (v_stack_mF8);
    local_r14 = (result + 2) - (v_stack_mF8);
loc_008F1663:
    if (local_rbx + v_stack_mF8 * 1 == 0) goto loc_008F1683;
    if ((uint16_t)(*(uint16_t *)(local_r14 + v_stack_mF8 * 1)) == 0) goto loc_008F1683;
    *(uint16_t *)(v_stack_mF8) = (uint16_t)(*(uint16_t *)(local_r14 + v_stack_mF8 * 1));
    Arg1 = (v_stack_mF8) + (2);
    Arg2 = (v_stack_mF8) - (1);
    if (condition_is_not_equal) goto loc_008F1663;
loc_008F1683:
    result = Arg1 - 2;
    if (Arg2 != NULL) { result = Arg1; }
    local_rdi = (uint32_t)(0x80000005ULL);
    if (Arg2 != NULL) { local_rdi = 0; }
    *(uint16_t *)(result) = 0;
    if (Arg2 != NULL) goto loc_008F111D;
    if (condition_is_below_or_equal) goto loc_008F111D;
    *(uint16_t *)(v_stack_mF8) = 0;
    goto loc_008F111D;
loc_008F16B4:
    goto loc_008F1637;
loc_008F16BF:
    if (local_r10 == 0) goto loc_008F1576;
    *(uint16_t *)(local_r15) = Arg3;
    goto loc_008F111D;
loc_008F16D8:
    result = (Arg3) & ((uint32_t)(0xC000000DULL));
    if (condition_is_below_or_equal) goto loc_008F1626;
    *(uint16_t *)(v_stack_mF8 + result * 2) = 0;
    goto loc_008F1626;
loc_008F16F4:
    if (Arg3 == 0) goto loc_008F178F;
    Arg1 = 0;
    *(uint16_t *)(v_stack_mF8 + result * 2) = 0;
    goto loc_008F111D;
loc_008F1710:
    if (Arg3 == 0) goto loc_008F111D;
    *(uint16_t *)(v_stack_mF8 + result * 2) = 0;
    goto loc_008F111D;
loc_008F1728:
    v_stack_p28 = 0x800ULL;
    v_stack_p20 = v_stack_m100;
    result = RtlStringExHandleOtherFlagsW(v_stack_m98, 78, result, v_stack_mF8);
    goto loc_008F111D;
loc_008F1750:
    v_stack_p28 = 0x800ULL;
    v_stack_p20 = v_stack_m100;
    result = RtlStringExHandleOtherFlagsW(local_r10, 78, result, v_stack_mF8);
    goto loc_008F111D;
loc_008F1777:
    goto loc_008F111D;
loc_008F1781:
    goto loc_008F151A;
loc_008F178F:
    local_r15 = 0;
    goto loc_008F1637;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0 + r8*2` | `64` | `R` |
| `Arg2` | `+ 0x0 + rax*2` | `64` | `R` |
| `Arg2` | `+ 0x0 + rbx*2` | `16` | `R` |
| `Arg2` | `+ 0x0 + rcx*1` | `16` | `R` |
| `Arg2` | `+ 0x0 + rdx*1` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg6` | `+ 0x0 + r10*1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F1010&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
