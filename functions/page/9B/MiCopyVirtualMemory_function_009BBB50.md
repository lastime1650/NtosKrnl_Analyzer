# MiCopyVirtualMemory

- RVA: `0x009BBB50`–`0x009BC579` (길이 `2,601` bytes)
- VA: `0x00000001409BBB50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EFAC`
- 디코드: `575`개 명령, `2,601/2,601` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009BBBF6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009BBCC6` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x009BBD61` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (function, `0x00316690`)
- `0x009BBE99` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009BBEB8` → [MiDbgReadWriteEnclave](MiDbgReadWriteEnclave_function_009BC580.md) (function, `0x009BC580`)
- `0x009BBEE2` → [VslDebugReadWriteSecureProcess](VslDebugReadWriteSecureProcess_function_009BC670.md) (function, `0x009BC670`)
- `0x009BBEFC` → [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) (function, `0x0023B990`)
- `0x009BBF81` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)
- `0x009BBFA0` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009BBFC4` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x009BC01C` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x009BC08A` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (function, `0x00316690`)
- `0x009BC122` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009BC162` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x009BC16F` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)
- `0x009BC186` → [MiDbgReadWriteEnclave](MiDbgReadWriteEnclave_function_009BC580.md) (function, `0x009BC580`)
- `0x009BC1B3` → [VslDebugReadWriteSecureProcess](VslDebugReadWriteSecureProcess_function_009BC670.md) (function, `0x009BC670`)
- `0x009BC1E4` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x009BC1F6` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)
- `0x009BC23E` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x009BC24B` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)
- `0x009BC25A` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009BC2B2` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009BC2D8` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x009BC2EF` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009BC306` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009BC345` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x009BC35E` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x009BC403` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009BC422` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009BC43E` → [MiVadRangeIsIoSpace](../../text/4D/MiVadRangeIsIoSpace_function_004D5CD4.md) (function, `0x004D5CD4`)
- `0x009BC460` → [MiVadRangeIsIoSpace](../../text/4D/MiVadRangeIsIoSpace_function_004D5CD4.md) (function, `0x004D5CD4`)
- `0x009BC4A0` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)

### Direct callers
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ACDFA`
- [MiReadWriteVirtualMemory](MiReadWriteVirtualMemory_function_009BB4E0.md) at `0x009BB6AB`
- [MmCopyVirtualMemory](MmCopyVirtualMemory_function_009BBB10.md) at `0x009BBB38`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE44E7`

### Static image references
- `0x009BBB63` → RVA `0x00E0A740` (`.data`; read)
- `0x009BBD44` → RVA `0x00E2DB78` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **29**
  - `0x009BBBF6` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009BBCC6` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x009BBD61` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (`PAGE` → `.text`)
  - `0x009BBE99` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009BBEFC` → [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) (`PAGE` → `.text`)
  - `0x009BBF81` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (`PAGE` → `.text`)
  - `0x009BBFA0` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009BBFC4` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x009BC01C` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x009BC08A` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (`PAGE` → `.text`)
  - `0x009BC122` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009BC162` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x009BC16F` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (`PAGE` → `.text`)
  - `0x009BC1E4` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x009BC1F6` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (`PAGE` → `.text`)
  - `0x009BC23E` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x009BC24B` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (`PAGE` → `.text`)
  - `0x009BC25A` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009BC2B2` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009BC2D8` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x009BC2EF` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009BC306` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009BC345` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (`PAGE` → `.text`)
  - `0x009BC35E` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x009BC403` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009BC422` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009BC43E` → [MiVadRangeIsIoSpace](../../text/4D/MiVadRangeIsIoSpace_function_004D5CD4.md) (`PAGE` → `.text`)
  - `0x009BC460` → [MiVadRangeIsIoSpace](../../text/4D/MiVadRangeIsIoSpace_function_004D5CD4.md) (`PAGE` → `.text`)
  - `0x009BC4A0` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009BBB50  40 53                           push rbx
009BBB52  56                              push rsi
009BBB53  57                              push rdi
009BBB54  41 54                           push r12
009BBB56  41 55                           push r13
009BBB58  41 56                           push r14
009BBB5A  41 57                           push r15
009BBB5C  48 81 EC E0 03 00 00            sub rsp, 0x3e0
009BBB63  48 8B 05 D6 EB 44 00            mov rax, qword ptr [rip + 0x44ebd6]
009BBB6A  48 33 C4                        xor rax, rsp
009BBB6D  48 89 84 24 D0 03 00 00         mov qword ptr [rsp + 0x3d0], rax
009BBB75  4D 8B F9                        mov r15, r9
009BBB78  4C 89 8C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r9
009BBB80  4D 8B E8                        mov r13, r8
009BBB83  4C 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], r8
009BBB8B  48 8B FA                        mov rdi, rdx
009BBB8E  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
009BBB93  48 8B D9                        mov rbx, rcx
009BBB96  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
009BBB9B  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
009BBBA3  48 89 94 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rdx
009BBBAB  4C 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r8
009BBBB3  4C 89 8C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r9
009BBBBB  48 8B 84 24 50 04 00 00         mov rax, qword ptr [rsp + 0x450]
009BBBC3  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
009BBBCB  0F 57 C0                        xorps xmm0, xmm0
009BBBCE  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
009BBBD6  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
009BBBDE  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
009BBBE6  33 D2                           xor edx, edx
009BBBE8  41 B8 A8 00 00 00               mov r8d, 0xa8
009BBBEE  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
009BBBF6  E8 45 B0 D0 FF                  call 0x1406c6c40
009BBBFB  33 F6                           xor esi, esi
009BBBFD  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
009BBC02  4C 8B A4 24 40 04 00 00         mov r12, qword ptr [rsp + 0x440]
009BBC0A  4D 85 E4                        test r12, r12
009BBC0D  0F 84 92 06 00 00               je 0x1409bc2a5
009BBC13  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
009BBC1B  48 89 30                        mov qword ptr [rax], rsi
009BBC1E  8B 8C 24 58 04 00 00            mov ecx, dword ptr [rsp + 0x458]
009BBC25  83 E1 01                        and ecx, 1
009BBC28  C1 E1 04                        shl ecx, 4
009BBC2B  FF C1                           inc ecx
009BBC2D  8B D1                           mov edx, ecx
009BBC2F  83 CA 04                        or edx, 4
009BBC32  F6 83 70 01 00 00 01            test byte ptr [rbx + 0x170], 1
009BBC39  0F 44 D1                        cmove edx, ecx
009BBC3C  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
009BBC44  4C 8B F7                        mov r14, rdi
009BBC47  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
009BBC4C  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
009BBC51  4C 89 A4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r12
009BBC59  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
009BBC5E  48 8D 84 24 20 01 00 00         lea rax, [rsp + 0x120]
009BBC66  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
009BBC6E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009BBC77  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
009BBC7F  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
009BBC83  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
009BBC88  48 89 B4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rsi
009BBC90  89 74 24 70                     mov dword ptr [rsp + 0x70], esi
009BBC94  8B DA                           mov ebx, edx
009BBC96  83 CB 08                        or ebx, 8
009BBC99  41 F6 85 70 01 00 00 01         test byte ptr [r13 + 0x170], 1
009BBCA1  0F 44 DA                        cmove ebx, edx
009BBCA4  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
009BBCA9  4D 85 ED                        test r13, r13
009BBCAC  0F 84 D9 05 00 00               je 0x1409bc28b
009BBCB2  4D 8B FD                        mov r15, r13
009BBCB5  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
009BBCB9  48 8D 94 24 F0 00 00 00         lea rdx, [rsp + 0xf0]
009BBCC1  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009BBCC6  E8 35 AB 85 FF                  call 0x140216800
009BBCCB  4C 3B F7                        cmp r14, rdi
009BBCCE  75 42                           jne 0x1409bbd12
009BBCD0  80 BC 24 48 04 00 00 00         cmp byte ptr [rsp + 0x448], 0
009BBCD8  74 38                           je 0x1409bbd12
009BBCDA  4A 8D 04 27                     lea rax, [rdi + r12]
009BBCDE  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
009BBCE8  48 3B C1                        cmp rax, rcx
009BBCEB  77 05                           ja 0x1409bbcf2
009BBCED  48 3B C7                        cmp rax, rdi
009BBCF0  73 08                           jae 0x1409bbcfa
009BBCF2  0F B6 01                        movzx eax, byte ptr [rcx]
009BBCF5  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
009BBCFA  EB 16                           jmp 0x1409bbd12
009BBCFC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009BBD00  4C 8B A4 24 40 04 00 00         mov r12, qword ptr [rsp + 0x440]
009BBD08  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
009BBD0D  E9 D3 05 00 00                  jmp 0x1409bc2e5
009BBD12  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
009BBD1A  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
009BBD24  4C 3B F0                        cmp r14, rax
009BBD27  0F 83 48 06 00 00               jae 0x1409bc375
009BBD2D  49 8B CE                        mov rcx, r14
009BBD30  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
009BBD37  48 81 F9 00 00 FE 7F            cmp rcx, 0x7ffe0000
009BBD3E  0F 84 A4 07 00 00               je 0x1409bc4e8
009BBD44  48 8B 05 2D 1E 47 00            mov rax, qword ptr [rip + 0x471e2d]
009BBD4B  48 3B C8                        cmp rcx, rax
009BBD4E  0F 84 8B 07 00 00               je 0x1409bc4df
009BBD54  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
009BBD59  BA 02 00 00 00                  mov edx, 2
009BBD5E  49 8B CE                        mov rcx, r14
009BBD61  E8 2A A9 95 FF                  call 0x140316690
009BBD66  48 8B F0                        mov rsi, rax
009BBD69  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
009BBD71  48 85 C0                        test rax, rax
009BBD74  0F 84 63 05 00 00               je 0x1409bc2dd
009BBD7A  0F B6 40 21                     movzx eax, byte ptr [rax + 0x21]
009BBD7E  48 C1 E0 20                     shl rax, 0x20
009BBD82  8B 4E 1C                        mov ecx, dword ptr [rsi + 0x1c]
009BBD85  48 0B C1                        or rax, rcx
009BBD88  48 C1 E0 0C                     shl rax, 0xc
009BBD8C  48 0D FF 0F 00 00               or rax, 0xfff
009BBD92  48 FF C0                        inc rax
009BBD95  33 FF                           xor edi, edi
009BBD97  49 2B C6                        sub rax, r14
009BBD9A  4C 3B E8                        cmp r13, rax
009BBD9D  4C 0F 47 F8                     cmova r15, rax
009BBDA1  44 8B F7                        mov r14d, edi
009BBDA4  48 85 F6                        test rsi, rsi
009BBDA7  74 13                           je 0x1409bbdbc
009BBDA9  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
009BBDAC  25 00 00 20 0C                  and eax, 0xc200000
009BBDB1  3D 00 00 20 08                  cmp eax, 0x8200000
009BBDB6  0F 84 7E 07 00 00               je 0x1409bc53a
009BBDBC  F6 C3 10                        test bl, 0x10
009BBDBF  74 12                           je 0x1409bbdd3
009BBDC1  48 85 F6                        test rsi, rsi
009BBDC4  74 0D                           je 0x1409bbdd3
009BBDC6  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
009BBDC9  24 70                           and al, 0x70
009BBDCB  3C 10                           cmp al, 0x10
009BBDCD  0F 84 85 06 00 00               je 0x1409bc458
009BBDD3  83 E3 FD                        and ebx, 0xfffffffd
009BBDD6  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
009BBDDA  4D 85 FF                        test r15, r15
009BBDDD  0F 84 96 01 00 00               je 0x1409bbf79
009BBDE3  F6 C3 04                        test bl, 4
009BBDE6  75 20                           jne 0x1409bbe08
009BBDE8  45 85 F6                        test r14d, r14d
009BBDEB  75 1B                           jne 0x1409bbe08
009BBDED  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
009BBDF2  48 83 B8 80 02 00 00 00         cmp qword ptr [rax + 0x280], 0
009BBDFA  75 0C                           jne 0x1409bbe08
009BBDFC  F6 C3 01                        test bl, 1
009BBDFF  74 07                           je 0x1409bbe08
009BBE01  83 CB 02                        or ebx, 2
009BBE04  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
009BBE08  49 81 FF 00 02 00 00            cmp r15, 0x200
009BBE0F  0F 83 69 05 00 00               jae 0x1409bc37e
009BBE15  83 E3 FD                        and ebx, 0xfffffffd
009BBE18  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
009BBE1C  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
009BBE24  48 85 C0                        test rax, rax
009BBE27  0F 85 23 06 00 00               jne 0x1409bc450
009BBE2D  49 81 FF 00 02 00 00            cmp r15, 0x200
009BBE34  0F 87 44 06 00 00               ja 0x1409bc47e
009BBE3A  48 8D 84 24 D0 01 00 00         lea rax, [rsp + 0x1d0]
009BBE42  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009BBE47  49 8B FF                        mov rdi, r15
009BBE4A  4C 3B FF                        cmp r15, rdi
009BBE4D  4C 0F 47 FF                     cmova r15, rdi
009BBE51  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
009BBE56  4C 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r15
009BBE5E  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
009BBE66  0F B6 79 7D                     movzx edi, byte ptr [rcx + 0x7d]
009BBE6A  40 88 7C 24 34                  mov byte ptr [rsp + 0x34], dil
009BBE6F  40 0F B6 C7                     movzx eax, dil
009BBE73  0C 04                           or al, 4
009BBE75  88 41 7D                        mov byte ptr [rcx + 0x7d], al
009BBE78  F6 C3 02                        test bl, 2
009BBE7B  75 6C                           jne 0x1409bbee9
009BBE7D  F6 C3 04                        test bl, 4
009BBE80  75 41                           jne 0x1409bbec3
009BBE82  41 83 FE 02                     cmp r14d, 2
009BBE86  74 3B                           je 0x1409bbec3
009BBE88  4D 8B C7                        mov r8, r15
009BBE8B  41 83 FE 01                     cmp r14d, 1
009BBE8F  74 0F                           je 0x1409bbea0
009BBE91  49 8B D2                        mov rdx, r10
009BBE94  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
009BBE99  E8 A2 A9 D0 FF                  call 0x1406c6840
009BBE9E  EB 61                           jmp 0x1409bbf01
009BBEA0  48 8D 44 24 58                  lea rax, [rsp + 0x58]
009BBEA5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009BBEAA  41 B9 01 00 00 00               mov r9d, 1
009BBEB0  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
009BBEB5  49 8B CA                        mov rcx, r10
009BBEB8  E8 C3 06 00 00                  call 0x1409bc580
009BBEBD  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009BBEC1  EB 3E                           jmp 0x1409bbf01
009BBEC3  48 8D 44 24 58                  lea rax, [rsp + 0x58]
009BBEC8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009BBECD  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
009BBED2  4D 8B CF                        mov r9, r15
009BBED5  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
009BBEDA  49 8B D2                        mov rdx, r10
009BBEDD  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009BBEE2  E8 89 07 00 00                  call 0x1409bc670
009BBEE7  EB D4                           jmp 0x1409bbebd
009BBEE9  45 33 C0                        xor r8d, r8d
009BBEEC  0F B6 94 24 48 04 00 00         movzx edx, byte ptr [rsp + 0x448]
009BBEF4  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
009BBEFC  E8 8F FA 87 FF                  call 0x14023b990
009BBF01  EB 64                           jmp 0x1409bbf67
009BBF03  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009BBF07  4C 8B A4 24 40 04 00 00         mov r12, qword ptr [rsp + 0x440]
009BBF0F  4C 8B BC 24 B0 00 00 00         mov r15, qword ptr [rsp + 0xb0]
009BBF17  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
009BBF1C  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
009BBF24  8B 5C 24 38                     mov ebx, dword ptr [rsp + 0x38]
009BBF28  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
009BBF30  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009BBF35  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
009BBF3D  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009BBF42  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
009BBF4A  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
009BBF52  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
009BBF5A  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
009BBF62  0F B6 7C 24 34                  movzx edi, byte ptr [rsp + 0x34]
009BBF67  40 F6 C7 04                     test dil, 4
009BBF6B  75 0C                           jne 0x1409bbf79
009BBF6D  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
009BBF75  80 61 7D FB                     and byte ptr [rcx + 0x7d], 0xfb
009BBF79  48 85 F6                        test rsi, rsi
009BBF7C  74 08                           je 0x1409bbf86
009BBF7E  48 8B CE                        mov rcx, rsi
009BBF81  E8 8A 2F 8F FF                  call 0x1402aef10
009BBF86  8B FB                           mov edi, ebx
009BBF88  83 E7 02                        and edi, 2
009BBF8B  83 7C 24 30 00                  cmp dword ptr [rsp + 0x30], 0
009BBF90  0F 8C 77 04 00 00               jl 0x1409bc40d
009BBF96  33 D2                           xor edx, edx
009BBF98  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
009BBFA0  E8 8B BD 85 FF                  call 0x140217d30
009BBFA5  33 F6                           xor esi, esi
009BBFA7  85 FF                           test edi, edi
009BBFA9  0F 85 79 03 00 00               jne 0x1409bc328
009BBFAF  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
009BBFB4  48 8D 94 24 F0 00 00 00         lea rdx, [rsp + 0xf0]
009BBFBC  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
009BBFC4  E8 37 A8 85 FF                  call 0x140216800
009BBFC9  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
009BBFCE  48 39 44 24 50                  cmp qword ptr [rsp + 0x50], rax
009BBFD3  75 5E                           jne 0x1409bc033
009BBFD5  80 BC 24 48 04 00 00 00         cmp byte ptr [rsp + 0x448], 0
009BBFDD  74 54                           je 0x1409bc033
009BBFDF  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
009BBFE7  4A 8D 04 21                     lea rax, [rcx + r12]
009BBFEB  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
009BBFF5  48 3B C2                        cmp rax, rdx
009BBFF8  77 05                           ja 0x1409bbfff
009BBFFA  48 3B C1                        cmp rax, rcx
009BBFFD  73 08                           jae 0x1409bc007
009BBFFF  0F B6 02                        movzx eax, byte ptr [rdx]
009BC002  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
009BC007  EB 2A                           jmp 0x1409bc033
009BC009  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009BC00D  F6 44 24 38 02                  test byte ptr [rsp + 0x38], 2
009BC012  74 0D                           je 0x1409bc021
009BC014  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
009BC01C  E8 BF 2E 8E FF                  call 0x14029eee0
009BC021  4C 8B A4 24 40 04 00 00         mov r12, qword ptr [rsp + 0x440]
009BC029  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
009BC02E  E9 B2 02 00 00                  jmp 0x1409bc2e5
009BC033  48 8B FE                        mov rdi, rsi
009BC036  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
009BC03E  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
009BC043  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
009BC04D  4C 3B D0                        cmp r10, rax
009BC050  0F 83 C9 02 00 00               jae 0x1409bc31f
009BC056  49 8B CA                        mov rcx, r10
009BC059  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
009BC060  48 81 F9 00 00 FE 7F            cmp rcx, 0x7ffe0000
009BC067  0F 84 A3 04 00 00               je 0x1409bc510
009BC06D  48 8B 05 04 1B 47 00            mov rax, qword ptr [rip + 0x471b04]
009BC074  48 3B C8                        cmp rcx, rax
009BC077  0F 84 D8 04 00 00               je 0x1409bc555
009BC07D  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
009BC082  BA 02 00 00 00                  mov edx, 2
009BC087  49 8B CA                        mov rcx, r10
009BC08A  E8 01 A6 95 FF                  call 0x140316690
009BC08F  48 8B F8                        mov rdi, rax
009BC092  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
009BC09A  48 85 C0                        test rax, rax
009BC09D  0F 84 28 02 00 00               je 0x1409bc2cb
009BC0A3  0F B6 48 21                     movzx ecx, byte ptr [rax + 0x21]
009BC0A7  48 C1 E1 20                     shl rcx, 0x20
009BC0AB  8B 40 1C                        mov eax, dword ptr [rax + 0x1c]
009BC0AE  48 0B C8                        or rcx, rax
009BC0B1  48 C1 E1 0C                     shl rcx, 0xc
009BC0B5  48 81 C9 FF 0F 00 00            or rcx, 0xfff
009BC0BC  48 FF C1                        inc rcx
009BC0BF  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
009BC0C4  49 2B CA                        sub rcx, r10
009BC0C7  4C 3B F9                        cmp r15, rcx
009BC0CA  4C 0F 47 F9                     cmova r15, rcx
009BC0CE  48 85 FF                        test rdi, rdi
009BC0D1  74 13                           je 0x1409bc0e6
009BC0D3  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
009BC0D6  25 00 00 20 0C                  and eax, 0xc200000
009BC0DB  3D 00 00 20 08                  cmp eax, 0x8200000
009BC0E0  0F 84 7A 04 00 00               je 0x1409bc560
009BC0E6  F6 C3 10                        test bl, 0x10
009BC0E9  74 12                           je 0x1409bc0fd
009BC0EB  48 85 FF                        test rdi, rdi
009BC0EE  74 0D                           je 0x1409bc0fd
009BC0F0  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
009BC0F3  24 70                           and al, 0x70
009BC0F5  3C 10                           cmp al, 0x10
009BC0F7  0F 84 3B 03 00 00               je 0x1409bc438
009BC0FD  4D 85 FF                        test r15, r15
009BC100  0F 84 B4 00 00 00               je 0x1409bc1ba
009BC106  F6 C3 08                        test bl, 8
009BC109  0F 85 84 00 00 00               jne 0x1409bc193
009BC10F  83 FE 02                        cmp esi, 2
009BC112  74 7F                           je 0x1409bc193
009BC114  4D 8B C7                        mov r8, r15
009BC117  49 8B D6                        mov rdx, r14
009BC11A  49 8B CA                        mov rcx, r10
009BC11D  83 FE 01                        cmp esi, 1
009BC120  74 57                           je 0x1409bc179
009BC122  E8 19 A7 D0 FF                  call 0x1406c6840
009BC127  33 F6                           xor esi, esi
009BC129  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
009BC12D  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
009BC132  8B C6                           mov eax, esi
009BC134  85 C0                           test eax, eax
009BC136  0F 89 97 00 00 00               jns 0x1409bc1d3
009BC13C  3D 05 00 00 C0                  cmp eax, 0xc0000005
009BC141  75 12                           jne 0x1409bc155
009BC143  4C 2B 6C 24 58                  sub r13, qword ptr [rsp + 0x58]
009BC148  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
009BC14D  C7 44 24 30 0D 00 00 80         mov dword ptr [rsp + 0x30], 0x8000000d
009BC155  F6 C3 02                        test bl, 2
009BC158  74 0D                           je 0x1409bc167
009BC15A  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
009BC162  E8 79 2D 8E FF                  call 0x14029eee0
009BC167  48 85 FF                        test rdi, rdi
009BC16A  74 08                           je 0x1409bc174
009BC16C  48 8B CF                        mov rcx, rdi
009BC16F  E8 9C 2D 8F FF                  call 0x1402aef10
009BC174  E9 6C 01 00 00                  jmp 0x1409bc2e5
009BC179  48 8D 44 24 58                  lea rax, [rsp + 0x58]
009BC17E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009BC183  45 33 C9                        xor r9d, r9d
009BC186  E8 F5 03 00 00                  call 0x1409bc580
009BC18B  33 F6                           xor esi, esi
009BC18D  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009BC191  EB A1                           jmp 0x1409bc134
009BC193  48 8D 44 24 58                  lea rax, [rsp + 0x58]
009BC198  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009BC19D  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
009BC1A2  4D 8B CF                        mov r9, r15
009BC1A5  4D 8B C6                        mov r8, r14
009BC1A8  49 8B D2                        mov rdx, r10
009BC1AB  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
009BC1B3  E8 B8 04 00 00                  call 0x1409bc670
009BC1B8  EB D1                           jmp 0x1409bc18b
009BC1BA  33 F6                           xor esi, esi
009BC1BC  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
009BC1C1  C7 44 24 30 0D 00 00 80         mov dword ptr [rsp + 0x30], 0x8000000d
009BC1C9  B8 0D 00 00 80                  mov eax, 0x8000000d
009BC1CE  E9 61 FF FF FF                  jmp 0x1409bc134
009BC1D3  EB 5C                           jmp 0x1409bc231
009BC1D5  F6 44 24 38 02                  test byte ptr [rsp + 0x38], 2
009BC1DA  74 0D                           je 0x1409bc1e9
009BC1DC  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
009BC1E4  E8 F7 2C 8E FF                  call 0x14029eee0
009BC1E9  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
009BC1F1  48 85 C9                        test rcx, rcx
009BC1F4  74 05                           je 0x1409bc1fb
009BC1F6  E8 15 2D 8F FF                  call 0x1402aef10
009BC1FB  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
009BC200  83 7C 24 70 00                  cmp dword ptr [rsp + 0x70], 0
009BC205  74 15                           je 0x1409bc21c
009BC207  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
009BC20C  48 2B 84 24 C8 00 00 00         sub rax, qword ptr [rsp + 0xc8]
009BC214  4C 03 E8                        add r13, rax
009BC217  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
009BC21C  C7 44 24 30 0D 00 00 80         mov dword ptr [rsp + 0x30], 0x8000000d
009BC224  4C 8B A4 24 40 04 00 00         mov r12, qword ptr [rsp + 0x440]
009BC22C  E9 B4 00 00 00                  jmp 0x1409bc2e5
009BC231  F6 C3 02                        test bl, 2
009BC234  74 0D                           je 0x1409bc243
009BC236  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
009BC23E  E8 9D 2C 8E FF                  call 0x14029eee0
009BC243  48 85 FF                        test rdi, rdi
009BC246  74 08                           je 0x1409bc250
009BC248  48 8B CF                        mov rcx, rdi
009BC24B  E8 C0 2C 8F FF                  call 0x1402aef10
009BC250  33 D2                           xor edx, edx
009BC252  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
009BC25A  E8 D1 BA 85 FF                  call 0x140217d30
009BC25F  4D 2B EF                        sub r13, r15
009BC262  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
009BC267  4C 29 BC 24 A0 00 00 00         sub qword ptr [rsp + 0xa0], r15
009BC26F  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
009BC274  4D 03 F7                        add r14, r15
009BC277  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
009BC27C  4C 01 7C 24 68                  add qword ptr [rsp + 0x68], r15
009BC281  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
009BC286  E9 1E FA FF FF                  jmp 0x1409bbca9
009BC28B  48 83 BC 24 90 00 00 00 00      cmp qword ptr [rsp + 0x90], 0
009BC294  0F 85 62 01 00 00               jne 0x1409bc3fc
009BC29A  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
009BC2A2  4C 89 20                        mov qword ptr [rax], r12
009BC2A5  33 C0                           xor eax, eax
009BC2A7  48 8B 8C 24 D0 03 00 00         mov rcx, qword ptr [rsp + 0x3d0]
009BC2AF  48 33 CC                        xor rcx, rsp
009BC2B2  E8 89 03 CF FF                  call 0x1406ac640
009BC2B7  48 81 C4 E0 03 00 00            add rsp, 0x3e0
009BC2BE  41 5F                           pop r15
009BC2C0  41 5E                           pop r14
009BC2C2  41 5D                           pop r13
009BC2C4  41 5C                           pop r12
009BC2C6  5F                              pop rdi
009BC2C7  5E                              pop rsi
009BC2C8  5B                              pop rbx
009BC2C9  C3                              ret
009BC2CA  CC                              int3
009BC2CB  F6 C3 02                        test bl, 2
009BC2CE  74 0D                           je 0x1409bc2dd
009BC2D0  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
009BC2D8  E8 03 2C 8E FF                  call 0x14029eee0
009BC2DD  C7 44 24 30 0D 00 00 80         mov dword ptr [rsp + 0x30], 0x8000000d
009BC2E5  33 D2                           xor edx, edx
009BC2E7  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
009BC2EF  E8 3C BA 85 FF                  call 0x140217d30
009BC2F4  48 83 BC 24 90 00 00 00 00      cmp qword ptr [rsp + 0x90], 0
009BC2FD  74 0C                           je 0x1409bc30b
009BC2FF  33 D2                           xor edx, edx
009BC301  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
009BC306  E8 65 65 1C 00                  call 0x140b82870
009BC30B  4D 2B E5                        sub r12, r13
009BC30E  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
009BC316  4C 89 20                        mov qword ptr [rax], r12
009BC319  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
009BC31D  EB 88                           jmp 0x1409bc2a7
009BC31F  4B 8D 0C 3A                     lea rcx, [r10 + r15]
009BC323  E9 9C FD FF FF                  jmp 0x1409bc0c4
009BC328  C7 44 24 28 20 00 00 C0         mov dword ptr [rsp + 0x28], 0xc0000020
009BC330  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
009BC334  45 33 C9                        xor r9d, r9d
009BC337  33 D2                           xor edx, edx
009BC339  45 8D 41 01                     lea r8d, [r9 + 1]
009BC33D  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
009BC345  E8 B6 C4 95 FF                  call 0x140318800
009BC34A  4C 8B F0                        mov r14, rax
009BC34D  48 85 C0                        test rax, rax
009BC350  0F 85 5E FC FF FF               jne 0x1409bbfb4
009BC356  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
009BC35E  E8 7D 2B 8E FF                  call 0x14029eee0
009BC363  83 E3 FE                        and ebx, 0xfffffffe
009BC366  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
009BC36B  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
009BC370  E9 34 F9 FF FF                  jmp 0x1409bbca9
009BC375  4B 8D 04 2E                     lea rax, [r14 + r13]
009BC379  E9 17 FA FF FF                  jmp 0x1409bbd95
009BC37E  F6 C3 02                        test bl, 2
009BC381  0F 84 8E FA FF FF               je 0x1409bbe15
009BC387  B8 00 E0 00 00                  mov eax, 0xe000
009BC38C  4C 3B F8                        cmp r15, rax
009BC38F  4C 0F 47 F8                     cmova r15, rax
009BC393  48 89 BC 24 20 01 00 00         mov qword ptr [rsp + 0x120], rdi
009BC39B  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
009BC3A0  41 8B D2                        mov edx, r10d
009BC3A3  8B CA                           mov ecx, edx
009BC3A5  81 E1 FF 0F 00 00               and ecx, 0xfff
009BC3AB  48 81 C1 FF 0F 00 00            add rcx, 0xfff
009BC3B2  49 03 CF                        add rcx, r15
009BC3B5  48 C1 E9 0C                     shr rcx, 0xc
009BC3B9  66 83 C1 06                     add cx, 6
009BC3BD  66 C1 E1 03                     shl cx, 3
009BC3C1  66 89 8C 24 28 01 00 00         mov word ptr [rsp + 0x128], cx
009BC3C9  66 89 BC 24 2A 01 00 00         mov word ptr [rsp + 0x12a], di
009BC3D1  49 8B C2                        mov rax, r10
009BC3D4  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
009BC3DA  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
009BC3E2  81 E2 FF 0F 00 00               and edx, 0xfff
009BC3E8  89 94 24 4C 01 00 00            mov dword ptr [rsp + 0x14c], edx
009BC3EF  44 89 BC 24 48 01 00 00         mov dword ptr [rsp + 0x148], r15d
009BC3F7  E9 5A FA FF FF                  jmp 0x1409bbe56
009BC3FC  33 D2                           xor edx, edx
009BC3FE  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
009BC403  E8 68 64 1C 00                  call 0x140b82870
009BC408  E9 8D FE FF FF                  jmp 0x1409bc29a
009BC40D  85 FF                           test edi, edi
009BC40F  0F 84 C8 FE FF FF               je 0x1409bc2dd
009BC415  83 E3 FE                        and ebx, 0xfffffffe
009BC418  33 D2                           xor edx, edx
009BC41A  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
009BC422  E8 09 B9 85 FF                  call 0x140217d30
009BC427  33 F6                           xor esi, esi
009BC429  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
009BC42E  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
009BC433  E9 71 F8 FF FF                  jmp 0x1409bbca9
009BC438  4D 8B C7                        mov r8, r15
009BC43B  49 8B D2                        mov rdx, r10
009BC43E  E8 91 98 B1 FF                  call 0x1404d5cd4
009BC443  4C 8B F8                        mov r15, rax
009BC446  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
009BC44B  E9 AD FC FF FF                  jmp 0x1409bc0fd
009BC450  48 8B F8                        mov rdi, rax
009BC453  E9 F2 F9 FF FF                  jmp 0x1409bbe4a
009BC458  4D 8B C7                        mov r8, r15
009BC45B  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
009BC460  E8 6F 98 B1 FF                  call 0x1404d5cd4
009BC465  4C 8B F8                        mov r15, rax
009BC468  48 85 C0                        test rax, rax
009BC46B  0F 85 62 F9 FF FF               jne 0x1409bbdd3
009BC471  C7 44 24 30 05 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000005
009BC479  E9 55 F9 FF FF                  jmp 0x1409bbdd3
009BC47E  48 8B BC 24 A0 00 00 00         mov rdi, qword ptr [rsp + 0xa0]
009BC486  B9 00 00 01 00                  mov ecx, 0x10000
009BC48B  48 3B F9                        cmp rdi, rcx
009BC48E  48 0F 47 F9                     cmova rdi, rcx
009BC492  41 B8 4D 6D 52 77               mov r8d, 0x77526d4d
009BC498  48 8B D7                        mov rdx, rdi
009BC49B  B9 00 01 00 00                  mov ecx, 0x100
009BC4A0  E8 9B F0 99 FF                  call 0x14035b540
009BC4A5  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009BC4AA  48 85 C0                        test rax, rax
009BC4AD  74 0D                           je 0x1409bc4bc
009BC4AF  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
009BC4B7  E9 8E F9 FF FF                  jmp 0x1409bbe4a
009BC4BC  48 D1 EF                        shr rdi, 1
009BC4BF  48 81 FF 00 02 00 00            cmp rdi, 0x200
009BC4C6  77 CA                           ja 0x1409bc492
009BC4C8  48 8D 84 24 D0 01 00 00         lea rax, [rsp + 0x1d0]
009BC4D0  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009BC4D5  BF 00 02 00 00                  mov edi, 0x200
009BC4DA  E9 6B F9 FF FF                  jmp 0x1409bbe4a
009BC4DF  48 85 C0                        test rax, rax
009BC4E2  0F 84 6C F8 FF FF               je 0x1409bbd54
009BC4E8  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
009BC4ED  8B 80 FC 05 00 00               mov eax, dword ptr [rax + 0x5fc]
009BC4F3  A8 01                           test al, 1
009BC4F5  0F 85 59 F8 FF FF               jne 0x1409bbd54
009BC4FB  33 FF                           xor edi, edi
009BC4FD  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
009BC501  83 CB 20                        or ebx, 0x20
009BC504  48 8D 81 00 10 00 00            lea rax, [rcx + 0x1000]
009BC50B  E9 87 F8 FF FF                  jmp 0x1409bbd97
009BC510  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
009BC515  8B 80 FC 05 00 00               mov eax, dword ptr [rax + 0x5fc]
009BC51B  A8 01                           test al, 1
009BC51D  0F 85 5A FB FF FF               jne 0x1409bc07d
009BC523  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
009BC527  83 CB 20                        or ebx, 0x20
009BC52A  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
009BC52E  48 81 C1 00 10 00 00            add rcx, 0x1000
009BC535  E9 8A FB FF FF                  jmp 0x1409bc0c4
009BC53A  8B 46 40                        mov eax, dword ptr [rsi + 0x40]
009BC53D  A8 04                           test al, 4
009BC53F  0F 84 8E F8 FF FF               je 0x1409bbdd3
009BC545  24 01                           and al, 1
009BC547  F6 D8                           neg al
009BC549  45 1B F6                        sbb r14d, r14d
009BC54C  41 83 C6 02                     add r14d, 2
009BC550  E9 7E F8 FF FF                  jmp 0x1409bbdd3
009BC555  48 85 C0                        test rax, rax
009BC558  0F 84 1F FB FF FF               je 0x1409bc07d
009BC55E  EB B0                           jmp 0x1409bc510
009BC560  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
009BC563  A8 04                           test al, 4
009BC565  0F 84 92 FB FF FF               je 0x1409bc0fd
009BC56B  24 01                           and al, 1
009BC56D  F6 D8                           neg al
009BC56F  1B F6                           sbb esi, esi
009BC571  83 C6 02                        add esi, 2
009BC574  E9 84 FB FF FF                  jmp 0x1409bc0fd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCopyVirtualMemory(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int8 a6, __int64 a7, unsigned int a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m328;
    unsigned __int64 v_stack_m330;
    unsigned __int64 v_stack_m338;
    unsigned __int64 v_stack_m340;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_m350;
    unsigned __int64 v_stack_m358;
    unsigned __int64 v_stack_m360;
    unsigned __int64 v_stack_m368;
    unsigned __int64 v_stack_m370;
    unsigned __int64 v_stack_m378;
    unsigned __int64 v_stack_m380;
    unsigned __int64 v_stack_m388;
    unsigned __int64 v_stack_m390;
    unsigned __int64 v_stack_m398;
    unsigned __int64 v_stack_m3A0;
    unsigned int v_stack_m3A8;
    unsigned __int64 v_stack_m3B0;
    unsigned __int64 v_stack_m3B8;
    unsigned __int64 v_stack_m3C0;
    unsigned __int64 v_stack_m3C8;
    unsigned __int64 v_stack_m3D0;
    unsigned __int64 v_stack_m3D8;
    unsigned int v_stack_m3E0;
    unsigned __int8 v_stack_m3E4;
    unsigned int v_stack_m3E8;
    unsigned __int64 v_stack_m3F0;
    unsigned __int64 v_stack_m3F8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p120;
    unsigned __int16 v_stack_p128;
    unsigned __int16 v_stack_p12A;
    unsigned __int64 v_stack_p140;
    unsigned int v_stack_p148;
    unsigned int v_stack_p14C;
    unsigned __int64 v_stack_p1D0;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pF0;

    v_rsp = (v_rsp) - (992);
    result = (*(unsigned __int64 *)(v_rip + 4516822)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m358 = a4;
    v_stack_m380 = a3;
    v_stack_m3A0 = a2;
    v_stack_m3B8 = a1;
    v_stack_m348 = a1;
    v_stack_m340 = a2;
    v_stack_m338 = a3;
    v_stack_m330 = a4;
    v_stack_m370 = a7;
    v_stack_m328 = v_xmm0;
    v_stack_m318 = v_xmm0;
    v_stack_m308 = v_xmm0;
    a2 = 0;
    result = memset(v_stack_m2F8, a2, 168, a4);
    v_rsi = 0;
    v_stack_m3C0 = 0;
    if (a5 == 0) goto loc_009BC2A5;
    *(unsigned __int64 *)(v_stack_m370) = 0;
    a1 = (unsigned int)(((unsigned int)(a8)) & (1));
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + 1);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (4));
    if (((*(unsigned __int8 *)(a1 + 368)) & (1)) == 0) { a2 = (unsigned int)(a1); }
    v_stack_m388 = 0;
    v_stack_m3C8 = a2;
    v_stack_m3B0 = a4;
    v_stack_m378 = a5;
    v_stack_m3D8 = a5;
    v_stack_m390 = v_stack_m2F8;
    v_stack_m360 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m3E8 = 0;
    v_stack_m3D0 = 0;
    v_stack_m350 = 0;
    v_stack_m3A8 = 0;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (8));
    if (((*(unsigned __int8 *)(a3 + 368)) & (1)) == 0) { v_rbx = (unsigned int)(a2); }
loc_009BBCA9:
    if (v_stack_m3D8 == 0) goto loc_009BC28B;
    v_stack_m3E8 = 0;
    result = KeStackAttachProcess(v_stack_m3B8, v_stack_m328, 168, a4);
    if (a2 != a2) goto loc_009BBD12;
    if (a6 == 0) goto loc_009BBD12;
    if ((a2 + a5 * 1) > v_stack_m3B8) goto loc_009BBCF2;
    result = a2 + a5 * 1;
    v_r13 = v_stack_m3D8;
    if ((a2 + a5 * 1) < a2) {
        result = *(unsigned __int8 *)(v_stack_m3B8);
        v_r13 = v_stack_m3D8;
    }
    goto loc_009BBD12;
loc_009BBD12:
    v_stack_m398 = 0;
    if (a2 >= result) goto loc_009BC375;
    a1 = (a2) & (0xFFFFFFFFFFFFF000ULL);
    if (a1 == 0x7FFE0000ULL) goto loc_009BC4E8;
    if (a1 == (*(unsigned __int64 *)(v_rip + 4660781))) goto loc_009BC4DF;
loc_009BBD54:
    result = MiObtainReferencedVadEx(a2, 2, v_stack_m3E8, a4);
    v_stack_m398 = result;
    if (result == 0) goto loc_009BC2DD;
    result = (*(unsigned __int8 *)(result + 33)) << (32);
    result = (result) | ((unsigned int)(*(unsigned int *)(result + 28)));
    result = (result) << (12);
    result = (result) | (0xFFFULL);
    result = (result) + 1;
loc_009BBD95:
    v_rdi = 0;
loc_009BBD97:
    result = (result) - (a2);
    v_r15 = v_stack_m3D8;
    if (v_r13 > result) { v_r15 = result; }
    if (result == 0) goto loc_009BBDBC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0xC200000ULL));
    if (((unsigned int)(result)) == 0x8200000ULL) goto loc_009BC53A;
loc_009BBDBC:
    if ((((unsigned __int8)(v_rbx)) & (16)) == 0) goto loc_009BBDD3;
    if (result == 0) goto loc_009BBDD3;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(result + 48))) & (112));
    if (((unsigned __int8)(result)) == 16) goto loc_009BC458;
loc_009BBDD3:
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFDULL));
    v_stack_m3E0 = (unsigned int)(v_rbx);
    if (v_r15 == 0) goto loc_009BBF79;
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) goto loc_009BBE08;
    if (0 != 0) goto loc_009BBE08;
    if ((*(unsigned __int64 *)(v_stack_m3B8 + 640)) != 0) goto loc_009BBE08;
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) {
        v_rbx = (unsigned int)((v_rbx) | (2));
        v_stack_m3E0 = (unsigned int)(v_rbx);
    }
    if (v_r15 >= 512) goto loc_009BC37E;
loc_009BBE15:
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFDULL));
    v_stack_m3E0 = (unsigned int)(v_rbx);
    if (v_stack_m388 != 0) goto loc_009BC450;
    if (v_r15 > 512) goto loc_009BC47E;
    v_stack_m3D0 = v_stack_m248;
loc_009BBE4A:
    if (v_r15 > v_r15) { v_r15 = v_r15; }
loc_009BBE56:
    v_stack_m368 = v_r15;
    v_stack_m3E4 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m360 + 125));
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_stack_m360 + 125))) | (4));
    *(unsigned __int8 *)(v_stack_m360 + 125) = (unsigned __int8)(result);
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_009BBEE9;
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) goto loc_009BBEC3;
    if (0 == 2) goto loc_009BBEC3;
    if (0 == 1) goto loc_009BBEA0;
    result = memcpy(v_stack_m3D0, v_stack_m3C8, v_r15, a4);
    goto loc_009BBF01;
loc_009BBEA0:
    v_stack_m3F8 = v_stack_m3C0;
    result = MiDbgReadWriteEnclave(v_stack_m3C8, v_stack_m3D0, v_r15, 1);
loc_009BBEBD:
    v_stack_m3E8 = (unsigned int)(result);
    goto loc_009BBF01;
loc_009BBEC3:
    v_stack_m3F0 = v_stack_m3C0;
    v_stack_m3F8 = 1;
    result = VslDebugReadWriteSecureProcess(v_stack_m3B8, v_stack_m3C8, v_stack_m3D0, v_r15);
    goto loc_009BBEBD;
loc_009BBEE9:
    a3 = 0;
    result = MmProbeAndLockPages(v_stack_m2F8, a6, a3, v_r15);
loc_009BBF01:
    goto loc_009BBF67;
loc_009BBF67:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m360 + 125))) & (4)) == 0) {
        a1 = v_stack_m360;
    }
    if (result != 0) {
        a1 = result;
        result = MiUnlockAndDereferenceVadShared(a1, a6, a3, v_r15);
    }
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (2));
    if (v_stack_m3E8 < 0) goto loc_009BC40D;
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m328, a2, a3, v_r15);
    v_rsi = 0;
    if ((unsigned int)(v_rdi) != 0) goto loc_009BC328;
loc_009BBFB4:
    result = KeStackAttachProcess(v_stack_m380, v_stack_m328, a3, v_r15);
    if (v_stack_m3C8 != v_stack_m3A0) goto loc_009BC033;
    if (a6 == 0) goto loc_009BC033;
    if ((v_stack_m358 + a5 * 1) > v_stack_m328) goto loc_009BBFFF;
    result = v_stack_m358 + a5 * 1;
    if ((v_stack_m358 + a5 * 1) < v_stack_m358) {
        result = *(unsigned __int8 *)(v_stack_m328);
        v_r13 = v_stack_m3D8;
    }
    goto loc_009BC033;
loc_009BC033:
    v_stack_m398 = 0;
    if (v_stack_m3B0 >= result) goto loc_009BC31F;
    a1 = (v_stack_m3B0) & (0xFFFFFFFFFFFFF000ULL);
    if (a1 == 0x7FFE0000ULL) goto loc_009BC510;
    if (a1 == (*(unsigned __int64 *)(v_rip + 4659972))) goto loc_009BC555;
loc_009BC07D:
    result = MiObtainReferencedVadEx(v_stack_m3B0, 2, v_stack_m3E8, v_r15);
    v_stack_m398 = result;
    if (result == 0) goto loc_009BC2CB;
    a1 = (*(unsigned __int8 *)(result + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(result + 28)));
    a1 = (a1) << (12);
    a1 = (a1) | (0xFFFULL);
    a1 = (a1) + 1;
loc_009BC0C4:
    a1 = (a1) - (v_stack_m3B0);
    if (v_r15 > a1) { v_r15 = a1; }
    if (result == 0) goto loc_009BC0E6;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0xC200000ULL));
    if (((unsigned int)(result)) == 0x8200000ULL) goto loc_009BC560;
loc_009BC0E6:
    if ((((unsigned __int8)(v_rbx)) & (16)) == 0) goto loc_009BC0FD;
    if (result == 0) goto loc_009BC0FD;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(result + 48))) & (112));
    if (((unsigned __int8)(result)) == 16) goto loc_009BC438;
loc_009BC0FD:
    if (v_r15 == 0) goto loc_009BC1BA;
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) goto loc_009BC193;
    if (0 == 2) goto loc_009BC193;
    if (0 == 1) goto loc_009BC179;
    result = memcpy(v_stack_m3B0, v_stack_m3D0, v_r15, v_r15);
    v_rsi = 0;
    v_stack_m3E8 = 0;
    v_stack_m3C0 = v_r15;
loc_009BC134:
    if (!sign_flag) goto loc_009BC1D3;
    if (0 == 0xC0000005ULL) {
        v_r13 = (v_r13) - (v_stack_m3C0);
        v_stack_m3D8 = v_r13;
        v_stack_m3E8 = 0x8000000DULL;
    }
    result = 0;
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) {
        a1 = v_stack_m390;
        result = MmUnlockPages(a1, v_stack_m3D0, v_r15, v_r15);
    }
    if (result != 0) {
        a1 = result;
        result = MiUnlockAndDereferenceVadShared(a1, v_stack_m3D0, v_r15, v_r15);
    }
    goto loc_009BC2E5;
loc_009BC179:
    v_stack_m3F8 = v_stack_m3C0;
    a4 = 0;
    result = MiDbgReadWriteEnclave(a1, v_stack_m3D0, v_r15, a4);
loc_009BC18B:
    v_rsi = 0;
    v_stack_m3E8 = (unsigned int)(result);
    goto loc_009BC134;
loc_009BC193:
    v_stack_m3F0 = v_stack_m3C0;
    v_stack_m3F8 = 0;
    result = VslDebugReadWriteSecureProcess(v_stack_m380, v_stack_m3B0, v_stack_m3D0, v_r15);
    goto loc_009BC18B;
loc_009BC1BA:
    v_rsi = 0;
    v_stack_m3C0 = 0;
    v_stack_m3E8 = 0x8000000DULL;
    goto loc_009BC134;
loc_009BC1D3:
    goto loc_009BC231;
loc_009BC231:
    result = (unsigned int)(0x8000000DULL);
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) {
        a1 = v_stack_m2F8;
        result = MmUnlockPages(a1, v_stack_m3B0, v_stack_m3D0, v_r15);
    }
    if (result != 0) {
        a1 = result;
        result = MiUnlockAndDereferenceVadShared(a1, v_stack_m3B0, v_stack_m3D0, v_r15);
    }
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m328, a2, v_stack_m3D0, v_r15);
    v_r13 = (v_r13) - (v_r15);
    v_stack_m3D8 = v_r13;
    v_r14 = (v_stack_m3C8) + (v_r15);
    v_stack_m3C8 = v_r14;
    goto loc_009BBCA9;
loc_009BC28B:
    if (v_stack_m388 != 0) goto loc_009BC3FC;
loc_009BC29A:
    *(unsigned __int64 *)(v_stack_m370) = a5;
loc_009BC2A5:
    result = 0;
loc_009BC2A7:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m3D0, v_r15);
    v_rsp = (v_rsp) + (992);
    return result;
loc_009BC2CB:
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) {
        a1 = v_stack_p88;
        result = MmUnlockPages(a1, a2, v_stack_m3D0, v_r15);
    }
    v_stack_p30 = 0x8000000DULL;
loc_009BC2E5:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF0, a2, v_stack_m3D0, v_r15);
    if (v_stack_p90 != 0) {
        a2 = 0;
        a1 = v_stack_p48;
        result = ExFreePoolWithTag(a1, a2, v_stack_m3D0, v_r15);
    }
    v_r12 = (a5) - (v_r13);
    *(unsigned __int64 *)(v_stack_pA8) = v_r12;
    goto loc_009BC2A7;
loc_009BC31F:
    goto loc_009BC0C4;
loc_009BC328:
    v_stack_p28 = 0xC0000020ULL;
    v_stack_p20 = 0;
    a4 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(v_stack_p120, a2, a4 + 1, a4);
    if (result != 0) goto loc_009BBFB4;
    result = MmUnlockPages(v_stack_p120, a2, a4 + 1, a4);
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFEULL));
    goto loc_009BBCA9;
loc_009BC375:
    goto loc_009BBD95;
loc_009BC37E:
    if ((((unsigned __int8)(v_rbx)) & (2)) == 0) goto loc_009BBE15;
    if (v_r15 > ((unsigned int)(0xE000ULL))) { v_r15 = (unsigned int)(0xE000ULL); }
    v_stack_p120 = v_stack_p78;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p50))))) & (0xFFFULL));
    a1 = (a1) + (0xFFFULL);
    a1 = (a1) + (v_r15);
    a1 = (a1) >> (12);
    a1 = (unsigned __int16)((a1) + (6));
    a1 = (unsigned __int16)((a1) << (3));
    v_stack_p128 = (unsigned __int16)(a1);
    v_stack_p12A = (unsigned __int16)(v_stack_p78);
    result = (v_stack_p50) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p140 = result;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p50))) & (0xFFFULL));
    v_stack_p14C = (unsigned int)(a2);
    v_stack_p148 = (unsigned int)(v_r15);
    goto loc_009BBE56;
loc_009BC3FC:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p48, a2, a4 + 1, a4);
    goto loc_009BC29A;
loc_009BC40D:
    if ((unsigned int)(v_stack_p78) == 0) goto loc_009BC2DD;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFEULL));
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF0, a2, a4 + 1, a4);
    v_rsi = 0;
    goto loc_009BBCA9;
loc_009BC438:
    result = MiVadRangeIsIoSpace(v_stack_pF0, v_stack_p50, v_r15, a4);
    goto loc_009BC0FD;
loc_009BC450:
    goto loc_009BBE4A;
loc_009BC458:
    result = MiVadRangeIsIoSpace(v_stack_pF0, v_stack_p50, result, a4);
    if (result != 0) goto loc_009BBDD3;
    v_stack_p30 = 0xC0000005ULL;
    goto loc_009BBDD3;
loc_009BC47E:
    v_rdi = v_stack_pA0;
    if (v_stack_pA0 > ((unsigned int)(0x10000ULL))) { v_rdi = (unsigned int)(0x10000ULL); }
loc_009BC492:
    result = MiAllocatePool(256, v_rdi, (unsigned int)(0x77526D4DULL), a4);
    v_stack_p48 = result;
    if (result == 0) goto loc_009BC4BC;
    v_stack_p90 = v_rdi;
    goto loc_009BBE4A;
loc_009BC4BC:
    v_rdi = (v_rdi) >> (1);
    if (v_rdi > 512) goto loc_009BC492;
    v_stack_p48 = v_stack_p1D0;
    goto loc_009BBE4A;
loc_009BC4DF:
    if (v_stack_p1D0 == 0) goto loc_009BBD54;
loc_009BC4E8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p60 + 1532)))) & (1)) != 0) goto loc_009BBD54;
    v_rdi = 0;
    v_stack_p30 = 0;
    v_rbx = (unsigned int)((v_rbx) | (32));
    goto loc_009BBD97;
loc_009BC510:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p60 + 1532)))) & (1)) != 0) goto loc_009BC07D;
    v_stack_p30 = 0;
    v_rbx = (unsigned int)((v_rbx) | (32));
    v_stack_p38 = (unsigned int)(v_rbx);
    a1 = (256) + (0x1000ULL);
    goto loc_009BC0C4;
loc_009BC53A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 64)))) & (4)) == 0) goto loc_009BBDD3;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rsi + 64))) & (1));
    result = (unsigned __int8)(-(result));
    v_r14 = (unsigned int)((v_stack_p50) + (2));
    goto loc_009BBDD3;
loc_009BC555:
    if (result == 0) goto loc_009BC07D;
    goto loc_009BC510;
loc_009BC560:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 64)))) & (4)) == 0) goto loc_009BC0FD;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rdi + 64))) & (1));
    result = (unsigned __int8)(-(result));
    v_rsi = (unsigned int)((v_rsi) + (2));
    goto loc_009BC0FD;
}
```

