# ExpUpdateProductSuiteTypeInRegistry

- RVA: `0x00C51BC0`–`0x00C52168` (길이 `1,448` bytes)
- VA: `0x0000000140C51BC0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D4A78`
- 디코드: `376`개 명령, `1,448/1,448` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **23**

### Outgoing calls
- `0x00C51C1D` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C51C3E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C51C69` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C51CA0` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C51CC9` → [NtSetValueKey](../../page/84/NtSetValueKey_function_00844EA0.md) (function, `0x00844EA0`)
- `0x00C51CE8` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C51CFA` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C51D06` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C51D3B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C51D50` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C51D83` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C51D93` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C51DC6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C51DD6` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C51E09` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C51E19` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C51E4C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C51E5C` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C51E8F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C51E9F` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C51ED2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C51EE2` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C51F15` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C51F25` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C51F58` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C51F68` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C51F9B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C51FAB` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C51FDE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C51FEE` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C52021` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C52031` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C52064` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C52074` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C520A7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C520B7` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (function, `0x004F80E0`)
- `0x00C520E4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C52112` → [NtSetValueKey](../../page/84/NtSetValueKey_function_00844EA0.md) (function, `0x00844EA0`)
- `0x00C52131` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C52141` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ExpWatchProductTypeInitialization](ExpWatchProductTypeInitialization_function_00C52170.md) at `0x00C524A3`

### Static image references
- `0x00C51BE6` → RVA `0x00E0A740` (`.data`; read)
- `0x00C51BF7` → RVA `0x00EFEE18` (`.data`; read)
- `0x00C51C25` → RVA `0x00EF0139` (`.data`; read)
- `0x00C51C32` → RVA `0x00B4AD80` (`PAGE`; read)
- `0x00C51C62` → RVA `0x00B4AD98` (`PAGE`; read)
- `0x00C51C8B` → RVA `0x00B4AD90` (`PAGE`; read)
- `0x00C51C94` → RVA `0x00B4AD88` (`PAGE`; read)
- `0x00C51CEE` → RVA `0x00B4ADA0` (`PAGE`; read)
- `0x00C51D0F` → RVA `0x00B4ADB8` (`PAGE`; read)
- `0x00C51D59` → RVA `0x00B4ADC0` (`PAGE`; read)
- `0x00C51D9C` → RVA `0x00B4ADD0` (`PAGE`; read)
- `0x00C51DDF` → RVA `0x00B4ADC8` (`PAGE`; read)
- `0x00C51E22` → RVA `0x00B4ADE0` (`PAGE`; read)
- `0x00C51E65` → RVA `0x00B4ADD8` (`PAGE`; read)
- `0x00C51EA8` → RVA `0x00B4ADE8` (`PAGE`; read)
- `0x00C51EEB` → RVA `0x00B4ADF0` (`PAGE`; read)
- `0x00C51F2E` → RVA `0x00B4ADF8` (`PAGE`; read)
- `0x00C51F71` → RVA `0x00B4AE00` (`PAGE`; read)
- `0x00C51FB4` → RVA `0x00B4AE08` (`PAGE`; read)
- `0x00C51FF7` → RVA `0x00B4AE10` (`PAGE`; read)
- `0x00C5203A` → RVA `0x00B4AE18` (`PAGE`; read)
- `0x00C5207D` → RVA `0x00B4AE20` (`PAGE`; read)
- `0x00C520C0` → RVA `0x00B4AE38` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **40**
  - `0x00C51C1D` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C51C3E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C51C69` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C51CA0` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C51CC9` → [NtSetValueKey](../../page/84/NtSetValueKey_function_00844EA0.md) (`INIT` → `PAGE`)
  - `0x00C51CE8` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C51CFA` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C51D06` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C51D3B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C51D50` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C51D83` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C51D93` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C51DC6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C51DD6` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C51E09` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C51E19` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C51E4C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C51E5C` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C51E8F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C51E9F` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C51ED2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C51EE2` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C51F15` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C51F25` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C51F58` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C51F68` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C51F9B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C51FAB` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C51FDE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C51FEE` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C52021` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C52031` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C52064` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C52074` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C520A7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C520B7` → [ExVerifySuite](../../text/4F/ExVerifySuite_function_004F80E0.md) (`INIT` → `.text`)
  - `0x00C520E4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C52112` → [NtSetValueKey](../../page/84/NtSetValueKey_function_00844EA0.md) (`INIT` → `PAGE`)
  - `0x00C52131` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C52141` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C51BC0  48 8B C4                        mov rax, rsp
