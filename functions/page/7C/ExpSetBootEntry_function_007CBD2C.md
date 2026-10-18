# ExpSetBootEntry

- RVA: `0x007CBD2C`–`0x007CC41B` (길이 `1,775` bytes)
- VA: `0x00000001407CBD2C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D51DC`
- 디코드: `462`개 명령, `1,775/1,775` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x007CBDED` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x007CBE0B` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x007CBE4D` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x007CBE73` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007CBE98` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007CBEFF` → [strcmp](../../text/6C/strcmp_function_006C7000.md) (function, `0x006C7000`)
- `0x007CBF1D` → [ExpVerifyWindowsOsOptions](../A2/ExpVerifyWindowsOsOptions_function_00A24CD8.md) (function, `0x00A24CD8`)
- `0x007CBF52` → [ExpSafeWcslen](../A2/ExpSafeWcslen_function_00A25698.md) (function, `0x00A25698`)
- `0x007CBF73` → [ExpVerifyFilePath](../A2/ExpVerifyFilePath_function_00A257F0.md) (function, `0x00A257F0`)
- `0x007CBFBA` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (function, `0x006B0BD0`)
- `0x007CBFDB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007CC017` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (function, `0x006B0BD0`)
- `0x007CC058` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (function, `0x006B0BD0`)
- `0x007CC093` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007CC0E5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007CC102` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007CC128` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007CC14D` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (function, `0x006B0BD0`)
- `0x007CC16C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007CC189` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x007CC1D2` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x007CC1F5` → [IoGetEnvironmentVariableEx](../95/IoGetEnvironmentVariableEx_function_00952760.md) (function, `0x00952760`)
- `0x007CC229` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x007CC24C` → [IoGetEnvironmentVariableEx](../95/IoGetEnvironmentVariableEx_function_00952760.md) (function, `0x00952760`)
- `0x007CC2A8` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x007CC2D2` → [IoGetEnvironmentVariableEx](../95/IoGetEnvironmentVariableEx_function_00952760.md) (function, `0x00952760`)
- `0x007CC30D` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x007CC330` → [IoGetEnvironmentVariableEx](../95/IoGetEnvironmentVariableEx_function_00952760.md) (function, `0x00952760`)
- `0x007CC360` → [IoSetEnvironmentVariableEx](../A9/IoSetEnvironmentVariableEx_function_00A91A84.md) (function, `0x00A91A84`)
- `0x007CC36E` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x007CC373` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007CC391` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007CC3A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007CC3B1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007CC3E6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007CC3F8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtAddBootEntry](NtAddBootEntry_function_007CD250.md) at `0x007CD26F`
- [NtModifyBootEntry](NtModifyBootEntry_function_007CDC80.md) at `0x007CDC9C`

