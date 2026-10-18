# PopEtEnergyTrackerQuery

- RVA: `0x0098B668`–`0x0098C6AC` (길이 `4,164` bytes)
- VA: `0x000000014098B668`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009874C`
- 디코드: `902`개 명령, `4,164/4,164` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0098B71F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x0098B76D` → [PsEnumProcesses](../91/PsEnumProcesses_function_0091BE84.md) (function, `0x0091BE84`)
- `0x0098B781` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x0098BAA5` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0098BFF8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0098C050` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0098C0A3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0098C0F5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0098C159` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0098C1BD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0098C378` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (function, `0x0045D2CC`)
- `0x0098C59D` → [PopEtEnergyTrackerCleanupAggregates](PopEtEnergyTrackerCleanupAggregates_function_0098D1D8.md) (function, `0x0098D1D8`)
- `0x0098C690` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x0098C6A2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x00957D3C`

### Static image references
- `0x0098B6D8` → RVA `0x00E67A30` (`.data`; read)
- `0x0098B766` → RVA `0x0091CCA0` (`PopEtProcessEnumSnapshotCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x0098B781` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x0098BAA5` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0098BFF8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0098C050` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0098C0A3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0098C0F5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0098C159` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0098C1BD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0098C378` → [KeQueryTimelineBitmapTime](../../text/45/KeQueryTimelineBitmapTime_function_0045D2CC.md) (`PAGE` → `.text`)
  - `0x0098C690` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x0098C6A2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0098C652` → [sub_00B2B8A6](../B2/Unknown_function_00B2B8A6.md) (`tail-transfer`)
  - `0x0098C667` → [sub_00B2B8A6](../B2/Unknown_function_00B2B8A6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0098B668  48 8B C4                        mov rax, rsp
0098B66B  48 89 58 08                     mov qword ptr [rax + 8], rbx
0098B66F  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0098B673  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
0098B677  57                              push rdi
0098B678  41 54                           push r12
0098B67A  41 55                           push r13
0098B67C  41 56                           push r14
0098B67E  41 57                           push r15
0098B680  48 81 EC 70 01 00 00            sub rsp, 0x170
0098B687  48 8B F2                        mov rsi, rdx
0098B68A  33 FF                           xor edi, edi
0098B68C  8B DF                           mov ebx, edi
0098B68E  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
0098B693  0F 57 C0                        xorps xmm0, xmm0
0098B696  0F 11 80 F8 FE FF FF            movups xmmword ptr [rax - 0x108], xmm0
0098B69D  0F 11 80 08 FF FF FF            movups xmmword ptr [rax - 0xf8], xmm0
0098B6A4  0F 57 C9                        xorps xmm1, xmm1
0098B6A7  0F 11 88 58 FF FF FF            movups xmmword ptr [rax - 0xa8], xmm1
0098B6AE  0F 11 88 68 FF FF FF            movups xmmword ptr [rax - 0x98], xmm1
0098B6B5  44 8A FF                        mov r15b, dil
0098B6B8  0F 11 80 28 FF FF FF            movups xmmword ptr [rax - 0xd8], xmm0
0098B6BF  0F 11 80 38 FF FF FF            movups xmmword ptr [rax - 0xc8], xmm0
0098B6C6  0F 11 48 B0                     movups xmmword ptr [rax - 0x50], xmm1
0098B6CA  0F 11 48 C0                     movups xmmword ptr [rax - 0x40], xmm1
0098B6CE  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
0098B6D3  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0098B6D8  48 39 3D 51 C3 4D 00            cmp qword ptr [rip + 0x4dc351], rdi
0098B6DF  0F 84 35 0F 00 00               je 0x14098c61a
0098B6E5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0098B6EE  44 8A 88 32 02 00 00            mov r9b, byte ptr [rax + 0x232]
0098B6F5  48 8B 05 34 C3 4D 00            mov rax, qword ptr [rip + 0x4dc334]
0098B6FC  4C 8B 40 20                     mov r8, qword ptr [rax + 0x20]
0098B700  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0098B705  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0098B70A  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0098B70F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0098B714  C7 44 24 20 50 6F 45 74         mov dword ptr [rsp + 0x20], 0x74456f50
0098B71C  8D 57 01                        lea edx, [rdi + 1]
0098B71F  E8 2C DF ED FF                  call 0x140869650
0098B724  44 8B F0                        mov r14d, eax
0098B727  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0098B72C  85 C0                           test eax, eax
0098B72E  0F 88 B3 0E 00 00               js 0x14098c5e7
0098B734  48 89 BC 24 4C 01 00 00         mov qword ptr [rsp + 0x14c], rdi
0098B73C  89 BC 24 54 01 00 00            mov dword ptr [rsp + 0x154], edi
0098B743  48 89 BC 24 60 01 00 00         mov qword ptr [rsp + 0x160], rdi
0098B74B  C7 84 24 48 01 00 00 02 00 00 00  mov dword ptr [rsp + 0x148], 2
0098B756  48 89 9C 24 58 01 00 00         mov qword ptr [rsp + 0x158], rbx
0098B75E  48 8D 94 24 48 01 00 00         lea rdx, [rsp + 0x148]
0098B766  48 8D 0D 33 15 F9 FF            lea rcx, [rip - 0x6eacd]
0098B76D  E8 12 07 F9 FF                  call 0x14091be84
0098B772  44 8B F0                        mov r14d, eax
0098B775  85 C0                           test eax, eax
0098B777  0F 88 6A 0E 00 00               js 0x14098c5e7
0098B77D  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0098B781  E8 BE 53 AA FF                  call 0x140430b44
0098B786  C6 84 24 B8 01 00 00 01         mov byte ptr [rsp + 0x1b8], 1
0098B78E  44 8B 7B 30                     mov r15d, dword ptr [rbx + 0x30]
0098B792  44 89 7C 24 48                  mov dword ptr [rsp + 0x48], r15d
0098B797  44 8B DF                        mov r11d, edi
0098B79A  44 8D 47 2C                     lea r8d, [rdi + 0x2c]
0098B79E  44 89 84 24 80 00 00 00         mov dword ptr [rsp + 0x80], r8d
0098B7A6  44 8B D7                        mov r10d, edi
0098B7A9  48 B9 02 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000002
0098B7B3  4C 8D 73 34                     lea r14, [rbx + 0x34]
0098B7B7  4D 85 D2                        test r10, r10
0098B7BA  0F 84 58 01 00 00               je 0x14098b918
0098B7C0  45 8B 0E                        mov r9d, dword ptr [r14]
0098B7C3  41 8B C9                        mov ecx, r9d
0098B7C6  83 E1 1F                        and ecx, 0x1f
0098B7C9  48 83 C8 FF                     or rax, 0xffffffffffffffff
0098B7CD  48 D3 E0                        shl rax, cl
0098B7D0  49 23 42 08                     and rax, qword ptr [r10 + 8]
0098B7D4  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0098B7D9  41 C1 E9 05                     shr r9d, 5
0098B7DD  0F B6 C0                        movzx eax, al
0098B7E0  48 05 CB 5D B1 00               add rax, 0xb15dcb
0098B7E6  48 6B C8 25                     imul rcx, rax, 0x25
0098B7EA  0F B6 44 24 41                  movzx eax, byte ptr [rsp + 0x41]
0098B7EF  48 03 C8                        add rcx, rax
0098B7F2  48 6B D1 25                     imul rdx, rcx, 0x25
0098B7F6  0F B6 44 24 42                  movzx eax, byte ptr [rsp + 0x42]
0098B7FB  48 03 D0                        add rdx, rax
0098B7FE  48 6B CA 25                     imul rcx, rdx, 0x25
0098B802  0F B6 44 24 43                  movzx eax, byte ptr [rsp + 0x43]
0098B807  48 03 C8                        add rcx, rax
0098B80A  48 6B D1 25                     imul rdx, rcx, 0x25
0098B80E  0F B6 44 24 44                  movzx eax, byte ptr [rsp + 0x44]
0098B813  48 03 D0                        add rdx, rax
0098B816  48 6B CA 25                     imul rcx, rdx, 0x25
0098B81A  0F B6 44 24 45                  movzx eax, byte ptr [rsp + 0x45]
0098B81F  48 03 C8                        add rcx, rax
0098B822  48 6B D1 25                     imul rdx, rcx, 0x25
0098B826  0F B6 44 24 46                  movzx eax, byte ptr [rsp + 0x46]
0098B82B  48 03 D0                        add rdx, rax
0098B82E  4C 6B C2 25                     imul r8, rdx, 0x25
0098B832  0F B6 44 24 47                  movzx eax, byte ptr [rsp + 0x47]
0098B837  49 03 C0                        add rax, r8
0098B83A  41 8D 49 FF                     lea ecx, [r9 - 1]
0098B83E  8B C0                           mov eax, eax
0098B840  48 23 C8                        and rcx, rax
0098B843  4C 8D 4B 38                     lea r9, [rbx + 0x38]
0098B847  49 8B 01                        mov rax, qword ptr [r9]
0098B84A  48 8D 14 C8                     lea rdx, [rax + rcx*8]
0098B84E  44 8B 84 24 80 00 00 00         mov r8d, dword ptr [rsp + 0x80]
0098B856  48 B9 02 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000002
0098B860  4D 85 D2                        test r10, r10
0098B863  74 21                           je 0x14098b886
0098B865  49 8B 02                        mov rax, qword ptr [r10]
0098B868  48 23 C1                        and rax, rcx
0098B86B  48 3B C1                        cmp rax, rcx
0098B86E  75 08                           jne 0x14098b878
0098B870  48 8B 07                        mov rax, qword ptr [rdi]
0098B873  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0098B878  4D 85 D2                        test r10, r10
0098B87B  74 09                           je 0x14098b886
0098B87D  4D 8B 12                        mov r10, qword ptr [r10]
0098B880  41 F6 C2 01                     test r10b, 1
0098B884  74 20                           je 0x14098b8a6
0098B886  48 83 C2 08                     add rdx, 8
0098B88A  41 8B 0E                        mov ecx, dword ptr [r14]
0098B88D  48 C1 E9 05                     shr rcx, 5
0098B891  49 8B 01                        mov rax, qword ptr [r9]
0098B894  4C 8D 0C C8                     lea r9, [rax + rcx*8]
0098B898  49 3B D1                        cmp rdx, r9
0098B89B  73 76                           jae 0x14098b913
0098B89D  4C 8B 12                        mov r10, qword ptr [rdx]
0098B8A0  41 F6 C2 01                     test r10b, 1
0098B8A4  75 67                           jne 0x14098b90d
0098B8A6  4D 85 D2                        test r10, r10
0098B8A9  74 7C                           je 0x14098b927
0098B8AB  49 8B 52 10                     mov rdx, qword ptr [r10 + 0x10]
0098B8AF  41 81 FB 00 00 00 10            cmp r11d, 0x10000000
0098B8B6  0F 83 C5 0D 00 00               jae 0x14098c681
0098B8BC  0F B7 42 56                     movzx eax, word ptr [rdx + 0x56]
0098B8C0  44 03 C0                        add r8d, eax
0098B8C3  44 89 84 24 80 00 00 00         mov dword ptr [rsp + 0x80], r8d
0098B8CB  0F B7 4A 54                     movzx ecx, word ptr [rdx + 0x54]
0098B8CF  0F B7 42 52                     movzx eax, word ptr [rdx + 0x52]
0098B8D3  03 C8                           add ecx, eax
0098B8D5  0F B7 42 50                     movzx eax, word ptr [rdx + 0x50]
0098B8D9  44 03 D8                        add r11d, eax
0098B8DC  44 03 D9                        add r11d, ecx
0098B8DF  49 8B 42 18                     mov rax, qword ptr [r10 + 0x18]
0098B8E3  48 85 C0                        test rax, rax
0098B8E6  48 B9 02 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000002
0098B8F0  0F 84 BD FE FF FF               je 0x14098b7b3
0098B8F6  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
0098B8FA  48 C1 E8 10                     shr rax, 0x10
0098B8FE  D1 E8                           shr eax, 1
0098B900  25 FF FF FF 1F                  and eax, 0x1fffffff
0098B905  44 03 D8                        add r11d, eax
0098B908  E9 A6 FE FF FF                  jmp 0x14098b7b3
0098B90D  48 83 C2 08                     add rdx, 8
0098B911  EB 85                           jmp 0x14098b898
0098B913  4C 8B D7                        mov r10, rdi
0098B916  EB 8E                           jmp 0x14098b8a6
0098B918  4C 8D 4B 38                     lea r9, [rbx + 0x38]
0098B91C  4D 8B 11                        mov r10, qword ptr [r9]
0098B91F  49 8B D2                        mov rdx, r10
0098B922  E9 39 FF FF FF                  jmp 0x14098b860
0098B927  0F 57 C0                        xorps xmm0, xmm0
0098B92A  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
0098B932  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
0098B93A  B8 68 00 00 00                  mov eax, 0x68
0098B93F  89 84 24 FC 00 00 00            mov dword ptr [rsp + 0xfc], eax
0098B946  4D 8B CF                        mov r9, r15
0098B949  49 6B D7 68                     imul rdx, r15, 0x68
0098B94D  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
0098B955  41 BA FF FF FF 7F               mov r10d, 0x7fffffff
0098B95B  49 3B D2                        cmp rdx, r10
0098B95E  0F 83 F3 0A 00 00               jae 0x14098c457
0098B964  48 8D 4A 48                     lea rcx, [rdx + 0x48]
0098B968  49 3B CA                        cmp rcx, r10
0098B96B  0F 83 E6 0A 00 00               jae 0x14098c457
0098B971  C7 84 24 F0 00 00 00 48 00 00 00  mov dword ptr [rsp + 0xf0], 0x48
0098B97C  89 8C 24 F8 00 00 00            mov dword ptr [rsp + 0xf8], ecx
0098B983  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
0098B986  C1 E8 1C                        shr eax, 0x1c
0098B989  85 C0                           test eax, eax
0098B98B  0F 85 91 0C 00 00               jne 0x14098c622
0098B991  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
0098B999  C7 84 24 9C 00 00 00 B0 01 00 00  mov dword ptr [rsp + 0x9c], 0x1b0
0098B9A4  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
0098B9AC  C7 84 24 A0 00 00 00 08 00 00 00  mov dword ptr [rsp + 0xa0], 8
0098B9B7  44 8B AC 24 9C 00 00 00         mov r13d, dword ptr [rsp + 0x9c]
0098B9BF  4D 0F AF E9                     imul r13, r9
0098B9C3  41 3B CA                        cmp ecx, r10d
0098B9C6  0F 83 3A 0A 00 00               jae 0x14098c406
0098B9CC  4D 3B EA                        cmp r13, r10
0098B9CF  0F 83 31 0A 00 00               jae 0x14098c406
0098B9D5  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
0098B9DC  FF C9                           dec ecx
0098B9DE  03 C8                           add ecx, eax
0098B9E0  FF C8                           dec eax
0098B9E2  F7 D0                           not eax
0098B9E4  23 C8                           and ecx, eax
0098B9E6  89 8C 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], ecx
0098B9ED  8B C1                           mov eax, ecx
0098B9EF  49 03 C5                        add rax, r13
0098B9F2  49 3B C2                        cmp rax, r10
0098B9F5  0F 83 0B 0A 00 00               jae 0x14098c406
0098B9FB  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
0098BA02  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
0098BA0A  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
0098BA12  41 8B D0                        mov edx, r8d
0098BA15  41 3B C2                        cmp eax, r10d
0098BA18  0F 83 06 0A 00 00               jae 0x14098c424
0098BA1E  45 3B C2                        cmp r8d, r10d
0098BA21  0F 83 FD 09 00 00               jae 0x14098c424
0098BA27  8D 48 03                        lea ecx, [rax + 3]
0098BA2A  83 E1 FC                        and ecx, 0xfffffffc
0098BA2D  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0098BA31  8B C1                           mov eax, ecx
0098BA33  48 03 C2                        add rax, rdx
0098BA36  49 3B C2                        cmp rax, r10
0098BA39  0F 83 E5 09 00 00               jae 0x14098c424
0098BA3F  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
0098BA46  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
0098BA4B  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0098BA50  45 8B E3                        mov r12d, r11d
0098BA53  4D 03 E4                        add r12, r12
0098BA56  41 3B C2                        cmp eax, r10d
0098BA59  0F 83 E6 09 00 00               jae 0x14098c445
0098BA5F  4D 3B E2                        cmp r12, r10
0098BA62  0F 83 DD 09 00 00               jae 0x14098c445
0098BA68  44 8D 78 01                     lea r15d, [rax + 1]
0098BA6C  41 83 E7 FE                     and r15d, 0xfffffffe
0098BA70  45 8B F7                        mov r14d, r15d
0098BA73  4D 03 F4                        add r14, r12
0098BA76  4D 3B F2                        cmp r14, r10
0098BA79  0F 83 C6 09 00 00               jae 0x14098c445
0098BA7F  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
0098BA84  8B 84 24 B0 01 00 00            mov eax, dword ptr [rsp + 0x1b0]
0098BA8B  44 3B F0                        cmp r14d, eax
0098BA8E  0F 87 B7 0B 00 00               ja 0x14098c64b
0098BA94  45 3B F2                        cmp r14d, r10d
0098BA97  0F 83 AE 0B 00 00               jae 0x14098c64b
0098BA9D  45 8B C6                        mov r8d, r14d
0098BAA0  33 D2                           xor edx, edx
0098BAA2  48 8B CE                        mov rcx, rsi
0098BAA5  E8 96 B1 D3 FF                  call 0x1406c6c40
0098BAAA  BA 68 00 00 00                  mov edx, 0x68
0098BAAF  39 94 24 88 00 00 00            cmp dword ptr [rsp + 0x88], edx
0098BAB6  72 1A                           jb 0x14098bad2
0098BAB8  8B 8C 24 F0 00 00 00            mov ecx, dword ptr [rsp + 0xf0]
0098BABF  48 8D 04 0E                     lea rax, [rsi + rcx]
0098BAC3  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
0098BACB  89 8C 24 04 01 00 00            mov dword ptr [rsp + 0x104], ecx
0098BAD2  44 3B AC 24 9C 00 00 00         cmp r13d, dword ptr [rsp + 0x9c]
0098BADA  72 1A                           jb 0x14098baf6
0098BADC  8B 8C 24 B0 00 00 00            mov ecx, dword ptr [rsp + 0xb0]
0098BAE3  48 8D 04 0E                     lea rax, [rsi + rcx]
0098BAE7  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
0098BAEF  89 8C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ecx
0098BAF6  83 BC 24 80 00 00 00 01         cmp dword ptr [rsp + 0x80], 1
0098BAFE  72 17                           jb 0x14098bb17
0098BB00  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
0098BB04  48 8D 04 0E                     lea rax, [rsi + rcx]
0098BB08  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
0098BB10  89 8C 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], ecx
0098BB17  41 83 FC 02                     cmp r12d, 2
0098BB1B  72 10                           jb 0x14098bb2d
0098BB1D  41 8B C7                        mov eax, r15d
0098BB20  48 03 C6                        add rax, rsi
0098BB23  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0098BB28  44 89 7C 24 74                  mov dword ptr [rsp + 0x74], r15d
0098BB2D  48 89 B4 24 40 01 00 00         mov qword ptr [rsp + 0x140], rsi
0098BB35  C7 06 13 00 20 00               mov dword ptr [rsi], 0x200013
0098BB3B  C7 46 04 48 00 00 00            mov dword ptr [rsi + 4], 0x48
0098BB42  44 89 76 08                     mov dword ptr [rsi + 8], r14d
0098BB46  8B 83 60 02 00 00               mov eax, dword ptr [rbx + 0x260]
0098BB4C  89 46 0C                        mov dword ptr [rsi + 0xc], eax
0098BB4F  49 BB 20 03 00 00 80 F7 FF FF   movabs r11, 0xfffff78000000320
0098BB59  49 8B 03                        mov rax, qword ptr [r11]
0098BB5C  48 BB 04 00 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000004
0098BB66  8B 0B                           mov ecx, dword ptr [rbx]
0098BB68  48 0F AF C8                     imul rcx, rax
0098BB6C  48 C1 E9 18                     shr rcx, 0x18
0098BB70  89 4E 18                        mov dword ptr [rsi + 0x18], ecx
0098BB73  8B 84 24 F0 00 00 00            mov eax, dword ptr [rsp + 0xf0]
0098BB7A  89 46 24                        mov dword ptr [rsi + 0x24], eax
0098BB7D  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0098BB81  89 46 28                        mov dword ptr [rsi + 0x28], eax
0098BB84  C7 46 38 68 00 10 00            mov dword ptr [rsi + 0x38], 0x100068
0098BB8B  41 BA 10 00 00 00               mov r10d, 0x10
0098BB91  44 8B AC 24 D4 00 00 00         mov r13d, dword ptr [rsp + 0xd4]
0098BB99  44 89 6E 34                     mov dword ptr [rsi + 0x34], r13d
0098BB9D  41 8D 4A FC                     lea ecx, [r10 - 4]
0098BBA1  66 89 4E 3C                     mov word ptr [rsi + 0x3c], cx
0098BBA5  45 8D 45 0C                     lea r8d, [r13 + 0xc]
0098BBA9  44 8B 8C 24 C8 00 00 00         mov r9d, dword ptr [rsp + 0xc8]
0098BBB1  4C 8B BC 24 D8 00 00 00         mov r15, qword ptr [rsp + 0xd8]
0098BBB9  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0098BBBE  45 3B C1                        cmp r8d, r9d
0098BBC1  77 27                           ja 0x14098bbea
0098BBC3  F2 0F 10 42 20                  movsd xmm0, qword ptr [rdx + 0x20]
0098BBC8  F2 41 0F 11 07                  movsd qword ptr [r15], xmm0
0098BBCD  8B 42 28                        mov eax, dword ptr [rdx + 0x28]
0098BBD0  41 89 47 08                     mov dword ptr [r15 + 8], eax
0098BBD4  4C 03 F9                        add r15, rcx
0098BBD7  4C 89 BC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r15
0098BBDF  45 8B E8                        mov r13d, r8d
0098BBE2  44 89 84 24 D4 00 00 00         mov dword ptr [rsp + 0xd4], r8d
0098BBEA  44 89 6E 2C                     mov dword ptr [rsi + 0x2c], r13d
0098BBEE  41 8D 45 10                     lea eax, [r13 + 0x10]
0098BBF2  41 3B C1                        cmp eax, r9d
0098BBF5  77 21                           ja 0x14098bc18
0098BBF7  0F 10 82 64 02 00 00            movups xmm0, xmmword ptr [rdx + 0x264]
0098BBFE  F3 41 0F 7F 07                  movdqu xmmword ptr [r15], xmm0
0098BC03  4D 03 FA                        add r15, r10
0098BC06  4C 89 BC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r15
0098BC0E  44 8B E8                        mov r13d, eax
0098BC11  89 84 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], eax
0098BC18  0F 10 82 74 02 00 00            movups xmm0, xmmword ptr [rdx + 0x274]
0098BC1F  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
0098BC27  66 0F 7E C0                     movd eax, xmm0
0098BC2B  03 82 64 02 00 00               add eax, dword ptr [rdx + 0x264]
0098BC31  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
0098BC38  8B 84 24 E4 00 00 00            mov eax, dword ptr [rsp + 0xe4]
0098BC3F  03 82 68 02 00 00               add eax, dword ptr [rdx + 0x268]
0098BC45  89 84 24 E4 00 00 00            mov dword ptr [rsp + 0xe4], eax
0098BC4C  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
0098BC53  03 82 6C 02 00 00               add eax, dword ptr [rdx + 0x26c]
0098BC59  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
0098BC60  8B 84 24 EC 00 00 00            mov eax, dword ptr [rsp + 0xec]
0098BC67  03 82 70 02 00 00               add eax, dword ptr [rdx + 0x270]
0098BC6D  89 84 24 EC 00 00 00            mov dword ptr [rsp + 0xec], eax
0098BC74  44 89 6E 30                     mov dword ptr [rsi + 0x30], r13d
0098BC78  41 8D 45 10                     lea eax, [r13 + 0x10]
0098BC7C  41 3B C1                        cmp eax, r9d
0098BC7F  77 22                           ja 0x14098bca3
0098BC81  0F 10 84 24 E0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xe0]
0098BC89  F3 41 0F 7F 07                  movdqu xmmword ptr [r15], xmm0
0098BC8E  4D 03 FA                        add r15, r10
0098BC91  4C 89 BC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r15
0098BC99  44 8B E8                        mov r13d, eax
0098BC9C  89 84 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], eax
0098BCA3  48 8B F7                        mov rsi, rdi
0098BCA6  4C 8B B4 24 08 01 00 00         mov r14, qword ptr [rsp + 0x108]
0098BCAE  44 8B 64 24 74                  mov r12d, dword ptr [rsp + 0x74]
0098BCB3  41 BA 2F CB 04 00               mov r10d, 0x4cb2f
0098BCB9  48 8D 42 30                     lea rax, [rdx + 0x30]
0098BCBD  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0098BCC5  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
0098BCCD  48 85 F6                        test rsi, rsi
0098BCD0  0F 84 E9 06 00 00               je 0x14098c3bf
0098BCD6  48 89 B4 24 18 01 00 00         mov qword ptr [rsp + 0x118], rsi
0098BCDE  8B 50 04                        mov edx, dword ptr [rax + 4]
0098BCE1  8B CA                           mov ecx, edx
0098BCE3  83 E1 1F                        and ecx, 0x1f
0098BCE6  48 83 C8 FF                     or rax, 0xffffffffffffffff
0098BCEA  48 D3 E0                        shl rax, cl
0098BCED  48 23 46 08                     and rax, qword ptr [rsi + 8]
0098BCF1  C1 EA 05                        shr edx, 5
0098BCF4  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
0098BCF8  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
0098BD00  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0098BD05  48 89 BC 24 28 01 00 00         mov qword ptr [rsp + 0x128], rdi
0098BD0D  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
0098BD12  4C 8D 84 24 38 01 00 00         lea r8, [rsp + 0x138]
0098BD1A  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0098BD1F  41 B9 08 00 00 00               mov r9d, 8
0098BD25  4C 89 8C 24 28 01 00 00         mov qword ptr [rsp + 0x128], r9
0098BD2D  41 8B D2                        mov edx, r10d
0098BD30  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098BD35  41 8B C2                        mov eax, r10d
0098BD38  4C 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], r10
0098BD40  4C 89 54 24 40                  mov qword ptr [rsp + 0x40], r10
0098BD45  4C 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r10
0098BD4D  41 8B DA                        mov ebx, r10d
0098BD50  45 8B DA                        mov r11d, r10d
0098BD53  41 8B CA                        mov ecx, r10d
0098BD56  49 83 F9 08                     cmp r9, 8
0098BD5A  0F 8C C5 00 00 00               jl 0x14098be25
0098BD60  48 6B D0 25                     imul rdx, rax, 0x25
0098BD64  41 0F B6 00                     movzx eax, byte ptr [r8]
0098BD68  48 03 D0                        add rdx, rax
0098BD6B  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098BD70  41 0F B6 48 01                  movzx ecx, byte ptr [r8 + 1]
0098BD75  48 6B D2 25                     imul rdx, rdx, 0x25
0098BD79  48 03 D1                        add rdx, rcx
0098BD7C  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098BD81  41 0F B6 48 02                  movzx ecx, byte ptr [r8 + 2]
0098BD86  48 6B D2 25                     imul rdx, rdx, 0x25
0098BD8A  48 03 D1                        add rdx, rcx
0098BD8D  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098BD92  41 0F B6 48 03                  movzx ecx, byte ptr [r8 + 3]
0098BD97  48 6B D2 25                     imul rdx, rdx, 0x25
0098BD9B  48 03 D1                        add rdx, rcx
0098BD9E  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098BDA3  41 0F B6 48 04                  movzx ecx, byte ptr [r8 + 4]
0098BDA8  48 6B D2 25                     imul rdx, rdx, 0x25
0098BDAC  48 03 D1                        add rdx, rcx
0098BDAF  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098BDB4  41 0F B6 48 05                  movzx ecx, byte ptr [r8 + 5]
0098BDB9  48 6B D2 25                     imul rdx, rdx, 0x25
0098BDBD  48 03 D1                        add rdx, rcx
0098BDC0  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098BDC5  41 0F B6 48 06                  movzx ecx, byte ptr [r8 + 6]
0098BDCA  48 6B D2 25                     imul rdx, rdx, 0x25
0098BDCE  48 03 D1                        add rdx, rcx
0098BDD1  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098BDD6  41 0F B6 48 07                  movzx ecx, byte ptr [r8 + 7]
0098BDDB  48 6B D2 25                     imul rdx, rdx, 0x25
0098BDDF  48 03 D1                        add rdx, rcx
0098BDE2  48 8B C2                        mov rax, rdx
0098BDE5  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098BDEA  49 83 C0 08                     add r8, 8
0098BDEE  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0098BDF3  49 83 E9 08                     sub r9, 8
0098BDF7  4C 89 8C 24 28 01 00 00         mov qword ptr [rsp + 0x128], r9
0098BDFF  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
0098BE07  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098BE0C  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
0098BE14  48 8B DA                        mov rbx, rdx
0098BE17  4C 8B DA                        mov r11, rdx
0098BE1A  4C 8B D2                        mov r10, rdx
0098BE1D  48 8B CA                        mov rcx, rdx
0098BE20  E9 31 FF FF FF                  jmp 0x14098bd56
0098BE25  49 83 E9 01                     sub r9, 1
0098BE29  74 22                           je 0x14098be4d
0098BE2B  49 83 E9 01                     sub r9, 1
0098BE2F  0F 85 F6 03 00 00               jne 0x14098c22b
0098BE35  49 6B CA 25                     imul rcx, r10, 0x25
0098BE39  41 0F B6 00                     movzx eax, byte ptr [r8]
0098BE3D  48 03 C8                        add rcx, rax
0098BE40  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0098BE45  49 FF C0                        inc r8
0098BE48  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0098BE4D  48 6B D1 25                     imul rdx, rcx, 0x25
0098BE51  41 0F B6 00                     movzx eax, byte ptr [r8]
0098BE55  48 03 D0                        add rdx, rax
0098BE58  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098BE5D  49 FF C0                        inc r8
0098BE60  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0098BE65  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
0098BE69  FF C9                           dec ecx
0098BE6B  8B C2                           mov eax, edx
0098BE6D  48 23 C8                        and rcx, rax
0098BE70  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0098BE78  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0098BE7C  48 8D 14 C8                     lea rdx, [rax + rcx*8]
0098BE80  48 89 94 24 20 01 00 00         mov qword ptr [rsp + 0x120], rdx
0098BE88  48 BB 04 00 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000004
0098BE92  49 BB 20 03 00 00 80 F7 FF FF   movabs r11, 0xfffff78000000320
0098BE9C  48 89 BC 24 30 01 00 00         mov qword ptr [rsp + 0x130], rdi
0098BEA4  48 85 F6                        test rsi, rsi
0098BEA7  74 53                           je 0x14098befc
0098BEA9  48 8B 06                        mov rax, qword ptr [rsi]
0098BEAC  48 B9 02 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000002
0098BEB6  48 23 C1                        and rax, rcx
0098BEB9  48 3B C1                        cmp rax, rcx
0098BEBC  75 30                           jne 0x14098beee
0098BEBE  48 8B 07                        mov rax, qword ptr [rdi]
0098BEC1  4C 8B B4 24 08 01 00 00         mov r14, qword ptr [rsp + 0x108]
0098BEC9  4C 8B BC 24 D8 00 00 00         mov r15, qword ptr [rsp + 0xd8]
0098BED1  44 8B AC 24 D4 00 00 00         mov r13d, dword ptr [rsp + 0xd4]
0098BED9  44 8B 64 24 74                  mov r12d, dword ptr [rsp + 0x74]
0098BEDE  48 8B 94 24 20 01 00 00         mov rdx, qword ptr [rsp + 0x120]
0098BEE6  48 8B B4 24 18 01 00 00         mov rsi, qword ptr [rsp + 0x118]
0098BEEE  48 85 F6                        test rsi, rsi
0098BEF1  74 09                           je 0x14098befc
0098BEF3  48 8B 36                        mov rsi, qword ptr [rsi]
0098BEF6  40 F6 C6 01                     test sil, 1
0098BEFA  74 41                           je 0x14098bf3d
0098BEFC  48 83 C2 08                     add rdx, 8
0098BF00  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
0098BF08  8B 48 04                        mov ecx, dword ptr [rax + 4]
0098BF0B  48 C1 E9 05                     shr rcx, 5
0098BF0F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0098BF13  4C 8D 04 C8                     lea r8, [rax + rcx*8]
0098BF17  48 89 94 24 30 01 00 00         mov qword ptr [rsp + 0x130], rdx
0098BF1F  49 3B D0                        cmp rdx, r8
0098BF22  0F 83 8F 04 00 00               jae 0x14098c3b7
0098BF28  48 8B 32                        mov rsi, qword ptr [rdx]
0098BF2B  40 F6 C6 01                     test sil, 1
0098BF2F  0F 85 ED 02 00 00               jne 0x14098c222
0098BF35  48 89 94 24 20 01 00 00         mov qword ptr [rsp + 0x120], rdx
0098BF3D  48 89 B4 24 18 01 00 00         mov qword ptr [rsp + 0x118], rsi
0098BF45  48 85 F6                        test rsi, rsi
0098BF48  0F 84 8D 03 00 00               je 0x14098c2db
0098BF4E  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
0098BF52  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098BF57  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
0098BF5B  49 89 06                        mov qword ptr [r14], rax
0098BF5E  8B 46 28                        mov eax, dword ptr [rsi + 0x28]
0098BF61  41 89 46 08                     mov dword ptr [r14 + 8], eax
0098BF65  8B 46 2C                        mov eax, dword ptr [rsi + 0x2c]
0098BF68  0F B7 C8                        movzx ecx, ax
0098BF6B  41 89 4E 0C                     mov dword ptr [r14 + 0xc], ecx
0098BF6F  8B 86 00 02 00 00               mov eax, dword ptr [rsi + 0x200]
0098BF75  41 89 46 48                     mov dword ptr [r14 + 0x48], eax
0098BF79  8B 86 04 02 00 00               mov eax, dword ptr [rsi + 0x204]
0098BF7F  41 89 46 4C                     mov dword ptr [r14 + 0x4c], eax
0098BF83  0F 10 86 E8 01 00 00            movups xmm0, xmmword ptr [rsi + 0x1e8]
0098BF8A  41 0F 11 46 50                  movups xmmword ptr [r14 + 0x50], xmm0
0098BF8F  F2 0F 10 8E F8 01 00 00         movsd xmm1, qword ptr [rsi + 0x1f8]
0098BF97  F2 41 0F 11 4E 60               movsd qword ptr [r14 + 0x60], xmm1
0098BF9D  48 8B 42 20                     mov rax, qword ptr [rdx + 0x20]
0098BFA1  8B 08                           mov ecx, dword ptr [rax]
0098BFA3  41 89 4E 14                     mov dword ptr [r14 + 0x14], ecx
0098BFA7  48 8B 42 20                     mov rax, qword ptr [rdx + 0x20]
0098BFAB  8B 48 04                        mov ecx, dword ptr [rax + 4]
0098BFAE  41 89 4E 18                     mov dword ptr [r14 + 0x18], ecx
0098BFB2  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
0098BFB6  8B 08                           mov ecx, dword ptr [rax]
0098BFB8  41 89 4E 2C                     mov dword ptr [r14 + 0x2c], ecx
0098BFBC  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
0098BFC0  8B 48 04                        mov ecx, dword ptr [rax + 4]
0098BFC3  41 89 4E 30                     mov dword ptr [r14 + 0x30], ecx
0098BFC7  45 89 6E 28                     mov dword ptr [r14 + 0x28], r13d
0098BFCB  0F B7 42 56                     movzx eax, word ptr [rdx + 0x56]
0098BFCF  66 41 89 46 3C                  mov word ptr [r14 + 0x3c], ax
0098BFD4  0F B7 42 56                     movzx eax, word ptr [rdx + 0x56]
0098BFD8  4C 8B 4A 48                     mov r9, qword ptr [rdx + 0x48]
0098BFDC  42 8D 0C 28                     lea ecx, [rax + r13]
0098BFE0  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
0098BFE4  3B 8C 24 C8 00 00 00            cmp ecx, dword ptr [rsp + 0xc8]
0098BFEB  77 2D                           ja 0x14098c01a
0098BFED  8B D8                           mov ebx, eax
0098BFEF  44 8B C0                        mov r8d, eax
0098BFF2  49 8B D1                        mov rdx, r9
0098BFF5  49 8B CF                        mov rcx, r15
0098BFF8  E8 43 A8 D3 FF                  call 0x1406c6840
0098BFFD  4C 03 FB                        add r15, rbx
0098C000  4C 89 BC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r15
0098C008  44 8B 6C 24 48                  mov r13d, dword ptr [rsp + 0x48]
0098C00D  44 89 AC 24 D4 00 00 00         mov dword ptr [rsp + 0xd4], r13d
0098C015  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
0098C01A  0F B7 42 50                     movzx eax, word ptr [rdx + 0x50]
0098C01E  66 41 89 46 34                  mov word ptr [r14 + 0x34], ax
0098C023  45 89 66 10                     mov dword ptr [r14 + 0x10], r12d
0098C027  0F B7 42 50                     movzx eax, word ptr [rdx + 0x50]
0098C02B  4C 8B 4A 30                     mov r9, qword ptr [rdx + 0x30]
0098C02F  03 C0                           add eax, eax
0098C031  42 8D 0C 20                     lea ecx, [rax + r12]
0098C035  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
0098C039  44 8B 54 24 68                  mov r10d, dword ptr [rsp + 0x68]
0098C03E  41 3B CA                        cmp ecx, r10d
0098C041  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0098C046  77 2E                           ja 0x14098c076
0098C048  8B D8                           mov ebx, eax
0098C04A  44 8B C0                        mov r8d, eax
0098C04D  49 8B D1                        mov rdx, r9
0098C050  E8 EB A7 D3 FF                  call 0x1406c6840
0098C055  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0098C05A  48 03 CB                        add rcx, rbx
0098C05D  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0098C062  44 8B 64 24 48                  mov r12d, dword ptr [rsp + 0x48]
0098C067  44 89 64 24 74                  mov dword ptr [rsp + 0x74], r12d
0098C06C  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
0098C071  44 8B 54 24 68                  mov r10d, dword ptr [rsp + 0x68]
0098C076  0F B7 42 52                     movzx eax, word ptr [rdx + 0x52]
0098C07A  66 41 89 46 36                  mov word ptr [r14 + 0x36], ax
0098C07F  45 89 66 1C                     mov dword ptr [r14 + 0x1c], r12d
0098C083  0F B7 42 52                     movzx eax, word ptr [rdx + 0x52]
0098C087  4C 8B 4A 38                     mov r9, qword ptr [rdx + 0x38]
0098C08B  03 C0                           add eax, eax
0098C08D  46 8D 04 20                     lea r8d, [rax + r12]
0098C091  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
0098C096  45 3B C2                        cmp r8d, r10d
0098C099  77 2E                           ja 0x14098c0c9
0098C09B  8B D8                           mov ebx, eax
0098C09D  44 8B C0                        mov r8d, eax
0098C0A0  49 8B D1                        mov rdx, r9
0098C0A3  E8 98 A7 D3 FF                  call 0x1406c6840
0098C0A8  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0098C0AD  48 03 CB                        add rcx, rbx
0098C0B0  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0098C0B5  44 8B 64 24 48                  mov r12d, dword ptr [rsp + 0x48]
0098C0BA  44 89 64 24 74                  mov dword ptr [rsp + 0x74], r12d
0098C0BF  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
0098C0C4  44 8B 54 24 68                  mov r10d, dword ptr [rsp + 0x68]
0098C0C9  0F B7 42 54                     movzx eax, word ptr [rdx + 0x54]
0098C0CD  66 41 89 46 38                  mov word ptr [r14 + 0x38], ax
0098C0D2  45 89 66 20                     mov dword ptr [r14 + 0x20], r12d
0098C0D6  0F B7 42 54                     movzx eax, word ptr [rdx + 0x54]
0098C0DA  4C 8B 4A 40                     mov r9, qword ptr [rdx + 0x40]
0098C0DE  03 C0                           add eax, eax
0098C0E0  42 8D 14 20                     lea edx, [rax + r12]
0098C0E4  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
0098C0E8  41 3B D2                        cmp edx, r10d
0098C0EB  77 29                           ja 0x14098c116
0098C0ED  8B D8                           mov ebx, eax
0098C0EF  44 8B C0                        mov r8d, eax
0098C0F2  49 8B D1                        mov rdx, r9
0098C0F5  E8 46 A7 D3 FF                  call 0x1406c6840
0098C0FA  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0098C0FF  48 03 CB                        add rcx, rbx
0098C102  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0098C107  44 8B 64 24 48                  mov r12d, dword ptr [rsp + 0x48]
0098C10C  44 89 64 24 74                  mov dword ptr [rsp + 0x74], r12d
0098C111  44 8B 54 24 68                  mov r10d, dword ptr [rsp + 0x68]
0098C116  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0098C11A  48 85 C0                        test rax, rax
0098C11D  0F 84 6F 02 00 00               je 0x14098c392
0098C123  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
0098C127  48 C1 E8 10                     shr rax, 0x10
0098C12B  66 D1 E8                        shr ax, 1
0098C12E  66 41 89 46 3A                  mov word ptr [r14 + 0x3a], ax
0098C133  45 89 66 24                     mov dword ptr [r14 + 0x24], r12d
0098C137  41 0F B7 46 3A                  movzx eax, word ptr [r14 + 0x3a]
0098C13C  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
0098C140  48 83 C2 20                     add rdx, 0x20
0098C144  03 C0                           add eax, eax
0098C146  46 8D 04 20                     lea r8d, [rax + r12]
0098C14A  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
0098C14F  45 3B C2                        cmp r8d, r10d
0098C152  77 19                           ja 0x14098c16d
0098C154  8B D8                           mov ebx, eax
0098C156  44 8B C0                        mov r8d, eax
0098C159  E8 E2 A6 D3 FF                  call 0x1406c6840
0098C15E  48 01 5C 24 78                  add qword ptr [rsp + 0x78], rbx
0098C163  44 8B 64 24 48                  mov r12d, dword ptr [rsp + 0x48]
0098C168  44 89 64 24 74                  mov dword ptr [rsp + 0x74], r12d
0098C16D  44 8B 84 24 A4 00 00 00         mov r8d, dword ptr [rsp + 0xa4]
0098C175  45 89 46 40                     mov dword ptr [r14 + 0x40], r8d
0098C179  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0098C17E  8B 42 28                        mov eax, dword ptr [rdx + 0x28]
0098C181  C1 E8 1C                        shr eax, 0x1c
0098C184  85 C0                           test eax, eax
0098C186  0F 85 4F 02 00 00               jne 0x14098c3db
0098C18C  41 C7 46 44 B0 01 00 00         mov dword ptr [r14 + 0x44], 0x1b0
0098C194  8B 8C 24 9C 00 00 00            mov ecx, dword ptr [rsp + 0x9c]
0098C19B  42 8D 04 01                     lea eax, [rcx + r8]
0098C19F  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0098C1A3  3B 84 24 98 00 00 00            cmp eax, dword ptr [rsp + 0x98]
0098C1AA  77 30                           ja 0x14098c1dc
0098C1AC  8B D9                           mov ebx, ecx
0098C1AE  48 8D 56 30                     lea rdx, [rsi + 0x30]
0098C1B2  44 8B C1                        mov r8d, ecx
0098C1B5  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
0098C1BD  E8 7E A6 D3 FF                  call 0x1406c6840
0098C1C2  48 01 9C 24 A8 00 00 00         add qword ptr [rsp + 0xa8], rbx
0098C1CA  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
0098C1CF  44 89 84 24 A4 00 00 00         mov dword ptr [rsp + 0xa4], r8d
0098C1D7  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0098C1DC  8B 8C 24 04 01 00 00            mov ecx, dword ptr [rsp + 0x104]
0098C1E3  44 8B 84 24 FC 00 00 00         mov r8d, dword ptr [rsp + 0xfc]
0098C1EB  41 03 C8                        add ecx, r8d
0098C1EE  3B 8C 24 F8 00 00 00            cmp ecx, dword ptr [rsp + 0xf8]
0098C1F5  77 12                           ja 0x14098c209
0098C1F7  89 8C 24 04 01 00 00            mov dword ptr [rsp + 0x104], ecx
0098C1FE  4D 03 F0                        add r14, r8
0098C201  4C 89 B4 24 08 01 00 00         mov qword ptr [rsp + 0x108], r14
0098C209  48 BB 04 00 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000004
0098C213  49 BB 20 03 00 00 80 F7 FF FF   movabs r11, 0xfffff78000000320
0098C21D  E9 91 FA FF FF                  jmp 0x14098bcb3
0098C222  48 83 C2 08                     add rdx, 8
0098C226  E9 EC FC FF FF                  jmp 0x14098bf17
0098C22B  49 83 E9 01                     sub r9, 1
0098C22F  0F 84 89 00 00 00               je 0x14098c2be
0098C235  49 83 E9 01                     sub r9, 1
0098C239  74 6B                           je 0x14098c2a6
0098C23B  49 83 E9 01                     sub r9, 1
0098C23F  0F 84 65 01 00 00               je 0x14098c3aa
0098C245  49 83 E9 01                     sub r9, 1
0098C249  0F 84 51 01 00 00               je 0x14098c3a0
0098C24F  49 83 F9 01                     cmp r9, 1
0098C253  0F 85 0C FC FF FF               jne 0x14098be65
0098C259  48 6B 8C 24 88 00 00 00 25      imul rcx, qword ptr [rsp + 0x88], 0x25
0098C262  41 0F B6 00                     movzx eax, byte ptr [r8]
0098C266  48 03 C1                        add rax, rcx
0098C269  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0098C26E  49 FF C0                        inc r8
0098C271  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0098C276  48 6B C8 25                     imul rcx, rax, 0x25
0098C27A  41 0F B6 00                     movzx eax, byte ptr [r8]
0098C27E  48 03 C1                        add rax, rcx
0098C281  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0098C286  49 FF C0                        inc r8
0098C289  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0098C28E  48 6B D8 25                     imul rbx, rax, 0x25
0098C292  41 0F B6 00                     movzx eax, byte ptr [r8]
0098C296  48 03 D8                        add rbx, rax
0098C299  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0098C29E  49 FF C0                        inc r8
0098C2A1  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0098C2A6  4C 6B DB 25                     imul r11, rbx, 0x25
0098C2AA  41 0F B6 00                     movzx eax, byte ptr [r8]
0098C2AE  4C 03 D8                        add r11, rax
0098C2B1  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
0098C2B6  49 FF C0                        inc r8
0098C2B9  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0098C2BE  4D 6B D3 25                     imul r10, r11, 0x25
0098C2C2  41 0F B6 00                     movzx eax, byte ptr [r8]
0098C2C6  4C 03 D0                        add r10, rax
0098C2C9  4C 89 54 24 40                  mov qword ptr [rsp + 0x40], r10
0098C2CE  49 FF C0                        inc r8
0098C2D1  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0098C2D6  E9 5A FB FF FF                  jmp 0x14098be35
0098C2DB  49 8B 03                        mov rax, qword ptr [r11]
0098C2DE  8B 0B                           mov ecx, dword ptr [rbx]
0098C2E0  48 0F AF C8                     imul rcx, rax
0098C2E4  48 C1 E9 18                     shr rcx, 0x18
0098C2E8  89 8C 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], ecx
0098C2EF  49 B8 B0 03 00 00 80 F7 FF FF   movabs r8, 0xfffff780000003b0
0098C2F9  49 B9 08 00 00 00 80 F7 FF FF   movabs r9, 0xfffff78000000008
0098C303  49 8B 10                        mov rdx, qword ptr [r8]
0098C306  49 8B 09                        mov rcx, qword ptr [r9]
0098C309  49 8B 00                        mov rax, qword ptr [r8]
0098C30C  48 3B D0                        cmp rdx, rax
0098C30F  75 F2                           jne 0x14098c303
0098C311  48 2B CA                        sub rcx, rdx
0098C314  48 B8 4B 59 86 38 D6 C5 6D 34   movabs rax, 0x346dc5d63886594b
0098C31E  48 F7 E1                        mul rcx
0098C321  48 C1 EA 0B                     shr rdx, 0xb
0098C325  89 94 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], edx
0098C32C  48 B9 14 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000014
0098C336  48 8B 09                        mov rcx, qword ptr [rcx]
0098C339  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
0098C341  8B 94 24 B8 00 00 00            mov edx, dword ptr [rsp + 0xb8]
0098C348  8B C2                           mov eax, edx
0098C34A  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
0098C34F  41 2B 83 58 02 00 00            sub eax, dword ptr [r11 + 0x258]
0098C356  4C 8B 84 24 40 01 00 00         mov r8, qword ptr [rsp + 0x140]
0098C35E  41 89 40 10                     mov dword ptr [r8 + 0x10], eax
0098C362  8B 84 24 BC 00 00 00            mov eax, dword ptr [rsp + 0xbc]
0098C369  41 2B 83 5C 02 00 00            sub eax, dword ptr [r11 + 0x25c]
0098C370  41 89 40 14                     mov dword ptr [r8 + 0x14], eax
0098C374  41 89 50 1C                     mov dword ptr [r8 + 0x1c], edx
0098C378  E8 4F 0F AD FF                  call 0x14045d2cc
0098C37D  41 89 40 20                     mov dword ptr [r8 + 0x20], eax
0098C381  41 89 48 40                     mov dword ptr [r8 + 0x40], ecx
0098C385  48 C1 E9 20                     shr rcx, 0x20
0098C389  41 89 48 44                     mov dword ptr [r8 + 0x44], ecx
0098C38D  E9 B1 02 00 00                  jmp 0x14098c643
0098C392  66 41 89 7E 3A                  mov word ptr [r14 + 0x3a], di
0098C397  45 89 66 24                     mov dword ptr [r14 + 0x24], r12d
0098C39B  E9 CD FD FF FF                  jmp 0x14098c16d
0098C3A0  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0098C3A5  E9 CC FE FF FF                  jmp 0x14098c276
0098C3AA  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0098C3B2  E9 D7 FE FF FF                  jmp 0x14098c28e
0098C3B7  48 8B F7                        mov rsi, rdi
0098C3BA  E9 86 FB FF FF                  jmp 0x14098bf45
0098C3BF  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
0098C3C3  48 89 94 24 20 01 00 00         mov qword ptr [rsp + 0x120], rdx
0098C3CB  48 8B F2                        mov rsi, rdx
0098C3CE  48 89 94 24 18 01 00 00         mov qword ptr [rsp + 0x118], rdx
0098C3D6  E9 C1 FA FF FF                  jmp 0x14098be9c
0098C3DB  83 F8 01                        cmp eax, 1
0098C3DE  0F 85 B0 FD FF FF               jne 0x14098c194
0098C3E4  41 C7 46 44 B8 01 00 00         mov dword ptr [r14 + 0x44], 0x1b8
0098C3EC  E9 A3 FD FF FF                  jmp 0x14098c194
0098C3F1  44 8B F0                        mov r14d, eax
0098C3F4  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0098C3F9  44 8A BC 24 B8 01 00 00         mov r15b, byte ptr [rsp + 0x1b8]
0098C401  E9 E1 01 00 00                  jmp 0x14098c5e7
0098C406  41 8B C2                        mov eax, r10d
0098C409  44 8B AC 24 94 00 00 00         mov r13d, dword ptr [rsp + 0x94]
0098C411  8B 8C 24 90 00 00 00            mov ecx, dword ptr [rsp + 0x90]
0098C418  89 8C 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], ecx
0098C41F  E9 DE F5 FF FF                  jmp 0x14098ba02
0098C424  41 8B C2                        mov eax, r10d
0098C427  8B 8C 24 C4 00 00 00            mov ecx, dword ptr [rsp + 0xc4]
0098C42E  89 8C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ecx
0098C435  8B 8C 24 C0 00 00 00            mov ecx, dword ptr [rsp + 0xc0]
0098C43C  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0098C440  E9 01 F6 FF FF                  jmp 0x14098ba46
0098C445  45 8B F2                        mov r14d, r10d
0098C448  44 8B 64 24 64                  mov r12d, dword ptr [rsp + 0x64]
0098C44D  44 8B 7C 24 60                  mov r15d, dword ptr [rsp + 0x60]
0098C452  E9 2D F6 FF FF                  jmp 0x14098ba84
0098C457  41 8B CA                        mov ecx, r10d
0098C45A  8B 84 24 F4 00 00 00            mov eax, dword ptr [rsp + 0xf4]
0098C461  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0098C469  E9 15 F5 FF FF                  jmp 0x14098b983
0098C46E  48 83 C2 08                     add rdx, 8
0098C472  41 8B 4B 44                     mov ecx, dword ptr [r11 + 0x44]
0098C476  48 C1 E9 05                     shr rcx, 5
0098C47A  49 8B 43 48                     mov rax, qword ptr [r11 + 0x48]
0098C47E  4C 8D 04 C8                     lea r8, [rax + rcx*8]
0098C482  49 3B D0                        cmp rdx, r8
0098C485  0F 83 F9 00 00 00               jae 0x14098c584
0098C48B  4C 8B 12                        mov r10, qword ptr [rdx]
0098C48E  41 F6 C2 01                     test r10b, 1
0098C492  0F 85 E3 00 00 00               jne 0x14098c57b
0098C498  4D 85 D2                        test r10, r10
0098C49B  0F 84 F4 00 00 00               je 0x14098c595
0098C4A1  41 0F BA B2 EC 01 00 00 1F      btr dword ptr [r10 + 0x1ec], 0x1f
0098C4AA  4D 85 D2                        test r10, r10
0098C4AD  0F 84 D9 00 00 00               je 0x14098c58c
0098C4B3  45 8B 4B 44                     mov r9d, dword ptr [r11 + 0x44]
0098C4B7  41 8B C9                        mov ecx, r9d
0098C4BA  83 E1 1F                        and ecx, 0x1f
0098C4BD  48 83 C8 FF                     or rax, 0xffffffffffffffff
0098C4C1  48 D3 E0                        shl rax, cl
0098C4C4  49 23 42 08                     and rax, qword ptr [r10 + 8]
0098C4C8  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0098C4CD  41 C1 E9 05                     shr r9d, 5
0098C4D1  0F B6 C0                        movzx eax, al
0098C4D4  48 05 CB 5D B1 00               add rax, 0xb15dcb
0098C4DA  48 6B C8 25                     imul rcx, rax, 0x25
0098C4DE  0F B6 44 24 49                  movzx eax, byte ptr [rsp + 0x49]
0098C4E3  48 03 C8                        add rcx, rax
0098C4E6  48 6B D1 25                     imul rdx, rcx, 0x25
0098C4EA  0F B6 44 24 4A                  movzx eax, byte ptr [rsp + 0x4a]
0098C4EF  48 03 D0                        add rdx, rax
0098C4F2  48 6B CA 25                     imul rcx, rdx, 0x25
0098C4F6  0F B6 44 24 4B                  movzx eax, byte ptr [rsp + 0x4b]
0098C4FB  48 03 C8                        add rcx, rax
0098C4FE  48 6B D1 25                     imul rdx, rcx, 0x25
0098C502  0F B6 44 24 4C                  movzx eax, byte ptr [rsp + 0x4c]
0098C507  48 03 D0                        add rdx, rax
0098C50A  48 6B CA 25                     imul rcx, rdx, 0x25
0098C50E  0F B6 44 24 4D                  movzx eax, byte ptr [rsp + 0x4d]
0098C513  48 03 C8                        add rcx, rax
0098C516  48 6B D1 25                     imul rdx, rcx, 0x25
0098C51A  0F B6 44 24 4E                  movzx eax, byte ptr [rsp + 0x4e]
0098C51F  48 03 D0                        add rdx, rax
0098C522  4C 6B C2 25                     imul r8, rdx, 0x25
0098C526  0F B6 44 24 4F                  movzx eax, byte ptr [rsp + 0x4f]
0098C52B  49 03 C0                        add rax, r8
0098C52E  41 8D 49 FF                     lea ecx, [r9 - 1]
0098C532  8B C0                           mov eax, eax
0098C534  48 23 C8                        and rcx, rax
0098C537  49 8B 43 48                     mov rax, qword ptr [r11 + 0x48]
0098C53B  48 8D 14 C8                     lea rdx, [rax + rcx*8]
0098C53F  4D 85 D2                        test r10, r10
0098C542  0F 84 26 FF FF FF               je 0x14098c46e
0098C548  49 8B 02                        mov rax, qword ptr [r10]
0098C54B  48 B9 02 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000002
0098C555  48 23 C1                        and rax, rcx
0098C558  48 3B C1                        cmp rax, rcx
0098C55B  75 03                           jne 0x14098c560
0098C55D  48 8B 07                        mov rax, qword ptr [rdi]
0098C560  4D 85 D2                        test r10, r10
0098C563  0F 84 05 FF FF FF               je 0x14098c46e
0098C569  4D 8B 12                        mov r10, qword ptr [r10]
0098C56C  41 F6 C2 01                     test r10b, 1
0098C570  0F 84 22 FF FF FF               je 0x14098c498
0098C576  E9 F3 FE FF FF                  jmp 0x14098c46e
0098C57B  48 83 C2 08                     add rdx, 8
0098C57F  E9 FE FE FF FF                  jmp 0x14098c482
0098C584  4C 8B D7                        mov r10, rdi
0098C587  E9 0C FF FF FF                  jmp 0x14098c498
0098C58C  4D 8B 53 48                     mov r10, qword ptr [r11 + 0x48]
0098C590  49 8B D2                        mov rdx, r10
0098C593  EB AA                           jmp 0x14098c53f
0098C595  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0098C59A  48 8B CB                        mov rcx, rbx
0098C59D  E8 36 0C 00 00                  call 0x14098d1d8
0098C5A2  FF 83 60 02 00 00               inc dword ptr [rbx + 0x260]
0098C5A8  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
0098C5AF  89 83 58 02 00 00               mov dword ptr [rbx + 0x258], eax
0098C5B5  8B 84 24 BC 00 00 00            mov eax, dword ptr [rsp + 0xbc]
0098C5BC  89 83 5C 02 00 00               mov dword ptr [rbx + 0x25c], eax
0098C5C2  0F 57 C0                        xorps xmm0, xmm0
0098C5C5  0F 11 83 64 02 00 00            movups xmmword ptr [rbx + 0x264], xmm0
0098C5CC  0F 10 8C 24 E0 00 00 00         movups xmm1, xmmword ptr [rsp + 0xe0]
0098C5D4  F3 0F 7F 8B 74 02 00 00         movdqu xmmword ptr [rbx + 0x274], xmm1
0098C5DC  44 8B F7                        mov r14d, edi
0098C5DF  44 8A BC 24 B8 01 00 00         mov r15b, byte ptr [rsp + 0x1b8]
0098C5E7  45 84 FF                        test r15b, r15b
0098C5EA  0F 85 9C 00 00 00               jne 0x14098c68c
0098C5F0  48 85 DB                        test rbx, rbx
0098C5F3  0F 85 A1 00 00 00               jne 0x14098c69a
0098C5F9  41 8B C6                        mov eax, r14d
0098C5FC  4C 8D 9C 24 70 01 00 00         lea r11, [rsp + 0x170]
0098C604  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0098C608  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0098C60C  49 8B E3                        mov rsp, r11
0098C60F  41 5F                           pop r15
0098C611  41 5E                           pop r14
0098C613  41 5D                           pop r13
0098C615  41 5C                           pop r12
0098C617  5F                              pop rdi
0098C618  C3                              ret
0098C619  CC                              int3
0098C61A  41 BE BB 00 00 C0               mov r14d, 0xc00000bb
0098C620  EB C5                           jmp 0x14098c5e7
0098C622  83 F8 01                        cmp eax, 1
0098C625  0F 85 8C F3 FF FF               jne 0x14098b9b7
0098C62B  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
0098C633  C7 84 24 9C 00 00 00 B8 01 00 00  mov dword ptr [rsp + 0x9c], 0x1b8
0098C63E  E9 61 F3 FF FF                  jmp 0x14098b9a4
0098C643  4C 8B D7                        mov r10, rdi
0098C646  E9 5F FE FF FF                  jmp 0x14098c4aa
0098C64B  B9 0C 00 00 00                  mov ecx, 0xc
0098C650  3B C1                           cmp eax, ecx
0098C652  0F 82 4E F2 19 00               jb 0x140b2b8a6
0098C658  33 C0                           xor eax, eax
0098C65A  48 89 06                        mov qword ptr [rsi], rax
0098C65D  C7 06 13 00 20 00               mov dword ptr [rsi], 0x200013
0098C663  44 89 76 08                     mov dword ptr [rsi + 8], r14d
0098C667  E9 3A F2 19 00                  jmp 0x140b2b8a6
0098C66C  44 8B F0                        mov r14d, eax
0098C66F  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0098C674  44 8A BC 24 B8 01 00 00         mov r15b, byte ptr [rsp + 0x1b8]
0098C67C  E9 66 FF FF FF                  jmp 0x14098c5e7
0098C681  41 BE CD 00 00 C0               mov r14d, 0xc00000cd
0098C687  E9 53 FF FF FF                  jmp 0x14098c5df
0098C68C  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0098C690  E8 27 35 95 FF                  call 0x1402dfbbc
0098C695  E9 56 FF FF FF                  jmp 0x14098c5f0
0098C69A  BA 50 6F 45 74                  mov edx, 0x74456f50
0098C69F  48 8B CB                        mov rcx, rbx
0098C6A2  E8 39 B2 96 FF                  call 0x1402f78e0
0098C6A7  E9 4D FF FF FF                  jmp 0x14098c5f9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopEtEnergyTrackerQuery(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m124;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned int v_stack_m134;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int8 v_stack_m149;
    unsigned __int8 v_stack_m14A;
    unsigned __int8 v_stack_m14B;
    unsigned __int8 v_stack_m14C;
    unsigned __int8 v_stack_m14D;
    unsigned __int8 v_stack_m14E;
    unsigned __int8 v_stack_m14F;
    unsigned int v_stack_m150;
    unsigned __int8 v_stack_m151;
    unsigned __int8 v_stack_m152;
    unsigned __int8 v_stack_m153;
    unsigned __int8 v_stack_m154;
    unsigned __int8 v_stack_m155;
    unsigned __int8 v_stack_m156;
    unsigned __int8 v_stack_m157;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p48;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (368);
    v_rdi = 0;
    v_stack_m148 = 0;
    *(unsigned __int64 *)(v_rsp - 264) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 248) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 168) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 152) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 216) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 200) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 80) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 64) = v_xmm1;
    v_stack_m138 = v_xmm0;
    v_stack_m128 = v_xmm0;
    if ((*(unsigned __int64 *)(v_rip + 5096273)) == 0) goto loc_0098C61A;
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    v_stack_m170 = v_stack_m148;
    v_stack_m178 = 0x74456F50ULL;
    result = ObpReferenceObjectByHandleWithTag(a1, v_rdi + 1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5096244) + 32), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (sign_flag) goto loc_0098C5E7;
    v_stack_m4C = 0;
    v_stack_m44 = 0;
    v_stack_m38 = 0;
    v_stack_m50 = 2;
    v_stack_m40 = v_stack_m148;
    result = PsEnumProcesses(v_rip - 453325, v_stack_m50, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5096244) + 32), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (sign_flag) goto loc_0098C5E7;
    result = PopAcquireRwLockExclusive(v_stack_m148 + 16, v_stack_m50, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5096244) + 32), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_p20 = 1;
    v_stack_m150 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m148 + 48)));
    v_stack_m118 = (unsigned int)(v_rdi + 44);
