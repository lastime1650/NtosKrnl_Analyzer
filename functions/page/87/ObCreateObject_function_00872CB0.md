# ObCreateObject

- RVA: `0x00872CB0`–`0x008731C0` (길이 `1,296` bytes)
- VA: `0x0000000140872CB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C674`
- 디코드: `322`개 명령, `1,296/1,296` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00872D18` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x00872D35` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x00872D53` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00872D8A` → [ObpCaptureObjectCreateInformation](../89/ObpCaptureObjectCreateInformation_function_0089B930.md) (function, `0x0089B930`)
- `0x00872DF1` → [ObpAllocateObject](../89/ObpAllocateObject_function_00899FF0.md) (function, `0x00899FF0`)
- `0x00872E43` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x00872E59` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00872E89` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x00872E97` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00872ECE` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x00872F15` → [SepPrivilegeCheck](../../text/40/SepPrivilegeCheck_function_0040B6B0.md) (function, `0x0040B6B0`)
- `0x00872F44` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x00872F55` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00872FC1` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00872FCD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00872FEC` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x00873003` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x00873034` → [SepAdtPrivilegedServiceAuditAlarm](SepAdtPrivilegedServiceAuditAlarm_function_008714F0.md) (function, `0x008714F0`)
- `0x0087314E` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00873169` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x0087317D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00873191` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0087319E` → [ObpRegisterObject](../AC/ObpRegisterObject_function_00ACF3EC.md) (function, `0x00ACF3EC`)
- `0x008731B6` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)

### Direct callers
- [PopPowerRequestCreateCommon](../../text/23/PopPowerRequestCreateCommon_function_00230150.md) at `0x00230216`
- [SepCreateTokenEx](../../text/4E/SepCreateTokenEx_function_004E9CD0.md) at `0x004EA2AC`
- [KiAllocatePrcbThread](../../text/5B/KiAllocatePrcbThread_function_005B9130.md) at `0x005B91B0`
- [ExCreateDpcEvent](../../text/65/ExCreateDpcEvent_function_00659520.md) at `0x0065959A`
- [CmpCreateRegistryRoot](../../init/C5/CmpCreateRegistryRoot_function_00C57880.md) at `0x00C5791D`
- [MiSectionInitialization](../../init/C6/MiSectionInitialization_function_00C644A4.md) at `0x00C6465C`
- [IopInitializeBuiltinDriver](../../init/C7/IopInitializeBuiltinDriver_function_00C7625C.md) at `0x00C76310`

### Static image references
- `0x00872CCC` → RVA `0x00E0A740` (`.data`; read)
- `0x00872E04` → RVA `0x00B82850` (`ExFreePool`; read)
- `0x00872EB8` → RVA `0x00FD9BD0` (`PAGEDATA`; read)
- `0x00872F3A` → RVA `0x00E67D58` (`.data`; read)
- `0x00872FD7` → RVA `0x00FD9AA0` (`PAGEDATA`; read)
- `0x0087301A` → RVA `0x000013A8` (`.rdata`; read)
- `0x00873050` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x00873071` → RVA `0x00FD8238` (`PAGEDATA`; read)
- `0x008730C7` → RVA `0x00B4BE28` (`SepServicesFilterPrivileges`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00872D18` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x00872D35` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x00872D53` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00872E43` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x00872E59` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00872E89` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x00872E97` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00872F15` → [SepPrivilegeCheck](../../text/40/SepPrivilegeCheck_function_0040B6B0.md) (`PAGE` → `.text`)
  - `0x00872F44` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x00872FC1` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00872FCD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00872FEC` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x00873003` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x0087314E` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x0087317D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00873191` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008731B6` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00872CB0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00872CB5  55                              push rbp
00872CB6  56                              push rsi
00872CB7  57                              push rdi
00872CB8  41 54                           push r12
00872CBA  41 55                           push r13
00872CBC  41 56                           push r14
00872CBE  41 57                           push r15
00872CC0  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
00872CC5  48 81 EC B0 00 00 00            sub rsp, 0xb0
00872CCC  48 8B 05 6D 7A 59 00            mov rax, qword ptr [rip + 0x597a6d]
00872CD3  48 33 C4                        xor rax, rsp
00872CD6  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00872CDA  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
00872CE3  44 0F B6 F9                     movzx r15d, cl
00872CE7  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
00872CEE  0F 57 C0                        xorps xmm0, xmm0
00872CF1  45 0F B6 E9                     movzx r13d, r9b
00872CF5  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00872CF9  4D 8B E0                        mov r12, r8
00872CFC  48 C7 45 A7 00 00 00 00         mov qword ptr [rbp - 0x59], 0
00872D04  48 8B 9E 40 08 00 00            mov rbx, qword ptr [rsi + 0x840]
00872D0B  4C 8B F2                        mov r14, rdx
00872D0E  48 8B CB                        mov rcx, rbx
00872D11  0F 11 45 97                     movups xmmword ptr [rbp - 0x69], xmm0
00872D15  FF 43 14                        inc dword ptr [rbx + 0x14]
00872D18  E8 53 78 E4 FF                  call 0x1406ba570
00872D1D  48 8B F8                        mov rdi, rax
00872D20  48 85 C0                        test rax, rax
00872D23  75 3B                           jne 0x140872d60
00872D25  FF 43 18                        inc dword ptr [rbx + 0x18]
00872D28  48 8B 9E 48 08 00 00            mov rbx, qword ptr [rsi + 0x848]
00872D2F  48 8B CB                        mov rcx, rbx
00872D32  FF 43 14                        inc dword ptr [rbx + 0x14]
00872D35  E8 36 78 E4 FF                  call 0x1406ba570
00872D3A  48 8B F8                        mov rdi, rax
00872D3D  48 85 C0                        test rax, rax
00872D40  75 1E                           jne 0x140872d60
00872D42  8B 53 2C                        mov edx, dword ptr [rbx + 0x2c]
00872D45  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
00872D49  44 8B 43 28                     mov r8d, dword ptr [rbx + 0x28]
00872D4D  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
00872D50  FF 43 18                        inc dword ptr [rbx + 0x18]
00872D53  E8 78 7D E4 FF                  call 0x1406baad0
00872D58  48 8B F8                        mov rdi, rax
00872D5B  48 85 C0                        test rax, rax
00872D5E  74 05                           je 0x140872d65
00872D60  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
00872D63  89 07                           mov dword ptr [rdi], eax
00872D65  48 85 FF                        test rdi, rdi
00872D68  0F 84 05 04 00 00               je 0x140873173
00872D6E  C7 44 24 28 00 00 00 00         mov dword ptr [rsp + 0x28], 0
00872D76  4C 8D 4D 97                     lea r9, [rbp - 0x69]
00872D7A  4D 8B C4                        mov r8, r12
00872D7D  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00872D82  41 0F B6 D5                     movzx edx, r13b
00872D86  41 0F B6 CF                     movzx ecx, r15b
00872D8A  E8 A1 8B 02 00                  call 0x14089b930
00872D8F  8B D8                           mov ebx, eax
00872D91  85 C0                           test eax, eax
00872D93  0F 88 D4 01 00 00               js 0x140872f6d
00872D99  8B 0F                           mov ecx, dword ptr [rdi]
00872D9B  41 85 4E 48                     test dword ptr [r14 + 0x48], ecx
00872D9F  0F 85 E2 03 00 00               jne 0x140873187
00872DA5  F6 C1 10                        test cl, 0x10
00872DA8  0F 85 0A 01 00 00               jne 0x140872eb8
00872DAE  8B 4D 77                        mov ecx, dword ptr [rbp + 0x77]
00872DB1  85 C9                           test ecx, ecx
00872DB3  75 04                           jne 0x140872db9
00872DB5  41 8B 4E 68                     mov ecx, dword ptr [r14 + 0x68]
00872DB9  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
00872DBC  85 C0                           test eax, eax
00872DBE  75 04                           jne 0x140872dc4
00872DC0  41 8B 46 6C                     mov eax, dword ptr [r14 + 0x6c]
00872DC4  89 47 18                        mov dword ptr [rdi + 0x18], eax
00872DC7  4C 8D 4D 97                     lea r9, [rbp - 0x69]
00872DCB  48 8D 45 A7                     lea rax, [rbp - 0x59]
00872DCF  48 C7 44 24 30 00 00 00 00      mov qword ptr [rsp + 0x30], 0
00872DD8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00872DDD  4D 8B C6                        mov r8, r14
00872DE0  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
00872DE3  41 0F B6 D5                     movzx edx, r13b
00872DE7  89 4F 14                        mov dword ptr [rdi + 0x14], ecx
00872DEA  48 8B CF                        mov rcx, rdi
00872DED  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00872DF1  E8 FA 71 02 00                  call 0x140899ff0
00872DF6  8B D8                           mov ebx, eax
00872DF8  85 C0                           test eax, eax
00872DFA  0F 89 50 02 00 00               jns 0x140873050
00872E00  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00872E04  48 8D 35 45 FA 30 00            lea rsi, [rip + 0x30fa45]
00872E0B  48 85 C9                        test rcx, rcx
00872E0E  74 38                           je 0x140872e48
00872E10  B8 F8 00 00 00                  mov eax, 0xf8
00872E15  66 39 45 99                     cmp word ptr [rbp - 0x67], ax
00872E19  0F 85 AC 01 00 00               jne 0x140872fcb
00872E1F  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00872E28  48 8B 8A 50 08 00 00            mov rcx, qword ptr [rdx + 0x850]
00872E2F  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00872E32  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00872E36  66 39 01                        cmp word ptr [rcx], ax
00872E39  0F 83 E5 02 00 00               jae 0x140873124
00872E3F  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
00872E43  E8 68 77 E4 FF                  call 0x1406ba5b0
00872E48  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00872E4C  48 85 C9                        test rcx, rcx
00872E4F  74 15                           je 0x140872e66
00872E51  80 7F 10 01                     cmp byte ptr [rdi + 0x10], 1
00872E55  77 07                           ja 0x140872e5e
00872E57  33 D2                           xor edx, edx
00872E59  E8 12 FA 30 00                  call 0x140b82870
00872E5E  48 C7 47 20 00 00 00 00         mov qword ptr [rdi + 0x20], 0
00872E66  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00872E6F  48 8B 8A 40 08 00 00            mov rcx, qword ptr [rdx + 0x840]
00872E76  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00872E79  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00872E7D  66 39 01                        cmp word ptr [rcx], ax
00872E80  0F 83 7F 02 00 00               jae 0x140873105
00872E86  48 8B D7                        mov rdx, rdi
00872E89  E8 22 77 E4 FF                  call 0x1406ba5b0
00872E8E  8B C3                           mov eax, ebx
00872E90  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
00872E94  48 33 CC                        xor rcx, rsp
00872E97  E8 A4 97 E3 FF                  call 0x1406ac640
00872E9C  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00872EA4  48 81 C4 B0 00 00 00            add rsp, 0xb0
00872EAB  41 5F                           pop r15
00872EAD  41 5E                           pop r14
00872EAF  41 5D                           pop r13
00872EB1  41 5C                           pop r12
00872EB3  5F                              pop rdi
00872EB4  5E                              pop rsi
00872EB5  5D                              pop rbp
00872EB6  C3                              ret
00872EB7  CC                              int3
00872EB8  48 8B 1D 11 6D 76 00            mov rbx, qword ptr [rip + 0x766d11]
00872EBF  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00872EC3  0F 57 C0                        xorps xmm0, xmm0
00872EC6  0F 11 45 AF                     movups xmmword ptr [rbp - 0x51], xmm0
00872ECA  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
00872ECE  E8 4D 89 FF FF                  call 0x14086b820
00872ED3  48 89 5D E7                     mov qword ptr [rbp - 0x19], rbx
00872ED7  BE 01 00 00 00                  mov esi, 1
00872EDC  89 75 DF                        mov dword ptr [rbp - 0x21], esi
00872EDF  89 75 E3                        mov dword ptr [rbp - 0x1d], esi
00872EE2  C7 45 EF 00 00 00 00            mov dword ptr [rbp - 0x11], 0
00872EE9  45 84 FF                        test r15b, r15b
00872EEC  0F 84 73 02 00 00               je 0x140873165
00872EF2  48 8B 5D AF                     mov rbx, qword ptr [rbp - 0x51]
00872EF6  48 85 DB                        test rbx, rbx
00872EF9  0F 85 3F 01 00 00               jne 0x14087303e
00872EFF  48 8B 5D BF                     mov rbx, qword ptr [rbp - 0x41]
00872F03  44 8B CE                        mov r9d, esi
00872F06  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
00872F0B  44 8B C6                        mov r8d, esi
00872F0E  48 8D 55 E7                     lea rdx, [rbp - 0x19]
00872F12  48 8B CB                        mov rcx, rbx
00872F15  E8 96 87 B9 FF                  call 0x14040b6b0
00872F1A  48 8B 5D AF                     mov rbx, qword ptr [rbp - 0x51]
00872F1E  44 0F B6 F8                     movzx r15d, al
00872F22  8B 75 DF                        mov esi, dword ptr [rbp - 0x21]
00872F25  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
00872F29  48 85 DB                        test rbx, rbx
00872F2C  48 0F 45 CB                     cmovne rcx, rbx
00872F30  48 8B 89 98 00 00 00            mov rcx, qword ptr [rcx + 0x98]
00872F37  4C 8B 21                        mov r12, qword ptr [rcx]
00872F3A  48 8B 0D 17 4E 5F 00            mov rcx, qword ptr [rip + 0x5f4e17]
00872F41  49 8B D4                        mov rdx, r12
00872F44  E8 87 DB B8 FF                  call 0x140400ad0
00872F49  84 C0                           test al, al
00872F4B  0F 84 86 00 00 00               je 0x140872fd7
00872F51  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00872F55  E8 B6 87 FF FF                  call 0x14086b710
00872F5A  45 84 FF                        test r15b, r15b
00872F5D  0F 85 4B FE FF FF               jne 0x140872dae
00872F63  BB 61 00 00 C0                  mov ebx, 0xc0000061
00872F68  E9 93 FE FF FF                  jmp 0x140872e00
00872F6D  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00872F76  48 8B 8A 40 08 00 00            mov rcx, qword ptr [rdx + 0x840]
00872F7D  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00872F80  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00872F84  66 39 01                        cmp word ptr [rcx], ax
00872F87  0F 82 F9 FE FF FF               jb 0x140872e86
00872F8D  FF 41 20                        inc dword ptr [rcx + 0x20]
00872F90  48 8B 8A 48 08 00 00            mov rcx, qword ptr [rdx + 0x848]
00872F97  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00872F9A  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00872F9E  66 39 01                        cmp word ptr [rcx], ax
00872FA1  0F 82 DF FE FF FF               jb 0x140872e86
00872FA7  48 8D 35 A2 F8 30 00            lea rsi, [rip + 0x30f8a2]
00872FAE  FF 41 20                        inc dword ptr [rcx + 0x20]
00872FB1  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00872FB5  48 8B CF                        mov rcx, rdi
00872FB8  48 3B C6                        cmp rax, rsi
00872FBB  0F 85 BC 01 00 00               jne 0x14087317d
00872FC1  E8 8A F8 30 00                  call 0x140b82850
00872FC6  E9 C3 FE FF FF                  jmp 0x140872e8e
00872FCB  33 D2                           xor edx, edx
00872FCD  E8 9E F8 30 00                  call 0x140b82870
00872FD2  E9 71 FE FF FF                  jmp 0x140872e48
00872FD7  48 8B 05 C2 6A 76 00            mov rax, qword ptr [rip + 0x766ac2]
00872FDE  49 8B D4                        mov rdx, r12
00872FE1  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00872FE5  48 8B 88 88 01 00 00            mov rcx, qword ptr [rax + 0x188]
00872FEC  E8 DF DA B8 FF                  call 0x140400ad0
00872FF1  84 C0                           test al, al
00872FF3  75 7C                           jne 0x140873071
00872FF5  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00872FF9  49 8B D4                        mov rdx, r12
00872FFC  48 8B 89 80 01 00 00            mov rcx, qword ptr [rcx + 0x180]
00873003  E8 C8 DA B8 FF                  call 0x140400ad0
00873008  84 C0                           test al, al
0087300A  75 65                           jne 0x140873071
0087300C  48 8D 45 DF                     lea rax, [rbp - 0x21]
00873010  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
00873015  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0087301A  48 8D 15 87 E3 78 FF            lea rdx, [rip - 0x871c79]
00873021  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
00873025  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00873029  4C 8B CB                        mov r9, rbx
0087302C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00873031  45 33 C0                        xor r8d, r8d
00873034  E8 B7 E4 FF FF                  call 0x1408714f0
00873039  E9 13 FF FF FF                  jmp 0x140872f51
0087303E  83 7D B7 02                     cmp dword ptr [rbp - 0x49], 2
00873042  0F 8D BB FE FF FF               jge 0x140872f03
00873048  45 32 FF                        xor r15b, r15b
0087304B  E9 D5 FE FF FF                  jmp 0x140872f25
00873050  83 3D B9 1F 75 00 00            cmp dword ptr [rip + 0x751fb9], 0
00873057  48 8B 7D A7                     mov rdi, qword ptr [rbp - 0x59]
0087305B  0F 85 3A 01 00 00               jne 0x14087319b
00873061  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
00873065  48 8D 4F 30                     lea rcx, [rdi + 0x30]
00873069  48 89 08                        mov qword ptr [rax], rcx
0087306C  E9 1D FE FF FF                  jmp 0x140872e8e
00873071  4C 8B 15 C0 51 76 00            mov r10, qword ptr [rip + 0x7651c0]
00873078  45 33 DB                        xor r11d, r11d
0087307B  85 F6                           test esi, esi
0087307D  0F 84 CE FE FF FF               je 0x140872f51
00873083  48 8D 55 E7                     lea rdx, [rbp - 0x19]
00873087  44 8B CE                        mov r9d, esi
0087308A  44 8B 02                        mov r8d, dword ptr [rdx]
0087308D  49 8B CA                        mov rcx, r10
00873090  49 8B 02                        mov rax, qword ptr [r10]
00873093  44 3B 00                        cmp r8d, dword ptr [rax]
00873096  74 0F                           je 0x1408730a7
00873098  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0087309C  48 83 C1 08                     add rcx, 8
008730A0  48 85 C0                        test rax, rax
008730A3  75 EE                           jne 0x140873093
008730A5  EB 0B                           jmp 0x1408730b2
008730A7  8B 40 04                        mov eax, dword ptr [rax + 4]
008730AA  39 42 04                        cmp dword ptr [rdx + 4], eax
008730AD  75 E9                           jne 0x140873098
008730AF  41 FF C3                        inc r11d
008730B2  48 83 C2 0C                     add rdx, 0xc
008730B6  49 83 E9 01                     sub r9, 1
008730BA  75 CE                           jne 0x14087308a
008730BC  85 F6                           test esi, esi
008730BE  74 37                           je 0x1408730f7
008730C0  48 8D 4D E7                     lea rcx, [rbp - 0x19]
008730C4  44 8B C6                        mov r8d, esi
008730C7  4C 8D 15 5A 8D 2D 00            lea r10, [rip + 0x2d8d5a]
008730CE  44 8B 09                        mov r9d, dword ptr [rcx]
008730D1  49 8B D2                        mov rdx, r10
008730D4  48 8B 05 4D 8D 2D 00            mov rax, qword ptr [rip + 0x2d8d4d]
008730DB  44 3B 08                        cmp r9d, dword ptr [rax]
008730DE  74 78                           je 0x140873158
008730E0  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
008730E4  48 83 C2 08                     add rdx, 8
008730E8  48 85 C0                        test rax, rax
008730EB  75 EE                           jne 0x1408730db
008730ED  48 83 C1 0C                     add rcx, 0xc
008730F1  49 83 E8 01                     sub r8, 1
008730F5  75 D7                           jne 0x1408730ce
008730F7  44 3B DE                        cmp r11d, esi
008730FA  0F 84 51 FE FF FF               je 0x140872f51
00873100  E9 07 FF FF FF                  jmp 0x14087300c
00873105  FF 41 20                        inc dword ptr [rcx + 0x20]
00873108  48 8B 8A 48 08 00 00            mov rcx, qword ptr [rdx + 0x848]
0087310F  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00873112  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00873116  66 39 01                        cmp word ptr [rcx], ax
00873119  0F 82 67 FD FF FF               jb 0x140872e86
0087311F  E9 8A FE FF FF                  jmp 0x140872fae
00873124  FF 41 20                        inc dword ptr [rcx + 0x20]
00873127  48 8B 8A 58 08 00 00            mov rcx, qword ptr [rdx + 0x858]
0087312E  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00873131  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00873135  66 39 01                        cmp word ptr [rcx], ax
00873138  0F 82 01 FD FF FF               jb 0x140872e3f
0087313E  FF 41 20                        inc dword ptr [rcx + 0x20]
00873141  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00873145  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00873149  48 3B C6                        cmp rax, rsi
0087314C  75 43                           jne 0x140873191
0087314E  E8 FD F6 30 00                  call 0x140b82850
00873153  E9 F0 FC FF FF                  jmp 0x140872e48
00873158  8B 40 04                        mov eax, dword ptr [rax + 4]
0087315B  39 41 04                        cmp dword ptr [rcx + 4], eax
0087315E  75 80                           jne 0x1408730e0
00873160  41 FF C3                        inc r11d
00873163  EB 88                           jmp 0x1408730ed
00873165  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00873169  E8 A2 85 FF FF                  call 0x14086b710
0087316E  E9 3B FC FF FF                  jmp 0x140872dae
00873173  B8 9A 00 00 C0                  mov eax, 0xc000009a
00873178  E9 13 FD FF FF                  jmp 0x140872e90
0087317D  E8 4E 79 E4 FF                  call 0x1406baad0
00873182  E9 07 FD FF FF                  jmp 0x140872e8e
00873187  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0087318C  E9 6F FC FF FF                  jmp 0x140872e00
00873191  E8 3A 79 E4 FF                  call 0x1406baad0
00873196  E9 AD FC FF FF                  jmp 0x140872e48
0087319B  48 8B CF                        mov rcx, rdi
0087319E  E8 49 C2 25 00                  call 0x140acf3ec
008731A3  41 B8 01 00 00 00               mov r8d, 1
008731A9  41 B9 44 66 6C 74               mov r9d, 0x746c6644
008731AF  41 0F B6 D0                     movzx edx, r8b
008731B3  48 8B CF                        mov rcx, rdi
008731B6  E8 29 D8 99 FF                  call 0x1402109e4
008731BB  E9 A1 FE FF FF                  jmp 0x140873061
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObCreateObject(unsigned __int8 a1, __int64 a2, __int64 a3, unsigned __int8 a4, __int64 a5, unsigned int a6, unsigned int a7, unsigned int a8, __int64 a9)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3F;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int16 v_stack_mA6;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 5864045)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m68 = a9;
    v_stack_m98 = 0;
    v_stack_mA8 = v_xmm0;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), a2, a3, a4);
    if (result != 0) goto loc_00872D60;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120), a2, a3, a4);
    if (result != 0) goto loc_00872D60;
    result = guard_dispatch_icall((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 36)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 44)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 40)), a4);
    if (result != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36);
        *(unsigned int *)(result) = (unsigned int)(result);
    }
    if (result == 0) goto loc_00873173;
    v_stack_mC0 = 0;
    v_stack_mC8 = result;
    result = ObpCaptureObjectCreateInformation(a1, a4, a3, v_stack_mA8);
    if (sign_flag) goto loc_00872F6D;
    if (((*(unsigned int *)(a2 + 72)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result))))) != 0) goto loc_00873187;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result)))) & (16)) != 0) goto loc_00872EB8;
