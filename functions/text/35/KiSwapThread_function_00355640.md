# KiSwapThread

- RVA: `0x00355640`–`0x00355C5A` (길이 `1,562` bytes)
- VA: `0x0000000140355640`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000792F0`
- 디코드: `365`개 명령, `1,562/1,562` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00355675` → [KiAbProcessPreContextSwitch](../21/KiAbProcessPreContextSwitch_function_0021D420.md) (function, `0x0021D420`)
- `0x00355680` → [KiCaptureTotalCyclesCurrentThread](../37/KiCaptureTotalCyclesCurrentThread_function_0037CB90.md) (function, `0x0037CB90`)
- `0x00355702` → [KiUpdateGroupSchedulingRank](KiUpdateGroupSchedulingRank_function_00355F50.md) (function, `0x00355F50`)
- `0x0035571C` → [KiSearchForNewThread](KiSearchForNewThread_function_00355C98.md) (function, `0x00355C98`)
- `0x00355724` → [Feature_HeteroRescheduleFixes__private_IsEnabledNoReportingNoInline](Feature_HeteroRescheduleFixes__private_IsEnabledNoReportingNoInline_function_00355C60.md) (function, `0x00355C60`)
- `0x00355795` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003557A0` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00355883` → [KiSwapContext](../6B/KiSwapContext_function_006B9740.md) (function, `0x006B9740`)
- `0x0035588E` → [KiAbProcessPostContextSwitch](../24/KiAbProcessPostContextSwitch_function_00248790.md) (function, `0x00248790`)
- `0x003558C9` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00355919` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0035592E` → [KiDeliverApc](../25/KiDeliverApc_function_00250F20.md) (function, `0x00250F20`)
- `0x00355984` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x0035598C` → [KiSendHeteroRescheduleIntRequest](KiSendHeteroRescheduleIntRequest_function_00354120.md) (function, `0x00354120`)
- `0x0035599B` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x003559B2` → [KiCancelTimer](../3D/KiCancelTimer_function_003D3A80.md) (function, `0x003D3A80`)
- `0x00355A13` → [KiResumeThreadCycleAccumulation](../30/KiResumeThreadCycleAccumulation_function_00309BC4.md) (function, `0x00309BC4`)
- `0x00355A1B` → [KiAbProcessPostContextSwitch](../24/KiAbProcessPostContextSwitch_function_00248790.md) (function, `0x00248790`)
- `0x00355ABC` → [EtwpCoverageSamplerContextSwap](../4F/EtwpCoverageSamplerContextSwap_function_004FC9F8.md) (function, `0x004FC9F8`)
- `0x00355ACE` → [EtwpLogContextSwapEvent](../41/EtwpLogContextSwapEvent_function_004175F0.md) (function, `0x004175F0`)
- `0x00355AFF` → [EtwpLogContextSwapEvent](../41/EtwpLogContextSwapEvent_function_004175F0.md) (function, `0x004175F0`)
- `0x00355B33` → [KiSwapContext](../6B/KiSwapContext_function_006B9740.md) (function, `0x006B9740`)
- `0x00355B3E` → [KiAbProcessPostContextSwitch](../24/KiAbProcessPostContextSwitch_function_00248790.md) (function, `0x00248790`)
- `0x00355B56` → [KiProcessThreadWaitList](../25/KiProcessThreadWaitList_function_00252CC0.md) (function, `0x00252CC0`)
- `0x00355B77` → [EtwpLogContextSwapEvent](../41/EtwpLogContextSwapEvent_function_004175F0.md) (function, `0x004175F0`)
- `0x00355BAB` → [EtwpLogContextSwapEvent](../41/EtwpLogContextSwapEvent_function_004175F0.md) (function, `0x004175F0`)
- `0x00355BBA` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x00355BC7` → [KiProcessScbTracingList](../45/KiProcessScbTracingList_function_0045A500.md) (function, `0x0045A500`)
- `0x00355BD6` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x00355C0D` → [KiInsertDeferredPreemptionApc](../30/KiInsertDeferredPreemptionApc_function_0030A8E8.md) (function, `0x0030A8E8`)
- `0x00355C17` → [PsGetEffectiveServerSilo](../22/PsGetEffectiveServerSilo_function_002257F0.md) (function, `0x002257F0`)
- `0x00355C24` → [PsGetEffectiveServerSilo](../22/PsGetEffectiveServerSilo_function_002257F0.md) (function, `0x002257F0`)

### Direct callers
- [KiCommitThreadWait](../20/KiCommitThreadWait_function_0020DFE0.md) at `0x0020E200`
- [KeTerminateThread](KeTerminateThread_function_00355138.md) at `0x00355387`
- [KiInSwapSingleProcess](KiInSwapSingleProcess_function_00355474.md) at `0x00355594`
- [KiExecuteDpcDelegate](../5C/KiExecuteDpcDelegate_function_005C8620.md) at `0x005C86AB`

