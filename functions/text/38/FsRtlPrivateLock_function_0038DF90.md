# FsRtlPrivateLock

- RVA: `0x0038DF90`–`0x0038E5C0` (길이 `1,584` bytes)
- VA: `0x000000014038DF90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000805C8`
- 디코드: `364`개 명령, `1,584/1,584` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0038E00C` → [FsRtlPrivateInitializeFileLock](FsRtlPrivateInitializeFileLock_function_0038ED34.md) (function, `0x0038ED34`)
- `0x0038E09E` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0038E0E8` → [ExAllocateFromNPagedLookasideList](ExAllocateFromNPagedLookasideList_function_0038E6C0.md) (function, `0x0038E6C0`)
- `0x0038E123` → [FsRtlPrivateInsertSharedLock](FsRtlPrivateInsertSharedLock_function_0038E810.md) (function, `0x0038E810`)
- `0x0038E15F` → [FsRtlPrivateCheckForExclusiveLockAccess](FsRtlPrivateCheckForExclusiveLockAccess_function_0038EA28.md) (function, `0x0038EA28`)
- `0x0038E1A2` → [ExAllocateFromNPagedLookasideList](ExAllocateFromNPagedLookasideList_function_0038E6C0.md) (function, `0x0038E6C0`)
- `0x0038E1D5` → [FsRtlPrivateInsertExclusiveLock](FsRtlPrivateInsertExclusiveLock_function_0038EBFC.md) (function, `0x0038EBFC`)
- `0x0038E239` → [RtlSplay](RtlSplay_function_0038F1E0.md) (function, `0x0038F1E0`)
- `0x0038E2D6` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x0038E2E5` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x0038E362` → [ExAllocateFromNPagedLookasideList](ExAllocateFromNPagedLookasideList_function_0038E6C0.md) (function, `0x0038E6C0`)
- `0x0038E43F` → [RtlRealSuccessor](RtlRealSuccessor_function_0038DF40.md) (function, `0x0038DF40`)
- `0x0038E45B` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x0038E46A` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x0038E493` → [FsRtlPrivateCancelFileLockIrp](../4D/FsRtlPrivateCancelFileLockIrp_function_004D4B70.md) (function, `0x004D4B70`)
- `0x0038E4B4` → [ExFreeToNPagedLookasideList](ExFreeToNPagedLookasideList_function_0038D9D0.md) (function, `0x0038D9D0`)
- `0x0038E4E6` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0038E539` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x0038E550` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0038E56A` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x0038E57C` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0038E599` → [FsRtlPrivateRemoveLock](../4E/FsRtlPrivateRemoveLock_function_004E3244.md) (function, `0x004E3244`)

### Direct callers
- [FsRtlProcessFileLock](../3F/FsRtlProcessFileLock_function_003FD0E0.md) at `0x003FD180`

### Static image references
- `0x0038E0E1` → RVA `0x00E12200` (`.data`; read)
- `0x0038E19B` → RVA `0x00E12180` (`.data`; read)
- `0x0038E35B` → RVA `0x00E12000` (`.data`; read)
- `0x0038E3B0` → RVA `0x004D4B70` (`FsRtlPrivateCancelFileLockIrp`; read)
- `0x0038E4C3` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0038E4D6` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0038E522` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0038E5AD` → [sub_006E5690](../6E/Unknown_function_006E5690.md) (`tail-transfer`)
  - `0x0038E5BB` → [sub_006E5690](../6E/Unknown_function_006E5690.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0038DF90  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0038DF95  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0038DF9A  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0038DF9F  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0038DFA4  57                              push rdi
0038DFA5  41 54                           push r12
0038DFA7  41 55                           push r13
0038DFA9  41 56                           push r14
0038DFAB  41 57                           push r15
0038DFAD  48 81 EC A0 00 00 00            sub rsp, 0xa0
0038DFB4  49 8B F9                        mov rdi, r9
0038DFB7  49 8B C0                        mov rax, r8
0038DFBA  4C 8B EA                        mov r13, rdx
0038DFBD  48 8B D9                        mov rbx, rcx
0038DFC0  48 8B B4 24 18 01 00 00         mov rsi, qword ptr [rsp + 0x118]
0038DFC8  45 32 E4                        xor r12b, r12b
0038DFCB  44 88 64 24 32                  mov byte ptr [rsp + 0x32], r12b
0038DFD0  48 C7 44 24 48 00 00 00 00      mov qword ptr [rsp + 0x48], 0
0038DFD9  45 33 FF                        xor r15d, r15d
0038DFDC  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
0038DFE1  C6 44 24 31 FF                  mov byte ptr [rsp + 0x31], 0xff
0038DFE6  0F 57 C0                        xorps xmm0, xmm0
0038DFE9  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
0038DFEE  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
0038DFF3  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
0038DFF8  48 85 F6                        test rsi, rsi
0038DFFB  0F 94 C2                        sete dl
0038DFFE  4C 8B 71 18                     mov r14, qword ptr [rcx + 0x18]
0038E002  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0038E007  4D 85 F6                        test r14, r14
0038E00A  75 2D                           jne 0x14038e039
0038E00C  E8 23 0D 00 00                  call 0x14038ed34
0038E011  84 C0                           test al, al
0038E013  75 0F                           jne 0x14038e024
0038E015  48 8B BC 24 10 01 00 00         mov rdi, qword ptr [rsp + 0x110]
0038E01D  32 DB                           xor bl, bl
0038E01F  E9 2A 01 00 00                  jmp 0x14038e14e
0038E024  C6 43 10 01                     mov byte ptr [rbx + 0x10], 1
0038E028  4C 8B 73 18                     mov r14, qword ptr [rbx + 0x18]
0038E02C  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0038E031  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
0038E039  48 8B 18                        mov rbx, qword ptr [rax]
0038E03C  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
0038E041  48 8B 3F                        mov rdi, qword ptr [rdi]
0038E044  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
0038E049  48 8D 4F FF                     lea rcx, [rdi - 1]
0038E04D  48 03 CB                        add rcx, rbx
0038E050  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
0038E058  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
0038E05F  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
0038E063  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
0038E068  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0038E070  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0038E075  0F B6 84 24 08 01 00 00         movzx eax, byte ptr [rsp + 0x108]
0038E07D  88 44 24 68                     mov byte ptr [rsp + 0x68], al
0038E081  4D 8D 7E 18                     lea r15, [r14 + 0x18]
0038E085  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
0038E08A  48 3B CB                        cmp rcx, rbx
0038E08D  0F 82 57 02 00 00               jb 0x14038e2ea
0038E093  41 B4 01                        mov r12b, 1
0038E096  44 88 64 24 32                  mov byte ptr [rsp + 0x32], r12b
0038E09B  49 8B CF                        mov rcx, r15
0038E09E  E8 CD A3 E7 FF                  call 0x140208470
0038E0A3  88 44 24 31                     mov byte ptr [rsp + 0x31], al
0038E0A7  0F B6 8C 24 08 01 00 00         movzx ecx, byte ptr [rsp + 0x108]
0038E0AF  84 C9                           test cl, cl
0038E0B1  0F 85 A0 00 00 00               jne 0x14038e157
0038E0B7  48 C7 44 24 38 00 00 00 00      mov qword ptr [rsp + 0x38], 0
0038E0C0  41 0F B6 C4                     movzx eax, r12b
0038E0C4  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0038E0C8  88 44 24 33                     mov byte ptr [rsp + 0x33], al
0038E0CC  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
0038E0D0  48 85 C0                        test rax, rax
0038E0D3  0F 85 06 01 00 00               jne 0x14038e1df
0038E0D9  84 C9                           test cl, cl
0038E0DB  0F 85 BA 00 00 00               jne 0x14038e19b
0038E0E1  48 8D 0D 18 41 A8 00            lea rcx, [rip + 0xa84118]
0038E0E8  E8 D3 05 00 00                  call 0x14038e6c0
0038E0ED  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0038E0F5  48 85 C0                        test rax, rax
0038E0F8  0F 84 C7 01 00 00               je 0x14038e2c5
0038E0FE  48 8D 78 08                     lea rdi, [rax + 8]
0038E102  0F 10 44 24 58                  movups xmm0, xmmword ptr [rsp + 0x58]
0038E107  0F 11 07                        movups xmmword ptr [rdi], xmm0
0038E10A  0F 10 4C 24 68                  movups xmm1, xmmword ptr [rsp + 0x68]
0038E10F  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
0038E113  0F 10 44 24 78                  movups xmm0, xmmword ptr [rsp + 0x78]
0038E118  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
0038E11C  49 8D 4E 18                     lea rcx, [r14 + 0x18]
0038E120  48 8B D0                        mov rdx, rax
0038E123  E8 E8 06 00 00                  call 0x14038e810
0038E128  84 C0                           test al, al
0038E12A  0F 84 75 03 00 00               je 0x14038e4a5
0038E130  49 89 7D 78                     mov qword ptr [r13 + 0x78], rdi
0038E134  49 3B 1E                        cmp rbx, qword ptr [r14]
0038E137  73 03                           jae 0x14038e13c
0038E139  49 89 1E                        mov qword ptr [r14], rbx
0038E13C  48 8B BC 24 10 01 00 00         mov rdi, qword ptr [rsp + 0x110]
0038E144  C7 07 00 00 00 00               mov dword ptr [rdi], 0
0038E14A  41 0F B6 DC                     movzx ebx, r12b
0038E14E  88 5C 24 30                     mov byte ptr [rsp + 0x30], bl
0038E152  E9 67 03 00 00                  jmp 0x14038e4be
0038E157  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
0038E15C  49 8B CF                        mov rcx, r15
0038E15F  E8 C4 08 00 00                  call 0x14038ea28
0038E164  0F B6 4C 24 68                  movzx ecx, byte ptr [rsp + 0x68]
0038E169  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0038E16E  88 44 24 34                     mov byte ptr [rsp + 0x34], al
0038E172  84 C0                           test al, al
0038E174  0F 85 5F FF FF FF               jne 0x14038e0d9
0038E17A  38 84 24 00 01 00 00            cmp byte ptr [rsp + 0x100], al
0038E181  0F 84 CB 01 00 00               je 0x14038e352
0038E187  48 8B BC 24 10 01 00 00         mov rdi, qword ptr [rsp + 0x110]
0038E18F  C7 07 55 00 00 C0               mov dword ptr [rdi], 0xc0000055
0038E195  41 0F B6 DC                     movzx ebx, r12b
0038E199  EB B3                           jmp 0x14038e14e
0038E19B  48 8D 0D DE 3F A8 00            lea rcx, [rip + 0xa83fde]
0038E1A2  E8 19 05 00 00                  call 0x14038e6c0
0038E1A7  48 85 C0                        test rax, rax
0038E1AA  0F 84 15 01 00 00               je 0x14038e2c5
0038E1B0  48 8D 78 18                     lea rdi, [rax + 0x18]
0038E1B4  0F 10 44 24 58                  movups xmm0, xmmword ptr [rsp + 0x58]
0038E1B9  0F 11 07                        movups xmmword ptr [rdi], xmm0
0038E1BC  0F 10 4C 24 68                  movups xmm1, xmmword ptr [rsp + 0x68]
0038E1C1  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
0038E1C5  0F 10 44 24 78                  movups xmm0, xmmword ptr [rsp + 0x78]
0038E1CA  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
0038E1CE  49 8D 4E 18                     lea rcx, [r14 + 0x18]
0038E1D2  48 8B D0                        mov rdx, rax
0038E1D5  E8 22 0A 00 00                  call 0x14038ebfc
0038E1DA  E9 51 FF FF FF                  jmp 0x14038e130
0038E1DF  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0038E1E4  33 D2                           xor edx, edx
0038E1E6  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
0038E1EE  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
0038E1F3  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
0038E1F8  45 33 C0                        xor r8d, r8d
0038E1FB  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
0038E200  48 8D 4F FF                     lea rcx, [rdi - 1]
0038E204  48 03 CB                        add rcx, rbx
0038E207  48 85 C0                        test rax, rax
0038E20A  75 48                           jne 0x14038e254
0038E20C  49 0F 44 D0                     cmove rdx, r8
0038E210  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
0038E218  48 85 D2                        test rdx, rdx
0038E21B  0F 85 E7 00 00 00               jne 0x14038e308
0038E221  48 85 D2                        test rdx, rdx
0038E224  0F 85 DE 00 00 00               jne 0x14038e308
0038E22A  0F B6 44 24 30                  movzx eax, byte ptr [rsp + 0x30]
0038E22F  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0038E234  48 85 C9                        test rcx, rcx
0038E237  74 0E                           je 0x14038e247
0038E239  E8 A2 0F 00 00                  call 0x14038f1e0
0038E23E  49 89 47 10                     mov qword ptr [r15 + 0x10], rax
0038E242  0F B6 44 24 30                  movzx eax, byte ptr [rsp + 0x30]
0038E247  0F B6 8C 24 08 01 00 00         movzx ecx, byte ptr [rsp + 0x108]
0038E24F  E9 1A FF FF FF                  jmp 0x14038e16e
0038E254  48 8B D0                        mov rdx, rax
0038E257  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0038E25F  4C 8B 58 40                     mov r11, qword ptr [rax + 0x40]
0038E263  4C 3B DB                        cmp r11, rbx
0038E266  72 29                           jb 0x14038e291
0038E268  4C 8B 48 18                     mov r9, qword ptr [rax + 0x18]
0038E26C  4D 85 C9                        test r9, r9
0038E26F  74 35                           je 0x14038e2a6
0038E271  4C 3B C9                        cmp r9, rcx
0038E274  77 3E                           ja 0x14038e2b4
0038E276  48 83 F9 FF                     cmp rcx, -1
0038E27A  0F 84 73 01 00 00               je 0x14038e3f3
0038E280  4C 3B CB                        cmp r9, rbx
0038E283  0F 87 78 01 00 00               ja 0x14038e401
0038E289  48 85 C0                        test rax, rax
0038E28C  E9 7B FF FF FF                  jmp 0x14038e20c
0038E291  4C 3B D9                        cmp r11, rcx
0038E294  0F 84 9A 00 00 00               je 0x14038e334
0038E29A  49 89 01                        mov qword ptr [r9], rax
0038E29D  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
0038E2A1  E9 61 FF FF FF                  jmp 0x14038e207
0038E2A6  48 83 78 20 00                  cmp qword ptr [rax + 0x20], 0
0038E2AB  75 C4                           jne 0x14038e271
0038E2AD  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0038E2B2  EB DD                           jmp 0x14038e291
0038E2B4  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0038E2B9  49 89 01                        mov qword ptr [r9], rax
0038E2BC  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0038E2C0  E9 42 FF FF FF                  jmp 0x14038e207
0038E2C5  48 85 F6                        test rsi, rsi
0038E2C8  0F 84 47 FD FF FF               je 0x14038e015
0038E2CE  0F B6 54 24 31                  movzx edx, byte ptr [rsp + 0x31]
0038E2D3  49 8B CF                        mov rcx, r15
0038E2D6  E8 C5 48 00 00                  call 0x140392ba0
0038E2DB  C6 44 24 32 00                  mov byte ptr [rsp + 0x32], 0
0038E2E0  B9 9A 00 00 C0                  mov ecx, 0xc000009a
0038E2E5  E8 66 87 F6 FF                  call 0x1402f6a50
0038E2EA  48 85 FF                        test rdi, rdi
0038E2ED  0F 84 A0 FD FF FF               je 0x14038e093
0038E2F3  48 8B BC 24 10 01 00 00         mov rdi, qword ptr [rsp + 0x110]
0038E2FB  C7 07 A1 01 00 C0               mov dword ptr [rdi], 0xc00001a1
0038E301  B3 01                           mov bl, 1
0038E303  E9 46 FE FF FF                  jmp 0x14038e14e
0038E308  48 39 4A 18                     cmp qword ptr [rdx + 0x18], rcx
0038E30C  0F 87 18 FF FF FF               ja 0x14038e22a
0038E312  4C 39 6A 30                     cmp qword ptr [rdx + 0x30], r13
0038E316  0F 84 F2 00 00 00               je 0x14038e40e
0038E31C  48 85 FF                        test rdi, rdi
0038E31F  0F 84 0C 01 00 00               je 0x14038e431
0038E325  32 C0                           xor al, al
0038E327  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0038E32B  88 44 24 33                     mov byte ptr [rsp + 0x33], al
0038E32F  E9 FB FE FF FF                  jmp 0x14038e22f
0038E334  48 39 58 18                     cmp qword ptr [rax + 0x18], rbx
0038E338  0F 85 5C FF FF FF               jne 0x14038e29a
0038E33E  4C 8B C0                        mov r8, rax
0038E341  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0038E346  49 89 01                        mov qword ptr [r9], rax
0038E349  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0038E34D  E9 B5 FE FF FF                  jmp 0x14038e207
0038E352  48 85 F6                        test rsi, rsi
0038E355  0F 84 BA FC FF FF               je 0x14038e015
0038E35B  48 8D 0D 9E 3C A8 00            lea rcx, [rip + 0xa83c9e]
0038E362  E8 59 03 00 00                  call 0x14038e6c0
0038E367  48 8B C8                        mov rcx, rax
0038E36A  48 85 C0                        test rax, rax
0038E36D  0F 84 E0 00 00 00               je 0x14038e453
0038E373  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0038E377  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
0038E37F  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
0038E383  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0038E387  48 89 41 08                     mov qword ptr [rcx + 8], rax
0038E38B  48 8B 86 B8 00 00 00            mov rax, qword ptr [rsi + 0xb8]
0038E392  44 08 60 03                     or byte ptr [rax + 3], r12b
0038E396  48 C7 01 00 00 00 00            mov qword ptr [rcx], 0
0038E39D  49 83 7F 18 00                  cmp qword ptr [r15 + 0x18], 0
0038E3A2  75 46                           jne 0x14038e3ea
0038E3A4  49 89 4F 18                     mov qword ptr [r15 + 0x18], rcx
0038E3A8  49 89 4F 20                     mov qword ptr [r15 + 0x20], rcx
0038E3AC  4C 89 76 38                     mov qword ptr [rsi + 0x38], r14
0038E3B0  48 8D 05 B9 67 14 00            lea rax, [rip + 0x1467b9]
0038E3B7  48 87 46 68                     xchg qword ptr [rsi + 0x68], rax
0038E3BB  80 7E 44 00                     cmp byte ptr [rsi + 0x44], 0
0038E3BF  0F 85 AA 00 00 00               jne 0x14038e46f
0038E3C5  44 0F B6 64 24 32               movzx r12d, byte ptr [rsp + 0x32]
0038E3CB  48 8B BC 24 10 01 00 00         mov rdi, qword ptr [rsp + 0x110]
0038E3D3  C7 07 03 01 00 00               mov dword ptr [rdi], 0x103
0038E3D9  B3 01                           mov bl, 1
0038E3DB  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
0038E3E0  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
0038E3E5  E9 64 FD FF FF                  jmp 0x14038e14e
0038E3EA  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
0038E3EE  48 89 08                        mov qword ptr [rax], rcx
0038E3F1  EB B5                           jmp 0x14038e3a8
0038E3F3  48 85 DB                        test rbx, rbx
0038E3F6  0F 84 B8 FE FF FF               je 0x14038e2b4
0038E3FC  E9 7F FE FF FF                  jmp 0x14038e280
0038E401  4C 8B C0                        mov r8, rax
0038E404  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0038E409  E9 A6 FE FF FF                  jmp 0x14038e2b4
0038E40E  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0038E416  48 39 42 38                     cmp qword ptr [rdx + 0x38], rax
0038E41A  0F 85 FC FE FF FF               jne 0x14038e31c
0038E420  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
0038E427  39 42 2C                        cmp dword ptr [rdx + 0x2c], eax
0038E42A  74 10                           je 0x14038e43c
0038E42C  E9 EB FE FF FF                  jmp 0x14038e31c
0038E431  48 83 7A 20 00                  cmp qword ptr [rdx + 0x20], 0
0038E436  0F 85 E9 FE FF FF               jne 0x14038e325
0038E43C  48 8B CA                        mov rcx, rdx
0038E43F  E8 FC FA FF FF                  call 0x14038df40
0038E444  48 8B D0                        mov rdx, rax
0038E447  48 8D 4F FF                     lea rcx, [rdi - 1]
0038E44B  48 03 CB                        add rcx, rbx
0038E44E  E9 CE FD FF FF                  jmp 0x14038e221
0038E453  0F B6 54 24 31                  movzx edx, byte ptr [rsp + 0x31]
0038E458  49 8B CF                        mov rcx, r15
0038E45B  E8 40 47 00 00                  call 0x140392ba0
0038E460  C6 44 24 32 00                  mov byte ptr [rsp + 0x32], 0
0038E465  B9 9A 00 00 C0                  mov ecx, 0xc000009a
0038E46A  E8 E1 85 F6 FF                  call 0x1402f6a50
0038E46F  33 C0                           xor eax, eax
0038E471  48 87 46 68                     xchg qword ptr [rsi + 0x68], rax
0038E475  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0038E47D  48 85 C0                        test rax, rax
0038E480  0F 84 3F FF FF FF               je 0x14038e3c5
0038E486  0F B6 44 24 31                  movzx eax, byte ptr [rsp + 0x31]
0038E48B  88 46 45                        mov byte ptr [rsi + 0x45], al
0038E48E  48 8B D6                        mov rdx, rsi
0038E491  33 C9                           xor ecx, ecx
0038E493  E8 D8 66 14 00                  call 0x1404d4b70
0038E498  45 32 E4                        xor r12b, r12b
0038E49B  44 88 64 24 32                  mov byte ptr [rsp + 0x32], r12b
0038E4A0  E9 26 FF FF FF                  jmp 0x14038e3cb
0038E4A5  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
0038E4AD  48 8D 0D 4C 3D A8 00            lea rcx, [rip + 0xa83d4c]
0038E4B4  E8 17 F5 FF FF                  call 0x14038d9d0
0038E4B9  E9 07 FE FF FF                  jmp 0x14038e2c5
0038E4BE  45 84 E4                        test r12b, r12b
0038E4C1  74 39                           je 0x14038e4fc
0038E4C3  F6 05 3C 86 C3 00 01            test byte ptr [rip + 0xc3863c], 1
0038E4CA  75 56                           jne 0x14038e522
0038E4CC  F0 49 83 27 00                  lock and qword ptr [r15], 0
0038E4D1  0F B6 5C 24 31                  movzx ebx, byte ptr [rsp + 0x31]
0038E4D6  83 3D 43 88 C3 00 00            cmp dword ptr [rip + 0xc38843], 0
0038E4DD  74 0C                           je 0x14038e4eb
0038E4DF  44 0F 20 C1                     mov rcx, cr8
0038E4E3  0F B6 D3                        movzx edx, bl
0038E4E6  E8 AD 71 16 00                  call 0x1404f5698
0038E4EB  0F B6 C3                        movzx eax, bl
0038E4EE  44 0F 22 C0                     mov cr8, rax
0038E4F2  0F B6 5C 24 30                  movzx ebx, byte ptr [rsp + 0x30]
0038E4F7  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
0038E4FC  48 85 F6                        test rsi, rsi
0038E4FF  75 3F                           jne 0x14038e540
0038E501  0F B6 C3                        movzx eax, bl
0038E504  4C 8D 9C 24 A0 00 00 00         lea r11, [rsp + 0xa0]
0038E50C  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0038E510  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
0038E514  49 8B E3                        mov rsp, r11
0038E517  41 5F                           pop r15
0038E519  41 5E                           pop r14
0038E51B  41 5D                           pop r13
0038E51D  41 5C                           pop r12
0038E51F  5F                              pop rdi
0038E520  C3                              ret
0038E521  CC                              int3
0038E522  8B 05 30 F9 B7 00               mov eax, dword ptr [rip + 0xb7f930]
0038E528  85 C0                           test eax, eax
0038E52A  75 74                           jne 0x14038e5a0
0038E52C  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0038E534  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0038E539  E8 B2 49 00 00                  call 0x140392ef0
0038E53E  EB 91                           jmp 0x14038e4d1
0038E540  81 3F 03 01 00 00               cmp dword ptr [rdi], 0x103
0038E546  74 B9                           je 0x14038e501
0038E548  BA 44 66 6C 74                  mov edx, 0x746c6644
0038E54D  49 8B CD                        mov rcx, r13
0038E550  E8 BB 21 E8 FF                  call 0x140210710
0038E555  44 8B 3F                        mov r15d, dword ptr [rdi]
0038E558  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0038E55C  48 85 C0                        test rax, rax
0038E55F  75 49                           jne 0x14038e5aa
0038E561  44 89 7E 30                     mov dword ptr [rsi + 0x30], r15d
0038E565  B2 01                           mov dl, 1
0038E567  48 8B CE                        mov rcx, rsi
0038E56A  E8 51 D0 F0 FF                  call 0x14029b5c0
0038E56F  45 85 FF                        test r15d, r15d
0038E572  78 15                           js 0x14038e589
0038E574  BA 44 66 6C 74                  mov edx, 0x746c6644
0038E579  49 8B CD                        mov rcx, r13
0038E57C  E8 5F 93 F6 FF                  call 0x1402f78e0
0038E581  44 89 3F                        mov dword ptr [rdi], r15d
0038E584  E9 78 FF FF FF                  jmp 0x14038e501
0038E589  83 3F 00                        cmp dword ptr [rdi], 0
0038E58C  7C E6                           jl 0x14038e574
0038E58E  41 B0 01                        mov r8b, 1
0038E591  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
0038E596  49 8B CE                        mov rcx, r14
0038E599  E8 A6 4C 15 00                  call 0x1404e3244
0038E59E  EB D4                           jmp 0x14038e574
0038E5A0  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
0038E5A5  E9 22 FF FF FF                  jmp 0x14038e4cc
0038E5AA  4D 85 ED                        test r13, r13
0038E5AD  0F 84 DD 70 35 00               je 0x1406e5690
0038E5B3  49 C7 45 78 00 00 00 00         mov qword ptr [r13 + 0x78], 0
0038E5BB  E9 D0 70 35 00                  jmp 0x1406e5690
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlPrivateLock(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned __int8 a7, unsigned __int8 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int8 v_stack_m94;
    unsigned __int8 v_stack_m95;
    unsigned __int8 v_stack_m96;
    unsigned __int8 v_stack_m97;
    unsigned __int8 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p20 = v_rsi;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (160);
    v_r12 = 0;
    v_stack_m96 = 0;
    v_stack_m80 = 0;
    v_r15 = 0;
    v_stack_m88 = 0;
    v_stack_m97 = 255;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    a2 = (a10 == 0) ? 1 : 0;
    v_stack_m80 = *(unsigned __int64 *)(a1 + 24);
    if (*(unsigned __int64 *)(a1 + 24) != 0) goto loc_0038E039;
    result = FsRtlPrivateInitializeFileLock(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0038E024;
loc_0038E015:
    v_rbx = 0;
    goto loc_0038E14E;
loc_0038E024:
    *(unsigned __int8 *)(v_rbx + 16) = 1;
    v_stack_m80 = *(unsigned __int64 *)(v_rbx + 24);
loc_0038E039:
    v_stack_m70 = *(unsigned __int64 *)(v_stack_p18);
    v_stack_m68 = *(unsigned __int64 *)(a9);
    a1 = (*(unsigned __int64 *)(a9) - 1) + (*(unsigned __int64 *)(v_stack_p18));
    v_stack_m48 = a1;
    v_stack_m5C = (unsigned int)((unsigned int)(a6));
    v_stack_m58 = a2;
    v_stack_m50 = a5;
    v_stack_m60 = a8;
    v_stack_m88 = *(unsigned __int64 *)(v_rbx + 24) + 24;
    if (a1 < (*(unsigned __int64 *)(v_stack_p18))) goto loc_0038E2EA;
loc_0038E093:
    v_stack_m96 = 1;
    result = KeAcquireSpinLockRaiseToDpc(*(unsigned __int64 *)(v_rbx + 24) + 24, a2, a3, a4);
    v_stack_m97 = (unsigned __int8)(result);
    if (a8 != 0) goto loc_0038E157;
    v_stack_m90 = 0;
    v_stack_m98 = 1;
    v_stack_m95 = 1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 24) + 24 + 16) != 0) goto loc_0038E1DF;