loc_00872DAE:
    if ((unsigned int)((unsigned int)(a7)) == 0) {
        a1 = *(unsigned int *)(a2 + 104);
    }
    result = (unsigned int)(a8);
    if ((unsigned int)((unsigned int)(a8)) == 0) {
        result = *(unsigned int *)(a2 + 108);
    }
    *(unsigned int *)(result + 24) = (unsigned int)(result);
    v_stack_mB8 = 0;
    v_stack_mC0 = v_stack_m98;
    *(unsigned int *)(result + 20) = a1;
    v_stack_mC8 = (unsigned int)((unsigned int)(a6));
    result = ObpAllocateObject(result, a4, a2, v_stack_mA8);
    if (!sign_flag) goto loc_00873050;
loc_00872E00:
    if (v_stack_mA0 == 0) goto loc_00872E48;
    if (v_stack_mA6 != 248) goto loc_00872FCB;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2128))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2128) + 16)))) goto loc_00873124;
loc_00872E3F:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2128), v_stack_mA0, a2, v_stack_mA8);
loc_00872E48:
    if (*(unsigned __int64 *)(result + 32) == 0) goto loc_00872E66;
    if ((*(unsigned __int8 *)(result + 16)) <= 1) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 32), a2, a2, v_stack_mA8);
    }
    *(unsigned __int64 *)(result + 32) = 0;
