# CmUnloadKey

- RVA: `0x009AF2FC`–`0x009AF8FA` (길이 `1,534` bytes)
- VA: `0x00000001409AF2FC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009E084`
- 디코드: `333`개 명령, `1,534/1,534` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x009AF347` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009AF35B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x009AF368` → [CmpInitializeParseContext](../87/CmpInitializeParseContext_function_008767F0.md) (function, `0x008767F0`)
- `0x009AF3E2` → [CmpAcquireHiveLoadUnloadRundown](../../pagecmrc/BC/CmpAcquireHiveLoadUnloadRundown_function_00BC9C6C.md) (function, `0x00BC9C6C`)
- `0x009AF3FD` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x009AF471` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x009AF489` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (function, `0x00461190`)
- `0x009AF4AA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009AF54D` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009AF56F` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009AF5F2` → [ObReferenceObjectByNameEx](../8B/ObReferenceObjectByNameEx_function_008BD524.md) (function, `0x008BD524`)
- `0x009AF624` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x009AF67B` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x009AF690` → [ExWnfHiveUnloaded](ExWnfHiveUnloaded_function_009AF900.md) (function, `0x009AF900`)
- `0x009AF69D` → [CmpIsHiveLoadUnloadRundownActive](../../pagecmrc/BC/CmpIsHiveLoadUnloadRundownActive_function_00BC9FE4.md) (function, `0x00BC9FE4`)
- `0x009AF6BA` → [CmpPerformUnloadKey](CmpPerformUnloadKey_function_009AFA28.md) (function, `0x009AFA28`)
- `0x009AF6E3` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x009AF70A` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x009AF7A9` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x009AF7D0` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x009AF7ED` → [CmpCleanupParseContext](../87/CmpCleanupParseContext_function_00876910.md) (function, `0x00876910`)
- `0x009AF7F8` → [CmpReleaseHiveLoadUnloadRundown](../../pagecmrc/BC/CmpReleaseHiveLoadUnloadRundown_function_00BC9CAC.md) (function, `0x00BC9CAC`)
- `0x009AF7FD` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x009AF80F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009AF83E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009AF85D` → [CmConvertHandleToKernelHandle](../87/CmConvertHandleToKernelHandle_function_00876DDC.md) (function, `0x00876DDC`)
- `0x009AF8B8` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x009AF8CF` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x009AF8E6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009AF8F0` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [NtUnloadKey2](../7E/NtUnloadKey2_function_007E13D0.md) at `0x007E13FF`
- [NtUnloadKeyEx](NtUnloadKeyEx_function_009AEC50.md) at `0x009AEC7B`
- [NtUnloadKey](NtUnloadKey_function_009AF2B0.md) at `0x009AF2DB`

### Static image references
- `0x009AF30F` → RVA `0x00E0A740` (`.data`; read)
- `0x009AF3F6` → RVA `0x00FD9AE0` (`PAGEDATA`; read)
- `0x009AF5DE` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x009AF617` → RVA `0x00EEFB88` (`.data`; read)
- `0x009AF892` → RVA `0x00FC6B80` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x009AF347` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009AF35B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x009AF3E2` → [CmpAcquireHiveLoadUnloadRundown](../../pagecmrc/BC/CmpAcquireHiveLoadUnloadRundown_function_00BC9C6C.md) (`PAGE` → `PAGECMRC`)
  - `0x009AF471` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x009AF489` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (`PAGE` → `.text`)
  - `0x009AF4AA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009AF624` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x009AF69D` → [CmpIsHiveLoadUnloadRundownActive](../../pagecmrc/BC/CmpIsHiveLoadUnloadRundownActive_function_00BC9FE4.md) (`PAGE` → `PAGECMRC`)
  - `0x009AF6E3` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (`PAGE` → `.text`)
  - `0x009AF70A` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x009AF7D0` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x009AF7F8` → [CmpReleaseHiveLoadUnloadRundown](../../pagecmrc/BC/CmpReleaseHiveLoadUnloadRundown_function_00BC9CAC.md) (`PAGE` → `PAGECMRC`)
  - `0x009AF7FD` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x009AF80F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009AF83E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009AF8CF` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x009AF8E6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009AF8F0` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009AF2FC  40 53                           push rbx