loc_0038E0D9:
    if (a8 != 0) goto loc_0038E19B;
    result = ExAllocateFromNPagedLookasideList(v_rip + 11026712, a2, a3, a4);
    v_stack_m38 = result;
    if (result == 0) goto loc_0038E2C5;
    *(unsigned __int64 *)(result + 8) = v_xmm0;
    *(unsigned __int64 *)(result + 8 + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 8 + 32) = v_xmm0;
    result = FsRtlPrivateInsertSharedLock(*(unsigned __int64 *)(v_rbx + 24) + 24, result, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0038E4A5;
loc_0038E130:
    *(unsigned __int64 *)(a2 + 120) = result + 8;
    if ((*(unsigned __int64 *)(v_stack_p18)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 24)))) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 24)) = *(unsigned __int64 *)(v_stack_p18);
    }
    *(unsigned int *)(a9) = 0;
loc_0038E14E:
    v_stack_m98 = 1;
    goto loc_0038E4BE;
loc_0038E157:
    result = FsRtlPrivateCheckForExclusiveLockAccess(*(unsigned __int64 *)(v_rbx + 24) + 24, v_stack_m70, a3, a4);
loc_0038E16E:
    v_stack_m94 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) goto loc_0038E0D9;
    if (a7 == ((unsigned __int8)(result))) goto loc_0038E352;
    *(unsigned int *)(a9) = 0xC0000055ULL;
    goto loc_0038E14E;
