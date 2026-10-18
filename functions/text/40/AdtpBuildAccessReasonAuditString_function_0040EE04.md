# AdtpBuildAccessReasonAuditString

- RVA: `0x0040EE04`–`0x0040F33E` (길이 `1,338` bytes)
- VA: `0x000000014040EE04`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009BAA4`
- 디코드: `352`개 명령, `1,338/1,338` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0040EEBF` → [AdtpEtwBuildDashString](../../page/AA/AdtpEtwBuildDashString_function_00AAB7B0.md) (function, `0x00AAB7B0`)
- `0x0040EF38` → [AdtpIsSDValidSelfRelative](../4D/AdtpIsSDValidSelfRelative_function_004DF684.md) (function, `0x004DF684`)
- `0x0040EF5F` → [RtlLengthSecurityDescriptor](../../page/8B/RtlLengthSecurityDescriptor_function_008BC870.md) (function, `0x008BC870`)
- `0x0040EF73` → [AdtpIsSDValidSelfRelative](../4D/AdtpIsSDValidSelfRelative_function_004DF684.md) (function, `0x004DF684`)
- `0x0040EF90` → [AdtpIsSDValidSelfRelative](../4D/AdtpIsSDValidSelfRelative_function_004DF684.md) (function, `0x004DF684`)
- `0x0040EFBE` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0040EFD1` → [AdtpBuildContextFromSecurityDescriptor](../69/AdtpBuildContextFromSecurityDescriptor_function_0069D99C.md) (function, `0x0069D99C`)
- `0x0040EFE6` → [AdtpBuildContextFromSecurityDescriptor](../69/AdtpBuildContextFromSecurityDescriptor_function_0069D99C.md) (function, `0x0069D99C`)
- `0x0040F014` → [AdtpPermissionBitPosition](../69/AdtpPermissionBitPosition_function_0069DE84.md) (function, `0x0069DE84`)
- `0x0040F059` → [AdtpBuildStagingReasonAuditStringInternal](../69/AdtpBuildStagingReasonAuditStringInternal_function_0069DA44.md) (function, `0x0069DA44`)
- `0x0040F0BA` → [AdtpBuildAccessReasonAuditStringInternal](AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (function, `0x0040F344`)
- `0x0040F144` → [AdtpBuildStagingReasonAuditStringInternal](../69/AdtpBuildStagingReasonAuditStringInternal_function_0069DA44.md) (function, `0x0069DA44`)
- `0x0040F1A6` → [AdtpBuildAccessReasonAuditStringInternal](AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) (function, `0x0040F344`)
- `0x0040F215` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0040F25E` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0040F2D0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0040F2F3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0040F30C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0040F31D` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_006F1C3C](../6F/Unknown_function_006F1C3C.md) at `0x006F1D84`

### Static image references
- `0x0040EE23` → RVA `0x00E0A740` (`.data`; read)
- `0x0040F002` → RVA `0x0001BED8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x0040EEBF` → [AdtpEtwBuildDashString](../../page/AA/AdtpEtwBuildDashString_function_00AAB7B0.md) (`.text` → `PAGE`)
  - `0x0040EF5F` → [RtlLengthSecurityDescriptor](../../page/8B/RtlLengthSecurityDescriptor_function_008BC870.md) (`.text` → `PAGE`)
  - `0x0040F215` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0040F2D0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0040F2F3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0040F30C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0040EE04  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0040EE09  55                              push rbp
0040EE0A  56                              push rsi
0040EE0B  57                              push rdi
0040EE0C  41 54                           push r12
0040EE0E  41 55                           push r13
0040EE10  41 56                           push r14
0040EE12  41 57                           push r15
0040EE14  48 8D AC 24 20 FE FF FF         lea rbp, [rsp - 0x1e0]
0040EE1C  48 81 EC E0 02 00 00            sub rsp, 0x2e0
0040EE23  48 8B 05 16 B9 9F 00            mov rax, qword ptr [rip + 0x9fb916]
0040EE2A  48 33 C4                        xor rax, rsp
0040EE2D  48 89 85 D0 01 00 00            mov qword ptr [rbp + 0x1d0], rax
0040EE34  48 8B 85 50 02 00 00            mov rax, qword ptr [rbp + 0x250]
0040EE3B  0F 57 C0                        xorps xmm0, xmm0
0040EE3E  4C 8B BD 48 02 00 00            mov r15, qword ptr [rbp + 0x248]
0040EE45  0F 57 C9                        xorps xmm1, xmm1
0040EE48  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0040EE4C  49 8B F0                        mov rsi, r8
0040EE4F  48 8B 85 58 02 00 00            mov rax, qword ptr [rbp + 0x258]
0040EE56  B3 01                           mov bl, 1
0040EE58  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0040EE5C  48 8B 85 60 02 00 00            mov rax, qword ptr [rbp + 0x260]
0040EE63  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0040EE67  33 C0                           xor eax, eax
0040EE69  44 88 4C 24 63                  mov byte ptr [rsp + 0x63], r9b
0040EE6E  45 33 C9                        xor r9d, r9d
0040EE71  41 8B F9                        mov edi, r9d
0040EE74  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
0040EE79  45 8B E1                        mov r12d, r9d
0040EE7C  48 89 4D 80                     mov qword ptr [rbp - 0x80], rcx
0040EE80  44 88 4C 24 64                  mov byte ptr [rsp + 0x64], r9b
0040EE85  44 89 4C 24 68                  mov dword ptr [rsp + 0x68], r9d
0040EE8A  44 88 4C 24 60                  mov byte ptr [rsp + 0x60], r9b
0040EE8F  44 88 4C 24 62                  mov byte ptr [rsp + 0x62], r9b
0040EE94  44 88 4C 24 61                  mov byte ptr [rsp + 0x61], r9b
0040EE99  4C 89 4C 24 70                  mov qword ptr [rsp + 0x70], r9
0040EE9E  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
0040EEA2  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0040EEA6  0F 11 4D A0                     movups xmmword ptr [rbp - 0x60], xmm1
0040EEAA  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0040EEAE  45 39 08                        cmp dword ptr [r8], r9d
0040EEB1  75 16                           jne 0x14040eec9
0040EEB3  4D 85 FF                        test r15, r15
0040EEB6  0F 84 26 04 00 00               je 0x14040f2e2
0040EEBC  49 8B CF                        mov rcx, r15
0040EEBF  E8 EC C8 69 00                  call 0x140aab7b0
0040EEC4  E9 19 04 00 00                  jmp 0x14040f2e2
0040EEC9  4D 8D A8 90 00 00 00            lea r13, [r8 + 0x90]
0040EED0  45 8B F1                        mov r14d, r9d
0040EED3  41 83 FE 20                     cmp r14d, 0x20
0040EED7  0F 83 CC 00 00 00               jae 0x14040efa9
0040EEDD  41 8B C6                        mov eax, r14d
0040EEE0  8B 4C 86 04                     mov ecx, dword ptr [rsi + rax*4 + 4]
0040EEE4  81 E1 00 00 FF 00               and ecx, 0xff0000
0040EEEA  0F 84 B1 00 00 00               je 0x14040efa1
0040EEF0  81 F9 00 00 01 00               cmp ecx, 0x10000
0040EEF6  0F 84 8C 00 00 00               je 0x14040ef88
0040EEFC  81 F9 00 00 02 00               cmp ecx, 0x20000
0040EF02  0F 84 80 00 00 00               je 0x14040ef88
0040EF08  81 F9 00 00 03 00               cmp ecx, 0x30000
0040EF0E  74 1D                           je 0x14040ef2d
0040EF10  81 F9 00 00 04 00               cmp ecx, 0x40000
0040EF16  74 15                           je 0x14040ef2d
0040EF18  81 F9 00 00 05 00               cmp ecx, 0x50000
0040EF1E  74 68                           je 0x14040ef88
0040EF20  81 F9 00 00 06 00               cmp ecx, 0x60000
0040EF26  74 05                           je 0x14040ef2d
0040EF28  41 8A D9                        mov bl, r9b
0040EF2B  EB 74                           jmp 0x14040efa1
0040EF2D  48 8D 54 24 61                  lea rdx, [rsp + 0x61]
0040EF32  49 8B CD                        mov rcx, r13
0040EF35  41 8A D9                        mov bl, r9b
0040EF38  E8 47 07 0D 00                  call 0x1404df684
0040EF3D  45 33 C9                        xor r9d, r9d
0040EF40  85 C0                           test eax, eax
0040EF42  78 11                           js 0x14040ef55
0040EF44  44 38 4C 24 61                  cmp byte ptr [rsp + 0x61], r9b
0040EF49  75 11                           jne 0x14040ef5c
0040EF4B  BF 0D 00 00 C0                  mov edi, 0xc000000d
0040EF50  E9 8D 03 00 00                  jmp 0x14040f2e2
0040EF55  3D 58 00 00 C0                  cmp eax, 0xc0000058
0040EF5A  75 EF                           jne 0x14040ef4b
0040EF5C  49 8B CD                        mov rcx, r13
0040EF5F  E8 0C D9 4A 00                  call 0x1408bc870
0040EF64  8B C0                           mov eax, eax
0040EF66  33 D2                           xor edx, edx
0040EF68  49 03 C5                        add rax, r13
0040EF6B  48 8B C8                        mov rcx, rax
0040EF6E  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0040EF73  E8 0C 07 0D 00                  call 0x1404df684
0040EF78  45 33 C9                        xor r9d, r9d
0040EF7B  8B F8                           mov edi, eax
0040EF7D  85 C0                           test eax, eax
0040EF7F  78 CA                           js 0x14040ef4b
0040EF81  C6 44 24 62 01                  mov byte ptr [rsp + 0x62], 1
0040EF86  EB 14                           jmp 0x14040ef9c
0040EF88  33 D2                           xor edx, edx
0040EF8A  49 8B CD                        mov rcx, r13
0040EF8D  41 8A D9                        mov bl, r9b
0040EF90  E8 EF 06 0D 00                  call 0x1404df684
0040EF95  45 33 C9                        xor r9d, r9d
0040EF98  85 C0                           test eax, eax
0040EF9A  78 AF                           js 0x14040ef4b
0040EF9C  C6 44 24 60 01                  mov byte ptr [rsp + 0x60], 1
0040EFA1  41 FF C6                        inc r14d
0040EFA4  E9 2A FF FF FF                  jmp 0x14040eed3
0040EFA9  80 FB 01                        cmp bl, 1
0040EFAC  0F 84 01 FF FF FF               je 0x14040eeb3
0040EFB2  33 D2                           xor edx, edx
0040EFB4  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0040EFB8  41 B8 00 02 00 00               mov r8d, 0x200
0040EFBE  E8 7D 7C 2B 00                  call 0x1406c6c40
0040EFC3  80 7C 24 60 01                  cmp byte ptr [rsp + 0x60], 1
0040EFC8  75 0C                           jne 0x14040efd6
0040EFCA  48 8D 55 88                     lea rdx, [rbp - 0x78]
0040EFCE  49 8B CD                        mov rcx, r13
0040EFD1  E8 C6 E9 28 00                  call 0x14069d99c
0040EFD6  80 7C 24 62 01                  cmp byte ptr [rsp + 0x62], 1
0040EFDB  75 0E                           jne 0x14040efeb
0040EFDD  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0040EFE2  48 8D 55 A0                     lea rdx, [rbp - 0x60]
0040EFE6  E8 B1 E9 28 00                  call 0x14069d99c
0040EFEB  45 33 C9                        xor r9d, r9d
0040EFEE  41 8B D9                        mov ebx, r9d
0040EFF1  44 8B EB                        mov r13d, ebx
0040EFF4  83 FB 07                        cmp ebx, 7
0040EFF7  0F 83 E5 00 00 00               jae 0x14040f0e2
0040EFFD  80 7C 24 63 01                  cmp byte ptr [rsp + 0x63], 1
0040F002  4C 8D 05 CF CE C0 FF            lea r8, [rip - 0x3f3131]
0040F009  8B C3                           mov eax, ebx
0040F00B  45 8B 04 80                     mov r8d, dword ptr [r8 + rax*4]
0040F00F  75 4F                           jne 0x14040f060
0040F011  41 8B C8                        mov ecx, r8d
0040F014  E8 6B EE 28 00                  call 0x14069de84
0040F019  0F B6 D0                        movzx edx, al
0040F01C  44 39 4C 96 04                  cmp dword ptr [rsi + rdx*4 + 4], r9d
0040F021  0F 8D B4 00 00 00               jge 0x14040f0db
0040F027  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0040F02C  4C 8D 75 D0                     lea r14, [rbp - 0x30]
0040F030  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0040F034  4C 8D 4D A0                     lea r9, [rbp - 0x60]
0040F038  41 8B C4                        mov eax, r12d
0040F03B  48 C1 E0 04                     shl rax, 4
0040F03F  4C 03 F0                        add r14, rax
0040F042  48 8D 46 04                     lea rax, [rsi + 4]
0040F046  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
0040F04B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0040F050  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
0040F055  4C 8D 45 88                     lea r8, [rbp - 0x78]
0040F059  E8 E6 E9 28 00                  call 0x14069da44
0040F05E  EB 5F                           jmp 0x14040f0bf
0040F060  44 23 06                        and r8d, dword ptr [rsi]
0040F063  74 76                           je 0x14040f0db
0040F065  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0040F06A  48 8D 4C 24 64                  lea rcx, [rsp + 0x64]
0040F06F  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
0040F074  4C 8D 75 D0                     lea r14, [rbp - 0x30]
0040F078  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0040F07C  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
0040F081  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
0040F086  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
0040F08B  4C 8D 4D A0                     lea r9, [rbp - 0x60]
0040F08F  41 8B C4                        mov eax, r12d
0040F092  48 C1 E0 04                     shl rax, 4
0040F096  4C 03 F0                        add r14, rax
0040F099  48 8D 46 04                     lea rax, [rsi + 4]
0040F09D  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
0040F0A2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0040F0A7  8A 86 88 00 00 00               mov al, byte ptr [rsi + 0x88]
0040F0AD  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0040F0B1  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
0040F0B6  4C 8D 45 88                     lea r8, [rbp - 0x78]
0040F0BA  E8 85 02 00 00                  call 0x14040f344
0040F0BF  45 33 C9                        xor r9d, r9d
0040F0C2  8B F8                           mov edi, eax
0040F0C4  85 C0                           test eax, eax
0040F0C6  0F 88 EE 01 00 00               js 0x14040f2ba
0040F0CC  41 0F B7 06                     movzx eax, word ptr [r14]
0040F0D0  44 03 E8                        add r13d, eax
0040F0D3  44 89 6C 24 68                  mov dword ptr [rsp + 0x68], r13d
0040F0D8  41 FF C4                        inc r12d
0040F0DB  FF C3                           inc ebx
0040F0DD  E9 12 FF FF FF                  jmp 0x14040eff4
0040F0E2  66 83 3E 00                     cmp word ptr [rsi], 0
0040F0E6  0F 84 E2 00 00 00               je 0x14040f1ce
0040F0EC  41 8B D9                        mov ebx, r9d
0040F0EF  41 BE 01 00 00 00               mov r14d, 1
0040F0F5  83 FB 10                        cmp ebx, 0x10
0040F0F8  0F 83 D0 00 00 00               jae 0x14040f1ce
0040F0FE  80 7C 24 63 01                  cmp byte ptr [rsp + 0x63], 1
0040F103  75 46                           jne 0x14040f14b
0040F105  8B C3                           mov eax, ebx
0040F107  44 39 4C 86 04                  cmp dword ptr [rsi + rax*4 + 4], r9d
0040F10C  0F 8D B2 00 00 00               jge 0x14040f1c4
0040F112  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0040F117  4C 8D 6D D0                     lea r13, [rbp - 0x30]
0040F11B  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0040F11F  4C 8D 4D A0                     lea r9, [rbp - 0x60]
0040F123  41 8B C4                        mov eax, r12d
0040F126  4C 8D 45 88                     lea r8, [rbp - 0x78]
0040F12A  48 C1 E0 04                     shl rax, 4
0040F12E  4C 03 E8                        add r13, rax
0040F131  48 8D 46 04                     lea rax, [rsi + 4]
0040F135  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
0040F13A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0040F13F  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
0040F144  E8 FB E8 28 00                  call 0x14069da44
0040F149  EB 60                           jmp 0x14040f1ab
0040F14B  41 8B CE                        mov ecx, r14d
0040F14E  23 0E                           and ecx, dword ptr [rsi]
0040F150  74 72                           je 0x14040f1c4
0040F152  48 8D 54 24 64                  lea rdx, [rsp + 0x64]
0040F157  41 8B C4                        mov eax, r12d
0040F15A  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
0040F15F  4C 8D 6D D0                     lea r13, [rbp - 0x30]
0040F163  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0040F168  4C 8D 45 88                     lea r8, [rbp - 0x78]
0040F16C  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
0040F171  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
0040F176  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
0040F17B  4C 8D 4D A0                     lea r9, [rbp - 0x60]
0040F17F  48 C1 E0 04                     shl rax, 4
0040F183  4C 03 E8                        add r13, rax
0040F186  48 8D 46 04                     lea rax, [rsi + 4]
0040F18A  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
0040F18F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0040F194  8A 86 88 00 00 00               mov al, byte ptr [rsi + 0x88]
0040F19A  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0040F19E  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
0040F1A2  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0040F1A6  E8 99 01 00 00                  call 0x14040f344
0040F1AB  45 33 C9                        xor r9d, r9d
0040F1AE  8B F8                           mov edi, eax
0040F1B0  85 C0                           test eax, eax
0040F1B2  0F 88 02 01 00 00               js 0x14040f2ba
0040F1B8  41 0F B7 45 00                  movzx eax, word ptr [r13]
0040F1BD  01 44 24 68                     add dword ptr [rsp + 0x68], eax
0040F1C1  41 FF C4                        inc r12d
0040F1C4  FF C3                           inc ebx
0040F1C6  45 03 F6                        add r14d, r14d
0040F1C9  E9 27 FF FF FF                  jmp 0x14040f0f5
0040F1CE  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
0040F1D2  4C 8B 45 B8                     mov r8, qword ptr [rbp - 0x48]
0040F1D6  D1 E8                           shr eax, 1
0040F1D8  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
0040F1DC  8D 58 01                        lea ebx, [rax + 1]
0040F1DF  4D 85 C0                        test r8, r8
0040F1E2  74 21                           je 0x14040f205
0040F1E4  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
0040F1E8  48 85 D2                        test rdx, rdx
0040F1EB  74 18                           je 0x14040f205
0040F1ED  8B 02                           mov eax, dword ptr [rdx]
0040F1EF  8D 0C 18                        lea ecx, [rax + rbx]
0040F1F2  81 F9 00 04 00 00               cmp ecx, 0x400
0040F1F8  73 0B                           jae 0x14040f205
0040F1FA  49 8D 34 40                     lea rsi, [r8 + rax*2]
0040F1FE  89 0A                           mov dword ptr [rdx], ecx
0040F200  41 8A C1                        mov al, r9b
0040F203  EB 2C                           jmp 0x14040f231
0040F205  8B D3                           mov edx, ebx
0040F207  B9 00 01 00 00                  mov ecx, 0x100
0040F20C  48 03 D2                        add rdx, rdx
0040F20F  41 B8 53 65 41 6B               mov r8d, 0x6b416553
0040F215  E8 D6 2E 77 00                  call 0x140b820f0
0040F21A  45 33 C9                        xor r9d, r9d
0040F21D  48 8B F0                        mov rsi, rax
0040F220  48 85 C0                        test rax, rax
0040F223  75 0A                           jne 0x14040f22f
0040F225  BF 17 00 00 C0                  mov edi, 0xc0000017
0040F22A  E9 8B 00 00 00                  jmp 0x14040f2ba
0040F22F  B0 01                           mov al, 1
0040F231  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
0040F235  45 8B E9                        mov r13d, r9d
0040F238  88 01                           mov byte ptr [rcx], al
0040F23A  45 85 E4                        test r12d, r12d
0040F23D  74 42                           je 0x14040f281
0040F23F  41 8B C4                        mov eax, r12d
0040F242  4C 8D 75 D0                     lea r14, [rbp - 0x30]
0040F246  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0040F24B  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
0040F24F  48 85 D2                        test rdx, rdx
0040F252  74 1E                           je 0x14040f272
0040F254  45 0F B7 06                     movzx r8d, word ptr [r14]
0040F258  41 8B CD                        mov ecx, r13d
0040F25B  48 03 CE                        add rcx, rsi
0040F25E  E8 DD 75 2B 00                  call 0x1406c6840
0040F263  41 0F B7 06                     movzx eax, word ptr [r14]
0040F267  44 03 E8                        add r13d, eax
0040F26A  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0040F26F  45 33 C9                        xor r9d, r9d
0040F272  49 83 C6 10                     add r14, 0x10
0040F276  48 83 E8 01                     sub rax, 1
0040F27A  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0040F27F  75 CA                           jne 0x14040f24b
0040F281  44 8B 6C 24 68                  mov r13d, dword ptr [rsp + 0x68]
0040F286  66 46 89 0C 6E                  mov word ptr [rsi + r13*2], r9w
0040F28B  4D 85 FF                        test r15, r15
0040F28E  74 10                           je 0x14040f2a0
0040F290  8D 04 1B                        lea eax, [rbx + rbx]
0040F293  49 89 37                        mov qword ptr [r15], rsi
0040F296  41 89 47 08                     mov dword ptr [r15 + 8], eax
0040F29A  45 89 4F 0C                     mov dword ptr [r15 + 0xc], r9d
0040F29E  EB 1A                           jmp 0x14040f2ba
0040F2A0  66 03 DB                        add bx, bx
0040F2A3  48 89 34 25 08 00 00 00         mov qword ptr [8], rsi
0040F2AB  66 89 1C 25 02 00 00 00         mov word ptr [2], bx
0040F2B3  8D 43 FE                        lea eax, [rbx - 2]
0040F2B6  66 41 89 01                     mov word ptr [r9], ax
0040F2BA  45 85 E4                        test r12d, r12d
0040F2BD  74 23                           je 0x14040f2e2
0040F2BF  48 8D 5D D8                     lea rbx, [rbp - 0x28]
0040F2C3  41 8B F4                        mov esi, r12d
0040F2C6  48 8B 0B                        mov rcx, qword ptr [rbx]
0040F2C9  48 85 C9                        test rcx, rcx
0040F2CC  74 0A                           je 0x14040f2d8
0040F2CE  33 D2                           xor edx, edx
0040F2D0  E8 9B 35 77 00                  call 0x140b82870
0040F2D5  45 33 C9                        xor r9d, r9d
0040F2D8  48 83 C3 10                     add rbx, 0x10
0040F2DC  48 83 EE 01                     sub rsi, 1
0040F2E0  75 E4                           jne 0x14040f2c6
0040F2E2  44 39 4D 90                     cmp dword ptr [rbp - 0x70], r9d
0040F2E6  74 13                           je 0x14040f2fb
0040F2E8  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0040F2EC  48 85 C9                        test rcx, rcx
0040F2EF  74 0A                           je 0x14040f2fb
0040F2F1  33 D2                           xor edx, edx
0040F2F3  E8 78 35 77 00                  call 0x140b82870
0040F2F8  45 33 C9                        xor r9d, r9d
0040F2FB  44 39 4D A8                     cmp dword ptr [rbp - 0x58], r9d
0040F2FF  74 10                           je 0x14040f311
0040F301  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0040F305  48 85 C9                        test rcx, rcx
0040F308  74 07                           je 0x14040f311
0040F30A  33 D2                           xor edx, edx
0040F30C  E8 5F 35 77 00                  call 0x140b82870
0040F311  8B C7                           mov eax, edi
0040F313  48 8B 8D D0 01 00 00            mov rcx, qword ptr [rbp + 0x1d0]
0040F31A  48 33 CC                        xor rcx, rsp
0040F31D  E8 1E D3 29 00                  call 0x1406ac640
0040F322  48 8B 9C 24 38 03 00 00         mov rbx, qword ptr [rsp + 0x338]
0040F32A  48 81 C4 E0 02 00 00            add rsp, 0x2e0
0040F331  41 5F                           pop r15
0040F333  41 5E                           pop r14
0040F335  41 5D                           pop r13
0040F337  41 5C                           pop r12
0040F339  5F                              pop rdi
0040F33A  5E                              pop rsi
0040F33B  5D                              pop rbp
0040F33C  C3                              ret
0040F33D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AdtpBuildAccessReasonAuditString(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned int v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned int v_stack_m2B0;
    unsigned __int8 v_stack_m2B4;
    unsigned __int8 v_stack_m2B5;
    unsigned __int8 v_stack_m2B6;
    unsigned __int8 v_stack_m2B7;
    unsigned __int8 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned __int8 v_stack_m2F0;
    unsigned int v_stack_m2F8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (736);
    result = (*(unsigned __int64 *)(v_rip + 10467606)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m260 = a7;
    v_stack_m258 = a8;
    v_stack_m250 = a9;
    result = 0;
    v_stack_m2B5 = (unsigned __int8)(a4);
    a4 = 0;
    v_stack_m2A0 = a2;
    v_stack_m298 = a1;
    v_stack_m2B4 = 0;
    v_stack_m2B0 = 0;
    v_stack_m2B8 = 0;
    v_stack_m2B6 = 0;
    v_stack_m2B7 = 0;
    v_stack_m2A8 = 0;
    v_stack_m290 = v_xmm0;
    v_stack_m280 = 0;
    v_stack_m278 = v_xmm1;
    v_stack_m268 = 0;
    if ((*(unsigned int *)(a3)) != 0) goto loc_0040EEC9;
loc_0040EEB3:
    if (a6 == 0) goto loc_0040F2E2;
    result = AdtpEtwBuildDashString(a6, a2, a3, a4);
    goto loc_0040F2E2;
loc_0040EEC9:
loc_0040EED3:
    if (0 >= 32) goto loc_0040EFA9;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 0 * 4 + 4))) & (0xFF0000ULL));
    if (condition_is_equal) goto loc_0040EFA1;
    if (((unsigned int)(a1)) == 0x10000ULL) goto loc_0040EF88;
    if (((unsigned int)(a1)) == 0x20000ULL) goto loc_0040EF88;
    if (((unsigned int)(a1)) == 0x30000ULL) goto loc_0040EF2D;
    if (((unsigned int)(a1)) == 0x40000ULL) goto loc_0040EF2D;
    if (((unsigned int)(a1)) == 0x50000ULL) goto loc_0040EF88;
    if (((unsigned int)(a1)) == 0x60000ULL) goto loc_0040EF2D;
    goto loc_0040EFA1;
loc_0040EF2D:
    result = AdtpIsSDValidSelfRelative(a3 + 144, v_stack_m2B7, a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_0040EF55;
    if (v_stack_m2B7 != 0) goto loc_0040EF5C;
loc_0040EF4B:
    goto loc_0040F2E2;
loc_0040EF55:
    if (((unsigned int)(result)) != 0xC0000058ULL) goto loc_0040EF4B;
loc_0040EF5C:
    result = RtlLengthSecurityDescriptor(a3 + 144, v_stack_m2B7, a3, a4);
    a2 = 0;
    result = ((unsigned int)((unsigned int)(result))) + (a3 + 144);
    v_stack_m2A8 = result;
    result = AdtpIsSDValidSelfRelative(result, a2, a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_0040EF4B;
    v_stack_m2B6 = 1;
    goto loc_0040EF9C;
loc_0040EF88:
    a2 = 0;
    result = AdtpIsSDValidSelfRelative(a3 + 144, a2, a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_0040EF4B;
loc_0040EF9C:
    v_stack_m2B8 = 1;
loc_0040EFA1:
    v_r14 = (unsigned int)((0) + 1);
    goto loc_0040EED3;
loc_0040EFA9:
    if (0 == 1) goto loc_0040EEB3;
    a2 = 0;
    result = memset(v_stack_m248, a2, 512, a4);
    if (v_stack_m2B8 == 1) {
        a2 = v_stack_m290;
        a1 = a3 + 144;
        result = AdtpBuildContextFromSecurityDescriptor(a1, a2, 512, a4);
    }
    if (v_stack_m2B6 == 1) {
        a1 = v_stack_m2A8;
        a2 = v_stack_m278;
        result = AdtpBuildContextFromSecurityDescriptor(a1, a2, 512, a4);
    }
    a4 = 0;
loc_0040EFF4:
    if (0 >= 7) goto loc_0040F0E2;
    if (v_stack_m2B5 != 1) goto loc_0040F060;
    result = AdtpPermissionBitPosition((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 4141361 + 0 * 4)))), a2, (unsigned int)(*(unsigned int *)(v_rip - 4141361 + 0 * 4)), a4);
    if ((*(unsigned int *)(a3 + (unsigned __int8)(result) * 4 + 4)) >= 0) goto loc_0040F0DB;
    result = (0) << (4);
    v_r14 = (v_stack_m248) + (result);
    v_stack_m2E0 = v_r14;
    v_stack_m2E8 = a3 + 4;
    v_stack_m2F8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 4141361 + 0 * 4)));
    result = AdtpBuildStagingReasonAuditStringInternal(v_stack_m298, v_stack_m2A0, v_stack_m290, v_stack_m278);
    goto loc_0040F0BF;
loc_0040F060:
    a3 = (unsigned int)((v_stack_m290) & (*(unsigned int *)(a3)));
    if (condition_is_equal) goto loc_0040F0DB;
    v_stack_m2C0 = v_stack_m2B4;
    v_stack_m2C8 = v_stack_m278;
    v_stack_m2D0 = v_stack_m278;
    v_stack_m2D8 = v_stack_m278;
    result = (0) << (4);
    v_r14 = (v_stack_m248) + (result);
    v_stack_m2E0 = v_r14;
    v_stack_m2E8 = a3 + 4;
    v_stack_m2F0 = (unsigned __int8)(*(unsigned __int8 *)(a3 + 136));
    v_stack_m2F8 = (unsigned int)(a3);
    result = AdtpBuildAccessReasonAuditStringInternal(v_stack_m298, v_stack_m2A0, v_stack_m290, v_stack_m278);
loc_0040F0BF:
    a4 = 0;
    if (sign_flag) goto loc_0040F2BA;
    v_r13 = (unsigned int)((0) + ((unsigned int)(*(unsigned __int16 *)(v_r14))));
    v_stack_m2B0 = (unsigned int)(v_r13);
    v_r12 = (unsigned int)((0) + 1);
loc_0040F0DB:
    v_rbx = (unsigned int)((0) + 1);
    goto loc_0040EFF4;
loc_0040F0E2:
    if ((*(unsigned __int16 *)(a3)) == 0) goto loc_0040F1CE;
loc_0040F0F5:
    if (0 >= 16) goto loc_0040F1CE;
    if (v_stack_m2B5 != 1) goto loc_0040F14B;
    if ((*(unsigned int *)(a3 + 0 * 4 + 4)) >= 0) goto loc_0040F1C4;
    result = ((unsigned int)((unsigned int)(v_r12))) << (4);
    v_r13 = (v_stack_m248) + (result);
    v_stack_m2E0 = v_r13;
    v_stack_m2E8 = a3 + 4;
    v_stack_m2F8 = 1;
    result = AdtpBuildStagingReasonAuditStringInternal(v_stack_m298, v_stack_m2A0, v_stack_m290, v_stack_m278);
    goto loc_0040F1AB;
loc_0040F14B:
    a1 = (unsigned int)((1) & (*(unsigned int *)(a3)));
    if (condition_is_equal) goto loc_0040F1C4;
    v_stack_m2C0 = v_stack_m2B4;
    v_stack_m2C8 = v_stack_m278;
    v_stack_m2D0 = v_stack_m278;
    v_stack_m2D8 = v_stack_m278;
    result = ((unsigned int)((unsigned int)(v_r12))) << (4);
    v_r13 = (v_stack_m248) + (result);
    v_stack_m2E0 = v_r13;
    v_stack_m2E8 = a3 + 4;
    v_stack_m2F0 = (unsigned __int8)(*(unsigned __int8 *)(a3 + 136));
    v_stack_m2F8 = (unsigned int)(a1);
    result = AdtpBuildAccessReasonAuditStringInternal(v_stack_m298, v_stack_m2A0, v_stack_m290, v_stack_m278);
loc_0040F1AB:
    a4 = 0;
    if (sign_flag) goto loc_0040F2BA;
    v_r12 = (unsigned int)((v_r12) + 1);
loc_0040F1C4:
    v_rbx = (unsigned int)((0) + 1);
    v_r14 = (unsigned int)((1) + (1));
    goto loc_0040F0F5;
loc_0040F1CE:
    result = (unsigned int)(((unsigned int)(v_stack_m2B0)) >> (1));
    v_stack_m2B0 = (unsigned int)(result);
    if (v_stack_m260 == 0) goto loc_0040F205;
    if (v_stack_m258 == 0) goto loc_0040F205;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m258)) + result + 1 * 1)) >= 0x400ULL) goto loc_0040F205;
    *(unsigned int *)(v_stack_m258) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m258)) + result + 1 * 1);
    goto loc_0040F231;
loc_0040F205:
    a2 = ((unsigned int)((unsigned int)(result + 1))) + ((unsigned int)((unsigned int)(result + 1)));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x6B416553ULL), a4);
    a4 = 0;
    if (result != 0) goto loc_0040F22F;
    goto loc_0040F2BA;
loc_0040F22F:
loc_0040F231:
    *(unsigned __int8 *)(v_stack_m250) = 1;
    if ((unsigned int)(v_r12) == 0) goto loc_0040F281;
    v_stack_m2A8 = (unsigned int)((unsigned int)(v_r12));
loc_0040F24B:
    result = (unsigned int)((unsigned int)(v_r12));
    v_r13 = 0;
    if (*(unsigned __int64 *)(v_stack_m248 + 8) != 0) {
        a3 = *(unsigned __int16 *)(v_stack_m248);
        a1 = 0;
        a1 = (a1) + (result);
        result = memcpy(a1, *(unsigned __int64 *)(v_stack_m248 + 8), a3, a4);
        result = *(unsigned __int16 *)(v_stack_m248);
        v_r13 = (unsigned int)((0) + ((unsigned int)(result)));
        result = v_stack_m2A8;
        a4 = 0;
    }
    v_r14 = (v_stack_m248) + (16);
    result = (result) - (1);
    v_stack_m2A8 = result;
    if (condition_is_not_equal) goto loc_0040F24B;
loc_0040F281:
    *(unsigned __int16 *)(result + (unsigned int)(v_stack_m2B0) * 2) = 0;
    if (a6 == 0) goto loc_0040F2A0;
    *(unsigned __int64 *)(a6) = result;
    *(unsigned int *)(a6 + 8) = (unsigned int)(result + 1 + result + 1 * 1);
    *(unsigned int *)(a6 + 12) = 0;
    goto loc_0040F2BA;
loc_0040F2A0:
    v_rbx = (unsigned __int16)((result + 1) + ((unsigned __int16)(result + 1)));
    *(unsigned __int64 *)(0 + 8) = result;
    *(unsigned __int16 *)(0 + 2) = (unsigned __int16)(v_rbx);
    *(unsigned __int16 *)(a4) = (unsigned __int16)(v_rbx - 2);
loc_0040F2BA:
    if ((unsigned int)(v_r12) == 0) goto loc_0040F2E2;
loc_0040F2C6:
    result = v_rbx - 2;
    if (*(unsigned __int64 *)(v_stack_m240) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m240), a2, a3, a4);
        a4 = 0;
    }
    v_rbx = (v_stack_m240) + (16);
    v_rsi = ((unsigned int)((unsigned int)(v_r12))) - (1);
    if (condition_is_not_equal) goto loc_0040F2C6;
loc_0040F2E2:
    if (v_stack_m288 == 0) goto loc_0040F2FB;
    if (v_stack_m280 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m280, a2, a3, a4);
        a4 = 0;
    }
    if (v_stack_m270 == 0) goto loc_0040F311;
    if (v_stack_m268 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m268, a2, a3, a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (736);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AdtpBuildAccessReasonAuditString(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, uint64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m218;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint32_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint32_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint32_t v_stack_m2B0;
    uint8_t v_stack_m2B4;
    uint8_t v_stack_m2B5;
    uint8_t v_stack_m2B6;
    uint8_t v_stack_m2B7;
    uint8_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint8_t v_stack_m2F0;
    uint32_t v_stack_m2F8;
    uint64_t v_stack_m48;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (736);
    result = (*(uint64_t *)(v_rip + 0x9FB916)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m260 = Arg7;
    v_stack_m258 = Arg8;
    v_stack_m250 = Arg9;
    result = 0;
    v_stack_m2B5 = (uint8_t)(Arg4);
    Arg4 = 0;
    v_stack_m2A0 = Arg2;
    v_stack_m298 = Arg1;
    v_stack_m2B4 = 0;
    v_stack_m2B0 = 0;
    v_stack_m2B8 = 0;
    v_stack_m2B6 = 0;
    v_stack_m2B7 = 0;
    v_stack_m2A8 = 0;
    v_stack_m290 = v_xmm0;
    v_stack_m280 = 0;
    v_stack_m278 = v_xmm1;
    v_stack_m268 = 0;
    if ((*(uint32_t *)(arg3)) != 0) goto loc_0040EEC9;
loc_0040EEB3:
    if (Arg6 == 0) goto loc_0040F2E2;
    result = AdtpEtwBuildDashString(Arg6, Arg2, Arg3, Arg4);
    goto loc_0040F2E2;
loc_0040EEC9:
loc_0040EED3:
    if (0 >= 32) goto loc_0040EFA9;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3 + 0x0 * 4 + 0x4))) & (0xFF0000ULL));
    if (condition_is_equal) goto loc_0040EFA1;
    if (((uint32_t)(Arg1)) == 0x10000ULL) goto loc_0040EF88;
    if (((uint32_t)(Arg1)) == 0x20000ULL) goto loc_0040EF88;
    if (((uint32_t)(Arg1)) == 0x30000ULL) goto loc_0040EF2D;
    if (((uint32_t)(Arg1)) == 0x40000ULL) goto loc_0040EF2D;
    if (((uint32_t)(Arg1)) == 0x50000ULL) goto loc_0040EF88;
    if (((uint32_t)(Arg1)) == 0x60000ULL) goto loc_0040EF2D;
    goto loc_0040EFA1;
loc_0040EF2D:
    result = AdtpIsSDValidSelfRelative(Arg3 + 144, v_stack_m2B7, Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_0040EF55;
    if (v_stack_m2B7 != 0) goto loc_0040EF5C;
loc_0040EF4B:
    goto loc_0040F2E2;
loc_0040EF55:
    if (((uint32_t)(result)) != 0xC0000058ULL) goto loc_0040EF4B;
loc_0040EF5C:
    result = RtlLengthSecurityDescriptor(Arg3 + 144, v_stack_m2B7, Arg3, Arg4);
    Arg2 = 0;
    result = ((uint32_t)((uint32_t)(result))) + (Arg3 + 144);
    v_stack_m2A8 = result;
    result = AdtpIsSDValidSelfRelative(result, Arg2, Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_0040EF4B;
    v_stack_m2B6 = 1;
    goto loc_0040EF9C;
loc_0040EF88:
    Arg2 = 0;
    result = AdtpIsSDValidSelfRelative(Arg3 + 144, Arg2, Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_0040EF4B;
loc_0040EF9C:
    v_stack_m2B8 = 1;
loc_0040EFA1:
    local_r14 = (uint32_t)((0) + 1);
    goto loc_0040EED3;
loc_0040EFA9:
    if (0 == 1) goto loc_0040EEB3;
    Arg2 = 0;
    result = memset(v_stack_m248, Arg2, 512, Arg4);
    if (v_stack_m2B8 == 1) {
        Arg2 = v_stack_m290;
        Arg1 = Arg3 + 144;
        result = AdtpBuildContextFromSecurityDescriptor(Arg1, Arg2, 512, Arg4);
    }
    if (v_stack_m2B6 == 1) {
        Arg1 = v_stack_m2A8;
        Arg2 = v_stack_m278;
        result = AdtpBuildContextFromSecurityDescriptor(Arg1, Arg2, 512, Arg4);
    }
    Arg4 = 0;
loc_0040EFF4:
    if (0 >= 7) goto loc_0040F0E2;
    if (v_stack_m2B5 != 1) goto loc_0040F060;
    result = AdtpPermissionBitPosition((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3F3131 + 0x0 * 4)))), Arg2, (uint32_t)(*(uint32_t *)(v_rip - 0x3F3131 + 0x0 * 4)), Arg4);
    if ((*(uint32_t *)(arg3 + (uint8_t)(result) * 4 + 0x4)) >= 0) goto loc_0040F0DB;
    result = (0) << (4);
    local_r14 = (v_stack_m248) + (result);
    v_stack_m2E0 = local_r14;
    v_stack_m2E8 = Arg3 + 4;
    v_stack_m2F8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3F3131 + 0x0 * 4)));
    result = AdtpBuildStagingReasonAuditStringInternal(v_stack_m298, v_stack_m2A0, v_stack_m290, v_stack_m278);
    goto loc_0040F0BF;
loc_0040F060:
    Arg3 = (uint32_t)((v_stack_m290) & (*(uint32_t *)(arg3)));
    if (condition_is_equal) goto loc_0040F0DB;
    v_stack_m2C0 = v_stack_m2B4;
    v_stack_m2C8 = v_stack_m278;
    v_stack_m2D0 = v_stack_m278;
    v_stack_m2D8 = v_stack_m278;
    result = (0) << (4);
    local_r14 = (v_stack_m248) + (result);
    v_stack_m2E0 = local_r14;
    v_stack_m2E8 = Arg3 + 4;
    v_stack_m2F0 = (uint8_t)(*(uint8_t *)(arg3 + 0x88));
    v_stack_m2F8 = (uint32_t)(Arg3);
    result = AdtpBuildAccessReasonAuditStringInternal(v_stack_m298, v_stack_m2A0, v_stack_m290, v_stack_m278);
loc_0040F0BF:
    Arg4 = 0;
    if (sign_flag) goto loc_0040F2BA;
    local_r13 = (uint32_t)((0) + ((uint32_t)(*(uint16_t *)(local_r14))));
    v_stack_m2B0 = (uint32_t)(local_r13);
    local_r12 = (uint32_t)((0) + 1);
loc_0040F0DB:
    local_rbx = (uint32_t)((0) + 1);
    goto loc_0040EFF4;
loc_0040F0E2:
    if ((*(uint16_t *)(arg3)) == 0) goto loc_0040F1CE;
loc_0040F0F5:
    if (0 >= 16) goto loc_0040F1CE;
    if (v_stack_m2B5 != 1) goto loc_0040F14B;
    if ((*(uint32_t *)(arg3 + 0x0 * 4 + 0x4)) >= 0) goto loc_0040F1C4;
    result = ((uint32_t)((uint32_t)(local_r12))) << (4);
    local_r13 = (v_stack_m248) + (result);
    v_stack_m2E0 = local_r13;
    v_stack_m2E8 = Arg3 + 4;
    v_stack_m2F8 = 1;
    result = AdtpBuildStagingReasonAuditStringInternal(v_stack_m298, v_stack_m2A0, v_stack_m290, v_stack_m278);
    goto loc_0040F1AB;
loc_0040F14B:
    Arg1 = (uint32_t)((1) & (*(uint32_t *)(arg3)));
    if (condition_is_equal) goto loc_0040F1C4;
    v_stack_m2C0 = v_stack_m2B4;
    v_stack_m2C8 = v_stack_m278;
    v_stack_m2D0 = v_stack_m278;
    v_stack_m2D8 = v_stack_m278;
    result = ((uint32_t)((uint32_t)(local_r12))) << (4);
    local_r13 = (v_stack_m248) + (result);
    v_stack_m2E0 = local_r13;
    v_stack_m2E8 = Arg3 + 4;
    v_stack_m2F0 = (uint8_t)(*(uint8_t *)(arg3 + 0x88));
    v_stack_m2F8 = (uint32_t)(Arg1);
    result = AdtpBuildAccessReasonAuditStringInternal(v_stack_m298, v_stack_m2A0, v_stack_m290, v_stack_m278);
loc_0040F1AB:
    Arg4 = 0;
    if (sign_flag) goto loc_0040F2BA;
    local_r12 = (uint32_t)((local_r12) + 1);
loc_0040F1C4:
    local_rbx = (uint32_t)((0) + 1);
    local_r14 = (uint32_t)((1) + (1));
    goto loc_0040F0F5;
loc_0040F1CE:
    result = (uint32_t)(((uint32_t)(v_stack_m2B0)) >> (1));
    v_stack_m2B0 = (uint32_t)(result);
    if (v_stack_m260 == 0) goto loc_0040F205;
    if (v_stack_m258 == 0) goto loc_0040F205;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m258)) + result + 1 * 1)) >= 0x400ULL) goto loc_0040F205;
    *(uint32_t *)(v_stack_m258) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m258)) + result + 1 * 1);
    goto loc_0040F231;
loc_0040F205:
    Arg2 = ((uint32_t)((uint32_t)(result + 1))) + ((uint32_t)((uint32_t)(result + 1)));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x6B416553ULL), Arg4);
    Arg4 = 0;
    if (result != 0) goto loc_0040F22F;
    goto loc_0040F2BA;
loc_0040F22F:
loc_0040F231:
    *(uint8_t *)(v_stack_m250) = 1;
    if ((uint32_t)(local_r12) == 0) goto loc_0040F281;
    v_stack_m2A8 = (uint32_t)((uint32_t)(local_r12));
loc_0040F24B:
    result = (uint32_t)((uint32_t)(local_r12));
    local_r13 = 0;
    if (*(uint64_t *)(v_stack_m248 + 0x8) != 0) {
        Arg3 = *(uint16_t *)(v_stack_m248);
        Arg1 = 0;
        Arg1 = (Arg1) + (result);
        result = memcpy(Arg1, *(uint64_t *)(v_stack_m248 + 0x8), Arg3, Arg4);
        result = *(uint16_t *)(v_stack_m248);
        local_r13 = (uint32_t)((0) + ((uint32_t)(result)));
        result = v_stack_m2A8;
        Arg4 = 0;
    }
    local_r14 = (v_stack_m248) + (16);
    result = (result) - (1);
    v_stack_m2A8 = result;
    if (condition_is_not_equal) goto loc_0040F24B;
loc_0040F281:
    *(uint16_t *)(result + (uint32_t)(v_stack_m2B0) * 2) = 0;
    if (Arg6 == 0) goto loc_0040F2A0;
    *(uint64_t *)(Arg6) = result;
    *(uint32_t *)(Arg6 + 0x8) = (uint32_t)(result + 1 + result + 1 * 1);
    *(uint32_t *)(Arg6 + 0xC) = 0;
    goto loc_0040F2BA;
loc_0040F2A0:
    local_rbx = (uint16_t)((result + 1) + ((uint16_t)(result + 1)));
    *(uint64_t *)(0 + 0x8) = result;
    *(uint16_t *)(0 + 0x2) = (uint16_t)(local_rbx);
    *(uint16_t *)(Arg4) = (uint16_t)(local_rbx - 2);
loc_0040F2BA:
    if ((uint32_t)(local_r12) == 0) goto loc_0040F2E2;
loc_0040F2C6:
    result = local_rbx - 2;
    if (*(uint64_t *)(v_stack_m240) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m240), Arg2, Arg3, Arg4);
        Arg4 = 0;
    }
    local_rbx = (v_stack_m240) + (16);
    local_rsi = ((uint32_t)((uint32_t)(local_r12))) - (1);
    if (condition_is_not_equal) goto loc_0040F2C6;
loc_0040F2E2:
    if (v_stack_m288 == 0) goto loc_0040F2FB;
    if (v_stack_m280 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m280, Arg2, Arg3, Arg4);
        Arg4 = 0;
    }
    if (v_stack_m270 == 0) goto loc_0040F311;
    if (v_stack_m268 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m268, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (736);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `16` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x4` | `64` | `R` |
| `Arg3` | `+ 0x4 + rax*4` | `32` | `R` |
| `Arg3` | `+ 0x4 + rdx*4` | `32` | `R` |
| `Arg3` | `+ 0x88` | `8` | `R` |
| `Arg3` | `+ 0x90` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0040EE04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
