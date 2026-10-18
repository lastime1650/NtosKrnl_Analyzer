# ObLogSecurityDescriptor

- RVA: `0x008C0020`–`0x008C034A` (길이 `810` bytes)
- VA: `0x00000001408C0020`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008341C`
- 디코드: `229`개 명령, `810/810` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008C0151` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008C0172` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008C01BD` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008C01C5` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008C01CD` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008C01EA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008C0219` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008C024B` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x008C027C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008C0284` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008C029E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008C02F1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008C02F9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008C0301` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008C0324` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)

### Direct callers
- [ObpInitObjectTypeSD](../74/ObpInitObjectTypeSD_function_0074F1B8.md) at `0x0074F1FF`
- [IopGetSetSecurityObject](../87/IopGetSetSecurityObject_function_00873A80.md) at `0x00873E51`
- [sub_008BA74A](../8B/Unknown_function_008BA74A.md) at `0x008BA80B`
- [ExpWnfCreateNameInstance](../8B/ExpWnfCreateNameInstance_function_008BF590.md) at `0x008BF645`
- [EtwpAllocGuidEntry](../8B/EtwpAllocGuidEntry_function_008BFF20.md) at `0x008BFFB8`
- [IopSetDeviceSecurityDescriptor](../A7/IopSetDeviceSecurityDescriptor_function_00A7199C.md) at `0x00A71A7E`
- [EtwpInitializeLoggerSecurityDescriptor](../AA/EtwpInitializeLoggerSecurityDescriptor_function_00AA7590.md) at `0x00AA75B0`
- [EtwpUpdateLoggerSecurityDescriptor](../AA/EtwpUpdateLoggerSecurityDescriptor_function_00AA9F64.md) at `0x00AA9F90`

### Static image references
- `0x008C0129` → RVA `0x00FD0EC0` (`CACHEALI`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x008C0151` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008C0172` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008C01BD` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008C01C5` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008C01CD` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008C01EA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008C0219` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008C024B` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x008C027C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008C0284` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008C029E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008C02F1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008C02F9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008C0301` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008C0324` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008C0020  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
008C0025  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
008C002A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
008C002F  55                              push rbp
008C0030  56                              push rsi
008C0031  57                              push rdi
008C0032  41 54                           push r12
008C0034  41 55                           push r13
008C0036  41 56                           push r14
008C0038  41 57                           push r15
008C003A  48 83 EC 20                     sub rsp, 0x20
008C003E  48 8B E9                        mov rbp, rcx
008C0041  0F BF 49 02                     movsx ecx, word ptr [rcx + 2]
008C0045  8B F1                           mov esi, ecx
008C0047  C1 FE 1F                        sar esi, 0x1f
008C004A  83 E6 EC                        and esi, 0xffffffec
008C004D  83 C6 28                        add esi, 0x28
008C0050  66 85 C9                        test cx, cx
008C0053  0F 89 62 02 00 00               jns 0x1408c02bb
008C0059  8B 45 04                        mov eax, dword ptr [rbp + 4]
008C005C  85 C0                           test eax, eax
008C005E  74 21                           je 0x1408c0081
008C0060  48 03 C5                        add rax, rbp
008C0063  48 85 C0                        test rax, rax
008C0066  74 10                           je 0x1408c0078
008C0068  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
008C006C  8D 04 85 0B 00 00 00            lea eax, [rax*4 + 0xb]
008C0073  83 E0 FC                        and eax, 0xfffffffc
008C0076  03 F0                           add esi, eax
008C0078  66 85 C9                        test cx, cx
008C007B  0F 89 43 02 00 00               jns 0x1408c02c4
008C0081  8B 45 08                        mov eax, dword ptr [rbp + 8]
008C0084  85 C0                           test eax, eax
008C0086  74 18                           je 0x1408c00a0
008C0088  48 03 C5                        add rax, rbp
008C008B  48 85 C0                        test rax, rax
008C008E  74 10                           je 0x1408c00a0
008C0090  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
008C0094  8D 04 85 0B 00 00 00            lea eax, [rax*4 + 0xb]
008C009B  83 E0 FC                        and eax, 0xfffffffc
008C009E  03 F0                           add esi, eax
008C00A0  F6 C1 04                        test cl, 4
008C00A3  74 24                           je 0x1408c00c9
008C00A5  66 85 C9                        test cx, cx
008C00A8  0F 89 80 02 00 00               jns 0x1408c032e
008C00AE  8B 45 10                        mov eax, dword ptr [rbp + 0x10]
008C00B1  85 C0                           test eax, eax
008C00B3  74 14                           je 0x1408c00c9
008C00B5  48 03 C5                        add rax, rbp
008C00B8  48 85 C0                        test rax, rax
008C00BB  74 0C                           je 0x1408c00c9
008C00BD  0F B7 40 02                     movzx eax, word ptr [rax + 2]
008C00C1  83 C0 03                        add eax, 3
008C00C4  83 E0 FC                        and eax, 0xfffffffc
008C00C7  03 F0                           add esi, eax
008C00C9  F6 C1 10                        test cl, 0x10
008C00CC  74 24                           je 0x1408c00f2
008C00CE  66 85 C9                        test cx, cx
008C00D1  0F 89 60 02 00 00               jns 0x1408c0337
008C00D7  8B 45 0C                        mov eax, dword ptr [rbp + 0xc]
008C00DA  85 C0                           test eax, eax
008C00DC  74 14                           je 0x1408c00f2
008C00DE  48 03 C5                        add rax, rbp
008C00E1  48 85 C0                        test rax, rax
008C00E4  74 0C                           je 0x1408c00f2
008C00E6  0F B7 40 02                     movzx eax, word ptr [rax + 2]
008C00EA  83 C0 03                        add eax, 3
008C00ED  83 E0 FC                        and eax, 0xfffffffc
008C00F0  03 F0                           add esi, eax
008C00F2  33 D2                           xor edx, edx
008C00F4  8B CE                           mov ecx, esi
008C00F6  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
008C00FA  8B DA                           mov ebx, edx
008C00FC  48 03 CD                        add rcx, rbp
008C00FF  48 8B C5                        mov rax, rbp
008C0102  48 3B E9                        cmp rbp, rcx
008C0105  73 19                           jae 0x1408c0120
008C0107  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
008C0110  48 33 18                        xor rbx, qword ptr [rax]
008C0113  48 83 C0 10                     add rax, 0x10
008C0117  48 C1 C3 03                     rol rbx, 3
008C011B  48 3B C1                        cmp rax, rcx
008C011E  72 F0                           jb 0x1408c0110
008C0120  65 4C 8B 2C 25 88 01 00 00      mov r13, qword ptr gs:[0x188]
008C0129  48 8D 05 90 0D 71 00            lea rax, [rip + 0x710d90]
008C0130  44 0F B6 FB                     movzx r15d, bl
008C0134  4C 8B E2                        mov r12, rdx
008C0137  49 C1 E7 04                     shl r15, 4
008C013B  4C 03 F8                        add r15, rax
008C013E  66 41 FF 8D E4 01 00 00         dec word ptr [r13 + 0x1e4]
008C0146  4D 8D 77 08                     lea r14, [r15 + 8]
008C014A  45 33 C0                        xor r8d, r8d
008C014D  49 8B CF                        mov rcx, r15
008C0150  90                              nop
008C0151  E8 DA 00 95 FF                  call 0x140210230
008C0156  48 8B F8                        mov rdi, rax
008C0159  B9 11 00 00 00                  mov ecx, 0x11
008C015E  33 C0                           xor eax, eax
008C0160  F0 49 0F B1 0F                  lock cmpxchg qword ptr [r15], rcx
008C0165  74 15                           je 0x1408c017c
008C0167  4D 8B CF                        mov r9, r15
008C016A  4C 8B C7                        mov r8, rdi
008C016D  33 D2                           xor edx, edx
008C016F  49 8B CF                        mov rcx, r15
008C0172  E8 D5 02 95 FF                  call 0x14021044c
008C0177  B9 11 00 00 00                  mov ecx, 0x11
008C017C  48 85 FF                        test rdi, rdi
008C017F  74 04                           je 0x1408c0185
008C0181  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
008C0185  49 8B 3E                        mov rdi, qword ptr [r14]
008C0188  48 85 FF                        test rdi, rdi
008C018B  74 18                           je 0x1408c01a5
008C018D  0F 1F 00                        nop dword ptr [rax]
008C0190  48 39 5F 10                     cmp qword ptr [rdi + 0x10], rbx
008C0194  0F 84 8B 00 00 00               je 0x1408c0225
008C019A  0F 86 8A 00 00 00               jbe 0x1408c022a
008C01A0  B9 11 00 00 00                  mov ecx, 0x11
008C01A5  4D 85 E4                        test r12, r12
008C01A8  0F 85 1F 01 00 00               jne 0x1408c02cd
008C01AE  48 8B C1                        mov rax, rcx
008C01B1  33 C9                           xor ecx, ecx
008C01B3  F0 49 0F B1 0F                  lock cmpxchg qword ptr [r15], rcx
008C01B8  74 08                           je 0x1408c01c2
008C01BA  49 8B CF                        mov rcx, r15
008C01BD  E8 7E 32 9A FF                  call 0x140263440
008C01C2  49 8B CF                        mov rcx, r15
008C01C5  E8 36 14 A2 FF                  call 0x1402e1600
008C01CA  49 8B CD                        mov rcx, r13
008C01CD  E8 1E EE 99 FF                  call 0x14025eff0
008C01D2  8D 46 28                        lea eax, [rsi + 0x28]
008C01D5  3B C6                           cmp eax, esi
008C01D7  0F 82 63 01 00 00               jb 0x1408c0340
008C01DD  8B D0                           mov edx, eax
008C01DF  B9 08 01 00 00                  mov ecx, 0x108
008C01E4  41 B8 4F 62 53 63               mov r8d, 0x6353624f
008C01EA  E8 01 1F 2C 00                  call 0x140b820f0
008C01EF  4C 8B E0                        mov r12, rax
008C01F2  48 85 C0                        test rax, rax
008C01F5  0F 84 45 01 00 00               je 0x1408c0340
008C01FB  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
008C01FF  49 8D 4C 24 20                  lea rcx, [r12 + 0x20]
008C0204  44 8B C6                        mov r8d, esi
008C0207  48 8B D5                        mov rdx, rbp
008C020A  49 89 44 24 08                  mov qword ptr [r12 + 8], rax
008C020F  49 89 5C 24 10                  mov qword ptr [r12 + 0x10], rbx
008C0214  41 89 74 24 18                  mov dword ptr [r12 + 0x18], esi
008C0219  E8 22 66 E0 FF                  call 0x1406c6840
008C021E  33 D2                           xor edx, edx
008C0220  E9 19 FF FF FF                  jmp 0x1408c013e
008C0225  39 77 18                        cmp dword ptr [rdi + 0x18], esi
008C0228  74 14                           je 0x1408c023e
008C022A  4C 8B F7                        mov r14, rdi
008C022D  48 8B 3F                        mov rdi, qword ptr [rdi]
008C0230  48 85 FF                        test rdi, rdi
008C0233  0F 84 67 FF FF FF               je 0x1408c01a0
008C0239  E9 52 FF FF FF                  jmp 0x1408c0190
008C023E  4C 8D 77 20                     lea r14, [rdi + 0x20]
008C0242  44 8B C6                        mov r8d, esi
008C0245  49 8B D6                        mov rdx, r14
008C0248  48 8B CD                        mov rcx, rbp
008C024B  E8 C0 68 E0 FF                  call 0x1406c6b10
008C0250  85 C0                           test eax, eax
008C0252  75 D6                           jne 0x1408c022a
008C0254  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
008C0258  F0 48 0F C1 4F 08               lock xadd qword ptr [rdi + 8], rcx
008C025E  48 85 C9                        test rcx, rcx
008C0261  0F 8E AE 00 00 00               jle 0x1408c0315
008C0267  B8 11 00 00 00                  mov eax, 0x11
008C026C  33 C9                           xor ecx, ecx
008C026E  F0 49 0F B1 0F                  lock cmpxchg qword ptr [r15], rcx
008C0273  0F 85 A8 00 00 00               jne 0x1408c0321
008C0279  49 8B CF                        mov rcx, r15
008C027C  E8 7F 13 A2 FF                  call 0x1402e1600
008C0281  49 8B CD                        mov rcx, r13
008C0284  E8 67 ED 99 FF                  call 0x14025eff0
008C0289  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008C028E  4C 89 31                        mov qword ptr [rcx], r14
008C0291  4D 85 E4                        test r12, r12
008C0294  74 0D                           je 0x1408c02a3
008C0296  BA 4F 62 53 63                  mov edx, 0x6353624f
008C029B  49 8B CC                        mov rcx, r12
008C029E  E8 CD 25 2C 00                  call 0x140b82870
008C02A3  33 C0                           xor eax, eax
008C02A5  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
008C02AA  48 83 C4 20                     add rsp, 0x20
008C02AE  41 5F                           pop r15
008C02B0  41 5E                           pop r14
008C02B2  41 5D                           pop r13
008C02B4  41 5C                           pop r12
008C02B6  5F                              pop rdi
008C02B7  5E                              pop rsi
008C02B8  5D                              pop rbp
008C02B9  C3                              ret
008C02BA  CC                              int3
008C02BB  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
008C02BF  E9 9F FD FF FF                  jmp 0x1408c0063
008C02C4  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
008C02C8  E9 BE FD FF FF                  jmp 0x1408c008b
008C02CD  49 89 3C 24                     mov qword ptr [r12], rdi
008C02D1  48 8B C7                        mov rax, rdi
008C02D4  F0 4D 0F B1 26                  lock cmpxchg qword ptr [r14], r12
008C02D9  4C 8B F0                        mov r14, rax
008C02DC  0F 85 A3 FE FF FF               jne 0x1408c0185
008C02E2  48 8B C1                        mov rax, rcx
008C02E5  33 C9                           xor ecx, ecx
008C02E7  F0 49 0F B1 0F                  lock cmpxchg qword ptr [r15], rcx
008C02EC  74 08                           je 0x1408c02f6
008C02EE  49 8B CF                        mov rcx, r15
008C02F1  E8 4A 31 9A FF                  call 0x140263440
008C02F6  49 8B CF                        mov rcx, r15
008C02F9  E8 02 13 A2 FF                  call 0x1402e1600
008C02FE  49 8B CD                        mov rcx, r13
008C0301  E8 EA EC 99 FF                  call 0x14025eff0
008C0306  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008C030B  49 8D 44 24 20                  lea rax, [r12 + 0x20]
008C0310  48 89 01                        mov qword ptr [rcx], rax
008C0313  EB 8E                           jmp 0x1408c02a3
008C0315  B9 0E 00 00 00                  mov ecx, 0xe
008C031A  CD 29                           int 0x29
008C031C  E9 46 FF FF FF                  jmp 0x1408c0267
008C0321  49 8B CF                        mov rcx, r15
008C0324  E8 17 31 9A FF                  call 0x140263440
008C0329  E9 4B FF FF FF                  jmp 0x1408c0279
008C032E  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
008C0332  E9 81 FD FF FF                  jmp 0x1408c00b8
008C0337  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
008C033B  E9 A1 FD FF FF                  jmp 0x1408c00e1
008C0340  B8 9A 00 00 C0                  mov eax, 0xc000009a
008C0345  E9 5B FF FF FF                  jmp 0x1408c02a5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObLogSecurityDescriptor(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p68;

    v_stack_p20 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (32);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((__int16)(*(unsigned __int16 *)(a1 + 2))))) >> (31));
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFECULL));
    v_rsi = (unsigned int)((v_rsi) + (40));
    if (!sign_flag) goto loc_008C02BB;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))) == 0) goto loc_008C0081;
    result = ((unsigned int)(*(unsigned int *)(a1 + 4))) + (a1);
loc_008C0063:
    if (result != 0) {
        result = *(unsigned __int8 *)(result + 1);
        result = result * 4 + 11;
        result = (unsigned int)((result) & (0xFFFFFFFCULL));
        v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(result)));
    }
    if (!sign_flag) goto loc_008C02C4;
loc_008C0081:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))) == 0) goto loc_008C00A0;
    result = ((unsigned int)(*(unsigned int *)(a1 + 8))) + (a1);
loc_008C008B:
    if (result != 0) {
        result = *(unsigned __int8 *)(result + 1);
        result = result * 4 + 11;
        result = (unsigned int)((result) & (0xFFFFFFFCULL));
        v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(result)));
    }
    if ((((unsigned __int8)((__int16)(*(unsigned __int16 *)(a1 + 2)))) & (4)) == 0) goto loc_008C00C9;
    if (!sign_flag) goto loc_008C032E;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))) == 0) goto loc_008C00C9;
    result = ((unsigned int)(*(unsigned int *)(a1 + 16))) + (a1);
loc_008C00B8:
    if (result != 0) {
        result = *(unsigned __int16 *)(result + 2);
        result = (unsigned int)((result) + (3));
        result = (unsigned int)((result) & (0xFFFFFFFCULL));
        v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(result)));
    }
    if ((((unsigned __int8)((__int16)(*(unsigned __int16 *)(a1 + 2)))) & (16)) == 0) goto loc_008C00F2;
    if (!sign_flag) goto loc_008C0337;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12))) == 0) goto loc_008C00F2;
    result = ((unsigned int)(*(unsigned int *)(a1 + 12))) + (a1);
loc_008C00E1:
    if (result != 0) {
        result = *(unsigned __int16 *)(result + 2);
        result = (unsigned int)((result) + (3));
        result = (unsigned int)((result) & (0xFFFFFFFCULL));
        v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(result)));
    }
    a2 = 0;
    a1 = ((unsigned int)((unsigned int)(v_rsi))) & (-8);
    a1 = (a1) + (a1);
    if (a1 >= a1) goto loc_008C0120;
loc_008C0110:
    v_rbx = (0) ^ (*(unsigned __int64 *)(a1));
    result = (a1) + (16);
    if (result < a1) goto loc_008C0110;
loc_008C0120:
    v_r15 = ((unsigned __int8)(v_rbx)) << (4);
    v_r15 = (v_r15) + (v_rip + 7409040);
loc_008C013E:
    a3 = 0;
    result = KeAbPreAcquire(v_r15, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_r15;
        a3 = 0;
        a2 = 0;
        a1 = v_r15;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a1 = 17;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(v_r15 + 8) == 0) goto loc_008C01A5;
loc_008C0190:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 16)) == v_rbx) goto loc_008C0225;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 16)) <= v_rbx) goto loc_008C022A;
loc_008C01A0:
loc_008C01A5:
    if (0 != 0) goto loc_008C02CD;
    a1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = v_r15;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_r15, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    if (((unsigned int)(v_rsi + 40)) < ((unsigned int)(v_rsi))) goto loc_008C0340;
    result = ExAllocatePool2(264, (unsigned int)((unsigned int)(v_rsi + 40)), (unsigned int)(0x6353624FULL), a4);
    if (result == 0) goto loc_008C0340;
    *(unsigned __int64 *)(result + 8) = (unsigned int)(v_stack_p18);
    *(unsigned __int64 *)(result + 16) = v_rbx;
    *(unsigned int *)(result + 24) = (unsigned int)(v_rsi);
    result = memcpy(result + 32, a1, (unsigned int)((unsigned int)(v_rsi)), a4);
    a2 = 0;
    goto loc_008C013E;
loc_008C0225:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 8) + 24)) == ((unsigned int)(v_rsi))) goto loc_008C023E;
loc_008C022A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8)) == 0) goto loc_008C01A0;
    goto loc_008C0190;
loc_008C023E:
    result = memcmp(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8)) + 32, (unsigned int)((unsigned int)(v_rsi)), a4);
    if ((unsigned int)(result) != 0) goto loc_008C022A;
    if (condition_is_less_or_equal) goto loc_008C0315;
loc_008C0267:
    a1 = 0;
    if (condition_is_not_equal) goto loc_008C0321;
loc_008C0279:
    result = KeAbPostRelease(v_r15, *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8)) + 32, (unsigned int)((unsigned int)(v_rsi)), a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8)) + 32, (unsigned int)((unsigned int)(v_rsi)), a4);
    *(unsigned __int64 *)(v_stack_p10) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8)) + 32;
    if (result != 0) {
        a2 = 0x6353624FULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)(v_rsi)), a4);
    }
    result = 0;
loc_008C02A5:
    v_rsp = (v_rsp) + (32);
    return result;
loc_008C02BB:
    goto loc_008C0063;
loc_008C02C4:
    goto loc_008C008B;
loc_008C02CD:
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8));
    if (condition_is_not_equal) goto loc_008C0185;
    a1 = 0;
    result = a1;
    if (!(condition_is_equal)) {
        a1 = v_r15;
        result = ExfReleasePushLockShared(a1, a2, (unsigned int)((unsigned int)(v_rsi)), a4);
    }
    result = KeAbPostRelease(v_r15, a2, (unsigned int)((unsigned int)(v_rsi)), a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, (unsigned int)((unsigned int)(v_rsi)), a4);
    *(unsigned __int64 *)(v_stack_p68) = result + 32;
    goto loc_008C02A3;
loc_008C0315:
    goto loc_008C0267;
loc_008C0321:
    result = ExfReleasePushLockShared(v_r15, a2, (unsigned int)((unsigned int)(v_rsi)), a4);
    goto loc_008C0279;
loc_008C032E:
    goto loc_008C00B8;
loc_008C0337:
    goto loc_008C00E1;
loc_008C0340:
    goto loc_008C02A5;
}
```

