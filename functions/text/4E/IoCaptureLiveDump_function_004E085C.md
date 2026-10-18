# IoCaptureLiveDump

- RVA: `0x004E085C`–`0x004E1108` (길이 `2,220` bytes)
- VA: `0x00000001404E085C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF078`
- 디코드: `500`개 명령, `2,220/2,220` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **52**; 고유 호출 대상: **32**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **23**

### Outgoing calls
- `0x004E090A` → [IopLiveDumpTraceIoCaptureLiveDumpEntry](../5A/IopLiveDumpTraceIoCaptureLiveDumpEntry_function_005A4320.md) (function, `0x005A4320`)
- `0x004E0916` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x004E091D` → [IopLiveDumpGetMillisecondCounter](../3F/IopLiveDumpGetMillisecondCounter_function_003F5964.md) (function, `0x003F5964`)
- `0x004E0945` → [IopLiveDumpCaptureDumpStart](../59/IopLiveDumpCaptureDumpStart_function_0059B02C.md) (function, `0x0059B02C`)
- `0x004E096D` → [ExAcquireResourceExclusiveLite](../21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x004E09AB` → [ExGetExtensionTable](../42/ExGetExtensionTable_function_00428814.md) (function, `0x00428814`)
- `0x004E09C1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004E09D1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004E09E6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004E09EF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x004E0A21` → [RtlInitUnicodeString](../42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x004E0A2F` → [IoCreateNotificationEvent](../../page/A8/IoCreateNotificationEvent_function_00A80470.md) (function, `0x00A80470`)
- `0x004E0A42` → [RtlInitUnicodeString](../42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x004E0A50` → [IoCreateNotificationEvent](../../page/A8/IoCreateNotificationEvent_function_00A80470.md) (function, `0x00A80470`)
- `0x004E0A63` → [RtlInitUnicodeString](../42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x004E0A71` → [IoCreateNotificationEvent](../../page/A8/IoCreateNotificationEvent_function_00A80470.md) (function, `0x00A80470`)
- `0x004E0A8B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004E0B77` → [IopLiveDumpInitRegistrySettings](../59/IopLiveDumpInitRegistrySettings_function_0059C8A4.md) (function, `0x0059C8A4`)
- `0x004E0BAE` → [EtwActivityIdControl](../41/EtwActivityIdControl_function_0041E720.md) (function, `0x0041E720`)
- `0x004E0BBF` → [EtwActivityIdControl](../41/EtwActivityIdControl_function_0041E720.md) (function, `0x0041E720`)
- `0x004E0BDE` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x004E0C2D` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E0C38` → [IopLiveDumpValidateParameters](../59/IopLiveDumpValidateParameters_function_0059F690.md) (function, `0x0059F690`)
- `0x004E0C6A` → [IopLiveDumpOpenVMMemoryPartition](../59/IopLiveDumpOpenVMMemoryPartition_function_0059D508.md) (function, `0x0059D508`)
- `0x004E0C72` → [IopLiveDumpAllocAndInitResources](../59/IopLiveDumpAllocAndInitResources_function_005993B0.md) (function, `0x005993B0`)
- `0x004E0C80` → [IopLiveDumpCaptureMemoryPages](../59/IopLiveDumpCaptureMemoryPages_function_0059B0A0.md) (function, `0x0059B0A0`)
- `0x004E0CAC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004E0CB5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x004E0CD1` → [ZwClose](../6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x004E0CDE` → [ZwClose](../6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x004E0CF0` → [ZwClose](../6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x004E0D04` → [IopLiveDumpIsTracingEnabled](../4F/IopLiveDumpIsTracingEnabled_function_004FC5AC.md) (function, `0x004FC5AC`)
- `0x004E0D14` → [IopLiveDumpTraceNoArgs](../5A/IopLiveDumpTraceNoArgs_function_005A43C0.md) (function, `0x005A43C0`)
- `0x004E0D2E` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x004E0D33` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x004E0D47` → [SecureDump_GetSecureDumpSettings](../4F/SecureDump_GetSecureDumpSettings_function_004F8128.md) (function, `0x004F8128`)
- `0x004E0D9D` → [IopLiveDumpTraceNoArgs](../5A/IopLiveDumpTraceNoArgs_function_005A43C0.md) (function, `0x005A43C0`)
- `0x004E0DA4` → [IopLiveDumpGetMillisecondCounter](../3F/IopLiveDumpGetMillisecondCounter_function_003F5964.md) (function, `0x003F5964`)
- `0x004E0DC1` → [IopLiveDumpWriteDumpFile](../3F/IopLiveDumpWriteDumpFile_function_003F6360.md) (function, `0x003F6360`)
- `0x004E0DCB` → [IopLiveDumpWriteDumpFileWithExtraPages](../59/IopLiveDumpWriteDumpFileWithExtraPages_function_0059F910.md) (function, `0x0059F910`)
- `0x004E0DD4` → [IopLiveDumpGetMillisecondCounter](../3F/IopLiveDumpGetMillisecondCounter_function_003F5964.md) (function, `0x003F5964`)
- `0x004E0DFA` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x004E0E8E` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E0EA2` → [IopLiveDumpTraceDumpFileWriteEnd](../59/IopLiveDumpTraceDumpFileWriteEnd_function_0059EB00.md) (function, `0x0059EB00`)
- `0x004E0EC4` → [IopLiveDumpGetMillisecondCounter](../3F/IopLiveDumpGetMillisecondCounter_function_003F5964.md) (function, `0x003F5964`)
- `0x004E0ED7` → [IopLiveDumpTraceInterfaceEnd](../59/IopLiveDumpTraceInterfaceEnd_function_0059EC24.md) (function, `0x0059EC24`)
- `0x004E0EFA` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x004E1093` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E10B0` → [EtwActivityIdControl](../41/EtwActivityIdControl_function_0041E720.md) (function, `0x0041E720`)
- `0x004E10C0` → [IopLiveDumpReleaseResources](../59/IopLiveDumpReleaseResources_function_0059DF1C.md) (function, `0x0059DF1C`)
- `0x004E10CD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004E10EE` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [DbgkCaptureLiveKernelDump](../58/DbgkCaptureLiveKernelDump_function_00580288.md) at `0x005805B9`
- [DbgkpWerCaptureLiveFullDump](../../page/AB/DbgkpWerCaptureLiveFullDump_function_00AB0DAC.md) at `0x00AB0F28`

### Static image references
- `0x004E0878` → RVA `0x00E0A740` (`.data`; read)
- `0x004E0893` → RVA `0x00E660BC` (`.data`; read)
- `0x004E08E8` → RVA `0x00E0A9B8` (`.data`; read)
- `0x004E08F5` → RVA `0x00E66182` (`.data`; read)
- `0x004E090F` → RVA `0x00F8D088` (`.data`; read)
- `0x004E092B` → RVA `0x00E0A9D0` (`.data`; read)
- `0x004E0933` → RVA `0x00E0A9D0` (`.data`; write)
- `0x004E093C` → RVA `0x00E0A9D4` (`.data`; write)
- `0x004E095C` → RVA `0x00F8D0A0` (`.data`; read)
- `0x004E099C` → RVA `0x00F225E0` (`.data`; read)
- `0x004E09B0` → RVA `0x00E66178` (`.data`; write)
- `0x004E09C6` → RVA `0x00E66178` (`.data`; read)
- `0x004E0A16` → RVA `0x006CA090` (` ?? ::FNODOBFM::`string'`; read)
- `0x004E0A34` → RVA `0x006CA1C0` (` ?? ::FNODOBFM::`string'`; read)
- `0x004E0A55` → RVA `0x006CA210` (` ?? ::FNODOBFM::`string'`; read)
- `0x004E0B3A` → RVA `0x00E66188` (`.data`; write)
- `0x004E0BC4` → RVA `0x00E06EA0` (`.data`; read)
- `0x004E0C0D` → RVA `0x000460A6` (`.rdata`; read)
- `0x004E0D0D` → RVA `0x00021460` (`.rdata`; read)
- `0x004E0D96` → RVA `0x000213C0` (`.rdata`; read)
- `0x004E0E2E` → RVA `0x000461DF` (`.rdata`; read)
- `0x004E0FE1` → RVA `0x00E66181` (`.data`; read)
- `0x004E107D` → RVA `0x000460D9` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x004E0A2F` → [IoCreateNotificationEvent](../../page/A8/IoCreateNotificationEvent_function_00A80470.md) (`.text` → `PAGE`)
  - `0x004E0A50` → [IoCreateNotificationEvent](../../page/A8/IoCreateNotificationEvent_function_00A80470.md) (`.text` → `PAGE`)
  - `0x004E0A71` → [IoCreateNotificationEvent](../../page/A8/IoCreateNotificationEvent_function_00A80470.md) (`.text` → `PAGE`)
  - `0x004E0A8B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004E10CD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004E085C  40 55                           push rbp
004E085E  53                              push rbx
004E085F  56                              push rsi
004E0860  57                              push rdi
004E0861  41 54                           push r12
004E0863  41 55                           push r13
004E0865  41 56                           push r14
004E0867  41 57                           push r15
004E0869  48 8D AC 24 18 FF FF FF         lea rbp, [rsp - 0xe8]
004E0871  48 81 EC E8 01 00 00            sub rsp, 0x1e8
004E0878  48 8B 05 C1 9E 92 00            mov rax, qword ptr [rip + 0x929ec1]
004E087F  48 33 C4                        xor rax, rsp
004E0882  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
004E0889  4C 8B BD 58 01 00 00            mov r15, qword ptr [rbp + 0x158]
004E0890  45 33 F6                        xor r14d, r14d
004E0893  44 38 35 22 58 98 00            cmp byte ptr [rip + 0x985822], r14b
004E089A  0F 57 C0                        xorps xmm0, xmm0
004E089D  4C 8B A5 60 01 00 00            mov r12, qword ptr [rbp + 0x160]
004E08A4  0F 57 C9                        xorps xmm1, xmm1
004E08A7  4C 89 4C 24 78                  mov qword ptr [rsp + 0x78], r9
004E08AC  41 8B FE                        mov edi, r14d
004E08AF  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
004E08B4  41 8B F6                        mov esi, r14d
004E08B7  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
004E08BC  45 8B EE                        mov r13d, r14d
004E08BF  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
004E08C3  41 8B DE                        mov ebx, r14d
004E08C6  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
004E08CB  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
004E08D0  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
004E08D5  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
004E08DA  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
004E08DE  0F 11 4D 90                     movups xmmword ptr [rbp - 0x70], xmm1
004E08E2  0F 85 EE 07 00 00               jne 0x1404e10d6
004E08E8  44 38 35 C9 A0 92 00            cmp byte ptr [rip + 0x92a0c9], r14b
004E08EF  0F 84 E1 07 00 00               je 0x1404e10d6
004E08F5  44 38 35 86 58 98 00            cmp byte ptr [rip + 0x985886], r14b
004E08FC  74 11                           je 0x1404e090f
004E08FE  48 8B 85 50 01 00 00            mov rax, qword ptr [rbp + 0x150]
004E0905  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004E090A  E8 11 3A 0C 00                  call 0x1405a4320
004E090F  48 8D 0D 72 C7 AA 00            lea rcx, [rip + 0xaac772]
004E0916  E8 C5 DE E9 FF                  call 0x14037e7e0
004E091B  B1 01                           mov cl, 1
004E091D  E8 42 50 F1 FF                  call 0x1403f5964
004E0922  A1 44 02 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff78000000244]
004E092B  39 05 9F A0 92 00               cmp dword ptr [rip + 0x92a09f], eax
004E0931  74 0F                           je 0x1404e0942
004E0933  89 05 97 A0 92 00               mov dword ptr [rip + 0x92a097], eax
004E0939  C1 E8 0C                        shr eax, 0xc
004E093C  89 05 92 A0 92 00               mov dword ptr [rip + 0x92a092], eax
004E0942  49 8B CF                        mov rcx, r15
004E0945  E8 E2 A6 0B 00                  call 0x14059b02c
004E094A  4D 85 E4                        test r12, r12
004E094D  74 04                           je 0x1404e0953
004E094F  4D 89 34 24                     mov qword ptr [r12], r14
004E0953  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004E095C  48 8D 0D 3D C7 AA 00            lea rcx, [rip + 0xaac73d]
004E0963  33 D2                           xor edx, edx
004E0965  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
004E096C  90                              nop
004E096D  E8 AE 44 D3 FF                  call 0x140214e20
004E0972  88 44 24 30                     mov byte ptr [rsp + 0x30], al
004E0976  3C 01                           cmp al, 1
004E0978  74 22                           je 0x1404e099c
004E097A  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004E097F  BF 2D 02 00 C0                  mov edi, 0xc000022d
004E0984  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
004E0989  49 83 C7 18                     add r15, 0x18
004E098D  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
004E0992  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
004E0997  E9 FF 02 00 00                  jmp 0x1404e0c9b
004E099C  4C 8B 2D 3D 1C A4 00            mov r13, qword ptr [rip + 0xa41c3d]
004E09A3  4D 85 ED                        test r13, r13
004E09A6  74 63                           je 0x1404e0a0b
004E09A8  49 8B CD                        mov rcx, r13
004E09AB  E8 64 7E F4 FF                  call 0x140428814
004E09B0  48 89 05 C1 57 98 00            mov qword ptr [rip + 0x9857c1], rax
004E09B7  48 85 C0                        test rax, rax
004E09BA  74 3F                           je 0x1404e09fb
004E09BC  48 8B 00                        mov rax, qword ptr [rax]
004E09BF  B1 01                           mov cl, 1
004E09C1  E8 0A A1 1D 00                  call 0x1406baad0
004E09C6  48 8B 05 AB 57 98 00            mov rax, qword ptr [rip + 0x9857ab]
004E09CD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
004E09D1  E8 FA A0 1D 00                  call 0x1406baad0
004E09D6  84 C0                           test al, al
004E09D8  75 21                           jne 0x1404e09fb
004E09DA  48 8B 05 97 57 98 00            mov rax, qword ptr [rip + 0x985797]
004E09E1  33 C9                           xor ecx, ecx
004E09E3  48 8B 00                        mov rax, qword ptr [rax]
004E09E6  E8 E5 A0 1D 00                  call 0x1406baad0
004E09EB  49 8D 4D 58                     lea rcx, [r13 + 0x58]
004E09EF  E8 8C 94 E6 FF                  call 0x140349e80
004E09F4  4C 89 35 7D 57 98 00            mov qword ptr [rip + 0x98577d], r14
004E09FB  48 8B 05 76 57 98 00            mov rax, qword ptr [rip + 0x985776]
004E0A02  48 F7 D8                        neg rax
004E0A05  48 1B C9                        sbb rcx, rcx
004E0A08  4C 23 E9                        and r13, rcx
004E0A0B  4D 8D 77 18                     lea r14, [r15 + 0x18]
004E0A0F  41 8B 06                        mov eax, dword ptr [r14]
004E0A12  A8 10                           test al, 0x10
004E0A14  74 65                           je 0x1404e0a7b
004E0A16  48 8D 15 73 96 1E 00            lea rdx, [rip + 0x1e9673]
004E0A1D  48 8D 4D 80                     lea rcx, [rbp - 0x80]
004E0A21  E8 5A 9D F4 FF                  call 0x14042a780
004E0A26  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
004E0A2B  48 8D 4D 80                     lea rcx, [rbp - 0x80]
004E0A2F  E8 3C FA 59 00                  call 0x140a80470
004E0A34  48 8D 15 85 97 1E 00            lea rdx, [rip + 0x1e9785]
004E0A3B  48 8B F8                        mov rdi, rax
004E0A3E  48 8D 4D 80                     lea rcx, [rbp - 0x80]
004E0A42  E8 39 9D F4 FF                  call 0x14042a780
004E0A47  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
004E0A4C  48 8D 4D 80                     lea rcx, [rbp - 0x80]
004E0A50  E8 1B FA 59 00                  call 0x140a80470
004E0A55  48 8D 15 B4 97 1E 00            lea rdx, [rip + 0x1e97b4]
004E0A5C  48 8B F0                        mov rsi, rax
004E0A5F  48 8D 4D 80                     lea rcx, [rbp - 0x80]
004E0A63  E8 18 9D F4 FF                  call 0x14042a780
004E0A68  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
004E0A6D  48 8D 4D 80                     lea rcx, [rbp - 0x80]
004E0A71  E8 FA F9 59 00                  call 0x140a80470
004E0A76  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
004E0A7B  BA C8 04 00 00                  mov edx, 0x4c8
004E0A80  B9 40 00 00 00                  mov ecx, 0x40
004E0A85  41 B8 4C 64 6D 70               mov r8d, 0x706d644c
004E0A8B  E8 60 16 6A 00                  call 0x140b820f0
004E0A90  48 8B D8                        mov rbx, rax
004E0A93  48 85 C0                        test rax, rax
004E0A96  75 21                           jne 0x1404e0ab9
004E0A98  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E0A9D  4D 8B FE                        mov r15, r14
004E0AA0  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
004E0AA5  BF 9A 00 00 C0                  mov edi, 0xc000009a
004E0AAA  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
004E0AAF  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
004E0AB4  E9 E2 01 00 00                  jmp 0x1404e0c9b
004E0AB9  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
004E0ABD  8B 4B 50                        mov ecx, dword ptr [rbx + 0x50]
004E0AC0  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
004E0AC6  83 E1 F3                        and ecx, 0xfffffff3
004E0AC9  89 03                           mov dword ptr [rbx], eax
004E0ACB  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
004E0AD0  48 89 43 08                     mov qword ptr [rbx + 8], rax
004E0AD4  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
004E0AD9  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
004E0ADD  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
004E0AE2  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
004E0AE6  48 8B 85 50 01 00 00            mov rax, qword ptr [rbp + 0x150]
004E0AED  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
004E0AF1  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
004E0AF6  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
004E0AFC  48 89 83 88 03 00 00            mov qword ptr [rbx + 0x388], rax
004E0B03  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004E0B08  48 89 83 90 03 00 00            mov qword ptr [rbx + 0x390], rax
004E0B0F  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E0B14  48 89 83 98 03 00 00            mov qword ptr [rbx + 0x398], rax
004E0B1B  33 C0                           xor eax, eax
004E0B1D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
004E0B22  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
004E0B27  48 89 BB A0 03 00 00            mov qword ptr [rbx + 0x3a0], rdi
004E0B2E  33 FF                           xor edi, edi
004E0B30  48 89 83 B0 03 00 00            mov qword ptr [rbx + 0x3b0], rax
004E0B37  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
004E0B3A  48 89 1D 47 56 98 00            mov qword ptr [rip + 0x985647], rbx
004E0B41  48 89 B3 A8 03 00 00            mov qword ptr [rbx + 0x3a8], rsi
004E0B48  48 89 BB 48 04 00 00            mov qword ptr [rbx + 0x448], rdi
004E0B4F  48 89 BB 50 04 00 00            mov qword ptr [rbx + 0x450], rdi
004E0B56  89 4B 50                        mov dword ptr [rbx + 0x50], ecx
004E0B59  A8 04                           test al, 4
004E0B5B  74 09                           je 0x1404e0b66
004E0B5D  81 C9 00 80 01 00               or ecx, 0x18000
004E0B63  89 4B 50                        mov dword ptr [rbx + 0x50], ecx
004E0B66  48 8D B3 B0 04 00 00            lea rsi, [rbx + 0x4b0]
004E0B6D  48 8B CB                        mov rcx, rbx
004E0B70  48 89 76 08                     mov qword ptr [rsi + 8], rsi
004E0B74  48 89 36                        mov qword ptr [rsi], rsi
004E0B77  E8 28 BD 0B 00                  call 0x14059c8a4
004E0B7C  40 38 3D 35 9E 92 00            cmp byte ptr [rip + 0x929e35], dil
004E0B83  0F 84 00 01 00 00               je 0x1404e0c89
004E0B89  F7 43 50 00 02 00 00            test dword ptr [rbx + 0x50], 0x200
004E0B90  74 0D                           je 0x1404e0b9f
004E0B92  48 39 BB 78 04 00 00            cmp qword ptr [rbx + 0x478], rdi
004E0B99  0F 84 EA 00 00 00               je 0x1404e0c89
004E0B9F  48 8D BB B8 03 00 00            lea rdi, [rbx + 0x3b8]
004E0BA6  B9 05 00 00 00                  mov ecx, 5
004E0BAB  48 8B D7                        mov rdx, rdi
004E0BAE  E8 6D DB F3 FF                  call 0x14041e720
004E0BB3  48 8D 93 C8 03 00 00            lea rdx, [rbx + 0x3c8]
004E0BBA  B9 01 00 00 00                  mov ecx, 1
004E0BBF  E8 5C DB F3 FF                  call 0x14041e720
004E0BC4  83 3D D5 62 92 00 05            cmp dword ptr [rip + 0x9262d5], 5
004E0BCB  76 65                           jbe 0x1404e0c32
004E0BCD  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
004E0BD7  48 8D 0D C2 62 92 00            lea rcx, [rip + 0x9262c2]
004E0BDE  E8 BD DE F4 FF                  call 0x14042eaa0
004E0BE3  84 C0                           test al, al
004E0BE5  74 4B                           je 0x1404e0c32
004E0BE7  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
004E0BEB  48 8D 44 24 50                  lea rax, [rsp + 0x50]
004E0BF0  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
004E0BF4  4C 8D 83 C8 03 00 00            lea r8, [rbx + 0x3c8]
004E0BFB  48 8D 45 A0                     lea rax, [rbp - 0x60]
004E0BFF  48 C7 44 24 50 00 00 00 01      mov qword ptr [rsp + 0x50], 0x1000000
004E0C08  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E0C0D  48 8D 15 92 54 B6 FF            lea rdx, [rip - 0x49ab6e]
004E0C14  4C 8B CF                        mov r9, rdi
004E0C17  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
004E0C1F  48 8D 0D 7A 62 92 00            lea rcx, [rip + 0x92627a]
004E0C26  C7 45 C8 08 00 00 00            mov dword ptr [rbp - 0x38], 8
004E0C2D  E8 AE 54 F4 FF                  call 0x1404260e0
004E0C32  49 8B D7                        mov rdx, r15
004E0C35  48 8B CB                        mov rcx, rbx
004E0C38  E8 53 EA 0B 00                  call 0x14059f690
004E0C3D  8B F8                           mov edi, eax
004E0C3F  4D 8B FE                        mov r15, r14
004E0C42  85 C0                           test eax, eax
004E0C44  78 4B                           js 0x1404e0c91
004E0C46  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
004E0C49  A8 04                           test al, 4
004E0C4B  74 07                           je 0x1404e0c54
004E0C4D  81 4B 50 00 80 01 00            or dword ptr [rbx + 0x50], 0x18000
004E0C54  48 89 76 08                     mov qword ptr [rsi + 8], rsi
004E0C58  48 89 36                        mov qword ptr [rsi], rsi
004E0C5B  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
004E0C5E  A8 08                           test al, 8
004E0C60  74 05                           je 0x1404e0c67
004E0C62  4D 85 E4                        test r12, r12
004E0C65  74 25                           je 0x1404e0c8c
004E0C67  48 8B CB                        mov rcx, rbx
004E0C6A  E8 99 C8 0B 00                  call 0x14059d508
004E0C6F  48 8B CB                        mov rcx, rbx
004E0C72  E8 39 87 0B 00                  call 0x1405993b0
004E0C77  8B F8                           mov edi, eax
004E0C79  85 C0                           test eax, eax
004E0C7B  78 14                           js 0x1404e0c91
004E0C7D  48 8B CB                        mov rcx, rbx
004E0C80  E8 1B A4 0B 00                  call 0x14059b0a0
004E0C85  8B F8                           mov edi, eax
004E0C87  EB 08                           jmp 0x1404e0c91
004E0C89  4D 8B FE                        mov r15, r14
004E0C8C  BF 0D 00 00 C0                  mov edi, 0xc000000d
004E0C91  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
004E0C96  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
004E0C9B  48 8B 05 D6 54 98 00            mov rax, qword ptr [rip + 0x9854d6]
004E0CA2  48 85 C0                        test rax, rax
004E0CA5  74 1F                           je 0x1404e0cc6
004E0CA7  48 8B 00                        mov rax, qword ptr [rax]
004E0CAA  33 C9                           xor ecx, ecx
004E0CAC  E8 1F 9E 1D 00                  call 0x1406baad0
004E0CB1  49 8D 4D 58                     lea rcx, [r13 + 0x58]
004E0CB5  E8 C6 91 E6 FF                  call 0x140349e80
004E0CBA  45 33 ED                        xor r13d, r13d
004E0CBD  4C 89 2D B4 54 98 00            mov qword ptr [rip + 0x9854b4], r13
004E0CC4  EB 03                           jmp 0x1404e0cc9
004E0CC6  45 33 ED                        xor r13d, r13d
004E0CC9  48 85 F6                        test rsi, rsi
004E0CCC  74 08                           je 0x1404e0cd6
004E0CCE  48 8B CE                        mov rcx, rsi
004E0CD1  E8 DA C5 1C 00                  call 0x1406ad2b0
004E0CD6  4D 85 F6                        test r14, r14
004E0CD9  74 08                           je 0x1404e0ce3
004E0CDB  49 8B CE                        mov rcx, r14
004E0CDE  E8 CD C5 1C 00                  call 0x1406ad2b0
004E0CE3  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E0CE8  48 85 C0                        test rax, rax
004E0CEB  74 08                           je 0x1404e0cf5
004E0CED  48 8B C8                        mov rcx, rax
004E0CF0  E8 BB C5 1C 00                  call 0x1406ad2b0
004E0CF5  41 8B 07                        mov eax, dword ptr [r15]
004E0CF8  A8 10                           test al, 0x10
004E0CFA  74 1D                           je 0x1404e0d19
004E0CFC  81 FF 40 02 00 C0               cmp edi, 0xc0000240
004E0D02  75 15                           jne 0x1404e0d19
004E0D04  E8 A3 B8 01 00                  call 0x1404fc5ac
004E0D09  3C 01                           cmp al, 1
004E0D0B  75 0C                           jne 0x1404e0d19
004E0D0D  48 8D 0D 4C 07 B4 FF            lea rcx, [rip - 0x4bf8b4]
004E0D14  E8 A7 36 0C 00                  call 0x1405a43c0
004E0D19  44 38 6C 24 30                  cmp byte ptr [rsp + 0x30], r13b
004E0D1E  74 13                           je 0x1404e0d33
004E0D20  48 8D 0D 79 C3 AA 00            lea rcx, [rip + 0xaac379]
004E0D27  4C 89 2D 5A 54 98 00            mov qword ptr [rip + 0x98545a], r13
004E0D2E  E8 DD EC D7 FF                  call 0x14025fa10
004E0D33  E8 78 CB D7 FF                  call 0x14025d8b0
004E0D38  85 FF                           test edi, edi
004E0D3A  0F 88 82 01 00 00               js 0x1404e0ec2
004E0D40  48 8D 8B D8 03 00 00            lea rcx, [rbx + 0x3d8]
004E0D47  E8 DC 73 01 00                  call 0x1404f8128
004E0D4C  8B F8                           mov edi, eax
004E0D4E  85 C0                           test eax, eax
004E0D50  0F 88 6C 01 00 00               js 0x1404e0ec2
004E0D56  44 38 29                        cmp byte ptr [rcx], r13b
004E0D59  74 30                           je 0x1404e0d8b
004E0D5B  8B 83 E0 03 00 00               mov eax, dword ptr [rbx + 0x3e0]
004E0D61  85 C0                           test eax, eax
004E0D63  74 1C                           je 0x1404e0d81
004E0D65  44 38 AB D9 03 00 00            cmp byte ptr [rbx + 0x3d9], r13b
004E0D6C  74 13                           je 0x1404e0d81
004E0D6E  81 BB DC 03 00 00 00 10 00 00   cmp dword ptr [rbx + 0x3dc], 0x1000
004E0D78  75 07                           jne 0x1404e0d81
004E0D7A  A9 FF 0F 00 00                  test eax, 0xfff
004E0D7F  74 0A                           je 0x1404e0d8b
004E0D81  BF 01 00 00 C0                  mov edi, 0xc0000001
004E0D86  E9 37 01 00 00                  jmp 0x1404e0ec2
004E0D8B  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
004E0D8E  A8 08                           test al, 8
004E0D90  0F 85 23 01 00 00               jne 0x1404e0eb9
004E0D96  48 8D 0D 23 06 B4 FF            lea rcx, [rip - 0x4bf9dd]
004E0D9D  E8 1E 36 0C 00                  call 0x1405a43c0
004E0DA2  33 C9                           xor ecx, ecx
004E0DA4  E8 BB 4B F1 FF                  call 0x1403f5964
004E0DA9  4C 8B F0                        mov r14, rax
004E0DAC  4C 39 AB C0 00 00 00            cmp qword ptr [rbx + 0xc0], r13
004E0DB3  75 13                           jne 0x1404e0dc8
004E0DB5  4C 39 AB C8 00 00 00            cmp qword ptr [rbx + 0xc8], r13
004E0DBC  75 0A                           jne 0x1404e0dc8
004E0DBE  48 8B CB                        mov rcx, rbx
004E0DC1  E8 9A 55 F1 FF                  call 0x1403f6360
004E0DC6  EB 08                           jmp 0x1404e0dd0
004E0DC8  48 8B CB                        mov rcx, rbx
004E0DCB  E8 40 EB 0B 00                  call 0x14059f910
004E0DD0  33 C9                           xor ecx, ecx
004E0DD2  8B F8                           mov edi, eax
004E0DD4  E8 8B 4B F1 FF                  call 0x1403f5964
004E0DD9  83 3D C0 60 92 00 05            cmp dword ptr [rip + 0x9260c0], 5
004E0DE0  48 8B F0                        mov rsi, rax
004E0DE3  0F 86 AA 00 00 00               jbe 0x1404e0e93
004E0DE9  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
004E0DF3  48 8D 0D A6 60 92 00            lea rcx, [rip + 0x9260a6]
004E0DFA  E8 A1 DC F4 FF                  call 0x14042eaa0
004E0DFF  84 C0                           test al, al
004E0E01  0F 84 8C 00 00 00               je 0x1404e0e93
004E0E07  48 8D 44 24 50                  lea rax, [rsp + 0x50]
004E0E0C  48 C7 44 24 50 00 00 00 01      mov qword ptr [rsp + 0x50], 0x1000000
004E0E15  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
004E0E19  4C 8D 8B B8 03 00 00            lea r9, [rbx + 0x3b8]
004E0E20  48 8B 83 30 02 00 00            mov rax, qword ptr [rbx + 0x230]
004E0E27  4C 8D 83 C8 03 00 00            lea r8, [rbx + 0x3c8]
004E0E2E  48 8D 15 AA 53 B6 FF            lea rdx, [rip - 0x49ac56]
004E0E35  48 C7 45 C8 08 00 00 00         mov qword ptr [rbp - 0x38], 8
004E0E3D  48 C7 45 D8 08 00 00 00         mov qword ptr [rbp - 0x28], 8
004E0E45  48 C7 45 E8 08 00 00 00         mov qword ptr [rbp - 0x18], 8
004E0E4D  48 8B 88 A0 0F 00 00            mov rcx, qword ptr [rax + 0xfa0]
004E0E54  48 8D 44 24 40                  lea rax, [rsp + 0x40]
004E0E59  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
004E0E5D  48 8B C6                        mov rax, rsi
004E0E60  49 2B C6                        sub rax, r14
004E0E63  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
004E0E68  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004E0E6D  48 8D 0D 2C 60 92 00            lea rcx, [rip + 0x92602c]
004E0E74  48 8D 44 24 48                  lea rax, [rsp + 0x48]
004E0E79  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
004E0E7D  48 8D 45 A0                     lea rax, [rbp - 0x60]
004E0E81  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E0E86  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
004E0E8E  E8 4D 52 F4 FF                  call 0x1404260e0
004E0E93  49 2B F6                        sub rsi, r14
004E0E96  44 8B CF                        mov r9d, edi
004E0E99  48 8B D6                        mov rdx, rsi
004E0E9C  45 33 C0                        xor r8d, r8d
004E0E9F  48 8B CB                        mov rcx, rbx
004E0EA2  E8 59 DC 0B 00                  call 0x14059eb00
004E0EA7  85 FF                           test edi, edi
004E0EA9  78 17                           js 0x1404e0ec2
004E0EAB  8B 43 50                        mov eax, dword ptr [rbx + 0x50]
004E0EAE  A8 02                           test al, 2
004E0EB0  74 10                           je 0x1404e0ec2
004E0EB2  BF 05 01 00 00                  mov edi, 0x105
004E0EB7  EB 09                           jmp 0x1404e0ec2
004E0EB9  BF 16 00 00 C0                  mov edi, 0xc0000016
004E0EBE  49 89 1C 24                     mov qword ptr [r12], rbx
004E0EC2  33 C9                           xor ecx, ecx
004E0EC4  E8 9B 4A F1 FF                  call 0x1403f5964
004E0EC9  4C 8B C8                        mov r9, rax
004E0ECC  44 8B C7                        mov r8d, edi
004E0ECF  33 D2                           xor edx, edx
004E0ED1  48 8B CB                        mov rcx, rbx
004E0ED4  48 8B F0                        mov rsi, rax
004E0ED7  E8 48 DD 0B 00                  call 0x14059ec24
004E0EDC  83 3D BD 5F 92 00 05            cmp dword ptr [rip + 0x925fbd], 5
004E0EE3  0F 86 AF 01 00 00               jbe 0x1404e1098
004E0EE9  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
004E0EF3  48 8D 0D A6 5F 92 00            lea rcx, [rip + 0x925fa6]
004E0EFA  E8 A1 DB F4 FF                  call 0x14042eaa0
004E0EFF  84 C0                           test al, al
004E0F01  0F 84 91 01 00 00               je 0x1404e1098
004E0F07  41 8B 0F                        mov ecx, dword ptr [r15]
004E0F0A  48 8D 44 24 50                  lea rax, [rsp + 0x50]
004E0F0F  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
004E0F13  BA 01 00 00 00                  mov edx, 1
004E0F18  48 8D 44 24 58                  lea rax, [rsp + 0x58]
004E0F1D  48 C7 44 24 50 00 00 00 01      mov qword ptr [rsp + 0x50], 0x1000000
004E0F26  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
004E0F2A  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
004E0F2E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
004E0F33  48 8D 44 24 40                  lea rax, [rsp + 0x40]
004E0F38  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
004E0F3C  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
004E0F41  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004E0F46  48 8D 44 24 68                  lea rax, [rsp + 0x68]
004E0F4B  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
004E0F4F  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
004E0F54  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
004E0F59  48 8D 44 24 70                  lea rax, [rsp + 0x70]
004E0F5E  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
004E0F62  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
004E0F67  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
004E0F6C  48 8D 44 24 78                  lea rax, [rsp + 0x78]
004E0F71  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
004E0F75  48 8B 85 50 01 00 00            mov rax, qword ptr [rbp + 0x150]
004E0F7C  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004E0F81  48 8D 44 24 48                  lea rax, [rsp + 0x48]
004E0F86  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
004E0F8A  8B C1                           mov eax, ecx
004E0F8C  C1 E8 03                        shr eax, 3
004E0F8F  22 C2                           and al, dl
004E0F91  48 C7 45 18 08 00 00 00         mov qword ptr [rbp + 0x18], 8
004E0F99  88 44 24 30                     mov byte ptr [rsp + 0x30], al
004E0F9D  48 8D 44 24 30                  lea rax, [rsp + 0x30]
004E0FA2  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
004E0FA9  8B C1                           mov eax, ecx
004E0FAB  C1 E8 04                        shr eax, 4
004E0FAE  22 C2                           and al, dl
004E0FB0  C1 E9 05                        shr ecx, 5
004E0FB3  88 44 24 31                     mov byte ptr [rsp + 0x31], al
004E0FB7  22 CA                           and cl, dl
004E0FB9  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
004E0FBD  48 8D 44 24 31                  lea rax, [rsp + 0x31]
004E0FC2  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
004E0FC9  48 8D 44 24 32                  lea rax, [rsp + 0x32]
004E0FCE  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
004E0FD5  48 8D 44 24 38                  lea rax, [rsp + 0x38]
004E0FDA  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
004E0FE1  8A 05 9A 51 98 00               mov al, byte ptr [rip + 0x98519a]
004E0FE7  88 44 24 33                     mov byte ptr [rsp + 0x33], al
004E0FEB  48 8D 44 24 33                  lea rax, [rsp + 0x33]
004E0FF0  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
004E0FF7  48 C7 45 28 04 00 00 00         mov qword ptr [rbp + 0x28], 4
004E0FFF  48 C7 45 38 08 00 00 00         mov qword ptr [rbp + 0x38], 8
004E1007  48 C7 45 48 08 00 00 00         mov qword ptr [rbp + 0x48], 8
004E100F  48 C7 45 58 08 00 00 00         mov qword ptr [rbp + 0x58], 8
004E1017  48 C7 45 68 08 00 00 00         mov qword ptr [rbp + 0x68], 8
004E101F  48 C7 45 78 08 00 00 00         mov qword ptr [rbp + 0x78], 8
004E1027  48 89 95 88 00 00 00            mov qword ptr [rbp + 0x88], rdx
004E102E  48 89 95 98 00 00 00            mov qword ptr [rbp + 0x98], rdx
004E1035  88 4C 24 32                     mov byte ptr [rsp + 0x32], cl
004E1039  48 89 95 A8 00 00 00            mov qword ptr [rbp + 0xa8], rdx
004E1040  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
004E1045  48 C7 85 B8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xb8], 8
004E1050  48 89 95 C8 00 00 00            mov qword ptr [rbp + 0xc8], rdx
004E1057  48 85 DB                        test rbx, rbx
004E105A  74 10                           je 0x1404e106c
004E105C  4C 8D 8B B8 03 00 00            lea r9, [rbx + 0x3b8]
004E1063  4C 8D 83 C8 03 00 00            lea r8, [rbx + 0x3c8]
004E106A  EB 08                           jmp 0x1404e1074
004E106C  4C 8D 4D 90                     lea r9, [rbp - 0x70]
004E1070  4C 8D 45 90                     lea r8, [rbp - 0x70]
004E1074  48 8D 45 F0                     lea rax, [rbp - 0x10]
004E1078  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E107D  48 8D 15 55 50 B6 FF            lea rdx, [rip - 0x49afab]
004E1084  48 8D 0D 15 5E 92 00            lea rcx, [rip + 0x925e15]
004E108B  C7 44 24 20 0E 00 00 00         mov dword ptr [rsp + 0x20], 0xe
004E1093  E8 48 50 F4 FF                  call 0x1404260e0
004E1098  48 85 DB                        test rbx, rbx
004E109B  74 35                           je 0x1404e10d2
004E109D  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
004E10A0  A8 08                           test al, 8
004E10A2  75 11                           jne 0x1404e10b5
004E10A4  48 8D 93 B8 03 00 00            lea rdx, [rbx + 0x3b8]
004E10AB  B9 02 00 00 00                  mov ecx, 2
004E10B0  E8 6B D6 F3 FF                  call 0x14041e720
004E10B5  81 FF 16 00 00 C0               cmp edi, 0xc0000016
004E10BB  74 15                           je 0x1404e10d2
004E10BD  48 8B CB                        mov rcx, rbx
004E10C0  E8 57 CE 0B 00                  call 0x14059df1c
004E10C5  BA 4C 64 6D 70                  mov edx, 0x706d644c
004E10CA  48 8B CB                        mov rcx, rbx
004E10CD  E8 9E 17 6A 00                  call 0x140b82870
004E10D2  8B C7                           mov eax, edi
004E10D4  EB 0E                           jmp 0x1404e10e4
004E10D6  4D 85 E4                        test r12, r12
004E10D9  74 04                           je 0x1404e10df
004E10DB  4D 89 34 24                     mov qword ptr [r12], r14
004E10DF  B8 BB 00 00 C0                  mov eax, 0xc00000bb
004E10E4  48 8B 8D D0 00 00 00            mov rcx, qword ptr [rbp + 0xd0]
004E10EB  48 33 CC                        xor rcx, rsp
004E10EE  E8 4D B5 1C 00                  call 0x1406ac640
004E10F3  48 81 C4 E8 01 00 00            add rsp, 0x1e8
004E10FA  41 5F                           pop r15
004E10FC  41 5E                           pop r14
004E10FE  41 5D                           pop r13
004E1100  41 5C                           pop r12
004E1102  5F                              pop rdi
004E1103  5E                              pop rsi
004E1104  5B                              pop rbx
004E1105  5D                              pop rbp
004E1106  C3                              ret
004E1107  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoCaptureLiveDump(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m15C;
    unsigned int v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int8 v_stack_m1F5;
    unsigned __int64 v_stack_m1F6;
    unsigned __int8 v_stack_m1F7;
    unsigned __int8 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (488);
    result = (*(unsigned __int64 *)(v_rip + 9608897)) ^ (v_rsp);
    v_stack_m58 = result;
    v_r14 = 0;
    v_stack_m1B0 = a4;
    v_stack_m1B8 = a3;
    v_stack_m1C0 = a2;
    v_stack_m1C8 = a1;
    v_stack_m1F0 = 0;
    v_stack_m1E0 = 0;
    v_stack_m1E8 = 0;
    v_stack_m1D8 = 0;
    v_stack_m1A8 = v_xmm0;
    v_stack_m198 = v_xmm1;
    if ((*(unsigned __int8 *)(v_rip + 9984034)) != 0) goto loc_004E10D6;
    if ((*(unsigned __int8 *)(v_rip + 9609417)) == 0) goto loc_004E10D6;
    if ((*(unsigned __int8 *)(v_rip + 9984134)) != 0) {
        result = a5;
        v_stack_m208 = result;
        result = IopLiveDumpTraceIoCaptureLiveDumpEntry(a1, a2, a3, a4);
    }
    result = KeQueryPerformanceCounter(v_rip + 11192178, a2, a3, a4);
    result = IopLiveDumpGetMillisecondCounter(1, a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 9609375)) != ((unsigned int)(result))) {
        *(unsigned int *)(v_rip + 9609367) = (unsigned int)(result);
        result = (unsigned int)((result) >> (12));
        *(unsigned int *)(v_rip + 9609362) = (unsigned int)(result);
    }
    result = IopLiveDumpCaptureDumpStart(a6, a2, a3, a4);
    if (a7 != 0) {
        *(unsigned __int64 *)(a7) = 0;
    }
    a2 = 0;
    result = ExAcquireResourceExclusiveLite(v_rip + 11192125, a2, a3, a4);
    v_stack_m1F8 = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) == 1) goto loc_004E099C;
    v_r15 = (a6) + (24);
    v_stack_m1E8 = v_stack_m1E8;
    goto loc_004E0C9B;
loc_004E099C:
    if (*(unsigned __int64 *)(v_rip + 10755133) == 0) goto loc_004E0A0B;
    result = ExGetExtensionTable(*(unsigned __int64 *)(v_rip + 10755133), a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 9983937) = result;
    if (result == 0) goto loc_004E09FB;
    result = guard_dispatch_icall(1, a2, a3, a4);
    result = guard_dispatch_icall(1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned __int64 *)(v_rip + 9983895);
        a1 = 0;
        result = *(unsigned __int64 *)(result);
        result = guard_dispatch_icall(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rip + 10755133) + 88;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
        *(unsigned __int64 *)(v_rip + 9983869) = v_stack_m1E0;
    }
    result = -(*(unsigned __int64 *)(v_rip + 9983862));
    v_r13 = (*(unsigned __int64 *)(v_rip + 10755133)) & (a1);