loc_00872E66:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 16)))) goto loc_00873105;
loc_00872E86:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), result, a2, v_stack_mA8);
loc_00872E8E:
loc_00872E90:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, result, a2, v_stack_mA8);
    v_rsp = (v_rsp) + (176);
    return result;
loc_00872EB8:
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_m90, result, a2, v_stack_mA8);
    v_stack_m58 = *(unsigned __int64 *)(v_rip + 7761169);
    v_stack_m60 = 1;
    v_stack_m5C = 1;
    v_stack_m50 = 0;
    if (a1 == 0) goto loc_00873165;
    if (v_stack_m90 != 0) goto loc_0087303E;
loc_00872F03:
    v_stack_p20 = a1;
    result = SepPrivilegeCheck(v_stack_m80, v_stack_m58, 1, 1);
loc_00872F25:
    a1 = v_stack_m80;
    if (v_stack_m90 != 0) { a1 = v_stack_m90; }
    result = RtlEqualSid(*(unsigned __int64 *)(v_rip + 6245911), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)), 1, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00872FD7;
loc_00872F51:
    result = SeReleaseSubjectContext(v_stack_m90, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)), 1, 1);
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_00872DAE;
    goto loc_00872E00;
loc_00872F6D:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 16)))) goto loc_00872E86;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 16)))) goto loc_00872E86;
loc_00872FAE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 56)) != (v_rip + 3209378)) goto loc_0087317D;
    result = ExFreePool(result, *(unsigned __int64 *)(gs_base + (0 + 32)), 1, 1);
    goto loc_00872E8E;
