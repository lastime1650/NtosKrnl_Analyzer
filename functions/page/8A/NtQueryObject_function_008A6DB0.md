# NtQueryObject

- RVA: `0x008A6DB0`–`0x008A757C` (길이 `1,996` bytes)
- VA: `0x00000001408A6DB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007F198`
- 디코드: `442`개 명령, `1,996/1,996` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008A6EBD` → [ExRaiseAccessViolation](../8E/ExRaiseAccessViolation_function_008E9240.md) (function, `0x008E9240`)
- `0x008A6EC3` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008A6F57` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x008A6FE7` → [ObQueryNameStringMode](ObQueryNameStringMode_function_008A7ED0.md) (function, `0x008A7ED0`)
- `0x008A7015` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008A7057` → [ObQueryTypeInfo](ObQueryTypeInfo_function_008A8CAC.md) (function, `0x008A8CAC`)
- `0x008A70C8` → [OBJECT_HEADER_TO_QUOTA_INFO](../../text/40/OBJECT_HEADER_TO_QUOTA_INFO_function_0040EA80.md) (function, `0x0040EA80`)
- `0x008A711D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008A713E` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008A7188` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008A7191` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008A719F` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008A7278` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008A7291` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008A729F` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008A72F1` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008A7317` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008A7373` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008A7387` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008A7391` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008A739F` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008A73A7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008A73B4` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008A73C2` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008A73D4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008A74C5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008A7524` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008A7533` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008A7544` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008A7556` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [IopLoadDriver](../99/IopLoadDriver_function_00997B54.md) at `0x009981F2`
- [IopQueryRegistryKeySystemPath](../99/IopQueryRegistryKeySystemPath_function_0099A1CC.md) at `0x0099A2AC`

