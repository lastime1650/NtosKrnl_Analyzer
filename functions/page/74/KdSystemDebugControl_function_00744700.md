# KdSystemDebugControl

- RVA: `0x00744700`–`0x00744ED5` (길이 `2,005` bytes)
- VA: `0x0000000140744700`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C9AE4`
- 디코드: `421`개 명령, `2,005/2,005` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x007447F2` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x00744820` → [KdpSysWriteControlSpace](../../pagekd/B8/KdpSysWriteControlSpace_function_00B89740.md) (function, `0x00B89740`)
- `0x00744888` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x007448B9` → [KdpSysReadControlSpace](../../pagekd/B8/KdpSysReadControlSpace_function_00B89658.md) (function, `0x00B89658`)
- `0x00744924` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x0074495C` → [KdpCopyMemoryChunks](../../pagekd/B8/KdpCopyMemoryChunks_function_00B8AACC.md) (function, `0x00B8AACC`)
- `0x007449CA` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x00744A5D` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x00744AF9` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x00744B3F` → [KdpSysGetVersion](../../pagekd/B8/KdpSysGetVersion_function_00B88514.md) (function, `0x00B88514`)
- `0x00744BAA` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x00744BF3` → [KdpSysReadIoSpace](../../text/5B/KdpSysReadIoSpace_function_005B11EC.md) (function, `0x005B11EC`)
- `0x00744C3B` → [KdpSysCheckLowMemory](../../pagekd/B8/KdpSysCheckLowMemory_function_00B884F0.md) (function, `0x00B884F0`)
- `0x00744CA1` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x00744CEA` → [KdpSysWriteBusData](../../pagekd/B8/KdpSysWriteBusData_function_00B885A8.md) (function, `0x00B885A8`)
- `0x00744D53` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x00744D9C` → [KdpSysReadBusData](../../pagekd/B8/KdpSysReadBusData_function_00B88540.md) (function, `0x00B88540`)
- `0x00744DBD` → [KdpSysWriteMsr](../../text/5B/KdpSysWriteMsr_function_005B13A4.md) (function, `0x005B13A4`)
- `0x00744DDE` → [KdpSysReadMsr](../../text/5B/KdpSysReadMsr_function_005B12B0.md) (function, `0x005B12B0`)
- `0x00744E44` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x00744E89` → [KdpSysWriteIoSpace](../../text/5B/KdpSysWriteIoSpace_function_005B12E4.md) (function, `0x005B12E4`)
- `0x00744EBC` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (function, `0x0029F258`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00744721` → RVA `0x00E0AA1D` (`.data`; read)
- `0x0074472A` → RVA `0x00E0AA1C` (`.data`; read)
- `0x00744733` → RVA `0x00F475F8` (`.data`; read)
- `0x0074473C` → RVA `0x00F55C80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00744820` → [KdpSysWriteControlSpace](../../pagekd/B8/KdpSysWriteControlSpace_function_00B89740.md) (`PAGE` → `PAGEKD`)
  - `0x007448B9` → [KdpSysReadControlSpace](../../pagekd/B8/KdpSysReadControlSpace_function_00B89658.md) (`PAGE` → `PAGEKD`)
  - `0x0074495C` → [KdpCopyMemoryChunks](../../pagekd/B8/KdpCopyMemoryChunks_function_00B8AACC.md) (`PAGE` → `PAGEKD`)
  - `0x00744B3F` → [KdpSysGetVersion](../../pagekd/B8/KdpSysGetVersion_function_00B88514.md) (`PAGE` → `PAGEKD`)
  - `0x00744BF3` → [KdpSysReadIoSpace](../../text/5B/KdpSysReadIoSpace_function_005B11EC.md) (`PAGE` → `.text`)
  - `0x00744C3B` → [KdpSysCheckLowMemory](../../pagekd/B8/KdpSysCheckLowMemory_function_00B884F0.md) (`PAGE` → `PAGEKD`)
  - `0x00744CEA` → [KdpSysWriteBusData](../../pagekd/B8/KdpSysWriteBusData_function_00B885A8.md) (`PAGE` → `PAGEKD`)
  - `0x00744D9C` → [KdpSysReadBusData](../../pagekd/B8/KdpSysReadBusData_function_00B88540.md) (`PAGE` → `PAGEKD`)
  - `0x00744DBD` → [KdpSysWriteMsr](../../text/5B/KdpSysWriteMsr_function_005B13A4.md) (`PAGE` → `.text`)
  - `0x00744DDE` → [KdpSysReadMsr](../../text/5B/KdpSysReadMsr_function_005B12B0.md) (`PAGE` → `.text`)
  - `0x00744E89` → [KdpSysWriteIoSpace](../../text/5B/KdpSysWriteIoSpace_function_005B12E4.md) (`PAGE` → `.text`)
  - `0x00744EBC` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00744700  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00744705  56                              push rsi
00744706  48 81 EC 70 01 00 00            sub rsp, 0x170
0074470D  4C 8B D2                        mov r10, rdx
00744710  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
00744715  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
0074471B  48 83 64 24 50 00               and qword ptr [rsp + 0x50], 0
00744721  80 3D F5 62 6C 00 00            cmp byte ptr [rip + 0x6c62f5], 0
00744728  75 12                           jne 0x14074473c
0074472A  80 3D EB 62 6C 00 00            cmp byte ptr [rip + 0x6c62eb], 0
00744731  75 09                           jne 0x14074473c
00744733  80 3D BE 2E 80 00 00            cmp byte ptr [rip + 0x802ebe], 0
0074473A  75 13                           jne 0x14074474f
0074473C  80 3D 3D 15 81 00 00            cmp byte ptr [rip + 0x81153d], 0
00744743  75 0A                           jne 0x14074474f
00744745  B8 22 00 00 C0                  mov eax, 0xc0000022
0074474A  E9 74 07 00 00                  jmp 0x140744ec3
0074474F  83 F9 0E                        cmp ecx, 0xe
00744752  0F 8F A5 04 00 00               jg 0x140744bfd
00744758  0F 84 ED 03 00 00               je 0x140744b4b
0074475E  83 E9 07                        sub ecx, 7
00744761  0F 84 C1 03 00 00               je 0x140744b28
00744767  83 E9 01                        sub ecx, 1
0074476A  0F 84 1F 03 00 00               je 0x140744a8f
00744770  83 E9 01                        sub ecx, 1
00744773  0F 84 83 02 00 00               je 0x1407449fc
00744779  83 E9 01                        sub ecx, 1
0074477C  0F 84 E4 01 00 00               je 0x140744966
00744782  83 E9 01                        sub ecx, 1
00744785  0F 84 38 01 00 00               je 0x1407448c3
0074478B  83 E9 01                        sub ecx, 1
0074478E  0F 84 96 00 00 00               je 0x14074482a
00744794  83 F9 01                        cmp ecx, 1
00744797  0F 85 8E 04 00 00               jne 0x140744c2b
0074479D  41 83 F8 18                     cmp r8d, 0x18
007447A1  74 0A                           je 0x1407447ad
007447A3  B8 04 00 00 C0                  mov eax, 0xc0000004
007447A8  E9 16 07 00 00                  jmp 0x140744ec3
007447AD  0F 10 02                        movups xmm0, xmmword ptr [rdx]
007447B0  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
007447B5  F2 0F 10 4A 10                  movsd xmm1, qword ptr [rdx + 0x10]
007447BA  F2 0F 11 4C 24 68               movsd qword ptr [rsp + 0x68], xmm1
007447C0  8B 74 24 68                     mov esi, dword ptr [rsp + 0x68]
007447C4  85 F6                           test esi, esi
007447C6  0F 84 F7 02 00 00               je 0x140744ac3
007447CC  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007447D1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007447D6  48 8D 44 24 48                  lea rax, [rsp + 0x48]
007447DB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007447E0  45 33 C9                        xor r9d, r9d
007447E3  44 8A 84 24 B0 01 00 00         mov r8b, byte ptr [rsp + 0x1b0]
007447EB  8B D6                           mov edx, esi
007447ED  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007447F2  E8 C1 EB 20 00                  call 0x1409533b8
007447F7  8B D8                           mov ebx, eax
007447F9  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007447FD  85 C0                           test eax, eax
007447FF  0F 88 8F 06 00 00               js 0x140744e94
00744805  48 8D 44 24 44                  lea rax, [rsp + 0x44]
0074480A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0074480F  44 8B CE                        mov r9d, esi
00744812  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00744817  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0074481C  8B 4C 24 6C                     mov ecx, dword ptr [rsp + 0x6c]
00744820  E8 1B 4F 44 00                  call 0x140b89740
00744825  E9 64 06 00 00                  jmp 0x140744e8e
0074482A  41 83 F8 18                     cmp r8d, 0x18
0074482E  74 0A                           je 0x14074483a
00744830  B8 04 00 00 C0                  mov eax, 0xc0000004
00744835  E9 89 06 00 00                  jmp 0x140744ec3
0074483A  0F 10 02                        movups xmm0, xmmword ptr [rdx]
0074483D  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
00744842  F2 0F 10 4A 10                  movsd xmm1, qword ptr [rdx + 0x10]
00744847  F2 0F 11 8C 24 80 00 00 00      movsd qword ptr [rsp + 0x80], xmm1
00744850  8B B4 24 80 00 00 00            mov esi, dword ptr [rsp + 0x80]
00744857  85 F6                           test esi, esi
00744859  0F 84 64 02 00 00               je 0x140744ac3
0074485F  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00744864  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00744869  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0074486E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00744873  41 B9 01 00 00 00               mov r9d, 1
00744879  44 8A 84 24 B0 01 00 00         mov r8b, byte ptr [rsp + 0x1b0]
00744881  8B D6                           mov edx, esi
00744883  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00744888  E8 2B EB 20 00                  call 0x1409533b8
0074488D  8B D8                           mov ebx, eax
0074488F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00744893  85 C0                           test eax, eax
00744895  0F 88 F9 05 00 00               js 0x140744e94
0074489B  48 8D 44 24 44                  lea rax, [rsp + 0x44]
007448A0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007448A5  44 8B CE                        mov r9d, esi
007448A8  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
007448AD  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
007448B2  8B 8C 24 84 00 00 00            mov ecx, dword ptr [rsp + 0x84]
007448B9  E8 9A 4D 44 00                  call 0x140b89658
007448BE  E9 CB 05 00 00                  jmp 0x140744e8e
007448C3  41 83 F8 18                     cmp r8d, 0x18
007448C7  74 0A                           je 0x1407448d3
007448C9  B8 04 00 00 C0                  mov eax, 0xc0000004
007448CE  E9 F0 05 00 00                  jmp 0x140744ec3
007448D3  0F 10 02                        movups xmm0, xmmword ptr [rdx]
007448D6  0F 11 84 24 08 01 00 00         movups xmmword ptr [rsp + 0x108], xmm0
007448DE  F2 0F 10 4A 10                  movsd xmm1, qword ptr [rdx + 0x10]
007448E3  F2 0F 11 8C 24 18 01 00 00      movsd qword ptr [rsp + 0x118], xmm1
007448EC  8B B4 24 18 01 00 00            mov esi, dword ptr [rsp + 0x118]
007448F3  85 F6                           test esi, esi
007448F5  0F 84 C8 01 00 00               je 0x140744ac3
007448FB  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00744900  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00744905  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0074490A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0074490F  45 33 C9                        xor r9d, r9d
00744912  44 8A 84 24 B0 01 00 00         mov r8b, byte ptr [rsp + 0x1b0]
0074491A  8B D6                           mov edx, esi
0074491C  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
00744924  E8 8F EA 20 00                  call 0x1409533b8
00744929  8B D8                           mov ebx, eax
0074492B  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0074492F  85 C0                           test eax, eax
00744931  0F 88 5D 05 00 00               js 0x140744e94
00744937  48 8D 44 24 44                  lea rax, [rsp + 0x44]
0074493C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00744941  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
00744949  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
00744951  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00744956  44 8B C6                        mov r8d, esi
00744959  45 33 C9                        xor r9d, r9d
0074495C  E8 6B 61 44 00                  call 0x140b8aacc
00744961  E9 28 05 00 00                  jmp 0x140744e8e
00744966  41 83 F8 18                     cmp r8d, 0x18
0074496A  74 0A                           je 0x140744976
0074496C  B8 04 00 00 C0                  mov eax, 0xc0000004
00744971  E9 4D 05 00 00                  jmp 0x140744ec3
00744976  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00744979  0F 11 84 24 20 01 00 00         movups xmmword ptr [rsp + 0x120], xmm0
00744981  F2 0F 10 4A 10                  movsd xmm1, qword ptr [rdx + 0x10]
00744986  F2 0F 11 8C 24 30 01 00 00      movsd qword ptr [rsp + 0x130], xmm1
0074498F  8B B4 24 30 01 00 00            mov esi, dword ptr [rsp + 0x130]
00744996  85 F6                           test esi, esi
00744998  0F 84 25 01 00 00               je 0x140744ac3
0074499E  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007449A3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007449A8  48 8D 44 24 48                  lea rax, [rsp + 0x48]
007449AD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007449B2  41 B9 01 00 00 00               mov r9d, 1
007449B8  44 8A 84 24 B0 01 00 00         mov r8b, byte ptr [rsp + 0x1b0]
007449C0  8B D6                           mov edx, esi
007449C2  48 8B 8C 24 28 01 00 00         mov rcx, qword ptr [rsp + 0x128]
007449CA  E8 E9 E9 20 00                  call 0x1409533b8
007449CF  8B D8                           mov ebx, eax
007449D1  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007449D5  85 C0                           test eax, eax
007449D7  0F 88 B7 04 00 00               js 0x140744e94
007449DD  48 8D 44 24 44                  lea rax, [rsp + 0x44]
007449E2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007449E7  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
007449EF  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
007449F7  E9 55 FF FF FF                  jmp 0x140744951
007449FC  41 83 F8 18                     cmp r8d, 0x18
00744A00  74 0A                           je 0x140744a0c
00744A02  B8 04 00 00 C0                  mov eax, 0xc0000004
00744A07  E9 B7 04 00 00                  jmp 0x140744ec3
00744A0C  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00744A0F  0F 11 84 24 38 01 00 00         movups xmmword ptr [rsp + 0x138], xmm0
00744A17  F2 0F 10 4A 10                  movsd xmm1, qword ptr [rdx + 0x10]
00744A1C  F2 0F 11 8C 24 48 01 00 00      movsd qword ptr [rsp + 0x148], xmm1
00744A25  8B B4 24 48 01 00 00            mov esi, dword ptr [rsp + 0x148]
00744A2C  85 F6                           test esi, esi
00744A2E  0F 84 8F 00 00 00               je 0x140744ac3
00744A34  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00744A39  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00744A3E  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00744A43  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00744A48  45 33 C9                        xor r9d, r9d
00744A4B  44 8A 84 24 B0 01 00 00         mov r8b, byte ptr [rsp + 0x1b0]
00744A53  8B D6                           mov edx, esi
00744A55  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
00744A5D  E8 56 E9 20 00                  call 0x1409533b8
00744A62  8B D8                           mov ebx, eax
00744A64  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00744A68  85 C0                           test eax, eax
00744A6A  0F 88 24 04 00 00               js 0x140744e94
00744A70  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00744A75  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00744A7A  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00744A82  48 8B 8C 24 38 01 00 00         mov rcx, qword ptr [rsp + 0x138]
00744A8A  E9 C2 FE FF FF                  jmp 0x140744951
00744A8F  41 83 F8 18                     cmp r8d, 0x18
00744A93  74 0A                           je 0x140744a9f
00744A95  B8 04 00 00 C0                  mov eax, 0xc0000004
00744A9A  E9 24 04 00 00                  jmp 0x140744ec3
00744A9F  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00744AA2  0F 11 84 24 50 01 00 00         movups xmmword ptr [rsp + 0x150], xmm0
00744AAA  F2 0F 10 4A 10                  movsd xmm1, qword ptr [rdx + 0x10]
00744AAF  F2 0F 11 8C 24 60 01 00 00      movsd qword ptr [rsp + 0x160], xmm1
00744AB8  8B B4 24 60 01 00 00            mov esi, dword ptr [rsp + 0x160]
00744ABF  85 F6                           test esi, esi
00744AC1  75 0A                           jne 0x140744acd
00744AC3  BB 05 00 00 C0                  mov ebx, 0xc0000005
00744AC8  E9 63 01 00 00                  jmp 0x140744c30
00744ACD  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00744AD2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00744AD7  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00744ADC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00744AE1  41 B9 01 00 00 00               mov r9d, 1
00744AE7  44 8A 84 24 B0 01 00 00         mov r8b, byte ptr [rsp + 0x1b0]
00744AEF  8B D6                           mov edx, esi
00744AF1  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
00744AF9  E8 BA E8 20 00                  call 0x1409533b8
00744AFE  8B D8                           mov ebx, eax
00744B00  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00744B04  85 C0                           test eax, eax
00744B06  0F 88 88 03 00 00               js 0x140744e94
00744B0C  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00744B11  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00744B16  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00744B1B  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
00744B23  E9 29 FE FF FF                  jmp 0x140744951
00744B28  83 BC 24 A0 01 00 00 28         cmp dword ptr [rsp + 0x1a0], 0x28
00744B30  74 0A                           je 0x140744b3c
00744B32  B8 04 00 00 C0                  mov eax, 0xc0000004
00744B37  E9 87 03 00 00                  jmp 0x140744ec3
00744B3C  49 8B C9                        mov rcx, r9
00744B3F  E8 D0 39 44 00                  call 0x140b88514
00744B44  33 DB                           xor ebx, ebx
00744B46  E9 E5 00 00 00                  jmp 0x140744c30
00744B4B  41 83 F8 20                     cmp r8d, 0x20
00744B4F  74 0A                           je 0x140744b5b
00744B51  B8 04 00 00 C0                  mov eax, 0xc0000004
00744B56  E9 68 03 00 00                  jmp 0x140744ec3
00744B5B  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00744B5E  0F 11 84 24 88 00 00 00         movups xmmword ptr [rsp + 0x88], xmm0
00744B66  0F 10 4A 10                     movups xmm1, xmmword ptr [rdx + 0x10]
00744B6A  0F 11 8C 24 98 00 00 00         movups xmmword ptr [rsp + 0x98], xmm1
00744B72  66 0F 7E CE                     movd esi, xmm1
00744B76  85 F6                           test esi, esi
00744B78  0F 84 45 FF FF FF               je 0x140744ac3
00744B7E  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00744B83  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00744B88  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00744B8D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00744B92  41 B9 01 00 00 00               mov r9d, 1
00744B98  44 8A 84 24 B0 01 00 00         mov r8b, byte ptr [rsp + 0x1b0]
00744BA0  8B D6                           mov edx, esi
00744BA2  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00744BAA  E8 09 E8 20 00                  call 0x1409533b8
00744BAF  8B D8                           mov ebx, eax
00744BB1  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00744BB5  85 C0                           test eax, eax
00744BB7  0F 88 D7 02 00 00               js 0x140744e94
00744BBD  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00744BC2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00744BC7  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00744BCB  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00744BD0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00744BD5  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
00744BDD  44 8B 84 24 A4 00 00 00         mov r8d, dword ptr [rsp + 0xa4]
00744BE5  8B 94 24 A0 00 00 00            mov edx, dword ptr [rsp + 0xa0]
00744BEC  8B 8C 24 9C 00 00 00            mov ecx, dword ptr [rsp + 0x9c]
00744BF3  E8 F4 C5 E6 FF                  call 0x1405b11ec
00744BF8  E9 91 02 00 00                  jmp 0x140744e8e
00744BFD  83 E9 0F                        sub ecx, 0xf
00744C00  0F 84 E2 01 00 00               je 0x140744de8
00744C06  83 E9 01                        sub ecx, 1
00744C09  0F 84 B8 01 00 00               je 0x140744dc7
00744C0F  83 E9 01                        sub ecx, 1
00744C12  0F 84 8E 01 00 00               je 0x140744da6
00744C18  83 E9 01                        sub ecx, 1
00744C1B  0F 84 D3 00 00 00               je 0x140744cf4
00744C21  83 E9 01                        sub ecx, 1
00744C24  74 1F                           je 0x140744c45
00744C26  83 F9 01                        cmp ecx, 1
00744C29  74 0E                           je 0x140744c39
00744C2B  BB 03 00 00 C0                  mov ebx, 0xc0000003
00744C30  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00744C34  E9 5B 02 00 00                  jmp 0x140744e94
00744C39  33 C9                           xor ecx, ecx
00744C3B  E8 B0 38 44 00                  call 0x140b884f0
00744C40  E9 49 02 00 00                  jmp 0x140744e8e
00744C45  41 83 F8 20                     cmp r8d, 0x20
00744C49  74 0A                           je 0x140744c55
00744C4B  B8 04 00 00 C0                  mov eax, 0xc0000004
00744C50  E9 6E 02 00 00                  jmp 0x140744ec3
00744C55  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00744C58  0F 11 84 24 A8 00 00 00         movups xmmword ptr [rsp + 0xa8], xmm0
00744C60  0F 10 4A 10                     movups xmm1, xmmword ptr [rdx + 0x10]
00744C64  0F 11 8C 24 B8 00 00 00         movups xmmword ptr [rsp + 0xb8], xmm1
00744C6C  66 0F 7E CE                     movd esi, xmm1
00744C70  85 F6                           test esi, esi
00744C72  0F 84 4B FE FF FF               je 0x140744ac3
00744C78  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00744C7D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00744C82  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00744C87  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00744C8C  45 33 C9                        xor r9d, r9d
00744C8F  44 8A 84 24 B0 01 00 00         mov r8b, byte ptr [rsp + 0x1b0]
00744C97  8B D6                           mov edx, esi
00744C99  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00744CA1  E8 12 E7 20 00                  call 0x1409533b8
00744CA6  8B D8                           mov ebx, eax
00744CA8  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00744CAC  85 C0                           test eax, eax
00744CAE  0F 88 E0 01 00 00               js 0x140744e94
00744CB4  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00744CB9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00744CBE  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00744CC2  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00744CC7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00744CCC  44 8B 8C 24 A8 00 00 00         mov r9d, dword ptr [rsp + 0xa8]
00744CD4  44 8B 84 24 C4 00 00 00         mov r8d, dword ptr [rsp + 0xc4]
00744CDC  8B 94 24 C0 00 00 00            mov edx, dword ptr [rsp + 0xc0]
00744CE3  8B 8C 24 BC 00 00 00            mov ecx, dword ptr [rsp + 0xbc]
00744CEA  E8 B9 38 44 00                  call 0x140b885a8
00744CEF  E9 9A 01 00 00                  jmp 0x140744e8e
00744CF4  41 83 F8 20                     cmp r8d, 0x20
00744CF8  74 0A                           je 0x140744d04
00744CFA  B8 04 00 00 C0                  mov eax, 0xc0000004
00744CFF  E9 BF 01 00 00                  jmp 0x140744ec3
00744D04  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00744D07  0F 11 84 24 C8 00 00 00         movups xmmword ptr [rsp + 0xc8], xmm0
00744D0F  0F 10 4A 10                     movups xmm1, xmmword ptr [rdx + 0x10]
00744D13  0F 11 8C 24 D8 00 00 00         movups xmmword ptr [rsp + 0xd8], xmm1
00744D1B  66 0F 7E CE                     movd esi, xmm1
00744D1F  85 F6                           test esi, esi
00744D21  0F 84 9C FD FF FF               je 0x140744ac3
00744D27  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00744D2C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00744D31  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00744D36  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00744D3B  41 B9 01 00 00 00               mov r9d, 1
00744D41  44 8A 84 24 B0 01 00 00         mov r8b, byte ptr [rsp + 0x1b0]
00744D49  8B D6                           mov edx, esi
00744D4B  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00744D53  E8 60 E6 20 00                  call 0x1409533b8
00744D58  8B D8                           mov ebx, eax
00744D5A  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00744D5E  85 C0                           test eax, eax
00744D60  0F 88 2E 01 00 00               js 0x140744e94
00744D66  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00744D6B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00744D70  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00744D74  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00744D79  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00744D7E  44 8B 8C 24 C8 00 00 00         mov r9d, dword ptr [rsp + 0xc8]
00744D86  44 8B 84 24 E4 00 00 00         mov r8d, dword ptr [rsp + 0xe4]
00744D8E  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
00744D95  8B 8C 24 DC 00 00 00            mov ecx, dword ptr [rsp + 0xdc]
00744D9C  E8 9F 37 44 00                  call 0x140b88540
00744DA1  E9 E8 00 00 00                  jmp 0x140744e8e
00744DA6  41 83 F8 10                     cmp r8d, 0x10
00744DAA  74 0A                           je 0x140744db6
00744DAC  B8 04 00 00 C0                  mov eax, 0xc0000004
00744DB1  E9 0D 01 00 00                  jmp 0x140744ec3
00744DB6  48 83 C2 08                     add rdx, 8
00744DBA  41 8B 0A                        mov ecx, dword ptr [r10]
00744DBD  E8 E2 C5 E6 FF                  call 0x1405b13a4
00744DC2  E9 C7 00 00 00                  jmp 0x140744e8e
00744DC7  41 83 F8 10                     cmp r8d, 0x10
00744DCB  74 0A                           je 0x140744dd7
00744DCD  B8 04 00 00 C0                  mov eax, 0xc0000004
00744DD2  E9 EC 00 00 00                  jmp 0x140744ec3
00744DD7  48 83 C2 08                     add rdx, 8
00744DDB  41 8B 0A                        mov ecx, dword ptr [r10]
00744DDE  E8 CD C4 E6 FF                  call 0x1405b12b0
00744DE3  E9 A6 00 00 00                  jmp 0x140744e8e
00744DE8  41 83 F8 20                     cmp r8d, 0x20
00744DEC  74 0A                           je 0x140744df8
00744DEE  B8 04 00 00 C0                  mov eax, 0xc0000004
00744DF3  E9 CB 00 00 00                  jmp 0x140744ec3
00744DF8  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00744DFB  0F 11 84 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm0
00744E03  0F 10 4A 10                     movups xmm1, xmmword ptr [rdx + 0x10]
00744E07  0F 11 8C 24 F8 00 00 00         movups xmmword ptr [rsp + 0xf8], xmm1
00744E0F  66 0F 7E CE                     movd esi, xmm1
00744E13  85 F6                           test esi, esi
00744E15  0F 84 A8 FC FF FF               je 0x140744ac3
00744E1B  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00744E20  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00744E25  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00744E2A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00744E2F  45 33 C9                        xor r9d, r9d
00744E32  44 8A 84 24 B0 01 00 00         mov r8b, byte ptr [rsp + 0x1b0]
00744E3A  8B D6                           mov edx, esi
00744E3C  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00744E44  E8 6F E5 20 00                  call 0x1409533b8
00744E49  8B D8                           mov ebx, eax
00744E4B  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00744E4F  85 C0                           test eax, eax
00744E51  78 41                           js 0x140744e94
00744E53  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00744E58  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00744E5D  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00744E61  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00744E66  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00744E6B  4C 8B 8C 24 E8 00 00 00         mov r9, qword ptr [rsp + 0xe8]
00744E73  44 8B 84 24 04 01 00 00         mov r8d, dword ptr [rsp + 0x104]
00744E7B  8B 94 24 00 01 00 00            mov edx, dword ptr [rsp + 0x100]
00744E82  8B 8C 24 FC 00 00 00            mov ecx, dword ptr [rsp + 0xfc]
00744E89  E8 56 C4 E6 FF                  call 0x1405b12e4
00744E8E  8B D8                           mov ebx, eax
00744E90  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00744E94  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
00744E9C  48 85 C9                        test rcx, rcx
00744E9F  74 06                           je 0x140744ea7
00744EA1  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
00744EA5  89 01                           mov dword ptr [rcx], eax
00744EA7  EB 06                           jmp 0x140744eaf
00744EA9  8B D8                           mov ebx, eax
00744EAB  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00744EAF  48 83 7C 24 48 00               cmp qword ptr [rsp + 0x48], 0
00744EB5  74 0A                           je 0x140744ec1
00744EB7  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00744EBC  E8 97 A3 B5 FF                  call 0x14029f258
00744EC1  8B C3                           mov eax, ebx
00744EC3  48 8B 9C 24 80 01 00 00         mov rbx, qword ptr [rsp + 0x180]
00744ECB  48 81 C4 70 01 00 00            add rsp, 0x170
00744ED2  5E                              pop rsi
00744ED3  C3                              ret
00744ED4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KdSystemDebugControl(int a1, __int64 a2, int a3, int a4, unsigned int a5, __int64 a6, unsigned __int8 a7)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m10C;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m134;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
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
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (368);
    if ((*(unsigned __int8 *)(v_rip + 7103221)) != 0) goto loc_0074473C;
    if ((*(unsigned __int8 *)(v_rip + 7103211)) != 0) goto loc_0074473C;
    if ((*(unsigned __int8 *)(v_rip + 8400574)) != 0) goto loc_0074474F;
loc_0074473C:
    if ((*(unsigned __int8 *)(v_rip + 8459581)) != 0) goto loc_0074474F;
    goto loc_00744EC3;
loc_0074474F:
    if (a1 > 14) goto loc_00744BFD;
    if (a1 == 14) goto loc_00744B4B;
    a1 = (unsigned int)((a1) - (7));
    if (condition_is_equal) goto loc_00744B28;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00744A8F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_007449FC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00744966;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_007448C3;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0074482A;
    if (a1 != 1) goto loc_00744C2B;
    if (a3 == 24) goto loc_007447AD;
    goto loc_00744EC3;
loc_007447AD:
    v_stack_m120 = v_xmm0;
    v_stack_m110 = v_xmm1;
    if ((unsigned int)((unsigned int)(v_stack_m110)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    a4 = 0;
    result = ExLockUserBuffer(v_stack_m118, (unsigned int)((unsigned int)((unsigned int)(v_stack_m110))), a7, a4);
    v_stack_m138 = (unsigned int)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m158 = v_stack_m134;
    result = KdpSysWriteControlSpace((unsigned int)(v_stack_m10C), v_stack_m120, v_stack_m130, (unsigned int)((unsigned int)((unsigned int)(v_stack_m110))));
    goto loc_00744E8E;
loc_0074482A:
    if (((unsigned int)(v_stack_m130)) == 24) goto loc_0074483A;
    goto loc_00744EC3;
loc_0074483A:
    v_stack_m108 = v_xmm0;
    v_stack_mF8 = v_xmm1;
    if ((unsigned int)((unsigned int)(v_stack_mF8)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    result = ExLockUserBuffer(v_stack_m100, (unsigned int)((unsigned int)((unsigned int)(v_stack_mF8))), a7, 1);
    v_stack_m138 = (unsigned int)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m158 = v_stack_m134;
    result = KdpSysReadControlSpace((unsigned int)(v_stack_mF4), v_stack_m108, v_stack_m130, (unsigned int)((unsigned int)((unsigned int)(v_stack_mF8))));
    goto loc_00744E8E;
loc_007448C3:
    if (((unsigned int)(v_stack_m130)) == 24) goto loc_007448D3;
    goto loc_00744EC3;
loc_007448D3:
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm1;
    if ((unsigned int)((unsigned int)(v_stack_m60)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    a4 = 0;
    result = ExLockUserBuffer(v_stack_m68, (unsigned int)((unsigned int)((unsigned int)(v_stack_m60))), a7, a4);
    v_stack_m138 = (unsigned int)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m150 = v_stack_m134;
    v_stack_m158 = 3;
loc_00744951:
    a4 = 0;
    result = KdpCopyMemoryChunks(v_stack_m70, v_stack_m130, (unsigned int)((unsigned int)((unsigned int)(v_stack_m60))), a4);
    goto loc_00744E8E;
loc_00744966:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m60))))) == 24) goto loc_00744976;
    goto loc_00744EC3;
loc_00744976:
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm1;
    if ((unsigned int)((unsigned int)(v_stack_m48)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    result = ExLockUserBuffer(v_stack_m50, (unsigned int)((unsigned int)((unsigned int)(v_stack_m48))), a7, 1);
    v_stack_m138 = (unsigned int)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m150 = v_stack_m134;
    v_stack_m158 = 2;
    goto loc_00744951;
loc_007449FC:
    if (a7 == 24) goto loc_00744A0C;
    goto loc_00744EC3;
loc_00744A0C:
    v_stack_m40 = v_xmm0;
    v_stack_m30 = v_xmm1;
    if ((unsigned int)((unsigned int)(v_stack_m30)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    a4 = 0;
    result = ExLockUserBuffer(v_stack_m38, (unsigned int)((unsigned int)((unsigned int)(v_stack_m30))), a7, a4);
    v_stack_m138 = (unsigned int)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m150 = v_stack_m134;
    v_stack_m158 = 1;
    goto loc_00744951;
loc_00744A8F:
    if (a7 == 24) goto loc_00744A9F;
    goto loc_00744EC3;
loc_00744A9F:
    v_stack_m28 = v_xmm0;
    v_stack_m18 = v_xmm1;
    if ((unsigned int)((unsigned int)(v_stack_m18)) != 0) goto loc_00744ACD;
loc_00744AC3:
    goto loc_00744C30;
loc_00744ACD:
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    result = ExLockUserBuffer(v_stack_m20, (unsigned int)((unsigned int)((unsigned int)(v_stack_m18))), a7, 1);
    v_stack_m138 = (unsigned int)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m150 = v_stack_m134;
    goto loc_00744951;
loc_00744B28:
    if (a5 == 40) goto loc_00744B3C;
    goto loc_00744EC3;
loc_00744B3C:
    result = KdpSysGetVersion(1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m18))), a7, 1);
    v_rbx = 0;
    goto loc_00744C30;
loc_00744B4B:
    if (a7 == 32) goto loc_00744B5B;
    goto loc_00744EC3;
loc_00744B5B:
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    if ((unsigned int)((unsigned int)(v_stack_m18)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    result = ExLockUserBuffer(v_stack_mE8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m18))), a7, 1);
    v_stack_m138 = (unsigned int)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m148 = v_stack_m134;
    v_stack_m150 = (unsigned int)((unsigned int)(v_stack_m18));
    v_stack_m158 = v_stack_m130;
    result = KdpSysReadIoSpace((unsigned int)(v_stack_mDC), (unsigned int)(v_stack_mD8), (unsigned int)(v_stack_mD4), v_stack_mF0);
    goto loc_00744E8E;
loc_00744BFD:
    a1 = (unsigned int)(((unsigned int)(v_stack_mDC)) - (15));
    if (condition_is_equal) goto loc_00744DE8;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00744DC7;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00744DA6;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00744CF4;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00744C45;
    if (a1 == 1) goto loc_00744C39;
loc_00744C2B:
loc_00744C30:
    v_stack_m138 = (unsigned int)((unsigned int)(0xC0000003ULL));
    goto loc_00744E94;
loc_00744C39:
    a1 = 0;
    result = KdpSysCheckLowMemory(a1, (unsigned int)(v_stack_mD8), (unsigned int)(v_stack_mD4), v_stack_mF0);
    goto loc_00744E8E;
loc_00744C45:
    if (((unsigned int)((unsigned int)(v_stack_mD4))) == 32) goto loc_00744C55;
    goto loc_00744EC3;
loc_00744C55:
    v_stack_mD0 = v_xmm0;
    v_stack_mC0 = v_xmm1;
    if ((unsigned int)((unsigned int)(v_stack_m18)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    a4 = 0;
    result = ExLockUserBuffer(v_stack_mC8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m18))), a7, a4);
    v_stack_m138 = (unsigned int)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m148 = v_stack_m134;
    v_stack_m150 = (unsigned int)((unsigned int)(v_stack_m18));
    v_stack_m158 = v_stack_m130;
    result = KdpSysWriteBusData((unsigned int)(v_stack_mBC), (unsigned int)(v_stack_mB8), (unsigned int)(v_stack_mB4), (unsigned int)(v_stack_mD0));
    goto loc_00744E8E;
loc_00744CF4:
    if (((unsigned int)((unsigned int)(v_stack_mB4))) == 32) goto loc_00744D04;
    goto loc_00744EC3;
loc_00744D04:
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm1;
    if ((unsigned int)((unsigned int)(v_stack_m18)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    result = ExLockUserBuffer(v_stack_mA8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m18))), a7, 1);
    v_stack_m138 = (unsigned int)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m148 = v_stack_m134;
    v_stack_m150 = (unsigned int)((unsigned int)(v_stack_m18));
    v_stack_m158 = v_stack_m130;
    result = KdpSysReadBusData((unsigned int)(v_stack_m9C), (unsigned int)(v_stack_m98), (unsigned int)(v_stack_m94), (unsigned int)(v_stack_mB0));
    goto loc_00744E8E;
loc_00744DA6:
    if (((unsigned int)((unsigned int)(v_stack_m94))) == 16) goto loc_00744DB6;
    goto loc_00744EC3;
loc_00744DB6:
    a2 = ((unsigned int)(v_stack_m98)) + (8);
    result = KdpSysWriteMsr((unsigned int)(*(unsigned int *)(a2)), a2, (unsigned int)(v_stack_m94), (unsigned int)(v_stack_mB0));
    goto loc_00744E8E;
loc_00744DC7:
    if (((unsigned int)((unsigned int)(v_stack_m94))) == 16) goto loc_00744DD7;
    goto loc_00744EC3;
loc_00744DD7:
    a2 = (a2) + (8);
    result = KdpSysReadMsr((unsigned int)(*(unsigned int *)(a2)), a2, (unsigned int)(v_stack_m94), (unsigned int)(v_stack_mB0));
    goto loc_00744E8E;
loc_00744DE8:
    if (((unsigned int)((unsigned int)(v_stack_m94))) == 32) goto loc_00744DF8;
    goto loc_00744EC3;
loc_00744DF8:
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm1;
    if ((unsigned int)((unsigned int)(v_stack_m18)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    a4 = 0;
    result = ExLockUserBuffer(v_stack_m88, (unsigned int)((unsigned int)((unsigned int)(v_stack_m18))), a7, a4);
    v_stack_m138 = (unsigned int)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m148 = v_stack_m134;
    v_stack_m150 = (unsigned int)((unsigned int)(v_stack_m18));
    v_stack_m158 = v_stack_m130;
    result = KdpSysWriteIoSpace((unsigned int)(v_stack_m7C), (unsigned int)(v_stack_m78), (unsigned int)(v_stack_m74), v_stack_m90);
loc_00744E8E:
    v_stack_m138 = (unsigned int)(result);
loc_00744E94:
    if (a6 != 0) {
        result = v_stack_m134;
        *(unsigned int *)(a6) = (unsigned int)(result);
    }
    goto loc_00744EAF;
loc_00744EAF:
    if (v_stack_m130 != 0) {
        a1 = v_stack_m128;
        result = ExUnlockUserBuffer(a1, (unsigned int)(v_stack_m78), (unsigned int)(v_stack_m74), v_stack_m90);
    }
loc_00744EC3:
    v_rsp = (v_rsp) + (368);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t KdSystemDebugControl(int32_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, int64_t Arg6, uint8_t Arg7)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m10C;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m134;
    uint32_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
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
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (368);
    if ((*(uint8_t *)(v_rip + 0x6C62F5)) != 0) goto loc_0074473C;
    if ((*(uint8_t *)(v_rip + 0x6C62EB)) != 0) goto loc_0074473C;
    if ((*(uint8_t *)(v_rip + 0x802EBE)) != 0) goto loc_0074474F;
loc_0074473C:
    if ((*(uint8_t *)(v_rip + 0x81153D)) != 0) goto loc_0074474F;
    goto loc_00744EC3;
loc_0074474F:
    if (Arg1 > 14) goto loc_00744BFD;
    if (Arg1 == 14) goto loc_00744B4B;
    Arg1 = (uint32_t)((Arg1) - (7));
    if (condition_is_equal) goto loc_00744B28;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00744A8F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_007449FC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00744966;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_007448C3;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0074482A;
    if (Arg1 != 1) goto loc_00744C2B;
    if (Arg3 == 24) goto loc_007447AD;
    goto loc_00744EC3;
loc_007447AD:
    v_stack_m120 = v_xmm0;
    v_stack_m110 = v_xmm1;
    if ((uint32_t)((uint32_t)(v_stack_m110)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    Arg4 = 0;
    result = ExLockUserBuffer(v_stack_m118, (uint32_t)((uint32_t)((uint32_t)(v_stack_m110))), Arg7, Arg4);
    v_stack_m138 = (uint32_t)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m158 = v_stack_m134;
    result = KdpSysWriteControlSpace((uint32_t)(v_stack_m10C), v_stack_m120, v_stack_m130, (uint32_t)((uint32_t)((uint32_t)(v_stack_m110))));
    goto loc_00744E8E;
loc_0074482A:
    if (((uint32_t)(v_stack_m130)) == 24) goto loc_0074483A;
    goto loc_00744EC3;
loc_0074483A:
    v_stack_m108 = v_xmm0;
    v_stack_mF8 = v_xmm1;
    if ((uint32_t)((uint32_t)(v_stack_mF8)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    result = ExLockUserBuffer(v_stack_m100, (uint32_t)((uint32_t)((uint32_t)(v_stack_mF8))), Arg7, 1);
    v_stack_m138 = (uint32_t)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m158 = v_stack_m134;
    result = KdpSysReadControlSpace((uint32_t)(v_stack_mF4), v_stack_m108, v_stack_m130, (uint32_t)((uint32_t)((uint32_t)(v_stack_mF8))));
    goto loc_00744E8E;
loc_007448C3:
    if (((uint32_t)(v_stack_m130)) == 24) goto loc_007448D3;
    goto loc_00744EC3;
loc_007448D3:
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm1;
    if ((uint32_t)((uint32_t)(v_stack_m60)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    Arg4 = 0;
    result = ExLockUserBuffer(v_stack_m68, (uint32_t)((uint32_t)((uint32_t)(v_stack_m60))), Arg7, Arg4);
    v_stack_m138 = (uint32_t)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m150 = v_stack_m134;
    v_stack_m158 = 3;
loc_00744951:
    Arg4 = 0;
    result = KdpCopyMemoryChunks(v_stack_m70, v_stack_m130, (uint32_t)((uint32_t)((uint32_t)(v_stack_m60))), Arg4);
    goto loc_00744E8E;
loc_00744966:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m60))))) == 24) goto loc_00744976;
    goto loc_00744EC3;
loc_00744976:
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm1;
    if ((uint32_t)((uint32_t)(v_stack_m48)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    result = ExLockUserBuffer(v_stack_m50, (uint32_t)((uint32_t)((uint32_t)(v_stack_m48))), Arg7, 1);
    v_stack_m138 = (uint32_t)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m150 = v_stack_m134;
    v_stack_m158 = 2;
    goto loc_00744951;
loc_007449FC:
    if (Arg7 == 24) goto loc_00744A0C;
    goto loc_00744EC3;
loc_00744A0C:
    v_stack_m40 = v_xmm0;
    v_stack_m30 = v_xmm1;
    if ((uint32_t)((uint32_t)(v_stack_m30)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    Arg4 = 0;
    result = ExLockUserBuffer(v_stack_m38, (uint32_t)((uint32_t)((uint32_t)(v_stack_m30))), Arg7, Arg4);
    v_stack_m138 = (uint32_t)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m150 = v_stack_m134;
    v_stack_m158 = 1;
    goto loc_00744951;
loc_00744A8F:
    if (Arg7 == 24) goto loc_00744A9F;
    goto loc_00744EC3;
loc_00744A9F:
    v_stack_m28 = v_xmm0;
    v_stack_m18 = v_xmm1;
    if ((uint32_t)((uint32_t)(v_stack_m18)) != 0) goto loc_00744ACD;
loc_00744AC3:
    goto loc_00744C30;
loc_00744ACD:
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    result = ExLockUserBuffer(v_stack_m20, (uint32_t)((uint32_t)((uint32_t)(v_stack_m18))), Arg7, 1);
    v_stack_m138 = (uint32_t)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m150 = v_stack_m134;
    goto loc_00744951;
loc_00744B28:
    if (Arg5 == 40) goto loc_00744B3C;
    goto loc_00744EC3;
loc_00744B3C:
    result = KdpSysGetVersion(1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m18))), Arg7, 1);
    local_rbx = 0;
    goto loc_00744C30;
loc_00744B4B:
    if (Arg7 == 32) goto loc_00744B5B;
    goto loc_00744EC3;
loc_00744B5B:
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    if ((uint32_t)((uint32_t)(v_stack_m18)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    result = ExLockUserBuffer(v_stack_mE8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m18))), Arg7, 1);
    v_stack_m138 = (uint32_t)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m148 = v_stack_m134;
    v_stack_m150 = (uint32_t)((uint32_t)(v_stack_m18));
    v_stack_m158 = v_stack_m130;
    result = KdpSysReadIoSpace((uint32_t)(v_stack_mDC), (uint32_t)(v_stack_mD8), (uint32_t)(v_stack_mD4), v_stack_mF0);
    goto loc_00744E8E;
loc_00744BFD:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_mDC)) - (15));
    if (condition_is_equal) goto loc_00744DE8;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00744DC7;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00744DA6;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00744CF4;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00744C45;
    if (Arg1 == 1) goto loc_00744C39;
loc_00744C2B:
loc_00744C30:
    v_stack_m138 = (uint32_t)((uint32_t)(0xC0000003ULL));
    goto loc_00744E94;
loc_00744C39:
    Arg1 = 0;
    result = KdpSysCheckLowMemory(Arg1, (uint32_t)(v_stack_mD8), (uint32_t)(v_stack_mD4), v_stack_mF0);
    goto loc_00744E8E;
loc_00744C45:
    if (((uint32_t)((uint32_t)(v_stack_mD4))) == 32) goto loc_00744C55;
    goto loc_00744EC3;
loc_00744C55:
    v_stack_mD0 = v_xmm0;
    v_stack_mC0 = v_xmm1;
    if ((uint32_t)((uint32_t)(v_stack_m18)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    Arg4 = 0;
    result = ExLockUserBuffer(v_stack_mC8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m18))), Arg7, Arg4);
    v_stack_m138 = (uint32_t)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m148 = v_stack_m134;
    v_stack_m150 = (uint32_t)((uint32_t)(v_stack_m18));
    v_stack_m158 = v_stack_m130;
    result = KdpSysWriteBusData((uint32_t)(v_stack_mBC), (uint32_t)(v_stack_mB8), (uint32_t)(v_stack_mB4), (uint32_t)(v_stack_mD0));
    goto loc_00744E8E;
loc_00744CF4:
    if (((uint32_t)((uint32_t)(v_stack_mB4))) == 32) goto loc_00744D04;
    goto loc_00744EC3;
loc_00744D04:
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm1;
    if ((uint32_t)((uint32_t)(v_stack_m18)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    result = ExLockUserBuffer(v_stack_mA8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m18))), Arg7, 1);
    v_stack_m138 = (uint32_t)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m148 = v_stack_m134;
    v_stack_m150 = (uint32_t)((uint32_t)(v_stack_m18));
    v_stack_m158 = v_stack_m130;
    result = KdpSysReadBusData((uint32_t)(v_stack_m9C), (uint32_t)(v_stack_m98), (uint32_t)(v_stack_m94), (uint32_t)(v_stack_mB0));
    goto loc_00744E8E;
loc_00744DA6:
    if (((uint32_t)((uint32_t)(v_stack_m94))) == 16) goto loc_00744DB6;
    goto loc_00744EC3;
loc_00744DB6:
    Arg2 = ((uint32_t)(v_stack_m98)) + (8);
    result = KdpSysWriteMsr((uint32_t)(*(uint32_t *)(arg2)), Arg2, (uint32_t)(v_stack_m94), (uint32_t)(v_stack_mB0));
    goto loc_00744E8E;
loc_00744DC7:
    if (((uint32_t)((uint32_t)(v_stack_m94))) == 16) goto loc_00744DD7;
    goto loc_00744EC3;
loc_00744DD7:
    Arg2 = (Arg2) + (8);
    result = KdpSysReadMsr((uint32_t)(*(uint32_t *)(arg2)), Arg2, (uint32_t)(v_stack_m94), (uint32_t)(v_stack_mB0));
    goto loc_00744E8E;
loc_00744DE8:
    if (((uint32_t)((uint32_t)(v_stack_m94))) == 32) goto loc_00744DF8;
    goto loc_00744EC3;
loc_00744DF8:
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm1;
    if ((uint32_t)((uint32_t)(v_stack_m18)) == 0) goto loc_00744AC3;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m130;
    Arg4 = 0;
    result = ExLockUserBuffer(v_stack_m88, (uint32_t)((uint32_t)((uint32_t)(v_stack_m18))), Arg7, Arg4);
    v_stack_m138 = (uint32_t)(result);
    if (sign_flag) goto loc_00744E94;
    v_stack_m148 = v_stack_m134;
    v_stack_m150 = (uint32_t)((uint32_t)(v_stack_m18));
    v_stack_m158 = v_stack_m130;
    result = KdpSysWriteIoSpace((uint32_t)(v_stack_m7C), (uint32_t)(v_stack_m78), (uint32_t)(v_stack_m74), v_stack_m90);
loc_00744E8E:
    v_stack_m138 = (uint32_t)(result);
loc_00744E94:
    if (Arg6 != 0) {
        result = v_stack_m134;
        *(uint32_t *)(Arg6) = (uint32_t)(result);
    }
    goto loc_00744EAF;
loc_00744EAF:
    if (v_stack_m130 != 0) {
        Arg1 = v_stack_m128;
        result = ExUnlockUserBuffer(Arg1, (uint32_t)(v_stack_m78), (uint32_t)(v_stack_m74), v_stack_m90);
    }
loc_00744EC3:
    local_rsp = (local_rsp) + (368);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x10` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00744700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