loc_00872FCB:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 1, 1);
    goto loc_00872E48;
loc_00872FD7:
    v_stack_m70 = *(unsigned __int64 *)(v_rip + 7760578);
    result = RtlEqualSid(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7760578) + 392), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)), 1, 1);
    if ((unsigned __int8)(result) != 0) goto loc_00873071;
    result = RtlEqualSid(*(unsigned __int64 *)(v_stack_m70 + 384), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)), 1, 1);
    if ((unsigned __int8)(result) != 0) goto loc_00873071;
loc_0087300C:
    v_stack_p30 = (unsigned __int8)((unsigned __int8)(result));
    v_stack_p28 = v_stack_m60;
    v_stack_p20 = v_stack_m80;
    a3 = 0;
    result = SepAdtPrivilegedServiceAuditAlarm(v_stack_m90, v_rip - 8854649, a3, (unsigned int)(0xC0000061ULL));
    goto loc_00872F51;
loc_0087303E:
    if (v_stack_m88 >= 2) goto loc_00872F03;
    v_r15 = 0;
    goto loc_00872F25;
loc_00873050:
    if ((*(unsigned int *)(v_rip + 7675833)) != 0) goto loc_0087319B;
loc_00873061:
    *(unsigned __int64 *)(v_stack_m68) = v_stack_m98 + 48;
    goto loc_00872E8E;