### Static image references
- `0x008A6F9D` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x008A6FA7` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x008A70E9` → RVA `0x00F0F658` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **25**
  - `0x008A7015` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008A70C8` → [OBJECT_HEADER_TO_QUOTA_INFO](../../text/40/OBJECT_HEADER_TO_QUOTA_INFO_function_0040EA80.md) (`PAGE` → `.text`)
  - `0x008A711D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008A713E` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008A7188` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008A7191` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008A719F` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008A7278` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008A7291` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008A729F` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008A72F1` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008A7317` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008A7373` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008A7387` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008A7391` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008A739F` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008A73A7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008A73B4` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008A73C2` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008A73D4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008A74C5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008A7524` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008A7533` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008A7544` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008A7556` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008A71C8` → [sub_00B19DBE](../B1/Unknown_function_00B19DBE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008A6DB0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008A6DB5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
008A6DBA  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
008A6DBF  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
008A6DC4  57                              push rdi
008A6DC5  41 54                           push r12
008A6DC7  41 55                           push r13
008A6DC9  41 56                           push r14
008A6DCB  41 57                           push r15
008A6DCD  48 81 EC 30 01 00 00            sub rsp, 0x130
008A6DD4  45 8B D9                        mov r11d, r9d
008A6DD7  4D 8B F0                        mov r14, r8
008A6DDA  44 8B FA                        mov r15d, edx
008A6DDD  4C 8B D1                        mov r10, rcx
008A6DE0  4C 8B AC 24 80 01 00 00         mov r13, qword ptr [rsp + 0x180]
008A6DE8  33 DB                           xor ebx, ebx
008A6DEA  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
008A6DF2  0F 57 C0                        xorps xmm0, xmm0
008A6DF5  33 C0                           xor eax, eax
008A6DF7  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
008A6DFF  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
008A6E07  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
008A6E0F  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
008A6E17  89 9C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ebx
008A6E1E  89 5C 24 7C                     mov dword ptr [rsp + 0x7c], ebx
008A6E22  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
008A6E26  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008A6E2F  44 0F B6 A0 32 02 00 00         movzx r12d, byte ptr [rax + 0x232]
008A6E37  44 88 64 24 5A                  mov byte ptr [rsp + 0x5a], r12b
008A6E3C  45 84 E4                        test r12b, r12b
008A6E3F  0F 84 DA 00 00 00               je 0x1408a6f1f
008A6E45  41 8B D3                        mov edx, r11d
008A6E48  41 83 FF 04                     cmp r15d, 4
008A6E4C  74 7B                           je 0x1408a6ec9
008A6E4E  45 85 C9                        test r9d, r9d
008A6E51  74 4B                           je 0x1408a6e9e
008A6E53  49 8B C8                        mov rcx, r8
008A6E56  41 F6 C6 03                     test r14b, 3
008A6E5A  75 67                           jne 0x1408a6ec3
008A6E5C  48 FF CA                        dec rdx
008A6E5F  49 03 D0                        add rdx, r8
008A6E62  4C 3B C2                        cmp r8, rdx
008A6E65  77 56                           ja 0x1408a6ebd
008A6E67  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
008A6E71  49 3B D0                        cmp rdx, r8
008A6E74  73 47                           jae 0x1408a6ebd
008A6E76  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
008A6E7D  48 81 C2 00 10 00 00            add rdx, 0x1000
008A6E84  0F B6 01                        movzx eax, byte ptr [rcx]
008A6E87  88 01                           mov byte ptr [rcx], al
008A6E89  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
008A6E90  48 81 C1 00 10 00 00            add rcx, 0x1000
008A6E97  48 3B CA                        cmp rcx, rdx
008A6E9A  75 E8                           jne 0x1408a6e84
008A6E9C  EB 0B                           jmp 0x1408a6ea9
008A6E9E  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
008A6EA8  90                              nop
008A6EA9  4D 85 ED                        test r13, r13
008A6EAC  74 6A                           je 0x1408a6f18
008A6EAE  4D 3B E8                        cmp r13, r8
008A6EB1  4D 0F 42 C5                     cmovb r8, r13
008A6EB5  41 8B 00                        mov eax, dword ptr [r8]
008A6EB8  41 89 00                        mov dword ptr [r8], eax
008A6EBB  EB 5B                           jmp 0x1408a6f18
008A6EBD  E8 7E 23 04 00                  call 0x1408e9240
008A6EC2  CC                              int3
008A6EC3  E8 08 31 FF FF                  call 0x140899fd0
008A6EC8  CC                              int3
008A6EC9  45 85 C9                        test r9d, r9d
008A6ECC  74 D0                           je 0x1408a6e9e
008A6ECE  49 8B C6                        mov rax, r14
008A6ED1  48 FF CA                        dec rdx
008A6ED4  49 03 D6                        add rdx, r14
008A6ED7  4C 3B F2                        cmp r14, rdx
008A6EDA  77 E1                           ja 0x1408a6ebd
008A6EDC  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
008A6EE6  49 3B D0                        cmp rdx, r8
008A6EE9  73 D2                           jae 0x1408a6ebd
008A6EEB  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
008A6EF2  48 81 C2 00 10 00 00            add rdx, 0x1000
008A6EF9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
008A6F00  0F B6 08                        movzx ecx, byte ptr [rax]
008A6F03  88 08                           mov byte ptr [rax], cl
008A6F05  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
008A6F0B  48 05 00 10 00 00               add rax, 0x1000
008A6F11  48 3B C2                        cmp rax, rdx
008A6F14  75 EA                           jne 0x1408a6f00
008A6F16  EB 91                           jmp 0x1408a6ea9
008A6F18  EB 05                           jmp 0x1408a6f1f
008A6F1A  E9 FD 00 00 00                  jmp 0x1408a701c
008A6F1F  41 83 FF 03                     cmp r15d, 3
008A6F23  0F 84 09 03 00 00               je 0x1408a7232
008A6F29  48 89 9C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rbx
008A6F31  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
008A6F39  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008A6F3E  48 8D 84 24 F8 00 00 00         lea rax, [rsp + 0xf8]
008A6F46  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008A6F4B  45 0F B6 CC                     movzx r9d, r12b
008A6F4F  45 33 C0                        xor r8d, r8d
008A6F52  33 D2                           xor edx, edx
008A6F54  49 8B CA                        mov rcx, r10
008A6F57  E8 54 1E FC FF                  call 0x140868db0
008A6F5C  8B F8                           mov edi, eax
008A6F5E  48 8B B4 24 F8 00 00 00         mov rsi, qword ptr [rsp + 0xf8]
008A6F66  48 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], rsi
008A6F6E  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008A6F72  85 C0                           test eax, eax
008A6F74  0F 88 A2 00 00 00               js 0x1408a701c
008A6F7A  44 8B 8C 24 94 00 00 00         mov r9d, dword ptr [rsp + 0x94]
008A6F82  44 89 4C 24 78                  mov dword ptr [rsp + 0x78], r9d
008A6F87  4C 8D 46 D0                     lea r8, [rsi - 0x30]
008A6F8B  49 8B C0                        mov rax, r8
008A6F8E  48 C1 E8 08                     shr rax, 8
008A6F92  0F B6 C8                        movzx ecx, al
008A6F95  41 0F B6 40 18                  movzx eax, byte ptr [r8 + 0x18]
008A6F9A  48 33 C8                        xor rcx, rax
008A6F9D  0F B6 05 A8 FE 71 00            movzx eax, byte ptr [rip + 0x71fea8]
008A6FA4  48 33 C8                        xor rcx, rax
008A6FA7  48 8D 15 52 90 75 FF            lea rdx, [rip - 0x8a6fae]
008A6FAE  4C 8B 94 CA 00 78 FC 00         mov r10, qword ptr [rdx + rcx*8 + 0xfc7800]
008A6FB6  4C 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], r10
008A6FBE  44 8B 9C 24 78 01 00 00         mov r11d, dword ptr [rsp + 0x178]
008A6FC6  4C 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r8
008A6FCE  41 83 FF 01                     cmp r15d, 1
008A6FD2  75 66                           jne 0x1408a703a
008A6FD4  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
008A6FD9  4C 8D 4C 24 54                  lea r9, [rsp + 0x54]
008A6FDE  45 8B C3                        mov r8d, r11d
008A6FE1  49 8B D6                        mov rdx, r14
008A6FE4  48 8B CE                        mov rcx, rsi
008A6FE7  E8 E4 0E 00 00                  call 0x1408a7ed0
008A6FEC  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008A6FF0  8B F8                           mov edi, eax
008A6FF2  4D 85 ED                        test r13, r13
008A6FF5  74 08                           je 0x1408a6fff
008A6FF7  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
008A6FFB  41 89 45 00                     mov dword ptr [r13], eax
008A6FFF  EB 0C                           jmp 0x1408a700d
008A7001  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
008A7009  8B 7C 24 50                     mov edi, dword ptr [rsp + 0x50]
008A700D  48 85 F6                        test rsi, rsi
008A7010  74 08                           je 0x1408a701a
008A7012  48 8B CE                        mov rcx, rsi
008A7015  E8 36 23 A5 FF                  call 0x1402f9350
008A701A  8B C7                           mov eax, edi
008A701C  4C 8D 9C 24 30 01 00 00         lea r11, [rsp + 0x130]
008A7024  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
008A7028  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
008A702C  49 8B E3                        mov rsp, r11
008A702F  41 5F                           pop r15
008A7031  41 5E                           pop r14
008A7033  41 5D                           pop r13
008A7035  41 5C                           pop r12
008A7037  5F                              pop rdi
008A7038  C3                              ret
008A7039  CC                              int3
008A703A  45 85 FF                        test r15d, r15d
008A703D  74 1F                           je 0x1408a705e
008A703F  41 83 EF 02                     sub r15d, 2
008A7043  0F 85 7B 01 00 00               jne 0x1408a71c4
008A7049  4C 8D 4C 24 54                  lea r9, [rsp + 0x54]
008A704E  45 8B C3                        mov r8d, r11d
008A7051  49 8B D6                        mov rdx, r14
008A7054  49 8B CA                        mov rcx, r10
008A7057  E8 50 1C 00 00                  call 0x1408a8cac
008A705C  EB 8E                           jmp 0x1408a6fec
008A705E  41 83 FB 38                     cmp r11d, 0x38
008A7062  0F 85 EB 04 00 00               jne 0x1408a7553
008A7068  0F 57 C0                        xorps xmm0, xmm0
008A706B  F3 0F 7F 84 24 D8 00 00 00      movdqu xmmword ptr [rsp + 0xd8], xmm0
008A7074  48 89 9C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rbx
008A707C  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
008A7084  89 84 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], eax
008A708B  41 0F B6 48 1B                  movzx ecx, byte ptr [r8 + 0x1b]
008A7090  F6 C1 10                        test cl, 0x10
008A7093  74 0A                           je 0x1408a709f
008A7095  83 C8 10                        or eax, 0x10
008A7098  89 84 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], eax
008A709F  F6 C1 08                        test cl, 8
008A70A2  0F 85 BD 04 00 00               jne 0x1408a7565
008A70A8  44 89 8C 24 C4 00 00 00         mov dword ptr [rsp + 0xc4], r9d
008A70B0  41 8B 40 08                     mov eax, dword ptr [r8 + 8]
008A70B4  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
008A70BB  41 8B 00                        mov eax, dword ptr [r8]
008A70BE  89 84 24 CC 00 00 00            mov dword ptr [rsp + 0xcc], eax
008A70C5  49 8B C8                        mov rcx, r8
008A70C8  E8 B3 79 B6 FF                  call 0x14040ea80
008A70CD  48 85 C0                        test rax, rax
008A70D0  0F 84 F9 03 00 00               je 0x1408a74cf
008A70D6  8B 08                           mov ecx, dword ptr [rax]
008A70D8  89 8C 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], ecx
008A70DF  8B 40 04                        mov eax, dword ptr [rax + 4]
008A70E2  89 84 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], eax
008A70E9  4C 3B 15 68 85 66 00            cmp r10, qword ptr [rip + 0x668568]
008A70F0  0F 84 7E 04 00 00               je 0x1408a7574
008A70F6  33 C0                           xor eax, eax
008A70F8  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
008A7100  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008A7109  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008A7110  90                              nop
008A7111  4D 8D 78 10                     lea r15, [r8 + 0x10]
008A7115  45 33 C0                        xor r8d, r8d
008A7118  33 D2                           xor edx, edx
008A711A  49 8B CF                        mov rcx, r15
008A711D  E8 0E 91 96 FF                  call 0x140210230
008A7122  48 8B F8                        mov rdi, rax
008A7125  BA 11 00 00 00                  mov edx, 0x11
008A712A  33 C0                           xor eax, eax
008A712C  F0 49 0F B1 17                  lock cmpxchg qword ptr [r15], rdx
008A7131  74 15                           je 0x1408a7148
008A7133  4D 8B CF                        mov r9, r15
008A7136  4C 8B C7                        mov r8, rdi
008A7139  33 D2                           xor edx, edx
008A713B  49 8B CF                        mov rcx, r15
008A713E  E8 09 93 96 FF                  call 0x14021044c
008A7143  BA 11 00 00 00                  mov edx, 0x11
008A7148  48 85 FF                        test rdi, rdi
008A714B  74 04                           je 0x1408a7151
008A714D  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
008A7151  48 8B BC 24 A0 00 00 00         mov rdi, qword ptr [rsp + 0xa0]
008A7159  0F B6 47 1A                     movzx eax, byte ptr [rdi + 0x1a]
008A715D  4C 8D 3D 9C 8E 75 FF            lea r15, [rip - 0x8a7164]
008A7164  A8 02                           test al, 2
008A7166  75 43                           jne 0x1408a71ab
008A7168  48 8B CB                        mov rcx, rbx
008A716B  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
008A7170  48 85 C9                        test rcx, rcx
008A7173  0F 85 EB 00 00 00               jne 0x1408a7264
008A7179  48 8B C2                        mov rax, rdx
008A717C  F0 48 0F B1 5F 10               lock cmpxchg qword ptr [rdi + 0x10], rbx
008A7182  74 09                           je 0x1408a718d
008A7184  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008A7188  E8 B3 C2 9B FF                  call 0x140263440
008A718D  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008A7191  E8 6A A4 A3 FF                  call 0x1402e1600
008A7196  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A719F  E8 4C 7E 9B FF                  call 0x14025eff0
008A71A4  8B C3                           mov eax, ebx
008A71A6  E9 35 02 00 00                  jmp 0x1408a73e0
008A71AB  83 E0 03                        and eax, 3
008A71AE  42 0F B6 84 38 80 FF F0 00      movzx eax, byte ptr [rax + r15 + 0xf0ff80]
008A71B7  48 8B CF                        mov rcx, rdi
008A71BA  48 2B C8                        sub rcx, rax
008A71BD  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
008A71C2  EB AC                           jmp 0x1408a7170
008A71C4  41 83 EF 01                     sub r15d, 1
008A71C8  0F 84 F0 2B 27 00               je 0x140b19dbe
008A71CE  41 83 FF 01                     cmp r15d, 1
008A71D2  0F 85 69 03 00 00               jne 0x1408a7541
008A71D8  C7 44 24 54 02 00 00 00         mov dword ptr [rsp + 0x54], 2
008A71E0  41 83 FB 02                     cmp r11d, 2
008A71E4  72 23                           jb 0x1408a7209
008A71E6  41 C6 06 00                     mov byte ptr [r14], 0
008A71EA  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
008A71F2  A8 02                           test al, 2
008A71F4  74 03                           je 0x1408a71f9
008A71F6  45 88 3E                        mov byte ptr [r14], r15b
008A71F9  41 C6 46 01 00                  mov byte ptr [r14 + 1], 0
008A71FE  A8 01                           test al, 1
008A7200  74 10                           je 0x1408a7212
008A7202  41 C6 46 01 01                  mov byte ptr [r14 + 1], 1
008A7207  EB 09                           jmp 0x1408a7212
008A7209  BF 04 00 00 C0                  mov edi, 0xc0000004
008A720E  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
008A7212  E9 DB FD FF FF                  jmp 0x1408a6ff2
008A7217  8B F8                           mov edi, eax
008A7219  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008A721D  4C 8B AC 24 80 01 00 00         mov r13, qword ptr [rsp + 0x180]
008A7225  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
008A722D  E9 C0 FD FF FF                  jmp 0x1408a6ff2
008A7232  44 8B CB                        mov r9d, ebx
008A7235  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
008A7239  48 8B F3                        mov rsi, rbx
008A723C  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
008A7244  4C 8B C3                        mov r8, rbx
008A7247  4C 8B D3                        mov r10, rbx
008A724A  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
008A7252  8B FB                           mov edi, ebx
008A7254  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
008A7258  48 8D 15 A1 8D 75 FF            lea rdx, [rip - 0x8a725f]
008A725F  E9 62 FD FF FF                  jmp 0x1408a6fc6
008A7264  48 8B 09                        mov rcx, qword ptr [rcx]
008A7267  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
008A726F  48 85 C9                        test rcx, rcx
008A7272  0F 84 01 FF FF FF               je 0x1408a7179
008A7278  E8 A3 87 96 FF                  call 0x14020fa20
008A727D  B8 11 00 00 00                  mov eax, 0x11
008A7282  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008A7286  F0 48 0F B1 19                  lock cmpxchg qword ptr [rcx], rbx
008A728B  0F 85 A2 02 00 00               jne 0x1408a7533
008A7291  E8 6A A3 A3 FF                  call 0x1402e1600
008A7296  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A729F  E8 4C 7D 9B FF                  call 0x14025eff0
008A72A4  48 8B BC 24 A8 00 00 00         mov rdi, qword ptr [rsp + 0xa8]
008A72AC  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008A72B1  44 0F B7 68 08                  movzx r13d, word ptr [rax + 8]
008A72B6  41 83 C5 02                     add r13d, 2
008A72BA  41 BC 11 00 00 00               mov r12d, 0x11
008A72C0  4C 8B F7                        mov r14, rdi
008A72C3  48 8D 4F D0                     lea rcx, [rdi - 0x30]
008A72C7  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
008A72CF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008A72D8  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008A72DF  90                              nop
008A72E0  48 8D 41 10                     lea rax, [rcx + 0x10]
008A72E4  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008A72E9  45 33 C0                        xor r8d, r8d
008A72EC  33 D2                           xor edx, edx
008A72EE  48 8B C8                        mov rcx, rax
008A72F1  E8 3A 8F 96 FF                  call 0x140210230
008A72F6  48 8B C8                        mov rcx, rax
008A72F9  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008A72FE  33 C0                           xor eax, eax
008A7300  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
008A7305  F0 4D 0F B1 22                  lock cmpxchg qword ptr [r10], r12
008A730A  74 1A                           je 0x1408a7326
008A730C  4D 8B CA                        mov r9, r10
008A730F  4C 8B C1                        mov r8, rcx
008A7312  33 D2                           xor edx, edx
008A7314  49 8B CA                        mov rcx, r10
008A7317  E8 30 91 96 FF                  call 0x14021044c
008A731C  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008A7321  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
008A7326  48 85 C9                        test rcx, rcx
008A7329  74 04                           je 0x1408a732f
008A732B  C6 41 0A 01                     mov byte ptr [rcx + 0xa], 1
008A732F  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
008A7337  0F B6 41 1A                     movzx eax, byte ptr [rcx + 0x1a]
008A733B  A8 02                           test al, 2
008A733D  0F 85 99 01 00 00               jne 0x1408a74dc
008A7343  48 8B CB                        mov rcx, rbx
008A7346  48 85 C9                        test rcx, rcx
008A7349  0F 84 A1 01 00 00               je 0x1408a74f0
008A734F  48 8B 11                        mov rdx, qword ptr [rcx]
008A7352  48 85 D2                        test rdx, rdx
008A7355  0F 84 95 01 00 00               je 0x1408a74f0
008A735B  0F B7 41 08                     movzx eax, word ptr [rcx + 8]
008A735F  83 C0 02                        add eax, 2
008A7362  44 03 E8                        add r13d, eax
008A7365  48 8B FA                        mov rdi, rdx
008A7368  48 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdx
008A7370  48 8B CA                        mov rcx, rdx
008A7373  E8 A8 86 96 FF                  call 0x14020fa20
008A7378  49 8B C4                        mov rax, r12
008A737B  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008A7380  F0 48 0F B1 19                  lock cmpxchg qword ptr [rcx], rbx
008A7385  74 0A                           je 0x1408a7391
008A7387  E8 B4 C0 9B FF                  call 0x140263440
008A738C  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008A7391  E8 6A A2 A3 FF                  call 0x1402e1600
008A7396  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A739F  E8 4C 7C 9B FF                  call 0x14025eff0
008A73A4  49 8B CE                        mov rcx, r14
008A73A7  E8 A4 1F A5 FF                  call 0x1402f9350
008A73AC  E9 0F FF FF FF                  jmp 0x1408a72c0
008A73B1  49 8B CA                        mov rcx, r10
008A73B4  E8 47 A2 A3 FF                  call 0x1402e1600
008A73B9  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008A73C2  E8 29 7C 9B FF                  call 0x14025eff0
008A73C7  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
008A73CF  48 85 C9                        test rcx, rcx
008A73D2  74 05                           je 0x1408a73d9
008A73D4  E8 77 1F A5 FF                  call 0x1402f9350
008A73D9  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
008A73DD  83 C0 12                        add eax, 0x12
008A73E0  89 84 24 E4 00 00 00            mov dword ptr [rsp + 0xe4], eax
008A73E7  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
008A73EF  41 0F B7 40 10                  movzx eax, word ptr [r8 + 0x10]
008A73F4  83 C0 6A                        add eax, 0x6a
008A73F7  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
008A73FE  F7 44 24 78 00 00 02 00         test dword ptr [rsp + 0x78], 0x20000
008A7406  75 6D                           jne 0x1408a7475
008A7408  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
008A740F  89 84 24 EC 00 00 00            mov dword ptr [rsp + 0xec], eax
008A7416  0F 10 84 24 C0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xc0]
008A741E  41 0F 11 06                     movups xmmword ptr [r14], xmm0
008A7422  0F 10 8C 24 D0 00 00 00         movups xmm1, xmmword ptr [rsp + 0xd0]
008A742A  41 0F 11 4E 10                  movups xmmword ptr [r14 + 0x10], xmm1
008A742F  0F 10 84 24 E0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xe0]
008A7437  41 0F 11 46 20                  movups xmmword ptr [r14 + 0x20], xmm0
008A743C  F2 0F 10 8C 24 F0 00 00 00      movsd xmm1, qword ptr [rsp + 0xf0]
008A7445  F2 41 0F 11 4E 30               movsd qword ptr [r14 + 0x30], xmm1
008A744B  C7 44 24 54 38 00 00 00         mov dword ptr [rsp + 0x54], 0x38
008A7453  8B 7C 24 50                     mov edi, dword ptr [rsp + 0x50]
008A7457  E9 96 FB FF FF                  jmp 0x1408a6ff2
008A745C  4C 8B AC 24 80 01 00 00         mov r13, qword ptr [rsp + 0x180]
008A7464  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
008A746C  8B 7C 24 50                     mov edi, dword ptr [rsp + 0x50]
008A7470  E9 7D FB FF FF                  jmp 0x1408a6ff2
008A7475  48 83 C7 28                     add rdi, 0x28
008A7479  48 83 3F 00                     cmp qword ptr [rdi], 0
008A747D  74 89                           je 0x1408a7408
008A747F  C7 44 24 7C 0F 00 00 00         mov dword ptr [rsp + 0x7c], 0xf
008A7487  41 8B 50 64                     mov edx, dword ptr [r8 + 0x64]
008A748B  49 8D 48 4C                     lea rcx, [r8 + 0x4c]
008A748F  49 8B 80 98 00 00 00            mov rax, qword ptr [r8 + 0x98]
008A7496  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
008A749B  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
008A74A0  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
008A74A4  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
008A74A9  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
008A74B1  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008A74B6  45 33 C9                        xor r9d, r9d
008A74B9  4C 8D 44 24 7C                  lea r8, [rsp + 0x7c]
008A74BE  41 8D 51 01                     lea edx, [r9 + 1]
008A74C2  48 8B CE                        mov rcx, rsi
008A74C5  E8 06 36 E1 FF                  call 0x1406baad0
008A74CA  E9 39 FF FF FF                  jmp 0x1408a7408
008A74CF  48 89 9C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rbx
008A74D7  E9 0D FC FF FF                  jmp 0x1408a70e9
008A74DC  83 E0 03                        and eax, 3
008A74DF  42 0F B6 84 38 80 FF F0 00      movzx eax, byte ptr [rax + r15 + 0xf0ff80]
008A74E8  48 2B C8                        sub rcx, rax
008A74EB  E9 56 FE FF FF                  jmp 0x1408a7346
008A74F0  44 89 6C 24 70                  mov dword ptr [rsp + 0x70], r13d
008A74F5  49 8B C4                        mov rax, r12
008A74F8  F0 49 0F B1 1A                  lock cmpxchg qword ptr [r10], rbx
008A74FD  4C 8B B4 24 70 01 00 00         mov r14, qword ptr [rsp + 0x170]
008A7505  44 0F B6 64 24 5A               movzx r12d, byte ptr [rsp + 0x5a]
008A750B  4C 8B AC 24 80 01 00 00         mov r13, qword ptr [rsp + 0x180]
008A7513  48 8B BC 24 A0 00 00 00         mov rdi, qword ptr [rsp + 0xa0]
008A751B  0F 84 90 FE FF FF               je 0x1408a73b1
008A7521  49 8B CA                        mov rcx, r10
008A7524  E8 17 BF 9B FF                  call 0x140263440
008A7529  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
008A752E  E9 7E FE FF FF                  jmp 0x1408a73b1
008A7533  E8 08 BF 9B FF                  call 0x140263440
008A7538  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008A753C  E9 50 FD FF FF                  jmp 0x1408a7291
008A7541  48 8B CE                        mov rcx, rsi
008A7544  E8 07 1E A5 FF                  call 0x1402f9350
008A7549  B8 03 00 00 C0                  mov eax, 0xc0000003
008A754E  E9 C9 FA FF FF                  jmp 0x1408a701c
008A7553  48 8B CE                        mov rcx, rsi
008A7556  E8 F5 1D A5 FF                  call 0x1402f9350
008A755B  B8 04 00 00 C0                  mov eax, 0xc0000004
008A7560  E9 B7 FA FF FF                  jmp 0x1408a701c
008A7565  83 C8 20                        or eax, 0x20
008A7568  89 84 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], eax
008A756F  E9 34 FB FF FF                  jmp 0x1408a70a8
008A7574  48 8B 06                        mov rax, qword ptr [rsi]
008A7577  E9 7C FB FF FF                  jmp 0x1408a70f8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryObject(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int8 v_stack_mD6;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned __int8 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int8 v_stack_mFE;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (304);
    v_rbx = 0;
    v_stack_mC8 = 0;
    result = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = 0;
    v_stack_mD8 = 0;
    v_stack_mDC = 0;
    v_stack_m104 = 0;
    v_stack_mFE = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008A6F1F;
    if (((unsigned int)((unsigned int)(a2))) == 4) goto loc_008A6EC9;
    if (a4 == 0) goto loc_008A6E9E;
    if ((((unsigned __int8)(a3)) & (3)) != 0) goto loc_008A6EC3;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(a4)))) - 1;
    a2 = (a2) + (a3);
    if (a3 > a2) goto loc_008A6EBD;
    if (a2 >= a3) goto loc_008A6EBD;
    a2 = (a2) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a2) + (0x1000ULL);