loc_0098B7B3:
    if (0 == 0) goto loc_0098B918;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m148 + 52))))) & (31));
    result = (result) | (-1);
    result = (result) << ((unsigned __int8)(a1));
    result = (result) & (*(unsigned __int64 *)(0 + 8));
    v_stack_m158 = result;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m148 + 52))) >> (5));
    result = ((unsigned __int8)(result)) + (0xB15DCBULL);
    a1 = (a1) * (result);
    a1 = (a1) + (v_stack_m157);
    a2 = (v_stack_m50) * (a1);
    a2 = (a2) + (v_stack_m156);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_m155);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_m154);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_m153);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_m152);
    a3 = (v_rdi + 44) * (a2);
    result = (v_stack_m151) + (a3);
    a1 = (a4 - 1) & ((unsigned int)((unsigned int)(result)));
loc_0098B860:
    if (0 == 0) goto loc_0098B886;
    result = (*(unsigned __int64 *)(0)) & (a1);
    v_rbx = v_stack_m148;
    if (result == a1) {
        result = *(unsigned __int64 *)(v_rdi);
        v_rbx = v_stack_m148;
    }
    if (0 == 0) goto loc_0098B886;
    if ((((unsigned __int8)(*(unsigned __int64 *)(0))) & (1)) == 0) goto loc_0098B8A6;
