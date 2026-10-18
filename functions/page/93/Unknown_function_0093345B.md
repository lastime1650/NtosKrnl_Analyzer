# sub_0093345B

- RVA: `0x0093345B`–`0x0093389E` (길이 `1,091` bytes)
- VA: `0x000000014093345B`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008EFCC`
- 디코드: `283`개 명령, `1,091/1,091` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00933525` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00933540` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (function, `0x003FEF30`)
- `0x00933576` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x00933584` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x009335C9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009335DE` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x009336A1` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x009336D5` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x009337A9` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00933854` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00933870` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00933878` → [VrpUnlockJobContextShared](VrpUnlockJobContextShared_function_009345D8.md) (function, `0x009345D8`)
- `0x0093388A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0093356A` → RVA `0x00AFC990` (` ?? ::NNGAKEGL::`string'`; read)
- `0x009336B0` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x00933525` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00933540` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (`PAGE` → `.text`)
  - `0x00933576` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x00933584` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x009335C9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009335DE` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x009336A1` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x009337A9` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00933854` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00933870` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0093388A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00933532` → [sub_009338D4 + 0xA](Unknown_function_009338D4.md) (`tail-transfer`)
  - `0x009336AA` → [sub_009330DC + 0x2E8](Unknown_function_009330DC.md) (`tail-transfer`)
  - `0x009336E2` → [sub_009330DC + 0x2E5](Unknown_function_009330DC.md) (`tail-transfer`)
  - `0x009337B4` → [sub_009330DC + 0x2E8](Unknown_function_009330DC.md) (`tail-transfer`)
  - `0x00933863` → [sub_009330DC + 0x2E5](Unknown_function_009330DC.md) (`tail-transfer`)
  - `0x00933899` → [sub_009330DC + 0x68](Unknown_function_009330DC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0093345B  48 8B CE                        mov rcx, rsi
0093345E  4D 85 C9                        test r9, r9
00933461  74 59                           je 0x1409334bc
00933463  41 0F B7 D7                     movzx edx, r15w
00933467  48 8D 04 09                     lea rax, [rcx + rcx]
0093346B  48 3B C2                        cmp rax, rdx
0093346E  73 0C                           jae 0x14093347c
00933470  66 41 83 3C 04 5C               cmp word ptr [r12 + rax], 0x5c
00933476  0F 84 C9 02 00 00               je 0x140933745
0093347C  48 8D 04 09                     lea rax, [rcx + rcx]
00933480  48 3B C2                        cmp rax, rdx
00933483  73 14                           jae 0x140933499
00933485  66 41 83 3C 04 5C               cmp word ptr [r12 + rax], 0x5c
0093348B  74 0C                           je 0x140933499
0093348D  48 FF C1                        inc rcx
00933490  48 8D 04 09                     lea rax, [rcx + rcx]
00933494  48 3B C2                        cmp rax, rdx
00933497  72 EC                           jb 0x140933485
00933499  48 8D 04 09                     lea rax, [rcx + rcx]
0093349D  48 3B C2                        cmp rax, rdx
009334A0  73 14                           jae 0x1409334b6
009334A2  66 41 83 3C 04 5C               cmp word ptr [r12 + rax], 0x5c
009334A8  75 0C                           jne 0x1409334b6
009334AA  48 FF C1                        inc rcx
009334AD  48 8D 04 09                     lea rax, [rcx + rcx]
009334B1  48 3B C2                        cmp rax, rdx
009334B4  72 EC                           jb 0x1409334a2
009334B6  49 83 E9 01                     sub r9, 1
009334BA  75 AB                           jne 0x140933467
009334BC  0F B7 C1                        movzx eax, cx
009334BF  49 8D 3C 4C                     lea rdi, [r12 + rcx*2]
009334C3  33 C9                           xor ecx, ecx
009334C5  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
009334C9  66 03 C0                        add ax, ax
009334CC  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
009334D0  66 44 2B F8                     sub r15w, ax
009334D4  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
009334D8  49 8D 75 18                     lea rsi, [r13 + 0x18]
009334DC  66 89 4C 24 50                  mov word ptr [rsp + 0x50], cx
009334E1  48 85 F6                        test rsi, rsi
009334E4  66 44 89 7D B0                  mov word ptr [rbp - 0x50], r15w
009334E9  48 8D 5D A0                     lea rbx, [rbp - 0x60]
009334ED  66 44 89 7D B2                  mov word ptr [rbp - 0x4e], r15w
009334F2  48 0F 45 DE                     cmovne rbx, rsi
009334F6  0F B7 03                        movzx eax, word ptr [rbx]
009334F9  41 8D 0C 07                     lea ecx, [r15 + rax]
009334FD  66 3B C8                        cmp cx, ax
00933500  0F 82 58 03 00 00               jb 0x14093385e
00933506  8D 41 02                        lea eax, [rcx + 2]
00933509  66 3B C1                        cmp ax, cx
0093350C  0F 82 4C 03 00 00               jb 0x14093385e
00933512  0F B7 D0                        movzx edx, ax
00933515  B9 00 01 00 00                  mov ecx, 0x100
0093351A  41 B8 56 52 65 67               mov r8d, 0x67655256
00933520  66 89 44 24 52                  mov word ptr [rsp + 0x52], ax
00933525  E8 C6 EB 24 00                  call 0x140b820f0
0093352A  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0093352F  48 85 C0                        test rax, rax
00933532  0F 84 A6 03 00 00               je 0x1409338de
00933538  48 8B D3                        mov rdx, rbx
0093353B  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00933540  E8 EB B9 AC FF                  call 0x1403fef30
00933545  66 45 85 FF                     test r15w, r15w
00933549  74 3E                           je 0x140933589
0093354B  66 83 3F 5C                     cmp word ptr [rdi], 0x5c
0093354F  74 2A                           je 0x14093357b
00933551  0F B7 03                        movzx eax, word ptr [rbx]
00933554  66 85 C0                        test ax, ax
00933557  74 11                           je 0x14093356a
00933559  8B C8                           mov ecx, eax
0093355B  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0093355F  48 D1 E9                        shr rcx, 1
00933562  66 83 7C 48 FE 5C               cmp word ptr [rax + rcx*2 - 2], 0x5c
00933568  74 11                           je 0x14093357b
0093356A  48 8D 15 1F 94 1C 00            lea rdx, [rip + 0x1c941f]
00933571  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00933576  E8 15 C4 AD FF                  call 0x14040f990
0093357B  48 8D 55 B0                     lea rdx, [rbp - 0x50]
0093357F  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00933584  E8 C7 C4 AD FF                  call 0x14040fa50
00933589  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
0093358E  8B C2                           mov eax, edx
00933590  48 D1 E8                        shr rax, 1
00933593  48 83 E8 01                     sub rax, 1
00933597  78 21                           js 0x1409335ba
00933599  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0093359E  41 BE FE FF 00 00               mov r14d, 0xfffe
009335A4  66 41 83 3C 40 5C               cmp word ptr [r8 + rax*2], 0x5c
009335AA  0F 84 8A 02 00 00               je 0x14093383a
009335B0  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009335B5  66 89 54 24 50                  mov word ptr [rsp + 0x50], dx
009335BA  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
009335BE  4C 3B 60 08                     cmp r12, qword ptr [rax + 8]
009335C2  74 0A                           je 0x1409335ce
009335C4  33 D2                           xor edx, edx
009335C6  49 8B CC                        mov rcx, r12
009335C9  E8 A2 F2 24 00                  call 0x140b82870
009335CE  0F 28 74 24 50                  movaps xmm6, xmmword ptr [rsp + 0x50]
009335D3  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
009335D8  33 D2                           xor edx, edx
009335DA  0F 29 75 90                     movaps xmmword ptr [rbp - 0x70], xmm6
009335DE  E8 9D 71 AF FF                  call 0x14042a780
009335E3  41 8B 4D 38                     mov ecx, dword ptr [r13 + 0x38]
009335E7  8B C1                           mov eax, ecx
009335E9  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
009335EE  83 E0 04                        and eax, 4
009335F1  48 8B 7D 60                     mov rdi, qword ptr [rbp + 0x60]
009335F5  44 0B E0                        or r12d, eax
009335F8  4C 3B F7                        cmp r14, rdi
009335FB  75 06                           jne 0x140933603
009335FD  83 E1 02                        and ecx, 2
00933600  44 0B E1                        or r12d, ecx
00933603  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
00933608  41 8B C4                        mov eax, r12d
0093360B  41 0F B7 4D 40                  movzx ecx, word ptr [r13 + 0x40]
00933610  0F BA E8 1D                     bts eax, 0x1d
00933614  49 8B 5D 10                     mov rbx, qword ptr [r13 + 0x10]
00933618  66 45 85 FF                     test r15w, r15w
0093361C  44 8B 7C 24 38                  mov r15d, dword ptr [rsp + 0x38]
00933621  41 0F 45 C4                     cmovne eax, r12d
00933625  45 0F B6 FF                     movzx r15d, r15b
00933629  44 8B E0                        mov r12d, eax
0093362C  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00933630  44 3B C1                        cmp r8d, ecx
00933633  B8 01 00 00 00                  mov eax, 1
00933638  44 0F 4C F8                     cmovl r15d, eax
0093363C  41 0F B7 45 42                  movzx eax, word ptr [r13 + 0x42]
00933641  2B C1                           sub eax, ecx
00933643  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
00933648  44 03 C0                        add r8d, eax
0093364B  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
00933650  48 85 DB                        test rbx, rbx
00933653  0F 85 0F 02 00 00               jne 0x140933868
00933659  48 8B BD 88 00 00 00            mov rdi, qword ptr [rbp + 0x88]
00933660  48 85 FF                        test rdi, rdi
00933663  0F 84 8C 00 00 00               je 0x1409336f5
00933669  45 84 FF                        test r15b, r15b
0093366C  0F 84 DB 01 00 00               je 0x14093384d
00933672  0F 57 C0                        xorps xmm0, xmm0
00933675  C7 45 D0 30 00 00 00            mov dword ptr [rbp - 0x30], 0x30
0093367C  45 33 E4                        xor r12d, r12d
0093367F  C7 45 E8 40 02 00 00            mov dword ptr [rbp - 0x18], 0x240
00933686  4C 8D 45 D0                     lea r8, [rbp - 0x30]
0093368A  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
0093368E  BA 00 00 00 80                  mov edx, 0x80000000
00933693  48 89 75 E0                     mov qword ptr [rbp - 0x20], rsi
00933697  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0093369C  F3 0F 7F 45 F0                  movdqu xmmword ptr [rbp - 0x10], xmm0
009336A1  E8 6A 9C D7 FF                  call 0x1406ad310
009336A6  8B D8                           mov ebx, eax
009336A8  85 C0                           test eax, eax
009336AA  0F 88 14 FD FF FF               js 0x1409333c4
009336B0  4C 8B 05 09 34 69 00            mov r8, qword ptr [rip + 0x693409]
009336B7  33 C0                           xor eax, eax
009336B9  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
009336BE  45 33 C9                        xor r9d, r9d
009336C1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009336C6  33 D2                           xor edx, edx
009336C8  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
009336CC  48 8D 45 88                     lea rax, [rbp - 0x78]
009336D0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009336D5  E8 D6 56 F3 FF                  call 0x140868db0
009336DA  4C 8B 65 88                     mov r12, qword ptr [rbp - 0x78]
009336DE  8B D8                           mov ebx, eax
009336E0  85 C0                           test eax, eax
009336E2  0F 88 D9 FC FF FF               js 0x1409333c1
009336E8  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
009336ED  4C 89 27                        mov qword ptr [rdi], r12
009336F0  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
009336F5  4C 8B 95 90 00 00 00            mov r10, qword ptr [rbp + 0x90]
009336FC  4D 85 D2                        test r10, r10
009336FF  74 7C                           je 0x14093377d
00933701  66 41 0F 7E F1                  movd r9d, xmm6
00933706  66 0F 6F C6                     movdqa xmm0, xmm6
0093370A  66 0F 73 D8 08                  psrldq xmm0, 8
0093370F  66 48 0F 7E C2                  movq rdx, xmm0
00933714  45 84 FF                        test r15b, r15b
00933717  0F 84 9C 00 00 00               je 0x1409337b9
0093371D  0F B7 0E                        movzx ecx, word ptr [rsi]
00933720  48 D1 E9                        shr rcx, 1
00933723  45 0F B7 C1                     movzx r8d, r9w
00933727  48 8D 04 09                     lea rax, [rcx + rcx]
0093372B  49 3B C0                        cmp rax, r8
0093372E  73 32                           jae 0x140933762
00933730  66 83 3C 10 5C                  cmp word ptr [rax + rdx], 0x5c
00933735  75 2B                           jne 0x140933762
00933737  48 FF C1                        inc rcx
0093373A  48 8D 04 09                     lea rax, [rcx + rcx]
0093373E  49 3B C0                        cmp rax, r8
00933741  72 ED                           jb 0x140933730
00933743  EB 1D                           jmp 0x140933762
00933745  48 FF C1                        inc rcx
00933748  48 8D 04 09                     lea rax, [rcx + rcx]
0093374C  48 3B C2                        cmp rax, rdx
0093374F  0F 82 1B FD FF FF               jb 0x140933470
00933755  E9 22 FD FF FF                  jmp 0x14093347c
0093375A  49 FF C3                        inc r11
0093375D  44 3B DB                        cmp r11d, ebx
00933760  7C 6E                           jl 0x1409337d0
00933762  0F B7 C1                        movzx eax, cx
00933765  66 03 C0                        add ax, ax
00933768  66 44 2B C8                     sub r9w, ax
0093376C  48 8D 04 4A                     lea rax, [rdx + rcx*2]
00933770  49 89 42 08                     mov qword ptr [r10 + 8], rax
00933774  66 45 89 0A                     mov word ptr [r10], r9w
00933778  66 45 89 4A 02                  mov word ptr [r10 + 2], r9w
0093377D  48 8B 85 98 00 00 00            mov rax, qword ptr [rbp + 0x98]
00933784  48 85 C0                        test rax, rax
00933787  74 03                           je 0x14093378c
00933789  44 89 20                        mov dword ptr [rax], r12d
0093378C  41 8B 4D 3C                     mov ecx, dword ptr [r13 + 0x3c]
00933790  33 D2                           xor edx, edx
00933792  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
00933799  89 08                           mov dword ptr [rax], ecx
0093379B  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0093379F  48 8B 85 80 00 00 00            mov rax, qword ptr [rbp + 0x80]
009337A6  0F 11 30                        movups xmmword ptr [rax], xmm6
009337A9  E8 D2 6F AF FF                  call 0x14042a780
009337AE  45 33 E4                        xor r12d, r12d
009337B1  41 8B DC                        mov ebx, r12d
009337B4  E9 0B FC FF FF                  jmp 0x1409333c4
009337B9  33 C0                           xor eax, eax
009337BB  8B C8                           mov ecx, eax
009337BD  44 8B D8                        mov r11d, eax
009337C0  45 85 C0                        test r8d, r8d
009337C3  7E 9D                           jle 0x140933762
009337C5  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
009337C9  45 0F B7 C1                     movzx r8d, r9w
009337CD  0F 1F 00                        nop dword ptr [rax]
009337D0  48 8D 04 09                     lea rax, [rcx + rcx]
009337D4  49 3B C0                        cmp rax, r8
009337D7  73 07                           jae 0x1409337e0
009337D9  66 83 3C 10 5C                  cmp word ptr [rax + rdx], 0x5c
009337DE  74 4C                           je 0x14093382c
009337E0  48 8D 04 09                     lea rax, [rcx + rcx]
009337E4  49 3B C0                        cmp rax, r8
009337E7  73 1A                           jae 0x140933803
009337E9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
009337F0  66 83 3C 10 5C                  cmp word ptr [rax + rdx], 0x5c
009337F5  74 0C                           je 0x140933803
009337F7  48 FF C1                        inc rcx
009337FA  48 8D 04 09                     lea rax, [rcx + rcx]
009337FE  49 3B C0                        cmp rax, r8
00933801  72 ED                           jb 0x1409337f0
00933803  48 8D 04 09                     lea rax, [rcx + rcx]
00933807  49 3B C0                        cmp rax, r8
0093380A  0F 83 4A FF FF FF               jae 0x14093375a
00933810  66 83 3C 10 5C                  cmp word ptr [rax + rdx], 0x5c
00933815  0F 85 3F FF FF FF               jne 0x14093375a
0093381B  48 FF C1                        inc rcx
0093381E  48 8D 04 09                     lea rax, [rcx + rcx]
00933822  49 3B C0                        cmp rax, r8
00933825  72 E9                           jb 0x140933810
00933827  E9 2E FF FF FF                  jmp 0x14093375a
0093382C  48 FF C1                        inc rcx
0093382F  48 8D 04 09                     lea rax, [rcx + rcx]
00933833  49 3B C0                        cmp rax, r8
00933836  72 A1                           jb 0x1409337d9
00933838  EB A6                           jmp 0x1409337e0
0093383A  66 41 03 D6                     add dx, r14w
0093383E  48 83 E8 01                     sub rax, 1
00933842  0F 89 5C FD FF FF               jns 0x1409335a4
00933848  E9 63 FD FF FF                  jmp 0x1409335b0
0093384D  4C 8B 65 68                     mov r12, qword ptr [rbp + 0x68]
00933851  49 8B CC                        mov rcx, r12
00933854  E8 C7 C1 8D FF                  call 0x14020fa20
00933859  E9 8A FE FF FF                  jmp 0x1409336e8
0093385E  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00933863  E9 59 FB FF FF                  jmp 0x1409333c1
00933868  BA 56 52 65 67                  mov edx, 0x67655256
0093386D  48 8B CB                        mov rcx, rbx
00933870  E8 9B CE 8D FF                  call 0x140210710
00933875  49 8B CE                        mov rcx, r14
00933878  E8 5B 0D 00 00                  call 0x1409345d8
0093387D  4C 3B F7                        cmp r14, rdi
00933880  74 0D                           je 0x14093388f
00933882  BA 56 52 65 67                  mov edx, 0x67655256
00933887  49 8B CE                        mov rcx, r14
0093388A  E8 51 40 9C FF                  call 0x1402f78e0
0093388F  4C 8B F3                        mov r14, rbx
00933892  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00933897  33 F6                           xor esi, esi
00933899  E9 A6 F8 FF FF                  jmp 0x140933144
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0093345B(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, __int64 a8, __int64 a9, unsigned __int16 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int16 v_stack_p50;
    unsigned __int16 v_stack_p52;
    unsigned __int64 v_stack_p58;

    if (a4 == 0) goto loc_009334BC;
loc_00933467:
    if ((v_rsi + v_rsi * 1) >= ((unsigned __int16)(v_r15))) goto loc_0093347C;
loc_00933470:
    if ((*(unsigned __int16 *)(v_r12 + v_rsi + v_rsi * 1 * 1)) == 92) goto loc_00933745;
loc_0093347C:
    if ((v_rsi + v_rsi * 1) >= ((unsigned __int16)(v_r15))) goto loc_00933499;
loc_00933485:
    if ((*(unsigned __int16 *)(v_r12 + v_rsi + v_rsi * 1 * 1)) == 92) goto loc_00933499;
    a1 = (v_rsi) + 1;
    if ((a1 + a1 * 1) < ((unsigned __int16)(v_r15))) goto loc_00933485;
loc_00933499:
    if ((a1 + a1 * 1) >= ((unsigned __int16)(v_r15))) goto loc_009334B6;
loc_009334A2:
    if ((*(unsigned __int16 *)(v_r12 + a1 + a1 * 1 * 1)) != 92) goto loc_009334B6;
    a1 = (a1) + 1;
    if ((a1 + a1 * 1) < ((unsigned __int16)(v_r15))) goto loc_009334A2;
loc_009334B6:
    a4 = (a4) - (1);
    if (condition_is_not_equal) goto loc_00933467;
loc_009334BC:
    a1 = 0;
    *(unsigned __int64 *)(v_rbp - 72) = v_r12 + a1 * 2;
    result = (unsigned __int16)(((unsigned __int16)(a1)) + ((unsigned __int16)((unsigned __int16)(a1))));
    *(unsigned __int64 *)(v_rbp - 96) = 0;
    v_r15 = (unsigned __int16)((v_r15) - ((unsigned __int16)(result)));
    *(unsigned __int64 *)(v_rbp - 88) = 0;
    v_stack_p50 = 0;
    *(unsigned __int16 *)(v_rbp - 80) = (unsigned __int16)(v_r15);
    *(unsigned __int16 *)(v_rbp - 78) = (unsigned __int16)(v_r15);
    v_rbx = v_rbp - 96;
    if (v_r13 + 24 != 0) { v_rbx = v_r13 + 24; }
    if (((unsigned __int16)(v_r15 + *(unsigned __int16 *)(v_rbx) * 1)) < ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)))) goto loc_0093385E;
    if (((unsigned __int16)(v_r15 + *(unsigned __int16 *)(v_rbx) * 1 + 2)) < ((unsigned __int16)(v_r15 + *(unsigned __int16 *)(v_rbx) * 1))) goto loc_0093385E;
    v_stack_p52 = (unsigned __int16)(v_r15 + *(unsigned __int16 *)(v_rbx) * 1 + 2);
    result = ExAllocatePool2(256, (unsigned __int16)(v_r15 + *(unsigned __int16 *)(v_rbx) * 1 + 2), (unsigned int)(0x67655256ULL), a4);
    v_stack_p58 = result;
    result = RtlCopyUnicodeString(a10, v_rbx, (unsigned int)(0x67655256ULL), a4);
    if ((unsigned __int16)(v_r15) == 0) goto loc_00933589;
    if ((*(unsigned __int16 *)(v_r12 + a1 * 2)) == 92) goto loc_0093357B;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)) == 0) goto loc_0093356A;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx)))) >> (1);
    result = *(unsigned __int64 *)(v_rbx + 8);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 8) + a1 * 2 - 2)) != 92) {
        a2 = v_rip + 1872927;
        a1 = a10;
        result = RtlAppendUnicodeToString(a1, a2, (unsigned int)(0x67655256ULL), a4);
    }
    result = RtlAppendUnicodeStringToString(a10, v_rbp - 80, (unsigned int)(0x67655256ULL), a4);
loc_00933589:
    result = ((unsigned int)(a10)) >> (1);
    result = (result) - (1);
    if (sign_flag) goto loc_009335BA;
loc_009335A4:
    if ((*(unsigned __int16 *)(a11 + result * 2)) == 92) goto loc_0093383A;
loc_009335B0:
    v_stack_p50 = a10;
loc_009335BA:
    result = *(unsigned __int64 *)(v_rbp + 120);
    if (v_r12 != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 120) + 8))) {
        a2 = 0;
        a1 = v_r12;
        result = ExFreePoolWithTag(a1, a2, a11, a4);
    }
    a2 = 0;
    *(unsigned __int64 *)(v_rbp - 112) = v_xmm6;
    result = RtlInitUnicodeString(a10, a2, a11, a4);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 56))))) & (4));
    v_r12 = (unsigned int)(((unsigned int)(v_stack_p34)) | ((unsigned int)(result)));
    if (a8 == (*(unsigned __int64 *)(v_rbp + 96))) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r13 + 56))) & (2));
        v_r12 = (unsigned int)((v_r12) | ((unsigned int)(a1)));
    }
    result = (unsigned int)((unsigned int)(v_r12));
    if ((unsigned __int16)(v_r15) != 0) { result = (unsigned int)(v_r12); }
    v_stack_p34 = (unsigned int)(result);
    v_r15 = (unsigned __int8)((unsigned int)(a7));
    if (((unsigned int)((unsigned int)(a6))) < ((unsigned int)(*(unsigned __int16 *)(v_r13 + 64)))) { v_r15 = 1; }
    result = (unsigned int)((*(unsigned __int16 *)(v_r13 + 66)) - ((unsigned int)(*(unsigned __int16 *)(v_r13 + 64))));
    v_stack_p38 = (unsigned int)(v_r15);
    a3 = (unsigned int)(((unsigned int)(a6)) + ((unsigned int)(result)));
    v_stack_p30 = (unsigned int)(a3);
    if (*(unsigned __int64 *)(v_r13 + 16) != 0) goto loc_00933868;
    if (*(unsigned __int64 *)(v_rbp + 136) == 0) goto loc_009336F5;
    if ((unsigned __int8)(v_r15) == 0) goto loc_0093384D;
    *(unsigned int *)(v_rbp - 48) = 48;
    v_r12 = 0;
    *(unsigned int *)(v_rbp - 24) = 576;
    *(unsigned __int64 *)(v_rbp - 40) = 0;
    *(unsigned __int64 *)(v_rbp - 32) = v_r13 + 24;
    *(unsigned __int64 *)(v_rbp - 16) = v_xmm0;
    result = ZwOpenKey(a14, (unsigned int)(0x80000000ULL), v_rbp - 48, a4);
    result = 0;
    a4 = 0;
    v_stack_p28 = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_rbp - 120) = 0;
    v_stack_p20 = v_rbp - 120;
    result = ObReferenceObjectByHandle(a14, a2, *(unsigned __int64 *)(v_rip + 6894601), a4);
loc_009336E8:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 136)) = *(unsigned __int64 *)(v_rbp - 120);
loc_009336F5:
    if (*(unsigned __int64 *)(v_rbp + 144) == 0) goto loc_0093377D;
    if ((unsigned __int8)(v_r15) == 0) goto loc_009337B9;
    a1 = (*(unsigned __int16 *)(v_r13 + 24)) >> (1);
    if ((a1 + a1 * 1) >= 0) goto loc_00933762;
loc_00933730:
    if ((*(unsigned __int16 *)(a1 + a1 * 1 + a2 * 1)) != 92) goto loc_00933762;
    a1 = (a1) + 1;
    if ((a1 + a1 * 1) < 0) goto loc_00933730;
    goto loc_00933762;
loc_00933745:
    a1 = (a1) + 1;
    if ((a1 + a1 * 1) < 0) goto loc_00933470;
    goto loc_0093347C;
loc_0093375A:
    v_r11 = (v_r11) + 1;
    if (((unsigned int)(v_r11)) < ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_009337D0;
loc_00933762:
    result = (unsigned __int16)(((unsigned __int16)(a1)) + ((unsigned __int16)((unsigned __int16)(a1))));
    a4 = (unsigned __int16)((a4) - ((unsigned __int16)(result)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 144) + 8) = a2 + a1 * 2;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 144)) = (unsigned __int16)(a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 144) + 2) = (unsigned __int16)(a4);
loc_0093377D:
    if (*(unsigned __int64 *)(v_rbp + 152) != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 152)) = (unsigned int)((unsigned int)(v_stack_p34));
    }
    a2 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 160)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 60)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 128)) = v_xmm6;
    result = RtlInitUnicodeString(v_rbp - 112, a2, 0, a4);
    v_r12 = 0;
loc_009337B9:
    result = 0;
    if (condition_is_less_or_equal) goto loc_00933762;
loc_009337D0:
    if ((0 + 0 * 1) >= ((unsigned __int16)(a4))) goto loc_009337E0;
loc_009337D9:
    if ((*(unsigned __int16 *)(0 + 0 * 1 + a2 * 1)) == 92) goto loc_0093382C;
loc_009337E0:
    if ((0 + 0 * 1) >= ((unsigned __int16)(a4))) goto loc_00933803;
loc_009337F0:
    if ((*(unsigned __int16 *)(0 + 0 * 1 + a2 * 1)) == 92) goto loc_00933803;
    a1 = (0) + 1;
    if ((a1 + a1 * 1) < ((unsigned __int16)(a4))) goto loc_009337F0;
loc_00933803:
    if ((a1 + a1 * 1) >= ((unsigned __int16)(a4))) goto loc_0093375A;
loc_00933810:
    if ((*(unsigned __int16 *)(a1 + a1 * 1 + a2 * 1)) != 92) goto loc_0093375A;
    a1 = (a1) + 1;
    if ((a1 + a1 * 1) < ((unsigned __int16)(a4))) goto loc_00933810;
    goto loc_0093375A;
loc_0093382C:
    a1 = (a1) + 1;
    if ((a1 + a1 * 1) < ((unsigned __int16)(a4))) goto loc_009337D9;
    goto loc_009337E0;
loc_0093383A:
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)(a8)));
    result = (a1 + a1 * 1) - (1);
    if (!sign_flag) goto loc_009335A4;
    goto loc_009335B0;
loc_0093384D:
    result = ObfReferenceObject(*(unsigned __int64 *)(v_rbp + 104), a2, (unsigned __int16)(a4), a4);
    goto loc_009336E8;
loc_0093385E:
loc_00933868:
    result = ObfReferenceObjectWithTag((unsigned int)(0xC000000DULL), (unsigned int)(0x67655256ULL), (unsigned __int16)(a4), a4);
    result = VrpUnlockJobContextShared(a8, (unsigned int)(0x67655256ULL), (unsigned __int16)(a4), a4);
    if (a8 != (*(unsigned __int64 *)(v_rbp + 136))) {
        a2 = 0x67655256ULL;
        a1 = a8;
        result = ObfDereferenceObjectWithTag(a1, a2, (unsigned __int16)(a4), a4);
    }
    v_stack_p40 = (unsigned int)(0xC000000DULL);
    v_rsi = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0093345B(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint32_t Arg6, uint32_t Arg7, int64_t Arg8, uint64_t Arg9, uint16_t Arg10, void *Arg11, uint64_t Arg12, uint64_t Arg13, int64_t Arg14)
{
    uint8_t *arg11 = (uint8_t *)Arg11;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint16_t v_stack_p50;
    uint16_t v_stack_p52;
    uint64_t v_stack_p58;

    if (Arg4 == 0) goto loc_009334BC;
loc_00933467:
    if ((local_rsi + local_rsi * 1) >= ((uint16_t)(local_r15))) goto loc_0093347C;
loc_00933470:
    if ((*(uint16_t *)(local_r12 + local_rsi + local_rsi * 1 * 1)) == 92) goto loc_00933745;
loc_0093347C:
    if ((local_rsi + local_rsi * 1) >= ((uint16_t)(local_r15))) goto loc_00933499;
loc_00933485:
    if ((*(uint16_t *)(local_r12 + local_rsi + local_rsi * 1 * 1)) == 92) goto loc_00933499;
    Arg1 = (local_rsi) + 1;
    if ((Arg1 + Arg1 * 1) < ((uint16_t)(local_r15))) goto loc_00933485;
loc_00933499:
    if ((Arg1 + Arg1 * 1) >= ((uint16_t)(local_r15))) goto loc_009334B6;
loc_009334A2:
    if ((*(uint16_t *)(local_r12 + Arg1 + Arg1 * 1 * 1)) != 92) goto loc_009334B6;
    Arg1 = (Arg1) + 1;
    if ((Arg1 + Arg1 * 1) < ((uint16_t)(local_r15))) goto loc_009334A2;
loc_009334B6:
    Arg4 = (Arg4) - (1);
    if (condition_is_not_equal) goto loc_00933467;
loc_009334BC:
    Arg1 = 0;
    *(uint64_t *)(local_rbp - 0x48) = local_r12 + Arg1 * 2;
    result = (uint16_t)(((uint16_t)(Arg1)) + ((uint16_t)((uint16_t)(Arg1))));
    *(uint64_t *)(local_rbp - 0x60) = 0;
    local_r15 = (uint16_t)((local_r15) - ((uint16_t)(result)));
    *(uint64_t *)(local_rbp - 0x58) = 0;
    v_stack_p50 = 0;
    *(uint16_t *)(local_rbp - 0x50) = (uint16_t)(local_r15);
    *(uint16_t *)(local_rbp - 0x4E) = (uint16_t)(local_r15);
    local_rbx = local_rbp - 96;
    if (local_r13 + 24 != 0) { local_rbx = local_r13 + 24; }
    if (((uint16_t)(local_r15 + *(uint16_t *)(local_rbx) * 1)) < ((uint16_t)(*(uint16_t *)(local_rbx)))) goto loc_0093385E;
    if (((uint16_t)(local_r15 + *(uint16_t *)(local_rbx) * 1 + 2)) < ((uint16_t)(local_r15 + *(uint16_t *)(local_rbx) * 1))) goto loc_0093385E;
    v_stack_p52 = (uint16_t)(local_r15 + *(uint16_t *)(local_rbx) * 1 + 2);
    result = ExAllocatePool2(256, (uint16_t)(local_r15 + *(uint16_t *)(local_rbx) * 1 + 2), (uint32_t)(0x67655256ULL), Arg4);
    v_stack_p58 = result;
    result = RtlCopyUnicodeString(Arg10, local_rbx, (uint32_t)(0x67655256ULL), Arg4);
    if ((uint16_t)(local_r15) == 0) goto loc_00933589;
    if ((*(uint16_t *)(local_r12 + Arg1 * 2)) == 92) goto loc_0093357B;
    if ((uint16_t)(*(uint16_t *)(local_rbx)) == 0) goto loc_0093356A;
    Arg1 = ((uint32_t)((uint32_t)(*(uint16_t *)(local_rbx)))) >> (1);
    result = *(uint64_t *)(local_rbx + 0x8);
    if ((*(uint16_t *)(*(uint64_t *)(local_rbx + 0x8) + Arg1 * 2 - 0x2)) != 92) {
        Arg2 = v_rip + 1872927;
        Arg1 = Arg10;
        result = RtlAppendUnicodeToString(Arg1, Arg2, (uint32_t)(0x67655256ULL), Arg4);
    }
    result = RtlAppendUnicodeStringToString(Arg10, local_rbp - 80, (uint32_t)(0x67655256ULL), Arg4);
loc_00933589:
    result = ((uint32_t)(Arg10)) >> (1);
    result = (result) - (1);
    if (sign_flag) goto loc_009335BA;
loc_009335A4:
    if ((*(uint16_t *)(arg11 + result * 2)) == 92) goto loc_0093383A;
loc_009335B0:
    v_stack_p50 = Arg10;
loc_009335BA:
    result = *(uint64_t *)(local_rbp + 0x78);
    if (local_r12 != (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x78) + 0x8))) {
        Arg2 = 0;
        Arg1 = local_r12;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg11, Arg4);
    }
    Arg2 = 0;
    *(uint64_t *)(local_rbp - 0x70) = v_xmm6;
    result = RtlInitUnicodeString(Arg10, Arg2, Arg11, Arg4);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0x38))))) & (4));
    local_r12 = (uint32_t)(((uint32_t)(v_stack_p34)) | ((uint32_t)(result)));
    if (Arg8 == (*(uint64_t *)(local_rbp + 0x60))) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r13 + 0x38))) & (2));
        local_r12 = (uint32_t)((local_r12) | ((uint32_t)(Arg1)));
    }
    result = (uint32_t)((uint32_t)(local_r12));
    if ((uint16_t)(local_r15) != 0) { result = (uint32_t)(local_r12); }
    v_stack_p34 = (uint32_t)(result);
    local_r15 = (uint8_t)((uint32_t)(Arg7));
    if (((uint32_t)((uint32_t)(Arg6))) < ((uint32_t)(*(uint16_t *)(local_r13 + 0x40)))) { local_r15 = 1; }
    result = (uint32_t)((*(uint16_t *)(local_r13 + 0x42)) - ((uint32_t)(*(uint16_t *)(local_r13 + 0x40))));
    v_stack_p38 = (uint32_t)(local_r15);
    Arg3 = (uint32_t)(((uint32_t)(Arg6)) + ((uint32_t)(result)));
    v_stack_p30 = (uint32_t)(Arg3);
    if (*(uint64_t *)(local_r13 + 0x10) != 0) goto loc_00933868;
    if (*(uint64_t *)(local_rbp + 0x88) == 0) goto loc_009336F5;
    if ((uint8_t)(local_r15) == 0) goto loc_0093384D;
    *(uint32_t *)(local_rbp - 0x30) = 48;
    local_r12 = 0;
    *(uint32_t *)(local_rbp - 0x18) = 576;
    *(uint64_t *)(local_rbp - 0x28) = 0;
    *(uint64_t *)(local_rbp - 0x20) = local_r13 + 24;
    *(uint64_t *)(local_rbp - 0x10) = v_xmm0;
    result = ZwOpenKey(Arg14, (uint32_t)(0x80000000ULL), local_rbp - 48, Arg4);
    result = 0;
    Arg4 = 0;
    v_stack_p28 = 0;
    Arg2 = 0;
    *(uint64_t *)(local_rbp - 0x78) = 0;
    v_stack_p20 = local_rbp - 120;
    result = ObReferenceObjectByHandle(Arg14, Arg2, *(uint64_t *)(v_rip + 0x693409), Arg4);
loc_009336E8:
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x88)) = *(uint64_t *)(local_rbp - 0x78);
loc_009336F5:
    if (*(uint64_t *)(local_rbp + 0x90) == 0) goto loc_0093377D;
    if ((uint8_t)(local_r15) == 0) goto loc_009337B9;
    Arg1 = (*(uint16_t *)(local_r13 + 0x18)) >> (1);
    if ((Arg1 + Arg1 * 1) >= 0) goto loc_00933762;
loc_00933730:
    if ((*(uint16_t *)(Arg1 + Arg1 * 1 + Arg2 * 1)) != 92) goto loc_00933762;
    Arg1 = (Arg1) + 1;
    if ((Arg1 + Arg1 * 1) < 0) goto loc_00933730;
    goto loc_00933762;
loc_00933745:
    Arg1 = (Arg1) + 1;
    if ((Arg1 + Arg1 * 1) < 0) goto loc_00933470;
    goto loc_0093347C;
loc_0093375A:
    local_r11 = (local_r11) + 1;
    if (((uint32_t)(local_r11)) < ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_009337D0;
loc_00933762:
    result = (uint16_t)(((uint16_t)(Arg1)) + ((uint16_t)((uint16_t)(Arg1))));
    Arg4 = (uint16_t)((Arg4) - ((uint16_t)(result)));
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x90) + 0x8) = Arg2 + Arg1 * 2;
    *(uint16_t *)(*(uint64_t *)(local_rbp + 0x90)) = (uint16_t)(Arg4);
    *(uint16_t *)(*(uint64_t *)(local_rbp + 0x90) + 0x2) = (uint16_t)(Arg4);
loc_0093377D:
    if (*(uint64_t *)(local_rbp + 0x98) != 0) {
        *(uint32_t *)(*(uint64_t *)(local_rbp + 0x98)) = (uint32_t)((uint32_t)(v_stack_p34));
    }
    Arg2 = 0;
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0xA0)) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0x3C)));
    *(uint64_t *)(*(uint64_t *)(local_rbp + 0x80)) = v_xmm6;
    result = RtlInitUnicodeString(local_rbp - 112, Arg2, 0, Arg4);
    local_r12 = 0;
loc_009337B9:
    result = 0;
    if (condition_is_less_or_equal) goto loc_00933762;
loc_009337D0:
    if ((0 + 0 * 1) >= ((uint16_t)(Arg4))) goto loc_009337E0;
loc_009337D9:
    if ((*(uint16_t *)(0 + 0x0 * 1 + Arg2 * 1)) == 92) goto loc_0093382C;
loc_009337E0:
    if ((0 + 0 * 1) >= ((uint16_t)(Arg4))) goto loc_00933803;
loc_009337F0:
    if ((*(uint16_t *)(0 + 0x0 * 1 + Arg2 * 1)) == 92) goto loc_00933803;
    Arg1 = (0) + 1;
    if ((Arg1 + Arg1 * 1) < ((uint16_t)(Arg4))) goto loc_009337F0;
loc_00933803:
    if ((Arg1 + Arg1 * 1) >= ((uint16_t)(Arg4))) goto loc_0093375A;
loc_00933810:
    if ((*(uint16_t *)(Arg1 + Arg1 * 1 + Arg2 * 1)) != 92) goto loc_0093375A;
    Arg1 = (Arg1) + 1;
    if ((Arg1 + Arg1 * 1) < ((uint16_t)(Arg4))) goto loc_00933810;
    goto loc_0093375A;
loc_0093382C:
    Arg1 = (Arg1) + 1;
    if ((Arg1 + Arg1 * 1) < ((uint16_t)(Arg4))) goto loc_009337D9;
    goto loc_009337E0;
loc_0093383A:
    Arg2 = (uint16_t)((Arg2) + ((uint16_t)(Arg8)));
    result = (Arg1 + Arg1 * 1) - (1);
    if (!sign_flag) goto loc_009335A4;
    goto loc_009335B0;
loc_0093384D:
    result = ObfReferenceObject(*(uint64_t *)(local_rbp + 0x68), Arg2, (uint16_t)(Arg4), Arg4);
    goto loc_009336E8;
loc_0093385E:
loc_00933868:
    result = ObfReferenceObjectWithTag((uint32_t)(0xC000000DULL), (uint32_t)(0x67655256ULL), (uint16_t)(Arg4), Arg4);
    result = VrpUnlockJobContextShared(Arg8, (uint32_t)(0x67655256ULL), (uint16_t)(Arg4), Arg4);
    if (Arg8 != (*(uint64_t *)(local_rbp + 0x88))) {
        Arg2 = 0x67655256ULL;
        Arg1 = Arg8;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, (uint16_t)(Arg4), Arg4);
    }
    v_stack_p40 = (uint32_t)(0xC000000DULL);
    local_rsi = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg11` | `+ 0x0 + rax*2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0093345B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