009AF2FE  56                              push rsi
009AF2FF  57                              push rdi
009AF300  41 54                           push r12
009AF302  41 55                           push r13
009AF304  41 56                           push r14
009AF306  41 57                           push r15
009AF308  48 81 EC F0 02 00 00            sub rsp, 0x2f0
009AF30F  48 8B 05 2A B4 45 00            mov rax, qword ptr [rip + 0x45b42a]
009AF316  48 33 C4                        xor rax, rsp
009AF319  48 89 84 24 E0 02 00 00         mov qword ptr [rsp + 0x2e0], rax
009AF321  4D 8B E1                        mov r12, r9
009AF324  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
009AF329  44 88 44 24 40                  mov byte ptr [rsp + 0x40], r8b
009AF32E  8B F2                           mov esi, edx
009AF330  89 54 24 70                     mov dword ptr [rsp + 0x70], edx
009AF334  48 8B F9                        mov rdi, rcx
009AF337  33 D2                           xor edx, edx
009AF339  41 B8 D0 01 00 00               mov r8d, 0x1d0
009AF33F  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
009AF347  E8 F4 78 D1 FF                  call 0x1406c6c40
009AF34C  0F 57 C0                        xorps xmm0, xmm0
009AF34F  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
009AF354  33 D2                           xor edx, edx
009AF356  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
009AF35B  E8 20 B4 A7 FF                  call 0x14042a780
009AF360  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
009AF368  E8 83 74 EC FF                  call 0x1408767f0
009AF36D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009AF376  44 8A B0 32 02 00 00            mov r14b, byte ptr [rax + 0x232]
009AF37D  33 DB                           xor ebx, ebx
009AF37F  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
009AF384  44 8B FB                        mov r15d, ebx
009AF387  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
009AF38C  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
009AF391  0F 57 C0                        xorps xmm0, xmm0
009AF394  33 C0                           xor eax, eax
009AF396  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
009AF39E  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
009AF3A6  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
009AF3AE  44 8A EB                        mov r13b, bl
009AF3B1  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
009AF3B9  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
009AF3C1  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
009AF3C9  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
009AF3D1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009AF3DA  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
009AF3E1  90                              nop
009AF3E2  E8 85 A8 21 00                  call 0x140bc9c6c
009AF3E7  88 44 24 42                     mov byte ptr [rsp + 0x42], al
009AF3EB  84 C0                           test al, al
009AF3ED  0F 84 F7 02 00 00               je 0x1409af6ea
009AF3F3  41 8A D6                        mov dl, r14b
009AF3F6  48 8B 0D E3 A6 62 00            mov rcx, qword ptr [rip + 0x62a6e3]
009AF3FD  E8 1E 2A EC FF                  call 0x140871e20
009AF402  84 C0                           test al, al
009AF404  0F 84 74 04 00 00               je 0x1409af87e
009AF40A  F7 C6 FE FF FF FF               test esi, 0xfffffffe
009AF410  0F 85 72 04 00 00               jne 0x1409af888
009AF416  41 80 FE 01                     cmp r14b, 1
009AF41A  0F 84 27 01 00 00               je 0x1409af547
009AF420  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
009AF42A  0F 10 07                        movups xmm0, xmmword ptr [rdi]
009AF42D  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
009AF435  0F 10 4F 10                     movups xmm1, xmmword ptr [rdi + 0x10]
009AF439  0F 11 8C 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm1
009AF441  0F 10 47 20                     movups xmm0, xmmword ptr [rdi + 0x20]
009AF445  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
009AF44D  41 80 FE 01                     cmp r14b, 1
009AF451  74 75                           je 0x1409af4c8
009AF453  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009AF457  0F 10 00                        movups xmm0, xmmword ptr [rax]
009AF45A  F3 0F 7F 44 24 60               movdqu xmmword ptr [rsp + 0x60], xmm0
009AF460  0F B7 7C 24 60                  movzx edi, word ptr [rsp + 0x60]
009AF465  66 85 FF                        test di, di
009AF468  75 16                           jne 0x1409af480
009AF46A  33 D2                           xor edx, edx
009AF46C  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
009AF471  E8 0A B3 A7 FF                  call 0x14042a780
009AF476  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
009AF47B  E9 F4 00 00 00                  jmp 0x1409af574
009AF480  41 B8 43 4D 37 35               mov r8d, 0x35374d43
009AF486  48 8B D7                        mov rdx, rdi
009AF489  E8 02 1D AB FF                  call 0x140461190
009AF48E  48 8B F0                        mov rsi, rax
009AF491  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009AF496  48 85 C0                        test rax, rax
009AF499  0F 84 9A 00 00 00               je 0x1409af539
009AF49F  4C 8B C7                        mov r8, rdi
009AF4A2  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
009AF4A7  48 8B C8                        mov rcx, rax
009AF4AA  E8 91 73 D1 FF                  call 0x1406c6840
009AF4AF  66 89 7C 24 60                  mov word ptr [rsp + 0x60], di
009AF4B4  66 89 7C 24 62                  mov word ptr [rsp + 0x62], di
009AF4B9  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
009AF4BE  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
009AF4C3  E9 AC 00 00 00                  jmp 0x1409af574
009AF4C8  0F 57 C0                        xorps xmm0, xmm0
009AF4CB  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
009AF4D3  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
009AF4DB  48 3B CA                        cmp rcx, rdx
009AF4DE  48 0F 43 CA                     cmovae rcx, rdx
009AF4E2  90                              nop
009AF4E3  8B 01                           mov eax, dword ptr [rcx]
009AF4E5  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
009AF4EC  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
009AF4F0  4C 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r8
009AF4F8  0F 28 84 24 D0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xd0]
009AF500  66 0F 7F 44 24 60               movdqa xmmword ptr [rsp + 0x60], xmm0
009AF506  66 0F 7E C0                     movd eax, xmm0
009AF50A  66 85 C0                        test ax, ax
009AF50D  0F 84 4D FF FF FF               je 0x1409af460
009AF513  41 F6 C0 01                     test r8b, 1
009AF517  75 56                           jne 0x1409af56f
009AF519  0F B7 C0                        movzx eax, ax
009AF51C  4E 8D 0C 00                     lea r9, [rax + r8]
009AF520  4A 8D 0C 00                     lea rcx, [rax + r8]
009AF524  48 3B CA                        cmp rcx, rdx
009AF527  77 09                           ja 0x1409af532
009AF529  4D 3B C8                        cmp r9, r8
009AF52C  0F 83 2E FF FF FF               jae 0x1409af460
009AF532  8A 02                           mov al, byte ptr [rdx]
009AF534  E9 27 FF FF FF                  jmp 0x1409af460
009AF539  BF 9A 00 00 C0                  mov edi, 0xc000009a
009AF53E  89 7C 24 74                     mov dword ptr [rsp + 0x74], edi
009AF542  E9 AD 01 00 00                  jmp 0x1409af6f4
009AF547  40 F6 C7 03                     test dil, 3
009AF54B  74 06                           je 0x1409af553
009AF54D  E8 7E AA EE FF                  call 0x140899fd0
009AF552  CC                              int3
009AF553  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
009AF55D  48 8B C2                        mov rax, rdx
009AF560  48 3B FA                        cmp rdi, rdx
009AF563  48 0F 42 C7                     cmovb rax, rdi
009AF567  90                              nop
009AF568  8A 00                           mov al, byte ptr [rax]
009AF56A  E9 BB FE FF FF                  jmp 0x1409af42a
009AF56F  E8 5C AA EE FF                  call 0x140899fd0
009AF574  48 8D 44 24 60                  lea rax, [rsp + 0x60]
009AF579  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
009AF581  0F 57 C0                        xorps xmm0, xmm0
009AF584  F3 0F 7F 84 24 B0 00 00 00      movdqu xmmword ptr [rsp + 0xb0], xmm0
009AF58D  EB 18                           jmp 0x1409af5a7
009AF58F  8B F8                           mov edi, eax
009AF591  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
009AF595  33 DB                           xor ebx, ebx
009AF597  44 8B FB                        mov r15d, ebx
009AF59A  44 8A EB                        mov r13b, bl
009AF59D  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
009AF5A2  E9 4D 01 00 00                  jmp 0x1409af6f4
009AF5A7  41 80 FE 01                     cmp r14b, 1
009AF5AB  0F 84 94 02 00 00               je 0x1409af845
009AF5B1  89 9C 24 28 01 00 00            mov dword ptr [rsp + 0x128], ebx
009AF5B8  C7 84 24 10 01 00 00 04 00 00 00  mov dword ptr [rsp + 0x110], 4
009AF5C3  48 8D 44 24 58                  lea rax, [rsp + 0x58]
009AF5C8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009AF5CD  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
009AF5D5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AF5DA  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
009AF5DE  4C 8B 0D DB 74 61 00            mov r9, qword ptr [rip + 0x6174db]
009AF5E5  45 33 C0                        xor r8d, r8d
009AF5E8  33 D2                           xor edx, edx
009AF5EA  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
009AF5F2  E8 2D DF F0 FF                  call 0x1408bd524
009AF5F7  BF 0D 00 00 C0                  mov edi, 0xc000000d
009AF5FC  3D 34 00 00 C0                  cmp eax, 0xc0000034
009AF601  0F 44 C7                        cmove eax, edi
009AF604  8B F8                           mov edi, eax
009AF606  85 C0                           test eax, eax
009AF608  0F 88 E6 00 00 00               js 0x1409af6f4
009AF60E  4D 85 E4                        test r12, r12
009AF611  0F 85 7B 02 00 00               jne 0x1409af892
009AF617  83 3D 6A 05 54 00 00            cmp dword ptr [rip + 0x54056a], 0
009AF61E  0F 84 04 02 00 00               je 0x1409af828
009AF624  E8 53 74 AA FF                  call 0x140456a7c
009AF629  85 C0                           test eax, eax
009AF62B  B8 01 00 00 00                  mov eax, 1
009AF630  0F 85 F2 01 00 00               jne 0x1409af828
009AF636  85 C0                           test eax, eax
009AF638  74 51                           je 0x1409af68b
009AF63A  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009AF63F  48 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rcx
009AF647  4C 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r15
009AF64F  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
009AF657  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009AF65C  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
009AF661  C7 44 24 20 23 00 00 00         mov dword ptr [rsp + 0x20], 0x23
009AF669  41 B1 01                        mov r9b, 1
009AF66C  45 33 C0                        xor r8d, r8d
009AF66F  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
009AF677  41 8D 48 22                     lea ecx, [r8 + 0x22]
009AF67B  E8 C0 68 EB FF                  call 0x140865f40
009AF680  85 C0                           test eax, eax
009AF682  0F 88 A7 01 00 00               js 0x1409af82f
009AF688  41 B5 01                        mov r13b, 1
009AF68B  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
009AF690  E8 6B 02 00 00                  call 0x1409af900
009AF695  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
009AF69A  44 8B F3                        mov r14d, ebx
009AF69D  E8 42 A9 21 00                  call 0x140bc9fe4
009AF6A2  84 C0                           test al, al
009AF6A4  0F 85 2F 02 00 00               jne 0x1409af8d9
009AF6AA  4D 8B CF                        mov r9, r15
009AF6AD  44 8A 44 24 40                  mov r8b, byte ptr [rsp + 0x40]
009AF6B2  41 8B D4                        mov edx, r12d
009AF6B5  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009AF6BA  E8 69 03 00 00                  call 0x1409afa28
009AF6BF  8B F8                           mov edi, eax
009AF6C1  3D 2D 02 00 C0                  cmp eax, 0xc000022d
009AF6C6  75 2C                           jne 0x1409af6f4
009AF6C8  41 FF C6                        inc r14d
009AF6CB  41 83 FE 0A                     cmp r14d, 0xa
009AF6CF  76 CC                           jbe 0x1409af69d
009AF6D1  48 C7 44 24 50 80 69 67 FF      mov qword ptr [rsp + 0x50], 0xffffffffff676980
009AF6DA  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
009AF6DF  33 D2                           xor edx, edx
009AF6E1  33 C9                           xor ecx, ecx
009AF6E3  E8 68 9E 85 FF                  call 0x140209550
009AF6E8  EB B0                           jmp 0x1409af69a
009AF6EA  BF 89 01 00 C0                  mov edi, 0xc0000189
009AF6EF  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
009AF6F4  45 84 ED                        test r13b, r13b
009AF6F7  0F 84 B8 00 00 00               je 0x1409af7b5
009AF6FD  83 3D 84 04 54 00 00            cmp dword ptr [rip + 0x540484], 0
009AF704  0F 84 AB 00 00 00               je 0x1409af7b5
009AF70A  E8 6D 73 AA FF                  call 0x140456a7c
009AF70F  85 C0                           test eax, eax
009AF711  0F 85 9E 00 00 00               jne 0x1409af7b5
009AF717  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
009AF71F  48 39 84 24 80 00 00 00         cmp qword ptr [rsp + 0x80], rax
009AF727  0F 84 88 00 00 00               je 0x1409af7b5
009AF72D  0F 57 C0                        xorps xmm0, xmm0
009AF730  33 C0                           xor eax, eax
009AF732  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
009AF73A  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
009AF742  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
009AF74A  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
009AF752  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009AF757  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
009AF75F  89 BC 24 98 00 00 00            mov dword ptr [rsp + 0x98], edi
009AF766  89 BC 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], edi
009AF76D  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
009AF775  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
009AF77D  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
009AF785  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009AF78A  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
009AF78F  C7 44 24 20 23 00 00 00         mov dword ptr [rsp + 0x20], 0x23
009AF797  45 33 C9                        xor r9d, r9d
009AF79A  45 33 C0                        xor r8d, r8d
009AF79D  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
009AF7A5  41 8D 49 23                     lea ecx, [r9 + 0x23]
009AF7A9  E8 92 67 EB FF                  call 0x140865f40
009AF7AE  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
009AF7B5  4D 85 FF                        test r15, r15
009AF7B8  0F 85 25 01 00 00               jne 0x1409af8e3
009AF7BE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009AF7C3  48 85 C9                        test rcx, rcx
009AF7C6  75 76                           jne 0x1409af83e
009AF7C8  48 85 F6                        test rsi, rsi
009AF7CB  74 08                           je 0x1409af7d5
009AF7CD  48 8B CE                        mov rcx, rsi
009AF7D0  E8 AB 65 AC FF                  call 0x140475d80
009AF7D5  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009AF7DA  48 85 C9                        test rcx, rcx
009AF7DD  0F 85 0D 01 00 00               jne 0x1409af8f0
009AF7E3  33 D2                           xor edx, edx
009AF7E5  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
009AF7ED  E8 1E 71 EC FF                  call 0x140876910
009AF7F2  38 5C 24 42                     cmp byte ptr [rsp + 0x42], bl
009AF7F6  74 05                           je 0x1409af7fd
009AF7F8  E8 AF A4 21 00                  call 0x140bc9cac
009AF7FD  E8 AE E0 8A FF                  call 0x14025d8b0
009AF802  8B C7                           mov eax, edi
009AF804  48 8B 8C 24 E0 02 00 00         mov rcx, qword ptr [rsp + 0x2e0]
009AF80C  48 33 CC                        xor rcx, rsp
009AF80F  E8 2C CE CF FF                  call 0x1406ac640
009AF814  48 81 C4 F0 02 00 00            add rsp, 0x2f0
009AF81B  41 5F                           pop r15
009AF81D  41 5E                           pop r14
009AF81F  41 5D                           pop r13
009AF821  41 5C                           pop r12
009AF823  5F                              pop rdi
009AF824  5E                              pop rsi
009AF825  5B                              pop rbx
009AF826  C3                              ret
009AF827  CC                              int3
009AF828  8B C3                           mov eax, ebx
009AF82A  E9 07 FE FF FF                  jmp 0x1409af636
009AF82F  8B FB                           mov edi, ebx
009AF831  3D 03 05 00 C0                  cmp eax, 0xc0000503
009AF836  0F 45 F8                        cmovne edi, eax
009AF839  E9 B6 FE FF FF                  jmp 0x1409af6f4
009AF83E  E8 0D 9B 94 FF                  call 0x1402f9350
009AF843  EB 83                           jmp 0x1409af7c8
009AF845  48 8D 44 24 78                  lea rax, [rsp + 0x78]
009AF84A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009AF84F  45 33 C9                        xor r9d, r9d
009AF852  41 B0 01                        mov r8b, 1
009AF855  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
009AF85D  E8 7A 75 EC FF                  call 0x140876ddc
009AF862  8B F8                           mov edi, eax
009AF864  85 C0                           test eax, eax
009AF866  0F 88 88 FE FF FF               js 0x1409af6f4
009AF86C  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
009AF871  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
009AF879  E9 33 FD FF FF                  jmp 0x1409af5b1
009AF87E  BF 61 00 00 C0                  mov edi, 0xc0000061
009AF883  E9 67 FE FF FF                  jmp 0x1409af6ef
009AF888  BF 0D 00 00 C0                  mov edi, 0xc000000d
009AF88D  E9 5D FE FF FF                  jmp 0x1409af6ef
009AF892  4C 8B 05 E7 72 61 00            mov r8, qword ptr [rip + 0x6172e7]
009AF899  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
009AF89E  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
009AF8A3  48 8D 44 24 50                  lea rax, [rsp + 0x50]
009AF8A8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009AF8AD  45 8A CE                        mov r9b, r14b
009AF8B0  BA 02 00 00 00                  mov edx, 2
009AF8B5  49 8B CC                        mov rcx, r12
009AF8B8  E8 F3 94 EB FF                  call 0x140868db0
009AF8BD  8B F8                           mov edi, eax
009AF8BF  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
009AF8C4  85 C0                           test eax, eax
009AF8C6  0F 88 28 FE FF FF               js 0x1409af6f4
009AF8CC  49 8B CF                        mov rcx, r15
009AF8CF  E8 7C 8A 89 FF                  call 0x140248350
009AF8D4  E9 3E FD FF FF                  jmp 0x1409af617
009AF8D9  BF 89 01 00 C0                  mov edi, 0xc0000189
009AF8DE  E9 11 FE FF FF                  jmp 0x1409af6f4
009AF8E3  49 8B CF                        mov rcx, r15
009AF8E6  E8 65 9A 94 FF                  call 0x1402f9350
009AF8EB  E9 CE FE FF FF                  jmp 0x1409af7be
009AF8F0  E8 BB D9 CF FF                  call 0x1406ad2b0
009AF8F5  E9 E9 FE FF FF                  jmp 0x1409af7e3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmUnloadKey(__int64 a1, int a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m200;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m278;
    unsigned int v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned int v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned int v_stack_m2B4;
    unsigned int v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int16 v_stack_m2C6;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned __int8 v_stack_m2E6;
    unsigned __int8 v_stack_m2E8;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int8 v_stack_m308;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p98;

    v_rsp = (v_rsp) - (752);
    result = (*(unsigned __int64 *)(v_rip + 4568106)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m2D8 = a4;
    v_stack_m2E8 = a3;
    v_stack_m2B8 = a2;
    a2 = 0;
    result = memset(v_stack_m218, a2, 464, a4);
    v_stack_m2C8 = v_xmm0;
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m2C8, a2, 464, a4);
    result = CmpInitializeParseContext(v_stack_m218, a2, 464, a4);
    v_rbx = 0;
    v_stack_m2D0 = 0;
    v_stack_m2E0 = 0;
    v_stack_m2B0 = 0;
    result = 0;
    v_stack_m248 = v_xmm0;
    v_stack_m238 = v_xmm0;
    v_stack_m228 = 0;
    v_stack_m2A0 = v_stack_m2A8;
    v_stack_m2A8 = v_stack_m2A8;
    result = CmpAcquireHiveLoadUnloadRundown(v_stack_m218, a2, 464, a4);
    v_stack_m2E6 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_009AF6EA;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 6465251), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 464, a4);
    if ((unsigned __int8)(result) == 0) goto loc_009AF87E;
    if ((((unsigned int)((unsigned int)(a2))) & (0xFFFFFFFEULL)) != 0) goto loc_009AF888;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) == 1) goto loc_009AF547;
