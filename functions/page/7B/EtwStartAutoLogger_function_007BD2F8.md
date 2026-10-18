# EtwStartAutoLogger

- RVA: `0x007BD2F8`–`0x007BE286` (길이 `3,982` bytes)
- VA: `0x00000001407BD2F8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D3CC0`
- 디코드: `835`개 명령, `3,982/3,982` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **28**

### Outgoing calls
- `0x007BD3C3` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x007BD3D7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007BD40C` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007BD431` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007BD45A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007BD47C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007BD4C5` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007BD55C` → [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) (function, `0x008C9050`)
- `0x007BD585` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007BD5D2` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x007BD5E4` → [EtwpCreateKeyTreeForPath](../../text/65/EtwpCreateKeyTreeForPath_function_0065287C.md) (function, `0x0065287C`)
- `0x007BD613` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x007BD695` → [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) (function, `0x008C9050`)
- `0x007BDBFF` → [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) (function, `0x008C9050`)
- `0x007BDDAB` → [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) (function, `0x008C9050`)
- `0x007BDE6C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007BDE91` → [EtwpParsePoolTagFilter](EtwpParsePoolTagFilter_function_007BE970.md) (function, `0x007BE970`)
- `0x007BDEDE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007BDF36` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007BDF7F` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x007BE002` → [RtlWriteRegistryValue](../A6/RtlWriteRegistryValue_function_00A6C620.md) (function, `0x00A6C620`)
- `0x007BE02B` → [wcscmp](../../text/50/wcscmp_function_00501AF0.md) (function, `0x00501AF0`)
- `0x007BE042` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x007BE07B` → [EtwpStartLogger](../A9/EtwpStartLogger_function_00A99D80.md) (function, `0x00A99D80`)
- `0x007BE148` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x007BE164` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x007BE179` → [EtwpUpdateDisallowList](../9E/EtwpUpdateDisallowList_function_009EA880.md) (function, `0x009EA880`)
- `0x007BE17E` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x007BE19D` → [EtwpEnableKeyProviders](EtwpEnableKeyProviders_function_007BE28C.md) (function, `0x007BE28C`)
- `0x007BE1BD` → [RtlNtStatusToDosError](../92/RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)
- `0x007BE1F6` → [RtlWriteRegistryValue](../A6/RtlWriteRegistryValue_function_00A6C620.md) (function, `0x00A6C620`)
- `0x007BE200` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007BE20F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007BE220` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x007BE22A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007BE239` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007BE242` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x007BE24B` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x007BE254` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x007BE265` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PerfDiagpStartPerfDiagLogger](../7A/PerfDiagpStartPerfDiagLogger_function_007AF144.md) at `0x007AF1ED`
- [EtwpEnumerateAutologgerPath](EtwpEnumerateAutologgerPath_function_007BE398.md) at `0x007BE5A1`
- [EtwpInitializeAutoLoggers](EtwpInitializeAutoLoggers_function_007BE694.md) at `0x007BE8E5`

### Static image references
- `0x007BD317` → RVA `0x00E0A740` (`.data`; read)
- `0x007BD4CF` → RVA `0x007BEA40` (`EtwpQueryRegistryCallback`; read)
- `0x007BD4FA` → RVA `0x00AFDF50` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD522` → RVA `0x00B07BA0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD6D8` → RVA `0x00B07B80` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD70D` → RVA `0x00B07AC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD734` → RVA `0x00B07AA0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD75B` → RVA `0x00B07B00` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD782` → RVA `0x00B07AE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD7A9` → RVA `0x00B07A40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD7E7` → RVA `0x00B067B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD817` → RVA `0x00B07A10` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD8C7` → RVA `0x00B07A80` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD8F9` → RVA `0x00B07A60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD92B` → RVA `0x00B079C0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD95D` → RVA `0x00B07980` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD985` → RVA `0x00B07A00` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD9B8` → RVA `0x00B079E0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BD9DF` → RVA `0x00B07D80` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BDA07` → RVA `0x00B07D60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BDAEA` → RVA `0x00B07DC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BDB11` → RVA `0x00B07D90` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BDB39` → RVA `0x00B07D00` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BDB6C` → RVA `0x00B07CE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BDF78` → RVA `0x00B07260` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BE024` → RVA `0x00B078D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007BE05E` → RVA `0x00B5A0B0` (`GlobalLoggerGuid`; read)
- `0x007BE1E2` → RVA `0x00AFF2C0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x007BD3C3` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x007BD3D7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007BD40C` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007BD431` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007BD45A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007BD47C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007BD4C5` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007BD585` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007BD5D2` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGE` → `.text`)
  - `0x007BD5E4` → [EtwpCreateKeyTreeForPath](../../text/65/EtwpCreateKeyTreeForPath_function_0065287C.md) (`PAGE` → `.text`)
  - `0x007BD613` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGE` → `.text`)
  - `0x007BDE6C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007BDEDE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007BDF36` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007BE02B` → [wcscmp](../../text/50/wcscmp_function_00501AF0.md) (`PAGE` → `.text`)
  - `0x007BE164` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x007BE17E` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x007BE200` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007BE20F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007BE22A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007BE239` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007BE265` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007BD2F8  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
