# MiUnlinkFreeOrZeroedPage

- RVA: `0x00336C40`–`0x0033780F` (길이 `3,023` bytes)
- VA: `0x0000000140336C40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000769C8`
- 디코드: `694`개 명령, `3,023/3,023` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **16**

### Outgoing calls
- `0x00336D4E` → [MI_PAGE_TO_FULL_COLOR](MI_PAGE_TO_FULL_COLOR_function_00337820.md) (function, `0x00337820`)
- `0x00336E4A` → [ExpWaitForSpinLockExclusiveAndAcquire](../32/ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) (function, `0x003239A0`)
- `0x00337045` → [MiUpdateLargePageCandidateValue](MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x00337143` → [ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented](../32/ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_00323A70.md) (function, `0x00323A70`)
- `0x00337297` → [MiWakeLargePageRebuild](../3B/MiWakeLargePageRebuild_function_003BA2C8.md) (function, `0x003BA2C8`)
- `0x00337326` → [MiUpdateLargePageCandidateValue](MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x00337357` → [MiRecordLargePageCandidate](../37/MiRecordLargePageCandidate_function_0037A624.md) (function, `0x0037A624`)
- `0x00337448` → [MiIsFreeZeroPfnCold](../31/MiIsFreeZeroPfnCold_function_0031E5E4.md) (function, `0x0031E5E4`)
- `0x003374B9` → [MiArePageContentsZero](../4D/MiArePageContentsZero_function_004D4278.md) (function, `0x004D4278`)
- `0x00337505` → [MiUpdateAvailableEventsAtDpc](../3B/MiUpdateAvailableEventsAtDpc_function_003BC804.md) (function, `0x003BC804`)
- `0x0033753D` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0033754C` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00337579` → [MiObtainFreePages](../3B/MiObtainFreePages_function_003BB724.md) (function, `0x003BB724`)
- `0x003375A4` → [MiSlabDemotionLowMemoryConditionUpdate](../3B/MiSlabDemotionLowMemoryConditionUpdate_function_003BB7E0.md) (function, `0x003BB7E0`)
- `0x003375C4` → [KeSetEvent](KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0033760C` → [MiUpdateLargePageCandidateValue](MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x0033765D` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x003376C2` → [MiPageListCollision](../43/MiPageListCollision_function_00436B48.md) (function, `0x00436B48`)
- `0x003376D1` → [MiSetFreeZeroPfnCold](../37/MiSetFreeZeroPfnCold_function_00379428.md) (function, `0x00379428`)
- `0x00337741` → [MiUpdateLargePageCandidateValue](MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x0033779C` → [MiIncreaseAvailablePages](../3B/MiIncreaseAvailablePages_function_003BCC10.md) (function, `0x003BCC10`)
- `0x003377AB` → [MiUpdateAvailableEventsAtDpc](../3B/MiUpdateAvailableEventsAtDpc_function_003BC804.md) (function, `0x003BC804`)

### Direct callers
- [MiGetPerfectColorHeadPage](../28/MiGetPerfectColorHeadPage_function_00289CA8.md) at `0x00289EAF`
- [MiTradePage](../28/MiTradePage_function_0028D160.md) at `0x0028D33B`
- [MiCoalesceFreeSmallPages](MiCoalesceFreeSmallPages_function_00336340.md) at `0x00336793`
- [MiPageFreeToZero](MiPageFreeToZero_function_00337A30.md) at `0x00337B89`
- [MiLargePagePromote](../37/MiLargePagePromote_function_0037915C.md) at `0x003792A8`
- [MiLargeFreePageToMdl](../42/MiLargeFreePageToMdl_function_00420880.md) at `0x004208CA`
- [MiDemoteLargeFreePage](../43/MiDemoteLargeFreePage_function_00435118.md) at `0x00435254`
- [MiPurgeZeroListHead](../4C/MiPurgeZeroListHead_function_004CE464.md) at `0x004CE553`
- [MiTryUnlinkNodeLargePages](../68/MiTryUnlinkNodeLargePages_function_0068ADA0.md) at `0x0068AF4D`
- [MiTransferPartitionPageRun](../69/MiTransferPartitionPageRun_function_00691DCC.md) at `0x00691FBA`
- [MiScrubLargePage](../69/MiScrubLargePage_function_006942E8.md) at `0x0069449C`
- [sub_006FA666](../6F/Unknown_function_006FA666.md) at `0x006FA697`

### Static image references
- `0x00336CA5` → RVA `0x00011C60` (`.rdata`; read)
- `0x00336CBD` → RVA `0x00E30088` (`.data`; read)
- `0x00336DB5` → RVA `0x00FC5002` (`ALMOSTRO`; read)
- `0x00336E26` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00336E82` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00336ECE` → RVA `0x00E3014C` (`.data`; read)
- `0x00337072` → RVA `0x00E2DC80` (`.data`; read)
- `0x0033708D` → RVA `0x00010880` (`.rdata`; read)
- `0x00337130` → RVA `0x00F0DE58` (`.data`; read)
- `0x00337282` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00337497` → RVA `0x00E30270` (`.data`; read)
- `0x0033749F` → RVA `0x00FC5054` (`ALMOSTRO`; reference)
- `0x003374A5` → RVA `0x00E30270` (`.data`; write)
- `0x0033752F` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00337626` → RVA `0x00FC6B30` (`ALMOSTRO`; read)
- `0x00337674` → RVA `0x00E301A8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00336C40  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00336C45  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00336C4A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00336C4F  55                              push rbp
00336C50  56                              push rsi
00336C51  57                              push rdi
00336C52  41 54                           push r12
00336C54  41 55                           push r13
00336C56  41 56                           push r14
00336C58  41 57                           push r15
00336C5A  48 81 EC A0 00 00 00            sub rsp, 0xa0
00336C61  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
00336C65  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00336C6F  48 C1 E1 04                     shl rcx, 4
00336C73  45 33 F6                        xor r14d, r14d
00336C76  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
00336C7E  41 8B D8                        mov ebx, r8d
00336C81  41 8B F6                        mov esi, r14d
00336C84  48 8B C0                        mov rax, rax
00336C87  4C 8D 2C 01                     lea r13, [rcx + rax]
00336C8B  41 BC 03 00 00 00               mov r12d, 3
00336C91  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
00336C95  41 8B CC                        mov ecx, r12d
00336C98  48 0F BA E0 28                  bt rax, 0x28
00336C9D  0F 82 75 04 00 00               jb 0x140337118
00336CA3  8B C1                           mov eax, ecx
00336CA5  4C 8D 3D B4 AF CD FF            lea r15, [rip - 0x32504c]
00336CAC  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00336CB1  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00336CB5  49 8B 14 C7                     mov rdx, qword ptr [r15 + rax*8]
00336CB9  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
00336CBD  48 8B 0D C4 93 AF 00            mov rcx, qword ptr [rip + 0xaf93c4]
00336CC4  48 C1 E8 2B                     shr rax, 0x2b
00336CC8  25 FF 03 00 00                  and eax, 0x3ff
00336CCD  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
00336CD2  48 8B 2C C1                     mov rbp, qword ptr [rcx + rax*8]
00336CD6  48 89 6C 24 50                  mov qword ptr [rsp + 0x50], rbp
00336CDB  48 83 FA 01                     cmp rdx, 1
00336CDF  0F 85 DE 07 00 00               jne 0x1403374c3
00336CE5  48 C7 C7 FF FF FF FF            mov rdi, 0xffffffffffffffff
00336CEC  F0 48 0F C1 BD 00 49 00 00      lock xadd qword ptr [rbp + 0x4900], rdi
00336CF5  48 FF CF                        dec rdi
00336CF8  48 3B BD 00 41 00 00            cmp rdi, qword ptr [rbp + 0x4100]
00336CFF  0F 84 A3 0A 00 00               je 0x1403377a8
00336D05  48 3B BD 08 41 00 00            cmp rdi, qword ptr [rbp + 0x4108]
00336D0C  0F 84 96 0A 00 00               je 0x1403377a8
00336D12  48 8D 47 01                     lea rax, [rdi + 1]
00336D16  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00336D1B  B9 01 00 00 00                  mov ecx, 1
00336D20  48 81 FF 20 04 00 00            cmp rdi, 0x420
00336D27  0F 86 35 08 00 00               jbe 0x140337562
00336D2D  48 81 FF 9F 00 00 00            cmp rdi, 0x9f
00336D34  0F 82 11 0A 00 00               jb 0x14033774b
00336D3A  41 0F B6 45 22                  movzx eax, byte ptr [r13 + 0x22]
00336D3F  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00336D47  83 E0 07                        and eax, 7
00336D4A  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00336D4E  E8 CD 0A 00 00                  call 0x140337820
00336D53  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
00336D58  8B E8                           mov ebp, eax
00336D5A  8B F8                           mov edi, eax
00336D5C  C1 ED 09                        shr ebp, 9
00336D5F  83 E5 3F                        and ebp, 0x3f
00336D62  8B C5                           mov eax, ebp
00336D64  48 69 D0 80 DF 00 00            imul rdx, rax, 0xdf80
00336D6B  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00336D70  49 03 52 10                     add rdx, qword ptr [r10 + 0x10]
00336D74  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00336D79  48 8D 0C 80                     lea rcx, [rax + rax*4]
00336D7D  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
00336D81  C1 E8 10                        shr eax, 0x10
00336D84  48 C1 E1 08                     shl rcx, 8
00336D88  48 03 CA                        add rcx, rdx
00336D8B  44 0F B6 C8                     movzx r9d, al
00336D8F  41 C1 E9 06                     shr r9d, 6
00336D93  F6 C3 04                        test bl, 4
00336D96  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00336D9B  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
00336D9F  0F 85 DF 05 00 00               jne 0x140337384
00336DA5  8B C7                           mov eax, edi
00336DA7  8B CF                           mov ecx, edi
00336DA9  C1 E8 10                        shr eax, 0x10
00336DAC  C1 E9 0F                        shr ecx, 0xf
00336DAF  83 E0 03                        and eax, 3
00336DB2  83 E1 01                        and ecx, 1
00336DB5  80 3D 46 E2 C8 00 01            cmp byte ptr [rip + 0xc8e246], 1
00336DBC  0F 87 45 09 00 00               ja 0x140337707
00336DC2  49 8B D6                        mov rdx, r14
00336DC5  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00336DCA  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00336DCF  48 8D 0C 80                     lea rcx, [rax + rax*4]
00336DD3  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00336DD8  44 0F B6 DF                     movzx r11d, dil
00336DDC  4C 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], r9
00336DE4  4C 89 5C 24 78                  mov qword ptr [rsp + 0x78], r11
00336DE9  48 8D 04 48                     lea rax, [rax + rcx*2]
00336DED  49 8D 0C 40                     lea rcx, [r8 + rax*2]
00336DF1  4D 6B C3 58                     imul r8, r11, 0x58
00336DF5  48 8D 04 4A                     lea rax, [rdx + rcx*2]
00336DF9  49 8D 0C 81                     lea rcx, [r9 + rax*4]
00336DFD  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00336E02  4C 03 84 C8 E0 03 00 00         add r8, qword ptr [rax + rcx*8 + 0x3e0]
00336E0A  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00336E0F  48 39 B4 24 E8 00 00 00         cmp qword ptr [rsp + 0xe8], rsi
00336E17  0F 85 91 00 00 00               jne 0x140336eae
00336E1D  49 83 C0 20                     add r8, 0x20
00336E21  BE 02 00 00 00                  mov esi, 2
00336E26  F6 05 D9 FC C8 00 21            test byte ptr [rip + 0xc8fcd9], 0x21
00336E2D  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00336E32  0F 85 F8 02 00 00               jne 0x140337130
00336E38  F0 41 0F BA 28 1F               lock bts dword ptr [r8], 0x1f
00336E3E  44 89 74 24 70                  mov dword ptr [rsp + 0x70], r14d
00336E43  73 18                           jae 0x140336e5d
00336E45  B2 FF                           mov dl, 0xff
00336E47  49 8B C8                        mov rcx, r8
00336E4A  E8 51 CB FE FF                  call 0x1403239a0
00336E4F  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00336E54  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
00336E59  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00336E5D  41 8B 10                        mov edx, dword ptr [r8]
00336E60  8B CA                           mov ecx, edx
00336E62  0F BA F1 1E                     btr ecx, 0x1e
00336E66  81 F9 00 00 00 80               cmp ecx, 0x80000000
00336E6C  74 3B                           je 0x140336ea9
00336E6E  8B 5C 24 70                     mov ebx, dword ptr [rsp + 0x70]
00336E72  0F BA E2 1E                     bt edx, 0x1e
00336E76  72 08                           jb 0x140336e80
00336E78  F0 41 81 08 00 00 00 40         lock or dword ptr [r8], 0x40000000
00336E80  FF C3                           inc ebx
00336E82  85 1D 24 E4 C8 00               test dword ptr [rip + 0xc8e424], ebx
00336E88  0F 84 A1 06 00 00               je 0x14033752f
00336E8E  F3 90                           pause
00336E90  41 8B 10                        mov edx, dword ptr [r8]
00336E93  8B C2                           mov eax, edx
00336E95  0F BA F0 1E                     btr eax, 0x1e
00336E99  3D 00 00 00 80                  cmp eax, 0x80000000
00336E9E  75 D2                           jne 0x140336e72
00336EA0  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
00336EA4  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
00336EA9  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00336EAE  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00336EB2  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00336EB7  48 F7 D9                        neg rcx
00336EBA  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
00336EC2  49 8B 84 C2 E0 1B 00 00         mov rax, qword ptr [r10 + rax*8 + 0x1be0]
00336ECA  F0 48 01 08                     lock add qword ptr [rax], rcx
00336ECE  83 3D 77 92 AF 00 01            cmp dword ptr [rip + 0xaf9277], 1
00336ED5  0F 84 91 07 00 00               je 0x14033766c
00336EDB  BA 01 00 00 00                  mov edx, 1
00336EE0  F0 49 FF 08                     lock dec qword ptr [r8]
00336EE4  49 B9 00 00 00 00 00 FF FF FF   movabs r9, 0xffffff0000000000
00336EEE  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
00336EF2  49 BB FF FF FF FF FF 00 00 00   movabs r11, 0xffffffffff
00336EFC  48 3B 84 24 E0 00 00 00         cmp rax, qword ptr [rsp + 0xe0]
00336F04  0F 85 43 02 00 00               jne 0x14033714d
00336F0A  49 8B 45 00                     mov rax, qword ptr [r13]
00336F0E  49 B9 FF FF FF FF 3F 00 00 00   movabs r9, 0x3fffffffff
00336F18  49 23 C3                        and rax, r11
00336F1B  49 89 40 10                     mov qword ptr [r8 + 0x10], rax
00336F1F  49 3B C1                        cmp rax, r9
00336F22  0F 84 86 02 00 00               je 0x1403371ae
00336F28  4C 8D 1C 40                     lea r11, [rax + rax*2]
00336F2C  48 B8 18 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000018
00336F36  49 C1 E3 04                     shl r11, 4
00336F3A  48 8B C0                        mov rax, rax
00336F3D  4C 03 D8                        add r11, rax
00336F40  48 B8 FF FF FF FF 3F FF FF FF   movabs rax, 0xffffff3fffffffff
00336F4A  49 8B 13                        mov rdx, qword ptr [r11]
00336F4D  48 8B CA                        mov rcx, rdx
00336F50  48 23 C8                        and rcx, rax
00336F53  48 8B C2                        mov rax, rdx
00336F56  49 0B C9                        or rcx, r9
00336F59  F0 49 0F B1 0B                  lock cmpxchg qword ptr [r11], rcx
00336F5E  4C 8B C0                        mov r8, rax
00336F61  48 3B D0                        cmp rdx, rax
00336F64  74 23                           je 0x140336f89
00336F66  48 BA FF FF FF FF 3F FF FF FF   movabs rdx, 0xffffff3fffffffff
00336F70  49 8B C8                        mov rcx, r8
00336F73  4C 23 C2                        and r8, rdx
00336F76  4D 0B C1                        or r8, r9
00336F79  48 8B C1                        mov rax, rcx
00336F7C  F0 4D 0F B1 03                  lock cmpxchg qword ptr [r11], r8
00336F81  4C 8B C0                        mov r8, rax
00336F84  48 3B C8                        cmp rcx, rax
00336F87  75 E7                           jne 0x140336f70
00336F89  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
00336F8E  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00336F93  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
00336F97  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00336F9B  C1 E8 10                        shr eax, 0x10
00336F9E  24 FD                           and al, 0xfd
00336FA0  0C 05                           or al, 5
00336FA2  88 44 24 32                     mov byte ptr [rsp + 0x32], al
00336FA6  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00336FAA  41 89 45 20                     mov dword ptr [r13 + 0x20], eax
00336FAE  44 39 74 24 34                  cmp dword ptr [rsp + 0x34], r14d
00336FB3  0F 84 8C 04 00 00               je 0x140337445
00336FB9  8B CE                           mov ecx, esi
00336FBB  83 C9 04                        or ecx, 4
00336FBE  45 38 B2 E5 3E 00 00            cmp byte ptr [r10 + 0x3ee5], r14b
00336FC5  0F 44 CE                        cmove ecx, esi
00336FC8  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00336FCC  F6 C1 02                        test cl, 2
00336FCF  74 11                           je 0x140336fe2
00336FD1  F6 05 2E FB C8 00 01            test byte ptr [rip + 0xc8fb2e], 1
00336FD8  0F 85 65 06 00 00               jne 0x140337643
00336FDE  45 89 70 20                     mov dword ptr [r8 + 0x20], r14d
00336FE2  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
00336FE6  49 8B C6                        mov rax, r14
00336FE9  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00336FEE  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00336FF6  F0 49 FF 4C C8 08               lock dec qword ptr [r8 + rcx*8 + 8]
00336FFC  48 81 FE 00 00 10 00            cmp rsi, 0x100000
00337003  0F 82 06 05 00 00               jb 0x14033750f
00337009  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
00337011  48 8D 04 82                     lea rax, [rdx + rax*4]
00337015  F0 49 FF 4C C0 18               lock dec qword ptr [r8 + rax*8 + 0x18]
0033701B  80 3D E0 DF C8 00 01            cmp byte ptr [rip + 0xc8dfe0], 1
00337022  0F 87 A6 05 00 00               ja 0x1403375ce
00337028  40 32 FF                        xor dil, dil
0033702B  83 FB 03                        cmp ebx, 3
0033702E  0F 85 6D 02 00 00               jne 0x1403372a1
00337034  45 33 C9                        xor r9d, r9d
00337037  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0033703C  45 8B C4                        mov r8d, r12d
0033703F  48 8B D6                        mov rdx, rsi
00337042  49 8B CA                        mov rcx, r10
00337045  E8 36 7F 00 00                  call 0x14033ef80
0033704A  41 F6 45 22 08                  test byte ptr [r13 + 0x22], 8
0033704F  0F 85 6A 06 00 00               jne 0x1403376bf
00337055  4D 89 75 00                     mov qword ptr [r13], r14
00337059  48 B9 00 00 00 00 00 FF FF FF   movabs rcx, 0xffffff0000000000
00337063  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
00337067  48 23 C1                        and rax, rcx
0033706A  49 89 45 18                     mov qword ptr [r13 + 0x18], rax
0033706E  49 8B 4D 10                     mov rcx, qword ptr [r13 + 0x10]
00337072  48 8B 05 07 6C AF 00            mov rax, qword ptr [rip + 0xaf6c07]
00337079  48 85 C0                        test rax, rax
0033707C  74 0F                           je 0x14033708d
0033707E  F6 C1 10                        test cl, 0x10
00337081  0F 85 9A 01 00 00               jne 0x140337221
00337087  48 F7 D0                        not rax
0033708A  48 23 C8                        and rcx, rax
0033708D  48 8B 05 EC 97 CD FF            mov rax, qword ptr [rip - 0x326814]
00337094  BB 01 00 00 00                  mov ebx, 1
00337099  49 89 45 10                     mov qword ptr [r13 + 0x10], rax
0033709D  B8 FD FF FF FF                  mov eax, 0xfffffffd
003370A2  48 C1 E9 20                     shr rcx, 0x20
003370A6  48 3B C8                        cmp rcx, rax
003370A9  0F 84 1D 06 00 00               je 0x1403376cc
003370AF  83 7C 24 34 01                  cmp dword ptr [rsp + 0x34], 1
003370B4  0F 85 C3 03 00 00               jne 0x14033747d
003370BA  49 8B 4D 10                     mov rcx, qword ptr [r13 + 0x10]
003370BE  B8 80 00 00 00                  mov eax, 0x80
003370C3  48 85 C9                        test rcx, rcx
003370C6  0F 85 54 04 00 00               jne 0x140337520
003370CC  48 8B 15 AD 6B AF 00            mov rdx, qword ptr [rip + 0xaf6bad]
003370D3  48 85 D2                        test rdx, rdx
003370D6  74 12                           je 0x1403370ea
003370D8  48 8B CA                        mov rcx, rdx
003370DB  48 0B C8                        or rcx, rax
003370DE  B8 90 00 00 00                  mov eax, 0x90
003370E3  F6 C2 80                        test dl, 0x80
003370E6  48 0F 44 C1                     cmove rax, rcx
003370EA  49 89 45 10                     mov qword ptr [r13 + 0x10], rax
003370EE  48 83 7C 24 60 10               cmp qword ptr [rsp + 0x60], 0x10
003370F4  0F 84 30 01 00 00               je 0x14033722a
003370FA  8B C3                           mov eax, ebx
003370FC  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00337104  48 81 C4 A0 00 00 00            add rsp, 0xa0
0033710B  41 5F                           pop r15
0033710D  41 5E                           pop r14
0033710F  41 5D                           pop r13
00337111  41 5C                           pop r12
00337113  5F                              pop rdi
00337114  5E                              pop rsi
00337115  5D                              pop rbp
00337116  C3                              ret
00337117  CC                              int3
00337118  41 8B 45 24                     mov eax, dword ptr [r13 + 0x24]
0033711C  C1 E8 1B                        shr eax, 0x1b
0033711F  83 E0 03                        and eax, 3
00337122  2B C8                           sub ecx, eax
00337124  41 3B CC                        cmp ecx, r12d
00337127  41 0F 44 CC                     cmove ecx, r12d
0033712B  E9 73 FB FF FF                  jmp 0x140336ca3
00337130  8B 05 22 6D BD 00               mov eax, dword ptr [rip + 0xbd6d22]
00337136  85 C0                           test eax, eax
00337138  0F 85 FA FC FF FF               jne 0x140336e38
0033713E  B2 FF                           mov dl, 0xff
00337140  49 8B C8                        mov rcx, r8
00337143  E8 28 C9 FE FF                  call 0x140323a70
00337148  E9 57 FD FF FF                  jmp 0x140336ea4
0033714D  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
00337151  49 23 C3                        and rax, r11
00337154  48 8D 14 40                     lea rdx, [rax + rax*2]
00337158  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00337162  48 C1 E2 04                     shl rdx, 4
00337166  48 8B C0                        mov rax, rax
00337169  48 03 D0                        add rdx, rax
0033716C  49 8B 45 00                     mov rax, qword ptr [r13]
00337170  48 8B C8                        mov rcx, rax
00337173  48 33 0A                        xor rcx, qword ptr [rdx]
00337176  49 23 C9                        and rcx, r9
00337179  49 B9 FF FF FF FF 3F 00 00 00   movabs r9, 0x3fffffffff
00337183  48 33 C8                        xor rcx, rax
00337186  48 89 0A                        mov qword ptr [rdx], rcx
00337189  49 8B 45 00                     mov rax, qword ptr [r13]
0033718D  49 23 C3                        and rax, r11
00337190  49 3B C1                        cmp rax, r9
00337193  0F 85 27 02 00 00               jne 0x1403373c0
00337199  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
0033719D  49 23 C3                        and rax, r11
003371A0  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
003371A5  49 89 40 18                     mov qword ptr [r8 + 0x18], rax
003371A9  E9 E5 FD FF FF                  jmp 0x140336f93
003371AE  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
003371B3  4C 8B D2                        mov r10, rdx
003371B6  4D 89 48 18                     mov qword ptr [r8 + 0x18], r9
003371BA  41 8B 40 08                     mov eax, dword ptr [r8 + 8]
003371BE  44 0F B6 C8                     movzx r9d, al
003371C2  44 8B C0                        mov r8d, eax
003371C5  8B D0                           mov edx, eax
003371C7  49 C1 E8 10                     shr r8, 0x10
003371CB  41 83 E0 03                     and r8d, 3
003371CF  48 C1 EA 0F                     shr rdx, 0xf
003371D3  41 0F B6 C9                     movzx ecx, r9b
003371D7  83 E2 01                        and edx, 1
003371DA  80 E1 3F                        and cl, 0x3f
003371DD  49 D3 E2                        shl r10, cl
003371E0  4B 8D 0C 80                     lea rcx, [r8 + r8*4]
003371E4  49 F7 D2                        not r10
003371E7  48 8D 14 4A                     lea rdx, [rdx + rcx*2]
003371EB  8B C8                           mov ecx, eax
003371ED  48 C1 E8 14                     shr rax, 0x14
003371F1  83 E0 01                        and eax, 1
003371F4  48 C1 E9 12                     shr rcx, 0x12
003371F8  83 E1 03                        and ecx, 3
003371FB  4C 8D 04 91                     lea r8, [rcx + rdx*4]
003371FF  4A 8D 04 40                     lea rax, [rax + r8*2]
00337203  48 03 C0                        add rax, rax
00337206  49 C1 E9 06                     shr r9, 6
0033720A  49 8B 84 C3 88 00 00 00         mov rax, qword ptr [r11 + rax*8 + 0x88]
00337212  F0 4E 21 14 C8                  lock and qword ptr [rax + r9*8], r10
00337217  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
0033721C  E9 6D FD FF FF                  jmp 0x140336f8e
00337221  48 83 E1 EF                     and rcx, 0xffffffffffffffef
00337225  E9 63 FE FF FF                  jmp 0x14033708d
0033722A  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
0033722F  41 8B 41 04                     mov eax, dword ptr [r9 + 4]
00337233  A8 10                           test al, 0x10
00337235  0F 85 BF FE FF FF               jne 0x1403370fa
0033723B  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00337240  48 83 C0 10                     add rax, 0x10
00337244  0F 1F 40 00                     nop dword ptr [rax]
00337248  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00337250  48 8B 50 F8                     mov rdx, qword ptr [rax - 8]
00337254  48 8B 08                        mov rcx, qword ptr [rax]
00337257  48 8D 80 00 05 00 00            lea rax, [rax + 0x500]
0033725E  4D 8B 07                        mov r8, qword ptr [r15]
00337261  4D 8D 7F 08                     lea r15, [r15 + 8]
00337265  48 03 D1                        add rdx, rcx
00337268  4C 0F AF C2                     imul r8, rdx
0033726C  4D 03 F0                        add r14, r8
0033726F  49 83 EC 01                     sub r12, 1
00337273  75 DB                           jne 0x140337250
00337275  49 81 FE 00 02 00 00            cmp r14, 0x200
0033727C  0F 87 78 FE FF FF               ja 0x1403370fa
00337282  F6 05 FF F7 C8 00 30            test byte ptr [rip + 0xc8f7ff], 0x30
00337289  0F 84 6B FE FF FF               je 0x1403370fa
0033728F  45 33 C0                        xor r8d, r8d
00337292  8B D5                           mov edx, ebp
00337294  49 8B C9                        mov rcx, r9
00337297  E8 2C 30 08 00                  call 0x1403ba2c8
0033729C  E9 59 FE FF FF                  jmp 0x1403370fa
003372A1  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
003372A6  48 8D 04 41                     lea rax, [rcx + rax*2]
003372AA  F0 49 FF 8C C0 80 03 00 00      lock dec qword ptr [r8 + rax*8 + 0x380]
003372B3  66 44 89 B4 24 F8 00 00 00      mov word ptr [rsp + 0xf8], r14w
003372BC  44 89 74 24 74                  mov dword ptr [rsp + 0x74], r14d
003372C1  48 B9 28 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000028
003372CB  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
003372D3  48 8B 04 08                     mov rax, qword ptr [rax + rcx]
003372D7  48 8B 0D AA 8D AF 00            mov rcx, qword ptr [rip + 0xaf8daa]
003372DE  48 C1 E8 2B                     shr rax, 0x2b
003372E2  25 FF 03 00 00                  and eax, 0x3ff
003372E7  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
003372EB  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
003372F3  44 38 B0 E6 3E 00 00            cmp byte ptr [rax + 0x3ee6], r14b
003372FA  74 65                           je 0x140337361
003372FC  45 33 C9                        xor r9d, r9d
003372FF  48 8B D6                        mov rdx, rsi
00337302  85 DB                           test ebx, ebx
00337304  0F 84 2C 04 00 00               je 0x140337736
0033730A  83 FB 02                        cmp ebx, 2
0033730D  0F 85 E9 02 00 00               jne 0x1403375fc
00337313  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
0033731B  44 8B C3                        mov r8d, ebx
0033731E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00337323  48 8B C8                        mov rcx, rax
00337326  E8 55 7C 00 00                  call 0x14033ef80
0033732B  0F B7 84 24 F8 00 00 00         movzx eax, word ptr [rsp + 0xf8]
00337333  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
00337339  48 3D 00 7C 00 00               cmp rax, 0x7c00
0033733F  75 1B                           jne 0x14033735c
00337341  B8 01 00 00 00                  mov eax, 1
00337346  44 8B C8                        mov r9d, eax
00337349  44 8B C0                        mov r8d, eax
0033734C  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00337354  48 8B D6                        mov rdx, rsi
00337357  E8 C8 32 04 00                  call 0x14037a624
0033735C  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00337361  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00337365  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0033736A  48 83 C0 3A                     add rax, 0x3a
0033736E  48 8D 0C 48                     lea rcx, [rax + rcx*2]
00337372  40 0F B6 C7                     movzx eax, dil
00337376  48 8D 0C 48                     lea rcx, [rax + rcx*2]
0033737A  F0 49 FF 0C C8                  lock dec qword ptr [r8 + rcx*8]
0033737F  E9 C6 FC FF FF                  jmp 0x14033704a
00337384  83 FB 02                        cmp ebx, 2
00337387  B8 58 3B 00 00                  mov eax, 0x3b58
0033738C  41 B8 60 3B 00 00               mov r8d, 0x3b60
00337392  44 0F 43 C0                     cmovae r8d, eax
00337396  4C 03 C2                        add r8, rdx
00337399  49 8B 00                        mov rax, qword ptr [r8]
0033739C  48 8D 50 01                     lea rdx, [rax + 1]
003373A0  48 8B CA                        mov rcx, rdx
003373A3  48 33 C8                        xor rcx, rax
003373A6  48 81 E1 00 00 FF FF            and rcx, 0xffffffffffff0000
003373AD  48 33 CA                        xor rcx, rdx
003373B0  F0 49 0F B1 08                  lock cmpxchg qword ptr [r8], rcx
003373B5  75 E5                           jne 0x14033739c
003373B7  F0 09 34 24                     lock or dword ptr [rsp], esi
003373BB  E9 E5 F9 FF FF                  jmp 0x140336da5
003373C0  4D 8B 4D 18                     mov r9, qword ptr [r13 + 0x18]
003373C4  4C 8D 1C 40                     lea r11, [rax + rax*2]
003373C8  49 C1 E3 04                     shl r11, 4
003373CC  48 B8 18 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000018
003373D6  48 8B C0                        mov rax, rax
003373D9  4C 03 D8                        add r11, rax
003373DC  48 B8 00 00 00 00 00 FF FF FF   movabs rax, 0xffffff0000000000
003373E6  49 8B 13                        mov rdx, qword ptr [r11]
003373E9  48 8B CA                        mov rcx, rdx
003373EC  49 33 C9                        xor rcx, r9
003373EF  48 23 C8                        and rcx, rax
003373F2  48 8B C2                        mov rax, rdx
003373F5  49 33 C9                        xor rcx, r9
003373F8  F0 49 0F B1 0B                  lock cmpxchg qword ptr [r11], rcx
003373FD  4C 8B C0                        mov r8, rax
00337400  48 3B D0                        cmp rdx, rax
00337403  0F 84 80 FB FF FF               je 0x140336f89
00337409  48 BB 00 00 00 00 00 FF FF FF   movabs rbx, 0xffffff0000000000
00337413  0F 1F 40 00                     nop dword ptr [rax]
00337417  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00337420  49 8B C8                        mov rcx, r8
00337423  4D 33 C1                        xor r8, r9
00337426  4C 23 C3                        and r8, rbx
00337429  48 8B C1                        mov rax, rcx
0033742C  4D 33 C1                        xor r8, r9
0033742F  F0 4D 0F B1 03                  lock cmpxchg qword ptr [r11], r8
00337434  4C 8B C0                        mov r8, rax
00337437  48 3B C8                        cmp rcx, rax
0033743A  75 E4                           jne 0x140337420
0033743C  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
00337440  E9 44 FB FF FF                  jmp 0x140336f89
00337445  49 8B CD                        mov rcx, r13
00337448  E8 97 71 FE FF                  call 0x14031e5e4
0033744D  85 C0                           test eax, eax
0033744F  0F 85 64 FB FF FF               jne 0x140336fb9
00337455  83 FB 03                        cmp ebx, 3
00337458  0F 85 5B FB FF FF               jne 0x140336fb9
0033745E  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00337463  48 8B C7                        mov rax, rdi
00337466  48 C1 E8 12                     shr rax, 0x12
0033746A  23 C3                           and eax, ebx
0033746C  49 8B 84 C3 00 14 00 00         mov rax, qword ptr [r11 + rax*8 + 0x1400]
00337474  48 FF 0C C8                     dec qword ptr [rax + rcx*8]
00337478  E9 3C FB FF FF                  jmp 0x140336fb9
0033747D  83 7C 24 30 04                  cmp dword ptr [rsp + 0x30], 4
00337482  0F 83 32 FC FF FF               jae 0x1403370ba
00337488  0F B6 05 F9 F5 C8 00            movzx eax, byte ptr [rip + 0xc8f5f9]
0033748F  84 C0                           test al, al
00337491  0F 89 57 FC FF FF               jns 0x1403370ee
00337497  8B 05 D3 8D AF 00               mov eax, dword ptr [rip + 0xaf8dd3]
0033749D  FF C0                           inc eax
0033749F  85 05 AF DB C8 00               test dword ptr [rip + 0xc8dbaf], eax
003374A5  89 05 C5 8D AF 00               mov dword ptr [rip + 0xaf8dc5], eax
003374AB  0F 85 3D FC FF FF               jne 0x1403370ee
003374B1  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
003374B6  48 8B CE                        mov rcx, rsi
003374B9  E8 BA CD 19 00                  call 0x1404d4278
003374BE  E9 2B FC FF FF                  jmp 0x1403370ee
003374C3  48 8B C2                        mov rax, rdx
003374C6  48 F7 D8                        neg rax
003374C9  F0 48 0F C1 85 00 49 00 00      lock xadd qword ptr [rbp + 0x4900], rax
003374D2  48 8B 8D 08 41 00 00            mov rcx, qword ptr [rbp + 0x4108]
003374D9  48 8B F8                        mov rdi, rax
003374DC  48 2B FA                        sub rdi, rdx
003374DF  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
003374E4  48 3B F9                        cmp rdi, rcx
003374E7  76 72                           jbe 0x14033755b
003374E9  48 8B 8D 00 41 00 00            mov rcx, qword ptr [rbp + 0x4100]
003374F0  48 3B F9                        cmp rdi, rcx
003374F3  0F 87 22 F8 FF FF               ja 0x140336d1b
003374F9  48 3B C1                        cmp rax, rcx
003374FC  0F 86 19 F8 FF FF               jbe 0x140336d1b
00337502  48 8B CD                        mov rcx, rbp
00337505  E8 FA 52 08 00                  call 0x1403bc804
0033750A  E9 0C F8 FF FF                  jmp 0x140336d1b
0033750F  83 FB 03                        cmp ebx, 3
00337512  BA 01 00 00 00                  mov edx, 1
00337517  48 0F 45 C2                     cmovne rax, rdx
0033751B  E9 E9 FA FF FF                  jmp 0x140337009
00337520  48 81 E1 9F FC FF FF            and rcx, 0xfffffffffffffc9f
00337527  48 0B C1                        or rax, rcx
0033752A  E9 BB FB FF FF                  jmp 0x1403370ea
0033752F  8B 05 83 F5 C8 00               mov eax, dword ptr [rip + 0xc8f583]
00337535  A8 40                           test al, 0x40
00337537  0F 84 51 F9 FF FF               je 0x140336e8e
0033753D  E8 4E 7F FD FF                  call 0x14030f490
00337542  84 C0                           test al, al
00337544  0F 84 BB 02 00 00               je 0x140337805
0033754A  8B CB                           mov ecx, ebx
0033754C  E8 0F 7F FD FF                  call 0x14030f460
00337551  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00337556  E9 35 F9 FF FF                  jmp 0x140336e90
0033755B  48 3B C1                        cmp rax, rcx
0033755E  76 89                           jbe 0x1403374e9
00337560  EB A0                           jmp 0x140337502
00337562  48 8B 85 C0 44 00 00            mov rax, qword ptr [rbp + 0x44c0]
00337569  48 85 C0                        test rax, rax
0033756C  74 08                           je 0x140337576
0033756E  0F B6 40 34                     movzx eax, byte ptr [rax + 0x34]
00337572  84 C0                           test al, al
00337574  75 0D                           jne 0x140337583
00337576  48 8B CD                        mov rcx, rbp
00337579  E8 A6 41 08 00                  call 0x1403bb724
0033757E  B9 01 00 00 00                  mov ecx, 1
00337583  48 81 FF A0 00 00 00            cmp rdi, 0xa0
0033758A  0F 83 9D F7 FF FF               jae 0x140336d2d
00337590  48 81 7C 24 68 A0 00 00 00      cmp qword ptr [rsp + 0x68], 0xa0
00337599  0F 82 8E F7 FF FF               jb 0x140336d2d
0033759F  8B D1                           mov edx, ecx
003375A1  48 8B CD                        mov rcx, rbp
003375A4  E8 37 42 08 00                  call 0x1403bb7e0
003375A9  8B 85 B4 04 00 00               mov eax, dword ptr [rbp + 0x4b4]
003375AF  83 F8 FF                        cmp eax, -1
003375B2  0F 84 75 F7 FF FF               je 0x140336d2d
003375B8  48 8D 8D 20 04 00 00            lea rcx, [rbp + 0x420]
003375BF  45 33 C0                        xor r8d, r8d
003375C2  33 D2                           xor edx, edx
003375C4  E8 47 7D 00 00                  call 0x14033f310
003375C9  E9 5F F7 FF FF                  jmp 0x140336d2d
003375CE  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
003375D3  C1 EF 08                        shr edi, 8
003375D6  40 80 E7 01                     and dil, 1
003375DA  40 0F B6 C7                     movzx eax, dil
003375DE  48 8D 0C 41                     lea rcx, [rcx + rax*2]
003375E2  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
003375EA  F0 48 01 84 CA 30 3B 00 00      lock add qword ptr [rdx + rcx*8 + 0x3b30], rax
003375F3  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
003375F7  E9 2F FA FF FF                  jmp 0x14033702b
003375FC  48 8D 4C 24 74                  lea rcx, [rsp + 0x74]
00337601  44 8B C3                        mov r8d, ebx
00337604  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00337609  48 8B C8                        mov rcx, rax
0033760C  E8 6F 79 00 00                  call 0x14033ef80
00337611  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
00337615  25 00 00 F8 1F                  and eax, 0x1ff80000
0033761A  48 3D 00 00 F8 0F               cmp rax, 0xff80000
00337620  0F 85 36 FD FF FF               jne 0x14033735c
00337626  48 0F BA 25 01 F5 C8 00 25      bt qword ptr [rip + 0xc8f501], 0x25
0033762F  0F 83 27 FD FF FF               jae 0x14033735c
00337635  41 B9 01 00 00 00               mov r9d, 1
0033763B  45 33 C0                        xor r8d, r8d
0033763E  E9 09 FD FF FF                  jmp 0x14033734c
00337643  8B 05 0F 68 BD 00               mov eax, dword ptr [rip + 0xbd680f]
00337649  85 C0                           test eax, eax
0033764B  0F 85 8D F9 FF FF               jne 0x140336fde
00337651  48 8B 94 24 D8 00 00 00         mov rdx, qword ptr [rsp + 0xd8]
00337659  49 8D 48 20                     lea rcx, [r8 + 0x20]
0033765D  E8 E2 98 F8 FF                  call 0x1402c0f44
00337662  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
00337667  E9 76 F9 FF FF                  jmp 0x140336fe2
0033766C  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
00337674  48 8B 05 2D 8B AF 00            mov rax, qword ptr [rip + 0xaf8b2d]
0033767B  4C 8B CA                        mov r9, rdx
0033767E  41 83 E1 1F                     and r9d, 0x1f
00337682  48 8B CA                        mov rcx, rdx
00337685  48 C1 E9 05                     shr rcx, 5
00337689  4C 8D 1C 88                     lea r11, [rax + rcx*4]
0033768D  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00337692  49 8D 04 09                     lea rax, [r9 + rcx]
00337696  48 83 F8 20                     cmp rax, 0x20
0033769A  77 3F                           ja 0x1403376db
0033769C  BA 01 00 00 00                  mov edx, 1
003376A1  48 83 F9 20                     cmp rcx, 0x20
003376A5  0F 84 4E 01 00 00               je 0x1403377f9
003376AB  8B C2                           mov eax, edx
003376AD  D3 E0                           shl eax, cl
003376AF  41 8B C9                        mov ecx, r9d
003376B2  FF C8                           dec eax
003376B4  D3 E0                           shl eax, cl
003376B6  F0 41 09 03                     lock or dword ptr [r11], eax
003376BA  E9 21 F8 FF FF                  jmp 0x140336ee0
003376BF  49 8B CD                        mov rcx, r13
003376C2  E8 81 F4 0F 00                  call 0x140436b48
003376C7  E9 89 F9 FF FF                  jmp 0x140337055
003376CC  8B D3                           mov edx, ebx
003376CE  49 8B CD                        mov rcx, r13
003376D1  E8 52 1D 04 00                  call 0x140379428
003376D6  E9 D4 F9 FF FF                  jmp 0x1403370af
003376DB  4D 85 C9                        test r9, r9
003376DE  0F 85 E2 00 00 00               jne 0x1403377c6
003376E4  48 83 F9 20                     cmp rcx, 0x20
003376E8  73 2B                           jae 0x140337715
003376EA  BA 01 00 00 00                  mov edx, 1
003376EF  48 85 C9                        test rcx, rcx
003376F2  0F 84 E8 F7 FF FF               je 0x140336ee0
003376F8  8B C2                           mov eax, edx
003376FA  D3 E0                           shl eax, cl
003376FC  FF C8                           dec eax
003376FE  F0 41 09 03                     lock or dword ptr [r11], eax
00337702  E9 D9 F7 FF FF                  jmp 0x140336ee0
00337707  8B D7                           mov edx, edi
00337709  48 C1 EA 08                     shr rdx, 8
0033770D  83 E2 01                        and edx, 1
00337710  E9 B0 F6 FF FF                  jmp 0x140336dc5
00337715  48 8B D1                        mov rdx, rcx
00337718  48 C1 EA 05                     shr rdx, 5
0033771C  48 6B C2 E0                     imul rax, rdx, -0x20
00337720  48 03 C8                        add rcx, rax
00337723  41 C7 03 FF FF FF FF            mov dword ptr [r11], 0xffffffff
0033772A  49 83 C3 04                     add r11, 4
0033772E  48 83 EA 01                     sub rdx, 1
00337732  74 B6                           je 0x1403376ea
00337734  EB ED                           jmp 0x140337723
00337736  45 33 C0                        xor r8d, r8d
00337739  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0033773E  48 8B C8                        mov rcx, rax
00337741  E8 3A 78 00 00                  call 0x14033ef80
00337746  E9 11 FC FF FF                  jmp 0x14033735c
0033774B  0F BA E3 09                     bt ebx, 9
0033774F  0F 82 E5 F5 FF FF               jb 0x140336d3a
00337755  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0033775E  8B 81 A4 05 00 00               mov eax, dword ptr [rcx + 0x5a4]
00337764  24 0C                           and al, 0xc
00337766  3C 08                           cmp al, 8
00337768  0F 84 CC F5 FF FF               je 0x140336d3a
0033776E  8B 45 04                        mov eax, dword ptr [rbp + 4]
00337771  48 83 FF 20                     cmp rdi, 0x20
00337775  72 49                           jb 0x1403377c0
00337777  8B 89 A4 05 00 00               mov ecx, dword ptr [rcx + 0x5a4]
0033777D  F6 C1 02                        test cl, 2
00337780  75 33                           jne 0x1403377b5
00337782  A8 10                           test al, 0x10
00337784  0F 85 B0 F5 FF FF               jne 0x140336d3a
0033778A  0F BA E3 08                     bt ebx, 8
0033778E  0F 83 A6 F5 FF FF               jae 0x140336d3a
00337794  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00337799  48 8B CD                        mov rcx, rbp
0033779C  E8 6F 54 08 00                  call 0x1403bcc10
003377A1  33 C0                           xor eax, eax
003377A3  E9 54 F9 FF FF                  jmp 0x1403370fc
003377A8  48 8B CD                        mov rcx, rbp
003377AB  E8 54 50 08 00                  call 0x1403bc804
003377B0  E9 5D F5 FF FF                  jmp 0x140336d12
003377B5  48 83 FF 21                     cmp rdi, 0x21
003377B9  72 C7                           jb 0x140337782
003377BB  E9 7A F5 FF FF                  jmp 0x140336d3a
003377C0  A8 04                           test al, 4
003377C2  74 B3                           je 0x140337777
003377C4  EB C4                           jmp 0x14033778a
003377C6  8B C2                           mov eax, edx
003377C8  BA 20 00 00 00                  mov edx, 0x20
003377CD  83 E0 1F                        and eax, 0x1f
003377D0  2B D0                           sub edx, eax
003377D2  B8 01 00 00 00                  mov eax, 1
003377D7  8B CA                           mov ecx, edx
003377D9  D3 E0                           shl eax, cl
003377DB  49 8B C9                        mov rcx, r9
003377DE  FF C8                           dec eax
003377E0  D3 E0                           shl eax, cl
003377E2  F0 41 09 03                     lock or dword ptr [r11], eax
003377E6  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
003377EB  8B C2                           mov eax, edx
003377ED  48 2B C8                        sub rcx, rax
003377F0  49 83 C3 04                     add r11, 4
003377F4  E9 EB FE FF FF                  jmp 0x1403376e4
003377F9  41 C7 03 FF FF FF FF            mov dword ptr [r11], 0xffffffff
00337800  E9 DB F6 FF FF                  jmp 0x140336ee0
00337805  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0033780A  E9 7F F6 FF FF                  jmp 0x140336e8e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnlinkFreeOrZeroedPage(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int8 v_stack_mA6;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p74;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int16 v_stack_pF8;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (160);
    a1 = (a1 + a1 * 2) << (4);
    v_r14 = 0;
    v_stack_m48 = a1;
    if (condition_is_below) goto loc_00337118;
loc_00336CA3:
    v_stack_m80 = 3;
    v_stack_mA8 = 3;
    result = (*(unsigned __int64 *)(a1 + result * 1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m78 = *(unsigned __int64 *)(v_rip - 3297356 + 3 * 8);
    v_stack_m88 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11506628) + result * 8);
    if ((*(unsigned __int64 *)(v_rip - 3297356 + 3 * 8)) != 1) goto loc_003374C3;
    v_rdi = (-1) - 1;
    if (v_rdi == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11506628) + result * 8) + 16640))) goto loc_003377A8;
    if (v_rdi == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11506628) + result * 8) + 16648))) goto loc_003377A8;
loc_00336D12:
    v_stack_m70 = v_rdi + 1;
loc_00336D1B:
    if (v_rdi <= 0x420ULL) goto loc_00337562;
loc_00336D2D:
    if (v_rdi < 159) goto loc_0033774B;
loc_00336D3A:
    result = (unsigned int)((*(unsigned __int8 *)(a1 + result * 1 + 34)) & (7));
    v_stack_mA4 = (unsigned int)(result);
    result = MI_PAGE_TO_FULL_COLOR(v_stack_p8, *(unsigned __int64 *)(v_rip - 3297356 + 3 * 8), a3, a4);
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (9));
    v_rbp = (unsigned int)((v_rbp) & (63));
    a2 = (*(unsigned __int64 *)(v_rip - 3297356 + 3 * 8)) * ((unsigned int)((unsigned int)(v_rbp)));
    a2 = (a2) + (*(unsigned __int64 *)(v_stack_m88 + 16));
    v_stack_mA0 = a2;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + result * 1 + 32))) >> (16));
    a1 = (v_stack_m80 + v_stack_m80 * 4) << (8);
    a1 = (a1) + (a2);
    a4 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    v_stack_m90 = a1;
    if ((((unsigned __int8)((unsigned int)(a3))) & (4)) != 0) goto loc_00337384;
loc_00336DA5:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) >> (16));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) >> (15));
    result = (unsigned int)((result) & (3));
    a1 = (unsigned int)((a1) & (1));
    if ((*(unsigned __int8 *)(v_rip + 13165126)) > 1) goto loc_00337707;
loc_00336DC5:
    v_stack_m70 = a1;
    v_stack_m58 = a4;
    v_stack_m60 = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    a3 = ((unsigned int)(v_stack_mA4)) * ((unsigned __int8)((unsigned int)((unsigned int)(result))));
    a3 = (a3) + (*(unsigned __int64 *)(v_stack_mA0 + a4 + 0 + (unsigned int)(v_stack_mA4) + v_stack_m70 + result + result * 4 * 2 * 2 * 2 * 4 * 8 + 992));
    v_stack_m98 = a3;
    if (v_stack_p10 != 0) goto loc_00336EAE;
    a3 = (a3) + (32);
    v_stack_m80 = a3;
    if (((*(unsigned __int8 *)(v_rip + 13171929)) & (33)) != 0) goto loc_00337130;
loc_00336E38:
    v_stack_m68 = 0;
    result = v_stack_mA0;
    v_r10 = v_stack_m88;
    if (!(condition_is_above_or_equal)) {
        a2 = 255;
        a1 = a3;
        result = ExpWaitForSpinLockExclusiveAndAcquire(a1, a2, a3, a4);
        a3 = v_stack_m80;
        v_r10 = v_stack_m88;
        v_stack_m68 = (unsigned int)(result);
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))))) == 0x80000000ULL) goto loc_00336EA9;
loc_00336E72:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))))) >= 0x80000000ULL) {
    }
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m68)) + 1);
    if (((*(unsigned int *)(v_rip + 13165604)) & ((unsigned int)(v_rbx))) == 0) goto loc_0033752F;
loc_00336E8E:
loc_00336E90:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))))) != 0x80000000ULL) goto loc_00336E72;
loc_00336EA4:
loc_00336EA9:
loc_00336EAE:
    a1 = -(v_stack_m78);
    v_stack_m50 = a1;
    if ((*(unsigned int *)(v_rip + 11506295)) == 1) goto loc_0033766C;
loc_00336EE0:
    if ((*(unsigned __int64 *)(v_stack_m98 + 16)) != v_stack_p8) goto loc_0033714D;
    result = (*(unsigned __int64 *)(a1 + result * 1)) & ((unsigned __int8)((unsigned int)((unsigned int)(result))));
    *(unsigned __int64 *)(v_stack_m98 + 16) = result;
    if (result == a4) goto loc_003371AE;
    v_r11 = (result + result * 2) << (4);
    v_r11 = (v_r11) + (result);
    a1 = (*(unsigned __int64 *)(v_r11)) & (result);
    a1 = (a1) | (a4);
    if ((*(unsigned __int64 *)(v_r11)) == (*(unsigned __int64 *)(v_r11))) goto loc_00336F89;
loc_00336F70:
    a3 = (*(unsigned __int64 *)(v_r11)) & (*(unsigned __int64 *)(v_r11));
    a3 = (a3) | (a4);
    if ((*(unsigned __int64 *)(v_r11)) != (*(unsigned __int64 *)(v_r11))) goto loc_00336F70;
loc_00336F89:
loc_00336F8E:
loc_00336F93:
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + result * 1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + result * 1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    v_stack_mA6 = (unsigned __int8)(result);
    *(unsigned int *)(a1 + result * 1 + 32) = (unsigned int)((unsigned int)(v_stack_mA8));
    if (v_stack_mA4 == 0) goto loc_00337445;
loc_00336FB9:
    a1 = (unsigned int)((2) | (4));
    if ((*(unsigned __int8 *)(v_stack_m88 + 16101)) == 0) { a1 = 2; }
    v_stack_mA8 = (unsigned int)(a1);
    if ((((unsigned __int8)(a1)) & (2)) == 0) goto loc_00336FE2;
    if (((*(unsigned __int8 *)(v_rip + 13171502)) & (1)) != 0) goto loc_00337643;
loc_00336FDE:
    *(unsigned int *)(v_stack_m98 + 32) = 0;
loc_00336FE2:
    if (v_stack_p8 < 0x100000ULL) goto loc_0033750F;
loc_00337009:
    if ((*(unsigned __int8 *)(v_rip + 13164512)) > 1) goto loc_003375CE;
    v_rdi = 0;
loc_0033702B:
    if (((unsigned int)((unsigned int)(v_stack_mA8))) != 3) goto loc_003372A1;
    a4 = 0;
    v_stack_mB8 = 0;
    result = MiUpdateLargePageCandidateValue(v_stack_m88, v_stack_p8, 3, a4);
loc_0033704A:
    if (((*(unsigned __int8 *)(a1 + result * 1 + 34)) & (8)) != 0) goto loc_003376BF;
loc_00337055:
    *(unsigned __int64 *)(a1 + result * 1) = 0;
    result = (*(unsigned __int64 *)(a1 + result * 1 + 24)) & (v_stack_m88);
    *(unsigned __int64 *)(a1 + result * 1 + 24) = result;
    if (*(unsigned __int64 *)(v_rip + 11496455) == 0) goto loc_0033708D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + result * 1 + 16))) & (16)) != 0) goto loc_00337221;
    result = ~(*(unsigned __int64 *)(v_rip + 11496455));
    a1 = (*(unsigned __int64 *)(a1 + result * 1 + 16)) & (result);
loc_0033708D:
    *(unsigned __int64 *)(a1 + result * 1 + 16) = *(unsigned __int64 *)(v_rip - 3303444);
    a1 = (a1) >> (32);
    if (a1 == ((unsigned int)(0xFFFFFFFDULL))) goto loc_003376CC;
loc_003370AF:
    if (v_stack_mA4 != 1) goto loc_0033747D;
loc_003370BA:
    if (*(unsigned __int64 *)(a1 + result * 1 + 16) != 0) goto loc_00337520;
    result = 128;
    if (*(unsigned __int64 *)(v_rip + 11496365) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 11496365);
        a1 = (a1) | (128);
        result = 144;
        if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 11496365))) & (128)) == 0) { result = a1; }
    }
    *(unsigned __int64 *)(a1 + result * 1 + 16) = result;
loc_003370EE:
    if (v_stack_m78 == 16) goto loc_0033722A;
loc_003370FA:
loc_003370FC:
    v_rsp = (v_rsp) + (160);
    return 1;
loc_00337118:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + result * 1 + 36))) >> (27));
    result = (unsigned int)((result) & (3));
    a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    if (((unsigned int)(a1)) == 3) { a1 = 3; }
    goto loc_00336CA3;
loc_00337130:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12414242))) != 0) goto loc_00336E38;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(3, 255, 3, a4);
    goto loc_00336EA4;
loc_0033714D:
    result = (*(unsigned __int64 *)(a1 + result * 1 + 24)) & (v_stack_mA0);
    a2 = (result + result * 2) << (4);
    a2 = (a2) + (result);
    a1 = (*(unsigned __int64 *)(a1 + result * 1)) ^ (*(unsigned __int64 *)(a2));
    a1 = (a1) & (0);
    a1 = (a1) ^ (*(unsigned __int64 *)(a1 + result * 1));
    *(unsigned __int64 *)(a2) = a1;
    result = (*(unsigned __int64 *)(a1 + result * 1)) & (v_stack_mA0);
    if (result != 0) goto loc_003373C0;
    result = (*(unsigned __int64 *)(a1 + result * 1 + 24)) & (v_stack_mA0);
    *(unsigned __int64 *)(3 + 24) = result;
    goto loc_00336F93;
loc_003371AE:
    *(unsigned __int64 *)(3 + 24) = 0;
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(3 + 8))))) >> (16);
    a3 = (unsigned int)((a3) & (3));
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(3 + 8))))) >> (15);
    a2 = (unsigned int)((a2) & (1));
    a1 = (unsigned __int8)(((unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(3 + 8))))) & (63));
    v_r10 = (a2) << ((unsigned __int8)(a1));
    v_r10 = ~(v_r10);
    result = ((unsigned int)(*(unsigned int *)(3 + 8))) >> (20);
    result = (unsigned int)((result) & (1));
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(3 + 8))))) >> (18);
    a1 = (unsigned int)((a1) & (3));
    result = (result + a1 + a2 + a3 + a3 * 4 * 2 * 4 * 2) + (result + a1 + a2 + a3 + a3 * 4 * 2 * 4 * 2);
    a4 = ((unsigned __int8)((unsigned int)(*(unsigned int *)(3 + 8)))) >> (6);
    goto loc_00336F8E;
loc_00337221:
    a1 = (a1) & (-17);
    goto loc_0033708D;
loc_0033722A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p50 + 4)))) & (16)) != 0) goto loc_003370FA;
    result = (v_stack_p38) + (16);
loc_00337250:
    a2 = (*(unsigned __int64 *)(result - 8)) + (*(unsigned __int64 *)(result));
    a3 = (*(unsigned __int64 *)(v_rip - 3297356)) * (a2);
    v_r14 = (v_r14) + (a3);
    v_r12 = (3) - (1);
    if (condition_is_not_equal) goto loc_00337250;
    if (v_r14 > 512) goto loc_003370FA;
    if (((*(unsigned __int8 *)(v_rip + 13170687)) & (48)) == 0) goto loc_003370FA;
    a3 = 0;
    result = MiWakeLargePageRebuild(v_stack_p50, (unsigned int)((unsigned int)(v_rbp)), a3, v_stack_p50);
    goto loc_003370FA;
loc_003372A1:
    v_stack_pF8 = (unsigned __int16)(v_r14);
    v_stack_p74 = (unsigned int)(v_r14);
    result = (*(unsigned __int64 *)(v_stack_p90 + v_stack_p50 * 1)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_pE0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11505066) + result * 8);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11505066) + result * 8) + 16102)) == ((unsigned __int8)(v_r14))) goto loc_00337361;
    a4 = 0;
    if ((unsigned int)(v_stack_p18) == 0) goto loc_00337736;
    if (((unsigned int)(v_stack_p18)) != 2) goto loc_003375FC;
    v_stack_p20 = v_stack_pF8;
    result = MiUpdateLargePageCandidateValue(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11505066) + result * 8), v_stack_p8, (unsigned int)((unsigned int)(v_stack_p18)), a4);
    result = (v_stack_pF8) & (0xFFFFFFFFFFFFFC00ULL);
    if (result != 0x7C00ULL) goto loc_0033735C;
loc_0033734C:
    result = MiRecordLargePageCandidate(v_stack_pE0, v_stack_p8, 1, 1);
loc_0033735C:
loc_00337361:
    result = ((unsigned int)(v_stack_p34)) + (58);
    goto loc_0033704A;
loc_00337384:
    a3 = (unsigned int)(0x3B60ULL);
    if (((unsigned int)(v_stack_p18)) >= 2) { a3 = (unsigned int)((unsigned int)(0x3B58ULL)); }
    a3 = (a3) + (v_stack_p8);
loc_0033739C:
    a1 = (*(unsigned __int64 *)(a3) + 1) ^ (*(unsigned __int64 *)(a3));
    a1 = (a1) & (0xFFFFFFFFFFFF0000ULL);
    a1 = (a1) ^ (*(unsigned __int64 *)(a3) + 1);
    if (condition_is_not_equal) goto loc_0033739C;
    goto loc_00336DA5;
loc_003373C0:
    v_r11 = (*(unsigned __int64 *)(a3) + *(unsigned __int64 *)(a3) * 2) << (4);
    v_r11 = (v_r11) + (*(unsigned __int64 *)(a3));
    a1 = (*(unsigned __int64 *)(v_r11)) ^ (*(unsigned __int64 *)(a1 + result * 1 + 24));
    a1 = (a1) & (*(unsigned __int64 *)(a3));
    a1 = (a1) ^ (*(unsigned __int64 *)(a1 + result * 1 + 24));
    if ((*(unsigned __int64 *)(v_r11)) == (*(unsigned __int64 *)(v_r11))) goto loc_00336F89;
loc_00337420:
    a3 = (*(unsigned __int64 *)(v_r11)) ^ (*(unsigned __int64 *)(a1 + result * 1 + 24));
    a3 = (a3) & (v_stack_p18);
    a3 = (a3) ^ (*(unsigned __int64 *)(a1 + result * 1 + 24));
    if ((*(unsigned __int64 *)(v_r11)) != (*(unsigned __int64 *)(v_r11))) goto loc_00337420;
    goto loc_00336F89;
loc_00337445:
    result = MiIsFreeZeroPfnCold(a1 + result * 1, *(unsigned __int64 *)(v_r11), *(unsigned __int64 *)(v_r11), *(unsigned __int64 *)(a1 + result * 1 + 24));
    if ((unsigned int)(result) != 0) goto loc_00336FB9;
    if (((unsigned int)((unsigned int)(v_stack_p30))) != 3) goto loc_00336FB9;
    result = (0) >> (18);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(v_stack_p30))));
    goto loc_00336FB9;
loc_0033747D:
    if (v_stack_p30 >= 4) goto loc_003370BA;
    if (!sign_flag) goto loc_003370EE;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11505107))) + 1);
    *(unsigned int *)(v_rip + 11505093) = (unsigned int)(result);
    if (((*(unsigned int *)(v_rip + 13163439)) & ((unsigned int)(result))) != 0) goto loc_003370EE;
    result = MiArePageContentsZero(v_stack_p8, v_stack_p60, *(unsigned __int64 *)(v_r11), *(unsigned __int64 *)(a1 + result * 1 + 24));
    goto loc_003370EE;
loc_003374C3:
    result = -(v_stack_p60);
    v_rdi = (result) - (v_stack_p60);
    v_stack_p68 = result;
    if (v_rdi <= (*(unsigned __int64 *)(v_rbp + 16648))) goto loc_0033755B;
loc_003374E9:
    if (v_rdi > (*(unsigned __int64 *)(v_rbp + 16640))) goto loc_00336D1B;
    if (result <= (*(unsigned __int64 *)(v_rbp + 16640))) goto loc_00336D1B;
loc_00337502:
    result = MiUpdateAvailableEventsAtDpc(v_rbp, v_stack_p60, *(unsigned __int64 *)(v_r11), *(unsigned __int64 *)(a1 + result * 1 + 24));
    goto loc_00336D1B;
loc_0033750F:
    if (((unsigned int)((unsigned int)(v_stack_p30))) != 3) { result = 1; }
    goto loc_00337009;
loc_00337520:
    a1 = (v_rbp) & (-865);
    result = (result) | (a1);
    goto loc_003370EA;
loc_0033752F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13170051)))) & (64)) == 0) goto loc_00336E8E;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, 1, *(unsigned __int64 *)(v_r11), *(unsigned __int64 *)(a1 + result * 1 + 24));
    if ((unsigned __int8)(result) == 0) goto loc_00337805;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)(v_stack_p30))), 1, *(unsigned __int64 *)(v_r11), *(unsigned __int64 *)(a1 + result * 1 + 24));
    goto loc_00336E90;
loc_0033755B:
    if (result <= ((unsigned int)((unsigned int)((unsigned int)(v_stack_p30))))) goto loc_003374E9;
    goto loc_00337502;
loc_00337562:
    if (*(unsigned __int64 *)(v_rbp + 17600) == 0) goto loc_00337576;
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 17600) + 52);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 17600) + 52)) == 0) {
        a1 = v_rbp;
        result = MiObtainFreePages(a1, 1, v_stack_p58, *(unsigned __int64 *)(a1 + result * 1 + 24));
        a1 = 1;
    }
    if (v_rdi >= 160) goto loc_00336D2D;
    if (v_stack_p68 < 160) goto loc_00336D2D;
    result = MiSlabDemotionLowMemoryConditionUpdate(v_rbp, (unsigned int)((unsigned int)(a1)), v_stack_p58, *(unsigned __int64 *)(a1 + result * 1 + 24));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 1204)))) == -1) goto loc_00336D2D;
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rbp + 1056, a2, a3, *(unsigned __int64 *)(a1 + result * 1 + 24));
    goto loc_00336D2D;
loc_003375CE:
    v_rdi = (unsigned int)((v_rdi) >> (8));
    v_rdi = (unsigned __int8)((v_rdi) & (1));
    goto loc_0033702B;
loc_003375FC:
    v_stack_p20 = v_stack_p74;
    result = MiUpdateLargePageCandidateValue(v_stack_p88, v_stack_p38, (unsigned int)((unsigned int)((unsigned int)(v_stack_p30))), *(unsigned __int64 *)(a1 + result * 1 + 24));
    result = (unsigned int)(((unsigned int)(v_stack_p74)) & (0x1FF80000ULL));
    if (result != 0xFF80000ULL) goto loc_0033735C;
    if (result >= 0xFF80000ULL) goto loc_0033735C;
    a3 = 0;
    goto loc_0033734C;
loc_00337643:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12412943))) != 0) goto loc_00336FDE;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(a3 + 32, v_stack_pD8, a3, 1);
    goto loc_00336FE2;
loc_0033766C:
    a4 = (unsigned int)((v_stack_pE0) & (31));
    a1 = (v_stack_pE0) >> (5);
    if ((a4 + v_stack_p60 * 1) > 32) goto loc_003376DB;
    if (v_stack_p60 == 32) goto loc_003377F9;
    result = (unsigned int)((1) << ((unsigned __int8)(v_stack_p60)));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) << ((unsigned __int8)((unsigned int)((unsigned int)(a4)))));
    goto loc_00336EE0;
loc_003376BF:
    result = MiPageListCollision(a1 + result * 1, 1, a3, a4);
    goto loc_00337055;
loc_003376CC:
    result = MiSetFreeZeroPfnCold(a1 + result * 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p30))), a3, a4);
    goto loc_003370AF;
loc_003376DB:
    if (a4 != 0) goto loc_003377C6;
loc_003376E4:
    if ((a1 + result * 1) >= 32) goto loc_00337715;
loc_003376EA:
    if (a1 + result * 1 == 0) goto loc_00336EE0;
    result = (unsigned int)((1) << ((unsigned __int8)(a1 + result * 1)));
    result = (unsigned int)((result) - 1);
    goto loc_00336EE0;
loc_00337707:
    a2 = ((unsigned int)((unsigned int)(v_rdi))) >> (8);
    a2 = (unsigned int)((a2) & (1));
    goto loc_00336DC5;
loc_00337715:
    a2 = (a1 + result * 1) >> (5);
    result = (result) * (a2);
    a1 = (a1 + result * 1) + (result);
loc_00337723:
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 11504429) + a1 * 4) = 0xFFFFFFFFULL;
    v_r11 = (*(unsigned __int64 *)(v_rip + 11504429) + a1 * 4) + (4);
    a2 = (a2) - (1);
    if (condition_is_equal) goto loc_003376EA;
    goto loc_00337723;
loc_00337736:
    a3 = 0;
    v_stack_p20 = v_r14;
    result = MiUpdateLargePageCandidateValue(result, a2, a3, a4);
    goto loc_0033735C;
loc_0033774B:
    if (condition_is_below) goto loc_00336D3A;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444))) & (12));
    if (((unsigned __int8)(result)) == 8) goto loc_00336D3A;
    if (v_rdi < 32) goto loc_003377C0;
loc_00337777:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444)))) & (2)) != 0) goto loc_003377B5;
loc_00337782:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp + 4)))) & (16)) != 0) goto loc_00336D3A;
loc_0033778A:
    if (condition_is_above_or_equal) goto loc_00336D3A;
    result = MiIncreaseAvailablePages(v_rbp, v_stack_p60, a3, a4);
    result = 0;
    goto loc_003370FC;
loc_003377A8:
    result = MiUpdateAvailableEventsAtDpc(v_rbp, v_stack_p60, a3, a4);
    goto loc_00336D12;
loc_003377B5:
    if (v_rdi < 33) goto loc_00337782;
    goto loc_00336D3A;
loc_003377C0:
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_00337777;
    goto loc_0033778A;
loc_003377C6:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p60))) & (31));
    a2 = (unsigned int)((32) - ((unsigned int)(result)));
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) << ((unsigned __int8)(a4)));
    a1 = (v_stack_p60) - ((unsigned int)((unsigned int)(a2)));
    v_r11 = (v_r11) + (4);
    goto loc_003376E4;
loc_003377F9:
    *(unsigned int *)(v_r11) = 0xFFFFFFFFULL;
    goto loc_00336EE0;
loc_00337805:
    goto loc_00336E8E;
}
```

## 5. (Beta) C Style

```c
int64_t MiUnlinkFreeOrZeroedPage(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint8_t v_stack_mA6;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint32_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint64_t v_stack_p38;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p74;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint16_t v_stack_pF8;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (160);
    Arg1 = (Arg1 + Arg1 * 2) << (4);
    local_r14 = 0;
    v_stack_m48 = Arg1;
    if (condition_is_below) goto loc_00337118;
loc_00336CA3:
    v_stack_m80 = 3;
    v_stack_mA8 = 3;
    result = (*(uint64_t *)(arg1 + result * 1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m78 = *(uint64_t *)(v_rip - 0x32504C + 0x3 * 8);
    v_stack_m88 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAF93C4) + result * 8);
    if ((*(uint64_t *)(v_rip - 0x32504C + 0x3 * 8)) != 1) goto loc_003374C3;
    local_rdi = (-1) - 1;
    if (local_rdi == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF93C4) + result * 8) + 0x4100))) goto loc_003377A8;
    if (local_rdi == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF93C4) + result * 8) + 0x4108))) goto loc_003377A8;
loc_00336D12:
    v_stack_m70 = local_rdi + 1;
loc_00336D1B:
    if (local_rdi <= 0x420ULL) goto loc_00337562;
loc_00336D2D:
    if (local_rdi < 159) goto loc_0033774B;
loc_00336D3A:
    result = (uint32_t)((*(uint8_t *)(arg1 + result * 1 + 0x22)) & (7));
    v_stack_mA4 = (uint32_t)(result);
    result = MI_PAGE_TO_FULL_COLOR(v_stack_p8, *(uint64_t *)(v_rip - 0x32504C + 0x3 * 8), Arg3, a4);
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (9));
    local_rbp = (uint32_t)((local_rbp) & (63));
    Arg2 = (*(uint64_t *)(v_rip - 0x32504C + 0x3 * 8)) * ((uint32_t)((uint32_t)(local_rbp)));
    Arg2 = (Arg2) + (*(uint64_t *)(v_stack_m88 + 0x10));
    v_stack_mA0 = Arg2;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + result * 1 + 0x20))) >> (16));
    Arg1 = (v_stack_m80 + v_stack_m80 * 4) << (8);
    Arg1 = (Arg1) + (Arg2);
    a4 = (uint32_t)(((uint8_t)(result)) >> (6));
    v_stack_m90 = Arg1;
    if ((((uint8_t)((uint32_t)(Arg3))) & (4)) != 0) goto loc_00337384;
loc_00336DA5:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) >> (16));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) >> (15));
    result = (uint32_t)((result) & (3));
    Arg1 = (uint32_t)((Arg1) & (1));
    if ((*(uint8_t *)(v_rip + 0xC8E246)) > 1) goto loc_00337707;
loc_00336DC5:
    v_stack_m70 = Arg1;
    v_stack_m58 = a4;
    v_stack_m60 = (uint8_t)((uint32_t)((uint32_t)(result)));
    Arg3 = ((uint32_t)(v_stack_mA4)) * ((uint8_t)((uint32_t)((uint32_t)(result))));
    Arg3 = (Arg3) + (*(uint64_t *)(v_stack_mA0 + a4 + 0x0 + (uint32_t)(v_stack_mA4) + v_stack_m70 + result + result * 4 * 2 * 2 * 2 * 4 * 8 + 0x3E0));
    v_stack_m98 = Arg3;
    if (v_stack_p10 != 0) goto loc_00336EAE;
    Arg3 = (Arg3) + (32);
    v_stack_m80 = Arg3;
    if (((*(uint8_t *)(v_rip + 0xC8FCD9)) & (33)) != 0) goto loc_00337130;
loc_00336E38:
    v_stack_m68 = 0;
    result = v_stack_mA0;
    local_r10 = v_stack_m88;
    if (!(condition_is_above_or_equal)) {
        Arg2 = 255;
        Arg1 = Arg3;
        result = ExpWaitForSpinLockExclusiveAndAcquire(Arg1, Arg2, Arg3, a4);
        Arg3 = v_stack_m80;
        local_r10 = v_stack_m88;
        v_stack_m68 = (uint32_t)(result);
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))))) == 0x80000000ULL) goto loc_00336EA9;
loc_00336E72:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))))) >= 0x80000000ULL) {
    }
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m68)) + 1);
    if (((*(uint32_t *)(v_rip + 0xC8E424)) & ((uint32_t)(local_rbx))) == 0) goto loc_0033752F;
loc_00336E8E:
loc_00336E90:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))))) != 0x80000000ULL) goto loc_00336E72;
loc_00336EA4:
loc_00336EA9:
loc_00336EAE:
    Arg1 = -(v_stack_m78);
    v_stack_m50 = Arg1;
    if ((*(uint32_t *)(v_rip + 0xAF9277)) == 1) goto loc_0033766C;
loc_00336EE0:
    if ((*(uint64_t *)(v_stack_m98 + 0x10)) != v_stack_p8) goto loc_0033714D;
    result = (*(uint64_t *)(arg1 + result * 1)) & ((uint8_t)((uint32_t)((uint32_t)(result))));
    *(uint64_t *)(v_stack_m98 + 0x10) = result;
    if (result == a4) goto loc_003371AE;
    local_r11 = (result + result * 2) << (4);
    local_r11 = (local_r11) + (result);
    Arg1 = (*(uint64_t *)(local_r11)) & (result);
    Arg1 = (Arg1) | (a4);
    if ((*(uint64_t *)(local_r11)) == (*(uint64_t *)(local_r11))) goto loc_00336F89;
loc_00336F70:
    Arg3 = (*(uint64_t *)(local_r11)) & (*(uint64_t *)(local_r11));
    Arg3 = (Arg3) | (a4);
    if ((*(uint64_t *)(local_r11)) != (*(uint64_t *)(local_r11))) goto loc_00336F70;
loc_00336F89:
loc_00336F8E:
loc_00336F93:
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + result * 1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + result * 1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    v_stack_mA6 = (uint8_t)(result);
    *(uint32_t *)(arg1 + result * 1 + 0x20) = (uint32_t)((uint32_t)(v_stack_mA8));
    if (v_stack_mA4 == 0) goto loc_00337445;
loc_00336FB9:
    Arg1 = (uint32_t)((2) | (4));
    if ((*(uint8_t *)(v_stack_m88 + 0x3EE5)) == 0) { Arg1 = 2; }
    v_stack_mA8 = (uint32_t)(Arg1);
    if ((((uint8_t)(Arg1)) & (2)) == 0) goto loc_00336FE2;
    if (((*(uint8_t *)(v_rip + 0xC8FB2E)) & (1)) != 0) goto loc_00337643;
loc_00336FDE:
    *(uint32_t *)(v_stack_m98 + 0x20) = 0;
loc_00336FE2:
    if (v_stack_p8 < 0x100000ULL) goto loc_0033750F;
loc_00337009:
    if ((*(uint8_t *)(v_rip + 0xC8DFE0)) > 1) goto loc_003375CE;
    local_rdi = 0;
loc_0033702B:
    if (((uint32_t)((uint32_t)(v_stack_mA8))) != 3) goto loc_003372A1;
    a4 = 0;
    v_stack_mB8 = 0;
    result = MiUpdateLargePageCandidateValue(v_stack_m88, v_stack_p8, 3, a4);
loc_0033704A:
    if (((*(uint8_t *)(arg1 + result * 1 + 0x22)) & (8)) != 0) goto loc_003376BF;
loc_00337055:
    *(uint64_t *)(arg1 + result * 1) = 0;
    result = (*(uint64_t *)(arg1 + result * 1 + 0x18)) & (v_stack_m88);
    *(uint64_t *)(arg1 + result * 1 + 0x18) = result;
    if (*(uint64_t *)(v_rip + 0xAF6C07) == 0) goto loc_0033708D;
    if ((((uint8_t)(*(uint64_t *)(arg1 + result * 1 + 0x10))) & (16)) != 0) goto loc_00337221;
    result = ~(*(uint64_t *)(v_rip + 0xAF6C07));
    Arg1 = (*(uint64_t *)(arg1 + result * 1 + 0x10)) & (result);
loc_0033708D:
    *(uint64_t *)(arg1 + result * 1 + 0x10) = *(uint64_t *)(v_rip - 0x326814);
    Arg1 = (Arg1) >> (32);
    if (Arg1 == ((uint32_t)(0xFFFFFFFDULL))) goto loc_003376CC;
loc_003370AF:
    if (v_stack_mA4 != 1) goto loc_0033747D;
loc_003370BA:
    if (*(uint64_t *)(arg1 + result * 1 + 0x10) != 0) goto loc_00337520;
    result = 128;
    if (*(uint64_t *)(v_rip + 0xAF6BAD) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0xAF6BAD);
        Arg1 = (Arg1) | (128);
        result = 144;
        if ((((uint8_t)(*(uint64_t *)(v_rip + 0xAF6BAD))) & (128)) == 0) { result = Arg1; }
    }
    *(uint64_t *)(arg1 + result * 1 + 0x10) = result;
loc_003370EE:
    if (v_stack_m78 == 16) goto loc_0033722A;
loc_003370FA:
loc_003370FC:
    local_rsp = (local_rsp) + (160);
    return 1;
loc_00337118:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + result * 1 + 0x24))) >> (27));
    result = (uint32_t)((result) & (3));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    if (((uint32_t)(Arg1)) == 3) { Arg1 = 3; }
    goto loc_00336CA3;
loc_00337130:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBD6D22))) != 0) goto loc_00336E38;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(3, 255, 3, a4);
    goto loc_00336EA4;
loc_0033714D:
    result = (*(uint64_t *)(arg1 + result * 1 + 0x18)) & (v_stack_mA0);
    Arg2 = (result + result * 2) << (4);
    Arg2 = (Arg2) + (result);
    Arg1 = (*(uint64_t *)(arg1 + result * 1)) ^ (*(uint64_t *)(Arg2));
    Arg1 = (Arg1) & (0);
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1 + result * 1));
    *(void **)(Arg2) = Arg1;
    result = (*(uint64_t *)(arg1 + result * 1)) & (v_stack_mA0);
    if (result != 0) goto loc_003373C0;
    result = (*(uint64_t *)(arg1 + result * 1 + 0x18)) & (v_stack_mA0);
    *(uint64_t *)(3 + 0x18) = result;
    goto loc_00336F93;
loc_003371AE:
    *(uint64_t *)(3 + 0x18) = 0;
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(3 + 0x8))))) >> (16);
    Arg3 = (uint32_t)((Arg3) & (3));
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(3 + 0x8))))) >> (15);
    Arg2 = (uint32_t)((Arg2) & (1));
    Arg1 = (uint8_t)(((uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(3 + 0x8))))) & (63));
    local_r10 = (Arg2) << ((uint8_t)(Arg1));
    local_r10 = ~(local_r10);
    result = ((uint32_t)(*(uint32_t *)(3 + 0x8))) >> (20);
    result = (uint32_t)((result) & (1));
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(3 + 0x8))))) >> (18);
    Arg1 = (uint32_t)((Arg1) & (3));
    result = (result + Arg1 + Arg2 + Arg3 + Arg3 * 4 * 2 * 4 * 2) + (result + Arg1 + Arg2 + Arg3 + Arg3 * 4 * 2 * 4 * 2);
    a4 = ((uint8_t)((uint32_t)(*(uint32_t *)(3 + 0x8)))) >> (6);
    goto loc_00336F8E;
loc_00337221:
    Arg1 = (Arg1) & (-17);
    goto loc_0033708D;
loc_0033722A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p50 + 0x4)))) & (16)) != 0) goto loc_003370FA;
    result = (v_stack_p38) + (16);
loc_00337250:
    Arg2 = (*(uint64_t *)(result - 0x8)) + (*(uint64_t *)(result));
    Arg3 = (*(uint64_t *)(v_rip - 0x32504C)) * (Arg2);
    local_r14 = (local_r14) + (Arg3);
    local_r12 = (3) - (1);
    if (condition_is_not_equal) goto loc_00337250;
    if (local_r14 > 512) goto loc_003370FA;
    if (((*(uint8_t *)(v_rip + 0xC8F7FF)) & (48)) == 0) goto loc_003370FA;
    Arg3 = 0;
    result = MiWakeLargePageRebuild(v_stack_p50, (uint32_t)((uint32_t)(local_rbp)), Arg3, v_stack_p50);
    goto loc_003370FA;
loc_003372A1:
    v_stack_pF8 = (uint16_t)(local_r14);
    v_stack_p74 = (uint32_t)(local_r14);
    result = (*(uint64_t *)(v_stack_p90 + v_stack_p50 * 1)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_pE0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAF8DAA) + result * 8);
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF8DAA) + result * 8) + 0x3EE6)) == ((uint8_t)(local_r14))) goto loc_00337361;
    a4 = 0;
    if ((uint32_t)(v_stack_p18) == 0) goto loc_00337736;
    if (((uint32_t)(v_stack_p18)) != 2) goto loc_003375FC;
    v_stack_p20 = v_stack_pF8;
    result = MiUpdateLargePageCandidateValue(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF8DAA) + result * 8), v_stack_p8, (uint32_t)((uint32_t)(v_stack_p18)), a4);
    result = (v_stack_pF8) & (0xFFFFFFFFFFFFFC00ULL);
    if (result != 0x7C00ULL) goto loc_0033735C;
loc_0033734C:
    result = MiRecordLargePageCandidate(v_stack_pE0, v_stack_p8, 1, 1);
loc_0033735C:
loc_00337361:
    result = ((uint32_t)(v_stack_p34)) + (58);
    goto loc_0033704A;
loc_00337384:
    Arg3 = (uint32_t)(0x3B60ULL);
    if (((uint32_t)(v_stack_p18)) >= 2) { Arg3 = (uint32_t)((uint32_t)(0x3B58ULL)); }
    Arg3 = (Arg3) + (v_stack_p8);
loc_0033739C:
    Arg1 = (*(uint64_t *)(Arg3) + 1) ^ (*(uint64_t *)(Arg3));
    Arg1 = (Arg1) & (0xFFFFFFFFFFFF0000ULL);
    Arg1 = (Arg1) ^ (*(uint64_t *)(Arg3) + 1);
    if (condition_is_not_equal) goto loc_0033739C;
    goto loc_00336DA5;
loc_003373C0:
    local_r11 = (*(uint64_t *)(Arg3) + *(uint64_t *)(Arg3) * 2) << (4);
    local_r11 = (local_r11) + (*(uint64_t *)(Arg3));
    Arg1 = (*(uint64_t *)(local_r11)) ^ (*(uint64_t *)(arg1 + result * 1 + 0x18));
    Arg1 = (Arg1) & (*(uint64_t *)(Arg3));
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1 + result * 1 + 0x18));
    if ((*(uint64_t *)(local_r11)) == (*(uint64_t *)(local_r11))) goto loc_00336F89;
loc_00337420:
    Arg3 = (*(uint64_t *)(local_r11)) ^ (*(uint64_t *)(arg1 + result * 1 + 0x18));
    Arg3 = (Arg3) & (v_stack_p18);
    Arg3 = (Arg3) ^ (*(uint64_t *)(arg1 + result * 1 + 0x18));
    if ((*(uint64_t *)(local_r11)) != (*(uint64_t *)(local_r11))) goto loc_00337420;
    goto loc_00336F89;
loc_00337445:
    result = MiIsFreeZeroPfnCold(Arg1 + result * 1, *(uint64_t *)(local_r11), *(uint64_t *)(local_r11), *(uint64_t *)(arg1 + result * 1 + 0x18));
    if ((uint32_t)(result) != 0) goto loc_00336FB9;
    if (((uint32_t)((uint32_t)(v_stack_p30))) != 3) goto loc_00336FB9;
    result = (0) >> (18);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(v_stack_p30))));
    goto loc_00336FB9;
loc_0033747D:
    if (v_stack_p30 >= 4) goto loc_003370BA;
    if (!sign_flag) goto loc_003370EE;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xAF8DD3))) + 1);
    *(uint32_t *)(v_rip + 0xAF8DC5) = (uint32_t)(result);
    if (((*(uint32_t *)(v_rip + 0xC8DBAF)) & ((uint32_t)(result))) != 0) goto loc_003370EE;
    result = MiArePageContentsZero(v_stack_p8, v_stack_p60, *(uint64_t *)(local_r11), *(uint64_t *)(arg1 + result * 1 + 0x18));
    goto loc_003370EE;
loc_003374C3:
    result = -(v_stack_p60);
    local_rdi = (result) - (v_stack_p60);
    v_stack_p68 = result;
    if (local_rdi <= (*(uint64_t *)(local_rbp + 0x4108))) goto loc_0033755B;
loc_003374E9:
    if (local_rdi > (*(uint64_t *)(local_rbp + 0x4100))) goto loc_00336D1B;
    if (result <= (*(uint64_t *)(local_rbp + 0x4100))) goto loc_00336D1B;
loc_00337502:
    result = MiUpdateAvailableEventsAtDpc(local_rbp, v_stack_p60, *(uint64_t *)(local_r11), *(uint64_t *)(arg1 + result * 1 + 0x18));
    goto loc_00336D1B;
loc_0033750F:
    if (((uint32_t)((uint32_t)(v_stack_p30))) != 3) { result = 1; }
    goto loc_00337009;
loc_00337520:
    Arg1 = (local_rbp) & (-865);
    result = (result) | (Arg1);
    goto loc_003370EA;
loc_0033752F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8F583)))) & (64)) == 0) goto loc_00336E8E;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, 1, *(uint64_t *)(local_r11), *(uint64_t *)(arg1 + result * 1 + 0x18));
    if ((uint8_t)(result) == 0) goto loc_00337805;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)(v_stack_p30))), 1, *(uint64_t *)(local_r11), *(uint64_t *)(arg1 + result * 1 + 0x18));
    goto loc_00336E90;
loc_0033755B:
    if (result <= ((uint32_t)((uint32_t)((uint32_t)(v_stack_p30))))) goto loc_003374E9;
    goto loc_00337502;
loc_00337562:
    if (*(uint64_t *)(local_rbp + 0x44C0) == 0) goto loc_00337576;
    result = *(uint8_t *)(*(uint64_t *)(local_rbp + 0x44C0) + 0x34);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp + 0x44C0) + 0x34)) == 0) {
        Arg1 = local_rbp;
        result = MiObtainFreePages(Arg1, 1, v_stack_p58, *(uint64_t *)(arg1 + result * 1 + 0x18));
        Arg1 = 1;
    }
    if (local_rdi >= 160) goto loc_00336D2D;
    if (v_stack_p68 < 160) goto loc_00336D2D;
    result = MiSlabDemotionLowMemoryConditionUpdate(local_rbp, (uint32_t)((uint32_t)(Arg1)), v_stack_p58, *(uint64_t *)(arg1 + result * 1 + 0x18));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x4B4)))) == -1) goto loc_00336D2D;
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(local_rbp + 1056, Arg2, Arg3, *(uint64_t *)(arg1 + result * 1 + 0x18));
    goto loc_00336D2D;
loc_003375CE:
    local_rdi = (uint32_t)((local_rdi) >> (8));
    local_rdi = (uint8_t)((local_rdi) & (1));
    goto loc_0033702B;
loc_003375FC:
    v_stack_p20 = v_stack_p74;
    result = MiUpdateLargePageCandidateValue(v_stack_p88, v_stack_p38, (uint32_t)((uint32_t)((uint32_t)(v_stack_p30))), *(uint64_t *)(arg1 + result * 1 + 0x18));
    result = (uint32_t)(((uint32_t)(v_stack_p74)) & (0x1FF80000ULL));
    if (result != 0xFF80000ULL) goto loc_0033735C;
    if (result >= 0xFF80000ULL) goto loc_0033735C;
    Arg3 = 0;
    goto loc_0033734C;
loc_00337643:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBD680F))) != 0) goto loc_00336FDE;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(Arg3 + 32, v_stack_pD8, Arg3, 1);
    goto loc_00336FE2;
loc_0033766C:
    a4 = (uint32_t)((v_stack_pE0) & (31));
    Arg1 = (v_stack_pE0) >> (5);
    if ((a4 + v_stack_p60 * 1) > 32) goto loc_003376DB;
    if (v_stack_p60 == 32) goto loc_003377F9;
    result = (uint32_t)((1) << ((uint8_t)(v_stack_p60)));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) << ((uint8_t)((uint32_t)((uint32_t)(a4)))));
    goto loc_00336EE0;
loc_003376BF:
    result = MiPageListCollision(Arg1 + result * 1, 1, Arg3, a4);
    goto loc_00337055;
loc_003376CC:
    result = MiSetFreeZeroPfnCold(Arg1 + result * 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p30))), Arg3, a4);
    goto loc_003370AF;
loc_003376DB:
    if (a4 != 0) goto loc_003377C6;
loc_003376E4:
    if ((Arg1 + result * 1) >= 32) goto loc_00337715;
loc_003376EA:
    if (Arg1 + result * 1 == 0) goto loc_00336EE0;
    result = (uint32_t)((1) << ((uint8_t)(Arg1 + result * 1)));
    result = (uint32_t)((result) - 1);
    goto loc_00336EE0;
loc_00337707:
    Arg2 = ((uint32_t)((uint32_t)(local_rdi))) >> (8);
    Arg2 = (uint32_t)((Arg2) & (1));
    goto loc_00336DC5;
loc_00337715:
    Arg2 = (Arg1 + result * 1) >> (5);
    result = (result) * (Arg2);
    Arg1 = (Arg1 + result * 1) + (result);
loc_00337723:
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xAF8B2D) + arg1 * 4) = 0xFFFFFFFFULL;
    local_r11 = (*(uint64_t *)(v_rip + 0xAF8B2D) + Arg1 * 4) + (4);
    Arg2 = (Arg2) - (1);
    if (condition_is_equal) goto loc_003376EA;
    goto loc_00337723;
loc_00337736:
    Arg3 = 0;
    v_stack_p20 = local_r14;
    result = MiUpdateLargePageCandidateValue(result, Arg2, Arg3, a4);
    goto loc_0033735C;
loc_0033774B:
    if (condition_is_below) goto loc_00336D3A;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4))) & (12));
    if (((uint8_t)(result)) == 8) goto loc_00336D3A;
    if (local_rdi < 32) goto loc_003377C0;
loc_00337777:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4)))) & (2)) != 0) goto loc_003377B5;
loc_00337782:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x4)))) & (16)) != 0) goto loc_00336D3A;
loc_0033778A:
    if (condition_is_above_or_equal) goto loc_00336D3A;
    result = MiIncreaseAvailablePages(local_rbp, v_stack_p60, Arg3, a4);
    result = 0;
    goto loc_003370FC;
loc_003377A8:
    result = MiUpdateAvailableEventsAtDpc(local_rbp, v_stack_p60, Arg3, a4);
    goto loc_00336D12;
loc_003377B5:
    if (local_rdi < 33) goto loc_00337782;
    goto loc_00336D3A;
loc_003377C0:
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_00337777;
    goto loc_0033778A;
loc_003377C6:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p60))) & (31));
    Arg2 = (uint32_t)((32) - ((uint32_t)(result)));
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(Arg2)))));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) << ((uint8_t)(a4)));
    Arg1 = (v_stack_p60) - ((uint32_t)((uint32_t)(Arg2)));
    local_r11 = (local_r11) + (4);
    goto loc_003376E4;
loc_003377F9:
    *(uint32_t *)(local_r11) = 0xFFFFFFFFULL;
    goto loc_00336EE0;
loc_00337805:
    goto loc_00336E8E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rcx*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00336C40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
