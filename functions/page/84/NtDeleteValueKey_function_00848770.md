# NtDeleteValueKey

- RVA: `0x00848770`–`0x00848DE0` (길이 `1,648` bytes)
- VA: `0x0000000140848770`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00069398`
- 디코드: `361`개 명령, `1,648/1,648` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0084880D` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x0084883D` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x00848869` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x00848899` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (function, `0x00BC9350`)
- `0x0084891E` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0084896C` → [CmpDoesBufferRequireCapturing](CmpDoesBufferRequireCapturing_function_00848DF0.md) (function, `0x00848DF0`)
- `0x0084897E` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (function, `0x00461190`)
- `0x0084899E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00848A5C` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x00848AA8` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x00848AF0` → [CmDeleteValueKey](CmDeleteValueKey_function_008476E8.md) (function, `0x008476E8`)
- `0x00848B07` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00848B22` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x00848BB8` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x00848BC9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00848BD8` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00848BFA` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00848C05` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x00848C12` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x00848C24` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00848C4F` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x00848C7F` → [CmpIsSystemEntity](../8B/CmpIsSystemEntity_function_008B4E90.md) (function, `0x008B4E90`)
- `0x00848CAC` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (function, `0x00BC9350`)
- `0x00848CBC` → [CmKeyBodyNeedsVirtualImage](CmKeyBodyNeedsVirtualImage_function_00849864.md) (function, `0x00849864`)
- `0x00848D6D` → [CmKeyBodyRemapToVirtual](../AC/CmKeyBodyRemapToVirtual_function_00AC9494.md) (function, `0x00AC9494`)
- `0x00848DD6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [ExpWatchProductTypeWork](../6F/ExpWatchProductTypeWork_function_006FFCA0.md) at `0x0070018C`