007BD2FD  55                              push rbp
007BD2FE  56                              push rsi
007BD2FF  57                              push rdi
007BD300  41 54                           push r12
007BD302  41 55                           push r13
007BD304  41 56                           push r14
007BD306  41 57                           push r15
007BD308  48 8D AC 24 90 F9 FF FF         lea rbp, [rsp - 0x670]
007BD310  48 81 EC 70 07 00 00            sub rsp, 0x770
007BD317  48 8B 05 22 D4 64 00            mov rax, qword ptr [rip + 0x64d422]
007BD31E  48 33 C4                        xor rax, rsp
007BD321  48 89 85 60 06 00 00            mov qword ptr [rbp + 0x660], rax
007BD328  45 33 ED                        xor r13d, r13d
007BD32B  4C 89 45 D0                     mov qword ptr [rbp - 0x30], r8
007BD32F  33 C0                           xor eax, eax
007BD331  48 89 55 50                     mov qword ptr [rbp + 0x50], rdx
007BD335  0F 57 C0                        xorps xmm0, xmm0
007BD338  48 89 45 B4                     mov qword ptr [rbp - 0x4c], rax
007BD33C  48 89 45 94                     mov qword ptr [rbp - 0x6c], rax
007BD340  0F 57 C9                        xorps xmm1, xmm1
007BD343  48 89 45 84                     mov qword ptr [rbp - 0x7c], rax
007BD347  4C 8B F1                        mov r14, rcx
007BD34A  44 8D 78 01                     lea r15d, [rax + 1]
007BD34E  48 89 4D 48                     mov qword ptr [rbp + 0x48], rcx
007BD352  44 89 7D C0                     mov dword ptr [rbp - 0x40], r15d
007BD356  41 8B F5                        mov esi, r13d
007BD359  44 89 6D 0C                     mov dword ptr [rbp + 0xc], r13d
007BD35D  41 8B DD                        mov ebx, r13d
007BD360  44 89 6D 24                     mov dword ptr [rbp + 0x24], r13d
007BD364  0F 11 45 38                     movups xmmword ptr [rbp + 0x38], xmm0
007BD368  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
007BD36D  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
007BD372  44 89 6C 24 70                  mov dword ptr [rsp + 0x70], r13d
007BD377  44 89 6C 24 68                  mov dword ptr [rsp + 0x68], r13d
007BD37C  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
007BD380  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
007BD384  0F 11 4D F8                     movups xmmword ptr [rbp - 8], xmm1
007BD388  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
007BD38C  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
007BD390  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
007BD394  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
007BD399  44 89 6C 24 6C                  mov dword ptr [rsp + 0x6c], r13d
007BD39E  44 89 6C 24 54                  mov dword ptr [rsp + 0x54], r13d
007BD3A3  44 89 6C 24 44                  mov dword ptr [rsp + 0x44], r13d
007BD3A8  66 44 89 6C 24 40               mov word ptr [rsp + 0x40], r13w
007BD3AE  44 89 6D C8                     mov dword ptr [rbp - 0x38], r13d
007BD3B2  C7 45 C4 64 00 00 00            mov dword ptr [rbp - 0x3c], 0x64
007BD3B9  66 44 89 6C 24 60               mov word ptr [rsp + 0x60], r13w
007BD3BF  0F 11 45 58                     movups xmmword ptr [rbp + 0x58], xmm0
007BD3C3  E8 28 0E B4 FF                  call 0x1402fe1f0
007BD3C8  48 8B 88 40 03 00 00            mov rcx, qword ptr [rax + 0x340]
007BD3CF  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
007BD3D3  48 8D 4D 38                     lea rcx, [rbp + 0x38]
007BD3D7  E8 A4 D3 C6 FF                  call 0x14042a780
007BD3DC  48 8D 45 38                     lea rax, [rbp + 0x38]
007BD3E0  C7 45 08 30 00 00 00            mov dword ptr [rbp + 8], 0x30
007BD3E7  0F 57 C0                        xorps xmm0, xmm0
007BD3EA  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
007BD3EE  4C 8D 45 08                     lea r8, [rbp + 8]
007BD3F2  4C 89 6D 10                     mov qword ptr [rbp + 0x10], r13
007BD3F6  BA 1F 00 02 00                  mov edx, 0x2001f
007BD3FB  C7 45 20 40 02 00 00            mov dword ptr [rbp + 0x20], 0x240
007BD402  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
007BD407  F3 0F 7F 45 28                  movdqu xmmword ptr [rbp + 0x28], xmm0
007BD40C  E8 FF FE EE FF                  call 0x1406ad310
007BD411  45 8D 65 04                     lea r12d, [r13 + 4]
007BD415  8B F8                           mov edi, eax
007BD417  85 C0                           test eax, eax
007BD419  0F 88 8E 0D 00 00               js 0x1407be1ad
007BD41F  BF 45 74 77 50                  mov edi, 0x50777445
007BD424  BA 00 20 00 00                  mov edx, 0x2000
007BD429  44 8B C7                        mov r8d, edi
007BD42C  B9 00 01 00 00                  mov ecx, 0x100
007BD431  E8 BA 4C 3C 00                  call 0x140b820f0
007BD436  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007BD43B  48 8B F0                        mov rsi, rax
007BD43E  48 85 C0                        test rax, rax
007BD441  75 0A                           jne 0x1407bd44d
007BD443  BF 17 00 00 C0                  mov edi, 0xc0000017
007BD448  E9 60 0D 00 00                  jmp 0x1407be1ad
007BD44D  44 8B C7                        mov r8d, edi
007BD450  BA 04 05 00 00                  mov edx, 0x504
007BD455  B9 00 01 00 00                  mov ecx, 0x100
007BD45A  E8 91 4C 3C 00                  call 0x140b820f0
007BD45F  48 8B D8                        mov rbx, rax
007BD462  48 85 C0                        test rax, rax
007BD465  74 DC                           je 0x1407bd443
007BD467  48 8D 88 90 00 00 00            lea rcx, [rax + 0x90]
007BD46E  C7 40 2C 00 00 02 00            mov dword ptr [rax + 0x2c], 0x20000
007BD475  49 8B D6                        mov rdx, r14
007BD478  44 89 60 30                     mov dword ptr [rax + 0x30], r12d
007BD47C  E8 FF D2 C6 FF                  call 0x14042a780
007BD481  C7 43 48 00 00 00 80            mov dword ptr [rbx + 0x48], 0x80000000
007BD488  48 8D B3 B4 00 00 00            lea rsi, [rbx + 0xb4]
007BD48F  4C 8D 66 2C                     lea r12, [rsi + 0x2c]
007BD493  C6 43 4A FF                     mov byte ptr [rbx + 0x4a], 0xff
007BD497  4D 8D B4 24 04 04 00 00         lea r14, [r12 + 0x404]
007BD49F  66 C7 43 48 B0 00               mov word ptr [rbx + 0x48], 0xb0
007BD4A5  44 89 BB B0 00 00 00            mov dword ptr [rbx + 0xb0], r15d
007BD4AC  48 8D 8D C0 01 00 00            lea rcx, [rbp + 0x1c0]
007BD4B3  33 D2                           xor edx, edx
007BD4B5  4D 8D 6E 14                     lea r13, [r14 + 0x14]
007BD4B9  41 B8 98 04 00 00               mov r8d, 0x498
007BD4BF  41 BF B4 00 00 00               mov r15d, 0xb4
007BD4C5  E8 76 97 F0 FF                  call 0x1406c6c40
007BD4CA  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
007BD4CF  4C 8D 0D 6A 15 00 00            lea r9, [rip + 0x156a]
007BD4D6  B9 04 00 00 00                  mov ecx, 4
007BD4DB  4C 89 8D C0 01 00 00            mov qword ptr [rbp + 0x1c0], r9
007BD4E2  48 8D 45 70                     lea rax, [rbp + 0x70]
007BD4E6  89 8D E0 01 00 00               mov dword ptr [rbp + 0x1e0], ecx
007BD4EC  48 89 85 D8 01 00 00            mov qword ptr [rbp + 0x1d8], rax
007BD4F3  4C 8D 85 C0 01 00 00            lea r8, [rbp + 0x1c0]
007BD4FA  48 8D 05 4F 0A 34 00            lea rax, [rip + 0x340a4f]
007BD501  89 4D 70                        mov dword ptr [rbp + 0x70], ecx
007BD504  48 89 85 D0 01 00 00            mov qword ptr [rbp + 0x1d0], rax
007BD50B  48 8D 44 24 68                  lea rax, [rsp + 0x68]
007BD510  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
007BD514  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
007BD51B  48 89 85 10 02 00 00            mov qword ptr [rbp + 0x210], rax
007BD522  48 8D 05 77 A6 34 00            lea rax, [rip + 0x34a677]
007BD529  48 89 85 08 02 00 00            mov qword ptr [rbp + 0x208], rax
007BD530  48 8D 44 24 44                  lea rax, [rsp + 0x44]
007BD535  4C 89 8D F8 01 00 00            mov qword ptr [rbp + 0x1f8], r9
007BD53C  45 33 C9                        xor r9d, r9d
007BD53F  89 8D 18 02 00 00               mov dword ptr [rbp + 0x218], ecx
007BD545  89 8D 80 00 00 00               mov dword ptr [rbp + 0x80], ecx
007BD54B  B9 00 00 00 40                  mov ecx, 0x40000000
007BD550  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
007BD557  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
007BD55C  E8 EF BA 10 00                  call 0x1408c9050
007BD561  33 D2                           xor edx, edx
007BD563  8B F8                           mov edi, eax
007BD565  85 C0                           test eax, eax
007BD567  0F 88 35 0C 00 00               js 0x1407be1a2
007BD56D  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
007BD571  48 85 C0                        test rax, rax
007BD574  0F 84 C1 00 00 00               je 0x1407bd63b
007BD57A  89 54 24 64                     mov dword ptr [rsp + 0x64], edx
007BD57E  48 8D 4D 38                     lea rcx, [rbp + 0x38]
007BD582  48 8B D0                        mov rdx, rax
007BD585  E8 F6 D1 C6 FF                  call 0x14042a780
007BD58A  33 C9                           xor ecx, ecx
007BD58C  C7 45 08 30 00 00 00            mov dword ptr [rbp + 8], 0x30
007BD593  48 8D 45 38                     lea rax, [rbp + 0x38]
007BD597  48 89 4D 10                     mov qword ptr [rbp + 0x10], rcx
007BD59B  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
007BD59F  4C 8D 45 08                     lea r8, [rbp + 8]
007BD5A3  48 8D 44 24 64                  lea rax, [rsp + 0x64]
007BD5A8  C7 45 20 40 02 00 00            mov dword ptr [rbp + 0x20], 0x240
007BD5AF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007BD5B4  0F 57 C0                        xorps xmm0, xmm0
007BD5B7  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
007BD5BB  45 33 C9                        xor r9d, r9d
007BD5BE  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
007BD5C3  BA 1F 00 02 00                  mov edx, 0x2001f
007BD5C8  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
007BD5CD  F3 0F 7F 45 28                  movdqu xmmword ptr [rbp + 0x28], xmm0
007BD5D2  E8 99 FE EE FF                  call 0x1406ad470
007BD5D7  8B F8                           mov edi, eax
007BD5D9  3D 34 00 00 C0                  cmp eax, 0xc0000034
007BD5DE  75 3A                           jne 0x1407bd61a
007BD5E0  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
007BD5E4  E8 93 52 E9 FF                  call 0x14065287c
007BD5E9  33 D2                           xor edx, edx
007BD5EB  85 C0                           test eax, eax
007BD5ED  75 31                           jne 0x1407bd620
007BD5EF  48 8D 44 24 64                  lea rax, [rsp + 0x64]
007BD5F4  45 33 C9                        xor r9d, r9d
007BD5F7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007BD5FC  4C 8D 45 08                     lea r8, [rbp + 8]
007BD600  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
007BD604  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
007BD609  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
007BD60E  BA 1F 00 02 00                  mov edx, 0x2001f
007BD613  E8 58 FE EE FF                  call 0x1406ad470
007BD618  8B F8                           mov edi, eax
007BD61A  33 D2                           xor edx, edx
007BD61C  85 FF                           test edi, edi
007BD61E  74 07                           je 0x1407bd627
007BD620  8B FA                           mov edi, edx
007BD622  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
007BD627  41 B8 01 00 00 00               mov r8d, 1
007BD62D  44 39 44 24 64                  cmp dword ptr [rsp + 0x64], r8d
007BD632  75 0D                           jne 0x1407bd641
007BD634  44 89 44 24 44                  mov dword ptr [rsp + 0x44], r8d
007BD639  EB 06                           jmp 0x1407bd641
007BD63B  41 B8 01 00 00 00               mov r8d, 1
007BD641  39 54 24 44                     cmp dword ptr [rsp + 0x44], edx
007BD645  75 5C                           jne 0x1407bd6a3
007BD647  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007BD64C  48 85 C9                        test rcx, rcx
007BD64F  74 52                           je 0x1407bd6a3
007BD651  0F 57 C0                        xorps xmm0, xmm0
007BD654  44 88 44 24 28                  mov byte ptr [rsp + 0x28], r8b
007BD659  33 C0                           xor eax, eax
007BD65B  4C 8D 85 C0 01 00 00            lea r8, [rbp + 0x1c0]
007BD662  48 89 85 28 02 00 00            mov qword ptr [rbp + 0x228], rax
007BD669  48 8B D1                        mov rdx, rcx
007BD66C  48 8D 44 24 68                  lea rax, [rsp + 0x68]
007BD671  45 33 C9                        xor r9d, r9d
007BD674  B9 00 00 00 40                  mov ecx, 0x40000000
007BD679  48 89 85 E8 01 00 00            mov qword ptr [rbp + 0x1e8], rax
007BD680  0F 11 85 F8 01 00 00            movups xmmword ptr [rbp + 0x1f8], xmm0
007BD687  0F 11 85 08 02 00 00            movups xmmword ptr [rbp + 0x208], xmm0
007BD68E  0F 11 85 18 02 00 00            movups xmmword ptr [rbp + 0x218], xmm0
007BD695  E8 B6 B9 10 00                  call 0x1408c9050
007BD69A  33 D2                           xor edx, edx
007BD69C  8B F8                           mov edi, eax
007BD69E  85 C0                           test eax, eax
007BD6A0  0F 48 FA                        cmovs edi, edx
007BD6A3  39 54 24 68                     cmp dword ptr [rsp + 0x68], edx
007BD6A7  0F 84 F5 0A 00 00               je 0x1407be1a2
007BD6AD  BA 04 00 00 00                  mov edx, 4
007BD6B2  C7 45 B0 28 00 00 00            mov dword ptr [rbp - 0x50], 0x28
007BD6B9  4C 8D 05 80 13 00 00            lea r8, [rip + 0x1380]
007BD6C0  89 95 E0 01 00 00               mov dword ptr [rbp + 0x1e0], edx
007BD6C6  48 8D 45 70                     lea rax, [rbp + 0x70]
007BD6CA  4C 89 85 C0 01 00 00            mov qword ptr [rbp + 0x1c0], r8
007BD6D1  48 89 85 D8 01 00 00            mov qword ptr [rbp + 0x1d8], rax
007BD6D8  48 8D 05 A1 A4 34 00            lea rax, [rip + 0x34a4a1]
007BD6DF  48 89 85 D0 01 00 00            mov qword ptr [rbp + 0x1d0], rax
007BD6E6  44 8D 4A FF                     lea r9d, [rdx - 1]
007BD6EA  48 8D 43 4C                     lea rax, [rbx + 0x4c]
007BD6EE  89 55 70                        mov dword ptr [rbp + 0x70], edx
007BD6F1  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
007BD6F5  8D 4A FD                        lea ecx, [rdx - 3]
007BD6F8  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
007BD6FF  4C 89 85 F8 01 00 00            mov qword ptr [rbp + 0x1f8], r8
007BD706  48 89 85 10 02 00 00            mov qword ptr [rbp + 0x210], rax
007BD70D  48 8D 05 AC A3 34 00            lea rax, [rip + 0x34a3ac]
007BD714  48 89 85 08 02 00 00            mov qword ptr [rbp + 0x208], rax
007BD71B  48 8D 43 30                     lea rax, [rbx + 0x30]
007BD71F  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
007BD726  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
007BD72D  48 89 85 48 02 00 00            mov qword ptr [rbp + 0x248], rax
007BD734  48 8D 05 65 A3 34 00            lea rax, [rip + 0x34a365]
007BD73B  48 89 85 40 02 00 00            mov qword ptr [rbp + 0x240], rax
007BD742  48 8D 43 34                     lea rax, [rbx + 0x34]
007BD746  48 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], rax
007BD74D  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
007BD754  48 89 85 80 02 00 00            mov qword ptr [rbp + 0x280], rax
007BD75B  48 8D 05 9E A3 34 00            lea rax, [rip + 0x34a39e]
007BD762  48 89 85 78 02 00 00            mov qword ptr [rbp + 0x278], rax
007BD769  48 8D 43 44                     lea rax, [rbx + 0x44]
007BD76D  48 89 85 A8 00 00 00            mov qword ptr [rbp + 0xa8], rax
007BD774  48 8D 85 B0 00 00 00            lea rax, [rbp + 0xb0]
007BD77B  48 89 85 B8 02 00 00            mov qword ptr [rbp + 0x2b8], rax
007BD782  48 8D 05 57 A3 34 00            lea rax, [rip + 0x34a357]
007BD789  48 89 85 B0 02 00 00            mov qword ptr [rbp + 0x2b0], rax
007BD790  48 8D 43 38                     lea rax, [rbx + 0x38]
007BD794  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
007BD79B  48 8D 85 C0 00 00 00            lea rax, [rbp + 0xc0]
007BD7A2  48 89 85 F0 02 00 00            mov qword ptr [rbp + 0x2f0], rax
007BD7A9  48 8D 05 90 A2 34 00            lea rax, [rip + 0x34a290]
007BD7B0  48 89 85 E8 02 00 00            mov qword ptr [rbp + 0x2e8], rax
007BD7B7  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007BD7BC  48 89 85 00 03 00 00            mov qword ptr [rbp + 0x300], rax
007BD7C3  48 8D 83 80 00 00 00            lea rax, [rbx + 0x80]
007BD7CA  48 89 85 C8 00 00 00            mov qword ptr [rbp + 0xc8], rax
007BD7D1  48 8D 46 04                     lea rax, [rsi + 4]
007BD7D5  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
007BD7D9  48 8D 85 D0 00 00 00            lea rax, [rbp + 0xd0]
007BD7E0  48 89 85 28 03 00 00            mov qword ptr [rbp + 0x328], rax
007BD7E7  48 8D 05 C2 8F 34 00            lea rax, [rip + 0x348fc2]
007BD7EE  48 89 85 20 03 00 00            mov qword ptr [rbp + 0x320], rax
007BD7F5  48 8D 45 B0                     lea rax, [rbp - 0x50]
007BD7F9  48 89 85 D8 00 00 00            mov qword ptr [rbp + 0xd8], rax
007BD800  49 8D 44 24 04                  lea rax, [r12 + 4]
007BD805  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
007BD809  48 8D 85 E0 00 00 00            lea rax, [rbp + 0xe0]
007BD810  48 89 85 60 03 00 00            mov qword ptr [rbp + 0x360], rax
007BD817  48 8D 05 F2 A1 34 00            lea rax, [rip + 0x34a1f2]
007BD81E  48 89 85 58 03 00 00            mov qword ptr [rbp + 0x358], rax
007BD825  89 95 18 02 00 00               mov dword ptr [rbp + 0x218], edx
007BD82B  89 95 80 00 00 00               mov dword ptr [rbp + 0x80], edx
007BD831  4C 89 85 30 02 00 00            mov qword ptr [rbp + 0x230], r8
007BD838  89 95 50 02 00 00               mov dword ptr [rbp + 0x250], edx
007BD83E  89 95 90 00 00 00               mov dword ptr [rbp + 0x90], edx
007BD844  4C 89 85 68 02 00 00            mov qword ptr [rbp + 0x268], r8
007BD84B  89 95 88 02 00 00               mov dword ptr [rbp + 0x288], edx
007BD851  89 95 A0 00 00 00               mov dword ptr [rbp + 0xa0], edx
007BD857  4C 89 85 A0 02 00 00            mov qword ptr [rbp + 0x2a0], r8
007BD85E  89 95 C0 02 00 00               mov dword ptr [rbp + 0x2c0], edx
007BD864  89 95 B0 00 00 00               mov dword ptr [rbp + 0xb0], edx
007BD86A  4C 89 85 D8 02 00 00            mov qword ptr [rbp + 0x2d8], r8
007BD871  89 8D F8 02 00 00               mov dword ptr [rbp + 0x2f8], ecx
007BD877  89 8D C0 00 00 00               mov dword ptr [rbp + 0xc0], ecx
007BD87D  4C 89 85 10 03 00 00            mov qword ptr [rbp + 0x310], r8
007BD884  44 89 8D 30 03 00 00            mov dword ptr [rbp + 0x330], r9d
007BD88B  44 89 8D D0 00 00 00            mov dword ptr [rbp + 0xd0], r9d
007BD892  C7 45 80 00 04 00 00            mov dword ptr [rbp - 0x80], 0x400
007BD899  4C 89 85 48 03 00 00            mov qword ptr [rbp + 0x348], r8
007BD8A0  44 89 8D 68 03 00 00            mov dword ptr [rbp + 0x368], r9d
007BD8A7  48 8D 45 80                     lea rax, [rbp - 0x80]
007BD8AB  44 89 8D E0 00 00 00            mov dword ptr [rbp + 0xe0], r9d
007BD8B2  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
007BD8B9  48 8D 85 F0 00 00 00            lea rax, [rbp + 0xf0]
007BD8C0  48 89 85 98 03 00 00            mov qword ptr [rbp + 0x398], rax
007BD8C7  48 8D 05 B2 A1 34 00            lea rax, [rip + 0x34a1b2]
007BD8CE  48 89 85 90 03 00 00            mov qword ptr [rbp + 0x390], rax
007BD8D5  48 8D 45 C0                     lea rax, [rbp - 0x40]
007BD8D9  48 89 85 A8 03 00 00            mov qword ptr [rbp + 0x3a8], rax
007BD8E0  48 8D 43 28                     lea rax, [rbx + 0x28]
007BD8E4  48 89 85 F8 00 00 00            mov qword ptr [rbp + 0xf8], rax
007BD8EB  48 8D 85 00 01 00 00            lea rax, [rbp + 0x100]
007BD8F2  48 89 85 D0 03 00 00            mov qword ptr [rbp + 0x3d0], rax
007BD8F9  48 8D 05 60 A1 34 00            lea rax, [rip + 0x34a160]
007BD900  48 89 85 C8 03 00 00            mov qword ptr [rbp + 0x3c8], rax
007BD907  48 8D 45 C4                     lea rax, [rbp - 0x3c]
007BD90B  48 89 85 E0 03 00 00            mov qword ptr [rbp + 0x3e0], rax
007BD912  48 8D 43 3C                     lea rax, [rbx + 0x3c]
007BD916  48 89 85 08 01 00 00            mov qword ptr [rbp + 0x108], rax
007BD91D  48 8D 85 10 01 00 00            lea rax, [rbp + 0x110]
007BD924  48 89 85 08 04 00 00            mov qword ptr [rbp + 0x408], rax
007BD92B  48 8D 05 8E A0 34 00            lea rax, [rip + 0x34a08e]
007BD932  48 89 85 00 04 00 00            mov qword ptr [rbp + 0x400], rax
007BD939  48 8D 45 C8                     lea rax, [rbp - 0x38]
007BD93D  48 89 85 18 04 00 00            mov qword ptr [rbp + 0x418], rax
007BD944  48 8D 43 40                     lea rax, [rbx + 0x40]
007BD948  48 89 85 18 01 00 00            mov qword ptr [rbp + 0x118], rax
007BD94F  48 8D 85 20 01 00 00            lea rax, [rbp + 0x120]
007BD956  48 89 85 40 04 00 00            mov qword ptr [rbp + 0x440], rax
007BD95D  48 8D 05 1C A0 34 00            lea rax, [rip + 0x34a01c]
007BD964  48 89 85 38 04 00 00            mov qword ptr [rbp + 0x438], rax
007BD96B  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
007BD970  48 89 85 28 01 00 00            mov qword ptr [rbp + 0x128], rax
007BD977  48 8D 85 30 01 00 00            lea rax, [rbp + 0x130]
007BD97E  48 89 85 78 04 00 00            mov qword ptr [rbp + 0x478], rax
007BD985  48 8D 05 74 A0 34 00            lea rax, [rip + 0x34a074]
007BD98C  48 89 85 70 04 00 00            mov qword ptr [rbp + 0x470], rax
007BD993  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007BD998  48 89 85 88 04 00 00            mov qword ptr [rbp + 0x488], rax
007BD99F  48 8D 45 E8                     lea rax, [rbp - 0x18]
007BD9A3  48 89 85 38 01 00 00            mov qword ptr [rbp + 0x138], rax
007BD9AA  48 8D 85 40 01 00 00            lea rax, [rbp + 0x140]
007BD9B1  48 89 85 B0 04 00 00            mov qword ptr [rbp + 0x4b0], rax
007BD9B8  48 8D 05 21 A0 34 00            lea rax, [rip + 0x34a021]
007BD9BF  48 89 85 A8 04 00 00            mov qword ptr [rbp + 0x4a8], rax
007BD9C6  48 8D 43 60                     lea rax, [rbx + 0x60]
007BD9CA  48 89 85 48 01 00 00            mov qword ptr [rbp + 0x148], rax
007BD9D1  48 8D 85 50 01 00 00            lea rax, [rbp + 0x150]
007BD9D8  48 89 85 E8 04 00 00            mov qword ptr [rbp + 0x4e8], rax
007BD9DF  48 8D 05 9A A3 34 00            lea rax, [rip + 0x34a39a]
007BD9E6  48 89 85 E0 04 00 00            mov qword ptr [rbp + 0x4e0], rax
007BD9ED  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007BD9F2  48 89 85 58 01 00 00            mov qword ptr [rbp + 0x158], rax
007BD9F9  48 8D 85 60 01 00 00            lea rax, [rbp + 0x160]
007BDA00  48 89 85 20 05 00 00            mov qword ptr [rbp + 0x520], rax
007BDA07  48 8D 05 52 A3 34 00            lea rax, [rip + 0x34a352]
007BDA0E  4C 89 85 80 03 00 00            mov qword ptr [rbp + 0x380], r8
007BDA15  89 95 A0 03 00 00               mov dword ptr [rbp + 0x3a0], edx
007BDA1B  89 95 B0 03 00 00               mov dword ptr [rbp + 0x3b0], edx
007BDA21  89 95 F0 00 00 00               mov dword ptr [rbp + 0xf0], edx
007BDA27  4C 89 85 B8 03 00 00            mov qword ptr [rbp + 0x3b8], r8
007BDA2E  89 95 D8 03 00 00               mov dword ptr [rbp + 0x3d8], edx
007BDA34  89 95 E8 03 00 00               mov dword ptr [rbp + 0x3e8], edx
007BDA3A  89 95 00 01 00 00               mov dword ptr [rbp + 0x100], edx
007BDA40  4C 89 85 F0 03 00 00            mov qword ptr [rbp + 0x3f0], r8
007BDA47  89 95 10 04 00 00               mov dword ptr [rbp + 0x410], edx
007BDA4D  89 95 20 04 00 00               mov dword ptr [rbp + 0x420], edx
007BDA53  89 95 10 01 00 00               mov dword ptr [rbp + 0x110], edx
007BDA59  4C 89 85 28 04 00 00            mov qword ptr [rbp + 0x428], r8
007BDA60  89 95 48 04 00 00               mov dword ptr [rbp + 0x448], edx
007BDA66  89 95 20 01 00 00               mov dword ptr [rbp + 0x120], edx
007BDA6C  4C 89 85 60 04 00 00            mov qword ptr [rbp + 0x460], r8
007BDA73  89 8D 80 04 00 00               mov dword ptr [rbp + 0x480], ecx
007BDA79  89 8D 30 01 00 00               mov dword ptr [rbp + 0x130], ecx
007BDA7F  4C 89 85 98 04 00 00            mov qword ptr [rbp + 0x498], r8
007BDA86  89 95 B8 04 00 00               mov dword ptr [rbp + 0x4b8], edx
007BDA8C  89 95 40 01 00 00               mov dword ptr [rbp + 0x140], edx
007BDA92  4C 89 85 D0 04 00 00            mov qword ptr [rbp + 0x4d0], r8
007BDA99  89 95 F0 04 00 00               mov dword ptr [rbp + 0x4f0], edx
007BDA9F  89 95 50 01 00 00               mov dword ptr [rbp + 0x150], edx
007BDAA5  4C 89 85 08 05 00 00            mov qword ptr [rbp + 0x508], r8
007BDAAC  48 89 85 18 05 00 00            mov qword ptr [rbp + 0x518], rax
007BDAB3  44 8D 52 04                     lea r10d, [rdx + 4]
007BDAB7  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007BDABC  89 8D 28 05 00 00               mov dword ptr [rbp + 0x528], ecx
007BDAC2  48 89 85 30 05 00 00            mov qword ptr [rbp + 0x530], rax
007BDAC9  48 8D 45 F8                     lea rax, [rbp - 8]
007BDACD  48 89 85 68 01 00 00            mov qword ptr [rbp + 0x168], rax
007BDAD4  49 8D 45 04                     lea rax, [r13 + 4]
007BDAD8  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
007BDADC  48 8D 85 70 01 00 00            lea rax, [rbp + 0x170]
007BDAE3  48 89 85 58 05 00 00            mov qword ptr [rbp + 0x558], rax
007BDAEA  48 8D 05 CF A2 34 00            lea rax, [rip + 0x34a2cf]
007BDAF1  48 89 85 50 05 00 00            mov qword ptr [rbp + 0x550], rax
007BDAF8  48 8D 45 90                     lea rax, [rbp - 0x70]
007BDAFC  48 89 85 78 01 00 00            mov qword ptr [rbp + 0x178], rax
007BDB03  48 8D 85 80 01 00 00            lea rax, [rbp + 0x180]
007BDB0A  48 89 85 90 05 00 00            mov qword ptr [rbp + 0x590], rax
007BDB11  48 8D 05 78 A2 34 00            lea rax, [rip + 0x34a278]
007BDB18  48 89 85 88 05 00 00            mov qword ptr [rbp + 0x588], rax
007BDB1F  48 8D 44 24 54                  lea rax, [rsp + 0x54]
007BDB24  48 89 85 88 01 00 00            mov qword ptr [rbp + 0x188], rax
007BDB2B  48 8D 85 90 01 00 00            lea rax, [rbp + 0x190]
007BDB32  48 89 85 C8 05 00 00            mov qword ptr [rbp + 0x5c8], rax
007BDB39  48 8D 05 C0 A1 34 00            lea rax, [rip + 0x34a1c0]
007BDB40  48 89 85 C0 05 00 00            mov qword ptr [rbp + 0x5c0], rax
007BDB47  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007BDB4C  48 89 85 D8 05 00 00            mov qword ptr [rbp + 0x5d8], rax
007BDB53  48 8D 45 D8                     lea rax, [rbp - 0x28]
007BDB57  48 89 85 98 01 00 00            mov qword ptr [rbp + 0x198], rax
007BDB5E  48 8D 85 A0 01 00 00            lea rax, [rbp + 0x1a0]
007BDB65  48 89 85 00 06 00 00            mov qword ptr [rbp + 0x600], rax
007BDB6C  48 8D 05 6D A1 34 00            lea rax, [rip + 0x34a16d]
007BDB73  48 89 85 F8 05 00 00            mov qword ptr [rbp + 0x5f8], rax
007BDB7A  8D 42 07                        lea eax, [rdx + 7]
007BDB7D  89 85 08 06 00 00               mov dword ptr [rbp + 0x608], eax
007BDB83  89 85 A0 01 00 00               mov dword ptr [rbp + 0x1a0], eax
007BDB89  48 8D 43 50                     lea rax, [rbx + 0x50]
007BDB8D  89 8D 60 01 00 00               mov dword ptr [rbp + 0x160], ecx
007BDB93  4C 89 85 40 05 00 00            mov qword ptr [rbp + 0x540], r8
007BDB9A  44 89 8D 60 05 00 00            mov dword ptr [rbp + 0x560], r9d
007BDBA1  44 89 8D 70 01 00 00            mov dword ptr [rbp + 0x170], r9d
007BDBA8  45 33 C9                        xor r9d, r9d
007BDBAB  4C 89 85 78 05 00 00            mov qword ptr [rbp + 0x578], r8
007BDBB2  89 95 98 05 00 00               mov dword ptr [rbp + 0x598], edx
007BDBB8  89 95 80 01 00 00               mov dword ptr [rbp + 0x180], edx
007BDBBE  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
007BDBC3  4C 89 85 B0 05 00 00            mov qword ptr [rbp + 0x5b0], r8
007BDBCA  89 8D D0 05 00 00               mov dword ptr [rbp + 0x5d0], ecx
007BDBD0  89 8D 90 01 00 00               mov dword ptr [rbp + 0x190], ecx
007BDBD6  4C 89 85 E8 05 00 00            mov qword ptr [rbp + 0x5e8], r8
007BDBDD  4C 8D 85 C0 01 00 00            lea r8, [rbp + 0x1c0]
007BDBE4  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
007BDBE8  B9 00 00 00 40                  mov ecx, 0x40000000
007BDBED  48 89 85 A8 01 00 00            mov qword ptr [rbp + 0x1a8], rax
007BDBF4  44 89 55 90                     mov dword ptr [rbp - 0x70], r10d
007BDBF8  44 89 95 18 06 00 00            mov dword ptr [rbp + 0x618], r10d
007BDBFF  E8 4C B4 10 00                  call 0x1408c9050
007BDC04  45 33 C0                        xor r8d, r8d
007BDC07  8B F8                           mov edi, eax
007BDC09  85 C0                           test eax, eax
007BDC0B  0F 88 91 05 00 00               js 0x1407be1a2
007BDC11  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
007BDC16  48 85 D2                        test rdx, rdx
007BDC19  0F 84 94 01 00 00               je 0x1407bddb3
007BDC1F  44 39 44 24 44                  cmp dword ptr [rsp + 0x44], r8d
007BDC24  0F 85 1F 01 00 00               jne 0x1407bdd49
007BDC2A  48 8D 43 4C                     lea rax, [rbx + 0x4c]
007BDC2E  48 89 85 E8 01 00 00            mov qword ptr [rbp + 0x1e8], rax
007BDC35  48 8D 43 30                     lea rax, [rbx + 0x30]
007BDC39  48 89 85 20 02 00 00            mov qword ptr [rbp + 0x220], rax
007BDC40  48 8D 43 34                     lea rax, [rbx + 0x34]
007BDC44  48 89 85 58 02 00 00            mov qword ptr [rbp + 0x258], rax
007BDC4B  48 8D 43 44                     lea rax, [rbx + 0x44]
007BDC4F  48 89 85 90 02 00 00            mov qword ptr [rbp + 0x290], rax
007BDC56  48 8D 43 38                     lea rax, [rbx + 0x38]
007BDC5A  48 89 85 C8 02 00 00            mov qword ptr [rbp + 0x2c8], rax
007BDC61  48 8B 83 88 00 00 00            mov rax, qword ptr [rbx + 0x88]
007BDC68  48 89 85 00 03 00 00            mov qword ptr [rbp + 0x300], rax
007BDC6F  0F B7 83 80 00 00 00            movzx eax, word ptr [rbx + 0x80]
007BDC76  89 85 08 03 00 00               mov dword ptr [rbp + 0x308], eax
007BDC7C  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
007BDC80  48 89 85 38 03 00 00            mov qword ptr [rbp + 0x338], rax
007BDC87  8B 45 B0                        mov eax, dword ptr [rbp - 0x50]
007BDC8A  89 85 40 03 00 00               mov dword ptr [rbp + 0x340], eax
007BDC90  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
007BDC94  48 89 85 70 03 00 00            mov qword ptr [rbp + 0x370], rax
007BDC9B  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
007BDC9E  89 85 78 03 00 00               mov dword ptr [rbp + 0x378], eax
007BDCA4  48 8D 43 28                     lea rax, [rbx + 0x28]
007BDCA8  48 89 85 A8 03 00 00            mov qword ptr [rbp + 0x3a8], rax
007BDCAF  48 8D 43 3C                     lea rax, [rbx + 0x3c]
007BDCB3  48 89 85 E0 03 00 00            mov qword ptr [rbp + 0x3e0], rax
007BDCBA  48 8D 43 40                     lea rax, [rbx + 0x40]
007BDCBE  48 89 85 18 04 00 00            mov qword ptr [rbp + 0x418], rax
007BDCC5  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
007BDCCA  48 89 85 50 04 00 00            mov qword ptr [rbp + 0x450], rax
007BDCD1  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
007BDCD5  48 89 85 88 04 00 00            mov qword ptr [rbp + 0x488], rax
007BDCDC  0F B7 45 E8                     movzx eax, word ptr [rbp - 0x18]
007BDCE0  89 85 90 04 00 00               mov dword ptr [rbp + 0x490], eax
007BDCE6  48 8D 43 60                     lea rax, [rbx + 0x60]
007BDCEA  48 89 85 C0 04 00 00            mov qword ptr [rbp + 0x4c0], rax
007BDCF1  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007BDCF6  48 89 85 F8 04 00 00            mov qword ptr [rbp + 0x4f8], rax
007BDCFD  48 8B 45 00                     mov rax, qword ptr [rbp]
007BDD01  48 89 85 30 05 00 00            mov qword ptr [rbp + 0x530], rax
007BDD08  0F B7 45 F8                     movzx eax, word ptr [rbp - 8]
007BDD0C  89 85 38 05 00 00               mov dword ptr [rbp + 0x538], eax
007BDD12  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
007BDD16  48 89 85 68 05 00 00            mov qword ptr [rbp + 0x568], rax
007BDD1D  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
007BDD20  89 85 70 05 00 00               mov dword ptr [rbp + 0x570], eax
007BDD26  48 8D 44 24 54                  lea rax, [rsp + 0x54]
007BDD2B  48 89 85 A0 05 00 00            mov qword ptr [rbp + 0x5a0], rax
007BDD32  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
007BDD36  48 89 85 D8 05 00 00            mov qword ptr [rbp + 0x5d8], rax
007BDD3D  0F B7 45 D8                     movzx eax, word ptr [rbp - 0x28]
007BDD41  89 85 E0 05 00 00               mov dword ptr [rbp + 0x5e0], eax
007BDD47  EB 4E                           jmp 0x1407bdd97
007BDD49  48 8D 85 40 01 00 00            lea rax, [rbp + 0x140]
007BDD50  4C 89 85 F8 01 00 00            mov qword ptr [rbp + 0x1f8], r8
007BDD57  48 89 85 D8 01 00 00            mov qword ptr [rbp + 0x1d8], rax
007BDD5E  4C 8D 0D DB 0C 00 00            lea r9, [rip + 0xcdb]
007BDD65  48 8D 05 74 9C 34 00            lea rax, [rip + 0x349c74]
007BDD6C  4C 89 8D C0 01 00 00            mov qword ptr [rbp + 0x1c0], r9
007BDD73  B9 04 00 00 00                  mov ecx, 4
007BDD78  48 89 85 D0 01 00 00            mov qword ptr [rbp + 0x1d0], rax
007BDD7F  48 8D 43 60                     lea rax, [rbx + 0x60]
007BDD83  89 8D E0 01 00 00               mov dword ptr [rbp + 0x1e0], ecx
007BDD89  48 89 85 E8 01 00 00            mov qword ptr [rbp + 0x1e8], rax
007BDD90  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
007BDD94  89 4D 70                        mov dword ptr [rbp + 0x70], ecx
007BDD97  45 33 C9                        xor r9d, r9d
007BDD9A  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
007BDD9F  4C 8D 85 C0 01 00 00            lea r8, [rbp + 0x1c0]
007BDDA6  B9 00 00 00 40                  mov ecx, 0x40000000
007BDDAB  E8 A0 B2 10 00                  call 0x1408c9050
007BDDB0  45 33 C0                        xor r8d, r8d
007BDDB3  8B 43 70                        mov eax, dword ptr [rbx + 0x70]
007BDDB6  41 B9 01 00 00 00               mov r9d, 1
007BDDBC  83 C8 02                        or eax, 2
007BDDBF  89 43 70                        mov dword ptr [rbx + 0x70], eax
007BDDC2  44 39 44 24 6C                  cmp dword ptr [rsp + 0x6c], r8d
007BDDC7  75 06                           jne 0x1407bddcf
007BDDC9  41 0B C1                        or eax, r9d
007BDDCC  89 43 70                        mov dword ptr [rbx + 0x70], eax
007BDDCF  8B 7D B0                        mov edi, dword ptr [rbp - 0x50]
007BDDD2  C1 EF 02                        shr edi, 2
007BDDD5  66 85 FF                        test di, di
007BDDD8  74 26                           je 0x1407bde00
007BDDDA  41 8D 04 39                     lea eax, [r9 + rdi]
007BDDDE  66 44 89 4E 02                  mov word ptr [rsi + 2], r9w
007BDDE3  66 89 06                        mov word ptr [rsi], ax
007BDDE6  66 44 01 8B B2 00 00 00         add word ptr [rbx + 0xb2], r9w
007BDDEE  66 01 83 B0 00 00 00            add word ptr [rbx + 0xb0], ax
007BDDF5  0F B7 06                        movzx eax, word ptr [rsi]
007BDDF8  44 8D 3C 85 B4 00 00 00         lea r15d, [rax*4 + 0xb4]
007BDE00  8B 55 80                        mov edx, dword ptr [rbp - 0x80]
007BDE03  85 D2                           test edx, edx
007BDE05  74 6D                           je 0x1407bde74
007BDE07  41 BA 03 00 00 00               mov r10d, 3
007BDE0D  8B C2                           mov eax, edx
007BDE0F  C1 E8 02                        shr eax, 2
007BDE12  41 84 D2                        test r10b, dl
007BDE15  66 45 89 54 24 02               mov word ptr [r12 + 2], r10w
007BDE1B  41 8D 0C 01                     lea ecx, [r9 + rax]
007BDE1F  66 0F 44 C8                     cmove cx, ax
007BDE23  41 8D 04 09                     lea eax, [r9 + rcx]
007BDE27  66 41 89 04 24                  mov word ptr [r12], ax
007BDE2C  66 44 01 8B B2 00 00 00         add word ptr [rbx + 0xb2], r9w
007BDE34  41 0F B7 04 24                  movzx eax, word ptr [r12]
007BDE39  66 01 83 B0 00 00 00            add word ptr [rbx + 0xb0], ax
007BDE40  41 0F B7 04 24                  movzx eax, word ptr [r12]
007BDE45  45 8D 3C 87                     lea r15d, [r15 + rax*4]
007BDE49  66 85 FF                        test di, di
007BDE4C  74 07                           je 0x1407bde55
007BDE4E  0F B7 06                        movzx eax, word ptr [rsi]
007BDE51  48 8D 34 86                     lea rsi, [rsi + rax*4]
007BDE55  49 3B F4                        cmp rsi, r12
007BDE58  74 1A                           je 0x1407bde74
007BDE5A  44 0F B7 C1                     movzx r8d, cx
007BDE5E  49 8B D4                        mov rdx, r12
007BDE61  48 8B CE                        mov rcx, rsi
007BDE64  4E 8D 04 85 04 00 00 00         lea r8, [r8*4 + 4]
007BDE6C  E8 CF 89 F0 FF                  call 0x1406c6840
007BDE71  45 33 C0                        xor r8d, r8d
007BDE74  4C 39 45 00                     cmp qword ptr [rbp], r8
007BDE78  74 6B                           je 0x1407bdee5
007BDE7A  0F B7 83 B0 00 00 00            movzx eax, word ptr [rbx + 0xb0]
007BDE81  49 8D 56 04                     lea rdx, [r14 + 4]
007BDE85  48 83 C0 2C                     add rax, 0x2c
007BDE89  48 8D 4D F8                     lea rcx, [rbp - 8]
007BDE8D  4C 8D 24 83                     lea r12, [rbx + rax*4]
007BDE91  E8 DA 0A 00 00                  call 0x1407be970
007BDE96  0F B7 F0                        movzx esi, ax
007BDE99  66 85 F6                        test si, si
007BDE9C  74 4C                           je 0x1407bdeea
007BDE9E  B8 01 00 00 00                  mov eax, 1
007BDEA3  66 41 C7 46 02 04 00            mov word ptr [r14 + 2], 4
007BDEAA  8D 0C 30                        lea ecx, [rax + rsi]
007BDEAD  66 41 89 0E                     mov word ptr [r14], cx
007BDEB1  66 01 83 B2 00 00 00            add word ptr [rbx + 0xb2], ax
007BDEB8  41 0F B7 0E                     movzx ecx, word ptr [r14]
007BDEBC  66 01 8B B0 00 00 00            add word ptr [rbx + 0xb0], cx
007BDEC3  41 0F B7 0E                     movzx ecx, word ptr [r14]
007BDEC7  45 8D 3C 8F                     lea r15d, [r15 + rcx*4]
007BDECB  4D 3B E6                        cmp r12, r14
007BDECE  74 1A                           je 0x1407bdeea
007BDED0  4C 8D 04 B5 04 00 00 00         lea r8, [rsi*4 + 4]
007BDED8  49 8B D6                        mov rdx, r14
007BDEDB  49 8B CC                        mov rcx, r12
007BDEDE  E8 5D 89 F0 FF                  call 0x1406c6840
007BDEE3  EB 05                           jmp 0x1407bdeea
007BDEE5  0F B7 74 24 60                  movzx esi, word ptr [rsp + 0x60]
007BDEEA  83 7D 90 08                     cmp dword ptr [rbp - 0x70], 8
007BDEEE  41 BE 01 00 00 00               mov r14d, 1
007BDEF4  75 45                           jne 0x1407bdf3b
007BDEF6  0F B7 8B B0 00 00 00            movzx ecx, word ptr [rbx + 0xb0]
007BDEFD  41 C7 45 00 03 00 05 00         mov dword ptr [r13], 0x50003
007BDF05  48 83 C1 2C                     add rcx, 0x2c
007BDF09  66 44 01 B3 B2 00 00 00         add word ptr [rbx + 0xb2], r14w
007BDF11  41 0F B7 45 00                  movzx eax, word ptr [r13]
007BDF16  66 01 83 B0 00 00 00            add word ptr [rbx + 0xb0], ax
007BDF1D  41 0F B7 45 00                  movzx eax, word ptr [r13]
007BDF22  48 8D 0C 8B                     lea rcx, [rbx + rcx*4]
007BDF26  45 8D 3C 87                     lea r15d, [r15 + rax*4]
007BDF2A  49 3B CD                        cmp rcx, r13
007BDF2D  74 0C                           je 0x1407bdf3b
007BDF2F  45 8D 46 0B                     lea r8d, [r14 + 0xb]
007BDF33  49 8B D5                        mov rdx, r13
007BDF36  E8 05 89 F0 FF                  call 0x1406c6840
007BDF3B  45 33 ED                        xor r13d, r13d
007BDF3E  66 85 FF                        test di, di
007BDF41  75 15                           jne 0x1407bdf58
007BDF43  44 39 6D 80                     cmp dword ptr [rbp - 0x80], r13d
007BDF47  75 0F                           jne 0x1407bdf58
007BDF49  44 39 6D 90                     cmp dword ptr [rbp - 0x70], r13d
007BDF4D  75 09                           jne 0x1407bdf58
007BDF4F  66 85 F6                        test si, si
007BDF52  75 04                           jne 0x1407bdf58
007BDF54  44 89 6B 48                     mov dword ptr [rbx + 0x48], r13d
007BDF58  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
007BDF5B  A9 00 05 00 00                  test eax, 0x500
007BDF60  74 06                           je 0x1407bdf68
007BDF62  0F BA E0 09                     bt eax, 9
007BDF66  73 2A                           jae 0x1407bdf92
007BDF68  4C 39 AB 88 00 00 00            cmp qword ptr [rbx + 0x88], r13
007BDF6F  75 21                           jne 0x1407bdf92
007BDF71  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
007BDF78  48 8D 15 E1 92 34 00            lea rdx, [rip + 0x3492e1]
007BDF7F  E8 DC F8 1F 00                  call 0x1409bd860
007BDF84  84 C0                           test al, al
007BDF86  75 0A                           jne 0x1407bdf92
007BDF88  BF 17 00 00 C0                  mov edi, 0xc0000017
007BDF8D  E9 10 02 00 00                  jmp 0x1407be1a2
007BDF92  44 39 6C 24 54                  cmp dword ptr [rsp + 0x54], r13d
007BDF97  74 1D                           je 0x1407bdfb6
007BDF99  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
007BDF9C  84 C0                           test al, al
007BDF9E  79 69                           jns 0x1407be009
007BDFA0  0F BA E0 08                     bt eax, 8
007BDFA4  73 63                           jae 0x1407be009
007BDFA6  4C 39 AB 88 00 00 00            cmp qword ptr [rbx + 0x88], r13
007BDFAD  75 5A                           jne 0x1407be009
007BDFAF  81 4B 70 00 40 00 08            or dword ptr [rbx + 0x70], 0x8004000
007BDFB6  44 39 6C 24 50                  cmp dword ptr [rsp + 0x50], r13d
007BDFBB  74 5D                           je 0x1407be01a
007BDFBD  8B 43 60                        mov eax, dword ptr [rbx + 0x60]
007BDFC0  41 03 C6                        add eax, r14d
007BDFC3  89 43 60                        mov dword ptr [rbx + 0x60], eax
007BDFC6  3B 44 24 50                     cmp eax, dword ptr [rsp + 0x50]
007BDFCA  77 05                           ja 0x1407bdfd1
007BDFCC  83 F8 10                        cmp eax, 0x10
007BDFCF  76 04                           jbe 0x1407bdfd5
007BDFD1  44 89 73 60                     mov dword ptr [rbx + 0x60], r14d
007BDFD5  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
007BDFDA  48 8D 43 60                     lea rax, [rbx + 0x60]
007BDFDE  4C 8D 05 FB 99 34 00            lea r8, [rip + 0x3499fb]
007BDFE5  41 BC 04 00 00 00               mov r12d, 4
007BDFEB  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
007BDFF0  B9 00 00 00 40                  mov ecx, 0x40000000
007BDFF5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007BDFFA  45 8B CC                        mov r9d, r12d
007BDFFD  48 85 D2                        test rdx, rdx
007BE000  74 11                           je 0x1407be013
007BE002  E8 19 E6 2A 00                  call 0x140a6c620
007BE007  EB 17                           jmp 0x1407be020
007BE009  BF 22 00 00 C0                  mov edi, 0xc0000022
007BE00E  E9 8F 01 00 00                  jmp 0x1407be1a2
007BE013  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
007BE018  EB E8                           jmp 0x1407be002
007BE01A  41 BC 04 00 00 00               mov r12d, 4
007BE020  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
007BE024  48 8D 15 A5 98 34 00            lea rdx, [rip + 0x3498a5]
007BE02B  E8 C0 3A D4 FF                  call 0x140501af0
007BE030  85 C0                           test eax, eax
007BE032  74 2A                           je 0x1407be05e
007BE034  4C 39 6D F0                     cmp qword ptr [rbp - 0x10], r13
007BE038  74 11                           je 0x1407be04b
007BE03A  48 8D 55 58                     lea rdx, [rbp + 0x58]
007BE03E  48 8D 4D E8                     lea rcx, [rbp - 0x18]
007BE042  E8 A9 3E 13 00                  call 0x1408f1ef0
007BE047  8B F8                           mov edi, eax
007BE049  EB 05                           jmp 0x1407be050
007BE04B  BF 0D 00 00 C0                  mov edi, 0xc000000d
007BE050  85 FF                           test edi, edi
007BE052  0F 88 50 01 00 00               js 0x1407be1a8
007BE058  0F 10 45 58                     movups xmm0, xmmword ptr [rbp + 0x58]
007BE05C  EB 0B                           jmp 0x1407be069
007BE05E  0F 10 05 4B C0 39 00            movups xmm0, xmmword ptr [rip + 0x39c04b]
007BE065  0F 11 45 58                     movups xmmword ptr [rbp + 0x58], xmm0
007BE069  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
007BE06D  48 8B D3                        mov rdx, rbx
007BE070  48 8B CE                        mov rcx, rsi
007BE073  44 89 3B                        mov dword ptr [rbx], r15d
007BE076  F3 0F 7F 43 18                  movdqu xmmword ptr [rbx + 0x18], xmm0
007BE07B  E8 00 BD 2D 00                  call 0x140a99d80
007BE080  44 0F B7 7B 08                  movzx r15d, word ptr [rbx + 8]
007BE085  8B F8                           mov edi, eax
007BE087  85 C0                           test eax, eax
007BE089  0F 88 19 01 00 00               js 0x1407be1a8
007BE08F  45 85 FF                        test r15d, r15d
007BE092  74 2A                           je 0x1407be0be
007BE094  44 39 6C 24 54                  cmp dword ptr [rsp + 0x54], r13d
007BE099  74 23                           je 0x1407be0be
007BE09B  41 8B C5                        mov eax, r13d
007BE09E  83 F8 10                        cmp eax, 0x10
007BE0A1  73 1B                           jae 0x1407be0be
007BE0A3  8B C8                           mov ecx, eax
007BE0A5  66 44 39 AC 4E D0 10 00 00      cmp word ptr [rsi + rcx*2 + 0x10d0], r13w
007BE0AE  74 05                           je 0x1407be0b5
007BE0B0  41 03 C6                        add eax, r14d
007BE0B3  EB E9                           jmp 0x1407be09e
007BE0B5  66 44 89 BC 4E D0 10 00 00      mov word ptr [rsi + rcx*2 + 0x10d0], r15w
007BE0BE  44 0F B7 45 D8                  movzx r8d, word ptr [rbp - 0x28]
007BE0C3  66 45 85 C0                     test r8w, r8w
007BE0C7  0F 84 B1 00 00 00               je 0x1407be17e
007BE0CD  41 B9 CB 6B 28 AF               mov r9d, 0xaf286bcb
007BE0D3  41 8B F0                        mov esi, r8d
007BE0D6  41 8B C1                        mov eax, r9d
007BE0D9  41 F7 E0                        mul r8d
007BE0DC  41 8B C0                        mov eax, r8d
007BE0DF  2B C2                           sub eax, edx
007BE0E1  D1 E8                           shr eax, 1
007BE0E3  03 C2                           add eax, edx
007BE0E5  C1 E8 06                        shr eax, 6
007BE0E8  6B C8 4C                        imul ecx, eax, 0x4c
007BE0EB  44 3B C1                        cmp r8d, ecx
007BE0EE  0F 85 8A 00 00 00               jne 0x1407be17e
007BE0F4  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
007BE0F8  B8 4C 00 00 00                  mov eax, 0x4c
007BE0FD  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
007BE101  0F B7 4D DA                     movzx ecx, word ptr [rbp - 0x26]
007BE105  66 41 2B C8                     sub cx, r8w
007BE109  66 89 45 A0                     mov word ptr [rbp - 0x60], ax
007BE10D  66 03 C8                        add cx, ax
007BE110  44 89 6D A4                     mov dword ptr [rbp - 0x5c], r13d
007BE114  41 8B C1                        mov eax, r9d
007BE117  66 89 4D A2                     mov word ptr [rbp - 0x5e], cx
007BE11B  F7 E6                           mul esi
007BE11D  2B F2                           sub esi, edx
007BE11F  D1 EE                           shr esi, 1
007BE121  03 F2                           add esi, edx
007BE123  C1 EE 06                        shr esi, 6
007BE126  81 FE 00 02 00 00               cmp esi, 0x200
007BE12C  77 50                           ja 0x1407be17e
007BE12E  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
007BE133  45 8B F5                        mov r14d, r13d
007BE136  85 F6                           test esi, esi
007BE138  74 26                           je 0x1407be160
007BE13A  41 8B D6                        mov edx, r14d
007BE13D  48 8D 4D A0                     lea rcx, [rbp - 0x60]
007BE141  48 C1 E2 04                     shl rdx, 4
007BE145  49 03 D4                        add rdx, r12
007BE148  E8 A3 3D 13 00                  call 0x1408f1ef0
007BE14D  8B F8                           mov edi, eax
007BE14F  85 C0                           test eax, eax
007BE151  75 2B                           jne 0x1407be17e
007BE153  48 83 45 A8 4C                  add qword ptr [rbp - 0x58], 0x4c
007BE158  41 FF C6                        inc r14d
007BE15B  44 3B F6                        cmp r14d, esi
007BE15E  72 DA                           jb 0x1407be13a
007BE160  85 FF                           test edi, edi
007BE162  75 1A                           jne 0x1407be17e
007BE164  E8 87 00 B4 FF                  call 0x1402fe1f0
007BE169  4D 8B CC                        mov r9, r12
007BE16C  44 8B C6                        mov r8d, esi
007BE16F  41 8B D7                        mov edx, r15d
007BE172  48 8B 88 40 03 00 00            mov rcx, qword ptr [rax + 0x340]
007BE179  E8 02 C7 22 00                  call 0x1409ea880
007BE17E  E8 6D 00 B4 FF                  call 0x1402fe1f0
007BE183  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
007BE187  41 8B D7                        mov edx, r15d
007BE18A  4C 8B 45 50                     mov r8, qword ptr [rbp + 0x50]
007BE18E  48 8B 88 40 03 00 00            mov rcx, qword ptr [rax + 0x340]
007BE195  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
007BE199  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007BE19D  E8 EA 00 00 00                  call 0x1407be28c
007BE1A2  41 BC 04 00 00 00               mov r12d, 4
007BE1A8  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
007BE1AD  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
007BE1B2  48 85 D2                        test rdx, rdx
007BE1B5  74 4E                           je 0x1407be205
007BE1B7  85 FF                           test edi, edi
007BE1B9  79 10                           jns 0x1407be1cb
007BE1BB  8B CF                           mov ecx, edi
007BE1BD  E8 7E 8A 16 00                  call 0x140926c40
007BE1C2  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
007BE1C7  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
007BE1CB  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007BE1D0  48 8D 44 24 70                  lea rax, [rsp + 0x70]
007BE1D5  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
007BE1DA  45 8B CC                        mov r9d, r12d
007BE1DD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007BE1E2  4C 8D 05 D7 10 34 00            lea r8, [rip + 0x3410d7]
007BE1E9  48 85 C9                        test rcx, rcx
007BE1EC  74 03                           je 0x1407be1f1
007BE1EE  48 8B D1                        mov rdx, rcx
007BE1F1  B9 00 00 00 40                  mov ecx, 0x40000000
007BE1F6  E8 25 E4 2A 00                  call 0x140a6c620
007BE1FB  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007BE200  E8 AB F0 EE FF                  call 0x1406ad2b0
007BE205  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007BE20A  48 85 C9                        test rcx, rcx
007BE20D  74 05                           je 0x1407be214
007BE20F  E8 9C F0 EE FF                  call 0x1406ad2b0
007BE214  48 85 DB                        test rbx, rbx
007BE217  74 16                           je 0x1407be22f
007BE219  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
007BE220  E8 DB 25 20 00                  call 0x1409c0800
007BE225  33 D2                           xor edx, edx
007BE227  48 8B CB                        mov rcx, rbx
007BE22A  E8 41 46 3C 00                  call 0x140b82870
007BE22F  48 85 F6                        test rsi, rsi
007BE232  74 0A                           je 0x1407be23e
007BE234  33 D2                           xor edx, edx
007BE236  48 8B CE                        mov rcx, rsi
007BE239  E8 32 46 3C 00                  call 0x140b82870
007BE23E  48 8D 4D E8                     lea rcx, [rbp - 0x18]
007BE242  E8 B9 25 20 00                  call 0x1409c0800
007BE247  48 8D 4D F8                     lea rcx, [rbp - 8]
007BE24B  E8 B0 25 20 00                  call 0x1409c0800
007BE250  48 8D 4D D8                     lea rcx, [rbp - 0x28]
007BE254  E8 A7 25 20 00                  call 0x1409c0800
007BE259  8B C7                           mov eax, edi
007BE25B  48 8B 8D 60 06 00 00            mov rcx, qword ptr [rbp + 0x660]
007BE262  48 33 CC                        xor rcx, rsp
007BE265  E8 D6 E3 EE FF                  call 0x1406ac640
007BE26A  48 8B 9C 24 C8 07 00 00         mov rbx, qword ptr [rsp + 0x7c8]
007BE272  48 81 C4 70 07 00 00            add rsp, 0x770
007BE279  41 5F                           pop r15
007BE27B  41 5E                           pop r14
007BE27D  41 5D                           pop r13
007BE27F  41 5C                           pop r12
007BE281  5F                              pop rdi
007BE282  5E                              pop rsi
007BE283  5D                              pop rbp
007BE284  C3                              ret
007BE285  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwStartAutoLogger(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E8;
    unsigned int v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m210;
    unsigned int v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned int v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m258;
    unsigned int v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m280;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned int v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B8;
    unsigned int v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned int v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned __int64 v_stack_m2F0;
    unsigned int v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned int v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m328;
    unsigned int v_stack_m330;
    unsigned __int64 v_stack_m338;
    unsigned int v_stack_m340;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_m350;
    unsigned __int64 v_stack_m360;
    unsigned int v_stack_m368;
    unsigned __int64 v_stack_m370;
    unsigned int v_stack_m378;
    unsigned __int64 v_stack_m380;
    unsigned __int64 v_stack_m388;
    unsigned __int64 v_stack_m398;
    unsigned int v_stack_m3A0;
    unsigned __int64 v_stack_m3A8;
    unsigned int v_stack_m3B0;
    unsigned __int64 v_stack_m3B8;
    unsigned __int64 v_stack_m3C0;
    unsigned __int64 v_stack_m3D0;
    unsigned __int64 v_stack_m3E0;
    unsigned int v_stack_m3E8;
    unsigned __int64 v_stack_m3F0;
    unsigned __int64 v_stack_m3F8;
    unsigned __int64 v_stack_m408;
    unsigned __int64 v_stack_m418;
    unsigned int v_stack_m420;
    unsigned __int64 v_stack_m428;
    unsigned __int64 v_stack_m430;
    unsigned __int64 v_stack_m440;
    unsigned __int64 v_stack_m450;
    unsigned int v_stack_m458;
    unsigned __int64 v_stack_m460;
    unsigned __int64 v_stack_m468;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m480;
    unsigned __int64 v_stack_m488;
    unsigned int v_stack_m490;
    unsigned __int64 v_stack_m498;
    unsigned __int64 v_stack_m4A0;
    unsigned __int64 v_stack_m4B0;
    unsigned __int64 v_stack_m4C0;
    unsigned int v_stack_m4C8;
    unsigned __int64 v_stack_m4D0;
    unsigned __int64 v_stack_m4D8;
    unsigned __int64 v_stack_m4E8;
    unsigned __int64 v_stack_m500;
    unsigned __int64 v_stack_m508;
    unsigned __int64 v_stack_m510;
    unsigned __int64 v_stack_m518;
    unsigned __int64 v_stack_m520;
    unsigned __int64 v_stack_m528;
    unsigned __int64 v_stack_m530;
    unsigned __int64 v_stack_m538;
    unsigned __int64 v_stack_m540;
    unsigned __int64 v_stack_m548;
    unsigned __int64 v_stack_m550;
    unsigned __int64 v_stack_m558;
    unsigned __int64 v_stack_m560;
    unsigned __int64 v_stack_m568;
    unsigned __int64 v_stack_m570;
    unsigned __int64 v_stack_m578;
    unsigned __int64 v_stack_m580;
    unsigned __int64 v_stack_m588;
    unsigned __int64 v_stack_m590;
    unsigned __int64 v_stack_m598;
    unsigned __int64 v_stack_m5A0;
    unsigned __int64 v_stack_m5A8;
    unsigned __int64 v_stack_m5B0;
    unsigned __int64 v_stack_m5B8;
    unsigned __int64 v_stack_m5C0;
    unsigned __int64 v_stack_m5C8;
    unsigned __int64 v_stack_m5D0;
    unsigned __int64 v_stack_m5D8;
    unsigned __int64 v_stack_m5E0;
    unsigned __int64 v_stack_m5E8;
    unsigned __int64 v_stack_m5F0;
    unsigned __int64 v_stack_m5F8;
    unsigned __int64 v_stack_m600;
    unsigned __int64 v_stack_m608;
    unsigned __int64 v_stack_m610;
    unsigned __int64 v_stack_m618;
    unsigned __int64 v_stack_m620;
    unsigned __int64 v_stack_m628;
    unsigned __int64 v_stack_m630;
    unsigned __int64 v_stack_m638;
    unsigned __int64 v_stack_m650;
    unsigned __int64 v_stack_m658;
    unsigned __int64 v_stack_m660;
    unsigned __int64 v_stack_m670;
    unsigned __int64 v_stack_m680;
    unsigned int v_stack_m684;
    unsigned int v_stack_m688;
    unsigned __int64 v_stack_m690;
    unsigned __int64 v_stack_m698;
    unsigned int v_stack_m69C;
    unsigned int v_stack_m6A0;
    unsigned __int64 v_stack_m6A8;
    unsigned __int64 v_stack_m6B0;
    unsigned __int64 v_stack_m6B8;
    unsigned __int64 v_stack_m6C0;
    unsigned __int64 v_stack_m6C8;
    unsigned __int16 v_stack_m6CE;
    unsigned __int64 v_stack_m6D0;
    unsigned __int64 v_stack_m6D8;
    unsigned int v_stack_m6E0;
    unsigned int v_stack_m6E4;
    unsigned int v_stack_m6E8;
    unsigned __int64 v_stack_m6F0;
    unsigned __int64 v_stack_m6F4;
    unsigned __int64 v_stack_m6F8;
    unsigned __int64 v_stack_m700;
    unsigned int v_stack_m704;
    unsigned __int16 v_stack_m706;
    unsigned __int64 v_stack_m708;
    unsigned __int64 v_stack_m710;
    unsigned __int64 v_stack_m714;
    unsigned __int64 v_stack_m718;
    unsigned __int64 v_stack_m720;
    unsigned __int64 v_stack_m724;
    unsigned __int64 v_stack_m728;
    unsigned __int64 v_stack_m730;
    unsigned int v_stack_m738;
    unsigned int v_stack_m73C;
    unsigned int v_stack_m740;
    unsigned int v_stack_m744;
    unsigned __int16 v_stack_m748;
    unsigned __int64 v_stack_m750;
    unsigned int v_stack_m754;
    unsigned int v_stack_m758;
    unsigned __int64 v_stack_m760;
    unsigned int v_stack_m764;
    unsigned __int16 v_stack_m768;
    unsigned __int64 v_stack_m778;
    unsigned __int8 v_stack_m780;
    unsigned __int64 v_stack_m788;
    unsigned int v_stack_m90;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (0x770ULL);
    result = (*(unsigned __int64 *)(v_rip + 6607906)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r13 = 0;
    v_stack_m6D8 = a3;
    result = 0;
    v_stack_m658 = a2;
    v_stack_m6F4 = 0;
    v_stack_m714 = 0;
    v_stack_m724 = 0;
    v_stack_m660 = a1;
    v_stack_m6E8 = (unsigned int)(result + 1);
    v_stack_m69C = 0;
    v_stack_m684 = 0;
    v_stack_m670 = v_xmm0;
    v_stack_m730 = 0;
    v_stack_m750 = 0;
    v_stack_m738 = 0;
    v_stack_m740 = 0;
    v_stack_m6C0 = v_xmm0;
    v_stack_m6F8 = 0;
    v_stack_m6B0 = v_xmm1;
    v_stack_m718 = 0;
    v_stack_m6D0 = v_xmm0;
    v_stack_m728 = 0;
    v_stack_m758 = 0;
    v_stack_m73C = 0;
    v_stack_m754 = 0;
    v_stack_m764 = 0;
    v_stack_m768 = 0;
    v_stack_m6E0 = 0;
    v_stack_m6E4 = 100;
    v_stack_m748 = 0;
    v_stack_m650 = v_xmm0;
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    v_stack_m708 = *(unsigned __int64 *)(result + 832);
    result = RtlInitUnicodeString(v_stack_m670, a2, a3, a4);
    v_stack_m6A0 = 48;
    v_stack_m690 = v_stack_m670;
    v_stack_m698 = 0;
    v_stack_m688 = 576;
    v_stack_m680 = v_xmm0;
    result = ZwOpenKey(v_stack_m730, (unsigned int)(0x2001FULL), v_stack_m6A0, a4);
    if (sign_flag) goto loc_007BE1AD;
    result = ExAllocatePool2(256, (unsigned int)(0x2000ULL), (unsigned int)((unsigned int)((unsigned int)(0x50777445ULL))), a4);
    v_stack_m760 = result;
    if (result != 0) goto loc_007BD44D;
loc_007BD443:
    goto loc_007BE1AD;
loc_007BD44D:
    result = ExAllocatePool2(256, (unsigned int)(0x504ULL), (unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))), a4);
    if (result == 0) goto loc_007BD443;
    *(unsigned int *)(result + 44) = 0x20000ULL;
    *(unsigned int *)(result + 48) = (unsigned int)(v_r13 + 4);
    result = RtlInitUnicodeString(result + 144, a1, (unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))), a4);
    *(unsigned int *)(result + 72) = 0x80000000ULL;
    *(unsigned __int8 *)(result + 74) = 255;
    *(unsigned __int16 *)(result + 72) = 176;
    *(unsigned int *)(result + 176) = (unsigned int)(result + 1);
    a2 = 0;
    result = memset(v_stack_m4E8, a2, (unsigned int)(0x498ULL), a4);
    v_stack_m4E8 = v_rip + 5482;
    v_stack_m4C8 = 4;
    v_stack_m4D0 = v_stack_m638;
    v_stack_m638 = 4;
    v_stack_m4D8 = v_rip + 3410511;
    v_stack_m630 = v_stack_m740;
    v_stack_m498 = v_stack_m628;
    v_stack_m4A0 = v_rip + 3450487;
    v_stack_m4B0 = v_rip + 5482;
    a4 = 0;
    v_stack_m490 = 4;
    v_stack_m628 = 4;
    v_stack_m620 = v_stack_m764;
    v_stack_m780 = 1;
    result = RtlpQueryRegistryValues((unsigned int)(0x40000000ULL), v_stack_m730, v_stack_m4E8, a4);
    a2 = 0;
    if (sign_flag) goto loc_007BE1A2;
    if (v_stack_m6D8 == 0) goto loc_007BD63B;
    v_stack_m744 = 0;
    result = RtlInitUnicodeString(v_stack_m670, v_stack_m6D8, v_stack_m4E8, a4);
    a1 = 0;
    v_stack_m6A0 = 48;
    v_stack_m698 = 0;
    v_stack_m690 = v_stack_m670;
    v_stack_m688 = 576;
    v_stack_m778 = v_stack_m744;
    v_stack_m780 = 0;
    a4 = 0;
    v_stack_m788 = 0;
    v_stack_m680 = v_xmm0;
    result = ZwCreateKey(v_stack_m750, (unsigned int)(0x2001FULL), v_stack_m6A0, a4);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_007BD61A;
    result = EtwpCreateKeyTreeForPath(v_stack_m6D8, (unsigned int)(0x2001FULL), v_stack_m6A0, a4);
    a2 = 0;
    if ((unsigned int)(result) != 0) goto loc_007BD620;
    a4 = 0;
    v_stack_m778 = v_stack_m744;
    v_stack_m780 = 0;
    v_stack_m788 = 0;
    result = ZwCreateKey(v_stack_m750, (unsigned int)(0x2001FULL), v_stack_m6A0, a4);
