# KiGroupSchedulingGenerationEnd

- RVA: `0x0030A9B4`–`0x0030B132` (길이 `1,918` bytes)
- VA: `0x000000014030A9B4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073C60`
- 디코드: `498`개 명령, `1,918/1,918` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0030A9F8` → [KiCaptureTotalCyclesCurrentThread](../37/KiCaptureTotalCyclesCurrentThread_function_0037CB90.md) (function, `0x0037CB90`)
- `0x0030AA18` → [KiTransitionSchedulingGroupGeneration](KiTransitionSchedulingGroupGeneration_function_003094C8.md) (function, `0x003094C8`)
- `0x0030AA34` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030AA42` → [KiStartRescheduleContext](KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x0030AA5B` → [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x0030AA8E` → [KiCommitRescheduleContextEntry](KiCommitRescheduleContextEntry_function_0030CFD0.md) (function, `0x0030CFD0`)
- `0x0030AAED` → [KiResumeThreadCycleAccumulation](KiResumeThreadCycleAccumulation_function_00309BC4.md) (function, `0x00309BC4`)
- `0x0030AB3C` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0030AB74` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x0030AC31` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0030AC53` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0030AC9E` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0030ACDA` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x0030AD99` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x0030ADBF` → [KiAcquirePrcbLocksForIsolationUnit](KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x0030ADD3` → [KiAddProcessorToSoftwareInterruptBatch](KiAddProcessorToSoftwareInterruptBatch_function_0030B138.md) (function, `0x0030B138`)
- `0x0030AE03` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x0030AE19` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x0030AE9A` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x0030AEC0` → [EtwTraceScheduleThread](EtwTraceScheduleThread_function_0030B74C.md) (function, `0x0030B74C`)
- `0x0030AED1` → [KiReadyDeferredReadyList](KiReadyDeferredReadyList_function_0030DD80.md) (function, `0x0030DD80`)
- `0x0030AEE1` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x0030AF62` → [KiAddThreadToPrcbQueue](../21/KiAddThreadToPrcbQueue_function_00218B00.md) (function, `0x00218B00`)
- `0x0030AF86` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x0030AFE7` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0030B009` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0030B057` → [KiAdjustRescheduleContextEntryForThreadRemoval](../35/KiAdjustRescheduleContextEntryForThreadRemoval_function_00352340.md) (function, `0x00352340`)
- `0x0030B0B1` → [KiDoesThreadDominateRescheduleContextEntry](../25/KiDoesThreadDominateRescheduleContextEntry_function_002581D0.md) (function, `0x002581D0`)
- `0x0030B0EC` → [KiAdjustRescheduleContextEntryForThreadRemoval](../35/KiAdjustRescheduleContextEntryForThreadRemoval_function_00352340.md) (function, `0x00352340`)
- `0x0030B117` → [EtwTraceReadyQueueInsertion](../22/EtwTraceReadyQueueInsertion_function_00223444.md) (function, `0x00223444`)
- `0x0030B128` → [KiProcessScbTracingList](../45/KiProcessScbTracingList_function_0045A500.md) (function, `0x0045A500`)

### Direct callers
- [KiGroupSchedulingQuantumEnd](KiGroupSchedulingQuantumEnd_function_0030B220.md) at `0x0030B444`

### Static image references
- `0x0030AA60` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x0030ACF4` → RVA `0x00FCD260` (`ALMOSTRO`; read)
- `0x0030AE56` → RVA `0x00FC5007` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0030A9B4  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0030A9B9  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0030A9BE  55                              push rbp
0030A9BF  56                              push rsi
0030A9C0  57                              push rdi
0030A9C1  41 54                           push r12
0030A9C3  41 55                           push r13
0030A9C5  41 56                           push r14
0030A9C7  41 57                           push r15
0030A9C9  48 8B EC                        mov rbp, rsp
0030A9CC  48 83 EC 50                     sub rsp, 0x50
0030A9D0  4C 8B 69 08                     mov r13, qword ptr [rcx + 8]
0030A9D4  4C 8B E2                        mov r12, rdx
0030A9D7  48 8B 59 18                     mov rbx, qword ptr [rcx + 0x18]
0030A9DB  49 8B D5                        mov rdx, r13
0030A9DE  83 65 58 00                     and dword ptr [rbp + 0x58], 0
0030A9E2  49 8B F8                        mov rdi, r8
0030A9E5  48 83 65 E8 00                  and qword ptr [rbp - 0x18], 0
0030A9EA  4C 8B F1                        mov r14, rcx
0030A9ED  4C 3B EB                        cmp r13, rbx
0030A9F0  4C 89 6D F8                     mov qword ptr [rbp - 8], r13
0030A9F4  0F 94 45 40                     sete byte ptr [rbp + 0x40]
0030A9F8  E8 93 21 07 00                  call 0x14037cb90
0030A9FD  4C 3B EB                        cmp r13, rbx
0030AA00  0F 84 05 01 00 00               je 0x14030ab0b
0030AA06  48 8D 45 E8                     lea rax, [rbp - 0x18]
0030AA0A  45 33 C9                        xor r9d, r9d
0030AA0D  4C 8B C7                        mov r8, rdi
0030AA10  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0030AA15  49 8B CE                        mov rcx, r14
0030AA18  E8 AB EA FF FF                  call 0x1403094c8
0030AA1D  49 8B B6 E8 37 00 00            mov rsi, qword ptr [r14 + 0x37e8]
0030AA24  33 D2                           xor edx, edx
0030AA26  48 83 65 E0 00                  and qword ptr [rbp - 0x20], 0
0030AA2B  48 8B CE                        mov rcx, rsi
0030AA2E  41 B8 F0 00 00 00               mov r8d, 0xf0
0030AA34  E8 07 C2 3B 00                  call 0x1406c6c40
0030AA39  45 33 C0                        xor r8d, r8d
0030AA3C  49 8B D4                        mov rdx, r12
0030AA3F  48 8B CE                        mov rcx, rsi
0030AA42  E8 69 1C 00 00                  call 0x14030c6b0
0030AA47  49 8B 7E 10                     mov rdi, qword ptr [r14 + 0x10]
0030AA4B  48 85 FF                        test rdi, rdi
0030AA4E  0F 85 E5 00 00 00               jne 0x14030ab39
0030AA54  48 8D 55 E0                     lea rdx, [rbp - 0x20]
0030AA58  48 8B CE                        mov rcx, rsi
0030AA5B  E8 C0 DB F4 FF                  call 0x140258620
0030AA60  8B 1D AE C0 CB 00               mov ebx, dword ptr [rip + 0xcbc0ae]
0030AA66  45 32 FF                        xor r15b, r15b
0030AA69  C1 EB 09                        shr ebx, 9
0030AA6C  33 FF                           xor edi, edi
0030AA6E  83 E3 02                        and ebx, 2
0030AA71  40 38 3E                        cmp byte ptr [rsi], dil
0030AA74  76 29                           jbe 0x14030aa9f
0030AA76  8B CF                           mov ecx, edi
0030AA78  4C 8D 4D E0                     lea r9, [rbp - 0x20]
0030AA7C  48 83 C1 02                     add rcx, 2
0030AA80  44 8B C3                        mov r8d, ebx
0030AA83  49 8B D6                        mov rdx, r14
0030AA86  48 8D 0C B9                     lea rcx, [rcx + rdi*4]
0030AA8A  48 8D 0C CE                     lea rcx, [rsi + rcx*8]
0030AA8E  E8 3D 25 00 00                  call 0x14030cfd0
0030AA93  44 0A F8                        or r15b, al
0030AA96  FF C7                           inc edi
0030AA98  0F B6 06                        movzx eax, byte ptr [rsi]
0030AA9B  3B F8                           cmp edi, eax
0030AA9D  72 D7                           jb 0x14030aa76
0030AA9F  83 7E 08 01                     cmp dword ptr [rsi + 8], 1
0030AAA3  75 1B                           jne 0x14030aac0
0030AAA5  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
0030AAA9  48 8B 88 58 8E 00 00            mov rcx, qword ptr [rax + 0x8e58]
0030AAB0  8A 41 01                        mov al, byte ptr [rcx + 1]
0030AAB3  FE C0                           inc al
0030AAB5  88 41 01                        mov byte ptr [rcx + 1], al
0030AAB8  3A 01                           cmp al, byte ptr [rcx]
0030AABA  72 04                           jb 0x14030aac0
0030AABC  C6 41 01 00                     mov byte ptr [rcx + 1], 0
0030AAC0  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
0030AAC4  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
0030AAC8  45 84 FF                        test r15b, r15b
0030AACB  0F 85 06 02 00 00               jne 0x14030acd7
0030AAD1  48 85 FF                        test rdi, rdi
0030AAD4  0F 85 FD 01 00 00               jne 0x14030acd7
0030AADA  48 85 DB                        test rbx, rbx
0030AADD  0F 85 F4 01 00 00               jne 0x14030acd7
0030AAE3  44 8A 45 40                     mov r8b, byte ptr [rbp + 0x40]
0030AAE7  49 8B D5                        mov rdx, r13
0030AAEA  49 8B CE                        mov rcx, r14
0030AAED  E8 D2 F0 FF FF                  call 0x140309bc4
0030AAF2  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
0030AAFA  48 83 C4 50                     add rsp, 0x50
0030AAFE  41 5F                           pop r15
0030AB00  41 5E                           pop r14
0030AB02  41 5D                           pop r13
0030AB04  41 5C                           pop r12
0030AB06  5F                              pop rdi
0030AB07  5E                              pop rsi
0030AB08  5D                              pop rbp
0030AB09  C3                              ret
0030AB0A  CC                              int3
0030AB0B  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0030AB0F  48 85 C0                        test rax, rax
0030AB12  74 18                           je 0x14030ab2c
0030AB14  49 3B 46 18                     cmp rax, qword ptr [r14 + 0x18]
0030AB18  74 12                           je 0x14030ab2c
0030AB1A  41 F6 46 23 01                  test byte ptr [r14 + 0x23], 1
0030AB1F  0F 85 E1 FE FF FF               jne 0x14030aa06
0030AB25  B9 1E 00 00 00                  mov ecx, 0x1e
0030AB2A  CD 29                           int 0x29
0030AB2C  41 F6 46 23 01                  test byte ptr [r14 + 0x23], 1
0030AB31  0F 84 CF FE FF FF               je 0x14030aa06
0030AB37  EB EC                           jmp 0x14030ab25
0030AB39  48 8B CF                        mov rcx, rdi
0030AB3C  E8 EF 86 04 00                  call 0x140353230
0030AB41  84 C0                           test al, al
0030AB43  0F 85 0B FF FF FF               jne 0x14030aa54
0030AB49  4D 8B 6E 08                     mov r13, qword ptr [r14 + 8]
0030AB4D  48 83 65 F0 00                  and qword ptr [rbp - 0x10], 0
0030AB52  45 8B 45 78                     mov r8d, dword ptr [r13 + 0x78]
0030AB56  41 0F BA E0 0C                  bt r8d, 0xc
0030AB5B  0F 82 1F 04 00 00               jb 0x14030af80
0030AB61  4D 3B AE 80 8E 00 00            cmp r13, qword ptr [r14 + 0x8e80]
0030AB68  0F 84 12 04 00 00               je 0x14030af80
0030AB6E  49 8B D6                        mov rdx, r14
0030AB71  48 8B CE                        mov rcx, rsi
0030AB74  E8 E7 84 04 00                  call 0x140353060
0030AB79  8B 4F 78                        mov ecx, dword ptr [rdi + 0x78]
0030AB7C  41 83 E0 02                     and r8d, 2
0030AB80  83 E1 02                        and ecx, 2
0030AB83  48 8B D8                        mov rbx, rax
0030AB86  44 3A C1                        cmp r8b, cl
0030AB89  0F 87 72 05 00 00               ja 0x14030b101
0030AB8F  48 8B 03                        mov rax, qword ptr [rbx]
0030AB92  41 B3 FE                        mov r11b, 0xfe
0030AB95  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0030AB99  48 89 4B 10                     mov qword ptr [rbx + 0x10], rcx
0030AB9D  48 3B 48 18                     cmp rcx, qword ptr [rax + 0x18]
0030ABA1  8A 43 20                        mov al, byte ptr [rbx + 0x20]
0030ABA4  0F 94 C2                        sete dl
0030ABA7  41 22 C3                        and al, r11b
0030ABAA  0A D0                           or dl, al
0030ABAC  88 53 20                        mov byte ptr [rbx + 0x20], dl
0030ABAF  80 E2 FD                        and dl, 0xfd
0030ABB2  8B 41 78                        mov eax, dword ptr [rcx + 0x78]
0030ABB5  48 83 63 18 00                  and qword ptr [rbx + 0x18], 0
0030ABBA  44 20 5B 21                     and byte ptr [rbx + 0x21], r11b
0030ABBE  80 4B 22 01                     or byte ptr [rbx + 0x22], 1
0030ABC2  D1 E8                           shr eax, 1
0030ABC4  24 01                           and al, 1
0030ABC6  02 C0                           add al, al
0030ABC8  32 C2                           xor al, dl
0030ABCA  24 C7                           and al, 0xc7
0030ABCC  0C 04                           or al, 4
0030ABCE  88 43 20                        mov byte ptr [rbx + 0x20], al
0030ABD1  41 8B 4D 78                     mov ecx, dword ptr [r13 + 0x78]
0030ABD5  0B 4F 78                        or ecx, dword ptr [rdi + 0x78]
0030ABD8  F6 C1 02                        test cl, 2
0030ABDB  0F 84 E5 00 00 00               je 0x14030acc6
0030ABE1  45 33 D2                        xor r10d, r10d
0030ABE4  44 38 16                        cmp byte ptr [rsi], r10b
0030ABE7  0F 86 D9 00 00 00               jbe 0x14030acc6
0030ABED  41 8B C2                        mov eax, r10d
0030ABF0  4E 8D 0C 95 02 00 00 00         lea r9, [r10*4 + 2]
0030ABF8  4C 03 C8                        add r9, rax
0030ABFB  4E 8D 0C CE                     lea r9, [rsi + r9*8]
0030ABFF  49 3B D9                        cmp rbx, r9
0030AC02  0F 84 AB 00 00 00               je 0x14030acb3
0030AC08  41 8B 45 78                     mov eax, dword ptr [r13 + 0x78]
0030AC0C  49 8B 49 18                     mov rcx, qword ptr [r9 + 0x18]
0030AC10  48 83 65 F0 00                  and qword ptr [rbp - 0x10], 0
0030AC15  4D 8B 39                        mov r15, qword ptr [r9]
0030AC18  A8 02                           test al, 2
0030AC1A  48 8D 41 FF                     lea rax, [rcx - 1]
0030AC1E  0F 84 B9 03 00 00               je 0x14030afdd
0030AC24  4D 8B A7 80 8E 00 00            mov r12, qword ptr [r15 + 0x8e80]
0030AC2B  48 83 F8 FC                     cmp rax, -4
0030AC2F  77 27                           ja 0x14030ac58
0030AC31  E8 FA 85 04 00                  call 0x140353230
0030AC36  84 C0                           test al, al
0030AC38  75 1E                           jne 0x14030ac58
0030AC3A  41 F6 41 21 01                  test byte ptr [r9 + 0x21], 1
0030AC3F  74 04                           je 0x14030ac45
0030AC41  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0030AC45  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0030AC4C  48 8B D1                        mov rdx, rcx
0030AC4F  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0030AC53  E8 B8 66 EF FF                  call 0x140201310
0030AC58  41 8A 41 20                     mov al, byte ptr [r9 + 0x20]
0030AC5C  41 22 C3                        and al, r11b
0030AC5F  4D 89 69 10                     mov qword ptr [r9 + 0x10], r13
0030AC63  41 88 41 20                     mov byte ptr [r9 + 0x20], al
0030AC67  24 FD                           and al, 0xfd
0030AC69  41 8B 4D 78                     mov ecx, dword ptr [r13 + 0x78]
0030AC6D  D1 E9                           shr ecx, 1
0030AC6F  80 E1 01                        and cl, 1
0030AC72  02 C9                           add cl, cl
0030AC74  32 C8                           xor cl, al
0030AC76  80 E1 E7                        and cl, 0xe7
0030AC79  80 C9 04                        or cl, 4
0030AC7C  8A C1                           mov al, cl
0030AC7E  80 C9 20                        or cl, 0x20
0030AC81  24 DF                           and al, 0xdf
0030AC83  0F B6 C9                        movzx ecx, cl
0030AC86  4D 3B EC                        cmp r13, r12
0030AC89  0F B6 C0                        movzx eax, al
0030AC8C  0F 44 C8                        cmove ecx, eax
0030AC8F  41 88 49 20                     mov byte ptr [r9 + 0x20], cl
0030AC93  45 20 59 21                     and byte ptr [r9 + 0x21], r11b
0030AC97  49 8B CC                        mov rcx, r12
0030AC9A  4D 89 61 18                     mov qword ptr [r9 + 0x18], r12
0030AC9E  E8 8D 85 04 00                  call 0x140353230
0030ACA3  84 C0                           test al, al
0030ACA5  75 0C                           jne 0x14030acb3
0030ACA7  41 8B 47 24                     mov eax, dword ptr [r15 + 0x24]
0030ACAB  41 89 84 24 18 02 00 00         mov dword ptr [r12 + 0x218], eax
0030ACB3  0F B6 06                        movzx eax, byte ptr [rsi]
0030ACB6  41 FF C2                        inc r10d
0030ACB9  44 3B D0                        cmp r10d, eax
0030ACBC  0F 82 2B FF FF FF               jb 0x14030abed
0030ACC2  4C 8B 65 48                     mov r12, qword ptr [rbp + 0x48]
0030ACC6  41 8B 45 78                     mov eax, dword ptr [r13 + 0x78]
0030ACCA  D1 E8                           shr eax, 1
0030ACCC  83 E0 01                        and eax, 1
0030ACCF  89 46 04                        mov dword ptr [rsi + 4], eax
0030ACD2  E9 50 02 00 00                  jmp 0x14030af27
0030ACD7  49 8B CC                        mov rcx, r12
0030ACDA  E8 71 EF 08 00                  call 0x140399c50
0030ACDF  45 84 FF                        test r15b, r15b
0030ACE2  0F 84 BA 00 00 00               je 0x14030ada2
0030ACE8  45 33 E4                        xor r12d, r12d
0030ACEB  44 38 26                        cmp byte ptr [rsi], r12b
0030ACEE  0F 86 9E 00 00 00               jbe 0x14030ad92
0030ACF4  4C 8D 2D 65 25 CC 00            lea r13, [rip + 0xcc2565]
0030ACFB  4B 8D 3C A4                     lea rdi, [r12 + r12*4]
0030ACFF  8A 44 FE 33                     mov al, byte ptr [rsi + rdi*8 + 0x33]
0030AD03  48 8B 5C FE 10                  mov rbx, qword ptr [rsi + rdi*8 + 0x10]
0030AD08  A8 10                           test al, 0x10
0030AD0A  0F 85 B9 00 00 00               jne 0x14030adc9
0030AD10  A8 08                           test al, 8
0030AD12  74 28                           je 0x14030ad3c
0030AD14  90                              nop
0030AD15  80 7B 07 00                     cmp byte ptr [rbx + 7], 0
0030AD19  74 21                           je 0x14030ad3c
0030AD1B  41 8A 86 D9 35 00 00            mov al, byte ptr [r14 + 0x35d9]
0030AD22  84 C0                           test al, al
0030AD24  0F 85 B3 00 00 00               jne 0x14030addd
0030AD2A  41 C6 86 D9 35 00 00 01         mov byte ptr [r14 + 0x35d9], 1
0030AD32  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0030AD35  41 89 86 DC 35 00 00            mov dword ptr [r14 + 0x35dc], eax
0030AD3C  F6 44 FE 33 02                  test byte ptr [rsi + rdi*8 + 0x33], 2
0030AD41  0F 85 6E 01 00 00               jne 0x14030aeb5
0030AD47  F6 44 FE 33 04                  test byte ptr [rsi + rdi*8 + 0x33], 4
0030AD4C  74 15                           je 0x14030ad63
0030AD4E  48 8B 8B B8 8E 00 00            mov rcx, qword ptr [rbx + 0x8eb8]
0030AD55  0F BE 54 FE 34                  movsx edx, byte ptr [rsi + rdi*8 + 0x34]
0030AD5A  48 85 C9                        test rcx, rcx
0030AD5D  0F 85 C9 00 00 00               jne 0x14030ae2c
0030AD63  F6 44 FE 33 01                  test byte ptr [rsi + rdi*8 + 0x33], 1
0030AD68  74 0D                           je 0x14030ad77
0030AD6A  48 8B 44 FE 28                  mov rax, qword ptr [rsi + rdi*8 + 0x28]
0030AD6F  66 F0 FF 88 64 03 00 00         lock dec word ptr [rax + 0x364]
0030AD77  0F B6 06                        movzx eax, byte ptr [rsi]
0030AD7A  41 FF C4                        inc r12d
0030AD7D  44 3B E0                        cmp r12d, eax
0030AD80  0F 82 75 FF FF FF               jb 0x14030acfb
0030AD86  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
0030AD8A  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
0030AD8E  4C 8B 6D F8                     mov r13, qword ptr [rbp - 8]
0030AD92  49 8D 8E D8 35 00 00            lea rcx, [r14 + 0x35d8]
0030AD99  E8 62 74 F4 FF                  call 0x140252200
0030AD9E  4C 8B 65 48                     mov r12, qword ptr [rbp + 0x48]
0030ADA2  48 85 DB                        test rbx, rbx
0030ADA5  0F 85 76 03 00 00               jne 0x14030b121
0030ADAB  48 85 FF                        test rdi, rdi
0030ADAE  0F 85 16 01 00 00               jne 0x14030aeca
0030ADB4  4D 8B C4                        mov r8, r12
0030ADB7  BA 01 00 00 00                  mov edx, 1
0030ADBC  49 8B CE                        mov rcx, r14
0030ADBF  E8 9C 3F 00 00                  call 0x14030ed60
0030ADC4  E9 1A FD FF FF                  jmp 0x14030aae3
0030ADC9  49 8D 8E D8 35 00 00            lea rcx, [r14 + 0x35d8]
0030ADD0  48 8B D3                        mov rdx, rbx
0030ADD3  E8 60 03 00 00                  call 0x14030b138
0030ADD8  E9 5F FF FF FF                  jmp 0x14030ad3c
0030ADDD  3C 01                           cmp al, 1
0030ADDF  75 42                           jne 0x14030ae23
0030ADE1  41 8B 96 DC 35 00 00            mov edx, dword ptr [r14 + 0x35dc]
0030ADE8  3B 53 24                        cmp edx, dword ptr [rbx + 0x24]
0030ADEB  0F 84 4B FF FF FF               je 0x14030ad3c
0030ADF1  4D 8D BE E0 35 00 00            lea r15, [r14 + 0x35e0]
0030ADF8  41 C6 86 D9 35 00 00 02         mov byte ptr [r14 + 0x35d9], 2
0030AE00  49 8B CF                        mov rcx, r15
0030AE03  E8 E8 08 F5 FF                  call 0x14025b6f0
0030AE08  0F B6 93 D0 00 00 00            movzx edx, byte ptr [rbx + 0xd0]
0030AE0F  49 8B CF                        mov rcx, r15
0030AE12  4C 8B 83 C8 00 00 00            mov r8, qword ptr [rbx + 0xc8]
0030AE19  E8 A2 08 F5 FF                  call 0x14025b6c0
0030AE1E  E9 19 FF FF FF                  jmp 0x14030ad3c
0030AE23  4D 8D BE E0 35 00 00            lea r15, [r14 + 0x35e0]
0030AE2A  EB DC                           jmp 0x14030ae08
0030AE2C  49 83 BE B8 8E 00 00 00         cmp qword ptr [r14 + 0x8eb8], 0
0030AE34  0F 84 29 FF FF FF               je 0x14030ad63
0030AE3A  4C 3B F3                        cmp r14, rbx
0030AE3D  0F 84 20 FF FF FF               je 0x14030ad63
0030AE43  8B 09                           mov ecx, dword ptr [rcx]
0030AE45  8B C1                           mov eax, ecx
0030AE47  25 00 00 04 00                  and eax, 0x40000
0030AE4C  0F BA E1 14                     bt ecx, 0x14
0030AE50  0F 83 16 02 00 00               jae 0x14030b06c
0030AE56  80 3D AA A1 CB 00 00            cmp byte ptr [rip + 0xcba1aa], 0
0030AE5D  49 8B 8E B8 8E 00 00            mov rcx, qword ptr [r14 + 0x8eb8]
0030AE64  C7 41 0C 02 00 00 00            mov dword ptr [rcx + 0xc], 2
0030AE6B  44 8B 7B 24                     mov r15d, dword ptr [rbx + 0x24]
0030AE6F  75 13                           jne 0x14030ae84
0030AE71  43 0F B6 44 7D 01               movzx eax, byte ptr [r13 + r15*2 + 1]
0030AE77  47 0F B6 7C 7D 00               movzx r15d, byte ptr [r13 + r15*2]
0030AE7D  41 C1 E7 06                     shl r15d, 6
0030AE81  44 0B F8                        or r15d, eax
0030AE84  44 89 79 08                     mov dword ptr [rcx + 8], r15d
0030AE88  8B 05 86 BC CB 00               mov eax, dword ptr [rip + 0xcbbc86]
0030AE8E  A8 20                           test al, 0x20
0030AE90  74 0D                           je 0x14030ae9f
0030AE92  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
0030AE95  BA 02 00 00 00                  mov edx, 2
0030AE9A  E8 21 04 1F 00                  call 0x1404fb2c0
0030AE9F  41 8B D7                        mov edx, r15d
0030AEA2  B9 C2 00 00 40                  mov ecx, 0x400000c2
0030AEA7  48 C1 EA 20                     shr rdx, 0x20
0030AEAB  41 8B C7                        mov eax, r15d
0030AEAE  0F 30                           wrmsr
0030AEB0  E9 AE FE FF FF                  jmp 0x14030ad63
0030AEB5  48 8B 4C FE 28                  mov rcx, qword ptr [rsi + rdi*8 + 0x28]
0030AEBA  45 33 C0                        xor r8d, r8d
0030AEBD  48 8B D3                        mov rdx, rbx
0030AEC0  E8 87 08 00 00                  call 0x14030b74c
0030AEC5  E9 7D FE FF FF                  jmp 0x14030ad47
0030AECA  48 8D 55 E0                     lea rdx, [rbp - 0x20]
0030AECE  49 8B CE                        mov rcx, r14
0030AED1  E8 AA 2E 00 00                  call 0x14030dd80
0030AED6  E9 D9 FE FF FF                  jmp 0x14030adb4
0030AEDB  49 8B D6                        mov rdx, r14
0030AEDE  48 8B CE                        mov rcx, rsi
0030AEE1  E8 7A 81 04 00                  call 0x140353060
0030AEE6  4C 8B D0                        mov r10, rax
0030AEE9  0F B6 50 20                     movzx edx, byte ptr [rax + 0x20]
0030AEED  4C 8B 00                        mov r8, qword ptr [rax]
0030AEF0  F6 C2 20                        test dl, 0x20
0030AEF3  75 04                           jne 0x14030aef9
0030AEF5  80 48 22 01                     or byte ptr [rax + 0x22], 1
0030AEF9  80 60 22 FD                     and byte ptr [rax + 0x22], 0xfd
0030AEFD  41 B3 FE                        mov r11b, 0xfe
0030AF00  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
0030AF04  49 89 42 10                     mov qword ptr [r10 + 0x10], rax
0030AF08  8A C2                           mov al, dl
0030AF0A  24 C5                           and al, 0xc5
0030AF0C  0C 05                           or al, 5
0030AF0E  41 88 42 20                     mov byte ptr [r10 + 0x20], al
0030AF12  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
0030AF16  45 20 5A 21                     and byte ptr [r10 + 0x21], r11b
0030AF1A  49 89 42 18                     mov qword ptr [r10 + 0x18], rax
0030AF1E  F6 C2 02                        test dl, 2
0030AF21  0F 85 9C 01 00 00               jne 0x14030b0c3
0030AF27  C6 87 84 01 00 00 01            mov byte ptr [rdi + 0x184], 1
0030AF2E  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0030AF38  41 B9 01 00 00 00               mov r9d, 1
0030AF3E  48 8B D7                        mov rdx, rdi
0030AF41  49 8B CE                        mov rcx, r14
0030AF44  8B 00                           mov eax, dword ptr [rax]
0030AF46  44 0F BE 87 C3 00 00 00         movsx r8d, byte ptr [rdi + 0xc3]
0030AF4E  89 87 B4 01 00 00               mov dword ptr [rdi + 0x1b4], eax
0030AF54  48 8D 45 58                     lea rax, [rbp + 0x58]
0030AF58  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0030AF5D  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
0030AF62  E8 99 DB F0 FF                  call 0x140218b00
0030AF67  F7 05 A3 BB CB 00 00 08 00 00   test dword ptr [rip + 0xcbbba3], 0x800
0030AF71  0F 85 92 01 00 00               jne 0x14030b109
0030AF77  4C 8B 6D F8                     mov r13, qword ptr [rbp - 8]
0030AF7B  E9 D4 FA FF FF                  jmp 0x14030aa54
0030AF80  49 8B D6                        mov rdx, r14
0030AF83  48 8B CE                        mov rcx, rsi
0030AF86  E8 D5 80 04 00                  call 0x140353060
0030AF8B  4C 8B D0                        mov r10, rax
0030AF8E  0F B6 50 20                     movzx edx, byte ptr [rax + 0x20]
0030AF92  4C 8B 00                        mov r8, qword ptr [rax]
0030AF95  F6 C2 20                        test dl, 0x20
0030AF98  75 04                           jne 0x14030af9e
0030AF9A  80 48 22 01                     or byte ptr [rax + 0x22], 1
0030AF9E  80 60 22 FD                     and byte ptr [rax + 0x22], 0xfd
0030AFA2  41 B3 FE                        mov r11b, 0xfe
0030AFA5  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
0030AFA9  49 89 42 10                     mov qword ptr [r10 + 0x10], rax
0030AFAD  8A C2                           mov al, dl
0030AFAF  24 C5                           and al, 0xc5
0030AFB1  0C 05                           or al, 5
0030AFB3  41 88 42 20                     mov byte ptr [r10 + 0x20], al
0030AFB7  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
0030AFBB  45 20 5A 21                     and byte ptr [r10 + 0x21], r11b
0030AFBF  49 89 42 18                     mov qword ptr [r10 + 0x18], rax
0030AFC3  F6 C2 02                        test dl, 2
0030AFC6  0F 84 5B FF FF FF               je 0x14030af27
0030AFCC  45 33 DB                        xor r11d, r11d
0030AFCF  44 38 1E                        cmp byte ptr [rsi], r11b
0030AFD2  77 66                           ja 0x14030b03a
0030AFD4  83 66 04 00                     and dword ptr [rsi + 4], 0
0030AFD8  E9 4A FF FF FF                  jmp 0x14030af27
0030AFDD  4D 8B 67 18                     mov r12, qword ptr [r15 + 0x18]
0030AFE1  48 83 F8 FC                     cmp rax, -4
0030AFE5  77 27                           ja 0x14030b00e
0030AFE7  E8 44 82 04 00                  call 0x140353230
0030AFEC  84 C0                           test al, al
0030AFEE  75 1E                           jne 0x14030b00e
0030AFF0  41 F6 41 21 01                  test byte ptr [r9 + 0x21], 1
0030AFF5  74 04                           je 0x14030affb
0030AFF7  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0030AFFB  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0030B002  48 8B D1                        mov rdx, rcx
0030B005  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0030B009  E8 02 63 EF FF                  call 0x140201310
0030B00E  41 8A 49 20                     mov cl, byte ptr [r9 + 0x20]
0030B012  80 C9 01                        or cl, 1
0030B015  4D 89 61 10                     mov qword ptr [r9 + 0x10], r12
0030B019  41 88 49 20                     mov byte ptr [r9 + 0x20], cl
0030B01D  80 E1 FD                        and cl, 0xfd
0030B020  41 8B 44 24 78                  mov eax, dword ptr [r12 + 0x78]
0030B025  D1 E8                           shr eax, 1
0030B027  24 01                           and al, 1
0030B029  02 C0                           add al, al
0030B02B  32 C1                           xor al, cl
0030B02D  24 C7                           and al, 0xc7
0030B02F  0C 04                           or al, 4
0030B031  41 88 41 20                     mov byte ptr [r9 + 0x20], al
0030B035  E9 59 FC FF FF                  jmp 0x14030ac93
0030B03A  41 8B C3                        mov eax, r11d
0030B03D  4A 8D 0C 9D 02 00 00 00         lea rcx, [r11*4 + 2]
0030B045  48 03 C8                        add rcx, rax
0030B048  48 8D 0C CE                     lea rcx, [rsi + rcx*8]
0030B04C  49 3B CA                        cmp rcx, r10
0030B04F  74 0B                           je 0x14030b05c
0030B051  45 33 C9                        xor r9d, r9d
0030B054  41 B0 01                        mov r8b, 1
0030B057  E8 E4 72 04 00                  call 0x140352340
0030B05C  0F B6 06                        movzx eax, byte ptr [rsi]
0030B05F  41 FF C3                        inc r11d
0030B062  44 3B D8                        cmp r11d, eax
0030B065  72 D3                           jb 0x14030b03a
0030B067  E9 68 FF FF FF                  jmp 0x14030afd4
0030B06C  85 C0                           test eax, eax
0030B06E  0F 84 EF FC FF FF               je 0x14030ad63
0030B074  0F B6 C1                        movzx eax, cl
0030B077  3B C2                           cmp eax, edx
0030B079  0F 8D E4 FC FF FF               jge 0x14030ad63
0030B07F  E9 D2 FD FF FF                  jmp 0x14030ae56
0030B084  0F B6 0E                        movzx ecx, byte ptr [rsi]
0030B087  44 3B F9                        cmp r15d, ecx
0030B08A  0F 83 FF FA FF FF               jae 0x14030ab8f
0030B090  41 8B C7                        mov eax, r15d
0030B093  4A 8D 0C BD 02 00 00 00         lea rcx, [r15*4 + 2]
0030B09B  48 03 C8                        add rcx, rax
0030B09E  48 8D 0C CE                     lea rcx, [rsi + rcx*8]
0030B0A2  48 3B D9                        cmp rbx, rcx
0030B0A5  74 17                           je 0x14030b0be
0030B0A7  45 33 C9                        xor r9d, r9d
0030B0AA  49 8B D5                        mov rdx, r13
0030B0AD  45 8D 41 02                     lea r8d, [r9 + 2]
0030B0B1  E8 1A D1 F4 FF                  call 0x1402581d0
0030B0B6  84 C0                           test al, al
0030B0B8  0F 84 1D FE FF FF               je 0x14030aedb
0030B0BE  41 FF C7                        inc r15d
0030B0C1  EB C1                           jmp 0x14030b084
0030B0C3  45 33 DB                        xor r11d, r11d
0030B0C6  44 38 1E                        cmp byte ptr [rsi], r11b
0030B0C9  0F 86 05 FF FF FF               jbe 0x14030afd4
0030B0CF  41 8B C3                        mov eax, r11d
0030B0D2  4A 8D 0C 9D 02 00 00 00         lea rcx, [r11*4 + 2]
0030B0DA  48 03 C8                        add rcx, rax
0030B0DD  48 8D 0C CE                     lea rcx, [rsi + rcx*8]
0030B0E1  49 3B CA                        cmp rcx, r10
0030B0E4  74 0B                           je 0x14030b0f1
0030B0E6  45 33 C9                        xor r9d, r9d
0030B0E9  41 B0 01                        mov r8b, 1
0030B0EC  E8 4F 72 04 00                  call 0x140352340
0030B0F1  0F B6 06                        movzx eax, byte ptr [rsi]
0030B0F4  41 FF C3                        inc r11d
0030B0F7  44 3B D8                        cmp r11d, eax
0030B0FA  72 D3                           jb 0x14030b0cf
0030B0FC  E9 D3 FE FF FF                  jmp 0x14030afd4
0030B101  45 33 FF                        xor r15d, r15d
0030B104  E9 7B FF FF FF                  jmp 0x14030b084
0030B109  44 8B 45 58                     mov r8d, dword ptr [rbp + 0x58]
0030B10D  45 33 C9                        xor r9d, r9d
0030B110  41 8B 56 24                     mov edx, dword ptr [r14 + 0x24]
0030B114  48 8B CF                        mov rcx, rdi
0030B117  E8 28 83 F1 FF                  call 0x140223444
0030B11C  E9 56 FE FF FF                  jmp 0x14030af77
0030B121  48 8D 55 E8                     lea rdx, [rbp - 0x18]
0030B125  49 8B CE                        mov rcx, r14
0030B128  E8 D3 F3 14 00                  call 0x14045a500
0030B12D  E9 79 FC FF FF                  jmp 0x14030adab
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiGroupSchedulingGenerationEnd(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (80);
    v_stack_m40 = *(unsigned __int64 *)(a1 + 8);
    result = KiCaptureTotalCyclesCurrentThread(a1, *(unsigned __int64 *)(a1 + 8), a3, a4);
    if ((*(unsigned __int64 *)(a1 + 8)) == (*(unsigned __int64 *)(a1 + 24))) goto loc_0030AB0B;
loc_0030AA06:
    a4 = 0;
    v_stack_m68 = v_stack_m50;
    result = KiTransitionSchedulingGroupGeneration(a1, *(unsigned __int64 *)(a1 + 8), a3, a4);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(a1 + 14312), a2, 240, a4);
    a3 = 0;
    result = KiStartRescheduleContext(*(unsigned __int64 *)(a1 + 14312), 0, a3, a4);
    if (*(unsigned __int64 *)(a1 + 16) != 0) goto loc_0030AB39;
loc_0030AA54:
    result = KiSearchForNewThreadsForRescheduleContext(*(unsigned __int64 *)(a1 + 14312), v_stack_m58, a3, a4);
    v_r15 = 0;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13353134))) >> (9));
    v_rdi = 0;
    v_rbx = (unsigned int)((v_rbx) & (2));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_0030AA9F;
