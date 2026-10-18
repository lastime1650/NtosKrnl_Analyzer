# sub_008EE966

- RVA: `0x008EE966`–`0x008EF0D3` (길이 `1,901` bytes)
- VA: `0x00000001408EE966`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086FA4`
- 디코드: `456`개 명령, `1,901/1,901` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x008EE9A8` → [_CmOpenDeviceRegKey](_CmOpenDeviceRegKey_function_008EE540.md) (function, `0x008EE540`)
- `0x008EE9C1` → [_CmGetDeviceRegKeySecurityDescriptor](../A8/_CmGetDeviceRegKeySecurityDescriptor_function_00A83E80.md) (function, `0x00A83E80`)
- `0x008EEA11` → [PnpCtxRegCreateTree](../93/PnpCtxRegCreateTree_function_00931CA0.md) (function, `0x00931CA0`)
- `0x008EEAC0` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x008EEAEF` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x008EEB0C` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x008EEBA2` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x008EEC21` → [RtlPrefixUnicodeString](../8F/RtlPrefixUnicodeString_function_008F4F70.md) (function, `0x008F4F70`)
- `0x008EED3E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008EED78` → [SysCtxRegOpenCurrentUserKey](../8F/SysCtxRegOpenCurrentUserKey_function_008F455C.md) (function, `0x008F455C`)
- `0x008EEE20` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x008EEE56` → [_CmGetDeviceSoftwareKeyPath](../99/_CmGetDeviceSoftwareKeyPath_function_00991090.md) (function, `0x00991090`)
- `0x008EF054` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x008EF0A8` → [PnpCtxRegOpenKey](PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x008EEA83` → RVA `0x00AFD5E0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008EEA8F` → RVA `0x00B0D550` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008EEAA3` → RVA `0x00AFDE50` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008EEB11` → RVA `0x00001A10` (`.rdata`; read)
- `0x008EEBA7` → RVA `0x00001A20` (`.rdata`; read)
- `0x008EEC1A` → RVA `0x00001B78` (`.rdata`; read)
- `0x008EEE03` → RVA `0x00AFD430` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008EEEF0` → RVA `0x00B0D370` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008EEF3D` → RVA `0x00B0D340` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008EEFC8` → RVA `0x00B0D590` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008EF02B` → RVA `0x00B0D620` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008EF03A` → RVA `0x00B0D700` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x008EEAC0` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
  - `0x008EEAEF` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x008EEB0C` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x008EEBA2` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x008EED3E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008EEE20` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
  - `0x008EF054` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **25**
  - `0x008EE969` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EE9B2` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EE9CB` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EEA43` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EEA4E` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EEA59` → [sub_008EE91B + 0x2C](Unknown_function_008EE91B.md) (`tail-transfer`)
  - `0x008EEA65` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EEA70` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EEAD5` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EEAF9` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EEB85` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EEBC8` → [sub_008EE74B + 0xD6](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EEC38` → [sub_008EE74B + 0xE0](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EED53` → [sub_008EE74B + 0x2B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EED59` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EED82` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EED8C` → [sub_008EE74B + 0x10B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EED97` → [sub_008EE74B + 0xE0](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EF06B` → [sub_00B1DB46 + 0x10](../B1/Unknown_function_00B1DB46.md) (`tail-transfer`)
  - `0x008EF078` → [sub_00B1DB46](../B1/Unknown_function_00B1DB46.md) (`tail-transfer`)
  - `0x008EF08D` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EF0B2` → [sub_008EE91B + 0x2C](Unknown_function_008EE91B.md) (`tail-transfer`)
  - `0x008EF0BA` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EF0C3` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)
  - `0x008EF0CE` → [sub_008EE74B + 0x15B](Unknown_function_008EE74B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008EE966  44 8B F8                        mov r15d, eax
008EE969  E9 38 FF FF FF                  jmp 0x1408ee8a6
008EE96E  83 FF 10                        cmp edi, 0x10
008EE971  75 08                           jne 0x1408ee97b
008EE973  F7 C6 00 0F 00 00               test esi, 0xf00
008EE979  74 3D                           je 0x1408ee9b8
008EE97B  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
008EE97F  48 8D 45 EF                     lea rax, [rbp - 0x11]
008EE983  48 C7 44 24 38 00 00 00 00      mov qword ptr [rsp + 0x38], 0
008EE98C  45 33 C9                        xor r9d, r9d
008EE98F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008EE994  49 8B CC                        mov rcx, r12
008EE997  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
008EE99C  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
008EE9A4  45 8D 41 10                     lea r8d, [r9 + 0x10]
008EE9A8  E8 93 FB FF FF                  call 0x1408ee540
008EE9AD  44 8B F8                        mov r15d, eax
008EE9B0  85 C0                           test eax, eax
008EE9B2  0F 88 EE FE FF FF               js 0x1408ee8a6
008EE9B8  4C 8D 45 DF                     lea r8, [rbp - 0x21]
008EE9BC  8B D6                           mov edx, esi
008EE9BE  49 8B CC                        mov rcx, r12
008EE9C1  E8 BA 54 19 00                  call 0x140a83e80
008EE9C6  44 8B F8                        mov r15d, eax
008EE9C9  85 C0                           test eax, eax
008EE9CB  0F 88 D5 FE FF FF               js 0x1408ee8a6
008EE9D1  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
008EE9D5  B8 06 00 0E 00                  mov eax, 0xe0006
008EE9DA  8B 75 67                        mov esi, dword ptr [rbp + 0x67]
008EE9DD  48 85 C9                        test rcx, rcx
008EE9E0  4D 8B C6                        mov r8, r14
008EE9E3  48 8B D3                        mov rdx, rbx
008EE9E6  0F 45 F0                        cmovne esi, eax
008EE9E9  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
008EE9ED  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008EE9F2  45 33 C9                        xor r9d, r9d
008EE9F5  48 8D 45 CF                     lea rax, [rbp - 0x31]
008EE9F9  83 FF 13                        cmp edi, 0x13
008EE9FC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008EEA01  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008EEA06  41 0F 94 C1                     sete r9b
008EEA0A  49 8B CC                        mov rcx, r12
008EEA0D  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
008EEA11  E8 8A 32 04 00                  call 0x140931ca0
008EEA16  3D 7C 01 00 C0                  cmp eax, 0xc000017c
008EEA1B  74 4D                           je 0x1408eea6a
008EEA1D  85 C0                           test eax, eax
008EEA1F  0F 88 65 06 00 00               js 0x1408ef08a
008EEA25  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
008EEA28  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
008EEA2C  3B F0                           cmp esi, eax
008EEA2E  0F 85 5E 06 00 00               jne 0x1408ef092
008EEA34  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
008EEA38  48 89 01                        mov qword ptr [rcx], rax
008EEA3B  48 C7 45 CF 00 00 00 00         mov qword ptr [rbp - 0x31], 0
008EEA43  E9 5E FE FF FF                  jmp 0x1408ee8a6
008EEA48  41 BF E5 00 00 C0               mov r15d, 0xc00000e5
008EEA4E  E9 53 FE FF FF                  jmp 0x1408ee8a6
008EEA53  F7 C6 00 0F 00 00               test esi, 0xf00
008EEA59  0F 85 E8 FE FF FF               jne 0x1408ee947
008EEA5F  41 BF 0E 00 00 C0               mov r15d, 0xc000000e
008EEA65  E9 3C FE FF FF                  jmp 0x1408ee8a6
008EEA6A  41 BF E5 00 00 C0               mov r15d, 0xc00000e5
008EEA70  E9 31 FE FF FF                  jmp 0x1408ee8a6
008EEA75  89 45 C7                        mov dword ptr [rbp - 0x39], eax
008EEA78  8B F8                           mov edi, eax
008EEA7A  41 3B C2                        cmp eax, r10d
008EEA7D  0F 87 F5 04 00 00               ja 0x1408eef78
008EEA83  48 8D 05 56 EB 20 00            lea rax, [rip + 0x20eb56]
008EEA8A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008EEA8F  48 8D 05 BA EA 21 00            lea rax, [rip + 0x21eaba]
008EEA96  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
008EEA9B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008EEAA0  45 33 C9                        xor r9d, r9d
008EEAA3  48 8D 05 A6 F3 20 00            lea rax, [rip + 0x20f3a6]
008EEAAA  41 8B D2                        mov edx, r10d
008EEAAD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008EEAB2  45 33 C0                        xor r8d, r8d
008EEAB5  49 8B CD                        mov rcx, r13
008EEAB8  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
008EEAC0  E8 CB C8 B3 FF                  call 0x14042b390
008EEAC5  3D 23 00 00 C0                  cmp eax, 0xc0000023
008EEACA  0F 84 69 02 00 00               je 0x1408eed39
008EEAD0  44 8B F8                        mov r15d, eax
008EEAD3  85 C0                           test eax, eax
008EEAD5  0F 88 CB FD FF FF               js 0x1408ee8a6
008EEADB  8B 75 57                        mov esi, dword ptr [rbp + 0x57]
008EEADE  0F BA E6 08                     bt esi, 8
008EEAE2  0F 82 76 02 00 00               jb 0x1408eed5e
008EEAE8  49 8B D5                        mov rdx, r13
008EEAEB  48 8D 4D F7                     lea rcx, [rbp - 9]
008EEAEF  E8 6C 4E B7 FF                  call 0x140463960
008EEAF4  44 8B F8                        mov r15d, eax
008EEAF7  85 C0                           test eax, eax
008EEAF9  0F 88 A7 FD FF FF               js 0x1408ee8a6
008EEAFF  0F B7 7D F7                     movzx edi, word ptr [rbp - 9]
008EEB03  3B FB                           cmp edi, ebx
008EEB05  73 78                           jae 0x1408eeb7f
008EEB07  83 FF 32                        cmp edi, 0x32
008EEB0A  76 73                           jbe 0x1408eeb7f
008EEB0C  E8 DF F6 A0 FF                  call 0x1402fe1f0
008EEB11  4C 8B 05 F8 2E 71 FF            mov r8, qword ptr [rip - 0x8ed108]
008EEB18  48 8B B0 B0 04 00 00            mov rsi, qword ptr [rax + 0x4b0]
008EEB1F  83 FF 32                        cmp edi, 0x32
008EEB22  72 5B                           jb 0x1408eeb7f
008EEB24  4C 8B 5D FF                     mov r11, qword ptr [rbp - 1]
008EEB28  49 8D 58 32                     lea rbx, [r8 + 0x32]
008EEB2C  4D 2B D8                        sub r11, r8
008EEB2F  41 BF C0 00 00 00               mov r15d, 0xc0
008EEB35  4C 3B C3                        cmp r8, rbx
008EEB38  73 50                           jae 0x1408eeb8a
008EEB3A  45 0F B7 08                     movzx r9d, word ptr [r8]
008EEB3E  47 0F B7 14 03                  movzx r10d, word ptr [r11 + r8]
008EEB43  66 45 3B CA                     cmp r9w, r10w
008EEB47  75 06                           jne 0x1408eeb4f
008EEB49  49 83 C0 02                     add r8, 2
008EEB4D  EB E6                           jmp 0x1408eeb35
008EEB4F  41 83 F9 61                     cmp r9d, 0x61
008EEB53  72 0F                           jb 0x1408eeb64
008EEB55  41 83 F9 7A                     cmp r9d, 0x7a
008EEB59  0F 87 DE 00 00 00               ja 0x1408eec3d
008EEB5F  66 41 83 E9 20                  sub r9w, 0x20
008EEB64  41 83 FA 61                     cmp r10d, 0x61
008EEB68  72 0F                           jb 0x1408eeb79
008EEB6A  41 83 FA 7A                     cmp r10d, 0x7a
008EEB6E  0F 87 08 01 00 00               ja 0x1408eec7c
008EEB74  66 41 83 EA 20                  sub r10w, 0x20
008EEB79  66 45 3B CA                     cmp r9w, r10w
008EEB7D  74 CA                           je 0x1408eeb49
008EEB7F  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
008EEB85  E9 1C FD FF FF                  jmp 0x1408ee8a6
008EEB8A  B8 CE FF 00 00                  mov eax, 0xffce
008EEB8F  4D 8D 75 32                     lea r14, [r13 + 0x32]
008EEB93  66 01 45 F9                     add word ptr [rbp - 7], ax
008EEB97  66 03 F8                        add di, ax
008EEB9A  66 89 7D F7                     mov word ptr [rbp - 9], di
008EEB9E  4C 89 75 FF                     mov qword ptr [rbp - 1], r14
008EEBA2  E8 49 F6 A0 FF                  call 0x1402fe1f0
008EEBA7  4C 8B 05 72 2E 71 FF            mov r8, qword ptr [rip - 0x8ed18e]
008EEBAE  48 8B B0 B0 04 00 00            mov rsi, qword ptr [rax + 0x4b0]
008EEBB5  66 83 FF 0A                     cmp di, 0xa
008EEBB9  72 58                           jb 0x1408eec13
008EEBBB  4D 8B DE                        mov r11, r14
008EEBBE  49 8D 58 0A                     lea rbx, [r8 + 0xa]
008EEBC2  4D 2B D8                        sub r11, r8
008EEBC5  4C 3B C3                        cmp r8, rbx
008EEBC8  0F 83 53 FC FF FF               jae 0x1408ee821
008EEBCE  45 0F B7 08                     movzx r9d, word ptr [r8]
008EEBD2  47 0F B7 14 03                  movzx r10d, word ptr [r11 + r8]
008EEBD7  66 45 3B CA                     cmp r9w, r10w
008EEBDB  75 06                           jne 0x1408eebe3
008EEBDD  49 83 C0 02                     add r8, 2
008EEBE1  EB E2                           jmp 0x1408eebc5
008EEBE3  41 83 F9 61                     cmp r9d, 0x61
008EEBE7  72 0F                           jb 0x1408eebf8
008EEBE9  41 83 F9 7A                     cmp r9d, 0x7a
008EEBED  0F 87 C8 00 00 00               ja 0x1408eecbb
008EEBF3  66 41 83 E9 20                  sub r9w, 0x20
008EEBF8  41 83 FA 61                     cmp r10d, 0x61
008EEBFC  72 0F                           jb 0x1408eec0d
008EEBFE  41 83 FA 7A                     cmp r10d, 0x7a
008EEC02  0F 87 F2 00 00 00               ja 0x1408eecfa
008EEC08  66 41 83 EA 20                  sub r10w, 0x20
008EEC0D  66 45 3B CA                     cmp r9w, r10w
008EEC11  74 CA                           je 0x1408eebdd
008EEC13  41 B0 01                        mov r8b, 1
008EEC16  48 8D 55 F7                     lea rdx, [rbp - 9]
008EEC1A  48 8D 0D 57 2F 71 FF            lea rcx, [rip - 0x8ed0a9]
008EEC21  E8 4A 63 00 00                  call 0x1408f4f70
008EEC26  84 C0                           test al, al
008EEC28  0F 84 63 01 00 00               je 0x1408eed91
008EEC2E  41 B8 0E 00 00 00               mov r8d, 0xe
008EEC34  49 83 C6 24                     add r14, 0x24
008EEC38  E9 EE FB FF FF                  jmp 0x1408ee82b
008EEC3D  48 85 F6                        test rsi, rsi
008EEC40  0F 84 1E FF FF FF               je 0x1408eeb64
008EEC46  66 45 3B CF                     cmp r9w, r15w
008EEC4A  0F 82 14 FF FF FF               jb 0x1408eeb64
008EEC50  49 8B C1                        mov rax, r9
008EEC53  41 8B D1                        mov edx, r9d
008EEC56  48 C1 E8 08                     shr rax, 8
008EEC5A  83 E2 0F                        and edx, 0xf
008EEC5D  0F B7 0C 46                     movzx ecx, word ptr [rsi + rax*2]
008EEC61  41 8B C1                        mov eax, r9d
008EEC64  C1 E8 04                        shr eax, 4
008EEC67  83 E0 0F                        and eax, 0xf
008EEC6A  03 C8                           add ecx, eax
008EEC6C  0F B7 0C 4E                     movzx ecx, word ptr [rsi + rcx*2]
008EEC70  03 CA                           add ecx, edx
008EEC72  66 44 03 0C 4E                  add r9w, word ptr [rsi + rcx*2]
008EEC77  E9 E8 FE FF FF                  jmp 0x1408eeb64
008EEC7C  48 85 F6                        test rsi, rsi
008EEC7F  0F 84 F4 FE FF FF               je 0x1408eeb79
008EEC85  66 45 3B D7                     cmp r10w, r15w
008EEC89  0F 82 EA FE FF FF               jb 0x1408eeb79
008EEC8F  49 8B C2                        mov rax, r10
008EEC92  41 8B D2                        mov edx, r10d
008EEC95  48 C1 E8 08                     shr rax, 8
008EEC99  83 E2 0F                        and edx, 0xf
008EEC9C  0F B7 0C 46                     movzx ecx, word ptr [rsi + rax*2]
008EECA0  41 8B C2                        mov eax, r10d
008EECA3  C1 E8 04                        shr eax, 4
008EECA6  83 E0 0F                        and eax, 0xf
008EECA9  03 C8                           add ecx, eax
008EECAB  0F B7 0C 4E                     movzx ecx, word ptr [rsi + rcx*2]
008EECAF  03 CA                           add ecx, edx
008EECB1  66 44 03 14 4E                  add r10w, word ptr [rsi + rcx*2]
008EECB6  E9 BE FE FF FF                  jmp 0x1408eeb79
008EECBB  48 85 F6                        test rsi, rsi
008EECBE  0F 84 34 FF FF FF               je 0x1408eebf8
008EECC4  66 45 3B CF                     cmp r9w, r15w
008EECC8  0F 82 2A FF FF FF               jb 0x1408eebf8
008EECCE  49 8B C1                        mov rax, r9
008EECD1  41 8B D1                        mov edx, r9d
008EECD4  48 C1 E8 08                     shr rax, 8
008EECD8  83 E2 0F                        and edx, 0xf
008EECDB  0F B7 0C 46                     movzx ecx, word ptr [rsi + rax*2]
008EECDF  41 8B C1                        mov eax, r9d
008EECE2  C1 E8 04                        shr eax, 4
008EECE5  83 E0 0F                        and eax, 0xf
008EECE8  03 C8                           add ecx, eax
008EECEA  0F B7 0C 4E                     movzx ecx, word ptr [rsi + rcx*2]
008EECEE  03 CA                           add ecx, edx
008EECF0  66 44 03 0C 4E                  add r9w, word ptr [rsi + rcx*2]
008EECF5  E9 FE FE FF FF                  jmp 0x1408eebf8
008EECFA  48 85 F6                        test rsi, rsi
008EECFD  0F 84 0A FF FF FF               je 0x1408eec0d
008EED03  66 45 3B D7                     cmp r10w, r15w
008EED07  0F 82 00 FF FF FF               jb 0x1408eec0d
008EED0D  49 8B C2                        mov rax, r10
008EED10  41 8B D2                        mov edx, r10d
008EED13  48 C1 E8 08                     shr rax, 8
008EED17  83 E2 0F                        and edx, 0xf
008EED1A  0F B7 0C 46                     movzx ecx, word ptr [rsi + rax*2]
008EED1E  41 8B C2                        mov eax, r10d
008EED21  C1 E8 04                        shr eax, 4
008EED24  83 E0 0F                        and eax, 0xf
008EED27  03 C8                           add ecx, eax
008EED29  0F B7 0C 4E                     movzx ecx, word ptr [rsi + rcx*2]
008EED2D  03 CA                           add ecx, edx
008EED2F  66 44 03 14 4E                  add r10w, word ptr [rsi + rcx*2]
008EED34  E9 D4 FE FF FF                  jmp 0x1408eec0d
008EED39  33 D2                           xor edx, edx
008EED3B  49 8B CD                        mov rcx, r13
008EED3E  E8 2D 3B 29 00                  call 0x140b82870
008EED43  8B DF                           mov ebx, edi
008EED45  45 33 ED                        xor r13d, r13d
008EED48  48 03 DB                        add rbx, rbx
008EED4B  B8 FF FF FF FF                  mov eax, 0xffffffff
008EED50  48 3B D8                        cmp rbx, rax
008EED53  0F 86 1D FA FF FF               jbe 0x1408ee776
008EED59  E9 48 FB FF FF                  jmp 0x1408ee8a6
008EED5E  4D 8B F5                        mov r14, r13
008EED61  4D 85 E4                        test r12, r12
008EED64  0F 85 13 03 00 00               jne 0x1408ef07d
008EED6A  33 C9                           xor ecx, ecx
008EED6C  4C 8D 4D D7                     lea r9, [rbp - 0x29]
008EED70  33 D2                           xor edx, edx
008EED72  41 B8 00 00 00 02               mov r8d, 0x2000000
008EED78  E8 DF 57 00 00                  call 0x1408f455c
008EED7D  44 8B F8                        mov r15d, eax
008EED80  85 C0                           test eax, eax
008EED82  0F 88 1E FB FF FF               js 0x1408ee8a6
008EED88  48 8B 5D D7                     mov rbx, qword ptr [rbp - 0x29]
008EED8C  E9 C5 FA FF FF                  jmp 0x1408ee856
008EED91  41 B8 04 00 00 00               mov r8d, 4
008EED97  E9 8F FA FF FF                  jmp 0x1408ee82b
008EED9C  8B 4D 57                        mov ecx, dword ptr [rbp + 0x57]
008EED9F  0F B6 C1                        movzx eax, cl
008EEDA2  83 F8 10                        cmp eax, 0x10
008EEDA5  0F 85 7F 00 00 00               jne 0x1408eee2a
008EEDAB  85 F6                           test esi, esi
008EEDAD  0F 85 CF 01 00 00               jne 0x1408eef82
008EEDB3  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
008EEDBA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
008EEDC0  48 FF C0                        inc rax
008EEDC3  66 41 83 3C 43 00               cmp word ptr [r11 + rax*2], 0
008EEDC9  75 F5                           jne 0x1408eedc0
008EEDCB  48 83 C0 1F                     add rax, 0x1f
008EEDCF  B9 FF FF FF FF                  mov ecx, 0xffffffff
008EEDD4  48 3B C1                        cmp rax, rcx
008EEDD7  76 08                           jbe 0x1408eede1
008EEDD9  41 8B C7                        mov eax, r15d
008EEDDC  E9 E4 FC FF FF                  jmp 0x1408eeac5
008EEDE1  89 45 C7                        mov dword ptr [rbp - 0x39], eax
008EEDE4  8B F8                           mov edi, eax
008EEDE6  41 3B C2                        cmp eax, r10d
008EEDE9  0F 87 5A 01 00 00               ja 0x1408eef49
008EEDEF  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
008EEDF4  48 8D 05 55 E7 21 00            lea rax, [rip + 0x21e755]
008EEDFB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008EEE00  45 33 C9                        xor r9d, r9d
008EEE03  48 8D 05 26 E6 20 00            lea rax, [rip + 0x20e626]
008EEE0A  41 8B D2                        mov edx, r10d
008EEE0D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008EEE12  45 33 C0                        xor r8d, r8d
008EEE15  49 8B CD                        mov rcx, r13
008EEE18  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
008EEE20  E8 6B C5 B3 FF                  call 0x14042b390
008EEE25  E9 9B FC FF FF                  jmp 0x1408eeac5
008EEE2A  83 F8 12                        cmp eax, 0x12
008EEE2D  75 34                           jne 0x1408eee63
008EEE2F  48 8D 45 C7                     lea rax, [rbp - 0x39]
008EEE33  44 8B C1                        mov r8d, ecx
008EEE36  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008EEE3B  45 8B CE                        mov r9d, r14d
008EEE3E  0F B6 45 6F                     movzx eax, byte ptr [rbp + 0x6f]
008EEE42  49 8B D3                        mov rdx, r11
008EEE45  44 89 54 24 30                  mov dword ptr [rsp + 0x30], r10d
008EEE4A  49 8B CC                        mov rcx, r12
008EEE4D  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
008EEE52  88 44 24 20                     mov byte ptr [rsp + 0x20], al
008EEE56  E8 35 22 0A 00                  call 0x140991090
008EEE5B  8B 7D C7                        mov edi, dword ptr [rbp - 0x39]
008EEE5E  E9 62 FC FF FF                  jmp 0x1408eeac5
008EEE63  83 F8 11                        cmp eax, 0x11
008EEE66  0F 84 90 00 00 00               je 0x1408eeefc
008EEE6C  83 F8 13                        cmp eax, 0x13
008EEE6F  74 41                           je 0x1408eeeb2
008EEE71  83 F8 14                        cmp eax, 0x14
008EEE74  0F 85 D9 00 00 00               jne 0x1408eef53
008EEE7A  F7 C1 EB FF FF FF               test ecx, 0xffffffeb
008EEE80  0F 85 CD 00 00 00               jne 0x1408eef53
008EEE86  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
008EEE8D  0F 1F 00                        nop dword ptr [rax]
008EEE90  48 FF C0                        inc rax
008EEE93  66 41 83 3C 43 00               cmp word ptr [r11 + rax*2], 0
008EEE99  75 F5                           jne 0x1408eee90
008EEE9B  48 83 C0 27                     add rax, 0x27
008EEE9F  B9 FF FF FF FF                  mov ecx, 0xffffffff
008EEEA4  48 3B C1                        cmp rax, rcx
008EEEA7  0F 87 2C FF FF FF               ja 0x1408eedd9
008EEEAD  E9 C3 FB FF FF                  jmp 0x1408eea75
008EEEB2  F7 C1 EC FF FF FF               test ecx, 0xffffffec
008EEEB8  0F 85 95 00 00 00               jne 0x1408eef53
008EEEBE  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
008EEEC5  48 FF C0                        inc rax
008EEEC8  66 41 83 3C 43 00               cmp word ptr [r11 + rax*2], 0
008EEECE  75 F5                           jne 0x1408eeec5
008EEED0  48 83 C0 27                     add rax, 0x27
008EEED4  B9 FF FF FF FF                  mov ecx, 0xffffffff
008EEED9  48 3B C1                        cmp rax, rcx
008EEEDC  0F 87 F7 FE FF FF               ja 0x1408eedd9
008EEEE2  89 45 C7                        mov dword ptr [rbp - 0x39], eax
008EEEE5  8B F8                           mov edi, eax
008EEEE7  41 3B C2                        cmp eax, r10d
008EEEEA  0F 87 88 00 00 00               ja 0x1408eef78
008EEEF0  48 8D 05 79 E4 21 00            lea rax, [rip + 0x21e479]
008EEEF7  E9 8E FB FF FF                  jmp 0x1408eea8a
008EEEFC  85 F6                           test esi, esi
008EEEFE  0F 85 64 01 00 00               jne 0x1408ef068
008EEF04  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
008EEF0B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
008EEF10  48 FF C0                        inc rax
008EEF13  66 41 83 3C 43 00               cmp word ptr [r11 + rax*2], 0
008EEF19  75 F5                           jne 0x1408eef10
008EEF1B  0F BA E1 08                     bt ecx, 8
008EEF1F  B9 FF FF FF FF                  mov ecx, 0xffffffff
008EEF24  72 37                           jb 0x1408eef5d
008EEF26  48 83 C0 31                     add rax, 0x31
008EEF2A  48 3B C1                        cmp rax, rcx
008EEF2D  0F 87 A6 FE FF FF               ja 0x1408eedd9
008EEF33  89 45 C7                        mov dword ptr [rbp - 0x39], eax
008EEF36  8B F8                           mov edi, eax
008EEF38  41 3B C2                        cmp eax, r10d
008EEF3B  77 3B                           ja 0x1408eef78
008EEF3D  48 8D 05 FC E3 21 00            lea rax, [rip + 0x21e3fc]
008EEF44  E9 41 FB FF FF                  jmp 0x1408eea8a
008EEF49  B8 23 00 00 C0                  mov eax, 0xc0000023
008EEF4E  E9 72 FB FF FF                  jmp 0x1408eeac5
008EEF53  B8 0D 00 00 C0                  mov eax, 0xc000000d
008EEF58  E9 68 FB FF FF                  jmp 0x1408eeac5
008EEF5D  48 83 C0 1F                     add rax, 0x1f
008EEF61  48 3B C1                        cmp rax, rcx
008EEF64  0F 87 6F FE FF FF               ja 0x1408eedd9
008EEF6A  89 45 C7                        mov dword ptr [rbp - 0x39], eax
008EEF6D  8B F8                           mov edi, eax
008EEF6F  41 3B C2                        cmp eax, r10d
008EEF72  0F 86 77 FE FF FF               jbe 0x1408eedef
008EEF78  B8 23 00 00 C0                  mov eax, 0xc0000023
008EEF7D  E9 43 FB FF FF                  jmp 0x1408eeac5
008EEF82  45 85 F6                        test r14d, r14d
008EEF85  75 4D                           jne 0x1408eefd4
008EEF87  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
008EEF8E  66 90                           nop
008EEF90  48 FF C0                        inc rax
008EEF93  66 41 83 3C 43 00               cmp word ptr [r11 + rax*2], 0
008EEF99  75 F5                           jne 0x1408eef90
008EEF9B  48 83 C0 52                     add rax, 0x52
008EEF9F  B9 FF FF FF FF                  mov ecx, 0xffffffff
008EEFA4  48 3B C1                        cmp rax, rcx
008EEFA7  0F 87 2C FE FF FF               ja 0x1408eedd9
008EEFAD  89 45 C7                        mov dword ptr [rbp - 0x39], eax
008EEFB0  8B F8                           mov edi, eax
008EEFB2  41 3B C2                        cmp eax, r10d
008EEFB5  77 C1                           ja 0x1408eef78
008EEFB7  48 8D 05 92 E5 21 00            lea rax, [rip + 0x21e592]
008EEFBE  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
008EEFC3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008EEFC8  48 8D 05 C1 E5 21 00            lea rax, [rip + 0x21e5c1]
008EEFCF  E9 C7 FA FF FF                  jmp 0x1408eea9b
008EEFD4  B9 FF FF FF FF                  mov ecx, 0xffffffff
008EEFD9  44 3B F1                        cmp r14d, ecx
008EEFDC  0F 84 71 FF FF FF               je 0x1408eef53
008EEFE2  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
008EEFE9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
008EEFF0  48 FF C0                        inc rax
008EEFF3  66 41 83 3C 43 00               cmp word ptr [r11 + rax*2], 0
008EEFF9  75 F5                           jne 0x1408eeff0
008EEFFB  48 83 C0 4F                     add rax, 0x4f
008EEFFF  48 3B C1                        cmp rax, rcx
008EF002  0F 87 D1 FD FF FF               ja 0x1408eedd9
008EF008  89 45 C7                        mov dword ptr [rbp - 0x39], eax
008EF00B  8B F8                           mov edi, eax
008EF00D  41 3B C2                        cmp eax, r10d
008EF010  77 4C                           ja 0x1408ef05e
008EF012  4C 89 5C 24 48                  mov qword ptr [rsp + 0x48], r11
008EF017  48 8D 05 32 E5 21 00            lea rax, [rip + 0x21e532]
008EF01E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008EF023  45 33 C9                        xor r9d, r9d
008EF026  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
008EF02B  48 8D 05 EE E5 21 00            lea rax, [rip + 0x21e5ee]
008EF032  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008EF037  45 33 C0                        xor r8d, r8d
008EF03A  48 8D 05 BF E6 21 00            lea rax, [rip + 0x21e6bf]
008EF041  41 8B D2                        mov edx, r10d
008EF044  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008EF049  49 8B CD                        mov rcx, r13
008EF04C  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
008EF054  E8 37 C3 B3 FF                  call 0x14042b390
008EF059  E9 67 FA FF FF                  jmp 0x1408eeac5
008EF05E  B8 23 00 00 C0                  mov eax, 0xc0000023
008EF063  E9 5D FA FF FF                  jmp 0x1408eeac5
008EF068  45 85 F6                        test r14d, r14d
008EF06B  0F 85 E5 EA 22 00               jne 0x140b1db56
008EF071  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
008EF078  E9 C9 EA 22 00                  jmp 0x140b1db46
008EF07D  49 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [r12 + 0xe0]
008EF085  E9 E2 FC FF FF                  jmp 0x1408eed6c
008EF08A  44 8B F8                        mov r15d, eax
008EF08D  E9 14 F8 FF FF                  jmp 0x1408ee8a6
008EF092  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
008EF096  45 33 C9                        xor r9d, r9d
008EF099  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008EF09E  45 33 C0                        xor r8d, r8d
008EF0A1  49 8B CC                        mov rcx, r12
008EF0A4  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EF0A8  E8 0B 07 00 00                  call 0x1408ef7b8
008EF0AD  3D 7C 01 00 C0                  cmp eax, 0xc000017c
008EF0B2  0F 84 8F F8 FF FF               je 0x1408ee947
008EF0B8  85 C0                           test eax, eax
008EF0BA  0F 89 E6 F7 FF FF               jns 0x1408ee8a6
008EF0C0  44 8B F8                        mov r15d, eax
008EF0C3  E9 DE F7 FF FF                  jmp 0x1408ee8a6
008EF0C8  41 BF 17 00 00 C0               mov r15d, 0xc0000017
008EF0CE  E9 D3 F7 FF FF                  jmp 0x1408ee8a6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008EE966(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
}
```

## 5. (Beta) C Style

```c
int64_t sub_008EE966(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint32_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008EE966&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
