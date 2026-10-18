# HvLoadHive

- RVA: `0x009B8138`–`0x009B8751` (길이 `1,561` bytes)
- VA: `0x00000001409B8138`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009E924`
- 디코드: `359`개 명령, `1,561/1,561` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x009B81B9` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009B81DF` → [HvpGetHiveHeader](HvpGetHiveHeader_function_009B8758.md) (function, `0x009B8758`)
- `0x009B8242` → [CmpInitializeActualFileSizes](CmpInitializeActualFileSizes_function_009B8900.md) (function, `0x009B8900`)
- `0x009B8287` → [HvpInitMap](HvpInitMap_function_009B8A68.md) (function, `0x009B8A68`)
- `0x009B82EE` → [HvpViewMapStart](HvpViewMapStart_function_009B98E0.md) (function, `0x009B98E0`)
- `0x009B830A` → [HvpMapHiveImageFromViewMap](HvpMapHiveImageFromViewMap_function_009B97F4.md) (function, `0x009B97F4`)
- `0x009B8327` → [CmpTraceHiveMountBaseFileMounted](CmpTraceHiveMountBaseFileMounted_function_009B8D0C.md) (function, `0x009B8D0C`)
- `0x009B8363` → [HvpAdjustHiveFreeDisplay](../84/HvpAdjustHiveFreeDisplay_function_0084DB80.md) (function, `0x0084DB80`)
- `0x009B837C` → [HvpRemapAndEnlistHiveBins](HvpRemapAndEnlistHiveBins_function_009B8E0C.md) (function, `0x009B8E0C`)
- `0x009B83C8` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x009B83F5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009B8406` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009B842C` → [CmpFileFlush](CmpFileFlush_function_009B9A04.md) (function, `0x009B9A04`)
- `0x009B844C` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x009B8475` → [HvpMapHiveImageFromFile](HvpMapHiveImageFromFile_function_009BA028.md) (function, `0x009BA028`)
- `0x009B84A4` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x009B8560` → [HvAnalyzeLogFiles](HvAnalyzeLogFiles_function_009B9A9C.md) (function, `0x009B9A9C`)
- `0x009B85E6` → [HvpPerformLogFileRecovery](HvpPerformLogFileRecovery_function_009B7994.md) (function, `0x009B7994`)
- `0x009B861C` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x009B865E` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x009B868E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009B8747` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HvHiveStartFileBacked](HvHiveStartFileBacked_function_009B7E20.md) at `0x009B7F2B`

### Static image references
- `0x009B8157` → RVA `0x00E0A740` (`.data`; read)
- `0x009B82D9` → RVA `0x00EF7200` (`.data`; read)
- `0x009B8503` → RVA `0x00A6DA60` (`HvpRecoverDataReadRoutine`; read)
- `0x009B857A` → RVA `0x00E09F58` (`.data`; read)
- `0x009B86D3` → RVA `0x00FD8002` (`PAGEDATA`; read)
- `0x009B86E0` → RVA `0x00EF7C60` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x009B81B9` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009B83C8` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x009B83F5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009B8406` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009B844C` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x009B84A4` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x009B861C` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x009B865E` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x009B868E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009B8747` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x009B8581` → [sub_00B2DF7A + 0x9](../B2/Unknown_function_00B2DF7A.md) (`tail-transfer`)
  - `0x009B8699` → [sub_00B2DF7A](../B2/Unknown_function_00B2DF7A.md) (`tail-transfer`)
  - `0x009B86AD` → [sub_00B2DF7A + 0x143](../B2/Unknown_function_00B2DF7A.md) (`tail-transfer`)
  - `0x009B86DA` → [sub_00B2DF7A + 0x87](../B2/Unknown_function_00B2DF7A.md) (`tail-transfer`)
  - `0x009B86EE` → [sub_00B2DF7A + 0x87](../B2/Unknown_function_00B2DF7A.md) (`tail-transfer`)
  - `0x009B8735` → [sub_00B2DF7A + 0x143](../B2/Unknown_function_00B2DF7A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009B8138  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
009B813D  55                              push rbp
009B813E  56                              push rsi
009B813F  57                              push rdi
009B8140  41 54                           push r12
009B8142  41 55                           push r13
009B8144  41 56                           push r14
009B8146  41 57                           push r15
009B8148  48 8D AC 24 70 FF FF FF         lea rbp, [rsp - 0x90]
009B8150  48 81 EC 90 01 00 00            sub rsp, 0x190
009B8157  48 8B 05 E2 25 45 00            mov rax, qword ptr [rip + 0x4525e2]
009B815E  48 33 C4                        xor rax, rsp
009B8161  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
009B8168  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
009B816E  0F 57 C0                        xorps xmm0, xmm0
009B8171  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
009B8176  0F 57 C9                        xorps xmm1, xmm1
009B8179  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
009B817F  48 8B F9                        mov rdi, rcx
009B8182  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
009B8187  48 8D 4D D0                     lea rcx, [rbp - 0x30]
009B818B  45 33 ED                        xor r13d, r13d
009B818E  45 32 E4                        xor r12b, r12b
009B8191  33 D2                           xor edx, edx
009B8193  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
009B8198  49 8B F1                        mov rsi, r9
009B819B  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
009B81A0  45 8D 45 5C                     lea r8d, [r13 + 0x5c]
009B81A4  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
009B81A9  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
009B81AD  0F 11 4D 98                     movups xmmword ptr [rbp - 0x68], xmm1
009B81B1  0F 11 4D A8                     movups xmmword ptr [rbp - 0x58], xmm1
009B81B5  0F 11 4D B8                     movups xmmword ptr [rbp - 0x48], xmm1
009B81B9  E8 82 EA D0 FF                  call 0x1406c6c40
009B81BE  F7 87 A0 00 00 00 01 80 00 00   test dword ptr [rdi + 0xa0], 0x8001
009B81C8  45 8D 7D 06                     lea r15d, [r13 + 6]
009B81CC  0F 84 55 02 00 00               je 0x1409b8427
009B81D2  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
009B81D7  48 8B CF                        mov rcx, rdi
009B81DA  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
009B81DF  E8 74 05 00 00                  call 0x1409b8758
009B81E4  BA 02 00 00 00                  mov edx, 2
009B81E9  44 8B F0                        mov r14d, eax
009B81EC  3B C2                           cmp eax, edx
009B81EE  0F 84 32 04 00 00               je 0x1409b8626
009B81F4  83 F8 07                        cmp eax, 7
009B81F7  0F 84 49 04 00 00               je 0x1409b8646
009B81FD  85 C0                           test eax, eax
009B81FF  0F 84 68 04 00 00               je 0x1409b866d
009B8205  83 C0 FC                        add eax, -4
009B8208  44 8D 4A FF                     lea r9d, [rdx - 1]
009B820C  41 3B C1                        cmp eax, r9d
009B820F  0F 86 99 02 00 00               jbe 0x1409b84ae
009B8215  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
009B821A  49 8B C7                        mov rax, r15
009B821D  4C 89 7F 40                     mov qword ptr [rdi + 0x40], r15
009B8221  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
009B8226  45 33 FF                        xor r15d, r15d
009B8229  8B 48 14                        mov ecx, dword ptr [rax + 0x14]
009B822C  8B 40 18                        mov eax, dword ptr [rax + 0x18]
009B822F  C1 E1 0C                        shl ecx, 0xc
009B8232  05 00 F0 FF FF                  add eax, 0xfffff000
009B8237  03 C8                           add ecx, eax
009B8239  89 8F DC 00 00 00               mov dword ptr [rdi + 0xdc], ecx
009B823F  48 8B CF                        mov rcx, rdi
009B8242  E8 B9 06 00 00                  call 0x1409b8900
009B8247  45 33 C9                        xor r9d, r9d
009B824A  8B D8                           mov ebx, eax
009B824C  85 C0                           test eax, eax
009B824E  0F 88 BB 03 00 00               js 0x1409b860f
009B8254  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
009B8258  8B 5C 24 50                     mov ebx, dword ptr [rsp + 0x50]
009B825C  44 8B 40 28                     mov r8d, dword ptr [rax + 0x28]
009B8260  41 8D 80 00 10 00 00            lea eax, [r8 + 0x1000]
009B8267  3B D8                           cmp ebx, eax
009B8269  0F 82 56 04 00 00               jb 0x1409b86c5
009B826F  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
009B8273  8B 48 28                        mov ecx, dword ptr [rax + 0x28]
009B8276  FF C9                           dec ecx
009B8278  81 F9 FF DF FF 7F               cmp ecx, 0x7fffdfff
009B827E  0F 87 A3 04 00 00               ja 0x1409b8727
009B8284  48 8B CF                        mov rcx, rdi
009B8287  E8 DC 07 00 00                  call 0x1409b8a68
009B828C  8B D8                           mov ebx, eax
009B828E  85 C0                           test eax, eax
009B8290  0F 88 5D 04 00 00               js 0x1409b86f3
009B8296  44 8B 8F A0 00 00 00            mov r9d, dword ptr [rdi + 0xa0]
009B829D  4C 8B 47 40                     mov r8, qword ptr [rdi + 0x40]
009B82A1  41 0F BA E1 11                  bt r9d, 0x11
009B82A6  0F 83 C2 01 00 00               jae 0x1409b846e
009B82AC  45 8B 40 28                     mov r8d, dword ptr [r8 + 0x28]
009B82B0  41 8B C9                        mov ecx, r9d
009B82B3  C1 E9 16                        shr ecx, 0x16
009B82B6  83 E1 02                        and ecx, 2
009B82B9  8B D1                           mov edx, ecx
009B82BB  83 CA 08                        or edx, 8
009B82BE  41 0F BA E1 1B                  bt r9d, 0x1b
009B82C3  0F 43 D1                        cmovae edx, ecx
009B82C6  48 8D 8F E0 00 00 00            lea rcx, [rdi + 0xe0]
009B82CD  8B C2                           mov eax, edx
009B82CF  83 C8 01                        or eax, 1
009B82D2  41 F7 C1 01 80 00 00            test r9d, 0x8001
009B82D9  4C 8D 0D 20 EF 53 00            lea r9, [rip + 0x53ef20]
009B82E0  0F 44 C2                        cmove eax, edx
009B82E3  48 8B 97 08 06 00 00            mov rdx, qword ptr [rdi + 0x608]
009B82EA  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009B82EE  E8 ED 15 00 00                  call 0x1409b98e0
009B82F3  33 D2                           xor edx, edx
009B82F5  8B D8                           mov ebx, eax
009B82F7  85 C0                           test eax, eax
009B82F9  0F 88 01 04 00 00               js 0x1409b8700
009B82FF  4C 8B 47 40                     mov r8, qword ptr [rdi + 0x40]
009B8303  48 8B CF                        mov rcx, rdi
009B8306  45 8B 40 28                     mov r8d, dword ptr [r8 + 0x28]
009B830A  E8 E5 14 00 00                  call 0x1409b97f4
009B830F  8B D8                           mov ebx, eax
009B8311  85 C0                           test eax, eax
009B8313  0F 88 E9 02 00 00               js 0x1409b8602
009B8319  48 8B 57 40                     mov rdx, qword ptr [rdi + 0x40]
009B831D  48 8B 8F 08 06 00 00            mov rcx, qword ptr [rdi + 0x608]
009B8324  8B 52 28                        mov edx, dword ptr [rdx + 0x28]
009B8327  E8 E0 09 00 00                  call 0x1409b8d0c
009B832C  44 39 7D 0C                     cmp dword ptr [rbp + 0xc], r15d
009B8330  0F 87 9F 02 00 00               ja 0x1409b85d5
009B8336  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
009B833A  8B 48 04                        mov ecx, dword ptr [rax + 4]
009B833D  89 8F AC 00 00 00               mov dword ptr [rdi + 0xac], ecx
009B8343  89 8F B8 00 00 00               mov dword ptr [rdi + 0xb8], ecx
009B8349  89 8F B0 00 00 00               mov dword ptr [rdi + 0xb0], ecx
009B834F  C6 87 C2 00 00 00 01            mov byte ptr [rdi + 0xc2], 1
009B8356  48 8B 57 40                     mov rdx, qword ptr [rdi + 0x40]
009B835A  45 33 C0                        xor r8d, r8d
009B835D  48 8B CF                        mov rcx, rdi
009B8360  8B 52 28                        mov edx, dword ptr [rdx + 0x28]
009B8363  E8 18 58 E9 FF                  call 0x14084db80
009B8368  8B D8                           mov ebx, eax
009B836A  85 C0                           test eax, eax
009B836C  0F 88 1F 02 00 00               js 0x1409b8591
009B8372  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
009B8376  4C 8B C6                        mov r8, rsi
009B8379  48 8B CF                        mov rcx, rdi
009B837C  E8 8B 0A 00 00                  call 0x1409b8e0c
009B8381  B9 09 00 00 40                  mov ecx, 0x40000009
009B8386  8B D8                           mov ebx, eax
009B8388  3B C1                           cmp eax, ecx
009B838A  0F 84 D6 00 00 00               je 0x1409b8466
009B8390  85 C0                           test eax, eax
009B8392  0F 88 F6 00 00 00               js 0x1409b848e
009B8398  8B 87 A0 00 00 00               mov eax, dword ptr [rdi + 0xa0]
009B839E  0F BA E0 11                     bt eax, 0x11
009B83A2  0F 83 70 03 00 00               jae 0x1409b8718
009B83A8  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
009B83AC  44 21 B8 FC 0F 00 00            and dword ptr [rax + 0xffc], r15d
009B83B3  41 83 FE 04                     cmp r14d, 4
009B83B7  0F 85 99 00 00 00               jne 0x1409b8456
009B83BD  8B D9                           mov ebx, ecx
009B83BF  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
009B83C3  48 85 C9                        test rcx, rcx
009B83C6  74 05                           je 0x1409b83cd
009B83C8  E8 B3 D9 AB FF                  call 0x140475d80
009B83CD  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
009B83D1  48 85 C9                        test rcx, rcx
009B83D4  0F 85 42 02 00 00               jne 0x1409b861c
009B83DA  4D 85 ED                        test r13, r13
009B83DD  0F 85 57 03 00 00               jne 0x1409b873a
009B83E3  4D 85 FF                        test r15, r15
009B83E6  74 12                           je 0x1409b83fa
009B83E8  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
009B83EC  49 8B CF                        mov rcx, r15
009B83EF  8B 97 84 00 00 00               mov edx, dword ptr [rdi + 0x84]
009B83F5  E8 D6 26 D0 FF                  call 0x1406baad0
009B83FA  8B C3                           mov eax, ebx
009B83FC  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
009B8403  48 33 CC                        xor rcx, rsp
009B8406  E8 35 42 CF FF                  call 0x1406ac640
009B840B  48 8B 9C 24 D8 01 00 00         mov rbx, qword ptr [rsp + 0x1d8]
009B8413  48 81 C4 90 01 00 00            add rsp, 0x190
009B841A  41 5F                           pop r15
009B841C  41 5E                           pop r14
009B841E  41 5D                           pop r13
009B8420  41 5C                           pop r12
009B8422  5F                              pop rdi
009B8423  5E                              pop rsi
009B8424  5D                              pop rbp
009B8425  C3                              ret
009B8426  CC                              int3
009B8427  33 D2                           xor edx, edx
009B8429  48 8B CF                        mov rcx, rdi
009B842C  E8 D3 15 00 00                  call 0x1409b9a04
009B8431  85 C0                           test eax, eax
009B8433  0F 89 99 FD FF FF               jns 0x1409b81d2
009B8439  44 8B C8                        mov r9d, eax
009B843C  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
009B8444  45 8B C7                        mov r8d, r15d
009B8447  33 D2                           xor edx, edx
009B8449  48 8B CE                        mov rcx, rsi
009B844C  E8 03 6B AB FF                  call 0x14046ef54
009B8451  E9 7C FD FF FF                  jmp 0x1409b81d2
009B8456  45 84 E4                        test r12b, r12b
009B8459  0F 85 5E FF FF FF               jne 0x1409b83bd
009B845F  33 DB                           xor ebx, ebx
009B8461  E9 59 FF FF FF                  jmp 0x1409b83bf
009B8466  41 B4 01                        mov r12b, 1
009B8469  E9 2A FF FF FF                  jmp 0x1409b8398
009B846E  45 8B 48 28                     mov r9d, dword ptr [r8 + 0x28]
009B8472  48 8B CF                        mov rcx, rdi
009B8475  E8 AE 1B 00 00                  call 0x1409ba028
009B847A  8B D8                           mov ebx, eax
009B847C  85 C0                           test eax, eax
009B847E  0F 89 95 FE FF FF               jns 0x1409b8319
009B8484  C7 44 24 20 90 00 00 00         mov dword ptr [rsp + 0x20], 0x90
009B848C  EB 08                           jmp 0x1409b8496
009B848E  C7 44 24 20 C0 00 00 00         mov dword ptr [rsp + 0x20], 0xc0
009B8496  44 8B C8                        mov r9d, eax
009B8499  33 D2                           xor edx, edx
009B849B  41 B8 06 00 00 00               mov r8d, 6
009B84A1  48 8B CE                        mov rcx, rsi
009B84A4  E8 AB 6A AB FF                  call 0x14046ef54
009B84A9  E9 11 FF FF FF                  jmp 0x1409b83bf
009B84AE  44 39 AF A8 00 00 00            cmp dword ptr [rdi + 0xa8], r13d
009B84B5  0F 84 78 01 00 00               je 0x1409b8633
009B84BB  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
009B84C0  41 83 FE 05                     cmp r14d, 5
009B84C4  74 0F                           je 0x1409b84d5
009B84C6  41 83 FE 04                     cmp r14d, 4
009B84CA  0F 85 4A FD FF FF               jne 0x1409b821a
009B84D0  45 33 E4                        xor r12d, r12d
009B84D3  EB 04                           jmp 0x1409b84d9
009B84D5  45 8B 67 08                     mov r12d, dword ptr [r15 + 8]
009B84D9  44 39 8F A8 00 00 00            cmp dword ptr [rdi + 0xa8], r9d
009B84E0  0F 84 B8 00 00 00               je 0x1409b859e
009B84E6  8B DA                           mov ebx, edx
009B84E8  48 8D 45 AC                     lea rax, [rbp - 0x54]
009B84EC  B9 04 00 00 00                  mov ecx, 4
009B84F1  48 89 78 EC                     mov qword ptr [rax - 0x14], rdi
009B84F5  89 08                           mov dword ptr [rax], ecx
009B84F7  41 03 C9                        add ecx, r9d
009B84FA  48 8D 40 18                     lea rax, [rax + 0x18]
009B84FE  49 2B D1                        sub rdx, r9
009B8501  75 EE                           jne 0x1409b84f1
009B8503  48 8D 05 56 55 0B 00            lea rax, [rip + 0xb5556]
009B850A  C7 44 24 68 04 00 00 00         mov dword ptr [rsp + 0x68], 4
009B8512  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
009B8517  48 8D 4D 98                     lea rcx, [rbp - 0x68]
009B851B  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
009B851F  48 8D 45 B0                     lea rax, [rbp - 0x50]
009B8523  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
009B8527  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
009B852C  C7 45 80 05 00 00 00            mov dword ptr [rbp - 0x80], 5
009B8533  41 83 FE 04                     cmp r14d, 4
009B8537  0F 84 3F 01 00 00               je 0x1409b867c
009B853D  48 8D 45 D0                     lea rax, [rbp - 0x30]
009B8541  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
009B8546  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009B854B  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
009B8550  41 0F 94 C0                     sete r8b
009B8554  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
009B8558  41 8B D4                        mov edx, r12d
009B855B  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
009B8560  E8 37 15 00 00                  call 0x1409b9a9c
009B8565  8B D8                           mov ebx, eax
009B8567  85 C0                           test eax, eax
009B8569  78 5D                           js 0x1409b85c8
009B856B  41 B8 04 00 00 00               mov r8d, 4
009B8571  45 3B F0                        cmp r14d, r8d
009B8574  0F 84 38 01 00 00               je 0x1409b86b2
009B857A  83 3D D7 19 45 00 05            cmp dword ptr [rip + 0x4519d7], 5
009B8581  0F 87 FC 59 17 00               ja 0x140b2df83
009B8587  44 8A 64 24 40                  mov r12b, byte ptr [rsp + 0x40]
009B858C  E9 89 FC FF FF                  jmp 0x1409b821a
009B8591  C7 44 24 20 B0 00 00 00         mov dword ptr [rsp + 0x20], 0xb0
009B8599  E9 F8 FE FF FF                  jmp 0x1409b8496
009B859E  48 8D 05 BB 54 0B 00            lea rax, [rip + 0xb54bb]
009B85A5  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
009B85A9  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
009B85AE  41 8B D9                        mov ebx, r9d
009B85B1  48 8D 45 98                     lea rax, [rbp - 0x68]
009B85B5  44 89 4D AC                     mov dword ptr [rbp - 0x54], r9d
009B85B9  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009B85BE  44 89 4C 24 68                  mov dword ptr [rsp + 0x68], r9d
009B85C3  E9 6B FF FF FF                  jmp 0x1409b8533
009B85C8  C7 44 24 20 38 00 00 00         mov dword ptr [rsp + 0x20], 0x38
009B85D0  E9 C1 FE FF FF                  jmp 0x1409b8496
009B85D5  4C 8D 4D D0                     lea r9, [rbp - 0x30]
009B85D9  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
009B85DE  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
009B85E3  48 8B CF                        mov rcx, rdi
009B85E6  E8 A9 F3 FF FF                  call 0x1409b7994
009B85EB  8B D8                           mov ebx, eax
009B85ED  85 C0                           test eax, eax
009B85EF  0F 89 1B 01 00 00               jns 0x1409b8710
009B85F5  C7 44 24 20 A0 00 00 00         mov dword ptr [rsp + 0x20], 0xa0
009B85FD  E9 94 FE FF FF                  jmp 0x1409b8496
009B8602  C7 44 24 20 8C 00 00 00         mov dword ptr [rsp + 0x20], 0x8c
009B860A  E9 87 FE FF FF                  jmp 0x1409b8496
009B860F  C7 44 24 20 80 00 00 00         mov dword ptr [rsp + 0x20], 0x80
009B8617  E9 7A FE FF FF                  jmp 0x1409b8496
009B861C  E8 5F D7 AB FF                  call 0x140475d80
009B8621  E9 B4 FD FF FF                  jmp 0x1409b83da
009B8626  44 21 6C 24 20                  and dword ptr [rsp + 0x20], r13d
009B862B  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
009B8631  EB 0E                           jmp 0x1409b8641
009B8633  41 B9 4C 01 00 C0               mov r9d, 0xc000014c
009B8639  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
009B8641  41 8B D9                        mov ebx, r9d
009B8644  EB 10                           jmp 0x1409b8656
009B8646  BB 4D 01 00 C0                  mov ebx, 0xc000014d
009B864B  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
009B8653  44 8B CB                        mov r9d, ebx
009B8656  45 8B C7                        mov r8d, r15d
009B8659  33 D2                           xor edx, edx
009B865B  48 8B CE                        mov rcx, rsi
009B865E  E8 F1 68 AB FF                  call 0x14046ef54
009B8663  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
009B8668  E9 52 FD FF FF                  jmp 0x1409b83bf
009B866D  BB 5C 01 00 C0                  mov ebx, 0xc000015c
009B8672  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
009B867A  EB D7                           jmp 0x1409b8653
009B867C  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
009B8680  41 B8 43 4D 33 34               mov r8d, 0x34334d43
009B8686  41 8A D1                        mov dl, r9b
009B8689  B9 00 10 00 00                  mov ecx, 0x1000
009B868E  E8 3D 24 D0 FF                  call 0x1406baad0
009B8693  4C 8B E8                        mov r13, rax
009B8696  48 85 C0                        test rax, rax
009B8699  0F 85 DB 58 17 00               jne 0x140b2df7a
009B869F  41 B9 9A 00 00 C0               mov r9d, 0xc000009a
009B86A5  C7 44 24 20 30 00 00 00         mov dword ptr [rsp + 0x20], 0x30
009B86AD  E9 0B 5A 17 00                  jmp 0x140b2e0bd
009B86B2  66 83 8F D0 00 00 00 40         or word ptr [rdi + 0xd0], 0x40
009B86BA  4D 8B FD                        mov r15, r13
009B86BD  45 33 ED                        xor r13d, r13d
009B86C0  E9 B5 FE FF FF                  jmp 0x1409b857a
009B86C5  F7 44 24 60 00 00 02 00         test dword ptr [rsp + 0x60], 0x20000
009B86CD  0F 85 9C FB FF FF               jne 0x1409b826f
009B86D3  44 38 0D 28 F9 61 00            cmp byte ptr [rip + 0x61f928], r9b
009B86DA  0F 85 21 59 17 00               jne 0x140b2e001
009B86E0  8B 05 7A F5 53 00               mov eax, dword ptr [rip + 0x53f57a]
009B86E6  A8 06                           test al, 6
009B86E8  0F 84 81 FB FF FF               je 0x1409b826f
009B86EE  E9 0E 59 17 00                  jmp 0x140b2e001
009B86F3  C7 44 24 20 84 00 00 00         mov dword ptr [rsp + 0x20], 0x84
009B86FB  E9 96 FD FF FF                  jmp 0x1409b8496
009B8700  C7 44 24 20 88 00 00 00         mov dword ptr [rsp + 0x20], 0x88
009B8708  44 8B C8                        mov r9d, eax
009B870B  E9 8B FD FF FF                  jmp 0x1409b849b
009B8710  41 B4 01                        mov r12b, 1
009B8713  E9 3E FC FF FF                  jmp 0x1409b8356
009B8718  0F BA E8 10                     bts eax, 0x10
009B871C  89 87 A0 00 00 00               mov dword ptr [rdi + 0xa0], eax
009B8722  E9 81 FC FF FF                  jmp 0x1409b83a8
009B8727  41 B9 4C 01 00 C0               mov r9d, 0xc000014c
009B872D  C7 44 24 20 70 00 00 00         mov dword ptr [rsp + 0x20], 0x70
009B8735  E9 83 59 17 00                  jmp 0x140b2e0bd
009B873A  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
009B873E  49 8B CD                        mov rcx, r13
009B8741  8B 97 84 00 00 00               mov edx, dword ptr [rdi + 0x84]
009B8747  E8 84 23 D0 FF                  call 0x1406baad0
009B874C  E9 92 FC FF FF                  jmp 0x1409b83e3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvLoadHive(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m11C;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int8 v_stack_m188;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_mBC;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 4531682)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m168 = a3;
    v_r13 = 0;
    v_r12 = 0;
    a2 = 0;
    v_stack_m188 = 0;
    v_stack_m160 = v_xmm0;
    v_stack_m150 = v_xmm0;
    v_stack_m140 = v_xmm0;
    v_stack_m130 = v_xmm1;
    v_stack_m120 = v_xmm1;
    v_stack_m110 = v_xmm1;
    result = memset(v_stack_mF8, a2, v_r13 + 92, a4);
    if (((*(unsigned int *)(a1 + 160)) & (0x8001ULL)) == 0) goto loc_009B8427;
loc_009B81D2:
    result = HvpGetHiveHeader(a1, v_stack_m180, v_stack_m170, a4);
    if (((unsigned int)(result)) == 2) goto loc_009B8626;
    if (((unsigned int)(result)) == 7) goto loc_009B8646;
    if ((unsigned int)(result) == 0) goto loc_009B866D;
    result = (unsigned int)((result) + (-4));
    if (((unsigned int)(result)) <= ((unsigned int)(2 - 1))) goto loc_009B84AE;
loc_009B821A:
    *(unsigned __int64 *)(a1 + 64) = v_stack_m180;
    v_r15 = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m180 + 20))) << (12));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m180 + 24))) + (0xFFFFF000ULL));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    *(unsigned int *)(a1 + 220) = (unsigned int)(a1);
    result = CmpInitializeActualFileSizes(a1, v_stack_m178, v_stack_m170, 2 - 1);
    a4 = 0;
    if (sign_flag) goto loc_009B860F;
    if (((unsigned int)((unsigned int)(v_stack_m178))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 40)) + 4096))) goto loc_009B86C5;