loc_008A6E84:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    a1 = (a3) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) + (0x1000ULL);
    if (a1 != a2) goto loc_008A6E84;
    goto loc_008A6EA9;
loc_008A6E9E:
loc_008A6EA9:
    if (a5 == 0) goto loc_008A6F18;
    if (a5 < a3) { a3 = a5; }
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    goto loc_008A6F18;
loc_008A6EBD:
    result = ExRaiseAccessViolation(a1, a2, a3, a4);
loc_008A6EC3:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_008A6EC9:
    if (a4 == 0) goto loc_008A6E9E;
    a2 = (a2) - 1;
    a2 = (a2) + (a3);
    if (a3 > a2) goto loc_008A6EBD;
    if (a2 >= a3) goto loc_008A6EBD;
    a2 = (a2) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a2) + (0x1000ULL);
loc_008A6F00:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    result = (a3) & (0xFFFFFFFFFFFFF000ULL);
    result = (result) + (0x1000ULL);
    if (result != a2) goto loc_008A6F00;
    goto loc_008A6EA9;
loc_008A6F18:
    goto loc_008A6F1F;
loc_008A6F1F:
    if (((unsigned int)((unsigned int)(a2))) == 3) goto loc_008A7232;
    v_stack_m60 = 0;
    v_stack_m130 = v_stack_mC8;
    v_stack_m138 = v_stack_m60;
    a3 = 0;
    a2 = 0;
    result = ObReferenceObjectByHandle(a1, a2, a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_mD0 = v_stack_m60;
    v_stack_m108 = (unsigned int)(result);
    if (sign_flag) goto loc_008A701C;
    v_stack_mE0 = (unsigned int)((unsigned int)(v_stack_mC4));
    result = (v_stack_m60 - 48) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_m60 - 48 + 24));
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7470760));
    v_stack_mC0 = *(unsigned __int64 *)(v_rip - 9072558 + a1 * 8 + 16545792);