loc_004E0A0B:
    result = (unsigned int)(*(unsigned int *)(v_r15 + 24));
    v_rsi = v_stack_m1F0;
    v_rdi = (unsigned int)(0xC000022DULL);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r15 + 24)))) & (16)) != 0) {
        a2 = v_rip + 2004595;
        a1 = v_stack_m1A8;
        result = RtlInitUnicodeString(a1, a2, a3, a4);
        a2 = v_stack_m1F0;
        a1 = v_stack_m1A8;
        result = IoCreateNotificationEvent(a1, a2, a3, a4);
        a2 = v_rip + 2004869;
        v_rdi = result;
        a1 = v_stack_m1A8;
        result = RtlInitUnicodeString(a1, a2, a3, a4);
        a2 = v_stack_m1E0;
        a1 = v_stack_m1A8;
        result = IoCreateNotificationEvent(a1, a2, a3, a4);
        a2 = v_rip + 2004916;
        v_rsi = result;
        a1 = v_stack_m1A8;
        result = RtlInitUnicodeString(a1, a2, a3, a4);
        a2 = v_stack_m1E8;
        a1 = v_stack_m1A8;
        result = IoCreateNotificationEvent(a1, a2, a3, a4);
        v_stack_m1D8 = result;
    }
    result = ExAllocatePool2(64, (unsigned int)(0x4C8ULL), (unsigned int)(0x706D644CULL), a4);
    if (result != 0) goto loc_004E0AB9;
    v_stack_m1E8 = v_stack_m1E8;
    goto loc_004E0C9B;