loc_009AF42A:
    v_stack_m298 = v_xmm0;
    v_stack_m288 = v_xmm1;
    v_stack_m278 = v_xmm0;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) == 1) goto loc_009AF4C8;
    v_stack_m2C8 = v_xmm0;
loc_009AF460:
    if ((unsigned __int16)(v_stack_m2C8) != 0) goto loc_009AF480;
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m2C8, a2, 464, a4);
    goto loc_009AF574;
loc_009AF480:
    result = CmpAllocateTransientPoolWithQuota(v_stack_m2C8, v_stack_m2C8, (unsigned int)(0x35374D43ULL), a4);
    v_stack_m2E0 = result;
    if (result == 0) goto loc_009AF539;
    result = memcpy(result, v_stack_m2C0, v_stack_m2C8, a4);
    v_stack_m2C8 = (unsigned __int16)(v_stack_m2C8);
    v_stack_m2C6 = (unsigned __int16)(v_stack_m2C8);
    v_stack_m2C0 = result;
    goto loc_009AF574;
loc_009AF4C8:
    v_stack_m258 = v_xmm0;
    a1 = v_stack_m288;
    if (v_stack_m288 >= v_stack_m2C0) { a1 = v_stack_m2C0; }
    v_stack_m258 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_m250 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m2C8 = v_xmm0;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_009AF460;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 8))) & (1)) != 0) goto loc_009AF56F;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1) > v_stack_m2C0) goto loc_009AF532;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1) >= (*(unsigned __int64 *)(a1 + 8))) goto loc_009AF460;