loc_009B826F:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 40))) - 1);
    if (((unsigned int)(a1)) > 0x7FFFDFFFULL) goto loc_009B8727;
    result = HvpInitMap(a1, v_stack_m178, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 40)), a4);
    if (sign_flag) goto loc_009B86F3;
    if (condition_is_above_or_equal) goto loc_009B846E;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 160))))) >> (22));
    a1 = (unsigned int)((a1) & (2));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (8));
    if (condition_is_above_or_equal) { a2 = (unsigned int)(a1); }
    result = (unsigned int)(((unsigned int)(a2)) | (1));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 160)))) & (0x8001ULL)) == 0) { result = a2; }
    v_stack_m1A8 = (unsigned int)(result);
    result = HvpViewMapStart(a1 + 224, *(unsigned __int64 *)(a1 + 1544), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 40)), v_rip + 5500704);
    a2 = 0;
    if (sign_flag) goto loc_009B8700;
    result = HvpMapHiveImageFromViewMap(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 40)), v_rip + 5500704);
    if (sign_flag) goto loc_009B8602;
loc_009B8319:
    result = CmpTraceHiveMountBaseFileMounted(*(unsigned __int64 *)(a1 + 1544), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 40)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 40)), v_rip + 5500704);
    if (v_stack_mBC > 0) goto loc_009B85D5;
    *(unsigned int *)(a1 + 172) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 4)));
    *(unsigned int *)(a1 + 184) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 4)));
    *(unsigned int *)(a1 + 176) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 4)));
    *(unsigned __int8 *)(a1 + 194) = 1;