loc_0030AA76:
    a1 = (0) + (2);
    result = KiCommitRescheduleContextEntry(*(unsigned __int64 *)(a1 + 14312) + a1 + v_rdi * 4 * 8, a1, (unsigned int)((unsigned int)(v_rbx)), v_stack_m58);
    v_r15 = (unsigned __int8)((v_r15) | ((unsigned __int8)(result)));
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0030AA76;
loc_0030AA9F:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 8)) != 1) goto loc_0030AAC0;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1) = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) >= (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1) = 0;
    }
    if ((unsigned __int8)(v_r15) != 0) goto loc_0030ACD7;
    if (v_stack_m58 != 0) goto loc_0030ACD7;
    if (v_stack_m50 != 0) goto loc_0030ACD7;
loc_0030AAE3:
    result = KiResumeThreadCycleAccumulation(a1, *(unsigned __int64 *)(a1 + 8), v_stack_p8, v_stack_m58);
    v_rsp = (v_rsp) + (80);
    return result;
loc_0030AB0B:
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_0030AB2C;
    if ((*(unsigned __int64 *)(a1 + 16)) == (*(unsigned __int64 *)(a1 + 24))) goto loc_0030AB2C;
    if (((*(unsigned __int8 *)(a1 + 35)) & (1)) != 0) goto loc_0030AA06;