loc_004E0AB9:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 80))) & (0xFFFFFFF3ULL));
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(v_stack_m1C8));
    *(unsigned __int64 *)(result + 8) = v_stack_m1C0;
    *(unsigned __int64 *)(result + 16) = v_stack_m1B8;
    *(unsigned __int64 *)(result + 24) = v_stack_m1B0;
    *(unsigned __int64 *)(result + 32) = a5;
    *(unsigned __int64 *)(result + 904) = v_stack_m1F0;
    *(unsigned __int64 *)(result + 912) = v_stack_m1E0;
    *(unsigned __int64 *)(result + 920) = v_stack_m1E8;
    result = 0;
    v_stack_m1E8 = 0;
    *(unsigned __int64 *)(result + 928) = (unsigned int)(0xC000009AULL);
    v_rdi = 0;
    *(unsigned __int64 *)(result + 944) = v_stack_m1D8;
    *(unsigned __int64 *)(v_rip + 9983559) = 0;
    *(unsigned __int64 *)(result + 936) = v_stack_m1F0;
    *(unsigned __int64 *)(result + 1096) = 0;
    *(unsigned __int64 *)(result + 1104) = 0;
    *(unsigned int *)(result + 80) = a1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 40)))) & (4)) != 0) {
        a1 = (unsigned int)((a1) | (0x18000ULL));
        *(unsigned int *)(result + 80) = a1;
    }
    *(unsigned __int64 *)(result + 1200 + 8) = result + 1200;
    *(unsigned __int64 *)(result + 1200) = result + 1200;
    result = IopLiveDumpInitRegistrySettings(0, (unsigned int)(0x4C8ULL), (unsigned int)(0x706D644CULL), a4);
    if ((*(unsigned __int8 *)(v_rip + 9608757)) == 0) goto loc_004E0C89;
    if (((*(unsigned int *)(result + 80)) & (512)) == 0) goto loc_004E0B9F;
    if ((*(unsigned __int64 *)(result + 1144)) == 0) goto loc_004E0C89;