loc_0038E19B:
    result = ExAllocateFromNPagedLookasideList(v_rip + 11026398, v_stack_m70, a3, a4);
    if (result == 0) goto loc_0038E2C5;
    *(unsigned __int64 *)(result + 24) = v_xmm0;
    *(unsigned __int64 *)(result + 24 + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 24 + 32) = v_xmm0;
    result = FsRtlPrivateInsertExclusiveLock(*(unsigned __int64 *)(v_rbx + 24) + 24, result, a3, a4);
    goto loc_0038E130;
loc_0038E1DF:
    a2 = 0;
    v_stack_m40 = 0;
    v_stack_m78 = 0;
    v_stack_m90 = 0;
    a3 = 0;
    v_stack_m78 = 0;
    a1 = (result + 24 - 1) + (1);
loc_0038E207:
    if (result != 0) goto loc_0038E254;
loc_0038E20C:
    if (result == 0) { a2 = 0; }
    v_stack_m40 = a2;
    if (a2 != 0) goto loc_0038E308;
loc_0038E221:
    if (a2 != 0) goto loc_0038E308;
loc_0038E22A:
loc_0038E22F:
    result = v_stack_m98;
    if (v_stack_m90 != 0) {
        result = RtlSplay(v_stack_m90, a2, a3, v_stack_m90);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 24) + 24 + 16) = result;
        result = v_stack_m98;
    }
    goto loc_0038E16E;
