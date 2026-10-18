# RtlpMuiRegLoadLicInformation

- RVA: `0x004CB26C`–`0x004CB774` (길이 `1,288` bytes)
- VA: `0x00000001404CB26C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD630`
- 디코드: `368`개 명령, `1,288/1,288` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **39**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x004CB2DC` → [RtlpGetWindowsPolicy](../../page/70/RtlpGetWindowsPolicy_function_00703DCC.md) (function, `0x00703DCC`)
- `0x004CB2F7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004CB313` → [RtlpGetWindowsPolicy](../../page/70/RtlpGetWindowsPolicy_function_00703DCC.md) (function, `0x00703DCC`)
- `0x004CB327` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004CB343` → [RtlpGetWindowsPolicy](../../page/70/RtlpGetWindowsPolicy_function_00703DCC.md) (function, `0x00703DCC`)
- `0x004CB36C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004CB38E` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004CB39D` → [wcspbrk](../50/wcspbrk_function_005025F0.md) (function, `0x005025F0`)
- `0x004CB3C0` → [RtlInitUnicodeString](../42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x004CB3CD` → [RtlCultureNameToLCID](../../page/AA/RtlCultureNameToLCID_function_00AACEF0.md) (function, `0x00AACEF0`)
- `0x004CB3E9` → [wcspbrk](../50/wcspbrk_function_005025F0.md) (function, `0x005025F0`)
- `0x004CB40F` → [RtlInitUnicodeString](../42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x004CB41C` → [RtlCultureNameToLCID](../../page/AA/RtlCultureNameToLCID_function_00AACEF0.md) (function, `0x00AACEF0`)
- `0x004CB430` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004CB44B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004CB467` → [RtlpGetWindowsPolicy](../../page/70/RtlpGetWindowsPolicy_function_00703DCC.md) (function, `0x00703DCC`)
- `0x004CB494` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004CB4B6` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004CB4C5` → [wcspbrk](../50/wcspbrk_function_005025F0.md) (function, `0x005025F0`)
- `0x004CB4E7` → [RtlInitUnicodeString](../42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x004CB4F4` → [RtlCultureNameToLCID](../../page/AA/RtlCultureNameToLCID_function_00AACEF0.md) (function, `0x00AACEF0`)
- `0x004CB510` → [wcspbrk](../50/wcspbrk_function_005025F0.md) (function, `0x005025F0`)
- `0x004CB537` → [RtlInitUnicodeString](../42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x004CB544` → [RtlCultureNameToLCID](../../page/AA/RtlCultureNameToLCID_function_00AACEF0.md) (function, `0x00AACEF0`)
- `0x004CB558` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004CB583` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004CB59F` → [RtlpGetWindowsPolicy](../../page/70/RtlpGetWindowsPolicy_function_00703DCC.md) (function, `0x00703DCC`)
- `0x004CB5C8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004CB5EB` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004CB5FA` → [wcspbrk](../50/wcspbrk_function_005025F0.md) (function, `0x005025F0`)
- `0x004CB62B` → [wcslen](../50/wcslen_function_00501BA0.md) (function, `0x00501BA0`)
- `0x004CB655` → [RtlCultureNameToLCID](../../page/AA/RtlCultureNameToLCID_function_00AACEF0.md) (function, `0x00AACEF0`)
- `0x004CB671` → [wcspbrk](../50/wcspbrk_function_005025F0.md) (function, `0x005025F0`)
- `0x004CB690` → [RtlInitUnicodeString](../42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x004CB69D` → [RtlCultureNameToLCID](../../page/AA/RtlCultureNameToLCID_function_00AACEF0.md) (function, `0x00AACEF0`)
- `0x004CB6B2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004CB6D9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004CB6F3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004CB707` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [RtlpMuiRegLoadRegistryInfo](../../page/83/RtlpMuiRegLoadRegistryInfo_function_0083EDC4.md) at `0x0083EDDF`

### Static image references
- `0x004CB2D5` → RVA `0x006D15B0` (` ?? ::FNODOBFM::`string'`; read)
- `0x004CB30C` → RVA `0x006D1570` (` ?? ::FNODOBFM::`string'`; read)
- `0x004CB33C` → RVA `0x006D15F0` (` ?? ::FNODOBFM::`string'`; read)
- `0x004CB393` → RVA `0x006D15E0` (` ?? ::FNODOBFM::`string'`; read)
- `0x004CB460` → RVA `0x006D1430` (` ?? ::FNODOBFM::`string'`; read)
- `0x004CB598` → RVA `0x006D1400` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x004CB2DC` → [RtlpGetWindowsPolicy](../../page/70/RtlpGetWindowsPolicy_function_00703DCC.md) (`.text` → `PAGE`)
  - `0x004CB2F7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004CB313` → [RtlpGetWindowsPolicy](../../page/70/RtlpGetWindowsPolicy_function_00703DCC.md) (`.text` → `PAGE`)
  - `0x004CB327` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004CB343` → [RtlpGetWindowsPolicy](../../page/70/RtlpGetWindowsPolicy_function_00703DCC.md) (`.text` → `PAGE`)
  - `0x004CB36C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004CB3CD` → [RtlCultureNameToLCID](../../page/AA/RtlCultureNameToLCID_function_00AACEF0.md) (`.text` → `PAGE`)
  - `0x004CB41C` → [RtlCultureNameToLCID](../../page/AA/RtlCultureNameToLCID_function_00AACEF0.md) (`.text` → `PAGE`)
  - `0x004CB430` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004CB44B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004CB467` → [RtlpGetWindowsPolicy](../../page/70/RtlpGetWindowsPolicy_function_00703DCC.md) (`.text` → `PAGE`)
  - `0x004CB494` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004CB4F4` → [RtlCultureNameToLCID](../../page/AA/RtlCultureNameToLCID_function_00AACEF0.md) (`.text` → `PAGE`)
  - `0x004CB544` → [RtlCultureNameToLCID](../../page/AA/RtlCultureNameToLCID_function_00AACEF0.md) (`.text` → `PAGE`)
  - `0x004CB558` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004CB583` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004CB59F` → [RtlpGetWindowsPolicy](../../page/70/RtlpGetWindowsPolicy_function_00703DCC.md) (`.text` → `PAGE`)
  - `0x004CB5C8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004CB655` → [RtlCultureNameToLCID](../../page/AA/RtlCultureNameToLCID_function_00AACEF0.md) (`.text` → `PAGE`)
  - `0x004CB69D` → [RtlCultureNameToLCID](../../page/AA/RtlCultureNameToLCID_function_00AACEF0.md) (`.text` → `PAGE`)
  - `0x004CB6B2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004CB6D9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004CB6F3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004CB707` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004CB26C  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
004CB271  55                              push rbp
004CB272  53                              push rbx
004CB273  56                              push rsi
004CB274  57                              push rdi
004CB275  41 54                           push r12
004CB277  41 55                           push r13
004CB279  41 56                           push r14
004CB27B  41 57                           push r15
004CB27D  48 8B EC                        mov rbp, rsp
004CB280  48 83 EC 68                     sub rsp, 0x68
004CB284  83 4D EC FF                     or dword ptr [rbp - 0x14], 0xffffffff
004CB288  33 F6                           xor esi, esi
004CB28A  89 75 58                        mov dword ptr [rbp + 0x58], esi
004CB28D  0F 57 C0                        xorps xmm0, xmm0
004CB290  89 75 60                        mov dword ptr [rbp + 0x60], esi
004CB293  48 8B F9                        mov rdi, rcx
004CB296  89 75 50                        mov dword ptr [rbp + 0x50], esi
004CB299  44 8B E6                        mov r12d, esi
004CB29C  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
004CB2A0  44 8B FE                        mov r15d, esi
004CB2A3  89 75 C4                        mov dword ptr [rbp - 0x3c], esi
004CB2A6  44 8B F6                        mov r14d, esi
004CB2A9  89 75 C0                        mov dword ptr [rbp - 0x40], esi
004CB2AC  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
004CB2B0  89 75 C8                        mov dword ptr [rbp - 0x38], esi
004CB2B3  89 75 E8                        mov dword ptr [rbp - 0x18], esi
004CB2B6  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
004CB2BA  48 85 C9                        test rcx, rcx
004CB2BD  75 0A                           jne 0x1404cb2c9
004CB2BF  BB 0D 00 00 C0                  mov ebx, 0xc000000d
004CB2C4  E9 49 04 00 00                  jmp 0x1404cb712
004CB2C9  4C 8D 4D B8                     lea r9, [rbp - 0x48]
004CB2CD  4C 8D 45 50                     lea r8, [rbp + 0x50]
004CB2D1  48 8D 55 60                     lea rdx, [rbp + 0x60]
004CB2D5  48 8D 0D D4 62 20 00            lea rcx, [rip + 0x2062d4]
004CB2DC  E8 EB 8A 23 00                  call 0x140703dcc
004CB2E1  85 C0                           test eax, eax
004CB2E3  78 1B                           js 0x1404cb300
004CB2E5  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
004CB2E9  C7 45 E8 01 00 00 00            mov dword ptr [rbp - 0x18], 1
004CB2F0  48 85 C9                        test rcx, rcx
004CB2F3  74 07                           je 0x1404cb2fc
004CB2F5  33 D2                           xor edx, edx
004CB2F7  E8 74 75 6B 00                  call 0x140b82870
004CB2FC  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
004CB300  4C 8D 4D B8                     lea r9, [rbp - 0x48]
004CB304  4C 8D 45 50                     lea r8, [rbp + 0x50]
004CB308  48 8D 55 60                     lea rdx, [rbp + 0x60]
004CB30C  48 8D 0D 5D 62 20 00            lea rcx, [rip + 0x20625d]
004CB313  E8 B4 8A 23 00                  call 0x140703dcc
004CB318  85 C0                           test eax, eax
004CB31A  78 14                           js 0x1404cb330
004CB31C  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
004CB320  33 D2                           xor edx, edx
004CB322  8B 01                           mov eax, dword ptr [rcx]
004CB324  89 45 EC                        mov dword ptr [rbp - 0x14], eax
004CB327  E8 44 75 6B 00                  call 0x140b82870
004CB32C  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
004CB330  4C 8D 4D B8                     lea r9, [rbp - 0x48]
004CB334  4C 8D 45 50                     lea r8, [rbp + 0x50]
004CB338  48 8D 55 60                     lea rdx, [rbp + 0x60]
004CB33C  48 8D 0D AD 62 20 00            lea rcx, [rip + 0x2062ad]
004CB343  E8 84 8A 23 00                  call 0x140703dcc
004CB348  85 C0                           test eax, eax
004CB34A  0F 88 04 01 00 00               js 0x1404cb454
004CB350  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
004CB353  83 C0 04                        add eax, 4
004CB356  89 45 C4                        mov dword ptr [rbp - 0x3c], eax
004CB359  0F 84 0B 02 00 00               je 0x1404cb56a
004CB35F  8B D0                           mov edx, eax
004CB361  B9 00 01 00 00                  mov ecx, 0x100
004CB366  41 B8 6D 6C 74 72               mov r8d, 0x72746c6d
004CB36C  E8 7F 6D 6B 00                  call 0x140b820f0
004CB371  48 8B D8                        mov rbx, rax
004CB374  4C 8B E0                        mov r12, rax
004CB377  48 85 C0                        test rax, rax
004CB37A  0F 84 EA 01 00 00               je 0x1404cb56a
004CB380  4C 8B 6D B8                     mov r13, qword ptr [rbp - 0x48]
004CB384  48 8B C8                        mov rcx, rax
004CB387  44 8B 45 50                     mov r8d, dword ptr [rbp + 0x50]
004CB38B  49 8B D5                        mov rdx, r13
004CB38E  E8 AD B4 1F 00                  call 0x1406c6840
004CB393  48 8D 15 46 62 20 00            lea rdx, [rip + 0x206246]
004CB39A  48 8B CB                        mov rcx, rbx
004CB39D  E8 4E 72 03 00                  call 0x1405025f0
004CB3A2  33 C9                           xor ecx, ecx
004CB3A4  48 85 C0                        test rax, rax
004CB3A7  74 5A                           je 0x1404cb403
004CB3A9  4C 8B F0                        mov r14, rax
004CB3AC  8D 79 02                        lea edi, [rcx + 2]
004CB3AF  45 33 ED                        xor r13d, r13d
004CB3B2  66 45 89 2E                     mov word ptr [r14], r13w
004CB3B6  48 8D 4D D8                     lea rcx, [rbp - 0x28]
004CB3BA  48 8B D3                        mov rdx, rbx
004CB3BD  4C 03 F7                        add r14, rdi
004CB3C0  E8 BB F3 F5 FF                  call 0x14042a780
004CB3C5  48 8D 55 58                     lea rdx, [rbp + 0x58]
004CB3C9  48 8D 4D D8                     lea rcx, [rbp - 0x28]
004CB3CD  E8 1E 1B 5E 00                  call 0x140aacef0
004CB3D2  8D 4E 01                        lea ecx, [rsi + 1]
004CB3D5  84 C0                           test al, al
004CB3D7  48 8D 15 02 62 20 00            lea rdx, [rip + 0x206202]
004CB3DE  49 8B DE                        mov rbx, r14
004CB3E1  0F 44 CE                        cmove ecx, esi
004CB3E4  8B F1                           mov esi, ecx
004CB3E6  49 8B CE                        mov rcx, r14
004CB3E9  E8 02 72 03 00                  call 0x1405025f0
004CB3EE  4C 8B F0                        mov r14, rax
004CB3F1  48 85 C0                        test rax, rax
004CB3F4  75 BC                           jne 0x1404cb3b2
004CB3F6  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
004CB3FA  45 8B F5                        mov r14d, r13d
004CB3FD  4C 8B 6D B8                     mov r13, qword ptr [rbp - 0x48]
004CB401  33 C9                           xor ecx, ecx
004CB403  66 39 0B                        cmp word ptr [rbx], cx
004CB406  74 1F                           je 0x1404cb427
004CB408  48 8B D3                        mov rdx, rbx
004CB40B  48 8D 4D D8                     lea rcx, [rbp - 0x28]
004CB40F  E8 6C F3 F5 FF                  call 0x14042a780
004CB414  48 8D 55 58                     lea rdx, [rbp + 0x58]
004CB418  48 8D 4D D8                     lea rcx, [rbp - 0x28]
004CB41C  E8 CF 1A 5E 00                  call 0x140aacef0
004CB421  84 C0                           test al, al
004CB423  74 02                           je 0x1404cb427
004CB425  FF C6                           inc esi
004CB427  85 F6                           test esi, esi
004CB429  75 14                           jne 0x1404cb43f
004CB42B  33 D2                           xor edx, edx
004CB42D  49 8B CC                        mov rcx, r12
004CB430  E8 3B 74 6B 00                  call 0x140b82870
004CB435  33 F6                           xor esi, esi
004CB437  89 75 C4                        mov dword ptr [rbp - 0x3c], esi
004CB43A  44 8B E6                        mov r12d, esi
004CB43D  EB 02                           jmp 0x1404cb441
004CB43F  33 F6                           xor esi, esi
004CB441  4D 85 ED                        test r13, r13
004CB444  74 0A                           je 0x1404cb450
004CB446  33 D2                           xor edx, edx
004CB448  49 8B CD                        mov rcx, r13
004CB44B  E8 20 74 6B 00                  call 0x140b82870
004CB450  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
004CB454  4C 8D 4D B8                     lea r9, [rbp - 0x48]
004CB458  4C 8D 45 50                     lea r8, [rbp + 0x50]
004CB45C  48 8D 55 60                     lea rdx, [rbp + 0x60]
004CB460  48 8D 0D C9 5F 20 00            lea rcx, [rip + 0x205fc9]
004CB467  E8 60 89 23 00                  call 0x140703dcc
004CB46C  85 C0                           test eax, eax
004CB46E  0F 88 18 01 00 00               js 0x1404cb58c
004CB474  44 8B 75 50                     mov r14d, dword ptr [rbp + 0x50]
004CB478  41 83 C6 04                     add r14d, 4
004CB47C  44 89 75 C0                     mov dword ptr [rbp - 0x40], r14d
004CB480  0F 84 3C 02 00 00               je 0x1404cb6c2
004CB486  41 8B D6                        mov edx, r14d
004CB489  B9 00 01 00 00                  mov ecx, 0x100
004CB48E  41 B8 6D 6C 74 72               mov r8d, 0x72746c6d
004CB494  E8 57 6C 6B 00                  call 0x140b820f0
004CB499  48 8B D8                        mov rbx, rax
004CB49C  4C 8B F8                        mov r15, rax
004CB49F  48 85 C0                        test rax, rax
004CB4A2  0F 84 1D 02 00 00               je 0x1404cb6c5
004CB4A8  4C 8B 6D B8                     mov r13, qword ptr [rbp - 0x48]
004CB4AC  48 8B C8                        mov rcx, rax
004CB4AF  44 8B 45 50                     mov r8d, dword ptr [rbp + 0x50]
004CB4B3  49 8B D5                        mov rdx, r13
004CB4B6  E8 85 B3 1F 00                  call 0x1406c6840
004CB4BB  48 8D 15 1E 61 20 00            lea rdx, [rip + 0x20611e]
004CB4C2  48 8B CB                        mov rcx, rbx
004CB4C5  E8 26 71 03 00                  call 0x1405025f0
004CB4CA  48 85 C0                        test rax, rax
004CB4CD  74 5A                           je 0x1404cb529
004CB4CF  45 33 ED                        xor r13d, r13d
004CB4D2  4C 8B F0                        mov r14, rax
004CB4D5  41 8D 7D 02                     lea edi, [r13 + 2]
004CB4D9  66 45 89 2E                     mov word ptr [r14], r13w
004CB4DD  48 8D 4D D8                     lea rcx, [rbp - 0x28]
004CB4E1  48 8B D3                        mov rdx, rbx
004CB4E4  4C 03 F7                        add r14, rdi
004CB4E7  E8 94 F2 F5 FF                  call 0x14042a780
004CB4EC  48 8D 55 58                     lea rdx, [rbp + 0x58]
004CB4F0  48 8D 4D D8                     lea rcx, [rbp - 0x28]
004CB4F4  E8 F7 19 5E 00                  call 0x140aacef0
004CB4F9  8D 4E 01                        lea ecx, [rsi + 1]
004CB4FC  84 C0                           test al, al
004CB4FE  48 8D 15 DB 60 20 00            lea rdx, [rip + 0x2060db]
004CB505  49 8B DE                        mov rbx, r14
004CB508  0F 44 CE                        cmove ecx, esi
004CB50B  8B F1                           mov esi, ecx
004CB50D  49 8B CE                        mov rcx, r14
004CB510  E8 DB 70 03 00                  call 0x1405025f0
004CB515  4C 8B F0                        mov r14, rax
004CB518  48 85 C0                        test rax, rax
004CB51B  75 BC                           jne 0x1404cb4d9
004CB51D  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
004CB521  44 8B 75 C0                     mov r14d, dword ptr [rbp - 0x40]
004CB525  4C 8B 6D B8                     mov r13, qword ptr [rbp - 0x48]
004CB529  33 C0                           xor eax, eax
004CB52B  66 39 03                        cmp word ptr [rbx], ax
004CB52E  74 1F                           je 0x1404cb54f
004CB530  48 8B D3                        mov rdx, rbx
004CB533  48 8D 4D D8                     lea rcx, [rbp - 0x28]
004CB537  E8 44 F2 F5 FF                  call 0x14042a780
004CB53C  48 8D 55 58                     lea rdx, [rbp + 0x58]
004CB540  48 8D 4D D8                     lea rcx, [rbp - 0x28]
004CB544  E8 A7 19 5E 00                  call 0x140aacef0
004CB549  84 C0                           test al, al
004CB54B  74 02                           je 0x1404cb54f
004CB54D  FF C6                           inc esi
004CB54F  85 F6                           test esi, esi
004CB551  75 24                           jne 0x1404cb577
004CB553  33 D2                           xor edx, edx
004CB555  49 8B CF                        mov rcx, r15
004CB558  E8 13 73 6B 00                  call 0x140b82870
004CB55D  33 F6                           xor esi, esi
004CB55F  44 8B F6                        mov r14d, esi
004CB562  89 75 C0                        mov dword ptr [rbp - 0x40], esi
004CB565  44 8B FE                        mov r15d, esi
004CB568  EB 0F                           jmp 0x1404cb579
004CB56A  89 75 C4                        mov dword ptr [rbp - 0x3c], esi
004CB56D  BB 17 00 00 C0                  mov ebx, 0xc0000017
004CB572  E9 71 01 00 00                  jmp 0x1404cb6e8
004CB577  33 F6                           xor esi, esi
004CB579  4D 85 ED                        test r13, r13
004CB57C  74 0A                           je 0x1404cb588
004CB57E  33 D2                           xor edx, edx
004CB580  49 8B CD                        mov rcx, r13
004CB583  E8 E8 72 6B 00                  call 0x140b82870
004CB588  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
004CB58C  4C 8D 4D B8                     lea r9, [rbp - 0x48]
004CB590  4C 8D 45 50                     lea r8, [rbp + 0x50]
004CB594  48 8D 55 60                     lea rdx, [rbp + 0x60]
004CB598  48 8D 0D 61 5E 20 00            lea rcx, [rip + 0x205e61]
004CB59F  E8 28 88 23 00                  call 0x140703dcc
004CB5A4  85 C0                           test eax, eax
004CB5A6  0F 88 36 01 00 00               js 0x1404cb6e2
004CB5AC  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
004CB5AF  83 C0 04                        add eax, 4
004CB5B2  89 45 C8                        mov dword ptr [rbp - 0x38], eax
004CB5B5  0F 84 AD 01 00 00               je 0x1404cb768
004CB5BB  8B D0                           mov edx, eax
004CB5BD  B9 00 01 00 00                  mov ecx, 0x100
004CB5C2  41 B8 6D 6C 74 72               mov r8d, 0x72746c6d
004CB5C8  E8 23 6B 6B 00                  call 0x140b820f0
004CB5CD  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
004CB5D1  48 8B D8                        mov rbx, rax
004CB5D4  48 85 C0                        test rax, rax
004CB5D7  0F 84 8F 01 00 00               je 0x1404cb76c
004CB5DD  4C 8B 6D B8                     mov r13, qword ptr [rbp - 0x48]
004CB5E1  48 8B C8                        mov rcx, rax
004CB5E4  44 8B 45 50                     mov r8d, dword ptr [rbp + 0x50]
004CB5E8  49 8B D5                        mov rdx, r13
004CB5EB  E8 50 B2 1F 00                  call 0x1406c6840
004CB5F0  48 8D 15 E9 5F 20 00            lea rdx, [rip + 0x205fe9]
004CB5F7  48 8B CB                        mov rcx, rbx
004CB5FA  E8 F1 6F 03 00                  call 0x1405025f0
004CB5FF  4C 8B F0                        mov r14, rax
004CB602  48 89 5D D0                     mov qword ptr [rbp - 0x30], rbx
004CB606  33 C0                           xor eax, eax
004CB608  4D 85 F6                        test r14, r14
004CB60B  74 77                           je 0x1404cb684
004CB60D  48 89 5D D0                     mov qword ptr [rbp - 0x30], rbx
004CB611  8D 78 02                        lea edi, [rax + 2]
004CB614  66 41 89 06                     mov word ptr [r14], ax
004CB618  4C 03 F7                        add r14, rdi
004CB61B  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
004CB61F  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
004CB623  48 85 DB                        test rbx, rbx
004CB626  74 25                           je 0x1404cb64d
004CB628  48 8B CB                        mov rcx, rbx
004CB62B  E8 70 65 03 00                  call 0x140501ba0
004CB630  48 03 C0                        add rax, rax
004CB633  B9 FC FF 00 00                  mov ecx, 0xfffc
004CB638  48 3D FE FF 00 00               cmp rax, 0xfffe
004CB63E  48 0F 43 C1                     cmovae rax, rcx
004CB642  66 89 45 D8                     mov word ptr [rbp - 0x28], ax
004CB646  66 03 C7                        add ax, di
004CB649  66 89 45 DA                     mov word ptr [rbp - 0x26], ax
004CB64D  48 8D 55 58                     lea rdx, [rbp + 0x58]
004CB651  48 8D 4D D8                     lea rcx, [rbp - 0x28]
004CB655  E8 96 18 5E 00                  call 0x140aacef0
004CB65A  8D 4E 01                        lea ecx, [rsi + 1]
004CB65D  84 C0                           test al, al
004CB65F  48 8D 15 7A 5F 20 00            lea rdx, [rip + 0x205f7a]
004CB666  49 8B DE                        mov rbx, r14
004CB669  0F 44 CE                        cmove ecx, esi
004CB66C  8B F1                           mov esi, ecx
004CB66E  49 8B CE                        mov rcx, r14
004CB671  E8 7A 6F 03 00                  call 0x1405025f0
004CB676  4C 8B F0                        mov r14, rax
004CB679  33 C0                           xor eax, eax
004CB67B  4D 85 F6                        test r14, r14
004CB67E  75 94                           jne 0x1404cb614
004CB680  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
004CB684  66 39 03                        cmp word ptr [rbx], ax
004CB687  74 1F                           je 0x1404cb6a8
004CB689  48 8B D3                        mov rdx, rbx
004CB68C  48 8D 4D D8                     lea rcx, [rbp - 0x28]
004CB690  E8 EB F0 F5 FF                  call 0x14042a780
004CB695  48 8D 55 58                     lea rdx, [rbp + 0x58]
004CB699  48 8D 4D D8                     lea rcx, [rbp - 0x28]
004CB69D  E8 4E 18 5E 00                  call 0x140aacef0
004CB6A2  84 C0                           test al, al
004CB6A4  74 02                           je 0x1404cb6a8
004CB6A6  FF C6                           inc esi
004CB6A8  85 F6                           test esi, esi
004CB6AA  75 21                           jne 0x1404cb6cd
004CB6AC  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
004CB6B0  33 D2                           xor edx, edx
004CB6B2  E8 B9 71 6B 00                  call 0x140b82870
004CB6B7  33 F6                           xor esi, esi
004CB6B9  89 75 C8                        mov dword ptr [rbp - 0x38], esi
004CB6BC  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
004CB6C0  EB 0D                           jmp 0x1404cb6cf
004CB6C2  4C 8B FE                        mov r15, rsi
004CB6C5  44 8B F6                        mov r14d, esi
004CB6C8  E9 A0 FE FF FF                  jmp 0x1404cb56d
004CB6CD  33 F6                           xor esi, esi
004CB6CF  4D 85 ED                        test r13, r13
004CB6D2  74 0A                           je 0x1404cb6de
004CB6D4  33 D2                           xor edx, edx
004CB6D6  49 8B CD                        mov rcx, r13
004CB6D9  E8 92 71 6B 00                  call 0x140b82870
004CB6DE  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
004CB6E2  44 8B 75 C0                     mov r14d, dword ptr [rbp - 0x40]
004CB6E6  8B DE                           mov ebx, esi
004CB6E8  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
004CB6EC  48 85 C9                        test rcx, rcx
004CB6EF  74 07                           je 0x1404cb6f8
004CB6F1  33 D2                           xor edx, edx
004CB6F3  E8 78 71 6B 00                  call 0x140b82870
004CB6F8  4D 85 E4                        test r12, r12
004CB6FB  74 15                           je 0x1404cb712
004CB6FD  4D 85 FF                        test r15, r15
004CB700  74 10                           je 0x1404cb712
004CB702  33 D2                           xor edx, edx
004CB704  49 8B CF                        mov rcx, r15
004CB707  E8 64 71 6B 00                  call 0x140b82870
004CB70C  4C 8B FE                        mov r15, rsi
004CB70F  44 8B F6                        mov r14d, esi
004CB712  8B 45 E8                        mov eax, dword ptr [rbp - 0x18]
004CB715  0F BA 2F 0B                     bts dword ptr [rdi], 0xb
004CB719  89 47 74                        mov dword ptr [rdi + 0x74], eax
004CB71C  8B 45 EC                        mov eax, dword ptr [rbp - 0x14]
004CB71F  89 47 78                        mov dword ptr [rdi + 0x78], eax
004CB722  8B 45 C4                        mov eax, dword ptr [rbp - 0x3c]
004CB725  89 87 94 00 00 00               mov dword ptr [rdi + 0x94], eax
004CB72B  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
004CB72F  48 89 87 88 00 00 00            mov qword ptr [rdi + 0x88], rax
004CB736  8B 45 C8                        mov eax, dword ptr [rbp - 0x38]
004CB739  89 87 90 00 00 00               mov dword ptr [rdi + 0x90], eax
004CB73F  8B C3                           mov eax, ebx
004CB741  4C 89 A7 80 00 00 00            mov qword ptr [rdi + 0x80], r12
004CB748  4C 89 BF 98 00 00 00            mov qword ptr [rdi + 0x98], r15
004CB74F  44 89 B7 A0 00 00 00            mov dword ptr [rdi + 0xa0], r14d
004CB756  48 83 C4 68                     add rsp, 0x68
004CB75A  41 5F                           pop r15
004CB75C  41 5E                           pop r14
004CB75E  41 5D                           pop r13
004CB760  41 5C                           pop r12
004CB762  5F                              pop rdi
004CB763  5E                              pop rsi
004CB764  5B                              pop rbx
004CB765  5D                              pop rbp
004CB766  C3                              ret
004CB767  CC                              int3
004CB768  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
004CB76C  89 75 C8                        mov dword ptr [rbp - 0x38], esi
004CB76F  E9 F9 FD FF FF                  jmp 0x1404cb56d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpMuiRegLoadLicInformation(__int64 a1)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int16 v_stack_m66;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    v_rsi = 0;
    v_stack_p18 = 0;
    v_stack_p20 = 0;
    v_stack_p10 = 0;
    v_stack_m88 = 0;
    v_stack_m7C = 0;
    v_stack_m80 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = v_xmm0;
    if (a1 != 0) goto loc_004CB2C9;
    goto loc_004CB712;
loc_004CB2C9:
    result = RtlpGetWindowsPolicy(v_rip + 2122452, v_stack_p20, v_stack_p10, v_stack_m88);
    if (sign_flag) goto loc_004CB300;
    v_stack_m58 = 1;
    if (v_stack_m88 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m88, a2, v_stack_p10, v_stack_m88);
    }
    v_stack_m88 = 0;
loc_004CB300:
    result = RtlpGetWindowsPolicy(v_rip + 2122333, v_stack_p20, v_stack_p10, v_stack_m88);
    if (!(sign_flag)) {
        a1 = v_stack_m88;
        a2 = 0;
        result = *(unsigned int *)(a1);
        v_stack_m54 = (unsigned int)(result);
        result = ExFreePoolWithTag(a1, a2, v_stack_p10, v_stack_m88);
        v_stack_m88 = 0;
    }
    result = RtlpGetWindowsPolicy(v_rip + 2122413, v_stack_p20, v_stack_p10, v_stack_m88);
    if (sign_flag) goto loc_004CB454;
    result = (unsigned int)(((unsigned int)(v_stack_p10)) + (4));
    v_stack_m7C = (unsigned int)(result);
    if (condition_is_equal) goto loc_004CB56A;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x72746C6DULL), v_stack_m88);
    if (result == 0) goto loc_004CB56A;
    result = memcpy(result, v_stack_m88, (unsigned int)(v_stack_p10), v_stack_m88);
    result = wcspbrk(result, v_rip + 2122310, (unsigned int)(v_stack_p10), v_stack_m88);
    a1 = 0;
    if (result == 0) goto loc_004CB403;
    v_r13 = 0;
loc_004CB3B2:
    *(unsigned __int16 *)(result) = 0;
    v_r14 = (result) + (a1 + 2);
    result = RtlInitUnicodeString(v_stack_m68, result, (unsigned int)(v_stack_p10), v_stack_m88);
    result = RtlCultureNameToLCID(v_stack_m68, v_stack_p18, (unsigned int)(v_stack_p10), v_stack_m88);
    a1 = v_rsi + 1;
    if ((unsigned __int8)(result) == 0) { a1 = 0; }
    result = wcspbrk(v_r14, v_rip + 2122242, (unsigned int)(v_stack_p10), v_stack_m88);
    if (result != 0) goto loc_004CB3B2;
    a1 = 0;
loc_004CB403:
    if ((*(unsigned __int16 *)(v_r14)) == 0) goto loc_004CB427;
    result = RtlInitUnicodeString(v_stack_m68, v_r14, (unsigned int)(v_stack_p10), v_stack_m88);
    result = RtlCultureNameToLCID(v_stack_m68, v_stack_p18, (unsigned int)(v_stack_p10), v_stack_m88);
    v_rsi = (unsigned int)((unsigned int)(a1));
    if ((unsigned __int8)(result) != 0) {
        v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a1))) + 1);
    }
    if ((unsigned int)(v_rsi) != 0) goto loc_004CB43F;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(v_stack_p10), v_stack_m88);
    v_rsi = 0;
    v_stack_m7C = 0;
    goto loc_004CB441;