00C51BC3  48 89 58 08                     mov qword ptr [rax + 8], rbx
00C51BC7  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00C51BCB  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00C51BCF  55                              push rbp
00C51BD0  41 54                           push r12
00C51BD2  41 55                           push r13
00C51BD4  41 56                           push r14
00C51BD6  41 57                           push r15
00C51BD8  48 8D A8 78 FD FF FF            lea rbp, [rax - 0x288]
00C51BDF  48 81 EC 60 03 00 00            sub rsp, 0x360
00C51BE6  48 8B 05 53 8B 1B 00            mov rax, qword ptr [rip + 0x1b8b53]
00C51BED  48 33 C4                        xor rax, rsp
00C51BF0  48 89 85 50 02 00 00            mov qword ptr [rbp + 0x250], rax
00C51BF7  4C 8B 25 1A D2 2A 00            mov r12, qword ptr [rip + 0x2ad21a]
00C51BFE  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00C51C03  0F 57 C0                        xorps xmm0, xmm0
00C51C06  0F 57 C9                        xorps xmm1, xmm1
00C51C09  BF F6 02 00 00                  mov edi, 0x2f6
00C51C0E  33 D2                           xor edx, edx
00C51C10  44 8B C7                        mov r8d, edi
00C51C13  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00C51C18  0F 11 4C 24 30                  movups xmmword ptr [rsp + 0x30], xmm1
00C51C1D  E8 1E 50 A7 FF                  call 0x1406c6c40
00C51C22  45 33 ED                        xor r13d, r13d
00C51C25  44 38 2D 0D E5 29 00            cmp byte ptr [rip + 0x29e50d], r13b
00C51C2C  0F 85 05 05 00 00               jne 0x140c52137
00C51C32  48 8B 15 47 91 EF FF            mov rdx, qword ptr [rip - 0x106eb9]
00C51C39  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00C51C3E  E8 3D 8B 7D FF                  call 0x14042a780
00C51C43  48 B9 64 02 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000264
00C51C4D  49 83 CE FF                     or r14, 0xffffffffffffffff
00C51C51  8B 09                           mov ecx, dword ptr [rcx]
00C51C53  83 E9 02                        sub ecx, 2
00C51C56  74 3C                           je 0x140c51c94
00C51C58  83 F9 01                        cmp ecx, 1
00C51C5B  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00C51C60  74 29                           je 0x140c51c8b
00C51C62  48 8B 15 2F 91 EF FF            mov rdx, qword ptr [rip - 0x106ed1]
00C51C69  E8 12 8B 7D FF                  call 0x14042a780
00C51C6E  48 8B 0D 23 91 EF FF            mov rcx, qword ptr [rip - 0x106edd]
00C51C75  49 8B C6                        mov rax, r14
00C51C78  48 FF C0                        inc rax
00C51C7B  66 44 39 2C 41                  cmp word ptr [rcx + rax*2], r13w
00C51C80  75 F6                           jne 0x140c51c78
00C51C82  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
00C51C89  EB 1F                           jmp 0x140c51caa
00C51C8B  48 8B 15 FE 90 EF FF            mov rdx, qword ptr [rip - 0x106f02]
00C51C92  EB 0C                           jmp 0x140c51ca0
00C51C94  48 8B 15 ED 90 EF FF            mov rdx, qword ptr [rip - 0x106f13]
00C51C9B  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00C51CA0  E8 DB 8A 7D FF                  call 0x14042a780
00C51CA5  B8 12 00 00 00                  mov eax, 0x12
00C51CAA  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00C51CAE  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00C51CB3  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00C51CB8  41 B9 01 00 00 00               mov r9d, 1
00C51CBE  45 33 C0                        xor r8d, r8d
00C51CC1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C51CC6  49 8B CC                        mov rcx, r12
00C51CC9  E8 D2 31 BF FF                  call 0x140844ea0
00C51CCE  85 C0                           test eax, eax
00C51CD0  79 1C                           jns 0x140c51cee
00C51CD2  BA 11 00 00 00                  mov edx, 0x11
00C51CD7  44 8B C0                        mov r8d, eax
00C51CDA  B9 9A 00 00 00                  mov ecx, 0x9a
00C51CDF  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C51CE4  44 8D 4A F0                     lea r9d, [rdx - 0x10]
00C51CE8  E8 73 B9 8A FF                  call 0x1404fd660
00C51CED  CC                              int3
00C51CEE  48 8B 15 AB 90 EF FF            mov rdx, qword ptr [rip - 0x106f55]
00C51CF5  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00C51CFA  E8 81 8A 7D FF                  call 0x14042a780
00C51CFF  33 C9                           xor ecx, ecx
00C51D01  48 8D 74 24 50                  lea rsi, [rsp + 0x50]
00C51D06  E8 D5 63 8A FF                  call 0x1404f80e0
00C51D0B  84 C0                           test al, al
00C51D0D  74 3C                           je 0x140c51d4b
00C51D0F  48 8B 15 A2 90 EF FF            mov rdx, qword ptr [rip - 0x106f5e]
00C51D16  49 8B C6                        mov rax, r14
00C51D19  48 FF C0                        inc rax
00C51D1C  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C51D21  75 F6                           jne 0x140c51d19
00C51D23  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C51D2B  44 3B FF                        cmp r15d, edi
00C51D2E  73 1B                           jae 0x140c51d4b
00C51D30  45 8B C7                        mov r8d, r15d
00C51D33  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00C51D38  41 8B DF                        mov ebx, r15d
00C51D3B  E8 00 4B A7 FF                  call 0x1406c6840
00C51D40  48 8D 74 24 50                  lea rsi, [rsp + 0x50]
00C51D45  48 03 F3                        add rsi, rbx
00C51D48  41 2B FF                        sub edi, r15d
00C51D4B  B9 01 00 00 00                  mov ecx, 1
00C51D50  E8 8B 63 8A FF                  call 0x1404f80e0
00C51D55  84 C0                           test al, al
00C51D57  74 35                           je 0x140c51d8e
00C51D59  48 8B 15 60 90 EF FF            mov rdx, qword ptr [rip - 0x106fa0]
00C51D60  49 8B C6                        mov rax, r14
00C51D63  48 FF C0                        inc rax
00C51D66  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C51D6B  75 F6                           jne 0x140c51d63
00C51D6D  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C51D75  41 3B FF                        cmp edi, r15d
00C51D78  76 14                           jbe 0x140c51d8e
00C51D7A  45 8B C7                        mov r8d, r15d
00C51D7D  48 8B CE                        mov rcx, rsi
00C51D80  41 8B DF                        mov ebx, r15d
00C51D83  E8 B8 4A A7 FF                  call 0x1406c6840
00C51D88  48 03 F3                        add rsi, rbx
00C51D8B  41 2B FF                        sub edi, r15d
00C51D8E  B9 02 00 00 00                  mov ecx, 2
00C51D93  E8 48 63 8A FF                  call 0x1404f80e0
00C51D98  84 C0                           test al, al
00C51D9A  74 35                           je 0x140c51dd1
00C51D9C  48 8B 15 2D 90 EF FF            mov rdx, qword ptr [rip - 0x106fd3]
00C51DA3  49 8B C6                        mov rax, r14
00C51DA6  48 FF C0                        inc rax
00C51DA9  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C51DAE  75 F6                           jne 0x140c51da6
00C51DB0  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C51DB8  41 3B FF                        cmp edi, r15d
00C51DBB  76 14                           jbe 0x140c51dd1
00C51DBD  45 8B C7                        mov r8d, r15d
00C51DC0  48 8B CE                        mov rcx, rsi
00C51DC3  41 8B DF                        mov ebx, r15d
00C51DC6  E8 75 4A A7 FF                  call 0x1406c6840
00C51DCB  48 03 F3                        add rsi, rbx
00C51DCE  41 2B FF                        sub edi, r15d
00C51DD1  B9 03 00 00 00                  mov ecx, 3
00C51DD6  E8 05 63 8A FF                  call 0x1404f80e0
00C51DDB  84 C0                           test al, al
00C51DDD  74 35                           je 0x140c51e14
00C51DDF  48 8B 15 E2 8F EF FF            mov rdx, qword ptr [rip - 0x10701e]
00C51DE6  49 8B C6                        mov rax, r14
00C51DE9  48 FF C0                        inc rax
00C51DEC  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C51DF1  75 F6                           jne 0x140c51de9
00C51DF3  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C51DFB  41 3B FF                        cmp edi, r15d
00C51DFE  76 14                           jbe 0x140c51e14
00C51E00  45 8B C7                        mov r8d, r15d
00C51E03  48 8B CE                        mov rcx, rsi
00C51E06  41 8B DF                        mov ebx, r15d
00C51E09  E8 32 4A A7 FF                  call 0x1406c6840
00C51E0E  48 03 F3                        add rsi, rbx
00C51E11  41 2B FF                        sub edi, r15d
00C51E14  B9 04 00 00 00                  mov ecx, 4
00C51E19  E8 C2 62 8A FF                  call 0x1404f80e0
00C51E1E  84 C0                           test al, al
00C51E20  74 35                           je 0x140c51e57
00C51E22  48 8B 15 B7 8F EF FF            mov rdx, qword ptr [rip - 0x107049]
00C51E29  49 8B C6                        mov rax, r14
00C51E2C  48 FF C0                        inc rax
00C51E2F  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C51E34  75 F6                           jne 0x140c51e2c
00C51E36  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C51E3E  41 3B FF                        cmp edi, r15d
00C51E41  76 14                           jbe 0x140c51e57
00C51E43  45 8B C7                        mov r8d, r15d
00C51E46  48 8B CE                        mov rcx, rsi
00C51E49  41 8B DF                        mov ebx, r15d
00C51E4C  E8 EF 49 A7 FF                  call 0x1406c6840
00C51E51  48 03 F3                        add rsi, rbx
00C51E54  41 2B FF                        sub edi, r15d
00C51E57  B9 05 00 00 00                  mov ecx, 5
00C51E5C  E8 7F 62 8A FF                  call 0x1404f80e0
00C51E61  84 C0                           test al, al
00C51E63  74 35                           je 0x140c51e9a
00C51E65  48 8B 15 6C 8F EF FF            mov rdx, qword ptr [rip - 0x107094]
00C51E6C  49 8B C6                        mov rax, r14
00C51E6F  48 FF C0                        inc rax
00C51E72  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C51E77  75 F6                           jne 0x140c51e6f
00C51E79  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C51E81  41 3B FF                        cmp edi, r15d
00C51E84  76 14                           jbe 0x140c51e9a
00C51E86  45 8B C7                        mov r8d, r15d
00C51E89  48 8B CE                        mov rcx, rsi
00C51E8C  41 8B DF                        mov ebx, r15d
00C51E8F  E8 AC 49 A7 FF                  call 0x1406c6840
00C51E94  48 03 F3                        add rsi, rbx
00C51E97  41 2B FF                        sub edi, r15d
00C51E9A  B9 06 00 00 00                  mov ecx, 6
00C51E9F  E8 3C 62 8A FF                  call 0x1404f80e0
00C51EA4  84 C0                           test al, al
00C51EA6  74 35                           je 0x140c51edd
00C51EA8  48 8B 15 39 8F EF FF            mov rdx, qword ptr [rip - 0x1070c7]
00C51EAF  49 8B C6                        mov rax, r14
00C51EB2  48 FF C0                        inc rax
00C51EB5  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C51EBA  75 F6                           jne 0x140c51eb2
00C51EBC  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C51EC4  41 3B FF                        cmp edi, r15d
00C51EC7  76 14                           jbe 0x140c51edd
00C51EC9  45 8B C7                        mov r8d, r15d
00C51ECC  48 8B CE                        mov rcx, rsi
00C51ECF  41 8B DF                        mov ebx, r15d
00C51ED2  E8 69 49 A7 FF                  call 0x1406c6840
00C51ED7  48 03 F3                        add rsi, rbx
00C51EDA  41 2B FF                        sub edi, r15d
00C51EDD  B9 07 00 00 00                  mov ecx, 7
00C51EE2  E8 F9 61 8A FF                  call 0x1404f80e0
00C51EE7  84 C0                           test al, al
00C51EE9  74 35                           je 0x140c51f20
00C51EEB  48 8B 15 FE 8E EF FF            mov rdx, qword ptr [rip - 0x107102]
00C51EF2  49 8B C6                        mov rax, r14
00C51EF5  48 FF C0                        inc rax
00C51EF8  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C51EFD  75 F6                           jne 0x140c51ef5
00C51EFF  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C51F07  41 3B FF                        cmp edi, r15d
00C51F0A  76 14                           jbe 0x140c51f20
00C51F0C  45 8B C7                        mov r8d, r15d
00C51F0F  48 8B CE                        mov rcx, rsi
00C51F12  41 8B DF                        mov ebx, r15d
00C51F15  E8 26 49 A7 FF                  call 0x1406c6840
00C51F1A  48 03 F3                        add rsi, rbx
00C51F1D  41 2B FF                        sub edi, r15d
00C51F20  B9 09 00 00 00                  mov ecx, 9
00C51F25  E8 B6 61 8A FF                  call 0x1404f80e0
00C51F2A  84 C0                           test al, al
00C51F2C  74 35                           je 0x140c51f63
00C51F2E  48 8B 15 C3 8E EF FF            mov rdx, qword ptr [rip - 0x10713d]
00C51F35  49 8B C6                        mov rax, r14
00C51F38  48 FF C0                        inc rax
00C51F3B  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C51F40  75 F6                           jne 0x140c51f38
00C51F42  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C51F4A  41 3B FF                        cmp edi, r15d
00C51F4D  76 14                           jbe 0x140c51f63
00C51F4F  45 8B C7                        mov r8d, r15d
00C51F52  48 8B CE                        mov rcx, rsi
00C51F55  41 8B DF                        mov ebx, r15d
00C51F58  E8 E3 48 A7 FF                  call 0x1406c6840
00C51F5D  48 03 F3                        add rsi, rbx
00C51F60  41 2B FF                        sub edi, r15d
00C51F63  B9 0A 00 00 00                  mov ecx, 0xa
00C51F68  E8 73 61 8A FF                  call 0x1404f80e0
00C51F6D  84 C0                           test al, al
00C51F6F  74 35                           je 0x140c51fa6
00C51F71  48 8B 15 88 8E EF FF            mov rdx, qword ptr [rip - 0x107178]
00C51F78  49 8B C6                        mov rax, r14
00C51F7B  48 FF C0                        inc rax
00C51F7E  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C51F83  75 F6                           jne 0x140c51f7b
00C51F85  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C51F8D  41 3B FF                        cmp edi, r15d
00C51F90  76 14                           jbe 0x140c51fa6
00C51F92  45 8B C7                        mov r8d, r15d
00C51F95  48 8B CE                        mov rcx, rsi
00C51F98  41 8B DF                        mov ebx, r15d
00C51F9B  E8 A0 48 A7 FF                  call 0x1406c6840
00C51FA0  48 03 F3                        add rsi, rbx
00C51FA3  41 2B FF                        sub edi, r15d
00C51FA6  B9 0B 00 00 00                  mov ecx, 0xb
00C51FAB  E8 30 61 8A FF                  call 0x1404f80e0
00C51FB0  84 C0                           test al, al
00C51FB2  74 35                           je 0x140c51fe9
00C51FB4  48 8B 15 4D 8E EF FF            mov rdx, qword ptr [rip - 0x1071b3]
00C51FBB  49 8B C6                        mov rax, r14
00C51FBE  48 FF C0                        inc rax
00C51FC1  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C51FC6  75 F6                           jne 0x140c51fbe
00C51FC8  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C51FD0  41 3B FF                        cmp edi, r15d
00C51FD3  76 14                           jbe 0x140c51fe9
00C51FD5  45 8B C7                        mov r8d, r15d
00C51FD8  48 8B CE                        mov rcx, rsi
00C51FDB  41 8B DF                        mov ebx, r15d
00C51FDE  E8 5D 48 A7 FF                  call 0x1406c6840
00C51FE3  48 03 F3                        add rsi, rbx
00C51FE6  41 2B FF                        sub edi, r15d
00C51FE9  B9 0C 00 00 00                  mov ecx, 0xc
00C51FEE  E8 ED 60 8A FF                  call 0x1404f80e0
00C51FF3  84 C0                           test al, al
00C51FF5  74 35                           je 0x140c5202c
00C51FF7  48 8B 15 12 8E EF FF            mov rdx, qword ptr [rip - 0x1071ee]
00C51FFE  49 8B C6                        mov rax, r14
00C52001  48 FF C0                        inc rax
00C52004  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C52009  75 F6                           jne 0x140c52001
00C5200B  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C52013  41 3B FF                        cmp edi, r15d
00C52016  76 14                           jbe 0x140c5202c
00C52018  45 8B C7                        mov r8d, r15d
00C5201B  48 8B CE                        mov rcx, rsi
00C5201E  41 8B DF                        mov ebx, r15d
00C52021  E8 1A 48 A7 FF                  call 0x1406c6840
00C52026  48 03 F3                        add rsi, rbx
00C52029  41 2B FF                        sub edi, r15d
00C5202C  B9 0D 00 00 00                  mov ecx, 0xd
00C52031  E8 AA 60 8A FF                  call 0x1404f80e0
00C52036  84 C0                           test al, al
00C52038  74 35                           je 0x140c5206f
00C5203A  48 8B 15 D7 8D EF FF            mov rdx, qword ptr [rip - 0x107229]
00C52041  49 8B C6                        mov rax, r14
00C52044  48 FF C0                        inc rax
00C52047  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C5204C  75 F6                           jne 0x140c52044
00C5204E  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C52056  41 3B FF                        cmp edi, r15d
00C52059  76 14                           jbe 0x140c5206f
00C5205B  45 8B C7                        mov r8d, r15d
00C5205E  48 8B CE                        mov rcx, rsi
00C52061  41 8B DF                        mov ebx, r15d
00C52064  E8 D7 47 A7 FF                  call 0x1406c6840
00C52069  48 03 F3                        add rsi, rbx
00C5206C  41 2B FF                        sub edi, r15d
00C5206F  B9 0E 00 00 00                  mov ecx, 0xe
00C52074  E8 67 60 8A FF                  call 0x1404f80e0
00C52079  84 C0                           test al, al
00C5207B  74 35                           je 0x140c520b2
00C5207D  48 8B 15 9C 8D EF FF            mov rdx, qword ptr [rip - 0x107264]
00C52084  49 8B C6                        mov rax, r14
00C52087  48 FF C0                        inc rax
00C5208A  66 44 39 2C 42                  cmp word ptr [rdx + rax*2], r13w
00C5208F  75 F6                           jne 0x140c52087
00C52091  44 8D 3C 45 02 00 00 00         lea r15d, [rax*2 + 2]
00C52099  41 3B FF                        cmp edi, r15d
00C5209C  76 14                           jbe 0x140c520b2
00C5209E  45 8B C7                        mov r8d, r15d
00C520A1  48 8B CE                        mov rcx, rsi
00C520A4  41 8B DF                        mov ebx, r15d
00C520A7  E8 94 47 A7 FF                  call 0x1406c6840
00C520AC  48 03 F3                        add rsi, rbx
00C520AF  41 2B FF                        sub edi, r15d
00C520B2  B9 10 00 00 00                  mov ecx, 0x10
00C520B7  E8 24 60 8A FF                  call 0x1404f80e0
00C520BC  84 C0                           test al, al
00C520BE  74 2C                           je 0x140c520ec
00C520C0  48 8B 15 71 8D EF FF            mov rdx, qword ptr [rip - 0x10728f]
00C520C7  49 FF C6                        inc r14
00C520CA  66 46 39 2C 72                  cmp word ptr [rdx + r14*2], r13w
00C520CF  75 F6                           jne 0x140c520c7
00C520D1  46 8D 34 75 02 00 00 00         lea r14d, [r14*2 + 2]
00C520D9  41 3B FE                        cmp edi, r14d
00C520DC  76 0E                           jbe 0x140c520ec
00C520DE  45 8B C6                        mov r8d, r14d
00C520E1  48 8B CE                        mov rcx, rsi
00C520E4  E8 57 47 A7 FF                  call 0x1406c6840
00C520E9  41 2B FE                        sub edi, r14d
00C520EC  B8 F8 02 00 00                  mov eax, 0x2f8
00C520F1  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00C520F6  2B C7                           sub eax, edi
00C520F8  41 B9 07 00 00 00               mov r9d, 7
00C520FE  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00C52102  45 33 C0                        xor r8d, r8d
00C52105  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00C5210A  49 8B CC                        mov rcx, r12
00C5210D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C52112  E8 89 2D BF FF                  call 0x140844ea0
00C52117  85 C0                           test eax, eax
00C52119  79 1C                           jns 0x140c52137
00C5211B  BA 11 00 00 00                  mov edx, 0x11
00C52120  44 8B C0                        mov r8d, eax
00C52123  B9 9A 00 00 00                  mov ecx, 0x9a
00C52128  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C5212D  44 8D 4A F1                     lea r9d, [rdx - 0xf]
00C52131  E8 2A B5 8A FF                  call 0x1404fd660
00C52136  CC                              int3
00C52137  48 8B 8D 50 02 00 00            mov rcx, qword ptr [rbp + 0x250]
00C5213E  48 33 CC                        xor rcx, rsp
00C52141  E8 FA A4 A5 FF                  call 0x1406ac640
00C52146  4C 8D 9C 24 60 03 00 00         lea r11, [rsp + 0x360]
00C5214E  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00C52152  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00C52156  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00C5215A  49 8B E3                        mov rsp, r11
00C5215D  41 5F                           pop r15
00C5215F  41 5E                           pop r14
00C52161  41 5D                           pop r13
00C52163  41 5C                           pop r12
00C52165  5D                              pop rbp
00C52166  C3                              ret
00C52167  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpUpdateProductSuiteTypeInRegistry(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m338;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_m350;
    unsigned __int64 v_stack_m358;
    unsigned int v_stack_m360;
    unsigned __int64 v_stack_m368;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (864);
    result = (*(unsigned __int64 *)(v_rip + 1805139)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 648 + 592) = result;
    a2 = 0;
    v_stack_m348 = v_xmm0;
    v_stack_m358 = v_xmm1;
    result = memset(v_stack_m338, a2, 758, a4);
    v_r13 = 0;
    if ((*(unsigned __int8 *)(v_rip + 2745613)) != 0) goto loc_00C52137;
    result = RtlInitUnicodeString(v_stack_m348, *(unsigned __int64 *)(v_rip - 1076921), 758, a4);
    v_r14 = (v_r14) | (-1);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m348))) - (2));
    if (condition_is_equal) goto loc_00C51C94;
    if (((unsigned int)(a1)) == 1) goto loc_00C51C8B;
    result = RtlInitUnicodeString(v_stack_m358, *(unsigned __int64 *)(v_rip - 1076945), 758, a4);