loc_009B8356:
    a3 = 0;
    result = HvpAdjustHiveFreeDisplay(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 40)), a3, v_rip + 5500704);
    if (sign_flag) goto loc_009B8591;
    result = HvpRemapAndEnlistHiveBins(a1, (unsigned int)(v_stack_m168), 0, v_rip + 5500704);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x40000009ULL)))) goto loc_009B8466;
    if (sign_flag) goto loc_009B848E;
loc_009B8398:
    if (condition_is_above_or_equal) goto loc_009B8718;
loc_009B83A8:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 4) goto loc_009B8456;
loc_009B83BD:
loc_009B83BF:
    result = *(unsigned __int64 *)(a1 + 64);
    if (v_stack_m128 != 0) {
        result = CmSiFreeMemory(v_stack_m128, (unsigned int)(v_stack_m168), 0, v_rip + 5500704);
    }
    if (v_stack_m110 != 0) goto loc_009B861C;
loc_009B83DA:
    if (0 != 0) goto loc_009B873A;
loc_009B83E3:
    if (0 != 0) {
        result = *(unsigned __int64 *)(a1 + 32);
        a1 = 0;
        a2 = *(unsigned int *)(a1 + 132);
        result = guard_dispatch_icall(a1, a2, 0, v_rip + 5500704);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 0, v_rip + 5500704);
    v_rsp = (v_rsp) + (400);
    return result;
