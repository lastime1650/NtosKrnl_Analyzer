# ExpSetDriverEntry

- RVA: `0x007CC424`–`0x007CC9A2` (길이 `1,406` bytes)
- VA: `0x00000001407CC424`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D5190`
- 디코드: `361`개 명령, `1,406/1,406` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x007CC4D4` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x007CC4F2` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x007CC539` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x007CC55F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007CC584` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007CC5C8` → [ExpSafeWcslen](../A2/ExpSafeWcslen_function_00A25698.md) (function, `0x00A25698`)
- `0x007CC5E1` → [ExpVerifyFilePath](../A2/ExpVerifyFilePath_function_00A257F0.md) (function, `0x00A257F0`)
- `0x007CC61D` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (function, `0x006B0BD0`)
- `0x007CC63E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007CC675` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (function, `0x006B0BD0`)
- `0x007CC6BB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007CC6EB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007CC700` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007CC71D` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x007CC75F` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x007CC780` → [IoGetEnvironmentVariableEx](../95/IoGetEnvironmentVariableEx_function_00952760.md) (function, `0x00952760`)
- `0x007CC7B4` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x007CC7D7` → [IoGetEnvironmentVariableEx](../95/IoGetEnvironmentVariableEx_function_00952760.md) (function, `0x00952760`)
- `0x007CC83B` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x007CC863` → [IoGetEnvironmentVariableEx](../95/IoGetEnvironmentVariableEx_function_00952760.md) (function, `0x00952760`)
- `0x007CC89E` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x007CC8C1` → [IoGetEnvironmentVariableEx](../95/IoGetEnvironmentVariableEx_function_00952760.md) (function, `0x00952760`)
- `0x007CC8F1` → [IoSetEnvironmentVariableEx](../A9/IoSetEnvironmentVariableEx_function_00A91A84.md) (function, `0x00A91A84`)
- `0x007CC8FF` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x007CC904` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007CC91D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007CC931` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007CC93B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007CC96D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007CC97F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtAddDriverEntry](NtAddDriverEntry_function_007CD280.md) at `0x007CD29F`
- [NtModifyDriverEntry](NtModifyDriverEntry_function_007CDCB0.md) at `0x007CDCCC`