### Static image references
- `0x0084878B` → RVA `0x00E0A740` (`.data`; read)
- `0x008487FB` → RVA `0x00FD8008` (`PAGEDATA`; read)
- `0x00848A53` → RVA `0x00EEFB88` (`.data`; read)
- `0x00848C57` → RVA `0x00E0ECA0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x0084880D` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (`PAGE` → `.text`)
  - `0x0084883D` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x00848869` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x00848899` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (`PAGE` → `PAGECMRC`)
  - `0x0084897E` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (`PAGE` → `.text`)
  - `0x0084899E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00848A5C` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x00848B22` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x00848BC9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00848BD8` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00848BFA` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00848C05` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x00848C12` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x00848C24` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00848CAC` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (`PAGE` → `PAGECMRC`)
  - `0x00848DD6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00848D86` → [sub_00B1642C](../B1/Unknown_function_00B1642C.md) (`tail-transfer`)
  - `0x00848DA4` → [sub_00B1642C](../B1/Unknown_function_00B1642C.md) (`tail-transfer`)
  - `0x00848DAA` → [sub_00B1642C + 0x2](../B1/Unknown_function_00B1642C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00848770  4C 8B DC                        mov r11, rsp
00848773  49 89 5B 18                     mov qword ptr [r11 + 0x18], rbx
00848777  49 89 73 20                     mov qword ptr [r11 + 0x20], rsi
0084877B  57                              push rdi
0084877C  41 54                           push r12
0084877E  41 55                           push r13
00848780  41 56                           push r14
00848782  41 57                           push r15
00848784  48 81 EC 70 01 00 00            sub rsp, 0x170
0084878B  48 8B 05 AE 1F 5C 00            mov rax, qword ptr [rip + 0x5c1fae]
00848792  48 33 C4                        xor rax, rsp
00848795  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
0084879D  4C 8B E2                        mov r12, rdx
008487A0  48 8B F9                        mov rdi, rcx
008487A3  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
008487AB  0F 57 C0                        xorps xmm0, xmm0
008487AE  33 C0                           xor eax, eax
008487B0  41 0F 11 43 98                  movups xmmword ptr [r11 - 0x68], xmm0
008487B5  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
008487B9  0F 57 C9                        xorps xmm1, xmm1
008487BC  0F 11 8C 24 08 01 00 00         movups xmmword ptr [rsp + 0x108], xmm1
008487C4  41 0F 11 4B 80                  movups xmmword ptr [r11 - 0x80], xmm1
008487C9  49 89 43 90                     mov qword ptr [r11 - 0x70], rax
008487CD  33 DB                           xor ebx, ebx
008487CF  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
008487D4  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
008487D9  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
008487DE  44 8A F3                        mov r14b, bl
008487E1  88 5C 24 41                     mov byte ptr [rsp + 0x41], bl
008487E5  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
008487E9  41 0F 11 43 B0                  movups xmmword ptr [r11 - 0x50], xmm0
008487EE  41 0F 11 43 C0                  movups xmmword ptr [r11 - 0x40], xmm0
008487F3  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
008487FB  48 39 05 06 F8 78 00            cmp qword ptr [rip + 0x78f806], rax
00848802  74 0E                           je 0x140848812
00848804  BA 00 00 02 00                  mov edx, 0x20000
00848809  49 8D 4B B0                     lea rcx, [r11 - 0x50]
0084880D  E8 3E 74 B5 FF                  call 0x14039fc50
00848812  44 8A EB                        mov r13b, bl
00848815  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
00848819  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
0084881E  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00848823  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0084882B  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00848830  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00848835  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
0084883D  E8 2E 36 BB FF                  call 0x1403fbe70
00848842  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0084884B  44 0F BE B9 32 02 00 00         movsx r15d, byte ptr [rcx + 0x232]
00848853  40 8A F3                        mov sil, bl
00848856  0F 57 C0                        xorps xmm0, xmm0
00848859  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
00848861  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
00848869  E8 92 0B 38 00                  call 0x140bc9400
0084886E  88 44 24 43                     mov byte ptr [rsp + 0x43], al
00848872  84 C0                           test al, al
00848874  0F 84 CC 04 00 00               je 0x140848d46
0084887A  48 8D 44 24 68                  lea rax, [rsp + 0x68]
0084887F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00848884  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00848889  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0084888E  45 8A CF                        mov r9b, r15b
00848891  BA 02 00 00 00                  mov edx, 2
00848896  48 8B CF                        mov rcx, rdi
00848899  E8 B2 0A 38 00                  call 0x140bc9350
0084889E  8B F8                           mov edi, eax
008488A0  3D 22 00 00 C0                  cmp eax, 0xc0000022
008488A5  0F 84 9C 03 00 00               je 0x140848c47
008488AB  41 8A F6                        mov sil, r14b
008488AE  85 FF                           test edi, edi
008488B0  0F 88 4B 04 00 00               js 0x140848d01
008488B6  48 39 1D 4B F7 78 00            cmp qword ptr [rip + 0x78f74b], rbx
008488BD  0F 85 46 04 00 00               jne 0x140848d09
008488C3  41 80 FF 01                     cmp r15b, 1
008488C7  0F 85 01 01 00 00               jne 0x1408489ce
008488CD  0F 57 C0                        xorps xmm0, xmm0
008488D0  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
008488D8  49 B9 00 00 FF FF FF 7F 00 00   movabs r9, 0x7fffffff0000
008488E2  49 8B C9                        mov rcx, r9
008488E5  4D 3B E1                        cmp r12, r9
008488E8  49 0F 42 CC                     cmovb rcx, r12
008488EC  90                              nop
008488ED  8B 01                           mov eax, dword ptr [rcx]
008488EF  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
008488F6  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
008488FA  48 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdx
00848902  0F 28 84 24 A0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xa0]
0084890A  66 0F 7F 44 24 50               movdqa xmmword ptr [rsp + 0x50], xmm0
00848910  66 0F 7E C0                     movd eax, xmm0
00848914  66 85 C0                        test ax, ax
00848917  74 27                           je 0x140848940
00848919  41 84 D7                        test r15b, dl
0084891C  74 05                           je 0x140848923
0084891E  E8 AD 16 05 00                  call 0x140899fd0
00848923  0F B7 C0                        movzx eax, ax
00848926  4C 8D 04 10                     lea r8, [rax + rdx]
0084892A  48 8D 0C 10                     lea rcx, [rax + rdx]
0084892E  49 3B C9                        cmp rcx, r9
00848931  0F 87 8F 00 00 00               ja 0x1408489c6
00848937  4C 3B C2                        cmp r8, rdx
0084893A  0F 82 86 00 00 00               jb 0x1408489c6
00848940  44 0F B7 44 24 50               movzx r8d, word ptr [rsp + 0x50]
00848946  41 0F B7 C0                     movzx eax, r8w
0084894A  66 F7 D8                        neg ax
0084894D  48 1B F6                        sbb rsi, rsi
00848950  48 23 74 24 58                  and rsi, qword ptr [rsp + 0x58]
00848955  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
0084895A  66 44 89 44 24 52               mov word ptr [rsp + 0x52], r8w
00848960  66 45 85 C0                     test r8w, r8w
00848964  74 78                           je 0x1408489de
00848966  41 8B CF                        mov ecx, r15d
00848969  48 8B D6                        mov rdx, rsi
0084896C  E8 7F 04 00 00                  call 0x140848df0
00848971  84 C0                           test al, al
00848973  74 69                           je 0x1408489de
00848975  41 8B D0                        mov edx, r8d
00848978  41 B8 43 4D 63 62               mov r8d, 0x62634d43
0084897E  E8 0D 88 C1 FF                  call 0x140461190
00848983  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00848988  48 85 C0                        test rax, rax
0084898B  74 23                           je 0x1408489b0
0084898D  44 0F B7 44 24 50               movzx r8d, word ptr [rsp + 0x50]
00848993  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00848998  48 8B F0                        mov rsi, rax
0084899B  48 8B C8                        mov rcx, rax
0084899E  E8 9D DE E7 FF                  call 0x1406c6840
008489A3  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
008489A8  44 0F B7 44 24 50               movzx r8d, word ptr [rsp + 0x50]
008489AE  EB 2E                           jmp 0x1408489de
008489B0  BF 9A 00 00 C0                  mov edi, 0xc000009a
008489B5  89 7C 24 64                     mov dword ptr [rsp + 0x64], edi
008489B9  41 8A F6                        mov sil, r14b
008489BC  44 8A 64 24 40                  mov r12b, byte ptr [rsp + 0x40]
008489C1  E9 34 01 00 00                  jmp 0x140848afa
008489C6  41 8A 01                        mov al, byte ptr [r9]
008489C9  E9 72 FF FF FF                  jmp 0x140848940
008489CE  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
008489D3  F3 0F 7F 44 24 50               movdqu xmmword ptr [rsp + 0x50], xmm0
008489D9  E9 62 FF FF FF                  jmp 0x140848940
008489DE  EB 24                           jmp 0x140848a04
008489E0  8B F8                           mov edi, eax
008489E2  33 C0                           xor eax, eax
008489E4  66 89 44 24 50                  mov word ptr [rsp + 0x50], ax
008489E9  48 21 44 24 58                  and qword ptr [rsp + 0x58], rax
008489EE  89 7C 24 64                     mov dword ptr [rsp + 0x64], edi
008489F2  40 8A 74 24 41                  mov sil, byte ptr [rsp + 0x41]
008489F7  33 DB                           xor ebx, ebx
008489F9  44 8A E0                        mov r12b, al
008489FC  44 8A E8                        mov r13b, al
008489FF  E9 F6 00 00 00                  jmp 0x140848afa
00848A04  41 F6 C0 01                     test r8b, 1
00848A08  0F 85 2C 03 00 00               jne 0x140848d3a
00848A0E  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00848A13  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00848A17  8B 41 08                        mov eax, dword ptr [rcx + 8]
00848A1A  84 C0                           test al, al
00848A1C  0F 88 B0 02 00 00               js 0x140848cd2
00848A22  41 0F B7 C8                     movzx ecx, r8w
00848A26  48 D1 E9                        shr rcx, 1
00848A29  48 FF C9                        dec rcx
00848A2C  48 8D 0C 4E                     lea rcx, [rsi + rcx*2]
00848A30  66 45 85 C0                     test r8w, r8w
00848A34  74 09                           je 0x140848a3f
00848A36  66 39 19                        cmp word ptr [rcx], bx
00848A39  0F 84 A5 02 00 00               je 0x140848ce4
00848A3F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00848A48  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00848A4F  90                              nop
00848A50  41 B4 01                        mov r12b, 1
00848A53  83 3D 2E 71 6A 00 00            cmp dword ptr [rip + 0x6a712e], 0
00848A5A  74 5C                           je 0x140848ab8
00848A5C  E8 1B E0 C0 FF                  call 0x140456a7c
00848A61  85 C0                           test eax, eax
00848A63  75 53                           jne 0x140848ab8
00848A65  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00848A6A  48 89 8C 24 08 01 00 00         mov qword ptr [rsp + 0x108], rcx
00848A72  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00848A77  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
00848A7F  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00848A84  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00848A89  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00848A8E  C7 44 24 20 11 00 00 00         mov dword ptr [rsp + 0x20], 0x11
00848A96  45 8A CC                        mov r9b, r12b
00848A99  45 33 C0                        xor r8d, r8d
00848A9C  48 8D 94 24 08 01 00 00         lea rdx, [rsp + 0x108]
00848AA4  41 8D 48 02                     lea ecx, [r8 + 2]
00848AA8  E8 93 D4 01 00                  call 0x140865f40
00848AAD  85 C0                           test eax, eax
00848AAF  0F 88 73 02 00 00               js 0x140848d28
00848AB5  45 8A EC                        mov r13b, r12b
00848AB8  45 84 F6                        test r14b, r14b
00848ABB  0F 85 8C 02 00 00               jne 0x140848d4d
00848AC1  0F 28 44 24 50                  movaps xmm0, xmmword ptr [rsp + 0x50]
00848AC6  66 0F 7F 84 24 A0 00 00 00      movdqa xmmword ptr [rsp + 0xa0], xmm0
00848ACF  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
00848AD4  41 C1 E9 02                     shr r9d, 2
00848AD8  45 22 CC                        and r9b, r12b
00848ADB  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
00848AE3  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
00848AEB  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00848AF0  E8 F3 EB FF FF                  call 0x1408476e8
00848AF5  8B F8                           mov edi, eax
00848AF7  41 8A F6                        mov sil, r14b
00848AFA  40 84 F6                        test sil, sil
00848AFD  74 0D                           je 0x140848b0c
00848AFF  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
00848B07  E8 04 2C 02 00                  call 0x14086b710
00848B0C  45 84 ED                        test r13b, r13b
00848B0F  0F 84 AF 00 00 00               je 0x140848bc4
00848B15  83 3D 6C 70 6A 00 00            cmp dword ptr [rip + 0x6a706c], 0
00848B1C  0F 84 A2 00 00 00               je 0x140848bc4
00848B22  E8 55 DF C0 FF                  call 0x140456a7c
00848B27  85 C0                           test eax, eax
00848B29  0F 85 95 00 00 00               jne 0x140848bc4
00848B2F  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00848B34  48 39 44 24 78                  cmp qword ptr [rsp + 0x78], rax
00848B39  0F 84 85 00 00 00               je 0x140848bc4
00848B3F  0F 57 C0                        xorps xmm0, xmm0
00848B42  33 C0                           xor eax, eax
00848B44  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
00848B4C  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
00848B54  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
00848B5C  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
00848B64  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00848B69  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
00848B71  89 BC 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], edi
00848B78  89 BC 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], edi
00848B7F  48 8D 84 24 08 01 00 00         lea rax, [rsp + 0x108]
00848B87  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
00848B8F  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00848B94  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00848B99  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00848B9E  C7 44 24 20 11 00 00 00         mov dword ptr [rsp + 0x20], 0x11
00848BA6  45 33 C9                        xor r9d, r9d
00848BA9  45 33 C0                        xor r8d, r8d
00848BAC  48 8D 94 24 D0 00 00 00         lea rdx, [rsp + 0xd0]
00848BB4  41 8D 49 11                     lea ecx, [r9 + 0x11]
00848BB8  E8 83 D3 01 00                  call 0x140865f40
00848BBD  8B BC 24 E8 00 00 00            mov edi, dword ptr [rsp + 0xe8]
00848BC4  45 84 E4                        test r12b, r12b
00848BC7  74 05                           je 0x140848bce
00848BC9  E8 E2 4C A1 FF                  call 0x14025d8b0
00848BCE  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00848BD3  48 85 C9                        test rcx, rcx
00848BD6  74 05                           je 0x140848bdd
00848BD8  E8 73 07 AB FF                  call 0x1402f9350
00848BDD  48 8B 05 24 F4 78 00            mov rax, qword ptr [rip + 0x78f424]
00848BE4  48 85 C0                        test rax, rax
00848BE7  0F 85 C2 01 00 00               jne 0x140848daf
00848BED  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00848BF2  48 85 F6                        test rsi, rsi
00848BF5  74 08                           je 0x140848bff
00848BF7  48 8B CE                        mov rcx, rsi
00848BFA  E8 81 D1 C2 FF                  call 0x140475d80
00848BFF  38 5C 24 43                     cmp byte ptr [rsp + 0x43], bl
00848C03  74 05                           je 0x140848c0a
00848C05  E8 76 0C 38 00                  call 0x140bc9880
00848C0A  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
00848C12  E8 39 71 BD FF                  call 0x14041fd50
00848C17  8B C7                           mov eax, edi
00848C19  48 8B 8C 24 68 01 00 00         mov rcx, qword ptr [rsp + 0x168]
00848C21  48 33 CC                        xor rcx, rsp
00848C24  E8 17 3A E6 FF                  call 0x1406ac640
00848C29  4C 8D 9C 24 70 01 00 00         lea r11, [rsp + 0x170]
00848C31  49 8B 5B 40                     mov rbx, qword ptr [r11 + 0x40]
00848C35  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00848C39  49 8B E3                        mov rsp, r11
00848C3C  41 5F                           pop r15
00848C3E  41 5E                           pop r14
00848C40  41 5D                           pop r13
00848C42  41 5C                           pop r12
00848C44  5F                              pop rdi
00848C45  C3                              ret
00848C46  CC                              int3
00848C47  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
00848C4F  E8 CC 2B 02 00                  call 0x14086b820
00848C54  40 B6 01                        mov sil, 1
00848C57  38 1D 43 60 5C 00               cmp byte ptr [rip + 0x5c6043], bl
00848C5D  0F 84 99 00 00 00               je 0x140848cfc
00848C63  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00848C6C  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00848C72  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00848C77  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
00848C7F  E8 0C C2 06 00                  call 0x1408b4e90
00848C84  84 C0                           test al, al
00848C86  75 74                           jne 0x140848cfc
00848C88  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00848C8D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00848C92  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00848C97  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00848C9C  45 8A CF                        mov r9b, r15b
00848C9F  BA 19 00 02 00                  mov edx, 0x20019
00848CA4  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00848CAC  E8 9F 06 38 00                  call 0x140bc9350
00848CB1  8B F8                           mov edi, eax
00848CB3  85 C0                           test eax, eax
00848CB5  78 4A                           js 0x140848d01
00848CB7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00848CBC  E8 A3 0B 00 00                  call 0x140849864
00848CC1  84 C0                           test al, al
00848CC3  74 37                           je 0x140848cfc
00848CC5  44 8A F6                        mov r14b, sil
00848CC8  40 88 74 24 41                  mov byte ptr [rsp + 0x41], sil
00848CCD  E9 D9 FB FF FF                  jmp 0x1408488ab
00848CD2  BF 22 00 00 C0                  mov edi, 0xc0000022
00848CD7  41 8A F6                        mov sil, r14b
00848CDA  44 8A 64 24 40                  mov r12b, byte ptr [rsp + 0x40]
00848CDF  E9 16 FE FF FF                  jmp 0x140848afa
00848CE4  B8 FE FF 00 00                  mov eax, 0xfffe
00848CE9  66 44 03 C0                     add r8w, ax
00848CED  66 44 89 44 24 50               mov word ptr [rsp + 0x50], r8w
00848CF3  48 83 E9 02                     sub rcx, 2
00848CF7  E9 34 FD FF FF                  jmp 0x140848a30
00848CFC  BF 22 00 00 C0                  mov edi, 0xc0000022
00848D01  44 8A E3                        mov r12b, bl
00848D04  E9 F1 FD FF FF                  jmp 0x140848afa
00848D09  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00848D0E  48 85 C9                        test rcx, rcx
00848D11  0F 84 AC FB FF FF               je 0x1408488c3
00848D17  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00848D1B  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00848D23  E9 9B FB FF FF                  jmp 0x1408488c3
00848D28  41 8A F6                        mov sil, r14b
00848D2B  8B FB                           mov edi, ebx
00848D2D  3D 03 05 00 C0                  cmp eax, 0xc0000503
00848D32  0F 45 F8                        cmovne edi, eax
00848D35  E9 C0 FD FF FF                  jmp 0x140848afa
00848D3A  66 89 5C 24 50                  mov word ptr [rsp + 0x50], bx
00848D3F  BF 0D 00 00 C0                  mov edi, 0xc000000d
00848D44  EB 91                           jmp 0x140848cd7
00848D46  BF 89 01 00 C0                  mov edi, 0xc0000189
00848D4B  EB B4                           jmp 0x140848d01
00848D4D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00848D52  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00848D57  4C 8D 8C 24 B0 00 00 00         lea r9, [rsp + 0xb0]
00848D5F  41 B8 02 00 00 00               mov r8d, 2
00848D65  41 8A D7                        mov dl, r15b
00848D68  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00848D6D  E8 22 07 28 00                  call 0x140ac9494
00848D72  8B F8                           mov edi, eax
00848D74  41 8A F6                        mov sil, r14b
00848D77  85 C0                           test eax, eax
00848D79  0F 88 7B FD FF FF               js 0x140848afa
00848D7F  80 3D 1A 5F 5C 00 00            cmp byte ptr [rip + 0x5c5f1a], 0
00848D86  0F 84 A0 D6 2C 00               je 0x140b1642c
00848D8C  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00848D91  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00848D95  F7 81 B8 00 00 00 00 00 00 01   test dword ptr [rcx + 0xb8], 0x1000000
00848D9F  B8 01 00 00 00                  mov eax, 1
00848DA4  0F 84 82 D6 2C 00               je 0x140b1642c
00848DAA  E9 7F D6 2C 00                  jmp 0x140b1642e
00848DAF  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00848DB4  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00848DB9  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00848DC1  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00848DC6  45 33 C9                        xor r9d, r9d
00848DC9  44 8B C7                        mov r8d, edi
00848DCC  48 8D 94 24 48 01 00 00         lea rdx, [rsp + 0x148]
00848DD4  B1 0F                           mov cl, 0xf
00848DD6  E8 F5 1C E7 FF                  call 0x1406baad0
00848DDB  E9 0D FE FF FF                  jmp 0x140848bed
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtDeleteValueKey(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int8 v_stack_m12F;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m134;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int16 v_stack_m146;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int8 v_stack_m155;
    unsigned __int8 v_stack_m157;
    unsigned __int8 v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 6037422)) ^ (v_rsp);
    v_stack_m30 = result;
    v_stack_m110 = a1;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    v_stack_m90 = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 128) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    v_rbx = 0;
    v_stack_m130 = 0;
    v_stack_m148 = v_xmm0;
    v_stack_m128 = 0;
    v_stack_m157 = 0;
    v_stack_m138 = 0;
    *(unsigned __int64 *)(v_rsp - 80) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 64) = v_xmm0;
    v_stack_m108 = 0;
    if ((*(unsigned __int64 *)(v_rip + 7927814)) != 0) {
        a2 = 0x20000ULL;
        a1 = v_rsp - 80;
        result = EtwGetKernelTraceTimestamp(a1, a2, a3, a4);
    }
    v_stack_m158 = 0;
    v_stack_m150 = 0;
    v_stack_m118 = v_stack_m120;
    v_stack_m120 = v_stack_m120;
    result = CmpInitializeThreadInfo(v_stack_m68, a2, a3, a4);
    v_stack_mE8 = v_xmm0;
    v_stack_mD8 = v_xmm0;
    result = CmpAcquireShutdownRundown(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_stack_m155 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_00848D46;
    v_stack_m170 = v_stack_m130;
    v_stack_m178 = v_stack_m150;
    result = CmObReferenceObjectByHandle(a1, 2, a3, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    if (((unsigned int)(result)) == 0xC0000022ULL) goto loc_00848C47;
loc_008488AB:
    if (sign_flag) goto loc_00848D01;
    if ((*(unsigned __int64 *)(v_rip + 7927627)) != 0) goto loc_00848D09;
loc_008488C3:
    if (((unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) != 1) goto loc_008489CE;
    v_stack_mF8 = v_xmm0;
    a1 = (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (a2 < ((unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))))) { a1 = a2; }
    v_stack_mF8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_mF0 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m148 = v_xmm0;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_00848940;
    result = (unsigned int)(*(unsigned int *)(a1));
    if ((((unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))) & ((unsigned __int8)(*(unsigned __int64 *)(a1 + 8)))) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, *(unsigned __int64 *)(a1 + 8), a3, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    }
    if (((unsigned __int16)(result) + *(unsigned __int64 *)(a1 + 8) * 1) > ((unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))))) goto loc_008489C6;
    if (((unsigned __int16)(result) + *(unsigned __int64 *)(a1 + 8) * 1) < (*(unsigned __int64 *)(a1 + 8))) goto loc_008489C6;
loc_00848940:
    result = (unsigned __int16)(-((unsigned __int16)(v_stack_m148)));
    v_rsi = (0) & (v_stack_m140);
    v_stack_m140 = v_rsi;
    v_stack_m146 = (unsigned __int16)(v_stack_m148);
    if ((unsigned __int16)(v_stack_m148) == 0) goto loc_008489DE;
    result = CmpDoesBufferRequireCapturing((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))), v_rsi, v_stack_m148, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    if ((unsigned __int8)(result) == 0) goto loc_008489DE;
    result = CmpAllocateTransientPoolWithQuota((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)))), (unsigned int)((unsigned int)(v_stack_m148)), (unsigned int)(0x62634D43ULL), (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    v_stack_m128 = result;
    if (result == 0) goto loc_008489B0;
    result = memcpy(result, v_stack_m140, v_stack_m148, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    v_stack_m140 = result;
    goto loc_008489DE;
loc_008489B0:
    v_stack_m134 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_00848AFA;
loc_008489C6:
    goto loc_00848940;
loc_008489CE:
    v_stack_m148 = v_xmm0;
    goto loc_00848940;
loc_008489DE:
    goto loc_00848A04;
loc_00848A04:
    if ((((unsigned __int8)(v_stack_m148)) & (1)) != 0) goto loc_00848D3A;
    if (sign_flag) goto loc_00848CD2;
    a1 = ((unsigned __int16)(v_stack_m148)) >> (1);
    a1 = (a1) - 1;
loc_00848A30:
    if ((unsigned __int16)(v_stack_m148) == 0) goto loc_00848A3F;
    if ((*(unsigned __int16 *)(0 + a1 * 2)) == 0) goto loc_00848CE4;
loc_00848A3F:
    if ((*(unsigned int *)(v_rip + 6975790)) == 0) goto loc_00848AB8;
    result = CmpIsRegistryLockAcquired(0 + a1 * 2, v_stack_m140, v_stack_m148, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    if ((unsigned int)(result) != 0) goto loc_00848AB8;
    v_stack_m90 = v_stack_m150;
    v_stack_m88 = v_stack_m148;
    v_stack_m168 = v_stack_m120;
    v_stack_m170 = v_stack_m150;
    v_stack_m178 = 17;
    a3 = 0;
    result = CmpCallCallBacksEx(a3 + 2, v_stack_m90, a3, 1);
    if (sign_flag) goto loc_00848D28;
loc_00848AB8:
    if (0 != 0) goto loc_00848D4D;
    v_stack_mF8 = v_xmm0;
    a4 = (unsigned int)((v_stack_m130) >> (2));
    a4 = (unsigned __int8)((a4) & (1));
    result = CmDeleteValueKey(v_stack_m150, v_stack_mF8, v_stack_m110, a4);
loc_00848AFA:
    if (0 != 0) {
        a1 = v_stack_mE8;
        result = SeReleaseSubjectContext(a1, v_stack_mF8, v_stack_m110, a4);
    }
    if (1 == 0) goto loc_00848BC4;
    if ((*(unsigned int *)(v_rip + 6975596)) == 0) goto loc_00848BC4;
    result = CmpIsRegistryLockAcquired(a1, v_stack_mF8, v_stack_m110, a4);
    if ((unsigned int)(result) != 0) goto loc_00848BC4;
    result = v_stack_m120;
    v_rdi = (unsigned int)((unsigned int)(result));
    if (v_stack_m120 != v_stack_m120) {
        result = 0;
        v_stack_mC8 = v_xmm0;
        v_stack_mB8 = v_xmm0;
        v_stack_mA8 = v_xmm0;
        v_stack_m98 = 0;
        a1 = v_stack_m150;
        v_stack_mC8 = a1;
        v_stack_mC0 = (unsigned int)((unsigned int)((unsigned int)(result)));
        v_stack_mB0 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = v_stack_m90;
        v_stack_mB8 = result;
        result = v_stack_m120;
        v_stack_m168 = result;
        v_stack_m170 = a1;
        v_stack_m178 = 17;
        a4 = 0;
        a3 = 0;
        a2 = v_stack_mC8;
        a1 = a4 + 17;
        result = CmpCallCallBacksEx(a1, a2, a3, a4);
        v_rdi = v_stack_mB0;
    }
    if (1 != 0) {
        result = KeLeaveCriticalRegion(a1, a2, a3, a4);
    }
    if (v_stack_m150 != 0) {
        result = ObfDereferenceObject(v_stack_m150, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rip + 7926820) != 0) goto loc_00848DAF;
loc_00848BED:
    result = *(unsigned __int64 *)(v_rip + 7926820);
    if (v_stack_m128 != 0) {
        a1 = v_stack_m128;
        result = CmSiFreeMemory(a1, a2, a3, a4);
    }
    if (v_stack_m155 != 0) {
        result = CmpReleaseShutdownRundown(a1, a2, a3, a4);
    }
    result = CmCleanupThreadInfo(v_stack_m68, a2, a3, a4);
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_00848C47:
    result = SeCaptureSubjectContext(v_stack_mC0, a2, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 6053955)) == ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64)))) goto loc_00848CFC;
    result = CmpIsSystemEntity(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), v_stack_mC0, v_stack_m110, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00848CFC;
    v_stack_m148 = v_stack_m108;
    v_stack_m150 = v_stack_m128;
    result = CmObReferenceObjectByHandle(v_stack_mE8, (unsigned int)(0x20019ULL), v_stack_m110, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    if (sign_flag) goto loc_00848D01;
    result = CmKeyBodyNeedsVirtualImage(v_stack_m128, (unsigned int)(0x20019ULL), v_stack_m110, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))));
    if ((unsigned __int8)(result) == 0) goto loc_00848CFC;
    v_stack_m12F = 1;
    goto loc_008488AB;
loc_00848CD2:
loc_00848CD7:
    goto loc_00848AFA;
loc_00848CE4:
    a3 = (unsigned __int16)((v_stack_m110) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    v_stack_m120 = (unsigned __int16)(a3);
    a1 = (v_stack_m128) - (2);
    goto loc_00848A30;
loc_00848CFC:
loc_00848D01:
    goto loc_00848AFA;
loc_00848D09:
    if (v_stack_m128 == 0) goto loc_008488C3;
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_m128 + 8);
    goto loc_008488C3;
loc_00848D28:
    v_rdi = (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)));
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m128 + 8))) != 0xC0000503ULL) { v_rdi = (unsigned int)(*(unsigned __int64 *)(v_stack_m128 + 8)); }
    goto loc_00848AFA;
loc_00848D3A:
    v_stack_m120 = (unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 64));
    goto loc_00848CD7;
loc_00848D46:
    goto loc_00848D01;
loc_00848D4D:
    v_stack_m150 = v_stack_m110;
    result = CmKeyBodyRemapToVirtual(v_stack_m128, (unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))), 2, v_stack_mC0);
    if (sign_flag) goto loc_00848AFA;
loc_00848DAF:
    v_stack_m148 = v_stack_m120;
    v_stack_m150 = v_stack_mE0;
    a4 = 0;
    result = guard_dispatch_icall(15, v_stack_m28, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    goto loc_00848BED;
}
```