loc_004CB43F:
    v_rsi = 0;
loc_004CB441:
    if (v_stack_m88 != 0) {
        a2 = 0;
        a1 = v_stack_m88;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(v_stack_p10), v_stack_m88);
    }
    v_stack_m88 = 0;
loc_004CB454:
    result = RtlpGetWindowsPolicy(v_rip + 2121673, v_stack_p20, v_stack_p10, v_stack_m88);
    if (sign_flag) goto loc_004CB58C;
    v_r14 = (unsigned int)(((unsigned int)(v_stack_p10)) + (4));
    v_stack_m80 = (unsigned int)(v_r14);
    if (condition_is_equal) goto loc_004CB6C2;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(0x72746C6DULL), v_stack_m88);
    if (result == 0) goto loc_004CB6C5;
    result = memcpy(result, v_stack_m88, (unsigned int)(v_stack_p10), v_stack_m88);
    result = wcspbrk(result, v_rip + 2122014, (unsigned int)(v_stack_p10), v_stack_m88);
    if (result == 0) goto loc_004CB529;
    v_r13 = 0;
loc_004CB4D9:
    *(unsigned __int16 *)(result) = 0;
    v_r14 = (result) + (v_r13 + 2);
    result = RtlInitUnicodeString(v_stack_m68, result, (unsigned int)(v_stack_p10), v_stack_m88);
    result = RtlCultureNameToLCID(v_stack_m68, v_stack_p18, (unsigned int)(v_stack_p10), v_stack_m88);
    a1 = v_rsi + 1;
    if ((unsigned __int8)(result) == 0) { a1 = 0; }
    result = wcspbrk(v_r14, v_rip + 2121947, (unsigned int)(v_stack_p10), v_stack_m88);
    if (result != 0) goto loc_004CB4D9;
