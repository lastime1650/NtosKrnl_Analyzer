# BgpFwLibraryInitialize

- RVA: `0x00BC5400`–`0x00BC5C67` (길이 `2,151` bytes)
- VA: `0x0000000140BC5400`
- 실행 섹션: `PAGEBGFX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BBEBC`
- 디코드: `488`개 명령, `2,151/2,151` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **43**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **50**

### Outgoing calls
- `0x00BC5460` → [BgpFwAcquireLock](../../text/4B/BgpFwAcquireLock_function_004B3AA4.md) (function, `0x004B3AA4`)
- `0x00BC54A2` → [BgpFwLibraryEnable](../../text/69/BgpFwLibraryEnable_function_0069ED8C.md) (function, `0x0069ED8C`)
- `0x00BC54E0` → [BgpFwReservePoolSwap](BgpFwReservePoolSwap_function_00BC1828.md) (function, `0x00BC1828`)
- `0x00BC54EC` → [ResFwConfigureDisplayStringResources](ResFwConfigureDisplayStringResources_function_00BC18C4.md) (function, `0x00BC18C4`)
- `0x00BC54FF` → [AnFwConfigureProgressResources](AnFwConfigureProgressResources_function_00BC1CFC.md) (function, `0x00BC1CFC`)
- `0x00BC550B` → [LogFwInitialize](LogFwInitialize_function_00BC2E70.md) (function, `0x00BC2E70`)
- `0x00BC551A` → [AnFwProgressIndicatorTransition](AnFwProgressIndicatorTransition_function_00BC0008.md) (function, `0x00BC0008`)
- `0x00BC551F` → [BgpFwReleaseLock](../../text/4B/BgpFwReleaseLock_function_004B357C.md) (function, `0x004B357C`)
- `0x00BC5534` → [BgpFwInitializeLock](../../init/C8/BgpFwInitializeLock_function_00C805CC.md) (function, `0x00C805CC`)
- `0x00BC5582` → [BgpFwInitializeReservePool](BgpFwInitializeReservePool_function_00BC1634.md) (function, `0x00BC1634`)
- `0x00BC558B` → [BgpFwLibraryEnable](../../text/69/BgpFwLibraryEnable_function_0069ED8C.md) (function, `0x0069ED8C`)
- `0x00BC55B1` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (function, `0x003E4374`)
- `0x00BC55E7` → [BgpFoInitialize](../../init/C8/BgpFoInitialize_function_00C806B0.md) (function, `0x00C806B0`)
- `0x00BC5629` → [BgpBcInitializeCriticalMode](../../init/C8/BgpBcInitializeCriticalMode_function_00C81454.md) (function, `0x00C81454`)
- `0x00BC5647` → [BgpFwAcquireLock](../../text/4B/BgpFwAcquireLock_function_004B3AA4.md) (function, `0x004B3AA4`)
- `0x00BC5650` → [BgpFwLibraryEnable](../../text/69/BgpFwLibraryEnable_function_0069ED8C.md) (function, `0x0069ED8C`)
- `0x00BC565B` → [BgpFwReleaseLock](../../text/4B/BgpFwReleaseLock_function_004B357C.md) (function, `0x004B357C`)
- `0x00BC566C` → [MmGetPhysicalAddress](../../text/23/MmGetPhysicalAddress_function_0023A500.md) (function, `0x0023A500`)
- `0x00BC57F5` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (function, `0x003E4374`)
- `0x00BC580C` → [BgpFwReleaseLock](../../text/4B/BgpFwReleaseLock_function_004B357C.md) (function, `0x004B357C`)
- `0x00BC5816` → [BgpFwLibraryDestroy](BgpFwLibraryDestroy_function_00BC1678.md) (function, `0x00BC1678`)
- `0x00BC58E9` → [BgpFwInitializeReservePool](BgpFwInitializeReservePool_function_00BC1634.md) (function, `0x00BC1634`)
- `0x00BC5915` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00BC593F` → [BgpFoInitialize](../../init/C8/BgpFoInitialize_function_00C806B0.md) (function, `0x00C806B0`)
- `0x00BC596C` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x00BC59A7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00BC59D7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00BC59EB` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (function, `0x003E4374`)
- `0x00BC5A0D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00BC5A3F` → [BgpGxProcessQrCodeBitmap](../../text/69/BgpGxProcessQrCodeBitmap_function_0069F244.md) (function, `0x0069F244`)
- `0x00BC5A74` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (function, `0x003E4374`)
- `0x00BC5AA1` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00BC5AB6` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (function, `0x003E4374`)
- `0x00BC5ACE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00BC5AD8` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (function, `0x003E4374`)
- `0x00BC5B00` → [BgpFoInitialize](../../init/C8/BgpFoInitialize_function_00C806B0.md) (function, `0x00C806B0`)
- `0x00BC5B15` → [BgpFwFreeMemory](../../text/3E/BgpFwFreeMemory_function_003E25E0.md) (function, `0x003E25E0`)
- `0x00BC5B1D` → [BgpFwFreeMemory](../../text/3E/BgpFwFreeMemory_function_003E25E0.md) (function, `0x003E25E0`)
- `0x00BC5B71` → [BgpBcInitializeCriticalMode](../../init/C8/BgpBcInitializeCriticalMode_function_00C81454.md) (function, `0x00C81454`)
- `0x00BC5B8F` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (function, `0x003E4374`)
- `0x00BC5BFD` → [ResFwConfigureDisplayStringResources](ResFwConfigureDisplayStringResources_function_00BC18C4.md) (function, `0x00BC18C4`)
- `0x00BC5C10` → [AnFwConfigureProgressResources](AnFwConfigureProgressResources_function_00BC1CFC.md) (function, `0x00BC1CFC`)
- `0x00BC5C2F` → [BgpFwReleaseLock](../../text/4B/BgpFwReleaseLock_function_004B357C.md) (function, `0x004B357C`)

### Direct callers
- [BgLibraryInitialize](BgLibraryInitialize_function_00BC0760.md) at `0x00BC0778`

### Static image references
- `0x00BC5438` → RVA `0x00EF0450` (`.data`; read)
- `0x00BC547B` → RVA `0x00EF0400` (`.data`; write)
- `0x00BC548E` → RVA `0x00EF0450` (`.data`; write)
- `0x00BC5494` → RVA `0x00EF03E0` (`.data`; read)
- `0x00BC549B` → RVA `0x00EF03F0` (`.data`; read)
- `0x00BC54AF` → RVA `0x00EF0450` (`.data`; read/write)
- `0x00BC54C0` → RVA `0x00EF0518` (`.data`; write)
- `0x00BC54C7` → RVA `0x00EF0510` (`.data`; write)
- `0x00BC5544` → RVA `0x00EF0520` (`.data`; read)
- `0x00BC554B` → RVA `0x00EF0528` (`.data`; write)
- `0x00BC5552` → RVA `0x00EF0520` (`.data`; write)
- `0x00BC5576` → RVA `0x00E64750` (`.data`; read)
- `0x00BC559E` → RVA `0x00EF0488` (`.data`; write)
- `0x00BC55E0` → RVA `0x00EF04F8` (`.data`; write)
- `0x00BC5604` → RVA `0x00EF05D0` (`.data`; write)
- `0x00BC5612` → RVA `0x00EF05D8` (`.data`; write)
- `0x00BC5623` → RVA `0x00EF05B8` (`.data`; write)
- `0x00BC5665` → RVA `0x00EF0400` (`.data`; read)
- `0x00BC5677` → RVA `0x00EF0430` (`.data`; write)
- `0x00BC567E` → RVA `0x00EF03E8` (`.data`; read)
- `0x00BC5684` → RVA `0x00EF0438` (`.data`; write)
- `0x00BC568A` → RVA `0x00EF03E4` (`.data`; read)
- `0x00BC5690` → RVA `0x00EF043C` (`.data`; write)
- `0x00BC5696` → RVA `0x00EF03EC` (`.data`; read)
- `0x00BC569C` → RVA `0x00EF0440` (`.data`; write)
- `0x00BC56AC` → RVA `0x00EF0448` (`.data`; write)
- `0x00BC56E4` → RVA `0x00EF0530` (`.data`; read)
- `0x00BC5707` → RVA `0x00EF0540` (`.data`; read)
- `0x00BC5715` → RVA `0x00EF0550` (`.data`; read)
- `0x00BC5723` → RVA `0x00EF0560` (`.data`; read)
- `0x00BC5731` → RVA `0x00EF0570` (`.data`; read)
- `0x00BC573F` → RVA `0x00EF0580` (`.data`; read)
- `0x00BC574D` → RVA `0x00EF0590` (`.data`; read)
- `0x00BC575B` → RVA `0x00EF05A0` (`.data`; read)
- `0x00BC57FD` → RVA `0x00EF0480` (`.data`; write)
- `0x00BC58F1` → RVA `0x00EF0500` (`.data`; write)
- `0x00BC5957` → RVA `0x00EF0500` (`.data`; read)
- `0x00BC5962` → RVA `0x00BC5D60` (` ?? ::CIJCHKMG::`string'`; read)
- `0x00BC5971` → RVA `0x00EF0508` (`.data`; write)
- `0x00BC59CC` → RVA `0x00EF0498` (`.data`; read)
- `0x00BC59F0` → RVA `0x00EF0498` (`.data`; write)
- `0x00BC5A18` → RVA `0x00EF04A8` (`.data`; write)
- `0x00BC5A25` → RVA `0x00EF04AC` (`.data`; write)
- `0x00BC5A38` → RVA `0x00EF04D8` (`.data`; read)
- `0x00BC5A48` → RVA `0x00EF04D8` (`.data`; write)
- `0x00BC5A79` → RVA `0x00EF04E0` (`.data`; write)
- `0x00BC5A96` → RVA `0x00EF04E0` (`.data`; read)
- `0x00BC5B5C` → RVA `0x00EF05DC` (`.data`; write)
- `0x00BC5C29` → RVA `0x00EF0454` (`.data`; write)
- `0x00BC5C3B` → RVA `0x00EF04F0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **33**
  - `0x00BC5460` → [BgpFwAcquireLock](../../text/4B/BgpFwAcquireLock_function_004B3AA4.md) (`PAGEBGFX` → `.text`)
  - `0x00BC54A2` → [BgpFwLibraryEnable](../../text/69/BgpFwLibraryEnable_function_0069ED8C.md) (`PAGEBGFX` → `.text`)
  - `0x00BC551F` → [BgpFwReleaseLock](../../text/4B/BgpFwReleaseLock_function_004B357C.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5534` → [BgpFwInitializeLock](../../init/C8/BgpFwInitializeLock_function_00C805CC.md) (`PAGEBGFX` → `INIT`)
  - `0x00BC558B` → [BgpFwLibraryEnable](../../text/69/BgpFwLibraryEnable_function_0069ED8C.md) (`PAGEBGFX` → `.text`)
  - `0x00BC55B1` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (`PAGEBGFX` → `.text`)
  - `0x00BC55E7` → [BgpFoInitialize](../../init/C8/BgpFoInitialize_function_00C806B0.md) (`PAGEBGFX` → `INIT`)
  - `0x00BC5629` → [BgpBcInitializeCriticalMode](../../init/C8/BgpBcInitializeCriticalMode_function_00C81454.md) (`PAGEBGFX` → `INIT`)
  - `0x00BC5647` → [BgpFwAcquireLock](../../text/4B/BgpFwAcquireLock_function_004B3AA4.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5650` → [BgpFwLibraryEnable](../../text/69/BgpFwLibraryEnable_function_0069ED8C.md) (`PAGEBGFX` → `.text`)
  - `0x00BC565B` → [BgpFwReleaseLock](../../text/4B/BgpFwReleaseLock_function_004B357C.md) (`PAGEBGFX` → `.text`)
  - `0x00BC566C` → [MmGetPhysicalAddress](../../text/23/MmGetPhysicalAddress_function_0023A500.md) (`PAGEBGFX` → `.text`)
  - `0x00BC57F5` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (`PAGEBGFX` → `.text`)
  - `0x00BC580C` → [BgpFwReleaseLock](../../text/4B/BgpFwReleaseLock_function_004B357C.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5915` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGEBGFX` → `.text`)
  - `0x00BC593F` → [BgpFoInitialize](../../init/C8/BgpFoInitialize_function_00C806B0.md) (`PAGEBGFX` → `INIT`)
  - `0x00BC596C` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (`PAGEBGFX` → `.text`)
  - `0x00BC59A7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGEBGFX` → `.text`)
  - `0x00BC59D7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGEBGFX` → `.text`)
  - `0x00BC59EB` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5A0D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5A3F` → [BgpGxProcessQrCodeBitmap](../../text/69/BgpGxProcessQrCodeBitmap_function_0069F244.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5A74` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5AA1` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5AB6` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5ACE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5AD8` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5B00` → [BgpFoInitialize](../../init/C8/BgpFoInitialize_function_00C806B0.md) (`PAGEBGFX` → `INIT`)
  - `0x00BC5B15` → [BgpFwFreeMemory](../../text/3E/BgpFwFreeMemory_function_003E25E0.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5B1D` → [BgpFwFreeMemory](../../text/3E/BgpFwFreeMemory_function_003E25E0.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5B71` → [BgpBcInitializeCriticalMode](../../init/C8/BgpBcInitializeCriticalMode_function_00C81454.md) (`PAGEBGFX` → `INIT`)
  - `0x00BC5B8F` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (`PAGEBGFX` → `.text`)
  - `0x00BC5C2F` → [BgpFwReleaseLock](../../text/4B/BgpFwReleaseLock_function_004B357C.md) (`PAGEBGFX` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC5400  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00BC5404  53                              push rbx
00BC5405  55                              push rbp
00BC5406  56                              push rsi
00BC5407  57                              push rdi
00BC5408  41 54                           push r12
00BC540A  41 55                           push r13
00BC540C  41 56                           push r14
00BC540E  41 57                           push r15
00BC5410  48 83 EC 28                     sub rsp, 0x28
00BC5414  45 33 ED                        xor r13d, r13d
00BC5417  8B DA                           mov ebx, edx
00BC5419  48 8B F1                        mov rsi, rcx
00BC541C  48 85 C9                        test rcx, rcx
00BC541F  0F 84 2B 08 00 00               je 0x140bc5c50
00BC5425  83 79 74 05                     cmp dword ptr [rcx + 0x74], 5
00BC5429  73 0A                           jae 0x140bc5435
00BC542B  B8 59 00 00 C0                  mov eax, 0xc0000059
00BC5430  E9 20 08 00 00                  jmp 0x140bc5c55
00BC5435  8B 69 78                        mov ebp, dword ptr [rcx + 0x78]
00BC5438  8B 05 12 B0 32 00               mov eax, dword ptr [rip + 0x32b012]
00BC543E  81 E5 00 00 FF 16               and ebp, 0x16ff0000
00BC5444  A8 01                           test al, 1
00BC5446  74 0E                           je 0x140bc5456
00BC5448  A8 04                           test al, 4
00BC544A  75 0A                           jne 0x140bc5456
00BC544C  0F BA E5 14                     bt ebp, 0x14
00BC5450  0F 83 FA 07 00 00               jae 0x140bc5c50
00BC5456  0F BA E5 14                     bt ebp, 0x14
00BC545A  0F 83 C9 00 00 00               jae 0x140bc5529
00BC5460  E8 3F E6 8E FF                  call 0x1404b3aa4
00BC5465  83 CF FF                        or edi, 0xffffffff
00BC5468  3B DF                           cmp ebx, edi
00BC546A  0F 85 A2 00 00 00               jne 0x140bc5512
00BC5470  8B 05 DA AF 32 00               mov eax, dword ptr [rip + 0x32afda]
00BC5476  33 C9                           xor ecx, ecx
00BC5478  0F 57 C0                        xorps xmm0, xmm0
00BC547B  48 89 0D 7E AF 32 00            mov qword ptr [rip + 0x32af7e], rcx
00BC5482  83 E0 FD                        and eax, 0xfffffffd
00BC5485  48 8D 4E 20                     lea rcx, [rsi + 0x20]
00BC5489  0D 00 18 10 00                  or eax, 0x101800
00BC548E  89 05 BC AF 32 00               mov dword ptr [rip + 0x32afbc], eax
00BC5494  0F 11 05 45 AF 32 00            movups xmmword ptr [rip + 0x32af45], xmm0
00BC549B  0F 11 05 4E AF 32 00            movups xmmword ptr [rip + 0x32af4e], xmm0
00BC54A2  E8 E5 98 AD FF                  call 0x14069ed8c
00BC54A7  85 C0                           test eax, eax
00BC54A9  0F 88 A6 07 00 00               js 0x140bc5c55
00BC54AF  0F BA 35 99 AF 32 00 0D         btr dword ptr [rip + 0x32af99], 0xd
00BC54B7  4C 8B 4E 10                     mov r9, qword ptr [rsi + 0x10]
00BC54BB  4D 85 C9                        test r9, r9
00BC54BE  75 10                           jne 0x140bc54d0
00BC54C0  4C 89 2D 51 B0 32 00            mov qword ptr [rip + 0x32b051], r13
00BC54C7  4C 89 2D 42 B0 32 00            mov qword ptr [rip + 0x32b042], r13
00BC54CE  EB 3B                           jmp 0x140bc550b
00BC54D0  44 8B 86 F8 00 00 00            mov r8d, dword ptr [rsi + 0xf8]
00BC54D7  33 C9                           xor ecx, ecx
00BC54D9  48 8B 96 F0 00 00 00            mov rdx, qword ptr [rsi + 0xf0]
00BC54E0  E8 43 C3 FF FF                  call 0x140bc1828
00BC54E5  48 8B 8E 00 01 00 00            mov rcx, qword ptr [rsi + 0x100]
00BC54EC  E8 D3 C3 FF FF                  call 0x140bc18c4
00BC54F1  48 89 05 20 B0 32 00            mov qword ptr [rip + 0x32b020], rax
00BC54F8  48 8B 8E 08 01 00 00            mov rcx, qword ptr [rsi + 0x108]
00BC54FF  E8 F8 C7 FF FF                  call 0x140bc1cfc
00BC5504  48 89 05 05 B0 32 00            mov qword ptr [rip + 0x32b005], rax
00BC550B  E8 60 D9 FF FF                  call 0x140bc2e70
00BC5510  EB 0D                           jmp 0x140bc551f
00BC5512  0F BA 35 36 AF 32 00 0C         btr dword ptr [rip + 0x32af36], 0xc
00BC551A  E8 E9 AA FF FF                  call 0x140bc0008
00BC551F  E8 58 E0 8E FF                  call 0x1404b357c
00BC5524  E9 19 07 00 00                  jmp 0x140bc5c42
00BC5529  83 CF FF                        or edi, 0xffffffff
00BC552C  3B DF                           cmp ebx, edi
00BC552E  0F 85 13 01 00 00               jne 0x140bc5647
00BC5534  E8 93 B0 0B 00                  call 0x140c805cc
00BC5539  0D 04 0C 00 00                  or eax, 0xc04
00BC553E  89 05 0C AF 32 00               mov dword ptr [rip + 0x32af0c], eax
00BC5544  48 8D 05 D5 AF 32 00            lea rax, [rip + 0x32afd5]
00BC554B  48 89 05 D6 AF 32 00            mov qword ptr [rip + 0x32afd6], rax
00BC5552  48 89 05 C7 AF 32 00            mov qword ptr [rip + 0x32afc7], rax
00BC5559  48 8B 89 F0 00 00 00            mov rcx, qword ptr [rcx + 0xf0]
00BC5560  48 85 C9                        test rcx, rcx
00BC5563  0F 84 D4 00 00 00               je 0x140bc563d
00BC5569  44 39 AE F8 00 00 00            cmp dword ptr [rsi + 0xf8], r13d
00BC5570  0F 84 C7 00 00 00               je 0x140bc563d
00BC5576  4C 8D 05 D3 F1 29 00            lea r8, [rip + 0x29f1d3]
00BC557D  BA 00 40 00 00                  mov edx, 0x4000
00BC5582  E8 AD C0 FF FF                  call 0x140bc1634
00BC5587  48 8D 4E 20                     lea rcx, [rsi + 0x20]
00BC558B  E8 FC 97 AD FF                  call 0x14069ed8c
00BC5590  8B D8                           mov ebx, eax
00BC5592  85 C0                           test eax, eax
00BC5594  0F 88 7C 02 00 00               js 0x140bc5816
00BC559A  0F 10 46 64                     movups xmm0, xmmword ptr [rsi + 0x64]
00BC559E  F3 0F 7F 05 E2 AE 32 00         movdqu xmmword ptr [rip + 0x32aee2], xmm0
00BC55A6  4C 39 6E 58                     cmp qword ptr [rsi + 0x58], r13
00BC55AA  74 4A                           je 0x140bc55f6
00BC55AC  B9 18 00 00 00                  mov ecx, 0x18
00BC55B1  E8 BE ED 81 FF                  call 0x1403e4374
00BC55B6  48 8B C8                        mov rcx, rax
00BC55B9  48 85 C0                        test rax, rax
00BC55BC  0F 84 4F 02 00 00               je 0x140bc5811
00BC55C2  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
00BC55C6  33 D2                           xor edx, edx
00BC55C8  48 89 01                        mov qword ptr [rcx], rax
00BC55CB  8B 46 60                        mov eax, dword ptr [rsi + 0x60]
00BC55CE  89 41 08                        mov dword ptr [rcx + 8], eax
00BC55D1  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
00BC55D5  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
00BC55D9  C7 41 0C 01 00 00 00            mov dword ptr [rcx + 0xc], 1
00BC55E0  48 89 0D 11 AF 32 00            mov qword ptr [rip + 0x32af11], rcx
00BC55E7  E8 C4 B0 0B 00                  call 0x140c806b0
00BC55EC  8B D8                           mov ebx, eax
00BC55EE  85 C0                           test eax, eax
00BC55F0  0F 88 20 02 00 00               js 0x140bc5816
00BC55F6  83 7E 74 03                     cmp dword ptr [rsi + 0x74], 3
00BC55FA  72 1C                           jb 0x140bc5618
00BC55FC  F2 0F 10 86 94 01 00 00         movsd xmm0, qword ptr [rsi + 0x194]
00BC5604  F2 0F 11 05 C4 AF 32 00         movsd qword ptr [rip + 0x32afc4], xmm0
00BC560C  8B 86 9C 01 00 00               mov eax, dword ptr [rsi + 0x19c]
00BC5612  89 05 C0 AF 32 00               mov dword ptr [rip + 0x32afc0], eax
00BC5618  8B 86 90 01 00 00               mov eax, dword ptr [rsi + 0x190]
00BC561E  8B D7                           mov edx, edi
00BC5620  48 8B CE                        mov rcx, rsi
00BC5623  89 05 8F AF 32 00               mov dword ptr [rip + 0x32af8f], eax
00BC5629  E8 26 BE 0B 00                  call 0x140c81454
00BC562E  8B D8                           mov ebx, eax
00BC5630  85 C0                           test eax, eax
00BC5632  0F 89 0A 06 00 00               jns 0x140bc5c42
00BC5638  E9 D9 01 00 00                  jmp 0x140bc5816
00BC563D  B8 9A 00 00 C0                  mov eax, 0xc000009a
00BC5642  E9 0E 06 00 00                  jmp 0x140bc5c55
00BC5647  E8 58 E4 8E FF                  call 0x1404b3aa4
00BC564C  48 8D 4E 20                     lea rcx, [rsi + 0x20]
00BC5650  E8 37 97 AD FF                  call 0x14069ed8c
00BC5655  8B D8                           mov ebx, eax
00BC5657  85 C0                           test eax, eax
00BC5659  79 0A                           jns 0x140bc5665
00BC565B  E8 1C DF 8E FF                  call 0x1404b357c
00BC5660  E9 B1 01 00 00                  jmp 0x140bc5816
00BC5665  48 8B 0D 94 AD 32 00            mov rcx, qword ptr [rip + 0x32ad94]
00BC566C  E8 8F 4E 67 FF                  call 0x14023a500
00BC5671  8B 0D 79 AD 32 00               mov ecx, dword ptr [rip + 0x32ad79]
00BC5677  48 89 05 B2 AD 32 00            mov qword ptr [rip + 0x32adb2], rax
00BC567E  8B 05 64 AD 32 00               mov eax, dword ptr [rip + 0x32ad64]
00BC5684  89 05 AE AD 32 00               mov dword ptr [rip + 0x32adae], eax
00BC568A  8B 05 54 AD 32 00               mov eax, dword ptr [rip + 0x32ad54]
00BC5690  89 05 A6 AD 32 00               mov dword ptr [rip + 0x32ada6], eax
00BC5696  8B 05 50 AD 32 00               mov eax, dword ptr [rip + 0x32ad50]
00BC569C  89 05 9E AD 32 00               mov dword ptr [rip + 0x32ad9e], eax
00BC56A2  83 E9 04                        sub ecx, 4
00BC56A5  74 1A                           je 0x140bc56c1
00BC56A7  83 F9 01                        cmp ecx, 1
00BC56AA  74 09                           je 0x140bc56b5
00BC56AC  44 89 2D 95 AD 32 00            mov dword ptr [rip + 0x32ad95], r13d
00BC56B3  EB 16                           jmp 0x140bc56cb
00BC56B5  C7 05 89 AD 32 00 04 00 00 00   mov dword ptr [rip + 0x32ad89], 4
00BC56BF  EB 0A                           jmp 0x140bc56cb
00BC56C1  C7 05 7D AD 32 00 03 00 00 00   mov dword ptr [rip + 0x32ad7d], 3
00BC56CB  0F 10 86 10 01 00 00            movups xmm0, xmmword ptr [rsi + 0x110]
00BC56D2  4C 8D 66 48                     lea r12, [rsi + 0x48]
00BC56D6  44 89 6C 24 70                  mov dword ptr [rsp + 0x70], r13d
00BC56DB  41 BF B0 01 00 00               mov r15d, 0x1b0
00BC56E1  41 8B DD                        mov ebx, r13d
00BC56E4  0F 11 05 45 AE 32 00            movups xmmword ptr [rip + 0x32ae45], xmm0
00BC56EB  41 8B C7                        mov eax, r15d
00BC56EE  45 8B C5                        mov r8d, r13d
00BC56F1  0F 10 8E 20 01 00 00            movups xmm1, xmmword ptr [rsi + 0x120]
00BC56F8  45 8B CD                        mov r9d, r13d
00BC56FB  41 BB 20 00 00 00               mov r11d, 0x20
00BC5701  41 BA F0 FF FF FF               mov r10d, 0xfffffff0
00BC5707  0F 11 0D 32 AE 32 00            movups xmmword ptr [rip + 0x32ae32], xmm1
00BC570E  0F 10 86 30 01 00 00            movups xmm0, xmmword ptr [rsi + 0x130]
00BC5715  0F 11 05 34 AE 32 00            movups xmmword ptr [rip + 0x32ae34], xmm0
00BC571C  0F 10 8E 40 01 00 00            movups xmm1, xmmword ptr [rsi + 0x140]
00BC5723  0F 11 0D 36 AE 32 00            movups xmmword ptr [rip + 0x32ae36], xmm1
00BC572A  0F 10 86 50 01 00 00            movups xmm0, xmmword ptr [rsi + 0x150]
00BC5731  0F 11 05 38 AE 32 00            movups xmmword ptr [rip + 0x32ae38], xmm0
00BC5738  0F 10 8E 60 01 00 00            movups xmm1, xmmword ptr [rsi + 0x160]
00BC573F  0F 11 0D 3A AE 32 00            movups xmmword ptr [rip + 0x32ae3a], xmm1
00BC5746  0F 10 86 70 01 00 00            movups xmm0, xmmword ptr [rsi + 0x170]
00BC574D  0F 11 05 3C AE 32 00            movups xmmword ptr [rip + 0x32ae3c], xmm0
00BC5754  0F 10 8E 80 01 00 00            movups xmm1, xmmword ptr [rsi + 0x180]
00BC575B  0F 11 0D 3E AE 32 00            movups xmmword ptr [rip + 0x32ae3e], xmm1
00BC5762  4D 39 2C 24                     cmp qword ptr [r12], r13
00BC5766  74 21                           je 0x140bc5789
00BC5768  8B 5E 50                        mov ebx, dword ptr [rsi + 0x50]
00BC576B  48 8D 4E 48                     lea rcx, [rsi + 0x48]
00BC576F  44 8B 4E 54                     mov r9d, dword ptr [rsi + 0x54]
00BC5773  83 C3 0F                        add ebx, 0xf
00BC5776  41 23 DA                        and ebx, r10d
00BC5779  44 89 5C 24 70                  mov dword ptr [rsp + 0x70], r11d
00BC577E  45 8B C3                        mov r8d, r11d
00BC5781  8D 83 D0 01 00 00               lea eax, [rbx + 0x1d0]
00BC5787  EB 03                           jmp 0x140bc578c
00BC5789  49 8B CC                        mov rcx, r12
00BC578C  41 8B D5                        mov edx, r13d
00BC578F  41 8B FD                        mov edi, r13d
00BC5792  89 94 24 80 00 00 00            mov dword ptr [rsp + 0x80], edx
00BC5799  4C 39 AE 80 00 00 00            cmp qword ptr [rsi + 0x80], r13
00BC57A0  74 1D                           je 0x140bc57bf
00BC57A2  8B BE 88 00 00 00               mov edi, dword ptr [rsi + 0x88]
00BC57A8  41 8B D3                        mov edx, r11d
00BC57AB  83 C7 0F                        add edi, 0xf
00BC57AE  89 94 24 80 00 00 00            mov dword ptr [rsp + 0x80], edx
00BC57B5  41 23 FA                        and edi, r10d
00BC57B8  03 C2                           add eax, edx
00BC57BA  03 C7                           add eax, edi
00BC57BC  4C 8B E1                        mov r12, rcx
00BC57BF  41 81 C1 70 40 00 00            add r9d, 0x4070
00BC57C6  41 03 C1                        add eax, r9d
00BC57C9  44 8B F0                        mov r14d, eax
00BC57CC  44 2B F3                        sub r14d, ebx
00BC57CF  44 2B F2                        sub r14d, edx
00BC57D2  44 2B F7                        sub r14d, edi
00BC57D5  45 2B F0                        sub r14d, r8d
00BC57D8  45 2B F7                        sub r14d, r15d
00BC57DB  45 8B EE                        mov r13d, r14d
00BC57DE  41 C1 ED 03                     shr r13d, 3
00BC57E2  41 83 C5 0F                     add r13d, 0xf
00BC57E6  45 23 EA                        and r13d, r10d
00BC57E9  41 03 C5                        add eax, r13d
00BC57EC  8B C8                           mov ecx, eax
00BC57EE  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
00BC57F5  E8 7A EB 81 FF                  call 0x1403e4374
00BC57FA  45 33 C0                        xor r8d, r8d
00BC57FD  48 89 05 7C AC 32 00            mov qword ptr [rip + 0x32ac7c], rax
00BC5804  4C 8B F8                        mov r15, rax
00BC5807  48 85 C0                        test rax, rax
00BC580A  75 14                           jne 0x140bc5820
00BC580C  E8 6B DD 8E FF                  call 0x1404b357c
00BC5811  BB 17 00 00 C0                  mov ebx, 0xc0000017
00BC5816  E8 5D BE FF FF                  call 0x140bc1678
00BC581B  E9 2C 04 00 00                  jmp 0x140bc5c4c
00BC5820  BA 03 00 00 00                  mov edx, 3
00BC5825  49 8B CF                        mov rcx, r15
00BC5828  48 8B C6                        mov rax, rsi
00BC582B  44 8D 4A 7D                     lea r9d, [rdx + 0x7d]
00BC582F  0F 10 00                        movups xmm0, xmmword ptr [rax]
00BC5832  0F 11 01                        movups xmmword ptr [rcx], xmm0
00BC5835  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00BC5839  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00BC583D  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
00BC5841  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00BC5845  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
00BC5849  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
00BC584D  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
00BC5851  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
00BC5855  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
00BC5859  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
00BC585D  0F 10 40 60                     movups xmm0, xmmword ptr [rax + 0x60]
00BC5861  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
00BC5865  49 03 C9                        add rcx, r9
00BC5868  0F 10 48 70                     movups xmm1, xmmword ptr [rax + 0x70]
00BC586C  49 03 C1                        add rax, r9
00BC586F  0F 11 49 F0                     movups xmmword ptr [rcx - 0x10], xmm1
00BC5873  48 83 EA 01                     sub rdx, 1
00BC5877  75 B6                           jne 0x140bc582f
00BC5879  0F 10 00                        movups xmm0, xmmword ptr [rax]
00BC587C  41 8B D6                        mov edx, r14d
00BC587F  0F 11 01                        movups xmmword ptr [rcx], xmm0
00BC5882  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00BC5886  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00BC588A  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
00BC588E  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
00BC5892  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
00BC5899  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
00BC589D  41 89 07                        mov dword ptr [r15], eax
00BC58A0  03 CB                           add ecx, ebx
00BC58A2  41 0F BA 6F 78 14               bts dword ptr [r15 + 0x78], 0x14
00BC58A8  4D 89 87 F0 00 00 00            mov qword ptr [r15 + 0xf0], r8
00BC58AF  45 89 87 F8 00 00 00            mov dword ptr [r15 + 0xf8], r8d
00BC58B6  4D 89 87 08 01 00 00            mov qword ptr [r15 + 0x108], r8
00BC58BD  4D 89 87 00 01 00 00            mov qword ptr [r15 + 0x100], r8
00BC58C4  44 8B 84 24 80 00 00 00         mov r8d, dword ptr [rsp + 0x80]
00BC58CC  41 81 C0 B0 01 00 00            add r8d, 0x1b0
00BC58D3  89 8C 24 88 00 00 00            mov dword ptr [rsp + 0x88], ecx
00BC58DA  44 03 C1                        add r8d, ecx
00BC58DD  41 8B CD                        mov ecx, r13d
00BC58E0  44 03 C7                        add r8d, edi
00BC58E3  4D 03 C7                        add r8, r15
00BC58E6  49 03 C8                        add rcx, r8
00BC58E9  E8 46 BD FF FF                  call 0x140bc1634
00BC58EE  45 33 ED                        xor r13d, r13d
00BC58F1  4C 89 2D 08 AC 32 00            mov qword ptr [rip + 0x32ac08], r13
00BC58F8  85 DB                           test ebx, ebx
00BC58FA  74 64                           je 0x140bc5960
00BC58FC  8B 5C 24 70                     mov ebx, dword ptr [rsp + 0x70]
00BC5900  4D 8D B7 B0 01 00 00            lea r14, [r15 + 0x1b0]
00BC5907  44 8B 46 50                     mov r8d, dword ptr [rsi + 0x50]
00BC590B  49 03 DE                        add rbx, r14
00BC590E  49 8B 14 24                     mov rdx, qword ptr [r12]
00BC5912  48 8B CB                        mov rcx, rbx
00BC5915  E8 26 0F B0 FF                  call 0x1406c6840
00BC591A  41 C7 46 0C 01 00 00 00         mov dword ptr [r14 + 0xc], 1
00BC5922  41 8D 55 01                     lea edx, [r13 + 1]
00BC5926  49 89 1E                        mov qword ptr [r14], rbx
00BC5929  49 8B CE                        mov rcx, r14
00BC592C  8B 46 50                        mov eax, dword ptr [rsi + 0x50]
00BC592F  41 89 46 08                     mov dword ptr [r14 + 8], eax
00BC5933  49 89 5E 10                     mov qword ptr [r14 + 0x10], rbx
00BC5937  0F BA 2D 11 AB 32 00 0B         bts dword ptr [rip + 0x32ab11], 0xb
00BC593F  E8 6C AD 0B 00                  call 0x140c806b0
00BC5944  0F BA 35 04 AB 32 00 0B         btr dword ptr [rip + 0x32ab04], 0xb
00BC594C  85 C0                           test eax, eax
00BC594E  78 07                           js 0x140bc5957
00BC5950  4C 89 35 A9 AB 32 00            mov qword ptr [rip + 0x32aba9], r14
00BC5957  4C 39 2D A2 AB 32 00            cmp qword ptr [rip + 0x32aba2], r13
00BC595E  75 11                           jne 0x140bc5971
00BC5960  33 D2                           xor edx, edx
00BC5962  4C 8D 05 F7 03 00 00            lea r8, [rip + 0x3f7]
00BC5969  8D 4A 65                        lea ecx, [rdx + 0x65]
00BC596C  E8 1F 39 79 FF                  call 0x140359290
00BC5971  4C 89 2D 90 AB 32 00            mov qword ptr [rip + 0x32ab90], r13
00BC5978  85 FF                           test edi, edi
00BC597A  74 4E                           je 0x140bc59ca
00BC597C  8B BC 24 88 00 00 00            mov edi, dword ptr [rsp + 0x88]
00BC5983  8B 9C 24 80 00 00 00            mov ebx, dword ptr [rsp + 0x80]
00BC598A  81 C7 B0 01 00 00               add edi, 0x1b0
00BC5990  44 8B 86 88 00 00 00            mov r8d, dword ptr [rsi + 0x88]
00BC5997  49 03 FF                        add rdi, r15
00BC599A  48 8B 96 80 00 00 00            mov rdx, qword ptr [rsi + 0x80]
00BC59A1  48 03 DF                        add rbx, rdi
00BC59A4  48 8B CB                        mov rcx, rbx
00BC59A7  E8 94 0E B0 FF                  call 0x1406c6840
00BC59AC  C7 47 0C 01 00 00 00            mov dword ptr [rdi + 0xc], 1
00BC59B3  48 89 1F                        mov qword ptr [rdi], rbx
00BC59B6  8B 86 88 00 00 00               mov eax, dword ptr [rsi + 0x88]
00BC59BC  89 47 08                        mov dword ptr [rdi + 8], eax
00BC59BF  48 89 5F 10                     mov qword ptr [rdi + 0x10], rbx
00BC59C3  48 89 3D 3E AB 32 00            mov qword ptr [rip + 0x32ab3e], rdi
00BC59CA  33 D2                           xor edx, edx
00BC59CC  48 8D 0D C5 AA 32 00            lea rcx, [rip + 0x32aac5]
00BC59D3  44 8D 42 58                     lea r8d, [rdx + 0x58]
00BC59D7  E8 64 12 B0 FF                  call 0x1406c6c40
00BC59DC  4C 39 AE 90 00 00 00            cmp qword ptr [rsi + 0x90], r13
00BC59E3  74 47                           je 0x140bc5a2c
00BC59E5  8B 8E A0 00 00 00               mov ecx, dword ptr [rsi + 0xa0]
00BC59EB  E8 84 E9 81 FF                  call 0x1403e4374
00BC59F0  48 89 05 A1 AA 32 00            mov qword ptr [rip + 0x32aaa1], rax
00BC59F7  48 85 C0                        test rax, rax
00BC59FA  74 30                           je 0x140bc5a2c
00BC59FC  44 8B 86 A0 00 00 00            mov r8d, dword ptr [rsi + 0xa0]
00BC5A03  48 8B C8                        mov rcx, rax
00BC5A06  48 8B 96 90 00 00 00            mov rdx, qword ptr [rsi + 0x90]
00BC5A0D  E8 2E 0E B0 FF                  call 0x1406c6840
00BC5A12  8B 86 A0 00 00 00               mov eax, dword ptr [rsi + 0xa0]
00BC5A18  89 05 8A AA 32 00               mov dword ptr [rip + 0x32aa8a], eax
00BC5A1E  48 8B 86 A4 00 00 00            mov rax, qword ptr [rsi + 0xa4]
00BC5A25  48 89 05 80 AA 32 00            mov qword ptr [rip + 0x32aa80], rax
00BC5A2C  48 8B 8E B8 00 00 00            mov rcx, qword ptr [rsi + 0xb8]
00BC5A33  48 85 C9                        test rcx, rcx
00BC5A36  74 17                           je 0x140bc5a4f
00BC5A38  48 8D 15 99 AA 32 00            lea rdx, [rip + 0x32aa99]
00BC5A3F  E8 00 98 AD FF                  call 0x14069f244
00BC5A44  85 C0                           test eax, eax
00BC5A46  79 07                           jns 0x140bc5a4f
00BC5A48  4C 89 2D 89 AA 32 00            mov qword ptr [rip + 0x32aa89], r13
00BC5A4F  48 8B 86 D8 00 00 00            mov rax, qword ptr [rsi + 0xd8]
00BC5A56  48 85 C0                        test rax, rax
00BC5A59  74 4B                           je 0x140bc5aa6
00BC5A5B  48 83 CB FF                     or rbx, 0xffffffffffffffff
00BC5A5F  48 8B CB                        mov rcx, rbx
00BC5A62  48 FF C1                        inc rcx
00BC5A65  66 44 39 2C 48                  cmp word ptr [rax + rcx*2], r13w
00BC5A6A  75 F6                           jne 0x140bc5a62
00BC5A6C  48 8D 0C 4D 02 00 00 00         lea rcx, [rcx*2 + 2]
00BC5A74  E8 FB E8 81 FF                  call 0x1403e4374
00BC5A79  48 89 05 60 AA 32 00            mov qword ptr [rip + 0x32aa60], rax
00BC5A80  48 85 C0                        test rax, rax
00BC5A83  74 21                           je 0x140bc5aa6
00BC5A85  4C 8B 86 D8 00 00 00            mov r8, qword ptr [rsi + 0xd8]
00BC5A8C  48 FF C3                        inc rbx
00BC5A8F  66 45 39 2C 58                  cmp word ptr [r8 + rbx*2], r13w
00BC5A94  75 F6                           jne 0x140bc5a8c
00BC5A96  48 8B 0D 43 AA 32 00            mov rcx, qword ptr [rip + 0x32aa43]
00BC5A9D  48 8D 53 01                     lea rdx, [rbx + 1]
00BC5AA1  E8 0A 0A 94 FF                  call 0x1405064b0
00BC5AA6  4C 89 2D 4B AA 32 00            mov qword ptr [rip + 0x32aa4b], r13
00BC5AAD  4C 39 6E 58                     cmp qword ptr [rsi + 0x58], r13
00BC5AB1  74 6F                           je 0x140bc5b22
00BC5AB3  8B 4E 60                        mov ecx, dword ptr [rsi + 0x60]
00BC5AB6  E8 B9 E8 81 FF                  call 0x1403e4374
00BC5ABB  48 8B F8                        mov rdi, rax
00BC5ABE  48 85 C0                        test rax, rax
00BC5AC1  74 5F                           je 0x140bc5b22
00BC5AC3  44 8B 46 60                     mov r8d, dword ptr [rsi + 0x60]
00BC5AC7  48 8B C8                        mov rcx, rax
00BC5ACA  48 8B 56 58                     mov rdx, qword ptr [rsi + 0x58]
00BC5ACE  E8 6D 0D B0 FF                  call 0x1406c6840
00BC5AD3  B9 18 00 00 00                  mov ecx, 0x18
00BC5AD8  E8 97 E8 81 FF                  call 0x1403e4374
00BC5ADD  48 8B D8                        mov rbx, rax
00BC5AE0  48 85 C0                        test rax, rax
00BC5AE3  75 05                           jne 0x140bc5aea
00BC5AE5  48 8B CF                        mov rcx, rdi
00BC5AE8  EB 33                           jmp 0x140bc5b1d
00BC5AEA  44 89 68 0C                     mov dword ptr [rax + 0xc], r13d
00BC5AEE  33 D2                           xor edx, edx
00BC5AF0  48 89 38                        mov qword ptr [rax], rdi
00BC5AF3  48 8B CB                        mov rcx, rbx
00BC5AF6  8B 46 60                        mov eax, dword ptr [rsi + 0x60]
00BC5AF9  89 43 08                        mov dword ptr [rbx + 8], eax
00BC5AFC  48 89 7B 10                     mov qword ptr [rbx + 0x10], rdi
00BC5B00  E8 AB AB 0B 00                  call 0x140c806b0
00BC5B05  85 C0                           test eax, eax
00BC5B07  78 09                           js 0x140bc5b12
00BC5B09  48 89 1D E8 A9 32 00            mov qword ptr [rip + 0x32a9e8], rbx
00BC5B10  EB 10                           jmp 0x140bc5b22
00BC5B12  48 8B CF                        mov rcx, rdi
00BC5B15  E8 C6 CA 81 FF                  call 0x1403e25e0
00BC5B1A  48 8B CB                        mov rcx, rbx
00BC5B1D  E8 BE CA 81 FF                  call 0x1403e25e0
00BC5B22  83 7E 74 03                     cmp dword ptr [rsi + 0x74], 3
00BC5B26  72 1C                           jb 0x140bc5b44
00BC5B28  F2 0F 10 86 94 01 00 00         movsd xmm0, qword ptr [rsi + 0x194]
00BC5B30  F2 0F 11 05 98 AA 32 00         movsd qword ptr [rip + 0x32aa98], xmm0
00BC5B38  8B 86 9C 01 00 00               mov eax, dword ptr [rsi + 0x19c]
00BC5B3E  89 05 94 AA 32 00               mov dword ptr [rip + 0x32aa94], eax
00BC5B44  8B 86 90 01 00 00               mov eax, dword ptr [rsi + 0x190]
00BC5B4A  89 05 68 AA 32 00               mov dword ptr [rip + 0x32aa68], eax
00BC5B50  83 7E 74 05                     cmp dword ptr [rsi + 0x74], 5
00BC5B54  72 0C                           jb 0x140bc5b62
00BC5B56  8B 86 A0 01 00 00               mov eax, dword ptr [rsi + 0x1a0]
00BC5B5C  89 05 7A AA 32 00               mov dword ptr [rip + 0x32aa7a], eax
00BC5B62  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
00BC5B66  48 8B CE                        mov rcx, rsi
00BC5B69  0F BA 2D DF A8 32 00 0F         bts dword ptr [rip + 0x32a8df], 0xf
00BC5B71  E8 DE B8 0B 00                  call 0x140c81454
00BC5B76  8B 05 D4 A8 32 00               mov eax, dword ptr [rip + 0x32a8d4]
00BC5B7C  B9 48 00 00 00                  mov ecx, 0x48
00BC5B81  0F BA F0 0F                     btr eax, 0xf
00BC5B85  0F BA E8 0B                     bts eax, 0xb
00BC5B89  89 05 C1 A8 32 00               mov dword ptr [rip + 0x32a8c1], eax
00BC5B8F  E8 E0 E7 81 FF                  call 0x1403e4374
00BC5B94  0F BA 35 B4 A8 32 00 0B         btr dword ptr [rip + 0x32a8b4], 0xb
00BC5B9C  48 8B C8                        mov rcx, rax
00BC5B9F  48 85 C0                        test rax, rax
00BC5BA2  74 52                           je 0x140bc5bf6
00BC5BA4  48 8B 86 00 01 00 00            mov rax, qword ptr [rsi + 0x100]
00BC5BAB  48 85 C0                        test rax, rax
00BC5BAE  74 1F                           je 0x140bc5bcf
00BC5BB0  0F 10 00                        movups xmm0, xmmword ptr [rax]
00BC5BB3  0F 11 01                        movups xmmword ptr [rcx], xmm0
00BC5BB6  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00BC5BBA  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00BC5BBE  8B 40 20                        mov eax, dword ptr [rax + 0x20]
00BC5BC1  89 41 20                        mov dword ptr [rcx + 0x20], eax
00BC5BC4  49 89 8F 00 01 00 00            mov qword ptr [r15 + 0x100], rcx
00BC5BCB  48 83 C1 24                     add rcx, 0x24
00BC5BCF  48 8B 86 08 01 00 00            mov rax, qword ptr [rsi + 0x108]
00BC5BD6  48 85 C0                        test rax, rax
00BC5BD9  74 1B                           je 0x140bc5bf6
00BC5BDB  0F 10 00                        movups xmm0, xmmword ptr [rax]
00BC5BDE  0F 11 01                        movups xmmword ptr [rcx], xmm0
00BC5BE1  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00BC5BE5  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00BC5BE9  8B 40 20                        mov eax, dword ptr [rax + 0x20]
00BC5BEC  89 41 20                        mov dword ptr [rcx + 0x20], eax
00BC5BEF  49 89 8F 08 01 00 00            mov qword ptr [r15 + 0x108], rcx
00BC5BF6  48 8B 8E 00 01 00 00            mov rcx, qword ptr [rsi + 0x100]
00BC5BFD  E8 C2 BC FF FF                  call 0x140bc18c4
00BC5C02  48 89 05 0F A9 32 00            mov qword ptr [rip + 0x32a90f], rax
00BC5C09  48 8B 8E 08 01 00 00            mov rcx, qword ptr [rsi + 0x108]
00BC5C10  E8 E7 C0 FF FF                  call 0x140bc1cfc
00BC5C15  48 89 05 F4 A8 32 00            mov qword ptr [rip + 0x32a8f4], rax
00BC5C1C  0F BA ED 07                     bts ebp, 7
00BC5C20  8B 46 7C                        mov eax, dword ptr [rsi + 0x7c]
00BC5C23  09 2D 27 A8 32 00               or dword ptr [rip + 0x32a827], ebp
00BC5C29  89 05 25 A8 32 00               mov dword ptr [rip + 0x32a825], eax
00BC5C2F  E8 48 D9 8E FF                  call 0x1404b357c
00BC5C34  48 8B 86 E8 00 00 00            mov rax, qword ptr [rsi + 0xe8]
00BC5C3B  48 89 05 AE A8 32 00            mov qword ptr [rip + 0x32a8ae], rax
00BC5C42  83 0D 07 A8 32 00 01            or dword ptr [rip + 0x32a807], 1
00BC5C49  41 8B DD                        mov ebx, r13d
00BC5C4C  8B C3                           mov eax, ebx
00BC5C4E  EB 05                           jmp 0x140bc5c55
00BC5C50  B8 0D 00 00 C0                  mov eax, 0xc000000d
00BC5C55  48 83 C4 28                     add rsp, 0x28
00BC5C59  41 5F                           pop r15
00BC5C5B  41 5E                           pop r14
00BC5C5D  41 5D                           pop r13
00BC5C5F  41 5C                           pop r12
00BC5C61  5F                              pop rdi
00BC5C62  5E                              pop rsi
00BC5C63  5D                              pop rbp
00BC5C64  5B                              pop rbx
00BC5C65  C3                              ret
00BC5C66  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgpFwLibraryInitialize(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (40);
    v_r13 = 0;
    if (a1 == 0) goto loc_00BC5C50;
    if ((*(unsigned int *)(a1 + 116)) >= 5) goto loc_00BC5435;
    goto loc_00BC5C55;
loc_00BC5435:
    v_rbp = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 120))) & (0x16FF0000ULL));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3321874)))) & (1)) == 0) goto loc_00BC5456;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3321874)))) & (4)) != 0) goto loc_00BC5456;
    if (condition_is_above_or_equal) goto loc_00BC5C50;
loc_00BC5456:
    if (condition_is_above_or_equal) goto loc_00BC5529;
    result = BgpFwAcquireLock(a1, a2, a3, a4);
    v_rdi = (unsigned int)((v_rdi) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(a2))) != ((unsigned int)(v_rdi))) goto loc_00BC5512;
    a1 = 0;
    *(unsigned __int64 *)(v_rip + 3321726) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3321818))) & (0xFFFFFFFDULL));
    result = (unsigned int)((result) | (0x101800ULL));
    *(unsigned int *)(v_rip + 3321788) = (unsigned int)(result);
    *(unsigned __int64 *)(v_rip + 3321669) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 3321678) = v_xmm0;
    result = BgpFwLibraryEnable(a1 + 32, a2, a3, a4);
    if (sign_flag) goto loc_00BC5C55;
    if (*(unsigned __int64 *)(a1 + 16) != 0) goto loc_00BC54D0;
    *(unsigned __int64 *)(v_rip + 3321937) = 0;
    *(unsigned __int64 *)(v_rip + 3321922) = 0;
    goto loc_00BC550B;
loc_00BC54D0:
    a1 = 0;
    result = BgpFwReservePoolSwap(a1, *(unsigned __int64 *)(a1 + 240), (unsigned int)(*(unsigned int *)(a1 + 248)), *(unsigned __int64 *)(a1 + 16));
    result = ResFwConfigureDisplayStringResources(*(unsigned __int64 *)(a1 + 256), *(unsigned __int64 *)(a1 + 240), (unsigned int)(*(unsigned int *)(a1 + 248)), *(unsigned __int64 *)(a1 + 16));
    *(unsigned __int64 *)(v_rip + 3321888) = result;
    result = AnFwConfigureProgressResources(*(unsigned __int64 *)(a1 + 264), *(unsigned __int64 *)(a1 + 240), (unsigned int)(*(unsigned int *)(a1 + 248)), *(unsigned __int64 *)(a1 + 16));
    *(unsigned __int64 *)(v_rip + 3321861) = result;
loc_00BC550B:
    result = LogFwInitialize(*(unsigned __int64 *)(a1 + 264), *(unsigned __int64 *)(a1 + 240), (unsigned int)(*(unsigned int *)(a1 + 248)), *(unsigned __int64 *)(a1 + 16));
    goto loc_00BC551F;
loc_00BC5512:
    result = AnFwProgressIndicatorTransition(*(unsigned __int64 *)(a1 + 264), *(unsigned __int64 *)(a1 + 240), (unsigned int)(*(unsigned int *)(a1 + 248)), *(unsigned __int64 *)(a1 + 16));
loc_00BC551F:
    result = BgpFwReleaseLock(*(unsigned __int64 *)(a1 + 264), *(unsigned __int64 *)(a1 + 240), (unsigned int)(*(unsigned int *)(a1 + 248)), *(unsigned __int64 *)(a1 + 16));
    goto loc_00BC5C42;
loc_00BC5529:
    v_rdi = (unsigned int)((v_rdi) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(a2))) != ((unsigned int)(v_rdi))) goto loc_00BC5647;
    result = BgpFwInitializeLock(*(unsigned __int64 *)(a1 + 264), *(unsigned __int64 *)(a1 + 240), (unsigned int)(*(unsigned int *)(a1 + 248)), *(unsigned __int64 *)(a1 + 16));
    result = (unsigned int)((result) | (0xC04ULL));
    *(unsigned int *)(v_rip + 3321612) = (unsigned int)(result);
    *(unsigned __int64 *)(v_rip + 3321814) = v_rip + 3321813;
    *(unsigned __int64 *)(v_rip + 3321799) = v_rip + 3321813;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 264) + 240) == 0) goto loc_00BC563D;
    if ((*(unsigned int *)(a1 + 248)) == 0) goto loc_00BC563D;
    result = BgpFwInitializeReservePool(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 264) + 240), (unsigned int)(0x4000ULL), v_rip + 2748883, *(unsigned __int64 *)(a1 + 16));
    result = BgpFwLibraryEnable(a1 + 32, (unsigned int)(0x4000ULL), v_rip + 2748883, *(unsigned __int64 *)(a1 + 16));
    if (sign_flag) goto loc_00BC5816;
    *(unsigned __int64 *)(v_rip + 3321570) = v_xmm0;
    if ((*(unsigned __int64 *)(a1 + 88)) == 0) goto loc_00BC55F6;
    result = BgpFwAllocateMemory(24, (unsigned int)(0x4000ULL), v_rip + 2748883, *(unsigned __int64 *)(a1 + 16));
    if (result == 0) goto loc_00BC5811;
    a2 = 0;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(a1 + 88);
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96)));
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(a1 + 88);
    *(unsigned int *)(result + 12) = 1;
    *(unsigned __int64 *)(v_rip + 3321617) = result;
    result = BgpFoInitialize(result, a2, v_rip + 2748883, *(unsigned __int64 *)(a1 + 16));
    if (sign_flag) goto loc_00BC5816;
loc_00BC55F6:
    if ((*(unsigned int *)(a1 + 116)) >= 3) {
        *(unsigned __int64 *)(v_rip + 3321796) = v_xmm0;
        result = *(unsigned int *)(a1 + 412);
        *(unsigned int *)(v_rip + 3321792) = (unsigned int)(result);
    }
    *(unsigned int *)(v_rip + 3321743) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 400)));
    result = BgpBcInitializeCriticalMode(0, (unsigned int)((unsigned int)(v_rdi)), v_rip + 2748883, *(unsigned __int64 *)(a1 + 16));
    if (!sign_flag) goto loc_00BC5C42;
    goto loc_00BC5816;
loc_00BC563D:
    goto loc_00BC5C55;
loc_00BC5647:
    result = BgpFwAcquireLock(0, (unsigned int)((unsigned int)(v_rdi)), v_rip + 2748883, *(unsigned __int64 *)(a1 + 16));
    result = BgpFwLibraryEnable(a1 + 32, (unsigned int)((unsigned int)(v_rdi)), v_rip + 2748883, *(unsigned __int64 *)(a1 + 16));
    if (!sign_flag) goto loc_00BC5665;
    result = BgpFwReleaseLock(a1 + 32, (unsigned int)((unsigned int)(v_rdi)), v_rip + 2748883, *(unsigned __int64 *)(a1 + 16));
    goto loc_00BC5816;
loc_00BC5665:
    result = MmGetPhysicalAddress(*(unsigned __int64 *)(v_rip + 3321236), (unsigned int)((unsigned int)(v_rdi)), v_rip + 2748883, *(unsigned __int64 *)(a1 + 16));
    *(unsigned __int64 *)(v_rip + 3321266) = result;
    *(unsigned int *)(v_rip + 3321262) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3321188)));
    *(unsigned int *)(v_rip + 3321254) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3321172)));
    *(unsigned int *)(v_rip + 3321246) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3321168)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3321209))) - (4));
    if (condition_is_equal) goto loc_00BC56C1;
    if (((unsigned int)(a1)) == 1) goto loc_00BC56B5;
    *(unsigned int *)(v_rip + 3321237) = 0;
    goto loc_00BC56CB;
loc_00BC56B5:
    *(unsigned int *)(v_rip + 3321225) = 4;
    goto loc_00BC56CB;
loc_00BC56C1:
    *(unsigned int *)(v_rip + 3321213) = 3;
loc_00BC56CB:
    v_stack_p8 = 0;
    *(unsigned __int64 *)(v_rip + 3321413) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 3321394) = v_xmm1;
    *(unsigned __int64 *)(v_rip + 3321396) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 3321398) = v_xmm1;
    *(unsigned __int64 *)(v_rip + 3321400) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 3321402) = v_xmm1;
    *(unsigned __int64 *)(v_rip + 3321404) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 3321406) = v_xmm1;
    if ((*(unsigned __int64 *)(a1 + 72)) == 0) goto loc_00BC5789;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 80))) + (15));
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)((unsigned int)(0xFFFFFFF0ULL))));
    v_stack_p8 = 32;
    goto loc_00BC578C;
loc_00BC5789:
loc_00BC578C:
    v_stack_p18 = 0;
    result = v_rbx + 464;
    v_rdi = 0;
    v_r12 = a1 + 72;
    if ((*(unsigned __int64 *)(a1 + 128)) != 0) {
        v_rdi = *(unsigned int *)(a1 + 136);
        a2 = 32;
        v_rdi = (unsigned int)((v_rdi) + (15));
        v_stack_p18 = a2;
        v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0xFFFFFFF0ULL))));
        result = (unsigned int)((v_rbx + 464) + (a2));
        result = (unsigned int)((result) + ((unsigned int)(v_rdi)));
        v_r12 = a1 + 72;
    }
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 84))) + (0x4070ULL));
    result = (unsigned int)((result) + ((unsigned int)(a4)));
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(result))) - ((unsigned int)(v_rbx)));
    v_r14 = (unsigned int)((v_r14) - (a2));
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)(v_rdi)));
    v_r14 = (unsigned int)((v_r14) - (32));
    v_r14 = (unsigned int)((v_r14) - (432));
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> (3));
    v_r13 = (unsigned int)((v_r13) + (15));
    v_r13 = (unsigned int)((v_r13) & ((unsigned int)((unsigned int)(0xFFFFFFF0ULL))));
    result = (unsigned int)((result) + ((unsigned int)(v_r13)));
    v_stack_p20 = (unsigned int)(result);
    result = BgpFwAllocateMemory((unsigned int)((unsigned int)(result)), a2, 32, a4);
    a3 = 0;
    *(unsigned __int64 *)(v_rip + 3320956) = result;
    if (result != 0) goto loc_00BC5820;
    result = BgpFwReleaseLock((unsigned int)((unsigned int)(result)), a2, a3, a4);
loc_00BC5811:
loc_00BC5816:
    result = BgpFwLibraryDestroy((unsigned int)((unsigned int)(result)), a2, a3, a4);
    goto loc_00BC5C4C;
loc_00BC5820:
loc_00BC582F:
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    *(unsigned __int64 *)(result + 64) = v_xmm0;
    *(unsigned __int64 *)(result + 80) = v_xmm1;
    *(unsigned __int64 *)(result + 96) = v_xmm0;
    a1 = (result) + (3 + 125);
    result = (a1) + (3 + 125);
    *(unsigned __int64 *)(a1 - 16) = v_xmm1;
    a2 = (3) - (1);
    if (condition_is_not_equal) goto loc_00BC582F;
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    *(unsigned __int64 *)(a1 + 32) = *(unsigned __int64 *)(result + 32);
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(v_stack_p20));
    a1 = (unsigned int)(((unsigned int)(v_stack_p8)) + ((unsigned int)((unsigned int)(0xC0000017ULL))));
    *(unsigned __int64 *)(result + 240) = 0;
    *(unsigned int *)(result + 248) = 0;
    *(unsigned __int64 *)(result + 264) = 0;
    *(unsigned __int64 *)(result + 256) = 0;
    a3 = (unsigned int)(((unsigned int)(v_stack_p18)) + (432));
    v_stack_p20 = (unsigned int)(a1);
    a3 = (unsigned int)((a3) + ((unsigned int)(a1)));
    a3 = (unsigned int)((a3) + ((unsigned int)(v_rdi)));
    a3 = (a3) + (result);
    a1 = ((unsigned int)((unsigned int)(v_r13))) + (a3);
    result = BgpFwInitializeReservePool(a1, (unsigned int)((unsigned int)(v_r14)), a3, 3 + 125);
    v_r13 = 0;
    *(unsigned __int64 *)(v_rip + 3320840) = 0;
    if ((unsigned int)((unsigned int)(0xC0000017ULL)) == 0) goto loc_00BC5960;
    v_rbx = ((unsigned int)(v_stack_p8)) + (result + 432);
    result = memcpy(v_rbx, *(unsigned __int64 *)(v_r12), (unsigned int)(*(unsigned int *)(a1 + 80)), 3 + 125);
    *(unsigned int *)(result + 432 + 12) = 1;
    *(unsigned __int64 *)(result + 432) = v_rbx;
    *(unsigned int *)(result + 432 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 80)));
    *(unsigned __int64 *)(result + 432 + 16) = v_rbx;
    result = BgpFoInitialize(result + 432, v_r13 + 1, (unsigned int)(*(unsigned int *)(a1 + 80)), 3 + 125);
    if (!(sign_flag)) {
        *(unsigned __int64 *)(v_rip + 3320745) = result + 432;
    }
    if ((*(unsigned __int64 *)(v_rip + 3320738)) == 0) {
        a2 = 0;
        a3 = v_rip + 1015;
        a1 = a2 + 101;
        result = DbgPrintEx(a1, a2, a3, 3 + 125);
    }
    *(unsigned __int64 *)(v_rip + 3320720) = 0;
    if ((unsigned int)(v_rdi) != 0) {
        v_rdi = v_stack_p20;
        v_rbx = v_stack_p18;
        v_rdi = (unsigned int)((v_rdi) + (432));
        a3 = *(unsigned int *)(a1 + 136);
        v_rdi = (v_rdi) + (result);
        a2 = *(unsigned __int64 *)(a1 + 128);
        v_rbx = (v_rbx) + (v_rdi);
        a1 = v_rbx;
        result = memcpy(a1, a2, a3, 3 + 125);
        *(unsigned int *)(v_rdi + 12) = 1;
        *(unsigned __int64 *)(v_rdi) = v_rbx;
        result = *(unsigned int *)(a1 + 136);
        *(unsigned int *)(v_rdi + 8) = (unsigned int)(result);
        *(unsigned __int64 *)(v_rdi + 16) = v_rbx;
        *(unsigned __int64 *)(v_rip + 3320638) = v_rdi;
    }
    a2 = 0;
    result = memset(v_rip + 3320517, a2, a2 + 88, 3 + 125);
    if ((*(unsigned __int64 *)(a1 + 144)) == 0) goto loc_00BC5A2C;
    result = BgpFwAllocateMemory((unsigned int)(*(unsigned int *)(a1 + 160)), a2, a2 + 88, 3 + 125);
    *(unsigned __int64 *)(v_rip + 3320481) = result;
    if (result != 0) {
        a3 = *(unsigned int *)(a1 + 160);
        a1 = result;
        a2 = *(unsigned __int64 *)(a1 + 144);
        result = memcpy(a1, a2, a3, 3 + 125);
        result = *(unsigned int *)(a1 + 160);
        *(unsigned int *)(v_rip + 3320458) = (unsigned int)(result);
        result = *(unsigned __int64 *)(a1 + 164);
        *(unsigned __int64 *)(v_rip + 3320448) = result;
    }
    if (*(unsigned __int64 *)(a1 + 184) == 0) goto loc_00BC5A4F;
    result = BgpGxProcessQrCodeBitmap(*(unsigned __int64 *)(a1 + 184), v_rip + 3320473, a3, 3 + 125);
    if (sign_flag) {
        *(unsigned __int64 *)(v_rip + 3320457) = 0;
    }
    if (*(unsigned __int64 *)(a1 + 216) == 0) goto loc_00BC5AA6;
    v_rbx = (v_rbx) | (-1);
loc_00BC5A62:
    a1 = (v_rbx) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 216) + a1 * 2)) != 0) goto loc_00BC5A62;
    result = BgpFwAllocateMemory(a1 * 2 + 2, v_rip + 3320473, a3, 3 + 125);
    *(unsigned __int64 *)(v_rip + 3320416) = result;
    if (result == 0) goto loc_00BC5AA6;
loc_00BC5A8C:
    v_rbx = (v_rbx) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 216) + v_rbx * 2)) != 0) goto loc_00BC5A8C;
    result = wcscpy_s(*(unsigned __int64 *)(v_rip + 3320387), v_rbx + 1, *(unsigned __int64 *)(a1 + 216), 3 + 125);
loc_00BC5AA6:
    *(unsigned __int64 *)(v_rip + 3320395) = 0;
    if ((*(unsigned __int64 *)(a1 + 88)) == 0) goto loc_00BC5B22;
    result = BgpFwAllocateMemory((unsigned int)(*(unsigned int *)(a1 + 96)), v_rbx + 1, *(unsigned __int64 *)(a1 + 216), 3 + 125);
    if (result == 0) goto loc_00BC5B22;
    result = memcpy(result, *(unsigned __int64 *)(a1 + 88), (unsigned int)(*(unsigned int *)(a1 + 96)), 3 + 125);
    result = BgpFwAllocateMemory(24, *(unsigned __int64 *)(a1 + 88), (unsigned int)(*(unsigned int *)(a1 + 96)), 3 + 125);
    if (result != 0) goto loc_00BC5AEA;
    goto loc_00BC5B1D;
loc_00BC5AEA:
    *(unsigned int *)(result + 12) = 0;
    a2 = 0;
    *(unsigned __int64 *)(result) = result;
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96)));
    *(unsigned __int64 *)(result + 16) = result;
    result = BgpFoInitialize(result, a2, (unsigned int)(*(unsigned int *)(a1 + 96)), 3 + 125);
    if (sign_flag) goto loc_00BC5B12;
    *(unsigned __int64 *)(v_rip + 3320296) = result;
    goto loc_00BC5B22;
loc_00BC5B12:
    result = BgpFwFreeMemory(result, a2, (unsigned int)(*(unsigned int *)(a1 + 96)), 3 + 125);
loc_00BC5B1D:
    result = BgpFwFreeMemory(result, a2, (unsigned int)(*(unsigned int *)(a1 + 96)), 3 + 125);
loc_00BC5B22:
    if ((*(unsigned int *)(a1 + 116)) >= 3) {
        *(unsigned __int64 *)(v_rip + 3320472) = v_xmm0;
        result = *(unsigned int *)(a1 + 412);
        *(unsigned int *)(v_rip + 3320468) = (unsigned int)(result);
    }
    *(unsigned int *)(v_rip + 3320424) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 400)));
    result = (unsigned int)(*(unsigned int *)(a1 + 400));
    if ((*(unsigned int *)(a1 + 116)) >= 5) {
        result = *(unsigned int *)(a1 + 416);
        *(unsigned int *)(v_rip + 3320442) = (unsigned int)(result);
    }
    result = BgpBcInitializeCriticalMode(a1, (unsigned int)(v_stack_p10), (unsigned int)(*(unsigned int *)(a1 + 96)), 3 + 125);
    *(unsigned int *)(v_rip + 3320001) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3320020)));
    result = BgpFwAllocateMemory(72, (unsigned int)(v_stack_p10), (unsigned int)(*(unsigned int *)(a1 + 96)), 3 + 125);
    if (result == 0) goto loc_00BC5BF6;
    result = *(unsigned __int64 *)(a1 + 256);
    if (*(unsigned __int64 *)(a1 + 256) != 0) {
        *(unsigned __int64 *)(result) = v_xmm0;
        *(unsigned __int64 *)(result + 16) = v_xmm1;
        result = *(unsigned int *)(*(unsigned __int64 *)(a1 + 256) + 32);
        *(unsigned int *)(result + 32) = (unsigned int)(result);
        *(unsigned __int64 *)(result + 256) = result;
        a1 = (result) + (36);
    }
    result = *(unsigned __int64 *)(a1 + 264);
    if (*(unsigned __int64 *)(a1 + 264) != 0) {
        *(unsigned __int64 *)(a1) = v_xmm0;
        *(unsigned __int64 *)(a1 + 16) = v_xmm1;
        result = *(unsigned int *)(*(unsigned __int64 *)(a1 + 264) + 32);
        *(unsigned int *)(a1 + 32) = (unsigned int)(result);
        *(unsigned __int64 *)(result + 264) = a1;
    }
    result = ResFwConfigureDisplayStringResources(*(unsigned __int64 *)(a1 + 256), (unsigned int)(v_stack_p10), (unsigned int)(*(unsigned int *)(a1 + 96)), 3 + 125);
    *(unsigned __int64 *)(v_rip + 3320079) = result;
    result = AnFwConfigureProgressResources(*(unsigned __int64 *)(a1 + 264), (unsigned int)(v_stack_p10), (unsigned int)(*(unsigned int *)(a1 + 96)), 3 + 125);
    *(unsigned __int64 *)(v_rip + 3320052) = result;
    *(unsigned int *)(v_rip + 3319845) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124)));
    result = BgpFwReleaseLock(*(unsigned __int64 *)(a1 + 264), (unsigned int)(v_stack_p10), (unsigned int)(*(unsigned int *)(a1 + 96)), 3 + 125);
    *(unsigned __int64 *)(v_rip + 3319982) = *(unsigned __int64 *)(a1 + 232);
loc_00BC5C42:
loc_00BC5C4C:
    goto loc_00BC5C55;
loc_00BC5C50:
loc_00BC5C55:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t BgpFwLibraryInitialize(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (40);
    local_r13 = 0;
    if (Arg1 == NULL) goto loc_00BC5C50;
    if ((*(uint32_t *)(arg1 + 0x74)) >= 5) goto loc_00BC5435;
    goto loc_00BC5C55;
loc_00BC5435:
    local_rbp = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x78))) & (0x16FF0000ULL));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x32B012)))) & (1)) == 0) goto loc_00BC5456;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x32B012)))) & (4)) != 0) goto loc_00BC5456;
    if (condition_is_above_or_equal) goto loc_00BC5C50;
loc_00BC5456:
    if (condition_is_above_or_equal) goto loc_00BC5529;
    result = BgpFwAcquireLock(Arg1, Arg2, a3, a4);
    local_rdi = (uint32_t)((local_rdi) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(Arg2))) != ((uint32_t)(local_rdi))) goto loc_00BC5512;
    Arg1 = 0;
    *(uint64_t *)(v_rip + 0x32AF7E) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x32AFDA))) & (0xFFFFFFFDULL));
    result = (uint32_t)((result) | (0x101800ULL));
    *(uint32_t *)(v_rip + 0x32AFBC) = (uint32_t)(result);
    *(uint64_t *)(v_rip + 0x32AF45) = v_xmm0;
    *(uint64_t *)(v_rip + 0x32AF4E) = v_xmm0;
    result = BgpFwLibraryEnable(Arg1 + 32, Arg2, a3, a4);
    if (sign_flag) goto loc_00BC5C55;
    if (*(uint64_t *)(arg1 + 0x10) != 0) goto loc_00BC54D0;
    *(uint64_t *)(v_rip + 0x32B051) = 0;
    *(uint64_t *)(v_rip + 0x32B042) = 0;
    goto loc_00BC550B;
loc_00BC54D0:
    Arg1 = 0;
    result = BgpFwReservePoolSwap(Arg1, *(uint64_t *)(arg1 + 0xF0), (uint32_t)(*(uint32_t *)(arg1 + 0xF8)), *(uint64_t *)(arg1 + 0x10));
    result = ResFwConfigureDisplayStringResources(*(uint64_t *)(arg1 + 0x100), *(uint64_t *)(arg1 + 0xF0), (uint32_t)(*(uint32_t *)(arg1 + 0xF8)), *(uint64_t *)(arg1 + 0x10));
    *(uint64_t *)(v_rip + 0x32B020) = result;
    result = AnFwConfigureProgressResources(*(uint64_t *)(arg1 + 0x108), *(uint64_t *)(arg1 + 0xF0), (uint32_t)(*(uint32_t *)(arg1 + 0xF8)), *(uint64_t *)(arg1 + 0x10));
    *(uint64_t *)(v_rip + 0x32B005) = result;
loc_00BC550B:
    result = LogFwInitialize(*(uint64_t *)(arg1 + 0x108), *(uint64_t *)(arg1 + 0xF0), (uint32_t)(*(uint32_t *)(arg1 + 0xF8)), *(uint64_t *)(arg1 + 0x10));
    goto loc_00BC551F;
loc_00BC5512:
    result = AnFwProgressIndicatorTransition(*(uint64_t *)(arg1 + 0x108), *(uint64_t *)(arg1 + 0xF0), (uint32_t)(*(uint32_t *)(arg1 + 0xF8)), *(uint64_t *)(arg1 + 0x10));
loc_00BC551F:
    result = BgpFwReleaseLock(*(uint64_t *)(arg1 + 0x108), *(uint64_t *)(arg1 + 0xF0), (uint32_t)(*(uint32_t *)(arg1 + 0xF8)), *(uint64_t *)(arg1 + 0x10));
    goto loc_00BC5C42;
loc_00BC5529:
    local_rdi = (uint32_t)((local_rdi) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(Arg2))) != ((uint32_t)(local_rdi))) goto loc_00BC5647;
    result = BgpFwInitializeLock(*(uint64_t *)(arg1 + 0x108), *(uint64_t *)(arg1 + 0xF0), (uint32_t)(*(uint32_t *)(arg1 + 0xF8)), *(uint64_t *)(arg1 + 0x10));
    result = (uint32_t)((result) | (0xC04ULL));
    *(uint32_t *)(v_rip + 0x32AF0C) = (uint32_t)(result);
    *(uint64_t *)(v_rip + 0x32AFD6) = v_rip + 3321813;
    *(uint64_t *)(v_rip + 0x32AFC7) = v_rip + 3321813;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x108) + 0xF0) == 0) goto loc_00BC563D;
    if ((*(uint32_t *)(arg1 + 0xF8)) == 0) goto loc_00BC563D;
    result = BgpFwInitializeReservePool(*(uint64_t *)(*(uint64_t *)(arg1 + 0x108) + 0xF0), (uint32_t)(0x4000ULL), v_rip + 2748883, *(uint64_t *)(arg1 + 0x10));
    result = BgpFwLibraryEnable(Arg1 + 32, (uint32_t)(0x4000ULL), v_rip + 2748883, *(uint64_t *)(arg1 + 0x10));
    if (sign_flag) goto loc_00BC5816;
    *(uint64_t *)(v_rip + 0x32AEE2) = v_xmm0;
    if ((*(uint64_t *)(arg1 + 0x58)) == 0) goto loc_00BC55F6;
    result = BgpFwAllocateMemory(24, (uint32_t)(0x4000ULL), v_rip + 2748883, *(uint64_t *)(arg1 + 0x10));
    if (result == 0) goto loc_00BC5811;
    Arg2 = 0;
    *(uint64_t *)(result) = *(uint64_t *)(arg1 + 0x58);
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60)));
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(arg1 + 0x58);
    *(uint32_t *)(result + 0xC) = 1;
    *(uint64_t *)(v_rip + 0x32AF11) = result;
    result = BgpFoInitialize(result, Arg2, v_rip + 2748883, *(uint64_t *)(arg1 + 0x10));
    if (sign_flag) goto loc_00BC5816;
loc_00BC55F6:
    if ((*(uint32_t *)(arg1 + 0x74)) >= 3) {
        *(uint64_t *)(v_rip + 0x32AFC4) = v_xmm0;
        result = *(uint32_t *)(arg1 + 0x19C);
        *(uint32_t *)(v_rip + 0x32AFC0) = (uint32_t)(result);
    }
    *(uint32_t *)(v_rip + 0x32AF8F) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x190)));
    result = BgpBcInitializeCriticalMode(0, (uint32_t)((uint32_t)(local_rdi)), v_rip + 2748883, *(uint64_t *)(arg1 + 0x10));
    if (!sign_flag) goto loc_00BC5C42;
    goto loc_00BC5816;
loc_00BC563D:
    goto loc_00BC5C55;
loc_00BC5647:
    result = BgpFwAcquireLock(0, (uint32_t)((uint32_t)(local_rdi)), v_rip + 2748883, *(uint64_t *)(arg1 + 0x10));
    result = BgpFwLibraryEnable(Arg1 + 32, (uint32_t)((uint32_t)(local_rdi)), v_rip + 2748883, *(uint64_t *)(arg1 + 0x10));
    if (!sign_flag) goto loc_00BC5665;
    result = BgpFwReleaseLock(Arg1 + 32, (uint32_t)((uint32_t)(local_rdi)), v_rip + 2748883, *(uint64_t *)(arg1 + 0x10));
    goto loc_00BC5816;
loc_00BC5665:
    result = MmGetPhysicalAddress(*(uint64_t *)(v_rip + 0x32AD94), (uint32_t)((uint32_t)(local_rdi)), v_rip + 2748883, *(uint64_t *)(arg1 + 0x10));
    *(uint64_t *)(v_rip + 0x32ADB2) = result;
    *(uint32_t *)(v_rip + 0x32ADAE) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x32AD64)));
    *(uint32_t *)(v_rip + 0x32ADA6) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x32AD54)));
    *(uint32_t *)(v_rip + 0x32AD9E) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x32AD50)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x32AD79))) - (4));
    if (condition_is_equal) goto loc_00BC56C1;
    if (((uint32_t)(Arg1)) == 1) goto loc_00BC56B5;
    *(uint32_t *)(v_rip + 0x32AD95) = 0;
    goto loc_00BC56CB;
loc_00BC56B5:
    *(uint32_t *)(v_rip + 0x32AD89) = 4;
    goto loc_00BC56CB;
loc_00BC56C1:
    *(uint32_t *)(v_rip + 0x32AD7D) = 3;
loc_00BC56CB:
    v_stack_p8 = 0;
    *(uint64_t *)(v_rip + 0x32AE45) = v_xmm0;
    *(uint64_t *)(v_rip + 0x32AE32) = v_xmm1;
    *(uint64_t *)(v_rip + 0x32AE34) = v_xmm0;
    *(uint64_t *)(v_rip + 0x32AE36) = v_xmm1;
    *(uint64_t *)(v_rip + 0x32AE38) = v_xmm0;
    *(uint64_t *)(v_rip + 0x32AE3A) = v_xmm1;
    *(uint64_t *)(v_rip + 0x32AE3C) = v_xmm0;
    *(uint64_t *)(v_rip + 0x32AE3E) = v_xmm1;
    if ((*(uint64_t *)(arg1 + 0x48)) == 0) goto loc_00BC5789;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x50))) + (15));
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)((uint32_t)(0xFFFFFFF0ULL))));
    v_stack_p8 = 32;
    goto loc_00BC578C;
loc_00BC5789:
loc_00BC578C:
    v_stack_p18 = 0;
    result = local_rbx + 464;
    local_rdi = 0;
    local_r12 = Arg1 + 72;
    if ((*(uint64_t *)(arg1 + 0x80)) != 0) {
        local_rdi = *(uint32_t *)(arg1 + 0x88);
        Arg2 = 32;
        local_rdi = (uint32_t)((local_rdi) + (15));
        v_stack_p18 = Arg2;
        local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0xFFFFFFF0ULL))));
        result = (uint32_t)((local_rbx + 464) + (Arg2));
        result = (uint32_t)((result) + ((uint32_t)(local_rdi)));
        local_r12 = Arg1 + 72;
    }
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x54))) + (0x4070ULL));
    result = (uint32_t)((result) + ((uint32_t)(a4)));
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(result))) - ((uint32_t)(local_rbx)));
    local_r14 = (uint32_t)((local_r14) - (Arg2));
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)(local_rdi)));
    local_r14 = (uint32_t)((local_r14) - (32));
    local_r14 = (uint32_t)((local_r14) - (432));
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> (3));
    local_r13 = (uint32_t)((local_r13) + (15));
    local_r13 = (uint32_t)((local_r13) & ((uint32_t)((uint32_t)(0xFFFFFFF0ULL))));
    result = (uint32_t)((result) + ((uint32_t)(local_r13)));
    v_stack_p20 = (uint32_t)(result);
    result = BgpFwAllocateMemory((uint32_t)((uint32_t)(result)), Arg2, 32, a4);
    a3 = 0;
    *(uint64_t *)(v_rip + 0x32AC7C) = result;
    if (result != 0) goto loc_00BC5820;
    result = BgpFwReleaseLock((uint32_t)((uint32_t)(result)), Arg2, a3, a4);
loc_00BC5811:
loc_00BC5816:
    result = BgpFwLibraryDestroy((uint32_t)((uint32_t)(result)), Arg2, a3, a4);
    goto loc_00BC5C4C;
loc_00BC5820:
loc_00BC582F:
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    *(uint64_t *)(result + 0x40) = v_xmm0;
    *(uint64_t *)(result + 0x50) = v_xmm1;
    *(uint64_t *)(result + 0x60) = v_xmm0;
    Arg1 = (result) + (3 + 125);
    result = (Arg1) + (3 + 125);
    *(uint64_t *)(arg1 - 0x10) = v_xmm1;
    Arg2 = (3) - (1);
    if (condition_is_not_equal) goto loc_00BC582F;
    *(uint64_t *)(arg1) = v_xmm0;
    *(uint64_t *)(arg1 + 0x10) = v_xmm1;
    *(uint64_t *)(arg1 + 0x20) = *(uint64_t *)(result + 0x20);
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(v_stack_p20));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p8)) + ((uint32_t)((uint32_t)(0xC0000017ULL))));
    *(uint64_t *)(result + 0xF0) = 0;
    *(uint32_t *)(result + 0xF8) = 0;
    *(uint64_t *)(result + 0x108) = 0;
    *(uint64_t *)(result + 0x100) = 0;
    a3 = (uint32_t)(((uint32_t)(v_stack_p18)) + (432));
    v_stack_p20 = (uint32_t)(Arg1);
    a3 = (uint32_t)((a3) + ((uint32_t)(Arg1)));
    a3 = (uint32_t)((a3) + ((uint32_t)(local_rdi)));
    a3 = (a3) + (result);
    Arg1 = ((uint32_t)((uint32_t)(local_r13))) + (a3);
    result = BgpFwInitializeReservePool(Arg1, (uint32_t)((uint32_t)(local_r14)), a3, 3 + 125);
    local_r13 = 0;
    *(uint64_t *)(v_rip + 0x32AC08) = 0;
    if ((uint32_t)((uint32_t)(0xC0000017ULL)) == 0) goto loc_00BC5960;
    local_rbx = ((uint32_t)(v_stack_p8)) + (result + 432);
    result = memcpy(local_rbx, *(uint64_t *)(local_r12), (uint32_t)(*(uint32_t *)(arg1 + 0x50)), 3 + 125);
    *(uint32_t *)(result + 0x1B0 + 0xC) = 1;
    *(uint64_t *)(result + 0x1B0) = local_rbx;
    *(uint32_t *)(result + 0x1B0 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)));
    *(uint64_t *)(result + 0x1B0 + 0x10) = local_rbx;
    result = BgpFoInitialize(result + 432, local_r13 + 1, (uint32_t)(*(uint32_t *)(arg1 + 0x50)), 3 + 125);
    if (!(sign_flag)) {
        *(uint64_t *)(v_rip + 0x32ABA9) = result + 432;
    }
    if ((*(uint64_t *)(v_rip + 0x32ABA2)) == 0) {
        Arg2 = 0;
        a3 = v_rip + 1015;
        Arg1 = Arg2 + 101;
        result = DbgPrintEx(Arg1, Arg2, a3, 3 + 125);
    }
    *(uint64_t *)(v_rip + 0x32AB90) = 0;
    if ((uint32_t)(local_rdi) != 0) {
        local_rdi = v_stack_p20;
        local_rbx = v_stack_p18;
        local_rdi = (uint32_t)((local_rdi) + (432));
        a3 = *(uint32_t *)(arg1 + 0x88);
        local_rdi = (local_rdi) + (result);
        Arg2 = *(uint64_t *)(arg1 + 0x80);
        local_rbx = (local_rbx) + (local_rdi);
        Arg1 = local_rbx;
        result = memcpy(Arg1, Arg2, a3, 3 + 125);
        *(uint32_t *)(local_rdi + 0xC) = 1;
        *(uint64_t *)(local_rdi) = local_rbx;
        result = *(uint32_t *)(arg1 + 0x88);
        *(uint32_t *)(local_rdi + 0x8) = (uint32_t)(result);
        *(uint64_t *)(local_rdi + 0x10) = local_rbx;
        *(uint64_t *)(v_rip + 0x32AB3E) = local_rdi;
    }
    Arg2 = 0;
    result = memset(v_rip + 3320517, Arg2, Arg2 + 88, 3 + 125);
    if ((*(uint64_t *)(arg1 + 0x90)) == 0) goto loc_00BC5A2C;
    result = BgpFwAllocateMemory((uint32_t)(*(uint32_t *)(arg1 + 0xA0)), Arg2, Arg2 + 88, 3 + 125);
    *(uint64_t *)(v_rip + 0x32AAA1) = result;
    if (result != 0) {
        a3 = *(uint32_t *)(arg1 + 0xA0);
        Arg1 = result;
        Arg2 = *(uint64_t *)(arg1 + 0x90);
        result = memcpy(Arg1, Arg2, a3, 3 + 125);
        result = *(uint32_t *)(arg1 + 0xA0);
        *(uint32_t *)(v_rip + 0x32AA8A) = (uint32_t)(result);
        result = *(uint64_t *)(arg1 + 0xA4);
        *(uint64_t *)(v_rip + 0x32AA80) = result;
    }
    if (*(uint64_t *)(arg1 + 0xB8) == 0) goto loc_00BC5A4F;
    result = BgpGxProcessQrCodeBitmap(*(uint64_t *)(arg1 + 0xB8), v_rip + 3320473, a3, 3 + 125);
    if (sign_flag) {
        *(uint64_t *)(v_rip + 0x32AA89) = 0;
    }
    if (*(uint64_t *)(arg1 + 0xD8) == 0) goto loc_00BC5AA6;
    local_rbx = (local_rbx) | (-1);
loc_00BC5A62:
    Arg1 = (local_rbx) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0xD8) + arg1 * 2)) != 0) goto loc_00BC5A62;
    result = BgpFwAllocateMemory(Arg1 * 2 + 2, v_rip + 3320473, a3, 3 + 125);
    *(uint64_t *)(v_rip + 0x32AA60) = result;
    if (result == 0) goto loc_00BC5AA6;
loc_00BC5A8C:
    local_rbx = (local_rbx) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0xD8) + local_rbx * 2)) != 0) goto loc_00BC5A8C;
    result = wcscpy_s(*(uint64_t *)(v_rip + 0x32AA43), local_rbx + 1, *(uint64_t *)(arg1 + 0xD8), 3 + 125);
loc_00BC5AA6:
    *(uint64_t *)(v_rip + 0x32AA4B) = 0;
    if ((*(uint64_t *)(arg1 + 0x58)) == 0) goto loc_00BC5B22;
    result = BgpFwAllocateMemory((uint32_t)(*(uint32_t *)(arg1 + 0x60)), local_rbx + 1, *(uint64_t *)(arg1 + 0xD8), 3 + 125);
    if (result == 0) goto loc_00BC5B22;
    result = memcpy(result, *(uint64_t *)(arg1 + 0x58), (uint32_t)(*(uint32_t *)(arg1 + 0x60)), 3 + 125);
    result = BgpFwAllocateMemory(24, *(uint64_t *)(arg1 + 0x58), (uint32_t)(*(uint32_t *)(arg1 + 0x60)), 3 + 125);
    if (result != 0) goto loc_00BC5AEA;
    goto loc_00BC5B1D;
loc_00BC5AEA:
    *(uint32_t *)(result + 0xC) = 0;
    Arg2 = 0;
    *(uint64_t *)(result) = result;
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60)));
    *(uint64_t *)(result + 0x10) = result;
    result = BgpFoInitialize(result, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x60)), 3 + 125);
    if (sign_flag) goto loc_00BC5B12;
    *(uint64_t *)(v_rip + 0x32A9E8) = result;
    goto loc_00BC5B22;
loc_00BC5B12:
    result = BgpFwFreeMemory(result, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x60)), 3 + 125);
loc_00BC5B1D:
    result = BgpFwFreeMemory(result, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x60)), 3 + 125);
loc_00BC5B22:
    if ((*(uint32_t *)(arg1 + 0x74)) >= 3) {
        *(uint64_t *)(v_rip + 0x32AA98) = v_xmm0;
        result = *(uint32_t *)(arg1 + 0x19C);
        *(uint32_t *)(v_rip + 0x32AA94) = (uint32_t)(result);
    }
    *(uint32_t *)(v_rip + 0x32AA68) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x190)));
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x190));
    if ((*(uint32_t *)(arg1 + 0x74)) >= 5) {
        result = *(uint32_t *)(arg1 + 0x1A0);
        *(uint32_t *)(v_rip + 0x32AA7A) = (uint32_t)(result);
    }
    result = BgpBcInitializeCriticalMode(Arg1, (uint32_t)(v_stack_p10), (uint32_t)(*(uint32_t *)(arg1 + 0x60)), 3 + 125);
    *(uint32_t *)(v_rip + 0x32A8C1) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x32A8D4)));
    result = BgpFwAllocateMemory(72, (uint32_t)(v_stack_p10), (uint32_t)(*(uint32_t *)(arg1 + 0x60)), 3 + 125);
    if (result == 0) goto loc_00BC5BF6;
    result = *(uint64_t *)(arg1 + 0x100);
    if (*(uint64_t *)(arg1 + 0x100) != 0) {
        *(uint64_t *)(result) = v_xmm0;
        *(uint64_t *)(result + 0x10) = v_xmm1;
        result = *(uint32_t *)(*(uint64_t *)(arg1 + 0x100) + 0x20);
        *(uint32_t *)(result + 0x20) = (uint32_t)(result);
        *(uint64_t *)(result + 0x100) = result;
        Arg1 = (result) + (36);
    }
    result = *(uint64_t *)(arg1 + 0x108);
    if (*(uint64_t *)(arg1 + 0x108) != 0) {
        *(uint64_t *)(arg1) = v_xmm0;
        *(uint64_t *)(arg1 + 0x10) = v_xmm1;
        result = *(uint32_t *)(*(uint64_t *)(arg1 + 0x108) + 0x20);
        *(uint32_t *)(arg1 + 0x20) = (uint32_t)(result);
        *(void **)(result + 0x108) = Arg1;
    }
    result = ResFwConfigureDisplayStringResources(*(uint64_t *)(arg1 + 0x100), (uint32_t)(v_stack_p10), (uint32_t)(*(uint32_t *)(arg1 + 0x60)), 3 + 125);
    *(uint64_t *)(v_rip + 0x32A90F) = result;
    result = AnFwConfigureProgressResources(*(uint64_t *)(arg1 + 0x108), (uint32_t)(v_stack_p10), (uint32_t)(*(uint32_t *)(arg1 + 0x60)), 3 + 125);
    *(uint64_t *)(v_rip + 0x32A8F4) = result;
    *(uint32_t *)(v_rip + 0x32A825) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C)));
    result = BgpFwReleaseLock(*(uint64_t *)(arg1 + 0x108), (uint32_t)(v_stack_p10), (uint32_t)(*(uint32_t *)(arg1 + 0x60)), 3 + 125);
    *(uint64_t *)(v_rip + 0x32A8AE) = *(uint64_t *)(arg1 + 0xE8);
loc_00BC5C42:
loc_00BC5C4C:
    goto loc_00BC5C55;
loc_00BC5C50:
loc_00BC5C55:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(0xC000000DULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `128` | `R` |
| `Arg1` | `+ 0x30` | `128` | `R` |
| `Arg1` | `+ 0x40` | `128` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x50` | `128` | `R` |
| `Arg1` | `+ 0x54` | `32` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x60` | `32` | `R` |
| `Arg1` | `+ 0x60` | `128` | `R` |
| `Arg1` | `+ 0x64` | `128` | `R` |
| `Arg1` | `+ 0x70` | `128` | `R` |
| `Arg1` | `+ 0x74` | `32` | `R` |
| `Arg1` | `+ 0x7C` | `32` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0x88` | `32` | `R` |
| `Arg1` | `+ 0x90` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `32` | `R` |
| `Arg1` | `+ 0xA4` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xD8` | `64` | `R` |
| `Arg1` | `+ 0xE8` | `64` | `R` |
| `Arg1` | `+ 0xF0` | `64` | `R` |
| `Arg1` | `+ 0xF8` | `32` | `R` |
| `Arg1` | `+ 0x100` | `64` | `R` |
| `Arg1` | `+ 0x108` | `64` | `R` |
| `Arg1` | `+ 0x110` | `128` | `R` |

추가 오프셋 11개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagebgfx&rva=0x00BC5400&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