loc_0098B886:
    a2 = (*(unsigned __int64 *)(v_stack_m148 + 56) + a1 * 8) + (8);
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m148 + 52))) >> (5);
loc_0098B898:
    if (a2 >= (*(unsigned __int64 *)(v_stack_m148 + 56) + a1 * 8)) goto loc_0098B913;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) != 0) goto loc_0098B90D;
loc_0098B8A6:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_0098B927;
    if (0 >= 0x10000000ULL) goto loc_0098C681;
    a3 = (unsigned int)(((unsigned int)(v_stack_m118)) + ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 86))));
    v_stack_m118 = a3;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 84)) + ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 82))));
    v_r11 = (unsigned int)((0) + ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 80))));
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)(a1)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24) == 0) goto loc_0098B7B3;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24) + 24)) >> (16);
    result = (unsigned int)((result) >> (1));
    result = (unsigned int)((result) & (0x1FFFFFFFULL));
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)(result)));
    goto loc_0098B7B3;
loc_0098B90D:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16)) + (8);
    goto loc_0098B898;
loc_0098B913:
    goto loc_0098B8A6;
loc_0098B918:
    goto loc_0098B860;
loc_0098B927:
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m9C = 104;
    a2 = (*(unsigned __int64 *)(v_rbx + 56)) * ((unsigned int)(*(unsigned int *)(v_stack_m148 + 48)));
    v_stack_m110 = a2;
    if (a2 >= ((unsigned int)(0x7FFFFFFFULL))) goto loc_0098C457;
    if ((a2 + 72) >= ((unsigned int)(0x7FFFFFFFULL))) goto loc_0098C457;
    v_stack_mA8 = 72;
    v_stack_mA0 = (unsigned int)(a2 + 72);