## 5. (Beta) C Style

```c
int64_t MiCopyVirtualMemory(void *Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, int64_t Arg5, uint8_t Arg6, int64_t Arg7, uint32_t Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m248;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m308;
    uint64_t v_stack_m318;
    uint64_t v_stack_m328;
    uint64_t v_stack_m330;
    uint64_t v_stack_m338;
    uint64_t v_stack_m340;
    uint64_t v_stack_m348;
    uint64_t v_stack_m350;
    uint64_t v_stack_m358;
    uint64_t v_stack_m360;
    uint64_t v_stack_m368;
    uint64_t v_stack_m370;
    uint64_t v_stack_m378;
    uint64_t v_stack_m380;
    uint64_t v_stack_m388;
    uint64_t v_stack_m390;
    uint64_t v_stack_m398;
    uint64_t v_stack_m3A0;
    uint32_t v_stack_m3A8;
    uint64_t v_stack_m3B0;
    uint64_t v_stack_m3B8;
    uint64_t v_stack_m3C0;
    uint64_t v_stack_m3C8;
    uint64_t v_stack_m3D0;
    uint64_t v_stack_m3D8;
    uint32_t v_stack_m3E0;
    uint8_t v_stack_m3E4;
    uint32_t v_stack_m3E8;
    uint64_t v_stack_m3F0;
    uint64_t v_stack_m3F8;
    uint64_t v_stack_m48;
    uint64_t v_stack_p120;
    uint16_t v_stack_p128;
    uint16_t v_stack_p12A;
    uint64_t v_stack_p140;
    uint32_t v_stack_p148;
    uint32_t v_stack_p14C;
    uint64_t v_stack_p1D0;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p78;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pF0;

    local_rsp = (local_rsp) - (992);
    result = (*(uint64_t *)(v_rip + 0x44EBD6)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m358 = Arg4;
    v_stack_m380 = Arg3;
    v_stack_m3A0 = Arg2;
    v_stack_m3B8 = Arg1;
    v_stack_m348 = Arg1;
    v_stack_m340 = Arg2;
    v_stack_m338 = Arg3;
    v_stack_m330 = Arg4;
    v_stack_m370 = Arg7;
    v_stack_m328 = v_xmm0;
    v_stack_m318 = v_xmm0;
    v_stack_m308 = v_xmm0;
    Arg2 = 0;
    result = memset(v_stack_m2F8, Arg2, 168, Arg4);
    local_rsi = 0;
    v_stack_m3C0 = 0;
    if (Arg5 == 0) goto loc_009BC2A5;
    *(uint64_t *)(v_stack_m370) = 0;
    Arg1 = (uint32_t)(((uint32_t)(Arg8)) & (1));
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (4));
    if (((*(uint8_t *)(arg1 + 0x170)) & (1)) == 0) { Arg2 = (uint32_t)(Arg1); }
    v_stack_m388 = 0;
    v_stack_m3C8 = Arg2;
    v_stack_m3B0 = Arg4;
    v_stack_m378 = Arg5;
    v_stack_m3D8 = Arg5;
    v_stack_m390 = v_stack_m2F8;
    v_stack_m360 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m3E8 = 0;
    v_stack_m3D0 = 0;
    v_stack_m350 = 0;
    v_stack_m3A8 = 0;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) | (8));
    if (((*(uint8_t *)(arg3 + 0x170)) & (1)) == 0) { local_rbx = (uint32_t)(Arg2); }
loc_009BBCA9:
    if (v_stack_m3D8 == 0) goto loc_009BC28B;
    v_stack_m3E8 = 0;
    result = KeStackAttachProcess(v_stack_m3B8, v_stack_m328, 168, Arg4);
    if (Arg2 != Arg2) goto loc_009BBD12;
    if (Arg6 == 0) goto loc_009BBD12;
    if ((Arg2 + Arg5 * 1) > v_stack_m3B8) goto loc_009BBCF2;
    result = Arg2 + Arg5 * 1;
    local_r13 = v_stack_m3D8;
    if ((Arg2 + Arg5 * 1) < Arg2) {
        result = *(uint8_t *)(v_stack_m3B8);
        local_r13 = v_stack_m3D8;
    }
    goto loc_009BBD12;
loc_009BBD12:
    v_stack_m398 = 0;
    if (Arg2 >= result) goto loc_009BC375;
    Arg1 = (Arg2) & (0xFFFFFFFFFFFFF000ULL);
    if (Arg1 == 0x7FFE0000ULL) goto loc_009BC4E8;
    if (Arg1 == (*(uint64_t *)(v_rip + 0x471E2D))) goto loc_009BC4DF;
loc_009BBD54:
    result = MiObtainReferencedVadEx(Arg2, 2, v_stack_m3E8, Arg4);
    v_stack_m398 = result;
    if (result == 0) goto loc_009BC2DD;
    result = (*(uint8_t *)(result + 0x21)) << (32);
    result = (result) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    result = (result) << (12);
    result = (result) | (0xFFFULL);
    result = (result) + 1;
loc_009BBD95:
    local_rdi = 0;
loc_009BBD97:
    result = (result) - (Arg2);
    local_r15 = v_stack_m3D8;
    if (local_r13 > result) { local_r15 = result; }
    if (result == 0) goto loc_009BBDBC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0xC200000ULL));
    if (((uint32_t)(result)) == 0x8200000ULL) goto loc_009BC53A;
loc_009BBDBC:
    if ((((uint8_t)(local_rbx)) & (16)) == 0) goto loc_009BBDD3;
    if (result == 0) goto loc_009BBDD3;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (112));
    if (((uint8_t)(result)) == 16) goto loc_009BC458;
loc_009BBDD3:
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFDULL));
    v_stack_m3E0 = (uint32_t)(local_rbx);
    if (local_r15 == 0) goto loc_009BBF79;
    if ((((uint8_t)(local_rbx)) & (4)) != 0) goto loc_009BBE08;
    if (0 != 0) goto loc_009BBE08;
    if ((*(uint64_t *)(v_stack_m3B8 + 0x280)) != 0) goto loc_009BBE08;
    if ((((uint8_t)(local_rbx)) & (1)) != 0) {
        local_rbx = (uint32_t)((local_rbx) | (2));
        v_stack_m3E0 = (uint32_t)(local_rbx);
    }
    if (local_r15 >= 512) goto loc_009BC37E;
loc_009BBE15:
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFDULL));
    v_stack_m3E0 = (uint32_t)(local_rbx);
    if (v_stack_m388 != 0) goto loc_009BC450;
    if (local_r15 > 512) goto loc_009BC47E;
    v_stack_m3D0 = v_stack_m248;
loc_009BBE4A:
    if (local_r15 > local_r15) { local_r15 = local_r15; }
loc_009BBE56:
    v_stack_m368 = local_r15;
    v_stack_m3E4 = (uint8_t)(*(uint8_t *)(v_stack_m360 + 0x7D));
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(v_stack_m360 + 0x7D))) | (4));
    *(uint8_t *)(v_stack_m360 + 0x7D) = (uint8_t)(result);
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_009BBEE9;
    if ((((uint8_t)(local_rbx)) & (4)) != 0) goto loc_009BBEC3;
    if (0 == 2) goto loc_009BBEC3;
    if (0 == 1) goto loc_009BBEA0;
    result = memcpy(v_stack_m3D0, v_stack_m3C8, local_r15, Arg4);
    goto loc_009BBF01;
loc_009BBEA0:
    v_stack_m3F8 = v_stack_m3C0;
    result = MiDbgReadWriteEnclave(v_stack_m3C8, v_stack_m3D0, local_r15, 1);
loc_009BBEBD:
    v_stack_m3E8 = (uint32_t)(result);
    goto loc_009BBF01;
loc_009BBEC3:
    v_stack_m3F0 = v_stack_m3C0;
    v_stack_m3F8 = 1;
    result = VslDebugReadWriteSecureProcess(v_stack_m3B8, v_stack_m3C8, v_stack_m3D0, local_r15);
    goto loc_009BBEBD;
loc_009BBEE9:
    Arg3 = 0;
    result = MmProbeAndLockPages(v_stack_m2F8, Arg6, Arg3, local_r15);
loc_009BBF01:
    goto loc_009BBF67;
loc_009BBF67:
    if ((((uint8_t)(*(uint8_t *)(v_stack_m360 + 0x7D))) & (4)) == 0) {
        Arg1 = v_stack_m360;
    }
    if (result != 0) {
        Arg1 = result;
        result = MiUnlockAndDereferenceVadShared(Arg1, Arg6, Arg3, local_r15);
    }
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (2));
    if (v_stack_m3E8 < 0) goto loc_009BC40D;
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m328, Arg2, Arg3, local_r15);
    local_rsi = 0;
    if ((uint32_t)(local_rdi) != 0) goto loc_009BC328;
loc_009BBFB4:
    result = KeStackAttachProcess(v_stack_m380, v_stack_m328, Arg3, local_r15);
    if (v_stack_m3C8 != v_stack_m3A0) goto loc_009BC033;
    if (Arg6 == 0) goto loc_009BC033;
    if ((v_stack_m358 + Arg5 * 1) > v_stack_m328) goto loc_009BBFFF;
    result = v_stack_m358 + Arg5 * 1;
    if ((v_stack_m358 + Arg5 * 1) < v_stack_m358) {
        result = *(uint8_t *)(v_stack_m328);
        local_r13 = v_stack_m3D8;
    }
    goto loc_009BC033;
loc_009BC033:
    v_stack_m398 = 0;
    if (v_stack_m3B0 >= result) goto loc_009BC31F;
    Arg1 = (v_stack_m3B0) & (0xFFFFFFFFFFFFF000ULL);
    if (Arg1 == 0x7FFE0000ULL) goto loc_009BC510;
    if (Arg1 == (*(uint64_t *)(v_rip + 0x471B04))) goto loc_009BC555;
loc_009BC07D:
    result = MiObtainReferencedVadEx(v_stack_m3B0, 2, v_stack_m3E8, local_r15);
    v_stack_m398 = result;
    if (result == 0) goto loc_009BC2CB;
    Arg1 = (*(uint8_t *)(result + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    Arg1 = (Arg1) << (12);
    Arg1 = (Arg1) | (0xFFFULL);
    Arg1 = (Arg1) + 1;
loc_009BC0C4:
    Arg1 = (Arg1) - (v_stack_m3B0);
    if (local_r15 > Arg1) { local_r15 = Arg1; }
    if (result == 0) goto loc_009BC0E6;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0xC200000ULL));
    if (((uint32_t)(result)) == 0x8200000ULL) goto loc_009BC560;
loc_009BC0E6:
    if ((((uint8_t)(local_rbx)) & (16)) == 0) goto loc_009BC0FD;
    if (result == 0) goto loc_009BC0FD;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (112));
    if (((uint8_t)(result)) == 16) goto loc_009BC438;
loc_009BC0FD:
    if (local_r15 == 0) goto loc_009BC1BA;
    if ((((uint8_t)(local_rbx)) & (8)) != 0) goto loc_009BC193;
    if (0 == 2) goto loc_009BC193;
    if (0 == 1) goto loc_009BC179;
    result = memcpy(v_stack_m3B0, v_stack_m3D0, local_r15, local_r15);
    local_rsi = 0;
    v_stack_m3E8 = 0;
    v_stack_m3C0 = local_r15;
loc_009BC134:
    if (!sign_flag) goto loc_009BC1D3;
    if (0 == 0xC0000005ULL) {
        local_r13 = (local_r13) - (v_stack_m3C0);
        v_stack_m3D8 = local_r13;
        v_stack_m3E8 = 0x8000000DULL;
    }
    result = 0;
    if ((((uint8_t)(local_rbx)) & (2)) != 0) {
        Arg1 = v_stack_m390;
        result = MmUnlockPages(Arg1, v_stack_m3D0, local_r15, local_r15);
    }
    if (result != 0) {
        Arg1 = result;
        result = MiUnlockAndDereferenceVadShared(Arg1, v_stack_m3D0, local_r15, local_r15);
    }
    goto loc_009BC2E5;
loc_009BC179:
    v_stack_m3F8 = v_stack_m3C0;
    Arg4 = 0;
    result = MiDbgReadWriteEnclave(Arg1, v_stack_m3D0, local_r15, Arg4);
loc_009BC18B:
    local_rsi = 0;
    v_stack_m3E8 = (uint32_t)(result);
    goto loc_009BC134;
loc_009BC193:
    v_stack_m3F0 = v_stack_m3C0;
    v_stack_m3F8 = 0;
    result = VslDebugReadWriteSecureProcess(v_stack_m380, v_stack_m3B0, v_stack_m3D0, local_r15);
    goto loc_009BC18B;
loc_009BC1BA:
    local_rsi = 0;
    v_stack_m3C0 = 0;
    v_stack_m3E8 = 0x8000000DULL;
    goto loc_009BC134;
loc_009BC1D3:
    goto loc_009BC231;
loc_009BC231:
    result = (uint32_t)(0x8000000DULL);
    if ((((uint8_t)(local_rbx)) & (2)) != 0) {
        Arg1 = v_stack_m2F8;
        result = MmUnlockPages(Arg1, v_stack_m3B0, v_stack_m3D0, local_r15);
    }
    if (result != 0) {
        Arg1 = result;
        result = MiUnlockAndDereferenceVadShared(Arg1, v_stack_m3B0, v_stack_m3D0, local_r15);
    }
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m328, Arg2, v_stack_m3D0, local_r15);
    local_r13 = (local_r13) - (local_r15);
    v_stack_m3D8 = local_r13;
    local_r14 = (v_stack_m3C8) + (local_r15);
    v_stack_m3C8 = local_r14;
    goto loc_009BBCA9;
loc_009BC28B:
    if (v_stack_m388 != 0) goto loc_009BC3FC;
loc_009BC29A:
    *(uint64_t *)(v_stack_m370) = Arg5;
loc_009BC2A5:
    result = 0;
loc_009BC2A7:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m3D0, local_r15);
    local_rsp = (local_rsp) + (992);
    return result;
loc_009BC2CB:
    if ((((uint8_t)(local_rbx)) & (2)) != 0) {
        Arg1 = v_stack_p88;
        result = MmUnlockPages(Arg1, Arg2, v_stack_m3D0, local_r15);
    }
    v_stack_p30 = 0x8000000DULL;
loc_009BC2E5:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF0, Arg2, v_stack_m3D0, local_r15);
    if (v_stack_p90 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_p48;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m3D0, local_r15);
    }
    local_r12 = (Arg5) - (local_r13);
    *(uint64_t *)(v_stack_pA8) = local_r12;
    goto loc_009BC2A7;
loc_009BC31F:
    goto loc_009BC0C4;
loc_009BC328:
    v_stack_p28 = 0xC0000020ULL;
    v_stack_p20 = 0;
    Arg4 = 0;
    Arg2 = 0;
    result = MmMapLockedPagesSpecifyCache(v_stack_p120, Arg2, Arg4 + 1, Arg4);
    if (result != 0) goto loc_009BBFB4;
    result = MmUnlockPages(v_stack_p120, Arg2, Arg4 + 1, Arg4);
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFEULL));
    goto loc_009BBCA9;
loc_009BC375:
    goto loc_009BBD95;
loc_009BC37E:
    if ((((uint8_t)(local_rbx)) & (2)) == 0) goto loc_009BBE15;
    if (local_r15 > ((uint32_t)(0xE000ULL))) { local_r15 = (uint32_t)(0xE000ULL); }
    v_stack_p120 = v_stack_p78;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p50))))) & (0xFFFULL));
    Arg1 = (Arg1) + (0xFFFULL);
    Arg1 = (Arg1) + (local_r15);
    Arg1 = (Arg1) >> (12);
    Arg1 = (uint16_t)((Arg1) + (6));
    Arg1 = (uint16_t)((Arg1) << (3));
    v_stack_p128 = (uint16_t)(Arg1);
    v_stack_p12A = (uint16_t)(v_stack_p78);
    result = (v_stack_p50) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p140 = result;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p50))) & (0xFFFULL));
    v_stack_p14C = (uint32_t)(Arg2);
    v_stack_p148 = (uint32_t)(local_r15);
    goto loc_009BBE56;
loc_009BC3FC:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p48, Arg2, Arg4 + 1, Arg4);
    goto loc_009BC29A;
loc_009BC40D:
    if ((uint32_t)(v_stack_p78) == 0) goto loc_009BC2DD;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFEULL));
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF0, Arg2, Arg4 + 1, Arg4);
    local_rsi = 0;
    goto loc_009BBCA9;
loc_009BC438:
    result = MiVadRangeIsIoSpace(v_stack_pF0, v_stack_p50, local_r15, Arg4);
    goto loc_009BC0FD;
loc_009BC450:
    goto loc_009BBE4A;
loc_009BC458:
    result = MiVadRangeIsIoSpace(v_stack_pF0, v_stack_p50, result, Arg4);
    if (result != 0) goto loc_009BBDD3;
    v_stack_p30 = 0xC0000005ULL;
    goto loc_009BBDD3;
loc_009BC47E:
    local_rdi = v_stack_pA0;
    if (v_stack_pA0 > ((uint32_t)(0x10000ULL))) { local_rdi = (uint32_t)(0x10000ULL); }
loc_009BC492:
    result = MiAllocatePool(256, local_rdi, (uint32_t)(0x77526D4DULL), Arg4);
    v_stack_p48 = result;
    if (result == 0) goto loc_009BC4BC;
    v_stack_p90 = local_rdi;
    goto loc_009BBE4A;
loc_009BC4BC:
    local_rdi = (local_rdi) >> (1);
    if (local_rdi > 512) goto loc_009BC492;
    v_stack_p48 = v_stack_p1D0;
    goto loc_009BBE4A;
loc_009BC4DF:
    if (v_stack_p1D0 == 0) goto loc_009BBD54;
loc_009BC4E8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p60 + 0x5FC)))) & (1)) != 0) goto loc_009BBD54;
    local_rdi = 0;
    v_stack_p30 = 0;
    local_rbx = (uint32_t)((local_rbx) | (32));
    goto loc_009BBD97;
loc_009BC510:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p60 + 0x5FC)))) & (1)) != 0) goto loc_009BC07D;
    v_stack_p30 = 0;
    local_rbx = (uint32_t)((local_rbx) | (32));
    v_stack_p38 = (uint32_t)(local_rbx);
    Arg1 = (256) + (0x1000ULL);
    goto loc_009BC0C4;
loc_009BC53A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x40)))) & (4)) == 0) goto loc_009BBDD3;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x40))) & (1));
    result = (uint8_t)(-(result));
    local_r14 = (uint32_t)((v_stack_p50) + (2));
    goto loc_009BBDD3;
loc_009BC555:
    if (result == 0) goto loc_009BC07D;
    goto loc_009BC510;
loc_009BC560:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x40)))) & (4)) == 0) goto loc_009BC0FD;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x40))) & (1));
    result = (uint8_t)(-(result));
    local_rsi = (uint32_t)((local_rsi) + (2));
    goto loc_009BC0FD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x170` | `8` | `R` |
| `Arg3` | `+ 0x170` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009BBB50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
