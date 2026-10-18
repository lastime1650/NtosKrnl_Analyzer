# NtQueryWnfStateData

- RVA: `0x00909DF0`–`0x0090A750` (길이 `2,400` bytes)
- VA: `0x0000000140909DF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00089060`
- 디코드: `531`개 명령, `2,400/2,400` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00909F69` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x0090A074` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x0090A0B6` → [ExRaiseAccessViolation](../8E/ExRaiseAccessViolation_function_008E9240.md) (function, `0x008E9240`)
- `0x0090A0F5` → [PsGetSessionById](../../text/22/PsGetSessionById_function_00225150.md) (function, `0x00225150`)
- `0x0090A18F` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x0090A20F` → [SeCaptureSid](../92/SeCaptureSid_function_009276D4.md) (function, `0x009276D4`)
- `0x0090A28E` → [ExpWnfResolveScopeInstance](ExpWnfResolveScopeInstance_function_0090B280.md) (function, `0x0090B280`)
- `0x0090A2B3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0090A2D4` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0090A348` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (function, `0x0034C050`)
- `0x0090A370` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0090A379` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0090A3E3` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x0090A42F` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x0090A43C` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x0090A4CE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0090A4DC` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0090A4FC` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0090A546` → [ExpWnfLookupPermanentName](../8B/ExpWnfLookupPermanentName_function_008BD914.md) (function, `0x008BD914`)
- `0x0090A573` → [ExpWnfValidatePubSubPreconditions](../9E/ExpWnfValidatePubSubPreconditions_function_009E6E00.md) (function, `0x009E6E00`)
- `0x0090A5C8` → [ExpWnfReadStateData](ExpWnfReadStateData_function_00909C50.md) (function, `0x00909C50`)
- `0x0090A61F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0090A65B` → [ExpWnfCheckCrossScopeAccess](ExpWnfCheckCrossScopeAccess_function_0090CA94.md) (function, `0x0090CA94`)
- `0x0090A674` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x0090A67E` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x0090A6EC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0090A71E` → [ExpWnfCreateNameInstance](../8B/ExpWnfCreateNameInstance_function_008BF590.md) (function, `0x008BF590`)
- `0x0090A736` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00909E03` → RVA `0x00E0A740` (`.data`; read)
- `0x0090A045` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x0090A407` → RVA `0x00B4B070` (`ExpWnfNotificationMapping`; read)
- `0x0090A6C3` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00909F69` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x0090A0F5` → [PsGetSessionById](../../text/22/PsGetSessionById_function_00225150.md) (`PAGE` → `.text`)
  - `0x0090A18F` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x0090A2B3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0090A2D4` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0090A348` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (`PAGE` → `.text`)
  - `0x0090A370` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0090A379` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0090A42F` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x0090A4CE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0090A4DC` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0090A4FC` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0090A61F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0090A674` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x0090A67E` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x0090A6EC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0090A736` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00909DF0  40 53                           push rbx
00909DF2  56                              push rsi
00909DF3  57                              push rdi
00909DF4  41 54                           push r12
00909DF6  41 55                           push r13
00909DF8  41 56                           push r14
00909DFA  41 57                           push r15
00909DFC  48 81 EC 30 01 00 00            sub rsp, 0x130
00909E03  48 8B 05 36 09 50 00            mov rax, qword ptr [rip + 0x500936]
00909E0A  48 33 C4                        xor rax, rsp
00909E0D  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
00909E15  4D 8B D1                        mov r10, r9
00909E18  4C 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r9
00909E20  4D 8B E0                        mov r12, r8
00909E23  4C 8B FA                        mov r15, rdx
00909E26  4C 8B 8C 24 98 01 00 00         mov r9, qword ptr [rsp + 0x198]
00909E2E  4C 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r9
00909E36  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
00909E3E  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00909E43  0F 57 C0                        xorps xmm0, xmm0
00909E46  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
00909E4E  45 33 DB                        xor r11d, r11d
00909E51  44 89 5C 24 60                  mov dword ptr [rsp + 0x60], r11d
00909E56  4C 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], r11
00909E5E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00909E67  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00909E6E  90                              nop
00909E6F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00909E78  44 0F B6 A8 32 02 00 00         movzx r13d, byte ptr [rax + 0x232]
00909E80  44 88 6C 24 54                  mov byte ptr [rsp + 0x54], r13b
00909E85  4C 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], r11
00909E8D  4C 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], r11
00909E95  4C 89 5C 24 78                  mov qword ptr [rsp + 0x78], r11
00909E9A  44 89 5C 24 5C                  mov dword ptr [rsp + 0x5c], r11d
00909E9F  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
00909EA7  48 89 94 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rdx
00909EAF  4C 89 9C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r11
00909EB7  48 BE 00 00 FF FF FF 7F 00 00   movabs rsi, 0x7fffffff0000
00909EC1  45 84 ED                        test r13b, r13b
00909EC4  0F 85 AD 02 00 00               jne 0x14090a177
00909ECA  48 8B 19                        mov rbx, qword ptr [rcx]
00909ECD  48 89 9C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rbx
00909ED5  48 B8 74 00 BC A3 6D 4E C6 41   movabs rax, 0x41c64e6da3bc0074
00909EDF  48 33 D8                        xor rbx, rax
00909EE2  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00909EE7  0F B6 C3                        movzx eax, bl
00909EEA  24 0F                           and al, 0xf
00909EEC  3C 01                           cmp al, 1
00909EEE  0F 85 76 02 00 00               jne 0x14090a16a
00909EF4  48 8B FB                        mov rdi, rbx
00909EF7  48 C1 EF 06                     shr rdi, 6
00909EFB  8B D7                           mov edx, edi
00909EFD  83 E2 0F                        and edx, 0xf
00909F00  4C 8B F3                        mov r14, rbx
00909F03  49 C1 EE 04                     shr r14, 4
00909F07  41 8B CE                        mov ecx, r14d
00909F0A  83 E1 03                        and ecx, 3
00909F0D  48 8B C3                        mov rax, rbx
00909F10  48 C1 E8 0A                     shr rax, 0xa
00909F14  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
00909F1C  44 8B C0                        mov r8d, eax
00909F1F  41 83 E0 01                     and r8d, 1
00909F23  83 F9 03                        cmp ecx, 3
00909F26  0F 85 24 02 00 00               jne 0x14090a150
00909F2C  83 FA 05                        cmp edx, 5
00909F2F  0F 85 7F 02 00 00               jne 0x14090a1b4
00909F35  45 85 C0                        test r8d, r8d
00909F38  0F 85 7E 01 00 00               jne 0x14090a0bc
00909F3E  44 89 5C 24 50                  mov dword ptr [rsp + 0x50], r11d
00909F43  45 84 ED                        test r13b, r13b
00909F46  0F 84 59 01 00 00               je 0x14090a0a5
00909F4C  4D 85 FF                        test r15, r15
00909F4F  74 40                           je 0x140909f91
00909F51  48 8B D6                        mov rdx, rsi
00909F54  4C 3B FE                        cmp r15, rsi
00909F57  49 0F 42 D7                     cmovb rdx, r15
00909F5B  41 B8 10 00 00 00               mov r8d, 0x10
00909F61  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00909F69  E8 62 2A DB FF                  call 0x1406bc9d0
00909F6E  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
00909F76  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00909F7E  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
00909F86  4C 8B 94 24 B8 00 00 00         mov r10, qword ptr [rsp + 0xb8]
00909F8E  45 33 DB                        xor r11d, r11d
00909F91  48 8B CE                        mov rcx, rsi
00909F94  4C 3B D6                        cmp r10, rsi
00909F97  49 0F 42 CA                     cmovb rcx, r10
00909F9B  8B 01                           mov eax, dword ptr [rcx]
00909F9D  89 01                           mov dword ptr [rcx], eax
00909F9F  48 8B C6                        mov rax, rsi
00909FA2  4C 3B CE                        cmp r9, rsi
00909FA5  49 0F 42 C1                     cmovb rax, r9
00909FA9  90                              nop
00909FAA  8B 10                           mov edx, dword ptr [rax]
00909FAC  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
00909FB0  48 8B CE                        mov rcx, rsi
00909FB3  49 0F 42 C9                     cmovb rcx, r9
00909FB7  8B 01                           mov eax, dword ptr [rcx]
00909FB9  89 01                           mov dword ptr [rcx], eax
00909FBB  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00909FC0  85 D2                           test edx, edx
00909FC2  74 44                           je 0x14090a008
00909FC4  8B C2                           mov eax, edx
00909FC6  49 8B CF                        mov rcx, r15
00909FC9  49 8D 57 FF                     lea rdx, [r15 - 1]
00909FCD  48 03 D0                        add rdx, rax
00909FD0  4C 3B FA                        cmp r15, rdx
00909FD3  0F 87 DD 00 00 00               ja 0x14090a0b6
00909FD9  48 3B D6                        cmp rdx, rsi
00909FDC  0F 83 D4 00 00 00               jae 0x14090a0b6
00909FE2  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
00909FE9  48 81 C2 00 10 00 00            add rdx, 0x1000
00909FF0  0F B6 01                        movzx eax, byte ptr [rcx]
00909FF3  88 01                           mov byte ptr [rcx], al
00909FF5  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00909FFC  48 81 C1 00 10 00 00            add rcx, 0x1000
0090A003  48 3B CA                        cmp rcx, rdx
0090A006  75 E8                           jne 0x140909ff0
0090A008  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0090A00D  41 83 E6 03                     and r14d, 3
0090A011  44 89 B4 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r14d
0090A019  83 E7 0F                        and edi, 0xf
0090A01C  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
0090A020  44 89 5C 24 58                  mov dword ptr [rsp + 0x58], r11d
0090A025  4D 85 E4                        test r12, r12
0090A028  75 12                           jne 0x14090a03c
0090A02A  4C 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], r11
0090A032  44 89 5C 24 50                  mov dword ptr [rsp + 0x50], r11d
0090A037  E9 F4 01 00 00                  jmp 0x14090a230
0090A03C  83 FF 03                        cmp edi, 3
0090A03F  0F 85 91 00 00 00               jne 0x14090a0d6
0090A045  4C 8B 05 4C CA 6B 00            mov r8, qword ptr [rip + 0x6bca4c]
0090A04C  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
0090A051  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
0090A056  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
0090A05E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0090A063  C7 44 24 20 57 6E 66 20         mov dword ptr [rsp + 0x20], 0x20666e57
0090A06B  45 0F B6 CD                     movzx r9d, r13b
0090A06F  33 D2                           xor edx, edx
0090A071  49 8B CC                        mov rcx, r12
0090A074  E8 D7 F5 F5 FF                  call 0x140869650
0090A079  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
0090A07D  45 33 DB                        xor r11d, r11d
0090A080  85 C0                           test eax, eax
0090A082  78 10                           js 0x14090a094
0090A084  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
0090A08C  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
0090A094  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090A098  85 C0                           test eax, eax
0090A09A  0F 89 90 01 00 00               jns 0x14090a230
0090A0A0  E9 C3 03 00 00                  jmp 0x14090a468
0090A0A5  41 8B 01                        mov eax, dword ptr [r9]
0090A0A8  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0090A0AC  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
0090A0B1  E9 57 FF FF FF                  jmp 0x14090a00d
0090A0B6  E8 85 F1 FD FF                  call 0x1408e9240
0090A0BB  CC                              int3
0090A0BC  F7 C2 F9 FF FF FF               test edx, 0xfffffff9
0090A0C2  0F 85 A2 00 00 00               jne 0x14090a16a
0090A0C8  83 FA 06                        cmp edx, 6
0090A0CB  0F 85 6D FE FF FF               jne 0x140909f3e
0090A0D1  E9 94 00 00 00                  jmp 0x14090a16a
0090A0D6  8B CF                           mov ecx, edi
0090A0D8  85 FF                           test edi, edi
0090A0DA  74 4A                           je 0x14090a126
0090A0DC  83 E9 01                        sub ecx, 1
0090A0DF  0F 85 FE 00 00 00               jne 0x14090a1e3
0090A0E5  45 84 ED                        test r13b, r13b
0090A0E8  75 4A                           jne 0x14090a134
0090A0EA  41 8B 0C 24                     mov ecx, dword ptr [r12]
0090A0EE  89 8C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ecx
0090A0F5  E8 56 B0 91 FF                  call 0x140225150
0090A0FA  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
0090A102  45 33 DB                        xor r11d, r11d
0090A105  48 85 C0                        test rax, rax
0090A108  74 1C                           je 0x14090a126
0090A10A  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
0090A112  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0090A11A  41 8B C3                        mov eax, r11d
0090A11D  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
0090A121  E9 6E FF FF FF                  jmp 0x14090a094
0090A126  B8 0D 00 00 C0                  mov eax, 0xc000000d
0090A12B  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
0090A12F  E9 60 FF FF FF                  jmp 0x14090a094
0090A134  4C 3B E6                        cmp r12, rsi
0090A137  49 0F 42 F4                     cmovb rsi, r12
0090A13B  90                              nop
0090A13C  8B 0E                           mov ecx, dword ptr [rsi]
0090A13E  89 8C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ecx
0090A145  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0090A14A  8B 7C 24 5C                     mov edi, dword ptr [rsp + 0x5c]
0090A14E  EB A5                           jmp 0x14090a0f5
0090A150  85 C9                           test ecx, ecx
0090A152  0F 84 D4 FD FF FF               je 0x140909f2c
0090A158  83 E9 01                        sub ecx, 1
0090A15B  0F 84 CB FD FF FF               je 0x140909f2c
0090A161  83 F9 01                        cmp ecx, 1
0090A164  0F 84 C2 FD FF FF               je 0x140909f2c
0090A16A  C7 44 24 50 0D 00 00 C0         mov dword ptr [rsp + 0x50], 0xc000000d
0090A172  E9 F1 02 00 00                  jmp 0x14090a468
0090A177  48 8B D6                        mov rdx, rsi
0090A17A  48 3B CE                        cmp rcx, rsi
0090A17D  48 0F 42 D1                     cmovb rdx, rcx
0090A181  41 B8 08 00 00 00               mov r8d, 8
0090A187  48 8D 8C 24 C8 00 00 00         lea rcx, [rsp + 0xc8]
0090A18F  E8 3C 28 DB FF                  call 0x1406bc9d0
0090A194  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0090A19C  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
0090A1A4  4C 8B 94 24 B8 00 00 00         mov r10, qword ptr [rsp + 0xb8]
0090A1AC  45 33 DB                        xor r11d, r11d
0090A1AF  E9 21 FD FF FF                  jmp 0x140909ed5
0090A1B4  8B CA                           mov ecx, edx
0090A1B6  85 D2                           test edx, edx
0090A1B8  0F 84 77 FD FF FF               je 0x140909f35
0090A1BE  83 E9 01                        sub ecx, 1
0090A1C1  0F 84 6E FD FF FF               je 0x140909f35
0090A1C7  83 E9 01                        sub ecx, 1
0090A1CA  0F 84 65 FD FF FF               je 0x140909f35
0090A1D0  83 E9 01                        sub ecx, 1
0090A1D3  0F 84 5C FD FF FF               je 0x140909f35
0090A1D9  83 F9 01                        cmp ecx, 1
0090A1DC  75 8C                           jne 0x14090a16a
0090A1DE  E9 52 FD FF FF                  jmp 0x140909f35
0090A1E3  83 E9 01                        sub ecx, 1
0090A1E6  74 0E                           je 0x14090a1f6
0090A1E8  B8 0D 00 00 C0                  mov eax, 0xc000000d
0090A1ED  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
0090A1F1  E9 9E FE FF FF                  jmp 0x14090a094
0090A1F6  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
0090A1FE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0090A203  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
0090A208  41 0F B6 D5                     movzx edx, r13b
0090A20C  49 8B CC                        mov rcx, r12
0090A20F  E8 C0 D4 01 00                  call 0x1409276d4
0090A214  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
0090A218  45 33 DB                        xor r11d, r11d
0090A21B  85 C0                           test eax, eax
0090A21D  0F 88 71 FE FF FF               js 0x14090a094
0090A223  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0090A22B  E9 5C FE FF FF                  jmp 0x14090a08c
0090A230  EB 0F                           jmp 0x14090a241
0090A232  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090A236  44 0F B6 6C 24 54               movzx r13d, byte ptr [rsp + 0x54]
0090A23C  E9 27 02 00 00                  jmp 0x14090a468
0090A241  45 84 ED                        test r13b, r13b
0090A244  0F 84 48 04 00 00               je 0x14090a692
0090A24A  45 8B F3                        mov r14d, r11d
0090A24D  4D 85 E4                        test r12, r12
0090A250  0F 85 02 04 00 00               jne 0x14090a658
0090A256  45 84 ED                        test r13b, r13b
0090A259  0F 84 61 04 00 00               je 0x14090a6c0
0090A25F  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
0090A268  49 8B B0 B8 00 00 00            mov rsi, qword ptr [r8 + 0xb8]
0090A26F  8B 7C 24 5C                     mov edi, dword ptr [rsp + 0x5c]
0090A273  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0090A27B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0090A280  44 8B CF                        mov r9d, edi
0090A283  48 8B D6                        mov rdx, rsi
0090A286  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
0090A28E  E8 ED 0F 00 00                  call 0x14090b280
0090A293  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090A297  85 C0                           test eax, eax
0090A299  0F 88 C9 01 00 00               js 0x14090a468
0090A29F  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
0090A2A7  48 83 C3 30                     add rbx, 0x30
0090A2AB  45 33 C0                        xor r8d, r8d
0090A2AE  33 D2                           xor edx, edx
0090A2B0  48 8B CB                        mov rcx, rbx
0090A2B3  E8 78 5F 90 FF                  call 0x140210230
0090A2B8  48 8B F8                        mov rdi, rax
0090A2BB  B9 11 00 00 00                  mov ecx, 0x11
0090A2C0  33 C0                           xor eax, eax
0090A2C2  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
0090A2C7  74 10                           je 0x14090a2d9
0090A2C9  4C 8B CB                        mov r9, rbx
0090A2CC  4C 8B C7                        mov r8, rdi
0090A2CF  33 D2                           xor edx, edx
0090A2D1  48 8B CB                        mov rcx, rbx
0090A2D4  E8 73 61 90 FF                  call 0x14021044c
0090A2D9  48 85 FF                        test rdi, rdi
0090A2DC  74 04                           je 0x14090a2e2
0090A2DE  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0090A2E2  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0090A2EA  48 8B 50 38                     mov rdx, qword ptr [rax + 0x38]
0090A2EE  48 85 D2                        test rdx, rdx
0090A2F1  0F 84 26 02 00 00               je 0x14090a51d
0090A2F7  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0090A2FC  0F 1F 40 00                     nop dword ptr [rax]
0090A300  48 3B 42 18                     cmp rax, qword ptr [rdx + 0x18]
0090A304  0F 82 0B 02 00 00               jb 0x14090a515
0090A30A  76 09                           jbe 0x14090a315
0090A30C  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
0090A310  48 85 D2                        test rdx, rdx
0090A313  75 EB                           jne 0x14090a300
0090A315  48 85 D2                        test rdx, rdx
0090A318  0F 84 FF 01 00 00               je 0x14090a51d
0090A31E  48 8D 5A F0                     lea rbx, [rdx - 0x10]
0090A322  48 85 DB                        test rbx, rbx
0090A325  0F 84 CB 03 00 00               je 0x14090a6f6
0090A32B  48 8D 4B 08                     lea rcx, [rbx + 8]
0090A32F  0F 0D 09                        prefetchw byte ptr [rcx]
0090A332  48 8B 01                        mov rax, qword ptr [rcx]
0090A335  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0090A339  48 8D 50 02                     lea rdx, [rax + 2]
0090A33D  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0090A342  0F 84 AE 03 00 00               je 0x14090a6f6
0090A348  E8 03 1D A4 FF                  call 0x14034c050
0090A34D  45 33 E4                        xor r12d, r12d
0090A350  84 C0                           test al, al
0090A352  75 03                           jne 0x14090a357
0090A354  41 8B DC                        mov ebx, r12d
0090A357  48 8B BC 24 80 00 00 00         mov rdi, qword ptr [rsp + 0x80]
0090A35F  B8 11 00 00 00                  mov eax, 0x11
0090A364  F0 4C 0F B1 67 30               lock cmpxchg qword ptr [rdi + 0x30], r12
0090A36A  74 09                           je 0x14090a375
0090A36C  48 8D 4F 30                     lea rcx, [rdi + 0x30]
0090A370  E8 CB 90 95 FF                  call 0x140263440
0090A375  48 8D 4F 30                     lea rcx, [rdi + 0x30]
0090A379  E8 82 72 9D FF                  call 0x1402e1600
0090A37E  48 85 DB                        test rbx, rbx
0090A381  0F 84 01 03 00 00               je 0x14090a688
0090A387  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
0090A38C  41 8B C4                        mov eax, r12d
0090A38F  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090A393  3D 34 00 00 C0                  cmp eax, 0xc0000034
0090A398  0F 84 8A 01 00 00               je 0x14090a528
0090A39E  85 C0                           test eax, eax
0090A3A0  0F 88 C2 00 00 00               js 0x14090a468
0090A3A6  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0090A3AB  45 85 F6                        test r14d, r14d
0090A3AE  0F 85 98 00 00 00               jne 0x14090a44c
0090A3B4  48 8B 5F 48                     mov rbx, qword ptr [rdi + 0x48]
0090A3B8  0F 57 C0                        xorps xmm0, xmm0
0090A3BB  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
0090A3C3  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
0090A3CB  44 89 A4 24 C4 00 00 00         mov dword ptr [rsp + 0xc4], r12d
0090A3D3  44 89 A4 24 88 00 00 00         mov dword ptr [rsp + 0x88], r12d
0090A3DB  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
0090A3E3  E8 38 14 F6 FF                  call 0x14086b820
0090A3E8  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
0090A3F0  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0090A3F5  48 8D 84 24 C4 00 00 00         lea rax, [rsp + 0xc4]
0090A3FD  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0090A402  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
0090A407  48 8D 05 62 0C 24 00            lea rax, [rip + 0x240c62]
0090A40E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0090A413  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
0090A418  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
0090A41D  45 8D 4E 01                     lea r9d, [r14 + 1]
0090A421  45 33 C0                        xor r8d, r8d
0090A424  48 8D 94 24 F0 00 00 00         lea rdx, [rsp + 0xf0]
0090A42C  48 8B CB                        mov rcx, rbx
0090A42F  E8 8C C7 A9 FF                  call 0x1403a6bc0
0090A434  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
0090A43C  E8 CF 12 F6 FF                  call 0x14086b710
0090A441  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
0090A448  85 C0                           test eax, eax
0090A44A  78 10                           js 0x14090a45c
0090A44C  48 8B 4F 40                     mov rcx, qword ptr [rdi + 0x40]
0090A450  48 85 C9                        test rcx, rcx
0090A453  0F 85 D0 01 00 00               jne 0x14090a629
0090A459  41 8B C4                        mov eax, r12d
0090A45C  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090A460  85 C0                           test eax, eax
0090A462  0F 89 35 01 00 00               jns 0x14090a59d
0090A468  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0090A46D  48 85 C9                        test rcx, rcx
0090A470  74 1D                           je 0x14090a48f
0090A472  48 83 C1 08                     add rcx, 8
0090A476  0F 0D 09                        prefetchw byte ptr [rcx]
0090A479  48 8B 01                        mov rax, qword ptr [rcx]
0090A47C  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0090A480  48 8D 50 FE                     lea rdx, [rax - 2]
0090A484  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0090A489  0F 85 E5 01 00 00               jne 0x14090a674
0090A48F  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0090A497  48 85 C9                        test rcx, rcx
0090A49A  74 1D                           je 0x14090a4b9
0090A49C  48 83 C1 08                     add rcx, 8
0090A4A0  0F 0D 09                        prefetchw byte ptr [rcx]
0090A4A3  48 8B 01                        mov rax, qword ptr [rcx]
0090A4A6  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0090A4AA  48 8D 50 FE                     lea rdx, [rax - 2]
0090A4AE  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0090A4B3  0F 85 C5 01 00 00               jne 0x14090a67e
0090A4B9  48 8B BC 24 98 00 00 00         mov rdi, qword ptr [rsp + 0x98]
0090A4C1  48 85 FF                        test rdi, rdi
0090A4C4  74 0D                           je 0x14090a4d3
0090A4C6  BA 57 6E 66 20                  mov edx, 0x20666e57
0090A4CB  48 8B CF                        mov rcx, rdi
0090A4CE  E8 9D 83 27 00                  call 0x140b82870
0090A4D3  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0090A4DC  E8 0F 4B 95 FF                  call 0x14025eff0
0090A4E1  8B 4C 24 5C                     mov ecx, dword ptr [rsp + 0x5c]
0090A4E5  85 C9                           test ecx, ecx
0090A4E7  0F 85 05 01 00 00               jne 0x14090a5f2
0090A4ED  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0090A4F1  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
0090A4F9  48 33 CC                        xor rcx, rsp
0090A4FC  E8 3F 21 DA FF                  call 0x1406ac640
0090A501  48 81 C4 30 01 00 00            add rsp, 0x130
0090A508  41 5F                           pop r15
0090A50A  41 5E                           pop r14
0090A50C  41 5D                           pop r13
0090A50E  41 5C                           pop r12
0090A510  5F                              pop rdi
0090A511  5E                              pop rsi
0090A512  5B                              pop rbx
0090A513  C3                              ret
0090A514  CC                              int3
0090A515  48 8B 12                        mov rdx, qword ptr [rdx]
0090A518  E9 F3 FD FF FF                  jmp 0x14090a310
0090A51D  45 33 E4                        xor r12d, r12d
0090A520  41 8B DC                        mov ebx, r12d
0090A523  E9 2F FE FF FF                  jmp 0x14090a357
0090A528  83 BC 24 C0 00 00 00 03         cmp dword ptr [rsp + 0xc0], 3
0090A530  0F 84 68 FE FF FF               je 0x14090a39e
0090A536  48 8D 94 24 98 00 00 00         lea rdx, [rsp + 0x98]
0090A53E  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0090A543  48 8B CB                        mov rcx, rbx
0090A546  E8 C9 33 FB FF                  call 0x1408bd914
0090A54B  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090A54F  85 C0                           test eax, eax
0090A551  0F 88 11 FF FF FF               js 0x14090a468
0090A557  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
0090A55C  4C 8B 8C 24 D0 00 00 00         mov r9, qword ptr [rsp + 0xd0]
0090A564  45 33 C0                        xor r8d, r8d
0090A567  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0090A56F  41 8D 48 01                     lea ecx, [r8 + 1]
0090A573  E8 88 C8 0D 00                  call 0x1409e6e00
0090A578  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090A57C  85 C0                           test eax, eax
0090A57E  0F 88 E4 FE FF FF               js 0x14090a468
0090A584  83 7C 24 5C 05                  cmp dword ptr [rsp + 0x5c], 5
0090A589  0F 84 6F 01 00 00               je 0x14090a6fe
0090A58F  F6 84 24 D8 00 00 00 01         test byte ptr [rsp + 0xd8], 1
0090A597  0F 85 61 01 00 00               jne 0x14090a6fe
0090A59D  90                              nop
0090A59E  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
0090A5A6  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0090A5AE  48 83 7C 24 78 00               cmp qword ptr [rsp + 0x78], 0
0090A5B4  74 1D                           je 0x14090a5d3
0090A5B6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0090A5BB  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
0090A5C0  4D 8B C7                        mov r8, r15
0090A5C3  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0090A5C8  E8 83 F6 FF FF                  call 0x140909c50
0090A5CD  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090A5D1  EB 0B                           jmp 0x14090a5de
0090A5D3  44 89 22                        mov dword ptr [rdx], r12d
0090A5D6  44 89 20                        mov dword ptr [rax], r12d
0090A5D9  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
0090A5DE  E9 85 FE FF FF                  jmp 0x14090a468
0090A5E3  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090A5E7  44 0F B6 6C 24 54               movzx r13d, byte ptr [rsp + 0x54]
0090A5ED  E9 76 FE FF FF                  jmp 0x14090a468
0090A5F2  83 E9 01                        sub ecx, 1
0090A5F5  74 49                           je 0x14090a640
0090A5F7  83 E9 01                        sub ecx, 1
0090A5FA  0F 84 CF 00 00 00               je 0x14090a6cf
0090A600  83 F9 01                        cmp ecx, 1
0090A603  0F 85 E4 FE FF FF               jne 0x14090a4ed
0090A609  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0090A611  48 85 C9                        test rcx, rcx
0090A614  0F 84 D3 FE FF FF               je 0x14090a4ed
0090A61A  BA 57 6E 66 20                  mov edx, 0x20666e57
0090A61F  E8 BC D2 9E FF                  call 0x1402f78e0
0090A624  E9 C4 FE FF FF                  jmp 0x14090a4ed
0090A629  48 8B 94 24 D0 00 00 00         mov rdx, qword ptr [rsp + 0xd0]
0090A631  48 85 D2                        test rdx, rdx
0090A634  75 67                           jne 0x14090a69d
0090A636  B8 0D 00 00 C0                  mov eax, 0xc000000d
0090A63B  E9 1C FE FF FF                  jmp 0x14090a45c
0090A640  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0090A648  48 85 C9                        test rcx, rcx
0090A64B  0F 84 9C FE FF FF               je 0x14090a4ed
0090A651  BA 50 73 51 79                  mov edx, 0x79517350
0090A656  EB C7                           jmp 0x14090a61f
0090A658  48 8B CB                        mov rcx, rbx
0090A65B  E8 34 24 00 00                  call 0x14090ca94
0090A660  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090A664  85 C0                           test eax, eax
0090A666  0F 88 FC FD FF FF               js 0x14090a468
0090A66C  45 33 DB                        xor r11d, r11d
0090A66F  E9 E2 FB FF FF                  jmp 0x14090a256
0090A674  E8 37 F8 A3 FF                  call 0x140349eb0
0090A679  E9 11 FE FF FF                  jmp 0x14090a48f
0090A67E  E8 2D F8 A3 FF                  call 0x140349eb0
0090A683  E9 31 FE FF FF                  jmp 0x14090a4b9
0090A688  B8 34 00 00 C0                  mov eax, 0xc0000034
0090A68D  E9 FD FC FF FF                  jmp 0x14090a38f
0090A692  41 BE 01 00 00 00               mov r14d, 1
0090A698  E9 B9 FB FF FF                  jmp 0x14090a256
0090A69D  4C 8B 01                        mov r8, qword ptr [rcx]
0090A6A0  4C 2B 02                        sub r8, qword ptr [rdx]
0090A6A3  75 08                           jne 0x14090a6ad
0090A6A5  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
0090A6A9  4C 2B 42 08                     sub r8, qword ptr [rdx + 8]
0090A6AD  4D 85 C0                        test r8, r8
0090A6B0  0F 84 A3 FD FF FF               je 0x14090a459
0090A6B6  B8 0D 00 00 C0                  mov eax, 0xc000000d
0090A6BB  E9 9C FD FF FF                  jmp 0x14090a45c
0090A6C0  4D 8B C3                        mov r8, r11
0090A6C3  48 8B 35 E6 C3 6B 00            mov rsi, qword ptr [rip + 0x6bc3e6]
0090A6CA  E9 A4 FB FF FF                  jmp 0x14090a273
0090A6CF  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0090A6D7  48 85 C9                        test rcx, rcx
0090A6DA  0F 84 0D FE FF FF               je 0x14090a4ed
0090A6E0  41 80 FD 01                     cmp r13b, 1
0090A6E4  0F 85 03 FE FF FF               jne 0x14090a4ed
0090A6EA  33 D2                           xor edx, edx
0090A6EC  E8 7F 81 27 00                  call 0x140b82870
0090A6F1  E9 F7 FD FF FF                  jmp 0x14090a4ed
0090A6F6  45 33 E4                        xor r12d, r12d
0090A6F9  E9 59 FC FF FF                  jmp 0x14090a357
0090A6FE  48 8D 44 24 78                  lea rax, [rsp + 0x78]
0090A703  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0090A708  4C 8B CE                        mov r9, rsi
0090A70B  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
0090A713  48 8B D3                        mov rdx, rbx
0090A716  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0090A71E  E8 6D 4E FB FF                  call 0x1408bf590
0090A723  8B D8                           mov ebx, eax
0090A725  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090A729  BA 57 6E 66 20                  mov edx, 0x20666e57
0090A72E  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
0090A736  E8 35 81 27 00                  call 0x140b82870
0090A73B  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
0090A743  85 DB                           test ebx, ebx
0090A745  0F 89 52 FE FF FF               jns 0x14090a59d
0090A74B  E9 18 FD FF FF                  jmp 0x14090a468
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryWnfStateData(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned int v_stack_m10C;
    unsigned int v_stack_m110;
    unsigned __int8 v_stack_m114;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p20;
    unsigned int v_stack_p50;
    unsigned __int8 v_stack_p54;
    unsigned int v_stack_p5C;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned int v_stack_pC0;
    unsigned __int64 v_stack_pD0;
    unsigned __int8 v_stack_pD8;

    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 5245238)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mB0 = a4;
    v_stack_mB8 = a6;
    v_stack_m100 = a5;
    v_stack_m58 = v_xmm0;
    v_r11 = 0;
    v_stack_m108 = 0;
    v_stack_mD8 = 0;
    v_stack_m114 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_mD0 = 0;
    v_stack_mE8 = 0;
    v_stack_mF0 = 0;
    v_stack_m10C = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_m98 = a2;
    v_stack_mA0 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_0090A177;
    v_stack_mA0 = *(unsigned __int64 *)(a1);
loc_00909ED5:
    v_rbx = (*(unsigned __int64 *)(a1)) ^ (*(unsigned __int64 *)(gs_base + (0 + 392)));
    v_stack_mF8 = v_rbx;
    result = (unsigned __int8)(((unsigned __int8)(v_rbx)) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_0090A16A;
    v_rdi = (v_rbx) >> (6);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (15));
    v_r14 = (v_rbx) >> (4);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (3));
    result = (v_rbx) >> (10);
    v_stack_m90 = result;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (1));
    if (((unsigned int)(a1)) != 3) goto loc_0090A150;
loc_00909F2C:
    if (((unsigned int)(a2)) != 5) goto loc_0090A1B4;
loc_00909F35:
    if ((unsigned int)(a3) != 0) goto loc_0090A0BC;
loc_00909F3E:
    v_stack_m118 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_0090A0A5;
    v_r10 = a4;
    if (a2 != 0) {
        a2 = v_rsi;
        if (a2 < v_rsi) { a2 = a2; }
        a3 = 16;
        a1 = v_stack_m58;
        result = RtlCopyVolatileMemory(a1, a2, a3, a6);
        result = v_stack_m58;
        v_stack_m98 = result;
        a4 = v_stack_mB8;
        v_r10 = v_stack_mB0;
        v_r11 = 0;
    }
    a1 = v_rsi;
    if (v_r10 < v_rsi) { a1 = v_r10; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    result = v_rsi;
    if (a4 < v_rsi) { result = a4; }
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    a1 = v_rsi;
    if (a4 < v_rsi) { a1 = a4; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result))) == 0) goto loc_0090A008;
    a2 = (v_stack_m100 - 1) + ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result)))));
    if (v_stack_m100 > a2) goto loc_0090A0B6;
    if (a2 >= v_rsi) goto loc_0090A0B6;
    a2 = (a2) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a2) + (0x1000ULL);
loc_00909FF0:
    *(unsigned __int8 *)(v_stack_m100) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m100));
    a1 = (v_stack_m100) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) + (0x1000ULL);
    if (a1 != a2) goto loc_00909FF0;
loc_0090A008:
loc_0090A00D:
    v_r14 = (unsigned int)((v_r14) & (3));
    v_stack_mA8 = (unsigned int)(v_r14);
    v_rdi = (unsigned int)((v_rdi) & (15));
    v_stack_m10C = (unsigned int)(v_rdi);
    v_stack_m110 = 0;
    if (a3 != 0) goto loc_0090A03C;
    v_stack_mD8 = 0;
    v_stack_m118 = 0;
    goto loc_0090A230;
loc_0090A03C:
    if (((unsigned int)(v_rdi)) != 3) goto loc_0090A0D6;
    v_stack_m130 = 0;
    v_stack_m138 = 0;
    v_stack_m140 = v_stack_mC8;
    v_stack_m148 = 0x20666E57ULL;
    a2 = 0;
    result = ObpReferenceObjectByHandleWithTag(a3, a2, *(unsigned __int64 *)(v_rip + 7064140), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m110 = (unsigned int)(result);
    v_r11 = 0;
    if (sign_flag) goto loc_0090A094;
loc_0090A08C:
    v_stack_mD8 = v_stack_mC8;
loc_0090A094:
    v_stack_m118 = (unsigned int)(result);
    if (!sign_flag) goto loc_0090A230;
    goto loc_0090A468;
loc_0090A0A5:
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))));
    goto loc_0090A00D;
loc_0090A0B6:
    result = ExRaiseAccessViolation(v_stack_mC8, a2, *(unsigned __int64 *)(v_rip + 7064140), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
loc_0090A0BC:
    if (((0) & (0xFFFFFFF9ULL)) != 0) goto loc_0090A16A;
    if (0 != 6) goto loc_00909F3E;
    goto loc_0090A16A;
loc_0090A0D6:
    if ((unsigned int)(v_rdi) == 0) goto loc_0090A126;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (1));
    if (condition_is_not_equal) goto loc_0090A1E3;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_0090A134;
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
loc_0090A0F5:
    result = PsGetSessionById((unsigned int)(*(unsigned int *)(a3)), a2, *(unsigned __int64 *)(v_rip + 7064140), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_mC8 = result;
    v_r11 = 0;
    if (result == 0) goto loc_0090A126;
    v_stack_mD8 = v_stack_mC0;
    v_stack_m110 = 0;
    goto loc_0090A094;
loc_0090A126:
    v_stack_m110 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_0090A094;
loc_0090A134:
    if (a3 < v_rsi) { v_rsi = a3; }
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)));
    goto loc_0090A0F5;
loc_0090A150:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))) == 0) goto loc_00909F2C;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) - (1));
    if (condition_is_equal) goto loc_00909F2C;
    if (((unsigned int)(a1)) == 1) goto loc_00909F2C;
loc_0090A16A:
    v_stack_m118 = 0xC000000DULL;
    goto loc_0090A468;
loc_0090A177:
    a2 = v_rsi;
    if (a1 < v_rsi) { a2 = a1; }
    result = RtlCopyVolatileMemory(v_stack_mA0, a2, 8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_r11 = 0;
    goto loc_00909ED5;
loc_0090A1B4:
    if ((unsigned int)(a2) == 0) goto loc_00909F35;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - (1));
    if (condition_is_equal) goto loc_00909F35;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00909F35;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00909F35;
    if (((unsigned int)(a1)) != 1) goto loc_0090A16A;
    goto loc_00909F35;
loc_0090A1E3:
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0090A1F6;
    v_stack_m110 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_0090A094;
loc_0090A1F6:
    v_stack_m138 = v_stack_mC8;
    v_stack_m140 = 0;
    result = SeCaptureSid(a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 8, v_stack_mB8);
    v_stack_m110 = (unsigned int)(result);
    v_r11 = 0;
    if (sign_flag) goto loc_0090A094;
    goto loc_0090A08C;
loc_0090A230:
    goto loc_0090A241;
loc_0090A241:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_0090A692;
    if (a3 != 0) goto loc_0090A658;
loc_0090A256:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_0090A6C0;
loc_0090A273:
    v_stack_m148 = v_stack_mD8;
    result = ExpWnfResolveScopeInstance(v_stack_mE8, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m10C))));
    v_stack_m118 = (unsigned int)(result);
    if (sign_flag) goto loc_0090A468;
    v_rbx = (v_stack_mE8) + (48);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rbx, a2, a3, (unsigned int)((unsigned int)((unsigned int)(v_stack_m10C))));
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rbx;
        a3 = 0;
        a2 = 0;
        a1 = v_rbx;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(v_stack_mE8 + 56) == 0) goto loc_0090A51D;
loc_0090A300:
    if (v_stack_mF8 < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 56) + 24))) goto loc_0090A515;
    if (v_stack_mF8 <= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 56) + 24))) goto loc_0090A315;
loc_0090A310:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 56) + 8) != 0) goto loc_0090A300;
loc_0090A315:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 56) + 8) == 0) goto loc_0090A51D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 56) + 8) - 16 == 0) goto loc_0090A6F6;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 56) + 8) - 16 + 8)) & (-2);
    if (condition_is_equal) goto loc_0090A6F6;
    result = ExfAcquireRundownProtection(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 56) + 8) - 16 + 8, result + 2, a3, a4);
    v_r12 = 0;
    v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 56) + 8) - 16;
    if ((unsigned __int8)(result) == 0) {
        v_rbx = 0;
    }
    result = 17;
    if ((unsigned __int8)(result) != 0) {
        a1 = v_stack_mE8 + 48;
        result = ExfReleasePushLockShared(a1, result + 2, a3, a4);
    }
    result = KeAbPostRelease(v_stack_mE8 + 48, result + 2, a3, a4);
    if (v_rbx == 0) goto loc_0090A688;
    v_stack_mF0 = v_rbx;
loc_0090A38F:
    v_stack_m118 = 0;
    if (0 == 0xC0000034ULL) goto loc_0090A528;
loc_0090A39E:
    if (sign_flag) goto loc_0090A468;
    if (0 != 0) goto loc_0090A44C;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_mA4 = 0;
    v_stack_mE0 = 0;
    result = SeCaptureSubjectContext(v_stack_m78, result + 2, a3, a4);
    v_stack_m120 = v_stack_mE0;
    v_stack_m128 = v_stack_mA4;
    v_stack_m130 = 1;
    v_stack_m138 = v_rip + 2362466;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    a3 = 0;
    result = SeAccessCheck(*(unsigned __int64 *)(v_stack_mF0 + 72), v_stack_m78, a3, 0 + 1);
    result = SeReleaseSubjectContext(v_stack_m78, v_stack_m78, a3, 0 + 1);
    if (sign_flag) goto loc_0090A45C;
loc_0090A44C:
    if (*(unsigned __int64 *)(v_stack_mF0 + 64) != 0) goto loc_0090A629;
loc_0090A459:
loc_0090A45C:
    v_stack_m118 = 0;
    if (!sign_flag) goto loc_0090A59D;
loc_0090A468:
    if (v_stack_mF0 == 0) goto loc_0090A48F;
    a1 = (v_stack_mF0) + (8);
    result = (*(unsigned __int64 *)(a1)) & (-2);
    if (condition_is_not_equal) goto loc_0090A674;
loc_0090A48F:
    if (v_stack_mE8 == 0) goto loc_0090A4B9;
    a1 = (v_stack_mE8) + (8);
    result = (*(unsigned __int64 *)(a1)) & (-2);
    if (condition_is_not_equal) goto loc_0090A67E;
loc_0090A4B9:
    if (v_stack_mD0 != 0) {
        a2 = 0x20666E57ULL;
        a1 = v_stack_mD0;
        result = ExFreePoolWithTag(a1, a2, a3, 0 + 1);
    }
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, 0 + 1);
    if ((unsigned int)((unsigned int)(v_stack_m10C)) != 0) goto loc_0090A5F2;
loc_0090A4ED:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, 0 + 1);
    v_rsp = (v_rsp) + (304);
    return result;
loc_0090A515:
    goto loc_0090A310;
loc_0090A51D:
    v_r12 = 0;
    goto loc_0090A357;
loc_0090A528:
    if (v_stack_pC0 == 3) goto loc_0090A39E;
    result = ExpWnfLookupPermanentName(v_stack_p70, v_stack_p98, a3, 0 + 1);
    v_stack_p50 = (unsigned int)(result);
    if (sign_flag) goto loc_0090A468;
    v_stack_p20 = 0;
    a3 = 0;
    result = ExpWnfValidatePubSubPreconditions(a3 + 1, v_stack_p98, a3, v_stack_pD0);
    v_stack_p50 = (unsigned int)(result);
    if (sign_flag) goto loc_0090A468;
    if (v_stack_p5C == 5) goto loc_0090A6FE;
    if (((v_stack_pD8) & (1)) != 0) goto loc_0090A6FE;
loc_0090A59D:
    if (v_stack_p78 == 0) goto loc_0090A5D3;
    v_stack_p20 = v_stack_pB0;
    result = ExpWnfReadStateData(v_stack_p78, v_stack_pB8, v_stack_m100, (unsigned int)(v_stack_p60));
    v_stack_p50 = (unsigned int)(result);
    goto loc_0090A5DE;
loc_0090A5D3:
    *(unsigned int *)(v_stack_pB8) = 0;
    *(unsigned int *)(result) = 0;
    v_stack_p50 = 0;
loc_0090A5DE:
    goto loc_0090A468;
loc_0090A5F2:
    a1 = (unsigned int)((v_stack_p78) - (1));
    if (condition_is_equal) goto loc_0090A640;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0090A6CF;
    if (((unsigned int)(a1)) != 1) goto loc_0090A4ED;
    if (v_stack_pA0 == 0) goto loc_0090A4ED;
loc_0090A61F:
    result = ObfDereferenceObjectWithTag(v_stack_pA0, (unsigned int)(0x20666E57ULL), v_stack_m100, (unsigned int)(v_stack_p60));
    goto loc_0090A4ED;
loc_0090A629:
    if (v_stack_pD0 != 0) goto loc_0090A69D;
    goto loc_0090A45C;
loc_0090A640:
    if (v_stack_pA0 == 0) goto loc_0090A4ED;
    goto loc_0090A61F;
loc_0090A658:
    result = ExpWnfCheckCrossScopeAccess(v_stack_p70, (unsigned int)(0x79517350ULL), v_stack_m100, (unsigned int)(v_stack_p60));
    v_stack_p50 = (unsigned int)(result);
    if (sign_flag) goto loc_0090A468;
    v_r11 = 0;
    goto loc_0090A256;
loc_0090A674:
    result = ExfReleaseRundownProtection(v_stack_p70, (unsigned int)(0x79517350ULL), v_stack_m100, (unsigned int)(v_stack_p60));
    goto loc_0090A48F;
loc_0090A67E:
    result = ExfReleaseRundownProtection(v_stack_p70, (unsigned int)(0x79517350ULL), v_stack_m100, (unsigned int)(v_stack_p60));
    goto loc_0090A4B9;
loc_0090A688:
    goto loc_0090A38F;
loc_0090A692:
    goto loc_0090A256;
loc_0090A69D:
    a3 = (*(unsigned __int64 *)(v_stack_p70)) - (*(unsigned __int64 *)((unsigned int)(0x79517350ULL)));
    if (!(condition_is_not_equal)) {
        a3 = *(unsigned __int64 *)(v_stack_p70 + 8);
        a3 = (a3) - (*(unsigned __int64 *)((unsigned int)(0x79517350ULL) + 8));
    }
    if (a3 == 0) goto loc_0090A459;
    goto loc_0090A45C;
loc_0090A6C0:
    goto loc_0090A273;
loc_0090A6CF:
    if (v_stack_pA0 == 0) goto loc_0090A4ED;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) != 1) goto loc_0090A4ED;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_pA0, a2, 0, (unsigned int)(v_stack_p60));
    goto loc_0090A4ED;
loc_0090A6F6:
    v_r12 = 0;
    goto loc_0090A357;
loc_0090A6FE:
    v_stack_p20 = v_stack_p78;
    result = ExpWnfCreateNameInstance(v_stack_p80, v_stack_p70, v_stack_p98, *(unsigned __int64 *)(v_rip + 7062502));
    v_stack_p50 = (unsigned int)(result);
    result = ExFreePoolWithTag(v_stack_p98, (unsigned int)(0x20666E57ULL), v_stack_p98, *(unsigned __int64 *)(v_rip + 7062502));
    v_stack_p98 = 0;
    if (!sign_flag) goto loc_0090A59D;
    goto loc_0090A468;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryWnfStateData(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint32_t v_stack_m10C;
    uint32_t v_stack_m110;
    uint8_t v_stack_m114;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p20;
    uint32_t v_stack_p50;
    uint8_t v_stack_p54;
    uint32_t v_stack_p5C;
    uint32_t v_stack_p60;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint32_t v_stack_pC0;
    uint64_t v_stack_pD0;
    uint8_t v_stack_pD8;

    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x500936)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mB0 = Arg4;
    v_stack_mB8 = Arg6;
    v_stack_m100 = Arg5;
    v_stack_m58 = v_xmm0;
    local_r11 = 0;
    v_stack_m108 = 0;
    v_stack_mD8 = 0;
    v_stack_m114 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_mD0 = 0;
    v_stack_mE8 = 0;
    v_stack_mF0 = 0;
    v_stack_m10C = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_m98 = Arg2;
    v_stack_mA0 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_0090A177;
    v_stack_mA0 = *(uint64_t *)(arg1);
loc_00909ED5:
    local_rbx = (*(uint64_t *)(arg1)) ^ (*(uint64_t *)(gs_base + (0 + 0x188)));
    v_stack_mF8 = local_rbx;
    result = (uint8_t)(((uint8_t)(local_rbx)) & (15));
    if (((uint8_t)(result)) != 1) goto loc_0090A16A;
    local_rdi = (local_rbx) >> (6);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (15));
    local_r14 = (local_rbx) >> (4);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (3));
    result = (local_rbx) >> (10);
    v_stack_m90 = result;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (1));
    if (((uint32_t)(Arg1)) != 3) goto loc_0090A150;
loc_00909F2C:
    if (((uint32_t)(Arg2)) != 5) goto loc_0090A1B4;
loc_00909F35:
    if ((uint32_t)(Arg3) != 0) goto loc_0090A0BC;
loc_00909F3E:
    v_stack_m118 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_0090A0A5;
    local_r10 = Arg4;
    if (Arg2 != 0) {
        Arg2 = local_rsi;
        if (Arg2 < local_rsi) { Arg2 = Arg2; }
        Arg3 = 16;
        Arg1 = v_stack_m58;
        result = RtlCopyVolatileMemory(Arg1, Arg2, Arg3, Arg6);
        result = v_stack_m58;
        v_stack_m98 = result;
        Arg4 = v_stack_mB8;
        local_r10 = v_stack_mB0;
        local_r11 = 0;
    }
    Arg1 = local_rsi;
    if (local_r10 < local_rsi) { Arg1 = local_r10; }
    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    result = local_rsi;
    if (Arg4 < local_rsi) { result = Arg4; }
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    Arg1 = local_rsi;
    if (Arg4 < local_rsi) { Arg1 = Arg4; }
    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result))) == 0) goto loc_0090A008;
    Arg2 = (v_stack_m100 - 1) + ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result)))));
    if (v_stack_m100 > Arg2) goto loc_0090A0B6;
    if (Arg2 >= local_rsi) goto loc_0090A0B6;
    Arg2 = (Arg2) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (Arg2) + (0x1000ULL);
loc_00909FF0:
    *(uint8_t *)(v_stack_m100) = (uint8_t)(*(uint8_t *)(v_stack_m100));
    Arg1 = (v_stack_m100) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) + (0x1000ULL);
    if (Arg1 != Arg2) goto loc_00909FF0;
loc_0090A008:
loc_0090A00D:
    local_r14 = (uint32_t)((local_r14) & (3));
    v_stack_mA8 = (uint32_t)(local_r14);
    local_rdi = (uint32_t)((local_rdi) & (15));
    v_stack_m10C = (uint32_t)(local_rdi);
    v_stack_m110 = 0;
    if (Arg3 != 0) goto loc_0090A03C;
    v_stack_mD8 = 0;
    v_stack_m118 = 0;
    goto loc_0090A230;
loc_0090A03C:
    if (((uint32_t)(local_rdi)) != 3) goto loc_0090A0D6;
    v_stack_m130 = 0;
    v_stack_m138 = 0;
    v_stack_m140 = v_stack_mC8;
    v_stack_m148 = 0x20666E57ULL;
    Arg2 = 0;
    result = ObpReferenceObjectByHandleWithTag(Arg3, Arg2, *(uint64_t *)(v_rip + 0x6BCA4C), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m110 = (uint32_t)(result);
    local_r11 = 0;
    if (sign_flag) goto loc_0090A094;
loc_0090A08C:
    v_stack_mD8 = v_stack_mC8;
loc_0090A094:
    v_stack_m118 = (uint32_t)(result);
    if (!sign_flag) goto loc_0090A230;
    goto loc_0090A468;
loc_0090A0A5:
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))));
    goto loc_0090A00D;
loc_0090A0B6:
    result = ExRaiseAccessViolation(v_stack_mC8, Arg2, *(uint64_t *)(v_rip + 0x6BCA4C), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
loc_0090A0BC:
    if (((0) & (0xFFFFFFF9ULL)) != 0) goto loc_0090A16A;
    if (0 != 6) goto loc_00909F3E;
    goto loc_0090A16A;
loc_0090A0D6:
    if ((uint32_t)(local_rdi) == 0) goto loc_0090A126;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (1));
    if (condition_is_not_equal) goto loc_0090A1E3;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_0090A134;
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3)));
loc_0090A0F5:
    result = PsGetSessionById((uint32_t)(*(uint32_t *)(Arg3)), Arg2, *(uint64_t *)(v_rip + 0x6BCA4C), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_mC8 = result;
    local_r11 = 0;
    if (result == 0) goto loc_0090A126;
    v_stack_mD8 = v_stack_mC0;
    v_stack_m110 = 0;
    goto loc_0090A094;
loc_0090A126:
    v_stack_m110 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_0090A094;
loc_0090A134:
    if (Arg3 < local_rsi) { local_rsi = Arg3; }
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)));
    goto loc_0090A0F5;
loc_0090A150:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))) == 0) goto loc_00909F2C;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) - (1));
    if (condition_is_equal) goto loc_00909F2C;
    if (((uint32_t)(Arg1)) == 1) goto loc_00909F2C;
loc_0090A16A:
    v_stack_m118 = 0xC000000DULL;
    goto loc_0090A468;
loc_0090A177:
    Arg2 = local_rsi;
    if (Arg1 < local_rsi) { Arg2 = Arg1; }
    result = RtlCopyVolatileMemory(v_stack_mA0, Arg2, 8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    local_r11 = 0;
    goto loc_00909ED5;
loc_0090A1B4:
    if ((uint32_t)(Arg2) == 0) goto loc_00909F35;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - (1));
    if (condition_is_equal) goto loc_00909F35;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00909F35;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00909F35;
    if (((uint32_t)(Arg1)) != 1) goto loc_0090A16A;
    goto loc_00909F35;
loc_0090A1E3:
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0090A1F6;
    v_stack_m110 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_0090A094;
loc_0090A1F6:
    v_stack_m138 = v_stack_mC8;
    v_stack_m140 = 0;
    result = SeCaptureSid(Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 8, v_stack_mB8);
    v_stack_m110 = (uint32_t)(result);
    local_r11 = 0;
    if (sign_flag) goto loc_0090A094;
    goto loc_0090A08C;
loc_0090A230:
    goto loc_0090A241;
loc_0090A241:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_0090A692;
    if (Arg3 != 0) goto loc_0090A658;
loc_0090A256:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_0090A6C0;
loc_0090A273:
    v_stack_m148 = v_stack_mD8;
    result = ExpWnfResolveScopeInstance(v_stack_mE8, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m10C))));
    v_stack_m118 = (uint32_t)(result);
    if (sign_flag) goto loc_0090A468;
    local_rbx = (v_stack_mE8) + (48);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbx, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(v_stack_m10C))));
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_rbx;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_rbx;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(v_stack_mE8 + 0x38) == 0) goto loc_0090A51D;
loc_0090A300:
    if (v_stack_mF8 < (*(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x38) + 0x18))) goto loc_0090A515;
    if (v_stack_mF8 <= (*(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x38) + 0x18))) goto loc_0090A315;
loc_0090A310:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x38) + 0x8) != 0) goto loc_0090A300;
loc_0090A315:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x38) + 0x8) == 0) goto loc_0090A51D;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x38) + 0x8) - 16 == 0) goto loc_0090A6F6;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x38) + 0x8) - 0x10 + 0x8)) & (-2);
    if (condition_is_equal) goto loc_0090A6F6;
    result = ExfAcquireRundownProtection(*(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x38) + 0x8) - 16 + 8, result + 2, Arg3, Arg4);
    local_r12 = 0;
    local_rbx = *(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x38) + 0x8) - 16;
    if ((uint8_t)(result) == 0) {
        local_rbx = 0;
    }
    result = 17;
    if ((uint8_t)(result) != 0) {
        Arg1 = v_stack_mE8 + 48;
        result = ExfReleasePushLockShared(Arg1, result + 2, Arg3, Arg4);
    }
    result = KeAbPostRelease(v_stack_mE8 + 48, result + 2, Arg3, Arg4);
    if (local_rbx == 0) goto loc_0090A688;
    v_stack_mF0 = local_rbx;
loc_0090A38F:
    v_stack_m118 = 0;
    if (0 == 0xC0000034ULL) goto loc_0090A528;
loc_0090A39E:
    if (sign_flag) goto loc_0090A468;
    if (0 != 0) goto loc_0090A44C;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_mA4 = 0;
    v_stack_mE0 = 0;
    result = SeCaptureSubjectContext(v_stack_m78, result + 2, Arg3, Arg4);
    v_stack_m120 = v_stack_mE0;
    v_stack_m128 = v_stack_mA4;
    v_stack_m130 = 1;
    v_stack_m138 = v_rip + 2362466;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    Arg3 = 0;
    result = SeAccessCheck(*(uint64_t *)(v_stack_mF0 + 0x48), v_stack_m78, Arg3, 0 + 1);
    result = SeReleaseSubjectContext(v_stack_m78, v_stack_m78, Arg3, 0 + 1);
    if (sign_flag) goto loc_0090A45C;
loc_0090A44C:
    if (*(uint64_t *)(v_stack_mF0 + 0x40) != 0) goto loc_0090A629;
loc_0090A459:
loc_0090A45C:
    v_stack_m118 = 0;
    if (!sign_flag) goto loc_0090A59D;
loc_0090A468:
    if (v_stack_mF0 == 0) goto loc_0090A48F;
    Arg1 = (v_stack_mF0) + (8);
    result = (*(uint64_t *)(arg1)) & (-2);
    if (condition_is_not_equal) goto loc_0090A674;
loc_0090A48F:
    if (v_stack_mE8 == 0) goto loc_0090A4B9;
    Arg1 = (v_stack_mE8) + (8);
    result = (*(uint64_t *)(arg1)) & (-2);
    if (condition_is_not_equal) goto loc_0090A67E;
loc_0090A4B9:
    if (v_stack_mD0 != 0) {
        Arg2 = 0x20666E57ULL;
        Arg1 = v_stack_mD0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, 0 + 1);
    }
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, 0 + 1);
    if ((uint32_t)((uint32_t)(v_stack_m10C)) != 0) goto loc_0090A5F2;
loc_0090A4ED:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, 0 + 1);
    local_rsp = (local_rsp) + (304);
    return result;
loc_0090A515:
    goto loc_0090A310;
loc_0090A51D:
    local_r12 = 0;
    goto loc_0090A357;
loc_0090A528:
    if (v_stack_pC0 == 3) goto loc_0090A39E;
    result = ExpWnfLookupPermanentName(v_stack_p70, v_stack_p98, Arg3, 0 + 1);
    v_stack_p50 = (uint32_t)(result);
    if (sign_flag) goto loc_0090A468;
    v_stack_p20 = 0;
    Arg3 = 0;
    result = ExpWnfValidatePubSubPreconditions(Arg3 + 1, v_stack_p98, Arg3, v_stack_pD0);
    v_stack_p50 = (uint32_t)(result);
    if (sign_flag) goto loc_0090A468;
    if (v_stack_p5C == 5) goto loc_0090A6FE;
    if (((v_stack_pD8) & (1)) != 0) goto loc_0090A6FE;
loc_0090A59D:
    if (v_stack_p78 == 0) goto loc_0090A5D3;
    v_stack_p20 = v_stack_pB0;
    result = ExpWnfReadStateData(v_stack_p78, v_stack_pB8, v_stack_m100, (uint32_t)(v_stack_p60));
    v_stack_p50 = (uint32_t)(result);
    goto loc_0090A5DE;
loc_0090A5D3:
    *(uint32_t *)(v_stack_pB8) = 0;
    *(uint32_t *)(result) = 0;
    v_stack_p50 = 0;
loc_0090A5DE:
    goto loc_0090A468;
loc_0090A5F2:
    Arg1 = (uint32_t)((v_stack_p78) - (1));
    if (condition_is_equal) goto loc_0090A640;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0090A6CF;
    if (((uint32_t)(Arg1)) != 1) goto loc_0090A4ED;
    if (v_stack_pA0 == 0) goto loc_0090A4ED;
loc_0090A61F:
    result = ObfDereferenceObjectWithTag(v_stack_pA0, (uint32_t)(0x20666E57ULL), v_stack_m100, (uint32_t)(v_stack_p60));
    goto loc_0090A4ED;
loc_0090A629:
    if (v_stack_pD0 != 0) goto loc_0090A69D;
    goto loc_0090A45C;
loc_0090A640:
    if (v_stack_pA0 == 0) goto loc_0090A4ED;
    goto loc_0090A61F;
loc_0090A658:
    result = ExpWnfCheckCrossScopeAccess(v_stack_p70, (uint32_t)(0x79517350ULL), v_stack_m100, (uint32_t)(v_stack_p60));
    v_stack_p50 = (uint32_t)(result);
    if (sign_flag) goto loc_0090A468;
    local_r11 = 0;
    goto loc_0090A256;
loc_0090A674:
    result = ExfReleaseRundownProtection(v_stack_p70, (uint32_t)(0x79517350ULL), v_stack_m100, (uint32_t)(v_stack_p60));
    goto loc_0090A48F;
loc_0090A67E:
    result = ExfReleaseRundownProtection(v_stack_p70, (uint32_t)(0x79517350ULL), v_stack_m100, (uint32_t)(v_stack_p60));
    goto loc_0090A4B9;
loc_0090A688:
    goto loc_0090A38F;
loc_0090A692:
    goto loc_0090A256;
loc_0090A69D:
    Arg3 = (*(uint64_t *)(v_stack_p70)) - (*(uint64_t *)((uint32_t)(0x79517350ULL)));
    if (!(condition_is_not_equal)) {
        Arg3 = *(uint64_t *)(v_stack_p70 + 0x8);
        Arg3 = (Arg3) - (*(uint64_t *)((uint32_t)(0x79517350ULL) + 0x8));
    }
    if (Arg3 == 0) goto loc_0090A459;
    goto loc_0090A45C;
loc_0090A6C0:
    goto loc_0090A273;
loc_0090A6CF:
    if (v_stack_pA0 == 0) goto loc_0090A4ED;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) != 1) goto loc_0090A4ED;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_pA0, Arg2, 0, (uint32_t)(v_stack_p60));
    goto loc_0090A4ED;
loc_0090A6F6:
    local_r12 = 0;
    goto loc_0090A357;
loc_0090A6FE:
    v_stack_p20 = v_stack_p78;
    result = ExpWnfCreateNameInstance(v_stack_p80, v_stack_p70, v_stack_p98, *(uint64_t *)(v_rip + 0x6BC3E6));
    v_stack_p50 = (uint32_t)(result);
    result = ExFreePoolWithTag(v_stack_p98, (uint32_t)(0x20666E57ULL), v_stack_p98, *(uint64_t *)(v_rip + 0x6BC3E6));
    v_stack_p98 = 0;
    if (!sign_flag) goto loc_0090A59D;
    goto loc_0090A468;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00909DF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