loc_004E0B9F:
    result = EtwActivityIdControl(5, result + 952, (unsigned int)(0x706D644CULL), a4);
    result = EtwActivityIdControl(1, result + 968, (unsigned int)(0x706D644CULL), a4);
    if ((*(unsigned int *)(v_rip + 9593557)) <= 5) goto loc_004E0C32;
    result = tlgKeywordOn(v_rip + 9593538, result + 968, (unsigned int)(0x706D644CULL), a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m1D8;
        v_stack_m168 = result;
        a3 = result + 968;
        result = v_stack_m188;
        v_stack_m1D8 = 0x1000000ULL;
        v_stack_m200 = result;
        a2 = v_rip - 4828014;
        a4 = result + 952;
        v_stack_m208 = 3;
        a1 = v_rip + 9593466;
        v_stack_m160 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    result = IopLiveDumpValidateParameters(result, v_r15 + 24, a3, a4);
    if (sign_flag) goto loc_004E0C91;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 40)))) & (4)) != 0) {
    }
    *(unsigned __int64 *)(result + 1200 + 8) = result + 1200;
    *(unsigned __int64 *)(result + 1200) = result + 1200;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 40)))) & (8)) == 0) goto loc_004E0C67;
    if (a7 == 0) goto loc_004E0C8C;