loc_007BD61A:
    a2 = 0;
    v_rdi = (unsigned int)((unsigned int)(result));
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) {
        v_rdi = 0;
        v_stack_m750 = 0;
    }
    if (v_stack_m744 != 1) goto loc_007BD641;
    v_stack_m764 = 1;
    goto loc_007BD641;
loc_007BD63B:
loc_007BD641:
    if (v_stack_m764 != 0) goto loc_007BD6A3;
    if (v_stack_m750 != 0) {
        v_stack_m780 = 1;
        result = 0;
        a3 = v_stack_m4E8;
        v_stack_m480 = 0;
        a2 = v_stack_m750;
        result = v_stack_m740;
        a4 = 0;
        a1 = 0x40000000ULL;
        v_stack_m4C0 = result;
        v_stack_m4B0 = v_xmm0;
        v_stack_m4A0 = v_xmm0;
        v_stack_m490 = v_xmm0;
        result = RtlpQueryRegistryValues(a1, a2, a3, a4);
        a2 = 0;
        v_rdi = (unsigned int)(result);
        if (sign_flag) { v_rdi = 0; }
    }
    if (v_stack_m740 == 0) goto loc_007BE1A2;
    v_stack_m6F8 = 40;
    v_stack_m4C8 = 4;
    v_stack_m4E8 = v_rip + 4992;
    v_stack_m4D0 = v_stack_m638;
    v_stack_m4D8 = v_rip + 3450017;
    v_stack_m638 = 4;
    v_stack_m630 = result + 76;
    v_stack_m4B0 = v_rip + 4992;
    v_stack_m498 = v_stack_m628;
    v_stack_m4A0 = v_rip + 3449772;
    v_stack_m620 = result + 48;
    v_stack_m460 = v_stack_m618;
    v_stack_m468 = v_rip + 3449701;
    v_stack_m610 = result + 52;
    v_stack_m428 = v_stack_m608;
    v_stack_m430 = v_rip + 3449758;
    v_stack_m600 = result + 68;
    v_stack_m3F0 = v_stack_m5F8;
    v_stack_m3F8 = v_rip + 3449687;
    v_stack_m5F0 = result + 56;
    v_stack_m3B8 = v_stack_m5E8;
    v_stack_m3C0 = v_rip + 3449488;
    v_stack_m3A8 = v_stack_m768;
    v_stack_m5E0 = result + 128;
    v_stack_m6F0 = result + 180 + 4;
    v_stack_m380 = v_stack_m5D8;
    v_stack_m388 = v_rip + 3444674;
    v_stack_m5D0 = v_stack_m6F8;
    v_stack_m720 = result + 180 + 44 + 4;
    v_stack_m348 = v_stack_m5C8;
    v_stack_m350 = v_rip + 3449330;
    v_stack_m490 = 4;
    v_stack_m628 = 4;
    v_stack_m478 = v_rip + 4992;
    v_stack_m458 = 4;
    v_stack_m618 = 4;
    v_stack_m440 = v_rip + 4992;
    v_stack_m420 = 4;
    v_stack_m608 = 4;
    v_stack_m408 = v_rip + 4992;
    v_stack_m3E8 = 4;
    v_stack_m5F8 = 4;
    v_stack_m3D0 = v_rip + 4992;
    v_stack_m3B0 = (unsigned int)(4 - 3);
    v_stack_m5E8 = (unsigned int)(4 - 3);
    v_stack_m398 = v_rip + 4992;
    v_stack_m378 = (unsigned int)(4 - 1);
    v_stack_m5D8 = (unsigned int)(4 - 1);
    v_stack_m728 = 0x400ULL;
    v_stack_m360 = v_rip + 4992;
    v_stack_m340 = (unsigned int)(4 - 1);
    v_stack_m5C8 = (unsigned int)(4 - 1);
    v_stack_m5C0 = v_stack_m728;
    v_stack_m310 = v_stack_m5B8;
    v_stack_m318 = v_rip + 3449266;
    v_stack_m300 = v_stack_m6E8;
    v_stack_m5B0 = result + 40;
    v_stack_m2D8 = v_stack_m5A8;
    v_stack_m2E0 = v_rip + 3449184;
    v_stack_m2C8 = v_stack_m6E4;
    v_stack_m5A0 = result + 60;
    v_stack_m2A0 = v_stack_m598;
    v_stack_m2A8 = v_rip + 3448974;
    v_stack_m290 = v_stack_m6E0;
    v_stack_m590 = result + 64;
    v_stack_m268 = v_stack_m588;
    v_stack_m270 = v_rip + 3448860;
    v_stack_m580 = v_stack_m73C;
    v_stack_m230 = v_stack_m578;
    v_stack_m238 = v_rip + 3448948;
    v_stack_m220 = v_stack_m768;
    v_stack_m570 = v_stack_m6C0;
    v_stack_m1F8 = v_stack_m568;
    v_stack_m200 = v_rip + 3448865;
    v_stack_m560 = result + 96;
    v_stack_m1C0 = v_stack_m558;
    v_stack_m1C8 = v_rip + 3449754;
    v_stack_m550 = v_stack_m758;
    v_stack_m188 = v_stack_m548;
    v_stack_m328 = v_rip + 4992;
    v_stack_m308 = 4;
    v_stack_m2F8 = 4;
    v_stack_m5B8 = 4;
    v_stack_m2F0 = v_rip + 4992;
    v_stack_m2D0 = 4;
    v_stack_m2C0 = 4;
    v_stack_m5A8 = 4;
    v_stack_m2B8 = v_rip + 4992;
    v_stack_m298 = 4;
    v_stack_m288 = 4;
    v_stack_m598 = 4;
    v_stack_m280 = v_rip + 4992;
    v_stack_m260 = 4;
    v_stack_m588 = 4;
    v_stack_m248 = v_rip + 4992;
    v_stack_m228 = (unsigned int)(4 - 3);
    v_stack_m578 = (unsigned int)(4 - 3);
    v_stack_m210 = v_rip + 4992;
    v_stack_m1F0 = 4;
    v_stack_m568 = 4;
    v_stack_m1D8 = v_rip + 4992;
    v_stack_m1B8 = 4;
    v_stack_m558 = 4;
    v_stack_m1A0 = v_rip + 4992;
    v_stack_m190 = v_rip + 3449682;
    v_stack_m180 = (unsigned int)(4 - 3);
    v_stack_m178 = v_stack_m768;
    v_stack_m540 = v_stack_m6B0;
    v_stack_m710 = result + 180 + 44 + 1028 + 20 + 4;
    v_stack_m150 = v_stack_m538;
    v_stack_m158 = v_rip + 3449551;
    v_stack_m530 = v_stack_m718;
    v_stack_m118 = v_stack_m528;
    v_stack_m120 = v_rip + 3449464;
    v_stack_m520 = v_stack_m754;
    v_stack_mE0 = v_stack_m518;
    v_stack_mE8 = v_rip + 3449280;
    v_stack_mD0 = v_stack_m768;
    v_stack_m510 = v_stack_m6D0;
    v_stack_mA8 = v_stack_m508;
    v_stack_mB0 = v_rip + 3449197;
    v_stack_mA0 = (unsigned int)(4 + 7);
    v_stack_m508 = (unsigned int)(4 + 7);
    v_stack_m548 = (unsigned int)(4 - 3);
    v_stack_m168 = v_rip + 4992;
    v_stack_m148 = (unsigned int)(4 - 1);
    v_stack_m538 = (unsigned int)(4 - 1);
    a4 = 0;
    v_stack_m130 = v_rip + 4992;
    v_stack_m110 = 4;
    v_stack_m528 = 4;
    v_stack_mF8 = v_rip + 4992;
    v_stack_mD8 = (unsigned int)(4 - 3);
    v_stack_m518 = (unsigned int)(4 - 3);
    v_stack_mC0 = v_rip + 4992;
    v_stack_m780 = (unsigned __int8)(4 - 3);
    v_stack_m500 = result + 80;
    v_stack_m718 = (unsigned int)(4 + 4);
    v_stack_m90 = (unsigned int)(4 + 4);
    result = RtlpQueryRegistryValues((unsigned int)(0x40000000ULL), v_stack_m730, v_stack_m4E8, a4);
    a3 = 0;
    if (sign_flag) goto loc_007BE1A2;
    if (v_stack_m750 == 0) goto loc_007BDDB3;
    if (v_stack_m764 != 0) goto loc_007BDD49;
    v_stack_m4C0 = result + 76;
    v_stack_m488 = result + 48;
    v_stack_m450 = result + 52;
    v_stack_m418 = result + 68;
    v_stack_m3E0 = result + 56;
    v_stack_m3A8 = *(unsigned __int64 *)(result + 136);
    v_stack_m3A0 = (unsigned int)(*(unsigned __int16 *)(result + 128));
    v_stack_m370 = v_stack_m6F0;
    v_stack_m368 = (unsigned int)((unsigned int)(v_stack_m6F8));
    v_stack_m338 = v_stack_m720;
    v_stack_m330 = (unsigned int)((unsigned int)(v_stack_m728));
    v_stack_m300 = result + 40;
    v_stack_m2C8 = result + 60;
    v_stack_m290 = result + 64;
    v_stack_m258 = v_stack_m73C;
    v_stack_m220 = v_stack_m6B8;
    v_stack_m218 = (unsigned int)(v_stack_m6C0);
    v_stack_m1E8 = result + 96;
    v_stack_m1B0 = v_stack_m758;
    v_stack_m178 = v_stack_m6A8;
    v_stack_m170 = (unsigned int)(v_stack_m6B0);
    v_stack_m140 = v_stack_m710;
    v_stack_m138 = (unsigned int)((unsigned int)(v_stack_m718));
    v_stack_m108 = v_stack_m754;
    v_stack_mD0 = v_stack_m6C8;
    v_stack_mC8 = (unsigned int)(v_stack_m6D0);
    goto loc_007BDD97;