loc_0030AB25:
loc_0030AB2C:
    if (((*(unsigned __int8 *)(a1 + 35)) & (1)) == 0) goto loc_0030AA06;
    goto loc_0030AB25;
loc_0030AB39:
    result = KiIsPrcbThread(v_stack_m58, *(unsigned __int64 *)(a1 + 8), v_stack_p8, v_stack_m58);
    if ((unsigned __int8)(result) != 0) goto loc_0030AA54;
    if (condition_is_below) goto loc_0030AF80;
    if ((*(unsigned __int64 *)(a1 + 8)) == (*(unsigned __int64 *)(a1 + 36480))) goto loc_0030AF80;
    result = KiFindRescheduleContextEntryForPrcb(*(unsigned __int64 *)(a1 + 14312), a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 120)), v_stack_m58);
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 120))) & (2));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m58 + 120))) & (2));
    if (((unsigned __int8)(a3)) > ((unsigned __int8)(a1))) goto loc_0030B101;
loc_0030AB8F:
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8);
    a2 = ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24))) ? 1 : 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(result + 32)) & (254));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(a2);
    a2 = (unsigned __int8)((a2) & (253));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a2)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(result);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 120))) | (*(unsigned int *)(v_stack_m58 + 120)));
    if ((((unsigned __int8)(a1)) & (2)) == 0) goto loc_0030ACC6;
    v_r10 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_0030ACC6;