loc_008A6FC6:
    v_stack_mB8 = v_stack_m60 - 48;
    if (((unsigned int)((unsigned int)(a2))) != 1) goto loc_008A703A;
    v_stack_m138 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = ObQueryNameStringMode(v_stack_m60, 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), v_stack_m104);
loc_008A6FEC:
    v_stack_m108 = (unsigned int)(result);
loc_008A6FF2:
    if (a5 != 0) {
        result = v_stack_m104;
        *(unsigned int *)(a5) = (unsigned int)(result);
    }
    goto loc_008A700D;
loc_008A700D:
    if (v_stack_m60 != 0) {
        a1 = v_stack_m60;
        result = ObfDereferenceObject(a1, 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), v_stack_m104);
    }
loc_008A701C:
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_008A703A:
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_008A705E;
    v_r15 = (unsigned int)(((unsigned int)(a2)) - (2));
    if (condition_is_not_equal) goto loc_008A71C4;
    result = ObQueryTypeInfo(*(unsigned __int64 *)(v_rip - 9072558 + a1 * 8 + 16545792), 0, (unsigned int)((unsigned int)(v_stack_m28)), v_stack_mDC);
    goto loc_008A6FEC;
loc_008A705E:
    if (((unsigned int)(v_stack_m28)) != 56) goto loc_008A7553;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = *(unsigned __int64 *)(v_stack_m28 + 48);
    v_stack_m70 = (unsigned int)(v_stack_mA0);
    result = v_stack_mA0;
    if ((((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_stack_m28)) + 27))) & (16)) != 0) {
        result = (unsigned int)((v_stack_mA0) | (16));
        v_stack_m70 = (unsigned int)(result);
    }
    if ((((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_stack_m28)) + 27))) & (8)) != 0) goto loc_008A7565;