### Static image references
- `0x00355772` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0035578B` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x003557A7` → RVA `0x00FC6B78` (`ALMOSTRO`; read)
- `0x003558B9` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00355962` → RVA `0x00FC6D04` (`ALMOSTRO`; read)
- `0x00355A2D` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x00355A79` → RVA `0x00FCF940` (`CACHEALI`; read)
- `0x00355AA3` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0035572F` → [sub_006E2870](../6E/Unknown_function_006E2870.md) (`tail-transfer`)
  - `0x00355C34` → [sub_006E2870 + 0x53](../6E/Unknown_function_006E2870.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00355640  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00355645  55                              push rbp
00355646  56                              push rsi
00355647  57                              push rdi
00355648  41 54                           push r12
0035564A  41 55                           push r13
0035564C  41 56                           push r14
0035564E  41 57                           push r15
00355650  48 83 EC 30                     sub rsp, 0x30
00355654  48 83 BA 08 2D 00 00 00         cmp qword ptr [rdx + 0x2d08], 0
0035565C  4D 8B E0                        mov r12, r8
0035565F  4C 8B F2                        mov r14, rdx
00355662  4C 8B E9                        mov r13, rcx
00355665  BF 01 00 00 00                  mov edi, 1
0035566A  0F 85 D8 04 00 00               jne 0x140355b48
00355670  33 D2                           xor edx, edx
00355672  49 8B CD                        mov rcx, r13
00355675  E8 A6 7D EC FF                  call 0x14021d420
0035567A  49 8B D5                        mov rdx, r13
0035567D  49 8B CE                        mov rcx, r14
00355680  E8 0B 75 02 00                  call 0x14037cb90
00355685  41 8B 4D 54                     mov ecx, dword ptr [r13 + 0x54]
00355689  41 8B 45 50                     mov eax, dword ptr [r13 + 0x50]
0035568D  D1 E9                           shr ecx, 1
0035568F  D1 E8                           shr eax, 1
00355691  03 C8                           add ecx, eax
00355693  45 33 FF                        xor r15d, r15d
00355696  41 89 4D 54                     mov dword ptr [r13 + 0x54], ecx
0035569A  45 89 7D 50                     mov dword ptr [r13 + 0x50], r15d
0035569E  49 8B C6                        mov rax, r14
003556A1  48 83 E0 FE                     and rax, 0xfffffffffffffffe
003556A5  48 0B C7                        or rax, rdi
003556A8  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
003556AD  49 8B 86 58 8E 00 00            mov rax, qword ptr [r14 + 0x8e58]
003556B4  0F B6 08                        movzx ecx, byte ptr [rax]
003556B7  48 8D 70 08                     lea rsi, [rax + 8]
003556BB  84 C9                           test cl, cl
003556BD  74 2B                           je 0x1403556ea
003556BF  8B E9                           mov ebp, ecx
003556C1  48 8B 1E                        mov rbx, qword ptr [rsi]
003556C4  41 8B FF                        mov edi, r15d
003556C7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
003556D0  F0 48 0F BA 6B 30 00            lock bts qword ptr [rbx + 0x30], 0
003556D7  0F 82 93 00 00 00               jb 0x140355770
003556DD  48 83 C6 08                     add rsi, 8
003556E1  48 83 ED 01                     sub rbp, 1
003556E5  75 DA                           jne 0x1403556c1
003556E7  8D 7D 01                        lea edi, [rbp + 1]
003556EA  48 8D 44 24 78                  lea rax, [rsp + 0x78]
003556EF  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
003556F4  45 33 C9                        xor r9d, r9d
003556F7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003556FC  49 8B D6                        mov rdx, r14
003556FF  49 8B CD                        mov rcx, r13
00355702  E8 49 08 00 00                  call 0x140355f50
00355707  4C 39 7C 24 78                  cmp qword ptr [rsp + 0x78], r15
0035570C  0F 85 A3 04 00 00               jne 0x140355bb5
00355712  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00355717  33 D2                           xor edx, edx
00355719  49 8B CE                        mov rcx, r14
0035571C  E8 77 05 00 00                  call 0x140355c98
00355721  48 8B E8                        mov rbp, rax
00355724  E8 37 05 00 00                  call 0x140355c60
00355729  49 8D 5E 18                     lea rbx, [r14 + 0x18]
0035572D  85 C0                           test eax, eax
0035572F  0F 84 3B D1 38 00               je 0x1406e2870
00355735  48 3B 2B                        cmp rbp, qword ptr [rbx]
00355738  74 6D                           je 0x1403557a7
0035573A  49 3B ED                        cmp rbp, r13
0035573D  74 7A                           je 0x1403557b9
0035573F  0F B6 45 71                     movzx eax, byte ptr [rbp + 0x71]
00355743  84 C0                           test al, al
00355745  74 72                           je 0x1403557b9
00355747  48 8B 2B                        mov rbp, qword ptr [rbx]
0035574A  49 89 6E 08                     mov qword ptr [r14 + 8], rbp
0035574E  0F B6 85 84 01 00 00            movzx eax, byte ptr [rbp + 0x184]
00355755  3C 01                           cmp al, 1
00355757  0F 84 80 02 00 00               je 0x1403559dd
0035575D  C6 85 84 01 00 00 02            mov byte ptr [rbp + 0x184], 2
00355764  E9 8C 00 00 00                  jmp 0x1403557f5
00355769  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00355770  FF C7                           inc edi
00355772  85 3D 34 FB C6 00               test dword ptr [rip + 0xc6fb34], edi
00355778  74 11                           je 0x14035578b
0035577A  F3 90                           pause
0035577C  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
00355780  48 85 C0                        test rax, rax
00355783  0F 84 47 FF FF FF               je 0x1403556d0
00355789  EB E5                           jmp 0x140355770
0035578B  8B 05 27 13 C7 00               mov eax, dword ptr [rip + 0xc71327]
00355791  A8 40                           test al, 0x40
00355793  74 E5                           je 0x14035577a
00355795  E8 F6 9C FB FF                  call 0x14030f490
0035579A  84 C0                           test al, al
0035579C  74 DC                           je 0x14035577a
0035579E  8B CF                           mov ecx, edi
003557A0  E8 BB 9C FB FF                  call 0x14030f460
003557A5  EB D5                           jmp 0x14035577c
003557A7  44 39 3D CA 13 C7 00            cmp dword ptr [rip + 0xc713ca], r15d
003557AE  0F 85 AE 01 00 00               jne 0x140355962
003557B4  48 3B 2B                        cmp rbp, qword ptr [rbx]
003557B7  75 81                           jne 0x14035573a
003557B9  4D 89 7E 10                     mov qword ptr [r14 + 0x10], r15
003557BD  49 89 6E 08                     mov qword ptr [r14 + 8], rbp
003557C1  0F B6 85 84 01 00 00            movzx eax, byte ptr [rbp + 0x184]
003557C8  3C 01                           cmp al, 1
003557CA  0F 84 75 01 00 00               je 0x140355945
003557D0  C6 85 84 01 00 00 02            mov byte ptr [rbp + 0x184], 2
003557D7  49 8B 96 C0 00 00 00            mov rdx, qword ptr [r14 + 0xc0]
003557DE  49 8B 8E C8 00 00 00            mov rcx, qword ptr [r14 + 0xc8]
003557E5  48 8B 82 90 01 00 00            mov rax, qword ptr [rdx + 0x190]
003557EC  48 85 C1                        test rcx, rax
003557EF  0F 85 40 01 00 00               jne 0x140355935
003557F5  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
003557FA  4D 8B C7                        mov r8, r15
003557FD  4C 8B C8                        mov r9, rax
00355800  41 8B D7                        mov edx, r15d
00355803  49 83 E1 FE                     and r9, 0xfffffffffffffffe
00355807  4C 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r9
0035580F  83 E0 01                        and eax, 1
00355812  0F 84 D6 00 00 00               je 0x1403558ee
00355818  83 F8 01                        cmp eax, 1
0035581B  75 15                           jne 0x140355832
0035581D  49 8B 81 58 8E 00 00            mov rax, qword ptr [r9 + 0x8e58]
00355824  4D 8B 81 58 8E 00 00            mov r8, qword ptr [r9 + 0x8e58]
0035582B  49 83 C0 08                     add r8, 8
0035582F  0F B6 10                        movzx edx, byte ptr [rax]
00355832  85 D2                           test edx, edx
00355834  74 1C                           je 0x140355852
00355836  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00355840  8D 42 FF                        lea eax, [rdx - 1]
00355843  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
00355847  8B D0                           mov edx, eax
00355849  F0 4C 21 79 30                  lock and qword ptr [rcx + 0x30], r15
0035584E  85 C0                           test eax, eax
00355850  75 EE                           jne 0x140355840
00355852  41 0F B6 9D 86 01 00 00         movzx ebx, byte ptr [r13 + 0x186]
0035585A  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
0035585F  4C 3B ED                        cmp r13, rbp
00355862  0F 84 92 01 00 00               je 0x1403559fa
00355868  40 32 FF                        xor dil, dil
0035586B  41 F7 45 78 00 00 40 00         test dword ptr [r13 + 0x78], 0x400000
00355873  0F 85 90 02 00 00               jne 0x140355b09
00355879  44 0F B6 C3                     movzx r8d, bl
0035587D  48 8B D5                        mov rdx, rbp
00355880  49 8B CD                        mov rcx, r13
00355883  E8 B8 3E 36 00                  call 0x1406b9740
00355888  49 8B CD                        mov rcx, r13
0035588B  0F B6 F0                        movzx esi, al
0035588E  E8 FD 2E EF FF                  call 0x140248790
00355893  40 84 FF                        test dil, dil
00355896  0F 85 9D 03 00 00               jne 0x140355c39
0035589C  49 8B BD C8 00 00 00            mov rdi, qword ptr [r13 + 0xc8]
003558A3  41 0F BA 75 74 09               btr dword ptr [r13 + 0x74], 9
003558A9  0F 82 FA 00 00 00               jb 0x1403559a9
003558AF  4D 85 E4                        test r12, r12
003558B2  75 49                           jne 0x1403558fd
003558B4  40 84 F6                        test sil, sil
003558B7  75 51                           jne 0x14035590a
003558B9  83 3D 60 14 C7 00 00            cmp dword ptr [rip + 0xc71460], 0
003558C0  74 0C                           je 0x1403558ce
003558C2  44 0F 20 C1                     mov rcx, cr8
003558C6  0F B6 D3                        movzx edx, bl
003558C9  E8 CA FD 19 00                  call 0x1404f5698
003558CE  44 0F 22 C3                     mov cr8, rbx
003558D2  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
003558DA  48 8B C7                        mov rax, rdi
003558DD  48 83 C4 30                     add rsp, 0x30
003558E1  41 5F                           pop r15
003558E3  41 5E                           pop r14
003558E5  41 5D                           pop r13
003558E7  41 5C                           pop r12
003558E9  5F                              pop rdi
003558EA  5E                              pop rsi
003558EB  5D                              pop rbp
003558EC  C3                              ret
003558ED  CC                              int3
003558EE  4C 8D 84 24 88 00 00 00         lea r8, [rsp + 0x88]
003558F6  8B D7                           mov edx, edi
003558F8  E9 43 FF FF FF                  jmp 0x140355840
003558FD  49 8B 85 D0 03 00 00            mov rax, qword ptr [r13 + 0x3d0]
00355904  49 89 04 24                     mov qword ptr [r12], rax
00355908  EB AA                           jmp 0x1403558b4
0035590A  83 3D 0F 14 C7 00 00            cmp dword ptr [rip + 0xc7140f], 0
00355911  74 0B                           je 0x14035591e
00355913  44 0F 20 C1                     mov rcx, cr8
00355917  B2 01                           mov dl, 1
00355919  E8 7A FD 19 00                  call 0x1404f5698
0035591E  B8 01 00 00 00                  mov eax, 1
00355923  44 0F 22 C0                     mov cr8, rax
00355927  45 33 C0                        xor r8d, r8d
0035592A  33 D2                           xor edx, edx
0035592C  33 C9                           xor ecx, ecx
0035592E  E8 ED B5 EF FF                  call 0x140250f20
00355933  EB 84                           jmp 0x1403558b9
00355935  48 F7 D1                        not rcx
00355938  F0 48 21 8A 90 01 00 00         lock and qword ptr [rdx + 0x190], rcx
00355940  E9 B0 FE FF FF                  jmp 0x1403557f5
00355945  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0035594F  8B 00                           mov eax, dword ptr [rax]
00355951  2B 85 B4 01 00 00               sub eax, dword ptr [rbp + 0x1b4]
00355957  01 85 84 00 00 00               add dword ptr [rbp + 0x84], eax
0035595D  E9 6E FE FF FF                  jmp 0x1403557d0
00355962  44 39 3D 9B 13 C7 00            cmp dword ptr [rip + 0xc7139b], r15d
00355969  0F 85 45 FE FF FF               jne 0x1403557b4
0035596F  41 0F B6 86 BB 38 00 00         movzx eax, byte ptr [r14 + 0x38bb]
00355977  84 C0                           test al, al
00355979  0F 85 35 FE FF FF               jne 0x1403557b4
0035597F  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00355984  E8 C7 42 04 00                  call 0x140399c50
00355989  49 8B CE                        mov rcx, r14
0035598C  E8 8F E7 FF FF                  call 0x140354120
00355991  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00355996  33 D2                           xor edx, edx
00355998  49 8B CE                        mov rcx, r14
0035599B  E8 C0 93 FB FF                  call 0x14030ed60
003559A0  49 8B 6E 10                     mov rbp, qword ptr [r14 + 0x10]
003559A4  E9 0B FE FF FF                  jmp 0x1403557b4
003559A9  49 8D 8D 00 01 00 00            lea rcx, [r13 + 0x100]
003559B0  B2 01                           mov dl, 1
003559B2  E8 C9 E0 07 00                  call 0x1403d3a80
003559B7  84 C0                           test al, al
003559B9  0F 85 F0 FE FF FF               jne 0x1403558af
003559BF  49 8D 85 D0 01 00 00            lea rax, [r13 + 0x1d0]
003559C6  C6 40 11 04                     mov byte ptr [rax + 0x11], 4
003559CA  49 89 85 08 01 00 00            mov qword ptr [r13 + 0x108], rax
003559D1  49 89 85 10 01 00 00            mov qword ptr [r13 + 0x110], rax
003559D8  E9 D2 FE FF FF                  jmp 0x1403558af
003559DD  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
003559E7  8B 00                           mov eax, dword ptr [rax]
003559E9  2B 85 B4 01 00 00               sub eax, dword ptr [rbp + 0x1b4]
003559EF  01 85 84 00 00 00               add dword ptr [rbp + 0x84], eax
003559F5  E9 63 FD FF FF                  jmp 0x14035575d
003559FA  44 38 BD C1 00 00 00            cmp byte ptr [rbp + 0xc1], r15b
00355A01  0F 85 D9 01 00 00               jne 0x140355be0
00355A07  40 32 F6                        xor sil, sil
00355A0A  45 33 C0                        xor r8d, r8d
00355A0D  48 8B D5                        mov rdx, rbp
00355A10  49 8B CE                        mov rcx, r14
00355A13  E8 AC 41 FB FF                  call 0x140309bc4
00355A18  49 8B CD                        mov rcx, r13
00355A1B  E8 70 2D EF FF                  call 0x140248790
00355A20  F7 45 78 00 08 00 00            test dword ptr [rbp + 0x78], 0x800
00355A27  0F 85 D1 01 00 00               jne 0x140355bfe
00355A2D  8B 05 D1 10 C7 00               mov eax, dword ptr [rip + 0xc710d1]
00355A33  A8 04                           test al, 4
00355A35  0F 84 61 FE FF FF               je 0x14035589c
00355A3B  49 8B 8D 98 06 00 00            mov rcx, qword ptr [r13 + 0x698]
00355A42  48 83 F9 FD                     cmp rcx, -3
00355A46  0F 85 CB 01 00 00               jne 0x140355c17
00355A4C  49 8B 85 20 02 00 00            mov rax, qword ptr [r13 + 0x220]
00355A53  48 8B B8 F0 05 00 00            mov rdi, qword ptr [rax + 0x5f0]
00355A5A  49 8B 8D 98 06 00 00            mov rcx, qword ptr [r13 + 0x698]
00355A61  48 83 F9 FD                     cmp rcx, -3
00355A65  0F 85 B9 01 00 00               jne 0x140355c24
00355A6B  49 8B 85 20 02 00 00            mov rax, qword ptr [r13 + 0x220]
00355A72  4C 8B B0 F0 05 00 00            mov r14, qword ptr [rax + 0x5f0]
00355A79  48 8D 05 C0 9E C7 00            lea rax, [rip + 0xc79ec0]
00355A80  48 85 FF                        test rdi, rdi
00355A83  0F 85 F8 00 00 00               jne 0x140355b81
00355A89  48 8B E8                        mov rbp, rax
00355A8C  48 8B AD 40 03 00 00            mov rbp, qword ptr [rbp + 0x340]
00355A93  4D 85 F6                        test r14, r14
00355A96  0F 85 F1 00 00 00               jne 0x140355b8d
00355A9C  4C 8B B8 40 03 00 00            mov r15, qword ptr [rax + 0x340]
00355AA3  48 8B 05 FE 0F C7 00            mov rax, qword ptr [rip + 0xc70ffe]
00355AAA  48 05 EC 12 00 00               add rax, 0x12ec
00355AB0  74 0F                           je 0x140355ac1
00355AB2  8B 40 04                        mov eax, dword ptr [rax + 4]
00355AB5  A8 04                           test al, 4
00355AB7  74 08                           je 0x140355ac1
00355AB9  49 8B CD                        mov rcx, r13
00355ABC  E8 37 6F 1A 00                  call 0x1404fc9f8
00355AC1  48 8B 0D E0 0F C7 00            mov rcx, qword ptr [rip + 0xc70fe0]
00355AC8  4D 8B C5                        mov r8, r13
00355ACB  49 8B D5                        mov rdx, r13
00355ACE  E8 1D 1B 0C 00                  call 0x1404175f0
00355AD3  49 3B FE                        cmp rdi, r14
00355AD6  0F 84 84 00 00 00               je 0x140355b60
00355ADC  48 85 FF                        test rdi, rdi
00355ADF  0F 85 B4 00 00 00               jne 0x140355b99
00355AE5  4D 85 F6                        test r14, r14
00355AE8  0F 84 AE FD FF FF               je 0x14035589c
00355AEE  4D 85 FF                        test r15, r15
00355AF1  0F 84 A5 FD FF FF               je 0x14035589c
00355AF7  4D 8B C5                        mov r8, r13
00355AFA  33 D2                           xor edx, edx
00355AFC  49 8B CF                        mov rcx, r15
00355AFF  E8 EC 1A 0C 00                  call 0x1404175f0
00355B04  E9 93 FD FF FF                  jmp 0x14035589c
00355B09  41 0F B6 85 84 01 00 00         movzx eax, byte ptr [r13 + 0x184]
00355B11  3C 05                           cmp al, 5
00355B13  0F 85 60 FD FF FF               jne 0x140355879
00355B19  41 0F B6 85 18 03 00 00         movzx eax, byte ptr [r13 + 0x318]
00355B21  84 C0                           test al, al
00355B23  0F 85 08 01 00 00               jne 0x140355c31
00355B29  44 0F B6 C3                     movzx r8d, bl
00355B2D  48 8B D5                        mov rdx, rbp
00355B30  49 8B CD                        mov rcx, r13
00355B33  E8 08 3C 36 00                  call 0x1406b9740
00355B38  49 8B CD                        mov rcx, r13
00355B3B  0F B6 F0                        movzx esi, al
00355B3E  E8 4D 2C EF FF                  call 0x140248790
00355B43  E9 54 FD FF FF                  jmp 0x14035589c
00355B48  41 B9 02 00 00 00               mov r9d, 2
00355B4E  45 33 C0                        xor r8d, r8d
00355B51  8B D7                           mov edx, edi
00355B53  49 8B CE                        mov rcx, r14
00355B56  E8 65 D1 EF FF                  call 0x140252cc0
00355B5B  E9 10 FB FF FF                  jmp 0x140355670
00355B60  48 85 FF                        test rdi, rdi
00355B63  74 80                           je 0x140355ae5
00355B65  48 85 ED                        test rbp, rbp
00355B68  0F 84 77 FF FF FF               je 0x140355ae5
00355B6E  4D 8B C5                        mov r8, r13
00355B71  49 8B D5                        mov rdx, r13
00355B74  48 8B CD                        mov rcx, rbp
00355B77  E8 74 1A 0C 00                  call 0x1404175f0
00355B7C  E9 1B FD FF FF                  jmp 0x14035589c
00355B81  48 8B AF E0 05 00 00            mov rbp, qword ptr [rdi + 0x5e0]
00355B88  E9 FF FE FF FF                  jmp 0x140355a8c
00355B8D  49 8B 86 E0 05 00 00            mov rax, qword ptr [r14 + 0x5e0]
00355B94  E9 03 FF FF FF                  jmp 0x140355a9c
00355B99  48 85 ED                        test rbp, rbp
00355B9C  0F 84 43 FF FF FF               je 0x140355ae5
00355BA2  45 33 C0                        xor r8d, r8d
00355BA5  49 8B D5                        mov rdx, r13
00355BA8  48 8B CD                        mov rcx, rbp
00355BAB  E8 40 1A 0C 00                  call 0x1404175f0
00355BB0  E9 30 FF FF FF                  jmp 0x140355ae5
00355BB5  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00355BBA  E8 91 40 04 00                  call 0x140399c50
00355BBF  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00355BC4  49 8B CE                        mov rcx, r14
00355BC7  E8 34 49 10 00                  call 0x14045a500
00355BCC  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00355BD1  8B D7                           mov edx, edi
00355BD3  49 8B CE                        mov rcx, r14
00355BD6  E8 85 91 FB FF                  call 0x14030ed60
00355BDB  E9 32 FB FF FF                  jmp 0x140355712
00355BE0  66 44 39 BD E6 01 00 00         cmp word ptr [rbp + 0x1e6], r15w
00355BE8  0F 85 19 FE FF FF               jne 0x140355a07
00355BEE  84 DB                           test bl, bl
00355BF0  0F 85 11 FE FF FF               jne 0x140355a07
00355BF6  40 B6 01                        mov sil, 1
00355BF9  E9 0C FE FF FF                  jmp 0x140355a0a
00355BFE  F0 0F BA 75 78 0B               lock btr dword ptr [rbp + 0x78], 0xb
00355C04  45 33 C0                        xor r8d, r8d
00355C07  48 8B D5                        mov rdx, rbp
00355C0A  49 8B CE                        mov rcx, r14
00355C0D  E8 D6 4C FB FF                  call 0x14030a8e8
00355C12  E9 16 FE FF FF                  jmp 0x140355a2d
00355C17  E8 D4 FB EC FF                  call 0x1402257f0
00355C1C  48 8B F8                        mov rdi, rax
00355C1F  E9 36 FE FF FF                  jmp 0x140355a5a
00355C24  E8 C7 FB EC FF                  call 0x1402257f0
00355C29  4C 8B F0                        mov r14, rax
00355C2C  E9 48 FE FF FF                  jmp 0x140355a79
00355C31  41 8B F7                        mov esi, r15d
00355C34  E9 8A CC 38 00                  jmp 0x1406e28c3
00355C39  41 F7 45 78 00 00 40 00         test dword ptr [r13 + 0x78], 0x400000
00355C41  0F 84 55 FC FF FF               je 0x14035589c
00355C47  49 8B 8D C8 03 00 00            mov rcx, qword ptr [r13 + 0x3c8]
00355C4E  F0 81 21 FF FF FB FF            lock and dword ptr [rcx], 0xfffbffff
00355C55  E9 42 FC FF FF                  jmp 0x14035589c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSwapThread(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p88;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (48);
    if ((*(unsigned __int64 *)(a2 + 11528)) != 0) goto loc_00355B48;
loc_00355670:
    a2 = 0;
    result = KiAbProcessPreContextSwitch(a1, a2, a3, a4);
    result = KiCaptureTotalCyclesCurrentThread(0, a1, a3, a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 84))) >> (1));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 80))) >> (1));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    v_r15 = 0;
    *(unsigned int *)(a1 + 84) = (unsigned int)(a1);
    *(unsigned int *)(a1 + 80) = 0;
    result = (0) & (-2);
    result = (result) | (1);
    v_stack_p8 = result;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36440))) == 0) goto loc_003556EA;
loc_003556C1:
loc_003556D0:
    if (condition_is_below) goto loc_00355770;
    v_rsi = (*(unsigned __int64 *)(a2 + 36440) + 8) + (8);
    v_rbp = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_003556C1;
loc_003556EA:
    v_stack_p10 = 0;
    a4 = 0;
    v_stack_m48 = v_stack_p10;
    result = KiUpdateGroupSchedulingRank(a1, 0, a3, a4);
    if (v_stack_p10 != 0) goto loc_00355BB5;
loc_00355712:
    a2 = 0;
    result = KiSearchForNewThread(0, a2, v_stack_p8, a4);
    result = Feature_HeteroRescheduleFixes__private_IsEnabledNoReportingNoInline(0, a2, v_stack_p8, a4);
    if (result == (*(unsigned __int64 *)(a2 + 24))) goto loc_003557A7;
loc_0035573A:
    if (result == a1) goto loc_003557B9;
    if ((unsigned __int8)(*(unsigned __int8 *)(result + 113)) == 0) goto loc_003557B9;
    *(unsigned __int64 *)(a2 + 8) = *(unsigned __int64 *)(a2 + 24);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 24) + 388))) == 1) goto loc_003559DD;
loc_0035575D:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 24) + 388) = 2;
    goto loc_003557F5;
loc_00355770:
    v_rdi = (unsigned int)((v_rbp + 1) + 1);
    if (((*(unsigned int *)(v_rip + 13040436)) & ((unsigned int)(v_rdi))) == 0) goto loc_0035578B;
loc_0035577A:
loc_0035577C:
    if (*(unsigned __int64 *)(a2 + 24 + 48) == 0) goto loc_003556D0;
    goto loc_00355770;
loc_0035578B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13046567)))) & (64)) == 0) goto loc_0035577A;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, a2, v_stack_p8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0035577A;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), a2, v_stack_p8, a4);
    goto loc_0035577C;
loc_003557A7:
    if ((*(unsigned int *)(v_rip + 13046730)) != 0) goto loc_00355962;
loc_003557B4:
    if ((*(unsigned __int64 *)(a2 + 24)) != (*(unsigned __int64 *)(a2 + 24))) goto loc_0035573A;
loc_003557B9:
    *(unsigned __int64 *)(a2 + 16) = 0;
    *(unsigned __int64 *)(a2 + 8) = *(unsigned __int64 *)(a2 + 24);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 24) + 388))) == 1) goto loc_00355945;
loc_003557D0:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 24) + 388) = 2;
    if (((*(unsigned __int64 *)(a2 + 200)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 192) + 400))) != 0) goto loc_00355935;
loc_003557F5:
    a4 = (v_stack_p8) & (-2);
    v_stack_p20 = a4;
    result = (unsigned int)((v_stack_p8) & (1));
    if (condition_is_equal) goto loc_003558EE;
    if (((unsigned int)(result)) == 1) {
        result = *(unsigned __int64 *)(a4 + 36440);
        a3 = *(unsigned __int64 *)(a4 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_00355852;
loc_00355840:
    if ((unsigned int)(a2 - 1) != 0) goto loc_00355840;
loc_00355852:
    v_stack_p8 = 0;
    if (a1 == (*(unsigned __int64 *)(a2 + 24))) goto loc_003559FA;
    v_rdi = 0;
    if (((*(unsigned int *)(a1 + 120)) & (0x400000ULL)) != 0) goto loc_00355B09;
loc_00355879:
    result = KiSwapContext(a1, *(unsigned __int64 *)(a2 + 24), (unsigned __int8)(*(unsigned __int8 *)(a1 + 390)), a4);
    result = KiAbProcessPostContextSwitch(a1, *(unsigned __int64 *)(a2 + 24), (unsigned __int8)(*(unsigned __int8 *)(a1 + 390)), a4);
    if (0 != 0) goto loc_00355C39;
loc_0035589C:
    if (condition_is_below) goto loc_003559A9;
loc_003558AF:
    if (a3 != 0) goto loc_003558FD;
loc_003558B4:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0035590A;
loc_003558B9:
    if ((*(unsigned int *)(v_rip + 13046880)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 390));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned __int8)(*(unsigned __int8 *)(a1 + 390)), a4);
    }
    v_rsp = (v_rsp) + (48);
    return *(unsigned __int64 *)(a1 + 200);
loc_003558EE:
    goto loc_00355840;
loc_003558FD:
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(a1 + 976);
    goto loc_003558B4;
loc_0035590A:
    result = *(unsigned __int64 *)(a1 + 976);
    if ((*(unsigned int *)(v_rip + 13046799)) != 0) {
        a1 = *(unsigned __int8 *)(a1 + 390);
        a2 = 1;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_p88, a4);
    }
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = KiDeliverApc(a1, a2, a3, a4);
    goto loc_003558B9;
loc_00355935:
    a1 = ~(a1);
    goto loc_003557F5;
loc_00355945:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) - (*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 436)));
    goto loc_003557D0;
loc_00355962:
    if ((*(unsigned int *)(v_rip + 13046683)) != 0) goto loc_003557B4;
    if ((unsigned __int8)(*(unsigned __int8 *)(a2 + 14523)) != 0) goto loc_003557B4;
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p70, a2, a3, a4);
    result = KiSendHeteroRescheduleIntRequest(0, a2, a3, a4);
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(0, a2, v_stack_p70, a4);
    goto loc_003557B4;
loc_003559A9:
    result = KiCancelTimer(a1 + 256, 1, v_stack_p70, a4);
    if ((unsigned __int8)(result) != 0) goto loc_003558AF;
    *(unsigned __int8 *)(a1 + 464 + 17) = 4;
    *(unsigned __int64 *)(a1 + 264) = a1 + 464;
    *(unsigned __int64 *)(a1 + 272) = a1 + 464;
    goto loc_003558AF;
loc_003559DD:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 464))) - (*(unsigned int *)(*(unsigned __int64 *)(a2 + 16) + 436)));
    goto loc_0035575D;
loc_003559FA:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 16) + 193)) != 0) goto loc_00355BE0;
loc_00355A07:
    v_rsi = 0;
loc_00355A0A:
    a3 = 0;
    result = KiResumeThreadCycleAccumulation(0, *(unsigned __int64 *)(a2 + 16), a3, a4);
    result = KiAbProcessPostContextSwitch(a1, *(unsigned __int64 *)(a2 + 16), a3, a4);
    if (((*(unsigned int *)(*(unsigned __int64 *)(a2 + 16) + 120)) & (0x800ULL)) != 0) goto loc_00355BFE;
loc_00355A2D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13045969)))) & (4)) == 0) goto loc_0035589C;
    if ((*(unsigned __int64 *)(a1 + 1688)) != -3) goto loc_00355C17;
loc_00355A5A:
    if ((*(unsigned __int64 *)(a1 + 1688)) != -3) goto loc_00355C24;
loc_00355A79:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520) != 0) goto loc_00355B81;
loc_00355A8C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520) != 0) goto loc_00355B8D;
loc_00355A9C:
    result = (*(unsigned __int64 *)(v_rip + 13045758)) + (0x12ECULL);
    if (condition_is_equal) goto loc_00355AC1;
    result = (unsigned int)(*(unsigned int *)(result + 4));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 4)))) & (4)) != 0) {
        a1 = a1;
        result = EtwpCoverageSamplerContextSwap(a1, *(unsigned __int64 *)(a2 + 16), a3, a4);
    }
    result = EtwpLogContextSwapEvent(*(unsigned __int64 *)(v_rip + 13045728), a1, a1, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520))) goto loc_00355B60;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520) != 0) goto loc_00355B99;
loc_00355AE5:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520) == 0) goto loc_0035589C;
    if (*(unsigned __int64 *)(v_rip + 13082304 + 832) == 0) goto loc_0035589C;
    a2 = 0;
    result = EtwpLogContextSwapEvent(*(unsigned __int64 *)(v_rip + 13082304 + 832), a2, a1, a4);
    goto loc_0035589C;
loc_00355B09:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 5) goto loc_00355879;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 792)) != 0) goto loc_00355C31;
    result = KiSwapContext(a1, *(unsigned __int64 *)(v_rip + 13082304 + 832), (unsigned __int8)(v_stack_p18), a4);
    result = KiAbProcessPostContextSwitch(a1, *(unsigned __int64 *)(v_rip + 13082304 + 832), (unsigned __int8)(v_stack_p18), a4);
    goto loc_0035589C;
loc_00355B48:
    a3 = 0;
    result = KiProcessThreadWaitList(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520), (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520))), a3, 2);
    goto loc_00355670;
loc_00355B60:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520) == 0) goto loc_00355AE5;
    if (*(unsigned __int64 *)(v_rip + 13082304 + 832) == 0) goto loc_00355AE5;
    result = EtwpLogContextSwapEvent(*(unsigned __int64 *)(v_rip + 13082304 + 832), a1, a1, 2);
    goto loc_0035589C;
loc_00355B81:
    goto loc_00355A8C;
loc_00355B8D:
    goto loc_00355A9C;
loc_00355B99:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520) + 1504) == 0) goto loc_00355AE5;
    a3 = 0;
    result = EtwpLogContextSwapEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520) + 1504), a1, a3, 2);
    goto loc_00355AE5;
loc_00355BB5:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p70, a1, a3, 2);
    result = KiProcessScbTracingList(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520), v_stack_p78, a3, 2);
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520), (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520))), v_stack_p70, 2);
    goto loc_00355712;
loc_00355BE0:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520) + 1504) + 486)) != ((unsigned __int16)(*(unsigned __int64 *)(v_rip + 13082304 + 832)))) goto loc_00355A07;
    if ((unsigned __int8)(v_stack_p18) != 0) goto loc_00355A07;
    goto loc_00355A0A;
loc_00355BFE:
    a3 = 0;
    result = KiInsertDeferredPreemptionApc(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520) + 1504), a3, 2);
    goto loc_00355A2D;
loc_00355C17:
    result = PsGetEffectiveServerSilo(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520) + 1504), a3, 2);
    goto loc_00355A5A;
loc_00355C24:
    result = PsGetEffectiveServerSilo(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520) + 1504), a3, 2);
    goto loc_00355A79;
loc_00355C31:
loc_00355C39:
    if (((*(unsigned int *)(a1 + 120)) & (0x400000ULL)) == 0) goto loc_0035589C;
    goto loc_0035589C;
}
```