loc_00873071:
    v_r11 = 0;
    if ((unsigned int)(v_rip + 3209378) == 0) goto loc_00872F51;
loc_0087308A:
loc_00873093:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58)))) == (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7754176))))) goto loc_008730A7;
loc_00873098:
    a1 = (*(unsigned __int64 *)(v_rip + 7754176)) + (8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7754176) + 8) != 0) goto loc_00873093;
    goto loc_008730B2;
loc_008730A7:
    if ((*(unsigned int *)(v_stack_m58 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7754176) + 8) + 4))))) goto loc_00873098;
    v_r11 = (unsigned int)((v_r11) + 1);
loc_008730B2:
    a2 = (v_stack_m58) + (12);
    a4 = ((unsigned int)((unsigned int)(v_rip + 3209378))) - (1);
    if (condition_is_not_equal) goto loc_0087308A;
    if ((unsigned int)(v_rip + 3209378) == 0) goto loc_008730F7;
loc_008730CE:
loc_008730DB:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58)))) == (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2985293)))) goto loc_00873158;
loc_008730E0:
    a2 = (v_rip + 2985306) + (8);
    if (*(unsigned __int64 *)(v_rip + 2985306 + 8) != 0) goto loc_008730DB;
loc_008730ED:
    a1 = (v_stack_m58) + (12);
    a3 = ((unsigned int)((unsigned int)(v_rip + 3209378))) - (1);
    if (condition_is_not_equal) goto loc_008730CE;