loc_0038E254:
    v_stack_m40 = result;
    if ((*(unsigned __int64 *)(result + 64)) < 1) goto loc_0038E291;
    if (*(unsigned __int64 *)(result + 24) == 0) goto loc_0038E2A6;
loc_0038E271:
    if ((*(unsigned __int64 *)(result + 24)) > a8) goto loc_0038E2B4;
    if (a8 == -1) goto loc_0038E3F3;
loc_0038E280:
    if ((*(unsigned __int64 *)(result + 24)) > 1) goto loc_0038E401;
    goto loc_0038E20C;
loc_0038E291:
    if ((*(unsigned __int64 *)(result + 64)) == a8) goto loc_0038E334;
loc_0038E29A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) = result;
    goto loc_0038E207;
loc_0038E2A6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 32)) != 0) goto loc_0038E271;
    goto loc_0038E291;
loc_0038E2B4:
    *(unsigned __int64 *)(v_stack_m90) = *(unsigned __int64 *)(result + 16);
    goto loc_0038E207;
loc_0038E2C5:
    if (a10 == 0) goto loc_0038E015;
    result = KeReleaseSpinLock(*(unsigned __int64 *)(v_rbx + 24) + 24, v_stack_m97, a3, v_stack_m90);
    v_stack_m96 = 0;
    result = RtlRaiseStatus((unsigned int)(0xC000009AULL), v_stack_m97, a3, v_stack_m90);