## 5. (Beta) C Style

```c
int64_t NtDeleteValueKey(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint8_t v_stack_m12F;
    uint64_t v_stack_m130;
    uint32_t v_stack_m134;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint16_t v_stack_m146;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint8_t v_stack_m155;
    uint8_t v_stack_m157;
    uint8_t v_stack_m158;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m68;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0x5C1FAE)) ^ (local_rsp);
    v_stack_m30 = result;
    v_stack_m110 = Arg1;
    result = 0;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    v_stack_m90 = v_xmm1;
    *(uint64_t *)(local_rsp - 0x80) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    local_rbx = 0;
    v_stack_m130 = 0;
    v_stack_m148 = v_xmm0;
    v_stack_m128 = 0;
    v_stack_m157 = 0;
    v_stack_m138 = 0;
    *(uint64_t *)(local_rsp - 0x50) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x40) = v_xmm0;
    v_stack_m108 = 0;
    if ((*(uint64_t *)(v_rip + 0x78F806)) != 0) {
        Arg2 = 0x20000ULL;
        Arg1 = local_rsp - 80;
        result = EtwGetKernelTraceTimestamp(Arg1, Arg2, a3, a4);
    }
    v_stack_m158 = 0;
    v_stack_m150 = 0;
    v_stack_m118 = v_stack_m120;
    v_stack_m120 = v_stack_m120;
    result = CmpInitializeThreadInfo(v_stack_m68, Arg2, a3, a4);
    v_stack_mE8 = v_xmm0;
    v_stack_mD8 = v_xmm0;
    result = CmpAcquireShutdownRundown(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, a3, a4);
    v_stack_m155 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_00848D46;
    v_stack_m170 = v_stack_m130;
    v_stack_m178 = v_stack_m150;
    result = CmObReferenceObjectByHandle(Arg1, 2, a3, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    if (((uint32_t)(result)) == 0xC0000022ULL) goto loc_00848C47;
loc_008488AB:
    if (sign_flag) goto loc_00848D01;
    if ((*(uint64_t *)(v_rip + 0x78F74B)) != 0) goto loc_00848D09;
loc_008488C3:
    if (((uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) != 1) goto loc_008489CE;
    v_stack_mF8 = v_xmm0;
    Arg1 = (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (Arg2 < ((uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))))) { Arg1 = Arg2; }
    v_stack_mF8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    v_stack_mF0 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m148 = v_xmm0;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) == 0) goto loc_00848940;
    result = (uint32_t)(*(uint32_t *)(Arg1));
    if ((((uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))) & ((uint8_t)(*(uint64_t *)(Arg1 + 0x8)))) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, *(uint64_t *)(Arg1 + 0x8), a3, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    }
    if (((uint16_t)(result) + *(uint64_t *)(Arg1 + 0x8) * 1) > ((uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))))) goto loc_008489C6;
    if (((uint16_t)(result) + *(uint64_t *)(Arg1 + 0x8) * 1) < (*(uint64_t *)(Arg1 + 0x8))) goto loc_008489C6;
loc_00848940:
    result = (uint16_t)(-((uint16_t)(v_stack_m148)));
    local_rsi = (0) & (v_stack_m140);
    v_stack_m140 = local_rsi;
    v_stack_m146 = (uint16_t)(v_stack_m148);
    if ((uint16_t)(v_stack_m148) == 0) goto loc_008489DE;
    result = CmpDoesBufferRequireCapturing((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))), local_rsi, v_stack_m148, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    if ((uint8_t)(result) == 0) goto loc_008489DE;
    result = CmpAllocateTransientPoolWithQuota((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)))), (uint32_t)((uint32_t)(v_stack_m148)), (uint32_t)(0x62634D43ULL), (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    v_stack_m128 = result;
    if (result == 0) goto loc_008489B0;
    result = memcpy(result, v_stack_m140, v_stack_m148, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    v_stack_m140 = result;
    goto loc_008489DE;
loc_008489B0:
    v_stack_m134 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_00848AFA;
loc_008489C6:
    goto loc_00848940;
loc_008489CE:
    v_stack_m148 = v_xmm0;
    goto loc_00848940;
loc_008489DE:
    goto loc_00848A04;
loc_00848A04:
    if ((((uint8_t)(v_stack_m148)) & (1)) != 0) goto loc_00848D3A;
    if (sign_flag) goto loc_00848CD2;
    Arg1 = ((uint16_t)(v_stack_m148)) >> (1);
    Arg1 = (Arg1) - 1;
loc_00848A30:
    if ((uint16_t)(v_stack_m148) == 0) goto loc_00848A3F;
    if ((*(uint16_t *)(0 + Arg1 * 2)) == 0) goto loc_00848CE4;
loc_00848A3F:
    if ((*(uint32_t *)(v_rip + 0x6A712E)) == 0) goto loc_00848AB8;
    result = CmpIsRegistryLockAcquired(0 + Arg1 * 2, v_stack_m140, v_stack_m148, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    if ((uint32_t)(result) != 0) goto loc_00848AB8;
    v_stack_m90 = v_stack_m150;
    v_stack_m88 = v_stack_m148;
    v_stack_m168 = v_stack_m120;
    v_stack_m170 = v_stack_m150;
    v_stack_m178 = 17;
    a3 = 0;
    result = CmpCallCallBacksEx(a3 + 2, v_stack_m90, a3, 1);
    if (sign_flag) goto loc_00848D28;
loc_00848AB8:
    if (0 != 0) goto loc_00848D4D;
    v_stack_mF8 = v_xmm0;
    a4 = (uint32_t)((v_stack_m130) >> (2));
    a4 = (uint8_t)((a4) & (1));
    result = CmDeleteValueKey(v_stack_m150, v_stack_mF8, v_stack_m110, a4);
loc_00848AFA:
    if (0 != 0) {
        Arg1 = v_stack_mE8;
        result = SeReleaseSubjectContext(Arg1, v_stack_mF8, v_stack_m110, a4);
    }
    if (1 == 0) goto loc_00848BC4;
    if ((*(uint32_t *)(v_rip + 0x6A706C)) == 0) goto loc_00848BC4;
    result = CmpIsRegistryLockAcquired(Arg1, v_stack_mF8, v_stack_m110, a4);
    if ((uint32_t)(result) != 0) goto loc_00848BC4;
    result = v_stack_m120;
    local_rdi = (uint32_t)((uint32_t)(result));
    if (v_stack_m120 != v_stack_m120) {
        result = 0;
        v_stack_mC8 = v_xmm0;
        v_stack_mB8 = v_xmm0;
        v_stack_mA8 = v_xmm0;
        v_stack_m98 = 0;
        Arg1 = v_stack_m150;
        v_stack_mC8 = Arg1;
        v_stack_mC0 = (uint32_t)((uint32_t)((uint32_t)(result)));
        v_stack_mB0 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = v_stack_m90;
        v_stack_mB8 = result;
        result = v_stack_m120;
        v_stack_m168 = result;
        v_stack_m170 = Arg1;
        v_stack_m178 = 17;
        a4 = 0;
        a3 = 0;
        Arg2 = v_stack_mC8;
        Arg1 = a4 + 17;
        result = CmpCallCallBacksEx(Arg1, Arg2, a3, a4);
        local_rdi = v_stack_mB0;
    }
    if (1 != 0) {
        result = KeLeaveCriticalRegion(Arg1, Arg2, a3, a4);
    }
    if (v_stack_m150 != 0) {
        result = ObfDereferenceObject(v_stack_m150, Arg2, a3, a4);
    }
    if (*(uint64_t *)(v_rip + 0x78F424) != 0) goto loc_00848DAF;
loc_00848BED:
    result = *(uint64_t *)(v_rip + 0x78F424);
    if (v_stack_m128 != 0) {
        Arg1 = v_stack_m128;
        result = CmSiFreeMemory(Arg1, Arg2, a3, a4);
    }
    if (v_stack_m155 != 0) {
        result = CmpReleaseShutdownRundown(Arg1, Arg2, a3, a4);
    }
    result = CmCleanupThreadInfo(v_stack_m68, Arg2, a3, a4);
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
loc_00848C47:
    result = SeCaptureSubjectContext(v_stack_mC0, Arg2, a3, a4);
    if ((*(uint8_t *)(v_rip + 0x5C6043)) == ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40)))) goto loc_00848CFC;
    result = CmpIsSystemEntity(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), v_stack_mC0, v_stack_m110, a4);
    if ((uint8_t)(result) != 0) goto loc_00848CFC;
    v_stack_m148 = v_stack_m108;
    v_stack_m150 = v_stack_m128;
    result = CmObReferenceObjectByHandle(v_stack_mE8, (uint32_t)(0x20019ULL), v_stack_m110, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    if (sign_flag) goto loc_00848D01;
    result = CmKeyBodyNeedsVirtualImage(v_stack_m128, (uint32_t)(0x20019ULL), v_stack_m110, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))));
    if ((uint8_t)(result) == 0) goto loc_00848CFC;
    v_stack_m12F = 1;
    goto loc_008488AB;
loc_00848CD2:
loc_00848CD7:
    goto loc_00848AFA;
loc_00848CE4:
    a3 = (uint16_t)((v_stack_m110) + ((uint16_t)((uint32_t)(0xFFFEULL))));
    v_stack_m120 = (uint16_t)(a3);
    Arg1 = (v_stack_m128) - (2);
    goto loc_00848A30;
loc_00848CFC:
loc_00848D01:
    goto loc_00848AFA;
loc_00848D09:
    if (v_stack_m128 == 0) goto loc_008488C3;
    v_stack_mE0 = *(uint64_t *)(v_stack_m128 + 0x8);
    goto loc_008488C3;
loc_00848D28:
    local_rdi = (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)));
    if (((uint32_t)(*(uint64_t *)(v_stack_m128 + 0x8))) != 0xC0000503ULL) { local_rdi = (uint32_t)(*(uint64_t *)(v_stack_m128 + 0x8)); }
    goto loc_00848AFA;
loc_00848D3A:
    v_stack_m120 = (uint16_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    goto loc_00848CD7;
loc_00848D46:
    goto loc_00848D01;
loc_00848D4D:
    v_stack_m150 = v_stack_m110;
    result = CmKeyBodyRemapToVirtual(v_stack_m128, (uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))), 2, v_stack_mC0);
    if (sign_flag) goto loc_00848AFA;
loc_00848DAF:
    v_stack_m148 = v_stack_m120;
    v_stack_m150 = v_stack_mE0;
    a4 = 0;
    result = guard_dispatch_icall(15, v_stack_m28, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    goto loc_00848BED;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00848770&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