loc_004E0C67:
    result = IopLiveDumpOpenVMMemoryPartition(result, v_r15 + 24, a3, a4);
    result = IopLiveDumpAllocAndInitResources(result, v_r15 + 24, a3, a4);
    if (sign_flag) goto loc_004E0C91;
    result = IopLiveDumpCaptureMemoryPages(result, v_r15 + 24, a3, a4);
    goto loc_004E0C91;
loc_004E0C89:
loc_004E0C8C:
loc_004E0C91:
loc_004E0C9B:
    if (*(unsigned __int64 *)(v_rip + 9983190) == 0) goto loc_004E0CC6;
    a1 = 0;
    result = guard_dispatch_icall(a1, v_r15 + 24, a3, a4);
    result = ExReleaseRundownProtection(v_r13 + 88, v_r15 + 24, a3, a4);
    v_r13 = 0;
    *(unsigned __int64 *)(v_rip + 9983156) = 0;
    goto loc_004E0CC9;
loc_004E0CC6:
    v_r13 = 0;
loc_004E0CC9:
    if (v_stack_m1D0 != 0) {
        a1 = v_stack_m1D0;
        result = ZwClose(a1, v_r15 + 24, a3, a4);
    }
    if (v_stack_m1F0 != 0) {
        a1 = v_stack_m1F0;
        result = ZwClose(a1, v_r15 + 24, a3, a4);
    }
    result = v_stack_m1E8;
    if (v_stack_m1E8 != 0) {
        a1 = v_stack_m1E8;
        result = ZwClose(a1, v_r15 + 24, a3, a4);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0)))) & (16)) == 0) goto loc_004E0D19;
    if (((unsigned int)((unsigned int)(0xC000000DULL))) != 0xC0000240ULL) goto loc_004E0D19;
    result = IopLiveDumpIsTracingEnabled(a1, v_r15 + 24, a3, a4);
    if (((unsigned __int8)(result)) == 1) {
        a1 = v_rip - 4978868;
        result = IopLiveDumpTraceNoArgs(a1, v_r15 + 24, a3, a4);
    }
    if (v_stack_m1F8 != 0) {
        a1 = v_rip + 11191161;
        *(unsigned __int64 *)(v_rip + 9983066) = 0;
        result = ExReleaseResourceLite(a1, v_r15 + 24, a3, a4);
    }
    result = KeLeaveCriticalRegion(a1, v_r15 + 24, a3, a4);
    if (sign_flag) goto loc_004E0EC2;
    result = SecureDump_GetSecureDumpSettings(result + 984, v_r15 + 24, a3, a4);
    if (sign_flag) goto loc_004E0EC2;
    if ((*(unsigned __int8 *)(result + 984)) == 0) goto loc_004E0D8B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 992))) == 0) goto loc_004E0D81;
    if ((*(unsigned __int8 *)(result + 985)) == 0) goto loc_004E0D81;
    if ((*(unsigned int *)(result + 988)) != 0x1000ULL) goto loc_004E0D81;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + 992)))) & (0xFFFULL)) == 0) goto loc_004E0D8B;
