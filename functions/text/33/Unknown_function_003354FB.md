# sub_003354FB

- RVA: `0x003354FB`–`0x0033603B` (길이 `2,880` bytes)
- VA: `0x00000001403354FB`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000768DC`
- 디코드: `651`개 명령, `2,880/2,880` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x003355EB` → [MiUpdateLargePageCandidateValue](MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x00335665` → [ExpWaitForSpinLockExclusiveAndAcquire](../32/ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) (function, `0x003239A0`)
- `0x003357CF` → [MiUpdateLargePageCandidateValue](MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x00335930` → [KeSetEvent](KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0033596E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00335A72` → [ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented](../32/ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_00323A70.md) (function, `0x00323A70`)
- `0x00335C0A` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x00335C2D` → [MiWakeZeroingThreads](../2C/MiWakeZeroingThreads_function_002CBEC0.md) (function, `0x002CBEC0`)
- `0x00335C3D` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00335C94` → [MI_NODE_FROM_PFN](../2B/MI_NODE_FROM_PFN_function_002B0F30.md) (function, `0x002B0F30`)
- `0x00335CBC` → [MiFreePageToSlabAllocator](../2A/MiFreePageToSlabAllocator_function_002A0A60.md) (function, `0x002A0A60`)
- `0x00335CE9` → [MiPageToChannel](../2B/MiPageToChannel_function_002B9B48.md) (function, `0x002B9B48`)
- `0x00335D18` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00335E37` → [MiUpdateAvailableEventsAtDpc](../3B/MiUpdateAvailableEventsAtDpc_function_003BC804.md) (function, `0x003BC804`)
- `0x00335E6F` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00335E7F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00335EA1` → [MiUpdateLargePageCandidateValue](MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x00335EF1` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00335F22` → [MiRecordLargePageCandidate](../37/MiRecordLargePageCandidate_function_0037A624.md) (function, `0x0037A624`)
- `0x00335F41` → [MiGetPagePrivilege](../28/MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)
- `0x00335F6E` → [VslRemoveProtectedPage](../40/VslRemoveProtectedPage_function_004079D0.md) (function, `0x004079D0`)
- `0x00335F80` → [MiSetPfnIdentity](../2A/MiSetPfnIdentity_function_002A2350.md) (function, `0x002A2350`)
- `0x00335FAA` → [MiUpdateLargePageCandidateValue](MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x00335FEB` → [MiSlabDemotionLowMemoryConditionUpdate](../3B/MiSlabDemotionLowMemoryConditionUpdate_function_003BB7E0.md) (function, `0x003BB7E0`)
- `0x0033600A` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x003355C9` → RVA `0x00FC5002` (`ALMOSTRO`; read)
- `0x00335647` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0033568F` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00335784` → RVA `0x00E30088` (`.data`; read)
- `0x00335905` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x003359F6` → RVA `0x00011C60` (`.rdata`; read)
- `0x00335A5E` → RVA `0x00F0DE58` (`.data`; read)
- `0x00335E61` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00335EBB` → RVA `0x00FC6B30` (`ALMOSTRO`; read)
- `0x00336021` → RVA `0x00FC5000` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **38**
  - `0x003354FF` → [sub_0033535B + 0xD1](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x0033551B` → [sub_0033535B](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x0033555B` → [sub_00336094 + 0x159](Unknown_function_00336094.md) (`tail-transfer`)
  - `0x00335568` → [sub_00336094 + 0x159](Unknown_function_00336094.md) (`tail-transfer`)
  - `0x003355D0` → [sub_00336291 + 0x71](Unknown_function_00336291.md) (`tail-transfer`)
  - `0x003358F4` → [sub_0033535B + 0x17E](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x003358FF` → [sub_0033535B + 0x17E](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x0033590C` → [sub_0033535B + 0x17E](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x00335917` → [sub_00336291 + 0x87](Unknown_function_00336291.md) (`tail-transfer`)
  - `0x00335922` → [sub_0033535B + 0x17E](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x00335935` → [sub_0033535B + 0x17E](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x00335955` → [sub_00334D90 + 0x2A9](Unknown_function_00334D90.md) (`tail-transfer`)
  - `0x00335A7F` → [sub_00334D90 + 0x3D3](Unknown_function_00334D90.md) (`tail-transfer`)
  - `0x00335A88` → [sub_00334D90 + 0x38B](Unknown_function_00334D90.md) (`tail-transfer`)
  - `0x00335AC2` → [sub_00334D90 + 0x27B](Unknown_function_00334D90.md) (`tail-transfer`)
  - `0x00335ACB` → [sub_00334D90 + 0x24B](Unknown_function_00334D90.md) (`tail-transfer`)
  - `0x00335C4F` → [sub_00334D90 + 0x1FE](Unknown_function_00334D90.md) (`tail-transfer`)
  - `0x00335C5A` → [sub_0033535B + 0x17E](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x00335CC1` → [sub_0033535B + 0x17E](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x00335CC9` → [sub_00334D90 + 0x38B](Unknown_function_00334D90.md) (`tail-transfer`)
  - `0x00335CF6` → [sub_00334D90 + 0x294](Unknown_function_00334D90.md) (`tail-transfer`)
  - `0x00335CFD` → [sub_00336291 + 0x69](Unknown_function_00336291.md) (`tail-transfer`)
  - `0x00335D73` → [sub_0033535B + 0x4E](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x00335D7F` → [sub_00334D90 + 0x305](Unknown_function_00334D90.md) (`tail-transfer`)
  - `0x00335D89` → [sub_00334D90 + 0x305](Unknown_function_00334D90.md) (`tail-transfer`)
  - `0x00335DA6` → [sub_0033535B + 0x17E](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x00335DAE` → [sub_00336212 + 0x5](Unknown_function_00336212.md) (`tail-transfer`)
  - `0x00335DBD` → [sub_0033535B + 0x17A](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x00335DFB` → [sub_00336094 + 0xC](Unknown_function_00336094.md) (`tail-transfer`)
  - `0x00335E5C` → [sub_00334D90 + 0x4CB](Unknown_function_00334D90.md) (`tail-transfer`)
  - `0x00335ED6` → [sub_0033535B + 0x3E](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x00335F0B` → [sub_0033535B + 0x30](Unknown_function_0033535B.md) (`tail-transfer`)
  - `0x00335F64` → [sub_00336094](Unknown_function_00336094.md) (`tail-transfer`)
  - `0x00335F75` → [sub_00336291 + 0x3D](Unknown_function_00336291.md) (`tail-transfer`)
  - `0x00335F9D` → [sub_00334D90 + 0xA1](Unknown_function_00334D90.md) (`tail-transfer`)
  - `0x00335FBB` → [sub_00336212](Unknown_function_00336212.md) (`tail-transfer`)
  - `0x00335FC8` → [sub_00336094 + 0x16B](Unknown_function_00336094.md) (`tail-transfer`)
  - `0x00335FD2` → [sub_00336094 + 0x116](Unknown_function_00336094.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003354FB  48 83 E3 EF                     and rbx, 0xffffffffffffffef
003354FF  E9 28 FF FF FF                  jmp 0x14033542c
00335504  41 B8 01 00 00 00               mov r8d, 1
0033550A  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0033550E  48 25 FF F3 FF F7               and rax, 0xfffffffff7fff3ff
00335514  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
00335518  45 85 DB                        test r11d, r11d
0033551B  0F 85 3A FE FF FF               jne 0x14033535b
00335521  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00335526  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
0033552B  48 83 FE 01                     cmp rsi, 1
0033552F  0F 85 AE 08 00 00               jne 0x140335de3
00335535  4D 8B F8                        mov r15, r8
00335538  F0 4D 0F C1 BA 00 49 00 00      lock xadd qword ptr [r10 + 0x4900], r15
00335541  49 FF C7                        inc r15
00335544  49 81 FF 20 04 00 00            cmp r15, 0x420
0033554B  0F 86 63 0A 00 00               jbe 0x140335fb4
00335551  49 FF CF                        dec r15
00335554  4D 3B BA 00 41 00 00            cmp r15, qword ptr [r10 + 0x4100]
0033555B  0F 84 8C 0C 00 00               je 0x1403361ed
00335561  4D 3B BA 08 41 00 00            cmp r15, qword ptr [r10 + 0x4108]
00335568  0F 84 7F 0C 00 00               je 0x1403361ed
0033556E  4C 8B 7D 70                     mov r15, qword ptr [rbp + 0x70]
00335572  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
00335577  44 8B 8D 88 00 00 00            mov r9d, dword ptr [rbp + 0x88]
0033557E  41 8B C5                        mov eax, r13d
00335581  4C 8D 2C 80                     lea r13, [rax + rax*4]
00335585  49 C1 E5 08                     shl r13, 8
00335589  4D 03 EB                        add r13, r11
0033558C  F0 4B FF 44 CD 08               lock inc qword ptr [r13 + r9*8 + 8]
00335592  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
00335596  48 8B C3                        mov rax, rbx
00335599  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
0033559E  49 81 FF 00 00 10 00            cmp r15, 0x100000
003355A5  0F 82 17 08 00 00               jb 0x140335dc2
003355AB  8B 74 24 70                     mov esi, dword ptr [rsp + 0x70]
003355AF  48 8D 04 86                     lea rax, [rsi + rax*4]
003355B3  F0 49 FF 44 C5 18               lock inc qword ptr [r13 + rax*8 + 0x18]
003355B9  44 8B E7                        mov r12d, edi
003355BC  41 C1 EC 08                     shr r12d, 8
003355C0  41 80 E4 01                     and r12b, 1
003355C4  83 FA 03                        cmp edx, 3
003355C7  75 33                           jne 0x1403355fc
003355C9  80 3D 32 FA C8 00 01            cmp byte ptr [rip + 0xc8fa32], 1
003355D0  0F 87 2C 0D 00 00               ja 0x140336302
003355D6  41 B9 01 00 00 00               mov r9d, 1
003355DC  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
003355E1  49 8B D7                        mov rdx, r15
003355E4  49 8B CA                        mov rcx, r10
003355E7  45 8D 41 02                     lea r8d, [r9 + 2]
003355EB  E8 90 99 00 00                  call 0x14033ef80
003355F0  44 8B 8D 88 00 00 00            mov r9d, dword ptr [rbp + 0x88]
003355F7  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
003355FC  8B C7                           mov eax, edi
003355FE  8B D7                           mov edx, edi
00335600  C1 E8 10                        shr eax, 0x10
00335603  C1 EA 0F                        shr edx, 0xf
00335606  83 E0 03                        and eax, 3
00335609  83 E2 01                        and edx, 1
0033560C  80 3D EF F9 C8 00 01            cmp byte ptr [rip + 0xc8f9ef], 1
00335613  0F 87 FF 09 00 00               ja 0x140336018
00335619  45 32 C0                        xor r8b, r8b
0033561C  48 8D 0C 80                     lea rcx, [rax + rax*4]
00335620  41 8B C1                        mov eax, r9d
00335623  48 8D 14 4A                     lea rdx, [rdx + rcx*2]
00335627  48 8D 0C 50                     lea rcx, [rax + rdx*2]
0033562B  41 0F B6 C0                     movzx eax, r8b
0033562F  48 8D 0C 48                     lea rcx, [rax + rcx*2]
00335633  48 8D 14 8E                     lea rdx, [rsi + rcx*4]
00335637  40 0F B6 CF                     movzx ecx, dil
0033563B  48 6B F1 58                     imul rsi, rcx, 0x58
0033563F  49 03 B4 D3 E0 03 00 00         add rsi, qword ptr [r11 + rdx*8 + 0x3e0]
00335647  F6 05 B8 14 C9 00 21            test byte ptr [rip + 0xc914b8], 0x21
0033564E  0F 85 0A 04 00 00               jne 0x140335a5e
00335654  F0 0F BA 6E 20 1F               lock bts dword ptr [rsi + 0x20], 0x1f
0033565A  44 8B FB                        mov r15d, ebx
0033565D  73 0E                           jae 0x14033566d
0033565F  B2 FF                           mov dl, 0xff
00335661  48 8D 4E 20                     lea rcx, [rsi + 0x20]
00335665  E8 36 E3 FE FF                  call 0x1403239a0
0033566A  44 8B F8                        mov r15d, eax
0033566D  8B 56 20                        mov edx, dword ptr [rsi + 0x20]
00335670  8B CA                           mov ecx, edx
00335672  0F BA F1 1E                     btr ecx, 0x1e
00335676  81 F9 00 00 00 80               cmp ecx, 0x80000000
0033567C  74 30                           je 0x1403356ae
0033567E  0F BA E2 1E                     bt edx, 0x1e
00335682  72 08                           jb 0x14033568c
00335684  F0 81 4E 20 00 00 00 40         lock or dword ptr [rsi + 0x20], 0x40000000
0033568C  41 FF C7                        inc r15d
0033568F  44 85 3D 16 FC C8 00            test dword ptr [rip + 0xc8fc16], r15d
00335696  0F 84 C5 07 00 00               je 0x140335e61
0033569C  F3 90                           pause
0033569E  8B 56 20                        mov edx, dword ptr [rsi + 0x20]
003356A1  8B C2                           mov eax, edx
003356A3  0F BA F0 1E                     btr eax, 0x1e
003356A7  3D 00 00 00 80                  cmp eax, 0x80000000
003356AC  75 D0                           jne 0x14033567e
003356AE  4C 8B 7D 70                     mov r15, qword ptr [rbp + 0x70]
003356B2  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
003356B6  49 B9 FF FF FF FF 3F 00 00 00   movabs r9, 0x3fffffffff
003356C0  49 3B C1                        cmp rax, r9
003356C3  75 62                           jne 0x140335727
003356C5  8B 46 08                        mov eax, dword ptr [rsi + 8]
003356C8  41 B9 01 00 00 00               mov r9d, 1
003356CE  44 0F B6 D0                     movzx r10d, al
003356D2  8B D0                           mov edx, eax
003356D4  41 0F B6 CA                     movzx ecx, r10b
003356D8  48 C1 EA 10                     shr rdx, 0x10
003356DC  80 E1 3F                        and cl, 0x3f
003356DF  83 E2 03                        and edx, 3
003356E2  49 D3 E1                        shl r9, cl
003356E5  8B C8                           mov ecx, eax
003356E7  48 C1 E9 0F                     shr rcx, 0xf
003356EB  83 E1 01                        and ecx, 1
003356EE  48 8D 14 92                     lea rdx, [rdx + rdx*4]
003356F2  4C 8D 04 51                     lea r8, [rcx + rdx*2]
003356F6  8B C8                           mov ecx, eax
003356F8  48 C1 E8 14                     shr rax, 0x14
003356FC  48 C1 E9 12                     shr rcx, 0x12
00335700  83 E0 01                        and eax, 1
00335703  83 E1 03                        and ecx, 3
00335706  4A 8D 14 81                     lea rdx, [rcx + r8*4]
0033570A  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0033570F  48 8D 04 50                     lea rax, [rax + rdx*2]
00335713  48 03 C0                        add rax, rax
00335716  49 C1 EA 06                     shr r10, 6
0033571A  48 8B 84 C1 88 00 00 00         mov rax, qword ptr [rcx + rax*8 + 0x88]
00335722  F0 4E 09 0C D0                  lock or qword ptr [rax + r10*8], r9
00335727  44 8B 54 24 30                  mov r10d, dword ptr [rsp + 0x30]
0033572C  41 83 FA 03                     cmp r10d, 3
00335730  0F 84 BC 00 00 00               je 0x1403357f2
00335736  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0033573B  8B 95 88 00 00 00               mov edx, dword ptr [rbp + 0x88]
00335741  41 0F B6 C4                     movzx eax, r12b
00335745  49 8D 48 1D                     lea rcx, [r8 + 0x1d]
00335749  48 8D 0C 4A                     lea rcx, [rdx + rcx*2]
0033574D  48 8D 0C 48                     lea rcx, [rax + rcx*2]
00335751  F0 49 FF 44 CD 00               lock inc qword ptr [r13 + rcx*8]
00335757  4A 8D 04 42                     lea rax, [rdx + r8*2]
0033575B  F0 49 FF 84 C5 80 03 00 00      lock inc qword ptr [r13 + rax*8 + 0x380]
00335764  4B 8D 04 7F                     lea rax, [r15 + r15*2]
00335768  66 89 9D 80 00 00 00            mov word ptr [rbp + 0x80], bx
0033576F  48 03 C0                        add rax, rax
00335772  89 5C 24 64                     mov dword ptr [rsp + 0x64], ebx
00335776  48 B9 28 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000028
00335780  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00335784  48 8B 0D FD A8 AF 00            mov rcx, qword ptr [rip + 0xafa8fd]
0033578B  48 C1 E8 2B                     shr rax, 0x2b
0033578F  25 FF 03 00 00                  and eax, 0x3ff
00335794  4C 8B 34 C1                     mov r14, qword ptr [rcx + rax*8]
00335798  41 38 9E E6 3E 00 00            cmp byte ptr [r14 + 0x3ee6], bl
0033579F  74 4C                           je 0x1403357ed
003357A1  41 B9 01 00 00 00               mov r9d, 1
003357A7  49 8B D7                        mov rdx, r15
003357AA  49 8B CE                        mov rcx, r14
003357AD  45 85 D2                        test r10d, r10d
003357B0  0F 84 EC 07 00 00               je 0x140335fa2
003357B6  41 83 FA 02                     cmp r10d, 2
003357BA  0F 85 D4 06 00 00               jne 0x140335e94
003357C0  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
003357C7  45 8B C2                        mov r8d, r10d
003357CA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003357CF  E8 AC 97 00 00                  call 0x14033ef80
003357D4  0F B7 85 80 00 00 00            movzx eax, word ptr [rbp + 0x80]
003357DB  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
003357E1  48 3D 00 80 00 00               cmp rax, 0x8000
003357E7  0F 84 23 07 00 00               je 0x140335f10
003357ED  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
003357F2  4C 8B E3                        mov r12, rbx
003357F5  4F 8D 0C 7F                     lea r9, [r15 + r15*2]
003357F9  49 BD 00 00 00 00 00 DE FF FF   movabs r13, 0xffffde0000000000
00335803  49 C1 E1 04                     shl r9, 4
00335807  49 8B C5                        mov rax, r13
0033580A  4C 03 C8                        add r9, rax
0033580D  49 BE FF FF FF FF 3F 00 00 00   movabs r14, 0x3fffffffff
00335817  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
0033581B  49 3B C6                        cmp rax, r14
0033581E  0F 84 69 02 00 00               je 0x140335a8d
00335824  83 7E 0C 01                     cmp dword ptr [rsi + 0xc], 1
00335828  0F 85 A2 02 00 00               jne 0x140335ad0
0033582E  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00335832  48 8D 0C 40                     lea rcx, [rax + rax*2]
00335836  48 C1 E1 04                     shl rcx, 4
0033583A  49 8B C5                        mov rax, r13
0033583D  48 8D 14 01                     lea rdx, [rcx + rax]
00335841  49 BB 00 00 00 00 00 FF FF FF   movabs r11, 0xffffff0000000000
0033584B  49 8B 41 18                     mov rax, qword ptr [r9 + 0x18]
0033584F  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
00335859  48 C1 F9 04                     sar rcx, 4
0033585D  49 0F AF C8                     imul rcx, r8
00335861  48 33 C1                        xor rax, rcx
00335864  49 23 C3                        and rax, r11
00335867  48 33 C1                        xor rax, rcx
0033586A  48 B9 FF FF FF FF 3F FF FF FF   movabs rcx, 0xffffff3fffffffff
00335874  49 89 41 18                     mov qword ptr [r9 + 0x18], rax
00335878  49 8B C7                        mov rax, r15
0033587B  48 33 02                        xor rax, qword ptr [rdx]
0033587E  49 23 C3                        and rax, r11
00335881  49 33 C7                        xor rax, r15
00335884  48 89 02                        mov qword ptr [rdx], rax
00335887  4C 89 7E 18                     mov qword ptr [rsi + 0x18], r15
0033588B  49 8B 01                        mov rax, qword ptr [r9]
0033588E  48 23 C1                        and rax, rcx
00335891  49 0B C6                        or rax, r14
00335894  49 89 01                        mov qword ptr [r9], rax
00335897  F0 48 FF 06                     lock inc qword ptr [rsi]
0033589B  44 8B 85 88 00 00 00            mov r8d, dword ptr [rbp + 0x88]
003358A2  44 8B 75 78                     mov r14d, dword ptr [rbp + 0x78]
003358A6  45 85 C0                        test r8d, r8d
003358A9  0F 84 CB 02 00 00               je 0x140335b7a
003358AF  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
003358B4  48 83 F9 01                     cmp rcx, 1
003358B8  0F 85 A4 04 00 00               jne 0x140335d62
003358BE  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
003358C3  F0 48 FF 00                     lock inc qword ptr [rax]
003358C7  F6 05 38 12 C9 00 01            test byte ptr [rip + 0xc91238], 1
003358CE  0F 85 07 06 00 00               jne 0x140335edb
003358D4  89 5E 20                        mov dword ptr [rsi + 0x20], ebx
003358D7  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
003358DC  41 0F BA E6 0D                  bt r14d, 0xd
003358E1  0F 82 37 04 00 00               jb 0x140335d1e
003358E7  41 83 F8 01                     cmp r8d, 1
003358EB  0F 84 83 00 00 00               je 0x140335974
003358F1  4D 85 E4                        test r12, r12
003358F4  0F 84 DF FB FF FF               je 0x1403354d9
003358FA  41 0F BA E6 09                  bt r14d, 9
003358FF  0F 82 D4 FB FF FF               jb 0x1403354d9
00335905  F6 05 7C 11 C9 00 30            test byte ptr [rip + 0xc9117c], 0x30
0033590C  0F 84 C7 FB FF FF               je 0x1403354d9
00335912  83 7C 24 30 01                  cmp dword ptr [rsp + 0x30], 1
00335917  0F 84 FB 09 00 00               je 0x140336318
0033591D  41 39 5C 24 04                  cmp dword ptr [r12 + 4], ebx
00335922  0F 85 B1 FB FF FF               jne 0x1403354d9
00335928  45 33 C0                        xor r8d, r8d
0033592B  33 D2                           xor edx, edx
0033592D  49 8B CC                        mov rcx, r12
00335930  E8 DB 99 00 00                  call 0x14033f310
00335935  E9 9F FB FF FF                  jmp 0x1403354d9
0033593A  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
0033593D  B9 03 00 00 00                  mov ecx, 3
00335942  C1 E8 1B                        shr eax, 0x1b
00335945  44 8B C1                        mov r8d, ecx
00335948  83 E0 03                        and eax, 3
0033594B  44 2B C0                        sub r8d, eax
0033594E  44 3B C1                        cmp r8d, ecx
00335951  44 0F 44 C1                     cmove r8d, ecx
00335955  E9 DF F6 FF FF                  jmp 0x140335039
0033595A  45 33 C9                        xor r9d, r9d
0033595D  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00335962  4D 8B C7                        mov r8, r15
00335965  BA 80 51 00 00                  mov edx, 0x5180
0033596A  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
0033596E  E8 ED 7C 1C 00                  call 0x1404fd660
00335973  CC                              int3
00335974  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00335979  8B 81 30 42 00 00               mov eax, dword ptr [rcx + 0x4230]
0033597F  85 C0                           test eax, eax
00335981  0F 85 6A FF FF FF               jne 0x1403358f1
00335987  44 8D 78 40                     lea r15d, [rax + 0x40]
0033598B  4C 8B F3                        mov r14, rbx
0033598E  4D 85 ED                        test r13, r13
00335991  0F 84 8A 06 00 00               je 0x140336021
00335997  8B 41 04                        mov eax, dword ptr [rcx + 4]
0033599A  A8 20                           test al, 0x20
0033599C  0F 85 B3 00 00 00               jne 0x140335a55
003359A2  41 BF 00 04 00 00               mov r15d, 0x400
003359A8  49 8D BD 80 DF 00 00            lea rdi, [r13 + 0xdf80]
003359AF  41 BE 00 00 10 00               mov r14d, 0x100000
003359B5  49 8B CD                        mov rcx, r13
003359B8  48 3B CF                        cmp rcx, rdi
003359BB  0F 83 94 00 00 00               jae 0x140335a55
003359C1  48 2B F9                        sub rdi, rcx
003359C4  48 8D B1 10 0F 00 00            lea rsi, [rcx + 0xf10]
003359CB  48 FF CF                        dec rdi
003359CE  48 B8 CB 21 7B 17 E9 D7 39 25   movabs rax, 0x2539d7e9177b21cb
003359D8  48 F7 E7                        mul rdi
003359DB  48 2B FA                        sub rdi, rdx
003359DE  48 D1 EF                        shr rdi, 1
003359E1  48 03 FA                        add rdi, rdx
003359E4  48 C1 EF 0F                     shr rdi, 0xf
003359E8  48 FF C7                        inc rdi
003359EB  0F B6 86 B0 2C 00 00            movzx eax, byte ptr [rsi + 0x2cb0]
003359F2  84 C0                           test al, al
003359F4  75 4D                           jne 0x140335a43
003359F6  4C 8D 25 63 C2 CD FF            lea r12, [rip - 0x323d9d]
003359FD  41 BB 03 00 00 00               mov r11d, 3
00335A03  49 8B D4                        mov rdx, r12
00335A06  4C 8D 86 00 F1 FF FF            lea r8, [rsi - 0xf00]
00335A0D  45 8B D3                        mov r10d, r11d
00335A10  4C 8B CB                        mov r9, rbx
00335A13  48 8B 02                        mov rax, qword ptr [rdx]
00335A16  48 8D 52 08                     lea rdx, [rdx + 8]
00335A1A  49 8B 08                        mov rcx, qword ptr [r8]
00335A1D  4D 8D 80 00 05 00 00            lea r8, [r8 + 0x500]
00335A24  48 0F AF C8                     imul rcx, rax
00335A28  4C 03 C9                        add r9, rcx
00335A2B  49 83 EA 01                     sub r10, 1
00335A2F  75 E2                           jne 0x140335a13
00335A31  4D 85 ED                        test r13, r13
00335A34  0F 84 4F 04 00 00               je 0x140335e89
00335A3A  4D 3B CF                        cmp r9, r15
00335A3D  0F 83 74 01 00 00               jae 0x140335bb7
00335A43  48 81 C6 80 DF 00 00            add rsi, 0xdf80
00335A4A  48 83 EF 01                     sub rdi, 1
00335A4E  75 9B                           jne 0x1403359eb
00335A50  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00335A55  44 8B 75 78                     mov r14d, dword ptr [rbp + 0x78]
00335A59  E9 93 FE FF FF                  jmp 0x1403358f1
00335A5E  8B 05 F4 83 BD 00               mov eax, dword ptr [rip + 0xbd83f4]
00335A64  85 C0                           test eax, eax
00335A66  0F 85 E8 FB FF FF               jne 0x140335654
00335A6C  B2 FF                           mov dl, 0xff
00335A6E  48 8D 4E 20                     lea rcx, [rsi + 0x20]
00335A72  E8 F9 DF FE FF                  call 0x140323a70
00335A77  E9 36 FC FF FF                  jmp 0x1403356b2
00335A7C  48 0B C1                        or rax, rcx
00335A7F  E9 DF F6 FF FF                  jmp 0x140335163
00335A84  48 83 E0 EF                     and rax, 0xffffffffffffffef
00335A88  E9 8E F6 FF FF                  jmp 0x14033511b
00335A8D  49 8B 41 18                     mov rax, qword ptr [r9 + 0x18]
00335A91  48 B9 FF FF FF FF 3F FF FF FF   movabs rcx, 0xffffff3fffffffff
00335A9B  48 23 C1                        and rax, rcx
00335A9E  49 0B C6                        or rax, r14
00335AA1  49 89 41 18                     mov qword ptr [r9 + 0x18], rax
00335AA5  49 8B 01                        mov rax, qword ptr [r9]
00335AA8  48 23 C1                        and rax, rcx
00335AAB  49 0B C6                        or rax, r14
00335AAE  49 89 01                        mov qword ptr [r9], rax
00335AB1  4C 89 7E 10                     mov qword ptr [rsi + 0x10], r15
00335AB5  4C 89 7E 18                     mov qword ptr [rsi + 0x18], r15
00335AB9  E9 D9 FD FF FF                  jmp 0x140335897
00335ABE  4C 3B 7E 10                     cmp r15, qword ptr [rsi + 0x10]
00335AC2  0F 82 43 F5 FF FF               jb 0x14033500b
00335AC8  8D 4A 01                        lea ecx, [rdx + 1]
00335ACB  E9 0B F5 FF FF                  jmp 0x140334fdb
00335AD0  F7 45 78 00 04 00 00            test dword ptr [rbp + 0x78], 0x400
00335AD7  0F 85 51 FD FF FF               jne 0x14033582e
00335ADD  4C 8D 14 40                     lea r10, [rax + rax*2]
00335AE1  49 C1 E2 04                     shl r10, 4
00335AE5  49 8B C5                        mov rax, r13
00335AE8  4C 03 D0                        add r10, rax
00335AEB  48 B9 FF FF FF FF 3F FF FF FF   movabs rcx, 0xffffff3fffffffff
00335AF5  49 8B 41 18                     mov rax, qword ptr [r9 + 0x18]
00335AF9  49 BB 00 00 00 00 00 FF FF FF   movabs r11, 0xffffff0000000000
00335B03  48 23 C1                        and rax, rcx
00335B06  49 0B C6                        or rax, r14
00335B09  49 89 41 18                     mov qword ptr [r9 + 0x18], rax
00335B0D  49 8B 52 18                     mov rdx, qword ptr [r10 + 0x18]
00335B11  48 8B CA                        mov rcx, rdx
00335B14  48 8B C2                        mov rax, rdx
00335B17  49 33 CF                        xor rcx, r15
00335B1A  49 23 CB                        and rcx, r11
00335B1D  49 33 CF                        xor rcx, r15
00335B20  F0 49 0F B1 4A 18               lock cmpxchg qword ptr [r10 + 0x18], rcx
00335B26  4C 8B C0                        mov r8, rax
00335B29  48 3B D0                        cmp rdx, rax
00335B2C  74 1F                           je 0x140335b4d
00335B2E  66 90                           nop
00335B30  49 8B C8                        mov rcx, r8
00335B33  4D 33 C7                        xor r8, r15
00335B36  4D 23 C3                        and r8, r11
00335B39  48 8B C1                        mov rax, rcx
00335B3C  4D 33 C7                        xor r8, r15
00335B3F  F0 4D 0F B1 42 18               lock cmpxchg qword ptr [r10 + 0x18], r8
00335B45  4C 8B C0                        mov r8, rax
00335B48  48 3B C8                        cmp rcx, rax
00335B4B  75 E3                           jne 0x140335b30
00335B4D  4C 89 7E 10                     mov qword ptr [rsi + 0x10], r15
00335B51  49 8B C5                        mov rax, r13
00335B54  4C 2B D0                        sub r10, rax
00335B57  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
00335B61  49 C1 FA 04                     sar r10, 4
00335B65  4D 0F AF D0                     imul r10, r8
00335B69  49 8B C2                        mov rax, r10
00335B6C  49 33 01                        xor rax, qword ptr [r9]
00335B6F  49 23 C3                        and rax, r11
00335B72  49 33 C2                        xor rax, r10
00335B75  E9 1A FD FF FF                  jmp 0x140335894
00335B7A  41 0F BA E6 0A                  bt r14d, 0xa
00335B7F  0F 82 2A FD FF FF               jb 0x1403358af
00335B85  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00335B8A  48 83 F9 01                     cmp rcx, 1
00335B8E  0F 85 CE 01 00 00               jne 0x140335d62
00335B94  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00335B99  8B C7                           mov eax, edi
00335B9B  48 C1 E8 12                     shr rax, 0x12
00335B9F  83 E0 03                        and eax, 3
00335BA2  40 0F B6 CF                     movzx ecx, dil
00335BA6  48 8B 84 C2 00 14 00 00         mov rax, qword ptr [rdx + rax*8 + 0x1400]
00335BAE  48 FF 04 C8                     inc qword ptr [rax + rcx*8]
00335BB2  E9 07 FD FF FF                  jmp 0x1403358be
00335BB7  4D 85 F6                        test r14, r14
00335BBA  74 3B                           je 0x140335bf7
00335BBC  4C 8B CB                        mov r9, rbx
00335BBF  4C 8D 86 F8 F0 FF FF            lea r8, [rsi - 0xf08]
00335BC6  49 8B D4                        mov rdx, r12
00335BC9  4D 8B D3                        mov r10, r11
00335BCC  0F 1F 40 00                     nop dword ptr [rax]
00335BD0  48 8B 02                        mov rax, qword ptr [rdx]
00335BD3  48 8D 52 08                     lea rdx, [rdx + 8]
00335BD7  49 8B 08                        mov rcx, qword ptr [r8]
00335BDA  4D 8D 80 00 05 00 00            lea r8, [r8 + 0x500]
00335BE1  48 0F AF C8                     imul rcx, rax
00335BE5  4C 03 C9                        add r9, rcx
00335BE8  49 83 EA 01                     sub r10, 1
00335BEC  75 E2                           jne 0x140335bd0
00335BEE  4D 3B CE                        cmp r9, r14
00335BF1  0F 83 4C FE FF FF               jae 0x140335a43
00335BF7  48 8D 8E A0 2C 00 00            lea rcx, [rsi + 0x2ca0]
00335BFE  4D 85 ED                        test r13, r13
00335C01  0F 84 03 04 00 00               je 0x14033600a
00335C07  41 B5 11                        mov r13b, 0x11
00335C0A  E8 71 32 F1 FF                  call 0x140248e80
00335C0F  48 8B 8E 98 2C 00 00            mov rcx, qword ptr [rsi + 0x2c98]
00335C16  48 85 C9                        test rcx, rcx
00335C19  74 17                           je 0x140335c32
00335C1B  0F B6 96 B0 2C 00 00            movzx edx, byte ptr [rsi + 0x2cb0]
00335C22  84 D2                           test dl, dl
00335C24  75 0C                           jne 0x140335c32
00335C26  C6 86 B0 2C 00 00 01            mov byte ptr [rsi + 0x2cb0], 1
00335C2D  E8 8E 62 F9 FF                  call 0x1402cbec0
00335C32  41 0F B6 D5                     movzx edx, r13b
00335C36  48 8D 8E A0 2C 00 00            lea rcx, [rsi + 0x2ca0]
00335C3D  E8 7E 26 F1 FF                  call 0x1402482c0
00335C42  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
00335C47  E9 F7 FD FF FF                  jmp 0x140335a43
00335C4C  83 FF 0A                        cmp edi, 0xa
00335C4F  0F 84 39 F3 FF FF               je 0x140334f8e
00335C55  41 0F BA E2 0B                  bt r10d, 0xb
00335C5A  0F 82 79 F8 FF FF               jb 0x1403354d9
00335C60  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00335C64  89 45 70                        mov dword ptr [rbp + 0x70], eax
00335C67  C1 E8 10                        shr eax, 0x10
00335C6A  24 F8                           and al, 0xf8
00335C6C  41 0A C4                        or al, r12b
00335C6F  88 45 72                        mov byte ptr [rbp + 0x72], al
00335C72  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
00335C75  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00335C79  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00335C7D  48 8B 0D 04 A4 AF 00            mov rcx, qword ptr [rip + 0xafa404]
00335C84  48 C1 E8 2B                     shr rax, 0x2b
00335C88  25 FF 03 00 00                  and eax, 0x3ff
00335C8D  48 8B 1C C1                     mov rbx, qword ptr [rcx + rax*8]
00335C91  49 8B CE                        mov rcx, r14
00335C94  E8 97 B2 F7 FF                  call 0x1402b0f30
00335C99  8B C8                           mov ecx, eax
00335C9B  48 69 C1 80 DF 00 00            imul rax, rcx, 0xdf80
00335CA2  48 69 D7 E8 00 00 00            imul rdx, rdi, 0xe8
00335CA9  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00335CAD  48 05 68 3C 00 00               add rax, 0x3c68
00335CB3  48 03 D0                        add rdx, rax
00335CB6  48 03 CA                        add rcx, rdx
00335CB9  49 8B D6                        mov rdx, r14
00335CBC  E8 9F AD F6 FF                  call 0x1402a0a60
00335CC1  E9 13 F8 FF FF                  jmp 0x1403354d9
00335CC6  48 8B C3                        mov rax, rbx
00335CC9  E9 4D F4 FF FF                  jmp 0x14033511b
00335CCE  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00335CD8  48 8B C0                        mov rax, rax
00335CDB  48 8B CF                        mov rcx, rdi
00335CDE  48 2B C8                        sub rcx, rax
00335CE1  48 C1 F9 04                     sar rcx, 4
00335CE5  49 0F AF C8                     imul rcx, r8
00335CE9  E8 5A 3E F8 FF                  call 0x1402b9b48
00335CEE  44 8B 55 78                     mov r10d, dword ptr [rbp + 0x78]
00335CF2  44 0F B6 C8                     movzx r9d, al
00335CF6  E9 29 F3 FF FF                  jmp 0x140335024
00335CFB  85 D2                           test edx, edx
00335CFD  0F 85 F7 05 00 00               jne 0x1403362fa
00335D03  4C 8B CE                        mov r9, rsi
00335D06  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00335D0B  4D 8B C7                        mov r8, r15
00335D0E  BA 80 51 00 00                  mov edx, 0x5180
00335D13  B9 1A 00 00 00                  mov ecx, 0x1a
00335D18  E8 43 79 1C 00                  call 0x1404fd660
00335D1D  CC                              int3
00335D1E  49 8B 85 60 3B 00 00            mov rax, qword ptr [r13 + 0x3b60]
00335D25  48 8D 50 FF                     lea rdx, [rax - 1]
00335D29  48 8B CA                        mov rcx, rdx
00335D2C  48 33 C8                        xor rcx, rax
00335D2F  48 81 E1 00 00 FF FF            and rcx, 0xffffffffffff0000
00335D36  48 33 CA                        xor rcx, rdx
00335D39  66 85 C9                        test cx, cx
00335D3C  75 14                           jne 0x140335d52
00335D3E  48 8D 91 00 00 01 00            lea rdx, [rcx + 0x10000]
00335D45  48 33 D1                        xor rdx, rcx
00335D48  48 81 E2 00 00 FF FF            and rdx, 0xffffffffffff0000
00335D4F  48 33 CA                        xor rcx, rdx
00335D52  F0 49 0F B1 8D 60 3B 00 00      lock cmpxchg qword ptr [r13 + 0x3b60], rcx
00335D5B  75 C8                           jne 0x140335d25
00335D5D  E9 85 FB FF FF                  jmp 0x1403358e7
00335D62  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00335D67  F0 48 01 08                     lock add qword ptr [rax], rcx
00335D6B  E9 57 FB FF FF                  jmp 0x1403358c7
00335D70  41 FF C0                        inc r8d
00335D73  E9 31 F6 FF FF                  jmp 0x1403353a9
00335D78  49 81 FF 00 00 10 00            cmp r15, 0x100000
00335D7F  0F 83 10 F3 FF FF               jae 0x140335095
00335D85  0F BA EF 0F                     bts edi, 0xf
00335D89  E9 07 F3 FF FF                  jmp 0x140335095
00335D8E  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00335D92  89 45 70                        mov dword ptr [rbp + 0x70], eax
00335D95  C1 E8 10                        shr eax, 0x10
00335D98  24 FD                           and al, 0xfd
00335D9A  0C 05                           or al, 5
00335D9C  88 45 72                        mov byte ptr [rbp + 0x72], al
00335D9F  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
00335DA2  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00335DA6  E9 2E F7 FF FF                  jmp 0x1403354d9
00335DAB  48 85 D2                        test rdx, rdx
00335DAE  0F 85 63 04 00 00               jne 0x140336217
00335DB4  49 8B CA                        mov rcx, r10
00335DB7  41 D3 E3                        shl r11d, cl
00335DBA  41 FF CB                        dec r11d
00335DBD  E9 13 F7 FF FF                  jmp 0x1403354d5
00335DC2  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00335DC7  83 FA 03                        cmp edx, 3
00335DCA  0F 84 DB F7 FF FF               je 0x1403355ab
00335DD0  48 C7 44 24 58 01 00 00 00      mov qword ptr [rsp + 0x58], 1
00335DD9  B8 01 00 00 00                  mov eax, 1
00335DDE  E9 C8 F7 FF FF                  jmp 0x1403355ab
00335DE3  4C 8B F6                        mov r14, rsi
00335DE6  F0 4D 0F C1 B2 00 49 00 00      lock xadd qword ptr [r10 + 0x4900], r14
00335DEF  49 8B C6                        mov rax, r14
00335DF2  4C 03 F6                        add r14, rsi
00335DF5  48 3D 20 04 00 00               cmp rax, 0x420
00335DFB  0F 82 9F 02 00 00               jb 0x1403360a0
00335E01  49 8B 8A 08 41 00 00            mov rcx, qword ptr [r10 + 0x4108]
00335E08  4C 3B F1                        cmp r14, rcx
00335E0B  76 0B                           jbe 0x140335e18
00335E0D  49 8B C6                        mov rax, r14
00335E10  48 2B C6                        sub rax, rsi
00335E13  48 3B C1                        cmp rax, rcx
00335E16  76 1C                           jbe 0x140335e34
00335E18  49 8B 82 00 41 00 00            mov rax, qword ptr [r10 + 0x4100]
00335E1F  4C 3B F0                        cmp r14, rax
00335E22  0F 86 4A F7 FF FF               jbe 0x140335572
00335E28  4C 2B F6                        sub r14, rsi
00335E2B  4C 3B F0                        cmp r14, rax
00335E2E  0F 87 3E F7 FF FF               ja 0x140335572
00335E34  49 8B CA                        mov rcx, r10
00335E37  E8 C8 69 08 00                  call 0x1403bc804
00335E3C  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
00335E41  E9 2C F7 FF FF                  jmp 0x140335572
00335E46  4A 8D 04 55 00 00 00 00         lea rax, [r10*2]
00335E4E  49 03 C5                        add rax, r13
00335E51  49 8B 8C C1 30 3B 00 00         mov rcx, qword ptr [r9 + rax*8 + 0x3b30]
00335E59  4C 03 E1                        add r12, rcx
00335E5C  E9 FA F3 FF FF                  jmp 0x14033525b
00335E61  8B 05 51 0C C9 00               mov eax, dword ptr [rip + 0xc90c51]
00335E67  A8 40                           test al, 0x40
00335E69  0F 84 2D F8 FF FF               je 0x14033569c
00335E6F  E8 1C 96 FD FF                  call 0x14030f490
00335E74  84 C0                           test al, al
00335E76  0F 84 20 F8 FF FF               je 0x14033569c
00335E7C  41 8B CF                        mov ecx, r15d
00335E7F  E8 DC 95 FD FF                  call 0x14030f460
00335E84  E9 15 F8 FF FF                  jmp 0x14033569e
00335E89  48 8B 06                        mov rax, qword ptr [rsi]
00335E8C  4C 03 C8                        add r9, rax
00335E8F  E9 A6 FB FF FF                  jmp 0x140335a3a
00335E94  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00335E99  45 8B C2                        mov r8d, r10d
00335E9C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00335EA1  E8 DA 90 00 00                  call 0x14033ef80
00335EA6  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00335EAA  25 00 00 F8 1F                  and eax, 0x1ff80000
00335EAF  48 3D 00 00 00 10               cmp rax, 0x10000000
00335EB5  0F 85 32 F9 FF FF               jne 0x1403357ed
00335EBB  48 0F BA 25 6C 0C C9 00 25      bt qword ptr [rip + 0xc90c6c], 0x25
00335EC4  0F 83 23 F9 FF FF               jae 0x1403357ed
00335ECA  45 33 C0                        xor r8d, r8d
00335ECD  EB 47                           jmp 0x140335f16
00335ECF  49 FF C2                        inc r10
00335ED2  49 83 C3 08                     add r11, 8
00335ED6  E9 BE F4 FF FF                  jmp 0x140335399
00335EDB  8B 05 77 7F BD 00               mov eax, dword ptr [rip + 0xbd7f77]
00335EE1  85 C0                           test eax, eax
00335EE3  0F 85 EB F9 FF FF               jne 0x1403358d4
00335EE9  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
00335EED  48 8D 4E 20                     lea rcx, [rsi + 0x20]
00335EF1  E8 4E B0 F8 FF                  call 0x1402c0f44
00335EF6  44 8B 85 88 00 00 00            mov r8d, dword ptr [rbp + 0x88]
00335EFD  E9 D5 F9 FF FF                  jmp 0x1403358d7
00335F02  49 81 C4 80 DF 00 00            add r12, 0xdf80
00335F09  FF C0                           inc eax
00335F0B  E9 7B F4 FF FF                  jmp 0x14033538b
00335F10  41 B8 01 00 00 00               mov r8d, 1
00335F16  41 B9 08 00 00 00               mov r9d, 8
00335F1C  49 8B D7                        mov rdx, r15
00335F1F  49 8B CE                        mov rcx, r14
00335F22  E8 FD 46 04 00                  call 0x14037a624
00335F27  4C 8B E0                        mov r12, rax
00335F2A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00335F2F  E9 C1 F8 FF FF                  jmp 0x1403357f5
00335F34  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00335F38  4C 8D 45 A8                     lea r8, [rbp - 0x58]
00335F3C  8B D1                           mov edx, ecx
00335F3E  49 8B CE                        mov rcx, r14
00335F41  E8 DA F4 F4 FF                  call 0x140285420
00335F46  85 C0                           test eax, eax
00335F48  74 31                           je 0x140335f7b
00335F4A  48 C1 FF 04                     sar rdi, 4
00335F4E  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
00335F58  49 0F AF F8                     imul rdi, r8
00335F5C  45 33 C0                        xor r8d, r8d
00335F5F  48 8B CF                        mov rcx, rdi
00335F62  A8 20                           test al, 0x20
00335F64  0F 85 2A 01 00 00               jne 0x140336094
00335F6A  48 8D 55 A8                     lea rdx, [rbp - 0x58]
00335F6E  E8 5D 1A 0D 00                  call 0x1404079d0
00335F73  85 C0                           test eax, eax
00335F75  0F 88 53 03 00 00               js 0x1403362ce
00335F7B  33 D2                           xor edx, edx
00335F7D  49 8B CE                        mov rcx, r14
00335F80  E8 CB C3 F6 FF                  call 0x1402a2350
00335F85  44 8B 55 78                     mov r10d, dword ptr [rbp + 0x78]
00335F89  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
00335F93  49 B9 00 00 00 00 00 01 00 00   movabs r9, 0x10000000000
00335F9D  E9 8F EE FF FF                  jmp 0x140334e31
00335FA2  45 33 C0                        xor r8d, r8d
00335FA5  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00335FAA  E8 D1 8F 00 00                  call 0x14033ef80
00335FAF  E9 39 F8 FF FF                  jmp 0x1403357ed
00335FB4  49 81 FF A0 00 00 00            cmp r15, 0xa0
00335FBB  0F 84 51 02 00 00               je 0x140336212
00335FC1  49 81 FF 20 04 00 00            cmp r15, 0x420
00335FC8  0F 84 31 02 00 00               je 0x1403361ff
00335FCE  49 83 FF 22                     cmp r15, 0x22
00335FD2  0F 84 D2 01 00 00               je 0x1403361aa
00335FD8  49 81 FF 20 01 00 00            cmp r15, 0x120
00335FDF  0F 85 6C F5 FF FF               jne 0x140335551
00335FE5  41 8B D0                        mov edx, r8d
00335FE8  49 8B CA                        mov rcx, r10
00335FEB  E8 F0 57 08 00                  call 0x1403bb7e0
00335FF0  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
00335FF5  E9 57 F5 FF FF                  jmp 0x140335551
00335FFA  44 8B 6C 24 30                  mov r13d, dword ptr [rsp + 0x30]
00335FFF  41 B8 01 00 00 00               mov r8d, 1
00336005  E9 17 F5 FF FF                  jmp 0x140335521
0033600A  E8 81 26 F1 FF                  call 0x140248690
0033600F  44 0F B6 E8                     movzx r13d, al
00336013  E9 F7 FB FF FF                  jmp 0x140335c0f
00336018  45 0F B6 C4                     movzx r8d, r12b
0033601C  E9 FB F5 FF FF                  jmp 0x14033561c
00336021  0F B7 05 D8 EF C8 00            movzx eax, word ptr [rip + 0xc8efd8]
00336028  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
0033602C  48 69 F8 80 DF 00 00            imul rdi, rax, 0xdf80
00336033  48 03 F9                        add rdi, rcx
00336036  E9 7D F9 FF FF                  jmp 0x1403359b8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003354FB(void)
{
    __int64 v_rbx;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_rbx = (v_rbx) & (-17);
}
```

## 5. (Beta) C Style

```c
void sub_003354FB(void)
{
    int64_t local_rbx;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p64;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;

    local_rbx = (local_rbx) & (-17);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003354FB&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