loc_008730F7:
    if (((unsigned int)(v_r11)) == ((unsigned int)(v_rip + 3209378))) goto loc_00872F51;
    goto loc_0087300C;
loc_00873105:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2120))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2120) + 16)))) goto loc_00872E86;
    goto loc_00872FAE;
loc_00873124:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2136))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2136) + 16)))) goto loc_00872E3F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2136) + 56)) != (v_rip + 3209378)) goto loc_00873191;
    result = ExFreePool(v_stack_mA0, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m58)));
    goto loc_00872E48;
loc_00873158:
    if ((*(unsigned int *)(v_stack_mA0 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 4))))) goto loc_008730E0;
    v_r11 = (unsigned int)((v_r11) + 1);
    goto loc_008730ED;
loc_00873165:
    result = SeReleaseSubjectContext(v_stack_m90, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m58)));
    goto loc_00872DAE;
loc_00873173:
    goto loc_00872E90;
loc_0087317D:
    result = guard_dispatch_icall(v_stack_m90, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m58)));
    goto loc_00872E8E;
loc_00873187:
    goto loc_00872E00;
loc_00873191:
    result = guard_dispatch_icall(v_stack_m90, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m58)));
    goto loc_00872E48;
loc_0087319B:
    result = ObpRegisterObject(v_stack_m98, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m58)));
    result = ObpPushStackInfo(v_stack_m98, 1, 1, (unsigned int)(0x746C6644ULL));
    goto loc_00873061;
}
```

## 5. (Beta) C Style

```c
int64_t ObCreateObject(uint8_t Arg1, void *Arg2, int64_t Arg3, uint8_t Arg4, uint64_t Arg5, uint32_t Arg6, uint32_t Arg7, uint32_t Arg8, int64_t Arg9)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r11;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m3F;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint16_t v_stack_mA6;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x597A6D)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m68 = Arg9;
    v_stack_m98 = 0;
    v_stack_mA8 = v_xmm0;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), Arg2, Arg3, Arg4);
    if (result != 0) goto loc_00872D60;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848), Arg2, Arg3, Arg4);
    if (result != 0) goto loc_00872D60;
    result = guard_dispatch_icall((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x24)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x2C)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x28)), Arg4);
    if (result != 0) {
        result = *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24);
        *(uint32_t *)(result) = (uint32_t)(result);
    }
    if (result == 0) goto loc_00873173;
    v_stack_mC0 = 0;
    v_stack_mC8 = result;
    result = ObpCaptureObjectCreateInformation(Arg1, Arg4, Arg3, v_stack_mA8);
    if (sign_flag) goto loc_00872F6D;
    if (((*(uint32_t *)(arg2 + 0x48)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result))))) != 0) goto loc_00873187;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result)))) & (16)) != 0) goto loc_00872EB8;