loc_008A70A8:
    v_stack_m6C = (unsigned int)(v_stack_mDC);
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_stack_m28)) + 8)));
    v_stack_m64 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_stack_m28)))));
    result = OBJECT_HEADER_TO_QUOTA_INFO((unsigned int)((unsigned int)(v_stack_m28)), 0, (unsigned int)((unsigned int)(v_stack_m28)), v_stack_mDC);
    if (result == 0) goto loc_008A74CF;
    v_stack_m60 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    v_stack_m5C = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
loc_008A70E9:
    if ((*(unsigned __int64 *)(v_rip - 9072558 + a1 * 8 + 16545792)) == (*(unsigned __int64 *)(v_rip + 6718824))) goto loc_008A7574;
    result = 0;
loc_008A70F8:
    v_stack_m40 = 0;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire((unsigned int)((unsigned int)(v_stack_m28)) + 16, a2, a3, v_stack_mDC);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = (unsigned int)((unsigned int)(v_stack_m28)) + 16;
        a3 = 0;
        a2 = 0;
        a1 = (unsigned int)((unsigned int)(v_stack_m28)) + 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a2 = 17;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m90 + 26))) & (2)) != 0) goto loc_008A71AB;
    v_stack_mD0 = *(unsigned __int64 *)(v_stack_m28 + 48);