loc_004CB529:
    result = 0;
    if ((*(unsigned __int16 *)(v_r14)) == 0) goto loc_004CB54F;
    result = RtlInitUnicodeString(v_stack_m68, v_r14, (unsigned int)(v_stack_p10), v_stack_m88);
    result = RtlCultureNameToLCID(v_stack_m68, v_stack_p18, (unsigned int)(v_stack_p10), v_stack_m88);
    v_rsi = (unsigned int)((unsigned int)(a1));
    if ((unsigned __int8)(result) != 0) {
        v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a1))) + 1);
    }
    if ((unsigned int)(v_rsi) != 0) goto loc_004CB577;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(v_stack_p10), v_stack_m88);
    v_rsi = 0;
    v_stack_m80 = 0;
    goto loc_004CB579;
loc_004CB56A:
    v_stack_m7C = 0;
loc_004CB56D:
    goto loc_004CB6E8;
loc_004CB577:
    v_rsi = 0;
loc_004CB579:
    if (v_stack_m88 != 0) {
        a2 = 0;
        a1 = v_stack_m88;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(v_stack_p10), v_stack_m88);
    }
    v_stack_m88 = 0;
loc_004CB58C:
    result = RtlpGetWindowsPolicy(v_rip + 2121313, v_stack_p20, v_stack_p10, v_stack_m88);
    if (sign_flag) goto loc_004CB6E2;
    result = (unsigned int)(((unsigned int)(v_stack_p10)) + (4));
    v_stack_m78 = (unsigned int)(result);
    if (condition_is_equal) goto loc_004CB768;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x72746C6DULL), v_stack_m88);
    v_stack_m70 = result;
    if (result == 0) goto loc_004CB76C;
    result = memcpy(result, v_stack_m88, (unsigned int)(v_stack_p10), v_stack_m88);
    result = wcspbrk(result, v_rip + 2121705, (unsigned int)(v_stack_p10), v_stack_m88);
    v_stack_m70 = result;
    result = 0;
    if (0 == 0) goto loc_004CB684;
    v_stack_m70 = 0;
