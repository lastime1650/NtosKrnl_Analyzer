# MiCopyToCfgBitMap

- RVA: `0x008D1140`–`0x008D16E4` (길이 `1,444` bytes)
- VA: `0x00000001408D1140`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00084B40`
- 디코드: `363`개 명령, `1,444/1,444` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008D127E` → [MiSplitPrivatePage](../../text/2A/MiSplitPrivatePage_function_002A6210.md) (function, `0x002A6210`)
- `0x008D1299` → [MiCopyToUserVa](../../text/3D/MiCopyToUserVa_function_003D1E68.md) (function, `0x003D1E68`)
- `0x008D12ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008D1309` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008D1362` → [RtlClearAllBitsEx](../../text/47/RtlClearAllBitsEx_function_00477DC0.md) (function, `0x00477DC0`)
- `0x008D138C` → [MiImageCfgEnumRvaListFirst](../8C/MiImageCfgEnumRvaListFirst_function_008CF598.md) (function, `0x008CF598`)
- `0x008D13EE` → [MiImageCfgEnumRvaListNext](MiImageCfgEnumRvaListNext_function_008D16F0.md) (function, `0x008D16F0`)
- `0x008D1430` → [RtlSetBitsEx](../../text/3B/RtlSetBitsEx_function_003B6570.md) (function, `0x003B6570`)
- `0x008D144F` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x008D14B8` → [MiEliminateZeroPages](../8C/MiEliminateZeroPages_function_008CF1A0.md) (function, `0x008CF1A0`)
- `0x008D1506` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008D15A4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008D1667` → [MiReadVadFlags2](../../text/45/MiReadVadFlags2_function_00452C1C.md) (function, `0x00452C1C`)
- `0x008D16B4` → [RtlClearBitsEx](../../text/29/RtlClearBitsEx_function_00297740.md) (function, `0x00297740`)

### Direct callers
- [MiMarkSharedImageCfgBits](MiMarkSharedImageCfgBits_function_008D0CC4.md) at `0x008D0F5A`
- [MiPopulateCfgBitMap](MiPopulateCfgBitMap_function_008D0FA4.md) at `0x008D10A6`

### Static image references
- `0x008D116E` → RVA `0x00E0A740` (`.data`; read)
- `0x008D11F3` → RVA `0x00E37460` (`.data`; read)
- `0x008D11FD` → RVA `0x00E37498` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x008D127E` → [MiSplitPrivatePage](../../text/2A/MiSplitPrivatePage_function_002A6210.md) (`PAGE` → `.text`)
  - `0x008D1299` → [MiCopyToUserVa](../../text/3D/MiCopyToUserVa_function_003D1E68.md) (`PAGE` → `.text`)
  - `0x008D12ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008D1309` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008D1362` → [RtlClearAllBitsEx](../../text/47/RtlClearAllBitsEx_function_00477DC0.md) (`PAGE` → `.text`)
  - `0x008D1430` → [RtlSetBitsEx](../../text/3B/RtlSetBitsEx_function_003B6570.md) (`PAGE` → `.text`)
  - `0x008D144F` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x008D1506` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008D15A4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008D1667` → [MiReadVadFlags2](../../text/45/MiReadVadFlags2_function_00452C1C.md) (`PAGE` → `.text`)
  - `0x008D16B4` → [RtlClearBitsEx](../../text/29/RtlClearBitsEx_function_00297740.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008D1140  40 55                           push rbp
008D1142  41 56                           push r14
008D1144  41 57                           push r15
008D1146  48 81 EC B0 00 00 00            sub rsp, 0xb0
008D114D  48 8D 6C 24 20                  lea rbp, [rsp + 0x20]
008D1152  48 89 9D B0 00 00 00            mov qword ptr [rbp + 0xb0], rbx
008D1159  48 89 B5 B8 00 00 00            mov qword ptr [rbp + 0xb8], rsi
008D1160  48 89 BD C0 00 00 00            mov qword ptr [rbp + 0xc0], rdi
008D1167  4C 89 A5 C8 00 00 00            mov qword ptr [rbp + 0xc8], r12
008D116E  48 8B 05 CB 95 53 00            mov rax, qword ptr [rip + 0x5395cb]
008D1175  48 33 C5                        xor rax, rbp
008D1178  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
008D117F  41 8B C1                        mov eax, r9d
008D1182  89 45 1C                        mov dword ptr [rbp + 0x1c], eax
008D1185  4C 8B FA                        mov r15, rdx
008D1188  48 89 55 38                     mov qword ptr [rbp + 0x38], rdx
008D118C  48 89 4D 70                     mov qword ptr [rbp + 0x70], rcx
008D1190  4C 8B B5 D0 00 00 00            mov r14, qword ptr [rbp + 0xd0]
008D1197  4C 89 75 78                     mov qword ptr [rbp + 0x78], r14
008D119B  0F 57 C0                        xorps xmm0, xmm0
008D119E  0F 11 45 58                     movups xmmword ptr [rbp + 0x58], xmm0
008D11A2  BB 01 00 00 00                  mov ebx, 1
008D11A7  48 3B D3                        cmp rdx, rbx
008D11AA  0F 87 12 03 00 00               ja 0x1408d14c2
008D11B0  4C 89 7D 50                     mov qword ptr [rbp + 0x50], r15
008D11B4  4D 8B DF                        mov r11, r15
008D11B7  4C 89 7D 08                     mov qword ptr [rbp + 8], r15
008D11BB  33 D2                           xor edx, edx
008D11BD  89 55 00                        mov dword ptr [rbp], edx
008D11C0  8B 85 E0 00 00 00               mov eax, dword ptr [rbp + 0xe0]
008D11C6  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
008D11CA  21 55 04                        and dword ptr [rbp + 4], edx
008D11CD  41 BA 00 10 00 00               mov r10d, 0x1000
008D11D3  4C 89 55 10                     mov qword ptr [rbp + 0x10], r10
008D11D7  21 55 18                        and dword ptr [rbp + 0x18], edx
008D11DA  48 8B 8D F8 00 00 00            mov rcx, qword ptr [rbp + 0xf8]
008D11E1  48 85 C9                        test rcx, rcx
008D11E4  0F 85 7D 04 00 00               jne 0x1408d1667
008D11EA  4C 3B FB                        cmp r15, rbx
008D11ED  0F 87 4E 02 00 00               ja 0x1408d1441
008D11F3  48 8B 3D 66 62 56 00            mov rdi, qword ptr [rip + 0x566266]
008D11FA  4D 85 FF                        test r15, r15
008D11FD  48 0F 44 3D 93 62 56 00         cmove rdi, qword ptr [rip + 0x566293]
008D1205  48 89 7D 28                     mov qword ptr [rbp + 0x28], rdi
008D1209  49 8B DE                        mov rbx, r14
008D120C  41 8B CE                        mov ecx, r14d
008D120F  41 B8 FF 0F 00 00               mov r8d, 0xfff
008D1215  41 23 C8                        and ecx, r8d
008D1218  4C 8B 8D F0 00 00 00            mov r9, qword ptr [rbp + 0xf0]
008D121F  45 8B E1                        mov r12d, r9d
008D1222  45 23 E0                        and r12d, r8d
008D1225  45 03 E0                        add r12d, r8d
008D1228  44 03 E1                        add r12d, ecx
008D122B  4C 89 65 48                     mov qword ptr [rbp + 0x48], r12
008D122F  4C 89 65 68                     mov qword ptr [rbp + 0x68], r12
008D1233  4C 89 8D 80 00 00 00            mov qword ptr [rbp + 0x80], r9
008D123A  33 F6                           xor esi, esi
008D123C  48 89 5D 40                     mov qword ptr [rbp + 0x40], rbx
008D1240  4D 85 C9                        test r9, r9
008D1243  0F 84 99 00 00 00               je 0x1408d12e2
008D1249  45 8D 42 FF                     lea r8d, [r10 - 1]
008D124D  8B CB                           mov ecx, ebx
008D124F  41 23 C8                        and ecx, r8d
008D1252  49 8B C2                        mov rax, r10
008D1255  48 2B C1                        sub rax, rcx
008D1258  41 8B F2                        mov esi, r10d
008D125B  2B F1                           sub esi, ecx
008D125D  49 3B C1                        cmp rax, r9
008D1260  41 0F 43 F1                     cmovae esi, r9d
008D1264  89 75 30                        mov dword ptr [rbp + 0x30], esi
008D1267  44 8B E6                        mov r12d, esi
008D126A  49 83 FF 01                     cmp r15, 1
008D126E  0F 87 C4 00 00 00               ja 0x1408d1338
008D1274  48 8B 95 D8 00 00 00            mov rdx, qword ptr [rbp + 0xd8]
008D127B  48 8B CB                        mov rcx, rbx
008D127E  E8 8D 4F 9D FF                  call 0x1402a6210
008D1283  8B F0                           mov esi, eax
008D1285  85 C0                           test eax, eax
008D1287  78 55                           js 0x1408d12de
008D1289  4D 8B CC                        mov r9, r12
008D128C  4C 8B C7                        mov r8, rdi
008D128F  48 8B 95 D8 00 00 00            mov rdx, qword ptr [rbp + 0xd8]
008D1296  48 8B CB                        mov rcx, rbx
008D1299  E8 CA 0B B0 FF                  call 0x1403d1e68
008D129E  8B F0                           mov esi, eax
008D12A0  85 C0                           test eax, eax
008D12A2  78 3A                           js 0x1408d12de
008D12A4  8B 55 00                        mov edx, dword ptr [rbp]
008D12A7  85 D2                           test edx, edx
008D12A9  0F 85 8B 02 00 00               jne 0x1408d153a
008D12AF  49 83 FF 01                     cmp r15, 1
008D12B3  0F 87 28 02 00 00               ja 0x1408d14e1
008D12B9  4C 8B 5D 08                     mov r11, qword ptr [rbp + 8]
008D12BD  4C 8B 55 10                     mov r10, qword ptr [rbp + 0x10]
008D12C1  49 03 DC                        add rbx, r12
008D12C4  4C 8B 8D F0 00 00 00            mov r9, qword ptr [rbp + 0xf0]
008D12CB  4D 2B CC                        sub r9, r12
008D12CE  4C 89 8D F0 00 00 00            mov qword ptr [rbp + 0xf0], r9
008D12D5  4C 8B 65 48                     mov r12, qword ptr [rbp + 0x48]
008D12D9  E9 5E FF FF FF                  jmp 0x1408d123c
008D12DE  4C 8B 65 48                     mov r12, qword ptr [rbp + 0x48]
008D12E2  83 7D 04 00                     cmp dword ptr [rbp + 4], 0
008D12E6  74 0A                           je 0x1408d12f2
008D12E8  33 D2                           xor edx, edx
008D12EA  48 8B CF                        mov rcx, rdi
008D12ED  E8 7E 15 2B 00                  call 0x140b82870
008D12F2  48 83 7D 50 00                  cmp qword ptr [rbp + 0x50], 0
008D12F7  0F 85 78 01 00 00               jne 0x1408d1475
008D12FD  8B C6                           mov eax, esi
008D12FF  48 8B 8D 88 00 00 00            mov rcx, qword ptr [rbp + 0x88]
008D1306  48 33 CD                        xor rcx, rbp
008D1309  E8 32 B3 DD FF                  call 0x1406ac640
008D130E  48 8B 9D B0 00 00 00            mov rbx, qword ptr [rbp + 0xb0]
008D1315  48 8B B5 B8 00 00 00            mov rsi, qword ptr [rbp + 0xb8]
008D131C  48 8B BD C0 00 00 00            mov rdi, qword ptr [rbp + 0xc0]
008D1323  4C 8B A5 C8 00 00 00            mov r12, qword ptr [rbp + 0xc8]
008D132A  48 8D A5 90 00 00 00            lea rsp, [rbp + 0x90]
008D1331  41 5F                           pop r15
008D1333  41 5E                           pop r14
008D1335  5D                              pop rbp
008D1336  C3                              ret
008D1337  CC                              int3
008D1338  8B 45 1C                        mov eax, dword ptr [rbp + 0x1c]
008D133B  83 F8 01                        cmp eax, 1
008D133E  0F 84 05 02 00 00               je 0x1408d1549
008D1344  44 8B E6                        mov r12d, esi
008D1347  85 C0                           test eax, eax
008D1349  0F 85 25 FF FF FF               jne 0x1408d1274
008D134F  48 89 7D 60                     mov qword ptr [rbp + 0x60], rdi
008D1353  8D 0C F5 00 00 00 00            lea ecx, [rsi*8]
008D135A  48 89 4D 58                     mov qword ptr [rbp + 0x58], rcx
008D135E  48 8D 4D 58                     lea rcx, [rbp + 0x58]
008D1362  E8 59 6A BA FF                  call 0x140477dc0
008D1367  D1 EE                           shr esi, 1
008D1369  C1 E6 07                        shl esi, 7
008D136C  03 B5 E0 00 00 00               add esi, dword ptr [rbp + 0xe0]
008D1372  48 8B 95 E8 00 00 00            mov rdx, qword ptr [rbp + 0xe8]
008D1379  44 8B 02                        mov r8d, dword ptr [rdx]
008D137C  4C 8B 65 50                     mov r12, qword ptr [rbp + 0x50]
008D1380  45 85 C0                        test r8d, r8d
008D1383  75 13                           jne 0x1408d1398
008D1385  44 8B 45 18                     mov r8d, dword ptr [rbp + 0x18]
008D1389  49 8B CC                        mov rcx, r12
008D138C  E8 07 E2 FF FF                  call 0x1408cf598
008D1391  44 8B C0                        mov r8d, eax
008D1394  85 C0                           test eax, eax
008D1396  74 72                           je 0x1408d140a
008D1398  44 8B B5 E0 00 00 00            mov r14d, dword ptr [rbp + 0xe0]
008D139F  4C 8B 7D 70                     mov r15, qword ptr [rbp + 0x70]
008D13A3  45 3B C6                        cmp r8d, r14d
008D13A6  72 3C                           jb 0x1408d13e4
008D13A8  44 3B C6                        cmp r8d, esi
008D13AB  73 4D                           jae 0x1408d13fa
008D13AD  48 8B 8D E8 00 00 00            mov rcx, qword ptr [rbp + 0xe8]
008D13B4  8B 51 04                        mov edx, dword ptr [rcx + 4]
008D13B7  F6 C2 01                        test dl, 1
008D13BA  74 28                           je 0x1408d13e4
008D13BC  41 8B C8                        mov ecx, r8d
008D13BF  41 2B CE                        sub ecx, r14d
008D13C2  48 C1 E9 04                     shr rcx, 4
008D13C6  48 03 C9                        add rcx, rcx
008D13C9  41 83 E0 0F                     and r8d, 0xf
008D13CD  45 3B 47 18                     cmp r8d, dword ptr [r15 + 0x18]
008D13D1  75 50                           jne 0x1408d1423
008D13D3  48 8D 41 01                     lea rax, [rcx + 1]
008D13D7  F6 C2 04                        test dl, 4
008D13DA  75 5B                           jne 0x1408d1437
008D13DC  48 0F AB 0F                     bts qword ptr [rdi], rcx
008D13E0  48 0F B3 07                     btr qword ptr [rdi], rax
008D13E4  48 8B 95 E8 00 00 00            mov rdx, qword ptr [rbp + 0xe8]
008D13EB  49 8B CC                        mov rcx, r12
008D13EE  E8 FD 02 00 00                  call 0x1408d16f0
008D13F3  44 8B C0                        mov r8d, eax
008D13F6  85 C0                           test eax, eax
008D13F8  75 A9                           jne 0x1408d13a3
008D13FA  4C 8B B5 D0 00 00 00            mov r14, qword ptr [rbp + 0xd0]
008D1401  4C 8B 7D 38                     mov r15, qword ptr [rbp + 0x38]
008D1405  45 85 C0                        test r8d, r8d
008D1408  75 0A                           jne 0x1408d1414
008D140A  48 8B 85 E8 00 00 00            mov rax, qword ptr [rbp + 0xe8]
008D1411  83 08 FF                        or dword ptr [rax], 0xffffffff
008D1414  89 B5 E0 00 00 00               mov dword ptr [rbp + 0xe0], esi
008D141A  44 8B 65 30                     mov r12d, dword ptr [rbp + 0x30]
008D141E  E9 51 FE FF FF                  jmp 0x1408d1274
008D1423  41 B8 02 00 00 00               mov r8d, 2
008D1429  48 8B D1                        mov rdx, rcx
008D142C  48 8D 4D 58                     lea rcx, [rbp + 0x58]
008D1430  E8 3B 51 AE FF                  call 0x1403b6570
008D1435  EB AD                           jmp 0x1408d13e4
008D1437  48 0F B3 0F                     btr qword ptr [rdi], rcx
008D143B  48 0F AB 07                     bts qword ptr [rdi], rax
008D143F  EB A3                           jmp 0x1408d13e4
008D1441  49 8B D2                        mov rdx, r10
008D1444  B9 40 00 00 00                  mov ecx, 0x40
008D1449  41 B8 4D 69 54 65               mov r8d, 0x6554694d
008D144F  E8 EC A0 A8 FF                  call 0x14035b540
008D1454  48 8B F8                        mov rdi, rax
008D1457  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
008D145B  4D 8B DF                        mov r11, r15
008D145E  48 85 C0                        test rax, rax
008D1461  0F 84 25 02 00 00               je 0x1408d168c
008D1467  89 5D 04                        mov dword ptr [rbp + 4], ebx
008D146A  33 D2                           xor edx, edx
008D146C  4C 8B 55 10                     mov r10, qword ptr [rbp + 0x10]
008D1470  E9 94 FD FF FF                  jmp 0x1408d1209
008D1475  85 F6                           test esi, esi
008D1477  0F 88 C0 01 00 00               js 0x1408d163d
008D147D  4C 8B 75 78                     mov r14, qword ptr [rbp + 0x78]
008D1481  48 C7 C0 00 F0 FF FF            mov rax, 0xfffffffffffff000
008D1488  4C 23 F0                        and r14, rax
008D148B  48 8B 9D 80 00 00 00            mov rbx, qword ptr [rbp + 0x80]
008D1492  48 23 D8                        and rbx, rax
008D1495  4C 23 E0                        and r12, rax
008D1498  49 03 DC                        add rbx, r12
008D149B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008D14A4  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
008D14AB  48 81 C1 00 04 00 00            add rcx, 0x400
008D14B2  4C 8B C3                        mov r8, rbx
008D14B5  49 8B D6                        mov rdx, r14
008D14B8  E8 E3 DC FF FF                  call 0x1408cf1a0
008D14BD  E9 3B FE FF FF                  jmp 0x1408d12fd
008D14C2  85 C0                           test eax, eax
008D14C4  0F 85 E6 FC FF FF               jne 0x1408d11b0
008D14CA  48 8B 85 E8 00 00 00            mov rax, qword ptr [rbp + 0xe8]
008D14D1  83 38 FF                        cmp dword ptr [rax], -1
008D14D4  4C 0F 44 FB                     cmove r15, rbx
008D14D8  4C 89 7D 38                     mov qword ptr [rbp + 0x38], r15
008D14DC  E9 CF FC FF FF                  jmp 0x1408d11b0
008D14E1  83 7D 1C 00                     cmp dword ptr [rbp + 0x1c], 0
008D14E5  0F 85 F0 01 00 00               jne 0x1408d16db
008D14EB  48 8B 85 E8 00 00 00            mov rax, qword ptr [rbp + 0xe8]
008D14F2  83 38 FF                        cmp dword ptr [rax], -1
008D14F5  0F 85 BE FD FF FF               jne 0x1408d12b9
008D14FB  83 7D 04 00                     cmp dword ptr [rbp + 4], 0
008D14FF  74 11                           je 0x1408d1512
008D1501  33 D2                           xor edx, edx
008D1503  48 8B CF                        mov rcx, rdi
008D1506  E8 65 13 2B 00                  call 0x140b82870
008D150B  83 65 04 00                     and dword ptr [rbp + 4], 0
008D150F  8B 55 00                        mov edx, dword ptr [rbp]
008D1512  41 BF 01 00 00 00               mov r15d, 1
008D1518  4C 89 7D 38                     mov qword ptr [rbp + 0x38], r15
008D151C  41 BA 00 10 00 00               mov r10d, 0x1000
008D1522  4C 89 55 10                     mov qword ptr [rbp + 0x10], r10
008D1526  48 8B 3D 33 5F 56 00            mov rdi, qword ptr [rip + 0x565f33]
008D152D  48 89 7D 28                     mov qword ptr [rbp + 0x28], rdi
008D1531  4C 8B 5D 08                     mov r11, qword ptr [rbp + 8]
008D1535  E9 87 FD FF FF                  jmp 0x1408d12c1
008D153A  4C 8B 5D 08                     mov r11, qword ptr [rbp + 8]
008D153E  49 8B 43 10                     mov rax, qword ptr [r11 + 0x10]
008D1542  89 10                           mov dword ptr [rax], edx
008D1544  E9 74 FD FF FF                  jmp 0x1408d12bd
008D1549  41 3B 13                        cmp edx, dword ptr [r11]
008D154C  73 35                           jae 0x1408d1583
008D154E  8B CA                           mov ecx, edx
008D1550  48 03 C9                        add rcx, rcx
008D1553  49 8B 43 08                     mov rax, qword ptr [r11 + 8]
008D1557  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
008D155B  4C 8B 5D 20                     mov r11, qword ptr [rbp + 0x20]
008D155F  49 2B D3                        sub rdx, r11
008D1562  49 8D 4A FF                     lea rcx, [r10 - 1]
008D1566  48 F7 D1                        not rcx
008D1569  48 23 CA                        and rcx, rdx
008D156C  48 8B C1                        mov rax, rcx
008D156F  48 C1 E8 04                     shr rax, 4
008D1573  48 03 C0                        add rax, rax
008D1576  48 C1 E8 03                     shr rax, 3
008D157A  49 3B C2                        cmp rax, r10
008D157D  0F 83 3B 01 00 00               jae 0x1408d16be
008D1583  8B CB                           mov ecx, ebx
008D1585  41 23 C8                        and ecx, r8d
008D1588  49 8B C2                        mov rax, r10
008D158B  48 2B C1                        sub rax, rcx
008D158E  45 8B E2                        mov r12d, r10d
008D1591  44 2B E1                        sub r12d, ecx
008D1594  49 3B C1                        cmp rax, r9
008D1597  45 0F 43 E1                     cmovae r12d, r9d
008D159B  45 8B C4                        mov r8d, r12d
008D159E  48 8B D3                        mov rdx, rbx
008D15A1  48 8B CF                        mov rcx, rdi
008D15A4  E8 97 52 DF FF                  call 0x1406c6840
008D15A9  EB 1A                           jmp 0x1408d15c5
008D15AB  8B F0                           mov esi, eax
008D15AD  4C 8B B5 D0 00 00 00            mov r14, qword ptr [rbp + 0xd0]
008D15B4  48 8B 7D 28                     mov rdi, qword ptr [rbp + 0x28]
008D15B8  48 8B 5D 40                     mov rbx, qword ptr [rbp + 0x40]
008D15BC  4C 8B 65 68                     mov r12, qword ptr [rbp + 0x68]
008D15C0  E9 1D FD FF FF                  jmp 0x1408d12e2
008D15C5  48 89 7D 60                     mov qword ptr [rbp + 0x60], rdi
008D15C9  42 8D 0C E5 00 00 00 00         lea ecx, [r12*8]
008D15D1  48 89 4D 58                     mov qword ptr [rbp + 0x58], rcx
008D15D5  8B 45 00                        mov eax, dword ptr [rbp]
008D15D8  48 8B 55 08                     mov rdx, qword ptr [rbp + 8]
008D15DC  3B 02                           cmp eax, dword ptr [rdx]
008D15DE  73 4C                           jae 0x1408d162c
008D15E0  41 8B F4                        mov esi, r12d
008D15E3  D1 EE                           shr esi, 1
008D15E5  C1 E6 07                        shl esi, 7
008D15E8  8B C8                           mov ecx, eax
008D15EA  48 03 C9                        add rcx, rcx
008D15ED  4C 8B 42 08                     mov r8, qword ptr [rdx + 8]
008D15F1  41 8B 04 C8                     mov eax, dword ptr [r8 + rcx*8]
008D15F5  2B 45 20                        sub eax, dword ptr [rbp + 0x20]
008D15F8  3B C6                           cmp eax, esi
008D15FA  73 30                           jae 0x1408d162c
008D15FC  48 C1 E8 04                     shr rax, 4
008D1600  48 8D 14 00                     lea rdx, [rax + rax]
008D1604  41 F6 44 C8 08 05               test byte ptr [r8 + rcx*8 + 8], 5
008D160A  0F 84 9A 00 00 00               je 0x1408d16aa
008D1610  48 8D 42 01                     lea rax, [rdx + 1]
008D1614  48 0F B3 07                     btr qword ptr [rdi], rax
008D1618  48 0F AB 17                     bts qword ptr [rdi], rdx
008D161C  8B 45 00                        mov eax, dword ptr [rbp]
008D161F  FF C0                           inc eax
008D1621  89 45 00                        mov dword ptr [rbp], eax
008D1624  48 8B 55 08                     mov rdx, qword ptr [rbp + 8]
008D1628  3B 02                           cmp eax, dword ptr [rdx]
008D162A  72 BC                           jb 0x1408d15e8
008D162C  41 8B C4                        mov eax, r12d
008D162F  D1 E8                           shr eax, 1
008D1631  C1 E0 07                        shl eax, 7
008D1634  48 01 45 20                     add qword ptr [rbp + 0x20], rax
008D1638  E9 37 FC FF FF                  jmp 0x1408d1274
008D163D  49 3B DE                        cmp rbx, r14
008D1640  0F 84 B7 FC FF FF               je 0x1408d12fd
008D1646  81 FE 06 00 00 C0               cmp esi, 0xc0000006
008D164C  0F 84 AB FC FF FF               je 0x1408d12fd
008D1652  48 C7 C0 00 F0 FF FF            mov rax, 0xfffffffffffff000
008D1659  4C 23 F0                        and r14, rax
008D165C  49 2B DE                        sub rbx, r14
008D165F  48 23 D8                        and rbx, rax
008D1662  E9 34 FE FF FF                  jmp 0x1408d149b
008D1667  E8 B0 15 B8 FF                  call 0x140452c1c
008D166C  A8 20                           test al, 0x20
008D166E  0F 84 76 FB FF FF               je 0x1408d11ea
008D1674  48 8B 41 48                     mov rax, qword ptr [rcx + 0x48]
008D1678  48 8B 08                        mov rcx, qword ptr [rax]
008D167B  48 8B 01                        mov rax, qword ptr [rcx]
008D167E  8B 40 08                        mov eax, dword ptr [rax + 8]
008D1681  C1 E0 0C                        shl eax, 0xc
008D1684  89 45 18                        mov dword ptr [rbp + 0x18], eax
008D1687  E9 5E FB FF FF                  jmp 0x1408d11ea
008D168C  41 BA 00 01 00 00               mov r10d, 0x100
008D1692  4C 89 55 10                     mov qword ptr [rbp + 0x10], r10
008D1696  8B 04 24                        mov eax, dword ptr [rsp]
008D1699  49 2B E2                        sub rsp, r10
008D169C  48 8D 7C 24 20                  lea rdi, [rsp + 0x20]
008D16A1  8B 07                           mov eax, dword ptr [rdi]
008D16A3  33 D2                           xor edx, edx
008D16A5  E9 5B FB FF FF                  jmp 0x1408d1205
008D16AA  41 B8 02 00 00 00               mov r8d, 2
008D16B0  48 8D 4D 58                     lea rcx, [rbp + 0x58]
008D16B4  E8 87 60 9C FF                  call 0x140297740
008D16B9  E9 5E FF FF FF                  jmp 0x1408d161c
008D16BE  4C 03 D9                        add r11, rcx
008D16C1  4C 89 5D 20                     mov qword ptr [rbp + 0x20], r11
008D16C5  48 03 D8                        add rbx, rax
008D16C8  48 89 5D 40                     mov qword ptr [rbp + 0x40], rbx
008D16CC  4C 2B C8                        sub r9, rax
008D16CF  4C 89 8D F0 00 00 00            mov qword ptr [rbp + 0xf0], r9
008D16D6  E9 A8 FE FF FF                  jmp 0x1408d1583
008D16DB  4C 8B 55 10                     mov r10, qword ptr [rbp + 0x10]
008D16DF  E9 4D FE FF FF                  jmp 0x1408d1531
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCopyToCfgBitMap(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (176);
    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_stack_p20 = v_r12;
    result = (*(unsigned __int64 *)(v_rip + 5477835)) ^ (v_stack_mA8);
    v_stack_m20 = result;
    v_stack_m8C = (unsigned int)((unsigned int)(a4));
    v_stack_m70 = a2;
    v_stack_m38 = a1;
    v_stack_m30 = a5;
    v_stack_m50 = v_xmm0;
    if (a2 > 1) goto loc_008D14C2;
loc_008D11B0:
    v_stack_m58 = a2;
    v_stack_mA0 = a2;
    a2 = 0;
    v_stack_mA8 = 0;
    v_stack_m88 = (unsigned int)(a7);
    v_stack_m98 = (unsigned int)(0x1000ULL);
    if (a10 != 0) goto loc_008D1667;
loc_008D11EA:
    if (0 > 1) goto loc_008D1441;
    v_rdi = *(unsigned __int64 *)(v_rip + 5661286);
    if (0 == 0) { v_rdi = *(unsigned __int64 *)(v_rip + 5661331); }
loc_008D1205:
    v_stack_m80 = v_rdi;
loc_008D1209:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a5))) & ((unsigned int)((unsigned int)(0xFFFULL))));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(a9))) & ((unsigned int)((unsigned int)(0xFFFULL))));
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)((unsigned int)(0xFFFULL))));
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)(a1)));
    v_stack_m60 = v_r12;
    v_stack_m40 = v_r12;
    v_stack_m28 = a9;
    v_rsi = 0;
loc_008D123C:
    v_stack_m68 = a5;
    if (a9 == 0) goto loc_008D12E2;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a5))) & ((unsigned int)((unsigned int)(0x1000ULL) - 1)));
    result = ((unsigned int)(0x1000ULL)) - (a1);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x1000ULL)))) - ((unsigned int)(a1)));
    if (result >= a9) { v_rsi = (unsigned int)(a9); }
    v_stack_m78 = (unsigned int)(v_rsi);
    if (0 > 1) goto loc_008D1338;
loc_008D1274:
    result = MiSplitPrivatePage(a5, a6, (unsigned int)(0x1000ULL) - 1, a9);
    if (sign_flag) goto loc_008D12DE;
    result = MiCopyToUserVa(a5, a6, v_rdi, (unsigned int)((unsigned int)(v_rsi)));
    if (sign_flag) goto loc_008D12DE;
    if ((unsigned int)((unsigned int)(v_stack_mA8)) != 0) goto loc_008D153A;
    if (0 > 1) goto loc_008D14E1;
loc_008D12B9:
loc_008D12BD:
loc_008D12C1:
    v_rbx = (a5) + ((unsigned int)((unsigned int)(v_rsi)));
    a4 = (a9) - ((unsigned int)((unsigned int)(v_rsi)));
    v_stack_p48 = a4;
    goto loc_008D123C;
loc_008D12DE:
loc_008D12E2:
    if (v_stack_mA4 != 0) {
        a2 = 0;
        a1 = v_rdi;
        result = ExFreePoolWithTag(a1, a2, v_rdi, a4);
    }
    if (v_stack_m58 != 0) goto loc_008D1475;
loc_008D12FD:
    a1 = (v_stack_m20) ^ (v_stack_mA8);
    result = _security_check_cookie(a1, a2, v_rdi, a4);
    return result;
loc_008D1338:
    if (((unsigned int)((unsigned int)(v_stack_m8C))) == 1) goto loc_008D1549;
    if ((unsigned int)((unsigned int)(v_stack_m8C)) != 0) goto loc_008D1274;
    v_stack_m48 = v_stack_p18;
    v_stack_m50 = v_stack_p10 * 8;
    result = RtlClearAllBitsEx(v_stack_m50, a2, v_rdi, a4);
    v_rsi = (unsigned int)((v_stack_p10) >> (1));
    v_rsi = (unsigned int)((v_rsi) << (7));
    v_rsi = (unsigned int)((v_rsi) + (a7));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a8))) != 0) goto loc_008D1398;
    result = MiImageCfgEnumRvaListFirst(v_stack_m58, a8, (unsigned int)(v_stack_m90), a4);
    if ((unsigned int)(result) == 0) goto loc_008D140A;
loc_008D1398:
loc_008D13A3:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) < ((unsigned int)((unsigned int)(a7)))) goto loc_008D13E4;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) >= ((unsigned int)(v_rsi))) goto loc_008D13FA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 4)))) & (1)) == 0) goto loc_008D13E4;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) - ((unsigned int)((unsigned int)(a7))));
    a1 = (a1) >> (4);
    a1 = (a1) + (a1);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (15));
    if (((unsigned int)(a3)) != (*(unsigned int *)(v_stack_m38 + 24))) goto loc_008D1423;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 4)))) & (4)) != 0) goto loc_008D1437;
loc_008D13E4:
    result = MiImageCfgEnumRvaListNext(v_stack_m58, a8, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_008D13A3;
loc_008D13FA:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) {
        result = a8;
    }
    v_stack_p38 = (unsigned int)(v_rsi);
    goto loc_008D1274;
loc_008D1423:
    result = RtlSetBitsEx(v_stack_m50, v_stack_m58, 2, a4);
    goto loc_008D13E4;
loc_008D1437:
    goto loc_008D13E4;
loc_008D1441:
    result = MiAllocatePool(64, v_stack_m98, (unsigned int)(0x6554694DULL), a4);
    v_stack_m80 = result;
    if (result == 0) goto loc_008D168C;
    v_stack_mA4 = (unsigned int)(v_stack_p8);
    a2 = 0;
    goto loc_008D1209;
loc_008D1475:
    if (sign_flag) goto loc_008D163D;
    v_r14 = (v_stack_m30) & (0xFFFFFFFFFFFFF000ULL);
    v_rbx = (v_stack_m28) & (0xFFFFFFFFFFFFF000ULL);
    v_r12 = ((unsigned int)(v_stack_m78)) & (0xFFFFFFFFFFFFF000ULL);
    v_rbx = (v_rbx) + (v_r12);
loc_008D149B:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    result = MiEliminateZeroPages(a1, v_r14, v_rbx, a4);
    goto loc_008D12FD;
loc_008D14C2:
    if ((unsigned int)(result) != 0) goto loc_008D11B0;
    v_r15 = v_stack_m70;
    if ((*(unsigned int *)(a8)) == -1) { v_r15 = v_rbx; }
    v_stack_m70 = v_r15;
    goto loc_008D11B0;
loc_008D14E1:
    if (v_stack_m8C != 0) goto loc_008D16DB;
    if ((*(unsigned int *)(a8)) != -1) goto loc_008D12B9;
    result = a8;
    if (v_stack_mA4 != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_rbx, a4);
        a2 = v_stack_mA8;
    }
    v_stack_m70 = 1;
    v_stack_m98 = (unsigned int)(0x1000ULL);
    v_stack_m80 = *(unsigned __int64 *)(v_rip + 5660467);
loc_008D1531:
    goto loc_008D12C1;
loc_008D153A:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 16)) = (unsigned int)(a2);
    goto loc_008D12BD;
loc_008D1549:
    if (((unsigned int)(a2)) >= (*(unsigned int *)(v_stack_mA0))) goto loc_008D1583;
    a1 = ((unsigned int)((unsigned int)(a2))) + ((unsigned int)((unsigned int)(a2)));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 8) + a1 * 8)) - (v_stack_m88);
    a1 = ~((unsigned int)(0x1000ULL) - 1);
    a1 = (a1) & (a2);
    result = (a1) >> (4);
    result = (result) + (result);
    result = (result) >> (3);
    if (result >= ((unsigned int)(0x1000ULL))) goto loc_008D16BE;
loc_008D1583:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & ((unsigned int)(v_rbx)));
    result = ((unsigned int)(0x1000ULL)) - (a1);
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x1000ULL)))) - ((unsigned int)(a1)));
    if (result >= a4) { v_r12 = a4; }
    result = memcpy(*(unsigned __int64 *)(v_rip + 5660467), v_rbx, (unsigned int)((unsigned int)(v_r12)), a4);
    goto loc_008D15C5;
loc_008D15C5:
    v_stack_m48 = *(unsigned __int64 *)(v_rip + 5660467);
    v_stack_m50 = v_r12 * 8;
    if (((unsigned int)((unsigned int)(v_stack_mA8))) >= (*(unsigned int *)(v_stack_mA0))) goto loc_008D162C;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) >> (1));
    v_rsi = (unsigned int)((v_rsi) << (7));
loc_008D15E8:
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_mA8)))) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_mA8))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 8) + a1 * 8))) - (v_stack_m88));
    if (((unsigned int)(result)) >= ((unsigned int)(v_rsi))) goto loc_008D162C;
    result = (result) >> (4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_mA0 + 8) + a1 * 8 + 8)) & (5)) == 0) goto loc_008D16AA;
loc_008D161C:
    result = (unsigned int)(((unsigned int)(v_stack_mA8)) + 1);
    v_stack_mA8 = (unsigned int)(result);
    if (((unsigned int)(result)) < (*(unsigned int *)(v_stack_mA0))) goto loc_008D15E8;
loc_008D162C:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) >> (1));
    result = (unsigned int)((result) << (7));
    goto loc_008D1274;
loc_008D163D:
    if (v_rbx == v_r14) goto loc_008D12FD;
    if (((unsigned int)(v_rsi)) == 0xC0000006ULL) goto loc_008D12FD;
    v_r14 = (v_r14) & (0xFFFFFFFFFFFFF000ULL);
    v_rbx = (v_rbx) - (v_r14);
    v_rbx = (v_rbx) & (0xFFFFFFFFFFFFF000ULL);
    goto loc_008D149B;
loc_008D1667:
    result = MiReadVadFlags2(a1, v_stack_mA0, *(unsigned __int64 *)(v_stack_mA0 + 8), a4);
    if ((((unsigned __int8)(result)) & (32)) == 0) goto loc_008D11EA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72))) + 8))) << (12));
    v_stack_m90 = (unsigned int)(result);
    goto loc_008D11EA;
loc_008D168C:
    v_stack_m98 = 256;
    v_rsp = (v_stack_m18) - (256);
    a2 = 0;
    goto loc_008D1205;
loc_008D16AA:
    result = RtlClearBitsEx(v_stack_m50, a2, 2, a4);
    goto loc_008D161C;
loc_008D16BE:
    v_r11 = (v_stack_m88) + (v_stack_m50);
    v_stack_m88 = v_r11;
    v_rbx = (v_rbx) + (result);
    v_stack_m68 = v_rbx;
    a4 = (a4) - (result);
    v_stack_p48 = a4;
    goto loc_008D1583;
loc_008D16DB:
    goto loc_008D1531;
}
```