loc_0030ABED:
    a4 = (v_r10 * 4 + 2) + (0);
    if (result == (*(unsigned __int64 *)(a1 + 14312) + a4 * 8)) goto loc_0030ACB3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 120)))) & (2)) == 0) goto loc_0030AFDD;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8 + 24) - 1) > -4) goto loc_0030AC58;
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8 + 24), a2, a3, *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
    if ((unsigned __int8)(result) != 0) goto loc_0030AC58;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8 + 33)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8 + 24) + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m48, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8 + 24), a3, *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
loc_0030AC58:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8 + 32)) & (254));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8 + 16) = *(unsigned __int64 *)(a1 + 8);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8 + 32) = (unsigned __int8)(result);
    result = (unsigned __int8)((result) & (253));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 120))) >> (1));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (231));
    a1 = (unsigned __int8)((a1) | (4));
    a1 = (unsigned __int8)((a1) | (32));
    result = (unsigned __int8)(((unsigned __int8)(a1)) & (223));
    a1 = (unsigned __int8)(a1);
    if ((*(unsigned __int64 *)(a1 + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8) + 36480))) { a1 = (unsigned int)((unsigned __int8)(result)); }
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8 + 32) = (unsigned __int8)(a1);
loc_0030AC93:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8) + 36480);
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8) + 36480), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8 + 24), a3, *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8) + 36);
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8) + 36480) + 536) = (unsigned int)(result);
    }
    v_r10 = (unsigned int)((v_r10) + 1);
    if (((unsigned int)(v_r10)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0030ABED;
loc_0030ACC6:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 120))) >> (1));
    result = (unsigned int)((result) & (1));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 4) = (unsigned int)(result);
    goto loc_0030AF27;