loc_004CB614:
    *(unsigned __int16 *)(result) = 0;
    v_r14 = (result) + (result + 2);
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    if (0 != 0) {
        a1 = 0;
        result = wcslen(a1, v_rip + 2121705, (unsigned int)(v_stack_p10), v_stack_m88);
        result = (result) + (result);
        a1 = 0xFFFCULL;
        if (result >= 0xFFFEULL) { result = a1; }
        v_stack_m68 = (unsigned __int16)(result);
        result = (unsigned __int16)((result) + ((unsigned __int16)(result + 2)));
        v_stack_m66 = (unsigned __int16)(result);
    }
    result = RtlCultureNameToLCID(v_stack_m68, v_stack_p18, (unsigned int)(v_stack_p10), v_stack_m88);
    a1 = v_rsi + 1;
    if ((unsigned __int8)(result) == 0) { a1 = 0; }
    result = wcspbrk(v_r14, v_rip + 2121594, (unsigned int)(v_stack_p10), v_stack_m88);
    result = 0;
    if (0 != 0) goto loc_004CB614;
loc_004CB684:
    if ((*(unsigned __int16 *)(v_r14)) == 0) goto loc_004CB6A8;
    result = RtlInitUnicodeString(v_stack_m68, v_r14, (unsigned int)(v_stack_p10), v_stack_m88);
    result = RtlCultureNameToLCID(v_stack_m68, v_stack_p18, (unsigned int)(v_stack_p10), v_stack_m88);
    v_rsi = (unsigned int)((unsigned int)(a1));
    if ((unsigned __int8)(result) != 0) {
        v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a1))) + 1);
    }
    if ((unsigned int)(v_rsi) != 0) goto loc_004CB6CD;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m70, a2, (unsigned int)(v_stack_p10), v_stack_m88);
    v_rsi = 0;
    v_stack_m78 = 0;
    v_stack_m70 = 0;
    goto loc_004CB6CF;