loc_008A7170:
    if (*(unsigned __int64 *)(v_stack_m28 + 48) != 0) goto loc_008A7264;
loc_008A7179:
    result = a2;
    if (*(unsigned __int64 *)(v_stack_m28 + 48) != 0) {
        a1 = v_stack_m90 + 16;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_stack_m90 + 16, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    goto loc_008A73E0;
loc_008A71AB:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48)))) & (3));
    a1 = (v_stack_m90) - (*(unsigned __int8 *)(result + v_rip - 9072996 * 1 + 15794048));
    v_stack_mD0 = a1;
    goto loc_008A7170;
loc_008A71C4:
    v_r15 = (unsigned int)((v_rip - 9072996) - (1));
    if (((unsigned int)(v_r15)) != 1) goto loc_008A7541;
    v_stack_mDC = 2;
    if (((unsigned int)(v_stack_m28)) < 2) goto loc_008A7209;
    *(unsigned __int8 *)(a3) = 0;
    if ((((unsigned __int8)(v_stack_mA0)) & (2)) != 0) {
        *(unsigned __int8 *)(a3) = (unsigned __int8)(v_r15);
    }
    *(unsigned __int8 *)(a3 + 1) = 0;
    if ((((unsigned __int8)(v_stack_mA0)) & (1)) == 0) goto loc_008A7212;
    *(unsigned __int8 *)(a3 + 1) = 1;
    goto loc_008A7212;
loc_008A7209:
    v_stack_mE0 = (unsigned int)((unsigned int)(0xC0000004ULL));
loc_008A7212:
    goto loc_008A6FF2;
loc_008A7232:
    v_stack_mB8 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48));
    v_stack_mA8 = *(unsigned __int64 *)(v_stack_m28 + 48);
    v_stack_m98 = *(unsigned __int64 *)(v_stack_m28 + 48);
    v_stack_mE0 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48));
    goto loc_008A6FC6;
loc_008A7264:
    v_stack_m88 = *(unsigned __int64 *)(a1);
    if (*(unsigned __int64 *)(a1) == 0) goto loc_008A7179;
    result = ObfReferenceObject(*(unsigned __int64 *)(a1), v_rip - 9073247, *(unsigned __int64 *)(v_stack_m28 + 48), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))));
    if (*(unsigned __int64 *)(a1) != 0) goto loc_008A7533;
loc_008A7291:
    result = KeAbPostRelease((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))) + 16, v_rip - 9073247, *(unsigned __int64 *)(v_stack_m28 + 48), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), v_rip - 9073247, *(unsigned __int64 *)(v_stack_m28 + 48), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))));
    v_r13 = (unsigned int)((*(unsigned __int16 *)(v_stack_mD0 + 8)) + (2));
loc_008A72C0:
    v_stack_m80 = v_stack_m88 - 48;
    v_stack_mD0 = v_stack_m88 - 48 + 16;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m88 - 48 + 16, a2, a3, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))));
    v_stack_mC0 = result;
    result = 0;
    v_r10 = v_stack_mD0;
    if (!(condition_is_equal)) {
        a4 = v_stack_mD0;
        a3 = 0;
        a2 = 0;
        a1 = v_stack_mD0;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a1 = v_stack_mC0;
        v_r10 = v_stack_mD0;
    }
    if (a1 != 0) {
        *(unsigned __int8 *)(a1 + 10) = 1;
    }
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m80 + 26))) & (2)) != 0) goto loc_008A74DC;
loc_008A7346:
    if (*(unsigned __int64 *)(v_stack_m28 + 48) == 0) goto loc_008A74F0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48)) == 0) goto loc_008A74F0;
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 8)) + (2));
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)(result)));
    v_stack_m88 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48));
    result = ObfReferenceObject(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48)), a3, a4);
    result = 17;
    if (!(condition_is_equal)) {
        result = ExfReleasePushLockShared(v_stack_mD0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48)), a3, a4);
        a1 = v_stack_mD0;
    }
    result = KeAbPostRelease(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48)), a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48)), a3, a4);
    result = ObfDereferenceObject(v_stack_m88, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48)), a3, a4);
    goto loc_008A72C0;
loc_008A73B1:
    result = KeAbPostRelease(v_r10, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48)), a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48)), a3, a4);
    if (v_stack_m88 != 0) {
        result = ObfDereferenceObject(v_stack_m88, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48)), a3, a4);
    }
    result = (unsigned int)(((unsigned int)(v_stack_mC0)) + (18));
loc_008A73E0:
    v_stack_m4C = (unsigned int)(result);
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_m98 + 16)) + (106));
    v_stack_m48 = (unsigned int)(result);
    if (((v_stack_mB8) & (0x20000ULL)) != 0) goto loc_008A7475;
loc_008A7408:
    v_stack_m44 = (unsigned int)((unsigned int)(v_stack_mB0));
    *(unsigned __int64 *)(v_stack_m88) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m88 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m88 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m88 + 48) = v_xmm1;
    v_stack_mDC = 56;
    goto loc_008A6FF2;
loc_008A7475:
    v_rdi = ((unsigned int)(v_stack_mE0)) + (40);
    if ((*(unsigned __int64 *)(v_rdi)) == 0) goto loc_008A7408;
    v_stack_mB4 = 15;
    v_stack_mF0 = 17;
    v_stack_mF8 = v_stack_m98 + 76;
    v_stack_m100 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m98 + 100)));
    v_stack_m108 = v_rdi;
    v_stack_m110 = v_stack_mB0;
    a4 = 0;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_m28 + 48), a4 + 1, v_stack_mB4, a4);
    goto loc_008A7408;
loc_008A74CF:
    v_stack_m60 = *(unsigned __int64 *)(v_stack_m28 + 48);
    goto loc_008A70E9;
loc_008A74DC:
    result = (unsigned int)((result) & (3));
    a1 = (*(unsigned __int64 *)(v_stack_m28 + 48)) - (*(unsigned __int8 *)(result + v_r15 * 1 + 15794048));
    goto loc_008A7346;
loc_008A74F0:
    v_stack_mC0 = (unsigned int)(v_r13);
    if (condition_is_equal) goto loc_008A73B1;
    result = ExfReleasePushLockShared(v_r10, a4 + 1, v_stack_mB4, a4);
    goto loc_008A73B1;
loc_008A7533:
    result = ExfReleasePushLockShared(v_r10, a4 + 1, v_stack_mB4, a4);
    goto loc_008A7291;
loc_008A7541:
    result = ObfDereferenceObject(*(unsigned __int64 *)(v_stack_m28 + 48), a4 + 1, v_stack_mB4, a4);
    goto loc_008A701C;
loc_008A7553:
    result = ObfDereferenceObject(*(unsigned __int64 *)(v_stack_m28 + 48), a4 + 1, v_stack_mB4, a4);
    goto loc_008A701C;
loc_008A7565:
    result = (unsigned int)(((unsigned int)(0xC0000004ULL)) | (32));
    v_stack_m70 = (unsigned int)(result);
    goto loc_008A70A8;