loc_0030ACD7:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p10, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8 + 24), a3, *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
    if ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + a4 * 8)) == 0) goto loc_0030ADA2;
    v_r12 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_0030AD92;
loc_0030ACFB:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 51))) & (16)) != 0) goto loc_0030ADC9;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 51))) & (8)) == 0) goto loc_0030AD3C;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 7)) == 0) goto loc_0030AD3C;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785)) != 0) goto loc_0030ADDD;
    *(unsigned __int8 *)(a1 + 13785) = 1;
    *(unsigned int *)(a1 + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 36)));
loc_0030AD3C:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 51)) & (2)) != 0) goto loc_0030AEB5;
loc_0030AD47:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 51)) & (4)) == 0) goto loc_0030AD63;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 36536) != 0) goto loc_0030AE2C;
loc_0030AD63:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 16) + 36));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 51)) & (1)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 40);
    }
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((unsigned int)(v_r12)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0030ACFB;
loc_0030AD92:
    result = KiFlushSoftwareInterruptBatch(a1 + 13784, (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_r12 + v_r12 * 4 * 8 + 52)), a3, *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
loc_0030ADA2:
    if (v_stack_m50 != 0) goto loc_0030B121;
loc_0030ADAB:
    if (v_stack_m58 != 0) goto loc_0030AECA;
loc_0030ADB4:
    result = KiAcquirePrcbLocksForIsolationUnit(a1, 1, v_stack_p10, *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
    goto loc_0030AAE3;
loc_0030ADC9:
    result = KiAddProcessorToSoftwareInterruptBatch(a1 + 13784, v_stack_m50, v_stack_p10, *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
    goto loc_0030AD3C;
loc_0030ADDD:
    if (((unsigned __int8)(result)) != 1) goto loc_0030AE23;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13788)))) == (*(unsigned int *)(v_stack_m50 + 36))) goto loc_0030AD3C;
    *(unsigned __int8 *)(a1 + 13785) = 2;
    result = KeAddProcessorAffinityEx(a1 + 13792, (unsigned int)(*(unsigned int *)(a1 + 13788)), v_stack_p10, *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
loc_0030AE08:
    result = KeAddGroupAffinityEx(a1 + 13792, *(unsigned __int8 *)(v_stack_m50 + 208), *(unsigned __int64 *)(v_stack_m50 + 200), *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
    goto loc_0030AD3C;
loc_0030AE23:
    goto loc_0030AE08;
loc_0030AE2C:
    if ((*(unsigned __int64 *)(a1 + 36536)) == 0) goto loc_0030AD63;
    if (a1 == v_stack_m50) goto loc_0030AD63;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13792))))) & (0x40000ULL));
    if (condition_is_above_or_equal) goto loc_0030B06C;