loc_007BDD49:
    v_stack_m4B0 = 0;
    v_stack_m4D0 = v_stack_m568;
    v_stack_m4E8 = v_rip + 3291;
    v_stack_m4D8 = v_rip + 3447924;
    v_stack_m4C8 = 4;
    v_stack_m4C0 = result + 96;
    v_stack_m630 = result + 96;
    v_stack_m638 = 4;
loc_007BDD97:
    a4 = 0;
    v_stack_m780 = 1;
    result = RtlpQueryRegistryValues((unsigned int)(0x40000000ULL), v_stack_m750, v_stack_m4E8, a4);
    a3 = 0;
loc_007BDDB3:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 112))) | (2));
    *(unsigned int *)(result + 112) = (unsigned int)(result);
    if (v_stack_m73C == 0) {
        result = (unsigned int)((result) | (1));
        *(unsigned int *)(result + 112) = (unsigned int)(result);
    }
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m6F8)) >> (2));
    v_r15 = 180;
    if ((unsigned __int16)(v_rdi) != 0) {
        result = 1 + v_rdi * 1;
        *(unsigned __int16 *)(result + 180 + 2) = 1;
        *(unsigned __int16 *)(result + 180) = (unsigned __int16)(result);
        result = *(unsigned __int16 *)(result + 180);
        v_r15 = result * 4 + 180;
    }
    if ((unsigned int)((unsigned int)(v_stack_m728)) == 0) goto loc_007BDE74;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m728)))) >> (2));
    *(unsigned __int16 *)(result + 180 + 44 + 2) = 3;
    a1 = 1 + result * 1;
    if (((3) & ((unsigned __int8)((unsigned int)(v_stack_m728)))) == 0) { a1 = (unsigned __int16)(result); }
    *(unsigned __int16 *)(result + 180 + 44) = (unsigned __int16)(1 + a1 * 1);
    result = *(unsigned __int16 *)(result + 180 + 44);
    v_rsi = result + 180;
    if ((unsigned __int16)(v_rdi) != 0) {
        result = *(unsigned __int16 *)(result + 180);
        v_rsi = result + 180 + result * 4;
    }
    if (v_rsi != (result + 180 + 44)) {
        a3 = (unsigned __int16)(a1);
        a2 = result + 180 + 44;
        a1 = v_rsi;
        a3 = a3 * 4 + 4;
        result = memcpy(a1, a2, a3, 1);
        a3 = 0;
    }
    if (v_stack_m6A8 == 0) goto loc_007BDEE5;
    result = (*(unsigned __int16 *)(result + 176)) + (44);
    result = EtwpParsePoolTagFilter(v_stack_m6B0, result + 180 + 44 + 1028 + 4, a3, 1);
    if ((unsigned __int16)((unsigned __int16)(result)) == 0) goto loc_007BDEEA;
    *(unsigned __int16 *)(result + 180 + 44 + 1028 + 2) = 4;
    *(unsigned __int16 *)(result + 180 + 44 + 1028) = (unsigned __int16)(1 + (unsigned __int16)(result) * 1);
    if ((result + result * 4) == (result + 180 + 44 + 1028)) goto loc_007BDEEA;
    result = memcpy(result + result * 4, result + 180 + 44 + 1028, (unsigned __int16)(result) * 4 + 4, 1);
    goto loc_007BDEEA;