loc_0038E2EA:
    if (result + 24 == 0) goto loc_0038E093;
    *(unsigned int *)(a9) = 0xC00001A1ULL;
    goto loc_0038E14E;
loc_0038E308:
    if ((*(unsigned __int64 *)(v_stack_m97 + 24)) > ((unsigned int)(0xC000009AULL))) goto loc_0038E22A;
    if ((*(unsigned __int64 *)(v_stack_m97 + 48)) == a2) goto loc_0038E40E;
loc_0038E31C:
    if (a9 == 0) goto loc_0038E431;
loc_0038E325:
    result = 0;
    v_stack_m98 = 0;
    v_stack_m95 = 0;
    goto loc_0038E22F;
loc_0038E334:
    if ((*(unsigned __int64 *)(result + 24)) != 1) goto loc_0038E29A;
    v_stack_m78 = 0;
    *(unsigned __int64 *)(v_stack_m90) = 0;
    goto loc_0038E207;
loc_0038E352:
    if (a10 == 0) goto loc_0038E015;
    result = ExAllocateFromNPagedLookasideList(v_rip + 11025566, v_stack_m97, 0, v_stack_m90);
    if (result == 0) goto loc_0038E453;
    *(unsigned __int64 *)(result + 24) = a10;
    *(unsigned __int64 *)(result + 16) = a11;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 24) + 8);
    *(unsigned __int64 *)(result) = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 24) + 24 + 24)) != 0) goto loc_0038E3EA;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 24) + 24 + 24) = result;
