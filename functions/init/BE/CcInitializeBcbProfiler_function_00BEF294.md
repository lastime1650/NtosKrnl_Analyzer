# CcInitializeBcbProfiler

- RVA: `0x00BEF294`–`0x00BEFA64` (길이 `2,000` bytes)
- VA: `0x0000000140BEF294`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2C50`
- 디코드: `545`개 명령, `2,000/2,000` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00BEF366` → [KiGetLoadOptions](../C3/KiGetLoadOptions_function_00C36E3C.md) (function, `0x00C36E3C`)
- `0x00BEF372` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00BEF38A` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x00BEF412` → [RtlSectionTableFromVirtualAddress](../../text/43/RtlSectionTableFromVirtualAddress_function_00432CF0.md) (function, `0x00432CF0`)
- `0x00BEF425` → [RtlLookupFunctionTable](../../text/2F/RtlLookupFunctionTable_function_002F2750.md) (function, `0x002F2750`)
- `0x00BEF6C3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00BEF6D8` → [KeInitializeTimer](../../text/45/KeInitializeTimer_function_0045B590.md) (function, `0x0045B590`)
- `0x00BEF7D5` → [RtlpConvertFunctionEntry](../../text/41/RtlpConvertFunctionEntry_function_00416CA0.md) (function, `0x00416CA0`)
- `0x00BEF7EA` → [RtlpLookupPrimaryFunctionEntry](../../text/48/RtlpLookupPrimaryFunctionEntry_function_0048E8D0.md) (function, `0x0048E8D0`)
- `0x00BEF951` → [KiAreCodePatchesAllowed](../C3/KiAreCodePatchesAllowed_function_00C36DF0.md) (function, `0x00C36DF0`)
- `0x00BEFA23` → [KeSetCoalescableTimer](../../text/22/KeSetCoalescableTimer_function_0022FFD0.md) (function, `0x0022FFD0`)
- `0x00BEFA5E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [CcInitializeCacheManager](CcInitializeCacheManager_function_00BEE2E8.md) at `0x00BEE43E`

### Static image references
- `0x00BEF380` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00BEF398` → RVA `0x005099B0` (`CcBcbProfiler`; read)
- `0x00BEF404` → RVA `0x00705ED0` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x00BEF372` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00BEF38A` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`INIT` → `.text`)
  - `0x00BEF412` → [RtlSectionTableFromVirtualAddress](../../text/43/RtlSectionTableFromVirtualAddress_function_00432CF0.md) (`INIT` → `.text`)
  - `0x00BEF425` → [RtlLookupFunctionTable](../../text/2F/RtlLookupFunctionTable_function_002F2750.md) (`INIT` → `.text`)
  - `0x00BEF6C3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00BEF6D8` → [KeInitializeTimer](../../text/45/KeInitializeTimer_function_0045B590.md) (`INIT` → `.text`)
  - `0x00BEF7D5` → [RtlpConvertFunctionEntry](../../text/41/RtlpConvertFunctionEntry_function_00416CA0.md) (`INIT` → `.text`)
  - `0x00BEF7EA` → [RtlpLookupPrimaryFunctionEntry](../../text/48/RtlpLookupPrimaryFunctionEntry_function_0048E8D0.md) (`INIT` → `.text`)
  - `0x00BEFA23` → [KeSetCoalescableTimer](../../text/22/KeSetCoalescableTimer_function_0022FFD0.md) (`INIT` → `.text`)
  - `0x00BEFA5E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BEF294  40 55                           push rbp
00BEF296  53                              push rbx
00BEF297  56                              push rsi
00BEF298  57                              push rdi
00BEF299  41 54                           push r12
00BEF29B  41 55                           push r13
00BEF29D  41 56                           push r14
00BEF29F  41 57                           push r15
00BEF2A1  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00BEF2A6  48 81 EC A8 00 00 00            sub rsp, 0xa8
00BEF2AD  48 B8 D4 02 00 00 80 F7 FF FF   movabs rax, 0xfffff780000002d4
00BEF2B7  80 38 02                        cmp byte ptr [rax], 2
00BEF2BA  0F 83 68 07 00 00               jae 0x140befa28
00BEF2C0  C7 45 6F 00 30 05 00            mov dword ptr [rbp + 0x6f], 0x53000
00BEF2C7  45 33 FF                        xor r15d, r15d
00BEF2CA  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
00BEF2CD  C1 C8 0C                        ror eax, 0xc
00BEF2D0  88 45 AF                        mov byte ptr [rbp - 0x51], al
00BEF2D3  C7 45 77 0D 64 08 00            mov dword ptr [rbp + 0x77], 0x8640d
00BEF2DA  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00BEF2DD  35 0D 44 00 00                  xor eax, 0x440d
00BEF2E2  C1 C8 2D                        ror eax, 0x2d
00BEF2E5  88 45 B0                        mov byte ptr [rbp - 0x50], al
00BEF2E8  C7 45 7F 00 00 18 01            mov dword ptr [rbp + 0x7f], 0x1180000
00BEF2EF  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
00BEF2F2  C1 C0 0E                        rol eax, 0xe
00BEF2F5  88 45 B1                        mov byte ptr [rbp - 0x4f], al
00BEF2F8  C7 45 BF 00 80 22 00            mov dword ptr [rbp - 0x41], 0x228000
00BEF2FF  8B 45 BF                        mov eax, dword ptr [rbp - 0x41]
00BEF302  C1 C8 0F                        ror eax, 0xf
00BEF305  88 45 B2                        mov byte ptr [rbp - 0x4e], al
00BEF308  C7 45 C3 10 44 80 10            mov dword ptr [rbp - 0x3d], 0x10804410
00BEF30F  8B 45 C3                        mov eax, dword ptr [rbp - 0x3d]
00BEF312  35 10 44 00 00                  xor eax, 0x4410
00BEF317  C1 C8 36                        ror eax, 0x36
00BEF31A  88 45 B3                        mov byte ptr [rbp - 0x4d], al
00BEF31D  C7 45 C7 00 80 27 00            mov dword ptr [rbp - 0x39], 0x278000
00BEF324  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
00BEF327  C1 C0 11                        rol eax, 0x11
00BEF32A  88 45 B4                        mov byte ptr [rbp - 0x4c], al
00BEF32D  C7 45 CB 00 00 3C 01            mov dword ptr [rbp - 0x35], 0x13c0000
00BEF334  8B 45 CB                        mov eax, dword ptr [rbp - 0x35]
00BEF337  C1 C8 12                        ror eax, 0x12
00BEF33A  88 45 B5                        mov byte ptr [rbp - 0x4b], al
00BEF33D  C7 45 CF 39 44 00 00            mov dword ptr [rbp - 0x31], 0x4439
00BEF344  8B 45 CF                        mov eax, dword ptr [rbp - 0x31]
00BEF347  35 13 44 00 00                  xor eax, 0x4413
00BEF34C  C1 C8 3F                        ror eax, 0x3f
00BEF34F  88 45 B6                        mov byte ptr [rbp - 0x4a], al
00BEF352  C7 45 D3 00 A0 03 00            mov dword ptr [rbp - 0x2d], 0x3a000
00BEF359  8B 45 D3                        mov eax, dword ptr [rbp - 0x2d]
00BEF35C  C1 C0 14                        rol eax, 0x14
00BEF35F  88 45 B7                        mov byte ptr [rbp - 0x49], al
00BEF362  44 88 7D B8                     mov byte ptr [rbp - 0x48], r15b
00BEF366  E8 D1 7A 04 00                  call 0x140c36e3c
00BEF36B  48 8B C8                        mov rcx, rax
00BEF36E  48 8D 55 AF                     lea rdx, [rbp - 0x51]
00BEF372  E8 09 03 91 FF                  call 0x1404ff680
00BEF377  48 85 C0                        test rax, rax
00BEF37A  0F 85 A8 06 00 00               jne 0x140befa28
00BEF380  4C 8D 2D 79 0C 41 FF            lea r13, [rip - 0xbef387]
00BEF387  49 8B CD                        mov rcx, r13
00BEF38A  E8 D1 47 85 FF                  call 0x140443b60
00BEF38F  4C 8B C8                        mov r9, rax
00BEF392  0F 31                           rdtsc
00BEF394  48 C1 E2 20                     shl rdx, 0x20
00BEF398  4C 8D 05 11 A6 91 FF            lea r8, [rip - 0x6e59ef]
00BEF39F  48 0B C2                        or rax, rdx
00BEF3A2  49 BC 01 20 00 04 80 00 10 70   movabs r12, 0x7010008004002001
00BEF3AC  48 8B C8                        mov rcx, rax
00BEF3AF  48 8B D0                        mov rdx, rax
00BEF3B2  48 C1 C9 03                     ror rcx, 3
00BEF3B6  49 8B C4                        mov rax, r12
00BEF3B9  48 33 D1                        xor rdx, rcx
00BEF3BC  49 8B C9                        mov rcx, r9
00BEF3BF  48 F7 E2                        mul rdx
00BEF3C2  48 8B F2                        mov rsi, rdx
00BEF3C5  48 89 55 EF                     mov qword ptr [rbp - 0x11], rdx
00BEF3C9  48 33 F0                        xor rsi, rax
00BEF3CC  48 B8 15 AE 47 E1 7A 14 AE 47   movabs rax, 0x47ae147ae147ae15
00BEF3D6  48 F7 E6                        mul rsi
00BEF3D9  48 8B C6                        mov rax, rsi
00BEF3DC  48 2B C2                        sub rax, rdx
00BEF3DF  48 D1 E8                        shr rax, 1
00BEF3E2  48 03 C2                        add rax, rdx
00BEF3E5  49 8B D5                        mov rdx, r13
00BEF3E8  48 C1 E8 06                     shr rax, 6
00BEF3EC  48 6B C0 64                     imul rax, rax, 0x64
00BEF3F0  48 2B F0                        sub rsi, rax
00BEF3F3  41 8B C7                        mov eax, r15d
00BEF3F6  48 83 FE 32                     cmp rsi, 0x32
00BEF3FA  48 89 75 DF                     mov qword ptr [rbp - 0x21], rsi
00BEF3FE  0F 93 C0                        setae al
00BEF401  89 45 D7                        mov dword ptr [rbp - 0x29], eax
00BEF404  48 8D 05 C5 6A B1 FF            lea rax, [rip - 0x4e953b]
00BEF40B  44 0F 43 C0                     cmovae r8d, eax
00BEF40F  45 2B C5                        sub r8d, r13d
00BEF412  E8 D9 38 84 FF                  call 0x140432cf0
00BEF417  4C 8D 45 67                     lea r8, [rbp + 0x67]
00BEF41B  48 8B C8                        mov rcx, rax
00BEF41E  48 8D 55 F7                     lea rdx, [rbp - 9]
00BEF422  48 8B D8                        mov rbx, rax
00BEF425  E8 26 33 70 FF                  call 0x1402f2750
00BEF42A  4C 8B C0                        mov r8, rax
00BEF42D  48 85 C0                        test rax, rax
00BEF430  0F 84 07 06 00 00               je 0x140befa3d
00BEF436  83 7D 67 0C                     cmp dword ptr [rbp + 0x67], 0xc
00BEF43A  0F 82 FD 05 00 00               jb 0x140befa3d
00BEF440  8B 4D 67                        mov ecx, dword ptr [rbp + 0x67]
00BEF443  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00BEF44D  48 F7 E1                        mul rcx
00BEF450  41 8B FF                        mov edi, r15d
00BEF453  45 8B F7                        mov r14d, r15d
00BEF456  48 C1 EA 03                     shr rdx, 3
00BEF45A  8B C2                           mov eax, edx
00BEF45C  8B 53 0C                        mov edx, dword ptr [rbx + 0xc]
00BEF45F  48 8D 0C 40                     lea rcx, [rax + rax*2]
00BEF463  8B 43 08                        mov eax, dword ptr [rbx + 8]
00BEF466  4D 8D 0C 88                     lea r9, [r8 + rcx*4]
00BEF46A  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
00BEF46D  3B C8                           cmp ecx, eax
00BEF46F  0F 46 C8                        cmovbe ecx, eax
00BEF472  03 CA                           add ecx, edx
00BEF474  41 8B 00                        mov eax, dword ptr [r8]
00BEF477  3B C2                           cmp eax, edx
00BEF479  72 10                           jb 0x140bef48b
00BEF47B  3B C1                           cmp eax, ecx
00BEF47D  73 19                           jae 0x140bef498
00BEF47F  48 85 FF                        test rdi, rdi
00BEF482  4D 8B F0                        mov r14, r8
00BEF485  49 0F 44 F8                     cmove rdi, r8
00BEF489  EB 04                           jmp 0x140bef48f
00BEF48B  3B C1                           cmp eax, ecx
00BEF48D  73 09                           jae 0x140bef498
00BEF48F  49 83 C0 0C                     add r8, 0xc
00BEF493  4D 3B C1                        cmp r8, r9
00BEF496  75 DC                           jne 0x140bef474
00BEF498  48 85 FF                        test rdi, rdi
00BEF49B  75 0C                           jne 0x140bef4a9
00BEF49D  49 C7 C1 FF 00 00 C0            mov r9, 0xffffffffc00000ff
00BEF4A4  E9 9B 05 00 00                  jmp 0x140befa44
00BEF4A9  0F 31                           rdtsc
00BEF4AB  48 C1 E2 20                     shl rdx, 0x20
00BEF4AF  48 0B C2                        or rax, rdx
00BEF4B2  48 8B C8                        mov rcx, rax
00BEF4B5  48 8B D0                        mov rdx, rax
00BEF4B8  48 C1 C9 03                     ror rcx, 3
00BEF4BC  49 8B C4                        mov rax, r12
00BEF4BF  48 33 D1                        xor rdx, rcx
00BEF4C2  48 F7 E2                        mul rdx
00BEF4C5  48 8B CA                        mov rcx, rdx
00BEF4C8  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
00BEF4CC  48 33 C8                        xor rcx, rax
00BEF4CF  48 B8 CD CC CC CC CC CC CC CC   movabs rax, 0xcccccccccccccccd
00BEF4D9  48 F7 E1                        mul rcx
00BEF4DC  48 C1 EA 03                     shr rdx, 3
00BEF4E0  48 8D 04 92                     lea rax, [rdx + rdx*4]
00BEF4E4  48 03 C0                        add rax, rax
00BEF4E7  48 2B C8                        sub rcx, rax
00BEF4EA  48 83 F9 05                     cmp rcx, 5
00BEF4EE  0F 83 34 05 00 00               jae 0x140befa28
00BEF4F4  0F 31                           rdtsc
00BEF4F6  48 C1 E2 20                     shl rdx, 0x20
00BEF4FA  48 0B C2                        or rax, rdx
00BEF4FD  48 8B C8                        mov rcx, rax
00BEF500  48 8B D0                        mov rdx, rax
00BEF503  48 C1 C9 03                     ror rcx, 3
00BEF507  49 8B C4                        mov rax, r12
00BEF50A  48 33 D1                        xor rdx, rcx
00BEF50D  48 F7 E2                        mul rdx
00BEF510  4C 8B C2                        mov r8, rdx
00BEF513  48 89 55 07                     mov qword ptr [rbp + 7], rdx
00BEF517  4C 33 C0                        xor r8, rax
00BEF51A  48 B8 A3 8B 2E BA E8 A2 8B 2E   movabs rax, 0x2e8ba2e8ba2e8ba3
00BEF524  49 F7 E0                        mul r8
00BEF527  48 D1 EA                        shr rdx, 1
00BEF52A  48 6B C2 0B                     imul rax, rdx, 0xb
00BEF52E  4C 2B C0                        sub r8, rax
00BEF531  41 83 F8 05                     cmp r8d, 5
00BEF535  77 78                           ja 0x140bef5af
00BEF537  74 6F                           je 0x140bef5a8
00BEF539  41 8B C0                        mov eax, r8d
00BEF53C  45 85 C0                        test r8d, r8d
00BEF53F  74 56                           je 0x140bef597
00BEF541  83 E8 01                        sub eax, 1
00BEF544  74 38                           je 0x140bef57e
00BEF546  83 E8 01                        sub eax, 1
00BEF549  74 1D                           je 0x140bef568
00BEF54B  83 F8 01                        cmp eax, 1
00BEF54E  74 07                           je 0x140bef557
00BEF550  B8 46 49 76 70                  mov eax, 0x70764946
00BEF555  EB 2C                           jmp 0x140bef583
00BEF557  41 8D 40 02                     lea eax, [r8 + 2]
00BEF55B  8D 0C 40                        lea ecx, [rax + rax*2]
00BEF55E  B8 44 50 77 72                  mov eax, 0x72775044
00BEF563  E9 3C 01 00 00                  jmp 0x140bef6a4
00BEF568  B8 43 64 6D 61                  mov eax, 0x616d6443
00BEF56D  41 8B C8                        mov ecx, r8d
00BEF570  D3 C0                           rol eax, cl
00BEF572  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00BEF575  44 8B 55 A7                     mov r10d, dword ptr [rbp - 0x59]
00BEF579  E9 35 01 00 00                  jmp 0x140bef6b3
00BEF57E  B8 43 63 5A 65                  mov eax, 0x655a6343
00BEF583  41 8B C8                        mov ecx, r8d
00BEF586  D3 C8                           ror eax, cl
00BEF588  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00BEF58B  44 8B 55 A7                     mov r10d, dword ptr [rbp - 0x59]
00BEF58F  41 D3 C2                        rol r10d, cl
00BEF592  E9 1F 01 00 00                  jmp 0x140bef6b6
00BEF597  41 8D 40 02                     lea eax, [r8 + 2]
00BEF59B  8D 0C 40                        lea ecx, [rax + rax*2]
00BEF59E  B8 43 63 42 63                  mov eax, 0x63426343
00BEF5A3  E9 FC 00 00 00                  jmp 0x140bef6a4
00BEF5A8  B8 4F 62 44 69                  mov eax, 0x6944624f
00BEF5AD  EB BE                           jmp 0x140bef56d
00BEF5AF  41 8B C0                        mov eax, r8d
00BEF5B2  83 E8 06                        sub eax, 6
00BEF5B5  0F 84 DD 00 00 00               je 0x140bef698
00BEF5BB  83 E8 01                        sub eax, 1
00BEF5BE  0F 84 CA 00 00 00               je 0x140bef68e
00BEF5C4  83 E8 01                        sub eax, 1
00BEF5C7  0F 84 B7 00 00 00               je 0x140bef684
00BEF5CD  83 F8 01                        cmp eax, 1
00BEF5D0  0F 84 A0 00 00 00               je 0x140bef676
00BEF5D6  0F 31                           rdtsc
00BEF5D8  48 C1 E2 20                     shl rdx, 0x20
00BEF5DC  41 BB 4F EC C4 4E               mov r11d, 0x4ec4ec4f
00BEF5E2  48 0B C2                        or rax, rdx
00BEF5E5  48 8B C8                        mov rcx, rax
00BEF5E8  48 8B D0                        mov rdx, rax
00BEF5EB  48 C1 C9 03                     ror rcx, 3
00BEF5EF  49 8B C4                        mov rax, r12
00BEF5F2  48 33 D1                        xor rdx, rcx
00BEF5F5  48 F7 E2                        mul rdx
00BEF5F8  4C 8B D0                        mov r10, rax
00BEF5FB  41 8B C3                        mov eax, r11d
00BEF5FE  44 33 D2                        xor r10d, edx
00BEF601  41 F7 E2                        mul r10d
00BEF604  45 8B C2                        mov r8d, r10d
00BEF607  41 8B C3                        mov eax, r11d
00BEF60A  C1 EA 03                        shr edx, 3
00BEF60D  6B CA 1A                        imul ecx, edx, 0x1a
00BEF610  41 C1 EA 05                     shr r10d, 5
00BEF614  41 F7 E2                        mul r10d
00BEF617  44 2B C1                        sub r8d, ecx
00BEF61A  45 8B CA                        mov r9d, r10d
00BEF61D  41 83 C0 61                     add r8d, 0x61
00BEF621  41 C1 EA 05                     shr r10d, 5
00BEF625  41 C1 E0 08                     shl r8d, 8
00BEF629  C1 EA 03                        shr edx, 3
00BEF62C  6B C2 1A                        imul eax, edx, 0x1a
00BEF62F  44 2B C8                        sub r9d, eax
00BEF632  41 8B C3                        mov eax, r11d
00BEF635  41 F7 E2                        mul r10d
00BEF638  41 83 C1 41                     add r9d, 0x41
00BEF63C  41 8B C3                        mov eax, r11d
00BEF63F  45 0B C8                        or r9d, r8d
00BEF642  C1 EA 03                        shr edx, 3
00BEF645  45 8B C2                        mov r8d, r10d
00BEF648  6B CA 1A                        imul ecx, edx, 0x1a
00BEF64B  41 C1 EA 05                     shr r10d, 5
00BEF64F  41 F7 E2                        mul r10d
00BEF652  44 2B C1                        sub r8d, ecx
00BEF655  41 C1 E1 08                     shl r9d, 8
00BEF659  41 83 C0 61                     add r8d, 0x61
00BEF65D  C1 EA 03                        shr edx, 3
00BEF660  6B C2 1A                        imul eax, edx, 0x1a
00BEF663  45 0B C1                        or r8d, r9d
00BEF666  41 C1 E0 08                     shl r8d, 8
00BEF66A  44 2B D0                        sub r10d, eax
00BEF66D  41 83 C2 41                     add r10d, 0x41
00BEF671  45 0B D0                        or r10d, r8d
00BEF674  EB 40                           jmp 0x140bef6b6
00BEF676  41 8D 40 02                     lea eax, [r8 + 2]
00BEF67A  8D 0C 40                        lea ecx, [rax + rax*2]
00BEF67D  B8 46 4F 43 58                  mov eax, 0x58434f46
00BEF682  EB 20                           jmp 0x140bef6a4
00BEF684  B8 41 66 64 42                  mov eax, 0x42646641
00BEF689  E9 DF FE FF FF                  jmp 0x140bef56d
00BEF68E  B8 41 6C 53 63                  mov eax, 0x63536c41
00BEF693  E9 EB FE FF FF                  jmp 0x140bef583
00BEF698  41 8D 40 02                     lea eax, [r8 + 2]
00BEF69C  8D 0C 40                        lea ecx, [rax + rax*2]
00BEF69F  B8 4E 74 46 57                  mov eax, 0x5746744e
00BEF6A4  D3 C0                           rol eax, cl
00BEF6A6  41 33 C0                        xor eax, r8d
00BEF6A9  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00BEF6AC  44 8B 55 A7                     mov r10d, dword ptr [rbp - 0x59]
00BEF6B0  45 33 D0                        xor r10d, r8d
00BEF6B3  41 D3 CA                        ror r10d, cl
00BEF6B6  45 8B C2                        mov r8d, r10d
00BEF6B9  BA D8 00 00 00                  mov edx, 0xd8
00BEF6BE  B9 40 00 00 00                  mov ecx, 0x40
00BEF6C3  E8 28 2A F9 FF                  call 0x140b820f0
00BEF6C8  48 8B D8                        mov rbx, rax
00BEF6CB  48 85 C0                        test rax, rax
00BEF6CE  0F 84 54 03 00 00               je 0x140befa28
00BEF6D4  48 8D 48 40                     lea rcx, [rax + 0x40]
00BEF6D8  E8 B3 BE 86 FF                  call 0x14045b590
00BEF6DD  48 8D 05 CC A2 91 FF            lea rax, [rip - 0x6e5d34]
00BEF6E4  C7 03 13 01 00 00               mov dword ptr [rbx], 0x113
00BEF6EA  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00BEF6EE  41 B8 01 00 00 00               mov r8d, 1
00BEF6F4  48 89 5B 20                     mov qword ptr [rbx + 0x20], rbx
00BEF6F8  4C 89 7B 38                     mov qword ptr [rbx + 0x38], r15
00BEF6FC  4C 89 7B 10                     mov qword ptr [rbx + 0x10], r15
00BEF700  0F 31                           rdtsc
00BEF702  48 C1 E2 20                     shl rdx, 0x20
00BEF706  48 0B C2                        or rax, rdx
00BEF709  48 8B C8                        mov rcx, rax
00BEF70C  48 8B D0                        mov rdx, rax
00BEF70F  48 C1 C9 03                     ror rcx, 3
00BEF713  49 8B C4                        mov rax, r12
00BEF716  48 33 D1                        xor rdx, rcx
00BEF719  48 F7 E2                        mul rdx
00BEF71C  48 33 D0                        xor rdx, rax
00BEF71F  48 89 93 A0 00 00 00            mov qword ptr [rbx + 0xa0], rdx
00BEF726  0F 31                           rdtsc
00BEF728  48 C1 E2 20                     shl rdx, 0x20
00BEF72C  48 0B C2                        or rax, rdx
00BEF72F  48 8B C8                        mov rcx, rax
00BEF732  48 8B D0                        mov rdx, rax
00BEF735  48 C1 C9 03                     ror rcx, 3
00BEF739  49 8B C4                        mov rax, r12
00BEF73C  48 33 D1                        xor rdx, rcx
00BEF73F  48 F7 E2                        mul rdx
00BEF742  48 8B CA                        mov rcx, rdx
00BEF745  48 33 C8                        xor rcx, rax
00BEF748  48 B8 11 04 41 10 04 41 10 04   movabs rax, 0x410410410410411
00BEF752  48 F7 E1                        mul rcx
00BEF755  48 8B C1                        mov rax, rcx
00BEF758  48 2B C2                        sub rax, rdx
00BEF75B  48 D1 E8                        shr rax, 1
00BEF75E  48 03 C2                        add rax, rdx
00BEF761  48 C1 E8 05                     shr rax, 5
00BEF765  48 6B C0 3F                     imul rax, rax, 0x3f
00BEF769  48 2B C8                        sub rcx, rax
00BEF76C  41 02 C8                        add cl, r8b
00BEF76F  88 8B A8 00 00 00               mov byte ptr [rbx + 0xa8], cl
00BEF775  0F 31                           rdtsc
00BEF777  48 C1 E2 20                     shl rdx, 0x20
00BEF77B  4C 2B F7                        sub r14, rdi
00BEF77E  48 0B C2                        or rax, rdx
00BEF781  4C 89 AB 88 00 00 00            mov qword ptr [rbx + 0x88], r13
00BEF788  48 8B C8                        mov rcx, rax
00BEF78B  48 8B D0                        mov rdx, rax
00BEF78E  48 C1 C9 03                     ror rcx, 3
00BEF792  49 8B C4                        mov rax, r12
00BEF795  48 33 D1                        xor rdx, rcx
00BEF798  48 F7 E2                        mul rdx
00BEF79B  4C 8B C0                        mov r8, rax
00BEF79E  4C 8B CA                        mov r9, rdx
00BEF7A1  4D 33 C8                        xor r9, r8
00BEF7A4  48 B8 AB AA AA AA AA AA AA 2A   movabs rax, 0x2aaaaaaaaaaaaaab
00BEF7AE  49 F7 EE                        imul r14
00BEF7B1  49 8B C1                        mov rax, r9
00BEF7B4  48 D1 FA                        sar rdx, 1
00BEF7B7  48 8B CA                        mov rcx, rdx
00BEF7BA  48 C1 E9 3F                     shr rcx, 0x3f
00BEF7BE  48 03 CA                        add rcx, rdx
00BEF7C1  33 D2                           xor edx, edx
00BEF7C3  8B C9                           mov ecx, ecx
00BEF7C5  48 F7 F1                        div rcx
00BEF7C8  8B C2                           mov eax, edx
00BEF7CA  49 8B D5                        mov rdx, r13
00BEF7CD  48 8D 0C 40                     lea rcx, [rax + rax*2]
00BEF7D1  48 8D 0C 8F                     lea rcx, [rdi + rcx*4]
00BEF7D5  E8 C6 74 82 FF                  call 0x140416ca0
00BEF7DA  48 8B 93 88 00 00 00            mov rdx, qword ptr [rbx + 0x88]
00BEF7E1  48 8B C8                        mov rcx, rax
00BEF7E4  44 8B 00                        mov r8d, dword ptr [rax]
00BEF7E7  4C 03 C2                        add r8, rdx
00BEF7EA  E8 E1 F0 89 FF                  call 0x14048e8d0
00BEF7EF  44 0F B6 A3 A8 00 00 00         movzx r12d, byte ptr [rbx + 0xa8]
00BEF7F7  48 8B F8                        mov rdi, rax
00BEF7FA  4C 8B BB A0 00 00 00            mov r15, qword ptr [rbx + 0xa0]
00BEF801  45 8B D4                        mov r10d, r12d
00BEF804  48 89 83 80 00 00 00            mov qword ptr [rbx + 0x80], rax
00BEF80B  8B 08                           mov ecx, dword ptr [rax]
00BEF80D  44 8B 70 04                     mov r14d, dword ptr [rax + 4]
00BEF811  44 8B E9                        mov r13d, ecx
00BEF814  4C 03 AB 88 00 00 00            add r13, qword ptr [rbx + 0x88]
00BEF81B  44 2B F1                        sub r14d, ecx
00BEF81E  41 8B CE                        mov ecx, r14d
00BEF821  4D 8B CD                        mov r9, r13
00BEF824  49 03 CD                        add rcx, r13
00BEF827  44 89 65 67                     mov dword ptr [rbp + 0x67], r12d
00BEF82B  49 8B C5                        mov rax, r13
00BEF82E  4C 3B E9                        cmp r13, rcx
00BEF831  73 0C                           jae 0x140bef83f
00BEF833  0F 18 00                        prefetchnta byte ptr [rax]
00BEF836  48 83 C0 40                     add rax, 0x40
00BEF83A  48 3B C1                        cmp rax, rcx
00BEF83D  72 F4                           jb 0x140bef833
00BEF83F  45 8B DE                        mov r11d, r14d
00BEF842  4D 8B C7                        mov r8, r15
00BEF845  41 C1 EB 07                     shr r11d, 7
00BEF849  45 85 DB                        test r11d, r11d
00BEF84C  74 62                           je 0x140bef8b0
00BEF84E  48 BE 01 20 00 04 80 00 10 70   movabs rsi, 0x7010008004002001
00BEF858  41 BC 01 00 00 00               mov r12d, 1
00BEF85E  B8 08 00 00 00                  mov eax, 8
00BEF863  4D 33 01                        xor r8, qword ptr [r9]
00BEF866  41 8B CA                        mov ecx, r10d
00BEF869  49 D3 C0                        rol r8, cl
00BEF86C  4D 33 41 08                     xor r8, qword ptr [r9 + 8]
00BEF870  49 83 C1 10                     add r9, 0x10
00BEF874  49 D3 C0                        rol r8, cl
00BEF877  49 2B C4                        sub rax, r12
00BEF87A  75 E7                           jne 0x140bef863
00BEF87C  49 8B C9                        mov rcx, r9
00BEF87F  49 2B CD                        sub rcx, r13
00BEF882  49 33 CF                        xor rcx, r15
00BEF885  48 8B C1                        mov rax, rcx
00BEF888  48 C1 C0 11                     rol rax, 0x11
00BEF88C  48 33 C8                        xor rcx, rax
00BEF88F  48 8B C6                        mov rax, rsi
00BEF892  48 F7 E1                        mul rcx
00BEF895  33 C2                           xor eax, edx
00BEF897  44 33 D0                        xor r10d, eax
00BEF89A  41 83 E2 3F                     and r10d, 0x3f
00BEF89E  45 0F 44 D4                     cmove r10d, r12d
00BEF8A2  41 83 C3 FF                     add r11d, -1
00BEF8A6  75 B6                           jne 0x140bef85e
00BEF8A8  48 8B 75 DF                     mov rsi, qword ptr [rbp - 0x21]
00BEF8AC  44 8B 65 67                     mov r12d, dword ptr [rbp + 0x67]
00BEF8B0  41 8B D6                        mov edx, r14d
00BEF8B3  41 BB 01 00 00 00               mov r11d, 1
00BEF8B9  83 E2 7F                        and edx, 0x7f
00BEF8BC  83 FA 08                        cmp edx, 8
00BEF8BF  72 1B                           jb 0x140bef8dc
00BEF8C1  8B C2                           mov eax, edx
00BEF8C3  48 C1 E8 03                     shr rax, 3
00BEF8C7  4D 33 01                        xor r8, qword ptr [r9]
00BEF8CA  41 8B CA                        mov ecx, r10d
00BEF8CD  49 D3 C0                        rol r8, cl
00BEF8D0  49 83 C1 08                     add r9, 8
00BEF8D4  83 C2 F8                        add edx, -8
00BEF8D7  49 2B C3                        sub rax, r11
00BEF8DA  75 EB                           jne 0x140bef8c7
00BEF8DC  85 D2                           test edx, edx
00BEF8DE  74 15                           je 0x140bef8f5
00BEF8E0  41 0F B6 01                     movzx eax, byte ptr [r9]
00BEF8E4  41 8B CA                        mov ecx, r10d
00BEF8E7  4C 33 C0                        xor r8, rax
00BEF8EA  4D 03 CB                        add r9, r11
00BEF8ED  49 D3 C0                        rol r8, cl
00BEF8F0  83 C2 FF                        add edx, -1
00BEF8F3  75 EB                           jne 0x140bef8e0
00BEF8F5  48 8D 4F 0C                     lea rcx, [rdi + 0xc]
00BEF8F9  4C 89 83 98 00 00 00            mov qword ptr [rbx + 0x98], r8
00BEF900  48 8B C7                        mov rax, rdi
00BEF903  48 3B F9                        cmp rdi, rcx
00BEF906  73 0C                           jae 0x140bef914
00BEF908  0F 18 00                        prefetchnta byte ptr [rax]
00BEF90B  48 83 C0 40                     add rax, 0x40
00BEF90F  48 3B C1                        cmp rax, rcx
00BEF912  72 F4                           jb 0x140bef908
00BEF914  4C 33 07                        xor r8, qword ptr [rdi]
00BEF917  41 8B CC                        mov ecx, r12d
00BEF91A  49 D3 C0                        rol r8, cl
00BEF91D  BA 04 00 00 00                  mov edx, 4
00BEF922  48 83 C7 08                     add rdi, 8
00BEF926  0F B6 07                        movzx eax, byte ptr [rdi]
00BEF929  41 8B CC                        mov ecx, r12d
00BEF92C  4C 33 C0                        xor r8, rax
00BEF92F  49 03 FB                        add rdi, r11
00BEF932  49 D3 C0                        rol r8, cl
00BEF935  83 C2 FF                        add edx, -1
00BEF938  75 EC                           jne 0x140bef926
00BEF93A  8B 45 D7                        mov eax, dword ptr [rbp - 0x29]
00BEF93D  89 83 AC 00 00 00               mov dword ptr [rbx + 0xac], eax
00BEF943  4C 89 83 98 00 00 00            mov qword ptr [rbx + 0x98], r8
00BEF94A  44 89 B3 90 00 00 00            mov dword ptr [rbx + 0x90], r14d
00BEF951  E8 9A 74 04 00                  call 0x140c36df0
00BEF956  33 C9                           xor ecx, ecx
00BEF958  85 C0                           test eax, eax
00BEF95A  0F 95 C1                        setne cl
00BEF95D  89 8B B0 00 00 00               mov dword ptr [rbx + 0xb0], ecx
00BEF963  48 83 FE 32                     cmp rsi, 0x32
00BEF967  72 1D                           jb 0x140bef986
00BEF969  48 83 A3 B8 00 00 00 00         and qword ptr [rbx + 0xb8], 0
00BEF971  48 8D 05 58 65 B1 FF            lea rax, [rip - 0x4e9aa8]
00BEF978  48 89 83 C8 00 00 00            mov qword ptr [rbx + 0xc8], rax
00BEF97F  48 89 9B D0 00 00 00            mov qword ptr [rbx + 0xd0], rbx
00BEF986  0F 31                           rdtsc
00BEF988  48 C1 E2 20                     shl rdx, 0x20
00BEF98C  49 B9 01 20 00 04 80 00 10 70   movabs r9, 0x7010008004002001
00BEF996  48 0B C2                        or rax, rdx
00BEF999  49 C7 C2 00 74 79 B8            mov r10, 0xffffffffb8797400
00BEF9A0  48 8B C8                        mov rcx, rax
00BEF9A3  48 8B D0                        mov rdx, rax
00BEF9A6  48 C1 C9 03                     ror rcx, 3
00BEF9AA  49 8B C1                        mov rax, r9
00BEF9AD  48 33 D1                        xor rdx, rcx
00BEF9B0  48 F7 E2                        mul rdx
00BEF9B3  4C 8B C2                        mov r8, rdx
00BEF9B6  4C 33 C0                        xor r8, rax
00BEF9B9  48 B8 FD CE 61 84 11 77 CC AB   movabs rax, 0xabcc77118461cefd
00BEF9C3  49 F7 E0                        mul r8
00BEF9C6  48 C1 EA 1A                     shr rdx, 0x1a
00BEF9CA  48 69 CA 00 E1 F5 05            imul rcx, rdx, 0x5f5e100
00BEF9D1  4C 2B C1                        sub r8, rcx
00BEF9D4  4D 2B D0                        sub r10, r8
00BEF9D7  0F 31                           rdtsc
00BEF9D9  48 C1 E2 20                     shl rdx, 0x20
00BEF9DD  45 33 C0                        xor r8d, r8d
00BEF9E0  48 0B C2                        or rax, rdx
00BEF9E3  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00BEF9E8  48 8B C8                        mov rcx, rax
00BEF9EB  48 8B D0                        mov rdx, rax
00BEF9EE  49 8B C1                        mov rax, r9
00BEF9F1  48 C1 C9 03                     ror rcx, 3
00BEF9F5  48 33 D1                        xor rdx, rcx
00BEF9F8  48 8D 4B 40                     lea rcx, [rbx + 0x40]
00BEF9FC  48 F7 E2                        mul rdx
00BEF9FF  4C 8B CA                        mov r9, rdx
00BEFA02  4C 33 C8                        xor r9, rax
00BEFA05  48 B8 4B 59 86 38 D6 C5 6D 34   movabs rax, 0x346dc5d63886594b
00BEFA0F  49 F7 E1                        mul r9
00BEFA12  48 C1 EA 0B                     shr rdx, 0xb
00BEFA16  48 69 C2 10 27 00 00            imul rax, rdx, 0x2710
00BEFA1D  49 8B D2                        mov rdx, r10
00BEFA20  4C 2B C8                        sub r9, rax
00BEFA23  E8 A8 05 64 FF                  call 0x14022ffd0
00BEFA28  48 81 C4 A8 00 00 00            add rsp, 0xa8
00BEFA2F  41 5F                           pop r15
00BEFA31  41 5E                           pop r14
00BEFA33  41 5D                           pop r13
00BEFA35  41 5C                           pop r12
00BEFA37  5F                              pop rdi
00BEFA38  5E                              pop rsi
00BEFA39  5B                              pop rbx
00BEFA3A  5D                              pop rbp
00BEFA3B  C3                              ret
00BEFA3C  CC                              int3
00BEFA3D  49 C7 C1 7B 00 00 C0            mov r9, 0xffffffffc000007b
00BEFA44  C7 45 A7 09 00 00 E8            mov dword ptr [rbp - 0x59], 0xe8000009
00BEFA4B  4C 8B C3                        mov r8, rbx
00BEFA4E  8B 4D A7                        mov ecx, dword ptr [rbp - 0x59]
00BEFA51  BA 06 00 00 00                  mov edx, 6
00BEFA56  C1 C1 65                        rol ecx, 0x65
00BEFA59  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00BEFA5E  E8 FD DB 90 FF                  call 0x1404fd660
00BEFA63  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcInitializeBcbProfiler(void)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned __int8 v_stack_mA7;
    unsigned __int8 v_stack_mA8;
    unsigned __int8 v_stack_mA9;
    unsigned __int8 v_stack_mAA;
    unsigned __int8 v_stack_mAB;
    unsigned __int8 v_stack_mAC;
    unsigned __int8 v_stack_mAD;
    unsigned __int8 v_stack_mAE;
    unsigned __int8 v_stack_mAF;
    unsigned __int8 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (168);
    if ((*(unsigned __int8 *)(result)) >= 2) goto loc_00BEFA28;
    v_stack_p10 = 0x53000ULL;
    v_r15 = 0;
    v_stack_mB0 = (unsigned __int8)((unsigned int)(v_stack_p10));
    v_stack_p18 = 0x8640DULL;
    result = (unsigned int)(((unsigned int)(v_stack_p18)) ^ (0x440DULL));
    v_stack_mAF = (unsigned __int8)(result);
    v_stack_p20 = 0x1180000ULL;
    v_stack_mAE = (unsigned __int8)((unsigned int)(v_stack_p20));
    v_stack_mA0 = 0x228000ULL;
    v_stack_mAD = (unsigned __int8)((unsigned int)(v_stack_mA0));
    v_stack_m9C = 0x10804410ULL;
    result = (unsigned int)(((unsigned int)(v_stack_m9C)) ^ (0x4410ULL));
    v_stack_mAC = (unsigned __int8)(result);
    v_stack_m98 = 0x278000ULL;
    v_stack_mAB = (unsigned __int8)((unsigned int)(v_stack_m98));
    v_stack_m94 = 0x13C0000ULL;
    v_stack_mAA = (unsigned __int8)((unsigned int)(v_stack_m94));
    v_stack_m90 = 0x4439ULL;
    result = (unsigned int)(((unsigned int)(v_stack_m90)) ^ (0x4413ULL));
    v_stack_mA9 = (unsigned __int8)(result);
    v_stack_m8C = 0x3A000ULL;
    v_stack_mA8 = (unsigned __int8)((unsigned int)(v_stack_m8C));
    v_stack_mA7 = 0;
    result = KiGetLoadOptions(a1, a2, a3, a4);
    result = strstr(result, v_stack_mB0, a3, a4);
    if (result != 0) goto loc_00BEFA28;
    result = RtlImageNtHeader(v_rip - 12514183, v_stack_mB0, a3, a4);
    a2 = (v_stack_mB0) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m70 = a2;
    v_rsi = (a2) ^ (v_r12);
    result = (v_rsi) - (a2);
    result = (result) >> (1);
    result = (result) + (a2);
    result = (result) >> (6);
    result = (result) * (result);
    v_rsi = (v_rsi) - (result);
    v_stack_m80 = v_rsi;
    result = (v_rsi >= 50) ? 1 : 0;
    v_stack_m88 = (unsigned int)(result);
    a3 = v_rip - 7231983;
    if (v_rsi >= 50) { a3 = (unsigned int)(v_rip - 5150011); }
    a3 = (unsigned int)((a3) - ((unsigned int)(v_rip - 12514183)));
    result = RtlSectionTableFromVirtualAddress(result, v_rip - 12514183, a3, result);
    result = RtlLookupFunctionTable(result, v_stack_m68, v_stack_p8, result);
    if (result == 0) goto loc_00BEFA3D;
    if (v_stack_p8 < 12) goto loc_00BEFA3D;
    a2 = (v_stack_m68) >> (3);
    a1 = (unsigned int)(*(unsigned int *)(result + 16));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 16)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(result + 8))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8))); }
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)(*(unsigned int *)(result + 12)))));
loc_00BEF474:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(result + 12))))) goto loc_00BEF48B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) >= ((unsigned int)(a1))) goto loc_00BEF498;
    v_rdi = 0;
    if (0 == 0) { v_rdi = result; }
    goto loc_00BEF48F;
loc_00BEF48B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) >= ((unsigned int)(a1))) goto loc_00BEF498;
loc_00BEF48F:
    a3 = (result) + (12);
    if (a3 != (result + (unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 2 * 4)) goto loc_00BEF474;
loc_00BEF498:
    if (v_rdi != 0) goto loc_00BEF4A9;
    goto loc_00BEFA44;
loc_00BEF4A9:
    a2 = ((unsigned int)(*(unsigned int *)(result + 12))) << (32);
    result = ((unsigned int)(*(unsigned int *)(result))) | (a2);
    a2 = (result) ^ (result);
    v_stack_m60 = a2;
    a1 = (a2) ^ (v_r12);
    a2 = (a2) >> (3);
    result = (a2 + a2 * 4) + (a2 + a2 * 4);
    a1 = (a1) - (result);
    if (a1 >= 5) goto loc_00BEFA28;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m58 = a2;
    a3 = (a2) ^ (v_r12);
    a2 = (a2) >> (1);
    result = (v_r12) * (a2);
    a3 = (a3) - (result);
    if (((unsigned int)(a3)) > 5) goto loc_00BEF5AF;
    if (((unsigned int)(a3)) == 5) goto loc_00BEF5A8;
    if ((unsigned int)(a3) == 0) goto loc_00BEF597;
    result = (unsigned int)(((unsigned int)((unsigned int)(a3))) - (1));
    if (condition_is_equal) goto loc_00BEF57E;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BEF568;
    if (((unsigned int)(result)) == 1) goto loc_00BEF557;
    goto loc_00BEF583;
loc_00BEF557:
    goto loc_00BEF6A4;
loc_00BEF568:
loc_00BEF56D:
    v_stack_mB8 = (unsigned int)((unsigned int)(0x616D6443ULL));
    goto loc_00BEF6B3;
loc_00BEF57E:
loc_00BEF583:
    v_stack_mB8 = (unsigned int)((unsigned int)(0x655A6343ULL));
    goto loc_00BEF6B6;
loc_00BEF597:
    goto loc_00BEF6A4;
loc_00BEF5A8:
    goto loc_00BEF56D;
loc_00BEF5AF:
    result = (unsigned int)(((unsigned int)((unsigned int)(a3))) - (6));
    if (condition_is_equal) goto loc_00BEF698;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BEF68E;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00BEF684;
    if (((unsigned int)(result)) == 1) goto loc_00BEF676;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_r10 = (unsigned int)((v_r12) ^ ((unsigned int)(a2)));
    a2 = (unsigned int)((a2) >> (3));
    a1 = (unsigned int)((result) * ((unsigned int)(a2)));
    v_r10 = (unsigned int)((v_r10) >> (5));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(a1)));
    a3 = (unsigned int)((a3) + (97));
    v_r10 = (unsigned int)((v_r10) >> (5));
    a3 = (unsigned int)((a3) << (8));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(result)));
    a4 = (unsigned int)((a4) + (65));
    a4 = (unsigned int)((a4) | ((unsigned int)(a3)));
    a2 = (unsigned int)((a2) >> (3));
    a1 = (unsigned int)((a1) * ((unsigned int)(a2)));
    v_r10 = (unsigned int)((v_r10) >> (5));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(a1)));
    a4 = (unsigned int)((a4) << (8));
    a3 = (unsigned int)((a3) + (97));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x4EC4EC4FULL)))) * ((unsigned int)(a2)));
    a3 = (unsigned int)((a3) | ((unsigned int)(a4)));
    a3 = (unsigned int)((a3) << (8));
    v_r10 = (unsigned int)((v_r10) - ((unsigned int)(result)));
    v_r10 = (unsigned int)((v_r10) + (65));
    v_r10 = (unsigned int)((v_r10) | ((unsigned int)(a3)));
    goto loc_00BEF6B6;
loc_00BEF676:
    goto loc_00BEF6A4;
loc_00BEF684:
    goto loc_00BEF56D;
loc_00BEF68E:
    goto loc_00BEF583;
loc_00BEF698:
loc_00BEF6A4:
    result = (unsigned int)(((unsigned int)(0x5746744EULL)) ^ ((unsigned int)(a3)));
    v_stack_mB8 = (unsigned int)(result);
    v_r10 = (unsigned int)(((unsigned int)(v_stack_mB8)) ^ ((unsigned int)(a3)));
loc_00BEF6B3:
loc_00BEF6B6:
    result = ExAllocatePool2(64, 216, (unsigned int)((unsigned int)(v_r10)), a4);
    if (result == 0) goto loc_00BEFA28;
    result = KeInitializeTimer(result + 64, 216, (unsigned int)((unsigned int)(v_r10)), a4);
    *(unsigned int *)(result) = 275;
    *(unsigned __int64 *)(result + 24) = v_rip - 7232820;
    *(unsigned __int64 *)(result + 32) = result;
    *(unsigned __int64 *)(result + 56) = 0;
    *(unsigned __int64 *)(result + 16) = 0;
    a2 = (216) << (32);
    result = (v_rip - 7232820) | (a2);
    a2 = (result) ^ (result);
    a2 = (a2) ^ (v_r12);
    *(unsigned __int64 *)(result + 160) = a2;
    a2 = (a2) << (32);
    result = (v_r12) | (a2);
    a2 = (result) ^ (result);
    a1 = (a2) ^ (v_r12);
    result = (a1) - (a2);
    result = (result) >> (1);
    result = (result) + (a2);
    result = (result) >> (5);
    result = (result) * (result);
    a1 = (a1) - (result);
    a1 = (unsigned __int8)((a1) + (1));
    *(unsigned __int8 *)(result + 168) = (unsigned __int8)(a1);
    a2 = (a2) << (32);
    v_r14 = (result) - (v_rdi);
    result = (result) | (a2);
    *(unsigned __int64 *)(result + 136) = v_rip - 12514183;
    a2 = (result) ^ (result);
    a4 = (a2) ^ (v_r12);
    a2 = (a2) >> (1);
    a1 = (a2) >> (63);
    a1 = (a1) + (a2);
    a2 = 0;
    result = RtlpConvertFunctionEntry(v_rdi + 0 + 0 * 2 * 4, v_rip - 12514183, v_r12, a4);
    a3 = ((unsigned int)(*(unsigned int *)(result))) + (*(unsigned __int64 *)(result + 136));
    result = RtlpLookupPrimaryFunctionEntry(result, *(unsigned __int64 *)(result + 136), a3, a4);
    *(unsigned __int64 *)(result + 128) = result;
    v_r13 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))) + (*(unsigned __int64 *)(result + 136));
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 4))) - ((unsigned int)((unsigned int)(*(unsigned int *)(result)))));
    a1 = ((unsigned int)((unsigned int)(v_r14))) + (v_r13);
    v_stack_p8 = (unsigned int)(*(unsigned __int8 *)(result + 168));
    if (v_r13 >= a1) goto loc_00BEF83F;
loc_00BEF833:
    result = (v_r13) + (64);
    if (result < a1) goto loc_00BEF833;
loc_00BEF83F:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> (7));
    if ((unsigned int)(v_r11) == 0) goto loc_00BEF8B0;
loc_00BEF85E:
loc_00BEF863:
    a3 = (*(unsigned __int64 *)(result + 160)) ^ (*(unsigned __int64 *)(v_r13));
    a3 = (a3) ^ (*(unsigned __int64 *)(v_r13 + 8));
    a4 = (v_r13) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BEF863;
    a1 = (a4) - (v_r13);
    a1 = (a1) ^ (*(unsigned __int64 *)(result + 160));
    a1 = (a1) ^ (a1);
    result = (unsigned int)((v_rsi) ^ ((unsigned int)(*(unsigned __int64 *)(result + 136))));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(result + 168)))) ^ ((unsigned int)(result)));
    v_r10 = (unsigned int)((v_r10) & (63));
    if (condition_is_equal) { v_r10 = 1; }
    v_r11 = (unsigned int)((v_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BEF85E;
loc_00BEF8B0:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (127));
    if (((unsigned int)(a2)) < 8) goto loc_00BEF8DC;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_00BEF8C7:
    a3 = (a3) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (8);
    a2 = (unsigned int)((a2) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BEF8C7;
loc_00BEF8DC:
    if ((unsigned int)(a2) == 0) goto loc_00BEF8F5;
loc_00BEF8E0:
    a3 = (a3) ^ (*(unsigned __int8 *)(a4));
    a4 = (a4) + (1);
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00BEF8E0;
loc_00BEF8F5:
    *(unsigned __int64 *)(result + 152) = a3;
    if (result >= (result + 12)) goto loc_00BEF914;
loc_00BEF908:
    result = (result) + (64);
    if (result < (result + 12)) goto loc_00BEF908;
loc_00BEF914:
    a3 = (a3) ^ (*(unsigned __int64 *)(result));
    v_rdi = (result) + (8);
loc_00BEF926:
    a3 = (a3) ^ (*(unsigned __int8 *)(v_rdi));
    v_rdi = (v_rdi) + (1);
    a2 = (unsigned int)((4) + (-1));
    if (condition_is_not_equal) goto loc_00BEF926;
    *(unsigned int *)(result + 172) = (unsigned int)((unsigned int)(v_stack_m88));
    *(unsigned __int64 *)(result + 152) = a3;
    *(unsigned int *)(result + 144) = (unsigned int)(v_r14);
    result = KiAreCodePatchesAllowed((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))), a2, a3, a4);
    a1 = 0;
    a1 = ((unsigned int)(result) != 0) ? 1 : 0;
    *(unsigned int *)(result + 176) = (unsigned int)(a1);
    if (v_stack_m80 >= 50) {
        result = v_rip - 5151400;
        *(unsigned __int64 *)(result + 200) = result;
        *(unsigned __int64 *)(result + 208) = result;
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    a3 = (a2) ^ (a4);
    a2 = (a2) >> (26);
    a1 = (result) * (a2);
    a3 = (a3) - (a1);
    v_r10 = (0xFFFFFFFFB8797400ULL) - (a3);
    a2 = (a2) << (32);
    a3 = 0;
    result = (a4) | (a2);
    v_stack_mC8 = result;
    a2 = (result) ^ (result);
    a4 = (a2) ^ (a4);
    a2 = (a2) >> (11);
    result = (a4) * (a2);
    a4 = (a4) - (result);
    result = KeSetCoalescableTimer(result + 64, v_r10, a3, a4);
loc_00BEFA28:
    v_rsp = (v_rsp) + (168);
    return result;
loc_00BEFA3D:
loc_00BEFA44:
    v_stack_mB8 = 0xE8000009ULL;
    v_stack_p20 = *(unsigned __int64 *)(result + 160);
    result = KeBugCheckEx((unsigned int)(v_stack_mB8), 6, result, 0xFFFFFFFFC000007BULL);
    return result;
}
```