loc_008A7574:
    goto loc_008A70F8;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryObject(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m28;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint8_t v_stack_mD6;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint8_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint8_t v_stack_mFE;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p40;
    uint64_t v_stack_p50;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (304);
    local_rbx = 0;
    v_stack_mC8 = 0;
    result = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = 0;
    v_stack_mD8 = 0;
    v_stack_mDC = 0;
    v_stack_m104 = 0;
    v_stack_mFE = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008A6F1F;
    if (((uint32_t)((uint32_t)(Arg2))) == 4) goto loc_008A6EC9;
    if (Arg4 == 0) goto loc_008A6E9E;
    if ((((uint8_t)(Arg3)) & (3)) != 0) goto loc_008A6EC3;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(Arg4)))) - 1;
    Arg2 = (Arg2) + (Arg3);
    if (Arg3 > Arg2) goto loc_008A6EBD;
    if (Arg2 >= Arg3) goto loc_008A6EBD;
    Arg2 = (Arg2) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (Arg2) + (0x1000ULL);
loc_008A6E84:
    *(uint8_t *)(Arg3) = (uint8_t)(*(uint8_t *)(Arg3));
    Arg1 = (Arg3) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) + (0x1000ULL);
    if (Arg1 != Arg2) goto loc_008A6E84;
    goto loc_008A6EA9;
loc_008A6E9E:
loc_008A6EA9:
    if (Arg5 == 0) goto loc_008A6F18;
    if (Arg5 < Arg3) { Arg3 = Arg5; }
    *(uint32_t *)(Arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3)));
    goto loc_008A6F18;
loc_008A6EBD:
    result = ExRaiseAccessViolation(Arg1, Arg2, Arg3, Arg4);
loc_008A6EC3:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_008A6EC9:
    if (Arg4 == 0) goto loc_008A6E9E;
    Arg2 = (Arg2) - 1;
    Arg2 = (Arg2) + (Arg3);
    if (Arg3 > Arg2) goto loc_008A6EBD;
    if (Arg2 >= Arg3) goto loc_008A6EBD;
    Arg2 = (Arg2) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (Arg2) + (0x1000ULL);
loc_008A6F00:
    *(uint8_t *)(Arg3) = (uint8_t)(*(uint8_t *)(Arg3));
    result = (Arg3) & (0xFFFFFFFFFFFFF000ULL);
    result = (result) + (0x1000ULL);
    if (result != Arg2) goto loc_008A6F00;
    goto loc_008A6EA9;
loc_008A6F18:
    goto loc_008A6F1F;
loc_008A6F1F:
    if (((uint32_t)((uint32_t)(Arg2))) == 3) goto loc_008A7232;
    v_stack_m60 = 0;
    v_stack_m130 = v_stack_mC8;
    v_stack_m138 = v_stack_m60;
    Arg3 = 0;
    Arg2 = 0;
    result = ObReferenceObjectByHandle(Arg1, Arg2, Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_mD0 = v_stack_m60;
    v_stack_m108 = (uint32_t)(result);
    if (sign_flag) goto loc_008A701C;
    v_stack_mE0 = (uint32_t)((uint32_t)(v_stack_mC4));
    result = (v_stack_m60 - 48) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_m60 - 0x30 + 0x18));
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x71FEA8));
    v_stack_mC0 = *(uint64_t *)(v_rip - 0x8A6FAE + Arg1 * 8 + 0xFC7800);
loc_008A6FC6:
    v_stack_mB8 = v_stack_m60 - 48;
    if (((uint32_t)((uint32_t)(Arg2))) != 1) goto loc_008A703A;
    v_stack_m138 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = ObQueryNameStringMode(v_stack_m60, 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), v_stack_m104);
loc_008A6FEC:
    v_stack_m108 = (uint32_t)(result);
loc_008A6FF2:
    if (Arg5 != 0) {
        result = v_stack_m104;
        *(uint32_t *)(Arg5) = (uint32_t)(result);
    }
    goto loc_008A700D;
loc_008A700D:
    if (v_stack_m60 != 0) {
        Arg1 = v_stack_m60;
        result = ObfDereferenceObject(Arg1, 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), v_stack_m104);
    }
loc_008A701C:
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_008A703A:
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_008A705E;
    local_r15 = (uint32_t)(((uint32_t)(Arg2)) - (2));
    if (condition_is_not_equal) goto loc_008A71C4;
    result = ObQueryTypeInfo(*(uint64_t *)(v_rip - 0x8A6FAE + Arg1 * 8 + 0xFC7800), 0, (uint32_t)((uint32_t)(v_stack_m28)), v_stack_mDC);
    goto loc_008A6FEC;
loc_008A705E:
    if (((uint32_t)(v_stack_m28)) != 56) goto loc_008A7553;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = *(uint64_t *)(v_stack_m28 + 0x30);
    v_stack_m70 = (uint32_t)(v_stack_mA0);
    result = v_stack_mA0;
    if ((((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(v_stack_m28)) + 0x1B))) & (16)) != 0) {
        result = (uint32_t)((v_stack_mA0) | (16));
        v_stack_m70 = (uint32_t)(result);
    }
    if ((((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(v_stack_m28)) + 0x1B))) & (8)) != 0) goto loc_008A7565;
loc_008A70A8:
    v_stack_m6C = (uint32_t)(v_stack_mDC);
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(v_stack_m28)) + 0x8)));
    v_stack_m64 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(v_stack_m28)))));
    result = OBJECT_HEADER_TO_QUOTA_INFO((uint32_t)((uint32_t)(v_stack_m28)), 0, (uint32_t)((uint32_t)(v_stack_m28)), v_stack_mDC);
    if (result == 0) goto loc_008A74CF;
    v_stack_m60 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    v_stack_m5C = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
loc_008A70E9:
    if ((*(uint64_t *)(v_rip - 0x8A6FAE + Arg1 * 8 + 0xFC7800)) == (*(uint64_t *)(v_rip + 0x668568))) goto loc_008A7574;
    result = 0;
loc_008A70F8:
    v_stack_m40 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire((uint32_t)((uint32_t)(v_stack_m28)) + 16, Arg2, Arg3, v_stack_mDC);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = (uint32_t)((uint32_t)(v_stack_m28)) + 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = (uint32_t)((uint32_t)(v_stack_m28)) + 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        Arg2 = 17;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((((uint8_t)(*(uint8_t *)(v_stack_m90 + 0x1A))) & (2)) != 0) goto loc_008A71AB;
    v_stack_mD0 = *(uint64_t *)(v_stack_m28 + 0x30);
loc_008A7170:
    if (*(uint64_t *)(v_stack_m28 + 0x30) != 0) goto loc_008A7264;