## 5. (Beta) C Style

```c
int64_t MiCopyToCfgBitMap(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, uint32_t Arg7, void *Arg8, int64_t Arg9, int64_t Arg10)
{
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint64_t v_stack_mA8;
    uint32_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p38;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (176);
    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    v_stack_p20 = local_r12;
    result = (*(uint64_t *)(v_rip + 0x5395CB)) ^ (v_stack_mA8);
    v_stack_m20 = result;
    v_stack_m8C = (uint32_t)((uint32_t)(Arg4));
    v_stack_m70 = Arg2;
    v_stack_m38 = Arg1;
    v_stack_m30 = Arg5;
    v_stack_m50 = v_xmm0;
    if (Arg2 > 1) goto loc_008D14C2;
loc_008D11B0:
    v_stack_m58 = Arg2;
    v_stack_mA0 = Arg2;
    Arg2 = 0;
    v_stack_mA8 = 0;
    v_stack_m88 = (uint32_t)(Arg7);
    v_stack_m98 = (uint32_t)(0x1000ULL);
    if (Arg10 != 0) goto loc_008D1667;
loc_008D11EA:
    if (0 > 1) goto loc_008D1441;
    local_rdi = *(uint64_t *)(v_rip + 0x566266);
    if (0 == 0) { local_rdi = *(uint64_t *)(v_rip + 0x566293); }
loc_008D1205:
    v_stack_m80 = local_rdi;
loc_008D1209:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg5))) & ((uint32_t)((uint32_t)(0xFFFULL))));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(Arg9))) & ((uint32_t)((uint32_t)(0xFFFULL))));
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)((uint32_t)(0xFFFULL))));
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)(Arg1)));
    v_stack_m60 = local_r12;
    v_stack_m40 = local_r12;
    v_stack_m28 = Arg9;
    local_rsi = 0;
loc_008D123C:
    v_stack_m68 = Arg5;
    if (Arg9 == 0) goto loc_008D12E2;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg5))) & ((uint32_t)((uint32_t)(0x1000ULL) - 1)));
    result = ((uint32_t)(0x1000ULL)) - (Arg1);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x1000ULL)))) - ((uint32_t)(Arg1)));
    if (result >= Arg9) { local_rsi = (uint32_t)(Arg9); }
    v_stack_m78 = (uint32_t)(local_rsi);
    if (0 > 1) goto loc_008D1338;
loc_008D1274:
    result = MiSplitPrivatePage(Arg5, Arg6, (uint32_t)(0x1000ULL) - 1, Arg9);
    if (sign_flag) goto loc_008D12DE;
    result = MiCopyToUserVa(Arg5, Arg6, local_rdi, (uint32_t)((uint32_t)(local_rsi)));
    if (sign_flag) goto loc_008D12DE;
    if ((uint32_t)((uint32_t)(v_stack_mA8)) != 0) goto loc_008D153A;
    if (0 > 1) goto loc_008D14E1;
loc_008D12B9:
loc_008D12BD:
loc_008D12C1:
    local_rbx = (Arg5) + ((uint32_t)((uint32_t)(local_rsi)));
    Arg4 = (Arg9) - ((uint32_t)((uint32_t)(local_rsi)));
    v_stack_p48 = Arg4;
    goto loc_008D123C;
loc_008D12DE:
loc_008D12E2:
    if (v_stack_mA4 != 0) {
        Arg2 = 0;
        Arg1 = local_rdi;
        result = ExFreePoolWithTag(Arg1, Arg2, local_rdi, Arg4);
    }
    if (v_stack_m58 != 0) goto loc_008D1475;
loc_008D12FD:
    Arg1 = (v_stack_m20) ^ (v_stack_mA8);
    result = _security_check_cookie(Arg1, Arg2, local_rdi, Arg4);
    return result;
loc_008D1338:
    if (((uint32_t)((uint32_t)(v_stack_m8C))) == 1) goto loc_008D1549;
    if ((uint32_t)((uint32_t)(v_stack_m8C)) != 0) goto loc_008D1274;
    v_stack_m48 = v_stack_p18;
    v_stack_m50 = v_stack_p10 * 8;
    result = RtlClearAllBitsEx(v_stack_m50, Arg2, local_rdi, Arg4);
    local_rsi = (uint32_t)((v_stack_p10) >> (1));
    local_rsi = (uint32_t)((local_rsi) << (7));
    local_rsi = (uint32_t)((local_rsi) + (Arg7));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg8))) != 0) goto loc_008D1398;
    result = MiImageCfgEnumRvaListFirst(v_stack_m58, Arg8, (uint32_t)(v_stack_m90), Arg4);
    if ((uint32_t)(result) == 0) goto loc_008D140A;
loc_008D1398:
loc_008D13A3:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) < ((uint32_t)((uint32_t)(Arg7)))) goto loc_008D13E4;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) >= ((uint32_t)(local_rsi))) goto loc_008D13FA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg8 + 0x4)))) & (1)) == 0) goto loc_008D13E4;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) - ((uint32_t)((uint32_t)(Arg7))));
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) + (Arg1);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (15));
    if (((uint32_t)(Arg3)) != (*(uint32_t *)(v_stack_m38 + 0x18))) goto loc_008D1423;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg8 + 0x4)))) & (4)) != 0) goto loc_008D1437;
loc_008D13E4:
    result = MiImageCfgEnumRvaListNext(v_stack_m58, Arg8, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_008D13A3;
loc_008D13FA:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) {
        result = Arg8;
    }
    v_stack_p38 = (uint32_t)(local_rsi);
    goto loc_008D1274;
loc_008D1423:
    result = RtlSetBitsEx(v_stack_m50, v_stack_m58, 2, Arg4);
    goto loc_008D13E4;
loc_008D1437:
    goto loc_008D13E4;
loc_008D1441:
    result = MiAllocatePool(64, v_stack_m98, (uint32_t)(0x6554694DULL), Arg4);
    v_stack_m80 = result;
    if (result == 0) goto loc_008D168C;
    v_stack_mA4 = (uint32_t)(v_stack_p8);
    Arg2 = 0;
    goto loc_008D1209;
loc_008D1475:
    if (sign_flag) goto loc_008D163D;
    local_r14 = (v_stack_m30) & (0xFFFFFFFFFFFFF000ULL);
    local_rbx = (v_stack_m28) & (0xFFFFFFFFFFFFF000ULL);
    local_r12 = ((uint32_t)(v_stack_m78)) & (0xFFFFFFFFFFFFF000ULL);
    local_rbx = (local_rbx) + (local_r12);
loc_008D149B:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    result = MiEliminateZeroPages(Arg1, local_r14, local_rbx, Arg4);
    goto loc_008D12FD;
loc_008D14C2:
    if ((uint32_t)(result) != 0) goto loc_008D11B0;
    local_r15 = v_stack_m70;
    if ((*(uint32_t *)(arg8)) == -1) { local_r15 = local_rbx; }
    v_stack_m70 = local_r15;
    goto loc_008D11B0;
loc_008D14E1:
    if (v_stack_m8C != 0) goto loc_008D16DB;
    if ((*(uint32_t *)(arg8)) != -1) goto loc_008D12B9;
    result = Arg8;
    if (v_stack_mA4 != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, local_rbx, Arg4);
        Arg2 = v_stack_mA8;
    }
    v_stack_m70 = 1;
    v_stack_m98 = (uint32_t)(0x1000ULL);
    v_stack_m80 = *(uint64_t *)(v_rip + 0x565F33);
loc_008D1531:
    goto loc_008D12C1;
loc_008D153A:
    *(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x10)) = (uint32_t)(Arg2);
    goto loc_008D12BD;
loc_008D1549:
    if (((uint32_t)(Arg2)) >= (*(uint32_t *)(v_stack_mA0))) goto loc_008D1583;
    Arg1 = ((uint32_t)((uint32_t)(Arg2))) + ((uint32_t)((uint32_t)(Arg2)));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x8) + Arg1 * 8)) - (v_stack_m88);
    Arg1 = ~((uint32_t)(0x1000ULL) - 1);
    Arg1 = (Arg1) & (Arg2);
    result = (Arg1) >> (4);
    result = (result) + (result);
    result = (result) >> (3);
    if (result >= ((uint32_t)(0x1000ULL))) goto loc_008D16BE;
loc_008D1583:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & ((uint32_t)(local_rbx)));
    result = ((uint32_t)(0x1000ULL)) - (Arg1);
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x1000ULL)))) - ((uint32_t)(Arg1)));
    if (result >= Arg4) { local_r12 = Arg4; }
    result = memcpy(*(uint64_t *)(v_rip + 0x565F33), local_rbx, (uint32_t)((uint32_t)(local_r12)), Arg4);
    goto loc_008D15C5;
loc_008D15C5:
    v_stack_m48 = *(uint64_t *)(v_rip + 0x565F33);
    v_stack_m50 = local_r12 * 8;
    if (((uint32_t)((uint32_t)(v_stack_mA8))) >= (*(uint32_t *)(v_stack_mA0))) goto loc_008D162C;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) >> (1));
    local_rsi = (uint32_t)((local_rsi) << (7));
loc_008D15E8:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_mA8)))) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_mA8))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x8) + Arg1 * 8))) - (v_stack_m88));
    if (((uint32_t)(result)) >= ((uint32_t)(local_rsi))) goto loc_008D162C;
    result = (result) >> (4);
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_mA0 + 0x8) + Arg1 * 8 + 0x8)) & (5)) == 0) goto loc_008D16AA;
loc_008D161C:
    result = (uint32_t)(((uint32_t)(v_stack_mA8)) + 1);
    v_stack_mA8 = (uint32_t)(result);
    if (((uint32_t)(result)) < (*(uint32_t *)(v_stack_mA0))) goto loc_008D15E8;
loc_008D162C:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) >> (1));
    result = (uint32_t)((result) << (7));
    goto loc_008D1274;
loc_008D163D:
    if (local_rbx == local_r14) goto loc_008D12FD;
    if (((uint32_t)(local_rsi)) == 0xC0000006ULL) goto loc_008D12FD;
    local_r14 = (local_r14) & (0xFFFFFFFFFFFFF000ULL);
    local_rbx = (local_rbx) - (local_r14);
    local_rbx = (local_rbx) & (0xFFFFFFFFFFFFF000ULL);
    goto loc_008D149B;
loc_008D1667:
    result = MiReadVadFlags2(Arg1, v_stack_mA0, *(uint64_t *)(v_stack_mA0 + 0x8), Arg4);
    if ((((uint8_t)(result)) & (32)) == 0) goto loc_008D11EA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x48))) + 0x8))) << (12));
    v_stack_m90 = (uint32_t)(result);
    goto loc_008D11EA;
loc_008D168C:
    v_stack_m98 = 256;
    local_rsp = (v_stack_m18) - (256);
    Arg2 = 0;
    goto loc_008D1205;
loc_008D16AA:
    result = RtlClearBitsEx(v_stack_m50, Arg2, 2, Arg4);
    goto loc_008D161C;
loc_008D16BE:
    local_r11 = (v_stack_m88) + (v_stack_m50);
    v_stack_m88 = local_r11;
    local_rbx = (local_rbx) + (result);
    v_stack_m68 = local_rbx;
    Arg4 = (Arg4) - (result);
    v_stack_p48 = Arg4;
    goto loc_008D1583;
loc_008D16DB:
    goto loc_008D1531;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg8` | `+ 0x0` | `32` | `R` |
| `Arg8` | `+ 0x0` | `32` | `R/W` |
| `Arg8` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008D1140&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
