# MmRegisterHotPatches

- RVA: `0x00C678DC`–`0x00C67CA2` (길이 `966` bytes)
- VA: `0x0000000140C678DC`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2468`
- 디코드: `269`개 명령, `966/966` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00C6790B` → [MiAcquireLoadLock](../../text/2A/MiAcquireLoadLock_function_002A3950.md) (function, `0x002A3950`)
- `0x00C67971` → [MiAllocateHotPatchRecord](../../page/80/MiAllocateHotPatchRecord_function_008017F0.md) (function, `0x008017F0`)
- `0x00C6798F` → [MiInsertHotPatchRecord](../../page/80/MiInsertHotPatchRecord_function_008041D4.md) (function, `0x008041D4`)
- `0x00C679A0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C679B9` → [MiLogHotPatchOperationStatus](../../page/80/MiLogHotPatchOperationStatus_function_00804E84.md) (function, `0x00804E84`)
- `0x00C679C8` → [MiAllocateSecureImageActivePatch](../../page/80/MiAllocateSecureImageActivePatch_function_00801890.md) (function, `0x00801890`)
- `0x00C679F3` → [MiInsertSecureImageActivePatch](../../page/80/MiInsertSecureImageActivePatch_function_0080448C.md) (function, `0x0080448C`)
- `0x00C67A16` → [MiLogHotPatchOperationStatus](../../page/80/MiLogHotPatchOperationStatus_function_00804E84.md) (function, `0x00804E84`)
- `0x00C67A3D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C67A51` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C67A96` → [MiCompareHotPatchNodes](../../page/80/MiCompareHotPatchNodes_function_00803114.md) (function, `0x00803114`)
- `0x00C67ABD` → [VslDetermineHotPatchType](../../page/71/VslDetermineHotPatchType_function_0071899C.md) (function, `0x0071899C`)
- `0x00C67AE9` → [MiLoadHotPatch](../../page/AB/MiLoadHotPatch_function_00AB521C.md) (function, `0x00AB521C`)
- `0x00C67BB6` → [MiFindHotPatchRecord](../../page/A6/MiFindHotPatchRecord_function_00A6E618.md) (function, `0x00A6E618`)
- `0x00C67BE3` → [MiLoadHotPatch](../../page/AB/MiLoadHotPatch_function_00AB521C.md) (function, `0x00AB521C`)
- `0x00C67C19` → [MiLogHotPatchOperationStatus](../../page/80/MiLogHotPatchOperationStatus_function_00804E84.md) (function, `0x00804E84`)
- `0x00C67C4B` → [MiUnloadSystemImage](../../page/AA/MiUnloadSystemImage_function_00AA2FD4.md) (function, `0x00AA2FD4`)
- `0x00C67C6E` → [MiHandleDriverNonPagedSections](../../page/A4/MiHandleDriverNonPagedSections_function_00A4AEA8.md) (function, `0x00A4AEA8`)
- `0x00C67C7F` → [MmReleaseLoadLock](../../text/4D/MmReleaseLoadLock_function_004D36D0.md) (function, `0x004D36D0`)

### Direct callers
- [IoInitSystemPreDrivers](../C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2BBD9`