## 5. (Beta) C Style

```c
void CcInitializeBcbProfiler(void)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint8_t v_stack_mA7;
    uint8_t v_stack_mA8;
    uint8_t v_stack_mA9;
    uint8_t v_stack_mAA;
    uint8_t v_stack_mAB;
    uint8_t v_stack_mAC;
    uint8_t v_stack_mAD;
    uint8_t v_stack_mAE;
    uint8_t v_stack_mAF;
    uint8_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (168);
    if ((*(uint8_t *)(result)) >= 2) goto loc_00BEFA28;
    v_stack_p10 = 0x53000ULL;
    local_r15 = 0;
    v_stack_mB0 = (uint8_t)((uint32_t)(v_stack_p10));
    v_stack_p18 = 0x8640DULL;
    result = (uint32_t)(((uint32_t)(v_stack_p18)) ^ (0x440DULL));
    v_stack_mAF = (uint8_t)(result);
    v_stack_p20 = 0x1180000ULL;
    v_stack_mAE = (uint8_t)((uint32_t)(v_stack_p20));
    v_stack_mA0 = 0x228000ULL;
    v_stack_mAD = (uint8_t)((uint32_t)(v_stack_mA0));
    v_stack_m9C = 0x10804410ULL;
    result = (uint32_t)(((uint32_t)(v_stack_m9C)) ^ (0x4410ULL));
    v_stack_mAC = (uint8_t)(result);
    v_stack_m98 = 0x278000ULL;
    v_stack_mAB = (uint8_t)((uint32_t)(v_stack_m98));
    v_stack_m94 = 0x13C0000ULL;
    v_stack_mAA = (uint8_t)((uint32_t)(v_stack_m94));
    v_stack_m90 = 0x4439ULL;
    result = (uint32_t)(((uint32_t)(v_stack_m90)) ^ (0x4413ULL));
    v_stack_mA9 = (uint8_t)(result);
    v_stack_m8C = 0x3A000ULL;
    v_stack_mA8 = (uint8_t)((uint32_t)(v_stack_m8C));
    v_stack_mA7 = 0;
    result = KiGetLoadOptions(a1, a2, a3, a4);
    result = strstr(result, v_stack_mB0, a3, a4);
    if (result != 0) goto loc_00BEFA28;
    result = RtlImageNtHeader(v_rip - 12514183, v_stack_mB0, a3, a4);
    a2 = (v_stack_mB0) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m70 = a2;
    local_rsi = (a2) ^ (local_r12);
    result = (local_rsi) - (a2);
    result = (result) >> (1);
    result = (result) + (a2);
    result = (result) >> (6);
    result = (result) * (result);
    local_rsi = (local_rsi) - (result);
    v_stack_m80 = local_rsi;
    result = (local_rsi >= 50) ? 1 : 0;
    v_stack_m88 = (uint32_t)(result);
    a3 = v_rip - 7231983;
    if (local_rsi >= 50) { a3 = (uint32_t)(v_rip - 5150011); }
    a3 = (uint32_t)((a3) - ((uint32_t)(v_rip - 12514183)));
    result = RtlSectionTableFromVirtualAddress(result, v_rip - 12514183, a3, result);
    result = RtlLookupFunctionTable(result, v_stack_m68, v_stack_p8, result);
    if (result == 0) goto loc_00BEFA3D;
    if (v_stack_p8 < 12) goto loc_00BEFA3D;
    a2 = (v_stack_m68) >> (3);
    a1 = (uint32_t)(*(uint32_t *)(result + 0x10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8))))) { a1 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8))); }
    a1 = (uint32_t)((a1) + ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC)))));
loc_00BEF474:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC))))) goto loc_00BEF48B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) >= ((uint32_t)(a1))) goto loc_00BEF498;
    local_rdi = 0;
    if (0 == 0) { local_rdi = result; }
    goto loc_00BEF48F;
loc_00BEF48B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) >= ((uint32_t)(a1))) goto loc_00BEF498;
loc_00BEF48F:
    a3 = (result) + (12);
    if (a3 != (result + (uint32_t)((uint32_t)(a2)) + (uint32_t)((uint32_t)(a2)) * 2 * 4)) goto loc_00BEF474;
loc_00BEF498:
    if (local_rdi != 0) goto loc_00BEF4A9;
    goto loc_00BEFA44;
loc_00BEF4A9:
    a2 = ((uint32_t)(*(uint32_t *)(result + 0xC))) << (32);
    result = ((uint32_t)(*(uint32_t *)(result))) | (a2);
    a2 = (result) ^ (result);
    v_stack_m60 = a2;
    a1 = (a2) ^ (local_r12);
    a2 = (a2) >> (3);
    result = (a2 + a2 * 4) + (a2 + a2 * 4);
    a1 = (a1) - (result);
    if (a1 >= 5) goto loc_00BEFA28;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m58 = a2;
    a3 = (a2) ^ (local_r12);
    a2 = (a2) >> (1);
    result = (local_r12) * (a2);
    a3 = (a3) - (result);
    if (((uint32_t)(a3)) > 5) goto loc_00BEF5AF;
    if (((uint32_t)(a3)) == 5) goto loc_00BEF5A8;
    if ((uint32_t)(a3) == 0) goto loc_00BEF597;
    result = (uint32_t)(((uint32_t)((uint32_t)(a3))) - (1));
    if (condition_is_equal) goto loc_00BEF57E;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BEF568;
    if (((uint32_t)(result)) == 1) goto loc_00BEF557;
    goto loc_00BEF583;
loc_00BEF557:
    goto loc_00BEF6A4;
loc_00BEF568:
loc_00BEF56D:
    v_stack_mB8 = (uint32_t)((uint32_t)(0x616D6443ULL));
    goto loc_00BEF6B3;
loc_00BEF57E:
loc_00BEF583:
    v_stack_mB8 = (uint32_t)((uint32_t)(0x655A6343ULL));
    goto loc_00BEF6B6;
loc_00BEF597:
    goto loc_00BEF6A4;
loc_00BEF5A8:
    goto loc_00BEF56D;
loc_00BEF5AF:
    result = (uint32_t)(((uint32_t)((uint32_t)(a3))) - (6));
    if (condition_is_equal) goto loc_00BEF698;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BEF68E;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00BEF684;
    if (((uint32_t)(result)) == 1) goto loc_00BEF676;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    local_r10 = (uint32_t)((local_r12) ^ ((uint32_t)(a2)));
    a2 = (uint32_t)((a2) >> (3));
    a1 = (uint32_t)((result) * ((uint32_t)(a2)));
    local_r10 = (uint32_t)((local_r10) >> (5));
    a3 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(a1)));
    a3 = (uint32_t)((a3) + (97));
    local_r10 = (uint32_t)((local_r10) >> (5));
    a3 = (uint32_t)((a3) << (8));
    a2 = (uint32_t)((a2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(a2)));
    a4 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(result)));
    a4 = (uint32_t)((a4) + (65));
    a4 = (uint32_t)((a4) | ((uint32_t)(a3)));
    a2 = (uint32_t)((a2) >> (3));
    a1 = (uint32_t)((a1) * ((uint32_t)(a2)));
    local_r10 = (uint32_t)((local_r10) >> (5));
    a3 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(a1)));
    a4 = (uint32_t)((a4) << (8));
    a3 = (uint32_t)((a3) + (97));
    a2 = (uint32_t)((a2) >> (3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x4EC4EC4FULL)))) * ((uint32_t)(a2)));
    a3 = (uint32_t)((a3) | ((uint32_t)(a4)));
    a3 = (uint32_t)((a3) << (8));
    local_r10 = (uint32_t)((local_r10) - ((uint32_t)(result)));
    local_r10 = (uint32_t)((local_r10) + (65));
    local_r10 = (uint32_t)((local_r10) | ((uint32_t)(a3)));
    goto loc_00BEF6B6;
loc_00BEF676:
    goto loc_00BEF6A4;
loc_00BEF684:
    goto loc_00BEF56D;
loc_00BEF68E:
    goto loc_00BEF583;
loc_00BEF698:
loc_00BEF6A4:
    result = (uint32_t)(((uint32_t)(0x5746744EULL)) ^ ((uint32_t)(a3)));
    v_stack_mB8 = (uint32_t)(result);
    local_r10 = (uint32_t)(((uint32_t)(v_stack_mB8)) ^ ((uint32_t)(a3)));
loc_00BEF6B3:
loc_00BEF6B6:
    result = ExAllocatePool2(64, 216, (uint32_t)((uint32_t)(local_r10)), a4);
    if (result == 0) goto loc_00BEFA28;
    result = KeInitializeTimer(result + 64, 216, (uint32_t)((uint32_t)(local_r10)), a4);
    *(uint32_t *)(result) = 275;
    *(uint64_t *)(result + 0x18) = v_rip - 7232820;
    *(uint64_t *)(result + 0x20) = result;
    *(uint64_t *)(result + 0x38) = 0;
    *(uint64_t *)(result + 0x10) = 0;
    a2 = (216) << (32);
    result = (v_rip - 7232820) | (a2);
    a2 = (result) ^ (result);
    a2 = (a2) ^ (local_r12);
    *(uint64_t *)(result + 0xA0) = a2;
    a2 = (a2) << (32);
    result = (local_r12) | (a2);
    a2 = (result) ^ (result);
    a1 = (a2) ^ (local_r12);
    result = (a1) - (a2);
    result = (result) >> (1);
    result = (result) + (a2);
    result = (result) >> (5);
    result = (result) * (result);
    a1 = (a1) - (result);
    a1 = (uint8_t)((a1) + (1));
    *(uint8_t *)(result + 0xA8) = (uint8_t)(a1);
    a2 = (a2) << (32);
    local_r14 = (result) - (local_rdi);
    result = (result) | (a2);
    *(uint64_t *)(result + 0x88) = v_rip - 12514183;
    a2 = (result) ^ (result);
    a4 = (a2) ^ (local_r12);
    a2 = (a2) >> (1);
    a1 = (a2) >> (63);
    a1 = (a1) + (a2);
    a2 = 0;
    result = RtlpConvertFunctionEntry(local_rdi + 0 + 0 * 2 * 4, v_rip - 12514183, local_r12, a4);
    a3 = ((uint32_t)(*(uint32_t *)(result))) + (*(uint64_t *)(result + 0x88));
    result = RtlpLookupPrimaryFunctionEntry(result, *(uint64_t *)(result + 0x88), a3, a4);
    *(uint64_t *)(result + 0x80) = result;
    local_r13 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))) + (*(uint64_t *)(result + 0x88));
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x4))) - ((uint32_t)((uint32_t)(*(uint32_t *)(result)))));
    a1 = ((uint32_t)((uint32_t)(local_r14))) + (local_r13);
    v_stack_p8 = (uint32_t)(*(uint8_t *)(result + 0xA8));
    if (local_r13 >= a1) goto loc_00BEF83F;
loc_00BEF833:
    result = (local_r13) + (64);
    if (result < a1) goto loc_00BEF833;
loc_00BEF83F:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> (7));
    if ((uint32_t)(local_r11) == 0) goto loc_00BEF8B0;
loc_00BEF85E:
loc_00BEF863:
    a3 = (*(uint64_t *)(result + 0xA0)) ^ (*(uint64_t *)(local_r13));
    a3 = (a3) ^ (*(uint64_t *)(local_r13 + 0x8));
    a4 = (local_r13) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BEF863;
    a1 = (a4) - (local_r13);
    a1 = (a1) ^ (*(uint64_t *)(result + 0xA0));
    a1 = (a1) ^ (a1);
    result = (uint32_t)((local_rsi) ^ ((uint32_t)(*(uint64_t *)(result + 0x88))));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(result + 0xA8)))) ^ ((uint32_t)(result)));
    local_r10 = (uint32_t)((local_r10) & (63));
    if (condition_is_equal) { local_r10 = 1; }
    local_r11 = (uint32_t)((local_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BEF85E;
loc_00BEF8B0:
    a2 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (127));
    if (((uint32_t)(a2)) < 8) goto loc_00BEF8DC;
    result = ((uint32_t)((uint32_t)(a2))) >> (3);
loc_00BEF8C7:
    a3 = (a3) ^ (*(uint64_t *)(a4));
    a4 = (a4) + (8);
    a2 = (uint32_t)((a2) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BEF8C7;
loc_00BEF8DC:
    if ((uint32_t)(a2) == 0) goto loc_00BEF8F5;
loc_00BEF8E0:
    a3 = (a3) ^ (*(uint8_t *)(a4));
    a4 = (a4) + (1);
    a2 = (uint32_t)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00BEF8E0;
loc_00BEF8F5:
    *(uint64_t *)(result + 0x98) = a3;
    if (result >= (result + 12)) goto loc_00BEF914;
loc_00BEF908:
    result = (result) + (64);
    if (result < (result + 12)) goto loc_00BEF908;
loc_00BEF914:
    a3 = (a3) ^ (*(uint64_t *)(result));
    local_rdi = (result) + (8);
loc_00BEF926:
    a3 = (a3) ^ (*(uint8_t *)(local_rdi));
    local_rdi = (local_rdi) + (1);
    a2 = (uint32_t)((4) + (-1));
    if (condition_is_not_equal) goto loc_00BEF926;
    *(uint32_t *)(result + 0xAC) = (uint32_t)((uint32_t)(v_stack_m88));
    *(uint64_t *)(result + 0x98) = a3;
    *(uint32_t *)(result + 0x90) = (uint32_t)(local_r14);
    result = KiAreCodePatchesAllowed((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))), a2, a3, a4);
    a1 = 0;
    a1 = ((uint32_t)(result) != 0) ? 1 : 0;
    *(uint32_t *)(result + 0xB0) = (uint32_t)(a1);
    if (v_stack_m80 >= 50) {
        result = v_rip - 5151400;
        *(uint64_t *)(result + 0xC8) = result;
        *(uint64_t *)(result + 0xD0) = result;
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    a3 = (a2) ^ (a4);
    a2 = (a2) >> (26);
    a1 = (result) * (a2);
    a3 = (a3) - (a1);
    local_r10 = (0xFFFFFFFFB8797400ULL) - (a3);
    a2 = (a2) << (32);
    a3 = 0;
    result = (a4) | (a2);
    v_stack_mC8 = result;
    a2 = (result) ^ (result);
    a4 = (a2) ^ (a4);
    a2 = (a2) >> (11);
    result = (a4) * (a2);
    a4 = (a4) - (result);
    result = KeSetCoalescableTimer(result + 64, local_r10, a3, a4);
loc_00BEFA28:
    local_rsp = (local_rsp) + (168);
    return result;
loc_00BEFA3D:
loc_00BEFA44:
    v_stack_mB8 = 0xE8000009ULL;
    v_stack_p20 = *(uint64_t *)(result + 0xA0);
    result = KeBugCheckEx((uint32_t)(v_stack_mB8), 6, result, 0xFFFFFFFFC000007BULL);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00BEF294&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