### Static image references
- `0x007CBD47` → RVA `0x00E0A740` (`.data`; read)
- `0x007CBE46` → RVA `0x00FD9AB8` (`PAGEDATA`; read)
- `0x007CBEF4` → RVA `0x00B08730` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007CC182` → RVA `0x00EFAB40` (`.data`; read)
- `0x007CC1A2` → RVA `0x00019EF0` (`.rdata`; read)
- `0x007CC1C0` → RVA `0x00B08740` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007CC217` → RVA `0x00B08700` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x007CBDED` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x007CBE73` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007CBE98` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007CBEFF` → [strcmp](../../text/6C/strcmp_function_006C7000.md) (`PAGE` → `.text`)
  - `0x007CBFBA` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (`PAGE` → `.text`)
  - `0x007CBFDB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007CC017` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (`PAGE` → `.text`)
  - `0x007CC058` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (`PAGE` → `.text`)
  - `0x007CC093` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007CC0E5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007CC102` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007CC128` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007CC14D` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (`PAGE` → `.text`)
  - `0x007CC16C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007CC189` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (`PAGE` → `.text`)
  - `0x007CC1D2` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x007CC229` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x007CC2A8` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x007CC30D` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x007CC36E` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x007CC373` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007CC391` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007CC3A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007CC3B1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007CC3E6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007CC3F8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007CBD2C  4C 8B DC                        mov r11, rsp
007CBD2F  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
007CBD33  49 89 73 20                     mov qword ptr [r11 + 0x20], rsi
007CBD37  57                              push rdi
007CBD38  41 54                           push r12
007CBD3A  41 55                           push r13
007CBD3C  41 56                           push r14
007CBD3E  41 57                           push r15
007CBD40  48 81 EC C0 00 00 00            sub rsp, 0xc0
007CBD47  48 8B 05 F2 E9 63 00            mov rax, qword ptr [rip + 0x63e9f2]
007CBD4E  48 33 C4                        xor rax, rsp
007CBD51  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
007CBD59  4D 8B F8                        mov r15, r8
007CBD5C  4C 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], r8
007CBD64  4C 8B F2                        mov r14, rdx
007CBD67  44 8B E9                        mov r13d, ecx
007CBD6A  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
007CBD6E  33 C9                           xor ecx, ecx
007CBD70  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
007CBD75  44 8B E1                        mov r12d, ecx
007CBD78  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
007CBD7C  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
007CBD81  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
007CBD86  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
007CBD8B  89 4C 24 3C                     mov dword ptr [rsp + 0x3c], ecx
007CBD8F  89 4C 24 4C                     mov dword ptr [rsp + 0x4c], ecx
007CBD93  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
007CBD97  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007CBDA0  49 89 43 B0                     mov qword ptr [r11 - 0x50], rax
007CBDA4  40 8A B8 32 02 00 00            mov dil, byte ptr [rax + 0x232]
007CBDAB  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
007CBDB0  48 8D 72 04                     lea rsi, [rdx + 4]
007CBDB4  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
007CBDBE  40 84 FF                        test dil, dil
007CBDC1  74 15                           je 0x1407cbdd8
007CBDC3  48 3B F3                        cmp rsi, rbx
007CBDC6  48 0F 43 F3                     cmovae rsi, rbx
007CBDCA  90                              nop
007CBDCB  8B 36                           mov esi, dword ptr [rsi]
007CBDCD  89 74 24 54                     mov dword ptr [rsp + 0x54], esi
007CBDD1  40 8A 7C 24 30                  mov dil, byte ptr [rsp + 0x30]
007CBDD6  EB 06                           jmp 0x1407cbdde
007CBDD8  8B 36                           mov esi, dword ptr [rsi]
007CBDDA  89 74 24 54                     mov dword ptr [rsp + 0x54], esi
007CBDDE  83 FE 1C                        cmp esi, 0x1c
007CBDE1  73 0A                           jae 0x1407cbded
007CBDE3  B8 0D 00 00 C0                  mov eax, 0xc000000d
007CBDE8  E9 00 06 00 00                  jmp 0x1407cc3ed
007CBDED  E8 EE A4 C6 FF                  call 0x1404362e0
007CBDF2  84 C0                           test al, al
007CBDF4  74 0A                           je 0x1407cbe00
007CBDF6  B8 02 00 00 C0                  mov eax, 0xc0000002
007CBDFB  E9 ED 05 00 00                  jmp 0x1407cc3ed
007CBE00  40 84 FF                        test dil, dil
007CBE03  74 5F                           je 0x1407cbe64
007CBE05  41 F6 C6 03                     test r14b, 3
007CBE09  74 05                           je 0x1407cbe10
007CBE0B  E8 C0 E1 0C 00                  call 0x140899fd0
007CBE10  8B CE                           mov ecx, esi
007CBE12  49 03 CE                        add rcx, r14
007CBE15  48 3B CB                        cmp rcx, rbx
007CBE18  77 05                           ja 0x1407cbe1f
007CBE1A  49 3B CE                        cmp rcx, r14
007CBE1D  73 0B                           jae 0x1407cbe2a
007CBE1F  8A 03                           mov al, byte ptr [rbx]
007CBE21  40 8A 7C 24 30                  mov dil, byte ptr [rsp + 0x30]
007CBE26  8B 74 24 54                     mov esi, dword ptr [rsp + 0x54]
007CBE2A  4D 85 FF                        test r15, r15
007CBE2D  74 14                           je 0x1407cbe43
007CBE2F  4C 3B FB                        cmp r15, rbx
007CBE32  49 0F 42 DF                     cmovb rbx, r15
007CBE36  8B 03                           mov eax, dword ptr [rbx]
007CBE38  89 03                           mov dword ptr [rbx], eax
007CBE3A  40 8A 7C 24 30                  mov dil, byte ptr [rsp + 0x30]
007CBE3F  8B 74 24 54                     mov esi, dword ptr [rsp + 0x54]
007CBE43  40 8A D7                        mov dl, dil
007CBE46  48 8B 0D 6B DC 80 00            mov rcx, qword ptr [rip + 0x80dc6b]
007CBE4D  E8 CE 5F 0A 00                  call 0x140871e20
007CBE52  88 44 24 50                     mov byte ptr [rsp + 0x50], al
007CBE56  84 C0                           test al, al
007CBE58  75 0A                           jne 0x1407cbe64
007CBE5A  B8 61 00 00 C0                  mov eax, 0xc0000061
007CBE5F  E9 89 05 00 00                  jmp 0x1407cc3ed
007CBE64  8B DE                           mov ebx, esi
007CBE66  41 B8 45 6E 76 72               mov r8d, 0x72766e45
007CBE6C  8B D6                           mov edx, esi
007CBE6E  B9 40 00 00 00                  mov ecx, 0x40
007CBE73  E8 78 62 3B 00                  call 0x140b820f0
007CBE78  48 8B F8                        mov rdi, rax
007CBE7B  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
007CBE80  48 85 C0                        test rax, rax
007CBE83  75 0A                           jne 0x1407cbe8f
007CBE85  B8 9A 00 00 C0                  mov eax, 0xc000009a
007CBE8A  E9 5E 05 00 00                  jmp 0x1407cc3ed
007CBE8F  4C 8B C3                        mov r8, rbx
007CBE92  49 8B D6                        mov rdx, r14
007CBE95  48 8B CF                        mov rcx, rdi
007CBE98  E8 A3 A9 EF FF                  call 0x1406c6840
007CBE9D  90                              nop
007CBE9E  4C 8D 3C 3B                     lea r15, [rbx + rdi]
007CBEA2  83 3F 01                        cmp dword ptr [rdi], 1
007CBEA5  75 0E                           jne 0x1407cbeb5
007CBEA7  45 85 ED                        test r13d, r13d
007CBEAA  75 18                           jne 0x1407cbec4
007CBEAC  81 7F 08 FF FF 00 00            cmp dword ptr [rdi + 8], 0xffff
007CBEB3  76 0F                           jbe 0x1407cbec4
007CBEB5  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007CBEBA  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
007CBEBF  E9 BE 04 00 00                  jmp 0x1407cc382
007CBEC4  83 67 0C 13                     and dword ptr [rdi + 0xc], 0x13
007CBEC8  44 8B 67 10                     mov r12d, dword ptr [rdi + 0x10]
007CBECC  41 F6 C4 01                     test r12b, 1
007CBED0  75 3B                           jne 0x1407cbf0d
007CBED2  44 8B 6F 14                     mov r13d, dword ptr [rdi + 0x14]
007CBED6  41 F6 C5 03                     test r13b, 3
007CBEDA  75 31                           jne 0x1407cbf0d
007CBEDC  8B 5F 18                        mov ebx, dword ptr [rdi + 0x18]
007CBEDF  3B DE                           cmp ebx, esi
007CBEE1  77 2A                           ja 0x1407cbf0d
007CBEE3  48 8D 73 1C                     lea rsi, [rbx + 0x1c]
007CBEE7  48 03 F7                        add rsi, rdi
007CBEEA  49 3B F7                        cmp rsi, r15
007CBEED  73 1E                           jae 0x1407cbf0d
007CBEEF  83 FB 08                        cmp ebx, 8
007CBEF2  72 4D                           jb 0x1407cbf41
007CBEF4  48 8D 15 35 C8 33 00            lea rdx, [rip + 0x33c835]
007CBEFB  48 8D 4F 1C                     lea rcx, [rdi + 0x1c]
007CBEFF  E8 FC B0 EF FF                  call 0x1406c7000
007CBF04  85 C0                           test eax, eax
007CBF06  75 39                           jne 0x1407cbf41
007CBF08  83 FB 14                        cmp ebx, 0x14
007CBF0B  77 0A                           ja 0x1407cbf17
007CBF0D  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007CBF12  E9 63 04 00 00                  jmp 0x1407cc37a
007CBF17  8B D3                           mov edx, ebx
007CBF19  48 8D 4F 1C                     lea rcx, [rdi + 0x1c]
007CBF1D  E8 B6 8D 25 00                  call 0x140a24cd8
007CBF22  8B D8                           mov ebx, eax
007CBF24  85 C0                           test eax, eax
007CBF26  0F 88 4E 04 00 00               js 0x1407cc37a
007CBF2C  C7 44 24 58 01 00 00 00         mov dword ptr [rsp + 0x58], 1
007CBF34  44 8B 77 2C                     mov r14d, dword ptr [rdi + 0x2c]
007CBF38  48 8D 47 1C                     lea rax, [rdi + 0x1c]
007CBF3C  4C 03 F0                        add r14, rax
007CBF3F  EB 08                           jmp 0x1407cbf49
007CBF41  83 64 24 58 00                  and dword ptr [rsp + 0x58], 0
007CBF46  45 33 F6                        xor r14d, r14d
007CBF49  4C 03 E7                        add r12, rdi
007CBF4C  49 8B D7                        mov rdx, r15
007CBF4F  49 8B CC                        mov rcx, r12
007CBF52  E8 41 97 25 00                  call 0x140a25698
007CBF57  83 F8 FF                        cmp eax, -1
007CBF5A  74 B1                           je 0x1407cbf0d
007CBF5C  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
007CBF63  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
007CBF67  4A 8D 04 2F                     lea rax, [rdi + r13]
007CBF6B  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
007CBF70  48 8B C8                        mov rcx, rax
007CBF73  E8 78 98 25 00                  call 0x140a257f0
007CBF78  8B D8                           mov ebx, eax
007CBF7A  85 C0                           test eax, eax
007CBF7C  0F 88 F8 03 00 00               js 0x1407cc37a
007CBF82  49 3B F4                        cmp rsi, r12
007CBF85  77 86                           ja 0x1407cbf0d
007CBF87  44 8B 7C 24 5C                  mov r15d, dword ptr [rsp + 0x5c]
007CBF8C  45 8B EF                        mov r13d, r15d
007CBF8F  4B 8D 04 3C                     lea rax, [r12 + r15]
007CBF93  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
007CBF98  48 3B C6                        cmp rax, rsi
007CBF9B  0F 87 6C FF FF FF               ja 0x1407cbf0d
007CBFA1  83 7E 08 04                     cmp dword ptr [rsi + 8], 4
007CBFA5  0F 84 81 00 00 00               je 0x1407cc02c
007CBFAB  4C 8D 4C 24 3C                  lea r9, [rsp + 0x3c]
007CBFB0  45 33 C0                        xor r8d, r8d
007CBFB3  41 8D 50 04                     lea edx, [r8 + 4]
007CBFB7  48 8B CE                        mov rcx, rsi
007CBFBA  E8 11 4C EE FF                  call 0x1406b0bd0
007CBFBF  8B D8                           mov ebx, eax
007CBFC1  3D 23 00 00 C0                  cmp eax, 0xc0000023
007CBFC6  0F 85 AE 03 00 00               jne 0x1407cc37a
007CBFCC  8B 54 24 3C                     mov edx, dword ptr [rsp + 0x3c]
007CBFD0  B9 40 00 00 00                  mov ecx, 0x40
007CBFD5  41 B8 45 6E 76 72               mov r8d, 0x72766e45
007CBFDB  E8 10 61 3B 00                  call 0x140b820f0
007CBFE0  48 8B C8                        mov rcx, rax
007CBFE3  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007CBFE8  48 85 C0                        test rax, rax
007CBFEB  75 12                           jne 0x1407cbfff
007CBFED  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007CBFF2  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
007CBFF7  4C 8B E8                        mov r13, rax
007CBFFA  E9 83 03 00 00                  jmp 0x1407cc382
007CBFFF  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
007CC003  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
007CC007  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
007CC00C  4C 8B C1                        mov r8, rcx
007CC00F  BA 04 00 00 00                  mov edx, 4
007CC014  48 8B CE                        mov rcx, rsi
007CC017  E8 B4 4B EE FF                  call 0x1406b0bd0
007CC01C  8B D8                           mov ebx, eax
007CC01E  85 C0                           test eax, eax
007CC020  0F 88 84 00 00 00               js 0x1407cc0aa
007CC026  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
007CC02A  EB 08                           jmp 0x1407cc034
007CC02C  8B 46 04                        mov eax, dword ptr [rsi + 4]
007CC02F  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
007CC034  83 C0 F4                        add eax, -0xc
007CC037  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
007CC03B  83 7C 24 58 00                  cmp dword ptr [rsp + 0x58], 0
007CC040  74 35                           je 0x1407cc077
007CC042  41 83 7E 08 04                  cmp dword ptr [r14 + 8], 4
007CC047  74 2E                           je 0x1407cc077
007CC049  4C 8D 4C 24 4C                  lea r9, [rsp + 0x4c]
007CC04E  45 33 C0                        xor r8d, r8d
007CC051  41 8D 50 04                     lea edx, [r8 + 4]
007CC055  49 8B CE                        mov rcx, r14
007CC058  E8 73 4B EE FF                  call 0x1406b0bd0
007CC05D  8B D8                           mov ebx, eax
007CC05F  3D 23 00 00 C0                  cmp eax, 0xc0000023
007CC064  75 44                           jne 0x1407cc0aa
007CC066  8B 77 18                        mov esi, dword ptr [rdi + 0x18]
007CC069  41 2B 76 04                     sub esi, dword ptr [r14 + 4]
007CC06D  03 74 24 4C                     add esi, dword ptr [rsp + 0x4c]
007CC071  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
007CC075  EB 03                           jmp 0x1407cc07a
007CC077  8B 77 18                        mov esi, dword ptr [rdi + 0x18]
007CC07A  83 C0 06                        add eax, 6
007CC07D  03 C6                           add eax, esi
007CC07F  41 03 C7                        add eax, r15d
007CC082  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
007CC086  8B D0                           mov edx, eax
007CC088  B9 40 00 00 00                  mov ecx, 0x40
007CC08D  41 B8 45 6E 76 72               mov r8d, 0x72766e45
007CC093  E8 58 60 3B 00                  call 0x140b820f0
007CC098  48 8B D8                        mov rbx, rax
007CC09B  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
007CC0A0  48 85 C0                        test rax, rax
007CC0A3  75 0F                           jne 0x1407cc0b4
007CC0A5  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007CC0AA  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
007CC0AF  E9 06 FE FF FF                  jmp 0x1407cbeba
007CC0B4  83 20 00                        and dword ptr [rax], 0
007CC0B7  33 C9                           xor ecx, ecx
007CC0B9  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
007CC0BC  8D 51 01                        lea edx, [rcx + 1]
007CC0BF  84 C2                           test dl, al
007CC0C1  74 04                           je 0x1407cc0c7
007CC0C3  89 13                           mov dword ptr [rbx], edx
007CC0C5  8B CA                           mov ecx, edx
007CC0C7  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
007CC0CA  A8 10                           test al, 0x10
007CC0CC  74 05                           je 0x1407cc0d3
007CC0CE  83 C9 08                        or ecx, 8
007CC0D1  89 0B                           mov dword ptr [rbx], ecx
007CC0D3  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
007CC0D7  66 89 43 04                     mov word ptr [rbx + 4], ax
007CC0DB  48 8D 4B 06                     lea rcx, [rbx + 6]
007CC0DF  4D 8B C5                        mov r8, r13
007CC0E2  49 8B D4                        mov rdx, r12
007CC0E5  E8 56 A7 EF FF                  call 0x1406c6840
007CC0EA  49 83 C5 06                     add r13, 6
007CC0EE  49 03 DD                        add rbx, r13
007CC0F1  44 8B 44 24 3C                  mov r8d, dword ptr [rsp + 0x3c]
007CC0F6  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
007CC0FB  49 8D 55 0C                     lea rdx, [r13 + 0xc]
007CC0FF  48 8B CB                        mov rcx, rbx
007CC102  E8 39 A7 EF FF                  call 0x1406c6840
007CC107  44 8B 7C 24 3C                  mov r15d, dword ptr [rsp + 0x3c]
007CC10C  4C 03 FB                        add r15, rbx
007CC10F  83 7C 24 58 00                  cmp dword ptr [rsp + 0x58], 0
007CC114  74 4C                           je 0x1407cc162
007CC116  41 83 7E 08 04                  cmp dword ptr [r14 + 8], 4
007CC11B  74 45                           je 0x1407cc162
007CC11D  44 8B 47 2C                     mov r8d, dword ptr [rdi + 0x2c]
007CC121  48 8D 57 1C                     lea rdx, [rdi + 0x1c]
007CC125  49 8B CF                        mov rcx, r15
007CC128  E8 13 A7 EF FF                  call 0x1406c6840
007CC12D  41 89 77 0C                     mov dword ptr [r15 + 0xc], esi
007CC131  44 8B 47 2C                     mov r8d, dword ptr [rdi + 0x2c]
007CC135  4D 03 C7                        add r8, r15
007CC138  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
007CC13C  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
007CC140  4C 8D 4C 24 4C                  lea r9, [rsp + 0x4c]
007CC145  BA 04 00 00 00                  mov edx, 4
007CC14A  49 8B CE                        mov rcx, r14
007CC14D  E8 7E 4A EE FF                  call 0x1406b0bd0
007CC152  8B D8                           mov ebx, eax
007CC154  85 C0                           test eax, eax
007CC156  74 19                           je 0x1407cc171
007CC158  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
007CC15D  E9 20 02 00 00                  jmp 0x1407cc382
007CC162  44 8B C6                        mov r8d, esi
007CC165  48 8D 57 1C                     lea rdx, [rdi + 0x1c]
007CC169  49 8B CF                        mov rcx, r15
007CC16C  E8 CF A6 EF FF                  call 0x1406c6840
007CC171  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007CC17A  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
007CC181  90                              nop
007CC182  48 8D 0D B7 E9 72 00            lea rcx, [rip + 0x72e9b7]
007CC189  E8 92 75 C2 FF                  call 0x1403f3720
007CC18E  41 BF 09 00 00 00               mov r15d, 9
007CC194  83 7C 24 68 00                  cmp dword ptr [rsp + 0x68], 0
007CC199  0F 84 EB 00 00 00               je 0x1407cc28a
007CC19F  45 33 E4                        xor r12d, r12d
007CC1A2  48 8D 35 47 DD 84 FF            lea rsi, [rip - 0x7b22b9]
007CC1A9  BF FF FF 00 00                  mov edi, 0xffff
007CC1AE  41 BE 00 01 00 C0               mov r14d, 0xc0000100
007CC1B4  44 3B E7                        cmp r12d, edi
007CC1B7  0F 87 B4 00 00 00               ja 0x1407cc271
007CC1BD  45 8B CC                        mov r9d, r12d
007CC1C0  4C 8D 05 79 C5 33 00            lea r8, [rip + 0x33c579]
007CC1C7  49 8B D7                        mov rdx, r15
007CC1CA  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
007CC1D2  E8 49 89 D3 FF                  call 0x140504b20
007CC1D7  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
007CC1DC  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007CC1E2  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
007CC1E7  45 33 C0                        xor r8d, r8d
007CC1EA  48 8B D6                        mov rdx, rsi
007CC1ED  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
007CC1F5  E8 66 65 18 00                  call 0x140952760
007CC1FA  8B D8                           mov ebx, eax
007CC1FC  41 3B C6                        cmp eax, r14d
007CC1FF  75 52                           jne 0x1407cc253
007CC201  43 8D 04 24                     lea eax, [r12 + r12]
007CC205  41 0B C4                        or eax, r12d
007CC208  25 44 44 44 C4                  and eax, 0xc4444444
007CC20D  03 C0                           add eax, eax
007CC20F  41 85 C4                        test r12d, eax
007CC212  74 3F                           je 0x1407cc253
007CC214  45 8B CC                        mov r9d, r12d
007CC217  4C 8D 05 E2 C4 33 00            lea r8, [rip + 0x33c4e2]
007CC21E  49 8B D7                        mov rdx, r15
007CC221  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
007CC229  E8 F2 88 D3 FF                  call 0x140504b20
007CC22E  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
007CC233  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007CC239  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
007CC23E  45 33 C0                        xor r8d, r8d
007CC241  48 8B D6                        mov rdx, rsi
007CC244  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
007CC24C  E8 0F 65 18 00                  call 0x140952760
007CC251  8B D8                           mov ebx, eax
007CC253  41 3B DE                        cmp ebx, r14d
007CC256  74 14                           je 0x1407cc26c
007CC258  85 DB                           test ebx, ebx
007CC25A  74 08                           je 0x1407cc264
007CC25C  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
007CC262  75 12                           jne 0x1407cc276
007CC264  41 FF C4                        inc r12d
007CC267  E9 48 FF FF FF                  jmp 0x1407cc1b4
007CC26C  44 3B E7                        cmp r12d, edi
007CC26F  76 0F                           jbe 0x1407cc280
007CC271  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007CC276  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
007CC27B  E9 E7 00 00 00                  jmp 0x1407cc367
007CC280  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
007CC285  E9 B9 00 00 00                  jmp 0x1407cc343
007CC28A  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
007CC28F  44 8B 67 08                     mov r12d, dword ptr [rdi + 8]
007CC293  45 8B CC                        mov r9d, r12d
007CC296  4C 8D 05 63 C4 33 00            lea r8, [rip + 0x33c463]
007CC29D  49 8B D7                        mov rdx, r15
007CC2A0  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
007CC2A8  E8 73 88 D3 FF                  call 0x140504b20
007CC2AD  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
007CC2B2  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007CC2B8  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
007CC2BD  45 33 C0                        xor r8d, r8d
007CC2C0  48 8D 35 29 DC 84 FF            lea rsi, [rip - 0x7b23d7]
007CC2C7  48 8B D6                        mov rdx, rsi
007CC2CA  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
007CC2D2  E8 89 64 18 00                  call 0x140952760
007CC2D7  8B D8                           mov ebx, eax
007CC2D9  41 BE 00 01 00 C0               mov r14d, 0xc0000100
007CC2DF  41 3B C6                        cmp eax, r14d
007CC2E2  75 53                           jne 0x1407cc337
007CC2E4  44 8B 4F 08                     mov r9d, dword ptr [rdi + 8]
007CC2E8  43 8D 04 09                     lea eax, [r9 + r9]
007CC2EC  41 0B C1                        or eax, r9d
007CC2EF  25 44 44 44 C4                  and eax, 0xc4444444
007CC2F4  03 C0                           add eax, eax
007CC2F6  41 85 C1                        test r9d, eax
007CC2F9  74 3C                           je 0x1407cc337
007CC2FB  4C 8D 05 3E C4 33 00            lea r8, [rip + 0x33c43e]
007CC302  49 8B D7                        mov rdx, r15
007CC305  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
007CC30D  E8 0E 88 D3 FF                  call 0x140504b20
007CC312  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
007CC317  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007CC31D  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
007CC322  45 33 C0                        xor r8d, r8d
007CC325  48 8B D6                        mov rdx, rsi
007CC328  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
007CC330  E8 2B 64 18 00                  call 0x140952760
007CC335  8B D8                           mov ebx, eax
007CC337  85 DB                           test ebx, ebx
007CC339  74 08                           je 0x1407cc343
007CC33B  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
007CC341  75 24                           jne 0x1407cc367
007CC343  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
007CC34B  44 8B 4C 24 5C                  mov r9d, dword ptr [rsp + 0x5c]
007CC350  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
007CC355  48 8B D6                        mov rdx, rsi
007CC358  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
007CC360  E8 1F 57 2C 00                  call 0x140a91a84
007CC365  8B D8                           mov ebx, eax
007CC367  48 8D 0D D2 E7 72 00            lea rcx, [rip + 0x72e7d2]
007CC36E  E8 2D 40 A8 FF                  call 0x1402503a0
007CC373  E8 38 15 A9 FF                  call 0x14025d8b0
007CC378  EB 08                           jmp 0x1407cc382
007CC37A  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
007CC37F  45 8B EC                        mov r13d, r12d
007CC382  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
007CC387  48 85 C0                        test rax, rax
007CC38A  74 0A                           je 0x1407cc396
007CC38C  33 D2                           xor edx, edx
007CC38E  48 8B C8                        mov rcx, rax
007CC391  E8 DA 64 3B 00                  call 0x140b82870
007CC396  4D 85 ED                        test r13, r13
007CC399  74 11                           je 0x1407cc3ac
007CC39B  4C 3B 6C 24 78                  cmp r13, qword ptr [rsp + 0x78]
007CC3A0  74 0A                           je 0x1407cc3ac
007CC3A2  33 D2                           xor edx, edx
007CC3A4  49 8B CD                        mov rcx, r13
007CC3A7  E8 C4 64 3B 00                  call 0x140b82870
007CC3AC  33 D2                           xor edx, edx
007CC3AE  48 8B CF                        mov rcx, rdi
007CC3B1  E8 BA 64 3B 00                  call 0x140b82870
007CC3B6  90                              nop
007CC3B7  83 7C 24 68 00                  cmp dword ptr [rsp + 0x68], 0
007CC3BC  74 14                           je 0x1407cc3d2
007CC3BE  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
007CC3C6  48 85 C0                        test rax, rax
007CC3C9  74 07                           je 0x1407cc3d2
007CC3CB  85 DB                           test ebx, ebx
007CC3CD  78 03                           js 0x1407cc3d2
007CC3CF  44 89 20                        mov dword ptr [rax], r12d
007CC3D2  8B C3                           mov eax, ebx
007CC3D4  EB 17                           jmp 0x1407cc3ed
007CC3D6  EB 15                           jmp 0x1407cc3ed
007CC3D8  8B D8                           mov ebx, eax
007CC3DA  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007CC3DF  48 85 C9                        test rcx, rcx
007CC3E2  74 07                           je 0x1407cc3eb
007CC3E4  33 D2                           xor edx, edx
007CC3E6  E8 85 64 3B 00                  call 0x140b82870
007CC3EB  8B C3                           mov eax, ebx
007CC3ED  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
007CC3F5  48 33 CC                        xor rcx, rsp
007CC3F8  E8 43 02 EE FF                  call 0x1406ac640
007CC3FD  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
007CC405  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
007CC409  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
007CC40D  49 8B E3                        mov rsp, r11
007CC410  41 5F                           pop r15
007CC412  41 5E                           pop r14
007CC414  41 5D                           pop r13
007CC416  41 5C                           pop r12
007CC418  5F                              pop rdi
007CC419  C3                              ret
007CC41A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpSetBootEntry(int a1, __int64 a2, __int64 a3)
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
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int8 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int8 v_stack_mB8;
    unsigned __int64 v_stack_mC8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 6547954)) ^ (v_rsp);
    v_stack_m30 = result;
    v_stack_m68 = a3;
    v_stack_m80 = a1;
    a1 = 0;
    v_stack_m88 = 0;
    v_stack_mB4 = 0;
    v_stack_m70 = 0;
    v_stack_mA8 = 0;
    v_stack_m78 = 0;
    v_stack_mAC = 0;
    v_stack_m9C = 0;
    v_stack_mB0 = 0;
    *(unsigned __int64 *)(v_rsp - 80) = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_mB8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_007CBDD8;
    v_rsi = a2 + 4;
    if ((a2 + 4) >= v_rbx) { v_rsi = v_rbx; }
    v_stack_m94 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)));
    goto loc_007CBDDE;
loc_007CBDD8:
    v_stack_m94 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsi)))));
loc_007CBDDE:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsi)))))) >= 28) goto loc_007CBDED;
    goto loc_007CC3ED;
loc_007CBDED:
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_007CBE00;
    goto loc_007CC3ED;
loc_007CBE00:
    if ((unsigned __int8)(v_stack_mB8) == 0) goto loc_007CBE64;
    result = (unsigned int)(0xC0000002ULL);
    if ((((unsigned __int8)(a2)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
    }
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsi))))))) + (a2);
    if (a1 > v_rbx) goto loc_007CBE1F;
    v_rsi = (unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rsi))));
    v_rdi = v_stack_mB8;
    if (a1 < a2) {
        result = *(unsigned __int8 *)(v_rbx);
        v_rdi = v_stack_mB8;
        v_rsi = v_stack_m94;
    }
    if (a3 != 0) {
        if (a3 < v_rbx) { v_rbx = a3; }
        result = *(unsigned int *)(v_rbx);
        *(unsigned int *)(v_rbx) = (unsigned int)(result);
        v_rdi = v_stack_mB8;
        v_rsi = v_stack_m94;
    }
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 8445035), (unsigned __int8)(v_rdi), a3, a4);
    v_stack_m98 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) goto loc_007CBE64;
    goto loc_007CC3ED;
loc_007CBE64:
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x72766E45ULL), a4);
    v_stack_m88 = result;
    if (result != 0) goto loc_007CBE8F;
    goto loc_007CC3ED;
loc_007CBE8F:
    result = memcpy(result, a2, (unsigned int)((unsigned int)(v_rsi)), a4);
    if ((*(unsigned int *)(result)) != 1) goto loc_007CBEB5;
    if ((unsigned int)((unsigned int)(a1)) != 0) goto loc_007CBEC4;
    if ((*(unsigned int *)(result + 8)) <= 0xFFFFULL) goto loc_007CBEC4;
loc_007CBEB5:
loc_007CBEBA:
    goto loc_007CC382;
loc_007CBEC4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 16)))) & (1)) != 0) goto loc_007CBF0D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 20)))) & (3)) != 0) goto loc_007CBF0D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 24)))) > ((unsigned int)(v_rsi))) goto loc_007CBF0D;
    v_rsi = ((unsigned int)(*(unsigned int *)(result + 24)) + 28) + (result);
    if (v_rsi >= ((unsigned int)((unsigned int)(v_rsi)) + result * 1)) goto loc_007CBF0D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 24)))) < 8) goto loc_007CBF41;
    result = strcmp(result + 28, v_rip + 3393589, (unsigned int)((unsigned int)(v_rsi)), a4);
    if ((unsigned int)(result) != 0) goto loc_007CBF41;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 24)))) > 20) goto loc_007CBF17;
loc_007CBF0D:
    goto loc_007CC37A;
loc_007CBF17:
    result = ExpVerifyWindowsOsOptions(result + 28, (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))), (unsigned int)((unsigned int)(v_rsi)), a4);
    if (sign_flag) goto loc_007CC37A;
    v_stack_m90 = 1;
    v_r14 = ((unsigned int)(*(unsigned int *)(result + 44))) + (result + 28);
    goto loc_007CBF49;
loc_007CBF41:
    v_r14 = 0;
loc_007CBF49:
    v_r12 = ((unsigned int)(*(unsigned int *)(result + 16))) + (result);
    result = ExpSafeWcslen(v_r12, (unsigned int)((unsigned int)(v_rsi)) + result * 1, (unsigned int)((unsigned int)(v_rsi)), a4);
    if (((unsigned int)(result)) == -1) goto loc_007CBF0D;
    v_stack_m8C = (unsigned int)(result * 2 + 2);
    v_stack_m70 = result + (unsigned int)(*(unsigned int *)(result + 20)) * 1;
    result = ExpVerifyFilePath(result + (unsigned int)(*(unsigned int *)(result + 20)) * 1, (unsigned int)((unsigned int)(v_rsi)) + result * 1, (unsigned int)((unsigned int)(v_rsi)), a4);
    if (sign_flag) goto loc_007CC37A;
    if (v_rsi > v_r12) goto loc_007CBF0D;
    if ((v_r12 + (unsigned int)(v_stack_m8C) * 1) > v_stack_m70) goto loc_007CBF0D;
    if ((*(unsigned int *)(v_stack_m70 + 8)) == 4) goto loc_007CC02C;
    a3 = 0;
    result = ZwTranslateFilePath(v_stack_m70, a3 + 4, a3, v_stack_mAC);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_007CC37A;
    result = ExAllocatePool2(64, (unsigned int)(v_stack_mAC), (unsigned int)(0x72766E45ULL), v_stack_mAC);
    v_stack_mA8 = result;
    if (result != 0) goto loc_007CBFFF;
    goto loc_007CC382;
loc_007CBFFF:
    v_stack_mB0 = (unsigned int)((unsigned int)(v_stack_mAC));
    result = ZwTranslateFilePath(v_stack_m70, 4, result, v_stack_mB0);
    if (sign_flag) goto loc_007CC0AA;
    goto loc_007CC034;
loc_007CC02C:
    v_stack_mA8 = v_stack_m70;
loc_007CC034:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m70 + 4))) + (-12));
    v_stack_mAC = (unsigned int)(result);
    if (v_stack_m90 == 0) goto loc_007CC077;
    if ((*(unsigned int *)(v_r14 + 8)) == 4) goto loc_007CC077;
    a3 = 0;
    result = ZwTranslateFilePath(0, a3 + 4, a3, v_stack_m9C);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_007CC0AA;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 24))) - (*(unsigned int *)(v_r14 + 4)));
    v_rsi = (unsigned int)((v_rsi) + (v_stack_m9C));
    goto loc_007CC07A;
loc_007CC077:
loc_007CC07A:
    result = (unsigned int)(((unsigned int)(v_stack_mAC)) + (6));
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(*(unsigned int *)(result + 24)))));
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(v_stack_m8C))));
    v_stack_m8C = (unsigned int)(result);
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(result)), (unsigned int)(0x72766E45ULL), v_stack_m9C);
    v_stack_m78 = result;
    if (result != 0) goto loc_007CC0B4;
loc_007CC0AA:
    goto loc_007CBEBA;
loc_007CC0B4:
    a1 = 0;
    if ((((unsigned __int8)(a1 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12))))) != 0) {
        *(unsigned int *)((unsigned int)(0xC000009AULL)) = (unsigned int)(a1 + 1);
        a1 = (unsigned int)(a1 + 1);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (16)) != 0) {
        a1 = (unsigned int)((a1) | (8));
        *(unsigned int *)((unsigned int)(0xC000009AULL)) = a1;
    }
    *(unsigned __int16 *)((unsigned int)(0xC000009AULL) + 4) = (unsigned __int16)((unsigned int)(v_stack_mAC));
    result = memcpy((unsigned int)(0xC000009AULL) + 6, (unsigned int)(v_stack_mB4), result, v_stack_m9C);
    v_r13 = (result) + (6);
    v_rbx = ((unsigned int)(0xC000009AULL)) + (v_r13);
    result = memcpy(v_rbx, v_stack_mA8 + 12, (unsigned int)(v_stack_mAC), v_stack_m9C);
    v_r15 = ((unsigned int)(v_stack_mAC)) + (v_rbx);
    if (v_stack_m90 == 0) goto loc_007CC162;
    if ((*(unsigned int *)(v_r14 + 8)) == 4) goto loc_007CC162;
    result = memcpy(v_r15, result + 28, (unsigned int)(*(unsigned int *)(result + 44)), v_stack_m9C);
    *(unsigned int *)(v_r15 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 24)));
    a3 = ((unsigned int)(*(unsigned int *)(result + 44))) + (v_r15);
    v_stack_mB0 = (unsigned int)((unsigned int)(v_stack_m9C));
    result = ZwTranslateFilePath(0, 4, a3, v_stack_m9C);
    if ((unsigned int)(result) == 0) goto loc_007CC171;
    goto loc_007CC382;
loc_007CC162:
    result = memcpy(v_r15, result + 28, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 24)))), v_stack_m9C);
loc_007CC171:
    result = ExAcquireFastMutexUnsafe(v_rip + 7530935, result + 28, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 24)))), v_stack_m9C);
    if (v_stack_m80 == 0) goto loc_007CC28A;
    v_r12 = 0;
loc_007CC1B4:
    if (0 > ((unsigned int)((unsigned int)(0xFFFFULL)))) goto loc_007CC271;
    result = swprintf_s(v_stack_m48, 9, v_rip + 3392889, 0);
    a3 = 0;
    result = IoGetEnvironmentVariableEx(v_stack_m48, v_rip - 8069817, a3, v_stack_mB0);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000100ULL)))) goto loc_007CC253;
    result = (unsigned int)((v_r12 + v_r12 * 1) | (0));
    result = (unsigned int)((result) & (0xC4444444ULL));
    result = (unsigned int)((result) + ((unsigned int)(result)));
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((0) & ((unsigned int)(result))) != 0) {
        a4 = 0;
        a3 = v_rip + 3392738;
        a2 = 9;
        a1 = v_stack_m48;
        result = swprintf_s(a1, a2, a3, a4);
        a4 = v_stack_mB0;
        a3 = 0;
        a2 = v_rip - 8069817;
        a1 = v_stack_m48;
        result = IoGetEnvironmentVariableEx(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (((unsigned int)(v_rbx)) == ((unsigned int)((unsigned int)(0xC0000100ULL)))) goto loc_007CC26C;
    if ((unsigned int)(v_rbx) == 0) goto loc_007CC264;
    if (((unsigned int)(v_rbx)) != 0xC0000023ULL) goto loc_007CC276;
loc_007CC264:
    v_r12 = (unsigned int)((v_r12) + 1);
    goto loc_007CC1B4;
loc_007CC26C:
    if (((unsigned int)(v_r12)) <= ((unsigned int)((unsigned int)(0xFFFFULL)))) goto loc_007CC280;
loc_007CC271:
loc_007CC276:
    goto loc_007CC367;
loc_007CC280:
    goto loc_007CC343;
loc_007CC28A:
    result = swprintf_s(v_stack_m48, 9, v_rip + 3392611, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 8)))));
    a3 = 0;
    result = IoGetEnvironmentVariableEx(v_stack_m48, v_rip - 8070103, a3, v_stack_mB0);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000100ULL)))) goto loc_007CC337;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m88 + 8)) + (unsigned int)(*(unsigned int *)(v_stack_m88 + 8)) * 1) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 8)))));
    result = (unsigned int)((result) & (0xC4444444ULL));
    result = (unsigned int)((result) + ((unsigned int)(result)));
    v_rbx = (unsigned int)((unsigned int)(result));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 8)))) & ((unsigned int)(result))) != 0) {
        a3 = v_rip + 3392574;
        a2 = 9;
        a1 = v_stack_m48;
        result = swprintf_s(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m88 + 8)));
        a4 = v_stack_mB0;
        a3 = 0;
        a2 = v_rip - 8070103;
        a1 = v_stack_m48;
        result = IoGetEnvironmentVariableEx(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if ((unsigned int)(v_rbx) == 0) goto loc_007CC343;
    if (((unsigned int)(v_rbx)) == 0xC0000023ULL) {
        v_stack_mC8 = 1;
        a4 = v_stack_m8C;
        a3 = v_stack_m78;
        a2 = v_rip - 8070103;
        a1 = v_stack_m48;
        result = IoSetEnvironmentVariableEx(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    result = ExReleaseFastMutexUnsafe(v_rip + 7530450, a2, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 7530450, a2, a3, a4);
    goto loc_007CC382;
loc_007CC37A:
loc_007CC382:
    result = v_stack_m78;
    if (v_stack_m78 != 0) {
        a2 = 0;
        a1 = v_stack_m78;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_mB4))) == 0) goto loc_007CC3AC;
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_mB4)))) != v_stack_m70) {
        a2 = 0;
        a1 = (unsigned int)((unsigned int)((unsigned int)(v_stack_mB4)));
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m88, a2, a3, a4);
    if (v_stack_m80 == 0) goto loc_007CC3D2;
    if (v_stack_m68 == 0) goto loc_007CC3D2;
    if (!(sign_flag)) {
        *(unsigned int *)(v_stack_m68) = (unsigned int)((unsigned int)(v_stack_mB4));
    }
    goto loc_007CC3ED;
loc_007CC3ED:
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpSetBootEntry(int32_t Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m48;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint8_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint8_t v_stack_mB8;
    uint64_t v_stack_mC8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x63E9F2)) ^ (local_rsp);
    v_stack_m30 = result;
    v_stack_m68 = Arg3;
    v_stack_m80 = Arg1;
    Arg1 = 0;
    v_stack_m88 = 0;
    v_stack_mB4 = 0;
    v_stack_m70 = 0;
    v_stack_mA8 = 0;
    v_stack_m78 = 0;
    v_stack_mAC = 0;
    v_stack_m9C = 0;
    v_stack_mB0 = 0;
    *(uint64_t *)(local_rsp - 0x50) = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_mB8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_007CBDD8;
    local_rsi = Arg2 + 4;
    if ((Arg2 + 4) >= local_rbx) { local_rsi = local_rbx; }
    v_stack_m94 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)));
    goto loc_007CBDDE;
loc_007CBDD8:
    v_stack_m94 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsi)))));
loc_007CBDDE:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsi)))))) >= 28) goto loc_007CBDED;
    goto loc_007CC3ED;
loc_007CBDED:
    result = PsIsCurrentThreadInServerSilo(Arg1, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_007CBE00;
    goto loc_007CC3ED;
loc_007CBE00:
    if ((uint8_t)(v_stack_mB8) == 0) goto loc_007CBE64;
    result = (uint32_t)(0xC0000002ULL);
    if ((((uint8_t)(Arg2)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsi))))))) + (Arg2);
    if (Arg1 > local_rbx) goto loc_007CBE1F;
    local_rsi = (uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rsi))));
    local_rdi = v_stack_mB8;
    if (Arg1 < Arg2) {
        result = *(uint8_t *)(local_rbx);
        local_rdi = v_stack_mB8;
        local_rsi = v_stack_m94;
    }
    if (Arg3 != 0) {
        if (Arg3 < local_rbx) { local_rbx = Arg3; }
        result = *(uint32_t *)(local_rbx);
        *(uint32_t *)(local_rbx) = (uint32_t)(result);
        local_rdi = v_stack_mB8;
        local_rsi = v_stack_m94;
    }
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x80DC6B), (uint8_t)(local_rdi), Arg3, a4);
    v_stack_m98 = (uint8_t)(result);
    if ((uint8_t)(result) != 0) goto loc_007CBE64;
    goto loc_007CC3ED;
loc_007CBE64:
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x72766E45ULL), a4);
    v_stack_m88 = result;
    if (result != 0) goto loc_007CBE8F;
    goto loc_007CC3ED;
loc_007CBE8F:
    result = memcpy(result, Arg2, (uint32_t)((uint32_t)(local_rsi)), a4);
    if ((*(uint32_t *)(result)) != 1) goto loc_007CBEB5;
    if ((uint32_t)((uint32_t)(Arg1)) != 0) goto loc_007CBEC4;
    if ((*(uint32_t *)(result + 0x8)) <= 0xFFFFULL) goto loc_007CBEC4;
loc_007CBEB5:
loc_007CBEBA:
    goto loc_007CC382;
loc_007CBEC4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x10)))) & (1)) != 0) goto loc_007CBF0D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x14)))) & (3)) != 0) goto loc_007CBF0D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)))) > ((uint32_t)(local_rsi))) goto loc_007CBF0D;
    local_rsi = ((uint32_t)(*(uint32_t *)(result + 0x18)) + 28) + (result);
    if (local_rsi >= ((uint32_t)((uint32_t)(local_rsi)) + result * 1)) goto loc_007CBF0D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)))) < 8) goto loc_007CBF41;
    result = strcmp(result + 28, v_rip + 3393589, (uint32_t)((uint32_t)(local_rsi)), a4);
    if ((uint32_t)(result) != 0) goto loc_007CBF41;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)))) > 20) goto loc_007CBF17;
loc_007CBF0D:
    goto loc_007CC37A;
loc_007CBF17:
    result = ExpVerifyWindowsOsOptions(result + 28, (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))), (uint32_t)((uint32_t)(local_rsi)), a4);
    if (sign_flag) goto loc_007CC37A;
    v_stack_m90 = 1;
    local_r14 = ((uint32_t)(*(uint32_t *)(result + 0x2C))) + (result + 28);
    goto loc_007CBF49;
loc_007CBF41:
    local_r14 = 0;
loc_007CBF49:
    local_r12 = ((uint32_t)(*(uint32_t *)(result + 0x10))) + (result);
    result = ExpSafeWcslen(local_r12, (uint32_t)((uint32_t)(local_rsi)) + result * 1, (uint32_t)((uint32_t)(local_rsi)), a4);
    if (((uint32_t)(result)) == -1) goto loc_007CBF0D;
    v_stack_m8C = (uint32_t)(result * 2 + 2);
    v_stack_m70 = result + (uint32_t)(*(uint32_t *)(result + 0x14)) * 1;
    result = ExpVerifyFilePath(result + (uint32_t)(*(uint32_t *)(result + 0x14)) * 1, (uint32_t)((uint32_t)(local_rsi)) + result * 1, (uint32_t)((uint32_t)(local_rsi)), a4);
    if (sign_flag) goto loc_007CC37A;
    if (local_rsi > local_r12) goto loc_007CBF0D;
    if ((local_r12 + (uint32_t)(v_stack_m8C) * 1) > v_stack_m70) goto loc_007CBF0D;
    if ((*(uint32_t *)(v_stack_m70 + 0x8)) == 4) goto loc_007CC02C;
    Arg3 = 0;
    result = ZwTranslateFilePath(v_stack_m70, Arg3 + 4, Arg3, v_stack_mAC);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_007CC37A;
    result = ExAllocatePool2(64, (uint32_t)(v_stack_mAC), (uint32_t)(0x72766E45ULL), v_stack_mAC);
    v_stack_mA8 = result;
    if (result != 0) goto loc_007CBFFF;
    goto loc_007CC382;
loc_007CBFFF:
    v_stack_mB0 = (uint32_t)((uint32_t)(v_stack_mAC));
    result = ZwTranslateFilePath(v_stack_m70, 4, result, v_stack_mB0);
    if (sign_flag) goto loc_007CC0AA;
    goto loc_007CC034;
loc_007CC02C:
    v_stack_mA8 = v_stack_m70;
loc_007CC034:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x4))) + (-12));
    v_stack_mAC = (uint32_t)(result);
    if (v_stack_m90 == 0) goto loc_007CC077;
    if ((*(uint32_t *)(local_r14 + 0x8)) == 4) goto loc_007CC077;
    Arg3 = 0;
    result = ZwTranslateFilePath(0, Arg3 + 4, Arg3, v_stack_m9C);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_007CC0AA;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x18))) - (*(uint32_t *)(local_r14 + 0x4)));
    local_rsi = (uint32_t)((local_rsi) + (v_stack_m9C));
    goto loc_007CC07A;
loc_007CC077:
loc_007CC07A:
    result = (uint32_t)(((uint32_t)(v_stack_mAC)) + (6));
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)))));
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(v_stack_m8C))));
    v_stack_m8C = (uint32_t)(result);
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(result)), (uint32_t)(0x72766E45ULL), v_stack_m9C);
    v_stack_m78 = result;
    if (result != 0) goto loc_007CC0B4;
loc_007CC0AA:
    goto loc_007CBEBA;
loc_007CC0B4:
    Arg1 = 0;
    if ((((uint8_t)(Arg1 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC))))) != 0) {
        *(uint32_t *)((uint32_t)(0xC000009AULL)) = (uint32_t)(Arg1 + 1);
        Arg1 = (uint32_t)(Arg1 + 1);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (16)) != 0) {
        Arg1 = (uint32_t)((Arg1) | (8));
        *(uint32_t *)((uint32_t)(0xC000009AULL)) = Arg1;
    }
    *(uint16_t *)((uint32_t)(0xC000009AULL) + 0x4) = (uint16_t)((uint32_t)(v_stack_mAC));
    result = memcpy((uint32_t)(0xC000009AULL) + 6, (uint32_t)(v_stack_mB4), result, v_stack_m9C);
    local_r13 = (result) + (6);
    local_rbx = ((uint32_t)(0xC000009AULL)) + (local_r13);
    result = memcpy(local_rbx, v_stack_mA8 + 12, (uint32_t)(v_stack_mAC), v_stack_m9C);
    local_r15 = ((uint32_t)(v_stack_mAC)) + (local_rbx);
    if (v_stack_m90 == 0) goto loc_007CC162;
    if ((*(uint32_t *)(local_r14 + 0x8)) == 4) goto loc_007CC162;
    result = memcpy(local_r15, result + 28, (uint32_t)(*(uint32_t *)(result + 0x2C)), v_stack_m9C);
    *(uint32_t *)(local_r15 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)));
    Arg3 = ((uint32_t)(*(uint32_t *)(result + 0x2C))) + (local_r15);
    v_stack_mB0 = (uint32_t)((uint32_t)(v_stack_m9C));
    result = ZwTranslateFilePath(0, 4, Arg3, v_stack_m9C);
    if ((uint32_t)(result) == 0) goto loc_007CC171;
    goto loc_007CC382;
loc_007CC162:
    result = memcpy(local_r15, result + 28, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)))), v_stack_m9C);
loc_007CC171:
    result = ExAcquireFastMutexUnsafe(v_rip + 7530935, result + 28, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)))), v_stack_m9C);
    if (v_stack_m80 == 0) goto loc_007CC28A;
    local_r12 = 0;
loc_007CC1B4:
    if (0 > ((uint32_t)((uint32_t)(0xFFFFULL)))) goto loc_007CC271;
    result = swprintf_s(v_stack_m48, 9, v_rip + 3392889, 0);
    Arg3 = 0;
    result = IoGetEnvironmentVariableEx(v_stack_m48, v_rip - 8069817, Arg3, v_stack_mB0);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000100ULL)))) goto loc_007CC253;
    result = (uint32_t)((local_r12 + local_r12 * 1) | (0));
    result = (uint32_t)((result) & (0xC4444444ULL));
    result = (uint32_t)((result) + ((uint32_t)(result)));
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((0) & ((uint32_t)(result))) != 0) {
        a4 = 0;
        Arg3 = v_rip + 3392738;
        Arg2 = 9;
        Arg1 = v_stack_m48;
        result = swprintf_s(Arg1, Arg2, Arg3, a4);
        a4 = v_stack_mB0;
        Arg3 = 0;
        Arg2 = v_rip - 8069817;
        Arg1 = v_stack_m48;
        result = IoGetEnvironmentVariableEx(Arg1, Arg2, Arg3, a4);
        local_rbx = (uint32_t)(result);
    }
    if (((uint32_t)(local_rbx)) == ((uint32_t)((uint32_t)(0xC0000100ULL)))) goto loc_007CC26C;
    if ((uint32_t)(local_rbx) == 0) goto loc_007CC264;
    if (((uint32_t)(local_rbx)) != 0xC0000023ULL) goto loc_007CC276;
loc_007CC264:
    local_r12 = (uint32_t)((local_r12) + 1);
    goto loc_007CC1B4;
loc_007CC26C:
    if (((uint32_t)(local_r12)) <= ((uint32_t)((uint32_t)(0xFFFFULL)))) goto loc_007CC280;
loc_007CC271:
loc_007CC276:
    goto loc_007CC367;
loc_007CC280:
    goto loc_007CC343;
loc_007CC28A:
    result = swprintf_s(v_stack_m48, 9, v_rip + 3392611, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x8)))));
    Arg3 = 0;
    result = IoGetEnvironmentVariableEx(v_stack_m48, v_rip - 8070103, Arg3, v_stack_mB0);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000100ULL)))) goto loc_007CC337;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x8)) + (uint32_t)(*(uint32_t *)(v_stack_m88 + 0x8)) * 1) | ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x8)))));
    result = (uint32_t)((result) & (0xC4444444ULL));
    result = (uint32_t)((result) + ((uint32_t)(result)));
    local_rbx = (uint32_t)((uint32_t)(result));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x8)))) & ((uint32_t)(result))) != 0) {
        Arg3 = v_rip + 3392574;
        Arg2 = 9;
        Arg1 = v_stack_m48;
        result = swprintf_s(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m88 + 0x8)));
        a4 = v_stack_mB0;
        Arg3 = 0;
        Arg2 = v_rip - 8070103;
        Arg1 = v_stack_m48;
        result = IoGetEnvironmentVariableEx(Arg1, Arg2, Arg3, a4);
        local_rbx = (uint32_t)(result);
    }
    if ((uint32_t)(local_rbx) == 0) goto loc_007CC343;
    if (((uint32_t)(local_rbx)) == 0xC0000023ULL) {
        v_stack_mC8 = 1;
        a4 = v_stack_m8C;
        Arg3 = v_stack_m78;
        Arg2 = v_rip - 8070103;
        Arg1 = v_stack_m48;
        result = IoSetEnvironmentVariableEx(Arg1, Arg2, Arg3, a4);
        local_rbx = (uint32_t)(result);
    }
    result = ExReleaseFastMutexUnsafe(v_rip + 7530450, Arg2, Arg3, a4);
    result = KeLeaveCriticalRegion(v_rip + 7530450, Arg2, Arg3, a4);
    goto loc_007CC382;
loc_007CC37A:
loc_007CC382:
    result = v_stack_m78;
    if (v_stack_m78 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m78;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, a4);
    }
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_mB4))) == 0) goto loc_007CC3AC;
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_mB4)))) != v_stack_m70) {
        Arg2 = 0;
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(v_stack_mB4)));
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, a4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m88, Arg2, Arg3, a4);
    if (v_stack_m80 == 0) goto loc_007CC3D2;
    if (v_stack_m68 == 0) goto loc_007CC3D2;
    if (!(sign_flag)) {
        *(uint32_t *)(v_stack_m68) = (uint32_t)((uint32_t)(v_stack_mB4));
    }
    goto loc_007CC3ED;
loc_007CC3ED:
    Arg1 = (v_stack_m30) ^ (local_rsp);
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007CBD2C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