loc_0098B983:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 40))) >> (28));
    if ((unsigned int)(result) != 0) goto loc_0098C622;
    v_stack_m108 = v_xmm0;
    v_stack_mFC = 432;
loc_0098B9A4:
    v_stack_mF8 = v_xmm0;
    v_stack_mF8 = 8;
loc_0098B9B7:
    v_r13 = ((unsigned int)(v_stack_mFC)) * ((unsigned int)(*(unsigned int *)(v_stack_m148 + 48)));
    if (((unsigned int)(a2 + 72)) >= ((unsigned int)((unsigned int)(0x7FFFFFFFULL)))) goto loc_0098C406;
    if (v_r13 >= ((unsigned int)(0x7FFFFFFFULL))) goto loc_0098C406;
    a1 = (unsigned int)((a2 + 72) - 1);
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)(v_stack_mF8))));
    result = (unsigned int)(((unsigned int)(v_stack_mF8)) - 1);
    result = (unsigned int)(~(result));
    a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    v_stack_mE8 = (unsigned int)(a1);
    result = ((unsigned int)((unsigned int)(a1))) + (v_r13);
    if (result >= ((unsigned int)(0x7FFFFFFFULL))) goto loc_0098C406;
    v_stack_m100 = (unsigned int)(result);
loc_0098BA02:
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(0x7FFFFFFFULL)))) goto loc_0098C424;
    if (a3 >= ((unsigned int)((unsigned int)(0x7FFFFFFFULL)))) goto loc_0098C424;
    a1 = (unsigned int)((result + 3) & (0xFFFFFFFCULL));
    v_stack_m158 = (unsigned int)(a1);
    result = ((unsigned int)((unsigned int)(a1))) + ((unsigned int)(a3));
    if (result >= ((unsigned int)(0x7FFFFFFFULL))) goto loc_0098C424;
    v_stack_mD0 = (unsigned int)(result);