loc_009AF532:
    goto loc_009AF460;
loc_009AF539:
    v_stack_m2B4 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_009AF6F4;
loc_009AF547:
    result = *(unsigned __int8 *)(v_stack_m2C0);
    if ((((unsigned __int8)((unsigned int)(0xC000009AULL))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1, v_stack_m2C0, *(unsigned __int64 *)(a1 + 8), (unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1);
    }
    result = v_stack_m2C0;
    if (((unsigned int)(0xC000009AULL)) < v_stack_m2C0) { result = (unsigned int)(0xC000009AULL); }
    goto loc_009AF42A;
loc_009AF56F:
    result = ExRaiseDatatypeMisalignment((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1, v_stack_m2C0, *(unsigned __int64 *)(a1 + 8), (unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1);
loc_009AF574:
    v_stack_m288 = v_stack_m2C8;
    v_stack_m278 = v_xmm0;
    goto loc_009AF5A7;
loc_009AF5A7:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) == 1) goto loc_009AF845;
loc_009AF5B1:
    v_stack_m200 = 0;
    v_stack_m218 = 4;
    v_stack_m2F8 = v_stack_m2D0;
    v_stack_m300 = v_stack_m218;
    v_stack_m308 = 0;
    a3 = 0;
    a2 = 0;
    result = ObReferenceObjectByNameEx(v_stack_m298, a2, a3, *(unsigned __int64 *)(v_rip + 6386907));
    if (((unsigned int)(result)) == 0xC0000034ULL) { result = (unsigned int)((unsigned int)(0xC000000DULL)); }
    if (sign_flag) goto loc_009AF6F4;
    if (v_stack_m2D8 != 0) goto loc_009AF892;
loc_009AF617:
    if ((*(unsigned int *)(v_rip + 5506410)) == 0) goto loc_009AF828;
    result = CmpIsRegistryLockAcquired(v_stack_m298, a2, a3, *(unsigned __int64 *)(v_rip + 6386907));
    if ((unsigned int)(result) != 0) goto loc_009AF828;
loc_009AF636:
    if (1 == 0) goto loc_009AF68B;
    v_stack_m248 = v_stack_m2D0;
    v_stack_m240 = 0;
    v_stack_m2F8 = v_stack_m2A8;
    v_stack_m300 = v_stack_m2D0;
    v_stack_m308 = 35;
    a3 = 0;
    result = CmpCallCallBacksEx(a3 + 34, v_stack_m248, a3, 1);
    if (sign_flag) goto loc_009AF82F;
loc_009AF68B:
    result = ExWnfHiveUnloaded(v_stack_m2C8, v_stack_m248, a3, 1);
loc_009AF69A:
loc_009AF69D:
    result = CmpIsHiveLoadUnloadRundownActive(v_stack_m2C8, v_stack_m248, a3, 1);
    if ((unsigned __int8)(result) != 0) goto loc_009AF8D9;
    result = CmpPerformUnloadKey(v_stack_m2D0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m2B8))), v_stack_m2E8, 0);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_009AF6F4;
    v_r14 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r14)) <= 10) goto loc_009AF69D;
    v_stack_m2D8 = 0xFFFFFFFFFF676980ULL;
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_stack_m2D8, 0);
    goto loc_009AF69A;