loc_007BDEE5:
loc_007BDEEA:
    if (v_stack_m718 != 8) goto loc_007BDF3B;
    *(unsigned int *)(result + 180 + 44 + 1028 + 20) = 0x50003ULL;
    a1 = (*(unsigned __int16 *)(result + 176)) + (44);
    result = *(unsigned __int16 *)(result + 180 + 44 + 1028 + 20);
    if ((result + a1 * 4) != (result + 180 + 44 + 1028 + 20)) {
        a3 = 1 + 11;
        a2 = result + 180 + 44 + 1028 + 20;
        result = memcpy(result + a1 * 4, a2, a3, 1);
    }
    v_r13 = 0;
    if ((unsigned __int16)(v_rdi) != 0) goto loc_007BDF58;
    if (v_stack_m728 != 0) goto loc_007BDF58;
    if (v_stack_m718 != 0) goto loc_007BDF58;
    if ((unsigned __int16)(v_stack_m748) == 0) {
        *(unsigned int *)(result + 72) = 0;
    }
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + 64)))) & (0x500ULL)) == 0) goto loc_007BDF68;
    if (condition_is_above_or_equal) goto loc_007BDF92;
loc_007BDF68:
    if ((*(unsigned __int64 *)(result + 136)) != 0) goto loc_007BDF92;
    result = RtlCreateUnicodeString(result + 128, v_rip + 3445473, a3, 1);
    if ((unsigned __int8)(result) != 0) goto loc_007BDF92;
    goto loc_007BE1A2;