loc_009B8427:
    a2 = 0;
    result = CmpFileFlush(a1, a2, 0, v_rip + 5500704);
    if (!sign_flag) goto loc_009B81D2;
    v_stack_p20 = 8;
    a2 = 0;
    result = SetFailureLocation(0, a2, 0, (unsigned int)((unsigned int)(result)));
    goto loc_009B81D2;
loc_009B8456:
    if (0 != 0) goto loc_009B83BD;
    v_rbx = 0;
    goto loc_009B83BF;
loc_009B8466:
    goto loc_009B8398;
loc_009B846E:
    result = HvpMapHiveImageFromFile(a1, a2, 0, (unsigned int)(*(unsigned int *)(0 + 40)));
    if (!sign_flag) goto loc_009B8319;
    v_stack_p20 = 144;
    goto loc_009B8496;
loc_009B848E:
    v_stack_p20 = 192;
loc_009B8496:
    a2 = 0;
loc_009B849B:
    result = SetFailureLocation(0, a2, 6, (unsigned int)((unsigned int)(result)));
    goto loc_009B83BF;
loc_009B84AE:
    if ((*(unsigned int *)(a1 + 168)) == 0) goto loc_009B8633;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 5) goto loc_009B84D5;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 4) goto loc_009B821A;
    v_r12 = 0;
    goto loc_009B84D9;