loc_008A7179:
    result = Arg2;
    if (*(uint64_t *)(v_stack_m28 + 0x30) != 0) {
        Arg1 = v_stack_m90 + 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(v_stack_m90 + 16, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    goto loc_008A73E0;
loc_008A71AB:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30)))) & (3));
    Arg1 = (v_stack_m90) - (*(uint8_t *)(result + v_rip - 0x8A7164 * 1 + 0xF0FF80));
    v_stack_mD0 = Arg1;
    goto loc_008A7170;
loc_008A71C4:
    local_r15 = (uint32_t)((v_rip - 9072996) - (1));
    if (((uint32_t)(local_r15)) != 1) goto loc_008A7541;
    v_stack_mDC = 2;
    if (((uint32_t)(v_stack_m28)) < 2) goto loc_008A7209;
    *(uint8_t *)(Arg3) = 0;
    if ((((uint8_t)(v_stack_mA0)) & (2)) != 0) {
        *(uint8_t *)(Arg3) = (uint8_t)(local_r15);
    }
    *(uint8_t *)(Arg3 + 0x1) = 0;
    if ((((uint8_t)(v_stack_mA0)) & (1)) == 0) goto loc_008A7212;
    *(uint8_t *)(Arg3 + 0x1) = 1;
    goto loc_008A7212;
loc_008A7209:
    v_stack_mE0 = (uint32_t)((uint32_t)(0xC0000004ULL));
loc_008A7212:
    goto loc_008A6FF2;
loc_008A7232:
    v_stack_mB8 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30));
    v_stack_mA8 = *(uint64_t *)(v_stack_m28 + 0x30);
    v_stack_m98 = *(uint64_t *)(v_stack_m28 + 0x30);
    v_stack_mE0 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30));
    goto loc_008A6FC6;
loc_008A7264:
    v_stack_m88 = *(uint64_t *)(Arg1);
    if (*(uint64_t *)(Arg1) == 0) goto loc_008A7179;
    result = ObfReferenceObject(*(uint64_t *)(Arg1), v_rip - 9073247, *(uint64_t *)(v_stack_m28 + 0x30), (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))));
    if (*(uint64_t *)(Arg1) != 0) goto loc_008A7533;
loc_008A7291:
    result = KeAbPostRelease((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))) + 16, v_rip - 9073247, *(uint64_t *)(v_stack_m28 + 0x30), (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), v_rip - 9073247, *(uint64_t *)(v_stack_m28 + 0x30), (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))));
    local_r13 = (uint32_t)((*(uint16_t *)(v_stack_mD0 + 0x8)) + (2));
loc_008A72C0:
    v_stack_m80 = v_stack_m88 - 48;
    v_stack_mD0 = v_stack_m88 - 48 + 16;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m88 - 48 + 16, Arg2, Arg3, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))));
    v_stack_mC0 = result;
    result = 0;
    local_r10 = v_stack_mD0;
    if (!(condition_is_equal)) {
        Arg4 = v_stack_mD0;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_mD0;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_mC0;
        local_r10 = v_stack_mD0;
    }
    if (Arg1 != 0) {
        *(uint8_t *)(Arg1 + 0xA) = 1;
    }
    if ((((uint8_t)(*(uint8_t *)(v_stack_m80 + 0x1A))) & (2)) != 0) goto loc_008A74DC;
loc_008A7346:
    if (*(uint64_t *)(v_stack_m28 + 0x30) == 0) goto loc_008A74F0;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30)) == 0) goto loc_008A74F0;
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x8)) + (2));
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)(result)));
    v_stack_m88 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30));
    result = ObfReferenceObject(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30)), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30)), Arg3, Arg4);
    result = 17;
    if (!(condition_is_equal)) {
        result = ExfReleasePushLockShared(v_stack_mD0, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30)), Arg3, Arg4);
        Arg1 = v_stack_mD0;
    }
    result = KeAbPostRelease(Arg1, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30)), Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30)), Arg3, Arg4);
    result = ObfDereferenceObject(v_stack_m88, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30)), Arg3, Arg4);
    goto loc_008A72C0;
loc_008A73B1:
    result = KeAbPostRelease(local_r10, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30)), Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30)), Arg3, Arg4);
    if (v_stack_m88 != 0) {
        result = ObfDereferenceObject(v_stack_m88, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30)), Arg3, Arg4);
    }
    result = (uint32_t)(((uint32_t)(v_stack_mC0)) + (18));
loc_008A73E0:
    v_stack_m4C = (uint32_t)(result);
    result = (uint32_t)((*(uint16_t *)(v_stack_m98 + 0x10)) + (106));
    v_stack_m48 = (uint32_t)(result);
    if (((v_stack_mB8) & (0x20000ULL)) != 0) goto loc_008A7475;
loc_008A7408:
    v_stack_m44 = (uint32_t)((uint32_t)(v_stack_mB0));
    *(uint64_t *)(v_stack_m88) = v_xmm0;
    *(uint64_t *)(v_stack_m88 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m88 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m88 + 0x30) = v_xmm1;
    v_stack_mDC = 56;
    goto loc_008A6FF2;
loc_008A7475:
    local_rdi = ((uint32_t)(v_stack_mE0)) + (40);
    if ((*(uint64_t *)(local_rdi)) == 0) goto loc_008A7408;
    v_stack_mB4 = 15;
    v_stack_mF0 = 17;
    v_stack_mF8 = v_stack_m98 + 76;
    v_stack_m100 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m98 + 0x64)));
    v_stack_m108 = local_rdi;
    v_stack_m110 = v_stack_mB0;
    Arg4 = 0;
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_m28 + 0x30), Arg4 + 1, v_stack_mB4, Arg4);
    goto loc_008A7408;
loc_008A74CF:
    v_stack_m60 = *(uint64_t *)(v_stack_m28 + 0x30);
    goto loc_008A70E9;
loc_008A74DC:
    result = (uint32_t)((result) & (3));
    Arg1 = (*(uint64_t *)(v_stack_m28 + 0x30)) - (*(uint8_t *)(result + local_r15 * 1 + 0xF0FF80));
    goto loc_008A7346;
loc_008A74F0:
    v_stack_mC0 = (uint32_t)(local_r13);
    if (condition_is_equal) goto loc_008A73B1;
    result = ExfReleasePushLockShared(local_r10, Arg4 + 1, v_stack_mB4, Arg4);
    goto loc_008A73B1;
loc_008A7533:
    result = ExfReleasePushLockShared(local_r10, Arg4 + 1, v_stack_mB4, Arg4);
    goto loc_008A7291;
loc_008A7541:
    result = ObfDereferenceObject(*(uint64_t *)(v_stack_m28 + 0x30), Arg4 + 1, v_stack_mB4, Arg4);
    goto loc_008A701C;
loc_008A7553:
    result = ObfDereferenceObject(*(uint64_t *)(v_stack_m28 + 0x30), Arg4 + 1, v_stack_mB4, Arg4);
    goto loc_008A701C;
loc_008A7565:
    result = (uint32_t)(((uint32_t)(0xC0000004ULL)) | (32));
    v_stack_m70 = (uint32_t)(result);
    goto loc_008A70A8;
loc_008A7574:
    goto loc_008A70F8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A6DB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