loc_00C51C78:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1076957) + result * 2)) != 0) goto loc_00C51C78;
    goto loc_00C51CAA;
loc_00C51C8B:
    goto loc_00C51CA0;
loc_00C51C94:
loc_00C51CA0:
    result = RtlInitUnicodeString(v_stack_m358, *(unsigned __int64 *)(v_rip - 1077011), 758, a4);
loc_00C51CAA:
    v_stack_m360 = 18;
    a3 = 0;
    v_stack_m368 = v_stack_m350;
    result = NtSetValueKey(*(unsigned __int64 *)(v_rip + 2806298), v_stack_m348, a3, 1);
    if (sign_flag) {
        a2 = 17;
        a3 = (unsigned int)(result);
        a1 = 154;
        v_stack_m368 = 0;
        a4 = a2 - 16;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = RtlInitUnicodeString(v_stack_m348, *(unsigned __int64 *)(v_rip - 1077077), a3, a4);
    a1 = 0;
    result = ExVerifySuite(a1, *(unsigned __int64 *)(v_rip - 1077077), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C51D4B;
loc_00C51D19:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077086) + result * 2)) != 0) goto loc_00C51D19;
    v_rsi = v_stack_m338;
    v_rdi = 758;
    if (((unsigned int)(result * 2 + 2)) < 758) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_stack_m338;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077086), a3, a4);
        v_rsi = v_stack_m338;
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((758) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(1, *(unsigned __int64 *)(v_rip - 1077086), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C51D8E;
loc_00C51D63:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077152) + result * 2)) != 0) goto loc_00C51D63;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077152), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(2, *(unsigned __int64 *)(v_rip - 1077152), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C51DD1;
loc_00C51DA6:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077203) + result * 2)) != 0) goto loc_00C51DA6;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077203), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(3, *(unsigned __int64 *)(v_rip - 1077203), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C51E14;
loc_00C51DE9:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077278) + result * 2)) != 0) goto loc_00C51DE9;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077278), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(4, *(unsigned __int64 *)(v_rip - 1077278), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C51E57;
loc_00C51E2C:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077321) + result * 2)) != 0) goto loc_00C51E2C;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077321), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(5, *(unsigned __int64 *)(v_rip - 1077321), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C51E9A;
loc_00C51E6F:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077396) + result * 2)) != 0) goto loc_00C51E6F;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077396), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(6, *(unsigned __int64 *)(v_rip - 1077396), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C51EDD;
loc_00C51EB2:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077447) + result * 2)) != 0) goto loc_00C51EB2;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077447), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(7, *(unsigned __int64 *)(v_rip - 1077447), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C51F20;
loc_00C51EF5:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077506) + result * 2)) != 0) goto loc_00C51EF5;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077506), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(9, *(unsigned __int64 *)(v_rip - 1077506), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C51F63;
loc_00C51F38:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077565) + result * 2)) != 0) goto loc_00C51F38;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077565), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(10, *(unsigned __int64 *)(v_rip - 1077565), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C51FA6;
loc_00C51F7B:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077624) + result * 2)) != 0) goto loc_00C51F7B;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077624), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(11, *(unsigned __int64 *)(v_rip - 1077624), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C51FE9;
loc_00C51FBE:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077683) + result * 2)) != 0) goto loc_00C51FBE;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077683), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(12, *(unsigned __int64 *)(v_rip - 1077683), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C5202C;
loc_00C52001:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077742) + result * 2)) != 0) goto loc_00C52001;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077742), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(13, *(unsigned __int64 *)(v_rip - 1077742), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C5206F;
loc_00C52044:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077801) + result * 2)) != 0) goto loc_00C52044;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077801), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(14, *(unsigned __int64 *)(v_rip - 1077801), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C520B2;
loc_00C52087:
    result = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077860) + result * 2)) != 0) goto loc_00C52087;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(result * 2 + 2))) {
        a3 = (unsigned int)(result * 2 + 2);
        a1 = v_rsi;
        v_rbx = (unsigned int)(result * 2 + 2);
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077860), a3, a4);
        v_rsi = (v_rsi) + (v_rbx);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result * 2 + 2)));
    }
    result = ExVerifySuite(16, *(unsigned __int64 *)(v_rip - 1077860), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C520EC;
loc_00C520C7:
    v_r14 = (v_r14) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 1077903) + v_r14 * 2)) != 0) goto loc_00C520C7;
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(v_r14 * 2 + 2))) {
        a3 = (unsigned int)(v_r14 * 2 + 2);
        a1 = v_rsi;
        result = memcpy(a1, *(unsigned __int64 *)(v_rip - 1077903), a3, a4);
        v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(v_r14 * 2 + 2)));
    }
    result = (unsigned int)((760) - ((unsigned int)(v_rdi)));
    v_stack_m360 = (unsigned int)(result);
    a3 = 0;
    v_stack_m368 = v_stack_m338;
    result = NtSetValueKey(*(unsigned __int64 *)(v_rip + 2806298), v_stack_m348, a3, 7);
    if (sign_flag) {
        a2 = 17;
        a3 = (unsigned int)(result);
        a1 = 154;
        v_stack_m368 = 0;
        a4 = a2 - 15;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 648 + 592)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpUpdateProductSuiteTypeInRegistry(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m338;
    uint64_t v_stack_m348;
    uint64_t v_stack_m350;
    uint64_t v_stack_m358;
    uint32_t v_stack_m360;
    uint64_t v_stack_m368;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (864);
    result = (*(uint64_t *)(v_rip + 0x1B8B53)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x288 + 0x250) = result;
    Arg2 = 0;
    v_stack_m348 = v_xmm0;
    v_stack_m358 = v_xmm1;
    result = memset(v_stack_m338, Arg2, 758, a4);
    local_r13 = 0;
    if ((*(uint8_t *)(v_rip + 0x29E50D)) != 0) goto loc_00C52137;
    result = RtlInitUnicodeString(v_stack_m348, *(uint64_t *)(v_rip - 0x106EB9), 758, a4);
    local_r14 = (local_r14) | (-1);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m348))) - (2));
    if (condition_is_equal) goto loc_00C51C94;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C51C8B;
    result = RtlInitUnicodeString(v_stack_m358, *(uint64_t *)(v_rip - 0x106ED1), 758, a4);