loc_0038E3A8:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 24) + 24 + 32) = result;
    *(unsigned __int64 *)(a10 + 56) = *(unsigned __int64 *)(v_rbx + 24);
    if ((*(unsigned __int8 *)(a10 + 68)) != 0) goto loc_0038E46F;
loc_0038E3C5:
loc_0038E3CB:
    *(unsigned int *)(a9) = 259;
    goto loc_0038E14E;
loc_0038E3EA:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88 + 32)) = result;
    goto loc_0038E3A8;
loc_0038E3F3:
    if (1 == 0) goto loc_0038E2B4;
    goto loc_0038E280;
loc_0038E401:
    v_stack_m78 = *(unsigned __int64 *)(v_stack_m88 + 32);
    goto loc_0038E2B4;
loc_0038E40E:
    if ((*(unsigned __int64 *)(v_stack_m97 + 56)) != a5) goto loc_0038E31C;
    if ((*(unsigned int *)(v_stack_m97 + 44)) == ((unsigned int)((unsigned int)(a6)))) goto loc_0038E43C;
    goto loc_0038E31C;
loc_0038E431:
    if ((*(unsigned __int64 *)(v_stack_m97 + 32)) != 0) goto loc_0038E325;
loc_0038E43C:
    result = RtlRealSuccessor(v_stack_m97, v_stack_m97, *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m90);
    a1 = (a9 - 1) + (1);
    goto loc_0038E221;
loc_0038E453:
    result = KeReleaseSpinLock(v_stack_m88, v_stack_m97, *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m90);
    v_stack_m96 = 0;
    result = RtlRaiseStatus((unsigned int)(0xC000009AULL), v_stack_m97, *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m90);
loc_0038E46F:
    result = 0;
    v_stack_m38 = 0;
    if (0 == 0) goto loc_0038E3C5;
    *(unsigned __int8 *)(a10 + 69) = (unsigned __int8)(v_stack_m97);
    a1 = 0;
    result = FsRtlPrivateCancelFileLockIrp(a1, a10, *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m90);
    v_r12 = 0;
    v_stack_m96 = 0;
    goto loc_0038E3CB;
loc_0038E4A5:
    result = ExFreeToNPagedLookasideList(v_rip + 11025740, v_stack_m38, *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m90);
    goto loc_0038E2C5;
loc_0038E4BE:
    if (0 == 0) goto loc_0038E4FC;
    if (((*(unsigned __int8 *)(v_rip + 12813884)) & (1)) != 0) goto loc_0038E522;
loc_0038E4CC:
loc_0038E4D1:
    if ((*(unsigned int *)(v_rip + 12814403)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(v_stack_m97);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m90);
    }
loc_0038E4FC:
    if (a10 != 0) goto loc_0038E540;
loc_0038E501:
    return (unsigned __int8)(v_stack_m98);
loc_0038E522:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12056880))) != 0) goto loc_0038E5A0;
    result = KiReleaseSpinLockInstrumented(v_stack_m60, v_stack_p28, *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m90);
    goto loc_0038E4D1;
loc_0038E540:
    if ((*(unsigned int *)(a9)) == 259) goto loc_0038E501;
    result = ObfReferenceObjectWithTag(a2, (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m90);
    if (*(unsigned __int64 *)(v_stack_m80 + 8) != 0) goto loc_0038E5AA;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(a9)));
    result = IofCompleteRequest(*(unsigned __int64 *)(v_stack_m28 + 72), 1, *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m90);
    if (sign_flag) goto loc_0038E589;
