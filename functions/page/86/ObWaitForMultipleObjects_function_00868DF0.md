# ObWaitForMultipleObjects

- RVA: `0x00868DF0`–`0x00869601` (길이 `2,065` bytes)
- VA: `0x0000000140868DF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006BE54`
- 디코드: `495`개 명령, `2,065/2,065` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00868E56` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00868E6D` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00868F0A` → [ExpLookupHandleTableEntry](ExpLookupHandleTableEntry_function_00869DB0.md) (function, `0x00869DB0`)
- `0x00868F4F` → [ExpBlockOnLockedHandleEntry](ExpBlockOnLockedHandleEntry_function_00868838.md) (function, `0x00868838`)
- `0x00868F95` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (function, `0x00430C90`)
- `0x00869064` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (function, `0x00210780`)
- `0x008690DF` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00869130` → [KeWaitForMultipleObjects](../../text/20/KeWaitForMultipleObjects_function_0020D110.md) (function, `0x0020D110`)
- `0x00869179` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008691A3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008691E0` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (function, `0x00430C90`)
- `0x008691F2` → [ExSlowReplenishHandleTableEntry](../../text/44/ExSlowReplenishHandleTableEntry_function_0044BEF0.md) (function, `0x0044BEF0`)
- `0x00869227` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x00869240` → [ExpBlockOnLockedHandleEntry](ExpBlockOnLockedHandleEntry_function_00868838.md) (function, `0x00868838`)
- `0x00869294` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008692CB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086930E` → [ExHandleLogBadReference](../../text/44/ExHandleLogBadReference_function_00440580.md) (function, `0x00440580`)
- `0x00869343` → [ExAllocateFromNPagedLookasideList](../../text/38/ExAllocateFromNPagedLookasideList_function_0038E6C0.md) (function, `0x0038E6C0`)
- `0x00869375` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x008693A3` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x008693C5` → [ExFreeToNPagedLookasideList](../../text/38/ExFreeToNPagedLookasideList_function_0038D9D0.md) (function, `0x0038D9D0`)
- `0x0086942D` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x00869454` → [ObReferenceProcessHandleTable](../89/ObReferenceProcessHandleTable_function_00893B70.md) (function, `0x00893B70`)
- `0x008694D5` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (function, `0x00430C90`)
- `0x008694FE` → [ExFastReplenishHandleTableEntry](../../text/47/ExFastReplenishHandleTableEntry_function_0047E210.md) (function, `0x0047E210`)
- `0x0086951B` → [KeSetKernelStackSwapEnable](../../text/45/KeSetKernelStackSwapEnable_function_00450760.md) (function, `0x00450760`)
- `0x00869545` → [_chkstk](../../text/6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x008695DA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x008695E4` → [KeSetKernelStackSwapEnable](../../text/45/KeSetKernelStackSwapEnable_function_00450760.md) (function, `0x00450760`)
- `0x008695EE` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)

### Direct callers
- [NtWaitForMultipleObjects](../99/NtWaitForMultipleObjects_function_0099E400.md) at `0x0099E515`
- [NtWaitForMultipleObjects32](../9C/NtWaitForMultipleObjects32_function_009C4290.md) at `0x009C43A5`

### Static image references
- `0x00868E0F` → RVA `0x00E0A740` (`.data`; read)
- `0x00868FE8` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00869026` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x00869049` → RVA `0x00EFA128` (`.data`; read)
- `0x0086926C` → RVA `0x00F0F5B8` (`.data`; read)
- `0x008692D5` → RVA `0x00FC6CC0` (`ALMOSTRO`; read)
- `0x00869332` → RVA `0x00E27400` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x00868E56` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00868E6D` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00868F95` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (`PAGE` → `.text`)
  - `0x00869064` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (`PAGE` → `.text`)
  - `0x008690DF` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00869130` → [KeWaitForMultipleObjects](../../text/20/KeWaitForMultipleObjects_function_0020D110.md) (`PAGE` → `.text`)
  - `0x00869179` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008691A3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008691E0` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (`PAGE` → `.text`)
  - `0x008691F2` → [ExSlowReplenishHandleTableEntry](../../text/44/ExSlowReplenishHandleTableEntry_function_0044BEF0.md) (`PAGE` → `.text`)
  - `0x00869227` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x00869294` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008692CB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086930E` → [ExHandleLogBadReference](../../text/44/ExHandleLogBadReference_function_00440580.md) (`PAGE` → `.text`)
  - `0x00869343` → [ExAllocateFromNPagedLookasideList](../../text/38/ExAllocateFromNPagedLookasideList_function_0038E6C0.md) (`PAGE` → `.text`)
  - `0x00869375` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x008693A3` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x008693C5` → [ExFreeToNPagedLookasideList](../../text/38/ExFreeToNPagedLookasideList_function_0038D9D0.md) (`PAGE` → `.text`)
  - `0x0086942D` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x008694D5` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (`PAGE` → `.text`)
  - `0x008694FE` → [ExFastReplenishHandleTableEntry](../../text/47/ExFastReplenishHandleTableEntry_function_0047E210.md) (`PAGE` → `.text`)
  - `0x0086951B` → [KeSetKernelStackSwapEnable](../../text/45/KeSetKernelStackSwapEnable_function_00450760.md) (`PAGE` → `.text`)
  - `0x00869545` → [_chkstk](../../text/6B/_chkstk_function_006BA960.md) (`PAGE` → `.text`)
  - `0x008695DA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x008695E4` → [KeSetKernelStackSwapEnable](../../text/45/KeSetKernelStackSwapEnable_function_00450760.md) (`PAGE` → `.text`)
  - `0x008695EE` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00868DF0  40 55                           push rbp
00868DF2  56                              push rsi
00868DF3  57                              push rdi
00868DF4  41 54                           push r12
00868DF6  41 55                           push r13
00868DF8  41 56                           push r14
00868DFA  41 57                           push r15
00868DFC  48 81 EC D0 04 00 00            sub rsp, 0x4d0
00868E03  48 8D 6C 24 40                  lea rbp, [rsp + 0x40]
00868E08  48 89 9D E0 04 00 00            mov qword ptr [rbp + 0x4e0], rbx
00868E0F  48 8B 05 2A 19 5A 00            mov rax, qword ptr [rip + 0x5a192a]
00868E16  48 33 C5                        xor rax, rbp
00868E19  48 89 85 80 04 00 00            mov qword ptr [rbp + 0x480], rax
00868E20  44 89 4D 18                     mov dword ptr [rbp + 0x18], r9d
00868E24  45 0F B6 F8                     movzx r15d, r8b
00868E28  44 88 45 01                     mov byte ptr [rbp + 1], r8b
00868E2C  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
00868E30  8B F1                           mov esi, ecx
00868E32  89 75 38                        mov dword ptr [rbp + 0x38], esi
00868E35  48 8B 85 00 05 00 00            mov rax, qword ptr [rbp + 0x500]
00868E3C  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00868E40  0F 57 C0                        xorps xmm0, xmm0
00868E43  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
00868E47  33 D2                           xor edx, edx
00868E49  41 B8 00 02 00 00               mov r8d, 0x200
00868E4F  48 8D 8D 80 02 00 00            lea rcx, [rbp + 0x280]
00868E56  E8 E5 DD E5 FF                  call 0x1406c6c40
00868E5B  45 33 ED                        xor r13d, r13d
00868E5E  33 D2                           xor edx, edx
00868E60  41 B8 00 02 00 00               mov r8d, 0x200
00868E66  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
00868E6D  E8 CE DD E5 FF                  call 0x1406c6c40
00868E72  44 88 6D 03                     mov byte ptr [rbp + 3], r13b
00868E76  44 88 6D 02                     mov byte ptr [rbp + 2], r13b
00868E7A  33 C0                           xor eax, eax
00868E7C  48 89 45 08                     mov qword ptr [rbp + 8], rax
00868E80  33 FF                           xor edi, edi
00868E82  48 89 7D 50                     mov qword ptr [rbp + 0x50], rdi
00868E86  83 FE 03                        cmp esi, 3
00868E89  0F 87 E9 03 00 00               ja 0x140869278
00868E8F  45 33 F6                        xor r14d, r14d
00868E92  45 32 E4                        xor r12b, r12b
00868E95  44 88 65 00                     mov byte ptr [rbp], r12b
00868E99  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
00868EA2  48 89 7D 20                     mov qword ptr [rbp + 0x20], rdi
00868EA6  48 8B 9F B8 00 00 00            mov rbx, qword ptr [rdi + 0xb8]
00868EAD  48 89 5D 10                     mov qword ptr [rbp + 0x10], rbx
00868EB1  48 89 5D 60                     mov qword ptr [rbp + 0x60], rbx
00868EB5  66 FF 8F E4 01 00 00            dec word ptr [rdi + 0x1e4]
00868EBC  90                              nop
00868EBD  48 3B 9F 20 02 00 00            cmp rbx, qword ptr [rdi + 0x220]
00868EC4  0F 85 87 05 00 00               jne 0x140869451
00868ECA  48 8B 8B 00 03 00 00            mov rcx, qword ptr [rbx + 0x300]
00868ED1  48 89 4D 48                     mov qword ptr [rbp + 0x48], rcx
00868ED5  45 33 E4                        xor r12d, r12d
00868ED8  4A 8D 1C E5 00 00 00 00         lea rbx, [r12*8]
00868EE0  48 89 5D 40                     mov qword ptr [rbp + 0x40], rbx
00868EE4  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00868EE8  48 8B 34 03                     mov rsi, qword ptr [rbx + rax]
00868EEC  45 84 FF                        test r15b, r15b
00868EEF  0F 84 55 03 00 00               je 0x14086924a
00868EF5  4C 8B F9                        mov r15, rcx
00868EF8  F7 C6 FC 03 00 00               test esi, 0x3fc
00868EFE  0F 84 EE 03 00 00               je 0x1408692f2
00868F04  48 8B D6                        mov rdx, rsi
00868F07  49 8B CF                        mov rcx, r15
00868F0A  E8 A1 0E 00 00                  call 0x140869db0
00868F0F  48 8B F8                        mov rdi, rax
00868F12  48 85 C0                        test rax, rax
00868F15  0F 84 D7 03 00 00               je 0x1408692f2
00868F1B  0F 0D 08                        prefetchw byte ptr [rax]
00868F1E  48 8B 00                        mov rax, qword ptr [rax]
00868F21  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
00868F25  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00868F29  4C 8B 45 28                     mov r8, qword ptr [rbp + 0x28]
00868F2D  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00868F31  90                              nop
00868F32  49 F7 C0 FE FF 01 00            test r8, 0x1fffe
00868F39  0F 84 84 02 00 00               je 0x1408691c3
00868F3F  41 0F B6 C0                     movzx eax, r8b
00868F43  F6 D0                           not al
00868F45  A8 01                           test al, 1
00868F47  74 13                           je 0x140868f5c
00868F49  48 8B D7                        mov rdx, rdi
00868F4C  49 8B CF                        mov rcx, r15
00868F4F  E8 E4 F8 FF FF                  call 0x140868838
00868F54  0F 0D 0F                        prefetchw byte ptr [rdi]
00868F57  48 8B 07                        mov rax, qword ptr [rdi]
00868F5A  EB C5                           jmp 0x140868f21
00868F5C  49 8D 58 FE                     lea rbx, [r8 - 2]
00868F60  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00868F64  49 8B C0                        mov rax, r8
00868F67  48 8B D1                        mov rdx, rcx
00868F6A  F0 48 0F C7 0F                  lock cmpxchg16b xmmword ptr [rdi]
00868F6F  4C 8B C0                        mov r8, rax
00868F72  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
00868F76  48 89 55 30                     mov qword ptr [rbp + 0x30], rdx
00868F7A  0F 94 C0                        sete al
00868F7D  84 C0                           test al, al
00868F7F  74 B0                           je 0x140868f31
00868F81  49 8B C8                        mov rcx, r8
00868F84  48 D1 E9                        shr rcx, 1
00868F87  66 83 F9 10                     cmp cx, 0x10
00868F8B  0F 84 28 05 00 00               je 0x1408694b9
00868F91  48 8D 4D 28                     lea rcx, [rbp + 0x28]
00868F95  E8 F6 7C BC FF                  call 0x140430c90
00868F9A  4C 8B E8                        mov r13, rax
00868F9D  48 8B 5D 40                     mov rbx, qword ptr [rbp + 0x40]
00868FA1  48 85 FF                        test rdi, rdi
00868FA4  0F 84 38 03 00 00               je 0x1408692e2
00868FAA  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
00868FAD  25 FF FF FF 01                  and eax, 0x1ffffff
00868FB2  41 FF C6                        inc r14d
00868FB5  44 89 75 3C                     mov dword ptr [rbp + 0x3c], r14d
00868FB9  49 8D 75 30                     lea rsi, [r13 + 0x30]
00868FBD  48 89 B4 1D 80 02 00 00         mov qword ptr [rbp + rbx + 0x280], rsi
00868FC5  44 0F B6 7D 01                  movzx r15d, byte ptr [rbp + 1]
00868FCA  41 80 FF 01                     cmp r15b, 1
00868FCE  75 44                           jne 0x140869014
00868FD0  F7 D0                           not eax
00868FD2  0F BA E0 14                     bt eax, 0x14
00868FD6  0F 82 98 05 00 00               jb 0x140869574
00868FDC  41 0F B6 45 1A                  movzx eax, byte ptr [r13 + 0x1a]
00868FE1  A8 40                           test al, 0x40
00868FE3  74 2F                           je 0x140869014
00868FE5  83 E0 7F                        and eax, 0x7f
00868FE8  48 8D 0D 11 70 79 FF            lea rcx, [rip - 0x868fef]
00868FEF  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
00868FF7  49 8B CD                        mov rcx, r13
00868FFA  48 2B C8                        sub rcx, rax
00868FFD  48 8B 01                        mov rax, qword ptr [rcx]
00869000  80 78 18 00                     cmp byte ptr [rax + 0x18], 0
00869004  74 0E                           je 0x140869014
00869006  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
0086900A  48 83 F8 01                     cmp rax, 1
0086900E  0F 84 85 04 00 00               je 0x140869499
00869014  49 8B C5                        mov rax, r13
00869017  48 C1 E8 08                     shr rax, 8
0086901B  0F B6 C8                        movzx ecx, al
0086901E  41 0F B6 45 18                  movzx eax, byte ptr [r13 + 0x18]
00869023  48 33 C8                        xor rcx, rax
00869026  0F B6 05 1F DE 75 00            movzx eax, byte ptr [rip + 0x75de1f]
0086902D  48 33 C8                        xor rcx, rax
00869030  48 8D 05 C9 6F 79 FF            lea rax, [rip - 0x869037]
00869037  48 8B BC C8 00 78 FC 00         mov rdi, qword ptr [rax + rcx*8 + 0xfc7800]
0086903F  83 7D 18 01                     cmp dword ptr [rbp + 0x18], 1
00869043  0F 85 8C 02 00 00               jne 0x1408692d5
00869049  48 3B 3D D8 10 69 00            cmp rdi, qword ptr [rip + 0x6910d8]
00869050  0F 84 2A 05 00 00               je 0x140869580
00869056  BA 01 00 00 00                  mov edx, 1
0086905B  41 B8 4F 62 57 74               mov r8d, 0x7457624f
00869061  49 8B CD                        mov rcx, r13
00869064  E8 17 77 9A FF                  call 0x140210780
00869069  48 8B 5F 20                     mov rbx, qword ptr [rdi + 0x20]
0086906D  F6 C3 01                        test bl, 1
00869070  0F 85 37 03 00 00               jne 0x1408693ad
00869076  48 85 DB                        test rbx, rbx
00869079  78 03                           js 0x14086907e
0086907B  48 03 DE                        add rbx, rsi
0086907E  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00869082  48 89 9C 05 80 00 00 00         mov qword ptr [rbp + rax + 0x80], rbx
0086908A  41 FF C4                        inc r12d
0086908D  8B 5D 38                        mov ebx, dword ptr [rbp + 0x38]
00869090  44 3B E3                        cmp r12d, ebx
00869093  73 09                           jae 0x14086909e
00869095  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
00869099  E9 3A FE FF FF                  jmp 0x140868ed8
0086909E  44 0F B6 65 00                  movzx r12d, byte ptr [rbp]
008690A3  48 8B 75 10                     mov rsi, qword ptr [rbp + 0x10]
008690A7  45 84 E4                        test r12b, r12b
008690AA  74 2C                           je 0x1408690d8
008690AC  45 32 E4                        xor r12b, r12b
008690AF  44 88 65 00                     mov byte ptr [rbp], r12b
008690B3  0F 0D 8E E8 01 00 00            prefetchw byte ptr [rsi + 0x1e8]
008690BA  48 8B 86 E8 01 00 00            mov rax, qword ptr [rsi + 0x1e8]
008690C1  48 83 E0 FE                     and rax, 0xfffffffffffffffe
008690C5  48 8D 48 FE                     lea rcx, [rax - 2]
008690C9  F0 48 0F B1 8E E8 01 00 00      lock cmpxchg qword ptr [rsi + 0x1e8], rcx
008690D2  0F 85 4E 03 00 00               jne 0x140869426
008690D8  48 8B 7D 20                     mov rdi, qword ptr [rbp + 0x20]
008690DC  48 8B CF                        mov rcx, rdi
008690DF  E8 2C 5F 9F FF                  call 0x14025f010
008690E4  45 32 ED                        xor r13b, r13b
008690E7  44 88 6D 01                     mov byte ptr [rbp + 1], r13b
008690EB  8B 4D 18                        mov ecx, dword ptr [rbp + 0x18]
008690EE  85 C9                           test ecx, ecx
008690F0  0F 84 57 02 00 00               je 0x14086934d
008690F6  4C 8B 7D 08                     mov r15, qword ptr [rbp + 8]
008690FA  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
008690FF  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
00869103  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00869108  0F B6 85 F8 04 00 00            movzx eax, byte ptr [rbp + 0x4f8]
0086910F  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00869113  0F B6 85 F0 04 00 00            movzx eax, byte ptr [rbp + 0x4f0]
0086911A  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0086911E  41 B9 06 00 00 00               mov r9d, 6
00869124  44 8B C1                        mov r8d, ecx
00869127  48 8D 95 80 00 00 00            lea rdx, [rbp + 0x80]
0086912E  8B CB                           mov ecx, ebx
00869130  E8 DB 3F 9A FF                  call 0x14020d110
00869135  89 45 04                        mov dword ptr [rbp + 4], eax
00869138  EB 20                           jmp 0x14086915a
0086913A  89 45 68                        mov dword ptr [rbp + 0x68], eax
0086913D  89 45 04                        mov dword ptr [rbp + 4], eax
00869140  48 8B 75 60                     mov rsi, qword ptr [rbp + 0x60]
00869144  44 0F B6 6D 01                  movzx r13d, byte ptr [rbp + 1]
00869149  44 8B 75 3C                     mov r14d, dword ptr [rbp + 0x3c]
0086914D  48 8B 7D 20                     mov rdi, qword ptr [rbp + 0x20]
00869151  44 0F B6 65 00                  movzx r12d, byte ptr [rbp]
00869156  4C 8B 7D 08                     mov r15, qword ptr [rbp + 8]
0086915A  45 85 F6                        test r14d, r14d
0086915D  74 25                           je 0x140869184
0086915F  41 8B C6                        mov eax, r14d
00869162  48 8D 9D 80 02 00 00            lea rbx, [rbp + 0x280]
00869169  48 8D 1C C3                     lea rbx, [rbx + rax*8]
0086916D  48 8D 5B F8                     lea rbx, [rbx - 8]
00869171  BA 4F 62 57 74                  mov edx, 0x7457624f
00869176  48 8B 0B                        mov rcx, qword ptr [rbx]
00869179  E8 62 E7 A8 FF                  call 0x1402f78e0
0086917E  41 83 C6 FF                     add r14d, -1
00869182  75 E9                           jne 0x14086916d
00869184  45 84 ED                        test r13b, r13b
00869187  0F 85 EE 01 00 00               jne 0x14086937b
0086918D  4D 85 FF                        test r15, r15
00869190  0F 85 19 01 00 00               jne 0x1408692af
00869196  8B 45 04                        mov eax, dword ptr [rbp + 4]
00869199  48 8B 8D 80 04 00 00            mov rcx, qword ptr [rbp + 0x480]
008691A0  48 33 CD                        xor rcx, rbp
008691A3  E8 98 34 E4 FF                  call 0x1406ac640
008691A8  48 8B 9D E0 04 00 00            mov rbx, qword ptr [rbp + 0x4e0]
008691AF  48 8D A5 90 04 00 00            lea rsp, [rbp + 0x490]
008691B6  41 5F                           pop r15
008691B8  41 5E                           pop r14
008691BA  41 5D                           pop r13
008691BC  41 5C                           pop r12
008691BE  5F                              pop rdi
008691BF  5E                              pop rsi
008691C0  5D                              pop rbp
008691C1  C3                              ret
008691C2  CC                              int3
008691C3  0F 0D 0F                        prefetchw byte ptr [rdi]
008691C6  4C 8B 07                        mov r8, qword ptr [rdi]
008691C9  41 F6 C0 01                     test r8b, 1
008691CD  74 62                           je 0x140869231
008691CF  49 8D 48 FF                     lea rcx, [r8 - 1]
008691D3  49 8B C0                        mov rax, r8
008691D6  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
008691DB  75 E6                           jne 0x1408691c3
008691DD  48 8B CF                        mov rcx, rdi
008691E0  E8 AB 7A BC FF                  call 0x140430c90
008691E5  4C 8B E8                        mov r13, rax
008691E8  0F 10 07                        movups xmm0, xmmword ptr [rdi]
008691EB  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
008691EF  48 8B CF                        mov rcx, rdi
008691F2  E8 F9 2C BE FF                  call 0x14044bef0
008691F7  FF C0                           inc eax
008691F9  48 63 C8                        movsxd rcx, eax
008691FC  48 8B C1                        mov rax, rcx
008691FF  F0 49 0F C1 45 00               lock xadd qword ptr [r13], rax
00869205  48 85 C0                        test rax, rax
00869208  0F 8E 52 01 00 00               jle 0x140869360
0086920E  F0 48 FF 07                     lock inc qword ptr [rdi]
00869212  49 8D 4F 30                     lea rcx, [r15 + 0x30]
00869216  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0086921B  48 83 39 00                     cmp qword ptr [rcx], 0
0086921F  0F 84 78 FD FF FF               je 0x140868f9d
00869225  33 D2                           xor edx, edx
00869227  E8 B4 AD A3 FF                  call 0x1402a3fe0
0086922C  E9 6C FD FF FF                  jmp 0x140868f9d
00869231  4D 85 C0                        test r8, r8
00869234  0F 84 B4 00 00 00               je 0x1408692ee
0086923A  48 8B D7                        mov rdx, rdi
0086923D  49 8B CF                        mov rcx, r15
00869240  E8 F3 F5 FF FF                  call 0x140868838
00869245  E9 79 FF FF FF                  jmp 0x1408691c3
0086924A  48 8B C6                        mov rax, rsi
0086924D  48 25 00 00 00 80               and rax, 0xffffffff80000000
00869253  48 83 FE FD                     cmp rsi, -3
00869257  0F 87 98 FC FF FF               ja 0x140868ef5
0086925D  48 3D 00 00 00 80               cmp rax, -0x80000000
00869263  0F 85 8C FC FF FF               jne 0x140868ef5
00869269  48 33 F0                        xor rsi, rax
0086926C  4C 8B 3D 45 63 6A 00            mov r15, qword ptr [rip + 0x6a6345]
00869273  E9 80 FC FF FF                  jmp 0x140868ef8
00869278  83 FE 0A                        cmp esi, 0xa
0086927B  0F 87 99 00 00 00               ja 0x14086931a
00869281  48 8D 14 76                     lea rdx, [rsi + rsi*2]
00869285  48 C1 E2 04                     shl rdx, 4
00869289  B9 40 00 00 00                  mov ecx, 0x40
0086928E  41 B8 4F 62 57 6D               mov r8d, 0x6d57624f
00869294  E8 57 8E 31 00                  call 0x140b820f0
00869299  48 89 45 08                     mov qword ptr [rbp + 8], rax
0086929D  48 85 C0                        test rax, rax
008692A0  0F 84 73 02 00 00               je 0x140869519
008692A6  C6 45 02 01                     mov byte ptr [rbp + 2], 1
008692AA  E9 E0 FB FF FF                  jmp 0x140868e8f
008692AF  80 7D 02 00                     cmp byte ptr [rbp + 2], 0
008692B3  0F 84 27 03 00 00               je 0x1408695e0
008692B9  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
008692BD  48 85 C0                        test rax, rax
008692C0  0F 85 F9 00 00 00               jne 0x1408693bf
008692C6  33 D2                           xor edx, edx
008692C8  49 8B CF                        mov rcx, r15
008692CB  E8 A0 95 31 00                  call 0x140b82870
008692D0  E9 C1 FE FF FF                  jmp 0x140869196
008692D5  48 3B 3D E4 D9 75 00            cmp rdi, qword ptr [rip + 0x75d9e4]
008692DC  0F 85 67 FD FF FF               jne 0x140869049
008692E2  C7 45 04 08 00 00 C0            mov dword ptr [rbp + 4], 0xc0000008
008692E9  E9 B2 01 00 00                  jmp 0x1408694a0
008692EE  48 8B 5D 40                     mov rbx, qword ptr [rbp + 0x40]
008692F2  48 85 F6                        test rsi, rsi
008692F5  74 1C                           je 0x140869313
008692F7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00869300  44 0F B6 80 32 02 00 00         movzx r8d, byte ptr [rax + 0x232]
00869308  48 8B D6                        mov rdx, rsi
0086930B  49 8B CF                        mov rcx, r15
0086930E  E8 6D 72 BD FF                  call 0x140440580
00869313  33 FF                           xor edi, edi
00869315  E9 87 FC FF FF                  jmp 0x140868fa1
0086931A  8D 4E F5                        lea ecx, [rsi - 0xb]
0086931D  B8 25 49 92 24                  mov eax, 0x24924925
00869322  F7 E1                           mul ecx
00869324  2B CA                           sub ecx, edx
00869326  D1 E9                           shr ecx, 1
00869328  8D 04 0A                        lea eax, [rdx + rcx]
0086932B  C1 E8 03                        shr eax, 3
0086932E  48 C1 E0 07                     shl rax, 7
00869332  48 8D 0D C7 E0 5B 00            lea rcx, [rip + 0x5be0c7]
00869339  48 03 C1                        add rax, rcx
0086933C  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00869340  48 8B C8                        mov rcx, rax
00869343  E8 78 53 B2 FF                  call 0x14038e6c0
00869348  E9 4C FF FF FF                  jmp 0x140869299
0086934D  41 B9 01 00 00 00               mov r9d, 1
00869353  44 3B CB                        cmp r9d, ebx
00869356  72 77                           jb 0x1408693cf
00869358  8B 4D 18                        mov ecx, dword ptr [rbp + 0x18]
0086935B  E9 96 FD FF FF                  jmp 0x1408690f6
00869360  48 03 C1                        add rax, rcx
00869363  4D 8D 45 30                     lea r8, [r13 + 0x30]
00869367  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0086936C  33 D2                           xor edx, edx
0086936E  8D 4A 18                        lea ecx, [rdx + 0x18]
00869371  44 8D 4A 10                     lea r9d, [rdx + 0x10]
00869375  E8 E6 42 C9 FF                  call 0x1404fd660
0086937A  CC                              int3
0086937B  45 84 E4                        test r12b, r12b
0086937E  74 20                           je 0x1408693a0
00869380  48 8D 8E E8 01 00 00            lea rcx, [rsi + 0x1e8]
00869387  0F 0D 09                        prefetchw byte ptr [rcx]
0086938A  48 8B 01                        mov rax, qword ptr [rcx]
0086938D  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00869391  48 8D 50 FE                     lea rdx, [rax - 2]
00869395  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0086939A  0F 85 4E 02 00 00               jne 0x1408695ee
008693A0  48 8B CF                        mov rcx, rdi
008693A3  E8 68 5C 9F FF                  call 0x14025f010
008693A8  E9 E0 FD FF FF                  jmp 0x14086918d
008693AD  F6 C3 02                        test bl, 2
008693B0  75 51                           jne 0x140869403
008693B2  48 8D 04 33                     lea rax, [rbx + rsi]
008693B6  48 8B 58 FF                     mov rbx, qword ptr [rax - 1]
008693BA  E9 BF FC FF FF                  jmp 0x14086907e
008693BF  49 8B D7                        mov rdx, r15
008693C2  48 8B C8                        mov rcx, rax
008693C5  E8 06 46 B2 FF                  call 0x14038d9d0
008693CA  E9 C7 FD FF FF                  jmp 0x140869196
008693CF  41 8B D1                        mov edx, r9d
008693D2  41 8B C1                        mov eax, r9d
008693D5  48 8B 8C C5 80 00 00 00         mov rcx, qword ptr [rbp + rax*8 + 0x80]
008693DD  44 8D 42 FF                     lea r8d, [rdx - 1]
008693E1  4A 8B 9C C5 80 00 00 00         mov rbx, qword ptr [rbp + r8*8 + 0x80]
008693E9  48 3B CB                        cmp rcx, rbx
008693EC  76 49                           jbe 0x140869437
008693EE  8B C2                           mov eax, edx
008693F0  48 89 8C C5 80 00 00 00         mov qword ptr [rbp + rax*8 + 0x80], rcx
008693F8  41 FF C1                        inc r9d
008693FB  8B 5D 38                        mov ebx, dword ptr [rbp + 0x38]
008693FE  E9 50 FF FF FF                  jmp 0x140869353
00869403  8B 97 B0 00 00 00               mov edx, dword ptr [rdi + 0xb0]
00869409  0F B7 87 B4 00 00 00            movzx eax, word ptr [rdi + 0xb4]
00869410  8B 0C 30                        mov ecx, dword ptr [rax + rsi]
00869413  23 CA                           and ecx, edx
00869415  3B CA                           cmp ecx, edx
00869417  0F 84 6F 01 00 00               je 0x14086958c
0086941D  48 83 C3 FD                     add rbx, -3
00869421  E9 55 FC FF FF                  jmp 0x14086907b
00869426  48 8D 8E E8 01 00 00            lea rcx, [rsi + 0x1e8]
0086942D  E8 7E 0A AE FF                  call 0x140349eb0
00869432  E9 A1 FC FF FF                  jmp 0x1408690d8
00869437  0F 84 27 01 00 00               je 0x140869564
0086943D  8B C2                           mov eax, edx
0086943F  48 89 9C C5 80 00 00 00         mov qword ptr [rbp + rax*8 + 0x80], rbx
00869447  41 8B D0                        mov edx, r8d
0086944A  45 85 C0                        test r8d, r8d
0086944D  74 9F                           je 0x1408693ee
0086944F  EB 8C                           jmp 0x1408693dd
00869451  48 8B CB                        mov rcx, rbx
00869454  E8 17 A7 02 00                  call 0x140893b70
00869459  48 8B C8                        mov rcx, rax
0086945C  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
00869460  48 85 C0                        test rax, rax
00869463  0F 85 F2 00 00 00               jne 0x14086955b
00869469  48 8B 5D 58                     mov rbx, qword ptr [rbp + 0x58]
0086946D  3B CE                           cmp ecx, esi
0086946F  0F 83 83 01 00 00               jae 0x1408695f8
00869475  48 8B 14 CB                     mov rdx, qword ptr [rbx + rcx*8]
00869479  45 84 FF                        test r15b, r15b
0086947C  0F 84 1A 01 00 00               je 0x14086959c
00869482  C7 45 04 0A 01 00 C0            mov dword ptr [rbp + 4], 0xc000010a
00869489  41 B5 01                        mov r13b, 1
0086948C  48 8B 75 10                     mov rsi, qword ptr [rbp + 0x10]
00869490  4C 8B 7D 08                     mov r15, qword ptr [rbp + 8]
00869494  E9 C1 FC FF FF                  jmp 0x14086915a
00869499  C7 45 04 06 A0 00 C0            mov dword ptr [rbp + 4], 0xc000a006
008694A0  48 8B 7D 20                     mov rdi, qword ptr [rbp + 0x20]
008694A4  44 0F B6 65 00                  movzx r12d, byte ptr [rbp]
008694A9  41 B5 01                        mov r13b, 1
008694AC  48 8B 75 10                     mov rsi, qword ptr [rbp + 0x10]
008694B0  4C 8B 7D 08                     mov r15, qword ptr [rbp + 8]
008694B4  E9 A1 FC FF FF                  jmp 0x14086915a
008694B9  48 8D 41 FF                     lea rax, [rcx - 1]
008694BD  0F B7 C8                        movzx ecx, ax
008694C0  48 03 C9                        add rcx, rcx
008694C3  49 81 E0 01 00 FE FF            and r8, 0xfffffffffffe0001
008694CA  49 0B C8                        or rcx, r8
008694CD  48 89 4D 28                     mov qword ptr [rbp + 0x28], rcx
008694D1  48 8D 4D 28                     lea rcx, [rbp + 0x28]
008694D5  E8 B6 77 BC FF                  call 0x140430c90
008694DA  4C 8B E8                        mov r13, rax
008694DD  B8 F0 7F 00 00                  mov eax, 0x7ff0
008694E2  F0 49 0F C1 45 00               lock xadd qword ptr [r13], rax
008694E8  48 85 C0                        test rax, rax
008694EB  0F 8E D1 00 00 00               jle 0x1408695c2
008694F1  41 B8 F0 7F 00 00               mov r8d, 0x7ff0
008694F7  48 8D 55 28                     lea rdx, [rbp + 0x28]
008694FB  48 8B CF                        mov rcx, rdi
008694FE  E8 0D 4D C1 FF                  call 0x14047e210
00869503  85 C0                           test eax, eax
00869505  0F 84 92 FA FF FF               je 0x140868f9d
0086950B  F7 D8                           neg eax
0086950D  48 98                           cdqe
0086950F  F0 49 01 45 00                  lock add qword ptr [r13], rax
00869514  E9 84 FA FF FF                  jmp 0x140868f9d
00869519  33 C9                           xor ecx, ecx
0086951B  E8 40 72 BE FF                  call 0x140450760
00869520  88 45 03                        mov byte ptr [rbp + 3], al
00869523  48 8D 04 76                     lea rax, [rsi + rsi*2]
00869527  48 C1 E0 04                     shl rax, 4
0086952B  48 8D 48 0F                     lea rcx, [rax + 0xf]
0086952F  48 3B C8                        cmp rcx, rax
00869532  77 0A                           ja 0x14086953e
00869534  48 B9 F0 FF FF FF FF FF FF 0F   movabs rcx, 0xffffffffffffff0
0086953E  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00869542  48 8B C1                        mov rax, rcx
00869545  E8 16 14 E5 FF                  call 0x1406ba960
0086954A  48 2B E1                        sub rsp, rcx
0086954D  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00869552  48 89 45 08                     mov qword ptr [rbp + 8], rax
00869556  E9 34 F9 FF FF                  jmp 0x140868e8f
0086955B  C6 45 00 01                     mov byte ptr [rbp], 1
0086955F  E9 71 F9 FF FF                  jmp 0x140868ed5
00869564  C7 45 04 30 00 00 C0            mov dword ptr [rbp + 4], 0xc0000030
0086956B  4C 8B 7D 08                     mov r15, qword ptr [rbp + 8]
0086956F  E9 E6 FB FF FF                  jmp 0x14086915a
00869574  C7 45 04 22 00 00 C0            mov dword ptr [rbp + 4], 0xc0000022
0086957B  E9 20 FF FF FF                  jmp 0x1408694a0
00869580  C7 45 04 24 00 00 C0            mov dword ptr [rbp + 4], 0xc0000024
00869587  E9 14 FF FF FF                  jmp 0x1408694a0
0086958C  0F B7 87 B6 00 00 00            movzx eax, word ptr [rdi + 0xb6]
00869593  48 8B 1C 30                     mov rbx, qword ptr [rax + rsi]
00869597  E9 E2 FA FF FF                  jmp 0x14086907e
0086959C  48 8B C2                        mov rax, rdx
0086959F  48 25 00 00 00 80               and rax, 0xffffffff80000000
008695A5  48 3D 00 00 00 80               cmp rax, -0x80000000
008695AB  0F 85 D1 FE FF FF               jne 0x140869482
008695B1  48 83 FA FD                     cmp rdx, -3
008695B5  0F 87 C7 FE FF FF               ja 0x140869482
008695BB  FF C1                           inc ecx
008695BD  E9 AB FE FF FF                  jmp 0x14086946d
008695C2  48 05 F0 7F 00 00               add rax, 0x7ff0
008695C8  4D 8D 45 30                     lea r8, [r13 + 0x30]
008695CC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008695D1  33 D2                           xor edx, edx
008695D3  8D 4A 18                        lea ecx, [rdx + 0x18]
008695D6  44 8D 4A 10                     lea r9d, [rdx + 0x10]
008695DA  E8 81 40 C9 FF                  call 0x1404fd660
008695DF  CC                              int3
008695E0  0F B6 4D 03                     movzx ecx, byte ptr [rbp + 3]
008695E4  E8 77 71 BE FF                  call 0x140450760
008695E9  E9 A8 FB FF FF                  jmp 0x140869196
008695EE  E8 BD 08 AE FF                  call 0x140349eb0
008695F3  E9 A8 FD FF FF                  jmp 0x1408693a0
008695F8  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
008695FC  E9 D4 F8 FF FF                  jmp 0x140868ed5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObWaitForMultipleObjects(int a1, __int64 a2, unsigned __int8 a3, int a4, unsigned __int8 a5, unsigned __int8 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m448;
    unsigned __int64 v_stack_m458;
    unsigned int v_stack_m460;
    unsigned __int64 v_stack_m468;
    unsigned __int64 v_stack_m470;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m480;
    unsigned __int64 v_stack_m488;
    unsigned int v_stack_m48C;
    unsigned int v_stack_m490;
    unsigned __int64 v_stack_m498;
    unsigned __int64 v_stack_m4A0;
    unsigned __int64 v_stack_m4A8;
    unsigned int v_stack_m4B0;
    unsigned __int64 v_stack_m4B8;
    unsigned __int64 v_stack_m4C0;
    unsigned int v_stack_m4C4;
    unsigned __int8 v_stack_m4C5;
    unsigned __int8 v_stack_m4C6;
    unsigned __int8 v_stack_m4C7;
    unsigned __int64 v_stack_m4C8;
    unsigned __int64 v_stack_m4D0;
    unsigned __int64 v_stack_m4D8;
    unsigned __int8 v_stack_m4E0;
    unsigned __int8 v_stack_m4E8;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p40;

    v_rsp = (v_rsp) - (0x4D0ULL);
    v_stack_p18 = v_rbx;
    result = (*(unsigned __int64 *)(v_rip + 5904682)) ^ (v_stack_m4C8);
    v_stack_m48 = result;
    v_stack_m4B0 = a4;
    v_stack_m4C7 = a3;
    v_stack_m470 = a2;
    v_stack_m490 = (unsigned int)((unsigned int)(a1));
    v_stack_m458 = a7;
    v_stack_m4A0 = v_xmm0;
    a2 = 0;
    result = memset(v_stack_m248, a2, 512, a4);
    v_r13 = 0;
    a2 = 0;
    result = memset(v_stack_m448, a2, 512, a4);
    v_stack_m4C5 = 0;
    v_stack_m4C6 = 0;
    result = 0;
    v_stack_m4C0 = 0;
    v_rdi = 0;
    v_stack_m478 = 0;
    if (((unsigned int)((unsigned int)(a1))) > 3) goto loc_00869278;
loc_00868E8F:
    v_r14 = 0;
    v_r12 = 0;
    v_stack_m4C8 = 0;
    v_stack_m4A8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m4B8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m468 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544))) goto loc_00869451;
    v_stack_m480 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 768);
loc_00868ED5:
    v_r12 = 0;
loc_00868ED8:
    v_stack_m488 = v_r12 * 8;
    if (a3 == 0) goto loc_0086924A;
loc_00868EF5:
loc_00868EF8:
    if ((((unsigned int)(*(unsigned __int64 *)(v_r12 * 8 + v_stack_m470 * 1))) & (0x3FCULL)) == 0) goto loc_008692F2;
    result = ExpLookupHandleTableEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 768), *(unsigned __int64 *)(v_r12 * 8 + v_stack_m470 * 1), 512, a4);
    if (result == 0) goto loc_008692F2;
loc_00868F21:
    v_stack_m4A0 = *(unsigned __int64 *)(result);
    v_stack_m498 = *(unsigned __int64 *)(result + 8);
loc_00868F31:
    if (((v_stack_m4A0) & (0x1FFFEULL)) == 0) goto loc_008691C3;
    result = (unsigned __int8)(~((unsigned __int8)(v_stack_m4A0)));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00868F5C;
    result = ExpBlockOnLockedHandleEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 768), result, v_stack_m4A0, a4);
    goto loc_00868F21;
loc_00868F5C:
    v_stack_m4A0 = v_stack_m4A0;
    v_stack_m498 = v_stack_m498;
    result = ((((unsigned __int8)(result)) & (1)) == 0) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) goto loc_00868F31;
    a1 = (v_stack_m4A0) >> (1);
    if (((unsigned __int16)(a1)) == 16) goto loc_008694B9;
    result = ExGetHandlePointer(v_stack_m4A0, v_stack_m498, v_stack_m4A0, a4);
loc_00868F9D:
loc_00868FA1:
    if (result == 0) goto loc_008692E2;
    result = (unsigned int)(((unsigned int)(v_stack_m498)) & (0x1FFFFFFULL));
    v_r14 = (unsigned int)((v_r14) + 1);
    v_stack_m48C = (unsigned int)(v_r14);
    *(unsigned __int64 *)(v_stack_m4C8 + v_stack_m488 * 1 + 640) = result + 48;
    if (((unsigned __int8)(v_stack_m4C7)) != 1) goto loc_00869014;
    result = (unsigned int)(~(result));
    if (((unsigned __int8)(v_stack_m4C7)) < 1) goto loc_00869574;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 26))) & (64)) == 0) goto loc_00869014;
    result = (unsigned int)((*(unsigned __int8 *)(result + 26)) & (127));
    a1 = (result) - (*(unsigned __int8 *)(result + v_rip - 8818671 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == 0) goto loc_00869014;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16)) == 1) goto loc_00869499;
loc_00869014:
    result = (result) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(result + 24));
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7724575));
    if (v_stack_m4B0 != 1) goto loc_008692D5;
loc_00869049:
    if ((*(unsigned __int64 *)(v_rip - 8818743 + a1 * 8 + 16545792)) == (*(unsigned __int64 *)(v_rip + 6885592))) goto loc_00869580;
    result = ObpTraceObjectReferenceIfActive(result, 1, (unsigned int)(0x7457624FULL), a4);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8818743 + a1 * 8 + 16545792) + 32))) & (1)) != 0) goto loc_008693AD;
    v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8818743 + a1 * 8 + 16545792) + 32);
    if (!(sign_flag)) {
        v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8818743 + a1 * 8 + 16545792) + 32)) + (result + 48);
    }
    *(unsigned __int64 *)(v_stack_m4C8 + v_stack_m488 * 1 + 128) = v_rbx;
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((unsigned int)(v_r12)) >= ((unsigned int)((unsigned int)(v_stack_m490)))) goto loc_0086909E;
    goto loc_00868ED8;
loc_0086909E:
    if ((unsigned __int8)(v_stack_m4C8) == 0) goto loc_008690D8;
    v_r12 = 0;
    v_stack_m4C8 = 0;
    result = (*(unsigned __int64 *)(v_stack_m4B8 + 488)) & (-2);
    if (condition_is_not_equal) goto loc_00869426;
loc_008690D8:
    result = KiLeaveCriticalRegionUnsafe(v_stack_m4A8, 1, (unsigned int)(0x7457624FULL), a4);
    v_r13 = 0;
    v_stack_m4C7 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m4B0)) == 0) goto loc_0086934D;
loc_008690F6:
    v_stack_m4D0 = v_stack_m4C0;
    v_stack_m4D8 = v_stack_m458;
    v_stack_m4E0 = a6;
    v_stack_m4E8 = a5;
    result = KeWaitForMultipleObjects((unsigned int)((unsigned int)((unsigned int)(v_stack_m490))), v_stack_m448, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4B0))), 6);
    v_stack_m4C4 = (unsigned int)(result);
    goto loc_0086915A;
loc_0086915A:
    if ((unsigned int)(v_r14) == 0) goto loc_00869184;
loc_0086916D:
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_stack_m248 + (unsigned int)((unsigned int)(v_r14)) * 8 - 8), (unsigned int)(0x7457624FULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_m4B0))), 6);
    v_r14 = (unsigned int)((v_r14) + (-1));
    if (condition_is_not_equal) goto loc_0086916D;
loc_00869184:
    if (0 != 0) goto loc_0086937B;
loc_0086918D:
    if (v_stack_m4C0 != 0) goto loc_008692AF;
loc_00869196:
    a1 = (v_stack_m48) ^ (v_stack_m4C8);
    result = _security_check_cookie(a1, (unsigned int)(0x7457624FULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_m4B0))), 6);
    return result;
loc_008691C3:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m4A8))) & (1)) == 0) goto loc_00869231;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m4A8))) & (1)) != 0) goto loc_008691C3;
    result = ExGetHandlePointer(v_stack_m4A8, (unsigned int)(0x7457624FULL), *(unsigned __int64 *)(v_stack_m4A8), 6);
    v_stack_m4A0 = v_xmm0;
    result = ExSlowReplenishHandleTableEntry(v_stack_m4A8, (unsigned int)(0x7457624FULL), *(unsigned __int64 *)(v_stack_m4A8), 6);
    result = (unsigned int)((result) + 1);
    if (condition_is_less_or_equal) goto loc_00869360;
    if ((*(unsigned __int64 *)(v_stack_m4C0 + 48)) == 0) goto loc_00868F9D;
    a2 = 0;
    result = ExfUnblockPushLock(v_stack_m4C0 + 48, a2, *(unsigned __int64 *)(v_stack_m4A8), 6);
    goto loc_00868F9D;
loc_00869231:
    if (*(unsigned __int64 *)(v_stack_m4A8) == 0) goto loc_008692EE;
    result = ExpBlockOnLockedHandleEntry(v_stack_m4C0, v_stack_m4A8, *(unsigned __int64 *)(v_stack_m4A8), 6);
    goto loc_008691C3;
loc_0086924A:
    result = (v_stack_m4B8) & (0xFFFFFFFF80000000ULL);
    if (v_stack_m4B8 > -3) goto loc_00868EF5;
    if (result != 0xFFFFFFFF80000000ULL) goto loc_00868EF5;
    v_rsi = (v_stack_m4B8) ^ (result);
    goto loc_00868EF8;
loc_00869278:
    if (((unsigned int)(v_rsi)) > 10) goto loc_0086931A;
    a2 = (v_rsi + v_rsi * 2) << (4);
    result = ExAllocatePool2(64, a2, (unsigned int)(0x6D57624FULL), 6);
loc_00869299:
    v_stack_m4C0 = result;
    if (result == 0) goto loc_00869519;
    v_stack_m4C6 = 1;
    goto loc_00868E8F;
loc_008692AF:
    if (v_stack_m4C6 == 0) goto loc_008695E0;
    if (v_stack_m478 != 0) goto loc_008693BF;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip + 6972229), a2, (unsigned int)(0x6D57624FULL), 6);
    goto loc_00869196;
loc_008692D5:
    if (v_stack_m4A8 != (*(unsigned __int64 *)(v_rip + 7723492))) goto loc_00869049;
loc_008692E2:
    v_stack_m4C4 = 0xC0000008ULL;
    goto loc_008694A0;
loc_008692EE:
loc_008692F2:
    if (v_rsi != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a3 = *(unsigned __int8 *)(result + 562);
        a2 = v_rsi;
        a1 = *(unsigned __int64 *)(v_rip + 6972229);
        result = ExHandleLogBadReference(a1, a2, a3, 6);
    }
    v_rdi = 0;
    goto loc_00868FA1;
loc_0086931A:
    a1 = (unsigned int)((v_rsi - 11) - ((unsigned int)(a2)));
    a1 = (unsigned int)((a1) >> (1));
    result = (unsigned int)((a2 + a1 * 1) >> (3));
    result = (result) << (7);
    result = (result) + (v_rip + 6021319);
    v_stack_m478 = result;
    result = ExAllocateFromNPagedLookasideList(result, a2, a3, 6);
    goto loc_00869299;
loc_0086934D:
loc_00869353:
    if (1 < ((unsigned int)(v_stack_m488))) goto loc_008693CF;
    goto loc_008690F6;
loc_00869360:
    result = (result) + ((unsigned int)(v_stack_m4B0));
    v_stack_p20 = result;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, result + 48, a2 + 16);
loc_0086937B:
    if (0 == 0) goto loc_008693A0;
    result = (*(unsigned __int64 *)(v_rsi + 488)) & (-2);
    if (condition_is_not_equal) goto loc_008695EE;
loc_008693A0:
    result = KiLeaveCriticalRegionUnsafe(0, result - 2, result + 48, a2 + 16);
    goto loc_0086918D;
loc_008693AD:
    if ((((unsigned __int8)(v_stack_m488)) & (2)) != 0) goto loc_00869403;
    goto loc_0086907E;
loc_008693BF:
    result = ExFreeToNPagedLookasideList(v_stack_m488 + v_rsi * 1, *(unsigned __int64 *)(v_rip + 6972229), result + 48, a2 + 16);
    goto loc_00869196;
loc_008693CF:
loc_008693DD:
    if ((*(unsigned __int64 *)(v_stack_m4C8 + (unsigned int)((unsigned int)(a2 + 16)) * 8 + 128)) <= (*(unsigned __int64 *)(v_stack_m4C8 + (unsigned int)((unsigned int)(a2 + 16)) - 1 * 8 + 128))) goto loc_00869437;
loc_008693EE:
    *(unsigned __int64 *)(v_stack_m4C8 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2 + 16)))) * 8 + 128) = *(unsigned __int64 *)(v_stack_m4C8 + (unsigned int)((unsigned int)(a2 + 16)) * 8 + 128);
    a4 = (unsigned int)((a2 + 16) + 1);
    goto loc_00869353;
loc_00869403:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int16 *)(v_rdi + 180) + v_rsi * 1))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 176)))));
    if (a1 == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 176))))) goto loc_0086958C;
    v_rbx = ((unsigned int)(v_stack_m490)) + (-3);
    goto loc_0086907B;
loc_00869426:
    result = ExfReleaseRundownProtection(v_rsi + 488, (unsigned int)(*(unsigned int *)(v_rdi + 176)), (unsigned int)((unsigned int)(a2 + 16)) - 1, a4);
    goto loc_008690D8;
loc_00869437:
    if (condition_is_equal) goto loc_00869564;
    *(unsigned __int64 *)(v_stack_m4C8 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 176)))) * 8 + 128) = v_rbx;
    if ((unsigned int)((unsigned int)((unsigned int)(a2 + 16)) - 1) == 0) goto loc_008693EE;
    goto loc_008693DD;
loc_00869451:
    result = ObReferenceProcessHandleTable(v_rbx, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2 + 16)) - 1)), (unsigned int)((unsigned int)(a2 + 16)) - 1, a4);
    v_stack_m480 = result;
    if (result != 0) goto loc_0086955B;
loc_0086946D:
    if (((unsigned int)(result)) >= ((unsigned int)(v_rsi))) goto loc_008695F8;
    if ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6972229)) == 0) goto loc_0086959C;
loc_00869482:
    v_stack_m4C4 = 0xC000010AULL;
    goto loc_0086915A;
loc_00869499:
    v_stack_m4C4 = 0xC000A006ULL;
loc_008694A0:
    goto loc_0086915A;
loc_008694B9:
    a1 = ((unsigned __int16)(result - 1)) + ((unsigned __int16)(result - 1));
    a3 = ((unsigned int)((unsigned int)(a2 + 16)) - 1) & (0xFFFFFFFFFFFE0001ULL);
    a1 = (a1) | (a3);
    v_stack_m4A0 = a1;
    result = ExGetHandlePointer(v_stack_m4A0, *(unsigned __int64 *)(v_stack_m470 + result * 8), a3, a4);
    if (condition_is_less_or_equal) goto loc_008695C2;
    result = ExFastReplenishHandleTableEntry(v_stack_m4A8, v_stack_m4A0, (unsigned int)(0x7FF0ULL), a4);
    if ((unsigned int)(result) == 0) goto loc_00868F9D;
    result = (unsigned int)(-(result));
    goto loc_00868F9D;
loc_00869519:
    a1 = 0;
    result = KeSetKernelStackSwapEnable(a1, v_stack_m4A0, (unsigned int)(0x7FF0ULL), a4);
    v_stack_m4C5 = (unsigned __int8)(result);
    result = (v_stack_m4B8 + v_stack_m4B8 * 2) << (4);
    if ((result + 15) <= result) {
    }
    a1 = (result + 15) & (-16);
    result = _chkstk(a1, v_stack_m4A0, (unsigned int)(0x7FF0ULL), a4);
    v_rsp = (v_stack_m38) - (a1);
    v_stack_m4C0 = v_stack_p40;
    goto loc_00868E8F;
loc_0086955B:
    v_stack_m4C8 = 1;
    goto loc_00868ED5;
loc_00869564:
    v_stack_m4C4 = 0xC0000030ULL;
    goto loc_0086915A;
loc_00869574:
    v_stack_m4C4 = 0xC0000022ULL;
    goto loc_008694A0;
loc_00869580:
    v_stack_m4C4 = 0xC0000024ULL;
    goto loc_008694A0;
loc_0086958C:
    goto loc_0086907E;
loc_0086959C:
    result = (v_stack_m4A0) & (0xFFFFFFFF80000000ULL);
    if (result != 0xFFFFFFFF80000000ULL) goto loc_00869482;
    if (v_stack_m4A0 > -3) goto loc_00869482;
    a1 = (unsigned int)((a1) + 1);
    goto loc_0086946D;
loc_008695C2:
    result = (result) + (0x7FF0ULL);
    v_stack_p20 = result;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, result + 48, a2 + 16);
loc_008695E0:
    result = KeSetKernelStackSwapEnable(v_stack_m4C5, a2, result + 48, a2 + 16);
    goto loc_00869196;
loc_008695EE:
    result = ExfReleaseRundownProtection(v_stack_m4C5, a2, result + 48, a2 + 16);
    goto loc_008693A0;
loc_008695F8:
    goto loc_00868ED5;
}
```

## 5. (Beta) C Style

```c
int64_t ObWaitForMultipleObjects(int32_t Arg1, int64_t Arg2, uint8_t Arg3, int32_t Arg4, uint8_t Arg5, uint8_t Arg6, int64_t Arg7)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m248;
    uint64_t v_stack_m38;
    uint64_t v_stack_m448;
    uint64_t v_stack_m458;
    uint32_t v_stack_m460;
    uint64_t v_stack_m468;
    uint64_t v_stack_m470;
    uint64_t v_stack_m478;
    uint64_t v_stack_m48;
    uint64_t v_stack_m480;
    uint64_t v_stack_m488;
    uint32_t v_stack_m48C;
    uint32_t v_stack_m490;
    uint64_t v_stack_m498;
    uint64_t v_stack_m4A0;
    uint64_t v_stack_m4A8;
    uint32_t v_stack_m4B0;
    uint64_t v_stack_m4B8;
    uint64_t v_stack_m4C0;
    uint32_t v_stack_m4C4;
    uint8_t v_stack_m4C5;
    uint8_t v_stack_m4C6;
    uint8_t v_stack_m4C7;
    uint64_t v_stack_m4C8;
    uint64_t v_stack_m4D0;
    uint64_t v_stack_m4D8;
    uint8_t v_stack_m4E0;
    uint8_t v_stack_m4E8;
    uint32_t v_stack_p0;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p40;

    local_rsp = (local_rsp) - (0x4D0ULL);
    v_stack_p18 = local_rbx;
    result = (*(uint64_t *)(v_rip + 0x5A192A)) ^ (v_stack_m4C8);
    v_stack_m48 = result;
    v_stack_m4B0 = Arg4;
    v_stack_m4C7 = Arg3;
    v_stack_m470 = Arg2;
    v_stack_m490 = (uint32_t)((uint32_t)(Arg1));
    v_stack_m458 = Arg7;
    v_stack_m4A0 = v_xmm0;
    Arg2 = 0;
    result = memset(v_stack_m248, Arg2, 512, Arg4);
    local_r13 = 0;
    Arg2 = 0;
    result = memset(v_stack_m448, Arg2, 512, Arg4);
    v_stack_m4C5 = 0;
    v_stack_m4C6 = 0;
    result = 0;
    v_stack_m4C0 = 0;
    local_rdi = 0;
    v_stack_m478 = 0;
    if (((uint32_t)((uint32_t)(Arg1))) > 3) goto loc_00869278;
loc_00868E8F:
    local_r14 = 0;
    local_r12 = 0;
    v_stack_m4C8 = 0;
    v_stack_m4A8 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m4B8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m468 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220))) goto loc_00869451;
    v_stack_m480 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x300);
loc_00868ED5:
    local_r12 = 0;
loc_00868ED8:
    v_stack_m488 = local_r12 * 8;
    if (Arg3 == 0) goto loc_0086924A;
loc_00868EF5:
loc_00868EF8:
    if ((((uint32_t)(*(uint64_t *)(local_r12 * 8 + v_stack_m470 * 1))) & (0x3FCULL)) == 0) goto loc_008692F2;
    result = ExpLookupHandleTableEntry(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x300), *(uint64_t *)(local_r12 * 8 + v_stack_m470 * 1), 512, Arg4);
    if (result == 0) goto loc_008692F2;
loc_00868F21:
    v_stack_m4A0 = *(uint64_t *)(result);
    v_stack_m498 = *(uint64_t *)(result + 0x8);
loc_00868F31:
    if (((v_stack_m4A0) & (0x1FFFEULL)) == 0) goto loc_008691C3;
    result = (uint8_t)(~((uint8_t)(v_stack_m4A0)));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00868F5C;
    result = ExpBlockOnLockedHandleEntry(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x300), result, v_stack_m4A0, Arg4);
    goto loc_00868F21;
loc_00868F5C:
    v_stack_m4A0 = v_stack_m4A0;
    v_stack_m498 = v_stack_m498;
    result = ((((uint8_t)(result)) & (1)) == 0) ? 1 : 0;
    if ((uint8_t)(result) == 0) goto loc_00868F31;
    Arg1 = (v_stack_m4A0) >> (1);
    if (((uint16_t)(Arg1)) == 16) goto loc_008694B9;
    result = ExGetHandlePointer(v_stack_m4A0, v_stack_m498, v_stack_m4A0, Arg4);
loc_00868F9D:
loc_00868FA1:
    if (result == 0) goto loc_008692E2;
    result = (uint32_t)(((uint32_t)(v_stack_m498)) & (0x1FFFFFFULL));
    local_r14 = (uint32_t)((local_r14) + 1);
    v_stack_m48C = (uint32_t)(local_r14);
    *(uint64_t *)(v_stack_m4C8 + v_stack_m488 * 1 + 0x280) = result + 48;
    if (((uint8_t)(v_stack_m4C7)) != 1) goto loc_00869014;
    result = (uint32_t)(~(result));
    if (((uint8_t)(v_stack_m4C7)) < 1) goto loc_00869574;
    if ((((uint8_t)(*(uint8_t *)(result + 0x1A))) & (64)) == 0) goto loc_00869014;
    result = (uint32_t)((*(uint8_t *)(result + 0x1A)) & (127));
    Arg1 = (result) - (*(uint8_t *)(result + v_rip - 0x868FEF * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(Arg1) + 0x18)) == 0) goto loc_00869014;
    if ((*(uint64_t *)(*(uint64_t *)(Arg1) + 0x10)) == 1) goto loc_00869499;
loc_00869014:
    result = (result) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(result + 0x18));
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x75DE1F));
    if (v_stack_m4B0 != 1) goto loc_008692D5;
loc_00869049:
    if ((*(uint64_t *)(v_rip - 0x869037 + Arg1 * 8 + 0xFC7800)) == (*(uint64_t *)(v_rip + 0x6910D8))) goto loc_00869580;
    result = ObpTraceObjectReferenceIfActive(result, 1, (uint32_t)(0x7457624FULL), Arg4);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x869037 + Arg1 * 8 + 0xFC7800) + 0x20))) & (1)) != 0) goto loc_008693AD;
    local_rbx = *(uint64_t *)(*(uint64_t *)(v_rip - 0x869037 + Arg1 * 8 + 0xFC7800) + 0x20);
    if (!(sign_flag)) {
        local_rbx = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x869037 + Arg1 * 8 + 0xFC7800) + 0x20)) + (result + 48);
    }
    *(uint64_t *)(v_stack_m4C8 + v_stack_m488 * 1 + 0x80) = local_rbx;
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((uint32_t)(local_r12)) >= ((uint32_t)((uint32_t)(v_stack_m490)))) goto loc_0086909E;
    goto loc_00868ED8;
loc_0086909E:
    if ((uint8_t)(v_stack_m4C8) == 0) goto loc_008690D8;
    local_r12 = 0;
    v_stack_m4C8 = 0;
    result = (*(uint64_t *)(v_stack_m4B8 + 0x1E8)) & (-2);
    if (condition_is_not_equal) goto loc_00869426;
loc_008690D8:
    result = KiLeaveCriticalRegionUnsafe(v_stack_m4A8, 1, (uint32_t)(0x7457624FULL), Arg4);
    local_r13 = 0;
    v_stack_m4C7 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m4B0)) == 0) goto loc_0086934D;
loc_008690F6:
    v_stack_m4D0 = v_stack_m4C0;
    v_stack_m4D8 = v_stack_m458;
    v_stack_m4E0 = Arg6;
    v_stack_m4E8 = Arg5;
    result = KeWaitForMultipleObjects((uint32_t)((uint32_t)((uint32_t)(v_stack_m490))), v_stack_m448, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4B0))), 6);
    v_stack_m4C4 = (uint32_t)(result);
    goto loc_0086915A;
loc_0086915A:
    if ((uint32_t)(local_r14) == 0) goto loc_00869184;
loc_0086916D:
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_stack_m248 + (uint32_t)((uint32_t)(local_r14)) * 8 - 0x8), (uint32_t)(0x7457624FULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_m4B0))), 6);
    local_r14 = (uint32_t)((local_r14) + (-1));
    if (condition_is_not_equal) goto loc_0086916D;
loc_00869184:
    if (0 != 0) goto loc_0086937B;
loc_0086918D:
    if (v_stack_m4C0 != 0) goto loc_008692AF;
loc_00869196:
    Arg1 = (v_stack_m48) ^ (v_stack_m4C8);
    result = _security_check_cookie(Arg1, (uint32_t)(0x7457624FULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_m4B0))), 6);
    return result;
loc_008691C3:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m4A8))) & (1)) == 0) goto loc_00869231;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m4A8))) & (1)) != 0) goto loc_008691C3;
    result = ExGetHandlePointer(v_stack_m4A8, (uint32_t)(0x7457624FULL), *(uint64_t *)(v_stack_m4A8), 6);
    v_stack_m4A0 = v_xmm0;
    result = ExSlowReplenishHandleTableEntry(v_stack_m4A8, (uint32_t)(0x7457624FULL), *(uint64_t *)(v_stack_m4A8), 6);
    result = (uint32_t)((result) + 1);
    if (condition_is_less_or_equal) goto loc_00869360;
    if ((*(uint64_t *)(v_stack_m4C0 + 0x30)) == 0) goto loc_00868F9D;
    Arg2 = 0;
    result = ExfUnblockPushLock(v_stack_m4C0 + 48, Arg2, *(uint64_t *)(v_stack_m4A8), 6);
    goto loc_00868F9D;
loc_00869231:
    if (*(uint64_t *)(v_stack_m4A8) == 0) goto loc_008692EE;
    result = ExpBlockOnLockedHandleEntry(v_stack_m4C0, v_stack_m4A8, *(uint64_t *)(v_stack_m4A8), 6);
    goto loc_008691C3;
loc_0086924A:
    result = (v_stack_m4B8) & (0xFFFFFFFF80000000ULL);
    if (v_stack_m4B8 > -3) goto loc_00868EF5;
    if (result != 0xFFFFFFFF80000000ULL) goto loc_00868EF5;
    local_rsi = (v_stack_m4B8) ^ (result);
    goto loc_00868EF8;
loc_00869278:
    if (((uint32_t)(local_rsi)) > 10) goto loc_0086931A;
    Arg2 = (local_rsi + local_rsi * 2) << (4);
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x6D57624FULL), 6);
loc_00869299:
    v_stack_m4C0 = result;
    if (result == 0) goto loc_00869519;
    v_stack_m4C6 = 1;
    goto loc_00868E8F;
loc_008692AF:
    if (v_stack_m4C6 == 0) goto loc_008695E0;
    if (v_stack_m478 != 0) goto loc_008693BF;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_rip + 0x6A6345), Arg2, (uint32_t)(0x6D57624FULL), 6);
    goto loc_00869196;
loc_008692D5:
    if (v_stack_m4A8 != (*(uint64_t *)(v_rip + 0x75D9E4))) goto loc_00869049;
loc_008692E2:
    v_stack_m4C4 = 0xC0000008ULL;
    goto loc_008694A0;
loc_008692EE:
loc_008692F2:
    if (local_rsi != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg3 = *(uint8_t *)(result + 0x232);
        Arg2 = local_rsi;
        Arg1 = *(uint64_t *)(v_rip + 0x6A6345);
        result = ExHandleLogBadReference(Arg1, Arg2, Arg3, 6);
    }
    local_rdi = 0;
    goto loc_00868FA1;
loc_0086931A:
    Arg1 = (uint32_t)((local_rsi - 11) - ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)((Arg1) >> (1));
    result = (uint32_t)((Arg2 + Arg1 * 1) >> (3));
    result = (result) << (7);
    result = (result) + (v_rip + 6021319);
    v_stack_m478 = result;
    result = ExAllocateFromNPagedLookasideList(result, Arg2, Arg3, 6);
    goto loc_00869299;
loc_0086934D:
loc_00869353:
    if (1 < ((uint32_t)(v_stack_m488))) goto loc_008693CF;
    goto loc_008690F6;
loc_00869360:
    result = (result) + ((uint32_t)(v_stack_m4B0));
    v_stack_p20 = result;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, result + 48, Arg2 + 16);
loc_0086937B:
    if (0 == 0) goto loc_008693A0;
    result = (*(uint64_t *)(local_rsi + 0x1E8)) & (-2);
    if (condition_is_not_equal) goto loc_008695EE;
loc_008693A0:
    result = KiLeaveCriticalRegionUnsafe(0, result - 2, result + 48, Arg2 + 16);
    goto loc_0086918D;
loc_008693AD:
    if ((((uint8_t)(v_stack_m488)) & (2)) != 0) goto loc_00869403;
    goto loc_0086907E;
loc_008693BF:
    result = ExFreeToNPagedLookasideList(v_stack_m488 + local_rsi * 1, *(uint64_t *)(v_rip + 0x6A6345), result + 48, Arg2 + 16);
    goto loc_00869196;
loc_008693CF:
loc_008693DD:
    if ((*(uint64_t *)(v_stack_m4C8 + (uint32_t)((uint32_t)(Arg2 + 0x10)) * 8 + 0x80)) <= (*(uint64_t *)(v_stack_m4C8 + (uint32_t)((uint32_t)(Arg2 + 0x10)) - 0x1 * 8 + 0x80))) goto loc_00869437;
loc_008693EE:
    *(uint64_t *)(v_stack_m4C8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2 + 0x10)))) * 8 + 0x80) = *(uint64_t *)(v_stack_m4C8 + (uint32_t)((uint32_t)(Arg2 + 0x10)) * 8 + 0x80);
    Arg4 = (uint32_t)((Arg2 + 16) + 1);
    goto loc_00869353;
loc_00869403:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint16_t *)(local_rdi + 0xB4) + local_rsi * 1))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xB0)))));
    if (Arg1 == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xB0))))) goto loc_0086958C;
    local_rbx = ((uint32_t)(v_stack_m490)) + (-3);
    goto loc_0086907B;
loc_00869426:
    result = ExfReleaseRundownProtection(local_rsi + 488, (uint32_t)(*(uint32_t *)(local_rdi + 0xB0)), (uint32_t)((uint32_t)(Arg2 + 16)) - 1, Arg4);
    goto loc_008690D8;
loc_00869437:
    if (condition_is_equal) goto loc_00869564;
    *(uint64_t *)(v_stack_m4C8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xB0)))) * 8 + 0x80) = local_rbx;
    if ((uint32_t)((uint32_t)((uint32_t)(Arg2 + 16)) - 1) == 0) goto loc_008693EE;
    goto loc_008693DD;
loc_00869451:
    result = ObReferenceProcessHandleTable(local_rbx, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2 + 16)) - 1)), (uint32_t)((uint32_t)(Arg2 + 16)) - 1, Arg4);
    v_stack_m480 = result;
    if (result != 0) goto loc_0086955B;
loc_0086946D:
    if (((uint32_t)(result)) >= ((uint32_t)(local_rsi))) goto loc_008695F8;
    if ((uint8_t)(*(uint64_t *)(v_rip + 0x6A6345)) == 0) goto loc_0086959C;
loc_00869482:
    v_stack_m4C4 = 0xC000010AULL;
    goto loc_0086915A;
loc_00869499:
    v_stack_m4C4 = 0xC000A006ULL;
loc_008694A0:
    goto loc_0086915A;
loc_008694B9:
    Arg1 = ((uint16_t)(result - 1)) + ((uint16_t)(result - 1));
    Arg3 = ((uint32_t)((uint32_t)(Arg2 + 16)) - 1) & (0xFFFFFFFFFFFE0001ULL);
    Arg1 = (Arg1) | (Arg3);
    v_stack_m4A0 = Arg1;
    result = ExGetHandlePointer(v_stack_m4A0, *(uint64_t *)(v_stack_m470 + result * 8), Arg3, Arg4);
    if (condition_is_less_or_equal) goto loc_008695C2;
    result = ExFastReplenishHandleTableEntry(v_stack_m4A8, v_stack_m4A0, (uint32_t)(0x7FF0ULL), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00868F9D;
    result = (uint32_t)(-(result));
    goto loc_00868F9D;
loc_00869519:
    Arg1 = 0;
    result = KeSetKernelStackSwapEnable(Arg1, v_stack_m4A0, (uint32_t)(0x7FF0ULL), Arg4);
    v_stack_m4C5 = (uint8_t)(result);
    result = (v_stack_m4B8 + v_stack_m4B8 * 2) << (4);
    if ((result + 15) <= result) {
    }
    Arg1 = (result + 15) & (-16);
    result = _chkstk(Arg1, v_stack_m4A0, (uint32_t)(0x7FF0ULL), Arg4);
    local_rsp = (v_stack_m38) - (Arg1);
    v_stack_m4C0 = v_stack_p40;
    goto loc_00868E8F;
loc_0086955B:
    v_stack_m4C8 = 1;
    goto loc_00868ED5;
loc_00869564:
    v_stack_m4C4 = 0xC0000030ULL;
    goto loc_0086915A;
loc_00869574:
    v_stack_m4C4 = 0xC0000022ULL;
    goto loc_008694A0;
loc_00869580:
    v_stack_m4C4 = 0xC0000024ULL;
    goto loc_008694A0;
loc_0086958C:
    goto loc_0086907E;
loc_0086959C:
    result = (v_stack_m4A0) & (0xFFFFFFFF80000000ULL);
    if (result != 0xFFFFFFFF80000000ULL) goto loc_00869482;
    if (v_stack_m4A0 > -3) goto loc_00869482;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_0086946D;
loc_008695C2:
    result = (result) + (0x7FF0ULL);
    v_stack_p20 = result;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, result + 48, Arg2 + 16);
loc_008695E0:
    result = KeSetKernelStackSwapEnable(v_stack_m4C5, Arg2, result + 48, Arg2 + 16);
    goto loc_00869196;
loc_008695EE:
    result = ExfReleaseRundownProtection(v_stack_m4C5, Arg2, result + 48, Arg2 + 16);
    goto loc_008693A0;
loc_008695F8:
    goto loc_00868ED5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00868DF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