loc_00872DAE:
    if ((uint32_t)((uint32_t)(Arg7)) == 0) {
        Arg1 = *(uint32_t *)(arg2 + 0x68);
    }
    result = (uint32_t)(Arg8);
    if ((uint32_t)((uint32_t)(Arg8)) == 0) {
        result = *(uint32_t *)(arg2 + 0x6C);
    }
    *(uint32_t *)(result + 0x18) = (uint32_t)(result);
    v_stack_mB8 = 0;
    v_stack_mC0 = v_stack_m98;
    *(uint32_t *)(result + 0x14) = Arg1;
    v_stack_mC8 = (uint32_t)((uint32_t)(Arg6));
    result = ObpAllocateObject(result, Arg4, Arg2, v_stack_mA8);
    if (!sign_flag) goto loc_00873050;
loc_00872E00:
    if (v_stack_mA0 == 0) goto loc_00872E48;
    if (v_stack_mA6 != 248) goto loc_00872FCB;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x850))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x850) + 0x10)))) goto loc_00873124;
loc_00872E3F:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x850), v_stack_mA0, Arg2, v_stack_mA8);
loc_00872E48:
    if (*(uint64_t *)(result + 0x20) == 0) goto loc_00872E66;
    if ((*(uint8_t *)(result + 0x10)) <= 1) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(result + 0x20), Arg2, Arg2, v_stack_mA8);
    }
    *(uint64_t *)(result + 0x20) = 0;
loc_00872E66:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x10)))) goto loc_00873105;
loc_00872E86:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), result, Arg2, v_stack_mA8);
loc_00872E8E:
loc_00872E90:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, result, Arg2, v_stack_mA8);
    local_rsp = (local_rsp) + (176);
    return result;
loc_00872EB8:
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_m90, result, Arg2, v_stack_mA8);
    v_stack_m58 = *(uint64_t *)(v_rip + 0x766D11);
    v_stack_m60 = 1;
    v_stack_m5C = 1;
    v_stack_m50 = 0;
    if (Arg1 == 0) goto loc_00873165;
    if (v_stack_m90 != 0) goto loc_0087303E;
loc_00872F03:
    v_stack_p20 = Arg1;
    result = SepPrivilegeCheck(v_stack_m80, v_stack_m58, 1, 1);
loc_00872F25:
    Arg1 = v_stack_m80;
    if (v_stack_m90 != 0) { Arg1 = v_stack_m90; }
    result = RtlEqualSid(*(uint64_t *)(v_rip + 0x5F4E17), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x98)), 1, 1);
    if ((uint8_t)(result) == 0) goto loc_00872FD7;
loc_00872F51:
    result = SeReleaseSubjectContext(v_stack_m90, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x98)), 1, 1);
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_00872DAE;
    goto loc_00872E00;