loc_0038E574:
    result = ObfDereferenceObjectWithTag(a2, (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(v_stack_m88 + 32), v_stack_m90);
    *(unsigned int *)(a9) = (unsigned int)((unsigned int)(*(unsigned int *)(a9)));
    goto loc_0038E501;
loc_0038E589:
    if ((*(unsigned int *)(a9)) < 0) goto loc_0038E574;
    result = FsRtlPrivateRemoveLock(v_stack_m80, v_stack_m48, 1, v_stack_m90);
    goto loc_0038E574;
loc_0038E5A0:
    goto loc_0038E4CC;
loc_0038E5AA:
    *(unsigned __int64 *)(a2 + 120) = 0;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlPrivateLock(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4, int64_t Arg5, uint32_t Arg6, uint8_t Arg7, uint8_t Arg8, void *Arg9, int64_t Arg10, int64_t Arg11)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint8_t v_stack_m94;
    uint8_t v_stack_m95;
    uint8_t v_stack_m96;
    uint8_t v_stack_m97;
    uint8_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p20 = local_rsi;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (160);
    local_r12 = 0;
    v_stack_m96 = 0;
    v_stack_m80 = 0;
    local_r15 = 0;
    v_stack_m88 = 0;
    v_stack_m97 = 255;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    Arg2 = (Arg10 == 0) ? 1 : 0;
    v_stack_m80 = *(uint64_t *)(arg1 + 0x18);
    if (*(uint64_t *)(arg1 + 0x18) != 0) goto loc_0038E039;
    result = FsRtlPrivateInitializeFileLock(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0038E024;
loc_0038E015:
    local_rbx = 0;
    goto loc_0038E14E;
loc_0038E024:
    *(uint8_t *)(local_rbx + 0x10) = 1;
    v_stack_m80 = *(uint64_t *)(local_rbx + 0x18);
loc_0038E039:
    v_stack_m70 = *(uint64_t *)(v_stack_p18);
    v_stack_m68 = *(uint64_t *)(arg9);
    Arg1 = (*(uint64_t *)(arg9) - 1) + (*(uint64_t *)(v_stack_p18));
    v_stack_m48 = Arg1;
    v_stack_m5C = (uint32_t)((uint32_t)(Arg6));
    v_stack_m58 = Arg2;
    v_stack_m50 = Arg5;
    v_stack_m60 = Arg8;
    v_stack_m88 = *(uint64_t *)(local_rbx + 0x18) + 24;
    if (Arg1 < (*(uint64_t *)(v_stack_p18))) goto loc_0038E2EA;
loc_0038E093:
    v_stack_m96 = 1;
    result = KeAcquireSpinLockRaiseToDpc(*(uint64_t *)(local_rbx + 0x18) + 24, Arg2, Arg3, Arg4);
    v_stack_m97 = (uint8_t)(result);
    if (Arg8 != 0) goto loc_0038E157;
    v_stack_m90 = 0;
    v_stack_m98 = 1;
    v_stack_m95 = 1;
    if (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x18) + 0x18 + 0x10) != 0) goto loc_0038E1DF;
loc_0038E0D9:
    if (Arg8 != 0) goto loc_0038E19B;
    result = ExAllocateFromNPagedLookasideList(v_rip + 11026712, Arg2, Arg3, Arg4);
    v_stack_m38 = result;
    if (result == 0) goto loc_0038E2C5;
    *(uint64_t *)(result + 0x8) = v_xmm0;
    *(uint64_t *)(result + 0x8 + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x8 + 0x20) = v_xmm0;
    result = FsRtlPrivateInsertSharedLock(*(uint64_t *)(local_rbx + 0x18) + 24, result, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0038E4A5;
loc_0038E130:
    *(uint64_t *)(arg2 + 0x78) = result + 8;
    if ((*(uint64_t *)(v_stack_p18)) < (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x18)))) {
        *(uint64_t *)(*(uint64_t *)(local_rbx + 0x18)) = *(uint64_t *)(v_stack_p18);
    }
    *(uint32_t *)(arg9) = 0;
loc_0038E14E:
    v_stack_m98 = 1;
    goto loc_0038E4BE;
loc_0038E157:
    result = FsRtlPrivateCheckForExclusiveLockAccess(*(uint64_t *)(local_rbx + 0x18) + 24, v_stack_m70, Arg3, Arg4);
loc_0038E16E:
    v_stack_m94 = (uint8_t)(result);
    if ((uint8_t)(result) != 0) goto loc_0038E0D9;
    if (Arg7 == ((uint8_t)(result))) goto loc_0038E352;
    *(uint32_t *)(arg9) = 0xC0000055ULL;
    goto loc_0038E14E;
loc_0038E19B:
    result = ExAllocateFromNPagedLookasideList(v_rip + 11026398, v_stack_m70, Arg3, Arg4);
    if (result == 0) goto loc_0038E2C5;
    *(uint64_t *)(result + 0x18) = v_xmm0;
    *(uint64_t *)(result + 0x18 + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x18 + 0x20) = v_xmm0;
    result = FsRtlPrivateInsertExclusiveLock(*(uint64_t *)(local_rbx + 0x18) + 24, result, Arg3, Arg4);
    goto loc_0038E130;
loc_0038E1DF:
    Arg2 = 0;
    v_stack_m40 = 0;
    v_stack_m78 = 0;
    v_stack_m90 = 0;
    Arg3 = 0;
    v_stack_m78 = 0;
    Arg1 = (result + 24 - 1) + (1);
loc_0038E207:
    if (result != 0) goto loc_0038E254;
loc_0038E20C:
    if (result == 0) { Arg2 = 0; }
    v_stack_m40 = Arg2;
    if (Arg2 != NULL) goto loc_0038E308;
loc_0038E221:
    if (Arg2 != NULL) goto loc_0038E308;
loc_0038E22A:
loc_0038E22F:
    result = v_stack_m98;
    if (v_stack_m90 != 0) {
        result = RtlSplay(v_stack_m90, Arg2, Arg3, v_stack_m90);
        *(uint64_t *)(*(uint64_t *)(local_rbx + 0x18) + 0x18 + 0x10) = result;
        result = v_stack_m98;
    }
    goto loc_0038E16E;
loc_0038E254:
    v_stack_m40 = result;
    if ((*(uint64_t *)(result + 0x40)) < 1) goto loc_0038E291;
    if (*(uint64_t *)(result + 0x18) == 0) goto loc_0038E2A6;
loc_0038E271:
    if ((*(uint64_t *)(result + 0x18)) > Arg8) goto loc_0038E2B4;
    if (Arg8 == -1) goto loc_0038E3F3;
loc_0038E280:
    if ((*(uint64_t *)(result + 0x18)) > 1) goto loc_0038E401;
    goto loc_0038E20C;
loc_0038E291:
    if ((*(uint64_t *)(result + 0x40)) == Arg8) goto loc_0038E334;
loc_0038E29A:
    *(uint64_t *)(*(uint64_t *)(result + 0x18)) = result;
    goto loc_0038E207;
loc_0038E2A6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x20)) != 0) goto loc_0038E271;
    goto loc_0038E291;
loc_0038E2B4:
    *(uint64_t *)(v_stack_m90) = *(uint64_t *)(result + 0x10);
    goto loc_0038E207;