loc_004CB6C2:
loc_004CB6C5:
    goto loc_004CB56D;
loc_004CB6CD:
    v_rsi = 0;
loc_004CB6CF:
    if (v_stack_m88 != 0) {
        a2 = 0;
        a1 = v_stack_m88;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(v_stack_p10), v_stack_m88);
    }
    v_stack_m88 = 0;
loc_004CB6E2:
loc_004CB6E8:
    if (v_stack_m88 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m88, a2, (unsigned int)(v_stack_p10), v_stack_m88);
    }
    if (0 == 0) goto loc_004CB712;
    v_r14 = (unsigned int)(v_stack_m80);
    v_r15 = 0;
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(v_stack_p10), v_stack_m88);
        v_r15 = 0;
        v_r14 = 0;
    }
    *(unsigned int *)(v_stack_p8 + 116) = (unsigned int)((unsigned int)(v_stack_m58));
    *(unsigned int *)(v_stack_p8 + 120) = (unsigned int)((unsigned int)(v_stack_m54));
    *(unsigned int *)(v_stack_p8 + 148) = (unsigned int)((unsigned int)(v_stack_m7C));
    *(unsigned __int64 *)(v_stack_p8 + 136) = v_stack_m70;
    *(unsigned int *)(v_stack_p8 + 144) = (unsigned int)((unsigned int)(v_stack_m78));
    *(unsigned __int64 *)(v_stack_p8 + 128) = 0;
    *(unsigned __int64 *)(v_stack_p8 + 152) = v_r15;
    *(unsigned int *)(v_stack_p8 + 160) = (unsigned int)(v_r14);
    v_rsp = (v_rsp) + (104);
    return 0;
