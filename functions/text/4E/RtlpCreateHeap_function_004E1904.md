# RtlpCreateHeap

- RVA: `0x004E1904`–`0x004E2460` (길이 `2,908` bytes)
- VA: `0x00000001404E1904`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF26C`
- 디코드: `620`개 명령, `2,908/2,908` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x004E1965` → [RtlGetNtGlobalFlags](../../page/AC/RtlGetNtGlobalFlags_function_00ACE530.md) (function, `0x00ACE530`)
- `0x004E19BB` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004E1ABE` → [RtlpHpFixedHeapCreate](../60/RtlpHpFixedHeapCreate_function_006038A0.md) (function, `0x006038A0`)
- `0x004E1AF7` → [DbgPrint](../35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x004E1AFC` → [RtlpHeapHandleError](../5F/RtlpHeapHandleError_function_005F12AC.md) (function, `0x005F12AC`)
- `0x004E1B1A` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004E1C60` → [ZwQuerySystemInformation](../6A/ZwQuerySystemInformation_function_006AD790.md) (function, `0x006AD790`)
- `0x004E1E20` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004E1E5C` → [ZwQueryVirtualMemory](../6A/ZwQueryVirtualMemory_function_006AD530.md) (function, `0x006AD530`)
- `0x004E1EB6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004E1EDE` → [ZwQueryVirtualMemory](../6A/ZwQueryVirtualMemory_function_006AD530.md) (function, `0x006AD530`)
- `0x004E1FFE` → [ZwAllocateVirtualMemory](../6A/ZwAllocateVirtualMemory_function_006AD3D0.md) (function, `0x006AD3D0`)
- `0x004E2043` → [ZwFreeVirtualMemory](../6A/ZwFreeVirtualMemory_function_006AD490.md) (function, `0x006AD490`)
- `0x004E20D0` → [ZwAllocateVirtualMemory](../6A/ZwAllocateVirtualMemory_function_006AD3D0.md) (function, `0x006AD3D0`)
- `0x004E20EE` → [RtlGetNtGlobalFlags](../../page/AC/RtlGetNtGlobalFlags_function_00ACE530.md) (function, `0x00ACE530`)
- `0x004E2182` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004E218C` → [RtlpCreateHeapEncoding](../5E/RtlpCreateHeapEncoding_function_005E9888.md) (function, `0x005E9888`)
- `0x004E2224` → [ExInitializeResourceLite2](../41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x004E2245` → [ExDeleteResourceLite](../38/ExDeleteResourceLite_function_0038BA60.md) (function, `0x0038BA60`)
- `0x004E226F` → [ZwFreeVirtualMemory](../6A/ZwFreeVirtualMemory_function_006AD490.md) (function, `0x006AD490`)
- `0x004E2282` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x004E22F5` → [RtlpInitializeHeapSegment](../5E/RtlpInitializeHeapSegment_function_005EB1DC.md) (function, `0x005EB1DC`)
- `0x004E230F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004E233E` → [RtlpPopulateListIndex](../5F/RtlpPopulateListIndex_function_005F1C84.md) (function, `0x005F1C84`)

### Direct callers
- [RtlCreateHeap](../../page/AC/RtlCreateHeap_function_00ACF950.md) at `0x00ACF96D`

### Static image references
- `0x004E1917` → RVA `0x00E0A740` (`.data`; read)
- `0x004E1A94` → RVA `0x00F05C00` (`.data`; read)
- `0x004E1AE3` → RVA `0x00E67B60` (`.data`; read)
- `0x004E1AF0` → RVA `0x006CC940` (` ?? ::FNODOBFM::`string'`; read)
- `0x004E1BC7` → RVA `0x00FC5238` (`ALMOSTRO`; read)
- `0x004E1BE2` → RVA `0x00FC5230` (`ALMOSTRO`; read)
- `0x004E1BFD` → RVA `0x00FC5220` (`ALMOSTRO`; read)
- `0x004E1C20` → RVA `0x00FC5228` (`ALMOSTRO`; read)
- `0x004E1C38` → RVA `0x00E67B28` (`.data`; read)
- `0x004E1C44` → RVA `0x00E67B38` (`.data`; write)
- `0x004E1C75` → RVA `0x00E67B28` (`.data`; write)
- `0x004E1C99` → RVA `0x00E67B38` (`.data`; read)
- `0x004E1F72` → RVA `0x00E28340` (`.data`; read)
- `0x004E23DE` → RVA `0x00E67B30` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x004E1965` → [RtlGetNtGlobalFlags](../../page/AC/RtlGetNtGlobalFlags_function_00ACE530.md) (`.text` → `PAGE`)
  - `0x004E20EE` → [RtlGetNtGlobalFlags](../../page/AC/RtlGetNtGlobalFlags_function_00ACE530.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004E1904  40 53                           push rbx
004E1906  56                              push rsi
004E1907  57                              push rdi
004E1908  41 54                           push r12
004E190A  41 55                           push r13
004E190C  41 56                           push r14
004E190E  41 57                           push r15
004E1910  48 81 EC D0 01 00 00            sub rsp, 0x1d0
004E1917  48 8B 05 22 8E 92 00            mov rax, qword ptr [rip + 0x928e22]
004E191E  48 33 C4                        xor rax, rsp
004E1921  48 89 84 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rax
004E1929  4D 8B F1                        mov r14, r9
004E192C  4D 8B F8                        mov r15, r8
004E192F  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
004E1934  4C 8B E2                        mov r12, rdx
004E1937  8B F9                           mov edi, ecx
004E1939  48 8B 84 24 30 02 00 00         mov rax, qword ptr [rsp + 0x230]
004E1941  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004E1946  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
004E194E  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
004E1956  48 8B B4 24 38 02 00 00         mov rsi, qword ptr [rsp + 0x238]
004E195E  33 DB                           xor ebx, ebx
004E1960  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
004E1965  E8 C6 CB 5E 00                  call 0x140ace530
004E196A  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
004E196E  0F 57 C0                        xorps xmm0, xmm0
004E1971  0F 11 84 24 20 01 00 00         movups xmmword ptr [rsp + 0x120], xmm0
004E1979  0F 11 84 24 30 01 00 00         movups xmmword ptr [rsp + 0x130], xmm0
004E1981  0F 11 84 24 40 01 00 00         movups xmmword ptr [rsp + 0x140], xmm0
004E1989  0F 57 C9                        xorps xmm1, xmm1
004E198C  0F 11 8C 24 50 01 00 00         movups xmmword ptr [rsp + 0x150], xmm1
004E1994  0F 11 8C 24 60 01 00 00         movups xmmword ptr [rsp + 0x160], xmm1
004E199C  0F 11 8C 24 70 01 00 00         movups xmmword ptr [rsp + 0x170], xmm1
004E19A4  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
004E19A8  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
004E19AD  33 D2                           xor edx, edx
004E19AF  44 8D 43 40                     lea r8d, [rbx + 0x40]
004E19B3  48 8D 8C 24 80 01 00 00         lea rcx, [rsp + 0x180]
004E19BB  E8 80 52 1E 00                  call 0x1406c6c40
004E19C0  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
004E19C5  44 8B EB                        mov r13d, ebx
004E19C8  0F BA E7 08                     bt edi, 8
004E19CC  0F 83 F9 00 00 00               jae 0x1404e1acb
004E19D2  4D 85 E4                        test r12, r12
004E19D5  0F 84 55 08 00 00               je 0x1404e2230
004E19DB  48 39 5C 24 48                  cmp qword ptr [rsp + 0x48], rbx
004E19E0  0F 85 4A 08 00 00               jne 0x1404e2230
004E19E6  40 F6 C7 02                     test dil, 2
004E19EA  0F 85 40 08 00 00               jne 0x1404e2230
004E19F0  8B CF                           mov ecx, edi
004E19F2  83 E1 FC                        and ecx, 0xfffffffc
004E19F5  C1 E1 1D                        shl ecx, 0x1d
004E19F8  8B D1                           mov edx, ecx
004E19FA  83 CA 02                        or edx, 2
004E19FD  40 F6 C7 08                     test dil, 8
004E1A01  0F 44 D1                        cmove edx, ecx
004E1A04  0F BA E7 1B                     bt edi, 0x1b
004E1A08  0F 93 C1                        setae cl
004E1A0B  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
004E1A10  41 0F BA E1 0C                  bt r9d, 0xc
004E1A15  0F 93 C0                        setae al
004E1A18  44 8B C2                        mov r8d, edx
004E1A1B  41 0F BA E8 1D                  bts r8d, 0x1d
004E1A20  84 C8                           test al, cl
004E1A22  44 0F 45 C2                     cmovne r8d, edx
004E1A26  40 F6 C7 20                     test dil, 0x20
004E1A2A  0F 94 C1                        sete cl
004E1A2D  41 F6 C1 10                     test r9b, 0x10
004E1A31  0F 94 C0                        sete al
004E1A34  41 8B D0                        mov edx, r8d
004E1A37  0F BA EA 0D                     bts edx, 0xd
004E1A3B  84 C8                           test al, cl
004E1A3D  41 0F 45 D0                     cmovne edx, r8d
004E1A41  8B CA                           mov ecx, edx
004E1A43  0F BA E9 1E                     bts ecx, 0x1e
004E1A47  0F BA E7 12                     bt edi, 0x12
004E1A4B  0F 43 CA                        cmovae ecx, edx
004E1A4E  8B D1                           mov edx, ecx
004E1A50  0F BA EA 1C                     bts edx, 0x1c
004E1A54  40 F6 C7 10                     test dil, 0x10
004E1A58  0F 44 D1                        cmove edx, ecx
004E1A5B  8B C2                           mov eax, edx
004E1A5D  0F BA E8 1B                     bts eax, 0x1b
004E1A61  0F BA E7 09                     bt edi, 9
004E1A65  0F 43 C2                        cmovae eax, edx
004E1A68  48 8B 56 48                     mov rdx, qword ptr [rsi + 0x48]
004E1A6C  48 85 D2                        test rdx, rdx
004E1A6F  74 23                           je 0x1404e1a94
004E1A71  4C 8B 76 38                     mov r14, qword ptr [rsi + 0x38]
004E1A75  4D 85 F6                        test r14, r14
004E1A78  0F 84 B2 07 00 00               je 0x1404e2230
004E1A7E  4C 8B 7E 40                     mov r15, qword ptr [rsi + 0x40]
004E1A82  4D 85 FF                        test r15, r15
004E1A85  0F 84 A5 07 00 00               je 0x1404e2230
004E1A8B  4D 3B F7                        cmp r14, r15
004E1A8E  0F 87 9C 07 00 00               ja 0x1404e2230
004E1A94  0F 10 05 65 41 A2 00            movups xmm0, xmmword ptr [rip + 0xa24165]
004E1A9B  F3 0F 7F 84 24 B0 00 00 00      movdqu xmmword ptr [rsp + 0xb0], xmm0
004E1AA4  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
004E1AAC  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
004E1AB1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
004E1AB5  4D 8B CE                        mov r9, r14
004E1AB8  4D 8B C7                        mov r8, r15
004E1ABB  49 8B CC                        mov rcx, r12
004E1ABE  E8 DD 1D 12 00                  call 0x1406038a0
004E1AC3  48 8B F8                        mov rdi, rax
004E1AC6  E9 68 07 00 00                  jmp 0x1404e2233
004E1ACB  0F BA E7 09                     bt edi, 9
004E1ACF  0F 82 5B 07 00 00               jb 0x1404e2230
004E1AD5  0F BA E7 1C                     bt edi, 0x1c
004E1AD9  72 31                           jb 0x1404e1b0c
004E1ADB  8B CF                           mov ecx, edi
004E1ADD  81 E1 00 0C F8 FF               and ecx, 0xfff80c00
004E1AE3  83 3D 76 60 98 00 02            cmp dword ptr [rip + 0x986076], 2
004E1AEA  7C 16                           jl 0x1404e1b02
004E1AEC  85 C9                           test ecx, ecx
004E1AEE  74 1C                           je 0x1404e1b0c
004E1AF0  48 8D 0D 49 AE 1E 00            lea rcx, [rip + 0x1eae49]
004E1AF7  E8 B4 71 E7 FF                  call 0x140358cb0
004E1AFC  E8 AB F7 10 00                  call 0x1405f12ac
004E1B01  CC                              int3
004E1B02  85 C9                           test ecx, ecx
004E1B04  74 06                           je 0x1404e1b0c
004E1B06  81 E7 FF F3 07 00               and edi, 0x7f3ff
004E1B0C  33 D2                           xor edx, edx
004E1B0E  44 8D 42 60                     lea r8d, [rdx + 0x60]
004E1B12  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
004E1B1A  E8 21 51 1E 00                  call 0x1406c6c40
004E1B1F  48 85 F6                        test rsi, rsi
004E1B22  74 6A                           je 0x1404e1b8e
004E1B24  83 3E 60                        cmp dword ptr [rsi], 0x60
004E1B27  75 47                           jne 0x1404e1b70
004E1B29  0F 10 06                        movups xmm0, xmmword ptr [rsi]
004E1B2C  0F 29 84 24 C0 00 00 00         movaps xmmword ptr [rsp + 0xc0], xmm0
004E1B34  0F 10 4E 10                     movups xmm1, xmmword ptr [rsi + 0x10]
004E1B38  0F 29 8C 24 D0 00 00 00         movaps xmmword ptr [rsp + 0xd0], xmm1
004E1B40  0F 10 46 20                     movups xmm0, xmmword ptr [rsi + 0x20]
004E1B44  0F 29 84 24 E0 00 00 00         movaps xmmword ptr [rsp + 0xe0], xmm0
004E1B4C  0F 10 4E 30                     movups xmm1, xmmword ptr [rsi + 0x30]
004E1B50  0F 29 8C 24 F0 00 00 00         movaps xmmword ptr [rsp + 0xf0], xmm1
004E1B58  0F 10 46 40                     movups xmm0, xmmword ptr [rsi + 0x40]
004E1B5C  0F 29 84 24 00 01 00 00         movaps xmmword ptr [rsp + 0x100], xmm0
004E1B64  0F 10 4E 50                     movups xmm1, xmmword ptr [rsi + 0x50]
004E1B68  0F 29 8C 24 10 01 00 00         movaps xmmword ptr [rsp + 0x110], xmm1
004E1B70  EB 1C                           jmp 0x1404e1b8e
004E1B72  33 FF                           xor edi, edi
004E1B74  33 DB                           xor ebx, ebx
004E1B76  44 8B EB                        mov r13d, ebx
004E1B79  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
004E1B81  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
004E1B89  E9 AA 06 00 00                  jmp 0x1404e2238
004E1B8E  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
004E1B93  8B CF                           mov ecx, edi
004E1B95  83 C9 20                        or ecx, 0x20
004E1B98  41 F6 C0 10                     test r8b, 0x10
004E1B9C  0F 44 CF                        cmove ecx, edi
004E1B9F  8B D1                           mov edx, ecx
004E1BA1  83 CA 40                        or edx, 0x40
004E1BA4  41 F6 C0 20                     test r8b, 0x20
004E1BA8  0F 44 D1                        cmove edx, ecx
004E1BAB  44 8B FA                        mov r15d, edx
004E1BAE  41 0F BA EF 07                  bts r15d, 7
004E1BB3  41 0F BA E0 15                  bt r8d, 0x15
004E1BB8  44 0F 43 FA                     cmovae r15d, edx
004E1BBC  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
004E1BC4  48 85 C9                        test rcx, rcx
004E1BC7  48 0F 44 0D 69 36 AE 00         cmove rcx, qword ptr [rip + 0xae3669]
004E1BCF  48 89 8C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rcx
004E1BD7  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
004E1BDF  48 85 C9                        test rcx, rcx
004E1BE2  48 0F 44 0D 46 36 AE 00         cmove rcx, qword ptr [rip + 0xae3646]
004E1BEA  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
004E1BF2  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
004E1BFA  48 85 C9                        test rcx, rcx
004E1BFD  48 0F 44 0D 1B 36 AE 00         cmove rcx, qword ptr [rip + 0xae361b]
004E1C05  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
004E1C0D  48 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rcx
004E1C15  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
004E1C1D  48 85 C9                        test rcx, rcx
004E1C20  48 0F 44 0D 00 36 AE 00         cmove rcx, qword ptr [rip + 0xae3600]
004E1C28  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
004E1C30  48 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rcx
004E1C38  48 8B 05 E9 5E 98 00            mov rax, qword ptr [rip + 0x985ee9]
004E1C3F  48 85 C0                        test rax, rax
004E1C42  75 38                           jne 0x1404e1c7c
004E1C44  48 C7 05 E9 5E 98 00 00 00 01 00  mov qword ptr [rip + 0x985ee9], 0x10000
004E1C4F  45 33 C9                        xor r9d, r9d
004E1C52  44 8D 40 40                     lea r8d, [rax + 0x40]
004E1C56  48 8D 94 24 80 01 00 00         lea rdx, [rsp + 0x180]
004E1C5E  33 C9                           xor ecx, ecx
004E1C60  E8 2B BB 1C 00                  call 0x1406ad790
004E1C65  85 C0                           test eax, eax
004E1C67  0F 88 C3 05 00 00               js 0x1404e2230
004E1C6D  48 8B 84 24 A8 01 00 00         mov rax, qword ptr [rsp + 0x1a8]
004E1C75  48 89 05 AC 5E 98 00            mov qword ptr [rip + 0x985eac], rax
004E1C7C  48 8B BC 24 E8 00 00 00         mov rdi, qword ptr [rsp + 0xe8]
004E1C84  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
004E1C8C  BE 00 10 00 00                  mov esi, 0x1000
004E1C91  48 85 FF                        test rdi, rdi
004E1C94  75 1D                           jne 0x1404e1cb3
004E1C96  48 8B F8                        mov rdi, rax
004E1C99  48 2B 3D 98 5E 98 00            sub rdi, qword ptr [rip + 0x985e98]
004E1CA0  48 2B FE                        sub rdi, rsi
004E1CA3  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
004E1CAB  48 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rdi
004E1CB3  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
004E1CBB  48 8D 41 FF                     lea rax, [rcx - 1]
004E1CBF  BA 00 F0 0F 00                  mov edx, 0xff000
004E1CC4  48 3D FF EF 0F 00               cmp rax, 0xfefff
004E1CCA  48 0F 47 CA                     cmova rcx, rdx
004E1CCE  48 89 8C 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rcx
004E1CD6  4D 85 F6                        test r14, r14
004E1CD9  75 07                           jne 0x1404e1ce2
004E1CDB  BA 00 20 00 00                  mov edx, 0x2000
004E1CE0  EB 0E                           jmp 0x1404e1cf0
004E1CE2  49 8D 96 FF 1F 00 00            lea rdx, [r14 + 0x1fff]
004E1CE9  48 81 E2 00 E0 FF FF            and rdx, 0xffffffffffffe000
004E1CF0  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
004E1CF5  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
004E1CFA  48 85 C9                        test rcx, rcx
004E1CFD  75 10                           jne 0x1404e1d0f
004E1CFF  48 8D 8A FF FF 00 00            lea rcx, [rdx + 0xffff]
004E1D06  48 81 E1 00 00 FF FF            and rcx, 0xffffffffffff0000
004E1D0D  EB 0E                           jmp 0x1404e1d1d
004E1D0F  48 81 C1 FF 1F 00 00            add rcx, 0x1fff
004E1D16  48 81 E1 00 E0 FF FF            and rcx, 0xffffffffffffe000
004E1D1D  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
004E1D22  4C 8B C2                        mov r8, rdx
004E1D25  48 3B D1                        cmp rdx, rcx
004E1D28  76 0B                           jbe 0x1404e1d35
004E1D2A  48 8B D1                        mov rdx, rcx
004E1D2D  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
004E1D32  4C 8B C1                        mov r8, rcx
004E1D35  41 F6 C7 02                     test r15b, 2
004E1D39  74 37                           je 0x1404e1d72
004E1D3B  4D 85 E4                        test r12, r12
004E1D3E  75 32                           jne 0x1404e1d72
004E1D40  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
004E1D48  41 8D 7C 24 02                  lea edi, [r12 + 2]
004E1D4D  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
004E1D51  48 8D 81 00 F0 FF FF            lea rax, [rcx - 0x1000]
004E1D58  49 3B C0                        cmp rax, r8
004E1D5B  73 21                           jae 0x1404e1d7e
004E1D5D  48 81 C1 FF 0F 01 00            add rcx, 0x10fff
004E1D64  48 81 E1 00 00 FF FF            and rcx, 0xffffffffffff0000
004E1D6B  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
004E1D70  EB 0C                           jmp 0x1404e1d7e
004E1D72  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
004E1D7A  8B 7C 24 60                     mov edi, dword ptr [rsp + 0x60]
004E1D7E  48 85 D2                        test rdx, rdx
004E1D81  0F 84 A9 04 00 00               je 0x1404e2230
004E1D87  48 85 C9                        test rcx, rcx
004E1D8A  0F 84 A0 04 00 00               je 0x1404e2230
004E1D90  C7 44 24 50 C8 02 00 00         mov dword ptr [rsp + 0x50], 0x2c8
004E1D98  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
004E1D9D  41 F6 C7 01                     test r15b, 1
004E1DA1  0F 85 88 00 00 00               jne 0x1404e1e2f
004E1DA7  48 85 D2                        test rdx, rdx
004E1DAA  74 05                           je 0x1404e1db1
004E1DAC  41 0F BA EF 1F                  bts r15d, 0x1f
004E1DB1  48 8B C2                        mov rax, rdx
004E1DB4  48 F7 D8                        neg rax
004E1DB7  1B C9                           sbb ecx, ecx
004E1DB9  83 E1 98                        and ecx, 0xffffff98
004E1DBC  81 C1 30 03 00 00               add ecx, 0x330
004E1DC2  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
004E1DC6  48 8B C2                        mov rax, rdx
004E1DC9  48 F7 D8                        neg rax
004E1DCC  4D 1B ED                        sbb r13, r13
004E1DCF  4C 23 EA                        and r13, rdx
004E1DD2  4D 85 E4                        test r12, r12
004E1DD5  0F 84 74 01 00 00               je 0x1404e1f4f
004E1DDB  48 39 9C 24 08 01 00 00         cmp qword ptr [rsp + 0x108], rbx
004E1DE3  74 57                           je 0x1404e1e3c
004E1DE5  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
004E1DED  48 85 C9                        test rcx, rcx
004E1DF0  74 42                           je 0x1404e1e34
004E1DF2  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
004E1DFA  48 85 C0                        test rax, rax
004E1DFD  74 35                           je 0x1404e1e34
004E1DFF  48 3B C8                        cmp rcx, rax
004E1E02  77 30                           ja 0x1404e1e34
004E1E04  41 F6 C7 02                     test r15b, 2
004E1E08  75 2A                           jne 0x1404e1e34
004E1E0A  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
004E1E0F  4D 8D 34 0C                     lea r14, [r12 + rcx]
004E1E13  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
004E1E18  4C 8B C6                        mov r8, rsi
004E1E1B  33 D2                           xor edx, edx
004E1E1D  49 8B CC                        mov rcx, r12
004E1E20  E8 1B 4E 1E 00                  call 0x1406c6c40
004E1E25  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
004E1E2A  E9 0C 01 00 00                  jmp 0x1404e1f3b
004E1E2F  48 85 D2                        test rdx, rdx
004E1E32  74 9E                           je 0x1404e1dd2
004E1E34  48 8B FB                        mov rdi, rbx
004E1E37  E9 FC 03 00 00                  jmp 0x1404e2238
004E1E3C  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
004E1E41  48 C7 44 24 20 30 00 00 00      mov qword ptr [rsp + 0x20], 0x30
004E1E4A  4C 8D 8C 24 20 01 00 00         lea r9, [rsp + 0x120]
004E1E52  45 33 C0                        xor r8d, r8d
004E1E55  49 8B D4                        mov rdx, r12
004E1E58  48 83 C9 FF                     or rcx, 0xffffffffffffffff
004E1E5C  E8 CF B6 1C 00                  call 0x1406ad530
004E1E61  85 C0                           test eax, eax
004E1E63  0F 88 C7 03 00 00               js 0x1404e2230
004E1E69  4C 8B B4 24 20 01 00 00         mov r14, qword ptr [rsp + 0x120]
004E1E71  4D 3B F4                        cmp r14, r12
004E1E74  0F 85 B6 03 00 00               jne 0x1404e2230
004E1E7A  81 BC 24 40 01 00 00 00 00 01 00  cmp dword ptr [rsp + 0x140], 0x10000
004E1E85  0F 84 A5 03 00 00               je 0x1404e2230
004E1E8B  49 8B CE                        mov rcx, r14
004E1E8E  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
004E1E93  39 B4 24 40 01 00 00            cmp dword ptr [rsp + 0x140], esi
004E1E9A  75 74                           jne 0x1404e1f10
004E1E9C  41 0F BA E7 12                  bt r15d, 0x12
004E1EA1  73 0E                           jae 0x1404e1eb1
004E1EA3  F6 84 24 44 01 00 00 40         test byte ptr [rsp + 0x144], 0x40
004E1EAB  0F 84 7F 03 00 00               je 0x1404e2230
004E1EB1  4C 8B C6                        mov r8, rsi
004E1EB4  33 D2                           xor edx, edx
004E1EB6  E8 85 4D 1E 00                  call 0x1406c6c40
004E1EBB  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
004E1EC0  48 C7 44 24 20 30 00 00 00      mov qword ptr [rsp + 0x20], 0x30
004E1EC9  4C 8D 8C 24 50 01 00 00         lea r9, [rsp + 0x150]
004E1ED1  41 B8 03 00 00 00               mov r8d, 3
004E1ED7  49 8B D4                        mov rdx, r12
004E1EDA  48 83 C9 FF                     or rcx, 0xffffffffffffffff
004E1EDE  E8 4D B6 1C 00                  call 0x1406ad530
004E1EE3  85 C0                           test eax, eax
004E1EE5  0F 88 45 03 00 00               js 0x1404e2230
004E1EEB  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
004E1EF3  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
004E1EF8  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
004E1F00  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004E1F05  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
004E1F0A  4C 8D 34 08                     lea r14, [rax + rcx]
004E1F0E  EB 2B                           jmp 0x1404e1f3b
004E1F10  48 8B 94 24 38 01 00 00         mov rdx, qword ptr [rsp + 0x138]
004E1F18  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
004E1F1D  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
004E1F22  48 3B C2                        cmp rax, rdx
004E1F25  76 08                           jbe 0x1404e1f2f
004E1F27  48 8B C2                        mov rax, rdx
004E1F2A  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
004E1F2F  48 3D 00 20 00 00               cmp rax, 0x2000
004E1F35  0F 82 F5 02 00 00               jb 0x1404e2230
004E1F3B  83 CF 01                        or edi, 1
004E1F3E  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
004E1F42  49 8B F4                        mov rsi, r12
004E1F45  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
004E1F4A  E9 5B 01 00 00                  jmp 0x1404e20aa
004E1F4F  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
004E1F54  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
004E1F5C  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
004E1F64  48 39 9C 24 08 01 00 00         cmp qword ptr [rsp + 0x108], rbx
004E1F6C  0F 85 C2 FE FF FF               jne 0x1404e1e34
004E1F72  48 8B 05 C7 63 94 00            mov rax, qword ptr [rip + 0x9463c7]
004E1F79  48 8B D0                        mov rdx, rax
004E1F7C  48 C1 EA 0C                     shr rdx, 0xc
004E1F80  48 33 D0                        xor rdx, rax
004E1F83  48 8B CA                        mov rcx, rdx
004E1F86  48 C1 E1 19                     shl rcx, 0x19
004E1F8A  48 33 D1                        xor rdx, rcx
004E1F8D  48 8B CA                        mov rcx, rdx
004E1F90  48 C1 E9 1B                     shr rcx, 0x1b
004E1F94  48 33 D1                        xor rdx, rcx
004E1F97  F0 48 0F B1 15 A0 63 94 00      lock cmpxchg qword ptr [rip + 0x9463a0], rdx
004E1FA0  75 D7                           jne 0x1404e1f79
004E1FA2  48 6B C2 FD                     imul rax, rdx, -3
004E1FA6  83 E0 1F                        and eax, 0x1f
004E1FA9  48 C1 E0 10                     shl rax, 0x10
004E1FAD  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
004E1FB5  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
004E1FBA  48 03 C1                        add rax, rcx
004E1FBD  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
004E1FC5  48 3B C1                        cmp rax, rcx
004E1FC8  73 10                           jae 0x1404e1fda
004E1FCA  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
004E1FD2  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
004E1FDA  C7 44 24 28 04 00 00 00         mov dword ptr [rsp + 0x28], 4
004E1FE2  C7 44 24 20 00 20 00 00         mov dword ptr [rsp + 0x20], 0x2000
004E1FEA  4C 8D 8C 24 88 00 00 00         lea r9, [rsp + 0x88]
004E1FF2  45 33 C0                        xor r8d, r8d
004E1FF5  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
004E1FFA  48 83 C9 FF                     or rcx, 0xffffffffffffffff
004E1FFE  E8 CD B3 1C 00                  call 0x1406ad3d0
004E2003  85 C0                           test eax, eax
004E2005  0F 88 25 02 00 00               js 0x1404e2230
004E200B  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
004E2010  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
004E2015  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
004E201D  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
004E2022  48 39 9C 24 80 00 00 00         cmp qword ptr [rsp + 0x80], rbx
004E202A  74 43                           je 0x1404e206f
004E202C  41 B9 00 80 00 00               mov r9d, 0x8000
004E2032  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
004E203A  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
004E203F  48 83 C9 FF                     or rcx, 0xffffffffffffffff
004E2043  E8 48 B4 1C 00                  call 0x1406ad490
004E2048  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
004E204D  48 03 B4 24 80 00 00 00         add rsi, qword ptr [rsp + 0x80]
004E2055  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
004E205A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
004E2062  48 2B 84 24 80 00 00 00         sub rax, qword ptr [rsp + 0x80]
004E206A  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
004E206F  48 8B CE                        mov rcx, rsi
004E2072  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
004E2077  4C 8B F6                        mov r14, rsi
004E207A  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
004E2082  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
004E208A  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
004E2092  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
004E209A  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
004E20A2  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
004E20AA  49 3B CE                        cmp rcx, r14
004E20AD  75 38                           jne 0x1404e20e7
004E20AF  C7 44 24 28 04 00 00 00         mov dword ptr [rsp + 0x28], 4
004E20B7  C7 44 24 20 00 10 00 00         mov dword ptr [rsp + 0x20], 0x1000
004E20BF  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
004E20C4  45 33 C0                        xor r8d, r8d
004E20C7  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
004E20CC  48 83 C9 FF                     or rcx, 0xffffffffffffffff
004E20D0  E8 FB B2 1C 00                  call 0x1406ad3d0
004E20D5  85 C0                           test eax, eax
004E20D7  0F 88 53 01 00 00               js 0x1404e2230
004E20DD  4C 03 74 24 68                  add r14, qword ptr [rsp + 0x68]
004E20E2  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
004E20E7  48 8D BE C8 02 00 00            lea rdi, [rsi + 0x2c8]
004E20EE  E8 3D C4 5E 00                  call 0x140ace530
004E20F3  0F BA E0 0B                     bt eax, 0xb
004E20F7  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
004E20FB  73 23                           jae 0x1404e2120
004E20FD  48 83 C7 07                     add rdi, 7
004E2101  48 83 E7 F8                     and rdi, 0xfffffffffffffff8
004E2105  48 89 BE 48 01 00 00            mov qword ptr [rsi + 0x148], rdi
004E210C  B9 10 08 00 00                  mov ecx, 0x810
004E2111  03 C1                           add eax, ecx
004E2113  48 03 F9                        add rdi, rcx
004E2116  41 0F BA EF 1A                  bts r15d, 0x1a
004E211B  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
004E2120  83 C0 0F                        add eax, 0xf
004E2123  83 E0 F0                        and eax, 0xfffffff0
004E2126  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
004E212A  C1 E8 04                        shr eax, 4
004E212D  66 89 46 08                     mov word ptr [rsi + 8], ax
004E2131  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E2136  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
004E213A  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E213F  C6 40 0F 01                     mov byte ptr [rax + 0xf], 1
004E2143  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E2148  C7 80 98 00 00 00 FF EE FF EE   mov dword ptr [rax + 0x98], 0xeeffeeff
004E2152  41 8B CF                        mov ecx, r15d
004E2155  0F BA F1 1C                     btr ecx, 0x1c
004E2159  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E215E  89 48 70                        mov dword ptr [rax + 0x70], ecx
004E2161  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E2166  89 98 90 00 00 00               mov dword ptr [rax + 0x90], ebx
004E216C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004E2171  48 81 C1 38 02 00 00            add rcx, 0x238
004E2178  BE 80 00 00 00                  mov esi, 0x80
004E217D  44 8B C6                        mov r8d, esi
004E2180  33 D2                           xor edx, edx
004E2182  E8 B9 4A 1E 00                  call 0x1406c6c40
004E2187  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004E218C  E8 F7 76 10 00                  call 0x1405e9888
004E2191  41 8B CF                        mov ecx, r15d
004E2194  81 E1 7D 00 01 60               and ecx, 0x6001007d
004E219A  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E219F  89 48 74                        mov dword ptr [rax + 0x74], ecx
004E21A2  0F B7 CF                        movzx ecx, di
004E21A5  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E21AA  66 2B C8                        sub cx, ax
004E21AD  66 89 88 D2 00 00 00            mov word ptr [rax + 0xd2], cx
004E21B4  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E21B9  48 89 98 D8 00 00 00            mov qword ptr [rax + 0xd8], rbx
004E21C0  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E21C5  48 05 50 01 00 00               add rax, 0x150
004E21CB  48 89 40 08                     mov qword ptr [rax + 8], rax
004E21CF  48 89 00                        mov qword ptr [rax], rax
004E21D2  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E21D7  48 05 10 01 00 00               add rax, 0x110
004E21DD  48 89 40 08                     mov qword ptr [rax + 8], rax
004E21E1  48 89 00                        mov qword ptr [rax], rax
004E21E4  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E21E9  48 05 20 01 00 00               add rax, 0x120
004E21EF  48 89 40 08                     mov qword ptr [rax + 8], rax
004E21F3  48 89 00                        mov qword ptr [rax], rax
004E21F6  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E21FB  48 05 F0 00 00 00               add rax, 0xf0
004E2201  48 89 40 08                     mov qword ptr [rax + 8], rax
004E2205  48 89 00                        mov qword ptr [rax], rax
004E2208  4D 85 ED                        test r13, r13
004E220B  0F 85 8E 00 00 00               jne 0x1404e229f
004E2211  41 F6 C7 01                     test r15b, 1
004E2215  0F 85 84 00 00 00               jne 0x1404e229f
004E221B  4C 8B EF                        mov r13, rdi
004E221E  83 CA FF                        or edx, 0xffffffff
004E2221  48 8B CF                        mov rcx, rdi
004E2224  E8 E7 D4 F3 FF                  call 0x14041f710
004E2229  85 C0                           test eax, eax
004E222B  79 6E                           jns 0x1404e229b
004E222D  4C 8B EB                        mov r13, rbx
004E2230  48 8B FB                        mov rdi, rbx
004E2233  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
004E2238  4D 85 ED                        test r13, r13
004E223B  74 0D                           je 0x1404e224a
004E223D  4C 3B EA                        cmp r13, rdx
004E2240  74 08                           je 0x1404e224a
004E2242  49 8B CD                        mov rcx, r13
004E2245  E8 16 98 EA FF                  call 0x14038ba60
004E224A  48 39 5C 24 40                  cmp qword ptr [rsp + 0x40], rbx
004E224F  74 23                           je 0x1404e2274
004E2251  4D 85 E4                        test r12, r12
004E2254  75 1E                           jne 0x1404e2274
004E2256  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
004E225B  41 B9 00 80 00 00               mov r9d, 0x8000
004E2261  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
004E2266  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
004E226B  48 83 C9 FF                     or rcx, 0xffffffffffffffff
004E226F  E8 1C B2 1C 00                  call 0x1406ad490
004E2274  48 8B C7                        mov rax, rdi
004E2277  48 8B 8C 24 C0 01 00 00         mov rcx, qword ptr [rsp + 0x1c0]
004E227F  48 33 CC                        xor rcx, rsp
004E2282  E8 B9 A3 1C 00                  call 0x1406ac640
004E2287  48 81 C4 D0 01 00 00            add rsp, 0x1d0
004E228E  41 5F                           pop r15
004E2290  41 5E                           pop r14
004E2292  41 5D                           pop r13
004E2294  41 5C                           pop r12
004E2296  5F                              pop rdi
004E2297  5E                              pop rsi
004E2298  5B                              pop rbx
004E2299  C3                              ret
004E229A  CC                              int3
004E229B  48 83 C7 68                     add rdi, 0x68
004E229F  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E22A4  4C 89 A8 60 01 00 00            mov qword ptr [rax + 0x160], r13
004E22AB  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E22B0  0F BA 68 78 1F                  bts dword ptr [rax + 0x78], 0x1f
004E22B5  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
004E22BA  48 2B 94 24 90 00 00 00         sub rdx, qword ptr [rsp + 0x90]
004E22C2  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
004E22C7  48 03 D1                        add rdx, rcx
004E22CA  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
004E22CF  41 81 C0 50 04 00 00            add r8d, 0x450
004E22D6  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
004E22DB  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
004E22E0  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
004E22E5  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
004E22E9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
004E22ED  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004E22F2  48 8B D1                        mov rdx, rcx
004E22F5  E8 E2 8E 10 00                  call 0x1405eb1dc
004E22FA  84 C0                           test al, al
004E22FC  0F 84 2E FF FF FF               je 0x1404e2230
004E2302  4D 85 E4                        test r12, r12
004E2305  74 0D                           je 0x1404e2314
004E2307  4C 8B C6                        mov r8, rsi
004E230A  33 D2                           xor edx, edx
004E230C  48 8B CF                        mov rcx, rdi
004E230F  E8 2C 49 1E 00                  call 0x1406c6c40
004E2314  89 77 08                        mov dword ptr [rdi + 8], esi
004E2317  48 8D 4F 38                     lea rcx, [rdi + 0x38]
004E231B  48 89 4F 28                     mov qword ptr [rdi + 0x28], rcx
004E231F  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E2324  48 05 50 01 00 00               add rax, 0x150
004E232A  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
004E232E  48 8D 41 10                     lea rax, [rcx + 0x10]
004E2332  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
004E2336  48 8B D7                        mov rdx, rdi
004E2339  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004E233E  E8 41 F9 10 00                  call 0x1405f1c84
004E2343  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E2348  66 89 98 D0 00 00 00            mov word ptr [rax + 0xd0], bx
004E234F  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E2354  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
004E235C  48 89 88 A0 00 00 00            mov qword ptr [rax + 0xa0], rcx
004E2363  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E2368  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
004E2370  48 89 88 A8 00 00 00            mov qword ptr [rax + 0xa8], rcx
004E2377  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
004E237F  48 C1 E9 04                     shr rcx, 4
004E2383  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E2388  48 89 88 B0 00 00 00            mov qword ptr [rax + 0xb0], rcx
004E238F  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
004E2397  48 C1 E9 04                     shr rcx, 4
004E239B  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E23A0  48 89 88 B8 00 00 00            mov qword ptr [rax + 0xb8], rcx
004E23A7  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E23AC  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
004E23B4  48 89 88 C8 00 00 00            mov qword ptr [rax + 0xc8], rcx
004E23BB  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
004E23C3  48 83 C1 0F                     add rcx, 0xf
004E23C7  48 C1 E9 04                     shr rcx, 4
004E23CB  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E23D0  89 88 94 00 00 00               mov dword ptr [rax + 0x94], ecx
004E23D6  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
004E23DE  48 33 0D 4B 57 98 00            xor rcx, qword ptr [rip + 0x98574b]
004E23E5  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E23EA  48 89 88 68 01 00 00            mov qword ptr [rax + 0x168], rcx
004E23F1  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E23F6  C7 80 B8 02 00 00 04 00 00 00   mov dword ptr [rax + 0x2b8], 4
004E2400  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E2405  48 C7 80 C0 02 00 00 00 E0 1F 00  mov qword ptr [rax + 0x2c0], 0x1fe000
004E2410  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E2415  48 C7 80 00 01 00 00 1F 00 00 00  mov qword ptr [rax + 0x100], 0x1f
004E2420  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
004E2425  48 C7 80 08 01 00 00 F0 FF FF FF  mov qword ptr [rax + 0x108], 0xfffffffffffffff0
004E2430  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004E2435  8B 41 70                        mov eax, dword ptr [rcx + 0x70]
004E2438  A8 20                           test al, 0x20
004E243A  74 0D                           je 0x1404e2449
004E243C  48 83 81 00 01 00 00 10         add qword ptr [rcx + 0x100], 0x10
004E2444  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004E2449  0F BA 71 78 1F                  btr dword ptr [rcx + 0x78], 0x1f
004E244E  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
004E2453  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
004E2458  4C 8B EB                        mov r13, rbx
004E245B  E9 D3 FD FF FF                  jmp 0x1404e2233
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpCreateHeap(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int8 v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p108;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pF0;

    v_rsp = (v_rsp) - (464);
    result = (*(unsigned __int64 *)(v_rip + 9604642)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m190 = a3;
    v_stack_m1C0 = a5;
    v_stack_m170 = a2;
    v_stack_m178 = a5;
    v_rbx = 0;
    v_stack_m198 = 0;
    result = RtlGetNtGlobalFlags(a1, a2, a3, a4);
    v_stack_m1B8 = (unsigned int)(result);
    v_stack_mE8 = v_xmm0;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm1;
    v_stack_mA8 = v_xmm1;
    v_stack_m98 = v_xmm1;
    v_stack_m1A8 = 0;
    v_stack_m1A0 = 0;
    a2 = 0;
    result = memset(v_stack_m88, a2, v_rbx + 64, a4);
    v_stack_m1C8 = 0;
    if (condition_is_above_or_equal) goto loc_004E1ACB;
    if (0 == 0) goto loc_004E2230;
    if (v_stack_m1C0 != 0) goto loc_004E2230;
    if ((((unsigned __int8)((unsigned int)(a1))) & (2)) != 0) goto loc_004E2230;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) & (0xFFFFFFFCULL));
    a1 = (unsigned int)((a1) << (29));
    a2 = (unsigned int)(((unsigned int)(a1)) | (2));
    if ((((unsigned __int8)((unsigned int)(a1))) & (8)) == 0) { a2 = a1; }
    a1 = (condition_is_above_or_equal) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    a3 = (unsigned int)((unsigned int)(a2));
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) { a3 = (unsigned int)(a2); }
    a1 = ((((unsigned __int8)((unsigned int)(a1))) & (32)) == 0) ? 1 : 0;
    result = ((((unsigned __int8)((unsigned int)(v_stack_m1B8))) & (16)) == 0) ? 1 : 0;
    a2 = (unsigned int)((unsigned int)(a3));
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) { a2 = (unsigned int)(a3); }
    a1 = (unsigned int)((unsigned int)(a2));
    if (condition_is_above_or_equal) { a1 = (unsigned int)(a2); }
    a2 = (unsigned int)(a1);
    if ((((unsigned __int8)((unsigned int)(a1))) & (16)) == 0) { a2 = a1; }
    result = (unsigned int)((unsigned int)(a2));
    if (condition_is_above_or_equal) { result = (unsigned int)(a2); }
    if (*(unsigned __int64 *)(a6 + 72) == 0) goto loc_004E1A94;
    if (*(unsigned __int64 *)(a6 + 56) == 0) goto loc_004E2230;
    if (*(unsigned __int64 *)(a6 + 64) == 0) goto loc_004E2230;
    if ((*(unsigned __int64 *)(a6 + 56)) > (*(unsigned __int64 *)(a6 + 64))) goto loc_004E2230;
loc_004E1A94:
    v_stack_m158 = v_xmm0;
    v_stack_m1E0 = v_stack_m158;
    v_stack_m1E8 = (unsigned int)(result);
    result = RtlpHpFixedHeapCreate(a2, *(unsigned __int64 *)(a6 + 72), *(unsigned __int64 *)(a6 + 64), *(unsigned __int64 *)(a6 + 56));
    goto loc_004E2233;
loc_004E1ACB:
    if ((*(unsigned __int64 *)(a6 + 56)) < (*(unsigned __int64 *)(a6 + 64))) goto loc_004E2230;
    if ((*(unsigned __int64 *)(a6 + 56)) < (*(unsigned __int64 *)(a6 + 64))) goto loc_004E1B0C;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0xFFF80C00ULL));
    if ((*(unsigned int *)(v_rip + 9986166)) < 2) goto loc_004E1B02;
    if (a1 == 0) goto loc_004E1B0C;
    result = DbgPrint(v_rip + 2010697, *(unsigned __int64 *)(a6 + 72), *(unsigned __int64 *)(a6 + 64), *(unsigned __int64 *)(a6 + 56));
    result = RtlpHeapHandleError(v_rip + 2010697, *(unsigned __int64 *)(a6 + 72), *(unsigned __int64 *)(a6 + 64), *(unsigned __int64 *)(a6 + 56));
loc_004E1B02:
    v_rdi = result;
    if ((unsigned int)(v_rip + 2010697) != 0) {
        v_rdi = (unsigned int)((result) & (0x7F3FFULL));
    }
    a2 = 0;
    result = memset(v_stack_m148, a2, a2 + 96, *(unsigned __int64 *)(a6 + 56));
    if (a6 == 0) goto loc_004E1B8E;
    if ((*(unsigned int *)(a6)) == 96) {
        v_stack_m148 = v_xmm0;
        v_stack_m138 = v_xmm1;
        v_stack_m128 = v_xmm0;
        v_stack_m118 = v_xmm1;
        v_stack_m108 = v_xmm0;
        v_stack_mF8 = v_xmm1;
    }
    goto loc_004E1B8E;
loc_004E1B8E:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) | (32));
    if ((((unsigned __int8)((unsigned int)(v_stack_m1B8))) & (16)) == 0) { a1 = (unsigned int)(v_rdi); }
    a2 = (unsigned int)(((unsigned int)(a1)) | (64));
    if ((((unsigned __int8)((unsigned int)(v_stack_m1B8))) & (32)) == 0) { a2 = a1; }
    v_r15 = (unsigned int)((unsigned int)(a2));
    if (condition_is_above_or_equal) { v_r15 = (unsigned int)(a2); }
    a1 = v_stack_m140;
    if (v_stack_m140 == 0) { a1 = *(unsigned __int64 *)(v_rip + 11417193); }
    v_stack_m140 = a1;
    a1 = v_stack_m138;
    if (v_stack_m138 == 0) { a1 = *(unsigned __int64 *)(v_rip + 11417158); }
    v_stack_m138 = a1;
    a1 = v_stack_m130;
    if (v_stack_m130 == 0) { a1 = *(unsigned __int64 *)(v_rip + 11417115); }
    v_stack_m170 = a1;
    v_stack_m130 = a1;
    a1 = v_stack_m128;
    if (v_stack_m128 == 0) { a1 = *(unsigned __int64 *)(v_rip + 11417088); }
    v_stack_m158 = a1;
    v_stack_m128 = a1;
    if (*(unsigned __int64 *)(v_rip + 9985769) != 0) goto loc_004E1C7C;
    *(unsigned __int64 *)(v_rip + 9985769) = 0x10000ULL;
    a4 = 0;
    a1 = 0;
    result = ZwQuerySystemInformation(a1, v_stack_m88, *(unsigned __int64 *)(v_rip + 9985769) + 64, a4);
    if (sign_flag) goto loc_004E2230;
    *(unsigned __int64 *)(v_rip + 9985708) = v_stack_m60;
loc_004E1C7C:
    v_stack_m168 = v_stack_m120;
    v_rdi = v_stack_m120;
    if (v_stack_m120 == 0) {
        v_rdi = v_stack_m60;
        v_rdi = (v_rdi) - (*(unsigned __int64 *)(v_rip + 9985688));
        v_rdi = (v_rdi) - ((unsigned int)(0x1000ULL));
        v_stack_m168 = v_rdi;
        v_stack_m120 = v_rdi;
    }
    a1 = v_stack_m118;
    if ((v_stack_m118 - 1) > 0xFEFFFULL) { a1 = (unsigned int)(0xFF000ULL); }
    v_stack_m118 = a1;
    if (*(unsigned __int64 *)(a6 + 56) != 0) goto loc_004E1CE2;
    goto loc_004E1CF0;
loc_004E1CE2:
    a2 = (*(unsigned __int64 *)(a6 + 56) + 8191) & (0xFFFFFFFFFFFFE000ULL);
loc_004E1CF0:
    v_stack_m1A0 = a2;
    if (v_stack_m190 != 0) goto loc_004E1D0F;
    a1 = (a2 + 65535) & (0xFFFFFFFFFFFF0000ULL);
    goto loc_004E1D1D;
loc_004E1D0F:
    a1 = (a1) + (0x1FFFULL);
    a1 = (a1) & (0xFFFFFFFFFFFFE000ULL);
loc_004E1D1D:
    v_stack_m1B0 = a1;
    if (a2 >= = a1) {
        a2 = a1;
        v_stack_m1A0 = a1;
        a3 = a1;
    }
    if ((((unsigned __int8)(v_r15)) & (2)) == 0) goto loc_004E1D72;
    if (a2 != 0) goto loc_004E1D72;
    v_stack_m178 = (unsigned int)(0x1000ULL);
    v_stack_m1A8 = (unsigned int)(a2 + 2);
    if ((a1 - 4096) >= a3) goto loc_004E1D7E;
    a1 = (a1) + (0x10FFFULL);
    a1 = (a1) & (0xFFFFFFFFFFFF0000ULL);
    v_stack_m1B0 = a1;
    goto loc_004E1D7E;
loc_004E1D72:
    v_stack_m178 = 0;
loc_004E1D7E:
    if (a2 == 0) goto loc_004E2230;
    if (a1 == 0) goto loc_004E2230;
    v_stack_m1B8 = 712;
    if ((((unsigned __int8)(v_r15)) & (1)) != 0) goto loc_004E1E2F;
    if (v_stack_m1C0 != 0) {
    }
    result = -(v_stack_m1C0);
    a1 = (unsigned int)((a1) & (0xFFFFFF98ULL));
    a1 = (unsigned int)((a1) + (816));
    v_stack_m1B8 = a1;
    result = -(v_stack_m1C0);
    v_r13 = (0) & (v_stack_m1C0);
loc_004E1DD2:
    if (a2 == 0) goto loc_004E1F4F;
    if (v_stack_m100 == 0) goto loc_004E1E3C;
    if (v_stack_m110 == 0) goto loc_004E1E34;
    if (v_stack_m108 == 0) goto loc_004E1E34;
    if (v_stack_m110 > v_stack_m108) goto loc_004E1E34;
    if ((((unsigned __int8)(v_r15)) & (2)) != 0) goto loc_004E1E34;
    v_stack_m198 = a2;
    v_stack_m1B0 = v_stack_m108;
    a2 = 0;
    result = memset(0, a2, (unsigned int)(0x1000ULL), a4);
    goto loc_004E1F3B;
loc_004E1E2F:
    if (0 == 0) goto loc_004E1DD2;
loc_004E1E34:
    goto loc_004E2238;
loc_004E1E3C:
    v_stack_m1E0 = 0;
    v_stack_m1E8 = 48;
    a3 = 0;
    a1 = (v_stack_m198) | (-1);
    result = ZwQueryVirtualMemory(a1, 0, a3, v_stack_mE8);
    if (sign_flag) goto loc_004E2230;
    if (v_stack_mE8 != 0) goto loc_004E2230;
    if (v_stack_mC8 == 0x10000ULL) goto loc_004E2230;
    v_stack_m198 = v_stack_mE8;
    if (v_stack_mC8 != ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_004E1F10;
    if (v_stack_mC8 >= ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_004E1EB1;
    if (((v_stack_mC4) & (64)) == 0) goto loc_004E2230;
loc_004E1EB1:
    a2 = 0;
    result = memset(v_stack_mE8, a2, (unsigned int)(0x1000ULL), v_stack_mE8);
    v_stack_m1E0 = 0;
    v_stack_m1E8 = 48;
    a1 = (v_stack_mE8) | (-1);
    result = ZwQueryVirtualMemory(a1, 0, 3, v_stack_mB8);
    if (sign_flag) goto loc_004E2230;
    v_stack_m1B0 = v_stack_mA8;
    v_stack_m1A0 = v_stack_mD0;
    goto loc_004E1F3B;
loc_004E1F10:
    v_stack_m1B0 = v_stack_mD0;
    result = v_stack_m1A0;
    if (v_stack_m1A0 >= = v_stack_mD0) {
        result = v_stack_mD0;
        v_stack_m1A0 = v_stack_mD0;
    }
    if (result < 0x2000ULL) goto loc_004E2230;
loc_004E1F3B:
    v_rdi = (unsigned int)((0) | (1));
    v_stack_m1A8 = (unsigned int)(v_rdi);
    v_stack_m1C8 = 0;
    goto loc_004E20AA;
loc_004E1F4F:
    v_stack_m190 = 0;
    v_stack_m180 = 0;
    v_stack_m188 = 0;
    if (v_stack_m100 != 0) goto loc_004E1E34;
loc_004E1F79:
    a2 = (*(unsigned __int64 *)(v_rip + 9724871)) >> (12);
    a2 = (a2) ^ (*(unsigned __int64 *)(v_rip + 9724871));
    a1 = (a2) << (25);
    a2 = (a2) ^ (a1);
    a1 = (a2) >> (27);
    a2 = (a2) ^ (a1);
    if (condition_is_not_equal) goto loc_004E1F79;
    result = (*(unsigned __int64 *)(v_rip + 9724871)) * (a2);
    result = (unsigned int)((result) & (31));
    result = (result) << (16);
    v_stack_m188 = result;
    result = (result) + (v_stack_m1B0);
    v_stack_m180 = result;
    if (result < v_stack_m1B0) {
        v_stack_m180 = v_stack_m1B0;
        v_stack_m188 = 0;
    }
    v_stack_m1E0 = 4;
    v_stack_m1E8 = 0x2000ULL;
    a3 = 0;
    a1 = (v_stack_m1B0) | (-1);
    result = ZwAllocateVirtualMemory(a1, v_stack_m190, a3, v_stack_m180);
    if (sign_flag) goto loc_004E2230;
    v_stack_m1C8 = v_stack_m190;
    v_stack_m1B0 = v_stack_m180;
    result = v_stack_m180;
    v_rsi = v_stack_m190;
    if (v_stack_m188 != 0) {
        a4 = 0x8000ULL;
        a3 = v_stack_m188;
        a2 = v_stack_m190;
        a1 = (a1) | (-1);
        result = ZwFreeVirtualMemory(a1, a2, a3, a4);
        v_rsi = v_stack_m190;
        v_rsi = (v_rsi) + (v_stack_m188);
        v_stack_m1C8 = v_rsi;
        result = v_stack_m180;
        result = (result) - (v_stack_m188);
        v_stack_m1B0 = result;
    }
    v_stack_m198 = v_rsi;
    v_stack_m168 = v_stack_m120;
    v_stack_m158 = v_stack_m128;
    v_stack_m170 = v_stack_m130;
loc_004E20AA:
    if (v_rsi != v_rsi) goto loc_004E20E7;
    v_stack_m1E0 = 4;
    v_stack_m1E8 = 0x1000ULL;
    a3 = 0;
    a1 = (v_rsi) | (-1);
    result = ZwAllocateVirtualMemory(a1, v_stack_m198, a3, v_stack_m1A0);
    if (sign_flag) goto loc_004E2230;
    v_r14 = (v_rsi) + (v_stack_m1A0);
loc_004E20E7:
    result = RtlGetNtGlobalFlags(a1, v_stack_m198, a3, v_stack_m1A0);
    result = (unsigned int)(v_stack_m1B8);
    v_rsi = v_stack_m1C8;
    v_rdi = v_stack_m1C8 + 712;
    if (!(condition_is_above_or_equal)) {
        v_rdi = (v_stack_m1C8 + 712) + (7);
        v_rdi = (v_rdi) & (-8);
        *(unsigned __int64 *)(v_stack_m1C8 + 328) = v_rdi;
        a1 = 0x810ULL;
        result = (unsigned int)(((unsigned int)(v_stack_m1B8)) + (a1));
        v_rdi = (v_rdi) + (a1);
        v_rsi = v_stack_m1C8;
    }
    result = (unsigned int)((result) + (15));
    result = (unsigned int)((result) & (0xFFFFFFF0ULL));
    v_stack_m1B8 = (unsigned int)(result);
    result = (unsigned int)((result) >> (4));
    *(unsigned __int16 *)(v_rsi + 8) = (unsigned __int16)(result);
    *(unsigned __int8 *)(v_stack_m1C8 + 10) = 1;
    *(unsigned __int8 *)(v_stack_m1C8 + 15) = 1;
    *(unsigned int *)(v_stack_m1C8 + 152) = 0xEEFFEEFFULL;
    *(unsigned int *)(v_stack_m1C8 + 112) = (unsigned int)((unsigned int)((unsigned int)(v_r15)));
    *(unsigned int *)(v_stack_m1C8 + 144) = 0;
    a1 = (v_stack_m1C8) + (568);
    a2 = 0;
    result = memset(a1, a2, 128, v_stack_m1A0);
    result = RtlpCreateHeapEncoding(v_stack_m1C8, a2, 128, v_stack_m1A0);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (0x6001007DULL));
    *(unsigned int *)(v_stack_m1C8 + 116) = a1;
    a1 = (unsigned __int16)(((unsigned __int16)(v_rdi)) - ((unsigned __int16)(v_stack_m1C8)));
    *(unsigned __int16 *)(v_stack_m1C8 + 210) = (unsigned __int16)(a1);
    *(unsigned __int64 *)(v_stack_m1C8 + 216) = 0;
    result = (v_stack_m1C8) + (336);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    result = (v_stack_m1C8) + (272);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    result = (v_stack_m1C8) + (288);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    result = (v_stack_m1C8) + (240);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    if (v_r13 != 0) goto loc_004E229F;
    if ((((unsigned __int8)(v_r15)) & (1)) != 0) goto loc_004E229F;
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    result = ExInitializeResourceLite2(v_rdi, a2, 128, v_stack_m1A0);
    if (!sign_flag) goto loc_004E229B;
loc_004E2230:
loc_004E2233:
loc_004E2238:
    if (0 == 0) goto loc_004E224A;
    if (0 != v_stack_m1C0) {
        a1 = 0;
        result = ExDeleteResourceLite(a1, v_stack_m1C0, 128, v_stack_m1A0);
    }
    if (v_stack_m1C8 == 0) goto loc_004E2274;
    if (a2 == 0) {
        v_stack_m1B0 = 0;
        a4 = 0x8000ULL;
        a3 = v_stack_m1B0;
        a2 = v_stack_m1C8;
        a1 = (a1) | (-1);
        result = ZwFreeVirtualMemory(a1, a2, a3, a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (464);
    return result;
loc_004E229B:
    v_rdi = (0) + (104);
loc_004E229F:
    *(unsigned __int64 *)(v_stack_p40 + 352) = 0;
    a2 = (v_stack_p58) - (v_stack_p90);
    a2 = (a2) + (v_stack_p70);
    a3 = (unsigned int)(((unsigned int)(v_stack_p50)) + (0x450ULL));
    v_stack_p38 = a2;
    v_stack_p30 = v_r14;
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p60));
    result = RtlpInitializeHeapSegment(v_stack_p40, v_stack_p40, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004E2230;
    if (a2 != 0) {
        a3 = 128;
        a2 = 0;
        a1 = v_rdi;
        result = memset(a1, a2, a3, a4);
    }
    *(unsigned int *)(v_rdi + 8) = 128;
    *(unsigned __int64 *)(v_rdi + 40) = v_rdi + 56;
    result = (v_stack_p40) + (336);
    *(unsigned __int64 *)(v_rdi + 32) = result;
    *(unsigned __int64 *)(v_rdi + 48) = v_rdi + 56 + 16;
    result = RtlpPopulateListIndex(v_stack_p40, v_rdi, a3, a4);
    *(unsigned __int16 *)(v_stack_p40 + 208) = 0;
    *(unsigned __int64 *)(v_stack_p40 + 160) = v_stack_pC8;
    *(unsigned __int64 *)(v_stack_p40 + 168) = v_stack_pD0;
    a1 = (v_stack_p98) >> (4);
    *(unsigned __int64 *)(v_stack_p40 + 176) = a1;
    a1 = (v_stack_pB0) >> (4);
    *(unsigned __int64 *)(v_stack_p40 + 184) = a1;
    *(unsigned __int64 *)(v_stack_p40 + 200) = v_stack_pA0;
    a1 = (v_stack_pF0) + (15);
    a1 = (a1) >> (4);
    *(unsigned int *)(v_stack_p40 + 148) = a1;
    a1 = (v_stack_p108) ^ (*(unsigned __int64 *)(v_rip + 9983819));
    *(unsigned __int64 *)(v_stack_p40 + 360) = a1;
    *(unsigned int *)(v_stack_p40 + 696) = 4;
    *(unsigned __int64 *)(v_stack_p40 + 704) = 0x1FE000ULL;
    *(unsigned __int64 *)(v_stack_p40 + 256) = 31;
    *(unsigned __int64 *)(v_stack_p40 + 264) = -16;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p40 + 112)))) & (32)) != 0) {
        a1 = v_stack_p40;
    }
    v_stack_p40 = 0;
    goto loc_004E2233;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpCreateHeap(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, void *Arg6)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m48;
    uint64_t v_stack_m60;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint8_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p108;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p70;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pF0;

    local_rsp = (local_rsp) - (464);
    result = (*(uint64_t *)(v_rip + 0x928E22)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m190 = Arg3;
    v_stack_m1C0 = Arg5;
    v_stack_m170 = Arg2;
    v_stack_m178 = Arg5;
    local_rbx = 0;
    v_stack_m198 = 0;
    result = RtlGetNtGlobalFlags(Arg1, Arg2, Arg3, Arg4);
    v_stack_m1B8 = (uint32_t)(result);
    v_stack_mE8 = v_xmm0;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm1;
    v_stack_mA8 = v_xmm1;
    v_stack_m98 = v_xmm1;
    v_stack_m1A8 = 0;
    v_stack_m1A0 = 0;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, local_rbx + 64, Arg4);
    v_stack_m1C8 = 0;
    if (condition_is_above_or_equal) goto loc_004E1ACB;
    if (0 == 0) goto loc_004E2230;
    if (v_stack_m1C0 != 0) goto loc_004E2230;
    if ((((uint8_t)((uint32_t)(Arg1))) & (2)) != 0) goto loc_004E2230;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) & (0xFFFFFFFCULL));
    Arg1 = (uint32_t)((Arg1) << (29));
    Arg2 = (uint32_t)(((uint32_t)(Arg1)) | (2));
    if ((((uint8_t)((uint32_t)(Arg1))) & (8)) == 0) { Arg2 = Arg1; }
    Arg1 = (condition_is_above_or_equal) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    Arg3 = (uint32_t)((uint32_t)(Arg2));
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) { Arg3 = (uint32_t)(Arg2); }
    Arg1 = ((((uint8_t)((uint32_t)(Arg1))) & (32)) == 0) ? 1 : 0;
    result = ((((uint8_t)((uint32_t)(v_stack_m1B8))) & (16)) == 0) ? 1 : 0;
    Arg2 = (uint32_t)((uint32_t)(Arg3));
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) { Arg2 = (uint32_t)(Arg3); }
    Arg1 = (uint32_t)((uint32_t)(Arg2));
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(Arg2); }
    Arg2 = (uint32_t)(Arg1);
    if ((((uint8_t)((uint32_t)(Arg1))) & (16)) == 0) { Arg2 = Arg1; }
    result = (uint32_t)((uint32_t)(Arg2));
    if (condition_is_above_or_equal) { result = (uint32_t)(Arg2); }
    if (*(uint64_t *)(arg6 + 0x48) == 0) goto loc_004E1A94;
    if (*(uint64_t *)(arg6 + 0x38) == 0) goto loc_004E2230;
    if (*(uint64_t *)(arg6 + 0x40) == 0) goto loc_004E2230;
    if ((*(uint64_t *)(arg6 + 0x38)) > (*(uint64_t *)(arg6 + 0x40))) goto loc_004E2230;
loc_004E1A94:
    v_stack_m158 = v_xmm0;
    v_stack_m1E0 = v_stack_m158;
    v_stack_m1E8 = (uint32_t)(result);
    result = RtlpHpFixedHeapCreate(Arg2, *(uint64_t *)(arg6 + 0x48), *(uint64_t *)(arg6 + 0x40), *(uint64_t *)(arg6 + 0x38));
    goto loc_004E2233;
loc_004E1ACB:
    if ((*(uint64_t *)(arg6 + 0x38)) < (*(uint64_t *)(arg6 + 0x40))) goto loc_004E2230;
    if ((*(uint64_t *)(arg6 + 0x38)) < (*(uint64_t *)(arg6 + 0x40))) goto loc_004E1B0C;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0xFFF80C00ULL));
    if ((*(uint32_t *)(v_rip + 0x986076)) < 2) goto loc_004E1B02;
    if (Arg1 == 0) goto loc_004E1B0C;
    result = DbgPrint(v_rip + 2010697, *(uint64_t *)(arg6 + 0x48), *(uint64_t *)(arg6 + 0x40), *(uint64_t *)(arg6 + 0x38));
    result = RtlpHeapHandleError(v_rip + 2010697, *(uint64_t *)(arg6 + 0x48), *(uint64_t *)(arg6 + 0x40), *(uint64_t *)(arg6 + 0x38));
loc_004E1B02:
    local_rdi = result;
    if ((uint32_t)(v_rip + 2010697) != 0) {
        local_rdi = (uint32_t)((result) & (0x7F3FFULL));
    }
    Arg2 = 0;
    result = memset(v_stack_m148, Arg2, Arg2 + 96, *(uint64_t *)(arg6 + 0x38));
    if (Arg6 == NULL) goto loc_004E1B8E;
    if ((*(uint32_t *)(arg6)) == 96) {
        v_stack_m148 = v_xmm0;
        v_stack_m138 = v_xmm1;
        v_stack_m128 = v_xmm0;
        v_stack_m118 = v_xmm1;
        v_stack_m108 = v_xmm0;
        v_stack_mF8 = v_xmm1;
    }
    goto loc_004E1B8E;
loc_004E1B8E:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) | (32));
    if ((((uint8_t)((uint32_t)(v_stack_m1B8))) & (16)) == 0) { Arg1 = (uint32_t)(local_rdi); }
    Arg2 = (uint32_t)(((uint32_t)(Arg1)) | (64));
    if ((((uint8_t)((uint32_t)(v_stack_m1B8))) & (32)) == 0) { Arg2 = Arg1; }
    local_r15 = (uint32_t)((uint32_t)(Arg2));
    if (condition_is_above_or_equal) { local_r15 = (uint32_t)(Arg2); }
    Arg1 = v_stack_m140;
    if (v_stack_m140 == 0) { Arg1 = *(uint64_t *)(v_rip + 0xAE3669); }
    v_stack_m140 = Arg1;
    Arg1 = v_stack_m138;
    if (v_stack_m138 == 0) { Arg1 = *(uint64_t *)(v_rip + 0xAE3646); }
    v_stack_m138 = Arg1;
    Arg1 = v_stack_m130;
    if (v_stack_m130 == 0) { Arg1 = *(uint64_t *)(v_rip + 0xAE361B); }
    v_stack_m170 = Arg1;
    v_stack_m130 = Arg1;
    Arg1 = v_stack_m128;
    if (v_stack_m128 == 0) { Arg1 = *(uint64_t *)(v_rip + 0xAE3600); }
    v_stack_m158 = Arg1;
    v_stack_m128 = Arg1;
    if (*(uint64_t *)(v_rip + 0x985EE9) != 0) goto loc_004E1C7C;
    *(uint64_t *)(v_rip + 0x985EE9) = 0x10000ULL;
    Arg4 = 0;
    Arg1 = 0;
    result = ZwQuerySystemInformation(Arg1, v_stack_m88, *(uint64_t *)(v_rip + 0x985EE9) + 64, Arg4);
    if (sign_flag) goto loc_004E2230;
    *(uint64_t *)(v_rip + 0x985EAC) = v_stack_m60;
loc_004E1C7C:
    v_stack_m168 = v_stack_m120;
    local_rdi = v_stack_m120;
    if (v_stack_m120 == 0) {
        local_rdi = v_stack_m60;
        local_rdi = (local_rdi) - (*(uint64_t *)(v_rip + 0x985E98));
        local_rdi = (local_rdi) - ((uint32_t)(0x1000ULL));
        v_stack_m168 = local_rdi;
        v_stack_m120 = local_rdi;
    }
    Arg1 = v_stack_m118;
    if ((v_stack_m118 - 1) > 0xFEFFFULL) { Arg1 = (uint32_t)(0xFF000ULL); }
    v_stack_m118 = Arg1;
    if (*(uint64_t *)(arg6 + 0x38) != 0) goto loc_004E1CE2;
    goto loc_004E1CF0;
loc_004E1CE2:
    Arg2 = (*(uint64_t *)(arg6 + 0x38) + 8191) & (0xFFFFFFFFFFFFE000ULL);
loc_004E1CF0:
    v_stack_m1A0 = Arg2;
    if (v_stack_m190 != 0) goto loc_004E1D0F;
    Arg1 = (Arg2 + 65535) & (0xFFFFFFFFFFFF0000ULL);
    goto loc_004E1D1D;
loc_004E1D0F:
    Arg1 = (Arg1) + (0x1FFFULL);
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFE000ULL);
loc_004E1D1D:
    v_stack_m1B0 = Arg1;
    if (Arg2 >= = Arg1) {
        Arg2 = Arg1;
        v_stack_m1A0 = Arg1;
        Arg3 = Arg1;
    }
    if ((((uint8_t)(local_r15)) & (2)) == 0) goto loc_004E1D72;
    if (Arg2 != 0) goto loc_004E1D72;
    v_stack_m178 = (uint32_t)(0x1000ULL);
    v_stack_m1A8 = (uint32_t)(Arg2 + 2);
    if ((Arg1 - 4096) >= Arg3) goto loc_004E1D7E;
    Arg1 = (Arg1) + (0x10FFFULL);
    Arg1 = (Arg1) & (0xFFFFFFFFFFFF0000ULL);
    v_stack_m1B0 = Arg1;
    goto loc_004E1D7E;
loc_004E1D72:
    v_stack_m178 = 0;
loc_004E1D7E:
    if (Arg2 == 0) goto loc_004E2230;
    if (Arg1 == 0) goto loc_004E2230;
    v_stack_m1B8 = 712;
    if ((((uint8_t)(local_r15)) & (1)) != 0) goto loc_004E1E2F;
    if (v_stack_m1C0 != 0) {
    }
    result = -(v_stack_m1C0);
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFF98ULL));
    Arg1 = (uint32_t)((Arg1) + (816));
    v_stack_m1B8 = Arg1;
    result = -(v_stack_m1C0);
    local_r13 = (0) & (v_stack_m1C0);
loc_004E1DD2:
    if (Arg2 == 0) goto loc_004E1F4F;
    if (v_stack_m100 == 0) goto loc_004E1E3C;
    if (v_stack_m110 == 0) goto loc_004E1E34;
    if (v_stack_m108 == 0) goto loc_004E1E34;
    if (v_stack_m110 > v_stack_m108) goto loc_004E1E34;
    if ((((uint8_t)(local_r15)) & (2)) != 0) goto loc_004E1E34;
    v_stack_m198 = Arg2;
    v_stack_m1B0 = v_stack_m108;
    Arg2 = 0;
    result = memset(0, Arg2, (uint32_t)(0x1000ULL), Arg4);
    goto loc_004E1F3B;
loc_004E1E2F:
    if (0 == 0) goto loc_004E1DD2;
loc_004E1E34:
    goto loc_004E2238;
loc_004E1E3C:
    v_stack_m1E0 = 0;
    v_stack_m1E8 = 48;
    Arg3 = 0;
    Arg1 = (v_stack_m198) | (-1);
    result = ZwQueryVirtualMemory(Arg1, 0, Arg3, v_stack_mE8);
    if (sign_flag) goto loc_004E2230;
    if (v_stack_mE8 != 0) goto loc_004E2230;
    if (v_stack_mC8 == 0x10000ULL) goto loc_004E2230;
    v_stack_m198 = v_stack_mE8;
    if (v_stack_mC8 != ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_004E1F10;
    if (v_stack_mC8 >= ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_004E1EB1;
    if (((v_stack_mC4) & (64)) == 0) goto loc_004E2230;
loc_004E1EB1:
    Arg2 = 0;
    result = memset(v_stack_mE8, Arg2, (uint32_t)(0x1000ULL), v_stack_mE8);
    v_stack_m1E0 = 0;
    v_stack_m1E8 = 48;
    Arg1 = (v_stack_mE8) | (-1);
    result = ZwQueryVirtualMemory(Arg1, 0, 3, v_stack_mB8);
    if (sign_flag) goto loc_004E2230;
    v_stack_m1B0 = v_stack_mA8;
    v_stack_m1A0 = v_stack_mD0;
    goto loc_004E1F3B;
loc_004E1F10:
    v_stack_m1B0 = v_stack_mD0;
    result = v_stack_m1A0;
    if (v_stack_m1A0 >= = v_stack_mD0) {
        result = v_stack_mD0;
        v_stack_m1A0 = v_stack_mD0;
    }
    if (result < 0x2000ULL) goto loc_004E2230;
loc_004E1F3B:
    local_rdi = (uint32_t)((0) | (1));
    v_stack_m1A8 = (uint32_t)(local_rdi);
    v_stack_m1C8 = 0;
    goto loc_004E20AA;
loc_004E1F4F:
    v_stack_m190 = 0;
    v_stack_m180 = 0;
    v_stack_m188 = 0;
    if (v_stack_m100 != 0) goto loc_004E1E34;
loc_004E1F79:
    Arg2 = (*(uint64_t *)(v_rip + 0x9463C7)) >> (12);
    Arg2 = (Arg2) ^ (*(uint64_t *)(v_rip + 0x9463C7));
    Arg1 = (Arg2) << (25);
    Arg2 = (Arg2) ^ (Arg1);
    Arg1 = (Arg2) >> (27);
    Arg2 = (Arg2) ^ (Arg1);
    if (condition_is_not_equal) goto loc_004E1F79;
    result = (*(uint64_t *)(v_rip + 0x9463C7)) * (Arg2);
    result = (uint32_t)((result) & (31));
    result = (result) << (16);
    v_stack_m188 = result;
    result = (result) + (v_stack_m1B0);
    v_stack_m180 = result;
    if (result < v_stack_m1B0) {
        v_stack_m180 = v_stack_m1B0;
        v_stack_m188 = 0;
    }
    v_stack_m1E0 = 4;
    v_stack_m1E8 = 0x2000ULL;
    Arg3 = 0;
    Arg1 = (v_stack_m1B0) | (-1);
    result = ZwAllocateVirtualMemory(Arg1, v_stack_m190, Arg3, v_stack_m180);
    if (sign_flag) goto loc_004E2230;
    v_stack_m1C8 = v_stack_m190;
    v_stack_m1B0 = v_stack_m180;
    result = v_stack_m180;
    local_rsi = v_stack_m190;
    if (v_stack_m188 != 0) {
        Arg4 = 0x8000ULL;
        Arg3 = v_stack_m188;
        Arg2 = v_stack_m190;
        Arg1 = (Arg1) | (-1);
        result = ZwFreeVirtualMemory(Arg1, Arg2, Arg3, Arg4);
        local_rsi = v_stack_m190;
        local_rsi = (local_rsi) + (v_stack_m188);
        v_stack_m1C8 = local_rsi;
        result = v_stack_m180;
        result = (result) - (v_stack_m188);
        v_stack_m1B0 = result;
    }
    v_stack_m198 = local_rsi;
    v_stack_m168 = v_stack_m120;
    v_stack_m158 = v_stack_m128;
    v_stack_m170 = v_stack_m130;
loc_004E20AA:
    if (local_rsi != local_rsi) goto loc_004E20E7;
    v_stack_m1E0 = 4;
    v_stack_m1E8 = 0x1000ULL;
    Arg3 = 0;
    Arg1 = (local_rsi) | (-1);
    result = ZwAllocateVirtualMemory(Arg1, v_stack_m198, Arg3, v_stack_m1A0);
    if (sign_flag) goto loc_004E2230;
    local_r14 = (local_rsi) + (v_stack_m1A0);
loc_004E20E7:
    result = RtlGetNtGlobalFlags(Arg1, v_stack_m198, Arg3, v_stack_m1A0);
    result = (uint32_t)(v_stack_m1B8);
    local_rsi = v_stack_m1C8;
    local_rdi = v_stack_m1C8 + 712;
    if (!(condition_is_above_or_equal)) {
        local_rdi = (v_stack_m1C8 + 712) + (7);
        local_rdi = (local_rdi) & (-8);
        *(uint64_t *)(v_stack_m1C8 + 0x148) = local_rdi;
        Arg1 = 0x810ULL;
        result = (uint32_t)(((uint32_t)(v_stack_m1B8)) + (Arg1));
        local_rdi = (local_rdi) + (Arg1);
        local_rsi = v_stack_m1C8;
    }
    result = (uint32_t)((result) + (15));
    result = (uint32_t)((result) & (0xFFFFFFF0ULL));
    v_stack_m1B8 = (uint32_t)(result);
    result = (uint32_t)((result) >> (4));
    *(uint16_t *)(local_rsi + 0x8) = (uint16_t)(result);
    *(uint8_t *)(v_stack_m1C8 + 0xA) = 1;
    *(uint8_t *)(v_stack_m1C8 + 0xF) = 1;
    *(uint32_t *)(v_stack_m1C8 + 0x98) = 0xEEFFEEFFULL;
    *(uint32_t *)(v_stack_m1C8 + 0x70) = (uint32_t)((uint32_t)((uint32_t)(local_r15)));
    *(uint32_t *)(v_stack_m1C8 + 0x90) = 0;
    Arg1 = (v_stack_m1C8) + (568);
    Arg2 = 0;
    result = memset(Arg1, Arg2, 128, v_stack_m1A0);
    result = RtlpCreateHeapEncoding(v_stack_m1C8, Arg2, 128, v_stack_m1A0);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (0x6001007DULL));
    *(uint32_t *)(v_stack_m1C8 + 0x74) = Arg1;
    Arg1 = (uint16_t)(((uint16_t)(local_rdi)) - ((uint16_t)(v_stack_m1C8)));
    *(uint16_t *)(v_stack_m1C8 + 0xD2) = (uint16_t)(Arg1);
    *(uint64_t *)(v_stack_m1C8 + 0xD8) = 0;
    result = (v_stack_m1C8) + (336);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    result = (v_stack_m1C8) + (272);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    result = (v_stack_m1C8) + (288);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    result = (v_stack_m1C8) + (240);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    if (local_r13 != 0) goto loc_004E229F;
    if ((((uint8_t)(local_r15)) & (1)) != 0) goto loc_004E229F;
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    result = ExInitializeResourceLite2(local_rdi, Arg2, 128, v_stack_m1A0);
    if (!sign_flag) goto loc_004E229B;
loc_004E2230:
loc_004E2233:
loc_004E2238:
    if (0 == 0) goto loc_004E224A;
    if (0 != v_stack_m1C0) {
        Arg1 = 0;
        result = ExDeleteResourceLite(Arg1, v_stack_m1C0, 128, v_stack_m1A0);
    }
    if (v_stack_m1C8 == 0) goto loc_004E2274;
    if (Arg2 == 0) {
        v_stack_m1B0 = 0;
        Arg4 = 0x8000ULL;
        Arg3 = v_stack_m1B0;
        Arg2 = v_stack_m1C8;
        Arg1 = (Arg1) | (-1);
        result = ZwFreeVirtualMemory(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (464);
    return result;
loc_004E229B:
    local_rdi = (0) + (104);
loc_004E229F:
    *(uint64_t *)(v_stack_p40 + 0x160) = 0;
    Arg2 = (v_stack_p58) - (v_stack_p90);
    Arg2 = (Arg2) + (v_stack_p70);
    Arg3 = (uint32_t)(((uint32_t)(v_stack_p50)) + (0x450ULL));
    v_stack_p38 = Arg2;
    v_stack_p30 = local_r14;
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p60));
    result = RtlpInitializeHeapSegment(v_stack_p40, v_stack_p40, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_004E2230;
    if (Arg2 != 0) {
        Arg3 = 128;
        Arg2 = 0;
        Arg1 = local_rdi;
        result = memset(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint32_t *)(local_rdi + 0x8) = 128;
    *(uint64_t *)(local_rdi + 0x28) = local_rdi + 56;
    result = (v_stack_p40) + (336);
    *(uint64_t *)(local_rdi + 0x20) = result;
    *(uint64_t *)(local_rdi + 0x30) = local_rdi + 56 + 16;
    result = RtlpPopulateListIndex(v_stack_p40, local_rdi, Arg3, Arg4);
    *(uint16_t *)(v_stack_p40 + 0xD0) = 0;
    *(uint64_t *)(v_stack_p40 + 0xA0) = v_stack_pC8;
    *(uint64_t *)(v_stack_p40 + 0xA8) = v_stack_pD0;
    Arg1 = (v_stack_p98) >> (4);
    *(uint64_t *)(v_stack_p40 + 0xB0) = Arg1;
    Arg1 = (v_stack_pB0) >> (4);
    *(uint64_t *)(v_stack_p40 + 0xB8) = Arg1;
    *(uint64_t *)(v_stack_p40 + 0xC8) = v_stack_pA0;
    Arg1 = (v_stack_pF0) + (15);
    Arg1 = (Arg1) >> (4);
    *(uint32_t *)(v_stack_p40 + 0x94) = Arg1;
    Arg1 = (v_stack_p108) ^ (*(uint64_t *)(v_rip + 0x98574B));
    *(uint64_t *)(v_stack_p40 + 0x168) = Arg1;
    *(uint32_t *)(v_stack_p40 + 0x2B8) = 4;
    *(uint64_t *)(v_stack_p40 + 0x2C0) = 0x1FE000ULL;
    *(uint64_t *)(v_stack_p40 + 0x100) = 31;
    *(uint64_t *)(v_stack_p40 + 0x108) = -16;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x70)))) & (32)) != 0) {
        Arg1 = v_stack_p40;
    }
    v_stack_p40 = 0;
    goto loc_004E2233;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x38` | `64` | `R` |
| `Arg6` | `+ 0x40` | `64` | `R` |
| `Arg6` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004E1904&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