loc_0098BA46:
    v_stack_m138 = v_xmm0;
    v_stack_m128 = v_xmm0;
    v_r12 = ((unsigned int)((unsigned int)(v_r11))) + ((unsigned int)((unsigned int)(v_r11)));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(0x7FFFFFFFULL)))) goto loc_0098C445;
    if (v_r12 >= ((unsigned int)(0x7FFFFFFFULL))) goto loc_0098C445;
    v_r15 = (unsigned int)((result + 1) & (0xFFFFFFFEULL));
    v_r14 = ((unsigned int)((unsigned int)(v_r15))) + (v_r12);
    if (v_r14 >= ((unsigned int)(0x7FFFFFFFULL))) goto loc_0098C445;
    v_stack_m130 = (unsigned int)(v_r14);
loc_0098BA84:
    if (((unsigned int)(v_r14)) > ((unsigned int)((unsigned int)(v_stack_p18)))) goto loc_0098C64B;
    if (((unsigned int)(v_r14)) >= ((unsigned int)((unsigned int)(0x7FFFFFFFULL)))) goto loc_0098C64B;
    a2 = 0;
    result = memset(0, a2, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(*(unsigned int *)(v_stack_m148 + 48)));
    if (v_stack_m110 >= 104) {
        a1 = v_stack_mA8;
        result = a2 + a1 * 1;
        v_stack_m90 = result;
        v_stack_m94 = (unsigned int)(a1);
    }
    if (((unsigned int)(v_r13)) >= v_stack_mFC) {
        a1 = v_stack_mE8;
        result = a2 + a1 * 1;
        v_stack_mF0 = result;
        v_stack_mF4 = (unsigned int)(a1);
    }
    if (v_stack_m118 >= 1) {
        a1 = v_stack_m158;
        result = a2 + a1 * 1;
        v_stack_mC0 = result;
        v_stack_mC4 = (unsigned int)(a1);
    }
    if (((unsigned int)(v_r12)) >= 2) {
        result = (unsigned int)(v_r15);
        result = (result) + (0);
        v_stack_m120 = result;
        v_stack_m124 = (unsigned int)(v_r15);
    }
    v_stack_m58 = 0;
    *(unsigned int *)(a2) = 0x200013ULL;
    *(unsigned int *)(a2 + 4) = 72;
    *(unsigned int *)(a2 + 8) = (unsigned int)(v_r14);
    *(unsigned int *)(a2 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 608)));
    a1 = ((unsigned int)(*(unsigned int *)(v_rbx))) * (*(unsigned __int64 *)(v_r11));
    a1 = (a1) >> (24);
    *(unsigned int *)(a2 + 24) = (unsigned int)(a1);
    *(unsigned int *)(a2 + 36) = (unsigned int)((unsigned int)(v_stack_mA8));
    *(unsigned int *)(a2 + 40) = (unsigned int)((unsigned int)(v_stack_m150));
    *(unsigned int *)(a2 + 56) = 0x100068ULL;
    *(unsigned int *)(a2 + 52) = (unsigned int)((unsigned int)(v_stack_mC4));
    *(unsigned __int16 *)(a2 + 60) = (unsigned __int16)(16 - 4);
    result = (unsigned int)(v_stack_m150);
    v_r13 = (unsigned int)(v_stack_mC4);
    v_r15 = v_stack_mC0;
    if (((unsigned int)((unsigned int)(v_stack_mC4) + 12)) <= ((unsigned int)((unsigned int)(v_stack_mD0)))) {
        *(unsigned __int64 *)(v_stack_mC0) = v_xmm0;
        result = *(unsigned int *)(v_stack_m148 + 40);
        *(unsigned int *)(v_stack_mC0 + 8) = (unsigned int)(result);
        v_r15 = (v_stack_mC0) + (16 - 4);
        v_stack_mC0 = v_r15;
        v_r13 = (unsigned int)((unsigned int)(v_stack_mC4) + 12);
        v_stack_mC4 = (unsigned int)((unsigned int)(v_stack_mC4) + 12);
    }
    *(unsigned int *)(a2 + 44) = (unsigned int)(v_r13);
    if (((unsigned int)(v_r13 + 16)) <= ((unsigned int)((unsigned int)(v_stack_mD0)))) {
        *(unsigned __int64 *)(v_r15) = v_xmm0;
        v_r15 = (v_r15) + (16);
        v_stack_mC0 = v_r15;
        v_r13 = (unsigned int)(v_r13 + 16);
        v_stack_mC4 = (unsigned int)(v_r13 + 16);
    }
    v_stack_mB8 = v_xmm0;
    result = (unsigned int)((v_r13 + 16) + (*(unsigned int *)(v_stack_m148 + 612)));
    v_stack_mB8 = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(v_stack_mB4)) + (*(unsigned int *)(v_stack_m148 + 616)));
    v_stack_mB4 = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(v_stack_mB0)) + (*(unsigned int *)(v_stack_m148 + 620)));
    v_stack_mB0 = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(v_stack_mAC)) + (*(unsigned int *)(v_stack_m148 + 624)));
    v_stack_mAC = (unsigned int)(result);
    *(unsigned int *)(a2 + 48) = (unsigned int)(v_r13);
    if (((unsigned int)(v_r13 + 16)) <= ((unsigned int)((unsigned int)(v_stack_mD0)))) {
        *(unsigned __int64 *)(v_r15) = v_xmm0;
        v_r15 = (v_r15) + (16);
        v_stack_mC0 = v_r15;
        v_r13 = (unsigned int)(v_r13 + 16);
        v_stack_mC4 = (unsigned int)(v_r13 + 16);
    }
loc_0098BCB3:
    v_stack_m118 = v_stack_m148 + 48;
    v_stack_m88 = v_stack_m148 + 48;
    if (0 == 0) goto loc_0098C3BF;
    v_stack_m80 = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m148 + 48 + 4))))) & (31));
    result = (v_stack_m148 + 48) | (-1);
    result = (result) << ((unsigned __int8)(a1));
    result = (result) & (*(unsigned __int64 *)(0 + 8));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m148 + 48 + 4))) >> (5));
    v_stack_m150 = (unsigned int)(a2);
    v_stack_m60 = result;
    v_stack_m140 = 0;
    v_stack_m70 = 0;
    v_stack_m158 = 0;
    v_stack_m140 = v_stack_m60;
    v_stack_m70 = 8;
    v_stack_m158 = (unsigned int)((unsigned int)((unsigned int)(0x4CB2FULL)));
    v_stack_m110 = (unsigned int)(0x4CB2FULL);
    v_stack_m158 = (unsigned int)(0x4CB2FULL);
    v_stack_mE8 = (unsigned int)(0x4CB2FULL);
loc_0098BD56:
    if (8 < 8) goto loc_0098BE25;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(0x4CB2FULL)))) * ((unsigned int)((unsigned int)((unsigned int)(0x4CB2FULL))));
    a2 = (a2) + (*(unsigned __int8 *)(v_stack_m60));
    v_stack_m158 = a2;
    a2 = (a2) * (a2);
    a2 = (a2) + (*(unsigned __int8 *)(v_stack_m60 + 1));
    v_stack_m158 = a2;
    a2 = (a2) * (a2);
    a2 = (a2) + (*(unsigned __int8 *)(v_stack_m60 + 2));
    v_stack_m158 = a2;
    a2 = (a2) * (a2);
    a2 = (a2) + (*(unsigned __int8 *)(v_stack_m60 + 3));
    v_stack_m158 = a2;
    a2 = (a2) * (a2);
    a2 = (a2) + (*(unsigned __int8 *)(v_stack_m60 + 4));
    v_stack_m158 = a2;
    a2 = (a2) * (a2);
    a2 = (a2) + (*(unsigned __int8 *)(v_stack_m60 + 5));
    v_stack_m158 = a2;
    a2 = (a2) * (a2);
    a2 = (a2) + (*(unsigned __int8 *)(v_stack_m60 + 6));
    v_stack_m158 = a2;
    a2 = (a2) * (a2);
    a2 = (a2) + (*(unsigned __int8 *)(v_stack_m60 + 7));
    v_stack_m158 = a2;
    a3 = (v_stack_m60) + (8);
    v_stack_m140 = a3;
    a4 = (8) - (8);
    v_stack_m70 = a4;
    v_stack_m110 = a2;
    v_stack_m158 = a2;
    v_stack_mE8 = a2;
    goto loc_0098BD56;
loc_0098BE25:
    a4 = (a4) - (1);
    if (condition_is_equal) goto loc_0098BE4D;
    a4 = (a4) - (1);
    if (condition_is_not_equal) goto loc_0098C22B;
loc_0098BE35:
    a1 = (a2) * (a2);
    a1 = (a1) + (*(unsigned __int8 *)(a3));
    v_stack_m158 = a1;
    a3 = (a3) + 1;
    v_stack_m140 = a3;
loc_0098BE4D:
    a2 = (a2) * (a1);
    a2 = (a2) + (*(unsigned __int8 *)(a3));
    v_stack_m158 = a2;
    a3 = (a3) + 1;
    v_stack_m140 = a3;
loc_0098BE65:
    a1 = (unsigned int)(((unsigned int)(v_stack_m150)) - 1);
    a1 = (a1) & ((unsigned int)((unsigned int)(a2)));
    v_stack_m78 = *(unsigned __int64 *)(v_stack_m118 + 8) + a1 * 8;
loc_0098BE9C:
    v_stack_m68 = 0;
    if (0 == 0) goto loc_0098BEFC;
    result = (*(unsigned __int64 *)(0)) & (a1);
    v_rsi = 0;
    v_r12 = (unsigned int)(v_stack_m124);
    v_r14 = v_stack_m90;
    if (result == a1) {
        result = *(unsigned __int64 *)(v_rdi);
        v_r14 = v_stack_m90;
        v_r15 = v_stack_mC0;
        v_r13 = v_stack_mC4;
        v_r12 = v_stack_m124;
        a2 = v_stack_m78;
        v_rsi = v_stack_m80;
    }
    if (v_rsi == 0) goto loc_0098BEFC;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsi))) & (1)) == 0) goto loc_0098BF3D;
loc_0098BEFC:
    a2 = (a2) + (8);
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m88 + 4))) >> (5);
loc_0098BF17:
    v_stack_m68 = a2;
    if (a2 >= (*(unsigned __int64 *)(v_stack_m88 + 8) + a1 * 8)) goto loc_0098C3B7;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) != 0) goto loc_0098C222;
    v_stack_m78 = a2;
loc_0098BF3D:
    v_stack_m80 = *(unsigned __int64 *)(a2);