loc_009B84D5:
loc_009B84D9:
    if ((*(unsigned int *)(a1 + 168)) == ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_009B859E;
loc_009B84F1:
    *(unsigned __int64 *)(v_stack_m11C - 20) = a1;
    *(unsigned int *)(v_stack_m11C) = 4;
    a1 = (unsigned int)((4) + ((unsigned int)((unsigned int)((unsigned int)(result)))));
    a2 = (a2) - ((unsigned int)((unsigned int)(result)));
    if (condition_is_not_equal) goto loc_009B84F1;
    v_stack_p68 = 4;
    v_stack_p70 = v_rip + 742742;
    v_stack_m140 = v_rip + 742742;
    v_stack_m138 = v_stack_m118;
    v_stack_p78 = v_stack_m130;
    v_stack_m148 = 5;
loc_009B8533:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 4) goto loc_009B867C;
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_mF8;
    a3 = (((unsigned int)((unsigned int)((unsigned int)(result)))) == 4) ? 1 : 0;
    v_stack_p20 = 0;
    result = HvAnalyzeLogFiles(v_stack_p58, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 8)))), a3, v_stack_p68);
    if (sign_flag) goto loc_009B85C8;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 4) goto loc_009B86B2;
loc_009B857A:
    goto loc_009B821A;
