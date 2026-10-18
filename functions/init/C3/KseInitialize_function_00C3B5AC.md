# KseInitialize

- RVA: `0x00C3B5AC`–`0x00C3BB59` (길이 `1,453` bytes)
- VA: `0x0000000140C3B5AC`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB428`
- 디코드: `324`개 명령, `1,453/1,453` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **34**

### Outgoing calls
- `0x00C3B617` → [KseShimDatabaseBootInitialize](KseShimDatabaseBootInitialize_function_00C3C124.md) (function, `0x00C3C124`)
- `0x00C3B64B` → [KsepEngineInitialize](KsepEngineInitialize_function_00C3B4A0.md) (function, `0x00C3B4A0`)
- `0x00C3B65D` → [KsepMatchInitMachineInfo](KsepMatchInitMachineInfo_function_00C3BFBC.md) (function, `0x00C3BFBC`)
- `0x00C3B682` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (function, `0x007494B0`)
- `0x00C3B6CB` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x00C3B6D9` → [KsepLogInfo](../../text/49/KsepLogInfo_function_00499A68.md) (function, `0x00499A68`)
- `0x00C3B736` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x00C3B740` → [KseShimDatabaseOpen](../../page/95/KseShimDatabaseOpen_function_0095AD7C.md) (function, `0x0095AD7C`)
- `0x00C3B75D` → [KseShimDatabaseClose](../../page/95/KseShimDatabaseClose_function_0095ABCC.md) (function, `0x0095ABCC`)
- `0x00C3B762` → [KseVersionLieInitialize](KseVersionLieInitialize_function_00C3C64C.md) (function, `0x00C3C64C`)
- `0x00C3B773` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (function, `0x007494B0`)
- `0x00C3B7B7` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x00C3B7C5` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (function, `0x00499A98`)
- `0x00C3B7D6` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (function, `0x007494B0`)
- `0x00C3B815` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x00C3B823` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (function, `0x00499A98`)
- `0x00C3B834` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (function, `0x007494B0`)
- `0x00C3B873` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x00C3B881` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (function, `0x00499A98`)
- `0x00C3B892` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (function, `0x007494B0`)
- `0x00C3B8D1` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x00C3B8DF` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (function, `0x00499A98`)
- `0x00C3B8F0` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (function, `0x007494B0`)
- `0x00C3B92F` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x00C3B93D` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (function, `0x00499A98`)
- `0x00C3B94E` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (function, `0x007494B0`)
- `0x00C3B98D` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x00C3B99B` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (function, `0x00499A98`)
- `0x00C3B9AC` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (function, `0x007494B0`)
- `0x00C3B9EB` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x00C3B9F9` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (function, `0x00499A98`)
- `0x00C3BA47` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x00C3BA58` → [KsepLogInfo](../../text/49/KsepLogInfo_function_00499A68.md) (function, `0x00499A68`)
- `0x00C3BA8A` → [KsepCacheUninitialize](../../page/74/KsepCacheUninitialize_function_0074AFB0.md) (function, `0x0074AFB0`)
- `0x00C3BAE8` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x00C3BAF6` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (function, `0x00499A98`)
- `0x00C3BB27` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x00C3BB38` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (function, `0x00499A98`)

### Direct callers
- [IoInitSystemPreDrivers](../C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B4CA`
- [IoInitSystemPreDrivers](../C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B8FC`

### Static image references
- `0x00C3B5C6` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00C3B5DF` → RVA `0x00E66C84` (`.data`; read)
- `0x00C3B644` → RVA `0x00E66C80` (`.data`; read)
- `0x00C3B66F` → RVA `0x00E66C84` (`.data`; write)
- `0x00C3B67B` → RVA `0x00E01650` (`.data`; read)
- `0x00C3B691` → RVA `0x00F105E0` (`.data`; read/write)
- `0x00C3B6B8` → RVA `0x00E66CE8` (`.data`; read)
- `0x00C3B6C2` → RVA `0x00C7BBA0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C3B6E3` → RVA `0x00F04984` (`.data`; read)
- `0x00C3B6EB` → RVA `0x00E66C88` (`.data`; read/write)
- `0x00C3B723` → RVA `0x00E66CE0` (`.data`; read)
- `0x00C3B72D` → RVA `0x00021D28` (`.rdata`; read)
- `0x00C3B76A` → RVA `0x00E01908` (`.data`; read)
- `0x00C3B783` → RVA `0x00F101C0` (`.data`; read/write)
- `0x00C3B7AE` → RVA `0x00C7BCA0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C3B7CD` → RVA `0x00E07140` (`.data`; read)
- `0x00C3B80C` → RVA `0x00C7BAB0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C3B82B` → RVA `0x00E07328` (`.data`; read)
- `0x00C3B86A` → RVA `0x00C7BBD0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C3B889` → RVA `0x00E073F8` (`.data`; read)
- `0x00C3B8C8` → RVA `0x00C7BC30` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C3B8E7` → RVA `0x00E073C0` (`.data`; read)
- `0x00C3B926` → RVA `0x00C7BC00` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C3B945` → RVA `0x00E018D0` (`.data`; read)
- `0x00C3B984` → RVA `0x00C7BC60` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C3B9A3` → RVA `0x00E01980` (`.data`; read)
- `0x00C3B9E2` → RVA `0x00C7BCE0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C3BA3E` → RVA `0x00C7B5B0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C3BA5D` → RVA `0x00FC4148` (`.data`; read)
- `0x00C3BA66` → RVA `0x00E66C80` (`.data`; read/write)
- `0x00C3BA74` → RVA `0x00E66CC8` (`.data`; read)
- `0x00C3BA8F` → RVA `0x00E66CC8` (`.data`; read/write)
- `0x00C3BADF` → RVA `0x00C7B510` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C3BB1E` → RVA `0x00C7B580` (` ?? ::PBOPGDP::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **34**
  - `0x00C3B682` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (`INIT` → `PAGE`)
  - `0x00C3B6CB` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`INIT` → `.text`)
  - `0x00C3B6D9` → [KsepLogInfo](../../text/49/KsepLogInfo_function_00499A68.md) (`INIT` → `.text`)
  - `0x00C3B736` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`INIT` → `PAGE`)
  - `0x00C3B740` → [KseShimDatabaseOpen](../../page/95/KseShimDatabaseOpen_function_0095AD7C.md) (`INIT` → `PAGE`)
  - `0x00C3B75D` → [KseShimDatabaseClose](../../page/95/KseShimDatabaseClose_function_0095ABCC.md) (`INIT` → `PAGE`)
  - `0x00C3B773` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (`INIT` → `PAGE`)
  - `0x00C3B7B7` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`INIT` → `.text`)
  - `0x00C3B7C5` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (`INIT` → `.text`)
  - `0x00C3B7D6` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (`INIT` → `PAGE`)
  - `0x00C3B815` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`INIT` → `.text`)
  - `0x00C3B823` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (`INIT` → `.text`)
  - `0x00C3B834` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (`INIT` → `PAGE`)
  - `0x00C3B873` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`INIT` → `.text`)
  - `0x00C3B881` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (`INIT` → `.text`)
  - `0x00C3B892` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (`INIT` → `PAGE`)
  - `0x00C3B8D1` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`INIT` → `.text`)
  - `0x00C3B8DF` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (`INIT` → `.text`)
  - `0x00C3B8F0` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (`INIT` → `PAGE`)
  - `0x00C3B92F` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`INIT` → `.text`)
  - `0x00C3B93D` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (`INIT` → `.text`)
  - `0x00C3B94E` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (`INIT` → `PAGE`)
  - `0x00C3B98D` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`INIT` → `.text`)
  - `0x00C3B99B` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (`INIT` → `.text`)
  - `0x00C3B9AC` → [KseRegisterShim](../../page/74/KseRegisterShim_function_007494B0.md) (`INIT` → `PAGE`)
  - `0x00C3B9EB` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`INIT` → `.text`)
  - `0x00C3B9F9` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (`INIT` → `.text`)
  - `0x00C3BA47` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`INIT` → `.text`)
  - `0x00C3BA58` → [KsepLogInfo](../../text/49/KsepLogInfo_function_00499A68.md) (`INIT` → `.text`)
  - `0x00C3BA8A` → [KsepCacheUninitialize](../../page/74/KsepCacheUninitialize_function_0074AFB0.md) (`INIT` → `PAGE`)
  - `0x00C3BAE8` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`INIT` → `.text`)
  - `0x00C3BAF6` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (`INIT` → `.text`)
  - `0x00C3BB27` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`INIT` → `.text`)
  - `0x00C3BB38` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C3B5AC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C3B5B1  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00C3B5B6  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00C3B5BB  57                              push rdi
00C3B5BC  41 55                           push r13
00C3B5BE  41 57                           push r15
00C3B5C0  48 83 EC 20                     sub rsp, 0x20
00C3B5C4  33 FF                           xor edi, edi
00C3B5C6  4C 8D 3D 33 4A 3C FF            lea r15, [rip - 0xc3b5cd]
00C3B5CD  8B EA                           mov ebp, edx
00C3B5CF  48 8B F1                        mov rsi, rcx
00C3B5D2  8D 5F 01                        lea ebx, [rdi + 1]
00C3B5D5  85 D2                           test edx, edx
00C3B5D7  0F 85 39 01 00 00               jne 0x140c3b716
00C3B5DD  33 C0                           xor eax, eax
00C3B5DF  F0 0F B1 1D 9D B6 22 00         lock cmpxchg dword ptr [rip + 0x22b69d], ebx
00C3B5E7  83 F8 02                        cmp eax, 2
00C3B5EA  75 07                           jne 0x140c3b5f3
00C3B5EC  33 C0                           xor eax, eax
00C3B5EE  E9 4C 05 00 00                  jmp 0x140c3bb3f
00C3B5F3  3B C3                           cmp eax, ebx
00C3B5F5  75 0A                           jne 0x140c3b601
00C3B5F7  B8 03 01 00 00                  mov eax, 0x103
00C3B5FC  E9 3E 05 00 00                  jmp 0x140c3bb3f
00C3B601  48 8B 89 F0 00 00 00            mov rcx, qword ptr [rcx + 0xf0]
00C3B608  44 8B 49 58                     mov r9d, dword ptr [rcx + 0x58]
00C3B60C  4C 8B 41 50                     mov r8, qword ptr [rcx + 0x50]
00C3B610  8B 51 48                        mov edx, dword ptr [rcx + 0x48]
00C3B613  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00C3B617  E8 08 0B 00 00                  call 0x140c3c124
00C3B61C  85 C0                           test eax, eax
00C3B61E  79 0A                           jns 0x140c3b62a
00C3B620  B8 01 00 00 C0                  mov eax, 0xc0000001
00C3B625  E9 15 05 00 00                  jmp 0x140c3bb3f
00C3B62A  48 8B 86 F0 00 00 00            mov rax, qword ptr [rsi + 0xf0]
00C3B631  48 39 78 40                     cmp qword ptr [rax + 0x40], rdi
00C3B635  0F 84 A8 00 00 00               je 0x140c3b6e3
00C3B63B  39 78 48                        cmp dword ptr [rax + 0x48], edi
00C3B63E  0F 84 9F 00 00 00               je 0x140c3b6e3
00C3B644  48 8D 0D 35 B6 22 00            lea rcx, [rip + 0x22b635]
00C3B64B  E8 50 FE FF FF                  call 0x140c3b4a0
00C3B650  8B F8                           mov edi, eax
00C3B652  85 C0                           test eax, eax
00C3B654  0F 88 1A 04 00 00               js 0x140c3ba74
00C3B65A  48 8B CE                        mov rcx, rsi
00C3B65D  E8 5A 09 00 00                  call 0x140c3bfbc
00C3B662  8B F8                           mov edi, eax
00C3B664  85 C0                           test eax, eax
00C3B666  0F 88 08 04 00 00               js 0x140c3ba74
00C3B66C  45 33 C0                        xor r8d, r8d
00C3B66F  C7 05 0B B6 22 00 02 00 00 00   mov dword ptr [rip + 0x22b60b], 2
00C3B679  33 D2                           xor edx, edx
00C3B67B  48 8D 0D CE 5F 1C 00            lea rcx, [rip + 0x1c5fce]
00C3B682  E8 29 DE B0 FF                  call 0x1407494b0
00C3B687  85 C0                           test eax, eax
00C3B689  0F 88 7E 03 00 00               js 0x140c3ba0d
00C3B68F  8B C3                           mov eax, ebx
00C3B691  F0 0F C1 05 47 4F 2D 00         lock xadd dword ptr [rip + 0x2d4f47], eax
00C3B699  03 C3                           add eax, ebx
00C3B69B  BE 0B 00 00 00                  mov esi, 0xb
00C3B6A0  83 E0 3F                        and eax, 0x3f
00C3B6A3  41 83 A4 C7 E4 03 F1 00 00      and dword ptr [r15 + rax*8 + 0xf103e4], 0
00C3B6AC  41 C7 84 C7 E0 03 F1 00 90 00 0B 00  mov dword ptr [r15 + rax*8 + 0xf103e0], 0xb0090
00C3B6B8  8B 05 2A B6 22 00               mov eax, dword ptr [rip + 0x22b62a]
00C3B6BE  84 C3                           test bl, al
00C3B6C0  74 0E                           je 0x140c3b6d0
00C3B6C2  48 8D 15 D7 04 04 00            lea rdx, [rip + 0x404d7]
00C3B6C9  8B CE                           mov ecx, esi
00C3B6CB  E8 20 19 8A FF                  call 0x1404dcff0
00C3B6D0  48 8D 15 C9 04 04 00            lea rdx, [rip + 0x404c9]
00C3B6D7  8B CE                           mov ecx, esi
00C3B6D9  E8 8A E3 85 FF                  call 0x140499a68
00C3B6DE  E9 2A 03 00 00                  jmp 0x140c3ba0d
00C3B6E3  39 3D 9B 92 2C 00               cmp dword ptr [rip + 0x2c929b], edi
00C3B6E9  74 07                           je 0x140c3b6f2
00C3B6EB  83 0D 96 B5 22 00 40            or dword ptr [rip + 0x22b596], 0x40
00C3B6F2  48 8B 86 F0 00 00 00            mov rax, qword ptr [rsi + 0xf0]
00C3B6F9  48 39 78 40                     cmp qword ptr [rax + 0x40], rdi
00C3B6FD  74 05                           je 0x140c3b704
00C3B6FF  39 78 48                        cmp dword ptr [rax + 0x48], edi
00C3B702  75 08                           jne 0x140c3b70c
00C3B704  0F BA 2D 7C B5 22 00 07         bts dword ptr [rip + 0x22b57c], 7
00C3B70C  BF BB 00 00 C0                  mov edi, 0xc00000bb
00C3B711  E9 5E 03 00 00                  jmp 0x140c3ba74
00C3B716  3B EB                           cmp ebp, ebx
00C3B718  0F 85 EF 02 00 00               jne 0x140c3ba0d
00C3B71E  48 21 7C 24 50                  and qword ptr [rsp + 0x50], rdi
00C3B723  4C 8D 0D B6 B5 22 00            lea r9, [rip + 0x22b5b6]
00C3B72A  45 33 C0                        xor r8d, r8d
00C3B72D  48 8D 0D F4 65 3E FF            lea rcx, [rip - 0xc19a0c]
00C3B734  33 D2                           xor edx, edx
00C3B736  E8 25 52 CE FF                  call 0x140920960
00C3B73B  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00C3B740  E8 37 F6 D1 FF                  call 0x14095ad7c
00C3B745  8B F8                           mov edi, eax
00C3B747  85 C0                           test eax, eax
00C3B749  0F 88 B1 02 00 00               js 0x140c3ba00
00C3B74F  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00C3B754  48 85 C9                        test rcx, rcx
00C3B757  0F 84 A3 02 00 00               je 0x140c3ba00
00C3B75D  E8 6A F4 D1 FF                  call 0x14095abcc
00C3B762  E8 E5 0E 00 00                  call 0x140c3c64c
00C3B767  45 33 C0                        xor r8d, r8d
00C3B76A  48 8D 0D 97 61 1C 00            lea rcx, [rip + 0x1c6197]
00C3B771  33 D2                           xor edx, edx
00C3B773  E8 38 DD B0 FF                  call 0x1407494b0
00C3B778  BE 0C 00 00 00                  mov esi, 0xc
00C3B77D  85 C0                           test eax, eax
00C3B77F  79 49                           jns 0x140c3b7ca
00C3B781  8B CB                           mov ecx, ebx
00C3B783  F0 0F C1 0D 35 4A 2D 00         lock xadd dword ptr [rip + 0x2d4a35], ecx
00C3B78B  03 CB                           add ecx, ebx
00C3B78D  83 E1 3F                        and ecx, 0x3f
00C3B790  41 89 84 CF E4 01 F1 00         mov dword ptr [r15 + rcx*8 + 0xf101e4], eax
00C3B798  8B 05 4A B5 22 00               mov eax, dword ptr [rip + 0x22b54a]
00C3B79E  41 C7 84 CF E0 01 F1 00 93 00 0D 00  mov dword ptr [r15 + rcx*8 + 0xf101e0], 0xd0093
00C3B7AA  A8 02                           test al, 2
00C3B7AC  74 0E                           je 0x140c3b7bc
00C3B7AE  48 8D 15 EB 04 04 00            lea rdx, [rip + 0x404eb]
00C3B7B5  8B CE                           mov ecx, esi
00C3B7B7  E8 34 18 8A FF                  call 0x1404dcff0
00C3B7BC  48 8D 15 DD 04 04 00            lea rdx, [rip + 0x404dd]
00C3B7C3  8B CE                           mov ecx, esi
00C3B7C5  E8 CE E2 85 FF                  call 0x140499a98
00C3B7CA  45 33 C0                        xor r8d, r8d
00C3B7CD  48 8D 0D 6C B9 1C 00            lea rcx, [rip + 0x1cb96c]
00C3B7D4  33 D2                           xor edx, edx
00C3B7D6  E8 D5 DC B0 FF                  call 0x1407494b0
00C3B7DB  85 C0                           test eax, eax
00C3B7DD  79 49                           jns 0x140c3b828
00C3B7DF  8B CB                           mov ecx, ebx
00C3B7E1  F0 0F C1 0D D7 49 2D 00         lock xadd dword ptr [rip + 0x2d49d7], ecx
00C3B7E9  03 CB                           add ecx, ebx
00C3B7EB  83 E1 3F                        and ecx, 0x3f
00C3B7EE  41 89 84 CF E4 01 F1 00         mov dword ptr [r15 + rcx*8 + 0xf101e4], eax
00C3B7F6  8B 05 EC B4 22 00               mov eax, dword ptr [rip + 0x22b4ec]
00C3B7FC  41 C7 84 CF E0 01 F1 00 74 00 10 00  mov dword ptr [r15 + rcx*8 + 0xf101e0], 0x100074
00C3B808  A8 02                           test al, 2
00C3B80A  74 0E                           je 0x140c3b81a
00C3B80C  48 8D 15 9D 02 04 00            lea rdx, [rip + 0x4029d]
00C3B813  8B CE                           mov ecx, esi
00C3B815  E8 D6 17 8A FF                  call 0x1404dcff0
00C3B81A  48 8D 15 8F 02 04 00            lea rdx, [rip + 0x4028f]
00C3B821  8B CE                           mov ecx, esi
00C3B823  E8 70 E2 85 FF                  call 0x140499a98
00C3B828  45 33 C0                        xor r8d, r8d
00C3B82B  48 8D 0D F6 BA 1C 00            lea rcx, [rip + 0x1cbaf6]
00C3B832  33 D2                           xor edx, edx
00C3B834  E8 77 DC B0 FF                  call 0x1407494b0
00C3B839  85 C0                           test eax, eax
00C3B83B  79 49                           jns 0x140c3b886
00C3B83D  8B CB                           mov ecx, ebx
00C3B83F  F0 0F C1 0D 79 49 2D 00         lock xadd dword ptr [rip + 0x2d4979], ecx
00C3B847  03 CB                           add ecx, ebx
00C3B849  83 E1 3F                        and ecx, 0x3f
00C3B84C  41 89 84 CF E4 01 F1 00         mov dword ptr [r15 + rcx*8 + 0xf101e4], eax
00C3B854  8B 05 8E B4 22 00               mov eax, dword ptr [rip + 0x22b48e]
00C3B85A  41 C7 84 CF E0 01 F1 00 7D 00 0E 00  mov dword ptr [r15 + rcx*8 + 0xf101e0], 0xe007d
00C3B866  A8 02                           test al, 2
00C3B868  74 0E                           je 0x140c3b878
00C3B86A  48 8D 15 5F 03 04 00            lea rdx, [rip + 0x4035f]
00C3B871  8B CE                           mov ecx, esi
00C3B873  E8 78 17 8A FF                  call 0x1404dcff0
00C3B878  48 8D 15 51 03 04 00            lea rdx, [rip + 0x40351]
00C3B87F  8B CE                           mov ecx, esi
00C3B881  E8 12 E2 85 FF                  call 0x140499a98
00C3B886  45 33 C0                        xor r8d, r8d
00C3B889  48 8D 0D 68 BB 1C 00            lea rcx, [rip + 0x1cbb68]
00C3B890  33 D2                           xor edx, edx
00C3B892  E8 19 DC B0 FF                  call 0x1407494b0
00C3B897  85 C0                           test eax, eax
00C3B899  79 49                           jns 0x140c3b8e4
00C3B89B  8B CB                           mov ecx, ebx
00C3B89D  F0 0F C1 0D 1B 49 2D 00         lock xadd dword ptr [rip + 0x2d491b], ecx
00C3B8A5  03 CB                           add ecx, ebx
00C3B8A7  83 E1 3F                        and ecx, 0x3f
00C3B8AA  41 89 84 CF E4 01 F1 00         mov dword ptr [r15 + rcx*8 + 0xf101e4], eax
00C3B8B2  8B 05 30 B4 22 00               mov eax, dword ptr [rip + 0x22b430]
00C3B8B8  41 C7 84 CF E0 01 F1 00 7D 00 0F 00  mov dword ptr [r15 + rcx*8 + 0xf101e0], 0xf007d
00C3B8C4  A8 02                           test al, 2
00C3B8C6  74 0E                           je 0x140c3b8d6
00C3B8C8  48 8D 15 61 03 04 00            lea rdx, [rip + 0x40361]
00C3B8CF  8B CE                           mov ecx, esi
00C3B8D1  E8 1A 17 8A FF                  call 0x1404dcff0
00C3B8D6  48 8D 15 53 03 04 00            lea rdx, [rip + 0x40353]
00C3B8DD  8B CE                           mov ecx, esi
00C3B8DF  E8 B4 E1 85 FF                  call 0x140499a98
00C3B8E4  45 33 C0                        xor r8d, r8d
00C3B8E7  48 8D 0D D2 BA 1C 00            lea rcx, [rip + 0x1cbad2]
00C3B8EE  33 D2                           xor edx, edx
00C3B8F0  E8 BB DB B0 FF                  call 0x1407494b0
00C3B8F5  85 C0                           test eax, eax
00C3B8F7  79 49                           jns 0x140c3b942
00C3B8F9  8B CB                           mov ecx, ebx
00C3B8FB  F0 0F C1 0D BD 48 2D 00         lock xadd dword ptr [rip + 0x2d48bd], ecx
00C3B903  03 CB                           add ecx, ebx
00C3B905  83 E1 3F                        and ecx, 0x3f
00C3B908  41 89 84 CF E4 01 F1 00         mov dword ptr [r15 + rcx*8 + 0xf101e4], eax
00C3B910  8B 05 D2 B3 22 00               mov eax, dword ptr [rip + 0x22b3d2]
00C3B916  41 C7 84 CF E0 01 F1 00 60 00 11 00  mov dword ptr [r15 + rcx*8 + 0xf101e0], 0x110060
00C3B922  A8 02                           test al, 2
00C3B924  74 0E                           je 0x140c3b934
00C3B926  48 8D 15 D3 02 04 00            lea rdx, [rip + 0x402d3]
00C3B92D  8B CE                           mov ecx, esi
00C3B92F  E8 BC 16 8A FF                  call 0x1404dcff0
00C3B934  48 8D 15 C5 02 04 00            lea rdx, [rip + 0x402c5]
00C3B93B  8B CE                           mov ecx, esi
00C3B93D  E8 56 E1 85 FF                  call 0x140499a98
00C3B942  45 33 C0                        xor r8d, r8d
00C3B945  48 8D 0D 84 5F 1C 00            lea rcx, [rip + 0x1c5f84]
00C3B94C  33 D2                           xor edx, edx
00C3B94E  E8 5D DB B0 FF                  call 0x1407494b0
00C3B953  85 C0                           test eax, eax
00C3B955  79 49                           jns 0x140c3b9a0
00C3B957  8B CB                           mov ecx, ebx
00C3B959  F0 0F C1 0D 5F 48 2D 00         lock xadd dword ptr [rip + 0x2d485f], ecx
00C3B961  03 CB                           add ecx, ebx
00C3B963  83 E1 3F                        and ecx, 0x3f
00C3B966  41 89 84 CF E4 01 F1 00         mov dword ptr [r15 + rcx*8 + 0xf101e4], eax
00C3B96E  8B 05 74 B3 22 00               mov eax, dword ptr [rip + 0x22b374]
00C3B974  41 C7 84 CF E0 01 F1 00 69 00 12 00  mov dword ptr [r15 + rcx*8 + 0xf101e0], 0x120069
00C3B980  A8 02                           test al, 2
00C3B982  74 0E                           je 0x140c3b992
00C3B984  48 8D 15 D5 02 04 00            lea rdx, [rip + 0x402d5]
00C3B98B  8B CE                           mov ecx, esi
00C3B98D  E8 5E 16 8A FF                  call 0x1404dcff0
00C3B992  48 8D 15 C7 02 04 00            lea rdx, [rip + 0x402c7]
00C3B999  8B CE                           mov ecx, esi
00C3B99B  E8 F8 E0 85 FF                  call 0x140499a98
00C3B9A0  45 33 C0                        xor r8d, r8d
00C3B9A3  48 8D 0D D6 5F 1C 00            lea rcx, [rip + 0x1c5fd6]
00C3B9AA  33 D2                           xor edx, edx
00C3B9AC  E8 FF DA B0 FF                  call 0x1407494b0
00C3B9B1  85 C0                           test eax, eax
00C3B9B3  79 58                           jns 0x140c3ba0d
00C3B9B5  8B D3                           mov edx, ebx
00C3B9B7  F0 0F C1 15 01 48 2D 00         lock xadd dword ptr [rip + 0x2d4801], edx
00C3B9BF  03 D3                           add edx, ebx
00C3B9C1  83 E2 3F                        and edx, 0x3f
00C3B9C4  41 89 84 D7 E4 01 F1 00         mov dword ptr [r15 + rdx*8 + 0xf101e4], eax
00C3B9CC  8B 05 16 B3 22 00               mov eax, dword ptr [rip + 0x22b316]
00C3B9D2  41 C7 84 D7 E0 01 F1 00 5B 00 13 00  mov dword ptr [r15 + rdx*8 + 0xf101e0], 0x13005b
00C3B9DE  A8 02                           test al, 2
00C3B9E0  74 0E                           je 0x140c3b9f0
00C3B9E2  48 8D 15 F7 02 04 00            lea rdx, [rip + 0x402f7]
00C3B9E9  8B CE                           mov ecx, esi
00C3B9EB  E8 00 16 8A FF                  call 0x1404dcff0
00C3B9F0  48 8D 15 E9 02 04 00            lea rdx, [rip + 0x402e9]
00C3B9F7  8B CE                           mov ecx, esi
00C3B9F9  E8 9A E0 85 FF                  call 0x140499a98
00C3B9FE  EB 0D                           jmp 0x140c3ba0d
00C3BA00  0F BA 2D 80 B2 22 00 07         bts dword ptr [rip + 0x22b280], 7
00C3BA08  BF BB 00 00 C0                  mov edi, 0xc00000bb
00C3BA0D  8B C3                           mov eax, ebx
00C3BA0F  F0 0F C1 05 C9 4B 2D 00         lock xadd dword ptr [rip + 0x2d4bc9], eax
00C3BA17  03 C3                           add eax, ebx
00C3BA19  83 E0 3F                        and eax, 0x3f
00C3BA1C  41 83 A4 C7 E4 03 F1 00 00      and dword ptr [r15 + rax*8 + 0xf103e4], 0
00C3BA25  41 C7 84 C7 E0 03 F1 00 FE 00 05 00  mov dword ptr [r15 + rax*8 + 0xf103e0], 0x500fe
00C3BA31  8B 05 B1 B2 22 00               mov eax, dword ptr [rip + 0x22b2b1]
00C3BA37  84 C3                           test bl, al
00C3BA39  74 11                           je 0x140c3ba4c
00C3BA3B  44 8B C5                        mov r8d, ebp
00C3BA3E  48 8D 15 6B FB 03 00            lea rdx, [rip + 0x3fb6b]
00C3BA45  8B CB                           mov ecx, ebx
00C3BA47  E8 A4 15 8A FF                  call 0x1404dcff0
00C3BA4C  44 8B C5                        mov r8d, ebp
00C3BA4F  48 8D 15 5A FB 03 00            lea rdx, [rip + 0x3fb5a]
00C3BA56  8B CB                           mov ecx, ebx
00C3BA58  E8 0B E0 85 FF                  call 0x140499a68
00C3BA5D  80 3D E4 86 38 00 00            cmp byte ptr [rip + 0x3886e4], 0
00C3BA64  74 06                           je 0x140c3ba6c
00C3BA66  09 1D 14 B2 22 00               or dword ptr [rip + 0x22b214], ebx
00C3BA6C  85 FF                           test edi, edi
00C3BA6E  0F 89 C9 00 00 00               jns 0x140c3bb3d
00C3BA74  48 8B 0D 4D B2 22 00            mov rcx, qword ptr [rip + 0x22b24d]
00C3BA7B  C7 05 FF B1 22 00 00 00 00 00   mov dword ptr [rip + 0x22b1ff], 0
00C3BA85  48 85 C9                        test rcx, rcx
00C3BA88  74 0D                           je 0x140c3ba97
00C3BA8A  E8 21 F5 B0 FF                  call 0x14074afb0
00C3BA8F  48 83 25 31 B2 22 00 00         and qword ptr [rip + 0x22b231], 0
00C3BA97  83 0D E2 B1 22 00 03            or dword ptr [rip + 0x22b1e2], 3
00C3BA9E  8B C3                           mov eax, ebx
00C3BAA0  0F BA 2D E0 B1 22 00 0A         bts dword ptr [rip + 0x22b1e0], 0xa
00C3BAA8  F0 0F C1 05 10 47 2D 00         lock xadd dword ptr [rip + 0x2d4710], eax
00C3BAB0  03 C3                           add eax, ebx
00C3BAB2  83 E0 3F                        and eax, 0x3f
00C3BAB5  81 FF BB 00 00 C0               cmp edi, 0xc00000bb
00C3BABB  75 40                           jne 0x140c3bafd
00C3BABD  41 C7 84 C7 E4 01 F1 00 BB 00 00 C0  mov dword ptr [r15 + rax*8 + 0xf101e4], 0xc00000bb
00C3BAC9  41 C7 84 C7 E0 01 F1 00 1A 01 05 00  mov dword ptr [r15 + rax*8 + 0xf101e0], 0x5011a
00C3BAD5  8B 05 0D B2 22 00               mov eax, dword ptr [rip + 0x22b20d]
00C3BADB  A8 02                           test al, 2
00C3BADD  74 0E                           je 0x140c3baed
00C3BADF  48 8D 15 2A FA 03 00            lea rdx, [rip + 0x3fa2a]
00C3BAE6  8B CB                           mov ecx, ebx
00C3BAE8  E8 03 15 8A FF                  call 0x1404dcff0
00C3BAED  48 8D 15 1C FA 03 00            lea rdx, [rip + 0x3fa1c]
00C3BAF4  8B CB                           mov ecx, ebx
00C3BAF6  E8 9D DF 85 FF                  call 0x140499a98
00C3BAFB  EB 40                           jmp 0x140c3bb3d
00C3BAFD  41 89 BC C7 E4 01 F1 00         mov dword ptr [r15 + rax*8 + 0xf101e4], edi
00C3BB05  41 C7 84 C7 E0 01 F1 00 1E 01 05 00  mov dword ptr [r15 + rax*8 + 0xf101e0], 0x5011e
00C3BB11  8B 05 D1 B1 22 00               mov eax, dword ptr [rip + 0x22b1d1]
00C3BB17  A8 02                           test al, 2
00C3BB19  74 11                           je 0x140c3bb2c
00C3BB1B  44 8B C7                        mov r8d, edi
00C3BB1E  48 8D 15 5B FA 03 00            lea rdx, [rip + 0x3fa5b]
00C3BB25  8B CB                           mov ecx, ebx
00C3BB27  E8 C4 14 8A FF                  call 0x1404dcff0
00C3BB2C  44 8B C7                        mov r8d, edi
00C3BB2F  48 8D 15 4A FA 03 00            lea rdx, [rip + 0x3fa4a]
00C3BB36  8B CB                           mov ecx, ebx
00C3BB38  E8 5B DF 85 FF                  call 0x140499a98
00C3BB3D  8B C7                           mov eax, edi
00C3BB3F  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00C3BB44  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00C3BB49  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00C3BB4E  48 83 C4 20                     add rsp, 0x20
00C3BB52  41 5F                           pop r15
00C3BB54  41 5D                           pop r13
00C3BB56  5F                              pop rdi
00C3BB57  C3                              ret
00C3BB58  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KseInitialize(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rdi = 0;
    if (a2 != 0) goto loc_00C3B716;
    result = 0;
    if (0 != 2) goto loc_00C3B5F3;
    result = 0;
    goto loc_00C3BB3F;
loc_00C3B5F3:
    if (0 != ((unsigned int)(v_rdi + 1))) goto loc_00C3B601;
    goto loc_00C3BB3F;
loc_00C3B601:
    result = KseShimDatabaseBootInitialize(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 64), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 72)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 80), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 88)));
    if (!sign_flag) goto loc_00C3B62A;
    goto loc_00C3BB3F;
loc_00C3B62A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 64)) == 0) goto loc_00C3B6E3;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 72)) == 0) goto loc_00C3B6E3;
    result = KsepEngineInitialize(v_rip + 2274869, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 72)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 80), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 88)));
    if (sign_flag) goto loc_00C3BA74;
    result = KsepMatchInitMachineInfo(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 72)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 80), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 88)));
    if (sign_flag) goto loc_00C3BA74;
    a3 = 0;
    *(unsigned int *)(v_rip + 2274827) = 2;
    a2 = 0;
    result = KseRegisterShim(v_rip + 1859534, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 88)));
    if (sign_flag) goto loc_00C3BA0D;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 1))) + ((unsigned int)(v_rdi + 1)));
    result = (unsigned int)((result) & (63));
    *(unsigned int *)(v_rip - 12826061 + result * 8 + 15795168) = 0xB0090ULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2274858));
    if ((((unsigned __int8)(v_rdi + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2274858))))) != 0) {
        a2 = v_rip + 263383;
        a1 = 11;
        result = KsepDebugPrint(a1, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 88)));
    }
    result = KsepLogInfo(11, v_rip + 263369, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 88)));
    goto loc_00C3BA0D;
loc_00C3B6E3:
    if ((*(unsigned int *)(v_rip + 2921115)) != ((unsigned int)((unsigned int)((unsigned int)(result))))) {
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(11 + 240) + 64)) == ((unsigned int)((unsigned int)(result)))) goto loc_00C3B704;
    if ((*(unsigned int *)(*(unsigned __int64 *)(11 + 240) + 72)) == ((unsigned int)((unsigned int)((unsigned int)(result))))) {
    }
    goto loc_00C3BA74;
loc_00C3B716:
    if (((unsigned int)((unsigned int)(a2))) != ((unsigned int)(v_rdi + 1))) goto loc_00C3BA0D;
    a3 = 0;
    a2 = 0;
    result = EtwRegister(v_rip - 12687884, a2, a3, v_rip + 2274742);
    result = KseShimDatabaseOpen(v_stack_p18, a2, a3, v_rip + 2274742);
    if (sign_flag) goto loc_00C3BA00;
    if (v_stack_p18 == 0) goto loc_00C3BA00;
    result = KseShimDatabaseClose(v_stack_p18, a2, a3, v_rip + 2274742);
    result = KseVersionLieInitialize(v_stack_p18, a2, a3, v_rip + 2274742);
    a3 = 0;
    a2 = 0;
    result = KseRegisterShim(v_rip + 1859991, a2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3B7CA;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 1))) + ((unsigned int)(v_rdi + 1)));
    a1 = (unsigned int)((a1) & (63));
    *(unsigned int *)(v_rip - 12826061 + a1 * 8 + 15794660) = (unsigned int)(result);
    *(unsigned int *)(v_rip - 12826061 + a1 * 8 + 15794656) = 0xD0093ULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2274634));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2274634)))) & (2)) != 0) {
        a2 = v_rip + 263403;
        a1 = 12;
        result = KsepDebugPrint(a1, a2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 263389, a3, v_rip + 2274742);
loc_00C3B7CA:
    a3 = 0;
    a2 = 0;
    result = KseRegisterShim(v_rip + 1882476, a2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3B828;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 1))) + ((unsigned int)(v_rdi + 1)));
    a1 = (unsigned int)((a1) & (63));
    *(unsigned int *)(v_rip - 12826061 + a1 * 8 + 15794660) = (unsigned int)(result);
    *(unsigned int *)(v_rip - 12826061 + a1 * 8 + 15794656) = 0x100074ULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2274540));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2274540)))) & (2)) != 0) {
        a2 = v_rip + 262813;
        a1 = 12;
        result = KsepDebugPrint(a1, a2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 262799, a3, v_rip + 2274742);
loc_00C3B828:
    a3 = 0;
    a2 = 0;
    result = KseRegisterShim(v_rip + 1882870, a2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3B886;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 1))) + ((unsigned int)(v_rdi + 1)));
    a1 = (unsigned int)((a1) & (63));
    *(unsigned int *)(v_rip - 12826061 + a1 * 8 + 15794660) = (unsigned int)(result);
    *(unsigned int *)(v_rip - 12826061 + a1 * 8 + 15794656) = 0xE007DULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2274446));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2274446)))) & (2)) != 0) {
        a2 = v_rip + 263007;
        a1 = 12;
        result = KsepDebugPrint(a1, a2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 262993, a3, v_rip + 2274742);
loc_00C3B886:
    a3 = 0;
    a2 = 0;
    result = KseRegisterShim(v_rip + 1882984, a2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3B8E4;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 1))) + ((unsigned int)(v_rdi + 1)));
    a1 = (unsigned int)((a1) & (63));
    *(unsigned int *)(v_rip - 12826061 + a1 * 8 + 15794660) = (unsigned int)(result);
    *(unsigned int *)(v_rip - 12826061 + a1 * 8 + 15794656) = 0xF007DULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2274352));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2274352)))) & (2)) != 0) {
        a2 = v_rip + 263009;
        a1 = 12;
        result = KsepDebugPrint(a1, a2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 262995, a3, v_rip + 2274742);
loc_00C3B8E4:
    a3 = 0;
    a2 = 0;
    result = KseRegisterShim(v_rip + 1882834, a2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3B942;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 1))) + ((unsigned int)(v_rdi + 1)));
    a1 = (unsigned int)((a1) & (63));
    *(unsigned int *)(v_rip - 12826061 + a1 * 8 + 15794660) = (unsigned int)(result);
    *(unsigned int *)(v_rip - 12826061 + a1 * 8 + 15794656) = 0x110060ULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2274258));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2274258)))) & (2)) != 0) {
        a2 = v_rip + 262867;
        a1 = 12;
        result = KsepDebugPrint(a1, a2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 262853, a3, v_rip + 2274742);
loc_00C3B942:
    a3 = 0;
    a2 = 0;
    result = KseRegisterShim(v_rip + 1859460, a2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3B9A0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 1))) + ((unsigned int)(v_rdi + 1)));
    a1 = (unsigned int)((a1) & (63));
    *(unsigned int *)(v_rip - 12826061 + a1 * 8 + 15794660) = (unsigned int)(result);
    *(unsigned int *)(v_rip - 12826061 + a1 * 8 + 15794656) = 0x120069ULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2274164));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2274164)))) & (2)) != 0) {
        a2 = v_rip + 262869;
        a1 = 12;
        result = KsepDebugPrint(a1, a2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 262855, a3, v_rip + 2274742);
loc_00C3B9A0:
    a3 = 0;
    a2 = 0;
    result = KseRegisterShim(v_rip + 1859542, a2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3BA0D;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 1))) + ((unsigned int)(v_rdi + 1)));
    a2 = (unsigned int)((a2) & (63));
    *(unsigned int *)(v_rip - 12826061 + a2 * 8 + 15794660) = (unsigned int)(result);
    *(unsigned int *)(v_rip - 12826061 + a2 * 8 + 15794656) = 0x13005BULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2274070));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2274070)))) & (2)) != 0) {
        a2 = v_rip + 262903;
        a1 = 12;
        result = KsepDebugPrint(a1, a2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 262889, a3, v_rip + 2274742);
    goto loc_00C3BA0D;
loc_00C3BA00:
loc_00C3BA0D:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 1))) + ((unsigned int)(v_rdi + 1)));
    result = (unsigned int)((result) & (63));
    *(unsigned int *)(v_rip - 12826061 + result * 8 + 15795168) = 0x500FEULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2273969));
    if ((((unsigned __int8)(v_rdi + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2273969))))) != 0) {
        a3 = (unsigned int)((unsigned int)(a2));
        a2 = v_rip + 260971;
        a1 = (unsigned int)(v_rdi + 1);
        result = KsepDebugPrint(a1, a2, a3, v_rip + 2274742);
    }
    result = KsepLogInfo((unsigned int)((unsigned int)(v_rdi + 1)), v_rip + 260954, (unsigned int)((unsigned int)((unsigned int)(a2))), v_rip + 2274742);
    if ((*(unsigned __int8 *)(v_rip + 3704548)) != 0) {
    }
    if (!sign_flag) goto loc_00C3BB3D;
loc_00C3BA74:
    *(unsigned int *)(v_rip + 2273791) = 0;
    if (*(unsigned __int64 *)(v_rip + 2273869) != 0) {
        result = KsepCacheUninitialize(*(unsigned __int64 *)(v_rip + 2273869), v_rip + 260954, (unsigned int)((unsigned int)((unsigned int)(a2))), v_rip + 2274742);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 1))) + ((unsigned int)(v_rdi + 1)));
    result = (unsigned int)((result) & (63));
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) != 0xC00000BBULL) goto loc_00C3BAFD;
    *(unsigned int *)(v_rip - 12826061 + result * 8 + 15794660) = 0xC00000BBULL;
    *(unsigned int *)(v_rip - 12826061 + result * 8 + 15794656) = 0x5011AULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2273805));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2273805)))) & (2)) != 0) {
        a2 = v_rip + 260650;
        a1 = (unsigned int)(v_rdi + 1);
        result = KsepDebugPrint(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a2))), v_rip + 2274742);
    }
    result = KsepLogError((unsigned int)((unsigned int)(v_rdi + 1)), v_rip + 260636, (unsigned int)((unsigned int)((unsigned int)(a2))), v_rip + 2274742);
    goto loc_00C3BB3D;
loc_00C3BAFD:
    *(unsigned int *)(v_rip - 12826061 + result * 8 + 15794660) = (unsigned int)((unsigned int)(0xC00000BBULL));
    *(unsigned int *)(v_rip - 12826061 + result * 8 + 15794656) = 0x5011EULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2273745));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2273745)))) & (2)) != 0) {
        a3 = (unsigned int)((unsigned int)(0xC00000BBULL));
        a2 = v_rip + 260699;
        a1 = (unsigned int)(v_rdi + 1);
        result = KsepDebugPrint(a1, a2, a3, v_rip + 2274742);
    }
    result = KsepLogError((unsigned int)((unsigned int)(v_rdi + 1)), v_rip + 260682, (unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL))), v_rip + 2274742);
loc_00C3BB3D:
loc_00C3BB3F:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)(0xC00000BBULL)));
}
```

## 5. (Beta) C Style

```c
int64_t KseInitialize(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
    if (Arg2 != 0) goto loc_00C3B716;
    result = 0;
    if (0 != 2) goto loc_00C3B5F3;
    result = 0;
    goto loc_00C3BB3F;
loc_00C3B5F3:
    if (0 != ((uint32_t)(local_rdi + 1))) goto loc_00C3B601;
    goto loc_00C3BB3F;
loc_00C3B601:
    result = KseShimDatabaseBootInitialize(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x40), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x48)), *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x50), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x58)));
    if (!sign_flag) goto loc_00C3B62A;
    goto loc_00C3BB3F;
loc_00C3B62A:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x40)) == 0) goto loc_00C3B6E3;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x48)) == 0) goto loc_00C3B6E3;
    result = KsepEngineInitialize(v_rip + 2274869, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x48)), *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x50), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x58)));
    if (sign_flag) goto loc_00C3BA74;
    result = KsepMatchInitMachineInfo(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x48)), *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x50), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x58)));
    if (sign_flag) goto loc_00C3BA74;
    a3 = 0;
    *(uint32_t *)(v_rip + 0x22B60B) = 2;
    Arg2 = 0;
    result = KseRegisterShim(v_rip + 1859534, Arg2, a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x58)));
    if (sign_flag) goto loc_00C3BA0D;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 1))) + ((uint32_t)(local_rdi + 1)));
    result = (uint32_t)((result) & (63));
    *(uint32_t *)(v_rip - 0xC3B5CD + result * 8 + 0xF103E0) = 0xB0090ULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x22B62A));
    if ((((uint8_t)(local_rdi + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x22B62A))))) != 0) {
        Arg2 = v_rip + 263383;
        Arg1 = 11;
        result = KsepDebugPrint(Arg1, Arg2, a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x58)));
    }
    result = KsepLogInfo(11, v_rip + 263369, a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x58)));
    goto loc_00C3BA0D;
loc_00C3B6E3:
    if ((*(uint32_t *)(v_rip + 0x2C929B)) != ((uint32_t)((uint32_t)((uint32_t)(result))))) {
    }
    if ((*(uint64_t *)(*(uint64_t *)(11 + 0xF0) + 0x40)) == ((uint32_t)((uint32_t)(result)))) goto loc_00C3B704;
    if ((*(uint32_t *)(*(uint64_t *)(11 + 0xF0) + 0x48)) == ((uint32_t)((uint32_t)((uint32_t)(result))))) {
    }
    goto loc_00C3BA74;
loc_00C3B716:
    if (((uint32_t)((uint32_t)(Arg2))) != ((uint32_t)(local_rdi + 1))) goto loc_00C3BA0D;
    a3 = 0;
    Arg2 = 0;
    result = EtwRegister(v_rip - 12687884, Arg2, a3, v_rip + 2274742);
    result = KseShimDatabaseOpen(v_stack_p18, Arg2, a3, v_rip + 2274742);
    if (sign_flag) goto loc_00C3BA00;
    if (v_stack_p18 == 0) goto loc_00C3BA00;
    result = KseShimDatabaseClose(v_stack_p18, Arg2, a3, v_rip + 2274742);
    result = KseVersionLieInitialize(v_stack_p18, Arg2, a3, v_rip + 2274742);
    a3 = 0;
    Arg2 = 0;
    result = KseRegisterShim(v_rip + 1859991, Arg2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3B7CA;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 1))) + ((uint32_t)(local_rdi + 1)));
    Arg1 = (uint32_t)((Arg1) & (63));
    *(uint32_t *)(v_rip - 0xC3B5CD + arg1 * 8 + 0xF101E4) = (uint32_t)(result);
    *(uint32_t *)(v_rip - 0xC3B5CD + arg1 * 8 + 0xF101E0) = 0xD0093ULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x22B54A));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x22B54A)))) & (2)) != 0) {
        Arg2 = v_rip + 263403;
        Arg1 = 12;
        result = KsepDebugPrint(Arg1, Arg2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 263389, a3, v_rip + 2274742);
loc_00C3B7CA:
    a3 = 0;
    Arg2 = 0;
    result = KseRegisterShim(v_rip + 1882476, Arg2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3B828;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 1))) + ((uint32_t)(local_rdi + 1)));
    Arg1 = (uint32_t)((Arg1) & (63));
    *(uint32_t *)(v_rip - 0xC3B5CD + arg1 * 8 + 0xF101E4) = (uint32_t)(result);
    *(uint32_t *)(v_rip - 0xC3B5CD + arg1 * 8 + 0xF101E0) = 0x100074ULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x22B4EC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x22B4EC)))) & (2)) != 0) {
        Arg2 = v_rip + 262813;
        Arg1 = 12;
        result = KsepDebugPrint(Arg1, Arg2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 262799, a3, v_rip + 2274742);
loc_00C3B828:
    a3 = 0;
    Arg2 = 0;
    result = KseRegisterShim(v_rip + 1882870, Arg2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3B886;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 1))) + ((uint32_t)(local_rdi + 1)));
    Arg1 = (uint32_t)((Arg1) & (63));
    *(uint32_t *)(v_rip - 0xC3B5CD + arg1 * 8 + 0xF101E4) = (uint32_t)(result);
    *(uint32_t *)(v_rip - 0xC3B5CD + arg1 * 8 + 0xF101E0) = 0xE007DULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x22B48E));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x22B48E)))) & (2)) != 0) {
        Arg2 = v_rip + 263007;
        Arg1 = 12;
        result = KsepDebugPrint(Arg1, Arg2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 262993, a3, v_rip + 2274742);
loc_00C3B886:
    a3 = 0;
    Arg2 = 0;
    result = KseRegisterShim(v_rip + 1882984, Arg2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3B8E4;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 1))) + ((uint32_t)(local_rdi + 1)));
    Arg1 = (uint32_t)((Arg1) & (63));
    *(uint32_t *)(v_rip - 0xC3B5CD + arg1 * 8 + 0xF101E4) = (uint32_t)(result);
    *(uint32_t *)(v_rip - 0xC3B5CD + arg1 * 8 + 0xF101E0) = 0xF007DULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x22B430));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x22B430)))) & (2)) != 0) {
        Arg2 = v_rip + 263009;
        Arg1 = 12;
        result = KsepDebugPrint(Arg1, Arg2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 262995, a3, v_rip + 2274742);
loc_00C3B8E4:
    a3 = 0;
    Arg2 = 0;
    result = KseRegisterShim(v_rip + 1882834, Arg2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3B942;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 1))) + ((uint32_t)(local_rdi + 1)));
    Arg1 = (uint32_t)((Arg1) & (63));
    *(uint32_t *)(v_rip - 0xC3B5CD + arg1 * 8 + 0xF101E4) = (uint32_t)(result);
    *(uint32_t *)(v_rip - 0xC3B5CD + arg1 * 8 + 0xF101E0) = 0x110060ULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x22B3D2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x22B3D2)))) & (2)) != 0) {
        Arg2 = v_rip + 262867;
        Arg1 = 12;
        result = KsepDebugPrint(Arg1, Arg2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 262853, a3, v_rip + 2274742);
loc_00C3B942:
    a3 = 0;
    Arg2 = 0;
    result = KseRegisterShim(v_rip + 1859460, Arg2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3B9A0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 1))) + ((uint32_t)(local_rdi + 1)));
    Arg1 = (uint32_t)((Arg1) & (63));
    *(uint32_t *)(v_rip - 0xC3B5CD + arg1 * 8 + 0xF101E4) = (uint32_t)(result);
    *(uint32_t *)(v_rip - 0xC3B5CD + arg1 * 8 + 0xF101E0) = 0x120069ULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x22B374));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x22B374)))) & (2)) != 0) {
        Arg2 = v_rip + 262869;
        Arg1 = 12;
        result = KsepDebugPrint(Arg1, Arg2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 262855, a3, v_rip + 2274742);
loc_00C3B9A0:
    a3 = 0;
    Arg2 = 0;
    result = KseRegisterShim(v_rip + 1859542, Arg2, a3, v_rip + 2274742);
    if (!sign_flag) goto loc_00C3BA0D;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 1))) + ((uint32_t)(local_rdi + 1)));
    Arg2 = (uint32_t)((Arg2) & (63));
    *(uint32_t *)(v_rip - 0xC3B5CD + Arg2 * 8 + 0xF101E4) = (uint32_t)(result);
    *(uint32_t *)(v_rip - 0xC3B5CD + Arg2 * 8 + 0xF101E0) = 0x13005BULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x22B316));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x22B316)))) & (2)) != 0) {
        Arg2 = v_rip + 262903;
        Arg1 = 12;
        result = KsepDebugPrint(Arg1, Arg2, a3, v_rip + 2274742);
    }
    result = KsepLogError(12, v_rip + 262889, a3, v_rip + 2274742);
    goto loc_00C3BA0D;
loc_00C3BA00:
loc_00C3BA0D:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 1))) + ((uint32_t)(local_rdi + 1)));
    result = (uint32_t)((result) & (63));
    *(uint32_t *)(v_rip - 0xC3B5CD + result * 8 + 0xF103E0) = 0x500FEULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x22B2B1));
    if ((((uint8_t)(local_rdi + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x22B2B1))))) != 0) {
        a3 = (uint32_t)((uint32_t)(Arg2));
        Arg2 = v_rip + 260971;
        Arg1 = (uint32_t)(local_rdi + 1);
        result = KsepDebugPrint(Arg1, Arg2, a3, v_rip + 2274742);
    }
    result = KsepLogInfo((uint32_t)((uint32_t)(local_rdi + 1)), v_rip + 260954, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_rip + 2274742);
    if ((*(uint8_t *)(v_rip + 0x3886E4)) != 0) {
    }
    if (!sign_flag) goto loc_00C3BB3D;
loc_00C3BA74:
    *(uint32_t *)(v_rip + 0x22B1FF) = 0;
    if (*(uint64_t *)(v_rip + 0x22B24D) != 0) {
        result = KsepCacheUninitialize(*(uint64_t *)(v_rip + 0x22B24D), v_rip + 260954, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_rip + 2274742);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 1))) + ((uint32_t)(local_rdi + 1)));
    result = (uint32_t)((result) & (63));
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) != 0xC00000BBULL) goto loc_00C3BAFD;
    *(uint32_t *)(v_rip - 0xC3B5CD + result * 8 + 0xF101E4) = 0xC00000BBULL;
    *(uint32_t *)(v_rip - 0xC3B5CD + result * 8 + 0xF101E0) = 0x5011AULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x22B20D));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x22B20D)))) & (2)) != 0) {
        Arg2 = v_rip + 260650;
        Arg1 = (uint32_t)(local_rdi + 1);
        result = KsepDebugPrint(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_rip + 2274742);
    }
    result = KsepLogError((uint32_t)((uint32_t)(local_rdi + 1)), v_rip + 260636, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_rip + 2274742);
    goto loc_00C3BB3D;
loc_00C3BAFD:
    *(uint32_t *)(v_rip - 0xC3B5CD + result * 8 + 0xF101E4) = (uint32_t)((uint32_t)(0xC00000BBULL));
    *(uint32_t *)(v_rip - 0xC3B5CD + result * 8 + 0xF101E0) = 0x5011EULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x22B1D1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x22B1D1)))) & (2)) != 0) {
        a3 = (uint32_t)((uint32_t)(0xC00000BBULL));
        Arg2 = v_rip + 260699;
        Arg1 = (uint32_t)(local_rdi + 1);
        result = KsepDebugPrint(Arg1, Arg2, a3, v_rip + 2274742);
    }
    result = KsepLogError((uint32_t)((uint32_t)(local_rdi + 1)), v_rip + 260682, (uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL))), v_rip + 2274742);
loc_00C3BB3D:
loc_00C3BB3F:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)(0xC00000BBULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xF0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C3B5AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