loc_009AF6EA:
loc_009AF6EF:
loc_009AF6F4:
    if (1 == 0) goto loc_009AF7B5;
    if ((*(unsigned int *)(v_rip + 5506180)) == 0) goto loc_009AF7B5;
    result = CmpIsRegistryLockAcquired(a1, a2, v_stack_m2D8, 0);
    if ((unsigned int)(result) != 0) goto loc_009AF7B5;
    result = v_stack_m2A8;
    v_rdi = (unsigned int)(0xC0000189ULL);
    if (v_stack_m2A8 != v_stack_m2A8) {
        result = 0;
        v_stack_m298 = v_xmm0;
        v_stack_m288 = v_xmm0;
        v_stack_m278 = v_xmm0;
        v_stack_m268 = 0;
        a1 = v_stack_m2D0;
        v_stack_m298 = a1;
        v_stack_m290 = (unsigned int)((unsigned int)(0xC0000189ULL));
        v_stack_m280 = (unsigned int)((unsigned int)(0xC0000189ULL));
        result = v_stack_m248;
        v_stack_m288 = result;
        result = v_stack_m2A8;
        v_stack_m2F8 = result;
        v_stack_m300 = a1;
        v_stack_m308 = 35;
        a4 = 0;
        a3 = 0;
        a2 = v_stack_m298;
        a1 = a4 + 35;
        result = CmpCallCallBacksEx(a1, a2, a3, a4);
        v_rdi = v_stack_m280;
    }
    if (0 != 0) goto loc_009AF8E3;