loc_0038E2C5:
    if (Arg10 == 0) goto loc_0038E015;
    result = KeReleaseSpinLock(*(uint64_t *)(local_rbx + 0x18) + 24, v_stack_m97, Arg3, v_stack_m90);
    v_stack_m96 = 0;
    result = RtlRaiseStatus((uint32_t)(0xC000009AULL), v_stack_m97, Arg3, v_stack_m90);
loc_0038E2EA:
    if (result + 24 == 0) goto loc_0038E093;
    *(uint32_t *)(arg9) = 0xC00001A1ULL;
    goto loc_0038E14E;
loc_0038E308:
    if ((*(uint64_t *)(v_stack_m97 + 0x18)) > ((uint32_t)(0xC000009AULL))) goto loc_0038E22A;
    if ((*(uint64_t *)(v_stack_m97 + 0x30)) == Arg2) goto loc_0038E40E;
loc_0038E31C:
    if (Arg9 == NULL) goto loc_0038E431;
loc_0038E325:
    result = 0;
    v_stack_m98 = 0;
    v_stack_m95 = 0;
    goto loc_0038E22F;
loc_0038E334:
    if ((*(uint64_t *)(result + 0x18)) != 1) goto loc_0038E29A;
    v_stack_m78 = 0;
    *(uint64_t *)(v_stack_m90) = 0;
    goto loc_0038E207;
loc_0038E352:
    if (Arg10 == 0) goto loc_0038E015;
    result = ExAllocateFromNPagedLookasideList(v_rip + 11025566, v_stack_m97, 0, v_stack_m90);
    if (result == 0) goto loc_0038E453;
    *(uint64_t *)(result + 0x18) = Arg10;
    *(uint64_t *)(result + 0x10) = Arg11;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(*(uint64_t *)(local_rbx + 0x18) + 0x8);
    *(uint64_t *)(result) = 0;
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x18) + 0x18 + 0x18)) != 0) goto loc_0038E3EA;
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x18) + 0x18 + 0x18) = result;
loc_0038E3A8:
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x18) + 0x18 + 0x20) = result;
    *(uint64_t *)(Arg10 + 0x38) = *(uint64_t *)(local_rbx + 0x18);
    if ((*(uint8_t *)(Arg10 + 0x44)) != 0) goto loc_0038E46F;
loc_0038E3C5:
loc_0038E3CB:
    *(uint32_t *)(arg9) = 259;
    goto loc_0038E14E;
loc_0038E3EA:
    *(uint64_t *)(*(uint64_t *)(v_stack_m88 + 0x20)) = result;
    goto loc_0038E3A8;
loc_0038E3F3:
    if (1 == 0) goto loc_0038E2B4;
    goto loc_0038E280;
loc_0038E401:
    v_stack_m78 = *(uint64_t *)(v_stack_m88 + 0x20);
    goto loc_0038E2B4;
loc_0038E40E:
    if ((*(uint64_t *)(v_stack_m97 + 0x38)) != Arg5) goto loc_0038E31C;
    if ((*(uint32_t *)(v_stack_m97 + 0x2C)) == ((uint32_t)((uint32_t)(Arg6)))) goto loc_0038E43C;
    goto loc_0038E31C;
loc_0038E431:
    if ((*(uint64_t *)(v_stack_m97 + 0x20)) != 0) goto loc_0038E325;
loc_0038E43C:
    result = RtlRealSuccessor(v_stack_m97, v_stack_m97, *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m90);
    Arg1 = (Arg9 - 1) + (1);
    goto loc_0038E221;
loc_0038E453:
    result = KeReleaseSpinLock(v_stack_m88, v_stack_m97, *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m90);
    v_stack_m96 = 0;
    result = RtlRaiseStatus((uint32_t)(0xC000009AULL), v_stack_m97, *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m90);
loc_0038E46F:
    result = 0;
    v_stack_m38 = 0;
    if (0 == 0) goto loc_0038E3C5;
    *(uint8_t *)(Arg10 + 0x45) = (uint8_t)(v_stack_m97);
    Arg1 = 0;
    result = FsRtlPrivateCancelFileLockIrp(Arg1, Arg10, *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m90);
    local_r12 = 0;
    v_stack_m96 = 0;
    goto loc_0038E3CB;
loc_0038E4A5:
    result = ExFreeToNPagedLookasideList(v_rip + 11025740, v_stack_m38, *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m90);
    goto loc_0038E2C5;
loc_0038E4BE:
    if (0 == 0) goto loc_0038E4FC;
    if (((*(uint8_t *)(v_rip + 0xC3863C)) & (1)) != 0) goto loc_0038E522;
loc_0038E4CC:
loc_0038E4D1:
    if ((*(uint32_t *)(v_rip + 0xC38843)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(v_stack_m97);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m90);
    }
loc_0038E4FC:
    if (Arg10 != 0) goto loc_0038E540;
loc_0038E501:
    return (uint8_t)(v_stack_m98);
loc_0038E522:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB7F930))) != 0) goto loc_0038E5A0;
    result = KiReleaseSpinLockInstrumented(v_stack_m60, v_stack_p28, *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m90);
    goto loc_0038E4D1;
loc_0038E540:
    if ((*(uint32_t *)(arg9)) == 259) goto loc_0038E501;
    result = ObfReferenceObjectWithTag(Arg2, (uint32_t)(0x746C6644ULL), *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m90);
    if (*(uint64_t *)(v_stack_m80 + 0x8) != 0) goto loc_0038E5AA;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(arg9)));
    result = IofCompleteRequest(*(uint64_t *)(v_stack_m28 + 0x48), 1, *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m90);
    if (sign_flag) goto loc_0038E589;
loc_0038E574:
    result = ObfDereferenceObjectWithTag(Arg2, (uint32_t)(0x746C6644ULL), *(uint64_t *)(v_stack_m88 + 0x20), v_stack_m90);
    *(uint32_t *)(arg9) = (uint32_t)((uint32_t)(*(uint32_t *)(arg9)));
    goto loc_0038E501;
loc_0038E589:
    if ((*(uint32_t *)(arg9)) < 0) goto loc_0038E574;
    result = FsRtlPrivateRemoveLock(v_stack_m80, v_stack_m48, 1, v_stack_m90);
    goto loc_0038E574;
loc_0038E5A0:
    goto loc_0038E4CC;
loc_0038E5AA:
    *(uint64_t *)(arg2 + 0x78) = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `8` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x78` | `64` | `W` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg9` | `+ 0x0` | `32` | `R` |
| `Arg9` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0038DF90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