loc_004CB768:
    v_stack_m70 = 0;
loc_004CB76C:
    v_stack_m78 = 0;
    goto loc_004CB56D;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpMuiRegLoadLicInformation(int64_t Arg1)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint16_t v_stack_m66;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    local_rsi = 0;
    v_stack_p18 = 0;
    v_stack_p20 = 0;
    v_stack_p10 = 0;
    v_stack_m88 = 0;
    v_stack_m7C = 0;
    v_stack_m80 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = v_xmm0;
    if (Arg1 != 0) goto loc_004CB2C9;
    goto loc_004CB712;
loc_004CB2C9:
    result = RtlpGetWindowsPolicy(v_rip + 2122452, v_stack_p20, v_stack_p10, v_stack_m88);
    if (sign_flag) goto loc_004CB300;
    v_stack_m58 = 1;
    if (v_stack_m88 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m88, a2, v_stack_p10, v_stack_m88);
    }
    v_stack_m88 = 0;
loc_004CB300:
    result = RtlpGetWindowsPolicy(v_rip + 2122333, v_stack_p20, v_stack_p10, v_stack_m88);
    if (!(sign_flag)) {
        Arg1 = v_stack_m88;
        a2 = 0;
        result = *(uint32_t *)(Arg1);
        v_stack_m54 = (uint32_t)(result);
        result = ExFreePoolWithTag(Arg1, a2, v_stack_p10, v_stack_m88);
        v_stack_m88 = 0;
    }
    result = RtlpGetWindowsPolicy(v_rip + 2122413, v_stack_p20, v_stack_p10, v_stack_m88);
    if (sign_flag) goto loc_004CB454;
    result = (uint32_t)(((uint32_t)(v_stack_p10)) + (4));
    v_stack_m7C = (uint32_t)(result);
    if (condition_is_equal) goto loc_004CB56A;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x72746C6DULL), v_stack_m88);
    if (result == 0) goto loc_004CB56A;
    result = memcpy(result, v_stack_m88, (uint32_t)(v_stack_p10), v_stack_m88);
    result = wcspbrk(result, v_rip + 2122310, (uint32_t)(v_stack_p10), v_stack_m88);
    Arg1 = 0;
    if (result == 0) goto loc_004CB403;
    local_r13 = 0;