loc_007BDF92:
    if (v_stack_m754 == 0) goto loc_007BDFB6;
    if (!sign_flag) goto loc_007BE009;
    if (condition_is_above_or_equal) goto loc_007BE009;
    if ((*(unsigned __int64 *)(result + 136)) != 0) goto loc_007BE009;
loc_007BDFB6:
    if (v_stack_m758 == 0) goto loc_007BE01A;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 96))) + (1));
    *(unsigned int *)(result + 96) = (unsigned int)(result);
    if (((unsigned int)(result)) > v_stack_m758) goto loc_007BDFD1;
    if (((unsigned int)(result)) >= = 16) {
        *(unsigned int *)(result + 96) = 1;
    }
    v_stack_m780 = 4;
    v_stack_m788 = result + 96;
    if (v_stack_m750 == 0) goto loc_007BE013;
loc_007BE002:
    result = RtlWriteRegistryValue((unsigned int)(0x40000000ULL), v_stack_m750, v_rip + 3447291, 4);
    goto loc_007BE020;
loc_007BE009:
    goto loc_007BE1A2;
loc_007BE013:
    goto loc_007BE002;
loc_007BE01A:
loc_007BE020:
    result = wcscmp(v_stack_m660, v_rip + 3446949, v_rip + 3447291, 4);
    if ((unsigned int)(result) == 0) goto loc_007BE05E;
    if (v_stack_m6B8 == 0) goto loc_007BE04B;
    result = RtlGUIDFromString(v_stack_m6C0, v_stack_m650, v_rip + 3447291, 4);
    goto loc_007BE050;
loc_007BE04B:
loc_007BE050:
    if (sign_flag) goto loc_007BE1A8;
    goto loc_007BE069;
loc_007BE05E:
    v_stack_m650 = v_xmm0;
loc_007BE069:
    *(unsigned int *)(result) = (unsigned int)(v_r15 + *(unsigned __int16 *)(result + 180 + 44) * 4 + *(unsigned __int16 *)(result + 180 + 44 + 1028) * 4 + *(unsigned __int16 *)(result + 180 + 44 + 1028 + 20) * 4);
    *(unsigned __int64 *)(result + 24) = v_xmm0;
    result = EtwpStartLogger(v_stack_m708, result, v_rip + 3447291, 4);
    if (sign_flag) goto loc_007BE1A8;
    if ((unsigned int)(*(unsigned __int16 *)(result + 8)) == 0) goto loc_007BE0BE;
    if (v_stack_m754 == 0) goto loc_007BE0BE;
loc_007BE09E:
    if (0 >= 16) goto loc_007BE0BE;
    if ((*(unsigned __int16 *)(v_stack_m708 + 0 * 2 + 4304)) == 0) goto loc_007BE0B5;
    result = (unsigned int)((0) + (1));
    goto loc_007BE09E;
loc_007BE0B5:
    *(unsigned __int16 *)(v_stack_m708 + 0 * 2 + 4304) = (unsigned __int16)(*(unsigned __int16 *)(result + 8));
loc_007BE0BE:
    if ((unsigned __int16)(v_stack_m6D0) == 0) goto loc_007BE17E;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m6D0))) - ((unsigned int)(result)));
    result = (unsigned int)((result) >> (1));
    result = (unsigned int)((result) + ((unsigned int)(result)));
    result = (unsigned int)((result) >> (6));
    a1 = (unsigned int)((0) * ((unsigned int)(result)));
    if (((unsigned int)(v_stack_m6D0)) != ((unsigned int)(a1))) goto loc_007BE17E;
    v_stack_m700 = v_stack_m6C8;
    a1 = (unsigned __int16)((v_stack_m6CE) - ((unsigned __int16)(v_stack_m6D0)));
    v_stack_m708 = 76;
    a1 = (unsigned __int16)((a1) + (76));
    v_stack_m704 = 0;
    v_stack_m706 = (unsigned __int16)(a1);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m6D0))) - ((unsigned int)(result)));
    v_rsi = (unsigned int)((v_rsi) >> (1));
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(result)));
    v_rsi = (unsigned int)((v_rsi) >> (6));
    if (((unsigned int)(v_rsi)) > 512) goto loc_007BE17E;
    if ((unsigned int)(v_rsi) == 0) goto loc_007BE160;
loc_007BE13A:
    a2 = (0) << (4);
    a2 = (a2) + (v_stack_m760);
    result = RtlGUIDFromString(v_stack_m708, a2, v_stack_m6D0, (unsigned int)(0xAF286BCBULL));
    if ((unsigned int)(result) != 0) goto loc_007BE17E;
    v_r14 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r14)) < ((unsigned int)(v_rsi))) goto loc_007BE13A;
loc_007BE160:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) {
        result = PsGetCurrentServerSiloGlobals(v_stack_m708, a2, v_stack_m6D0, (unsigned int)(0xAF286BCBULL));
        a4 = v_stack_m760;
        a3 = (unsigned int)(v_rsi);
        a2 = (unsigned int)(*(unsigned __int16 *)(result + 8));
        a1 = *(unsigned __int64 *)(result + 832);
        result = EtwpUpdateDisallowList(a1, a2, a3, a4);
    }
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    v_stack_m788 = (unsigned int)((unsigned int)(v_stack_m764));
    result = EtwpEnableKeyProviders(*(unsigned __int64 *)(result + 832), (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 8))), v_stack_m658, v_stack_m6D8);
loc_007BE1A2:
loc_007BE1A8:
loc_007BE1AD:
    if (v_stack_m730 == 0) goto loc_007BE205;
    if (sign_flag) {
        a1 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = RtlNtStatusToDosError(a1, v_stack_m730, v_stack_m658, v_stack_m6D8);
        a2 = v_stack_m730;
        v_stack_m738 = (unsigned int)(result);
    }
    v_stack_m780 = 4;
    v_stack_m788 = v_stack_m738;
    if (v_stack_m750 != 0) {
        a2 = v_stack_m750;
    }
    result = RtlWriteRegistryValue((unsigned int)(0x40000000ULL), a2, v_rip + 3412183, 4);
    result = ZwClose(v_stack_m730, a2, v_rip + 3412183, 4);