## 5. (Beta) C Style

```c
int64_t ObLogSecurityDescriptor(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p68;

    v_stack_p20 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (32);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(*(uint16_t *)(arg1 + 0x2))))) >> (31));
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFECULL));
    local_rsi = (uint32_t)((local_rsi) + (40));
    if (!sign_flag) goto loc_008C02BB;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))) == 0) goto loc_008C0081;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x4))) + (Arg1);
loc_008C0063:
    if (result != 0) {
        result = *(uint8_t *)(result + 0x1);
        result = result * 4 + 11;
        result = (uint32_t)((result) & (0xFFFFFFFCULL));
        local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(result)));
    }
    if (!sign_flag) goto loc_008C02C4;
loc_008C0081:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))) == 0) goto loc_008C00A0;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x8))) + (Arg1);
loc_008C008B:
    if (result != 0) {
        result = *(uint8_t *)(result + 0x1);
        result = result * 4 + 11;
        result = (uint32_t)((result) & (0xFFFFFFFCULL));
        local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(result)));
    }
    if ((((uint8_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) & (4)) == 0) goto loc_008C00C9;
    if (!sign_flag) goto loc_008C032E;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))) == 0) goto loc_008C00C9;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x10))) + (Arg1);
loc_008C00B8:
    if (result != 0) {
        result = *(uint16_t *)(result + 0x2);
        result = (uint32_t)((result) + (3));
        result = (uint32_t)((result) & (0xFFFFFFFCULL));
        local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(result)));
    }
    if ((((uint8_t)((int16_t)(*(uint16_t *)(arg1 + 0x2)))) & (16)) == 0) goto loc_008C00F2;
    if (!sign_flag) goto loc_008C0337;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC))) == 0) goto loc_008C00F2;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0xC))) + (Arg1);
loc_008C00E1:
    if (result != 0) {
        result = *(uint16_t *)(result + 0x2);
        result = (uint32_t)((result) + (3));
        result = (uint32_t)((result) & (0xFFFFFFFCULL));
        local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(result)));
    }
    Arg2 = 0;
    Arg1 = ((uint32_t)((uint32_t)(local_rsi))) & (-8);
    Arg1 = (Arg1) + (Arg1);
    if (Arg1 >= Arg1) goto loc_008C0120;
loc_008C0110:
    local_rbx = (0) ^ (*(uint64_t *)(arg1));
    result = (Arg1) + (16);
    if (result < Arg1) goto loc_008C0110;
loc_008C0120:
    local_r15 = ((uint8_t)(local_rbx)) << (4);
    local_r15 = (local_r15) + (v_rip + 7409040);
loc_008C013E:
    Arg3 = 0;
    result = KeAbPreAcquire(local_r15, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = local_r15;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_r15;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
        Arg1 = 17;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(local_r15 + 0x8) == 0) goto loc_008C01A5;
loc_008C0190:
    if ((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x10)) == local_rbx) goto loc_008C0225;
    if ((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x10)) <= local_rbx) goto loc_008C022A;
loc_008C01A0:
loc_008C01A5:
    if (0 != 0) goto loc_008C02CD;
    Arg1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = local_r15;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(local_r15, Arg2, Arg3, a4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, a4);
    if (((uint32_t)(local_rsi + 40)) < ((uint32_t)(local_rsi))) goto loc_008C0340;
    result = ExAllocatePool2(264, (uint32_t)((uint32_t)(local_rsi + 40)), (uint32_t)(0x6353624FULL), a4);
    if (result == 0) goto loc_008C0340;
    *(uint64_t *)(result + 0x8) = (uint32_t)(v_stack_p18);
    *(uint64_t *)(result + 0x10) = local_rbx;
    *(uint32_t *)(result + 0x18) = (uint32_t)(local_rsi);
    result = memcpy(result + 32, Arg1, (uint32_t)((uint32_t)(local_rsi)), a4);
    Arg2 = 0;
    goto loc_008C013E;
loc_008C0225:
    if ((*(uint32_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x18)) == ((uint32_t)(local_rsi))) goto loc_008C023E;
loc_008C022A:
    if (*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8)) == 0) goto loc_008C01A0;
    goto loc_008C0190;
loc_008C023E:
    result = memcmp(Arg1, *(uint64_t *)(*(uint64_t *)(local_r15 + 0x8)) + 32, (uint32_t)((uint32_t)(local_rsi)), a4);
    if ((uint32_t)(result) != 0) goto loc_008C022A;
    if (condition_is_less_or_equal) goto loc_008C0315;
loc_008C0267:
    Arg1 = 0;
    if (condition_is_not_equal) goto loc_008C0321;
loc_008C0279:
    result = KeAbPostRelease(local_r15, *(uint64_t *)(*(uint64_t *)(local_r15 + 0x8)) + 32, (uint32_t)((uint32_t)(local_rsi)), a4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(local_r15 + 0x8)) + 32, (uint32_t)((uint32_t)(local_rsi)), a4);
    *(uint64_t *)(v_stack_p10) = *(uint64_t *)(*(uint64_t *)(local_r15 + 0x8)) + 32;
    if (result != 0) {
        Arg2 = 0x6353624FULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(local_rsi)), a4);
    }
    result = 0;
loc_008C02A5:
    local_rsp = (local_rsp) + (32);
    return result;
loc_008C02BB:
    goto loc_008C0063;
loc_008C02C4:
    goto loc_008C008B;
loc_008C02CD:
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(local_r15 + 0x8));
    if (condition_is_not_equal) goto loc_008C0185;
    Arg1 = 0;
    result = Arg1;
    if (!(condition_is_equal)) {
        Arg1 = local_r15;
        result = ExfReleasePushLockShared(Arg1, Arg2, (uint32_t)((uint32_t)(local_rsi)), a4);
    }
    result = KeAbPostRelease(local_r15, Arg2, (uint32_t)((uint32_t)(local_rsi)), a4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, (uint32_t)((uint32_t)(local_rsi)), a4);
    *(uint64_t *)(v_stack_p68) = result + 32;
    goto loc_008C02A3;
loc_008C0315:
    goto loc_008C0267;
loc_008C0321:
    result = ExfReleasePushLockShared(local_r15, Arg2, (uint32_t)((uint32_t)(local_rsi)), a4);
    goto loc_008C0279;
loc_008C032E:
    goto loc_008C00B8;
loc_008C0337:
    goto loc_008C00E1;
loc_008C0340:
    goto loc_008C02A5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*1` | `16` | `R` |
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C0020&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