### Static image references
- `0x007CC43F` → RVA `0x00E0A740` (`.data`; read)
- `0x007CC532` → RVA `0x00FD9AB8` (`PAGEDATA`; read)
- `0x007CC716` → RVA `0x00EFAB40` (`.data`; read)
- `0x007CC734` → RVA `0x000394B8` (`.rdata`; read)
- `0x007CC74D` → RVA `0x00B08990` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007CC7A2` → RVA `0x00B08900` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x007CC4D4` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x007CC55F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007CC584` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007CC61D` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (`PAGE` → `.text`)
  - `0x007CC63E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007CC675` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (`PAGE` → `.text`)
  - `0x007CC6BB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007CC6EB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007CC700` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007CC71D` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (`PAGE` → `.text`)
  - `0x007CC75F` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x007CC7B4` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x007CC83B` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x007CC89E` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x007CC8FF` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x007CC904` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007CC91D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007CC931` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007CC93B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007CC96D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007CC97F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007CC424  4C 8B DC                        mov r11, rsp
007CC427  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
007CC42B  49 89 73 20                     mov qword ptr [r11 + 0x20], rsi
007CC42F  57                              push rdi
007CC430  41 54                           push r12
007CC432  41 55                           push r13
007CC434  41 56                           push r14
007CC436  41 57                           push r15
007CC438  48 81 EC B0 00 00 00            sub rsp, 0xb0
007CC43F  48 8B 05 FA E2 63 00            mov rax, qword ptr [rip + 0x63e2fa]
007CC446  48 33 C4                        xor rax, rsp
007CC449  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
007CC451  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
007CC456  4C 8B F2                        mov r14, rdx
007CC459  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
007CC45D  33 C9                           xor ecx, ecx
007CC45F  49 89 4B 80                     mov qword ptr [r11 - 0x80], rcx
007CC463  44 8B F9                        mov r15d, ecx
007CC466  44 8B E9                        mov r13d, ecx
007CC469  44 8B E1                        mov r12d, ecx
007CC46C  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
007CC471  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
007CC476  89 4C 24 3C                     mov dword ptr [rsp + 0x3c], ecx
007CC47A  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
007CC47E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007CC487  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
007CC48B  40 8A B0 32 02 00 00            mov sil, byte ptr [rax + 0x232]
007CC492  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
007CC497  48 8D 7A 04                     lea rdi, [rdx + 4]
007CC49B  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
007CC4A5  40 84 F6                        test sil, sil
007CC4A8  74 15                           je 0x1407cc4bf
007CC4AA  48 3B FB                        cmp rdi, rbx
007CC4AD  48 0F 43 FB                     cmovae rdi, rbx
007CC4B1  90                              nop
007CC4B2  8B 3F                           mov edi, dword ptr [rdi]
007CC4B4  89 7C 24 4C                     mov dword ptr [rsp + 0x4c], edi
007CC4B8  40 8A 74 24 30                  mov sil, byte ptr [rsp + 0x30]
007CC4BD  EB 06                           jmp 0x1407cc4c5
007CC4BF  8B 3F                           mov edi, dword ptr [rdi]
007CC4C1  89 7C 24 4C                     mov dword ptr [rsp + 0x4c], edi
007CC4C5  83 FF 14                        cmp edi, 0x14
007CC4C8  73 0A                           jae 0x1407cc4d4
007CC4CA  B8 0D 00 00 C0                  mov eax, 0xc000000d
007CC4CF  E9 A0 04 00 00                  jmp 0x1407cc974
007CC4D4  E8 07 9E C6 FF                  call 0x1404362e0
007CC4D9  84 C0                           test al, al
007CC4DB  74 0A                           je 0x1407cc4e7
007CC4DD  B8 02 00 00 C0                  mov eax, 0xc0000002
007CC4E2  E9 8D 04 00 00                  jmp 0x1407cc974
007CC4E7  40 84 F6                        test sil, sil
007CC4EA  74 64                           je 0x1407cc550
007CC4EC  41 F6 C6 03                     test r14b, 3
007CC4F0  74 05                           je 0x1407cc4f7
007CC4F2  E8 D9 DA 0C 00                  call 0x140899fd0
007CC4F7  8B CF                           mov ecx, edi
007CC4F9  49 03 CE                        add rcx, r14
007CC4FC  48 3B CB                        cmp rcx, rbx
007CC4FF  77 05                           ja 0x1407cc506
007CC501  49 3B CE                        cmp rcx, r14
007CC504  73 0B                           jae 0x1407cc511
007CC506  8A 03                           mov al, byte ptr [rbx]
007CC508  40 8A 74 24 30                  mov sil, byte ptr [rsp + 0x30]
007CC50D  8B 7C 24 4C                     mov edi, dword ptr [rsp + 0x4c]
007CC511  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
007CC516  48 85 C0                        test rax, rax
007CC519  74 14                           je 0x1407cc52f
007CC51B  48 3B C3                        cmp rax, rbx
007CC51E  48 0F 42 D8                     cmovb rbx, rax
007CC522  8B 03                           mov eax, dword ptr [rbx]
007CC524  89 03                           mov dword ptr [rbx], eax
007CC526  40 8A 74 24 30                  mov sil, byte ptr [rsp + 0x30]
007CC52B  8B 7C 24 4C                     mov edi, dword ptr [rsp + 0x4c]
007CC52F  40 8A D6                        mov dl, sil
007CC532  48 8B 0D 7F D5 80 00            mov rcx, qword ptr [rip + 0x80d57f]
007CC539  E8 E2 58 0A 00                  call 0x140871e20
007CC53E  88 44 24 48                     mov byte ptr [rsp + 0x48], al
007CC542  84 C0                           test al, al
007CC544  75 0A                           jne 0x1407cc550
007CC546  B8 61 00 00 C0                  mov eax, 0xc0000061
007CC54B  E9 24 04 00 00                  jmp 0x1407cc974
007CC550  8B DF                           mov ebx, edi
007CC552  41 B8 45 6E 76 72               mov r8d, 0x72766e45
007CC558  8B D7                           mov edx, edi
007CC55A  B9 40 00 00 00                  mov ecx, 0x40
007CC55F  E8 8C 5B 3B 00                  call 0x140b820f0
007CC564  48 8B F8                        mov rdi, rax
007CC567  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007CC56C  48 85 C0                        test rax, rax
007CC56F  75 0A                           jne 0x1407cc57b
007CC571  B8 9A 00 00 C0                  mov eax, 0xc000009a
007CC576  E9 F9 03 00 00                  jmp 0x1407cc974
007CC57B  4C 8B C3                        mov r8, rbx
007CC57E  49 8B D6                        mov rdx, r14
007CC581  48 8B CF                        mov rcx, rdi
007CC584  E8 B7 A2 EF FF                  call 0x1406c6840
007CC589  90                              nop
007CC58A  48 8D 14 3B                     lea rdx, [rbx + rdi]
007CC58E  83 3F 01                        cmp dword ptr [rdi], 1
007CC591  75 13                           jne 0x1407cc5a6
007CC593  41 BE FF FF 00 00               mov r14d, 0xffff
007CC599  83 7C 24 50 00                  cmp dword ptr [rsp + 0x50], 0
007CC59E  75 10                           jne 0x1407cc5b0
007CC5A0  44 39 77 08                     cmp dword ptr [rdi + 8], r14d
007CC5A4  76 0A                           jbe 0x1407cc5b0
007CC5A6  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007CC5AB  E9 5E 03 00 00                  jmp 0x1407cc90e
007CC5B0  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
007CC5B3  A8 01                           test al, 1
007CC5B5  75 EF                           jne 0x1407cc5a6
007CC5B7  44 8B 47 10                     mov r8d, dword ptr [rdi + 0x10]
007CC5BB  41 F6 C0 03                     test r8b, 3
007CC5BF  75 E5                           jne 0x1407cc5a6
007CC5C1  48 8D 34 07                     lea rsi, [rdi + rax]
007CC5C5  48 8B CE                        mov rcx, rsi
007CC5C8  E8 CB 90 25 00                  call 0x140a25698
007CC5CD  83 F8 FF                        cmp eax, -1
007CC5D0  74 D4                           je 0x1407cc5a6
007CC5D2  44 8D 24 45 02 00 00 00         lea r12d, [rax*2 + 2]
007CC5DA  4E 8D 2C 07                     lea r13, [rdi + r8]
007CC5DE  49 8B CD                        mov rcx, r13
007CC5E1  E8 0A 92 25 00                  call 0x140a257f0
007CC5E6  8B D8                           mov ebx, eax
007CC5E8  85 C0                           test eax, eax
007CC5EA  0F 88 19 03 00 00               js 0x1407cc909
007CC5F0  49 8D 04 34                     lea rax, [r12 + rsi]
007CC5F4  49 3B C5                        cmp rax, r13
007CC5F7  76 0A                           jbe 0x1407cc603
007CC5F9  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007CC5FE  E9 06 03 00 00                  jmp 0x1407cc909
007CC603  41 83 7D 08 04                  cmp dword ptr [r13 + 8], 4
007CC608  0F 84 81 00 00 00               je 0x1407cc68f
007CC60E  4C 8D 4C 24 3C                  lea r9, [rsp + 0x3c]
007CC613  45 33 C0                        xor r8d, r8d
007CC616  41 8D 50 04                     lea edx, [r8 + 4]
007CC61A  49 8B CD                        mov rcx, r13
007CC61D  E8 AE 45 EE FF                  call 0x1406b0bd0
007CC622  8B D8                           mov ebx, eax
007CC624  3D 23 00 00 C0                  cmp eax, 0xc0000023
007CC629  0F 85 DA 02 00 00               jne 0x1407cc909
007CC62F  8B 54 24 3C                     mov edx, dword ptr [rsp + 0x3c]
007CC633  B9 40 00 00 00                  mov ecx, 0x40
007CC638  41 B8 45 6E 76 72               mov r8d, 0x72766e45
007CC63E  E8 AD 5A 3B 00                  call 0x140b820f0
007CC643  48 8B C8                        mov rcx, rax
007CC646  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007CC64B  48 85 C0                        test rax, rax
007CC64E  75 0D                           jne 0x1407cc65d
007CC650  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007CC655  4C 8B E0                        mov r12, rax
007CC658  E9 B1 02 00 00                  jmp 0x1407cc90e
007CC65D  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
007CC661  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
007CC665  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
007CC66A  4C 8B C1                        mov r8, rcx
007CC66D  BA 04 00 00 00                  mov edx, 4
007CC672  49 8B CD                        mov rcx, r13
007CC675  E8 56 45 EE FF                  call 0x1406b0bd0
007CC67A  8B D8                           mov ebx, eax
007CC67C  85 C0                           test eax, eax
007CC67E  0F 88 85 02 00 00               js 0x1407cc909
007CC684  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
007CC688  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
007CC68D  EB 0C                           jmp 0x1407cc69b
007CC68F  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
007CC693  49 8B DD                        mov rbx, r13
007CC696  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
007CC69B  83 C0 F4                        add eax, -0xc
007CC69E  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
007CC6A2  41 8B D4                        mov edx, r12d
007CC6A5  83 C2 06                        add edx, 6
007CC6A8  03 C2                           add eax, edx
007CC6AA  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
007CC6AE  8B D0                           mov edx, eax
007CC6B0  B9 40 00 00 00                  mov ecx, 0x40
007CC6B5  41 B8 45 6E 76 72               mov r8d, 0x72766e45
007CC6BB  E8 30 5A 3B 00                  call 0x140b820f0
007CC6C0  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
007CC6C5  48 85 C0                        test rax, rax
007CC6C8  75 0A                           jne 0x1407cc6d4
007CC6CA  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007CC6CF  E9 35 02 00 00                  jmp 0x1407cc909
007CC6D4  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
007CC6D8  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
007CC6DD  66 89 47 04                     mov word ptr [rdi + 4], ax
007CC6E1  48 8D 4F 06                     lea rcx, [rdi + 6]
007CC6E5  4D 8B C4                        mov r8, r12
007CC6E8  48 8B D6                        mov rdx, rsi
007CC6EB  E8 50 A1 EF FF                  call 0x1406c6840
007CC6F0  48 8D 4F 06                     lea rcx, [rdi + 6]
007CC6F4  49 03 CC                        add rcx, r12
007CC6F7  44 8B 44 24 3C                  mov r8d, dword ptr [rsp + 0x3c]
007CC6FC  48 8D 53 0C                     lea rdx, [rbx + 0xc]
007CC700  E8 3B A1 EF FF                  call 0x1406c6840
007CC705  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007CC70E  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
007CC715  90                              nop
007CC716  48 8D 0D 23 E4 72 00            lea rcx, [rip + 0x72e423]
007CC71D  E8 FE 6F C2 FF                  call 0x1403f3720
007CC722  33 DB                           xor ebx, ebx
007CC724  39 5C 24 50                     cmp dword ptr [rsp + 0x50], ebx
007CC728  0F 84 E9 00 00 00               je 0x1407cc817
007CC72E  44 8B FB                        mov r15d, ebx
007CC731  8D 7B 0B                        lea edi, [rbx + 0xb]
007CC734  48 8D 35 7D CD 86 FF            lea rsi, [rip - 0x793283]
007CC73B  41 BC 00 01 00 C0               mov r12d, 0xc0000100
007CC741  45 3B FE                        cmp r15d, r14d
007CC744  0F 87 B4 00 00 00               ja 0x1407cc7fe
007CC74A  45 8B CF                        mov r9d, r15d
007CC74D  4C 8D 05 3C C2 33 00            lea r8, [rip + 0x33c23c]
007CC754  48 8B D7                        mov rdx, rdi
007CC757  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
007CC75F  E8 BC 83 D3 FF                  call 0x140504b20
007CC764  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
007CC768  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
007CC76D  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
007CC772  45 33 C0                        xor r8d, r8d
007CC775  48 8B D6                        mov rdx, rsi
007CC778  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
007CC780  E8 DB 5F 18 00                  call 0x140952760
007CC785  8B D8                           mov ebx, eax
007CC787  41 3B C4                        cmp eax, r12d
007CC78A  75 52                           jne 0x1407cc7de
007CC78C  43 8D 04 3F                     lea eax, [r15 + r15]
007CC790  41 0B C7                        or eax, r15d
007CC793  25 44 44 44 C4                  and eax, 0xc4444444
007CC798  03 C0                           add eax, eax
007CC79A  41 85 C7                        test r15d, eax
007CC79D  74 3F                           je 0x1407cc7de
007CC79F  45 8B CF                        mov r9d, r15d
007CC7A2  4C 8D 05 57 C1 33 00            lea r8, [rip + 0x33c157]
007CC7A9  48 8B D7                        mov rdx, rdi
007CC7AC  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
007CC7B4  E8 67 83 D3 FF                  call 0x140504b20
007CC7B9  83 64 24 34 00                  and dword ptr [rsp + 0x34], 0
007CC7BE  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007CC7C4  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
007CC7C9  45 33 C0                        xor r8d, r8d
007CC7CC  48 8B D6                        mov rdx, rsi
007CC7CF  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
007CC7D7  E8 84 5F 18 00                  call 0x140952760
007CC7DC  8B D8                           mov ebx, eax
007CC7DE  41 3B DC                        cmp ebx, r12d
007CC7E1  74 16                           je 0x1407cc7f9
007CC7E3  85 DB                           test ebx, ebx
007CC7E5  74 08                           je 0x1407cc7ef
007CC7E7  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
007CC7ED  75 14                           jne 0x1407cc803
007CC7EF  41 FF C7                        inc r15d
007CC7F2  33 DB                           xor ebx, ebx
007CC7F4  E9 48 FF FF FF                  jmp 0x1407cc741
007CC7F9  45 3B FE                        cmp r15d, r14d
007CC7FC  76 0F                           jbe 0x1407cc80d
007CC7FE  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007CC803  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
007CC808  E9 EB 00 00 00                  jmp 0x1407cc8f8
007CC80D  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
007CC812  E9 BD 00 00 00                  jmp 0x1407cc8d4
007CC817  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
007CC81C  44 8B 7F 08                     mov r15d, dword ptr [rdi + 8]
007CC820  45 8B CF                        mov r9d, r15d
007CC823  4C 8D 05 D6 C0 33 00            lea r8, [rip + 0x33c0d6]
007CC82A  41 BE 0B 00 00 00               mov r14d, 0xb
007CC830  41 8B D6                        mov edx, r14d
007CC833  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
007CC83B  E8 E0 82 D3 FF                  call 0x140504b20
007CC840  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
007CC844  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
007CC849  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
007CC84E  45 33 C0                        xor r8d, r8d
007CC851  48 8D 35 60 CC 86 FF            lea rsi, [rip - 0x7933a0]
007CC858  48 8B D6                        mov rdx, rsi
007CC85B  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
007CC863  E8 F8 5E 18 00                  call 0x140952760
007CC868  8B D8                           mov ebx, eax
007CC86A  41 BC 00 01 00 C0               mov r12d, 0xc0000100
007CC870  41 3B C4                        cmp eax, r12d
007CC873  75 53                           jne 0x1407cc8c8
007CC875  44 8B 4F 08                     mov r9d, dword ptr [rdi + 8]
007CC879  43 8D 04 09                     lea eax, [r9 + r9]
007CC87D  41 0B C1                        or eax, r9d
007CC880  25 44 44 44 C4                  and eax, 0xc4444444
007CC885  03 C0                           add eax, eax
007CC887  41 85 C1                        test r9d, eax
007CC88A  74 3C                           je 0x1407cc8c8
007CC88C  4C 8D 05 FD C0 33 00            lea r8, [rip + 0x33c0fd]
007CC893  41 8B D6                        mov edx, r14d
007CC896  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
007CC89E  E8 7D 82 D3 FF                  call 0x140504b20
007CC8A3  83 64 24 34 00                  and dword ptr [rsp + 0x34], 0
007CC8A8  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007CC8AE  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
007CC8B3  45 33 C0                        xor r8d, r8d
007CC8B6  48 8B D6                        mov rdx, rsi
007CC8B9  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
007CC8C1  E8 9A 5E 18 00                  call 0x140952760
007CC8C6  8B D8                           mov ebx, eax
007CC8C8  85 DB                           test ebx, ebx
007CC8CA  74 08                           je 0x1407cc8d4
007CC8CC  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
007CC8D2  75 24                           jne 0x1407cc8f8
007CC8D4  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
007CC8DC  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
007CC8E1  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
007CC8E6  48 8B D6                        mov rdx, rsi
007CC8E9  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
007CC8F1  E8 8E 51 2C 00                  call 0x140a91a84
007CC8F6  8B D8                           mov ebx, eax
007CC8F8  48 8D 0D 41 E2 72 00            lea rcx, [rip + 0x72e241]
007CC8FF  E8 9C 3A A8 FF                  call 0x1402503a0
007CC904  E8 A7 0F A9 FF                  call 0x14025d8b0
007CC909  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
007CC90E  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
007CC913  48 85 F6                        test rsi, rsi
007CC916  74 0A                           je 0x1407cc922
007CC918  33 D2                           xor edx, edx
007CC91A  48 8B CE                        mov rcx, rsi
007CC91D  E8 4E 5F 3B 00                  call 0x140b82870
007CC922  4D 85 E4                        test r12, r12
007CC925  74 0F                           je 0x1407cc936
007CC927  4D 3B E5                        cmp r12, r13
007CC92A  74 0A                           je 0x1407cc936
007CC92C  33 D2                           xor edx, edx
007CC92E  49 8B CC                        mov rcx, r12
007CC931  E8 3A 5F 3B 00                  call 0x140b82870
007CC936  33 D2                           xor edx, edx
007CC938  48 8B CF                        mov rcx, rdi
007CC93B  E8 30 5F 3B 00                  call 0x140b82870
007CC940  90                              nop
007CC941  83 7C 24 50 00                  cmp dword ptr [rsp + 0x50], 0
007CC946  74 11                           je 0x1407cc959
007CC948  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
007CC94D  48 85 C0                        test rax, rax
007CC950  74 07                           je 0x1407cc959
007CC952  85 DB                           test ebx, ebx
007CC954  78 03                           js 0x1407cc959
007CC956  44 89 38                        mov dword ptr [rax], r15d
007CC959  8B C3                           mov eax, ebx
007CC95B  EB 17                           jmp 0x1407cc974
007CC95D  EB 15                           jmp 0x1407cc974
007CC95F  8B D8                           mov ebx, eax
007CC961  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007CC966  48 85 C9                        test rcx, rcx
007CC969  74 07                           je 0x1407cc972
007CC96B  33 D2                           xor edx, edx
007CC96D  E8 FE 5E 3B 00                  call 0x140b82870
007CC972  8B C3                           mov eax, ebx
007CC974  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
007CC97C  48 33 CC                        xor rcx, rsp
007CC97F  E8 BC FC ED FF                  call 0x1406ac640
007CC984  4C 8D 9C 24 B0 00 00 00         lea r11, [rsp + 0xb0]
007CC98C  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
007CC990  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
007CC994  49 8B E3                        mov rsp, r11
007CC997  41 5F                           pop r15
007CC999  41 5E                           pop r14
007CC99B  41 5D                           pop r13
007CC99D  41 5C                           pop r12
007CC99F  5F                              pop rdi
007CC9A0  C3                              ret
007CC9A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpSetDriverEntry(int a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned __int8 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA4;
    unsigned __int8 v_stack_mA8;
    unsigned __int64 v_stack_mB8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 6546170)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m70 = a3;
    v_stack_m88 = a1;
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 128) = 0;
    v_stack_m98 = 0;
    v_stack_m78 = 0;
    v_stack_m9C = 0;
    v_stack_mA4 = 0;
    *(unsigned __int64 *)(v_rsp - 88) = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_mA8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_007CC4BF;
    v_rdi = a2 + 4;
    if ((a2 + 4) >= v_rbx) { v_rdi = v_rbx; }
    v_stack_m8C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)));
    goto loc_007CC4C5;
loc_007CC4BF:
    v_stack_m8C = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi)))));
loc_007CC4C5:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi)))))) >= 20) goto loc_007CC4D4;
    goto loc_007CC974;
loc_007CC4D4:
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_007CC4E7;
    goto loc_007CC974;
loc_007CC4E7:
    if ((unsigned __int8)(v_stack_mA8) == 0) goto loc_007CC550;
    result = (unsigned int)(0xC0000002ULL);
    if ((((unsigned __int8)(a2)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
    }
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi))))))) + (a2);
    if (a1 > v_rbx) goto loc_007CC506;
    v_rsi = v_stack_mA8;
    v_rdi = (unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi))));
    if (a1 < a2) {
        result = *(unsigned __int8 *)(v_rbx);
        v_rsi = v_stack_mA8;
        v_rdi = v_stack_m8C;
    }
    result = v_stack_m70;
    if (v_stack_m70 != 0) {
        if (v_stack_m70 < v_rbx) { v_rbx = v_stack_m70; }
        result = *(unsigned int *)(v_rbx);
        *(unsigned int *)(v_rbx) = (unsigned int)(result);
        v_rsi = v_stack_mA8;
        v_rdi = v_stack_m8C;
    }
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 8443263), (unsigned __int8)(v_rsi), a3, a4);
    v_stack_m90 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) goto loc_007CC550;
    goto loc_007CC974;
loc_007CC550:
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x72766E45ULL), a4);
    v_stack_m80 = result;
    if (result != 0) goto loc_007CC57B;
    goto loc_007CC974;
loc_007CC57B:
    result = memcpy(result, a2, (unsigned int)((unsigned int)(v_rdi)), a4);
    if ((*(unsigned int *)(result)) != 1) goto loc_007CC5A6;
    if (v_stack_m88 != 0) goto loc_007CC5B0;
    if ((*(unsigned int *)(result + 8)) <= ((unsigned int)((unsigned int)(0xFFFFULL)))) goto loc_007CC5B0;
loc_007CC5A6:
    goto loc_007CC90E;
loc_007CC5B0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (1)) != 0) goto loc_007CC5A6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 16)))) & (3)) != 0) goto loc_007CC5A6;
    result = ExpSafeWcslen(result + (unsigned int)(*(unsigned int *)(result + 12)) * 1, (unsigned int)((unsigned int)(v_rdi)) + result * 1, (unsigned int)(*(unsigned int *)(result + 16)), a4);
    if (((unsigned int)(result)) == -1) goto loc_007CC5A6;
    result = ExpVerifyFilePath(result + (unsigned int)(*(unsigned int *)(result + 16)) * 1, (unsigned int)((unsigned int)(v_rdi)) + result * 1, (unsigned int)(*(unsigned int *)(result + 16)), a4);
    if (sign_flag) goto loc_007CC909;
    if ((result * 2 + 2 + result + (unsigned int)(*(unsigned int *)(result + 12)) * 1 * 1) <= (result + (unsigned int)(*(unsigned int *)(result + 16)) * 1)) goto loc_007CC603;
    goto loc_007CC909;
loc_007CC603:
    if ((*(unsigned int *)(result + (unsigned int)(*(unsigned int *)(result + 16)) * 1 + 8)) == 4) goto loc_007CC68F;
    a3 = 0;
    result = ZwTranslateFilePath(result + (unsigned int)(*(unsigned int *)(result + 16)) * 1, a3 + 4, a3, v_stack_m9C);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_007CC909;
    result = ExAllocatePool2(64, (unsigned int)(v_stack_m9C), (unsigned int)(0x72766E45ULL), v_stack_m9C);
    v_stack_m98 = result;
    if (result != 0) goto loc_007CC65D;
    goto loc_007CC90E;
loc_007CC65D:
    v_stack_mA4 = (unsigned int)((unsigned int)(v_stack_m9C));
    result = ZwTranslateFilePath(result + (unsigned int)(*(unsigned int *)(result + 16)) * 1, 4, result, v_stack_mA4);
    if (sign_flag) goto loc_007CC909;
    goto loc_007CC69B;
loc_007CC68F:
    v_stack_m98 = result + (unsigned int)(*(unsigned int *)(result + 16)) * 1;
loc_007CC69B:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + (unsigned int)(*(unsigned int *)(result + 16)) * 1 + 4))) + (-12));
    v_stack_m9C = (unsigned int)(result);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) + (6));
    result = (unsigned int)((result) + ((unsigned int)(a2)));
    v_stack_m84 = (unsigned int)(result);
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(result)), (unsigned int)(0x72766E45ULL), v_stack_mA4);
    v_stack_m78 = result;
    if (result != 0) goto loc_007CC6D4;
    goto loc_007CC909;
loc_007CC6D4:
    *(unsigned __int16 *)(v_stack_m78 + 4) = (unsigned __int16)((unsigned int)(v_stack_m9C));
    result = memcpy(v_stack_m78 + 6, result + (unsigned int)(*(unsigned int *)(result + 12)) * 1, result, v_stack_mA4);
    a1 = (v_stack_m78 + 6) + (result);
    result = memcpy(a1, (unsigned int)(0xC000009AULL) + 12, (unsigned int)(v_stack_m9C), v_stack_mA4);
    result = ExAcquireFastMutexUnsafe(v_rip + 7529507, (unsigned int)(0xC000009AULL) + 12, (unsigned int)(v_stack_m9C), v_stack_mA4);
    v_rbx = 0;
    if (v_stack_m88 == 0) goto loc_007CC817;
loc_007CC741:
    if (0 > ((unsigned int)((unsigned int)(0xFFFFULL)))) goto loc_007CC7FE;
    result = swprintf_s(v_stack_m50, v_rbx + 11, v_rip + 3392060, 0);
    v_stack_mA4 = 0;
    v_stack_mB8 = 0;
    a3 = 0;
    result = IoGetEnvironmentVariableEx(v_stack_m50, v_rip - 7942787, a3, v_stack_mA4);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000100ULL)))) goto loc_007CC7DE;
    result = (unsigned int)((0 + 0 * 1) | (0));
    result = (unsigned int)((result) & (0xC4444444ULL));
    result = (unsigned int)((result) + ((unsigned int)(result)));
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((0) & ((unsigned int)(result))) != 0) {
        a4 = 0;
        a3 = v_rip + 3391831;
        a2 = v_rbx + 11;
        a1 = v_stack_m50;
        result = swprintf_s(a1, a2, a3, a4);
        a4 = v_stack_mA4;
        a3 = 0;
        a2 = v_rip - 7942787;
        a1 = v_stack_m50;
        result = IoGetEnvironmentVariableEx(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (((unsigned int)(v_rbx)) == ((unsigned int)((unsigned int)(0xC0000100ULL)))) goto loc_007CC7F9;
    if ((unsigned int)(v_rbx) == 0) goto loc_007CC7EF;
    if (((unsigned int)(v_rbx)) != 0xC0000023ULL) goto loc_007CC803;
loc_007CC7EF:
    v_r15 = (unsigned int)((0) + 1);
    v_rbx = 0;
    goto loc_007CC741;
loc_007CC7F9:
    if (((unsigned int)(v_r15)) <= ((unsigned int)((unsigned int)(0xFFFFULL)))) goto loc_007CC80D;
loc_007CC7FE:
loc_007CC803:
    goto loc_007CC8F8;
loc_007CC80D:
    goto loc_007CC8D4;
loc_007CC817:
    result = swprintf_s(v_stack_m50, 11, v_rip + 3391702, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m80 + 8)))));
    v_stack_mA4 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_mB8 = (unsigned int)(0xC000009AULL);
    a3 = 0;
    result = IoGetEnvironmentVariableEx(v_stack_m50, v_rip - 7943072, a3, v_stack_mA4);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000100ULL)))) goto loc_007CC8C8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m80 + 8)) + (unsigned int)(*(unsigned int *)(v_stack_m80 + 8)) * 1) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m80 + 8)))));
    result = (unsigned int)((result) & (0xC4444444ULL));
    result = (unsigned int)((result) + ((unsigned int)(result)));
    v_rbx = (unsigned int)((unsigned int)(result));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m80 + 8)))) & ((unsigned int)(result))) != 0) {
        a3 = v_rip + 3391741;
        a2 = 11;
        a1 = v_stack_m50;
        result = swprintf_s(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m80 + 8)));
        a4 = v_stack_mA4;
        a3 = 0;
        a2 = v_rip - 7943072;
        a1 = v_stack_m50;
        result = IoGetEnvironmentVariableEx(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if ((unsigned int)(v_rbx) == 0) goto loc_007CC8D4;
    if (((unsigned int)(v_rbx)) == 0xC0000023ULL) {
        v_stack_mB8 = 1;
        a4 = v_stack_m84;
        a3 = v_stack_m78;
        a2 = v_rip - 7943072;
        a1 = v_stack_m50;
        result = IoSetEnvironmentVariableEx(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    result = ExReleaseFastMutexUnsafe(v_rip + 7529025, a2, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 7529025, a2, a3, a4);
loc_007CC909:
loc_007CC90E:
    if (v_stack_m78 != 0) {
        a2 = 0;
        a1 = v_stack_m78;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (v_stack_m98 == 0) goto loc_007CC936;
    if (v_stack_m98 != (result + (unsigned int)(*(unsigned int *)(result + 16)) * 1)) {
        a2 = 0;
        a1 = v_stack_m98;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m80, a2, a3, a4);
    if (v_stack_m88 == 0) goto loc_007CC959;
    if (v_stack_m70 == 0) goto loc_007CC959;
    if (!(sign_flag)) {
        *(unsigned int *)(v_stack_m70) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m80 + 8)));
    }
    goto loc_007CC974;
loc_007CC974:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpSetDriverEntry(int32_t Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m50;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint8_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA4;
    uint8_t v_stack_mA8;
    uint64_t v_stack_mB8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x63E2FA)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m70 = Arg3;
    v_stack_m88 = Arg1;
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x80) = 0;
    v_stack_m98 = 0;
    v_stack_m78 = 0;
    v_stack_m9C = 0;
    v_stack_mA4 = 0;
    *(uint64_t *)(local_rsp - 0x58) = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_mA8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_007CC4BF;
    local_rdi = Arg2 + 4;
    if ((Arg2 + 4) >= local_rbx) { local_rdi = local_rbx; }
    v_stack_m8C = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)));
    goto loc_007CC4C5;
loc_007CC4BF:
    v_stack_m8C = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi)))));
loc_007CC4C5:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi)))))) >= 20) goto loc_007CC4D4;
    goto loc_007CC974;
loc_007CC4D4:
    result = PsIsCurrentThreadInServerSilo(Arg1, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_007CC4E7;
    goto loc_007CC974;
loc_007CC4E7:
    if ((uint8_t)(v_stack_mA8) == 0) goto loc_007CC550;
    result = (uint32_t)(0xC0000002ULL);
    if ((((uint8_t)(Arg2)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi))))))) + (Arg2);
    if (Arg1 > local_rbx) goto loc_007CC506;
    local_rsi = v_stack_mA8;
    local_rdi = (uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi))));
    if (Arg1 < Arg2) {
        result = *(uint8_t *)(local_rbx);
        local_rsi = v_stack_mA8;
        local_rdi = v_stack_m8C;
    }
    result = v_stack_m70;
    if (v_stack_m70 != 0) {
        if (v_stack_m70 < local_rbx) { local_rbx = v_stack_m70; }
        result = *(uint32_t *)(local_rbx);
        *(uint32_t *)(local_rbx) = (uint32_t)(result);
        local_rsi = v_stack_mA8;
        local_rdi = v_stack_m8C;
    }
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x80D57F), (uint8_t)(local_rsi), Arg3, a4);
    v_stack_m90 = (uint8_t)(result);
    if ((uint8_t)(result) != 0) goto loc_007CC550;
    goto loc_007CC974;
loc_007CC550:
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x72766E45ULL), a4);
    v_stack_m80 = result;
    if (result != 0) goto loc_007CC57B;
    goto loc_007CC974;
loc_007CC57B:
    result = memcpy(result, Arg2, (uint32_t)((uint32_t)(local_rdi)), a4);
    if ((*(uint32_t *)(result)) != 1) goto loc_007CC5A6;
    if (v_stack_m88 != 0) goto loc_007CC5B0;
    if ((*(uint32_t *)(result + 0x8)) <= ((uint32_t)((uint32_t)(0xFFFFULL)))) goto loc_007CC5B0;
loc_007CC5A6:
    goto loc_007CC90E;
loc_007CC5B0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (1)) != 0) goto loc_007CC5A6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x10)))) & (3)) != 0) goto loc_007CC5A6;
    result = ExpSafeWcslen(result + (uint32_t)(*(uint32_t *)(result + 0xC)) * 1, (uint32_t)((uint32_t)(local_rdi)) + result * 1, (uint32_t)(*(uint32_t *)(result + 0x10)), a4);
    if (((uint32_t)(result)) == -1) goto loc_007CC5A6;
    result = ExpVerifyFilePath(result + (uint32_t)(*(uint32_t *)(result + 0x10)) * 1, (uint32_t)((uint32_t)(local_rdi)) + result * 1, (uint32_t)(*(uint32_t *)(result + 0x10)), a4);
    if (sign_flag) goto loc_007CC909;
    if ((result * 2 + 2 + result + (uint32_t)(*(uint32_t *)(result + 0xC)) * 1 * 1) <= (result + (uint32_t)(*(uint32_t *)(result + 0x10)) * 1)) goto loc_007CC603;
    goto loc_007CC909;
loc_007CC603:
    if ((*(uint32_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x10)) * 1 + 0x8)) == 4) goto loc_007CC68F;
    Arg3 = 0;
    result = ZwTranslateFilePath(result + (uint32_t)(*(uint32_t *)(result + 0x10)) * 1, Arg3 + 4, Arg3, v_stack_m9C);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_007CC909;
    result = ExAllocatePool2(64, (uint32_t)(v_stack_m9C), (uint32_t)(0x72766E45ULL), v_stack_m9C);
    v_stack_m98 = result;
    if (result != 0) goto loc_007CC65D;
    goto loc_007CC90E;
loc_007CC65D:
    v_stack_mA4 = (uint32_t)((uint32_t)(v_stack_m9C));
    result = ZwTranslateFilePath(result + (uint32_t)(*(uint32_t *)(result + 0x10)) * 1, 4, result, v_stack_mA4);
    if (sign_flag) goto loc_007CC909;
    goto loc_007CC69B;
loc_007CC68F:
    v_stack_m98 = result + (uint32_t)(*(uint32_t *)(result + 0x10)) * 1;
loc_007CC69B:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x10)) * 1 + 0x4))) + (-12));
    v_stack_m9C = (uint32_t)(result);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) + (6));
    result = (uint32_t)((result) + ((uint32_t)(Arg2)));
    v_stack_m84 = (uint32_t)(result);
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(result)), (uint32_t)(0x72766E45ULL), v_stack_mA4);
    v_stack_m78 = result;
    if (result != 0) goto loc_007CC6D4;
    goto loc_007CC909;
loc_007CC6D4:
    *(uint16_t *)(v_stack_m78 + 0x4) = (uint16_t)((uint32_t)(v_stack_m9C));
    result = memcpy(v_stack_m78 + 6, result + (uint32_t)(*(uint32_t *)(result + 0xC)) * 1, result, v_stack_mA4);
    Arg1 = (v_stack_m78 + 6) + (result);
    result = memcpy(Arg1, (uint32_t)(0xC000009AULL) + 12, (uint32_t)(v_stack_m9C), v_stack_mA4);
    result = ExAcquireFastMutexUnsafe(v_rip + 7529507, (uint32_t)(0xC000009AULL) + 12, (uint32_t)(v_stack_m9C), v_stack_mA4);
    local_rbx = 0;
    if (v_stack_m88 == 0) goto loc_007CC817;
loc_007CC741:
    if (0 > ((uint32_t)((uint32_t)(0xFFFFULL)))) goto loc_007CC7FE;
    result = swprintf_s(v_stack_m50, local_rbx + 11, v_rip + 3392060, 0);
    v_stack_mA4 = 0;
    v_stack_mB8 = 0;
    Arg3 = 0;
    result = IoGetEnvironmentVariableEx(v_stack_m50, v_rip - 7942787, Arg3, v_stack_mA4);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000100ULL)))) goto loc_007CC7DE;
    result = (uint32_t)((0 + 0 * 1) | (0));
    result = (uint32_t)((result) & (0xC4444444ULL));
    result = (uint32_t)((result) + ((uint32_t)(result)));
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((0) & ((uint32_t)(result))) != 0) {
        a4 = 0;
        Arg3 = v_rip + 3391831;
        Arg2 = local_rbx + 11;
        Arg1 = v_stack_m50;
        result = swprintf_s(Arg1, Arg2, Arg3, a4);
        a4 = v_stack_mA4;
        Arg3 = 0;
        Arg2 = v_rip - 7942787;
        Arg1 = v_stack_m50;
        result = IoGetEnvironmentVariableEx(Arg1, Arg2, Arg3, a4);
        local_rbx = (uint32_t)(result);
    }
    if (((uint32_t)(local_rbx)) == ((uint32_t)((uint32_t)(0xC0000100ULL)))) goto loc_007CC7F9;
    if ((uint32_t)(local_rbx) == 0) goto loc_007CC7EF;
    if (((uint32_t)(local_rbx)) != 0xC0000023ULL) goto loc_007CC803;
loc_007CC7EF:
    local_r15 = (uint32_t)((0) + 1);
    local_rbx = 0;
    goto loc_007CC741;
loc_007CC7F9:
    if (((uint32_t)(local_r15)) <= ((uint32_t)((uint32_t)(0xFFFFULL)))) goto loc_007CC80D;
loc_007CC7FE:
loc_007CC803:
    goto loc_007CC8F8;
loc_007CC80D:
    goto loc_007CC8D4;
loc_007CC817:
    result = swprintf_s(v_stack_m50, 11, v_rip + 3391702, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x8)))));
    v_stack_mA4 = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_mB8 = (uint32_t)(0xC000009AULL);
    Arg3 = 0;
    result = IoGetEnvironmentVariableEx(v_stack_m50, v_rip - 7943072, Arg3, v_stack_mA4);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000100ULL)))) goto loc_007CC8C8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x8)) + (uint32_t)(*(uint32_t *)(v_stack_m80 + 0x8)) * 1) | ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x8)))));
    result = (uint32_t)((result) & (0xC4444444ULL));
    result = (uint32_t)((result) + ((uint32_t)(result)));
    local_rbx = (uint32_t)((uint32_t)(result));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x8)))) & ((uint32_t)(result))) != 0) {
        Arg3 = v_rip + 3391741;
        Arg2 = 11;
        Arg1 = v_stack_m50;
        result = swprintf_s(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m80 + 0x8)));
        a4 = v_stack_mA4;
        Arg3 = 0;
        Arg2 = v_rip - 7943072;
        Arg1 = v_stack_m50;
        result = IoGetEnvironmentVariableEx(Arg1, Arg2, Arg3, a4);
        local_rbx = (uint32_t)(result);
    }
    if ((uint32_t)(local_rbx) == 0) goto loc_007CC8D4;
    if (((uint32_t)(local_rbx)) == 0xC0000023ULL) {
        v_stack_mB8 = 1;
        a4 = v_stack_m84;
        Arg3 = v_stack_m78;
        Arg2 = v_rip - 7943072;
        Arg1 = v_stack_m50;
        result = IoSetEnvironmentVariableEx(Arg1, Arg2, Arg3, a4);
        local_rbx = (uint32_t)(result);
    }
    result = ExReleaseFastMutexUnsafe(v_rip + 7529025, Arg2, Arg3, a4);
    result = KeLeaveCriticalRegion(v_rip + 7529025, Arg2, Arg3, a4);
loc_007CC909:
loc_007CC90E:
    if (v_stack_m78 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m78;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, a4);
    }
    if (v_stack_m98 == 0) goto loc_007CC936;
    if (v_stack_m98 != (result + (uint32_t)(*(uint32_t *)(result + 0x10)) * 1)) {
        Arg2 = 0;
        Arg1 = v_stack_m98;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, a4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m80, Arg2, Arg3, a4);
    if (v_stack_m88 == 0) goto loc_007CC959;
    if (v_stack_m70 == 0) goto loc_007CC959;
    if (!(sign_flag)) {
        *(uint32_t *)(v_stack_m70) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x8)));
    }
    goto loc_007CC974;
loc_007CC974:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x4` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007CC424&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