loc_0098BF45:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_0098C2DB;
    v_stack_m158 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16);
    *(unsigned __int64 *)(v_r14) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 32);
    *(unsigned int *)(v_r14 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 40)));
    *(unsigned int *)(v_r14 + 12) = (unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 44))));
    *(unsigned int *)(v_r14 + 72) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 512)));
    *(unsigned int *)(v_r14 + 76) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 516)));
    *(unsigned __int64 *)(v_r14 + 80) = v_xmm0;
    *(unsigned __int64 *)(v_r14 + 96) = v_xmm1;
    *(unsigned int *)(v_r14 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 32))));
    *(unsigned int *)(v_r14 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 32) + 4)));
    *(unsigned int *)(v_r14 + 44) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 40))));
    *(unsigned int *)(v_r14 + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 40) + 4)));
    *(unsigned int *)(v_r14 + 40) = (unsigned int)(v_r13);
    *(unsigned __int16 *)(v_r14 + 60) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 86));
    v_stack_m150 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 86) + v_r13 * 1);
    result = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 86);
    v_rbx = a2;
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 86) + v_r13 * 1)) <= v_stack_mD0) {
        v_rbx = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 86));
        a3 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 86));
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 72);
        a1 = v_r15;
        result = memcpy(a1, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16) + 72));
        v_r15 = (v_r15) + (v_rbx);
        v_stack_mC0 = v_r15;
        v_r13 = v_stack_m150;
        v_stack_mC4 = (unsigned int)(v_r13);
        a2 = v_stack_m158;
    }
    *(unsigned __int16 *)(v_r14 + 52) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 80));
    *(unsigned int *)(v_r14 + 16) = (unsigned int)(v_r12);
    result = (unsigned int)((*(unsigned __int16 *)(a2 + 80)) + ((unsigned int)(*(unsigned __int16 *)(a2 + 80))));
    v_stack_m150 = (unsigned int)(result + v_r12 * 1);
    v_r10 = (unsigned int)(v_stack_m130);
    if (((unsigned int)(result + v_r12 * 1)) <= ((unsigned int)((unsigned int)(v_stack_m130)))) {
        v_rbx = (unsigned int)(result);
        a3 = (unsigned int)(result);
        a2 = *(unsigned __int64 *)(a2 + 48);
        result = memcpy(v_stack_m120, a2, a3, *(unsigned __int64 *)(a2 + 48));
        a1 = v_stack_m120;
        a1 = (a1) + (v_rbx);
        v_stack_m120 = a1;
        v_r12 = v_stack_m150;
        v_stack_m124 = (unsigned int)(v_r12);
        a2 = v_stack_m158;
        v_r10 = v_stack_m130;
    }
    *(unsigned __int16 *)(v_r14 + 54) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 82));
    *(unsigned int *)(v_r14 + 28) = (unsigned int)(v_r12);
    result = (unsigned int)((*(unsigned __int16 *)(a2 + 82)) + ((unsigned int)(*(unsigned __int16 *)(a2 + 82))));
    v_stack_m150 = (unsigned int)(result + v_r12 * 1);
    if (((unsigned int)(result + v_r12 * 1)) <= ((unsigned int)(v_r10))) {
        v_rbx = (unsigned int)(result);
        a3 = (unsigned int)(result);
        a2 = *(unsigned __int64 *)(a2 + 56);
        result = memcpy(a1, a2, a3, *(unsigned __int64 *)(a2 + 56));
        a1 = v_stack_m120;
        a1 = (a1) + (v_rbx);
        v_stack_m120 = a1;
        v_r12 = v_stack_m150;
        v_stack_m124 = (unsigned int)(v_r12);
        a2 = v_stack_m158;
        v_r10 = v_stack_m130;
    }
    *(unsigned __int16 *)(v_r14 + 56) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 84));
    *(unsigned int *)(v_r14 + 32) = (unsigned int)(v_r12);
    result = (unsigned int)((*(unsigned __int16 *)(a2 + 84)) + ((unsigned int)(*(unsigned __int16 *)(a2 + 84))));
    v_stack_m150 = (unsigned int)(result + v_r12 * 1);
    if (((unsigned int)(result + v_r12 * 1)) <= ((unsigned int)(v_r10))) {
        v_rbx = (unsigned int)(result);
        a3 = (unsigned int)(result);
        a2 = *(unsigned __int64 *)(a2 + 64);
        result = memcpy(a1, a2, a3, *(unsigned __int64 *)(a2 + 64));
        a1 = v_stack_m120;
        a1 = (a1) + (v_rbx);
        v_stack_m120 = a1;
        v_r12 = v_stack_m150;
        v_stack_m124 = (unsigned int)(v_r12);
        v_r10 = v_stack_m130;
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24) == 0) goto loc_0098C392;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24) + 24)) >> (16);
    result = (unsigned __int16)((result) >> (1));
    *(unsigned __int16 *)(v_r14 + 58) = (unsigned __int16)(result);
    *(unsigned int *)(v_r14 + 36) = (unsigned int)(v_r12);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24)) + (32);
    result = (unsigned int)((*(unsigned __int16 *)(v_r14 + 58)) + ((unsigned int)(*(unsigned __int16 *)(v_r14 + 58))));
    v_stack_m150 = (unsigned int)(result + v_r12 * 1);
    if (((unsigned int)(result + v_r12 * 1)) <= ((unsigned int)(v_r10))) {
        v_rbx = (unsigned int)(result);
        a3 = (unsigned int)(result);
        result = memcpy(a1, a2, a3, *(unsigned __int64 *)(a2 + 64));
        v_r12 = v_stack_m150;
        v_stack_m124 = (unsigned int)(v_r12);
    }
    *(unsigned int *)(v_r14 + 64) = (unsigned int)((unsigned int)(v_stack_mF4));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m148 + 40))) >> (28));
    if ((unsigned int)(result) != 0) goto loc_0098C3DB;
    *(unsigned int *)(v_r14 + 68) = 432;
loc_0098C194:
    v_stack_m150 = (unsigned int)((unsigned int)(v_stack_mFC) + (unsigned int)(v_stack_mF4) * 1);
    result = (unsigned int)(v_stack_mFC) + (unsigned int)(v_stack_mF4) * 1;
    if (((unsigned int)((unsigned int)(v_stack_mFC) + (unsigned int)(v_stack_mF4) * 1)) <= v_stack_m100) {
        v_rbx = (unsigned int)((unsigned int)(v_stack_mFC));
        a2 = *(unsigned __int64 *)(a2) + 48;
        a3 = (unsigned int)((unsigned int)(v_stack_mFC));
        a1 = v_stack_mF0;
        result = memcpy(a1, a2, a3, *(unsigned __int64 *)(a2 + 64));
        a3 = v_stack_m150;
        v_stack_mF4 = a3;
        a2 = v_stack_m148;
    }
    a1 = (unsigned int)(((unsigned int)(v_stack_m94)) + ((unsigned int)((unsigned int)(v_stack_m9C))));
    if (((unsigned int)(a1)) <= v_stack_mA0) {
        v_stack_m94 = (unsigned int)(a1);
        v_r14 = (v_r14) + ((unsigned int)(v_stack_m9C));
        v_stack_m90 = v_r14;
    }
    goto loc_0098BCB3;
loc_0098C222:
    a2 = (a2) + (8);
    goto loc_0098BF17;
loc_0098C22B:
    a4 = (*(unsigned __int64 *)(a2 + 64)) - (1);
    if (condition_is_equal) goto loc_0098C2BE;
    a4 = (a4) - (1);
    if (condition_is_equal) goto loc_0098C2A6;
    a4 = (a4) - (1);
    if (condition_is_equal) goto loc_0098C3AA;
    a4 = (a4) - (1);
    if (condition_is_equal) goto loc_0098C3A0;
    if (a4 != 1) goto loc_0098BE65;
    a1 = (a1) * (v_stack_m110);
    result = (*(unsigned __int8 *)((unsigned int)(v_stack_m9C))) + (a1);
    v_stack_m158 = result;
    a3 = ((unsigned int)(v_stack_m9C)) + 1;
    v_stack_m140 = a3;
loc_0098C276:
    a1 = (a1) * (result);
    result = (*(unsigned __int8 *)(a3)) + (a1);
    v_stack_m158 = result;
    a3 = (a3) + 1;
    v_stack_m140 = a3;
loc_0098C28E:
    v_rbx = (v_rbx) * (result);
    v_rbx = (v_rbx) + (*(unsigned __int8 *)(a3));
    v_stack_m158 = v_rbx;
    a3 = (a3) + 1;
    v_stack_m140 = a3;
loc_0098C2A6:
    v_r11 = (a2) * (v_rbx);
    v_r11 = (v_r11) + (*(unsigned __int8 *)(a3));
    v_stack_m158 = v_r11;
    a3 = (a3) + 1;
    v_stack_m140 = a3;
loc_0098C2BE:
    v_r10 = (v_r10) * (v_r11);
    v_r10 = (v_r10) + (*(unsigned __int8 *)(a3));
    v_stack_m158 = v_r10;
    a3 = (a3) + 1;
    v_stack_m140 = a3;
    goto loc_0098BE35;
loc_0098C2DB:
    a1 = ((unsigned int)(*(unsigned int *)(v_rbx))) * (*(unsigned __int64 *)(v_r11));
    a1 = (a1) >> (24);
    v_stack_mE0 = (unsigned int)(a1);
loc_0098C303:
    if ((*(unsigned __int64 *)(a3)) != (*(unsigned __int64 *)(a3))) goto loc_0098C303;
    a1 = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(a3));
    a2 = (*(unsigned __int64 *)(a3)) >> (11);
    v_stack_mDC = (unsigned int)(a2);
    v_stack_m110 = *(unsigned __int64 *)(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mE0)))) - (*(unsigned int *)(v_stack_m148 + 600)));
    *(unsigned int *)(v_stack_m58 + 16) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(v_stack_mDC)) - (*(unsigned int *)(v_stack_m148 + 604)));
    *(unsigned int *)(v_stack_m58 + 20) = (unsigned int)(result);
    *(unsigned int *)(v_stack_m58 + 28) = (unsigned int)((unsigned int)(v_stack_mE0));
    result = KeQueryTimelineBitmapTime(*(unsigned __int64 *)(a1), (unsigned int)(v_stack_mE0), v_stack_m58, a4);
    *(unsigned int *)(v_stack_m58 + 32) = (unsigned int)(result);
    *(unsigned int *)(v_stack_m58 + 64) = (unsigned int)(*(unsigned __int64 *)(a1));
    a1 = (*(unsigned __int64 *)(a1)) >> (32);
    *(unsigned int *)(v_stack_m58 + 68) = (unsigned int)(a1);
    goto loc_0098C643;
loc_0098C392:
    *(unsigned __int16 *)(v_r14 + 58) = 0;
    *(unsigned int *)(v_r14 + 36) = (unsigned int)(v_r12);
    goto loc_0098C16D;
loc_0098C3A0:
    goto loc_0098C276;
loc_0098C3AA:
    goto loc_0098C28E;
loc_0098C3B7:
    goto loc_0098BF45;
loc_0098C3BF:
    v_stack_m78 = *(unsigned __int64 *)(v_stack_mE8 + 8);
    v_stack_m80 = *(unsigned __int64 *)(v_stack_mE8 + 8);
    goto loc_0098BE9C;
loc_0098C3DB:
    if (((unsigned int)(v_stack_mE8)) != 1) goto loc_0098C194;
    *(unsigned int *)(v_r14 + 68) = 440;
    goto loc_0098C194;
loc_0098C406:
    v_stack_mE8 = (unsigned int)((unsigned int)(v_stack_m108));
    goto loc_0098BA02;
loc_0098C424:
    v_stack_m118 = (unsigned int)((unsigned int)(v_stack_mD4));
    v_stack_m158 = (unsigned int)((unsigned int)(v_stack_mD8));
    goto loc_0098BA46;
loc_0098C445:
    goto loc_0098BA84;
loc_0098C457:
    v_stack_m110 = (unsigned int)(v_stack_mA4);
    goto loc_0098B983;
loc_0098C46E:
    a2 = (*(unsigned __int64 *)(v_stack_mE8 + 8)) + (8);
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m148 + 68))) >> (5);
loc_0098C482:
    if (a2 >= (*(unsigned __int64 *)(v_stack_m148 + 72) + a1 * 8)) goto loc_0098C584;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) != 0) goto loc_0098C57B;
loc_0098C498:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_0098C595;
loc_0098C4AA:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_0098C58C;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m148 + 68))))) & (31));
    result = (*(unsigned __int64 *)(v_stack_m148 + 72)) | (-1);
    result = (result) << ((unsigned __int8)(a1));
    result = (result) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 8));
    v_stack_m150 = result;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m148 + 68))) >> (5));
    result = ((unsigned __int8)(result)) + (0xB15DCBULL);
    a1 = (a1) * (result);
    a1 = (a1) + (v_stack_m14F);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_m14E);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_m14D);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_m14C);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_m14B);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_m14A);
    a3 = (*(unsigned __int64 *)(v_stack_m148 + 72) + a1 * 8) * (a2);
    result = (v_stack_m149) + (a3);
    a1 = (a4 - 1) & ((unsigned int)((unsigned int)(result)));
loc_0098C53F:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_0098C46E;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2))) & (a1);
    if (result == a1) {
        result = *(unsigned __int64 *)(v_rdi);
    }
    if (*(unsigned __int64 *)(a2) == 0) goto loc_0098C46E;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2)))) & (1)) == 0) goto loc_0098C498;
    goto loc_0098C46E;
loc_0098C57B:
    a2 = (*(unsigned __int64 *)(v_stack_m148 + 72) + a1 * 8) + (8);
    goto loc_0098C482;
loc_0098C584:
    goto loc_0098C498;
loc_0098C58C:
    goto loc_0098C53F;
loc_0098C595:
    result = PopEtEnergyTrackerCleanupAggregates(v_stack_m148, *(unsigned __int64 *)(v_stack_m148 + 72), a3, a4);
    *(unsigned int *)(v_stack_m148 + 600) = (unsigned int)((unsigned int)(v_stack_mE0));
    *(unsigned int *)(v_stack_m148 + 604) = (unsigned int)((unsigned int)(v_stack_mDC));
    *(unsigned __int64 *)(v_stack_m148 + 612) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m148 + 628) = v_xmm1;
loc_0098C5DF:
loc_0098C5E7:
    if ((unsigned __int8)(v_stack_p20) != 0) goto loc_0098C68C;
loc_0098C5F0:
    if (v_stack_m148 != 0) goto loc_0098C69A;
loc_0098C5F9:
    return 0;
loc_0098C61A:
    goto loc_0098C5E7;
loc_0098C622:
    if (0 != 1) goto loc_0098B9B7;
    v_stack_mE0 = v_xmm0;
    v_stack_mD4 = 440;
    goto loc_0098B9A4;
loc_0098C643:
    goto loc_0098C4AA;
loc_0098C64B:
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56)) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56)) = 0x200013ULL;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 8) = (unsigned int)((unsigned int)(0xC00000BBULL));
loc_0098C681:
    goto loc_0098C5DF;
loc_0098C68C:
    result = PopReleaseRwLock(*(unsigned __int64 *)(v_stack_m28 + 48) + 16, *(unsigned __int64 *)(v_stack_m148 + 72), a3, a4);
    goto loc_0098C5F0;
loc_0098C69A:
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_stack_m28 + 48), (unsigned int)(0x74456F50ULL), a3, a4);
    goto loc_0098C5F9;
}
```

## 5. (Beta) C Style

```c
int64_t PopEtEnergyTrackerQuery(int64_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m124;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint32_t v_stack_m134;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint8_t v_stack_m149;
    uint8_t v_stack_m14A;
    uint8_t v_stack_m14B;
    uint8_t v_stack_m14C;
    uint8_t v_stack_m14D;
    uint8_t v_stack_m14E;
    uint8_t v_stack_m14F;
    uint32_t v_stack_m150;
    uint8_t v_stack_m151;
    uint8_t v_stack_m152;
    uint8_t v_stack_m153;
    uint8_t v_stack_m154;
    uint8_t v_stack_m155;
    uint8_t v_stack_m156;
    uint8_t v_stack_m157;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint64_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint32_t v_stack_p18;
    uint8_t v_stack_p20;
    uint8_t v_stack_p48;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (368);
    local_rdi = 0;
    v_stack_m148 = 0;
    *(uint64_t *)(local_rsp - 0x108) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xF8) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xA8) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x98) = v_xmm1;
    *(uint64_t *)(local_rsp - 0xD8) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xC8) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x50) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x40) = v_xmm1;
    v_stack_m138 = v_xmm0;
    v_stack_m128 = v_xmm0;
    if ((*(uint64_t *)(v_rip + 0x4DC351)) == 0) goto loc_0098C61A;
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    v_stack_m170 = v_stack_m148;
    v_stack_m178 = 0x74456F50ULL;
    result = ObpReferenceObjectByHandleWithTag(Arg1, local_rdi + 1, *(uint64_t *)(*(uint64_t *)(v_rip + 0x4DC334) + 0x20), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (sign_flag) goto loc_0098C5E7;
    v_stack_m4C = 0;
    v_stack_m44 = 0;
    v_stack_m38 = 0;
    v_stack_m50 = 2;
    v_stack_m40 = v_stack_m148;
    result = PsEnumProcesses(v_rip - 453325, v_stack_m50, *(uint64_t *)(*(uint64_t *)(v_rip + 0x4DC334) + 0x20), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (sign_flag) goto loc_0098C5E7;
    result = PopAcquireRwLockExclusive(v_stack_m148 + 16, v_stack_m50, *(uint64_t *)(*(uint64_t *)(v_rip + 0x4DC334) + 0x20), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_p20 = 1;
    v_stack_m150 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x30)));
    v_stack_m118 = (uint32_t)(local_rdi + 44);
loc_0098B7B3:
    if (0 == 0) goto loc_0098B918;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x34))))) & (31));
    result = (result) | (-1);
    result = (result) << ((uint8_t)(Arg1));
    result = (result) & (*(uint64_t *)(0 + 0x8));
    v_stack_m158 = result;
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x34))) >> (5));
    result = ((uint8_t)(result)) + (0xB15DCBULL);
    Arg1 = (Arg1) * (result);
    Arg1 = (Arg1) + (v_stack_m157);
    Arg2 = (v_stack_m50) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m156);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_m155);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m154);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_m153);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m152);
    Arg3 = (local_rdi + 44) * (Arg2);
    result = (v_stack_m151) + (Arg3);
    Arg1 = (a4 - 1) & ((uint32_t)((uint32_t)(result)));