### Static image references
- `0x00C67985` → RVA `0x00E37578` (`.data`; read)
- `0x00C67A75` → RVA `0x00E37588` (`.data`; read)
- `0x00C67B52` → RVA `0x00E375B4` (`.data`; read)
- `0x00C67C28` → RVA `0x00EF54C0` (`.data`; read)
- `0x00C67C86` → RVA `0x00E375A8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x00C6790B` → [MiAcquireLoadLock](../../text/2A/MiAcquireLoadLock_function_002A3950.md) (`INIT` → `.text`)
  - `0x00C67971` → [MiAllocateHotPatchRecord](../../page/80/MiAllocateHotPatchRecord_function_008017F0.md) (`INIT` → `PAGE`)
  - `0x00C6798F` → [MiInsertHotPatchRecord](../../page/80/MiInsertHotPatchRecord_function_008041D4.md) (`INIT` → `PAGE`)
  - `0x00C679A0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C679B9` → [MiLogHotPatchOperationStatus](../../page/80/MiLogHotPatchOperationStatus_function_00804E84.md) (`INIT` → `PAGE`)
  - `0x00C679C8` → [MiAllocateSecureImageActivePatch](../../page/80/MiAllocateSecureImageActivePatch_function_00801890.md) (`INIT` → `PAGE`)
  - `0x00C679F3` → [MiInsertSecureImageActivePatch](../../page/80/MiInsertSecureImageActivePatch_function_0080448C.md) (`INIT` → `PAGE`)
  - `0x00C67A16` → [MiLogHotPatchOperationStatus](../../page/80/MiLogHotPatchOperationStatus_function_00804E84.md) (`INIT` → `PAGE`)
  - `0x00C67A3D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C67A51` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C67A96` → [MiCompareHotPatchNodes](../../page/80/MiCompareHotPatchNodes_function_00803114.md) (`INIT` → `PAGE`)
  - `0x00C67ABD` → [VslDetermineHotPatchType](../../page/71/VslDetermineHotPatchType_function_0071899C.md) (`INIT` → `PAGE`)
  - `0x00C67AE9` → [MiLoadHotPatch](../../page/AB/MiLoadHotPatch_function_00AB521C.md) (`INIT` → `PAGE`)
  - `0x00C67BB6` → [MiFindHotPatchRecord](../../page/A6/MiFindHotPatchRecord_function_00A6E618.md) (`INIT` → `PAGE`)
  - `0x00C67BE3` → [MiLoadHotPatch](../../page/AB/MiLoadHotPatch_function_00AB521C.md) (`INIT` → `PAGE`)
  - `0x00C67C19` → [MiLogHotPatchOperationStatus](../../page/80/MiLogHotPatchOperationStatus_function_00804E84.md) (`INIT` → `PAGE`)
  - `0x00C67C4B` → [MiUnloadSystemImage](../../page/AA/MiUnloadSystemImage_function_00AA2FD4.md) (`INIT` → `PAGE`)
  - `0x00C67C6E` → [MiHandleDriverNonPagedSections](../../page/A4/MiHandleDriverNonPagedSections_function_00A4AEA8.md) (`INIT` → `PAGE`)
  - `0x00C67C7F` → [MmReleaseLoadLock](../../text/4D/MmReleaseLoadLock_function_004D36D0.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C678DC  40 55                           push rbp
00C678DE  53                              push rbx
00C678DF  56                              push rsi
00C678E0  57                              push rdi
00C678E1  41 54                           push r12
00C678E3  41 55                           push r13
00C678E5  41 56                           push r14
00C678E7  41 57                           push r15
00C678E9  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00C678EE  48 81 EC 88 00 00 00            sub rsp, 0x88
00C678F5  33 F6                           xor esi, esi
00C678F7  4C 8B F9                        mov r15, rcx
00C678FA  89 75 6F                        mov dword ptr [rbp + 0x6f], esi
00C678FD  8B DE                           mov ebx, esi
00C678FF  89 75 67                        mov dword ptr [rbp + 0x67], esi
00C67902  44 8B EE                        mov r13d, esi
00C67905  89 75 77                        mov dword ptr [rbp + 0x77], esi
00C67908  8D 4E 01                        lea ecx, [rsi + 1]
00C6790B  E8 40 C0 63 FF                  call 0x1402a3950
00C67910  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
00C67914  44 8D 66 01                     lea r12d, [rsi + 1]
00C67918  49 8B 87 F0 00 00 00            mov rax, qword ptr [r15 + 0xf0]
00C6791F  48 8B B8 C8 0E 00 00            mov rdi, qword ptr [rax + 0xec8]
00C67926  49 8B 87 F0 00 00 00            mov rax, qword ptr [r15 + 0xf0]
00C6792D  48 05 C8 0E 00 00               add rax, 0xec8
00C67933  48 3B F8                        cmp rdi, rax
00C67936  0F 84 07 01 00 00               je 0x140c67a43
00C6793C  8B 57 28                        mov edx, dword ptr [rdi + 0x28]
00C6793F  41 8D 4D 01                     lea ecx, [r13 + 1]
00C67943  8B C2                           mov eax, edx
00C67945  24 06                           and al, 6
00C67947  3C 04                           cmp al, 4
00C67949  41 0F 45 CD                     cmovne ecx, r13d
00C6794D  44 8B E9                        mov r13d, ecx
00C67950  41 84 D4                        test r12b, dl
00C67953  0F 84 C2 00 00 00               je 0x140c67a1b
00C67959  8B 47 2C                        mov eax, dword ptr [rdi + 0x2c]
00C6795C  48 8D 77 10                     lea rsi, [rdi + 0x10]
00C67960  44 8B 47 44                     mov r8d, dword ptr [rdi + 0x44]
00C67964  4C 8B CE                        mov r9, rsi
00C67967  8B 57 24                        mov edx, dword ptr [rdi + 0x24]
00C6796A  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
00C6796D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00C67971  E8 7A 9E B9 FF                  call 0x1408017f0
00C67976  4C 8B F0                        mov r14, rax
00C67979  48 85 C0                        test rax, rax
00C6797C  0F 84 A1 00 00 00               je 0x140c67a23
00C67982  45 33 C0                        xor r8d, r8d
00C67985  48 8D 0D EC FB 1C 00            lea rcx, [rip + 0x1cfbec]
00C6798C  48 8B D0                        mov rdx, rax
00C6798F  E8 40 C8 B9 FF                  call 0x1408041d4
00C67994  3D FF 00 00 00                  cmp eax, 0xff
00C67999  75 0A                           jne 0x140c679a5
00C6799B  33 D2                           xor edx, edx
00C6799D  49 8B CE                        mov rcx, r14
00C679A0  E8 CB AE F1 FF                  call 0x140b82870
00C679A5  8B 57 24                        mov edx, dword ptr [rdi + 0x24]
00C679A8  45 33 C9                        xor r9d, r9d
00C679AB  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
00C679AE  4C 8B C6                        mov r8, rsi
00C679B1  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00C679B9  E8 C6 D4 B9 FF                  call 0x140804e84
00C679BE  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
00C679C1  A8 02                           test al, 2
00C679C3  74 3D                           je 0x140c67a02
00C679C5  48 8B CE                        mov rcx, rsi
00C679C8  E8 C3 9E B9 FF                  call 0x140801890
00C679CD  48 8B C8                        mov rcx, rax
00C679D0  48 85 C0                        test rax, rax
00C679D3  74 4E                           je 0x140c67a23
00C679D5  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00C679D8  89 41 18                        mov dword ptr [rcx + 0x18], eax
00C679DB  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00C679DE  89 41 1C                        mov dword ptr [rcx + 0x1c], eax
00C679E1  8B 47 48                        mov eax, dword ptr [rdi + 0x48]
00C679E4  89 41 20                        mov dword ptr [rcx + 0x20], eax
00C679E7  8B 47 4C                        mov eax, dword ptr [rdi + 0x4c]
00C679EA  89 41 24                        mov dword ptr [rcx + 0x24], eax
00C679ED  8B 47 44                        mov eax, dword ptr [rdi + 0x44]
00C679F0  89 41 28                        mov dword ptr [rcx + 0x28], eax
00C679F3  E8 94 CA B9 FF                  call 0x14080448c
00C679F8  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
00C67A00  EB 08                           jmp 0x140c67a0a
00C67A02  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
00C67A0A  8B 57 24                        mov edx, dword ptr [rdi + 0x24]
00C67A0D  45 33 C9                        xor r9d, r9d
00C67A10  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
00C67A13  4C 8B C6                        mov r8, rsi
00C67A16  E8 69 D4 B9 FF                  call 0x140804e84
00C67A1B  48 8B 3F                        mov rdi, qword ptr [rdi]
00C67A1E  E9 03 FF FF FF                  jmp 0x140c67926
00C67A23  B9 9A 00 00 C0                  mov ecx, 0xc000009a
00C67A28  4C 63 C1                        movsxd r8, ecx
00C67A2B  4D 8B CC                        mov r9, r12
00C67A2E  B9 1A 00 00 00                  mov ecx, 0x1a
00C67A33  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00C67A38  BA C5 15 05 00                  mov edx, 0x515c5
00C67A3D  E8 1E 5C 89 FF                  call 0x1404fd660
00C67A42  CC                              int3
00C67A43  33 D2                           xor edx, edx
00C67A45  48 8D 4D D7                     lea rcx, [rbp - 0x29]
00C67A49  44 8D 42 40                     lea r8d, [rdx + 0x40]
00C67A4D  44 8D 62 02                     lea r12d, [rdx + 2]
00C67A51  E8 EA F1 A5 FF                  call 0x1406c6c40
00C67A56  48 8B 05 1B FB 1C 00            mov rax, qword ptr [rip + 0x1cfb1b]
00C67A5D  33 F6                           xor esi, esi
00C67A5F  EB 06                           jmp 0x140c67a67
00C67A61  48 8B D8                        mov rbx, rax
00C67A64  48 8B 00                        mov rax, qword ptr [rax]
00C67A67  48 85 C0                        test rax, rax
00C67A6A  75 F5                           jne 0x140c67a61
00C67A6C  48 85 DB                        test rbx, rbx
00C67A6F  0F 84 D0 00 00 00               je 0x140c67b45
00C67A75  48 8B 3D 0C FB 1C 00            mov rdi, qword ptr [rip + 0x1cfb0c]
00C67A7C  8B 73 18                        mov esi, dword ptr [rbx + 0x18]
00C67A7F  44 8B 73 1C                     mov r14d, dword ptr [rbx + 0x1c]
00C67A83  89 75 EF                        mov dword ptr [rbp - 0x11], esi
00C67A86  44 89 75 F3                     mov dword ptr [rbp - 0xd], r14d
00C67A8A  48 85 FF                        test rdi, rdi
00C67A8D  74 25                           je 0x140c67ab4
00C67A8F  48 8B D7                        mov rdx, rdi
00C67A92  48 8D 4D D7                     lea rcx, [rbp - 0x29]
00C67A96  E8 79 B6 B9 FF                  call 0x140803114
00C67A9B  85 C0                           test eax, eax
00C67A9D  79 05                           jns 0x140c67aa4
00C67A9F  48 8B 3F                        mov rdi, qword ptr [rdi]
00C67AA2  EB 06                           jmp 0x140c67aaa
00C67AA4  7E 09                           jle 0x140c67aaf
00C67AA6  48 8B 7F 08                     mov rdi, qword ptr [rdi + 8]
00C67AAA  48 85 FF                        test rdi, rdi
00C67AAD  75 E0                           jne 0x140c67a8f
00C67AAF  48 85 FF                        test rdi, rdi
00C67AB2  75 46                           jne 0x140c67afa
00C67AB4  4C 8D 45 77                     lea r8, [rbp + 0x77]
00C67AB8  41 8B D6                        mov edx, r14d
00C67ABB  8B CE                           mov ecx, esi
00C67ABD  E8 DA 0E AB FF                  call 0x14071899c
00C67AC2  33 F6                           xor esi, esi
00C67AC4  8B C8                           mov ecx, eax
00C67AC6  85 C0                           test eax, eax
00C67AC8  0F 88 5A FF FF FF               js 0x140c67a28
00C67ACE  F6 45 77 03                     test byte ptr [rbp + 0x77], 3
00C67AD2  74 28                           je 0x140c67afc
00C67AD4  48 8D 4B 28                     lea rcx, [rbx + 0x28]
00C67AD8  89 75 6F                        mov dword ptr [rbp + 0x6f], esi
00C67ADB  4C 8D 4D 67                     lea r9, [rbp + 0x67]
00C67ADF  89 75 67                        mov dword ptr [rbp + 0x67], esi
00C67AE2  4C 8D 45 6F                     lea r8, [rbp + 0x6f]
00C67AE6  41 8B D4                        mov edx, r12d
00C67AE9  E8 2E D7 E4 FF                  call 0x140ab521c
00C67AEE  8B C8                           mov ecx, eax
00C67AF0  85 C0                           test eax, eax
00C67AF2  0F 88 30 FF FF FF               js 0x140c67a28
00C67AF8  EB 02                           jmp 0x140c67afc
00C67AFA  33 F6                           xor esi, esi
00C67AFC  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00C67B00  48 8B CB                        mov rcx, rbx
00C67B03  48 85 C0                        test rax, rax
00C67B06  74 2E                           je 0x140c67b36
00C67B08  48 8B 08                        mov rcx, qword ptr [rax]
00C67B0B  48 8B D8                        mov rbx, rax
00C67B0E  48 85 C9                        test rcx, rcx
00C67B11  0F 84 55 FF FF FF               je 0x140c67a6c
00C67B17  48 8B 01                        mov rax, qword ptr [rcx]
00C67B1A  48 8B D9                        mov rbx, rcx
00C67B1D  48 8B C8                        mov rcx, rax
00C67B20  48 85 C0                        test rax, rax
00C67B23  75 F2                           jne 0x140c67b17
00C67B25  E9 42 FF FF FF                  jmp 0x140c67a6c
00C67B2A  48 39 0B                        cmp qword ptr [rbx], rcx
00C67B2D  0F 84 39 FF FF FF               je 0x140c67a6c
00C67B33  48 8B CB                        mov rcx, rbx
00C67B36  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
00C67B3A  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
00C67B3E  75 EA                           jne 0x140c67b2a
00C67B40  E9 27 FF FF FF                  jmp 0x140c67a6c
00C67B45  49 8B 9F F0 00 00 00            mov rbx, qword ptr [r15 + 0xf0]
00C67B4C  41 BC 03 00 00 00               mov r12d, 3
00C67B52  8B 05 5C FA 1C 00               mov eax, dword ptr [rip + 0x1cfa5c]
00C67B58  48 81 C3 C8 0E 00 00            add rbx, 0xec8
00C67B5F  A8 01                           test al, 1
00C67B61  74 03                           je 0x140c67b66
00C67B63  48 8B 1B                        mov rbx, qword ptr [rbx]
00C67B66  41 BE 00 00 00 80               mov r14d, 0x80000000
00C67B6C  49 8B 87 F0 00 00 00            mov rax, qword ptr [r15 + 0xf0]
00C67B73  48 05 C8 0E 00 00               add rax, 0xec8
00C67B79  48 3B D8                        cmp rbx, rax
00C67B7C  0F 84 A6 00 00 00               je 0x140c67c28
00C67B82  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
00C67B85  41 84 C4                        test r12b, al
00C67B88  0F 85 92 00 00 00               jne 0x140c67c20
00C67B8E  44 8B 43 20                     mov r8d, dword ptr [rbx + 0x20]
00C67B92  48 8D 0D DF F9 1C 00            lea rcx, [rip + 0x1cf9df]
00C67B99  44 8B 4B 24                     mov r9d, dword ptr [rbx + 0x24]
00C67B9D  33 D2                           xor edx, edx
00C67B9F  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
00C67BA4  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00C67BA9  66 89 74 24 20                  mov word ptr [rsp + 0x20], si
00C67BAE  44 89 45 EF                     mov dword ptr [rbp - 0x11], r8d
00C67BB2  44 89 4D F3                     mov dword ptr [rbp - 0xd], r9d
00C67BB6  E8 5D 6A E0 FF                  call 0x140a6e618
00C67BBB  8B F8                           mov edi, eax
00C67BBD  4C 8D 4D 67                     lea r9, [rbp + 0x67]
00C67BC1  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00C67BC4  4C 8D 45 6F                     lea r8, [rbp + 0x6f]
00C67BC8  C1 FF 1F                        sar edi, 0x1f
00C67BCB  48 8D 4B 10                     lea rcx, [rbx + 0x10]
00C67BCF  83 E7 FD                        and edi, 0xfffffffd
00C67BD2  89 45 6F                        mov dword ptr [rbp + 0x6f], eax
00C67BD5  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
00C67BD8  83 C7 04                        add edi, 4
00C67BDB  83 CF 08                        or edi, 8
00C67BDE  89 45 67                        mov dword ptr [rbp + 0x67], eax
00C67BE1  8B D7                           mov edx, edi
00C67BE3  E8 34 D6 E4 FF                  call 0x140ab521c
00C67BE8  8B C8                           mov ecx, eax
00C67BEA  41 03 C6                        add eax, r14d
00C67BED  41 85 C6                        test r14d, eax
00C67BF0  75 0C                           jne 0x140c67bfe
00C67BF2  81 F9 34 04 00 C0               cmp ecx, 0xc0000434
00C67BF8  0F 85 2A FE FF FF               jne 0x140c67a28
00C67BFE  40 F6 C7 01                     test dil, 1
00C67C02  74 1A                           je 0x140c67c1e
00C67C04  8B 53 24                        mov edx, dword ptr [rbx + 0x24]
00C67C07  4C 8D 43 10                     lea r8, [rbx + 0x10]
00C67C0B  44 8B C9                        mov r9d, ecx
00C67C0E  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00C67C16  8B 4B 20                        mov ecx, dword ptr [rbx + 0x20]
00C67C19  E8 66 D2 B9 FF                  call 0x140804e84
00C67C1E  33 F6                           xor esi, esi
00C67C20  48 8B 1B                        mov rbx, qword ptr [rbx]
00C67C23  E9 44 FF FF FF                  jmp 0x140c67b6c
00C67C28  48 8D 3D 91 D8 28 00            lea rdi, [rip + 0x28d891]
00C67C2F  45 85 ED                        test r13d, r13d
00C67C32  74 21                           je 0x140c67c55
00C67C34  48 8B 1D 85 D8 28 00            mov rbx, qword ptr [rip + 0x28d885]
00C67C3B  EB 13                           jmp 0x140c67c50
00C67C3D  48 8B CB                        mov rcx, rbx
00C67C40  48 8B 1B                        mov rbx, qword ptr [rbx]
00C67C43  66 0F BA 61 6E 09               bt word ptr [rcx + 0x6e], 9
00C67C49  73 05                           jae 0x140c67c50
00C67C4B  E8 84 B3 E3 FF                  call 0x140aa2fd4
00C67C50  48 3B DF                        cmp rbx, rdi
00C67C53  75 E8                           jne 0x140c67c3d
00C67C55  48 8B 1D 64 D8 28 00            mov rbx, qword ptr [rip + 0x28d864]
00C67C5C  EB 18                           jmp 0x140c67c76
00C67C5E  66 0F BA 63 6E 09               bt word ptr [rbx + 0x6e], 9
00C67C64  73 0D                           jae 0x140c67c73
00C67C66  BA 02 00 00 00                  mov edx, 2
00C67C6B  48 8B CB                        mov rcx, rbx
00C67C6E  E8 35 32 DE FF                  call 0x140a4aea8
00C67C73  48 8B 1B                        mov rbx, qword ptr [rbx]
00C67C76  48 3B DF                        cmp rbx, rdi
00C67C79  75 E3                           jne 0x140c67c5e
00C67C7B  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
00C67C7F  E8 4C BA 86 FF                  call 0x1404d36d0
00C67C84  8B C6                           mov eax, esi
00C67C86  C6 05 1B F9 1C 00 01            mov byte ptr [rip + 0x1cf91b], 1
00C67C8D  48 81 C4 88 00 00 00            add rsp, 0x88
00C67C94  41 5F                           pop r15
00C67C96  41 5E                           pop r14
00C67C98  41 5D                           pop r13
00C67C9A  41 5C                           pop r12
00C67C9C  5F                              pop rdi
00C67C9D  5E                              pop rsi
00C67C9E  5B                              pop rbx
00C67C9F  5D                              pop rbp
00C67CA0  C3                              ret
00C67CA1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmRegisterHotPatches(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (136);
    v_rsi = 0;
    v_stack_p10 = 0;
    v_stack_p8 = 0;
    v_stack_p18 = 0;
    result = MiAcquireLoadLock(v_rsi + 1, a2, a3, a4);
    v_stack_p20 = result;
loc_00C67926:
    result = (*(unsigned __int64 *)(a1 + 240)) + (0xEC8ULL);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784)) == result) goto loc_00C67A43;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 40))))) & (6));
    a1 = 0 + 1;
    if (((unsigned __int8)(result)) != 4) { a1 = 0; }
    if ((((unsigned __int8)(v_rsi + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 40))))) == 0) goto loc_00C67A1B;
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 44)));
    result = MiAllocateHotPatchRecord((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 32)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 36)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 68)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 16);
    if (result == 0) goto loc_00C67A23;
    a3 = 0;
    result = MiInsertHotPatchRecord(v_rip + 1899500, result, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 16);
    if (((unsigned int)(result)) == 255) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 16);
    }
    a4 = 0;
    v_stack_mA8 = 4;
    result = MiLogHotPatchOperationStatus((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 32)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 36)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 16, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 40)))) & (2)) == 0) goto loc_00C67A02;
    result = MiAllocateSecureImageActivePatch(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 16, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 36)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 16, a4);
    if (result == 0) goto loc_00C67A23;
    *(unsigned int *)(result + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 32)));
    *(unsigned int *)(result + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 36)));
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 72)));
    *(unsigned int *)(result + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 76)));
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 68)));
    result = MiInsertSecureImageActivePatch(result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 36)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 16, a4);
    v_stack_mA8 = 5;
    goto loc_00C67A0A;
loc_00C67A02:
    v_stack_mA8 = 6;
loc_00C67A0A:
    a4 = 0;
    result = MiLogHotPatchOperationStatus((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 32)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 36)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3784) + 16, a4);
loc_00C67A1B:
    goto loc_00C67926;
loc_00C67A23:
loc_00C67A28:
    v_stack_mA8 = 0;
    result = KeBugCheckEx(26, (unsigned int)(0x515C5ULL), (int)((unsigned int)((unsigned int)(0xC000009AULL))), v_rsi + 1);
loc_00C67A43:
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 64, v_rsi + 1);
    v_rsi = 0;
    goto loc_00C67A67;
loc_00C67A61:
loc_00C67A67:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 1899291)) != 0) goto loc_00C67A61;
loc_00C67A6C:
    if (*(unsigned __int64 *)(v_rip + 1899291) == 0) goto loc_00C67B45;
    v_stack_m70 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 1899291) + 24)));
    v_stack_m6C = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 1899291) + 28)));
    if (*(unsigned __int64 *)(v_rip + 1899276) == 0) goto loc_00C67AB4;
loc_00C67A8F:
    result = MiCompareHotPatchNodes(v_stack_m88, *(unsigned __int64 *)(v_rip + 1899276), a2 + 64, v_rsi + 1);
    if (!sign_flag) goto loc_00C67AA4;
    goto loc_00C67AAA;
loc_00C67AA4:
    if (condition_is_less_or_equal) goto loc_00C67AAF;
loc_00C67AAA:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 1899276)) + 8) != 0) goto loc_00C67A8F;
loc_00C67AAF:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 1899276)) + 8) != 0) goto loc_00C67AFA;
loc_00C67AB4:
    result = VslDetermineHotPatchType((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 1899291) + 24)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 1899291) + 28)))), v_stack_p18, v_rsi + 1);
    v_rsi = 0;
    if (sign_flag) goto loc_00C67A28;
    if (((v_stack_p18) & (3)) == 0) goto loc_00C67AFC;
    v_stack_p10 = 0;
    v_stack_p8 = 0;
    result = MiLoadHotPatch(*(unsigned __int64 *)(v_rip + 1899291) + 40, (unsigned int)((unsigned int)(a2 + 2)), v_stack_p10, v_stack_p8);
    if (sign_flag) goto loc_00C67A28;
    goto loc_00C67AFC;
loc_00C67AFA:
    v_rsi = 0;
loc_00C67AFC:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 1899291) + 8) == 0) goto loc_00C67B36;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 1899291) + 8)) == 0) goto loc_00C67A6C;
loc_00C67B17:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 1899291) + 8))) != 0) goto loc_00C67B17;
    goto loc_00C67A6C;
loc_00C67B2A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 1899291) + 8)))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 1899291) + 8))))) goto loc_00C67A6C;
loc_00C67B36:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 1899291) + 8)) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00C67B2A;
    goto loc_00C67A6C;
loc_00C67B45:
    v_rbx = (*(unsigned __int64 *)(a1 + 240)) + (0xEC8ULL);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 1899100)))) & (1)) != 0) {
        v_rbx = *(unsigned __int64 *)(v_rbx);
    }
loc_00C67B6C:
    result = (*(unsigned __int64 *)(a1 + 240)) + (0xEC8ULL);
    if (v_rbx == result) goto loc_00C67C28;
    if (((3) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 40))))) != 0) goto loc_00C67C20;
    a2 = 0;
    v_stack_m98 = 0;
    v_stack_mA0 = 0;
    v_stack_mA8 = 0;
    v_stack_m70 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
    v_stack_m6C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 36)));
    result = MiFindHotPatchRecord(v_rip + 1898975, a2, (unsigned int)(*(unsigned int *)(v_rbx + 32)), (unsigned int)(*(unsigned int *)(v_rbx + 36)));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (31));
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFDULL));
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
    v_rdi = (unsigned int)((v_rdi) + (4));
    v_rdi = (unsigned int)((v_rdi) | (8));
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 36)));
    result = MiLoadHotPatch(v_rbx + 16, (unsigned int)((unsigned int)(v_rdi)), v_stack_p10, v_stack_p8);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) != 0) goto loc_00C67BFE;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000434ULL) goto loc_00C67A28;
loc_00C67BFE:
    if ((((unsigned __int8)(v_rdi)) & (1)) != 0) {
        a2 = *(unsigned int *)(v_rbx + 36);
        a3 = v_rbx + 16;
        a4 = (unsigned int)((unsigned int)((unsigned int)(result)));
        v_stack_mA8 = 4;
        a1 = *(unsigned int *)(v_rbx + 32);
        result = MiLogHotPatchOperationStatus(a1, a2, a3, a4);
    }
    v_rsi = 0;
loc_00C67C20:
    goto loc_00C67B6C;
loc_00C67C28:
    if ((unsigned int)((unsigned int)((unsigned int)(a1))) == 0) goto loc_00C67C55;
    goto loc_00C67C50;
loc_00C67C3D:
    if (!(condition_is_above_or_equal)) {
        result = MiUnloadSystemImage(*(unsigned __int64 *)(v_rip + 2676869), a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2676869))) != (v_rip + 2676881)) goto loc_00C67C3D;
loc_00C67C55:
    goto loc_00C67C76;
loc_00C67C5E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2676869))) < (v_rip + 2676881)) {
        a2 = 2;
        a1 = *(unsigned __int64 *)(v_rip + 2676836);
        result = MiHandleDriverNonPagedSections(a1, a2, a3, a4);
    }
loc_00C67C76:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2676836))) != (v_rip + 2676881)) goto loc_00C67C5E;
    result = MmReleaseLoadLock(v_stack_p20, a2, a3, a4);
    *(unsigned __int8 *)(v_rip + 1898779) = 1;
    v_rsp = (v_rsp) + (136);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t MmRegisterHotPatches(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (136);
    local_rsi = 0;
    v_stack_p10 = 0;
    v_stack_p8 = 0;
    v_stack_p18 = 0;
    result = MiAcquireLoadLock(local_rsi + 1, a2, a3, a4);
    v_stack_p20 = result;
loc_00C67926:
    result = (*(uint64_t *)(arg1 + 0xF0)) + (0xEC8ULL);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8)) == result) goto loc_00C67A43;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x28))))) & (6));
    Arg1 = 0 + 1;
    if (((uint8_t)(result)) != 4) { Arg1 = 0; }
    if ((((uint8_t)(local_rsi + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x28))))) == 0) goto loc_00C67A1B;
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x2C)));
    result = MiAllocateHotPatchRecord((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x20)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x24)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x44)), *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 16);
    if (result == 0) goto loc_00C67A23;
    a3 = 0;
    result = MiInsertHotPatchRecord(v_rip + 1899500, result, a3, *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 16);
    if (((uint32_t)(result)) == 255) {
        a2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, a2, a3, *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 16);
    }
    a4 = 0;
    v_stack_mA8 = 4;
    result = MiLogHotPatchOperationStatus((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x20)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x24)), *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 16, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x28)))) & (2)) == 0) goto loc_00C67A02;
    result = MiAllocateSecureImageActivePatch(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 16, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x24)), *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 16, a4);
    if (result == 0) goto loc_00C67A23;
    *(uint32_t *)(result + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x20)));
    *(uint32_t *)(result + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x24)));
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x48)));
    *(uint32_t *)(result + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x4C)));
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x44)));
    result = MiInsertSecureImageActivePatch(result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x24)), *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 16, a4);
    v_stack_mA8 = 5;
    goto loc_00C67A0A;
loc_00C67A02:
    v_stack_mA8 = 6;
loc_00C67A0A:
    a4 = 0;
    result = MiLogHotPatchOperationStatus((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x20)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 0x24)), *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xEC8) + 16, a4);
loc_00C67A1B:
    goto loc_00C67926;
loc_00C67A23:
loc_00C67A28:
    v_stack_mA8 = 0;
    result = KeBugCheckEx(26, (uint32_t)(0x515C5ULL), (int32_t)((uint32_t)((uint32_t)(0xC000009AULL))), local_rsi + 1);
loc_00C67A43:
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 64, local_rsi + 1);
    local_rsi = 0;
    goto loc_00C67A67;
loc_00C67A61:
loc_00C67A67:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x1CFB1B)) != 0) goto loc_00C67A61;
loc_00C67A6C:
    if (*(uint64_t *)(v_rip + 0x1CFB1B) == 0) goto loc_00C67B45;
    v_stack_m70 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x1CFB1B) + 0x18)));
    v_stack_m6C = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x1CFB1B) + 0x1C)));
    if (*(uint64_t *)(v_rip + 0x1CFB0C) == 0) goto loc_00C67AB4;
loc_00C67A8F:
    result = MiCompareHotPatchNodes(v_stack_m88, *(uint64_t *)(v_rip + 0x1CFB0C), a2 + 64, local_rsi + 1);
    if (!sign_flag) goto loc_00C67AA4;
    goto loc_00C67AAA;
loc_00C67AA4:
    if (condition_is_less_or_equal) goto loc_00C67AAF;
loc_00C67AAA:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x1CFB0C)) + 0x8) != 0) goto loc_00C67A8F;
loc_00C67AAF:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x1CFB0C)) + 0x8) != 0) goto loc_00C67AFA;
loc_00C67AB4:
    result = VslDetermineHotPatchType((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x1CFB1B) + 0x18)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x1CFB1B) + 0x1C)))), v_stack_p18, local_rsi + 1);
    local_rsi = 0;
    if (sign_flag) goto loc_00C67A28;
    if (((v_stack_p18) & (3)) == 0) goto loc_00C67AFC;
    v_stack_p10 = 0;
    v_stack_p8 = 0;
    result = MiLoadHotPatch(*(uint64_t *)(v_rip + 0x1CFB1B) + 40, (uint32_t)((uint32_t)(a2 + 2)), v_stack_p10, v_stack_p8);
    if (sign_flag) goto loc_00C67A28;
    goto loc_00C67AFC;
loc_00C67AFA:
    local_rsi = 0;
loc_00C67AFC:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x1CFB1B) + 0x8) == 0) goto loc_00C67B36;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x1CFB1B) + 0x8)) == 0) goto loc_00C67A6C;
loc_00C67B17:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x1CFB1B) + 0x8))) != 0) goto loc_00C67B17;
    goto loc_00C67A6C;
loc_00C67B2A:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x1CFB1B) + 0x8)))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x1CFB1B) + 0x8))))) goto loc_00C67A6C;
loc_00C67B36:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x1CFB1B) + 0x8)) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00C67B2A;
    goto loc_00C67A6C;
loc_00C67B45:
    local_rbx = (*(uint64_t *)(arg1 + 0xF0)) + (0xEC8ULL);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1CFA5C)))) & (1)) != 0) {
        local_rbx = *(uint64_t *)(local_rbx);
    }
loc_00C67B6C:
    result = (*(uint64_t *)(arg1 + 0xF0)) + (0xEC8ULL);
    if (local_rbx == result) goto loc_00C67C28;
    if (((3) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x28))))) != 0) goto loc_00C67C20;
    a2 = 0;
    v_stack_m98 = 0;
    v_stack_mA0 = 0;
    v_stack_mA8 = 0;
    v_stack_m70 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
    v_stack_m6C = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x24)));
    result = MiFindHotPatchRecord(v_rip + 1898975, a2, (uint32_t)(*(uint32_t *)(local_rbx + 0x20)), (uint32_t)(*(uint32_t *)(local_rbx + 0x24)));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (31));
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFDULL));
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
    local_rdi = (uint32_t)((local_rdi) + (4));
    local_rdi = (uint32_t)((local_rdi) | (8));
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x24)));
    result = MiLoadHotPatch(local_rbx + 16, (uint32_t)((uint32_t)(local_rdi)), v_stack_p10, v_stack_p8);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) != 0) goto loc_00C67BFE;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000434ULL) goto loc_00C67A28;
loc_00C67BFE:
    if ((((uint8_t)(local_rdi)) & (1)) != 0) {
        a2 = *(uint32_t *)(local_rbx + 0x24);
        a3 = local_rbx + 16;
        a4 = (uint32_t)((uint32_t)((uint32_t)(result)));
        v_stack_mA8 = 4;
        Arg1 = *(uint32_t *)(local_rbx + 0x20);
        result = MiLogHotPatchOperationStatus(Arg1, a2, a3, a4);
    }
    local_rsi = 0;
loc_00C67C20:
    goto loc_00C67B6C;
loc_00C67C28:
    if ((uint32_t)((uint32_t)((uint32_t)(Arg1))) == 0) goto loc_00C67C55;
    goto loc_00C67C50;
loc_00C67C3D:
    if (!(condition_is_above_or_equal)) {
        result = MiUnloadSystemImage(*(uint64_t *)(v_rip + 0x28D885), a2, a3, a4);
    }
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x28D885))) != (v_rip + 2676881)) goto loc_00C67C3D;
loc_00C67C55:
    goto loc_00C67C76;
loc_00C67C5E:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x28D885))) < (v_rip + 2676881)) {
        a2 = 2;
        Arg1 = *(uint64_t *)(v_rip + 0x28D864);
        result = MiHandleDriverNonPagedSections(Arg1, a2, a3, a4);
    }
loc_00C67C76:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x28D864))) != (v_rip + 2676881)) goto loc_00C67C5E;
    result = MmReleaseLoadLock(v_stack_p20, a2, a3, a4);
    *(uint8_t *)(v_rip + 0x1CF91B) = 1;
    local_rsp = (local_rsp) + (136);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xF0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C678DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