loc_009B8591:
    v_stack_p20 = 176;
    goto loc_009B8496;
loc_009B859E:
    v_stack_m130 = a1;
    v_stack_p70 = v_rip + 742587;
    v_stack_m11C = (unsigned int)(v_stack_p68);
    v_stack_p78 = v_stack_m130;
    v_stack_p68 = (unsigned int)(v_stack_p68);
    goto loc_009B8533;
loc_009B85C8:
    v_stack_p20 = 56;
    goto loc_009B8496;
loc_009B85D5:
    v_stack_p20 = 0;
    result = HvpPerformLogFileRecovery(a1, v_stack_p68, 4, v_stack_mF8);
    if (!sign_flag) goto loc_009B8710;
    v_stack_p20 = 160;
    goto loc_009B8496;
loc_009B8602:
    v_stack_p20 = 140;
    goto loc_009B8496;
loc_009B860F:
    v_stack_p20 = 128;
    goto loc_009B8496;
loc_009B861C:
    result = CmSiFreeMemory(a1, v_stack_p68, 4, v_stack_mF8);
    goto loc_009B83DA;
loc_009B8626:
    goto loc_009B8641;
loc_009B8633:
    v_stack_p20 = 32;
loc_009B8641:
    goto loc_009B8656;
loc_009B8646:
    v_stack_p20 = 8;
loc_009B8653:
loc_009B8656:
    a2 = 0;
    result = SetFailureLocation(0, a2, (unsigned int)((unsigned int)(v_stack_p48)), (unsigned int)((unsigned int)((unsigned int)(0xC000014DULL))));
    goto loc_009B83BF;
loc_009B866D:
    v_stack_p20 = 16;
    goto loc_009B8653;
loc_009B867C:
    result = guard_dispatch_icall((unsigned int)(0x1000ULL), (unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0xC000014DULL)))), (unsigned int)(0x34334D43ULL), (unsigned int)((unsigned int)((unsigned int)(0xC000014DULL))));
    v_stack_p20 = 48;
loc_009B86B2:
    v_r13 = 0;
    goto loc_009B857A;