loc_007BE205:
    if (v_stack_m750 != 0) {
        result = ZwClose(v_stack_m750, a2, v_rip + 3412183, 4);
    }
    if (result != 0) {
        a1 = result + 128;
        result = RtlFreeAnsiString(a1, a2, v_rip + 3412183, 4);
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_rip + 3412183, 4);
    }
    if (v_stack_m760 != 0) {
        a2 = 0;
        a1 = v_stack_m760;
        result = ExFreePoolWithTag(a1, a2, v_rip + 3412183, 4);
    }
    result = RtlFreeAnsiString(v_stack_m6C0, a2, v_rip + 3412183, 4);
    result = RtlFreeAnsiString(v_stack_m6B0, a2, v_rip + 3412183, 4);
    result = RtlFreeAnsiString(v_stack_m6D0, a2, v_rip + 3412183, 4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_rip + 3412183, 4);
    v_rsp = (v_rsp) + (0x770ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwStartAutoLogger(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E8;
    uint32_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m210;
    uint32_t v_stack_m218;
    uint64_t v_stack_m220;
    uint32_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m248;
    uint64_t v_stack_m258;
    uint32_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m280;
    uint32_t v_stack_m288;
    uint64_t v_stack_m290;
    uint32_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B8;
    uint32_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint32_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint64_t v_stack_m2F0;
    uint32_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint32_t v_stack_m308;
    uint64_t v_stack_m310;
    uint64_t v_stack_m318;
    uint64_t v_stack_m328;
    uint32_t v_stack_m330;
    uint64_t v_stack_m338;
    uint32_t v_stack_m340;
    uint64_t v_stack_m348;
    uint64_t v_stack_m350;
    uint64_t v_stack_m360;
    uint32_t v_stack_m368;
    uint64_t v_stack_m370;
    uint32_t v_stack_m378;
    uint64_t v_stack_m380;
    uint64_t v_stack_m388;
    uint64_t v_stack_m398;
    uint32_t v_stack_m3A0;
    uint64_t v_stack_m3A8;
    uint32_t v_stack_m3B0;
    uint64_t v_stack_m3B8;
    uint64_t v_stack_m3C0;
    uint64_t v_stack_m3D0;
    uint64_t v_stack_m3E0;
    uint32_t v_stack_m3E8;
    uint64_t v_stack_m3F0;
    uint64_t v_stack_m3F8;
    uint64_t v_stack_m408;
    uint64_t v_stack_m418;
    uint32_t v_stack_m420;
    uint64_t v_stack_m428;
    uint64_t v_stack_m430;
    uint64_t v_stack_m440;
    uint64_t v_stack_m450;
    uint32_t v_stack_m458;
    uint64_t v_stack_m460;
    uint64_t v_stack_m468;
    uint64_t v_stack_m478;
    uint64_t v_stack_m48;
    uint64_t v_stack_m480;
    uint64_t v_stack_m488;
    uint32_t v_stack_m490;
    uint64_t v_stack_m498;
    uint64_t v_stack_m4A0;
    uint64_t v_stack_m4B0;
    uint64_t v_stack_m4C0;
    uint32_t v_stack_m4C8;
    uint64_t v_stack_m4D0;
    uint64_t v_stack_m4D8;
    uint64_t v_stack_m4E8;
    uint64_t v_stack_m500;
    uint64_t v_stack_m508;
    uint64_t v_stack_m510;
    uint64_t v_stack_m518;
    uint64_t v_stack_m520;
    uint64_t v_stack_m528;
    uint64_t v_stack_m530;
    uint64_t v_stack_m538;
    uint64_t v_stack_m540;
    uint64_t v_stack_m548;
    uint64_t v_stack_m550;
    uint64_t v_stack_m558;
    uint64_t v_stack_m560;
    uint64_t v_stack_m568;
    uint64_t v_stack_m570;
    uint64_t v_stack_m578;
    uint64_t v_stack_m580;
    uint64_t v_stack_m588;
    uint64_t v_stack_m590;
    uint64_t v_stack_m598;
    uint64_t v_stack_m5A0;
    uint64_t v_stack_m5A8;
    uint64_t v_stack_m5B0;
    uint64_t v_stack_m5B8;
    uint64_t v_stack_m5C0;
    uint64_t v_stack_m5C8;
    uint64_t v_stack_m5D0;
    uint64_t v_stack_m5D8;
    uint64_t v_stack_m5E0;
    uint64_t v_stack_m5E8;
    uint64_t v_stack_m5F0;
    uint64_t v_stack_m5F8;
    uint64_t v_stack_m600;
    uint64_t v_stack_m608;
    uint64_t v_stack_m610;
    uint64_t v_stack_m618;
    uint64_t v_stack_m620;
    uint64_t v_stack_m628;
    uint64_t v_stack_m630;
    uint64_t v_stack_m638;
    uint64_t v_stack_m650;
    uint64_t v_stack_m658;
    uint64_t v_stack_m660;
    uint64_t v_stack_m670;
    uint64_t v_stack_m680;
    uint32_t v_stack_m684;
    uint32_t v_stack_m688;
    uint64_t v_stack_m690;
    uint64_t v_stack_m698;
    uint32_t v_stack_m69C;
    uint32_t v_stack_m6A0;
    uint64_t v_stack_m6A8;
    uint64_t v_stack_m6B0;
    uint64_t v_stack_m6B8;
    uint64_t v_stack_m6C0;
    uint64_t v_stack_m6C8;
    uint16_t v_stack_m6CE;
    uint64_t v_stack_m6D0;
    uint64_t v_stack_m6D8;
    uint32_t v_stack_m6E0;
    uint32_t v_stack_m6E4;
    uint32_t v_stack_m6E8;
    uint64_t v_stack_m6F0;
    uint64_t v_stack_m6F4;
    uint64_t v_stack_m6F8;
    uint64_t v_stack_m700;
    uint32_t v_stack_m704;
    uint16_t v_stack_m706;
    uint64_t v_stack_m708;
    uint64_t v_stack_m710;
    uint64_t v_stack_m714;
    uint64_t v_stack_m718;
    uint64_t v_stack_m720;
    uint64_t v_stack_m724;
    uint64_t v_stack_m728;
    uint64_t v_stack_m730;
    uint32_t v_stack_m738;
    uint32_t v_stack_m73C;
    uint32_t v_stack_m740;
    uint32_t v_stack_m744;
    uint16_t v_stack_m748;
    uint64_t v_stack_m750;
    uint32_t v_stack_m754;
    uint32_t v_stack_m758;
    uint64_t v_stack_m760;
    uint32_t v_stack_m764;
    uint16_t v_stack_m768;
    uint64_t v_stack_m778;
    uint8_t v_stack_m780;
    uint64_t v_stack_m788;
    uint32_t v_stack_m90;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (0x770ULL);
    result = (*(uint64_t *)(v_rip + 0x64D422)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r13 = 0;
    v_stack_m6D8 = Arg3;
    result = 0;
    v_stack_m658 = Arg2;
    v_stack_m6F4 = 0;
    v_stack_m714 = 0;
    v_stack_m724 = 0;
    v_stack_m660 = Arg1;
    v_stack_m6E8 = (uint32_t)(result + 1);
    v_stack_m69C = 0;
    v_stack_m684 = 0;
    v_stack_m670 = v_xmm0;
    v_stack_m730 = 0;
    v_stack_m750 = 0;
    v_stack_m738 = 0;
    v_stack_m740 = 0;
    v_stack_m6C0 = v_xmm0;
    v_stack_m6F8 = 0;
    v_stack_m6B0 = v_xmm1;
    v_stack_m718 = 0;
    v_stack_m6D0 = v_xmm0;
    v_stack_m728 = 0;
    v_stack_m758 = 0;
    v_stack_m73C = 0;
    v_stack_m754 = 0;
    v_stack_m764 = 0;
    v_stack_m768 = 0;
    v_stack_m6E0 = 0;
    v_stack_m6E4 = 100;
    v_stack_m748 = 0;
    v_stack_m650 = v_xmm0;
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, a4);
    v_stack_m708 = *(uint64_t *)(result + 0x340);
    result = RtlInitUnicodeString(v_stack_m670, Arg2, Arg3, a4);
    v_stack_m6A0 = 48;
    v_stack_m690 = v_stack_m670;
    v_stack_m698 = 0;
    v_stack_m688 = 576;
    v_stack_m680 = v_xmm0;
    result = ZwOpenKey(v_stack_m730, (uint32_t)(0x2001FULL), v_stack_m6A0, a4);
    if (sign_flag) goto loc_007BE1AD;
    result = ExAllocatePool2(256, (uint32_t)(0x2000ULL), (uint32_t)((uint32_t)((uint32_t)(0x50777445ULL))), a4);
    v_stack_m760 = result;
    if (result != 0) goto loc_007BD44D;
loc_007BD443:
    goto loc_007BE1AD;
loc_007BD44D:
    result = ExAllocatePool2(256, (uint32_t)(0x504ULL), (uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))), a4);
    if (result == 0) goto loc_007BD443;
    *(uint32_t *)(result + 0x2C) = 0x20000ULL;
    *(uint32_t *)(result + 0x30) = (uint32_t)(local_r13 + 4);
    result = RtlInitUnicodeString(result + 144, Arg1, (uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))), a4);
    *(uint32_t *)(result + 0x48) = 0x80000000ULL;
    *(uint8_t *)(result + 0x4A) = 255;
    *(uint16_t *)(result + 0x48) = 176;
    *(uint32_t *)(result + 0xB0) = (uint32_t)(result + 1);
    Arg2 = 0;
    result = memset(v_stack_m4E8, Arg2, (uint32_t)(0x498ULL), a4);
    v_stack_m4E8 = v_rip + 5482;
    v_stack_m4C8 = 4;
    v_stack_m4D0 = v_stack_m638;
    v_stack_m638 = 4;
    v_stack_m4D8 = v_rip + 3410511;
    v_stack_m630 = v_stack_m740;
    v_stack_m498 = v_stack_m628;
    v_stack_m4A0 = v_rip + 3450487;
    v_stack_m4B0 = v_rip + 5482;
    a4 = 0;
    v_stack_m490 = 4;
    v_stack_m628 = 4;
    v_stack_m620 = v_stack_m764;
    v_stack_m780 = 1;
    result = RtlpQueryRegistryValues((uint32_t)(0x40000000ULL), v_stack_m730, v_stack_m4E8, a4);
    Arg2 = 0;
    if (sign_flag) goto loc_007BE1A2;
    if (v_stack_m6D8 == 0) goto loc_007BD63B;
    v_stack_m744 = 0;
    result = RtlInitUnicodeString(v_stack_m670, v_stack_m6D8, v_stack_m4E8, a4);
    Arg1 = 0;
    v_stack_m6A0 = 48;
    v_stack_m698 = 0;
    v_stack_m690 = v_stack_m670;
    v_stack_m688 = 576;
    v_stack_m778 = v_stack_m744;
    v_stack_m780 = 0;
    a4 = 0;
    v_stack_m788 = 0;
    v_stack_m680 = v_xmm0;
    result = ZwCreateKey(v_stack_m750, (uint32_t)(0x2001FULL), v_stack_m6A0, a4);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_007BD61A;
    result = EtwpCreateKeyTreeForPath(v_stack_m6D8, (uint32_t)(0x2001FULL), v_stack_m6A0, a4);
    Arg2 = 0;
    if ((uint32_t)(result) != 0) goto loc_007BD620;
    a4 = 0;
    v_stack_m778 = v_stack_m744;
    v_stack_m780 = 0;
    v_stack_m788 = 0;
    result = ZwCreateKey(v_stack_m750, (uint32_t)(0x2001FULL), v_stack_m6A0, a4);
loc_007BD61A:
    Arg2 = 0;
    local_rdi = (uint32_t)((uint32_t)(result));
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) {
        local_rdi = 0;
        v_stack_m750 = 0;
    }
    if (v_stack_m744 != 1) goto loc_007BD641;
    v_stack_m764 = 1;
    goto loc_007BD641;
loc_007BD63B:
loc_007BD641:
    if (v_stack_m764 != 0) goto loc_007BD6A3;
    if (v_stack_m750 != 0) {
        v_stack_m780 = 1;
        result = 0;
        Arg3 = v_stack_m4E8;
        v_stack_m480 = 0;
        Arg2 = v_stack_m750;
        result = v_stack_m740;
        a4 = 0;
        Arg1 = 0x40000000ULL;
        v_stack_m4C0 = result;
        v_stack_m4B0 = v_xmm0;
        v_stack_m4A0 = v_xmm0;
        v_stack_m490 = v_xmm0;
        result = RtlpQueryRegistryValues(Arg1, Arg2, Arg3, a4);
        Arg2 = 0;
        local_rdi = (uint32_t)(result);
        if (sign_flag) { local_rdi = 0; }
    }
    if (v_stack_m740 == 0) goto loc_007BE1A2;
    v_stack_m6F8 = 40;
    v_stack_m4C8 = 4;
    v_stack_m4E8 = v_rip + 4992;
    v_stack_m4D0 = v_stack_m638;
    v_stack_m4D8 = v_rip + 3450017;
    v_stack_m638 = 4;
    v_stack_m630 = result + 76;
    v_stack_m4B0 = v_rip + 4992;
    v_stack_m498 = v_stack_m628;
    v_stack_m4A0 = v_rip + 3449772;
    v_stack_m620 = result + 48;
    v_stack_m460 = v_stack_m618;
    v_stack_m468 = v_rip + 3449701;
    v_stack_m610 = result + 52;
    v_stack_m428 = v_stack_m608;
    v_stack_m430 = v_rip + 3449758;
    v_stack_m600 = result + 68;
    v_stack_m3F0 = v_stack_m5F8;
    v_stack_m3F8 = v_rip + 3449687;
    v_stack_m5F0 = result + 56;
    v_stack_m3B8 = v_stack_m5E8;
    v_stack_m3C0 = v_rip + 3449488;
    v_stack_m3A8 = v_stack_m768;
    v_stack_m5E0 = result + 128;
    v_stack_m6F0 = result + 180 + 4;
    v_stack_m380 = v_stack_m5D8;
    v_stack_m388 = v_rip + 3444674;
    v_stack_m5D0 = v_stack_m6F8;
    v_stack_m720 = result + 180 + 44 + 4;
    v_stack_m348 = v_stack_m5C8;
    v_stack_m350 = v_rip + 3449330;
    v_stack_m490 = 4;
    v_stack_m628 = 4;
    v_stack_m478 = v_rip + 4992;
    v_stack_m458 = 4;
    v_stack_m618 = 4;
    v_stack_m440 = v_rip + 4992;
    v_stack_m420 = 4;
    v_stack_m608 = 4;
    v_stack_m408 = v_rip + 4992;
    v_stack_m3E8 = 4;
    v_stack_m5F8 = 4;
    v_stack_m3D0 = v_rip + 4992;
    v_stack_m3B0 = (uint32_t)(4 - 3);
    v_stack_m5E8 = (uint32_t)(4 - 3);
    v_stack_m398 = v_rip + 4992;
    v_stack_m378 = (uint32_t)(4 - 1);
    v_stack_m5D8 = (uint32_t)(4 - 1);
    v_stack_m728 = 0x400ULL;
    v_stack_m360 = v_rip + 4992;
    v_stack_m340 = (uint32_t)(4 - 1);
    v_stack_m5C8 = (uint32_t)(4 - 1);
    v_stack_m5C0 = v_stack_m728;
    v_stack_m310 = v_stack_m5B8;
    v_stack_m318 = v_rip + 3449266;
    v_stack_m300 = v_stack_m6E8;
    v_stack_m5B0 = result + 40;
    v_stack_m2D8 = v_stack_m5A8;
    v_stack_m2E0 = v_rip + 3449184;
    v_stack_m2C8 = v_stack_m6E4;
    v_stack_m5A0 = result + 60;
    v_stack_m2A0 = v_stack_m598;
    v_stack_m2A8 = v_rip + 3448974;
    v_stack_m290 = v_stack_m6E0;
    v_stack_m590 = result + 64;
    v_stack_m268 = v_stack_m588;
    v_stack_m270 = v_rip + 3448860;
    v_stack_m580 = v_stack_m73C;
    v_stack_m230 = v_stack_m578;
    v_stack_m238 = v_rip + 3448948;
    v_stack_m220 = v_stack_m768;
    v_stack_m570 = v_stack_m6C0;
    v_stack_m1F8 = v_stack_m568;
    v_stack_m200 = v_rip + 3448865;
    v_stack_m560 = result + 96;
    v_stack_m1C0 = v_stack_m558;
    v_stack_m1C8 = v_rip + 3449754;
    v_stack_m550 = v_stack_m758;
    v_stack_m188 = v_stack_m548;
    v_stack_m328 = v_rip + 4992;
    v_stack_m308 = 4;
    v_stack_m2F8 = 4;
    v_stack_m5B8 = 4;
    v_stack_m2F0 = v_rip + 4992;
    v_stack_m2D0 = 4;
    v_stack_m2C0 = 4;
    v_stack_m5A8 = 4;
    v_stack_m2B8 = v_rip + 4992;
    v_stack_m298 = 4;
    v_stack_m288 = 4;
    v_stack_m598 = 4;
    v_stack_m280 = v_rip + 4992;
    v_stack_m260 = 4;
    v_stack_m588 = 4;
    v_stack_m248 = v_rip + 4992;
    v_stack_m228 = (uint32_t)(4 - 3);
    v_stack_m578 = (uint32_t)(4 - 3);
    v_stack_m210 = v_rip + 4992;
    v_stack_m1F0 = 4;
    v_stack_m568 = 4;
    v_stack_m1D8 = v_rip + 4992;
    v_stack_m1B8 = 4;
    v_stack_m558 = 4;
    v_stack_m1A0 = v_rip + 4992;
    v_stack_m190 = v_rip + 3449682;
    v_stack_m180 = (uint32_t)(4 - 3);
    v_stack_m178 = v_stack_m768;
    v_stack_m540 = v_stack_m6B0;
    v_stack_m710 = result + 180 + 44 + 1028 + 20 + 4;
    v_stack_m150 = v_stack_m538;
    v_stack_m158 = v_rip + 3449551;
    v_stack_m530 = v_stack_m718;
    v_stack_m118 = v_stack_m528;
    v_stack_m120 = v_rip + 3449464;
    v_stack_m520 = v_stack_m754;
    v_stack_mE0 = v_stack_m518;
    v_stack_mE8 = v_rip + 3449280;
    v_stack_mD0 = v_stack_m768;
    v_stack_m510 = v_stack_m6D0;
    v_stack_mA8 = v_stack_m508;
    v_stack_mB0 = v_rip + 3449197;
    v_stack_mA0 = (uint32_t)(4 + 7);
    v_stack_m508 = (uint32_t)(4 + 7);
    v_stack_m548 = (uint32_t)(4 - 3);
    v_stack_m168 = v_rip + 4992;
    v_stack_m148 = (uint32_t)(4 - 1);
    v_stack_m538 = (uint32_t)(4 - 1);
    a4 = 0;
    v_stack_m130 = v_rip + 4992;
    v_stack_m110 = 4;
    v_stack_m528 = 4;
    v_stack_mF8 = v_rip + 4992;
    v_stack_mD8 = (uint32_t)(4 - 3);
    v_stack_m518 = (uint32_t)(4 - 3);
    v_stack_mC0 = v_rip + 4992;
    v_stack_m780 = (uint8_t)(4 - 3);
    v_stack_m500 = result + 80;
    v_stack_m718 = (uint32_t)(4 + 4);
    v_stack_m90 = (uint32_t)(4 + 4);
    result = RtlpQueryRegistryValues((uint32_t)(0x40000000ULL), v_stack_m730, v_stack_m4E8, a4);
    Arg3 = 0;
    if (sign_flag) goto loc_007BE1A2;
    if (v_stack_m750 == 0) goto loc_007BDDB3;
    if (v_stack_m764 != 0) goto loc_007BDD49;
    v_stack_m4C0 = result + 76;
    v_stack_m488 = result + 48;
    v_stack_m450 = result + 52;
    v_stack_m418 = result + 68;
    v_stack_m3E0 = result + 56;
    v_stack_m3A8 = *(uint64_t *)(result + 0x88);
    v_stack_m3A0 = (uint32_t)(*(uint16_t *)(result + 0x80));
    v_stack_m370 = v_stack_m6F0;
    v_stack_m368 = (uint32_t)((uint32_t)(v_stack_m6F8));
    v_stack_m338 = v_stack_m720;
    v_stack_m330 = (uint32_t)((uint32_t)(v_stack_m728));
    v_stack_m300 = result + 40;
    v_stack_m2C8 = result + 60;
    v_stack_m290 = result + 64;
    v_stack_m258 = v_stack_m73C;
    v_stack_m220 = v_stack_m6B8;
    v_stack_m218 = (uint32_t)(v_stack_m6C0);
    v_stack_m1E8 = result + 96;
    v_stack_m1B0 = v_stack_m758;
    v_stack_m178 = v_stack_m6A8;
    v_stack_m170 = (uint32_t)(v_stack_m6B0);
    v_stack_m140 = v_stack_m710;
    v_stack_m138 = (uint32_t)((uint32_t)(v_stack_m718));
    v_stack_m108 = v_stack_m754;
    v_stack_mD0 = v_stack_m6C8;
    v_stack_mC8 = (uint32_t)(v_stack_m6D0);
    goto loc_007BDD97;
