# FsRtlNotifyFilterReportChangeLiteEx

- RVA: `0x00A1F2B0`–`0x00A1F983` (길이 `1,747` bytes)
- VA: `0x0000000140A1F2B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AAB10`
- 디코드: `419`개 명령, `1,747/1,747` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A1F317` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x00A1F5A6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A1F5D4` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A1F678` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A1F6E0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A1F785` → [FsRtlNotifyCompleteIrp](FsRtlNotifyCompleteIrp_function_00A1FA28.md) (function, `0x00A1FA28`)
- `0x00A1F7A4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A1F7DD` → [PsChargePoolQuota](../../text/3E/PsChargePoolQuota_function_003EC7F0.md) (function, `0x003EC7F0`)
- `0x00A1F7F5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A1F82D` → [PsReturnProcessPagedPoolQuota](../../text/2A/PsReturnProcessPagedPoolQuota_function_002A6860.md) (function, `0x002A6860`)
- `0x00A1F889` → [PsReturnProcessPagedPoolQuota](../../text/2A/PsReturnProcessPagedPoolQuota_function_002A6860.md) (function, `0x002A6860`)
- `0x00A1F894` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A1F8FC` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x00A1F92E` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x00A1F95C` → [FsRtlNotifyInitializeSync](../A7/FsRtlNotifyInitializeSync_function_00A7BDE0.md) (function, `0x00A7BDE0`)
- `0x00A1F979` → [FsRtlNotifyUninitializeSync](../A8/FsRtlNotifyUninitializeSync_function_00A8A410.md) (function, `0x00A8A410`)

### Direct callers
- [FsRtlNotifyFilterReportChangeLite](../71/FsRtlNotifyFilterReportChangeLite_function_00716E30.md) at `0x00716E75`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x00A1F317` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (`PAGE` → `.text`)
  - `0x00A1F5A6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A1F5D4` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A1F678` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A1F6E0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A1F7A4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A1F7DD` → [PsChargePoolQuota](../../text/3E/PsChargePoolQuota_function_003EC7F0.md) (`PAGE` → `.text`)
  - `0x00A1F7F5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A1F82D` → [PsReturnProcessPagedPoolQuota](../../text/2A/PsReturnProcessPagedPoolQuota_function_002A6860.md) (`PAGE` → `.text`)
  - `0x00A1F889` → [PsReturnProcessPagedPoolQuota](../../text/2A/PsReturnProcessPagedPoolQuota_function_002A6860.md) (`PAGE` → `.text`)
  - `0x00A1F894` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A1F8FC` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (`PAGE` → `.text`)
  - `0x00A1F92E` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A1F2B0  48 8B C4                        mov rax, rsp
00A1F2B3  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00A1F2B7  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00A1F2BB  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00A1F2BF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00A1F2C3  53                              push rbx
00A1F2C4  56                              push rsi
00A1F2C5  57                              push rdi
00A1F2C6  41 54                           push r12
00A1F2C8  41 55                           push r13
00A1F2CA  41 56                           push r14
00A1F2CC  41 57                           push r15
00A1F2CE  48 81 EC A0 00 00 00            sub rsp, 0xa0
00A1F2D5  48 8B FA                        mov rdi, rdx
00A1F2D8  4C 8B E1                        mov r12, rcx
00A1F2DB  33 F6                           xor esi, esi
00A1F2DD  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
00A1F2E1  48 39 12                        cmp qword ptr [rdx], rdx
00A1F2E4  0F 84 49 06 00 00               je 0x140a1f933
00A1F2EA  48 8B 84 24 28 01 00 00         mov rax, qword ptr [rsp + 0x128]
00A1F2F2  48 85 C0                        test rax, rax
00A1F2F5  0F 85 4C 06 00 00               jne 0x140a1f947
00A1F2FB  48 39 31                        cmp qword ptr [rcx], rsi
00A1F2FE  0F 84 4E 06 00 00               je 0x140a1f952
00A1F304  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
00A1F30D  49 8B 0C 24                     mov rcx, qword ptr [r12]
00A1F311  48 3B 59 38                     cmp rbx, qword ptr [rcx + 0x38]
00A1F315  74 0D                           je 0x140a1f324
00A1F317  E8 04 44 9D FF                  call 0x1403f3720
00A1F31C  49 8B 04 24                     mov rax, qword ptr [r12]
00A1F320  48 89 58 38                     mov qword ptr [rax + 0x38], rbx
00A1F324  49 8B 04 24                     mov rax, qword ptr [r12]
00A1F328  FF 40 40                        inc dword ptr [rax + 0x40]
00A1F32B  48 8B 1F                        mov rbx, qword ptr [rdi]
00A1F32E  41 BD 02 00 00 00               mov r13d, 2
00A1F334  45 8D 75 52                     lea r14d, [r13 + 0x52]
00A1F338  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00A1F33D  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
00A1F342  48 3B DF                        cmp rbx, rdi
00A1F345  0F 84 CB 05 00 00               je 0x140a1f916
00A1F34B  48 8D 7B E0                     lea rdi, [rbx - 0x20]
00A1F34F  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00A1F354  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
00A1F35C  8B 47 4C                        mov eax, dword ptr [rdi + 0x4c]
00A1F35F  85 84 24 00 01 00 00            test dword ptr [rsp + 0x100], eax
00A1F366  75 0D                           jne 0x140a1f375
00A1F368  48 8B 1B                        mov rbx, qword ptr [rbx]
00A1F36B  48 8B BC 24 E8 00 00 00         mov rdi, qword ptr [rsp + 0xe8]
00A1F373  EB C3                           jmp 0x140a1f338
00A1F375  F6 84 24 20 01 00 00 01         test byte ptr [rsp + 0x120], 1
00A1F37D  0F 84 14 01 00 00               je 0x140a1f497
00A1F383  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
00A1F387  48 85 C0                        test rax, rax
00A1F38A  0F 85 FF 03 00 00               jne 0x140a1f78f
00A1F390  44 84 6F 48                     test byte ptr [rdi + 0x48], r13b
00A1F394  0F 85 CC 00 00 00               jne 0x140a1f466
00A1F39A  44 8B 7F 60                     mov r15d, dword ptr [rdi + 0x60]
00A1F39E  45 85 FF                        test r15d, r15d
00A1F3A1  0F 84 BF 00 00 00               je 0x140a1f466
00A1F3A7  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
00A1F3AB  48 8B CE                        mov rcx, rsi
00A1F3AE  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
00A1F3B6  8B 47 64                        mov eax, dword ptr [rdi + 0x64]
00A1F3B9  85 C0                           test eax, eax
00A1F3BB  0F 85 A9 04 00 00               jne 0x140a1f86a
00A1F3C1  48 8D 47 30                     lea rax, [rdi + 0x30]
00A1F3C5  48 8B 10                        mov rdx, qword ptr [rax]
00A1F3C8  48 3B D0                        cmp rdx, rax
00A1F3CB  74 1A                           je 0x140a1f3e7
00A1F3CD  48 8D 8A 58 FF FF FF            lea rcx, [rdx - 0xa8]
00A1F3D4  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
00A1F3DC  48 8B 81 B8 00 00 00            mov rax, qword ptr [rcx + 0xb8]
00A1F3E3  44 8B 78 08                     mov r15d, dword ptr [rax + 8]
00A1F3E7  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
00A1F3EC  8B 47 74                        mov eax, dword ptr [rdi + 0x74]
00A1F3EF  83 F8 03                        cmp eax, 3
00A1F3F2  0F 85 BE 03 00 00               jne 0x140a1f7b6
00A1F3F8  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00A1F3FD  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
00A1F405  0F B7 00                        movzx eax, word ptr [rax]
00A1F408  44 03 F0                        add r14d, eax
00A1F40B  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00A1F410  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
00A1F418  48 85 C0                        test rax, rax
00A1F41B  0F 85 94 04 00 00               jne 0x140a1f8b5
00A1F421  44 8B 6F 68                     mov r13d, dword ptr [rdi + 0x68]
00A1F425  41 83 C5 03                     add r13d, 3
00A1F429  41 83 E5 FC                     and r13d, 0xfffffffc
00A1F42D  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
00A1F432  43 8D 04 2E                     lea eax, [r14 + r13]
00A1F436  41 3B C5                        cmp eax, r13d
00A1F439  72 52                           jb 0x140a1f48d
00A1F43B  8B D6                           mov edx, esi
00A1F43D  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
00A1F441  45 3B F7                        cmp r14d, r15d
00A1F444  76 60                           jbe 0x140a1f4a6
00A1F446  0F B7 47 48                     movzx eax, word ptr [rdi + 0x48]
00A1F44A  41 BD 02 00 00 00               mov r13d, 2
00A1F450  66 41 0B C5                     or ax, r13w
00A1F454  66 89 47 48                     mov word ptr [rdi + 0x48], ax
00A1F458  45 8D 75 52                     lea r14d, [r13 + 0x52]
00A1F45C  44 84 6F 48                     test byte ptr [rdi + 0x48], r13b
00A1F460  0F 85 0C 04 00 00               jne 0x140a1f872
00A1F466  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00A1F46E  0F B7 41 48                     movzx eax, word ptr [rcx + 0x48]
00A1F472  83 BC 24 08 01 00 00 04         cmp dword ptr [rsp + 0x108], 4
00A1F47A  0F 85 9A 02 00 00               jne 0x140a1f71a
00A1F480  66 83 C8 08                     or ax, 8
00A1F484  66 89 41 48                     mov word ptr [rcx + 0x48], ax
00A1F488  E9 DB FE FF FF                  jmp 0x140a1f368
00A1F48D  83 C8 FF                        or eax, 0xffffffff
00A1F490  BA 95 00 00 C0                  mov edx, 0xc0000095
00A1F495  EB A6                           jmp 0x140a1f43d
00A1F497  F6 47 48 01                     test byte ptr [rdi + 0x48], 1
00A1F49B  0F 84 C7 FE FF FF               je 0x140a1f368
00A1F4A1  E9 1D 02 00 00                  jmp 0x140a1f6c3
00A1F4A6  85 D2                           test edx, edx
00A1F4A8  75 9C                           jne 0x140a1f446
00A1F4AA  41 3B C7                        cmp eax, r15d
00A1F4AD  77 97                           ja 0x140a1f446
00A1F4AF  48 8B DE                        mov rbx, rsi
00A1F4B2  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00A1F4B7  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
00A1F4BB  48 85 C0                        test rax, rax
00A1F4BE  0F 85 2E 02 00 00               jne 0x140a1f6f2
00A1F4C4  48 85 C9                        test rcx, rcx
00A1F4C7  74 1A                           je 0x140a1f4e3
00A1F4C9  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00A1F4CD  48 85 C0                        test rax, rax
00A1F4D0  0F 85 F2 03 00 00               jne 0x140a1f8c8
00A1F4D6  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00A1F4DA  48 85 C9                        test rcx, rcx
00A1F4DD  0F 85 F3 03 00 00               jne 0x140a1f8d6
00A1F4E3  48 39 77 58                     cmp qword ptr [rdi + 0x58], rsi
00A1F4E7  0F 84 DF 02 00 00               je 0x140a1f7cc
00A1F4ED  41 BF 02 00 00 00               mov r15d, 2
00A1F4F3  48 85 DB                        test rbx, rbx
00A1F4F6  0F 84 86 01 00 00               je 0x140a1f682
00A1F4FC  8B 4F 68                        mov ecx, dword ptr [rdi + 0x68]
00A1F4FF  44 3B E9                        cmp r13d, ecx
00A1F502  0F 87 C0 00 00 00               ja 0x140a1f5c8
00A1F508  89 33                           mov dword ptr [rbx], esi
00A1F50A  8B 84 24 08 01 00 00            mov eax, dword ptr [rsp + 0x108]
00A1F511  89 43 04                        mov dword ptr [rbx + 4], eax
00A1F514  8B 47 74                        mov eax, dword ptr [rdi + 0x74]
00A1F517  83 F8 03                        cmp eax, 3
00A1F51A  0F 85 BE 00 00 00               jne 0x140a1f5de
00A1F520  4C 8B BC 24 28 01 00 00         mov r15, qword ptr [rsp + 0x128]
00A1F528  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00A1F52C  48 89 43 08                     mov qword ptr [rbx + 8], rax
00A1F530  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
00A1F534  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00A1F538  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00A1F53C  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00A1F540  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
00A1F544  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
00A1F548  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00A1F54C  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
00A1F550  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
00A1F554  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
00A1F558  41 8B 47 38                     mov eax, dword ptr [r15 + 0x38]
00A1F55C  89 43 38                        mov dword ptr [rbx + 0x38], eax
00A1F55F  41 8B 47 3C                     mov eax, dword ptr [r15 + 0x3c]
00A1F563  89 43 3C                        mov dword ptr [rbx + 0x3c], eax
00A1F566  49 8B 47 40                     mov rax, qword ptr [r15 + 0x40]
00A1F56A  48 89 43 40                     mov qword ptr [rbx + 0x40], rax
00A1F56E  49 8B 47 48                     mov rax, qword ptr [r15 + 0x48]
00A1F572  48 89 43 48                     mov qword ptr [rbx + 0x48], rax
00A1F576  41 8D 46 AC                     lea eax, [r14 - 0x54]
00A1F57A  66 89 43 50                     mov word ptr [rbx + 0x50], ax
00A1F57E  41 8A 47 50                     mov al, byte ptr [r15 + 0x50]
00A1F582  88 43 52                        mov byte ptr [rbx + 0x52], al
00A1F585  40 88 73 53                     mov byte ptr [rbx + 0x53], sil
00A1F589  48 83 C3 54                     add rbx, 0x54
00A1F58D  41 BF 02 00 00 00               mov r15d, 2
00A1F593  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
00A1F59B  44 0F B7 00                     movzx r8d, word ptr [rax]
00A1F59F  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00A1F5A3  48 8B CB                        mov rcx, rbx
00A1F5A6  E8 95 72 CA FF                  call 0x1406c6840
00A1F5AB  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
00A1F5B3  48 85 C9                        test rcx, rcx
00A1F5B6  0F 85 98 00 00 00               jne 0x140a1f654
00A1F5BC  43 8D 04 2E                     lea eax, [r14 + r13]
00A1F5C0  89 47 68                        mov dword ptr [rdi + 0x68], eax
00A1F5C3  E9 BA 00 00 00                  jmp 0x140a1f682
00A1F5C8  45 8B C5                        mov r8d, r13d
00A1F5CB  44 2B C1                        sub r8d, ecx
00A1F5CE  48 03 4F 58                     add rcx, qword ptr [rdi + 0x58]
00A1F5D2  33 D2                           xor edx, edx
00A1F5D4  E8 67 76 CA FF                  call 0x1406c6c40
00A1F5D9  E9 2A FF FF FF                  jmp 0x140a1f508
00A1F5DE  41 3B C7                        cmp eax, r15d
00A1F5E1  74 0D                           je 0x140a1f5f0
00A1F5E3  41 8D 46 F4                     lea eax, [r14 - 0xc]
00A1F5E7  89 43 08                        mov dword ptr [rbx + 8], eax
00A1F5EA  48 83 C3 0C                     add rbx, 0xc
00A1F5EE  EB A3                           jmp 0x140a1f593
00A1F5F0  48 8B 8C 24 28 01 00 00         mov rcx, qword ptr [rsp + 0x128]
00A1F5F8  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00A1F5FC  48 89 43 08                     mov qword ptr [rbx + 8], rax
00A1F600  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00A1F604  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00A1F608  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00A1F60C  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00A1F610  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
00A1F614  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
00A1F618  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00A1F61C  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
00A1F620  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
00A1F624  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
00A1F628  8B 41 38                        mov eax, dword ptr [rcx + 0x38]
00A1F62B  89 43 38                        mov dword ptr [rbx + 0x38], eax
00A1F62E  8B 41 3C                        mov eax, dword ptr [rcx + 0x3c]
00A1F631  89 43 3C                        mov dword ptr [rbx + 0x3c], eax
00A1F634  48 8B 41 40                     mov rax, qword ptr [rcx + 0x40]
00A1F638  48 89 43 40                     mov qword ptr [rbx + 0x40], rax
00A1F63C  48 8B 41 48                     mov rax, qword ptr [rcx + 0x48]
00A1F640  48 89 43 48                     mov qword ptr [rbx + 0x48], rax
00A1F644  41 8D 46 AC                     lea eax, [r14 - 0x54]
00A1F648  89 43 50                        mov dword ptr [rbx + 0x50], eax
00A1F64B  48 83 C3 54                     add rbx, 0x54
00A1F64F  E9 3F FF FF FF                  jmp 0x140a1f593
00A1F654  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
00A1F65C  0F B7 00                        movzx eax, word ptr [rax]
00A1F65F  48 03 D8                        add rbx, rax
00A1F662  B8 3A 00 00 00                  mov eax, 0x3a
00A1F667  66 89 03                        mov word ptr [rbx], ax
00A1F66A  49 03 DF                        add rbx, r15
00A1F66D  44 0F B7 01                     movzx r8d, word ptr [rcx]
00A1F671  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00A1F675  48 8B CB                        mov rcx, rbx
00A1F678  E8 C3 71 CA FF                  call 0x1406c6840
00A1F67D  E9 3A FF FF FF                  jmp 0x140a1f5bc
00A1F682  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
00A1F687  41 BD 02 00 00 00               mov r13d, 2
00A1F68D  45 8D 75 52                     lea r14d, [r13 + 0x52]
00A1F691  E9 C6 FD FF FF                  jmp 0x140a1f45c
00A1F696  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00A1F69B  0F B7 47 48                     movzx eax, word ptr [rdi + 0x48]
00A1F69F  66 83 C8 02                     or ax, 2
00A1F6A3  66 89 47 48                     mov word ptr [rdi + 0x48], ax
00A1F6A7  33 F6                           xor esi, esi
00A1F6A9  44 8D 6E 02                     lea r13d, [rsi + 2]
00A1F6AD  44 8D 76 54                     lea r14d, [rsi + 0x54]
00A1F6B1  4C 8B A4 24 E0 00 00 00         mov r12, qword ptr [rsp + 0xe0]
00A1F6B9  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00A1F6BE  E9 99 FD FF FF                  jmp 0x140a1f45c
00A1F6C3  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00A1F6C7  48 85 C0                        test rax, rax
00A1F6CA  0F 84 B3 FC FF FF               je 0x140a1f383
00A1F6D0  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
00A1F6D4  48 8B 94 24 10 01 00 00         mov rdx, qword ptr [rsp + 0x110]
00A1F6DC  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00A1F6E0  E8 EB B3 C9 FF                  call 0x1406baad0
00A1F6E5  84 C0                           test al, al
00A1F6E7  0F 84 7B FC FF FF               je 0x140a1f368
00A1F6ED  E9 91 FC FF FF                  jmp 0x140a1f383
00A1F6F2  8B 4F 6C                        mov ecx, dword ptr [rdi + 0x6c]
00A1F6F5  48 8D 14 08                     lea rdx, [rax + rcx]
00A1F6F9  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00A1F6FE  41 8B C5                        mov eax, r13d
00A1F701  2B C1                           sub eax, ecx
00A1F703  89 02                           mov dword ptr [rdx], eax
00A1F705  44 89 6F 6C                     mov dword ptr [rdi + 0x6c], r13d
00A1F709  41 8B DD                        mov ebx, r13d
00A1F70C  48 03 5F 58                     add rbx, qword ptr [rdi + 0x58]
00A1F710  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00A1F715  E9 C9 FD FF FF                  jmp 0x140a1f4e3
00A1F71A  BA F7 FF 00 00                  mov edx, 0xfff7
00A1F71F  66 23 C2                        and ax, dx
00A1F722  66 89 41 48                     mov word ptr [rcx + 0x48], ax
00A1F726  4C 8D 4F 30                     lea r9, [rdi + 0x30]
00A1F72A  49 8B 11                        mov rdx, qword ptr [r9]
00A1F72D  49 3B D1                        cmp rdx, r9
00A1F730  0F 84 52 FD FF FF               je 0x140a1f488
00A1F736  44 8B 47 68                     mov r8d, dword ptr [rdi + 0x68]
00A1F73A  0F B7 47 48                     movzx eax, word ptr [rdi + 0x48]
00A1F73E  B9 FD FF 00 00                  mov ecx, 0xfffd
00A1F743  66 23 C1                        and ax, cx
00A1F746  66 89 47 48                     mov word ptr [rdi + 0x48], ax
00A1F74A  48 83 67 68 00                  and qword ptr [rdi + 0x68], 0
00A1F74F  48 8D 8A 58 FF FF FF            lea rcx, [rdx - 0xa8]
00A1F756  48 8B 02                        mov rax, qword ptr [rdx]
00A1F759  4C 39 4A 08                     cmp qword ptr [rdx + 8], r9
00A1F75D  0F 85 4B 01 00 00               jne 0x140a1f8ae
00A1F763  48 39 50 08                     cmp qword ptr [rax + 8], rdx
00A1F767  0F 85 41 01 00 00               jne 0x140a1f8ae
00A1F76D  49 89 01                        mov qword ptr [r9], rax
00A1F770  4C 89 48 08                     mov qword ptr [rax + 8], r9
00A1F774  48 89 32                        mov qword ptr [rdx], rsi
00A1F777  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00A1F77F  45 33 C9                        xor r9d, r9d
00A1F782  48 8B D7                        mov rdx, rdi
00A1F785  E8 9E 02 00 00                  call 0x140a1fa28
00A1F78A  E9 F9 FC FF FF                  jmp 0x140a1f488
00A1F78F  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
00A1F797  48 85 D2                        test rdx, rdx
00A1F79A  0F 84 F0 FB FF FF               je 0x140a1f390
00A1F7A0  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00A1F7A4  E8 27 B3 C9 FF                  call 0x1406baad0
00A1F7A9  84 C0                           test al, al
00A1F7AB  0F 84 B7 FB FF FF               je 0x140a1f368
00A1F7B1  E9 DA FB FF FF                  jmp 0x140a1f390
00A1F7B6  41 BE 0C 00 00 00               mov r14d, 0xc
00A1F7BC  41 3B C5                        cmp eax, r13d
00A1F7BF  41 8D 46 48                     lea eax, [r14 + 0x48]
00A1F7C3  44 0F 44 F0                     cmove r14d, eax
00A1F7C7  E9 2C FC FF FF                  jmp 0x140a1f3f8
00A1F7CC  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
00A1F7D1  45 8B C7                        mov r8d, r15d
00A1F7D4  BA 01 00 00 00                  mov edx, 1
00A1F7D9  48 8B 4F 78                     mov rcx, qword ptr [rdi + 0x78]
00A1F7DD  E8 0E D0 9C FF                  call 0x1403ec7f0
00A1F7E2  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00A1F7E7  41 B8 46 53 72 4E               mov r8d, 0x4e725346
00A1F7ED  41 8B D7                        mov edx, r15d
00A1F7F0  B9 22 01 00 00                  mov ecx, 0x122
00A1F7F5  E8 F6 28 16 00                  call 0x140b820f0
00A1F7FA  48 8B D8                        mov rbx, rax
00A1F7FD  48 89 47 58                     mov qword ptr [rdi + 0x58], rax
00A1F801  48 89 47 50                     mov qword ptr [rdi + 0x50], rax
00A1F805  44 89 7F 64                     mov dword ptr [rdi + 0x64], r15d
00A1F809  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A1F80E  41 BF 02 00 00 00               mov r15d, 2
00A1F814  E9 DA FC FF FF                  jmp 0x140a1f4f3
00A1F819  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00A1F81E  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
00A1F823  74 0D                           je 0x140a1f832
00A1F825  8B 54 24 34                     mov edx, dword ptr [rsp + 0x34]
00A1F829  48 8B 4F 78                     mov rcx, qword ptr [rdi + 0x78]
00A1F82D  E8 2E 70 88 FF                  call 0x1402a6860
00A1F832  0F B7 47 48                     movzx eax, word ptr [rdi + 0x48]
00A1F836  66 83 C8 02                     or ax, 2
00A1F83A  66 89 47 48                     mov word ptr [rdi + 0x48], ax
00A1F83E  33 F6                           xor esi, esi
00A1F840  44 8D 7E 02                     lea r15d, [rsi + 2]
00A1F844  4C 8B A4 24 E0 00 00 00         mov r12, qword ptr [rsp + 0xe0]
00A1F84C  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A1F851  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A1F856  44 8B 74 24 38                  mov r14d, dword ptr [rsp + 0x38]
00A1F85B  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
00A1F860  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00A1F865  E9 89 FC FF FF                  jmp 0x140a1f4f3
00A1F86A  44 8B F8                        mov r15d, eax
00A1F86D  E9 75 FB FF FF                  jmp 0x140a1f3e7
00A1F872  48 39 77 58                     cmp qword ptr [rdi + 0x58], rsi
00A1F876  0F 84 EA FB FF FF               je 0x140a1f466
00A1F87C  48 39 77 50                     cmp qword ptr [rdi + 0x50], rsi
00A1F880  74 17                           je 0x140a1f899
00A1F882  8B 57 64                        mov edx, dword ptr [rdi + 0x64]
00A1F885  48 8B 4F 78                     mov rcx, qword ptr [rdi + 0x78]
00A1F889  E8 D2 6F 88 FF                  call 0x1402a6860
00A1F88E  33 D2                           xor edx, edx
00A1F890  48 8B 4F 50                     mov rcx, qword ptr [rdi + 0x50]
00A1F894  E8 D7 2F 16 00                  call 0x140b82870
00A1F899  48 89 77 58                     mov qword ptr [rdi + 0x58], rsi
00A1F89D  48 89 77 50                     mov qword ptr [rdi + 0x50], rsi
00A1F8A1  48 83 67 68 00                  and qword ptr [rdi + 0x68], 0
00A1F8A6  89 77 64                        mov dword ptr [rdi + 0x64], esi
00A1F8A9  E9 B8 FB FF FF                  jmp 0x140a1f466
00A1F8AE  B9 03 00 00 00                  mov ecx, 3
00A1F8B3  CD 29                           int 0x29
00A1F8B5  0F B7 00                        movzx eax, word ptr [rax]
00A1F8B8  83 C0 02                        add eax, 2
00A1F8BB  44 03 F0                        add r14d, eax
00A1F8BE  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00A1F8C3  E9 59 FB FF FF                  jmp 0x140a1f421
00A1F8C8  48 8B D8                        mov rbx, rax
00A1F8CB  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A1F8D0  48 89 47 58                     mov qword ptr [rdi + 0x58], rax
00A1F8D4  EB 37                           jmp 0x140a1f90d
00A1F8D6  F6 41 0A 05                     test byte ptr [rcx + 0xa], 5
00A1F8DA  74 0B                           je 0x140a1f8e7
00A1F8DC  48 8B 59 18                     mov rbx, qword ptr [rcx + 0x18]
00A1F8E0  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00A1F8E5  EB 22                           jmp 0x140a1f909
00A1F8E7  C7 44 24 28 10 00 00 40         mov dword ptr [rsp + 0x28], 0x40000010
00A1F8EF  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00A1F8F3  45 33 C9                        xor r9d, r9d
00A1F8F6  33 D2                           xor edx, edx
00A1F8F8  45 8D 41 01                     lea r8d, [r9 + 1]
00A1F8FC  E8 FF 8E 8F FF                  call 0x140318800
00A1F901  48 8B D8                        mov rbx, rax
00A1F904  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A1F909  48 89 5F 58                     mov qword ptr [rdi + 0x58], rbx
00A1F90D  44 89 7F 64                     mov dword ptr [rdi + 0x64], r15d
00A1F911  E9 CD FB FF FF                  jmp 0x140a1f4e3
00A1F916  49 8B 04 24                     mov rax, qword ptr [r12]
00A1F91A  FF 48 40                        dec dword ptr [rax + 0x40]
00A1F91D  49 8B 04 24                     mov rax, qword ptr [r12]
00A1F921  39 70 40                        cmp dword ptr [rax + 0x40], esi
00A1F924  75 0D                           jne 0x140a1f933
00A1F926  48 89 70 38                     mov qword ptr [rax + 0x38], rsi
00A1F92A  49 8B 0C 24                     mov rcx, qword ptr [r12]
00A1F92E  E8 6D 0A 83 FF                  call 0x1402503a0
00A1F933  48 81 C4 A0 00 00 00            add rsp, 0xa0
00A1F93A  41 5F                           pop r15
00A1F93C  41 5E                           pop r14
00A1F93E  41 5D                           pop r13
00A1F940  41 5C                           pop r12
00A1F942  5F                              pop rdi
00A1F943  5E                              pop rsi
00A1F944  5B                              pop rbx
00A1F945  C3                              ret
00A1F946  CC                              int3
00A1F947  83 38 58                        cmp dword ptr [rax], 0x58
00A1F94A  0F 83 AB F9 FF FF               jae 0x140a1f2fb
00A1F950  EB E1                           jmp 0x140a1f933
00A1F952  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00A1F957  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00A1F95C  E8 7F C4 05 00                  call 0x140a7bde0
00A1F961  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A1F966  33 C0                           xor eax, eax
00A1F968  F0 49 0F B1 0C 24               lock cmpxchg qword ptr [r12], rcx
00A1F96E  0F 84 90 F9 FF FF               je 0x140a1f304
00A1F974  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00A1F979  E8 92 AA 06 00                  call 0x140a8a410
00A1F97E  E9 81 F9 FF FF                  jmp 0x140a1f304
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlNotifyFilterReportChangeLiteEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8, unsigned __int8 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int8 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    v_rsi = 0;
    v_stack_m90 = 0;
    if ((*(unsigned __int64 *)(a2)) == a2) goto loc_00A1F933;
    if (a10 != 0) goto loc_00A1F947;
loc_00A1F2FB:
    if ((*(unsigned __int64 *)(a1)) == 0) goto loc_00A1F952;
loc_00A1F304:
    result = a10;
    if ((*(unsigned __int64 *)(gs_base + (0 + 392))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56))) {
        result = ExAcquireFastMutexUnsafe(*(unsigned __int64 *)(a1), a2, a3, a4);
        result = *(unsigned __int64 *)(a1);
        *(unsigned __int64 *)(result + 56) = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
loc_00A1F338:
    v_stack_m68 = *(unsigned __int64 *)(a2);
    v_stack_m70 = *(unsigned __int64 *)(a2);
    if ((*(unsigned __int64 *)(a2)) == a2) goto loc_00A1F916;
    v_stack_m78 = *(unsigned __int64 *)(a2) - 32;
    v_stack_m50 = *(unsigned __int64 *)(a2) - 32;
    if (((v_stack_p28) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) - 32 + 76))))) != 0) goto loc_00A1F375;
loc_00A1F368:
    goto loc_00A1F338;
loc_00A1F375:
    if (((a9) & (1)) == 0) goto loc_00A1F497;
loc_00A1F383:
    if (*(unsigned __int64 *)(v_stack_p10 + 64) != 0) goto loc_00A1F78F;
loc_00A1F390:
    if (((*(unsigned __int8 *)(v_stack_p10 + 72)) & (2)) != 0) goto loc_00A1F466;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 96))) == 0) goto loc_00A1F466;
    v_stack_mA4 = 0;
    v_stack_m58 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 100))) != 0) goto loc_00A1F86A;
    result = v_stack_p10 + 48;
    v_r15 = (unsigned int)(*(unsigned int *)(v_stack_p10 + 96));
    if ((*(unsigned __int64 *)(v_stack_p10 + 48)) != (v_stack_p10 + 48)) {
        a1 = *(unsigned __int64 *)(v_stack_p10 + 48) - 168;
        v_stack_m58 = a1;
        result = *(unsigned __int64 *)(a1 + 184);
        v_r15 = *(unsigned int *)(result + 8);
    }
    v_stack_mA4 = (unsigned int)(v_r15);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 116)))) != 3) goto loc_00A1F7B6;
loc_00A1F3F8:
    v_stack_mA0 = (unsigned int)(2 + 82);
    v_r14 = (unsigned int)((2 + 82) + ((unsigned int)(*(unsigned __int16 *)(v_stack_p18))));
    v_stack_mA0 = (unsigned int)(v_r14);
    if (v_stack_p20 != 0) goto loc_00A1F8B5;
loc_00A1F421:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 104))) + (3));
    v_r13 = (unsigned int)((v_r13) & (0xFFFFFFFCULL));
    v_stack_m88 = (unsigned int)(v_r13);
    if (((unsigned int)(v_r14 + v_r13 * 1)) < ((unsigned int)(v_r13))) goto loc_00A1F48D;
loc_00A1F43D:
    v_stack_m8C = (unsigned int)(v_r14 + v_r13 * 1);
    if (((unsigned int)(v_r14)) <= ((unsigned int)(v_r15))) goto loc_00A1F4A6;
loc_00A1F446:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p10 + 72)) | (2));
    *(unsigned __int16 *)(v_stack_p10 + 72) = (unsigned __int16)(result);
loc_00A1F45C:
    if (((*(unsigned __int8 *)(v_stack_p10 + 72)) & (2)) != 0) goto loc_00A1F872;
loc_00A1F466:
    if (a6 != 4) goto loc_00A1F71A;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m50 + 72)) | (8));
    *(unsigned __int16 *)(v_stack_m50 + 72) = (unsigned __int16)(result);
loc_00A1F488:
    goto loc_00A1F368;
loc_00A1F48D:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    goto loc_00A1F43D;
loc_00A1F497:
    if (((*(unsigned __int8 *)(v_stack_p10 + 72)) & (1)) == 0) goto loc_00A1F368;
    goto loc_00A1F6C3;
loc_00A1F4A6:
    if ((unsigned int)((unsigned int)(0xC0000095ULL)) != 0) goto loc_00A1F446;
    if (((unsigned int)(result)) > ((unsigned int)(v_r15))) goto loc_00A1F446;
    v_stack_m98 = 0;
    if (*(unsigned __int64 *)(v_stack_p10 + 88) != 0) goto loc_00A1F6F2;
    if (v_stack_m50 == 0) goto loc_00A1F4E3;
    if (*(unsigned __int64 *)(v_stack_m50 + 24) != 0) goto loc_00A1F8C8;
    if (*(unsigned __int64 *)(v_stack_m50 + 8) != 0) goto loc_00A1F8D6;
loc_00A1F4E3:
    if ((*(unsigned __int64 *)(v_stack_p10 + 88)) == 0) goto loc_00A1F7CC;
loc_00A1F4F3:
    if (0 == 0) goto loc_00A1F682;
    if (2 > ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 104))))) goto loc_00A1F5C8;
loc_00A1F508:
    *(unsigned int *)(0) = 0;
    *(unsigned int *)(0 + 4) = (unsigned int)((unsigned int)(a6));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 116)))) != 3) goto loc_00A1F5DE;
    *(unsigned __int64 *)(0 + 8) = *(unsigned __int64 *)(a10 + 8);
    *(unsigned __int64 *)(0 + 16) = *(unsigned __int64 *)(a10 + 16);
    *(unsigned __int64 *)(0 + 24) = *(unsigned __int64 *)(a10 + 24);
    *(unsigned __int64 *)(0 + 32) = *(unsigned __int64 *)(a10 + 32);
    *(unsigned __int64 *)(0 + 40) = *(unsigned __int64 *)(a10 + 40);
    *(unsigned __int64 *)(0 + 48) = *(unsigned __int64 *)(a10 + 48);
    *(unsigned int *)(0 + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(a10 + 56)));
    *(unsigned int *)(0 + 60) = (unsigned int)((unsigned int)(*(unsigned int *)(a10 + 60)));
    *(unsigned __int64 *)(0 + 64) = *(unsigned __int64 *)(a10 + 64);
    *(unsigned __int64 *)(0 + 72) = *(unsigned __int64 *)(a10 + 72);
    *(unsigned __int16 *)(0 + 80) = (unsigned __int16)(2 + 82 - 84);
    *(unsigned __int8 *)(0 + 82) = (unsigned __int8)(*(unsigned __int8 *)(a10 + 80));
    *(unsigned __int8 *)(0 + 83) = 0;
    v_rbx = (0) + (84);
loc_00A1F593:
    result = memcpy(v_rbx, *(unsigned __int64 *)(v_stack_p18 + 8), *(unsigned __int16 *)(v_stack_p18), a4);
    if (v_stack_p20 != 0) goto loc_00A1F654;
loc_00A1F5BC:
    *(unsigned int *)(v_stack_p10 + 104) = (unsigned int)(2 + 82 + 2 * 1);
    goto loc_00A1F682;
loc_00A1F5C8:
    a3 = (unsigned int)((2) - ((unsigned int)(v_stack_p20)));
    a1 = (v_stack_p20) + (*(unsigned __int64 *)(v_stack_p10 + 88));
    a2 = 0;
    result = memset(a1, a2, a3, a4);
    goto loc_00A1F508;
loc_00A1F5DE:
    if (((unsigned int)(result)) == 2) goto loc_00A1F5F0;
    *(unsigned int *)(v_rbx + 8) = (unsigned int)(2 + 82 - 12);
    v_rbx = (v_rbx) + (12);
    goto loc_00A1F593;
loc_00A1F5F0:
    *(unsigned __int64 *)(v_rbx + 8) = *(unsigned __int64 *)(a10 + 8);
    *(unsigned __int64 *)(v_rbx + 16) = *(unsigned __int64 *)(a10 + 16);
    *(unsigned __int64 *)(v_rbx + 24) = *(unsigned __int64 *)(a10 + 24);
    *(unsigned __int64 *)(v_rbx + 32) = *(unsigned __int64 *)(a10 + 32);
    *(unsigned __int64 *)(v_rbx + 40) = *(unsigned __int64 *)(a10 + 40);
    *(unsigned __int64 *)(v_rbx + 48) = *(unsigned __int64 *)(a10 + 48);
    *(unsigned int *)(v_rbx + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(a10 + 56)));
    *(unsigned int *)(v_rbx + 60) = (unsigned int)((unsigned int)(*(unsigned int *)(a10 + 60)));
    *(unsigned __int64 *)(v_rbx + 64) = *(unsigned __int64 *)(a10 + 64);
    *(unsigned __int64 *)(v_rbx + 72) = *(unsigned __int64 *)(a10 + 72);
    *(unsigned int *)(v_rbx + 80) = (unsigned int)(2 + 82 - 84);
    v_rbx = (v_rbx) + (84);
    goto loc_00A1F593;
loc_00A1F654:
    v_rbx = (v_rbx) + (*(unsigned __int16 *)(v_stack_p18));
    *(unsigned __int16 *)(v_rbx) = 58;
    v_rbx = (v_rbx) + (2);
    result = memcpy(v_rbx, *(unsigned __int64 *)(a10 + 8), *(unsigned __int16 *)(a10), a4);
    goto loc_00A1F5BC;
loc_00A1F682:
    goto loc_00A1F45C;
loc_00A1F6C3:
    if (*(unsigned __int64 *)(v_stack_p10 + 16) == 0) goto loc_00A1F383;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_p10 + 8), a7, *(unsigned __int64 *)(v_stack_p10 + 24), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A1F368;
    goto loc_00A1F383;
loc_00A1F6F2:
    v_stack_m98 = result + (unsigned int)(*(unsigned int *)(v_stack_p10 + 108)) * 1;
    result = (unsigned int)((2) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 108)))));
    *(unsigned int *)(result + (unsigned int)(*(unsigned int *)(v_stack_p10 + 108)) * 1) = (unsigned int)(result);
    *(unsigned int *)(v_stack_p10 + 108) = 2;
    v_rbx = (2) + (*(unsigned __int64 *)(v_stack_p10 + 88));
    v_stack_m98 = v_rbx;
    goto loc_00A1F4E3;
loc_00A1F71A:
    result = (unsigned __int16)((result) & ((unsigned __int16)((unsigned int)(0xFFF7ULL))));
    *(unsigned __int16 *)((unsigned int)(*(unsigned int *)(v_stack_p10 + 108)) + 72) = (unsigned __int16)(result);
    if ((*(unsigned __int64 *)(v_stack_p10 + 48)) == (v_stack_p10 + 48)) goto loc_00A1F488;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p10 + 72)) & ((unsigned __int16)((unsigned int)(0xFFFDULL))));
    *(unsigned __int16 *)(v_stack_p10 + 72) = (unsigned __int16)(result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 48) + 8)) != (v_stack_p10 + 48)) goto loc_00A1F8AE;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 48)) + 8)) != (*(unsigned __int64 *)(v_stack_p10 + 48))) goto loc_00A1F8AE;
    *(unsigned __int64 *)(v_stack_p10 + 48) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 48));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 48)) + 8) = v_stack_p10 + 48;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 48)) = 0;
    v_stack_mB8 = 1;
    a4 = 0;
    result = FsRtlNotifyCompleteIrp(*(unsigned __int64 *)(v_stack_p10 + 48) - 168, v_stack_p10, (unsigned int)(*(unsigned int *)(v_stack_p10 + 104)), a4);
    goto loc_00A1F488;
loc_00A1F78F:
    if (a8 == 0) goto loc_00A1F390;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_p10 + 8), a8, (unsigned int)(*(unsigned int *)(v_stack_p10 + 104)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A1F368;
    goto loc_00A1F390;
loc_00A1F7B6:
    v_r14 = 12;
    if (((unsigned int)(result)) == 2) { v_r14 = (unsigned int)(12 + 72); }
    goto loc_00A1F3F8;
loc_00A1F7CC:
    v_stack_mA8 = 0;
    result = PsChargePoolQuota(*(unsigned __int64 *)(v_stack_p10 + 120), 1, 2, a4);
    v_stack_mA8 = 1;
    result = ExAllocatePool2(290, 2, (unsigned int)(0x4E725346ULL), a4);
    *(unsigned __int64 *)(v_stack_p10 + 88) = result;
    *(unsigned __int64 *)(v_stack_p10 + 80) = result;
    *(unsigned int *)(v_stack_p10 + 100) = 2;
    v_stack_m98 = result;
    goto loc_00A1F4F3;
loc_00A1F86A:
    goto loc_00A1F3E7;
loc_00A1F872:
    if ((*(unsigned __int64 *)(v_stack_p10 + 88)) == 0) goto loc_00A1F466;
    if ((*(unsigned __int64 *)(v_stack_p10 + 80)) != 0) {
        a2 = *(unsigned int *)(v_stack_p10 + 100);
        a1 = *(unsigned __int64 *)(v_stack_p10 + 120);
        result = PsReturnProcessPagedPoolQuota(a1, a2, (unsigned int)(0x4E725346ULL), a4);
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_stack_p10 + 80);
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x4E725346ULL), a4);
    }
    *(unsigned __int64 *)(v_stack_p10 + 88) = 0;
    *(unsigned __int64 *)(v_stack_p10 + 80) = 0;
    *(unsigned int *)(v_stack_p10 + 100) = 0;
    goto loc_00A1F466;
loc_00A1F8AE:
loc_00A1F8B5:
    result = (unsigned int)((*(unsigned __int16 *)(result)) + (2));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
    v_stack_mA0 = (unsigned int)(v_r14);
    goto loc_00A1F421;
loc_00A1F8C8:
    v_stack_m98 = result;
    *(unsigned __int64 *)(v_stack_p10 + 88) = result;
    goto loc_00A1F90D;
loc_00A1F8D6:
    if (((*(unsigned __int8 *)(3 + 10)) & (5)) == 0) goto loc_00A1F8E7;
    v_stack_m98 = *(unsigned __int64 *)(3 + 24);
    goto loc_00A1F909;
loc_00A1F8E7:
    v_stack_mB0 = 0x40000010ULL;
    v_stack_mB8 = 0;
    a4 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(3, a2, a4 + 1, a4);
    v_stack_m98 = result;
loc_00A1F909:
    *(unsigned __int64 *)(v_stack_p10 + 88) = result;
loc_00A1F90D:
    *(unsigned int *)(v_stack_p10 + 100) = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_00A1F4E3;
loc_00A1F916:
    result = *(unsigned __int64 *)(a1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 64)) == 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) = 0;
        a1 = *(unsigned __int64 *)(a1);
        result = ExReleaseFastMutexUnsafe(a1, a2, a4 + 1, a4);
    }
    v_rsp = (v_rsp) + (160);
    return result;
loc_00A1F947:
    if ((*(unsigned int *)(result)) >= 88) goto loc_00A1F2FB;
    goto loc_00A1F933;
loc_00A1F952:
    v_stack_p58 = 0;
    result = FsRtlNotifyInitializeSync(v_stack_p58, a2, a4 + 1, a4);
    result = 0;
    if (condition_is_equal) goto loc_00A1F304;
    result = FsRtlNotifyUninitializeSync(v_stack_p58, a2, a4 + 1, a4);
    goto loc_00A1F304;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlNotifyFilterReportChangeLiteEx(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8, uint8_t Arg9, void *Arg10)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg10 = (uint8_t *)Arg10;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint8_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p58;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    local_rsi = 0;
    v_stack_m90 = 0;
    if ((*(uint64_t *)(arg2)) == Arg2) goto loc_00A1F933;
    if (Arg10 != NULL) goto loc_00A1F947;
loc_00A1F2FB:
    if ((*(uint64_t *)(arg1)) == 0) goto loc_00A1F952;
loc_00A1F304:
    result = Arg10;
    if ((*(uint64_t *)(gs_base + (0 + 0x188))) != (*(uint64_t *)(*(uint64_t *)(arg1) + 0x38))) {
        result = ExAcquireFastMutexUnsafe(*(uint64_t *)(arg1), Arg2, Arg3, Arg4);
        result = *(uint64_t *)(arg1);
        *(uint64_t *)(result + 0x38) = *(uint64_t *)(gs_base + (0 + 0x188));
    }
loc_00A1F338:
    v_stack_m68 = *(uint64_t *)(arg2);
    v_stack_m70 = *(uint64_t *)(arg2);
    if ((*(uint64_t *)(arg2)) == Arg2) goto loc_00A1F916;
    v_stack_m78 = *(uint64_t *)(arg2) - 32;
    v_stack_m50 = *(uint64_t *)(arg2) - 32;
    if (((v_stack_p28) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) - 0x20 + 0x4C))))) != 0) goto loc_00A1F375;
loc_00A1F368:
    goto loc_00A1F338;
loc_00A1F375:
    if (((Arg9) & (1)) == 0) goto loc_00A1F497;
loc_00A1F383:
    if (*(uint64_t *)(v_stack_p10 + 0x40) != 0) goto loc_00A1F78F;
loc_00A1F390:
    if (((*(uint8_t *)(v_stack_p10 + 0x48)) & (2)) != 0) goto loc_00A1F466;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x60))) == 0) goto loc_00A1F466;
    v_stack_mA4 = 0;
    v_stack_m58 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x64))) != 0) goto loc_00A1F86A;
    result = v_stack_p10 + 48;
    local_r15 = (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x60));
    if ((*(uint64_t *)(v_stack_p10 + 0x30)) != (v_stack_p10 + 48)) {
        Arg1 = *(uint64_t *)(v_stack_p10 + 0x30) - 168;
        v_stack_m58 = Arg1;
        result = *(uint64_t *)(arg1 + 0xB8);
        local_r15 = *(uint32_t *)(result + 0x8);
    }
    v_stack_mA4 = (uint32_t)(local_r15);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x74)))) != 3) goto loc_00A1F7B6;
loc_00A1F3F8:
    v_stack_mA0 = (uint32_t)(2 + 82);
    local_r14 = (uint32_t)((2 + 82) + ((uint32_t)(*(uint16_t *)(v_stack_p18))));
    v_stack_mA0 = (uint32_t)(local_r14);
    if (v_stack_p20 != 0) goto loc_00A1F8B5;
loc_00A1F421:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x68))) + (3));
    local_r13 = (uint32_t)((local_r13) & (0xFFFFFFFCULL));
    v_stack_m88 = (uint32_t)(local_r13);
    if (((uint32_t)(local_r14 + local_r13 * 1)) < ((uint32_t)(local_r13))) goto loc_00A1F48D;
loc_00A1F43D:
    v_stack_m8C = (uint32_t)(local_r14 + local_r13 * 1);
    if (((uint32_t)(local_r14)) <= ((uint32_t)(local_r15))) goto loc_00A1F4A6;
loc_00A1F446:
    result = (uint16_t)((*(uint16_t *)(v_stack_p10 + 0x48)) | (2));
    *(uint16_t *)(v_stack_p10 + 0x48) = (uint16_t)(result);
loc_00A1F45C:
    if (((*(uint8_t *)(v_stack_p10 + 0x48)) & (2)) != 0) goto loc_00A1F872;
loc_00A1F466:
    if (Arg6 != 4) goto loc_00A1F71A;
    result = (uint16_t)((*(uint16_t *)(v_stack_m50 + 0x48)) | (8));
    *(uint16_t *)(v_stack_m50 + 0x48) = (uint16_t)(result);
loc_00A1F488:
    goto loc_00A1F368;
loc_00A1F48D:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    goto loc_00A1F43D;
loc_00A1F497:
    if (((*(uint8_t *)(v_stack_p10 + 0x48)) & (1)) == 0) goto loc_00A1F368;
    goto loc_00A1F6C3;
loc_00A1F4A6:
    if ((uint32_t)((uint32_t)(0xC0000095ULL)) != 0) goto loc_00A1F446;
    if (((uint32_t)(result)) > ((uint32_t)(local_r15))) goto loc_00A1F446;
    v_stack_m98 = 0;
    if (*(uint64_t *)(v_stack_p10 + 0x58) != 0) goto loc_00A1F6F2;
    if (v_stack_m50 == 0) goto loc_00A1F4E3;
    if (*(uint64_t *)(v_stack_m50 + 0x18) != 0) goto loc_00A1F8C8;
    if (*(uint64_t *)(v_stack_m50 + 0x8) != 0) goto loc_00A1F8D6;
loc_00A1F4E3:
    if ((*(uint64_t *)(v_stack_p10 + 0x58)) == 0) goto loc_00A1F7CC;
loc_00A1F4F3:
    if (0 == 0) goto loc_00A1F682;
    if (2 > ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x68))))) goto loc_00A1F5C8;
loc_00A1F508:
    *(uint32_t *)(0) = 0;
    *(uint32_t *)(0 + 0x4) = (uint32_t)((uint32_t)(Arg6));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x74)))) != 3) goto loc_00A1F5DE;
    *(uint64_t *)(0 + 0x8) = *(uint64_t *)(arg10 + 0x8);
    *(uint64_t *)(0 + 0x10) = *(uint64_t *)(arg10 + 0x10);
    *(uint64_t *)(0 + 0x18) = *(uint64_t *)(arg10 + 0x18);
    *(uint64_t *)(0 + 0x20) = *(uint64_t *)(arg10 + 0x20);
    *(uint64_t *)(0 + 0x28) = *(uint64_t *)(arg10 + 0x28);
    *(uint64_t *)(0 + 0x30) = *(uint64_t *)(arg10 + 0x30);
    *(uint32_t *)(0 + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(arg10 + 0x38)));
    *(uint32_t *)(0 + 0x3C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg10 + 0x3C)));
    *(uint64_t *)(0 + 0x40) = *(uint64_t *)(arg10 + 0x40);
    *(uint64_t *)(0 + 0x48) = *(uint64_t *)(arg10 + 0x48);
    *(uint16_t *)(0 + 0x50) = (uint16_t)(2 + 82 - 84);
    *(uint8_t *)(0 + 0x52) = (uint8_t)(*(uint8_t *)(arg10 + 0x50));
    *(uint8_t *)(0 + 0x53) = 0;
    local_rbx = (0) + (84);
loc_00A1F593:
    result = memcpy(local_rbx, *(uint64_t *)(v_stack_p18 + 0x8), *(uint16_t *)(v_stack_p18), Arg4);
    if (v_stack_p20 != 0) goto loc_00A1F654;
loc_00A1F5BC:
    *(uint32_t *)(v_stack_p10 + 0x68) = (uint32_t)(2 + 82 + 2 * 1);
    goto loc_00A1F682;
loc_00A1F5C8:
    Arg3 = (uint32_t)((2) - ((uint32_t)(v_stack_p20)));
    Arg1 = (v_stack_p20) + (*(uint64_t *)(v_stack_p10 + 0x58));
    Arg2 = 0;
    result = memset(Arg1, Arg2, Arg3, Arg4);
    goto loc_00A1F508;
loc_00A1F5DE:
    if (((uint32_t)(result)) == 2) goto loc_00A1F5F0;
    *(uint32_t *)(local_rbx + 0x8) = (uint32_t)(2 + 82 - 12);
    local_rbx = (local_rbx) + (12);
    goto loc_00A1F593;
loc_00A1F5F0:
    *(uint64_t *)(local_rbx + 0x8) = *(uint64_t *)(arg10 + 0x8);
    *(uint64_t *)(local_rbx + 0x10) = *(uint64_t *)(arg10 + 0x10);
    *(uint64_t *)(local_rbx + 0x18) = *(uint64_t *)(arg10 + 0x18);
    *(uint64_t *)(local_rbx + 0x20) = *(uint64_t *)(arg10 + 0x20);
    *(uint64_t *)(local_rbx + 0x28) = *(uint64_t *)(arg10 + 0x28);
    *(uint64_t *)(local_rbx + 0x30) = *(uint64_t *)(arg10 + 0x30);
    *(uint32_t *)(local_rbx + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(arg10 + 0x38)));
    *(uint32_t *)(local_rbx + 0x3C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg10 + 0x3C)));
    *(uint64_t *)(local_rbx + 0x40) = *(uint64_t *)(arg10 + 0x40);
    *(uint64_t *)(local_rbx + 0x48) = *(uint64_t *)(arg10 + 0x48);
    *(uint32_t *)(local_rbx + 0x50) = (uint32_t)(2 + 82 - 84);
    local_rbx = (local_rbx) + (84);
    goto loc_00A1F593;
loc_00A1F654:
    local_rbx = (local_rbx) + (*(uint16_t *)(v_stack_p18));
    *(uint16_t *)(local_rbx) = 58;
    local_rbx = (local_rbx) + (2);
    result = memcpy(local_rbx, *(uint64_t *)(arg10 + 0x8), *(uint16_t *)(arg10), Arg4);
    goto loc_00A1F5BC;
loc_00A1F682:
    goto loc_00A1F45C;
loc_00A1F6C3:
    if (*(uint64_t *)(v_stack_p10 + 0x10) == 0) goto loc_00A1F383;
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_p10 + 0x8), Arg7, *(uint64_t *)(v_stack_p10 + 0x18), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A1F368;
    goto loc_00A1F383;
loc_00A1F6F2:
    v_stack_m98 = result + (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x6C)) * 1;
    result = (uint32_t)((2) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x6C)))));
    *(uint32_t *)(result + (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x6C)) * 1) = (uint32_t)(result);
    *(uint32_t *)(v_stack_p10 + 0x6C) = 2;
    local_rbx = (2) + (*(uint64_t *)(v_stack_p10 + 0x58));
    v_stack_m98 = local_rbx;
    goto loc_00A1F4E3;
loc_00A1F71A:
    result = (uint16_t)((result) & ((uint16_t)((uint32_t)(0xFFF7ULL))));
    *(uint16_t *)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x6C)) + 0x48) = (uint16_t)(result);
    if ((*(uint64_t *)(v_stack_p10 + 0x30)) == (v_stack_p10 + 48)) goto loc_00A1F488;
    result = (uint16_t)((*(uint16_t *)(v_stack_p10 + 0x48)) & ((uint16_t)((uint32_t)(0xFFFDULL))));
    *(uint16_t *)(v_stack_p10 + 0x48) = (uint16_t)(result);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x30) + 0x8)) != (v_stack_p10 + 48)) goto loc_00A1F8AE;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x30)) + 0x8)) != (*(uint64_t *)(v_stack_p10 + 0x30))) goto loc_00A1F8AE;
    *(uint64_t *)(v_stack_p10 + 0x30) = *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x30));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x30)) + 0x8) = v_stack_p10 + 48;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x30)) = 0;
    v_stack_mB8 = 1;
    Arg4 = 0;
    result = FsRtlNotifyCompleteIrp(*(uint64_t *)(v_stack_p10 + 0x30) - 168, v_stack_p10, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x68)), Arg4);
    goto loc_00A1F488;
loc_00A1F78F:
    if (Arg8 == 0) goto loc_00A1F390;
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_p10 + 0x8), Arg8, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x68)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A1F368;
    goto loc_00A1F390;
loc_00A1F7B6:
    local_r14 = 12;
    if (((uint32_t)(result)) == 2) { local_r14 = (uint32_t)(12 + 72); }
    goto loc_00A1F3F8;
loc_00A1F7CC:
    v_stack_mA8 = 0;
    result = PsChargePoolQuota(*(uint64_t *)(v_stack_p10 + 0x78), 1, 2, Arg4);
    v_stack_mA8 = 1;
    result = ExAllocatePool2(290, 2, (uint32_t)(0x4E725346ULL), Arg4);
    *(uint64_t *)(v_stack_p10 + 0x58) = result;
    *(uint64_t *)(v_stack_p10 + 0x50) = result;
    *(uint32_t *)(v_stack_p10 + 0x64) = 2;
    v_stack_m98 = result;
    goto loc_00A1F4F3;
loc_00A1F86A:
    goto loc_00A1F3E7;
loc_00A1F872:
    if ((*(uint64_t *)(v_stack_p10 + 0x58)) == 0) goto loc_00A1F466;
    if ((*(uint64_t *)(v_stack_p10 + 0x50)) != 0) {
        Arg2 = *(uint32_t *)(v_stack_p10 + 0x64);
        Arg1 = *(uint64_t *)(v_stack_p10 + 0x78);
        result = PsReturnProcessPagedPoolQuota(Arg1, Arg2, (uint32_t)(0x4E725346ULL), Arg4);
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_stack_p10 + 0x50);
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x4E725346ULL), Arg4);
    }
    *(uint64_t *)(v_stack_p10 + 0x58) = 0;
    *(uint64_t *)(v_stack_p10 + 0x50) = 0;
    *(uint32_t *)(v_stack_p10 + 0x64) = 0;
    goto loc_00A1F466;
loc_00A1F8AE:
loc_00A1F8B5:
    result = (uint32_t)((*(uint16_t *)(result)) + (2));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
    v_stack_mA0 = (uint32_t)(local_r14);
    goto loc_00A1F421;
loc_00A1F8C8:
    v_stack_m98 = result;
    *(uint64_t *)(v_stack_p10 + 0x58) = result;
    goto loc_00A1F90D;
loc_00A1F8D6:
    if (((*(uint8_t *)(3 + 0xA)) & (5)) == 0) goto loc_00A1F8E7;
    v_stack_m98 = *(uint64_t *)(3 + 0x18);
    goto loc_00A1F909;
loc_00A1F8E7:
    v_stack_mB0 = 0x40000010ULL;
    v_stack_mB8 = 0;
    Arg4 = 0;
    Arg2 = 0;
    result = MmMapLockedPagesSpecifyCache(3, Arg2, Arg4 + 1, Arg4);
    v_stack_m98 = result;
loc_00A1F909:
    *(uint64_t *)(v_stack_p10 + 0x58) = result;
loc_00A1F90D:
    *(uint32_t *)(v_stack_p10 + 0x64) = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_00A1F4E3;
loc_00A1F916:
    result = *(uint64_t *)(arg1);
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x40)) == 0) {
        *(uint64_t *)(*(uint64_t *)(arg1) + 0x38) = 0;
        Arg1 = *(uint64_t *)(arg1);
        result = ExReleaseFastMutexUnsafe(Arg1, Arg2, Arg4 + 1, Arg4);
    }
    local_rsp = (local_rsp) + (160);
    return result;
loc_00A1F947:
    if ((*(uint32_t *)(result)) >= 88) goto loc_00A1F2FB;
    goto loc_00A1F933;
loc_00A1F952:
    v_stack_p58 = 0;
    result = FsRtlNotifyInitializeSync(v_stack_p58, Arg2, Arg4 + 1, Arg4);
    result = 0;
    if (condition_is_equal) goto loc_00A1F304;
    result = FsRtlNotifyUninitializeSync(v_stack_p58, Arg2, Arg4 + 1, Arg4);
    goto loc_00A1F304;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg10` | `+ 0x8` | `64` | `R` |
| `Arg10` | `+ 0x10` | `64` | `R` |
| `Arg10` | `+ 0x18` | `64` | `R` |
| `Arg10` | `+ 0x20` | `64` | `R` |
| `Arg10` | `+ 0x28` | `64` | `R` |
| `Arg10` | `+ 0x30` | `64` | `R` |
| `Arg10` | `+ 0x38` | `32` | `R` |
| `Arg10` | `+ 0x3C` | `32` | `R` |
| `Arg10` | `+ 0x40` | `64` | `R` |
| `Arg10` | `+ 0x48` | `64` | `R` |
| `Arg10` | `+ 0x50` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A1F2B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