loc_0098B860:
    if (0 == 0) goto loc_0098B886;
    result = (*(uint64_t *)(0)) & (Arg1);
    local_rbx = v_stack_m148;
    if (result == Arg1) {
        result = *(uint64_t *)(local_rdi);
        local_rbx = v_stack_m148;
    }
    if (0 == 0) goto loc_0098B886;
    if ((((uint8_t)(*(uint64_t *)(0))) & (1)) == 0) goto loc_0098B8A6;
loc_0098B886:
    Arg2 = (*(uint64_t *)(v_stack_m148 + 0x38) + Arg1 * 8) + (8);
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x34))) >> (5);
loc_0098B898:
    if (Arg2 >= (*(uint64_t *)(v_stack_m148 + 0x38) + Arg1 * 8)) goto loc_0098B913;
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (1)) != 0) goto loc_0098B90D;
loc_0098B8A6:
    if (*(uint64_t *)(arg2) == 0) goto loc_0098B927;
    if (0 >= 0x10000000ULL) goto loc_0098C681;
    Arg3 = (uint32_t)(((uint32_t)(v_stack_m118)) + ((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x56))));
    v_stack_m118 = Arg3;
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x54)) + ((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x52))));
    local_r11 = (uint32_t)((0) + ((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x50))));
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)(Arg1)));
    if (*(uint64_t *)(*(uint64_t *)(arg2) + 0x18) == 0) goto loc_0098B7B3;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x18) + 0x18)) >> (16);
    result = (uint32_t)((result) >> (1));
    result = (uint32_t)((result) & (0x1FFFFFFFULL));
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)(result)));
    goto loc_0098B7B3;
loc_0098B90D:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg2) + 0x10)) + (8);
    goto loc_0098B898;
loc_0098B913:
    goto loc_0098B8A6;
loc_0098B918:
    goto loc_0098B860;
loc_0098B927:
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m9C = 104;
    Arg2 = (*(uint64_t *)(local_rbx + 0x38)) * ((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x30)));
    v_stack_m110 = Arg2;
    if (Arg2 >= ((uint32_t)(0x7FFFFFFFULL))) goto loc_0098C457;
    if ((Arg2 + 72) >= ((uint32_t)(0x7FFFFFFFULL))) goto loc_0098C457;
    v_stack_mA8 = 72;
    v_stack_mA0 = (uint32_t)(Arg2 + 72);
loc_0098B983:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x28))) >> (28));
    if ((uint32_t)(result) != 0) goto loc_0098C622;
    v_stack_m108 = v_xmm0;
    v_stack_mFC = 432;
loc_0098B9A4:
    v_stack_mF8 = v_xmm0;
    v_stack_mF8 = 8;
loc_0098B9B7:
    local_r13 = ((uint32_t)(v_stack_mFC)) * ((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x30)));
    if (((uint32_t)(Arg2 + 72)) >= ((uint32_t)((uint32_t)(0x7FFFFFFFULL)))) goto loc_0098C406;
    if (local_r13 >= ((uint32_t)(0x7FFFFFFFULL))) goto loc_0098C406;
    Arg1 = (uint32_t)((Arg2 + 72) - 1);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)(v_stack_mF8))));
    result = (uint32_t)(((uint32_t)(v_stack_mF8)) - 1);
    result = (uint32_t)(~(result));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    v_stack_mE8 = (uint32_t)(Arg1);
    result = ((uint32_t)((uint32_t)(Arg1))) + (local_r13);
    if (result >= ((uint32_t)(0x7FFFFFFFULL))) goto loc_0098C406;
    v_stack_m100 = (uint32_t)(result);
loc_0098BA02:
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(0x7FFFFFFFULL)))) goto loc_0098C424;
    if (Arg3 >= ((uint32_t)((uint32_t)(0x7FFFFFFFULL)))) goto loc_0098C424;
    Arg1 = (uint32_t)((result + 3) & (0xFFFFFFFCULL));
    v_stack_m158 = (uint32_t)(Arg1);
    result = ((uint32_t)((uint32_t)(Arg1))) + ((uint32_t)(Arg3));
    if (result >= ((uint32_t)(0x7FFFFFFFULL))) goto loc_0098C424;
    v_stack_mD0 = (uint32_t)(result);
loc_0098BA46:
    v_stack_m138 = v_xmm0;
    v_stack_m128 = v_xmm0;
    local_r12 = ((uint32_t)((uint32_t)(local_r11))) + ((uint32_t)((uint32_t)(local_r11)));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(0x7FFFFFFFULL)))) goto loc_0098C445;
    if (local_r12 >= ((uint32_t)(0x7FFFFFFFULL))) goto loc_0098C445;
    local_r15 = (uint32_t)((result + 1) & (0xFFFFFFFEULL));
    local_r14 = ((uint32_t)((uint32_t)(local_r15))) + (local_r12);
    if (local_r14 >= ((uint32_t)(0x7FFFFFFFULL))) goto loc_0098C445;
    v_stack_m130 = (uint32_t)(local_r14);
loc_0098BA84:
    if (((uint32_t)(local_r14)) > ((uint32_t)((uint32_t)(v_stack_p18)))) goto loc_0098C64B;
    if (((uint32_t)(local_r14)) >= ((uint32_t)((uint32_t)(0x7FFFFFFFULL)))) goto loc_0098C64B;
    Arg2 = 0;
    result = memset(0, Arg2, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(*(uint32_t *)(v_stack_m148 + 0x30)));
    if (v_stack_m110 >= 104) {
        Arg1 = v_stack_mA8;
        result = Arg2 + Arg1 * 1;
        v_stack_m90 = result;
        v_stack_m94 = (uint32_t)(Arg1);
    }
    if (((uint32_t)(local_r13)) >= v_stack_mFC) {
        Arg1 = v_stack_mE8;
        result = Arg2 + Arg1 * 1;
        v_stack_mF0 = result;
        v_stack_mF4 = (uint32_t)(Arg1);
    }
    if (v_stack_m118 >= 1) {
        Arg1 = v_stack_m158;
        result = Arg2 + Arg1 * 1;
        v_stack_mC0 = result;
        v_stack_mC4 = (uint32_t)(Arg1);
    }
    if (((uint32_t)(local_r12)) >= 2) {
        result = (uint32_t)(local_r15);
        result = (result) + (0);
        v_stack_m120 = result;
        v_stack_m124 = (uint32_t)(local_r15);
    }
    v_stack_m58 = 0;
    *(uint32_t *)(arg2) = 0x200013ULL;
    *(uint32_t *)(arg2 + 0x4) = 72;
    *(uint32_t *)(arg2 + 0x8) = (uint32_t)(local_r14);
    *(uint32_t *)(arg2 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x260)));
    Arg1 = ((uint32_t)(*(uint32_t *)(local_rbx))) * (*(uint64_t *)(local_r11));
    Arg1 = (Arg1) >> (24);
    *(uint32_t *)(arg2 + 0x18) = (uint32_t)(Arg1);
    *(uint32_t *)(arg2 + 0x24) = (uint32_t)((uint32_t)(v_stack_mA8));
    *(uint32_t *)(arg2 + 0x28) = (uint32_t)((uint32_t)(v_stack_m150));
    *(uint32_t *)(arg2 + 0x38) = 0x100068ULL;
    *(uint32_t *)(arg2 + 0x34) = (uint32_t)((uint32_t)(v_stack_mC4));
    *(uint16_t *)(arg2 + 0x3C) = (uint16_t)(16 - 4);
    result = (uint32_t)(v_stack_m150);
    local_r13 = (uint32_t)(v_stack_mC4);
    local_r15 = v_stack_mC0;
    if (((uint32_t)((uint32_t)(v_stack_mC4) + 12)) <= ((uint32_t)((uint32_t)(v_stack_mD0)))) {
        *(uint64_t *)(v_stack_mC0) = v_xmm0;
        result = *(uint32_t *)(v_stack_m148 + 0x28);
        *(uint32_t *)(v_stack_mC0 + 0x8) = (uint32_t)(result);
        local_r15 = (v_stack_mC0) + (16 - 4);
        v_stack_mC0 = local_r15;
        local_r13 = (uint32_t)((uint32_t)(v_stack_mC4) + 12);
        v_stack_mC4 = (uint32_t)((uint32_t)(v_stack_mC4) + 12);
    }
    *(uint32_t *)(arg2 + 0x2C) = (uint32_t)(local_r13);
    if (((uint32_t)(local_r13 + 16)) <= ((uint32_t)((uint32_t)(v_stack_mD0)))) {
        *(uint64_t *)(local_r15) = v_xmm0;
        local_r15 = (local_r15) + (16);
        v_stack_mC0 = local_r15;
        local_r13 = (uint32_t)(local_r13 + 16);
        v_stack_mC4 = (uint32_t)(local_r13 + 16);
    }
    v_stack_mB8 = v_xmm0;
    result = (uint32_t)((local_r13 + 16) + (*(uint32_t *)(v_stack_m148 + 0x264)));
    v_stack_mB8 = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(v_stack_mB4)) + (*(uint32_t *)(v_stack_m148 + 0x268)));
    v_stack_mB4 = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(v_stack_mB0)) + (*(uint32_t *)(v_stack_m148 + 0x26C)));
    v_stack_mB0 = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(v_stack_mAC)) + (*(uint32_t *)(v_stack_m148 + 0x270)));
    v_stack_mAC = (uint32_t)(result);
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)(local_r13);
    if (((uint32_t)(local_r13 + 16)) <= ((uint32_t)((uint32_t)(v_stack_mD0)))) {
        *(uint64_t *)(local_r15) = v_xmm0;
        local_r15 = (local_r15) + (16);
        v_stack_mC0 = local_r15;
        local_r13 = (uint32_t)(local_r13 + 16);
        v_stack_mC4 = (uint32_t)(local_r13 + 16);
    }
loc_0098BCB3:
    v_stack_m118 = v_stack_m148 + 48;
    v_stack_m88 = v_stack_m148 + 48;
    if (0 == 0) goto loc_0098C3BF;
    v_stack_m80 = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x30 + 0x4))))) & (31));
    result = (v_stack_m148 + 48) | (-1);
    result = (result) << ((uint8_t)(Arg1));
    result = (result) & (*(uint64_t *)(0 + 0x8));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x30 + 0x4))) >> (5));
    v_stack_m150 = (uint32_t)(Arg2);
    v_stack_m60 = result;
    v_stack_m140 = 0;
    v_stack_m70 = 0;
    v_stack_m158 = 0;
    v_stack_m140 = v_stack_m60;
    v_stack_m70 = 8;
    v_stack_m158 = (uint32_t)((uint32_t)((uint32_t)(0x4CB2FULL)));
    v_stack_m110 = (uint32_t)(0x4CB2FULL);
    v_stack_m158 = (uint32_t)(0x4CB2FULL);
    v_stack_mE8 = (uint32_t)(0x4CB2FULL);
loc_0098BD56:
    if (8 < 8) goto loc_0098BE25;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(0x4CB2FULL)))) * ((uint32_t)((uint32_t)((uint32_t)(0x4CB2FULL))));
    Arg2 = (Arg2) + (*(uint8_t *)(v_stack_m60));
    v_stack_m158 = Arg2;
    Arg2 = (Arg2) * (Arg2);
    Arg2 = (Arg2) + (*(uint8_t *)(v_stack_m60 + 0x1));
    v_stack_m158 = Arg2;
    Arg2 = (Arg2) * (Arg2);
    Arg2 = (Arg2) + (*(uint8_t *)(v_stack_m60 + 0x2));
    v_stack_m158 = Arg2;
    Arg2 = (Arg2) * (Arg2);
    Arg2 = (Arg2) + (*(uint8_t *)(v_stack_m60 + 0x3));
    v_stack_m158 = Arg2;
    Arg2 = (Arg2) * (Arg2);
    Arg2 = (Arg2) + (*(uint8_t *)(v_stack_m60 + 0x4));
    v_stack_m158 = Arg2;
    Arg2 = (Arg2) * (Arg2);
    Arg2 = (Arg2) + (*(uint8_t *)(v_stack_m60 + 0x5));
    v_stack_m158 = Arg2;
    Arg2 = (Arg2) * (Arg2);
    Arg2 = (Arg2) + (*(uint8_t *)(v_stack_m60 + 0x6));
    v_stack_m158 = Arg2;
    Arg2 = (Arg2) * (Arg2);
    Arg2 = (Arg2) + (*(uint8_t *)(v_stack_m60 + 0x7));
    v_stack_m158 = Arg2;
    Arg3 = (v_stack_m60) + (8);
    v_stack_m140 = Arg3;
    a4 = (8) - (8);
    v_stack_m70 = a4;
    v_stack_m110 = Arg2;
    v_stack_m158 = Arg2;
    v_stack_mE8 = Arg2;
    goto loc_0098BD56;
loc_0098BE25:
    a4 = (a4) - (1);
    if (condition_is_equal) goto loc_0098BE4D;
    a4 = (a4) - (1);
    if (condition_is_not_equal) goto loc_0098C22B;
loc_0098BE35:
    Arg1 = (Arg2) * (Arg2);
    Arg1 = (Arg1) + (*(uint8_t *)(Arg3));
    v_stack_m158 = Arg1;
    Arg3 = (Arg3) + 1;
    v_stack_m140 = Arg3;
loc_0098BE4D:
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (*(uint8_t *)(Arg3));
    v_stack_m158 = Arg2;
    Arg3 = (Arg3) + 1;
    v_stack_m140 = Arg3;
loc_0098BE65:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m150)) - 1);
    Arg1 = (Arg1) & ((uint32_t)((uint32_t)(Arg2)));
    v_stack_m78 = *(uint64_t *)(v_stack_m118 + 0x8) + Arg1 * 8;
loc_0098BE9C:
    v_stack_m68 = 0;
    if (0 == 0) goto loc_0098BEFC;
    result = (*(uint64_t *)(0)) & (Arg1);
    local_rsi = 0;
    local_r12 = (uint32_t)(v_stack_m124);
    local_r14 = v_stack_m90;
    if (result == Arg1) {
        result = *(uint64_t *)(local_rdi);
        local_r14 = v_stack_m90;
        local_r15 = v_stack_mC0;
        local_r13 = v_stack_mC4;
        local_r12 = v_stack_m124;
        Arg2 = v_stack_m78;
        local_rsi = v_stack_m80;
    }
    if (local_rsi == 0) goto loc_0098BEFC;
    if ((((uint8_t)(*(uint64_t *)(local_rsi))) & (1)) == 0) goto loc_0098BF3D;
loc_0098BEFC:
    Arg2 = (Arg2) + (8);
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x4))) >> (5);
loc_0098BF17:
    v_stack_m68 = Arg2;
    if (Arg2 >= (*(uint64_t *)(v_stack_m88 + 0x8) + Arg1 * 8)) goto loc_0098C3B7;
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (1)) != 0) goto loc_0098C222;
    v_stack_m78 = Arg2;
loc_0098BF3D:
    v_stack_m80 = *(uint64_t *)(arg2);