loc_004E0D81:
    goto loc_004E0EC2;
loc_004E0D8B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 40)))) & (8)) != 0) goto loc_004E0EB9;
    result = IopLiveDumpTraceNoArgs(v_rip - 4979165, v_r15 + 24, a3, a4);
    a1 = 0;
    result = IopLiveDumpGetMillisecondCounter(a1, v_r15 + 24, a3, a4);
    if ((*(unsigned __int64 *)(result + 192)) != 0) goto loc_004E0DC8;
    if ((*(unsigned __int64 *)(result + 200)) != 0) goto loc_004E0DC8;
    result = IopLiveDumpWriteDumpFile(result, v_r15 + 24, a3, a4);
    goto loc_004E0DD0;
loc_004E0DC8:
    result = IopLiveDumpWriteDumpFileWithExtraPages(result, v_r15 + 24, a3, a4);
loc_004E0DD0:
    a1 = 0;
    result = IopLiveDumpGetMillisecondCounter(a1, v_r15 + 24, a3, a4);
    if ((*(unsigned int *)(v_rip + 9593024)) <= 5) goto loc_004E0E93;
    result = tlgKeywordOn(v_rip + 9592998, v_r15 + 24, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m1D8;
        v_stack_m1D8 = 0x1000000ULL;
        v_stack_m168 = result;
        a4 = result + 952;
        result = *(unsigned __int64 *)(result + 560);
        a3 = result + 968;
        a2 = v_rip - 4828246;
        v_stack_m160 = 8;
        v_stack_m150 = 8;
        v_stack_m140 = 8;
        a1 = *(unsigned __int64 *)(result + 4000);
        result = v_stack_m1E8;
        v_stack_m158 = result;
        result = result;
        result = (result) - (result);
        v_stack_m1E8 = a1;
        v_stack_m1E0 = result;
        a1 = v_rip + 9592876;
        result = v_stack_m1E0;
        v_stack_m148 = result;
        result = v_stack_m188;
        v_stack_m200 = result;
        v_stack_m208 = 5;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    v_rsi = (result) - (result);
    a3 = 0;
    result = IopLiveDumpTraceDumpFileWriteEnd(result, v_rsi, a3, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (sign_flag) goto loc_004E0EC2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 80)))) & (2)) == 0) goto loc_004E0EC2;
    goto loc_004E0EC2;
loc_004E0EB9:
    *(unsigned __int64 *)(a7) = result;
loc_004E0EC2:
    a1 = 0;
    result = IopLiveDumpGetMillisecondCounter(a1, v_rsi, a3, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    a2 = 0;
    result = IopLiveDumpTraceInterfaceEnd(result, a2, (unsigned int)((unsigned int)((unsigned int)(0xC0000016ULL))), result);
    if ((*(unsigned int *)(v_rip + 9592765)) <= 5) goto loc_004E1098;
    result = tlgKeywordOn(v_rip + 9592742, a2, (unsigned int)((unsigned int)((unsigned int)(0xC0000016ULL))), result);
    if ((unsigned __int8)(result) == 0) goto loc_004E1098;
    v_stack_m118 = v_stack_m1D8;
    v_stack_m1D8 = 0x1000000ULL;
    v_stack_m108 = v_stack_m1D0;
    v_stack_m1E8 = (unsigned int)(v_stack_m1C8);
    v_stack_mF8 = v_stack_m1E8;
    v_stack_m1C0 = v_stack_m1C0;
    v_stack_mE8 = v_stack_m1C0;
    v_stack_m1B8 = v_stack_m1B8;
    v_stack_mD8 = v_stack_m1B8;
    v_stack_m1B0 = v_stack_m1B0;
    v_stack_mC8 = v_stack_m1B0;
    v_stack_m1E0 = a5;
    v_stack_mB8 = v_stack_m1E0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1E0))))) >> (3));
    result = (unsigned __int8)((result) & (1));
    v_stack_m110 = 8;
    v_stack_m1F8 = (unsigned __int8)(result);
    v_stack_mA8 = v_stack_m1F8;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1E0))))) >> (4));
    result = (unsigned __int8)((result) & (1));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1E0))) >> (5));
    v_stack_m1F7 = (unsigned __int8)(result);
    a1 = (unsigned __int8)((a1) & (1));
    v_stack_m1D0 = (unsigned int)((unsigned int)(0xC0000016ULL));
    v_stack_m98 = v_stack_m1F7;
    v_stack_m88 = v_stack_m1F6;
    v_stack_m78 = v_stack_m1F0;
    v_stack_m1F5 = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 9982362));
    v_stack_m68 = v_stack_m1F5;
    v_stack_m100 = 4;
    v_stack_mF0 = 8;
    v_stack_mE0 = 8;
    v_stack_mD0 = 8;
    v_stack_mC0 = 8;
    v_stack_mB0 = 8;
    v_stack_mA0 = 1;
    v_stack_m90 = 1;
    v_stack_m1F6 = (unsigned __int8)(a1);
    v_stack_m80 = 1;
    v_stack_m1F0 = result;
    v_stack_m70 = 8;
    v_stack_m60 = 1;
    if (result == 0) goto loc_004E106C;
    goto loc_004E1074;