loc_0030AE56:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 36536) + 12) = 2;
    v_r15 = (unsigned int)(*(unsigned int *)(v_stack_m50 + 36));
    if ((*(unsigned __int8 *)(v_rip + 13345194)) == 0) {
        result = *(unsigned __int8 *)(v_stack_m40 + (unsigned int)(*(unsigned int *)(v_stack_m50 + 36)) * 2 + 1);
        v_r15 = *(unsigned __int8 *)(v_stack_m40 + (unsigned int)(*(unsigned int *)(v_stack_m50 + 36)) * 2);
        v_r15 = (unsigned int)((v_r15) << (6));
        v_r15 = (unsigned int)((v_r15) | ((unsigned int)(result)));
    }
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 36536) + 8) = (unsigned int)(v_r15);
    result = (unsigned int)(*(unsigned int *)(v_rip + 13352070));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13352070)))) & (32)) != 0) {
        a1 = *(unsigned int *)(v_stack_m50 + 36);
        a2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(a1, a2, *(unsigned __int64 *)(v_stack_m50 + 200), *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
    }
    a2 = ((unsigned int)((unsigned int)(v_r15))) >> (32);
    goto loc_0030AD63;
loc_0030AEB5:
    a3 = 0;
    result = EtwTraceScheduleThread(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_stack_m58 * 8 + 40), v_stack_m50, a3, *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
    goto loc_0030AD47;
loc_0030AECA:
    result = KiReadyDeferredReadyList(a1, v_stack_m58, a3, *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
    goto loc_0030ADB4;
loc_0030AEDB:
    result = KiFindRescheduleContextEntryForPrcb(*(unsigned __int64 *)(a1 + 14312), a1, a3, *(unsigned __int64 *)(a1 + 14312) + a4 * 8);
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (32)) == 0) {
    }
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (197));
    result = (unsigned __int8)((result) | (5));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(result);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (2)) != 0) goto loc_0030B0C3;
loc_0030AF27:
    *(unsigned __int8 *)(v_stack_m58 + 388) = 1;
    *(unsigned int *)(v_stack_m58 + 436) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24))));
    v_stack_p28 = v_stack_p20;
    v_stack_p20 = 0;
    result = KiAddThreadToPrcbQueue(a1, v_stack_m58, (__int8)(*(unsigned __int8 *)(v_stack_m58 + 195)), 1);
    if (((*(unsigned int *)(v_rip + 13351843)) & (0x800ULL)) != 0) goto loc_0030B109;
loc_0030AF77:
    goto loc_0030AA54;
loc_0030AF80:
    result = KiFindRescheduleContextEntryForPrcb(*(unsigned __int64 *)(a1 + 14312), a1, (__int8)(*(unsigned __int8 *)(v_stack_m58 + 195)), 1);
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (32)) == 0) {
    }
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (197));
    result = (unsigned __int8)((result) | (5));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(result);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (2)) == 0) goto loc_0030AF27;
    v_r11 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) > 0) goto loc_0030B03A;
loc_0030AFD4:
    goto loc_0030AF27;
loc_0030AFDD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24)) > -4) goto loc_0030B00E;
    result = KiIsPrcbThread(*(unsigned __int64 *)(a1 + 14312), *(unsigned __int8 *)(result + 32), *(unsigned __int64 *)(result), 1);
    if ((unsigned __int8)(result) != 0) goto loc_0030B00E;
    if (((*(unsigned __int8 *)(1 + 33)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m48, *(unsigned __int64 *)(a1 + 14312), *(unsigned __int64 *)(result), 1);
loc_0030B00E:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(1 + 32)) | (1));
    *(unsigned __int64 *)(1 + 16) = *(unsigned __int64 *)(v_r15 + 24);
    *(unsigned __int8 *)(1 + 32) = (unsigned __int8)(a1);
    a1 = (unsigned __int8)((a1) & (253));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 24) + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(1 + 32) = (unsigned __int8)(result);
    goto loc_0030AC93;
loc_0030B03A:
    a1 = (v_r11 * 4 + 2) + (0);
    result = 0;
    if ((*(unsigned __int64 *)(a1 + 14312) + a1 * 8) != result) {
        a4 = 0;
        a3 = 1;
        result = KiAdjustRescheduleContextEntryForThreadRemoval(*(unsigned __int64 *)(a1 + 14312) + a1 * 8, *(unsigned __int64 *)(a1 + 14312), a3, a4);
    }
    v_r11 = (unsigned int)((v_r11) + 1);
    if (((unsigned int)(v_r11)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0030B03A;
    goto loc_0030AFD4;
loc_0030B06C:
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) == 0) goto loc_0030AD63;
    if (((unsigned int)((unsigned __int8)(*(unsigned __int64 *)(a1 + 14312) + a1 * 8))) >= ((unsigned int)(*(unsigned __int64 *)(a1 + 14312)))) goto loc_0030AD63;
    goto loc_0030AE56;