loc_004CB3B2:
    *(uint16_t *)(result) = 0;
    local_r14 = (result) + (Arg1 + 2);
    result = RtlInitUnicodeString(v_stack_m68, result, (uint32_t)(v_stack_p10), v_stack_m88);
    result = RtlCultureNameToLCID(v_stack_m68, v_stack_p18, (uint32_t)(v_stack_p10), v_stack_m88);
    Arg1 = local_rsi + 1;
    if ((uint8_t)(result) == 0) { Arg1 = 0; }
    result = wcspbrk(local_r14, v_rip + 2122242, (uint32_t)(v_stack_p10), v_stack_m88);
    if (result != 0) goto loc_004CB3B2;
    Arg1 = 0;
loc_004CB403:
    if ((*(uint16_t *)(local_r14)) == 0) goto loc_004CB427;
    result = RtlInitUnicodeString(v_stack_m68, local_r14, (uint32_t)(v_stack_p10), v_stack_m88);
    result = RtlCultureNameToLCID(v_stack_m68, v_stack_p18, (uint32_t)(v_stack_p10), v_stack_m88);
    local_rsi = (uint32_t)((uint32_t)(Arg1));
    if ((uint8_t)(result) != 0) {
        local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) + 1);
    }
    if ((uint32_t)(local_rsi) != 0) goto loc_004CB43F;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (uint32_t)(v_stack_p10), v_stack_m88);
    local_rsi = 0;
    v_stack_m7C = 0;
    goto loc_004CB441;
loc_004CB43F:
    local_rsi = 0;
loc_004CB441:
    if (v_stack_m88 != 0) {
        a2 = 0;
        Arg1 = v_stack_m88;
        result = ExFreePoolWithTag(Arg1, a2, (uint32_t)(v_stack_p10), v_stack_m88);
    }
    v_stack_m88 = 0;
loc_004CB454:
    result = RtlpGetWindowsPolicy(v_rip + 2121673, v_stack_p20, v_stack_p10, v_stack_m88);
    if (sign_flag) goto loc_004CB58C;
    local_r14 = (uint32_t)(((uint32_t)(v_stack_p10)) + (4));
    v_stack_m80 = (uint32_t)(local_r14);
    if (condition_is_equal) goto loc_004CB6C2;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(0x72746C6DULL), v_stack_m88);
    if (result == 0) goto loc_004CB6C5;
    result = memcpy(result, v_stack_m88, (uint32_t)(v_stack_p10), v_stack_m88);
    result = wcspbrk(result, v_rip + 2122014, (uint32_t)(v_stack_p10), v_stack_m88);
    if (result == 0) goto loc_004CB529;
    local_r13 = 0;