loc_004E106C:
loc_004E1074:
    v_stack_m200 = v_stack_m138;
    v_stack_m208 = 14;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 9592341, v_rip - 4829099, v_stack_m198, v_stack_m198);
loc_004E1098:
    if (result == 0) goto loc_004E10D2;
    result = (unsigned int)(*(unsigned int *)(result + 40));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 40)))) & (8)) == 0) {
        a2 = result + 952;
        a1 = 2;
        result = EtwActivityIdControl(a1, a2, v_stack_m198, v_stack_m198);
    }
    if (((unsigned int)((unsigned int)(0xC0000016ULL))) != 0xC0000016ULL) {
        a1 = result;
        result = IopLiveDumpReleaseResources(a1, a2, v_stack_m198, v_stack_m198);
        a2 = 0x706D644CULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_m198, v_stack_m198);
    }
    goto loc_004E10E4;
loc_004E10D6:
    if (a7 != 0) {
        *(unsigned __int64 *)(a7) = result;
    }
loc_004E10E4:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m198, v_stack_m198);
    v_rsp = (v_rsp) + (488);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoCaptureLiveDump(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, void *Arg6, int64_t Arg7)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m15C;
    uint32_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m188;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint8_t v_stack_m1F5;
    uint64_t v_stack_m1F6;
    uint8_t v_stack_m1F7;
    uint8_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (488);
    result = (*(uint64_t *)(v_rip + 0x929EC1)) ^ (local_rsp);
    v_stack_m58 = result;
    local_r14 = 0;
    v_stack_m1B0 = Arg4;
    v_stack_m1B8 = Arg3;
    v_stack_m1C0 = Arg2;
    v_stack_m1C8 = Arg1;
    v_stack_m1F0 = 0;
    v_stack_m1E0 = 0;
    v_stack_m1E8 = 0;
    v_stack_m1D8 = 0;
    v_stack_m1A8 = v_xmm0;
    v_stack_m198 = v_xmm1;
    if ((*(uint8_t *)(v_rip + 0x985822)) != 0) goto loc_004E10D6;
    if ((*(uint8_t *)(v_rip + 0x92A0C9)) == 0) goto loc_004E10D6;
    if ((*(uint8_t *)(v_rip + 0x985886)) != 0) {
        result = Arg5;
        v_stack_m208 = result;
        result = IopLiveDumpTraceIoCaptureLiveDumpEntry(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeQueryPerformanceCounter(v_rip + 11192178, Arg2, Arg3, Arg4);
    result = IopLiveDumpGetMillisecondCounter(1, Arg2, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x92A09F)) != ((uint32_t)(result))) {
        *(uint32_t *)(v_rip + 0x92A097) = (uint32_t)(result);
        result = (uint32_t)((result) >> (12));
        *(uint32_t *)(v_rip + 0x92A092) = (uint32_t)(result);
    }
    result = IopLiveDumpCaptureDumpStart(Arg6, Arg2, Arg3, Arg4);
    if (Arg7 != 0) {
        *(uint64_t *)(Arg7) = 0;
    }
    Arg2 = 0;
    result = ExAcquireResourceExclusiveLite(v_rip + 11192125, Arg2, Arg3, Arg4);
    v_stack_m1F8 = (uint8_t)(result);
    if (((uint8_t)(result)) == 1) goto loc_004E099C;
    local_r15 = (Arg6) + (24);
    v_stack_m1E8 = v_stack_m1E8;
    goto loc_004E0C9B;
loc_004E099C:
    if (*(uint64_t *)(v_rip + 0xA41C3D) == 0) goto loc_004E0A0B;
    result = ExGetExtensionTable(*(uint64_t *)(v_rip + 0xA41C3D), Arg2, Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x9857C1) = result;
    if (result == 0) goto loc_004E09FB;
    result = guard_dispatch_icall(1, Arg2, Arg3, Arg4);
    result = guard_dispatch_icall(1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) {
        result = *(uint64_t *)(v_rip + 0x985797);
        Arg1 = 0;
        result = *(uint64_t *)(result);
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(v_rip + 0xA41C3D) + 88;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
        *(uint64_t *)(v_rip + 0x98577D) = v_stack_m1E0;
    }
    result = -(*(uint64_t *)(v_rip + 0x985776));
    local_r13 = (*(uint64_t *)(v_rip + 0xA41C3D)) & (Arg1);
loc_004E0A0B:
    result = (uint32_t)(*(uint32_t *)(local_r15 + 0x18));
    local_rsi = v_stack_m1F0;
    local_rdi = (uint32_t)(0xC000022DULL);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x18)))) & (16)) != 0) {
        Arg2 = v_rip + 2004595;
        Arg1 = v_stack_m1A8;
        result = RtlInitUnicodeString(Arg1, Arg2, Arg3, Arg4);
        Arg2 = v_stack_m1F0;
        Arg1 = v_stack_m1A8;
        result = IoCreateNotificationEvent(Arg1, Arg2, Arg3, Arg4);
        Arg2 = v_rip + 2004869;
        local_rdi = result;
        Arg1 = v_stack_m1A8;
        result = RtlInitUnicodeString(Arg1, Arg2, Arg3, Arg4);
        Arg2 = v_stack_m1E0;
        Arg1 = v_stack_m1A8;
        result = IoCreateNotificationEvent(Arg1, Arg2, Arg3, Arg4);
        Arg2 = v_rip + 2004916;
        local_rsi = result;
        Arg1 = v_stack_m1A8;
        result = RtlInitUnicodeString(Arg1, Arg2, Arg3, Arg4);
        Arg2 = v_stack_m1E8;
        Arg1 = v_stack_m1A8;
        result = IoCreateNotificationEvent(Arg1, Arg2, Arg3, Arg4);
        v_stack_m1D8 = result;
    }
    result = ExAllocatePool2(64, (uint32_t)(0x4C8ULL), (uint32_t)(0x706D644CULL), Arg4);
    if (result != 0) goto loc_004E0AB9;
    v_stack_m1E8 = v_stack_m1E8;
    goto loc_004E0C9B;
loc_004E0AB9:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x50))) & (0xFFFFFFF3ULL));
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(v_stack_m1C8));
    *(uint64_t *)(result + 0x8) = v_stack_m1C0;
    *(uint64_t *)(result + 0x10) = v_stack_m1B8;
    *(uint64_t *)(result + 0x18) = v_stack_m1B0;
    *(uint64_t *)(result + 0x20) = Arg5;
    *(uint64_t *)(result + 0x388) = v_stack_m1F0;
    *(uint64_t *)(result + 0x390) = v_stack_m1E0;
    *(uint64_t *)(result + 0x398) = v_stack_m1E8;
    result = 0;
    v_stack_m1E8 = 0;
    *(uint64_t *)(result + 0x3A0) = (uint32_t)(0xC000009AULL);
    local_rdi = 0;
    *(uint64_t *)(result + 0x3B0) = v_stack_m1D8;
    *(uint64_t *)(v_rip + 0x985647) = 0;
    *(uint64_t *)(result + 0x3A8) = v_stack_m1F0;
    *(uint64_t *)(result + 0x448) = 0;
    *(uint64_t *)(result + 0x450) = 0;
    *(uint32_t *)(result + 0x50) = Arg1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x28)))) & (4)) != 0) {
        Arg1 = (uint32_t)((Arg1) | (0x18000ULL));
        *(uint32_t *)(result + 0x50) = Arg1;
    }
    *(uint64_t *)(result + 0x4B0 + 0x8) = result + 1200;
    *(uint64_t *)(result + 0x4B0) = result + 1200;
    result = IopLiveDumpInitRegistrySettings(0, (uint32_t)(0x4C8ULL), (uint32_t)(0x706D644CULL), Arg4);
    if ((*(uint8_t *)(v_rip + 0x929E35)) == 0) goto loc_004E0C89;
    if (((*(uint32_t *)(result + 0x50)) & (512)) == 0) goto loc_004E0B9F;
    if ((*(uint64_t *)(result + 0x478)) == 0) goto loc_004E0C89;
loc_004E0B9F:
    result = EtwActivityIdControl(5, result + 952, (uint32_t)(0x706D644CULL), Arg4);
    result = EtwActivityIdControl(1, result + 968, (uint32_t)(0x706D644CULL), Arg4);
    if ((*(uint32_t *)(v_rip + 0x9262D5)) <= 5) goto loc_004E0C32;
    result = tlgKeywordOn(v_rip + 9593538, result + 968, (uint32_t)(0x706D644CULL), Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m1D8;
        v_stack_m168 = result;
        Arg3 = result + 968;
        result = v_stack_m188;
        v_stack_m1D8 = 0x1000000ULL;
        v_stack_m200 = result;
        Arg2 = v_rip - 4828014;
        Arg4 = result + 952;
        v_stack_m208 = 3;
        Arg1 = v_rip + 9593466;
        v_stack_m160 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    result = IopLiveDumpValidateParameters(result, local_r15 + 24, Arg3, Arg4);
    if (sign_flag) goto loc_004E0C91;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x28)))) & (4)) != 0) {
    }
    *(uint64_t *)(result + 0x4B0 + 0x8) = result + 1200;
    *(uint64_t *)(result + 0x4B0) = result + 1200;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x28)))) & (8)) == 0) goto loc_004E0C67;
    if (Arg7 == 0) goto loc_004E0C8C;