loc_0098BF45:
    if (*(uint64_t *)(arg2) == 0) goto loc_0098C2DB;
    v_stack_m158 = *(uint64_t *)(*(uint64_t *)(arg2) + 0x10);
    *(uint64_t *)(local_r14) = *(uint64_t *)(*(uint64_t *)(arg2) + 0x20);
    *(uint32_t *)(local_r14 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x28)));
    *(uint32_t *)(local_r14 + 0xC) = (uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x2C))));
    *(uint32_t *)(local_r14 + 0x48) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x200)));
    *(uint32_t *)(local_r14 + 0x4C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x204)));
    *(uint64_t *)(local_r14 + 0x50) = v_xmm0;
    *(uint64_t *)(local_r14 + 0x60) = v_xmm1;
    *(uint32_t *)(local_r14 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x20))));
    *(uint32_t *)(local_r14 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x20) + 0x4)));
    *(uint32_t *)(local_r14 + 0x2C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x28))));
    *(uint32_t *)(local_r14 + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x28) + 0x4)));
    *(uint32_t *)(local_r14 + 0x28) = (uint32_t)(local_r13);
    *(uint16_t *)(local_r14 + 0x3C) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x56));
    v_stack_m150 = (uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x56) + local_r13 * 1);
    result = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x56);
    local_rbx = Arg2;
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x56) + local_r13 * 1)) <= v_stack_mD0) {
        local_rbx = (uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x56));
        Arg3 = (uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x56));
        Arg2 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x48);
        Arg1 = local_r15;
        result = memcpy(Arg1, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x10) + 0x48));
        local_r15 = (local_r15) + (local_rbx);
        v_stack_mC0 = local_r15;
        local_r13 = v_stack_m150;
        v_stack_mC4 = (uint32_t)(local_r13);
        Arg2 = v_stack_m158;
    }
    *(uint16_t *)(local_r14 + 0x34) = (uint16_t)(*(uint16_t *)(arg2 + 0x50));
    *(uint32_t *)(local_r14 + 0x10) = (uint32_t)(local_r12);
    result = (uint32_t)((*(uint16_t *)(arg2 + 0x50)) + ((uint32_t)(*(uint16_t *)(arg2 + 0x50))));
    v_stack_m150 = (uint32_t)(result + local_r12 * 1);
    local_r10 = (uint32_t)(v_stack_m130);
    if (((uint32_t)(result + local_r12 * 1)) <= ((uint32_t)((uint32_t)(v_stack_m130)))) {
        local_rbx = (uint32_t)(result);
        Arg3 = (uint32_t)(result);
        Arg2 = *(uint64_t *)(arg2 + 0x30);
        result = memcpy(v_stack_m120, Arg2, Arg3, *(uint64_t *)(arg2 + 0x30));
        Arg1 = v_stack_m120;
        Arg1 = (Arg1) + (local_rbx);
        v_stack_m120 = Arg1;
        local_r12 = v_stack_m150;
        v_stack_m124 = (uint32_t)(local_r12);
        Arg2 = v_stack_m158;
        local_r10 = v_stack_m130;
    }
    *(uint16_t *)(local_r14 + 0x36) = (uint16_t)(*(uint16_t *)(arg2 + 0x52));
    *(uint32_t *)(local_r14 + 0x1C) = (uint32_t)(local_r12);
    result = (uint32_t)((*(uint16_t *)(arg2 + 0x52)) + ((uint32_t)(*(uint16_t *)(arg2 + 0x52))));
    v_stack_m150 = (uint32_t)(result + local_r12 * 1);
    if (((uint32_t)(result + local_r12 * 1)) <= ((uint32_t)(local_r10))) {
        local_rbx = (uint32_t)(result);
        Arg3 = (uint32_t)(result);
        Arg2 = *(uint64_t *)(arg2 + 0x38);
        result = memcpy(Arg1, Arg2, Arg3, *(uint64_t *)(arg2 + 0x38));
        Arg1 = v_stack_m120;
        Arg1 = (Arg1) + (local_rbx);
        v_stack_m120 = Arg1;
        local_r12 = v_stack_m150;
        v_stack_m124 = (uint32_t)(local_r12);
        Arg2 = v_stack_m158;
        local_r10 = v_stack_m130;
    }
    *(uint16_t *)(local_r14 + 0x38) = (uint16_t)(*(uint16_t *)(arg2 + 0x54));
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)(local_r12);
    result = (uint32_t)((*(uint16_t *)(arg2 + 0x54)) + ((uint32_t)(*(uint16_t *)(arg2 + 0x54))));
    v_stack_m150 = (uint32_t)(result + local_r12 * 1);
    if (((uint32_t)(result + local_r12 * 1)) <= ((uint32_t)(local_r10))) {
        local_rbx = (uint32_t)(result);
        Arg3 = (uint32_t)(result);
        Arg2 = *(uint64_t *)(arg2 + 0x40);
        result = memcpy(Arg1, Arg2, Arg3, *(uint64_t *)(arg2 + 0x40));
        Arg1 = v_stack_m120;
        Arg1 = (Arg1) + (local_rbx);
        v_stack_m120 = Arg1;
        local_r12 = v_stack_m150;
        v_stack_m124 = (uint32_t)(local_r12);
        local_r10 = v_stack_m130;
    }
    if (*(uint64_t *)(*(uint64_t *)(arg2) + 0x18) == 0) goto loc_0098C392;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x18) + 0x18)) >> (16);
    result = (uint16_t)((result) >> (1));
    *(uint16_t *)(local_r14 + 0x3A) = (uint16_t)(result);
    *(uint32_t *)(local_r14 + 0x24) = (uint32_t)(local_r12);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg2) + 0x18)) + (32);
    result = (uint32_t)((*(uint16_t *)(local_r14 + 0x3A)) + ((uint32_t)(*(uint16_t *)(local_r14 + 0x3A))));
    v_stack_m150 = (uint32_t)(result + local_r12 * 1);
    if (((uint32_t)(result + local_r12 * 1)) <= ((uint32_t)(local_r10))) {
        local_rbx = (uint32_t)(result);
        Arg3 = (uint32_t)(result);
        result = memcpy(Arg1, Arg2, Arg3, *(uint64_t *)(arg2 + 0x40));
        local_r12 = v_stack_m150;
        v_stack_m124 = (uint32_t)(local_r12);
    }
    *(uint32_t *)(local_r14 + 0x40) = (uint32_t)((uint32_t)(v_stack_mF4));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x28))) >> (28));
    if ((uint32_t)(result) != 0) goto loc_0098C3DB;
    *(uint32_t *)(local_r14 + 0x44) = 432;
loc_0098C194:
    v_stack_m150 = (uint32_t)((uint32_t)(v_stack_mFC) + (uint32_t)(v_stack_mF4) * 1);
    result = (uint32_t)(v_stack_mFC) + (uint32_t)(v_stack_mF4) * 1;
    if (((uint32_t)((uint32_t)(v_stack_mFC) + (uint32_t)(v_stack_mF4) * 1)) <= v_stack_m100) {
        local_rbx = (uint32_t)((uint32_t)(v_stack_mFC));
        Arg2 = *(uint64_t *)(arg2) + 48;
        Arg3 = (uint32_t)((uint32_t)(v_stack_mFC));
        Arg1 = v_stack_mF0;
        result = memcpy(Arg1, Arg2, Arg3, *(uint64_t *)(arg2 + 0x40));
        Arg3 = v_stack_m150;
        v_stack_mF4 = Arg3;
        Arg2 = v_stack_m148;
    }
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m94)) + ((uint32_t)((uint32_t)(v_stack_m9C))));
    if (((uint32_t)(Arg1)) <= v_stack_mA0) {
        v_stack_m94 = (uint32_t)(Arg1);
        local_r14 = (local_r14) + ((uint32_t)(v_stack_m9C));
        v_stack_m90 = local_r14;
    }
    goto loc_0098BCB3;
loc_0098C222:
    Arg2 = (Arg2) + (8);
    goto loc_0098BF17;
loc_0098C22B:
    a4 = (*(uint64_t *)(arg2 + 0x40)) - (1);
    if (condition_is_equal) goto loc_0098C2BE;
    a4 = (a4) - (1);
    if (condition_is_equal) goto loc_0098C2A6;
    a4 = (a4) - (1);
    if (condition_is_equal) goto loc_0098C3AA;
    a4 = (a4) - (1);
    if (condition_is_equal) goto loc_0098C3A0;
    if (a4 != 1) goto loc_0098BE65;
    Arg1 = (Arg1) * (v_stack_m110);
    result = (*(uint8_t *)((uint32_t)(v_stack_m9C))) + (Arg1);
    v_stack_m158 = result;
    Arg3 = ((uint32_t)(v_stack_m9C)) + 1;
    v_stack_m140 = Arg3;
loc_0098C276:
    Arg1 = (Arg1) * (result);
    result = (*(uint8_t *)(Arg3)) + (Arg1);
    v_stack_m158 = result;
    Arg3 = (Arg3) + 1;
    v_stack_m140 = Arg3;
loc_0098C28E:
    local_rbx = (local_rbx) * (result);
    local_rbx = (local_rbx) + (*(uint8_t *)(Arg3));
    v_stack_m158 = local_rbx;
    Arg3 = (Arg3) + 1;
    v_stack_m140 = Arg3;
loc_0098C2A6:
    local_r11 = (Arg2) * (local_rbx);
    local_r11 = (local_r11) + (*(uint8_t *)(Arg3));
    v_stack_m158 = local_r11;
    Arg3 = (Arg3) + 1;
    v_stack_m140 = Arg3;
loc_0098C2BE:
    local_r10 = (local_r10) * (local_r11);
    local_r10 = (local_r10) + (*(uint8_t *)(Arg3));
    v_stack_m158 = local_r10;
    Arg3 = (Arg3) + 1;
    v_stack_m140 = Arg3;
    goto loc_0098BE35;
loc_0098C2DB:
    Arg1 = ((uint32_t)(*(uint32_t *)(local_rbx))) * (*(uint64_t *)(local_r11));
    Arg1 = (Arg1) >> (24);
    v_stack_mE0 = (uint32_t)(Arg1);
loc_0098C303:
    if ((*(uint64_t *)(Arg3)) != (*(uint64_t *)(Arg3))) goto loc_0098C303;
    Arg1 = (*(uint64_t *)(a4)) - (*(uint64_t *)(Arg3));
    Arg2 = (*(uint64_t *)(Arg3)) >> (11);
    v_stack_mDC = (uint32_t)(Arg2);
    v_stack_m110 = *(uint64_t *)(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mE0)))) - (*(uint32_t *)(v_stack_m148 + 0x258)));
    *(uint32_t *)(v_stack_m58 + 0x10) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(v_stack_mDC)) - (*(uint32_t *)(v_stack_m148 + 0x25C)));
    *(uint32_t *)(v_stack_m58 + 0x14) = (uint32_t)(result);
    *(uint32_t *)(v_stack_m58 + 0x1C) = (uint32_t)((uint32_t)(v_stack_mE0));
    result = KeQueryTimelineBitmapTime(*(uint64_t *)(Arg1), (uint32_t)(v_stack_mE0), v_stack_m58, a4);
    *(uint32_t *)(v_stack_m58 + 0x20) = (uint32_t)(result);
    *(uint32_t *)(v_stack_m58 + 0x40) = (uint32_t)(*(uint64_t *)(Arg1));
    Arg1 = (*(uint64_t *)(Arg1)) >> (32);
    *(uint32_t *)(v_stack_m58 + 0x44) = (uint32_t)(Arg1);
    goto loc_0098C643;
loc_0098C392:
    *(uint16_t *)(local_r14 + 0x3A) = 0;
    *(uint32_t *)(local_r14 + 0x24) = (uint32_t)(local_r12);
    goto loc_0098C16D;
loc_0098C3A0:
    goto loc_0098C276;
loc_0098C3AA:
    goto loc_0098C28E;
loc_0098C3B7:
    goto loc_0098BF45;
loc_0098C3BF:
    v_stack_m78 = *(uint64_t *)(v_stack_mE8 + 0x8);
    v_stack_m80 = *(uint64_t *)(v_stack_mE8 + 0x8);
    goto loc_0098BE9C;
loc_0098C3DB:
    if (((uint32_t)(v_stack_mE8)) != 1) goto loc_0098C194;
    *(uint32_t *)(local_r14 + 0x44) = 440;
    goto loc_0098C194;
loc_0098C406:
    v_stack_mE8 = (uint32_t)((uint32_t)(v_stack_m108));
    goto loc_0098BA02;
loc_0098C424:
    v_stack_m118 = (uint32_t)((uint32_t)(v_stack_mD4));
    v_stack_m158 = (uint32_t)((uint32_t)(v_stack_mD8));
    goto loc_0098BA46;
loc_0098C445:
    goto loc_0098BA84;
loc_0098C457:
    v_stack_m110 = (uint32_t)(v_stack_mA4);
    goto loc_0098B983;
loc_0098C46E:
    Arg2 = (*(uint64_t *)(v_stack_mE8 + 0x8)) + (8);
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x44))) >> (5);
loc_0098C482:
    if (Arg2 >= (*(uint64_t *)(v_stack_m148 + 0x48) + Arg1 * 8)) goto loc_0098C584;
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (1)) != 0) goto loc_0098C57B;
loc_0098C498:
    if (*(uint64_t *)(arg2) == 0) goto loc_0098C595;
loc_0098C4AA:
    if (*(uint64_t *)(arg2) == 0) goto loc_0098C58C;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x44))))) & (31));
    result = (*(uint64_t *)(v_stack_m148 + 0x48)) | (-1);
    result = (result) << ((uint8_t)(Arg1));
    result = (result) & (*(uint64_t *)(*(uint64_t *)(arg2) + 0x8));
    v_stack_m150 = result;
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x44))) >> (5));
    result = ((uint8_t)(result)) + (0xB15DCBULL);
    Arg1 = (Arg1) * (result);
    Arg1 = (Arg1) + (v_stack_m14F);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m14E);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_m14D);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m14C);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_m14B);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m14A);
    Arg3 = (*(uint64_t *)(v_stack_m148 + 0x48) + Arg1 * 8) * (Arg2);
    result = (v_stack_m149) + (Arg3);
    Arg1 = (a4 - 1) & ((uint32_t)((uint32_t)(result)));
loc_0098C53F:
    if (*(uint64_t *)(arg2) == 0) goto loc_0098C46E;
    result = (*(uint64_t *)(*(uint64_t *)(arg2))) & (Arg1);
    if (result == Arg1) {
        result = *(uint64_t *)(local_rdi);
    }
    if (*(uint64_t *)(arg2) == 0) goto loc_0098C46E;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg2)))) & (1)) == 0) goto loc_0098C498;
    goto loc_0098C46E;
loc_0098C57B:
    Arg2 = (*(uint64_t *)(v_stack_m148 + 0x48) + Arg1 * 8) + (8);
    goto loc_0098C482;
loc_0098C584:
    goto loc_0098C498;
loc_0098C58C:
    goto loc_0098C53F;
loc_0098C595:
    result = PopEtEnergyTrackerCleanupAggregates(v_stack_m148, *(uint64_t *)(v_stack_m148 + 0x48), Arg3, a4);
    *(uint32_t *)(v_stack_m148 + 0x258) = (uint32_t)((uint32_t)(v_stack_mE0));
    *(uint32_t *)(v_stack_m148 + 0x25C) = (uint32_t)((uint32_t)(v_stack_mDC));
    *(uint64_t *)(v_stack_m148 + 0x264) = v_xmm0;
    *(uint64_t *)(v_stack_m148 + 0x274) = v_xmm1;
loc_0098C5DF:
loc_0098C5E7:
    if ((uint8_t)(v_stack_p20) != 0) goto loc_0098C68C;
loc_0098C5F0:
    if (v_stack_m148 != 0) goto loc_0098C69A;
loc_0098C5F9:
    return 0;
loc_0098C61A:
    goto loc_0098C5E7;
loc_0098C622:
    if (0 != 1) goto loc_0098B9B7;
    v_stack_mE0 = v_xmm0;
    v_stack_mD4 = 440;
    goto loc_0098B9A4;
loc_0098C643:
    goto loc_0098C4AA;
loc_0098C64B:
    result = 0;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38)) = 0;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38)) = 0x200013ULL;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8) = (uint32_t)((uint32_t)(0xC00000BBULL));
loc_0098C681:
    goto loc_0098C5DF;
loc_0098C68C:
    result = PopReleaseRwLock(*(uint64_t *)(v_stack_m28 + 0x30) + 16, *(uint64_t *)(v_stack_m148 + 0x48), Arg3, a4);
    goto loc_0098C5F0;
loc_0098C69A:
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_stack_m28 + 0x30), (uint32_t)(0x74456F50ULL), Arg3, a4);
    goto loc_0098C5F9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x0 + rcx*1` | `64` | `R` |
| `Arg2` | `+ 0x4` | `32` | `W` |
| `Arg2` | `+ 0x8` | `32` | `W` |
| `Arg2` | `+ 0xC` | `32` | `W` |
| `Arg2` | `+ 0x18` | `32` | `W` |
| `Arg2` | `+ 0x24` | `32` | `W` |
| `Arg2` | `+ 0x28` | `32` | `W` |
| `Arg2` | `+ 0x2C` | `32` | `W` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x34` | `32` | `W` |
| `Arg2` | `+ 0x38` | `32` | `W` |
| `Arg2` | `+ 0x3C` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0098B668&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