loc_004CB4D9:
    *(uint16_t *)(result) = 0;
    local_r14 = (result) + (local_r13 + 2);
    result = RtlInitUnicodeString(v_stack_m68, result, (uint32_t)(v_stack_p10), v_stack_m88);
    result = RtlCultureNameToLCID(v_stack_m68, v_stack_p18, (uint32_t)(v_stack_p10), v_stack_m88);
    Arg1 = local_rsi + 1;
    if ((uint8_t)(result) == 0) { Arg1 = 0; }
    result = wcspbrk(local_r14, v_rip + 2121947, (uint32_t)(v_stack_p10), v_stack_m88);
    if (result != 0) goto loc_004CB4D9;
loc_004CB529:
    result = 0;
    if ((*(uint16_t *)(local_r14)) == 0) goto loc_004CB54F;
    result = RtlInitUnicodeString(v_stack_m68, local_r14, (uint32_t)(v_stack_p10), v_stack_m88);
    result = RtlCultureNameToLCID(v_stack_m68, v_stack_p18, (uint32_t)(v_stack_p10), v_stack_m88);
    local_rsi = (uint32_t)((uint32_t)(Arg1));
    if ((uint8_t)(result) != 0) {
        local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) + 1);
    }
    if ((uint32_t)(local_rsi) != 0) goto loc_004CB577;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (uint32_t)(v_stack_p10), v_stack_m88);
    local_rsi = 0;
    v_stack_m80 = 0;
    goto loc_004CB579;
loc_004CB56A:
    v_stack_m7C = 0;
loc_004CB56D:
    goto loc_004CB6E8;
loc_004CB577:
    local_rsi = 0;
loc_004CB579:
    if (v_stack_m88 != 0) {
        a2 = 0;
        Arg1 = v_stack_m88;
        result = ExFreePoolWithTag(Arg1, a2, (uint32_t)(v_stack_p10), v_stack_m88);
    }
    v_stack_m88 = 0;
loc_004CB58C:
    result = RtlpGetWindowsPolicy(v_rip + 2121313, v_stack_p20, v_stack_p10, v_stack_m88);
    if (sign_flag) goto loc_004CB6E2;
    result = (uint32_t)(((uint32_t)(v_stack_p10)) + (4));
    v_stack_m78 = (uint32_t)(result);
    if (condition_is_equal) goto loc_004CB768;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x72746C6DULL), v_stack_m88);
    v_stack_m70 = result;
    if (result == 0) goto loc_004CB76C;
    result = memcpy(result, v_stack_m88, (uint32_t)(v_stack_p10), v_stack_m88);
    result = wcspbrk(result, v_rip + 2121705, (uint32_t)(v_stack_p10), v_stack_m88);
    v_stack_m70 = result;
    result = 0;
    if (0 == 0) goto loc_004CB684;
    v_stack_m70 = 0;
loc_004CB614:
    *(uint16_t *)(result) = 0;
    local_r14 = (result) + (result + 2);
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    if (0 != 0) {
        Arg1 = 0;
        result = wcslen(Arg1, v_rip + 2121705, (uint32_t)(v_stack_p10), v_stack_m88);
        result = (result) + (result);
        Arg1 = 0xFFFCULL;
        if (result >= 0xFFFEULL) { result = Arg1; }
        v_stack_m68 = (uint16_t)(result);
        result = (uint16_t)((result) + ((uint16_t)(result + 2)));
        v_stack_m66 = (uint16_t)(result);
    }
    result = RtlCultureNameToLCID(v_stack_m68, v_stack_p18, (uint32_t)(v_stack_p10), v_stack_m88);
    Arg1 = local_rsi + 1;
    if ((uint8_t)(result) == 0) { Arg1 = 0; }
    result = wcspbrk(local_r14, v_rip + 2121594, (uint32_t)(v_stack_p10), v_stack_m88);
    result = 0;
    if (0 != 0) goto loc_004CB614;
loc_004CB684:
    if ((*(uint16_t *)(local_r14)) == 0) goto loc_004CB6A8;
    result = RtlInitUnicodeString(v_stack_m68, local_r14, (uint32_t)(v_stack_p10), v_stack_m88);
    result = RtlCultureNameToLCID(v_stack_m68, v_stack_p18, (uint32_t)(v_stack_p10), v_stack_m88);
    local_rsi = (uint32_t)((uint32_t)(Arg1));
    if ((uint8_t)(result) != 0) {
        local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) + 1);
    }
    if ((uint32_t)(local_rsi) != 0) goto loc_004CB6CD;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m70, a2, (uint32_t)(v_stack_p10), v_stack_m88);
    local_rsi = 0;
    v_stack_m78 = 0;
    v_stack_m70 = 0;
    goto loc_004CB6CF;
loc_004CB6C2:
loc_004CB6C5:
    goto loc_004CB56D;
loc_004CB6CD:
    local_rsi = 0;
loc_004CB6CF:
    if (v_stack_m88 != 0) {
        a2 = 0;
        Arg1 = v_stack_m88;
        result = ExFreePoolWithTag(Arg1, a2, (uint32_t)(v_stack_p10), v_stack_m88);
    }
    v_stack_m88 = 0;
loc_004CB6E2:
loc_004CB6E8:
    if (v_stack_m88 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m88, a2, (uint32_t)(v_stack_p10), v_stack_m88);
    }
    if (0 == 0) goto loc_004CB712;
    local_r14 = (uint32_t)(v_stack_m80);
    local_r15 = 0;
    if (0 != 0) {
        a2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, a2, (uint32_t)(v_stack_p10), v_stack_m88);
        local_r15 = 0;
        local_r14 = 0;
    }
    *(uint32_t *)(v_stack_p8 + 0x74) = (uint32_t)((uint32_t)(v_stack_m58));
    *(uint32_t *)(v_stack_p8 + 0x78) = (uint32_t)((uint32_t)(v_stack_m54));
    *(uint32_t *)(v_stack_p8 + 0x94) = (uint32_t)((uint32_t)(v_stack_m7C));
    *(uint64_t *)(v_stack_p8 + 0x88) = v_stack_m70;
    *(uint32_t *)(v_stack_p8 + 0x90) = (uint32_t)((uint32_t)(v_stack_m78));
    *(uint64_t *)(v_stack_p8 + 0x80) = 0;
    *(uint64_t *)(v_stack_p8 + 0x98) = local_r15;
    *(uint32_t *)(v_stack_p8 + 0xA0) = (uint32_t)(local_r14);
    local_rsp = (local_rsp) + (104);
    return 0;
loc_004CB768:
    v_stack_m70 = 0;
loc_004CB76C:
    v_stack_m78 = 0;
    goto loc_004CB56D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004CB26C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