loc_00872F6D:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x10)))) goto loc_00872E86;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x10)))) goto loc_00872E86;
loc_00872FAE:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x38)) != (v_rip + 3209378)) goto loc_0087317D;
    result = ExFreePool(result, *(uint64_t *)(gs_base + (0 + 0x20)), 1, 1);
    goto loc_00872E8E;
loc_00872FCB:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 1, 1);
    goto loc_00872E48;
loc_00872FD7:
    v_stack_m70 = *(uint64_t *)(v_rip + 0x766AC2);
    result = RtlEqualSid(*(uint64_t *)(*(uint64_t *)(v_rip + 0x766AC2) + 0x188), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x98)), 1, 1);
    if ((uint8_t)(result) != 0) goto loc_00873071;
    result = RtlEqualSid(*(uint64_t *)(v_stack_m70 + 0x180), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x98)), 1, 1);
    if ((uint8_t)(result) != 0) goto loc_00873071;
loc_0087300C:
    v_stack_p30 = (uint8_t)((uint8_t)(result));
    v_stack_p28 = v_stack_m60;
    v_stack_p20 = v_stack_m80;
    Arg3 = 0;
    result = SepAdtPrivilegedServiceAuditAlarm(v_stack_m90, v_rip - 8854649, Arg3, (uint32_t)(0xC0000061ULL));
    goto loc_00872F51;
loc_0087303E:
    if (v_stack_m88 >= 2) goto loc_00872F03;
    local_r15 = 0;
    goto loc_00872F25;
loc_00873050:
    if ((*(uint32_t *)(v_rip + 0x751FB9)) != 0) goto loc_0087319B;
loc_00873061:
    *(uint64_t *)(v_stack_m68) = v_stack_m98 + 48;
    goto loc_00872E8E;
loc_00873071:
    local_r11 = 0;
    if ((uint32_t)(v_rip + 3209378) == 0) goto loc_00872F51;
loc_0087308A:
loc_00873093:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58)))) == (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7651C0))))) goto loc_008730A7;
loc_00873098:
    Arg1 = (*(uint64_t *)(v_rip + 0x7651C0)) + (8);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x7651C0) + 0x8) != 0) goto loc_00873093;
    goto loc_008730B2;
loc_008730A7:
    if ((*(uint32_t *)(v_stack_m58 + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7651C0) + 0x8) + 0x4))))) goto loc_00873098;
    local_r11 = (uint32_t)((local_r11) + 1);
loc_008730B2:
    Arg2 = (v_stack_m58) + (12);
    Arg4 = ((uint32_t)((uint32_t)(v_rip + 3209378))) - (1);
    if (condition_is_not_equal) goto loc_0087308A;
    if ((uint32_t)(v_rip + 3209378) == 0) goto loc_008730F7;
loc_008730CE:
loc_008730DB:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58)))) == (*(uint32_t *)(*(uint64_t *)(v_rip + 0x2D8D4D)))) goto loc_00873158;
loc_008730E0:
    Arg2 = (v_rip + 2985306) + (8);
    if (*(uint64_t *)(v_rip + 0x2D8D5A + 0x8) != 0) goto loc_008730DB;
loc_008730ED:
    Arg1 = (v_stack_m58) + (12);
    Arg3 = ((uint32_t)((uint32_t)(v_rip + 3209378))) - (1);
    if (condition_is_not_equal) goto loc_008730CE;
loc_008730F7:
    if (((uint32_t)(local_r11)) == ((uint32_t)(v_rip + 3209378))) goto loc_00872F51;
    goto loc_0087300C;
loc_00873105:
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x848))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x848) + 0x10)))) goto loc_00872E86;
    goto loc_00872FAE;
loc_00873124:
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x858))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x858) + 0x10)))) goto loc_00872E3F;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x858) + 0x38)) != (v_rip + 3209378)) goto loc_00873191;
    result = ExFreePool(v_stack_mA0, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m58)));
    goto loc_00872E48;
loc_00873158:
    if ((*(uint32_t *)(v_stack_mA0 + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))))) goto loc_008730E0;
    local_r11 = (uint32_t)((local_r11) + 1);
    goto loc_008730ED;
loc_00873165:
    result = SeReleaseSubjectContext(v_stack_m90, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m58)));
    goto loc_00872DAE;
loc_00873173:
    goto loc_00872E90;
loc_0087317D:
    result = guard_dispatch_icall(v_stack_m90, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m58)));
    goto loc_00872E8E;
loc_00873187:
    goto loc_00872E00;
loc_00873191:
    result = guard_dispatch_icall(v_stack_m90, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m58)));
    goto loc_00872E48;
loc_0087319B:
    result = ObpRegisterObject(v_stack_m98, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m58)));
    result = ObpPushStackInfo(v_stack_m98, 1, 1, (uint32_t)(0x746C6644ULL));
    goto loc_00873061;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x48` | `32` | `R` |
| `Arg2` | `+ 0x68` | `32` | `R` |
| `Arg2` | `+ 0x6C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00872CB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