loc_004E0C67:
    result = IopLiveDumpOpenVMMemoryPartition(result, local_r15 + 24, Arg3, Arg4);
    result = IopLiveDumpAllocAndInitResources(result, local_r15 + 24, Arg3, Arg4);
    if (sign_flag) goto loc_004E0C91;
    result = IopLiveDumpCaptureMemoryPages(result, local_r15 + 24, Arg3, Arg4);
    goto loc_004E0C91;
loc_004E0C89:
loc_004E0C8C:
loc_004E0C91:
loc_004E0C9B:
    if (*(uint64_t *)(v_rip + 0x9854D6) == 0) goto loc_004E0CC6;
    Arg1 = 0;
    result = guard_dispatch_icall(Arg1, local_r15 + 24, Arg3, Arg4);
    result = ExReleaseRundownProtection(local_r13 + 88, local_r15 + 24, Arg3, Arg4);
    local_r13 = 0;
    *(uint64_t *)(v_rip + 0x9854B4) = 0;
    goto loc_004E0CC9;
loc_004E0CC6:
    local_r13 = 0;
loc_004E0CC9:
    if (v_stack_m1D0 != 0) {
        Arg1 = v_stack_m1D0;
        result = ZwClose(Arg1, local_r15 + 24, Arg3, Arg4);
    }
    if (v_stack_m1F0 != 0) {
        Arg1 = v_stack_m1F0;
        result = ZwClose(Arg1, local_r15 + 24, Arg3, Arg4);
    }
    result = v_stack_m1E8;
    if (v_stack_m1E8 != 0) {
        Arg1 = v_stack_m1E8;
        result = ZwClose(Arg1, local_r15 + 24, Arg3, Arg4);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0)))) & (16)) == 0) goto loc_004E0D19;
    if (((uint32_t)((uint32_t)(0xC000000DULL))) != 0xC0000240ULL) goto loc_004E0D19;
    result = IopLiveDumpIsTracingEnabled(Arg1, local_r15 + 24, Arg3, Arg4);
    if (((uint8_t)(result)) == 1) {
        Arg1 = v_rip - 4978868;
        result = IopLiveDumpTraceNoArgs(Arg1, local_r15 + 24, Arg3, Arg4);
    }
    if (v_stack_m1F8 != 0) {
        Arg1 = v_rip + 11191161;
        *(uint64_t *)(v_rip + 0x98545A) = 0;
        result = ExReleaseResourceLite(Arg1, local_r15 + 24, Arg3, Arg4);
    }
    result = KeLeaveCriticalRegion(Arg1, local_r15 + 24, Arg3, Arg4);
    if (sign_flag) goto loc_004E0EC2;
    result = SecureDump_GetSecureDumpSettings(result + 984, local_r15 + 24, Arg3, Arg4);
    if (sign_flag) goto loc_004E0EC2;
    if ((*(uint8_t *)(result + 0x3D8)) == 0) goto loc_004E0D8B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x3E0))) == 0) goto loc_004E0D81;
    if ((*(uint8_t *)(result + 0x3D9)) == 0) goto loc_004E0D81;
    if ((*(uint32_t *)(result + 0x3DC)) != 0x1000ULL) goto loc_004E0D81;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x3E0)))) & (0xFFFULL)) == 0) goto loc_004E0D8B;
loc_004E0D81:
    goto loc_004E0EC2;
loc_004E0D8B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x28)))) & (8)) != 0) goto loc_004E0EB9;
    result = IopLiveDumpTraceNoArgs(v_rip - 4979165, local_r15 + 24, Arg3, Arg4);
    Arg1 = 0;
    result = IopLiveDumpGetMillisecondCounter(Arg1, local_r15 + 24, Arg3, Arg4);
    if ((*(uint64_t *)(result + 0xC0)) != 0) goto loc_004E0DC8;
    if ((*(uint64_t *)(result + 0xC8)) != 0) goto loc_004E0DC8;
    result = IopLiveDumpWriteDumpFile(result, local_r15 + 24, Arg3, Arg4);
    goto loc_004E0DD0;
loc_004E0DC8:
    result = IopLiveDumpWriteDumpFileWithExtraPages(result, local_r15 + 24, Arg3, Arg4);
loc_004E0DD0:
    Arg1 = 0;
    result = IopLiveDumpGetMillisecondCounter(Arg1, local_r15 + 24, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x9260C0)) <= 5) goto loc_004E0E93;
    result = tlgKeywordOn(v_rip + 9592998, local_r15 + 24, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m1D8;
        v_stack_m1D8 = 0x1000000ULL;
        v_stack_m168 = result;
        Arg4 = result + 952;
        result = *(uint64_t *)(result + 0x230);
        Arg3 = result + 968;
        Arg2 = v_rip - 4828246;
        v_stack_m160 = 8;
        v_stack_m150 = 8;
        v_stack_m140 = 8;
        Arg1 = *(uint64_t *)(result + 0xFA0);
        result = v_stack_m1E8;
        v_stack_m158 = result;
        result = result;
        result = (result) - (result);
        v_stack_m1E8 = Arg1;
        v_stack_m1E0 = result;
        Arg1 = v_rip + 9592876;
        result = v_stack_m1E0;
        v_stack_m148 = result;
        result = v_stack_m188;
        v_stack_m200 = result;
        v_stack_m208 = 5;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsi = (result) - (result);
    Arg3 = 0;
    result = IopLiveDumpTraceDumpFileWriteEnd(result, local_rsi, Arg3, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (sign_flag) goto loc_004E0EC2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x50)))) & (2)) == 0) goto loc_004E0EC2;
    goto loc_004E0EC2;
loc_004E0EB9:
    *(uint64_t *)(Arg7) = result;
loc_004E0EC2:
    Arg1 = 0;
    result = IopLiveDumpGetMillisecondCounter(Arg1, local_rsi, Arg3, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    Arg2 = 0;
    result = IopLiveDumpTraceInterfaceEnd(result, Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC0000016ULL))), result);
    if ((*(uint32_t *)(v_rip + 0x925FBD)) <= 5) goto loc_004E1098;
    result = tlgKeywordOn(v_rip + 9592742, Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC0000016ULL))), result);
    if ((uint8_t)(result) == 0) goto loc_004E1098;
    v_stack_m118 = v_stack_m1D8;
    v_stack_m1D8 = 0x1000000ULL;
    v_stack_m108 = v_stack_m1D0;
    v_stack_m1E8 = (uint32_t)(v_stack_m1C8);
    v_stack_mF8 = v_stack_m1E8;
    v_stack_m1C0 = v_stack_m1C0;
    v_stack_mE8 = v_stack_m1C0;
    v_stack_m1B8 = v_stack_m1B8;
    v_stack_mD8 = v_stack_m1B8;
    v_stack_m1B0 = v_stack_m1B0;
    v_stack_mC8 = v_stack_m1B0;
    v_stack_m1E0 = Arg5;
    v_stack_mB8 = v_stack_m1E0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0))))) >> (3));
    result = (uint8_t)((result) & (1));
    v_stack_m110 = 8;
    v_stack_m1F8 = (uint8_t)(result);
    v_stack_mA8 = v_stack_m1F8;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0))))) >> (4));
    result = (uint8_t)((result) & (1));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1E0))) >> (5));
    v_stack_m1F7 = (uint8_t)(result);
    Arg1 = (uint8_t)((Arg1) & (1));
    v_stack_m1D0 = (uint32_t)((uint32_t)(0xC0000016ULL));
    v_stack_m98 = v_stack_m1F7;
    v_stack_m88 = v_stack_m1F6;
    v_stack_m78 = v_stack_m1F0;
    v_stack_m1F5 = (uint8_t)(*(uint8_t *)(v_rip + 0x98519A));
    v_stack_m68 = v_stack_m1F5;
    v_stack_m100 = 4;
    v_stack_mF0 = 8;
    v_stack_mE0 = 8;
    v_stack_mD0 = 8;
    v_stack_mC0 = 8;
    v_stack_mB0 = 8;
    v_stack_mA0 = 1;
    v_stack_m90 = 1;
    v_stack_m1F6 = (uint8_t)(Arg1);
    v_stack_m80 = 1;
    v_stack_m1F0 = result;
    v_stack_m70 = 8;
    v_stack_m60 = 1;
    if (result == 0) goto loc_004E106C;
    goto loc_004E1074;
loc_004E106C:
loc_004E1074:
    v_stack_m200 = v_stack_m138;
    v_stack_m208 = 14;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 9592341, v_rip - 4829099, v_stack_m198, v_stack_m198);
loc_004E1098:
    if (result == 0) goto loc_004E10D2;
    result = (uint32_t)(*(uint32_t *)(result + 0x28));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x28)))) & (8)) == 0) {
        Arg2 = result + 952;
        Arg1 = 2;
        result = EtwActivityIdControl(Arg1, Arg2, v_stack_m198, v_stack_m198);
    }
    if (((uint32_t)((uint32_t)(0xC0000016ULL))) != 0xC0000016ULL) {
        Arg1 = result;
        result = IopLiveDumpReleaseResources(Arg1, Arg2, v_stack_m198, v_stack_m198);
        Arg2 = 0x706D644CULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m198, v_stack_m198);
    }
    goto loc_004E10E4;
loc_004E10D6:
    if (Arg7 != 0) {
        *(uint64_t *)(Arg7) = result;
    }
loc_004E10E4:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m198, v_stack_m198);
    local_rsp = (local_rsp) + (488);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `32` | `R` |
| `Arg6` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004E085C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