loc_009AF7BE:
    if (v_stack_m2D0 != 0) goto loc_009AF83E;
loc_009AF7C8:
    if (v_stack_m2E0 != 0) {
        a1 = v_stack_m2E0;
        result = CmSiFreeMemory(a1, a2, a3, a4);
    }
    if (v_stack_m2B0 != 0) goto loc_009AF8F0;
loc_009AF7E3:
    a2 = 0;
    result = CmpCleanupParseContext(v_stack_m218, a2, a3, a4);
    if (v_stack_m2E6 != 0) {
        result = CmpReleaseHiveLoadUnloadRundown(v_stack_m218, a2, a3, a4);
    }
    result = KeLeaveCriticalRegion(v_stack_m218, a2, a3, a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (752);
    return result;
loc_009AF828:
    goto loc_009AF636;
loc_009AF82F:
    v_rdi = 0;
    if (0 != 0xC0000503ULL) { v_rdi = 0; }
    goto loc_009AF6F4;
loc_009AF83E:
    result = ObfDereferenceObject(a1, a2, a3, a4);
    goto loc_009AF7C8;
loc_009AF845:
    v_stack_p20 = v_stack_p78;
    a4 = 0;
    result = CmConvertHandleToKernelHandle(v_stack_p98, a2, 1, a4);
    if (sign_flag) goto loc_009AF6F4;
    v_stack_p98 = v_stack_p78;
    goto loc_009AF5B1;
loc_009AF87E:
    goto loc_009AF6EF;
loc_009AF888:
    goto loc_009AF6EF;
loc_009AF892:
    v_stack_p50 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p50;
    result = ObReferenceObjectByHandle((unsigned int)(v_stack_m2B8), 2, *(unsigned __int64 *)(v_rip + 6386407), (unsigned __int8)(v_r14));
    if (sign_flag) goto loc_009AF6F4;
    result = KeResetEvent(v_stack_p50, 2, *(unsigned __int64 *)(v_rip + 6386407), (unsigned __int8)(v_r14));
    goto loc_009AF617;
loc_009AF8D9:
    goto loc_009AF6F4;
loc_009AF8E3:
    result = ObfDereferenceObject(v_stack_p50, 2, *(unsigned __int64 *)(v_rip + 6386407), (unsigned __int8)(v_r14));
    goto loc_009AF7BE;
loc_009AF8F0:
    result = ZwClose(v_stack_p50, 2, *(unsigned __int64 *)(v_rip + 6386407), (unsigned __int8)(v_r14));
    goto loc_009AF7E3;
}
```

## 5. (Beta) C Style

```c
int64_t CmUnloadKey(int64_t Arg1, int32_t Arg2, uint8_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m200;
    uint64_t v_stack_m218;
    uint64_t v_stack_m228;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m268;
    uint64_t v_stack_m278;
    uint32_t v_stack_m280;
    uint64_t v_stack_m288;
    uint32_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint32_t v_stack_m2B4;
    uint32_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint16_t v_stack_m2C6;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint8_t v_stack_m2E6;
    uint8_t v_stack_m2E8;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint8_t v_stack_m308;
    uint64_t v_stack_m48;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p50;
    uint64_t v_stack_p78;
    uint64_t v_stack_p98;

    local_rsp = (local_rsp) - (752);
    result = (*(uint64_t *)(v_rip + 0x45B42A)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m2D8 = Arg4;
    v_stack_m2E8 = Arg3;
    v_stack_m2B8 = Arg2;
    Arg2 = 0;
    result = memset(v_stack_m218, Arg2, 464, Arg4);
    v_stack_m2C8 = v_xmm0;
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m2C8, Arg2, 464, Arg4);
    result = CmpInitializeParseContext(v_stack_m218, Arg2, 464, Arg4);
    local_rbx = 0;
    v_stack_m2D0 = 0;
    v_stack_m2E0 = 0;
    v_stack_m2B0 = 0;
    result = 0;
    v_stack_m248 = v_xmm0;
    v_stack_m238 = v_xmm0;
    v_stack_m228 = 0;
    v_stack_m2A0 = v_stack_m2A8;
    v_stack_m2A8 = v_stack_m2A8;
    result = CmpAcquireHiveLoadUnloadRundown(v_stack_m218, Arg2, 464, Arg4);
    v_stack_m2E6 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_009AF6EA;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x62A6E3), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 464, Arg4);
    if ((uint8_t)(result) == 0) goto loc_009AF87E;
    if ((((uint32_t)((uint32_t)(Arg2))) & (0xFFFFFFFEULL)) != 0) goto loc_009AF888;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) == 1) goto loc_009AF547;