loc_007BDD49:
    v_stack_m4B0 = 0;
    v_stack_m4D0 = v_stack_m568;
    v_stack_m4E8 = v_rip + 3291;
    v_stack_m4D8 = v_rip + 3447924;
    v_stack_m4C8 = 4;
    v_stack_m4C0 = result + 96;
    v_stack_m630 = result + 96;
    v_stack_m638 = 4;
loc_007BDD97:
    a4 = 0;
    v_stack_m780 = 1;
    result = RtlpQueryRegistryValues((uint32_t)(0x40000000ULL), v_stack_m750, v_stack_m4E8, a4);
    Arg3 = 0;
loc_007BDDB3:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x70))) | (2));
    *(uint32_t *)(result + 0x70) = (uint32_t)(result);
    if (v_stack_m73C == 0) {
        result = (uint32_t)((result) | (1));
        *(uint32_t *)(result + 0x70) = (uint32_t)(result);
    }
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m6F8)) >> (2));
    local_r15 = 180;
    if ((uint16_t)(local_rdi) != 0) {
        result = 1 + local_rdi * 1;
        *(uint16_t *)(result + 0xB4 + 0x2) = 1;
        *(uint16_t *)(result + 0xB4) = (uint16_t)(result);
        result = *(uint16_t *)(result + 0xB4);
        local_r15 = result * 4 + 180;
    }
    if ((uint32_t)((uint32_t)(v_stack_m728)) == 0) goto loc_007BDE74;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m728)))) >> (2));
    *(uint16_t *)(result + 0xB4 + 0x2C + 0x2) = 3;
    Arg1 = 1 + result * 1;
    if (((3) & ((uint8_t)((uint32_t)(v_stack_m728)))) == 0) { Arg1 = (uint16_t)(result); }
    *(uint16_t *)(result + 0xB4 + 0x2C) = (uint16_t)(1 + Arg1 * 1);
    result = *(uint16_t *)(result + 0xB4 + 0x2C);
    local_rsi = result + 180;
    if ((uint16_t)(local_rdi) != 0) {
        result = *(uint16_t *)(result + 0xB4);
        local_rsi = result + 180 + result * 4;
    }
    if (local_rsi != (result + 180 + 44)) {
        Arg3 = (uint16_t)(Arg1);
        Arg2 = result + 180 + 44;
        Arg1 = local_rsi;
        Arg3 = Arg3 * 4 + 4;
        result = memcpy(Arg1, Arg2, Arg3, 1);
        Arg3 = 0;
    }
    if (v_stack_m6A8 == 0) goto loc_007BDEE5;
    result = (*(uint16_t *)(result + 0xB0)) + (44);
    result = EtwpParsePoolTagFilter(v_stack_m6B0, result + 180 + 44 + 1028 + 4, Arg3, 1);
    if ((uint16_t)((uint16_t)(result)) == 0) goto loc_007BDEEA;
    *(uint16_t *)(result + 0xB4 + 0x2C + 0x404 + 0x2) = 4;
    *(uint16_t *)(result + 0xB4 + 0x2C + 0x404) = (uint16_t)(1 + (uint16_t)(result) * 1);
    if ((result + result * 4) == (result + 180 + 44 + 1028)) goto loc_007BDEEA;
    result = memcpy(result + result * 4, result + 180 + 44 + 1028, (uint16_t)(result) * 4 + 4, 1);
    goto loc_007BDEEA;
loc_007BDEE5:
loc_007BDEEA:
    if (v_stack_m718 != 8) goto loc_007BDF3B;
    *(uint32_t *)(result + 0xB4 + 0x2C + 0x404 + 0x14) = 0x50003ULL;
    Arg1 = (*(uint16_t *)(result + 0xB0)) + (44);
    result = *(uint16_t *)(result + 0xB4 + 0x2C + 0x404 + 0x14);
    if ((result + Arg1 * 4) != (result + 180 + 44 + 1028 + 20)) {
        Arg3 = 1 + 11;
        Arg2 = result + 180 + 44 + 1028 + 20;
        result = memcpy(result + Arg1 * 4, Arg2, Arg3, 1);
    }
    local_r13 = 0;
    if ((uint16_t)(local_rdi) != 0) goto loc_007BDF58;
    if (v_stack_m728 != 0) goto loc_007BDF58;
    if (v_stack_m718 != 0) goto loc_007BDF58;
    if ((uint16_t)(v_stack_m748) == 0) {
        *(uint32_t *)(result + 0x48) = 0;
    }
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x40)))) & (0x500ULL)) == 0) goto loc_007BDF68;
    if (condition_is_above_or_equal) goto loc_007BDF92;
loc_007BDF68:
    if ((*(uint64_t *)(result + 0x88)) != 0) goto loc_007BDF92;
    result = RtlCreateUnicodeString(result + 128, v_rip + 3445473, Arg3, 1);
    if ((uint8_t)(result) != 0) goto loc_007BDF92;
    goto loc_007BE1A2;
loc_007BDF92:
    if (v_stack_m754 == 0) goto loc_007BDFB6;
    if (!sign_flag) goto loc_007BE009;
    if (condition_is_above_or_equal) goto loc_007BE009;
    if ((*(uint64_t *)(result + 0x88)) != 0) goto loc_007BE009;
loc_007BDFB6:
    if (v_stack_m758 == 0) goto loc_007BE01A;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x60))) + (1));
    *(uint32_t *)(result + 0x60) = (uint32_t)(result);
    if (((uint32_t)(result)) > v_stack_m758) goto loc_007BDFD1;
    if (((uint32_t)(result)) >= = 16) {
        *(uint32_t *)(result + 0x60) = 1;
    }
    v_stack_m780 = 4;
    v_stack_m788 = result + 96;
    if (v_stack_m750 == 0) goto loc_007BE013;
loc_007BE002:
    result = RtlWriteRegistryValue((uint32_t)(0x40000000ULL), v_stack_m750, v_rip + 3447291, 4);
    goto loc_007BE020;
loc_007BE009:
    goto loc_007BE1A2;
loc_007BE013:
    goto loc_007BE002;
loc_007BE01A:
loc_007BE020:
    result = wcscmp(v_stack_m660, v_rip + 3446949, v_rip + 3447291, 4);
    if ((uint32_t)(result) == 0) goto loc_007BE05E;
    if (v_stack_m6B8 == 0) goto loc_007BE04B;
    result = RtlGUIDFromString(v_stack_m6C0, v_stack_m650, v_rip + 3447291, 4);
    goto loc_007BE050;
loc_007BE04B:
loc_007BE050:
    if (sign_flag) goto loc_007BE1A8;
    goto loc_007BE069;
loc_007BE05E:
    v_stack_m650 = v_xmm0;
loc_007BE069:
    *(uint32_t *)(result) = (uint32_t)(local_r15 + *(uint16_t *)(result + 0xB4 + 0x2C) * 4 + *(uint16_t *)(result + 0xB4 + 0x2C + 0x404) * 4 + *(uint16_t *)(result + 0xB4 + 0x2C + 0x404 + 0x14) * 4);
    *(uint64_t *)(result + 0x18) = v_xmm0;
    result = EtwpStartLogger(v_stack_m708, result, v_rip + 3447291, 4);
    if (sign_flag) goto loc_007BE1A8;
    if ((uint32_t)(*(uint16_t *)(result + 0x8)) == 0) goto loc_007BE0BE;
    if (v_stack_m754 == 0) goto loc_007BE0BE;
loc_007BE09E:
    if (0 >= 16) goto loc_007BE0BE;
    if ((*(uint16_t *)(v_stack_m708 + 0x0 * 2 + 0x10D0)) == 0) goto loc_007BE0B5;
    result = (uint32_t)((0) + (1));
    goto loc_007BE09E;
loc_007BE0B5:
    *(uint16_t *)(v_stack_m708 + 0x0 * 2 + 0x10D0) = (uint16_t)(*(uint16_t *)(result + 0x8));
loc_007BE0BE:
    if ((uint16_t)(v_stack_m6D0) == 0) goto loc_007BE17E;
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m6D0))) - ((uint32_t)(result)));
    result = (uint32_t)((result) >> (1));
    result = (uint32_t)((result) + ((uint32_t)(result)));
    result = (uint32_t)((result) >> (6));
    Arg1 = (uint32_t)((0) * ((uint32_t)(result)));
    if (((uint32_t)(v_stack_m6D0)) != ((uint32_t)(Arg1))) goto loc_007BE17E;
    v_stack_m700 = v_stack_m6C8;
    Arg1 = (uint16_t)((v_stack_m6CE) - ((uint16_t)(v_stack_m6D0)));
    v_stack_m708 = 76;
    Arg1 = (uint16_t)((Arg1) + (76));
    v_stack_m704 = 0;
    v_stack_m706 = (uint16_t)(Arg1);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m6D0))) - ((uint32_t)(result)));
    local_rsi = (uint32_t)((local_rsi) >> (1));
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(result)));
    local_rsi = (uint32_t)((local_rsi) >> (6));
    if (((uint32_t)(local_rsi)) > 512) goto loc_007BE17E;
    if ((uint32_t)(local_rsi) == 0) goto loc_007BE160;
loc_007BE13A:
    Arg2 = (0) << (4);
    Arg2 = (Arg2) + (v_stack_m760);
    result = RtlGUIDFromString(v_stack_m708, Arg2, v_stack_m6D0, (uint32_t)(0xAF286BCBULL));
    if ((uint32_t)(result) != 0) goto loc_007BE17E;
    local_r14 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r14)) < ((uint32_t)(local_rsi))) goto loc_007BE13A;
loc_007BE160:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) {
        result = PsGetCurrentServerSiloGlobals(v_stack_m708, Arg2, v_stack_m6D0, (uint32_t)(0xAF286BCBULL));
        a4 = v_stack_m760;
        Arg3 = (uint32_t)(local_rsi);
        Arg2 = (uint32_t)(*(uint16_t *)(result + 0x8));
        Arg1 = *(uint64_t *)(result + 0x340);
        result = EtwpUpdateDisallowList(Arg1, Arg2, Arg3, a4);
    }
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, a4);
    v_stack_m788 = (uint32_t)((uint32_t)(v_stack_m764));
    result = EtwpEnableKeyProviders(*(uint64_t *)(result + 0x340), (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x8))), v_stack_m658, v_stack_m6D8);
loc_007BE1A2:
loc_007BE1A8:
loc_007BE1AD:
    if (v_stack_m730 == 0) goto loc_007BE205;
    if (sign_flag) {
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = RtlNtStatusToDosError(Arg1, v_stack_m730, v_stack_m658, v_stack_m6D8);
        Arg2 = v_stack_m730;
        v_stack_m738 = (uint32_t)(result);
    }
    v_stack_m780 = 4;
    v_stack_m788 = v_stack_m738;
    if (v_stack_m750 != 0) {
        Arg2 = v_stack_m750;
    }
    result = RtlWriteRegistryValue((uint32_t)(0x40000000ULL), Arg2, v_rip + 3412183, 4);
    result = ZwClose(v_stack_m730, Arg2, v_rip + 3412183, 4);
loc_007BE205:
    if (v_stack_m750 != 0) {
        result = ZwClose(v_stack_m750, Arg2, v_rip + 3412183, 4);
    }
    if (result != 0) {
        Arg1 = result + 128;
        result = RtlFreeAnsiString(Arg1, Arg2, v_rip + 3412183, 4);
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_rip + 3412183, 4);
    }
    if (v_stack_m760 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m760;
        result = ExFreePoolWithTag(Arg1, Arg2, v_rip + 3412183, 4);
    }
    result = RtlFreeAnsiString(v_stack_m6C0, Arg2, v_rip + 3412183, 4);
    result = RtlFreeAnsiString(v_stack_m6B0, Arg2, v_rip + 3412183, 4);
    result = RtlFreeAnsiString(v_stack_m6D0, Arg2, v_rip + 3412183, 4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_rip + 3412183, 4);
    local_rsp = (local_rsp) + (0x770ULL);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007BD2F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