loc_00C51C78:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x106EDD) + result * 2)) != 0) goto loc_00C51C78;
    goto loc_00C51CAA;
loc_00C51C8B:
    goto loc_00C51CA0;
loc_00C51C94:
loc_00C51CA0:
    result = RtlInitUnicodeString(v_stack_m358, *(uint64_t *)(v_rip - 0x106F13), 758, a4);
loc_00C51CAA:
    v_stack_m360 = 18;
    a3 = 0;
    v_stack_m368 = v_stack_m350;
    result = NtSetValueKey(*(uint64_t *)(v_rip + 0x2AD21A), v_stack_m348, a3, 1);
    if (sign_flag) {
        Arg2 = 17;
        a3 = (uint32_t)(result);
        Arg1 = 154;
        v_stack_m368 = 0;
        a4 = Arg2 - 16;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = RtlInitUnicodeString(v_stack_m348, *(uint64_t *)(v_rip - 0x106F55), a3, a4);
    Arg1 = 0;
    result = ExVerifySuite(Arg1, *(uint64_t *)(v_rip - 0x106F55), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C51D4B;
loc_00C51D19:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x106F5E) + result * 2)) != 0) goto loc_00C51D19;
    local_rsi = v_stack_m338;
    local_rdi = 758;
    if (((uint32_t)(result * 2 + 2)) < 758) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = v_stack_m338;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x106F5E), a3, a4);
        local_rsi = v_stack_m338;
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((758) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(1, *(uint64_t *)(v_rip - 0x106F5E), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C51D8E;
loc_00C51D63:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x106FA0) + result * 2)) != 0) goto loc_00C51D63;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x106FA0), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(2, *(uint64_t *)(v_rip - 0x106FA0), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C51DD1;
loc_00C51DA6:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x106FD3) + result * 2)) != 0) goto loc_00C51DA6;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x106FD3), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(3, *(uint64_t *)(v_rip - 0x106FD3), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C51E14;
loc_00C51DE9:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x10701E) + result * 2)) != 0) goto loc_00C51DE9;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x10701E), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(4, *(uint64_t *)(v_rip - 0x10701E), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C51E57;
loc_00C51E2C:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x107049) + result * 2)) != 0) goto loc_00C51E2C;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x107049), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(5, *(uint64_t *)(v_rip - 0x107049), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C51E9A;
loc_00C51E6F:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x107094) + result * 2)) != 0) goto loc_00C51E6F;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x107094), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(6, *(uint64_t *)(v_rip - 0x107094), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C51EDD;
loc_00C51EB2:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x1070C7) + result * 2)) != 0) goto loc_00C51EB2;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x1070C7), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(7, *(uint64_t *)(v_rip - 0x1070C7), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C51F20;
loc_00C51EF5:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x107102) + result * 2)) != 0) goto loc_00C51EF5;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x107102), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(9, *(uint64_t *)(v_rip - 0x107102), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C51F63;
loc_00C51F38:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x10713D) + result * 2)) != 0) goto loc_00C51F38;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x10713D), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(10, *(uint64_t *)(v_rip - 0x10713D), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C51FA6;
loc_00C51F7B:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x107178) + result * 2)) != 0) goto loc_00C51F7B;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x107178), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(11, *(uint64_t *)(v_rip - 0x107178), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C51FE9;
loc_00C51FBE:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x1071B3) + result * 2)) != 0) goto loc_00C51FBE;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x1071B3), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(12, *(uint64_t *)(v_rip - 0x1071B3), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C5202C;
loc_00C52001:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x1071EE) + result * 2)) != 0) goto loc_00C52001;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x1071EE), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(13, *(uint64_t *)(v_rip - 0x1071EE), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C5206F;
loc_00C52044:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x107229) + result * 2)) != 0) goto loc_00C52044;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x107229), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(14, *(uint64_t *)(v_rip - 0x107229), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C520B2;
loc_00C52087:
    result = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x107264) + result * 2)) != 0) goto loc_00C52087;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(result * 2 + 2))) {
        a3 = (uint32_t)(result * 2 + 2);
        Arg1 = local_rsi;
        local_rbx = (uint32_t)(result * 2 + 2);
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x107264), a3, a4);
        local_rsi = (local_rsi) + (local_rbx);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result * 2 + 2)));
    }
    result = ExVerifySuite(16, *(uint64_t *)(v_rip - 0x107264), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C520EC;
loc_00C520C7:
    local_r14 = (local_r14) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x10728F) + local_r14 * 2)) != 0) goto loc_00C520C7;
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(local_r14 * 2 + 2))) {
        a3 = (uint32_t)(local_r14 * 2 + 2);
        Arg1 = local_rsi;
        result = memcpy(Arg1, *(uint64_t *)(v_rip - 0x10728F), a3, a4);
        local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(local_r14 * 2 + 2)));
    }
    result = (uint32_t)((760) - ((uint32_t)(local_rdi)));
    v_stack_m360 = (uint32_t)(result);
    a3 = 0;
    v_stack_m368 = v_stack_m338;
    result = NtSetValueKey(*(uint64_t *)(v_rip + 0x2AD21A), v_stack_m348, a3, 7);
    if (sign_flag) {
        Arg2 = 17;
        a3 = (uint32_t)(result);
        Arg1 = 154;
        v_stack_m368 = 0;
        a4 = Arg2 - 15;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x288 + 0x250)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C51BC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