loc_009AF42A:
    v_stack_m298 = v_xmm0;
    v_stack_m288 = v_xmm1;
    v_stack_m278 = v_xmm0;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) == 1) goto loc_009AF4C8;
    v_stack_m2C8 = v_xmm0;
loc_009AF460:
    if ((uint16_t)(v_stack_m2C8) != 0) goto loc_009AF480;
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m2C8, Arg2, 464, Arg4);
    goto loc_009AF574;
loc_009AF480:
    result = CmpAllocateTransientPoolWithQuota(v_stack_m2C8, v_stack_m2C8, (uint32_t)(0x35374D43ULL), Arg4);
    v_stack_m2E0 = result;
    if (result == 0) goto loc_009AF539;
    result = memcpy(result, v_stack_m2C0, v_stack_m2C8, Arg4);
    v_stack_m2C8 = (uint16_t)(v_stack_m2C8);
    v_stack_m2C6 = (uint16_t)(v_stack_m2C8);
    v_stack_m2C0 = result;
    goto loc_009AF574;
loc_009AF4C8:
    v_stack_m258 = v_xmm0;
    Arg1 = v_stack_m288;
    if (v_stack_m288 >= v_stack_m2C0) { Arg1 = v_stack_m2C0; }
    v_stack_m258 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    v_stack_m250 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m2C8 = v_xmm0;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) == 0) goto loc_009AF460;
    if ((((uint8_t)(*(uint64_t *)(Arg1 + 0x8))) & (1)) != 0) goto loc_009AF56F;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1) > v_stack_m2C0) goto loc_009AF532;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1) >= (*(uint64_t *)(Arg1 + 0x8))) goto loc_009AF460;
loc_009AF532:
    goto loc_009AF460;
loc_009AF539:
    v_stack_m2B4 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_009AF6F4;
loc_009AF547:
    result = *(uint8_t *)(v_stack_m2C0);
    if ((((uint8_t)((uint32_t)(0xC000009AULL))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1, v_stack_m2C0, *(uint64_t *)(Arg1 + 0x8), (uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1);
    }
    result = v_stack_m2C0;
    if (((uint32_t)(0xC000009AULL)) < v_stack_m2C0) { result = (uint32_t)(0xC000009AULL); }
    goto loc_009AF42A;
loc_009AF56F:
    result = ExRaiseDatatypeMisalignment((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1, v_stack_m2C0, *(uint64_t *)(Arg1 + 0x8), (uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1);
loc_009AF574:
    v_stack_m288 = v_stack_m2C8;
    v_stack_m278 = v_xmm0;
    goto loc_009AF5A7;
loc_009AF5A7:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) == 1) goto loc_009AF845;
loc_009AF5B1:
    v_stack_m200 = 0;
    v_stack_m218 = 4;
    v_stack_m2F8 = v_stack_m2D0;
    v_stack_m300 = v_stack_m218;
    v_stack_m308 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = ObReferenceObjectByNameEx(v_stack_m298, Arg2, Arg3, *(uint64_t *)(v_rip + 0x6174DB));
    if (((uint32_t)(result)) == 0xC0000034ULL) { result = (uint32_t)((uint32_t)(0xC000000DULL)); }
    if (sign_flag) goto loc_009AF6F4;
    if (v_stack_m2D8 != 0) goto loc_009AF892;
loc_009AF617:
    if ((*(uint32_t *)(v_rip + 0x54056A)) == 0) goto loc_009AF828;
    result = CmpIsRegistryLockAcquired(v_stack_m298, Arg2, Arg3, *(uint64_t *)(v_rip + 0x6174DB));
    if ((uint32_t)(result) != 0) goto loc_009AF828;
loc_009AF636:
    if (1 == 0) goto loc_009AF68B;
    v_stack_m248 = v_stack_m2D0;
    v_stack_m240 = 0;
    v_stack_m2F8 = v_stack_m2A8;
    v_stack_m300 = v_stack_m2D0;
    v_stack_m308 = 35;
    Arg3 = 0;
    result = CmpCallCallBacksEx(Arg3 + 34, v_stack_m248, Arg3, 1);
    if (sign_flag) goto loc_009AF82F;
loc_009AF68B:
    result = ExWnfHiveUnloaded(v_stack_m2C8, v_stack_m248, Arg3, 1);
loc_009AF69A:
loc_009AF69D:
    result = CmpIsHiveLoadUnloadRundownActive(v_stack_m2C8, v_stack_m248, Arg3, 1);
    if ((uint8_t)(result) != 0) goto loc_009AF8D9;
    result = CmpPerformUnloadKey(v_stack_m2D0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m2B8))), v_stack_m2E8, 0);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_009AF6F4;
    local_r14 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r14)) <= 10) goto loc_009AF69D;
    v_stack_m2D8 = 0xFFFFFFFFFF676980ULL;
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_stack_m2D8, 0);
    goto loc_009AF69A;