loc_0030B084:
    if (((unsigned int)(v_r15)) >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0030AB8F;
    a1 = (v_r15 * 4 + 2) + ((unsigned int)((unsigned int)(v_r15)));
    if (v_stack_m50 == (*(unsigned __int64 *)(a1 + 14312) + a1 * 8)) goto loc_0030B0BE;
    a4 = 0;
    result = KiDoesThreadDominateRescheduleContextEntry(*(unsigned __int64 *)(a1 + 14312) + a1 * 8, v_stack_m40, a4 + 2, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0030AEDB;
loc_0030B0BE:
    v_r15 = (unsigned int)((v_r15) + 1);
    goto loc_0030B084;
loc_0030B0C3:
    v_r11 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_0030AFD4;
loc_0030B0CF:
    a1 = (v_r11 * 4 + 2) + (0);
    result = 0;
    if ((*(unsigned __int64 *)(a1 + 14312) + a1 * 8) != result) {
        a4 = 0;
        a3 = 1;
        result = KiAdjustRescheduleContextEntryForThreadRemoval(*(unsigned __int64 *)(a1 + 14312) + a1 * 8, v_stack_m40, a3, a4);
    }
    v_r11 = (unsigned int)((v_r11) + 1);
    if (((unsigned int)(v_r11)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_0030B0CF;
    goto loc_0030AFD4;
loc_0030B101:
    v_r15 = 0;
    goto loc_0030B084;
loc_0030B109:
    a4 = 0;
    result = EtwTraceReadyQueueInsertion(v_stack_m58, (unsigned int)(*(unsigned int *)(a1 + 36)), (unsigned int)(v_stack_p20), a4);
    goto loc_0030AF77;
loc_0030B121:
    result = KiProcessScbTracingList(a1, v_stack_m50, (unsigned int)(v_stack_p20), a4);
    goto loc_0030ADAB;
}
```

## 5. (Beta) C Style

```c
int64_t KiGroupSchedulingGenerationEnd(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (80);
    v_stack_m40 = *(uint64_t *)(arg1 + 0x8);
    result = KiCaptureTotalCyclesCurrentThread(Arg1, *(uint64_t *)(arg1 + 0x8), Arg3, Arg4);
    if ((*(uint64_t *)(arg1 + 0x8)) == (*(uint64_t *)(arg1 + 0x18))) goto loc_0030AB0B;
loc_0030AA06:
    Arg4 = 0;
    v_stack_m68 = v_stack_m50;
    result = KiTransitionSchedulingGroupGeneration(Arg1, *(uint64_t *)(arg1 + 0x8), Arg3, Arg4);
    Arg2 = 0;
    result = memset(*(uint64_t *)(arg1 + 0x37E8), Arg2, 240, Arg4);
    Arg3 = 0;
    result = KiStartRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), 0, Arg3, Arg4);
    if (*(uint64_t *)(arg1 + 0x10) != 0) goto loc_0030AB39;
loc_0030AA54:
    result = KiSearchForNewThreadsForRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), v_stack_m58, Arg3, Arg4);
    local_r15 = 0;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xCBC0AE))) >> (9));
    local_rdi = 0;
    local_rbx = (uint32_t)((local_rbx) & (2));
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_0030AA9F;
loc_0030AA76:
    Arg1 = (0) + (2);
    result = KiCommitRescheduleContextEntry(*(uint64_t *)(arg1 + 0x37E8) + Arg1 + local_rdi * 4 * 8, Arg1, (uint32_t)((uint32_t)(local_rbx)), v_stack_m58);
    local_r15 = (uint8_t)((local_r15) | ((uint8_t)(result)));
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0030AA76;
loc_0030AA9F:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x8)) != 1) goto loc_0030AAC0;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1)) + 1);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = (uint8_t)(result);
    if (((uint8_t)(result)) >= (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58)))) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = 0;
    }
    if ((uint8_t)(local_r15) != 0) goto loc_0030ACD7;
    if (v_stack_m58 != 0) goto loc_0030ACD7;
    if (v_stack_m50 != 0) goto loc_0030ACD7;
loc_0030AAE3:
    result = KiResumeThreadCycleAccumulation(Arg1, *(uint64_t *)(arg1 + 0x8), v_stack_p8, v_stack_m58);
    local_rsp = (local_rsp) + (80);
    return result;
loc_0030AB0B:
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_0030AB2C;
    if ((*(uint64_t *)(arg1 + 0x10)) == (*(uint64_t *)(arg1 + 0x18))) goto loc_0030AB2C;
    if (((*(uint8_t *)(arg1 + 0x23)) & (1)) != 0) goto loc_0030AA06;
loc_0030AB25:
loc_0030AB2C:
    if (((*(uint8_t *)(arg1 + 0x23)) & (1)) == 0) goto loc_0030AA06;
    goto loc_0030AB25;
loc_0030AB39:
    result = KiIsPrcbThread(v_stack_m58, *(uint64_t *)(arg1 + 0x8), v_stack_p8, v_stack_m58);
    if ((uint8_t)(result) != 0) goto loc_0030AA54;
    if (condition_is_below) goto loc_0030AF80;
    if ((*(uint64_t *)(arg1 + 0x8)) == (*(uint64_t *)(arg1 + 0x8E80))) goto loc_0030AF80;
    result = KiFindRescheduleContextEntryForPrcb(*(uint64_t *)(arg1 + 0x37E8), Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x78)), v_stack_m58);
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x78))) & (2));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x78))) & (2));
    if (((uint8_t)(Arg3)) > ((uint8_t)(Arg1))) goto loc_0030B101;
loc_0030AB8F:
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(result) + 0x8);
    Arg2 = ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(result) + 0x18))) ? 1 : 0;
    result = (uint8_t)((*(uint8_t *)(result + 0x20)) & (254));
    Arg2 = (uint8_t)((Arg2) | ((uint8_t)(result)));
    *(uint8_t *)(result + 0x20) = (uint8_t)(Arg2);
    Arg2 = (uint8_t)((Arg2) & (253));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result) + 0x8) + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg2)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(result + 0x20) = (uint8_t)(result);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x78))) | (*(uint32_t *)(v_stack_m58 + 0x78)));
    if ((((uint8_t)(Arg1)) & (2)) == 0) goto loc_0030ACC6;
    local_r10 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_0030ACC6;
loc_0030ABED:
    Arg4 = (local_r10 * 4 + 2) + (0);
    if (result == (*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8)) goto loc_0030ACB3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x78)))) & (2)) == 0) goto loc_0030AFDD;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8 + 0x18) - 1) > -4) goto loc_0030AC58;
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8 + 0x18), Arg2, Arg3, *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
    if ((uint8_t)(result) != 0) goto loc_0030AC58;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8 + 0x21)) & (1)) != 0) {
    }
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8 + 0x18) + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m48, *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8 + 0x18), Arg3, *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
loc_0030AC58:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8 + 0x20)) & (254));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8 + 0x10) = *(uint64_t *)(arg1 + 0x8);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8 + 0x20) = (uint8_t)(result);
    result = (uint8_t)((result) & (253));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x78))) >> (1));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (231));
    Arg1 = (uint8_t)((Arg1) | (4));
    Arg1 = (uint8_t)((Arg1) | (32));
    result = (uint8_t)(((uint8_t)(Arg1)) & (223));
    Arg1 = (uint8_t)(Arg1);
    if ((*(uint64_t *)(arg1 + 0x8)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8) + 0x8E80))) { Arg1 = (uint32_t)((uint8_t)(result)); }
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8 + 0x20) = (uint8_t)(Arg1);
loc_0030AC93:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8 + 0x18) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8) + 0x8E80);
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8) + 0x8E80), *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8 + 0x18), Arg3, *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
    if ((uint8_t)(result) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8) + 0x24);
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8) + 0x8E80) + 0x218) = (uint32_t)(result);
    }
    local_r10 = (uint32_t)((local_r10) + 1);
    if (((uint32_t)(local_r10)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0030ABED;
loc_0030ACC6:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x78))) >> (1));
    result = (uint32_t)((result) & (1));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x4) = (uint32_t)(result);
    goto loc_0030AF27;
loc_0030ACD7:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p10, *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8 + 0x18), Arg3, *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
    if ((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8)) == 0) goto loc_0030ADA2;
    local_r12 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_0030AD92;
loc_0030ACFB:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x33))) & (16)) != 0) goto loc_0030ADC9;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x33))) & (8)) == 0) goto loc_0030AD3C;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x7)) == 0) goto loc_0030AD3C;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x35D9)) != 0) goto loc_0030ADDD;
    *(uint8_t *)(arg1 + 0x35D9) = 1;
    *(uint32_t *)(arg1 + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x24)));