## 5. (Beta) C Style

```c
int64_t KiSwapThread(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p88;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (48);
    if ((*(uint64_t *)(arg2 + 0x2D08)) != 0) goto loc_00355B48;
loc_00355670:
    Arg2 = 0;
    result = KiAbProcessPreContextSwitch(Arg1, Arg2, Arg3, Arg4);
    result = KiCaptureTotalCyclesCurrentThread(0, Arg1, Arg3, Arg4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x54))) >> (1));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x50))) >> (1));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    local_r15 = 0;
    *(uint32_t *)(arg1 + 0x54) = (uint32_t)(Arg1);
    *(uint32_t *)(arg1 + 0x50) = 0;
    result = (0) & (-2);
    result = (result) | (1);
    v_stack_p8 = result;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E58))) == 0) goto loc_003556EA;
loc_003556C1:
loc_003556D0:
    if (condition_is_below) goto loc_00355770;
    local_rsi = (*(uint64_t *)(arg2 + 0x8E58) + 8) + (8);
    local_rbp = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_003556C1;
loc_003556EA:
    v_stack_p10 = 0;
    Arg4 = 0;
    v_stack_m48 = v_stack_p10;
    result = KiUpdateGroupSchedulingRank(Arg1, 0, Arg3, Arg4);
    if (v_stack_p10 != 0) goto loc_00355BB5;
loc_00355712:
    Arg2 = 0;
    result = KiSearchForNewThread(0, Arg2, v_stack_p8, Arg4);
    result = Feature_HeteroRescheduleFixes__private_IsEnabledNoReportingNoInline(0, Arg2, v_stack_p8, Arg4);
    if (result == (*(uint64_t *)(arg2 + 0x18))) goto loc_003557A7;
loc_0035573A:
    if (result == Arg1) goto loc_003557B9;
    if ((uint8_t)(*(uint8_t *)(result + 0x71)) == 0) goto loc_003557B9;
    *(uint64_t *)(arg2 + 0x8) = *(uint64_t *)(arg2 + 0x18);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x18) + 0x184))) == 1) goto loc_003559DD;
loc_0035575D:
    *(uint8_t *)(*(uint64_t *)(arg2 + 0x18) + 0x184) = 2;
    goto loc_003557F5;
loc_00355770:
    local_rdi = (uint32_t)((local_rbp + 1) + 1);
    if (((*(uint32_t *)(v_rip + 0xC6FB34)) & ((uint32_t)(local_rdi))) == 0) goto loc_0035578B;
loc_0035577A:
loc_0035577C:
    if (*(uint64_t *)(arg2 + 0x18 + 0x30) == 0) goto loc_003556D0;
    goto loc_00355770;
loc_0035578B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC71327)))) & (64)) == 0) goto loc_0035577A;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, Arg2, v_stack_p8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0035577A;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), Arg2, v_stack_p8, Arg4);
    goto loc_0035577C;
loc_003557A7:
    if ((*(uint32_t *)(v_rip + 0xC713CA)) != 0) goto loc_00355962;
loc_003557B4:
    if ((*(uint64_t *)(arg2 + 0x18)) != (*(uint64_t *)(arg2 + 0x18))) goto loc_0035573A;
loc_003557B9:
    *(uint64_t *)(arg2 + 0x10) = 0;
    *(uint64_t *)(arg2 + 0x8) = *(uint64_t *)(arg2 + 0x18);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x18) + 0x184))) == 1) goto loc_00355945;
loc_003557D0:
    *(uint8_t *)(*(uint64_t *)(arg2 + 0x18) + 0x184) = 2;
    if (((*(uint64_t *)(arg2 + 0xC8)) & (*(uint64_t *)(*(uint64_t *)(arg2 + 0xC0) + 0x190))) != 0) goto loc_00355935;
loc_003557F5:
    Arg4 = (v_stack_p8) & (-2);
    v_stack_p20 = Arg4;
    result = (uint32_t)((v_stack_p8) & (1));
    if (condition_is_equal) goto loc_003558EE;
    if (((uint32_t)(result)) == 1) {
        result = *(uint64_t *)(Arg4 + 0x8E58);
        Arg3 = *(uint64_t *)(Arg4 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_00355852;
loc_00355840:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_00355840;
loc_00355852:
    v_stack_p8 = 0;
    if (Arg1 == (*(uint64_t *)(arg2 + 0x18))) goto loc_003559FA;
    local_rdi = 0;
    if (((*(uint32_t *)(arg1 + 0x78)) & (0x400000ULL)) != 0) goto loc_00355B09;
loc_00355879:
    result = KiSwapContext(Arg1, *(uint64_t *)(arg2 + 0x18), (uint8_t)(*(uint8_t *)(arg1 + 0x186)), Arg4);
    result = KiAbProcessPostContextSwitch(Arg1, *(uint64_t *)(arg2 + 0x18), (uint8_t)(*(uint8_t *)(arg1 + 0x186)), Arg4);
    if (0 != 0) goto loc_00355C39;
loc_0035589C:
    if (condition_is_below) goto loc_003559A9;
loc_003558AF:
    if (Arg3 != 0) goto loc_003558FD;
loc_003558B4:
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0035590A;
loc_003558B9:
    if ((*(uint32_t *)(v_rip + 0xC71460)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(*(uint8_t *)(arg1 + 0x186));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint8_t)(*(uint8_t *)(arg1 + 0x186)), Arg4);
    }
    local_rsp = (local_rsp) + (48);
    return *(uint64_t *)(arg1 + 0xC8);
loc_003558EE:
    goto loc_00355840;
loc_003558FD:
    *(uint64_t *)(Arg3) = *(uint64_t *)(arg1 + 0x3D0);
    goto loc_003558B4;
loc_0035590A:
    result = *(uint64_t *)(arg1 + 0x3D0);
    if ((*(uint32_t *)(v_rip + 0xC7140F)) != 0) {
        Arg1 = *(uint8_t *)(arg1 + 0x186);
        Arg2 = 1;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_p88, Arg4);
    }
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = KiDeliverApc(Arg1, Arg2, Arg3, Arg4);
    goto loc_003558B9;
loc_00355935:
    Arg1 = ~(Arg1);
    goto loc_003557F5;
loc_00355945:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) - (*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x1B4)));
    goto loc_003557D0;
loc_00355962:
    if ((*(uint32_t *)(v_rip + 0xC7139B)) != 0) goto loc_003557B4;
    if ((uint8_t)(*(uint8_t *)(arg2 + 0x38BB)) != 0) goto loc_003557B4;
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p70, Arg2, Arg3, Arg4);
    result = KiSendHeteroRescheduleIntRequest(0, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(0, Arg2, v_stack_p70, Arg4);
    goto loc_003557B4;
loc_003559A9:
    result = KiCancelTimer(Arg1 + 256, 1, v_stack_p70, Arg4);
    if ((uint8_t)(result) != 0) goto loc_003558AF;
    *(uint8_t *)(arg1 + 0x1D0 + 0x11) = 4;
    *(void **)(arg1 + 0x108) = Arg1 + 464;
    *(void **)(arg1 + 0x110) = Arg1 + 464;
    goto loc_003558AF;
loc_003559DD:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1D0))) - (*(uint32_t *)(*(uint64_t *)(arg2 + 0x10) + 0x1B4)));
    goto loc_0035575D;
loc_003559FA:
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x10) + 0xC1)) != 0) goto loc_00355BE0;
loc_00355A07:
    local_rsi = 0;
loc_00355A0A:
    Arg3 = 0;
    result = KiResumeThreadCycleAccumulation(0, *(uint64_t *)(arg2 + 0x10), Arg3, Arg4);
    result = KiAbProcessPostContextSwitch(Arg1, *(uint64_t *)(arg2 + 0x10), Arg3, Arg4);
    if (((*(uint32_t *)(*(uint64_t *)(arg2 + 0x10) + 0x78)) & (0x800ULL)) != 0) goto loc_00355BFE;
loc_00355A2D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC710D1)))) & (4)) == 0) goto loc_0035589C;
    if ((*(uint64_t *)(arg1 + 0x698)) != -3) goto loc_00355C17;
loc_00355A5A:
    if ((*(uint64_t *)(arg1 + 0x698)) != -3) goto loc_00355C24;
loc_00355A79:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0) != 0) goto loc_00355B81;
loc_00355A8C:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0) != 0) goto loc_00355B8D;
loc_00355A9C:
    result = (*(uint64_t *)(v_rip + 0xC70FFE)) + (0x12ECULL);
    if (condition_is_equal) goto loc_00355AC1;
    result = (uint32_t)(*(uint32_t *)(result + 0x4));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) & (4)) != 0) {
        Arg1 = Arg1;
        result = EtwpCoverageSamplerContextSwap(Arg1, *(uint64_t *)(arg2 + 0x10), Arg3, Arg4);
    }
    result = EtwpLogContextSwapEvent(*(uint64_t *)(v_rip + 0xC70FE0), Arg1, Arg1, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0))) goto loc_00355B60;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0) != 0) goto loc_00355B99;
loc_00355AE5:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0) == 0) goto loc_0035589C;
    if (*(uint64_t *)(v_rip + 0xC79EC0 + 0x340) == 0) goto loc_0035589C;
    Arg2 = 0;
    result = EtwpLogContextSwapEvent(*(uint64_t *)(v_rip + 0xC79EC0 + 0x340), Arg2, Arg1, Arg4);
    goto loc_0035589C;
loc_00355B09:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x184))) != 5) goto loc_00355879;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x318)) != 0) goto loc_00355C31;
    result = KiSwapContext(Arg1, *(uint64_t *)(v_rip + 0xC79EC0 + 0x340), (uint8_t)(v_stack_p18), Arg4);
    result = KiAbProcessPostContextSwitch(Arg1, *(uint64_t *)(v_rip + 0xC79EC0 + 0x340), (uint8_t)(v_stack_p18), Arg4);
    goto loc_0035589C;
loc_00355B48:
    Arg3 = 0;
    result = KiProcessThreadWaitList(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0), (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0))), Arg3, 2);
    goto loc_00355670;
loc_00355B60:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0) == 0) goto loc_00355AE5;
    if (*(uint64_t *)(v_rip + 0xC79EC0 + 0x340) == 0) goto loc_00355AE5;
    result = EtwpLogContextSwapEvent(*(uint64_t *)(v_rip + 0xC79EC0 + 0x340), Arg1, Arg1, 2);
    goto loc_0035589C;
loc_00355B81:
    goto loc_00355A8C;
loc_00355B8D:
    goto loc_00355A9C;
loc_00355B99:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0) + 0x5E0) == 0) goto loc_00355AE5;
    Arg3 = 0;
    result = EtwpLogContextSwapEvent(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0) + 0x5E0), Arg1, Arg3, 2);
    goto loc_00355AE5;
loc_00355BB5:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p70, Arg1, Arg3, 2);
    result = KiProcessScbTracingList(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0), v_stack_p78, Arg3, 2);
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0), (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0))), v_stack_p70, 2);
    goto loc_00355712;
loc_00355BE0:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0) + 0x5E0) + 0x1E6)) != ((uint16_t)(*(uint64_t *)(v_rip + 0xC79EC0 + 0x340)))) goto loc_00355A07;
    if ((uint8_t)(v_stack_p18) != 0) goto loc_00355A07;
    goto loc_00355A0A;
loc_00355BFE:
    Arg3 = 0;
    result = KiInsertDeferredPreemptionApc(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0) + 0x5E0), Arg3, 2);
    goto loc_00355A2D;
loc_00355C17:
    result = PsGetEffectiveServerSilo(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0) + 0x5E0), Arg3, 2);
    goto loc_00355A5A;
loc_00355C24:
    result = PsGetEffectiveServerSilo(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0) + 0x5E0), Arg3, 2);
    goto loc_00355A79;
loc_00355C31:
loc_00355C39:
    if (((*(uint32_t *)(arg1 + 0x78)) & (0x400000ULL)) == 0) goto loc_0035589C;
    goto loc_0035589C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x50` | `32` | `W` |
| `Arg1` | `+ 0x54` | `32` | `R` |
| `Arg1` | `+ 0x54` | `32` | `W` |
| `Arg1` | `+ 0x186` | `8` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `W` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0xC0` | `64` | `R` |
| `Arg2` | `+ 0xC8` | `64` | `R` |
| `Arg2` | `+ 0x2D08` | `64` | `R` |
| `Arg2` | `+ 0x38BB` | `8` | `R` |
| `Arg2` | `+ 0x8E58` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00355640&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
