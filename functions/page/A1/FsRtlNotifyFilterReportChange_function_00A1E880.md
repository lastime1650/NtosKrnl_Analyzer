# FsRtlNotifyFilterReportChange

- RVA: `0x00A1E880`–`0x00A1F2A5` (길이 `2,597` bytes)
- VA: `0x0000000140A1E880`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AAAB4`
- 디코드: `574`개 명령, `2,597/2,597` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A1E932` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x00A1EAA2` → [RtlMultiByteToUnicodeSize](../90/RtlMultiByteToUnicodeSize_function_0090CBC0.md) (function, `0x0090CBC0`)
- `0x00A1EB41` → [PsChargePoolQuota](../../text/3E/PsChargePoolQuota_function_003EC7F0.md) (function, `0x003EC7F0`)
- `0x00A1EB59` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A1EB94` → [PsReturnProcessPagedPoolQuota](../../text/2A/PsReturnProcessPagedPoolQuota_function_002A6860.md) (function, `0x002A6860`)
- `0x00A1EC6A` → [FsRtlNotifyCompleteIrpList](FsRtlNotifyCompleteIrpList_function_00A1F98C.md) (function, `0x00A1F98C`)
- `0x00A1ED5A` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00A1EE02` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A1EE28` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A1F085` → [RtlMultiByteToUnicodeSize](../90/RtlMultiByteToUnicodeSize_function_0090CBC0.md) (function, `0x0090CBC0`)
- `0x00A1F109` → [RtlMultiByteToUnicodeSize](../90/RtlMultiByteToUnicodeSize_function_0090CBC0.md) (function, `0x0090CBC0`)
- `0x00A1F194` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x00A1F1CD` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A1F209` → [FsRtlNotifyUpdateBuffer](../A8/FsRtlNotifyUpdateBuffer_function_00A892A4.md) (function, `0x00A892A4`)
- `0x00A1F239` → [PsReturnProcessPagedPoolQuota](../../text/2A/PsReturnProcessPagedPoolQuota_function_002A6860.md) (function, `0x002A6860`)
- `0x00A1F244` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A1F29E` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)