loc_009B86C5:
    if (((v_stack_p60) & (0x20000ULL)) != 0) goto loc_009B826F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5502330)))) & (6)) == 0) goto loc_009B826F;
loc_009B86F3:
    v_stack_p20 = 132;
    goto loc_009B8496;
loc_009B8700:
    v_stack_p20 = 136;
    goto loc_009B849B;
loc_009B8710:
    goto loc_009B8356;
loc_009B8718:
    *(unsigned int *)(a1 + 160) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5502330)));
    goto loc_009B83A8;
loc_009B8727:
    v_stack_p20 = 112;
loc_009B873A:
    result = guard_dispatch_icall(0, (unsigned int)(*(unsigned int *)(a1 + 132)), (unsigned int)(0x34334D43ULL), (unsigned int)(0xC000014CULL));
    goto loc_009B83E3;
}
```

## 5. (Beta) C Style

```c
int64_t HvLoadHive(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m11C;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m160;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint8_t v_stack_m188;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m48;
    uint32_t v_stack_mBC;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0x4525E2)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m168 = Arg3;
    local_r13 = 0;
    local_r12 = 0;
    Arg2 = 0;
    v_stack_m188 = 0;
    v_stack_m160 = v_xmm0;
    v_stack_m150 = v_xmm0;
    v_stack_m140 = v_xmm0;
    v_stack_m130 = v_xmm1;
    v_stack_m120 = v_xmm1;
    v_stack_m110 = v_xmm1;
    result = memset(v_stack_mF8, Arg2, local_r13 + 92, Arg4);
    if (((*(uint32_t *)(arg1 + 0xA0)) & (0x8001ULL)) == 0) goto loc_009B8427;
loc_009B81D2:
    result = HvpGetHiveHeader(Arg1, v_stack_m180, v_stack_m170, Arg4);
    if (((uint32_t)(result)) == 2) goto loc_009B8626;
    if (((uint32_t)(result)) == 7) goto loc_009B8646;
    if ((uint32_t)(result) == 0) goto loc_009B866D;
    result = (uint32_t)((result) + (-4));
    if (((uint32_t)(result)) <= ((uint32_t)(2 - 1))) goto loc_009B84AE;
loc_009B821A:
    *(uint64_t *)(arg1 + 0x40) = v_stack_m180;
    local_r15 = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m180 + 0x14))) << (12));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m180 + 0x18))) + (0xFFFFF000ULL));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    *(uint32_t *)(arg1 + 0xDC) = (uint32_t)(Arg1);
    result = CmpInitializeActualFileSizes(Arg1, v_stack_m178, v_stack_m170, 2 - 1);
    Arg4 = 0;
    if (sign_flag) goto loc_009B860F;
    if (((uint32_t)((uint32_t)(v_stack_m178))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x28)) + 4096))) goto loc_009B86C5;
loc_009B826F:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x28))) - 1);
    if (((uint32_t)(Arg1)) > 0x7FFFDFFFULL) goto loc_009B8727;
    result = HvpInitMap(Arg1, v_stack_m178, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x28)), Arg4);
    if (sign_flag) goto loc_009B86F3;
    if (condition_is_above_or_equal) goto loc_009B846E;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA0))))) >> (22));
    Arg1 = (uint32_t)((Arg1) & (2));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (8));
    if (condition_is_above_or_equal) { Arg2 = (uint32_t)(Arg1); }
    result = (uint32_t)(((uint32_t)(Arg2)) | (1));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA0)))) & (0x8001ULL)) == 0) { result = Arg2; }
    v_stack_m1A8 = (uint32_t)(result);
    result = HvpViewMapStart(Arg1 + 224, *(uint64_t *)(arg1 + 0x608), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x28)), v_rip + 5500704);
    Arg2 = 0;
    if (sign_flag) goto loc_009B8700;
    result = HvpMapHiveImageFromViewMap(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x28)), v_rip + 5500704);
    if (sign_flag) goto loc_009B8602;
loc_009B8319:
    result = CmpTraceHiveMountBaseFileMounted(*(uint64_t *)(arg1 + 0x608), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x28)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x28)), v_rip + 5500704);
    if (v_stack_mBC > 0) goto loc_009B85D5;
    *(uint32_t *)(arg1 + 0xAC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x4)));
    *(uint32_t *)(arg1 + 0xB8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x4)));
    *(uint32_t *)(arg1 + 0xB0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x4)));
    *(uint8_t *)(arg1 + 0xC2) = 1;
loc_009B8356:
    Arg3 = 0;
    result = HvpAdjustHiveFreeDisplay(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x28)), Arg3, v_rip + 5500704);
    if (sign_flag) goto loc_009B8591;
    result = HvpRemapAndEnlistHiveBins(Arg1, (uint32_t)(v_stack_m168), 0, v_rip + 5500704);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x40000009ULL)))) goto loc_009B8466;
    if (sign_flag) goto loc_009B848E;
loc_009B8398:
    if (condition_is_above_or_equal) goto loc_009B8718;
loc_009B83A8:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 4) goto loc_009B8456;
loc_009B83BD:
loc_009B83BF:
    result = *(uint64_t *)(arg1 + 0x40);
    if (v_stack_m128 != 0) {
        result = CmSiFreeMemory(v_stack_m128, (uint32_t)(v_stack_m168), 0, v_rip + 5500704);
    }
    if (v_stack_m110 != 0) goto loc_009B861C;
loc_009B83DA:
    if (0 != 0) goto loc_009B873A;
loc_009B83E3:
    if (0 != 0) {
        result = *(uint64_t *)(arg1 + 0x20);
        Arg1 = 0;
        Arg2 = *(uint32_t *)(arg1 + 0x84);
        result = guard_dispatch_icall(Arg1, Arg2, 0, v_rip + 5500704);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 0, v_rip + 5500704);
    local_rsp = (local_rsp) + (400);
    return result;
loc_009B8427:
    Arg2 = 0;
    result = CmpFileFlush(Arg1, Arg2, 0, v_rip + 5500704);
    if (!sign_flag) goto loc_009B81D2;
    v_stack_p20 = 8;
    Arg2 = 0;
    result = SetFailureLocation(0, Arg2, 0, (uint32_t)((uint32_t)(result)));
    goto loc_009B81D2;