loc_0030AD3C:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x33)) & (2)) != 0) goto loc_0030AEB5;
loc_0030AD47:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x33)) & (4)) == 0) goto loc_0030AD63;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x8EB8) != 0) goto loc_0030AE2C;
loc_0030AD63:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x10) + 0x24));
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x33)) & (1)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x28);
    }
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((uint32_t)(local_r12)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0030ACFB;
loc_0030AD92:
    result = KiFlushSoftwareInterruptBatch(Arg1 + 13784, (int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_r12 + local_r12 * 4 * 8 + 0x34)), Arg3, *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
loc_0030ADA2:
    if (v_stack_m50 != 0) goto loc_0030B121;
loc_0030ADAB:
    if (v_stack_m58 != 0) goto loc_0030AECA;
loc_0030ADB4:
    result = KiAcquirePrcbLocksForIsolationUnit(Arg1, 1, v_stack_p10, *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
    goto loc_0030AAE3;
loc_0030ADC9:
    result = KiAddProcessorToSoftwareInterruptBatch(Arg1 + 13784, v_stack_m50, v_stack_p10, *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
    goto loc_0030AD3C;
loc_0030ADDD:
    if (((uint8_t)(result)) != 1) goto loc_0030AE23;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35DC)))) == (*(uint32_t *)(v_stack_m50 + 0x24))) goto loc_0030AD3C;
    *(uint8_t *)(arg1 + 0x35D9) = 2;
    result = KeAddProcessorAffinityEx(Arg1 + 13792, (uint32_t)(*(uint32_t *)(arg1 + 0x35DC)), v_stack_p10, *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
loc_0030AE08:
    result = KeAddGroupAffinityEx(Arg1 + 13792, *(uint8_t *)(v_stack_m50 + 0xD0), *(uint64_t *)(v_stack_m50 + 0xC8), *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
    goto loc_0030AD3C;
loc_0030AE23:
    goto loc_0030AE08;
loc_0030AE2C:
    if ((*(uint64_t *)(arg1 + 0x8EB8)) == 0) goto loc_0030AD63;
    if (Arg1 == v_stack_m50) goto loc_0030AD63;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35E0))))) & (0x40000ULL));
    if (condition_is_above_or_equal) goto loc_0030B06C;
loc_0030AE56:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8EB8) + 0xC) = 2;
    local_r15 = (uint32_t)(*(uint32_t *)(v_stack_m50 + 0x24));
    if ((*(uint8_t *)(v_rip + 0xCBA1AA)) == 0) {
        result = *(uint8_t *)(v_stack_m40 + (uint32_t)(*(uint32_t *)(v_stack_m50 + 0x24)) * 2 + 0x1);
        local_r15 = *(uint8_t *)(v_stack_m40 + (uint32_t)(*(uint32_t *)(v_stack_m50 + 0x24)) * 2);
        local_r15 = (uint32_t)((local_r15) << (6));
        local_r15 = (uint32_t)((local_r15) | ((uint32_t)(result)));
    }
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8EB8) + 0x8) = (uint32_t)(local_r15);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xCBBC86));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCBBC86)))) & (32)) != 0) {
        Arg1 = *(uint32_t *)(v_stack_m50 + 0x24);
        Arg2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(Arg1, Arg2, *(uint64_t *)(v_stack_m50 + 0xC8), *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
    }
    Arg2 = ((uint32_t)((uint32_t)(local_r15))) >> (32);
    goto loc_0030AD63;
loc_0030AEB5:
    Arg3 = 0;
    result = EtwTraceScheduleThread(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + v_stack_m58 * 8 + 0x28), v_stack_m50, Arg3, *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
    goto loc_0030AD47;
loc_0030AECA:
    result = KiReadyDeferredReadyList(Arg1, v_stack_m58, Arg3, *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
    goto loc_0030ADB4;
loc_0030AEDB:
    result = KiFindRescheduleContextEntryForPrcb(*(uint64_t *)(arg1 + 0x37E8), Arg1, Arg3, *(uint64_t *)(arg1 + 0x37E8) + Arg4 * 8);
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (32)) == 0) {
    }
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(result + 0x20))) & (197));
    result = (uint8_t)((result) | (5));
    *(uint8_t *)(result + 0x20) = (uint8_t)(result);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (2)) != 0) goto loc_0030B0C3;
loc_0030AF27:
    *(uint8_t *)(v_stack_m58 + 0x184) = 1;
    *(uint32_t *)(v_stack_m58 + 0x1B4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result) + 0x18))));
    v_stack_p28 = v_stack_p20;
    v_stack_p20 = 0;
    result = KiAddThreadToPrcbQueue(Arg1, v_stack_m58, (int8_t)(*(uint8_t *)(v_stack_m58 + 0xC3)), 1);
    if (((*(uint32_t *)(v_rip + 0xCBBBA3)) & (0x800ULL)) != 0) goto loc_0030B109;
loc_0030AF77:
    goto loc_0030AA54;
loc_0030AF80:
    result = KiFindRescheduleContextEntryForPrcb(*(uint64_t *)(arg1 + 0x37E8), Arg1, (int8_t)(*(uint8_t *)(v_stack_m58 + 0xC3)), 1);
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (32)) == 0) {
    }
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(result + 0x20))) & (197));
    result = (uint8_t)((result) | (5));
    *(uint8_t *)(result + 0x20) = (uint8_t)(result);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (2)) == 0) goto loc_0030AF27;
    local_r11 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) > 0) goto loc_0030B03A;
loc_0030AFD4:
    goto loc_0030AF27;
loc_0030AFDD:
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x18)) > -4) goto loc_0030B00E;
    result = KiIsPrcbThread(*(uint64_t *)(arg1 + 0x37E8), *(uint8_t *)(result + 0x20), *(uint64_t *)(result), 1);
    if ((uint8_t)(result) != 0) goto loc_0030B00E;
    if (((*(uint8_t *)(1 + 0x21)) & (1)) != 0) {
    }
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m48, *(uint64_t *)(arg1 + 0x37E8), *(uint64_t *)(result), 1);
loc_0030B00E:
    Arg1 = (uint8_t)((*(uint8_t *)(1 + 0x20)) | (1));
    *(uint64_t *)(1 + 0x10) = *(uint64_t *)(local_r15 + 0x18);
    *(uint8_t *)(1 + 0x20) = (uint8_t)(Arg1);
    Arg1 = (uint8_t)((Arg1) & (253));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x18) + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(1 + 0x20) = (uint8_t)(result);
    goto loc_0030AC93;
loc_0030B03A:
    Arg1 = (local_r11 * 4 + 2) + (0);
    result = 0;
    if ((*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8) != result) {
        Arg4 = 0;
        Arg3 = 1;
        result = KiAdjustRescheduleContextEntryForThreadRemoval(*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8, *(uint64_t *)(arg1 + 0x37E8), Arg3, Arg4);
    }
    local_r11 = (uint32_t)((local_r11) + 1);
    if (((uint32_t)(local_r11)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0030B03A;
    goto loc_0030AFD4;
loc_0030B06C:
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) == 0) goto loc_0030AD63;
    if (((uint32_t)((uint8_t)(*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8))) >= ((uint32_t)(*(uint64_t *)(arg1 + 0x37E8)))) goto loc_0030AD63;
    goto loc_0030AE56;
loc_0030B084:
    if (((uint32_t)(local_r15)) >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0030AB8F;
    Arg1 = (local_r15 * 4 + 2) + ((uint32_t)((uint32_t)(local_r15)));
    if (v_stack_m50 == (*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8)) goto loc_0030B0BE;
    Arg4 = 0;
    result = KiDoesThreadDominateRescheduleContextEntry(*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8, v_stack_m40, Arg4 + 2, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0030AEDB;
loc_0030B0BE:
    local_r15 = (uint32_t)((local_r15) + 1);
    goto loc_0030B084;
loc_0030B0C3:
    local_r11 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_0030AFD4;
loc_0030B0CF:
    Arg1 = (local_r11 * 4 + 2) + (0);
    result = 0;
    if ((*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8) != result) {
        Arg4 = 0;
        Arg3 = 1;
        result = KiAdjustRescheduleContextEntryForThreadRemoval(*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8, v_stack_m40, Arg3, Arg4);
    }
    local_r11 = (uint32_t)((local_r11) + 1);
    if (((uint32_t)(local_r11)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_0030B0CF;
    goto loc_0030AFD4;
loc_0030B101:
    local_r15 = 0;
    goto loc_0030B084;
loc_0030B109:
    Arg4 = 0;
    result = EtwTraceReadyQueueInsertion(v_stack_m58, (uint32_t)(*(uint32_t *)(arg1 + 0x24)), (uint32_t)(v_stack_p20), Arg4);
    goto loc_0030AF77;
loc_0030B121:
    result = KiProcessScbTracingList(Arg1, v_stack_m50, (uint32_t)(v_stack_p20), Arg4);
    goto loc_0030ADAB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x23` | `8` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x37E8` | `64` | `R` |
| `Arg1` | `+ 0x8E80` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030A9B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