loc_009AF6EA:
loc_009AF6EF:
loc_009AF6F4:
    if (1 == 0) goto loc_009AF7B5;
    if ((*(uint32_t *)(v_rip + 0x540484)) == 0) goto loc_009AF7B5;
    result = CmpIsRegistryLockAcquired(Arg1, Arg2, v_stack_m2D8, 0);
    if ((uint32_t)(result) != 0) goto loc_009AF7B5;
    result = v_stack_m2A8;
    local_rdi = (uint32_t)(0xC0000189ULL);
    if (v_stack_m2A8 != v_stack_m2A8) {
        result = 0;
        v_stack_m298 = v_xmm0;
        v_stack_m288 = v_xmm0;
        v_stack_m278 = v_xmm0;
        v_stack_m268 = 0;
        Arg1 = v_stack_m2D0;
        v_stack_m298 = Arg1;
        v_stack_m290 = (uint32_t)((uint32_t)(0xC0000189ULL));
        v_stack_m280 = (uint32_t)((uint32_t)(0xC0000189ULL));
        result = v_stack_m248;
        v_stack_m288 = result;
        result = v_stack_m2A8;
        v_stack_m2F8 = result;
        v_stack_m300 = Arg1;
        v_stack_m308 = 35;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_stack_m298;
        Arg1 = Arg4 + 35;
        result = CmpCallCallBacksEx(Arg1, Arg2, Arg3, Arg4);
        local_rdi = v_stack_m280;
    }
    if (0 != 0) goto loc_009AF8E3;
loc_009AF7BE:
    if (v_stack_m2D0 != 0) goto loc_009AF83E;
loc_009AF7C8:
    if (v_stack_m2E0 != 0) {
        Arg1 = v_stack_m2E0;
        result = CmSiFreeMemory(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m2B0 != 0) goto loc_009AF8F0;
loc_009AF7E3:
    Arg2 = 0;
    result = CmpCleanupParseContext(v_stack_m218, Arg2, Arg3, Arg4);
    if (v_stack_m2E6 != 0) {
        result = CmpReleaseHiveLoadUnloadRundown(v_stack_m218, Arg2, Arg3, Arg4);
    }
    result = KeLeaveCriticalRegion(v_stack_m218, Arg2, Arg3, Arg4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (752);
    return result;
loc_009AF828:
    goto loc_009AF636;
loc_009AF82F:
    local_rdi = 0;
    if (0 != 0xC0000503ULL) { local_rdi = 0; }
    goto loc_009AF6F4;
loc_009AF83E:
    result = ObfDereferenceObject(Arg1, Arg2, Arg3, Arg4);
    goto loc_009AF7C8;
loc_009AF845:
    v_stack_p20 = v_stack_p78;
    Arg4 = 0;
    result = CmConvertHandleToKernelHandle(v_stack_p98, Arg2, 1, Arg4);
    if (sign_flag) goto loc_009AF6F4;
    v_stack_p98 = v_stack_p78;
    goto loc_009AF5B1;
loc_009AF87E:
    goto loc_009AF6EF;
loc_009AF888:
    goto loc_009AF6EF;
loc_009AF892:
    v_stack_p50 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p50;
    result = ObReferenceObjectByHandle((uint32_t)(v_stack_m2B8), 2, *(uint64_t *)(v_rip + 0x6172E7), (uint8_t)(local_r14));
    if (sign_flag) goto loc_009AF6F4;
    result = KeResetEvent(v_stack_p50, 2, *(uint64_t *)(v_rip + 0x6172E7), (uint8_t)(local_r14));
    goto loc_009AF617;
loc_009AF8D9:
    goto loc_009AF6F4;
loc_009AF8E3:
    result = ObfDereferenceObject(v_stack_p50, 2, *(uint64_t *)(v_rip + 0x6172E7), (uint8_t)(local_r14));
    goto loc_009AF7BE;
loc_009AF8F0:
    result = ZwClose(v_stack_p50, 2, *(uint64_t *)(v_rip + 0x6172E7), (uint8_t)(local_r14));
    goto loc_009AF7E3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009AF2FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