### Direct callers
- [FsRtlNotifyReportChange](../71/FsRtlNotifyReportChange_function_00716E90.md) at `0x00716EC5`
- [FsRtlNotifyFullReportChange](FsRtlNotifyFullReportChange_function_00A1E820.md) at `0x00A1E866`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00A1E932` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (`PAGE` → `.text`)
  - `0x00A1EB41` → [PsChargePoolQuota](../../text/3E/PsChargePoolQuota_function_003EC7F0.md) (`PAGE` → `.text`)
  - `0x00A1EB59` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A1EB94` → [PsReturnProcessPagedPoolQuota](../../text/2A/PsReturnProcessPagedPoolQuota_function_002A6860.md) (`PAGE` → `.text`)
  - `0x00A1ED5A` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00A1EE02` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A1EE28` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A1F194` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (`PAGE` → `.text`)
  - `0x00A1F1CD` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A1F239` → [PsReturnProcessPagedPoolQuota](../../text/2A/PsReturnProcessPagedPoolQuota_function_002A6860.md) (`PAGE` → `.text`)
  - `0x00A1F244` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A1F29E` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A1E880  4C 8B DC                        mov r11, rsp
00A1E883  66 45 89 4B 20                  mov word ptr [r11 + 0x20], r9w
00A1E888  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
00A1E88C  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
00A1E890  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
00A1E894  53                              push rbx
00A1E895  56                              push rsi
00A1E896  57                              push rdi
00A1E897  41 54                           push r12
00A1E899  41 55                           push r13
00A1E89B  41 56                           push r14
00A1E89D  41 57                           push r15
00A1E89F  48 81 EC 20 01 00 00            sub rsp, 0x120
00A1E8A6  45 0F B7 F1                     movzx r14d, r9w
00A1E8AA  4D 8B F8                        mov r15, r8
00A1E8AD  4C 8B C2                        mov r8, rdx
00A1E8B0  48 8B F1                        mov rsi, rcx
00A1E8B3  4C 89 BC 24 00 01 00 00         mov qword ptr [rsp + 0x100], r15
00A1E8BB  41 0F B7 D1                     movzx edx, r9w
00A1E8BF  66 89 54 24 4E                  mov word ptr [rsp + 0x4e], dx
00A1E8C4  48 8B 84 24 80 01 00 00         mov rax, qword ptr [rsp + 0x180]
00A1E8CC  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
00A1E8D4  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
00A1E8DC  0F 57 C0                        xorps xmm0, xmm0
00A1E8DF  41 0F 11 43 90                  movups xmmword ptr [r11 - 0x70], xmm0
00A1E8E4  33 FF                           xor edi, edi
00A1E8E6  49 89 BB 40 FF FF FF            mov qword ptr [r11 - 0xc0], rdi
00A1E8ED  49 89 BB 50 FF FF FF            mov qword ptr [r11 - 0xb0], rdi
00A1E8F4  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00A1E8F9  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00A1E8FE  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
00A1E902  89 BC 24 94 00 00 00            mov dword ptr [rsp + 0x94], edi
00A1E909  66 45 85 C9                     test r9w, r9w
00A1E90D  0F 84 7A 09 00 00               je 0x140a1f28d
00A1E913  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
00A1E91B  48 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdi
00A1E923  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
00A1E92C  48 3B 59 38                     cmp rbx, qword ptr [rcx + 0x38]
00A1E930  74 15                           je 0x140a1e947
00A1E932  E8 E9 4D 9D FF                  call 0x1403f3720
00A1E937  48 89 5E 38                     mov qword ptr [rsi + 0x38], rbx
00A1E93B  41 0F B7 D6                     movzx edx, r14w
00A1E93F  4C 8B 84 24 68 01 00 00         mov r8, qword ptr [rsp + 0x168]
00A1E947  FF 46 40                        inc dword ptr [rsi + 0x40]
00A1E94A  4D 8B 20                        mov r12, qword ptr [r8]
00A1E94D  41 BD 02 00 00 00               mov r13d, 2
00A1E953  0F B7 84 24 98 00 00 00         movzx eax, word ptr [rsp + 0x98]
00A1E95B  66 89 44 24 44                  mov word ptr [rsp + 0x44], ax
00A1E960  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00A1E968  48 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rcx
00A1E970  0F B7 84 24 A8 00 00 00         movzx eax, word ptr [rsp + 0xa8]
00A1E978  66 89 44 24 4C                  mov word ptr [rsp + 0x4c], ax
00A1E97D  0F B7 44 24 78                  movzx eax, word ptr [rsp + 0x78]
00A1E982  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00A1E986  4C 89 A4 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r12
00A1E98E  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
00A1E993  4D 3B E0                        cmp r12, r8
00A1E996  0F 84 CF 08 00 00               je 0x140a1f26b
00A1E99C  49 8D 74 24 E0                  lea rsi, [r12 - 0x20]
00A1E9A1  48 89 B4 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rsi
00A1E9A9  48 8B CE                        mov rcx, rsi
00A1E9AC  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
00A1E9B4  4D 85 FF                        test r15, r15
00A1E9B7  74 27                           je 0x140a1e9e0
00A1E9B9  48 8B 86 88 00 00 00            mov rax, qword ptr [rsi + 0x88]
00A1E9C0  66 39 38                        cmp word ptr [rax], di
00A1E9C3  74 10                           je 0x140a1e9d5
00A1E9C5  8B 46 4C                        mov eax, dword ptr [rsi + 0x4c]
00A1E9C8  85 84 24 90 01 00 00            test dword ptr [rsp + 0x190], eax
00A1E9CF  0F 85 13 03 00 00               jne 0x140a1ece8
00A1E9D5  4D 8B 24 24                     mov r12, qword ptr [r12]
00A1E9D9  0F B7 54 24 4E                  movzx edx, word ptr [rsp + 0x4e]
00A1E9DE  EB A6                           jmp 0x140a1e986
00A1E9E0  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
00A1E9E8  48 3B 46 18                     cmp rax, qword ptr [rsi + 0x18]
00A1E9EC  75 E7                           jne 0x140a1e9d5
00A1E9EE  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
00A1E9F6  8B C7                           mov eax, edi
00A1E9F8  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00A1E9FC  66 89 44 24 78                  mov word ptr [rsp + 0x78], ax
00A1EA01  41 B3 01                        mov r11b, 1
00A1EA04  44 88 5C 24 40                  mov byte ptr [rsp + 0x40], r11b
00A1EA09  40 8A DF                        mov bl, dil
00A1EA0C  88 5C 24 41                     mov byte ptr [rsp + 0x41], bl
00A1EA10  0F B7 56 48                     movzx edx, word ptr [rsi + 0x48]
00A1EA14  41 84 D5                        test r13b, dl
00A1EA17  0F 85 19 02 00 00               jne 0x140a1ec36
00A1EA1D  44 8B 66 60                     mov r12d, dword ptr [rsi + 0x60]
00A1EA21  45 85 E4                        test r12d, r12d
00A1EA24  0F 84 07 02 00 00               je 0x140a1ec31
00A1EA2A  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
00A1EA2E  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
00A1EA32  4C 8B EF                        mov r13, rdi
00A1EA35  48 89 BC 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdi
00A1EA3D  8B 46 64                        mov eax, dword ptr [rsi + 0x64]
00A1EA40  85 C0                           test eax, eax
00A1EA42  0F 84 EE 03 00 00               je 0x140a1ee36
00A1EA48  44 8B E0                        mov r12d, eax
00A1EA4B  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
00A1EA50  84 DB                           test bl, bl
00A1EA52  0F 84 0D 04 00 00               je 0x140a1ee65
00A1EA58  0F B7 C7                        movzx eax, di
00A1EA5B  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00A1EA5F  66 89 44 24 78                  mov word ptr [rsp + 0x78], ax
00A1EA64  41 BE 0C 00 00 00               mov r14d, 0xc
00A1EA6A  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A1EA6F  45 84 DB                        test r11b, r11b
00A1EA72  0F 84 04 02 00 00               je 0x140a1ec7c
00A1EA78  48 8B 84 24 80 01 00 00         mov rax, qword ptr [rsp + 0x180]
00A1EA80  44 0F B7 30                     movzx r14d, word ptr [rax]
00A1EA84  41 83 C6 0C                     add r14d, 0xc
00A1EA88  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A1EA8D  EB 36                           jmp 0x140a1eac5
00A1EA8F  89 BC 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], edi
00A1EA96  44 0F B7 C1                     movzx r8d, cx
00A1EA9A  48 8D 8C 24 8C 00 00 00         lea rcx, [rsp + 0x8c]
00A1EAA2  E8 19 E1 EE FF                  call 0x14090cbc0
00A1EAA7  44 03 B4 24 8C 00 00 00         add r14d, dword ptr [rsp + 0x8c]
00A1EAAF  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A1EAB4  48 8B 8C 24 80 01 00 00         mov rcx, qword ptr [rsp + 0x180]
00A1EABC  48 85 C9                        test rcx, rcx
00A1EABF  0F 85 11 06 00 00               jne 0x140a1f0d6
00A1EAC5  44 8B 7E 68                     mov r15d, dword ptr [rsi + 0x68]
00A1EAC9  41 83 C7 03                     add r15d, 3
00A1EACD  41 83 E7 FC                     and r15d, 0xfffffffc
00A1EAD1  44 89 BC 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r15d
00A1EAD9  43 8D 0C 37                     lea ecx, [r15 + r14]
00A1EADD  83 C8 FF                        or eax, 0xffffffff
00A1EAE0  41 3B CF                        cmp ecx, r15d
00A1EAE3  0F 43 C1                        cmovae eax, ecx
00A1EAE6  89 84 24 14 01 00 00            mov dword ptr [rsp + 0x114], eax
00A1EAED  45 3B F4                        cmp r14d, r12d
00A1EAF0  0F 87 DB 01 00 00               ja 0x140a1ecd1
00A1EAF6  41 3B CF                        cmp ecx, r15d
00A1EAF9  0F 82 D2 01 00 00               jb 0x140a1ecd1
00A1EAFF  41 3B C4                        cmp eax, r12d
00A1EB02  0F 87 C9 01 00 00               ja 0x140a1ecd1
00A1EB08  48 8B DF                        mov rbx, rdi
00A1EB0B  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
00A1EB10  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
00A1EB14  48 85 C0                        test rax, rax
00A1EB17  0F 85 05 06 00 00               jne 0x140a1f122
00A1EB1D  4D 85 ED                        test r13, r13
00A1EB20  0F 85 24 06 00 00               jne 0x140a1f14a
00A1EB26  48 39 7E 58                     cmp qword ptr [rsi + 0x58], rdi
00A1EB2A  0F 85 7E 06 00 00               jne 0x140a1f1ae
00A1EB30  40 88 7C 24 43                  mov byte ptr [rsp + 0x43], dil
00A1EB35  45 8B C4                        mov r8d, r12d
00A1EB38  BA 01 00 00 00                  mov edx, 1
00A1EB3D  48 8B 4E 78                     mov rcx, qword ptr [rsi + 0x78]
00A1EB41  E8 AA DC 9C FF                  call 0x1403ec7f0
00A1EB46  C6 44 24 43 01                  mov byte ptr [rsp + 0x43], 1
00A1EB4B  41 B8 46 53 72 4E               mov r8d, 0x4e725346
00A1EB51  41 8B D4                        mov edx, r12d
00A1EB54  B9 22 01 00 00                  mov ecx, 0x122
00A1EB59  E8 92 35 16 00                  call 0x140b820f0
00A1EB5E  48 8B D8                        mov rbx, rax
00A1EB61  48 89 46 58                     mov qword ptr [rsi + 0x58], rax
00A1EB65  48 89 46 50                     mov qword ptr [rsi + 0x50], rax
00A1EB69  44 89 66 64                     mov dword ptr [rsi + 0x64], r12d
00A1EB6D  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A1EB72  41 BD 02 00 00 00               mov r13d, 2
00A1EB78  E9 90 00 00 00                  jmp 0x140a1ec0d
00A1EB7D  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00A1EB85  80 7C 24 43 00                  cmp byte ptr [rsp + 0x43], 0
00A1EB8A  74 0D                           je 0x140a1eb99
00A1EB8C  8B 54 24 58                     mov edx, dword ptr [rsp + 0x58]
00A1EB90  48 8B 4E 78                     mov rcx, qword ptr [rsi + 0x78]
00A1EB94  E8 C7 7C 88 FF                  call 0x1402a6860
00A1EB99  0F B7 46 48                     movzx eax, word ptr [rsi + 0x48]
00A1EB9D  66 83 C8 02                     or ax, 2
00A1EBA1  66 89 46 48                     mov word ptr [rsi + 0x48], ax
00A1EBA5  33 FF                           xor edi, edi
00A1EBA7  44 8D 6F 02                     lea r13d, [rdi + 2]
00A1EBAB  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00A1EBB3  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00A1EBB8  0F B7 84 24 98 00 00 00         movzx eax, word ptr [rsp + 0x98]
00A1EBC0  66 89 44 24 44                  mov word ptr [rsp + 0x44], ax
00A1EBC5  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00A1EBCD  48 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rcx
00A1EBD5  0F B7 84 24 A8 00 00 00         movzx eax, word ptr [rsp + 0xa8]
00A1EBDD  66 89 44 24 4C                  mov word ptr [rsp + 0x4c], ax
00A1EBE2  0F B7 44 24 78                  movzx eax, word ptr [rsp + 0x78]
00A1EBE7  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00A1EBEB  44 8B 74 24 48                  mov r14d, dword ptr [rsp + 0x48]
00A1EBF0  44 8B BC 24 C0 00 00 00         mov r15d, dword ptr [rsp + 0xc0]
00A1EBF8  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
00A1EBFD  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
00A1EC05  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
00A1EC0D  48 85 DB                        test rbx, rbx
00A1EC10  0F 85 A3 05 00 00               jne 0x140a1f1b9
00A1EC16  44 84 6E 48                     test byte ptr [rsi + 0x48], r13b
00A1EC1A  0F 85 02 06 00 00               jne 0x140a1f222
00A1EC20  44 0F B7 B4 24 78 01 00 00      movzx r14d, word ptr [rsp + 0x178]
00A1EC29  4C 8B BC 24 70 01 00 00         mov r15, qword ptr [rsp + 0x170]
00A1EC31  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00A1EC36  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00A1EC3E  0F B7 41 48                     movzx eax, word ptr [rcx + 0x48]
00A1EC42  83 BC 24 98 01 00 00 04         cmp dword ptr [rsp + 0x198], 4
00A1EC4A  0F 84 0E 06 00 00               je 0x140a1f25e
00A1EC50  BA F7 FF 00 00                  mov edx, 0xfff7
00A1EC55  66 23 C2                        and ax, dx
00A1EC58  66 89 41 48                     mov word ptr [rcx + 0x48], ax
00A1EC5C  48 8D 46 30                     lea rax, [rsi + 0x30]
00A1EC60  48 39 00                        cmp qword ptr [rax], rax
00A1EC63  74 0A                           je 0x140a1ec6f
00A1EC65  33 D2                           xor edx, edx
00A1EC67  48 8B CE                        mov rcx, rsi
00A1EC6A  E8 1D 0D 00 00                  call 0x140a1f98c
00A1EC6F  4C 8B 84 24 68 01 00 00         mov r8, qword ptr [rsp + 0x168]
00A1EC77  E9 59 FD FF FF                  jmp 0x140a1e9d5
00A1EC7C  84 DB                           test bl, bl
00A1EC7E  75 23                           jne 0x140a1eca3
00A1EC80  80 BE 90 00 00 00 01            cmp byte ptr [rsi + 0x90], 1
00A1EC87  0F 84 DD 03 00 00               je 0x140a1f06a
00A1EC8D  44 0F B7 F0                     movzx r14d, ax
00A1EC91  41 83 C6 0C                     add r14d, 0xc
00A1EC95  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A1EC9A  41 83 C6 02                     add r14d, 2
00A1EC9E  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A1ECA3  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
00A1ECAB  48 85 D2                        test rdx, rdx
00A1ECAE  0F 84 E3 03 00 00               je 0x140a1f097
00A1ECB4  0F B7 4C 24 4C                  movzx ecx, word ptr [rsp + 0x4c]
00A1ECB9  80 BE 90 00 00 00 01            cmp byte ptr [rsi + 0x90], 1
00A1ECC0  0F 84 C9 FD FF FF               je 0x140a1ea8f
00A1ECC6  0F B7 C1                        movzx eax, cx
00A1ECC9  44 03 F0                        add r14d, eax
00A1ECCC  E9 DE FD FF FF                  jmp 0x140a1eaaf
00A1ECD1  41 BD 02 00 00 00               mov r13d, 2
00A1ECD7  0F B7 46 48                     movzx eax, word ptr [rsi + 0x48]
00A1ECDB  66 41 0B C5                     or ax, r13w
00A1ECDF  66 89 46 48                     mov word ptr [rsi + 0x48], ax
00A1ECE3  E9 2E FF FF FF                  jmp 0x140a1ec16
00A1ECE8  4C 8B 94 24 88 01 00 00         mov r10, qword ptr [rsp + 0x188]
00A1ECF0  4D 85 D2                        test r10, r10
00A1ECF3  0F 84 85 00 00 00               je 0x140a1ed7e
00A1ECF9  4C 8B 8E 88 00 00 00            mov r9, qword ptr [rsi + 0x88]
00A1ED00  41 0F B7 11                     movzx edx, word ptr [r9]
00A1ED04  66 41 3B 12                     cmp dx, word ptr [r10]
00A1ED08  0F 87 C7 FC FF FF               ja 0x140a1e9d5
00A1ED0E  0F 84 BC 00 00 00               je 0x140a1edd0
00A1ED14  0F B7 46 48                     movzx eax, word ptr [rsi + 0x48]
00A1ED18  A8 01                           test al, 1
00A1ED1A  0F 84 B5 FC FF FF               je 0x140a1e9d5
00A1ED20  A8 10                           test al, 0x10
00A1ED22  75 24                           jne 0x140a1ed48
00A1ED24  48 8B 81 88 00 00 00            mov rax, qword ptr [rcx + 0x88]
00A1ED2B  0F B7 08                        movzx ecx, word ptr [rax]
00A1ED2E  49 03 4A 08                     add rcx, qword ptr [r10 + 8]
00A1ED32  80 BE 90 00 00 00 01            cmp byte ptr [rsi + 0x90], 1
00A1ED39  0F 85 98 00 00 00               jne 0x140a1edd7
00A1ED3F  80 39 5C                        cmp byte ptr [rcx], 0x5c
00A1ED42  0F 85 8D FC FF FF               jne 0x140a1e9d5
00A1ED48  40 8A DF                        mov bl, dil
00A1ED4B  88 5C 24 41                     mov byte ptr [rsp + 0x41], bl
00A1ED4F  4C 8B C2                        mov r8, rdx
00A1ED52  49 8B 52 08                     mov rdx, qword ptr [r10 + 8]
00A1ED56  49 8B 49 08                     mov rcx, qword ptr [r9 + 8]
00A1ED5A  E8 B1 7D CA FF                  call 0x1406c6b10
00A1ED5F  85 C0                           test eax, eax
00A1ED61  75 7D                           jne 0x140a1ede0
00A1ED63  84 DB                           test bl, bl
00A1ED65  74 7E                           je 0x140a1ede5
00A1ED67  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
00A1ED6B  48 85 C0                        test rax, rax
00A1ED6E  0F 85 9C 00 00 00               jne 0x140a1ee10
00A1ED74  44 8A 5C 24 40                  mov r11b, byte ptr [rsp + 0x40]
00A1ED79  E9 92 FC FF FF                  jmp 0x140a1ea10
00A1ED7E  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00A1ED82  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00A1ED8A  41 0F B7 CE                     movzx ecx, r14w
00A1ED8E  66 89 8C 24 E8 00 00 00         mov word ptr [rsp + 0xe8], cx
00A1ED96  0F B6 86 90 00 00 00            movzx eax, byte ptr [rsi + 0x90]
00A1ED9D  66 3B D0                        cmp dx, ax
00A1EDA0  74 0E                           je 0x140a1edb0
00A1EDA2  0F B7 CA                        movzx ecx, dx
00A1EDA5  66 2B C8                        sub cx, ax
00A1EDA8  66 89 8C 24 E8 00 00 00         mov word ptr [rsp + 0xe8], cx
00A1EDB0  66 89 8C 24 EA 00 00 00         mov word ptr [rsp + 0xea], cx
00A1EDB8  4C 8D 94 24 E8 00 00 00         lea r10, [rsp + 0xe8]
00A1EDC0  4C 89 94 24 88 01 00 00         mov qword ptr [rsp + 0x188], r10
00A1EDC8  48 8B CE                        mov rcx, rsi
00A1EDCB  E9 29 FF FF FF                  jmp 0x140a1ecf9
00A1EDD0  B3 01                           mov bl, 1
00A1EDD2  E9 74 FF FF FF                  jmp 0x140a1ed4b
00A1EDD7  66 83 39 5C                     cmp word ptr [rcx], 0x5c
00A1EDDB  E9 62 FF FF FF                  jmp 0x140a1ed42
00A1EDE0  E9 8A FE FF FF                  jmp 0x140a1ec6f
00A1EDE5  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00A1EDE9  48 85 C0                        test rax, rax
00A1EDEC  0F 84 75 FF FF FF               je 0x140a1ed67
00A1EDF2  4C 8B 46 18                     mov r8, qword ptr [rsi + 0x18]
00A1EDF6  48 8B 94 24 A0 01 00 00         mov rdx, qword ptr [rsp + 0x1a0]
00A1EDFE  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00A1EE02  E8 C9 BC C9 FF                  call 0x1406baad0
00A1EE07  84 C0                           test al, al
00A1EE09  74 D5                           je 0x140a1ede0
00A1EE0B  E9 57 FF FF FF                  jmp 0x140a1ed67
00A1EE10  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
00A1EE18  48 85 C9                        test rcx, rcx
00A1EE1B  0F 84 53 FF FF FF               je 0x140a1ed74
00A1EE21  48 8B D1                        mov rdx, rcx
00A1EE24  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00A1EE28  E8 A3 BC C9 FF                  call 0x1406baad0
00A1EE2D  84 C0                           test al, al
00A1EE2F  74 AF                           je 0x140a1ede0
00A1EE31  E9 3E FF FF FF                  jmp 0x140a1ed74
00A1EE36  48 8D 46 30                     lea rax, [rsi + 0x30]
00A1EE3A  48 8B 08                        mov rcx, qword ptr [rax]
00A1EE3D  48 3B C8                        cmp rcx, rax
00A1EE40  0F 84 05 FC FF FF               je 0x140a1ea4b
00A1EE46  4C 8D A9 58 FF FF FF            lea r13, [rcx - 0xa8]
00A1EE4D  4C 89 AC 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r13
00A1EE55  49 8B 85 B8 00 00 00            mov rax, qword ptr [r13 + 0xb8]
00A1EE5C  44 8B 60 08                     mov r12d, dword ptr [rax + 8]
00A1EE60  E9 E6 FB FF FF                  jmp 0x140a1ea4b
00A1EE65  45 84 DB                        test r11b, r11b
00A1EE68  0F 85 F3 01 00 00               jne 0x140a1f061
00A1EE6E  66 83 E2 10                     and dx, 0x10
00A1EE72  75 48                           jne 0x140a1eebc
00A1EE74  49 8D 47 08                     lea rax, [r15 + 8]
00A1EE78  4C 8B 94 24 88 01 00 00         mov r10, qword ptr [rsp + 0x188]
00A1EE80  4D 8B 4A 08                     mov r9, qword ptr [r10 + 8]
00A1EE84  4C 3B 08                        cmp r9, qword ptr [rax]
00A1EE87  75 3F                           jne 0x140a1eec8
00A1EE89  48 8B 86 88 00 00 00            mov rax, qword ptr [rsi + 0x88]
00A1EE90  44 0F B7 00                     movzx r8d, word ptr [rax]
00A1EE94  0F B6 96 90 00 00 00            movzx edx, byte ptr [rsi + 0x90]
00A1EE9B  42 8D 04 02                     lea eax, [rdx + r8]
00A1EE9F  8B C8                           mov ecx, eax
00A1EEA1  49 03 C9                        add rcx, r9
00A1EEA4  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
00A1EEAC  41 0F B7 02                     movzx eax, word ptr [r10]
00A1EEB0  66 2B C2                        sub ax, dx
00A1EEB3  66 41 2B C0                     sub ax, r8w
00A1EEB7  E9 88 01 00 00                  jmp 0x140a1f044
00A1EEBC  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
00A1EEC4  48 83 C0 08                     add rax, 8
00A1EEC8  48 83 BC 24 A0 00 00 00 00      cmp qword ptr [rsp + 0xa0], 0
00A1EED1  75 4D                           jne 0x140a1ef20
00A1EED3  48 8B 00                        mov rax, qword ptr [rax]
00A1EED6  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00A1EEDE  66 44 89 74 24 44               mov word ptr [rsp + 0x44], r14w
00A1EEE4  66 44 89 B4 24 98 00 00 00      mov word ptr [rsp + 0x98], r14w
00A1EEED  0F B6 86 90 00 00 00            movzx eax, byte ptr [rsi + 0x90]
00A1EEF4  0F B7 4C 24 4E                  movzx ecx, word ptr [rsp + 0x4e]
00A1EEF9  66 3B C8                        cmp cx, ax
00A1EEFC  74 17                           je 0x140a1ef15
00A1EEFE  44 0F B7 F1                     movzx r14d, cx
00A1EF02  66 44 2B F0                     sub r14w, ax
00A1EF06  66 44 89 74 24 44               mov word ptr [rsp + 0x44], r14w
00A1EF0C  66 44 89 B4 24 98 00 00 00      mov word ptr [rsp + 0x98], r14w
00A1EF15  66 44 89 B4 24 9A 00 00 00      mov word ptr [rsp + 0x9a], r14w
00A1EF1E  EB 06                           jmp 0x140a1ef26
00A1EF20  44 0F B7 74 24 44               movzx r14d, word ptr [rsp + 0x44]
00A1EF26  44 8A D7                        mov r10b, dil
00A1EF29  40 88 7C 24 42                  mov byte ptr [rsp + 0x42], dil
00A1EF2E  44 8B C7                        mov r8d, edi
00A1EF31  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
00A1EF35  66 85 D2                        test dx, dx
00A1EF38  0F 85 DF 00 00 00               jne 0x140a1f01d
00A1EF3E  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
00A1EF42  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
00A1EF46  41 B9 01 00 00 00               mov r9d, 1
00A1EF4C  44 89 4C 24 5C                  mov dword ptr [rsp + 0x5c], r9d
00A1EF51  8B D7                           mov edx, edi
00A1EF53  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
00A1EF57  44 38 8E 90 00 00 00            cmp byte ptr [rsi + 0x90], r9b
00A1EF5E  75 57                           jne 0x140a1efb7
00A1EF60  4C 8B 9E 88 00 00 00            mov r11, qword ptr [rsi + 0x88]
00A1EF67  41 0F B7 03                     movzx eax, word ptr [r11]
00A1EF6B  3B D0                           cmp edx, eax
00A1EF6D  73 1C                           jae 0x140a1ef8b
00A1EF6F  8B CA                           mov ecx, edx
00A1EF71  49 8B 43 08                     mov rax, qword ptr [r11 + 8]
00A1EF75  80 3C 01 5C                     cmp byte ptr [rcx + rax], 0x5c
00A1EF79  75 08                           jne 0x140a1ef83
00A1EF7B  41 FF C1                        inc r9d
00A1EF7E  44 89 4C 24 5C                  mov dword ptr [rsp + 0x5c], r9d
00A1EF83  FF C2                           inc edx
00A1EF85  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
00A1EF89  EB D5                           jmp 0x140a1ef60
00A1EF8B  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00A1EF93  41 8B C0                        mov eax, r8d
00A1EF96  80 3C 08 5C                     cmp byte ptr [rax + rcx], 0x5c
00A1EF9A  75 11                           jne 0x140a1efad
00A1EF9C  41 FE C2                        inc r10b
00A1EF9F  44 88 54 24 42                  mov byte ptr [rsp + 0x42], r10b
00A1EFA4  41 0F B6 C2                     movzx eax, r10b
00A1EFA8  41 3B C1                        cmp eax, r9d
00A1EFAB  74 6B                           je 0x140a1f018
00A1EFAD  41 FF C0                        inc r8d
00A1EFB0  44 89 44 24 54                  mov dword ptr [rsp + 0x54], r8d
00A1EFB5  EB DC                           jmp 0x140a1ef93
00A1EFB7  4C 8B 9E 88 00 00 00            mov r11, qword ptr [rsi + 0x88]
00A1EFBE  41 0F B7 03                     movzx eax, word ptr [r11]
00A1EFC2  D1 E8                           shr eax, 1
00A1EFC4  3B D0                           cmp edx, eax
00A1EFC6  73 1D                           jae 0x140a1efe5
00A1EFC8  8B CA                           mov ecx, edx
00A1EFCA  49 8B 43 08                     mov rax, qword ptr [r11 + 8]
00A1EFCE  66 83 3C 48 5C                  cmp word ptr [rax + rcx*2], 0x5c
00A1EFD3  75 08                           jne 0x140a1efdd
00A1EFD5  41 FF C1                        inc r9d
00A1EFD8  44 89 4C 24 5C                  mov dword ptr [rsp + 0x5c], r9d
00A1EFDD  FF C2                           inc edx
00A1EFDF  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
00A1EFE3  EB D2                           jmp 0x140a1efb7
00A1EFE5  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00A1EFED  41 8B C0                        mov eax, r8d
00A1EFF0  66 83 3C 41 5C                  cmp word ptr [rcx + rax*2], 0x5c
00A1EFF5  75 60                           jne 0x140a1f057
00A1EFF7  41 FE C2                        inc r10b
00A1EFFA  44 88 54 24 42                  mov byte ptr [rsp + 0x42], r10b
00A1EFFF  41 0F B6 C2                     movzx eax, r10b
00A1F003  41 3B C1                        cmp eax, r9d
00A1F006  75 4F                           jne 0x140a1f057
00A1F008  0F B6 86 90 00 00 00            movzx eax, byte ptr [rsi + 0x90]
00A1F00F  44 0F AF C0                     imul r8d, eax
00A1F013  44 89 44 24 54                  mov dword ptr [rsp + 0x54], r8d
00A1F018  44 8A 5C 24 40                  mov r11b, byte ptr [rsp + 0x40]
00A1F01D  0F B6 8E 90 00 00 00            movzx ecx, byte ptr [rsi + 0x90]
00A1F024  41 03 C8                        add ecx, r8d
00A1F027  8B C1                           mov eax, ecx
00A1F029  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
00A1F02D  48 03 84 24 A0 00 00 00         add rax, qword ptr [rsp + 0xa0]
00A1F035  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00A1F03D  41 0F B7 C6                     movzx eax, r14w
00A1F041  66 2B C1                        sub ax, cx
00A1F044  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00A1F048  66 89 44 24 78                  mov word ptr [rsp + 0x78], ax
00A1F04D  66 89 44 24 7A                  mov word ptr [rsp + 0x7a], ax
00A1F052  E9 0D FA FF FF                  jmp 0x140a1ea64
00A1F057  41 FF C0                        inc r8d
00A1F05A  44 89 44 24 54                  mov dword ptr [rsp + 0x54], r8d
00A1F05F  EB 8C                           jmp 0x140a1efed
00A1F061  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00A1F065  E9 FA F9 FF FF                  jmp 0x140a1ea64
00A1F06A  89 BC 24 88 00 00 00            mov dword ptr [rsp + 0x88], edi
00A1F071  44 0F B7 C0                     movzx r8d, ax
00A1F075  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
00A1F07D  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
00A1F085  E8 36 DB EE FF                  call 0x14090cbc0
00A1F08A  44 8B B4 24 88 00 00 00         mov r14d, dword ptr [rsp + 0x88]
00A1F092  E9 FA FB FF FF                  jmp 0x140a1ec91
00A1F097  0F B7 84 24 78 01 00 00         movzx eax, word ptr [rsp + 0x178]
00A1F09F  8B D0                           mov edx, eax
00A1F0A1  49 03 57 08                     add rdx, qword ptr [r15 + 8]
00A1F0A5  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
00A1F0AD  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
00A1F0B5  41 0F B7 0F                     movzx ecx, word ptr [r15]
00A1F0B9  66 2B C8                        sub cx, ax
00A1F0BC  66 89 4C 24 4C                  mov word ptr [rsp + 0x4c], cx
00A1F0C1  66 89 8C 24 A8 00 00 00         mov word ptr [rsp + 0xa8], cx
00A1F0C9  66 89 8C 24 AA 00 00 00         mov word ptr [rsp + 0xaa], cx
00A1F0D1  E9 E3 FB FF FF                  jmp 0x140a1ecb9
00A1F0D6  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00A1F0DE  0F B7 00                        movzx eax, word ptr [rax]
00A1F0E1  41 8B DE                        mov ebx, r14d
00A1F0E4  80 BE 90 00 00 00 02            cmp byte ptr [rsi + 0x90], 2
00A1F0EB  75 06                           jne 0x140a1f0f3
00A1F0ED  44 8D 70 02                     lea r14d, [rax + 2]
00A1F0F1  EB 27                           jmp 0x140a1f11a
00A1F0F3  89 BC 24 90 00 00 00            mov dword ptr [rsp + 0x90], edi
00A1F0FA  44 8B C0                        mov r8d, eax
00A1F0FD  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00A1F101  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
00A1F109  E8 B2 DA EE FF                  call 0x14090cbc0
00A1F10E  44 8B B4 24 90 00 00 00         mov r14d, dword ptr [rsp + 0x90]
00A1F116  41 83 C6 02                     add r14d, 2
00A1F11A  44 03 F3                        add r14d, ebx
00A1F11D  E9 66 F9 FF FF                  jmp 0x140a1ea88
00A1F122  8B 4E 6C                        mov ecx, dword ptr [rsi + 0x6c]
00A1F125  48 8D 14 08                     lea rdx, [rax + rcx]
00A1F129  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00A1F12E  41 8B C7                        mov eax, r15d
00A1F131  2B C1                           sub eax, ecx
00A1F133  89 02                           mov dword ptr [rdx], eax
00A1F135  44 89 7E 6C                     mov dword ptr [rsi + 0x6c], r15d
00A1F139  41 8B DF                        mov ebx, r15d
00A1F13C  48 03 5E 58                     add rbx, qword ptr [rsi + 0x58]
00A1F140  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
00A1F145  E9 DC F9 FF FF                  jmp 0x140a1eb26
00A1F14A  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
00A1F14E  48 85 C0                        test rax, rax
00A1F151  74 0E                           je 0x140a1f161
00A1F153  48 8B D8                        mov rbx, rax
00A1F156  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A1F15B  48 89 46 58                     mov qword ptr [rsi + 0x58], rax
00A1F15F  EB 44                           jmp 0x140a1f1a5
00A1F161  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00A1F165  48 85 C9                        test rcx, rcx
00A1F168  0F 84 B8 F9 FF FF               je 0x140a1eb26
00A1F16E  F6 41 0A 05                     test byte ptr [rcx + 0xa], 5
00A1F172  74 0B                           je 0x140a1f17f
00A1F174  48 8B 59 18                     mov rbx, qword ptr [rcx + 0x18]
00A1F178  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
00A1F17D  EB 22                           jmp 0x140a1f1a1
00A1F17F  C7 44 24 28 10 00 00 40         mov dword ptr [rsp + 0x28], 0x40000010
00A1F187  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00A1F18B  45 33 C9                        xor r9d, r9d
00A1F18E  33 D2                           xor edx, edx
00A1F190  45 8D 41 01                     lea r8d, [r9 + 1]
00A1F194  E8 67 96 8F FF                  call 0x140318800
00A1F199  48 8B D8                        mov rbx, rax
00A1F19C  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A1F1A1  48 89 5E 58                     mov qword ptr [rsi + 0x58], rbx
00A1F1A5  44 89 66 64                     mov dword ptr [rsi + 0x64], r12d
00A1F1A9  E9 78 F9 FF FF                  jmp 0x140a1eb26
00A1F1AE  41 BD 02 00 00 00               mov r13d, 2
00A1F1B4  E9 54 FA FF FF                  jmp 0x140a1ec0d
00A1F1B9  8B 4E 68                        mov ecx, dword ptr [rsi + 0x68]
00A1F1BC  44 3B F9                        cmp r15d, ecx
00A1F1BF  76 11                           jbe 0x140a1f1d2
00A1F1C1  45 8B C7                        mov r8d, r15d
00A1F1C4  44 2B C1                        sub r8d, ecx
00A1F1C7  48 03 4E 58                     add rcx, qword ptr [rsi + 0x58]
00A1F1CB  33 D2                           xor edx, edx
00A1F1CD  E8 6E 7A CA FF                  call 0x1406c6c40
00A1F1D2  44 38 AE 90 00 00 00            cmp byte ptr [rsi + 0x90], r13b
00A1F1D9  0F 94 C0                        sete al
00A1F1DC  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00A1F1E1  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A1F1E5  48 8B 84 24 80 01 00 00         mov rax, qword ptr [rsp + 0x180]
00A1F1ED  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1F1F2  4C 8D 8C 24 A8 00 00 00         lea r9, [rsp + 0xa8]
00A1F1FA  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00A1F1FF  8B 94 24 98 01 00 00            mov edx, dword ptr [rsp + 0x198]
00A1F206  48 8B CB                        mov rcx, rbx
00A1F209  E8 96 A0 06 00                  call 0x140a892a4
00A1F20E  84 C0                           test al, al
00A1F210  0F 84 C1 FA FF FF               je 0x140a1ecd7
00A1F216  43 8D 04 37                     lea eax, [r15 + r14]
00A1F21A  89 46 68                        mov dword ptr [rsi + 0x68], eax
00A1F21D  E9 F4 F9 FF FF                  jmp 0x140a1ec16
00A1F222  48 39 7E 58                     cmp qword ptr [rsi + 0x58], rdi
00A1F226  0F 84 F4 F9 FF FF               je 0x140a1ec20
00A1F22C  48 39 7E 50                     cmp qword ptr [rsi + 0x50], rdi
00A1F230  74 17                           je 0x140a1f249
00A1F232  8B 56 64                        mov edx, dword ptr [rsi + 0x64]
00A1F235  48 8B 4E 78                     mov rcx, qword ptr [rsi + 0x78]
00A1F239  E8 22 76 88 FF                  call 0x1402a6860
00A1F23E  33 D2                           xor edx, edx
00A1F240  48 8B 4E 50                     mov rcx, qword ptr [rsi + 0x50]
00A1F244  E8 27 36 16 00                  call 0x140b82870
00A1F249  48 89 7E 58                     mov qword ptr [rsi + 0x58], rdi
00A1F24D  48 89 7E 50                     mov qword ptr [rsi + 0x50], rdi
00A1F251  48 83 66 68 00                  and qword ptr [rsi + 0x68], 0
00A1F256  89 7E 64                        mov dword ptr [rsi + 0x64], edi
00A1F259  E9 C2 F9 FF FF                  jmp 0x140a1ec20
00A1F25E  66 83 C8 08                     or ax, 8
00A1F262  66 89 41 48                     mov word ptr [rcx + 0x48], ax
00A1F266  E9 04 FA FF FF                  jmp 0x140a1ec6f
00A1F26B  48 8B B4 24 60 01 00 00         mov rsi, qword ptr [rsp + 0x160]
00A1F273  83 6E 40 01                     sub dword ptr [rsi + 0x40], 1
00A1F277  74 1E                           je 0x140a1f297
00A1F279  48 81 C4 20 01 00 00            add rsp, 0x120
00A1F280  41 5F                           pop r15
00A1F282  41 5E                           pop r14
00A1F284  41 5D                           pop r13
00A1F286  41 5C                           pop r12
00A1F288  5F                              pop rdi
00A1F289  5E                              pop rsi
00A1F28A  5B                              pop rbx
00A1F28B  C3                              ret
00A1F28C  CC                              int3
00A1F28D  4D 85 FF                        test r15, r15
00A1F290  75 E7                           jne 0x140a1f279
00A1F292  E9 7C F6 FF FF                  jmp 0x140a1e913
00A1F297  48 89 7E 38                     mov qword ptr [rsi + 0x38], rdi
00A1F29B  48 8B CE                        mov rcx, rsi
00A1F29E  E8 FD 10 83 FF                  call 0x1402503a0
00A1F2A3  EB D4                           jmp 0x140a1f279
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlNotifyFilterReportChange(__int64 a1, __int64 a2, __int64 a3, unsigned __int16 a4, __int64 a5, __int64 a6, __int64 a7, unsigned int a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int16 v_stack_m10A;
    unsigned __int16 v_stack_m10C;
    unsigned int v_stack_m110;
    unsigned __int16 v_stack_m114;
    unsigned __int8 v_stack_m115;
    unsigned __int8 v_stack_m116;
    unsigned __int8 v_stack_m117;
    unsigned __int8 v_stack_m118;
    unsigned int v_stack_m128;
    unsigned int v_stack_m130;
    unsigned int v_stack_m138;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int16 v_stack_m6E;
    unsigned __int16 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int16 v_stack_mAE;
    unsigned __int16 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int16 v_stack_mBE;
    unsigned __int16 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int16 v_stack_mDE;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int16 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p8;

    *(unsigned __int16 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (288);
    v_stack_m58 = a3;
    v_stack_m10A = a4;
    v_stack_m90 = a5;
    v_stack_m50 = a5;
    *(unsigned __int64 *)(v_rsp - 112) = v_xmm0;
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 192) = 0;
    *(unsigned __int64 *)(v_rsp - 176) = 0;
    v_stack_mE0 = v_xmm0;
    v_stack_m118 = 0;
    v_stack_m104 = 0;
    v_stack_mC4 = 0;
    if (a4 == 0) goto loc_00A1F28D;
loc_00A1E913:
    v_stack_mB8 = 0;
    v_stack_mA8 = 0;
    result = a5;
    if ((*(unsigned __int64 *)(gs_base + (0 + 392))) != (*(unsigned __int64 *)(a1 + 56))) {
        result = ExAcquireFastMutexUnsafe(a1, a4, a2, a4);
        *(unsigned __int64 *)(a1 + 56) = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = a4;
        a3 = v_stack_p10;
    }
    v_stack_m114 = (unsigned __int16)(v_stack_mC0);
    v_stack_mA0 = v_stack_mA8;
    v_stack_m10C = (unsigned __int16)(v_stack_mB0);
    v_stack_m108 = (unsigned int)(v_stack_mE0);
loc_00A1E986:
    v_stack_m80 = *(unsigned __int64 *)(a3);
    v_stack_mE8 = *(unsigned __int64 *)(a3);
    if ((*(unsigned __int64 *)(a3)) == a3) goto loc_00A1F26B;
    v_stack_m78 = *(unsigned __int64 *)(a3) - 32;
    v_stack_m88 = *(unsigned __int64 *)(a3) - 32;
    if (a3 == 0) goto loc_00A1E9E0;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136))) == 0) goto loc_00A1E9D5;
    if (((v_stack_p38) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 76))))) != 0) goto loc_00A1ECE8;
loc_00A1E9D5:
    goto loc_00A1E986;
loc_00A1E9E0:
    if (a9 != (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 24))) goto loc_00A1E9D5;
    v_stack_mD8 = 0;
    v_stack_m108 = 0;
    v_stack_mE0 = 0;
    v_stack_m118 = 1;
    v_stack_m117 = 0;
loc_00A1EA10:
    if (((2) & ((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3) - 32 + 72)))) != 0) goto loc_00A1EC36;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 96))) == 0) goto loc_00A1EC31;
    v_stack_m100 = 0;
    v_stack_m100 = 0;
    v_stack_m60 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 100))) == 0) goto loc_00A1EE36;
loc_00A1EA4B:
    v_stack_m100 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 100)))));
    if (0 == 0) goto loc_00A1EE65;
    v_stack_m108 = 0;
    v_stack_mE0 = 0;
loc_00A1EA64:
    v_stack_m110 = 12;
    if (1 == 0) goto loc_00A1EC7C;
    v_r14 = (unsigned int)((*(unsigned __int16 *)(a5)) + (12));
loc_00A1EA88:
    v_stack_m110 = (unsigned int)(v_r14);
    goto loc_00A1EAC5;
loc_00A1EA8F:
    v_stack_mCC = 0;
    result = RtlMultiByteToUnicodeSize(v_stack_mCC, *(unsigned __int16 *)(*(unsigned __int64 *)(a3) - 32 + 72), (unsigned __int16)(*(unsigned __int64 *)(a3) - 32), a4);
    v_r14 = (unsigned int)((v_r14) + (v_stack_mCC));
loc_00A1EAAF:
    v_stack_m110 = (unsigned int)(v_r14);
    if (a5 != 0) goto loc_00A1F0D6;
loc_00A1EAC5:
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 104))) + (3));
    v_r15 = (unsigned int)((v_r15) & (0xFFFFFFFCULL));
    v_stack_m98 = (unsigned int)(v_r15);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)(v_r15 + v_r14 * 1)) >= ((unsigned int)(v_r15))) { result = (unsigned int)(v_r15 + v_r14 * 1); }
    v_stack_m44 = (unsigned int)(result);
    if (((unsigned int)(v_r14)) > ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 100))))))) goto loc_00A1ECD1;
    if (((unsigned int)(v_r15 + v_r14 * 1)) < ((unsigned int)(v_r15))) goto loc_00A1ECD1;
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 100))))))) goto loc_00A1ECD1;
    v_stack_mF0 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 88) != 0) goto loc_00A1F122;
    if (0 != 0) goto loc_00A1F14A;
loc_00A1EB26:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 88)) != 0) goto loc_00A1F1AE;
    v_stack_m115 = 0;
    result = PsChargePoolQuota(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 120), 1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 100)))))), a4);
    v_stack_m115 = 1;
    result = ExAllocatePool2(290, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 100)))))), (unsigned int)(0x4E725346ULL), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 88) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 80) = result;
    *(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 100) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 100)))));
    v_stack_mF0 = result;
    goto loc_00A1EC0D;
loc_00A1EC0D:
    if (result != 0) goto loc_00A1F1B9;
loc_00A1EC16:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 72)) & (2)) != 0) goto loc_00A1F222;
loc_00A1EC20:
loc_00A1EC31:
loc_00A1EC36:
    if (a8 == 4) goto loc_00A1F25E;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m88 + 72)) & ((unsigned __int16)((unsigned int)(0xFFF7ULL))));
    *(unsigned __int16 *)(v_stack_m88 + 72) = (unsigned __int16)(result);
    result = *(unsigned __int64 *)(a3) - 32 + 48;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 48)) != (*(unsigned __int64 *)(a3) - 32 + 48)) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(a3) - 32;
        result = FsRtlNotifyCompleteIrpList(a1, a2, (unsigned int)(0x4E725346ULL), a4);
    }
    goto loc_00A1E9D5;
loc_00A1EC7C:
    if ((unsigned __int8)(result) != 0) goto loc_00A1ECA3;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144)) == 1) goto loc_00A1F06A;
loc_00A1EC91:
    v_r14 = (unsigned int)(((unsigned __int16)(result)) + (12));
    v_stack_m110 = (unsigned int)(v_r14);
    v_r14 = (unsigned int)((v_r14) + (2));
    v_stack_m110 = (unsigned int)(v_r14);
loc_00A1ECA3:
    if (v_stack_mA0 == 0) goto loc_00A1F097;
loc_00A1ECB9:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144)) == 1) goto loc_00A1EA8F;
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)((unsigned __int16)(v_stack_m10C))));
    goto loc_00A1EAAF;
loc_00A1ECD1:
loc_00A1ECD7:
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a3) - 32 + 72)) | (2));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a3) - 32 + 72) = (unsigned __int16)(result);
    goto loc_00A1EC16;
loc_00A1ECE8:
    if (a6 == 0) goto loc_00A1ED7E;
loc_00A1ECF9:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136)))) > (*(unsigned __int16 *)(a6))) goto loc_00A1E9D5;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136)))) == (*(unsigned __int16 *)(a6))) goto loc_00A1EDD0;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3) - 32 + 72))) & (1)) == 0) goto loc_00A1E9D5;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3) - 32 + 72))) & (16)) != 0) goto loc_00A1ED48;
    a1 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m10C + 136))) + (*(unsigned __int64 *)(a6 + 8));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144)) != 1) goto loc_00A1EDD7;
loc_00A1ED42:
    if ((*(unsigned __int8 *)(a1)) != 92) goto loc_00A1E9D5;
loc_00A1ED48:
loc_00A1ED4B:
    v_stack_m117 = 0;
    result = memcmp(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136) + 8), *(unsigned __int64 *)(a6 + 8), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136)), *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136));
    if ((unsigned int)(result) != 0) goto loc_00A1EDE0;
    if (0 == 0) goto loc_00A1EDE5;
loc_00A1ED67:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 64) != 0) goto loc_00A1EE10;
loc_00A1ED74:
    goto loc_00A1EA10;
loc_00A1ED7E:
    v_stack_m68 = *(unsigned __int64 *)(v_stack_p18 + 8);
    v_stack_m70 = (unsigned __int16)((unsigned __int16)(v_r14));
    if (((unsigned __int16)(*(unsigned __int64 *)(a6 + 8))) != ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144)))) {
        a1 = (unsigned __int16)(*(unsigned __int64 *)(a6 + 8));
        a1 = (unsigned __int16)((a1) - ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144))));
        v_stack_m70 = (unsigned __int16)(a1);
    }
    v_stack_m6E = (unsigned __int16)(a1);
    v_stack_p30 = v_stack_m70;
    goto loc_00A1ECF9;
loc_00A1EDD0:
    goto loc_00A1ED4B;
loc_00A1EDD7:
    goto loc_00A1ED42;
loc_00A1EDE0:
    goto loc_00A1EC6F;
loc_00A1EDE5:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 16) == 0) goto loc_00A1ED67;
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 8), a9, *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 24), *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136));
    if ((unsigned __int8)(result) == 0) goto loc_00A1EDE0;
    goto loc_00A1ED67;
loc_00A1EE10:
    if (a10 == 0) goto loc_00A1ED74;
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 8), a10, *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 24), *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136));
    if ((unsigned __int8)(result) == 0) goto loc_00A1EDE0;
    goto loc_00A1ED74;
loc_00A1EE36:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 48)) == (*(unsigned __int64 *)(a3) - 32 + 48)) goto loc_00A1EA4B;
    v_stack_m60 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 48) - 168;
    goto loc_00A1EA4B;
loc_00A1EE65:
    if ((unsigned __int8)(v_stack_m118) != 0) goto loc_00A1F061;
    a2 = (unsigned __int16)((a10) & (16));
    if (condition_is_not_equal) goto loc_00A1EEBC;
    if ((*(unsigned __int64 *)(a6 + 8)) != (*(unsigned __int64 *)(v_stack_p18 + 8))) goto loc_00A1EEC8;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136)) * 1))) + (*(unsigned __int64 *)(a6 + 8));
    v_stack_mD8 = a1;
    result = (unsigned __int16)((*(unsigned __int16 *)(a6)) - ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144))));
    result = (unsigned __int16)((result) - ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136)))));
    goto loc_00A1F044;
loc_00A1EEBC:
    result = (v_stack_m58) + (8);
loc_00A1EEC8:
    if (v_stack_mB8 != 0) goto loc_00A1EF20;
    v_stack_mB8 = *(unsigned __int64 *)(result);
    v_stack_m114 = (unsigned __int16)(v_r14);
    v_stack_mC0 = (unsigned __int16)(v_r14);
    if (((unsigned __int16)(v_stack_m10A)) != ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144)))) {
        v_r14 = (unsigned __int16)(v_stack_m10A);
        v_r14 = (unsigned __int16)((v_r14) - ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144))));
        v_stack_m114 = (unsigned __int16)(v_r14);
        v_stack_mC0 = (unsigned __int16)(v_r14);
    }
    v_stack_mBE = (unsigned __int16)(v_r14);
    goto loc_00A1EF26;
loc_00A1EF20:
loc_00A1EF26:
    v_stack_m116 = 0;
    v_stack_m104 = 0;
    if ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144)) != 0) goto loc_00A1F01D;
    v_stack_mFC = 0;
    v_stack_mF8 = 0;
    v_stack_mFC = 1;
    v_stack_mF8 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144)) != 1) goto loc_00A1EFB7;
loc_00A1EF60:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136))))) goto loc_00A1EF8B;
    if ((*(unsigned __int8 *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136) + 8) * 1)) == 92) {
        a4 = (unsigned int)((1) + 1);
        v_stack_mFC = a4;
    }
    a2 = (unsigned int)((0) + 1);
    v_stack_mF8 = (unsigned int)(a2);
    goto loc_00A1EF60;
loc_00A1EF8B:
loc_00A1EF93:
    if ((*(unsigned __int8 *)(0 + v_stack_mB8 * 1)) != 92) goto loc_00A1EFAD;
    v_r10 = (unsigned __int8)((0) + 1);
    v_stack_m116 = (unsigned __int8)(v_r10);
    if (((unsigned int)((unsigned __int8)(v_r10))) == a4) goto loc_00A1F018;
loc_00A1EFAD:
    a3 = (unsigned int)((0) + 1);
    v_stack_m104 = (unsigned int)(a3);
    goto loc_00A1EF93;
loc_00A1EFB7:
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136))) >> (1));
    if (((unsigned int)(a2)) >= ((unsigned int)(result))) goto loc_00A1EFE5;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 136) + 8) + (unsigned int)((unsigned int)(a2)) * 2)) == 92) {
        a4 = (unsigned int)((a4) + 1);
        v_stack_mFC = a4;
    }
    a2 = (unsigned int)((a2) + 1);
    v_stack_mF8 = (unsigned int)(a2);
    goto loc_00A1EFB7;
loc_00A1EFE5:
loc_00A1EFED:
    if ((*(unsigned __int16 *)(v_stack_mB8 + (unsigned int)((unsigned int)(a3)) * 2)) != 92) goto loc_00A1F057;
    v_r10 = (unsigned __int8)((v_r10) + 1);
    v_stack_m116 = (unsigned __int8)(v_r10);
    if (((unsigned int)((unsigned __int8)(v_r10))) != a4) goto loc_00A1F057;
    a3 = (unsigned int)((a3) * ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144))));
    v_stack_m104 = (unsigned int)(a3);
loc_00A1F018:
loc_00A1F01D:
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144)) + ((unsigned int)(a3)));
    v_stack_m104 = (unsigned int)(a1);
    result = ((unsigned int)((unsigned int)(a1))) + (v_stack_mB8);
    v_stack_mD8 = result;
    result = (unsigned __int16)(((unsigned __int16)(v_stack_m114)) - ((unsigned __int16)(a1)));
loc_00A1F044:
    v_stack_m108 = (unsigned int)(result);
    v_stack_mE0 = (unsigned __int16)(result);
    v_stack_mDE = (unsigned __int16)(result);
    goto loc_00A1EA64;
loc_00A1F057:
    a3 = (unsigned int)((a3) + 1);
    v_stack_m104 = (unsigned int)(a3);
    goto loc_00A1EFED;
loc_00A1F061:
    goto loc_00A1EA64;
loc_00A1F06A:
    v_stack_mD0 = 0;
    result = RtlMultiByteToUnicodeSize(v_stack_mD0, v_stack_mD8, (unsigned __int16)((unsigned int)(v_stack_m108)), a4);
    goto loc_00A1EC91;
loc_00A1F097:
    a2 = ((unsigned int)((unsigned int)(v_stack_p20))) + (*(unsigned __int64 *)(v_stack_p18 + 8));
    v_stack_mA0 = a2;
    v_stack_mA8 = a2;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p18)) - ((unsigned __int16)(v_stack_p20)));
    v_stack_m10C = (unsigned __int16)(a1);
    v_stack_mB0 = (unsigned __int16)(a1);
    v_stack_mAE = (unsigned __int16)(a1);
    goto loc_00A1ECB9;
loc_00A1F0D6:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144)) != 2) goto loc_00A1F0F3;
    goto loc_00A1F11A;
loc_00A1F0F3:
    v_stack_mC8 = 0;
    result = RtlMultiByteToUnicodeSize(v_stack_mC8, *(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m90))), a4);
    v_r14 = (unsigned int)(((unsigned int)(v_stack_mC8)) + (2));
loc_00A1F11A:
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mD0))))));
    goto loc_00A1EA88;
loc_00A1F122:
    v_stack_mF0 = result + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 108)) * 1;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p18))) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 108)))));
    *(unsigned int *)(result + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 108)) * 1) = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 108) = (unsigned int)(v_stack_p18);
    v_rbx = ((unsigned int)((unsigned int)(v_stack_p18))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 88));
    v_stack_mF0 = v_rbx;
    goto loc_00A1EB26;
loc_00A1F14A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 48) - 168 + 24) == 0) goto loc_00A1F161;
    v_stack_mF0 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 48) - 168 + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 48) - 168 + 24);
    goto loc_00A1F1A5;
loc_00A1F161:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 48) - 168 + 8) == 0) goto loc_00A1EB26;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 48) - 168 + 8) + 10)) & (5)) == 0) goto loc_00A1F17F;
    v_stack_mF0 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 48) - 168 + 8) + 24);
    goto loc_00A1F1A1;
loc_00A1F17F:
    v_stack_m130 = 0x40000010ULL;
    v_stack_m138 = 0;
    a4 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 48) - 168 + 8), a2, a4 + 1, a4);
    v_stack_mF0 = result;
loc_00A1F1A1:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 88) = result;
loc_00A1F1A5:
    *(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 100) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 48) - 168 + 184) + 8)));
    goto loc_00A1EB26;
loc_00A1F1AE:
    goto loc_00A1EC0D;
loc_00A1F1B9:
    if (((unsigned int)(v_stack_p18)) >= = ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 104))))) {
        a3 = (unsigned int)(v_stack_p18);
        a3 = (unsigned int)((a3) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 104)))));
        a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 104))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 88));
        a2 = 0;
        result = memset(a1, a2, a3, a4);
    }
    result = ((*(unsigned __int8 *)(*(unsigned __int64 *)(a3) - 32 + 144)) == 2) ? 1 : 0;
    v_stack_m128 = (unsigned int)(v_r14);
    v_stack_m130 = (unsigned __int8)(result);
    v_stack_m138 = a5;
    result = FsRtlNotifyUpdateBuffer(result, (unsigned int)(a8), v_stack_mE0, v_stack_mB0);
    if ((unsigned __int8)(result) == 0) goto loc_00A1ECD7;
    *(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 104) = (unsigned int)(v_stack_p18 + v_r14 * 1);
    goto loc_00A1EC16;
loc_00A1F222:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 88)) == 0) goto loc_00A1EC20;
    result = v_stack_p18 + v_r14 * 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 80)) != 0) {
        a2 = *(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 100);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 120);
        result = PsReturnProcessPagedPoolQuota(a1, a2, v_stack_mE0, v_stack_mB0);
        a2 = 0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 80);
        result = ExFreePoolWithTag(a1, a2, v_stack_mE0, v_stack_mB0);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 88) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 32 + 80) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a3) - 32 + 100) = 0;
    goto loc_00A1EC20;
loc_00A1F25E:
    result = (unsigned __int16)((result) | (8));
    *(unsigned __int16 *)(a1 + 72) = (unsigned __int16)(result);
    goto loc_00A1EC6F;
loc_00A1F26B:
    if (condition_is_equal) goto loc_00A1F297;
loc_00A1F279:
    v_rsp = (v_rsp) + (288);
    return result;
loc_00A1F28D:
    if (v_stack_p18 != 0) goto loc_00A1F279;
    goto loc_00A1E913;
loc_00A1F297:
    *(unsigned __int64 *)(v_stack_p8 + 56) = 0;
    result = ExReleaseFastMutexUnsafe(v_stack_p8, a2, v_stack_mE0, v_stack_mB0);
    goto loc_00A1F279;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlNotifyFilterReportChange(void *Arg1, int64_t Arg2, int64_t Arg3, uint16_t Arg4, void *Arg5, void *Arg6, uint64_t Arg7, uint32_t Arg8, int64_t Arg9, int64_t Arg10)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint16_t v_stack_m10A;
    uint16_t v_stack_m10C;
    uint32_t v_stack_m110;
    uint16_t v_stack_m114;
    uint8_t v_stack_m115;
    uint8_t v_stack_m116;
    uint8_t v_stack_m117;
    uint8_t v_stack_m118;
    uint32_t v_stack_m128;
    uint32_t v_stack_m130;
    uint32_t v_stack_m138;
    uint32_t v_stack_m44;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint16_t v_stack_m6E;
    uint16_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint16_t v_stack_mAE;
    uint16_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint16_t v_stack_mBE;
    uint16_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint16_t v_stack_mDE;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint16_t v_stack_p20;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p8;

    *(uint16_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (288);
    v_stack_m58 = Arg3;
    v_stack_m10A = Arg4;
    v_stack_m90 = Arg5;
    v_stack_m50 = Arg5;
    *(uint64_t *)(local_rsp - 0x70) = v_xmm0;
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0xC0) = 0;
    *(uint64_t *)(local_rsp - 0xB0) = 0;
    v_stack_mE0 = v_xmm0;
    v_stack_m118 = 0;
    v_stack_m104 = 0;
    v_stack_mC4 = 0;
    if (Arg4 == 0) goto loc_00A1F28D;
loc_00A1E913:
    v_stack_mB8 = 0;
    v_stack_mA8 = 0;
    result = Arg5;
    if ((*(uint64_t *)(gs_base + (0 + 0x188))) != (*(uint64_t *)(arg1 + 0x38))) {
        result = ExAcquireFastMutexUnsafe(Arg1, Arg4, Arg2, Arg4);
        *(uint64_t *)(arg1 + 0x38) = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = Arg4;
        Arg3 = v_stack_p10;
    }
    v_stack_m114 = (uint16_t)(v_stack_mC0);
    v_stack_mA0 = v_stack_mA8;
    v_stack_m10C = (uint16_t)(v_stack_mB0);
    v_stack_m108 = (uint32_t)(v_stack_mE0);
loc_00A1E986:
    v_stack_m80 = *(uint64_t *)(Arg3);
    v_stack_mE8 = *(uint64_t *)(Arg3);
    if ((*(uint64_t *)(Arg3)) == Arg3) goto loc_00A1F26B;
    v_stack_m78 = *(uint64_t *)(Arg3) - 32;
    v_stack_m88 = *(uint64_t *)(Arg3) - 32;
    if (Arg3 == 0) goto loc_00A1E9E0;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88))) == 0) goto loc_00A1E9D5;
    if (((v_stack_p38) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x4C))))) != 0) goto loc_00A1ECE8;
loc_00A1E9D5:
    goto loc_00A1E986;
loc_00A1E9E0:
    if (Arg9 != (*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x18))) goto loc_00A1E9D5;
    v_stack_mD8 = 0;
    v_stack_m108 = 0;
    v_stack_mE0 = 0;
    v_stack_m118 = 1;
    v_stack_m117 = 0;
loc_00A1EA10:
    if (((2) & ((uint8_t)(*(uint16_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x48)))) != 0) goto loc_00A1EC36;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x60))) == 0) goto loc_00A1EC31;
    v_stack_m100 = 0;
    v_stack_m100 = 0;
    v_stack_m60 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x64))) == 0) goto loc_00A1EE36;
loc_00A1EA4B:
    v_stack_m100 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x64)))));
    if (0 == 0) goto loc_00A1EE65;
    v_stack_m108 = 0;
    v_stack_mE0 = 0;
loc_00A1EA64:
    v_stack_m110 = 12;
    if (1 == 0) goto loc_00A1EC7C;
    local_r14 = (uint32_t)((*(uint16_t *)(arg5)) + (12));
loc_00A1EA88:
    v_stack_m110 = (uint32_t)(local_r14);
    goto loc_00A1EAC5;
loc_00A1EA8F:
    v_stack_mCC = 0;
    result = RtlMultiByteToUnicodeSize(v_stack_mCC, *(uint16_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x48), (uint16_t)(*(uint64_t *)(Arg3) - 32), Arg4);
    local_r14 = (uint32_t)((local_r14) + (v_stack_mCC));
loc_00A1EAAF:
    v_stack_m110 = (uint32_t)(local_r14);
    if (Arg5 != NULL) goto loc_00A1F0D6;
loc_00A1EAC5:
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x68))) + (3));
    local_r15 = (uint32_t)((local_r15) & (0xFFFFFFFCULL));
    v_stack_m98 = (uint32_t)(local_r15);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)(local_r15 + local_r14 * 1)) >= ((uint32_t)(local_r15))) { result = (uint32_t)(local_r15 + local_r14 * 1); }
    v_stack_m44 = (uint32_t)(result);
    if (((uint32_t)(local_r14)) > ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x64))))))) goto loc_00A1ECD1;
    if (((uint32_t)(local_r15 + local_r14 * 1)) < ((uint32_t)(local_r15))) goto loc_00A1ECD1;
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x64))))))) goto loc_00A1ECD1;
    v_stack_mF0 = 0;
    if (*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x58) != 0) goto loc_00A1F122;
    if (0 != 0) goto loc_00A1F14A;
loc_00A1EB26:
    if ((*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x58)) != 0) goto loc_00A1F1AE;
    v_stack_m115 = 0;
    result = PsChargePoolQuota(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x78), 1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x64)))))), Arg4);
    v_stack_m115 = 1;
    result = ExAllocatePool2(290, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x64)))))), (uint32_t)(0x4E725346ULL), Arg4);
    *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x58) = result;
    *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x50) = result;
    *(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x64) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x64)))));
    v_stack_mF0 = result;
    goto loc_00A1EC0D;
loc_00A1EC0D:
    if (result != 0) goto loc_00A1F1B9;
loc_00A1EC16:
    if (((*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x48)) & (2)) != 0) goto loc_00A1F222;
loc_00A1EC20:
loc_00A1EC31:
loc_00A1EC36:
    if (Arg8 == 4) goto loc_00A1F25E;
    result = (uint16_t)((*(uint16_t *)(v_stack_m88 + 0x48)) & ((uint16_t)((uint32_t)(0xFFF7ULL))));
    *(uint16_t *)(v_stack_m88 + 0x48) = (uint16_t)(result);
    result = *(uint64_t *)(Arg3) - 32 + 48;
    if ((*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x30)) != (*(uint64_t *)(Arg3) - 32 + 48)) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(Arg3) - 32;
        result = FsRtlNotifyCompleteIrpList(Arg1, Arg2, (uint32_t)(0x4E725346ULL), Arg4);
    }
    goto loc_00A1E9D5;
loc_00A1EC7C:
    if ((uint8_t)(result) != 0) goto loc_00A1ECA3;
    if ((*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90)) == 1) goto loc_00A1F06A;
loc_00A1EC91:
    local_r14 = (uint32_t)(((uint16_t)(result)) + (12));
    v_stack_m110 = (uint32_t)(local_r14);
    local_r14 = (uint32_t)((local_r14) + (2));
    v_stack_m110 = (uint32_t)(local_r14);
loc_00A1ECA3:
    if (v_stack_mA0 == 0) goto loc_00A1F097;
loc_00A1ECB9:
    if ((*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90)) == 1) goto loc_00A1EA8F;
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)((uint16_t)(v_stack_m10C))));
    goto loc_00A1EAAF;
loc_00A1ECD1:
loc_00A1ECD7:
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x48)) | (2));
    *(uint16_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x48) = (uint16_t)(result);
    goto loc_00A1EC16;
loc_00A1ECE8:
    if (Arg6 == NULL) goto loc_00A1ED7E;
loc_00A1ECF9:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88)))) > (*(uint16_t *)(arg6))) goto loc_00A1E9D5;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88)))) == (*(uint16_t *)(arg6))) goto loc_00A1EDD0;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x48))) & (1)) == 0) goto loc_00A1E9D5;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x48))) & (16)) != 0) goto loc_00A1ED48;
    Arg1 = (*(uint16_t *)(*(uint64_t *)(v_stack_m10C + 0x88))) + (*(uint64_t *)(arg6 + 0x8));
    if ((*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90)) != 1) goto loc_00A1EDD7;
loc_00A1ED42:
    if ((*(uint8_t *)(arg1)) != 92) goto loc_00A1E9D5;
loc_00A1ED48:
loc_00A1ED4B:
    v_stack_m117 = 0;
    result = memcmp(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88) + 0x8), *(uint64_t *)(arg6 + 0x8), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88)), *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88));
    if ((uint32_t)(result) != 0) goto loc_00A1EDE0;
    if (0 == 0) goto loc_00A1EDE5;
loc_00A1ED67:
    if (*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x40) != 0) goto loc_00A1EE10;
loc_00A1ED74:
    goto loc_00A1EA10;
loc_00A1ED7E:
    v_stack_m68 = *(uint64_t *)(v_stack_p18 + 0x8);
    v_stack_m70 = (uint16_t)((uint16_t)(local_r14));
    if (((uint16_t)(*(uint64_t *)(arg6 + 0x8))) != ((uint16_t)(*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90)))) {
        Arg1 = (uint16_t)(*(uint64_t *)(arg6 + 0x8));
        Arg1 = (uint16_t)((Arg1) - ((uint16_t)(*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90))));
        v_stack_m70 = (uint16_t)(Arg1);
    }
    v_stack_m6E = (uint16_t)(Arg1);
    v_stack_p30 = v_stack_m70;
    goto loc_00A1ECF9;
loc_00A1EDD0:
    goto loc_00A1ED4B;
loc_00A1EDD7:
    goto loc_00A1ED42;
loc_00A1EDE0:
    goto loc_00A1EC6F;
loc_00A1EDE5:
    if (*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x10) == 0) goto loc_00A1ED67;
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x8), Arg9, *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x18), *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88));
    if ((uint8_t)(result) == 0) goto loc_00A1EDE0;
    goto loc_00A1ED67;
loc_00A1EE10:
    if (Arg10 == 0) goto loc_00A1ED74;
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x8), Arg10, *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x18), *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88));
    if ((uint8_t)(result) == 0) goto loc_00A1EDE0;
    goto loc_00A1ED74;
loc_00A1EE36:
    if ((*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x30)) == (*(uint64_t *)(Arg3) - 32 + 48)) goto loc_00A1EA4B;
    v_stack_m60 = *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x30) - 168;
    goto loc_00A1EA4B;
loc_00A1EE65:
    if ((uint8_t)(v_stack_m118) != 0) goto loc_00A1F061;
    Arg2 = (uint16_t)((Arg10) & (16));
    if (condition_is_not_equal) goto loc_00A1EEBC;
    if ((*(uint64_t *)(arg6 + 0x8)) != (*(uint64_t *)(v_stack_p18 + 0x8))) goto loc_00A1EEC8;
    Arg1 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88)) * 1))) + (*(uint64_t *)(arg6 + 0x8));
    v_stack_mD8 = Arg1;
    result = (uint16_t)((*(uint16_t *)(arg6)) - ((uint16_t)(*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90))));
    result = (uint16_t)((result) - ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88)))));
    goto loc_00A1F044;
loc_00A1EEBC:
    result = (v_stack_m58) + (8);
loc_00A1EEC8:
    if (v_stack_mB8 != 0) goto loc_00A1EF20;
    v_stack_mB8 = *(uint64_t *)(result);
    v_stack_m114 = (uint16_t)(local_r14);
    v_stack_mC0 = (uint16_t)(local_r14);
    if (((uint16_t)(v_stack_m10A)) != ((uint16_t)(*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90)))) {
        local_r14 = (uint16_t)(v_stack_m10A);
        local_r14 = (uint16_t)((local_r14) - ((uint16_t)(*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90))));
        v_stack_m114 = (uint16_t)(local_r14);
        v_stack_mC0 = (uint16_t)(local_r14);
    }
    v_stack_mBE = (uint16_t)(local_r14);
    goto loc_00A1EF26;
loc_00A1EF20:
loc_00A1EF26:
    v_stack_m116 = 0;
    v_stack_m104 = 0;
    if ((uint16_t)(*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90)) != 0) goto loc_00A1F01D;
    v_stack_mFC = 0;
    v_stack_mF8 = 0;
    v_stack_mFC = 1;
    v_stack_mF8 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90)) != 1) goto loc_00A1EFB7;
loc_00A1EF60:
    if (0 >= ((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88))))) goto loc_00A1EF8B;
    if ((*(uint8_t *)(0 + *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88) + 0x8) * 1)) == 92) {
        Arg4 = (uint32_t)((1) + 1);
        v_stack_mFC = Arg4;
    }
    Arg2 = (uint32_t)((0) + 1);
    v_stack_mF8 = (uint32_t)(Arg2);
    goto loc_00A1EF60;
loc_00A1EF8B:
loc_00A1EF93:
    if ((*(uint8_t *)(0 + v_stack_mB8 * 1)) != 92) goto loc_00A1EFAD;
    local_r10 = (uint8_t)((0) + 1);
    v_stack_m116 = (uint8_t)(local_r10);
    if (((uint32_t)((uint8_t)(local_r10))) == Arg4) goto loc_00A1F018;
loc_00A1EFAD:
    Arg3 = (uint32_t)((0) + 1);
    v_stack_m104 = (uint32_t)(Arg3);
    goto loc_00A1EF93;
loc_00A1EFB7:
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88))) >> (1));
    if (((uint32_t)(Arg2)) >= ((uint32_t)(result))) goto loc_00A1EFE5;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x88) + 0x8) + (uint32_t)((uint32_t)(Arg2)) * 2)) == 92) {
        Arg4 = (uint32_t)((Arg4) + 1);
        v_stack_mFC = Arg4;
    }
    Arg2 = (uint32_t)((Arg2) + 1);
    v_stack_mF8 = (uint32_t)(Arg2);
    goto loc_00A1EFB7;
loc_00A1EFE5:
loc_00A1EFED:
    if ((*(uint16_t *)(v_stack_mB8 + (uint32_t)((uint32_t)(Arg3)) * 2)) != 92) goto loc_00A1F057;
    local_r10 = (uint8_t)((local_r10) + 1);
    v_stack_m116 = (uint8_t)(local_r10);
    if (((uint32_t)((uint8_t)(local_r10))) != Arg4) goto loc_00A1F057;
    Arg3 = (uint32_t)((Arg3) * ((uint32_t)(*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90))));
    v_stack_m104 = (uint32_t)(Arg3);
loc_00A1F018:
loc_00A1F01D:
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90)) + ((uint32_t)(Arg3)));
    v_stack_m104 = (uint32_t)(Arg1);
    result = ((uint32_t)((uint32_t)(Arg1))) + (v_stack_mB8);
    v_stack_mD8 = result;
    result = (uint16_t)(((uint16_t)(v_stack_m114)) - ((uint16_t)(Arg1)));
loc_00A1F044:
    v_stack_m108 = (uint32_t)(result);
    v_stack_mE0 = (uint16_t)(result);
    v_stack_mDE = (uint16_t)(result);
    goto loc_00A1EA64;
loc_00A1F057:
    Arg3 = (uint32_t)((Arg3) + 1);
    v_stack_m104 = (uint32_t)(Arg3);
    goto loc_00A1EFED;
loc_00A1F061:
    goto loc_00A1EA64;
loc_00A1F06A:
    v_stack_mD0 = 0;
    result = RtlMultiByteToUnicodeSize(v_stack_mD0, v_stack_mD8, (uint16_t)((uint32_t)(v_stack_m108)), Arg4);
    goto loc_00A1EC91;
loc_00A1F097:
    Arg2 = ((uint32_t)((uint32_t)(v_stack_p20))) + (*(uint64_t *)(v_stack_p18 + 0x8));
    v_stack_mA0 = Arg2;
    v_stack_mA8 = Arg2;
    Arg1 = (uint16_t)((*(uint16_t *)(v_stack_p18)) - ((uint16_t)(v_stack_p20)));
    v_stack_m10C = (uint16_t)(Arg1);
    v_stack_mB0 = (uint16_t)(Arg1);
    v_stack_mAE = (uint16_t)(Arg1);
    goto loc_00A1ECB9;
loc_00A1F0D6:
    if ((*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90)) != 2) goto loc_00A1F0F3;
    goto loc_00A1F11A;
loc_00A1F0F3:
    v_stack_mC8 = 0;
    result = RtlMultiByteToUnicodeSize(v_stack_mC8, *(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m90))), Arg4);
    local_r14 = (uint32_t)(((uint32_t)(v_stack_mC8)) + (2));
loc_00A1F11A:
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mD0))))));
    goto loc_00A1EA88;
loc_00A1F122:
    v_stack_mF0 = result + (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x6C)) * 1;
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p18))) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x6C)))));
    *(uint32_t *)(result + (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x6C)) * 1) = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x6C) = (uint32_t)(v_stack_p18);
    local_rbx = ((uint32_t)((uint32_t)(v_stack_p18))) + (*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x58));
    v_stack_mF0 = local_rbx;
    goto loc_00A1EB26;
loc_00A1F14A:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x30) - 0xA8 + 0x18) == 0) goto loc_00A1F161;
    v_stack_mF0 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x30) - 0xA8 + 0x18);
    *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x58) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x30) - 0xA8 + 0x18);
    goto loc_00A1F1A5;
loc_00A1F161:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x30) - 0xA8 + 0x8) == 0) goto loc_00A1EB26;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x30) - 0xA8 + 0x8) + 0xA)) & (5)) == 0) goto loc_00A1F17F;
    v_stack_mF0 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x30) - 0xA8 + 0x8) + 0x18);
    goto loc_00A1F1A1;
loc_00A1F17F:
    v_stack_m130 = 0x40000010ULL;
    v_stack_m138 = 0;
    Arg4 = 0;
    Arg2 = 0;
    result = MmMapLockedPagesSpecifyCache(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x30) - 0xA8 + 0x8), Arg2, Arg4 + 1, Arg4);
    v_stack_mF0 = result;
loc_00A1F1A1:
    *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x58) = result;
loc_00A1F1A5:
    *(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x64) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x30) - 0xA8 + 0xB8) + 0x8)));
    goto loc_00A1EB26;
loc_00A1F1AE:
    goto loc_00A1EC0D;
loc_00A1F1B9:
    if (((uint32_t)(v_stack_p18)) >= = ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x68))))) {
        Arg3 = (uint32_t)(v_stack_p18);
        Arg3 = (uint32_t)((Arg3) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x68)))));
        Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x68))) + (*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x58));
        Arg2 = 0;
        result = memset(Arg1, Arg2, Arg3, Arg4);
    }
    result = ((*(uint8_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x90)) == 2) ? 1 : 0;
    v_stack_m128 = (uint32_t)(local_r14);
    v_stack_m130 = (uint8_t)(result);
    v_stack_m138 = Arg5;
    result = FsRtlNotifyUpdateBuffer(result, (uint32_t)(Arg8), v_stack_mE0, v_stack_mB0);
    if ((uint8_t)(result) == 0) goto loc_00A1ECD7;
    *(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x68) = (uint32_t)(v_stack_p18 + local_r14 * 1);
    goto loc_00A1EC16;
loc_00A1F222:
    if ((*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x58)) == 0) goto loc_00A1EC20;
    result = v_stack_p18 + local_r14 * 1;
    if ((*(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x50)) != 0) {
        Arg2 = *(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x64);
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x78);
        result = PsReturnProcessPagedPoolQuota(Arg1, Arg2, v_stack_mE0, v_stack_mB0);
        Arg2 = 0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x50);
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_mE0, v_stack_mB0);
    }
    *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x58) = 0;
    *(uint64_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x50) = 0;
    *(uint32_t *)(*(uint64_t *)(Arg3) - 0x20 + 0x64) = 0;
    goto loc_00A1EC20;
loc_00A1F25E:
    result = (uint16_t)((result) | (8));
    *(uint16_t *)(arg1 + 0x48) = (uint16_t)(result);
    goto loc_00A1EC6F;
loc_00A1F26B:
    if (condition_is_equal) goto loc_00A1F297;
loc_00A1F279:
    local_rsp = (local_rsp) + (288);
    return result;
loc_00A1F28D:
    if (v_stack_p18 != 0) goto loc_00A1F279;
    goto loc_00A1E913;
loc_00A1F297:
    *(uint64_t *)(v_stack_p8 + 0x38) = 0;
    result = ExReleaseFastMutexUnsafe(v_stack_p8, Arg2, v_stack_mE0, v_stack_mB0);
    goto loc_00A1F279;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `W` |
| `Arg1` | `+ 0x40` | `32` | `R/W` |
| `Arg5` | `+ 0x0` | `16` | `R` |
| `Arg6` | `+ 0x0` | `16` | `R` |
| `Arg6` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A1E880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