loc_009B8456:
    if (0 != 0) goto loc_009B83BD;
    local_rbx = 0;
    goto loc_009B83BF;
loc_009B8466:
    goto loc_009B8398;
loc_009B846E:
    result = HvpMapHiveImageFromFile(Arg1, Arg2, 0, (uint32_t)(*(uint32_t *)(0 + 0x28)));
    if (!sign_flag) goto loc_009B8319;
    v_stack_p20 = 144;
    goto loc_009B8496;
loc_009B848E:
    v_stack_p20 = 192;
loc_009B8496:
    Arg2 = 0;
loc_009B849B:
    result = SetFailureLocation(0, Arg2, 6, (uint32_t)((uint32_t)(result)));
    goto loc_009B83BF;
loc_009B84AE:
    if ((*(uint32_t *)(arg1 + 0xA8)) == 0) goto loc_009B8633;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 5) goto loc_009B84D5;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 4) goto loc_009B821A;
    local_r12 = 0;
    goto loc_009B84D9;
loc_009B84D5:
loc_009B84D9:
    if ((*(uint32_t *)(arg1 + 0xA8)) == ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_009B859E;
loc_009B84F1:
    *(void **)(v_stack_m11C - 0x14) = Arg1;
    *(uint32_t *)(v_stack_m11C) = 4;
    Arg1 = (uint32_t)((4) + ((uint32_t)((uint32_t)((uint32_t)(result)))));
    Arg2 = (Arg2) - ((uint32_t)((uint32_t)(result)));
    if (condition_is_not_equal) goto loc_009B84F1;
    v_stack_p68 = 4;
    v_stack_p70 = v_rip + 742742;
    v_stack_m140 = v_rip + 742742;
    v_stack_m138 = v_stack_m118;
    v_stack_p78 = v_stack_m130;
    v_stack_m148 = 5;
loc_009B8533:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 4) goto loc_009B867C;
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_mF8;
    Arg3 = (((uint32_t)((uint32_t)((uint32_t)(result)))) == 4) ? 1 : 0;
    v_stack_p20 = 0;
    result = HvAnalyzeLogFiles(v_stack_p58, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x8)))), Arg3, v_stack_p68);
    if (sign_flag) goto loc_009B85C8;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 4) goto loc_009B86B2;
loc_009B857A:
    goto loc_009B821A;
loc_009B8591:
    v_stack_p20 = 176;
    goto loc_009B8496;
loc_009B859E:
    v_stack_m130 = Arg1;
    v_stack_p70 = v_rip + 742587;
    v_stack_m11C = (uint32_t)(v_stack_p68);
    v_stack_p78 = v_stack_m130;
    v_stack_p68 = (uint32_t)(v_stack_p68);
    goto loc_009B8533;
loc_009B85C8:
    v_stack_p20 = 56;
    goto loc_009B8496;
loc_009B85D5:
    v_stack_p20 = 0;
    result = HvpPerformLogFileRecovery(Arg1, v_stack_p68, 4, v_stack_mF8);
    if (!sign_flag) goto loc_009B8710;
    v_stack_p20 = 160;
    goto loc_009B8496;
loc_009B8602:
    v_stack_p20 = 140;
    goto loc_009B8496;
loc_009B860F:
    v_stack_p20 = 128;
    goto loc_009B8496;
loc_009B861C:
    result = CmSiFreeMemory(Arg1, v_stack_p68, 4, v_stack_mF8);
    goto loc_009B83DA;
loc_009B8626:
    goto loc_009B8641;
loc_009B8633:
    v_stack_p20 = 32;
loc_009B8641:
    goto loc_009B8656;
loc_009B8646:
    v_stack_p20 = 8;
loc_009B8653:
loc_009B8656:
    Arg2 = 0;
    result = SetFailureLocation(0, Arg2, (uint32_t)((uint32_t)(v_stack_p48)), (uint32_t)((uint32_t)((uint32_t)(0xC000014DULL))));
    goto loc_009B83BF;
loc_009B866D:
    v_stack_p20 = 16;
    goto loc_009B8653;
loc_009B867C:
    result = guard_dispatch_icall((uint32_t)(0x1000ULL), (uint8_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014DULL)))), (uint32_t)(0x34334D43ULL), (uint32_t)((uint32_t)((uint32_t)(0xC000014DULL))));
    v_stack_p20 = 48;
loc_009B86B2:
    local_r13 = 0;
    goto loc_009B857A;
loc_009B86C5:
    if (((v_stack_p60) & (0x20000ULL)) != 0) goto loc_009B826F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x53F57A)))) & (6)) == 0) goto loc_009B826F;
loc_009B86F3:
    v_stack_p20 = 132;
    goto loc_009B8496;
loc_009B8700:
    v_stack_p20 = 136;
    goto loc_009B849B;
loc_009B8710:
    goto loc_009B8356;
loc_009B8718:
    *(uint32_t *)(arg1 + 0xA0) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x53F57A)));
    goto loc_009B83A8;
loc_009B8727:
    v_stack_p20 = 112;
loc_009B873A:
    result = guard_dispatch_icall(0, (uint32_t)(*(uint32_t *)(arg1 + 0x84)), (uint32_t)(0x34334D43ULL), (uint32_t)(0xC000014CULL));
    goto loc_009B83E3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x84` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `32` | `W` |
| `Arg1` | `+ 0xA8` | `32` | `R` |
| `Arg1` | `+ 0xAC` | `32` | `W` |
| `Arg1` | `+ 0xB0` | `32` | `W` |
| `Arg1` | `+ 0xB8` | `32` | `W` |
| `Arg1` | `+ 0xC2` | `8` | `W` |
| `Arg1` | `+ 0xD0` | `16` | `R/W` |
| `Arg1` | `+ 0xDC` | `32` | `W` |
| `Arg1` | `+ 0xE0` | `64` | `R` |
| `Arg1` | `+ 0x608` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009B8138&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
