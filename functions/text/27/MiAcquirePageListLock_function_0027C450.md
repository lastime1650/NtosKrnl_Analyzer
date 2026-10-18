# MiAcquirePageListLock

- RVA: `0x0027C450`–`0x0027CBDF` (길이 `1,935` bytes)
- VA: `0x000000014027C450`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006614C`
- 디코드: `445`개 명령, `1,935/1,935` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x0027C4FB` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x0027C8D1` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0027C8E1` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x0027C908` → [ExpWaitForSpinLockExclusiveAndAcquire](../32/ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) (function, `0x003239A0`)
- `0x0027C9B7` → [ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented](../32/ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_00323A70.md) (function, `0x00323A70`)
- `0x0027C9CC` → [MiSearchChannelTable](../33/MiSearchChannelTable_function_0033BE24.md) (function, `0x0033BE24`)
- `0x0027CA9E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0027CB29` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0027CB5A` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0027CB6E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0027CB97` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)

### Direct callers
- [sub_00287607](../28/Unknown_function_00287607.md) at `0x00287784`
- [sub_00287A62](../28/Unknown_function_00287A62.md) at `0x00287B7A`
- [sub_00287A62](../28/Unknown_function_00287A62.md) at `0x00287D44`
- [sub_00287A62](../28/Unknown_function_00287A62.md) at `0x00287D99`
- [MiReplaceTransitionPage](../2B/MiReplaceTransitionPage_function_002B1120.md) at `0x002B13A0`
- [MiReplaceTransitionPage](../2B/MiReplaceTransitionPage_function_002B1120.md) at `0x002B180A`
- [sub_00338E63](../33/Unknown_function_00338E63.md) at `0x00338F53`
- [MiUnlinkPageFromBadList](../3B/MiUnlinkPageFromBadList_function_003BD620.md) at `0x003BD6E4`
- [MiDecayPfnFullyInitialized](../44/MiDecayPfnFullyInitialized_function_00447748.md) at `0x00447818`
- [MiUpdatePageAttributeStamp](../48/MiUpdatePageAttributeStamp_function_00482364.md) at `0x00482437`

### Static image references
- `0x0027C4B4` → RVA `0x00E35C00` (`.data`; read)
- `0x0027C4E6` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0027C4EF` → RVA `0x00F0DE58` (`.data`; read)
- `0x0027C625` → RVA `0x00E30088` (`.data`; read)
- `0x0027C63E` → RVA `0x00E2DBC0` (`.data`; read)
- `0x0027C64A` → RVA `0x00E2DBC4` (`.data`; read)
- `0x0027C65B` → RVA `0x00E2DC20` (`.data`; read)
- `0x0027C6A6` → RVA `0x00E2DBC0` (`.data`; write)
- `0x0027C6D6` → RVA `0x00E2DC28` (`.data`; read)
- `0x0027C934` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0027C9E1` → RVA `0x00E2DCE0` (`.data`; read)
- `0x0027CA45` → RVA `0x00E3CBE6` (`.data`; read)
- `0x0027CA52` → RVA `0x00E3D240` (`.data`; read)
- `0x0027CB4C` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0027C450  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0027C455  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0027C45A  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0027C45F  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0027C464  57                              push rdi
0027C465  41 54                           push r12
0027C467  41 55                           push r13
0027C469  41 56                           push r14
0027C46B  41 57                           push r15
0027C46D  48 83 EC 60                     sub rsp, 0x60
0027C471  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
0027C479  45 33 DB                        xor r11d, r11d
0027C47C  45 8B E3                        mov r12d, r11d
0027C47F  4D 63 E8                        movsxd r13, r8d
0027C482  41 8B F9                        mov edi, r9d
0027C485  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0027C48F  4C 8B F2                        mov r14, rdx
0027C492  4C 8B D1                        mov r10, rcx
0027C495  48 8B C0                        mov rax, rax
0027C498  48 8B F2                        mov rsi, rdx
0027C49B  41 8D 4B 01                     lea ecx, [r11 + 1]
0027C49F  48 2B F0                        sub rsi, rax
0027C4A2  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0027C4AC  48 C1 FE 04                     sar rsi, 4
0027C4B0  48 0F AF F0                     imul rsi, rax
0027C4B4  48 8B 05 45 97 BB 00            mov rax, qword ptr [rip + 0xbb9745]
0027C4BB  48 3B F0                        cmp rsi, rax
0027C4BE  0F 82 F1 03 00 00               jb 0x14027c8b5
0027C4C4  48 05 00 08 00 00               add rax, 0x800
0027C4CA  48 3B F0                        cmp rsi, rax
0027C4CD  0F 83 E2 03 00 00               jae 0x14027c8b5
0027C4D3  44 8B F9                        mov r15d, ecx
0027C4D6  41 83 FD 09                     cmp r13d, 9
0027C4DA  0F 8C 29 06 00 00               jl 0x14027cb09
0027C4E0  88 0B                           mov byte ptr [rbx], cl
0027C4E2  49 8D 4A 20                     lea rcx, [r10 + 0x20]
0027C4E6  F6 05 19 A6 D4 00 21            test byte ptr [rip + 0xd4a619], 0x21
0027C4ED  74 1E                           je 0x14027c50d
0027C4EF  8B 05 63 19 C9 00               mov eax, dword ptr [rip + 0xc91963]
0027C4F5  85 C0                           test eax, eax
0027C4F7  75 14                           jne 0x14027c50d
0027C4F9  B2 FF                           mov dl, 0xff
0027C4FB  E8 20 08 00 00                  call 0x14027cd20
0027C500  4C 8B 94 24 90 00 00 00         mov r10, qword ptr [rsp + 0x90]
0027C508  45 33 DB                        xor r11d, r11d
0027C50B  EB 16                           jmp 0x14027c523
0027C50D  0F 0D 09                        prefetchw byte ptr [rcx]
0027C510  8B 01                           mov eax, dword ptr [rcx]
0027C512  0F BA F0 1F                     btr eax, 0x1f
0027C516  8D 50 01                        lea edx, [rax + 1]
0027C519  F0 0F B1 11                     lock cmpxchg dword ptr [rcx], edx
0027C51D  0F 85 B4 03 00 00               jne 0x14027c8d7
0027C523  4D 8B 06                        mov r8, qword ptr [r14]
0027C526  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0027C530  4D 8B 4E 18                     mov r9, qword ptr [r14 + 0x18]
0027C534  4C 23 C0                        and r8, rax
0027C537  4C 23 C8                        and r9, rax
0027C53A  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
0027C544  4C 3B C8                        cmp r9, rax
0027C547  0F 84 4B 04 00 00               je 0x14027c998
0027C54D  4B 8D 14 49                     lea rdx, [r9 + r9*2]
0027C551  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0027C55B  48 C1 E2 04                     shl rdx, 4
0027C55F  48 8B C0                        mov rax, rax
0027C562  48 03 D0                        add rdx, rax
0027C565  49 8D 4A 28                     lea rcx, [r10 + 0x28]
0027C569  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
0027C573  F0 48 0F BA 6A 18 3F            lock bts qword ptr [rdx + 0x18], 0x3f
0027C57A  0F 82 AD 02 00 00               jb 0x14027c82d
0027C580  48 89 53 10                     mov qword ptr [rbx + 0x10], rdx
0027C584  48 8D 7B 10                     lea rdi, [rbx + 0x10]
0027C588  4C 89 4B 08                     mov qword ptr [rbx + 8], r9
0027C58C  C6 43 18 01                     mov byte ptr [rbx + 0x18], 1
0027C590  4C 3B C0                        cmp r8, rax
0027C593  74 18                           je 0x14027c5ad
0027C595  4B 8D 0C 40                     lea rcx, [r8 + r8*2]
0027C599  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0027C5A3  48 C1 E1 04                     shl rcx, 4
0027C5A7  48 8B C0                        mov rax, rax
0027C5AA  48 03 C8                        add rcx, rax
0027C5AD  4D 3B C1                        cmp r8, r9
0027C5B0  0F 84 24 04 00 00               je 0x14027c9da
0027C5B6  F0 48 0F BA 69 18 3F            lock bts qword ptr [rcx + 0x18], 0x3f
0027C5BD  0F 82 63 02 00 00               jb 0x14027c826
0027C5C3  48 89 4B 28                     mov qword ptr [rbx + 0x28], rcx
0027C5C7  B1 01                           mov cl, 1
0027C5C9  4C 89 43 20                     mov qword ptr [rbx + 0x20], r8
0027C5CD  B8 30 00 00 00                  mov eax, 0x30
0027C5D2  48 8B D3                        mov rdx, rbx
0027C5D5  88 0C 03                        mov byte ptr [rbx + rax], cl
0027C5D8  41 83 7A 0C 02                  cmp dword ptr [r10 + 0xc], 2
0027C5DD  0F 85 1B 02 00 00               jne 0x14027c7fe
0027C5E3  45 85 FF                        test r15d, r15d
0027C5E6  0F 85 12 02 00 00               jne 0x14027c7fe
0027C5EC  45 85 E4                        test r12d, r12d
0027C5EF  0F 85 09 02 00 00               jne 0x14027c7fe
0027C5F5  0F 57 C0                        xorps xmm0, xmm0
0027C5F8  49 BC 00 00 00 00 00 DE FF FF   movabs r12, 0xffffde0000000000
0027C602  0F 57 C9                        xorps xmm1, xmm1
0027C605  4C 8D 3C 76                     lea r15, [rsi + rsi*2]
0027C609  F3 0F 7F 44 24 40               movdqu xmmword ptr [rsp + 0x40], xmm0
0027C60F  49 C1 E7 04                     shl r15, 4
0027C613  F3 0F 7F 4C 24 50               movdqu xmmword ptr [rsp + 0x50], xmm1
0027C619  49 8B C4                        mov rax, r12
0027C61C  4D 8D 04 07                     lea r8, [r15 + rax]
0027C620  49 8B 44 07 28                  mov rax, qword ptr [r15 + rax + 0x28]
0027C625  48 8B 0D 5C 3A BB 00            mov rcx, qword ptr [rip + 0xbb3a5c]
0027C62C  48 C1 E8 2B                     shr rax, 0x2b
0027C630  25 FF 03 00 00                  and eax, 0x3ff
0027C635  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
0027C63A  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
0027C63E  48 63 0D 7B 15 BB 00            movsxd rcx, dword ptr [rip + 0xbb157b]
0027C645  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
0027C64A  8B 15 74 15 BB 00               mov edx, dword ptr [rip + 0xbb1574]
0027C650  3B CA                           cmp ecx, edx
0027C652  77 1D                           ja 0x14027c671
0027C654  48 8B C1                        mov rax, rcx
0027C657  48 C1 E0 04                     shl rax, 4
0027C65B  48 03 05 BE 15 BB 00            add rax, qword ptr [rip + 0xbb15be]
0027C662  48 3B 30                        cmp rsi, qword ptr [rax]
0027C665  72 0A                           jb 0x14027c671
0027C667  3B CA                           cmp ecx, edx
0027C669  74 41                           je 0x14027c6ac
0027C66B  48 3B 70 10                     cmp rsi, qword ptr [rax + 0x10]
0027C66F  72 3B                           jb 0x14027c6ac
0027C671  45 8B CB                        mov r9d, r11d
0027C674  41 3B D1                        cmp edx, r9d
0027C677  0F 8C 40 02 00 00               jl 0x14027c8bd
0027C67D  41 8D 0C 11                     lea ecx, [r9 + rdx]
0027C681  D1 F9                           sar ecx, 1
0027C683  48 63 C1                        movsxd rax, ecx
0027C686  48 C1 E0 04                     shl rax, 4
0027C68A  48 03 05 8F 15 BB 00            add rax, qword ptr [rip + 0xbb158f]
0027C691  48 3B 30                        cmp rsi, qword ptr [rax]
0027C694  0F 82 E7 03 00 00               jb 0x14027ca81
0027C69A  3B 0D 24 15 BB 00               cmp ecx, dword ptr [rip + 0xbb1524]
0027C6A0  0F 85 DF 02 00 00               jne 0x14027c985
0027C6A6  89 0D 14 15 BB 00               mov dword ptr [rip + 0xbb1514], ecx
0027C6AC  8B 40 08                        mov eax, dword ptr [rax + 8]
0027C6AF  41 8B 70 20                     mov esi, dword ptr [r8 + 0x20]
0027C6B3  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0027C6B7  41 8B 40 20                     mov eax, dword ptr [r8 + 0x20]
0027C6BB  C1 E8 18                        shr eax, 0x18
0027C6BE  A8 08                           test al, 8
0027C6C0  0F 85 A3 02 00 00               jne 0x14027c969
0027C6C6  48 BA AB AA AA AA AA AA AA AA   movabs rdx, 0xaaaaaaaaaaaaaaab
0027C6D0  C1 EE 18                        shr esi, 0x18
0027C6D3  83 E6 07                        and esi, 7
0027C6D6  48 83 3D 4A 15 BB 00 00         cmp qword ptr [rip + 0xbb154a], 0
0027C6DE  0F 85 DD 02 00 00               jne 0x14027c9c1
0027C6E4  32 C9                           xor cl, cl
0027C6E6  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0027C6EA  48 69 D0 80 DF 00 00            imul rdx, rax, 0xdf80
0027C6F1  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0027C6F6  48 03 50 10                     add rdx, qword ptr [rax + 0x10]
0027C6FA  41 83 FD 09                     cmp r13d, 9
0027C6FE  0F 8C D4 03 00 00               jl 0x14027cad8
0027C704  0F B6 C9                        movzx ecx, cl
0027C707  8B C6                           mov eax, esi
0027C709  48 8D 0C CD 3B 00 00 00         lea rcx, [rcx*8 + 0x3b]
0027C711  48 03 C8                        add rcx, rax
0027C714  4C 6B C9 58                     imul r9, rcx, 0x58
0027C718  4C 03 CA                        add r9, rdx
0027C71B  49 8B 4E 28                     mov rcx, qword ptr [r14 + 0x28]
0027C71F  48 B8 00 00 00 00 00 00 80 0F   movabs rax, 0xf80000000000000
0027C729  48 23 C8                        and rcx, rax
0027C72C  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
0027C731  49 8B 06                        mov rax, qword ptr [r14]
0027C734  48 BA FF FF FF FF 3F 00 00 00   movabs rdx, 0x3fffffffff
0027C73E  48 C1 E8 14                     shr rax, 0x14
0027C742  48 0B C8                        or rcx, rax
0027C745  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
0027C749  48 25 00 00 E0 FF               and rax, 0xffffffffffe00000
0027C74F  48 C1 E9 14                     shr rcx, 0x14
0027C753  48 C1 E0 03                     shl rax, 3
0027C757  48 0B C8                        or rcx, rax
0027C75A  48 3B CA                        cmp rcx, rdx
0027C75D  0F 84 15 04 00 00               je 0x14027cb78
0027C763  4C 8D 0C 49                     lea r9, [rcx + rcx*2]
0027C767  49 C1 E1 04                     shl r9, 4
0027C76B  49 8B C4                        mov rax, r12
0027C76E  4C 03 C8                        add r9, rax
0027C771  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0027C775  45 8B 46 24                     mov r8d, dword ptr [r14 + 0x24]
0027C779  41 81 E0 FF FF 1F 00            and r8d, 0x1fffff
0027C780  48 C1 E8 28                     shr rax, 0x28
0027C784  49 C1 E0 13                     shl r8, 0x13
0027C788  25 FF FF 07 00                  and eax, 0x7ffff
0027C78D  4C 0B C0                        or r8, rax
0027C790  4C 3B C2                        cmp r8, rdx
0027C793  0F 84 A5 03 00 00               je 0x14027cb3e
0027C799  4F 8D 14 40                     lea r10, [r8 + r8*2]
0027C79D  49 C1 E2 04                     shl r10, 4
0027C7A1  49 8B C4                        mov rax, r12
0027C7A4  4C 03 D0                        add r10, rax
0027C7A7  45 33 DB                        xor r11d, r11d
0027C7AA  48 8B C7                        mov rax, rdi
0027C7AD  41 8B D3                        mov edx, r11d
0027C7B0  48 83 FA 04                     cmp rdx, 4
0027C7B4  0F 8D 08 03 00 00               jge 0x14027cac2
0027C7BA  44 38 58 08                     cmp byte ptr [rax + 8], r11b
0027C7BE  75 09                           jne 0x14027c7c9
0027C7C0  48 FF C2                        inc rdx
0027C7C3  48 83 C0 18                     add rax, 0x18
0027C7C7  EB E7                           jmp 0x14027c7b0
0027C7C9  4C 3B 08                        cmp r9, qword ptr [rax]
0027C7CC  75 F2                           jne 0x14027c7c0
0027C7CE  4C 89 4B 58                     mov qword ptr [rbx + 0x58], r9
0027C7D2  49 8B C3                        mov rax, r11
0027C7D5  48 89 4B 50                     mov qword ptr [rbx + 0x50], rcx
0027C7D9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0027C7E0  48 83 F8 04                     cmp rax, 4
0027C7E4  0F 8D BA 02 00 00               jge 0x14027caa4
0027C7EA  44 38 5F 08                     cmp byte ptr [rdi + 8], r11b
0027C7EE  75 09                           jne 0x14027c7f9
0027C7F0  48 FF C0                        inc rax
0027C7F3  48 83 C7 18                     add rdi, 0x18
0027C7F7  EB E7                           jmp 0x14027c7e0
0027C7F9  4C 3B 17                        cmp r10, qword ptr [rdi]
0027C7FC  75 F2                           jne 0x14027c7f0
0027C7FE  B8 01 00 00 00                  mov eax, 1
0027C803  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
0027C808  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0027C80C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0027C810  49 8B E3                        mov rsp, r11
0027C813  41 5F                           pop r15
0027C815  41 5E                           pop r14
0027C817  41 5D                           pop r13
0027C819  41 5C                           pop r12
0027C81B  5F                              pop rdi
0027C81C  C3                              ret
0027C81D  CC                              int3
0027C81E  4C 8B 94 24 90 00 00 00         mov r10, qword ptr [rsp + 0x90]
0027C826  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
0027C82D  80 3B 00                        cmp byte ptr [rbx], 0
0027C830  0F 84 EF 02 00 00               je 0x14027cb25
0027C836  80 7B 18 00                     cmp byte ptr [rbx + 0x18], 0
0027C83A  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
0027C844  74 0D                           je 0x14027c853
0027C846  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0027C84A  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
0027C84F  C6 43 18 00                     mov byte ptr [rbx + 0x18], 0
0027C853  80 7B 30 00                     cmp byte ptr [rbx + 0x30], 0
0027C857  74 0D                           je 0x14027c866
0027C859  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0027C85D  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
0027C862  C6 43 30 00                     mov byte ptr [rbx + 0x30], 0
0027C866  80 7B 48 00                     cmp byte ptr [rbx + 0x48], 0
0027C86A  74 0D                           je 0x14027c879
0027C86C  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0027C870  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
0027C875  C6 43 48 00                     mov byte ptr [rbx + 0x48], 0
0027C879  80 7B 60 00                     cmp byte ptr [rbx + 0x60], 0
0027C87D  74 0D                           je 0x14027c88c
0027C87F  48 8B 43 58                     mov rax, qword ptr [rbx + 0x58]
0027C883  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
0027C888  C6 43 60 00                     mov byte ptr [rbx + 0x60], 0
0027C88C  F6 05 73 A2 D4 00 01            test byte ptr [rip + 0xd4a273], 1
0027C893  49 8D 4A 20                     lea rcx, [r10 + 0x20]
0027C897  0F 85 E4 02 00 00               jne 0x14027cb81
0027C89D  F0 81 21 FF FF FF BF            lock and dword ptr [rcx], 0xbfffffff
0027C8A4  F0 FF 09                        lock dec dword ptr [rcx]
0027C8A7  C6 03 00                        mov byte ptr [rbx], 0
0027C8AA  85 FF                           test edi, edi
0027C8AC  75 3D                           jne 0x14027c8eb
0027C8AE  33 C0                           xor eax, eax
0027C8B0  E9 4E FF FF FF                  jmp 0x14027c803
0027C8B5  45 8B FB                        mov r15d, r11d
0027C8B8  E9 19 FC FF FF                  jmp 0x14027c4d6
0027C8BD  45 33 C9                        xor r9d, r9d
0027C8C0  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
0027C8C5  4C 8B C6                        mov r8, rsi
0027C8C8  BA 80 51 00 00                  mov edx, 0x5180
0027C8CD  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
0027C8D1  E8 8A 0D 28 00                  call 0x1404fd660
0027C8D6  CC                              int3
0027C8D7  85 C0                           test eax, eax
0027C8D9  0F 89 37 FC FF FF               jns 0x14027c516
0027C8DF  B2 FF                           mov dl, 0xff
0027C8E1  E8 9A 5A 0E 00                  call 0x140362380
0027C8E6  E9 15 FC FF FF                  jmp 0x14027c500
0027C8EB  F6 05 14 A2 D4 00 21            test byte ptr [rip + 0xd4a214], 0x21
0027C8F2  49 8D 5A 20                     lea rbx, [r10 + 0x20]
0027C8F6  0F 85 A8 00 00 00               jne 0x14027c9a4
0027C8FC  F0 0F BA 2B 1F                  lock bts dword ptr [rbx], 0x1f
0027C901  73 0D                           jae 0x14027c910
0027C903  B2 FF                           mov dl, 0xff
0027C905  48 8B CB                        mov rcx, rbx
0027C908  E8 93 70 0A 00                  call 0x1403239a0
0027C90D  44 8B D8                        mov r11d, eax
0027C910  8B 13                           mov edx, dword ptr [rbx]
0027C912  8B CA                           mov ecx, edx
0027C914  0F BA F1 1E                     btr ecx, 0x1e
0027C918  81 F9 00 00 00 80               cmp ecx, 0x80000000
0027C91E  0F 84 DA FE FF FF               je 0x14027c7fe
0027C924  0F BA E2 1E                     bt edx, 0x1e
0027C928  72 07                           jb 0x14027c931
0027C92A  F0 81 0B 00 00 00 40            lock or dword ptr [rbx], 0x40000000
0027C931  41 FF C3                        inc r11d
0027C934  44 85 1D 71 89 D4 00            test dword ptr [rip + 0xd48971], r11d
0027C93B  4C 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r11
0027C943  0F 84 03 02 00 00               je 0x14027cb4c
0027C949  F3 90                           pause
0027C94B  8B 13                           mov edx, dword ptr [rbx]
0027C94D  8B CA                           mov ecx, edx
0027C94F  4C 8B 9C 24 B0 00 00 00         mov r11, qword ptr [rsp + 0xb0]
0027C957  0F BA F1 1E                     btr ecx, 0x1e
0027C95B  81 F9 00 00 00 80               cmp ecx, 0x80000000
0027C961  0F 84 97 FE FF FF               je 0x14027c7fe
0027C967  EB BB                           jmp 0x14027c924
0027C969  49 8B C4                        mov rax, r12
0027C96C  4C 3B C0                        cmp r8, rax
0027C96F  73 70                           jae 0x14027c9e1
0027C971  48 BA AB AA AA AA AA AA AA AA   movabs rdx, 0xaaaaaaaaaaaaaaab
0027C97B  BE 05 00 00 00                  mov esi, 5
0027C980  E9 51 FD FF FF                  jmp 0x14027c6d6
0027C985  48 3B 70 10                     cmp rsi, qword ptr [rax + 0x10]
0027C989  0F 82 17 FD FF FF               jb 0x14027c6a6
0027C98F  44 8D 49 01                     lea r9d, [rcx + 1]
0027C993  E9 DC FC FF FF                  jmp 0x14027c674
0027C998  49 8D 52 28                     lea rdx, [r10 + 0x28]
0027C99C  48 8B CA                        mov rcx, rdx
0027C99F  E9 CF FB FF FF                  jmp 0x14027c573
0027C9A4  8B 05 AE 14 C9 00               mov eax, dword ptr [rip + 0xc914ae]
0027C9AA  85 C0                           test eax, eax
0027C9AC  0F 85 4A FF FF FF               jne 0x14027c8fc
0027C9B2  B2 FF                           mov dl, 0xff
0027C9B4  48 8B CB                        mov rcx, rbx
0027C9B7  E8 B4 70 0A 00                  call 0x140323a70
0027C9BC  E9 3D FE FF FF                  jmp 0x14027c7fe
0027C9C1  49 8B CF                        mov rcx, r15
0027C9C4  48 C1 F9 04                     sar rcx, 4
0027C9C8  48 0F AF CA                     imul rcx, rdx
0027C9CC  E8 53 F4 0B 00                  call 0x14033be24
0027C9D1  0F B6 48 0C                     movzx ecx, byte ptr [rax + 0xc]
0027C9D5  E9 0C FD FF FF                  jmp 0x14027c6e6
0027C9DA  32 C9                           xor cl, cl
0027C9DC  E9 EC FB FF FF                  jmp 0x14027c5cd
0027C9E1  48 8B 05 F8 12 BB 00            mov rax, qword ptr [rip + 0xbb12f8]
0027C9E8  48 8D 0C 40                     lea rcx, [rax + rax*2]
0027C9EC  48 C1 E1 04                     shl rcx, 4
0027C9F0  48 B8 30 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000030
0027C9FA  48 03 C8                        add rcx, rax
0027C9FD  48 BA AB AA AA AA AA AA AA AA   movabs rdx, 0xaaaaaaaaaaaaaaab
0027CA07  4C 3B C1                        cmp r8, rcx
0027CA0A  0F 83 6B FF FF FF               jae 0x14027c97b
0027CA10  48 8B 05 E9 91 BB 00            mov rax, qword ptr [rip + 0xbb91e9]
0027CA17  49 8B CF                        mov rcx, r15
0027CA1A  48 C1 F9 04                     sar rcx, 4
0027CA1E  48 0F AF CA                     imul rcx, rdx
0027CA22  48 3B C8                        cmp rcx, rax
0027CA25  72 0F                           jb 0x14027ca36
0027CA27  48 05 00 08 00 00               add rax, 0x800
0027CA2D  48 3B C8                        cmp rcx, rax
0027CA30  0F 82 45 FF FF FF               jb 0x14027c97b
0027CA36  8B C6                           mov eax, esi
0027CA38  C1 E8 10                        shr eax, 0x10
0027CA3B  24 07                           and al, 7
0027CA3D  3C 06                           cmp al, 6
0027CA3F  0F 84 8B FC FF FF               je 0x14027c6d0
0027CA45  80 3D 9A 01 BC 00 00            cmp byte ptr [rip + 0xbc019a], 0
0027CA4C  0F 84 29 FF FF FF               je 0x14027c97b
0027CA52  48 8B 05 E7 07 BC 00            mov rax, qword ptr [rip + 0xbc07e7]
0027CA59  48 C1 E9 09                     shr rcx, 9
0027CA5D  0F B6 14 48                     movzx edx, byte ptr [rax + rcx*2]
0027CA61  84 D2                           test dl, dl
0027CA63  0F 84 08 FF FF FF               je 0x14027c971
0027CA69  80 FA 0A                        cmp dl, 0xa
0027CA6C  48 BA AB AA AA AA AA AA AA AA   movabs rdx, 0xaaaaaaaaaaaaaaab
0027CA76  0F 85 54 FC FF FF               jne 0x14027c6d0
0027CA7C  E9 FA FE FF FF                  jmp 0x14027c97b
0027CA81  85 C9                           test ecx, ecx
0027CA83  0F 85 4E 01 00 00               jne 0x14027cbd7
0027CA89  4C 8B C8                        mov r9, rax
0027CA8C  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
0027CA91  4C 8B C6                        mov r8, rsi
0027CA94  BA 80 51 00 00                  mov edx, 0x5180
0027CA99  B9 1A 00 00 00                  mov ecx, 0x1a
0027CA9E  E8 BD 0B 28 00                  call 0x1404fd660
0027CAA3  CC                              int3
0027CAA4  F0 49 0F BA 6A 18 3F            lock bts qword ptr [r10 + 0x18], 0x3f
0027CAAB  0F 82 6D FD FF FF               jb 0x14027c81e
0027CAB1  4C 89 53 40                     mov qword ptr [rbx + 0x40], r10
0027CAB5  4C 89 43 38                     mov qword ptr [rbx + 0x38], r8
0027CAB9  C6 43 48 01                     mov byte ptr [rbx + 0x48], 1
0027CABD  E9 3C FD FF FF                  jmp 0x14027c7fe
0027CAC2  F0 49 0F BA 69 18 3F            lock bts qword ptr [r9 + 0x18], 0x3f
0027CAC9  0F 82 4F FD FF FF               jb 0x14027c81e
0027CACF  C6 43 60 01                     mov byte ptr [rbx + 0x60], 1
0027CAD3  E9 F6 FC FF FF                  jmp 0x14027c7ce
0027CAD8  41 83 FD 08                     cmp r13d, 8
0027CADC  0F 84 CA 00 00 00               je 0x14027cbac
0027CAE2  32 C9                           xor cl, cl
0027CAE4  88 4C 24 58                     mov byte ptr [rsp + 0x58], cl
0027CAE8  0F B6 C9                        movzx ecx, cl
0027CAEB  8B C6                           mov eax, esi
0027CAED  48 8D 0C C8                     lea rcx, [rax + rcx*8]
0027CAF1  4C 6B C9 58                     imul r9, rcx, 0x58
0027CAF5  49 69 CD E8 00 00 00            imul rcx, r13, 0xe8
0027CAFC  4C 03 8C 11 98 3D 00 00         add r9, qword ptr [rcx + rdx + 0x3d98]
0027CB04  E9 12 FC FF FF                  jmp 0x14027c71b
0027CB09  41 83 7A 0C 02                  cmp dword ptr [r10 + 0xc], 2
0027CB0E  0F 85 CC F9 FF FF               jne 0x14027c4e0
0027CB14  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
0027CB17  C1 E8 18                        shr eax, 0x18
0027CB1A  A8 08                           test al, 8
0027CB1C  44 0F 45 E1                     cmovne r12d, ecx
0027CB20  E9 BB F9 FF FF                  jmp 0x14027c4e0
0027CB25  49 8D 4A 20                     lea rcx, [r10 + 0x20]
0027CB29  E8 B2 CC FC FF                  call 0x1402497e0
0027CB2E  4C 8B 94 24 90 00 00 00         mov r10, qword ptr [rsp + 0x90]
0027CB36  45 33 DB                        xor r11d, r11d
0027CB39  E9 69 FD FF FF                  jmp 0x14027c8a7
0027CB3E  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
0027CB43  49 83 C2 28                     add r10, 0x28
0027CB47  E9 5B FC FF FF                  jmp 0x14027c7a7
0027CB4C  8B 05 66 9F D4 00               mov eax, dword ptr [rip + 0xd49f66]
0027CB52  A8 40                           test al, 0x40
0027CB54  0F 84 EF FD FF FF               je 0x14027c949
0027CB5A  E8 31 29 09 00                  call 0x14030f490
0027CB5F  84 C0                           test al, al
0027CB61  0F 84 E2 FD FF FF               je 0x14027c949
0027CB67  8B 8C 24 B0 00 00 00            mov ecx, dword ptr [rsp + 0xb0]
0027CB6E  E8 ED 28 09 00                  call 0x14030f460
0027CB73  E9 D3 FD FF FF                  jmp 0x14027c94b
0027CB78  49 83 C1 28                     add r9, 0x28
0027CB7C  E9 F0 FB FF FF                  jmp 0x14027c771
0027CB81  8B 05 D1 12 C9 00               mov eax, dword ptr [rip + 0xc912d1]
0027CB87  85 C0                           test eax, eax
0027CB89  0F 85 0E FD FF FF               jne 0x14027c89d
0027CB8F  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0027CB97  E8 AC 43 07 00                  call 0x1402f0f48
0027CB9C  4C 8B 94 24 90 00 00 00         mov r10, qword ptr [rsp + 0x90]
0027CBA4  45 33 DB                        xor r11d, r11d
0027CBA7  E9 FB FC FF FF                  jmp 0x14027c8a7
0027CBAC  49 C1 FF 04                     sar r15, 4
0027CBB0  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0027CBBA  4C 0F AF F8                     imul r15, rax
0027CBBE  48 8B 05 7B 06 BC 00            mov rax, qword ptr [rip + 0xbc067b]
0027CBC5  49 C1 EF 09                     shr r15, 9
0027CBC9  42 0F B6 4C 78 01               movzx ecx, byte ptr [rax + r15*2 + 1]
0027CBCF  80 E1 7F                        and cl, 0x7f
0027CBD2  E9 0D FF FF FF                  jmp 0x14027cae4
0027CBD7  8D 51 FF                        lea edx, [rcx - 1]
0027CBDA  E9 95 FA FF FF                  jmp 0x14027c674
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAcquirePageListLock(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int8 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = a4;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (96);
    v_r11 = 0;
    v_rsi = (a2) - (result);
    v_rsi = (v_rsi) >> (4);
    v_rsi = (v_rsi) * (result);
    if (v_rsi < (*(unsigned __int64 *)(v_rip + 12293957))) goto loc_0027C8B5;
    result = (*(unsigned __int64 *)(v_rip + 12293957)) + (0x800ULL);
    if (v_rsi >= result) goto loc_0027C8B5;
loc_0027C4D6:
    if (((unsigned int)((int)(a3))) < 9) goto loc_0027CB09;
loc_0027C4E0:
    *(unsigned __int8 *)(a5) = (unsigned __int8)(v_r11 + 1);
    if (((*(unsigned __int8 *)(v_rip + 13936153)) & (33)) == 0) goto loc_0027C50D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13179235))) != 0) goto loc_0027C50D;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(a1 + 32, 255, a3, a4);
loc_0027C500:
    v_r11 = 0;
    goto loc_0027C523;
loc_0027C50D:
loc_0027C516:
    if (condition_is_not_equal) goto loc_0027C8D7;
loc_0027C523:
    a3 = (*(unsigned __int64 *)(a2)) & ((unsigned int)(*(unsigned int *)(a1 + 32)));
    a4 = (*(unsigned __int64 *)(a2 + 24)) & ((unsigned int)(*(unsigned int *)(a1 + 32)));
    if (a4 == ((unsigned int)(*(unsigned int *)(a1 + 32)))) goto loc_0027C998;
    a2 = (a4 + a4 * 2) << (4);
    a2 = (a2) + ((unsigned int)(*(unsigned int *)(a1 + 32)));
loc_0027C573:
    if (condition_is_below) goto loc_0027C82D;
    *(unsigned __int64 *)(a5 + 16) = a2;
    *(unsigned __int64 *)(a5 + 8) = a4;
    *(unsigned __int8 *)(a5 + 24) = 1;
    result = (unsigned int)(*(unsigned int *)(a1 + 32));
    if (a3 != ((unsigned int)(*(unsigned int *)(a1 + 32)))) {
        a1 = a3 + a3 * 2;
        a1 = (a1) << (4);
        result = (unsigned int)(*(unsigned int *)(a1 + 32));
        a1 = (a1) + (result);
    }
    if (a3 == a4) goto loc_0027C9DA;
    if (a3 < a4) goto loc_0027C826;
    *(unsigned __int64 *)(a5 + 40) = a1;
    *(unsigned __int64 *)(a5 + 32) = a3;
loc_0027C5CD:
    *(unsigned __int8 *)(a5 + 48 * 1) = 1;
    if ((*(unsigned int *)(v_stack_p8 + 12)) != 2) goto loc_0027C7FE;
    if ((unsigned int)((unsigned int)((unsigned int)(v_r11 + 1))) != 0) goto loc_0027C7FE;
    if (0 != 0) goto loc_0027C7FE;
    v_stack_m48 = v_xmm0;
    v_r15 = (v_rsi + v_rsi * 2) << (4);
    v_stack_m38 = v_xmm1;
    result = (*(unsigned __int64 *)(v_r15 + 0 * 1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m50 = v_r15 + 0 * 1;
    v_stack_m58 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12270172) + result * 8);
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 12260731)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12260724))))) goto loc_0027C671;
    result = ((int)(*(unsigned int *)(v_rip + 12260731))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 12260798));
    if (v_rsi < (*(unsigned __int64 *)(result))) goto loc_0027C671;
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 12260731)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12260724))))) goto loc_0027C6AC;
    if (v_rsi < (*(unsigned __int64 *)(result + 16))) goto loc_0027C6AC;
loc_0027C671:
loc_0027C674:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12260724)))) < 0) goto loc_0027C8BD;
    a1 = (unsigned int)((0 + (unsigned int)(*(unsigned int *)(v_rip + 12260724)) * 1) >> (1));
    result = ((int)((unsigned int)(a1))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 12260751));
    if (v_rsi < (*(unsigned __int64 *)(result))) goto loc_0027CA81;
    if (((unsigned int)(a1)) != (*(unsigned int *)(v_rip + 12260644))) goto loc_0027C985;
loc_0027C6A6:
    *(unsigned int *)(v_rip + 12260628) = (unsigned int)(a1);
loc_0027C6AC:
    v_stack_m40 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 0 * 1 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_0027C969;
loc_0027C6D0:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 0 * 1 + 32))) >> (24));
    v_rsi = (unsigned int)((v_rsi) & (7));
loc_0027C6D6:
    if ((*(unsigned __int64 *)(v_rip + 12260682)) != 0) goto loc_0027C9C1;
    a1 = 0;
loc_0027C6E6:
    a2 = ((unsigned int)(*(unsigned int *)(v_rip + 12260724))) * ((unsigned int)(v_stack_m40));
    a2 = (a2) + (*(unsigned __int64 *)(v_stack_m58 + 16));
    if (((unsigned int)((int)(a3))) < 9) goto loc_0027CAD8;
    a1 = (0 * 8 + 59) + ((unsigned int)((unsigned int)(v_rsi)));
    a4 = (0) * (a1);
    a4 = (a4) + (a2);
loc_0027C71B:
    a1 = (*(unsigned __int64 *)(a2 + 40)) & ((unsigned int)((unsigned int)(v_rsi)));
    v_stack_m48 = a4;
    result = (*(unsigned __int64 *)(a2)) >> (20);
    a1 = (a1) | (result);
    result = ((unsigned int)(*(unsigned int *)(a2 + 36))) & (0xFFFFFFFFFFE00000ULL);
    a1 = (a1) >> (20);
    result = (result) << (3);
    a1 = (a1) | (result);
    if (a1 == a2) goto loc_0027CB78;
    a4 = (a1 + a1 * 2) << (4);
    a4 = (a4) + (0);
loc_0027C771:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 36))) & (0x1FFFFFULL));
    result = (*(unsigned __int64 *)(a2 + 24)) >> (40);
    a3 = (a3) << (19);
    result = (unsigned int)((result) & (0x7FFFFULL));
    a3 = (a3) | (result);
    if (a3 == a2) goto loc_0027CB3E;
    v_r10 = (a3 + a3 * 2) << (4);
    v_r10 = (v_r10) + (0);
loc_0027C7A7:
    v_r11 = 0;
loc_0027C7B0:
    if (0 >= 4) goto loc_0027CAC2;
    if ((*(unsigned __int8 *)(a5 + 16 + 8)) != 0) goto loc_0027C7C9;
loc_0027C7C0:
    a2 = (0) + 1;
    result = (a5 + 16) + (24);
    goto loc_0027C7B0;
loc_0027C7C9:
    if (a4 != (*(unsigned __int64 *)(result))) goto loc_0027C7C0;
loc_0027C7CE:
    *(unsigned __int64 *)(a5 + 88) = a4;
    *(unsigned __int64 *)(a5 + 80) = a1;
loc_0027C7E0:
    if (0 >= 4) goto loc_0027CAA4;
    if ((*(unsigned __int8 *)(a5 + 16 + 8)) != 0) goto loc_0027C7F9;
loc_0027C7F0:
    result = (0) + 1;
    v_rdi = (a5 + 16) + (24);
    goto loc_0027C7E0;
loc_0027C7F9:
    if (v_r10 != (*(unsigned __int64 *)(v_rdi))) goto loc_0027C7F0;
loc_0027C7FE:
loc_0027C803:
    return 1;
loc_0027C81E:
loc_0027C826:
loc_0027C82D:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56))) == 0) goto loc_0027CB25;
    result = 1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 24)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16);
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 24) = 0;
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 48)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 40);
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 48) = 0;
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 72)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 64);
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 72) = 0;
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 96)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 88);
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 96) = 0;
    }
    if (((*(unsigned __int8 *)(v_rip + 13935219)) & (1)) != 0) goto loc_0027CB81;
loc_0027C89D:
loc_0027C8A7:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56)) = 0;
    if ((unsigned int)((unsigned int)(v_stack_p48)) != 0) goto loc_0027C8EB;
    result = 0;
    goto loc_0027C803;
loc_0027C8B5:
    goto loc_0027C4D6;
loc_0027C8BD:
    a4 = 0;
    v_stack_m40 = v_stack_m28;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x5180ULL), *(unsigned __int64 *)(v_stack_m28 + 64), a4);
loc_0027C8D7:
    if (!sign_flag) goto loc_0027C516;
    result = ExpWaitForSpinLockSharedAndAcquire(a4 + 26, 255, *(unsigned __int64 *)(v_stack_m28 + 64), a4);
    goto loc_0027C500;
loc_0027C8EB:
    if (((*(unsigned __int8 *)(v_rip + 13935124)) & (33)) != 0) goto loc_0027C9A4;
loc_0027C8FC:
    v_r11 = v_stack_m28;
    if (!(condition_is_above_or_equal)) {
        a2 = 255;
        a1 = v_stack_p30 + 32;
        result = ExpWaitForSpinLockExclusiveAndAcquire(a1, a2, *(unsigned __int64 *)(v_stack_m28 + 64), a4);
        v_r11 = (unsigned int)(result);
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p30 + 32)))))) == 0x80000000ULL) goto loc_0027C7FE;
loc_0027C924:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p30 + 32)))))) >= 0x80000000ULL) {
    }
    v_r11 = (unsigned int)((v_r11) + 1);
    v_stack_p50 = v_r11;
    if (((*(unsigned int *)(v_rip + 13928817)) & ((unsigned int)(v_r11))) == 0) goto loc_0027CB4C;
loc_0027C949:
loc_0027C94B:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p30 + 32)))))) == 0x80000000ULL) goto loc_0027C7FE;
    goto loc_0027C924;
loc_0027C969:
    if ((*(unsigned __int64 *)(v_stack_m28 + 64)) >= 0) goto loc_0027C9E1;
loc_0027C971:
loc_0027C97B:
    goto loc_0027C6D6;
loc_0027C985:
    if (5 < (*(unsigned __int64 *)(0 + 16))) goto loc_0027C6A6;
    goto loc_0027C674;
loc_0027C998:
    goto loc_0027C573;
loc_0027C9A4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13178030))) != 0) goto loc_0027C8FC;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_stack_p30 + 32, 255, *(unsigned __int64 *)(v_stack_m28 + 64), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p30 + 32)))) + 1);
    goto loc_0027C7FE;
loc_0027C9C1:
    a1 = ((unsigned int)((unsigned int)(v_stack_m28))) >> (4);
    a1 = (a1) * (255);
    result = MiSearchChannelTable(a1, 255, *(unsigned __int64 *)(v_stack_m28 + 64), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p30 + 32)))) + 1);
    goto loc_0027C6E6;
loc_0027C9DA:
    a1 = 0;
    goto loc_0027C5CD;
loc_0027C9E1:
    a1 = (*(unsigned __int64 *)(v_rip + 12260088) + *(unsigned __int64 *)(v_rip + 12260088) * 2) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 12260088));
    if ((*(unsigned __int64 *)(v_stack_m28 + 64)) >= a1) goto loc_0027C97B;
    a1 = ((unsigned int)((unsigned int)(v_stack_m28))) >> (4);
    a1 = (a1) * (255);
    if (a1 < (*(unsigned __int64 *)(v_rip + 12292585))) goto loc_0027CA36;
    result = (*(unsigned __int64 *)(v_rip + 12292585)) + (0x800ULL);
    if (a1 < result) goto loc_0027C97B;
loc_0027CA36:
    result = (unsigned int)((5) >> (16));
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 6) goto loc_0027C6D0;
    if ((*(unsigned __int8 *)(v_rip + 12321178)) == 0) goto loc_0027C97B;
    a1 = (a1) >> (9);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12322791) + a1 * 2)) == 0) goto loc_0027C971;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12322791) + a1 * 2))) != 10) goto loc_0027C6D0;
    goto loc_0027C97B;
loc_0027CA81:
    if ((unsigned int)(a1) != 0) goto loc_0027CBD7;
    v_stack_m40 = a5;
    result = KeBugCheckEx(26, (unsigned int)(0x5180ULL), 5, *(unsigned __int64 *)(v_rip + 12322791));
loc_0027CAA4:
    if (condition_is_below) goto loc_0027C81E;
    *(unsigned __int64 *)(v_stack_p30 + 32 + 64) = v_stack_p30;
    *(unsigned __int64 *)(v_stack_p30 + 32 + 56) = 5;
    *(unsigned __int8 *)(v_stack_p30 + 32 + 72) = 1;
    goto loc_0027C7FE;
loc_0027CAC2:
    if (condition_is_below) goto loc_0027C81E;
    *(unsigned __int8 *)(v_stack_p30 + 32 + 96) = 1;
    goto loc_0027C7CE;
loc_0027CAD8:
    if (((unsigned int)((int)(a3))) == 8) goto loc_0027CBAC;
    a1 = 0;
loc_0027CAE4:
    v_stack_m8 = 0;
    a4 = (*(unsigned __int64 *)(v_rip + 12322791)) * (5 + 0 * 8);
    a1 = (5 + 0 * 8) * ((int)(a3));
    a4 = (a4) + (*(unsigned __int64 *)(a1 + (unsigned int)(0x5180ULL) * 1 + 15768));
    goto loc_0027C71B;
loc_0027CB09:
    if ((*(unsigned int *)(v_stack_p30 + 12)) != 2) goto loc_0027C4E0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(0x5180ULL) + 32))) >> (24));
    v_r12 = 0;
    if ((((unsigned __int8)(result)) & (8)) != 0) { v_r12 = (unsigned int)(a1); }
    goto loc_0027C4E0;
loc_0027CB25:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_p30 + 32, (unsigned int)(0x5180ULL), 5, a4);
    v_r11 = 0;
    goto loc_0027C8A7;
loc_0027CB3E:
    v_r10 = (v_stack_m20) + (40);
    goto loc_0027C7A7;
loc_0027CB4C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13934438)))) & (64)) == 0) goto loc_0027C949;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p30 + 32, (unsigned int)(0x5180ULL), 5, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0027C949;
    result = HvlNotifyLongSpinWait((unsigned int)(a5), (unsigned int)(0x5180ULL), 5, a4);
    goto loc_0027C94B;
loc_0027CB78:
    a4 = (a4) + (40);
    goto loc_0027C771;
loc_0027CB81:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13177553))) != 0) goto loc_0027C89D;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented((unsigned int)(a5), v_stack_p28, 5, a4);
    v_r11 = 0;
    goto loc_0027C8A7;
loc_0027CBAC:
    v_r15 = ((unsigned int)((unsigned int)(v_stack_m28))) >> (4);
    v_r15 = (v_r15) * (result);
    v_r15 = (v_r15) >> (9);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12322427) + v_r15 * 2 + 1)) & (127));
    goto loc_0027CAE4;
loc_0027CBD7:
    goto loc_0027C674;
}
```

## 5. (Beta) C Style

```c
int64_t MiAcquirePageListLock(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint8_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = Arg4;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (96);
    local_r11 = 0;
    local_rsi = (Arg2) - (result);
    local_rsi = (local_rsi) >> (4);
    local_rsi = (local_rsi) * (result);
    if (local_rsi < (*(uint64_t *)(v_rip + 0xBB9745))) goto loc_0027C8B5;
    result = (*(uint64_t *)(v_rip + 0xBB9745)) + (0x800ULL);
    if (local_rsi >= result) goto loc_0027C8B5;
loc_0027C4D6:
    if (((uint32_t)((int32_t)(Arg3))) < 9) goto loc_0027CB09;
loc_0027C4E0:
    *(uint8_t *)(arg5) = (uint8_t)(local_r11 + 1);
    if (((*(uint8_t *)(v_rip + 0xD4A619)) & (33)) == 0) goto loc_0027C50D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC91963))) != 0) goto loc_0027C50D;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(Arg1 + 32, 255, Arg3, Arg4);
loc_0027C500:
    local_r11 = 0;
    goto loc_0027C523;
loc_0027C50D:
loc_0027C516:
    if (condition_is_not_equal) goto loc_0027C8D7;
loc_0027C523:
    Arg3 = (*(uint64_t *)(arg2)) & ((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    Arg4 = (*(uint64_t *)(arg2 + 0x18)) & ((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    if (Arg4 == ((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) goto loc_0027C998;
    Arg2 = (Arg4 + Arg4 * 2) << (4);
    Arg2 = (Arg2) + ((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
loc_0027C573:
    if (condition_is_below) goto loc_0027C82D;
    *(void **)(arg5 + 0x10) = Arg2;
    *(uint64_t *)(arg5 + 0x8) = Arg4;
    *(uint8_t *)(arg5 + 0x18) = 1;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x20));
    if (Arg3 != ((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) {
        Arg1 = Arg3 + Arg3 * 2;
        Arg1 = (Arg1) << (4);
        result = (uint32_t)(*(uint32_t *)(arg1 + 0x20));
        Arg1 = (Arg1) + (result);
    }
    if (Arg3 == Arg4) goto loc_0027C9DA;
    if (Arg3 < Arg4) goto loc_0027C826;
    *(void **)(arg5 + 0x28) = Arg1;
    *(uint64_t *)(arg5 + 0x20) = Arg3;
loc_0027C5CD:
    *(uint8_t *)(arg5 + 0x30 * 1) = 1;
    if ((*(uint32_t *)(v_stack_p8 + 0xC)) != 2) goto loc_0027C7FE;
    if ((uint32_t)((uint32_t)((uint32_t)(local_r11 + 1))) != 0) goto loc_0027C7FE;
    if (0 != 0) goto loc_0027C7FE;
    v_stack_m48 = v_xmm0;
    local_r15 = (local_rsi + local_rsi * 2) << (4);
    v_stack_m38 = v_xmm1;
    result = (*(uint64_t *)(local_r15 + 0x0 * 1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m50 = local_r15 + 0 * 1;
    v_stack_m58 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBB3A5C) + result * 8);
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xBB157B)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB1574))))) goto loc_0027C671;
    result = ((int32_t)(*(uint32_t *)(v_rip + 0xBB157B))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xBB15BE));
    if (local_rsi < (*(uint64_t *)(result))) goto loc_0027C671;
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xBB157B)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB1574))))) goto loc_0027C6AC;
    if (local_rsi < (*(uint64_t *)(result + 0x10))) goto loc_0027C6AC;
loc_0027C671:
loc_0027C674:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB1574)))) < 0) goto loc_0027C8BD;
    Arg1 = (uint32_t)((0 + (uint32_t)(*(uint32_t *)(v_rip + 0xBB1574)) * 1) >> (1));
    result = ((int32_t)((uint32_t)(Arg1))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xBB158F));
    if (local_rsi < (*(uint64_t *)(result))) goto loc_0027CA81;
    if (((uint32_t)(Arg1)) != (*(uint32_t *)(v_rip + 0xBB1524))) goto loc_0027C985;
loc_0027C6A6:
    *(uint32_t *)(v_rip + 0xBB1514) = (uint32_t)(Arg1);
loc_0027C6AC:
    v_stack_m40 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x0 * 1 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_0027C969;
loc_0027C6D0:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x0 * 1 + 0x20))) >> (24));
    local_rsi = (uint32_t)((local_rsi) & (7));
loc_0027C6D6:
    if ((*(uint64_t *)(v_rip + 0xBB154A)) != 0) goto loc_0027C9C1;
    Arg1 = 0;
loc_0027C6E6:
    Arg2 = ((uint32_t)(*(uint32_t *)(v_rip + 0xBB1574))) * ((uint32_t)(v_stack_m40));
    Arg2 = (Arg2) + (*(uint64_t *)(v_stack_m58 + 0x10));
    if (((uint32_t)((int32_t)(Arg3))) < 9) goto loc_0027CAD8;
    Arg1 = (0 * 8 + 59) + ((uint32_t)((uint32_t)(local_rsi)));
    Arg4 = (0) * (Arg1);
    Arg4 = (Arg4) + (Arg2);
loc_0027C71B:
    Arg1 = (*(uint64_t *)(arg2 + 0x28)) & ((uint32_t)((uint32_t)(local_rsi)));
    v_stack_m48 = Arg4;
    result = (*(uint64_t *)(arg2)) >> (20);
    Arg1 = (Arg1) | (result);
    result = ((uint32_t)(*(uint32_t *)(arg2 + 0x24))) & (0xFFFFFFFFFFE00000ULL);
    Arg1 = (Arg1) >> (20);
    result = (result) << (3);
    Arg1 = (Arg1) | (result);
    if (Arg1 == Arg2) goto loc_0027CB78;
    Arg4 = (Arg1 + Arg1 * 2) << (4);
    Arg4 = (Arg4) + (0);
loc_0027C771:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x24))) & (0x1FFFFFULL));
    result = (*(uint64_t *)(arg2 + 0x18)) >> (40);
    Arg3 = (Arg3) << (19);
    result = (uint32_t)((result) & (0x7FFFFULL));
    Arg3 = (Arg3) | (result);
    if (Arg3 == Arg2) goto loc_0027CB3E;
    local_r10 = (Arg3 + Arg3 * 2) << (4);
    local_r10 = (local_r10) + (0);
loc_0027C7A7:
    local_r11 = 0;
loc_0027C7B0:
    if (0 >= 4) goto loc_0027CAC2;
    if ((*(uint8_t *)(arg5 + 0x10 + 0x8)) != 0) goto loc_0027C7C9;
loc_0027C7C0:
    Arg2 = (0) + 1;
    result = (Arg5 + 16) + (24);
    goto loc_0027C7B0;
loc_0027C7C9:
    if (Arg4 != (*(uint64_t *)(result))) goto loc_0027C7C0;
loc_0027C7CE:
    *(uint64_t *)(arg5 + 0x58) = Arg4;
    *(void **)(arg5 + 0x50) = Arg1;
loc_0027C7E0:
    if (0 >= 4) goto loc_0027CAA4;
    if ((*(uint8_t *)(arg5 + 0x10 + 0x8)) != 0) goto loc_0027C7F9;
loc_0027C7F0:
    result = (0) + 1;
    local_rdi = (Arg5 + 16) + (24);
    goto loc_0027C7E0;
loc_0027C7F9:
    if (local_r10 != (*(uint64_t *)(local_rdi))) goto loc_0027C7F0;
loc_0027C7FE:
loc_0027C803:
    return 1;
loc_0027C81E:
loc_0027C826:
loc_0027C82D:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38))) == 0) goto loc_0027CB25;
    result = 1;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x18)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10);
        *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x18) = 0;
    }
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x30)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x28);
        *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x30) = 0;
    }
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x48)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x40);
        *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x48) = 0;
    }
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x60)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x58);
        *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x60) = 0;
    }
    if (((*(uint8_t *)(v_rip + 0xD4A273)) & (1)) != 0) goto loc_0027CB81;
loc_0027C89D:
loc_0027C8A7:
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38)) = 0;
    if ((uint32_t)((uint32_t)(v_stack_p48)) != 0) goto loc_0027C8EB;
    result = 0;
    goto loc_0027C803;
loc_0027C8B5:
    goto loc_0027C4D6;
loc_0027C8BD:
    Arg4 = 0;
    v_stack_m40 = v_stack_m28;
    result = KeBugCheckEx(Arg4 + 26, (uint32_t)(0x5180ULL), *(uint64_t *)(v_stack_m28 + 0x40), Arg4);
loc_0027C8D7:
    if (!sign_flag) goto loc_0027C516;
    result = ExpWaitForSpinLockSharedAndAcquire(Arg4 + 26, 255, *(uint64_t *)(v_stack_m28 + 0x40), Arg4);
    goto loc_0027C500;
loc_0027C8EB:
    if (((*(uint8_t *)(v_rip + 0xD4A214)) & (33)) != 0) goto loc_0027C9A4;
loc_0027C8FC:
    local_r11 = v_stack_m28;
    if (!(condition_is_above_or_equal)) {
        Arg2 = 255;
        Arg1 = v_stack_p30 + 32;
        result = ExpWaitForSpinLockExclusiveAndAcquire(Arg1, Arg2, *(uint64_t *)(v_stack_m28 + 0x40), Arg4);
        local_r11 = (uint32_t)(result);
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p30 + 0x20)))))) == 0x80000000ULL) goto loc_0027C7FE;
loc_0027C924:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p30 + 0x20)))))) >= 0x80000000ULL) {
    }
    local_r11 = (uint32_t)((local_r11) + 1);
    v_stack_p50 = local_r11;
    if (((*(uint32_t *)(v_rip + 0xD48971)) & ((uint32_t)(local_r11))) == 0) goto loc_0027CB4C;
loc_0027C949:
loc_0027C94B:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p30 + 0x20)))))) == 0x80000000ULL) goto loc_0027C7FE;
    goto loc_0027C924;
loc_0027C969:
    if ((*(uint64_t *)(v_stack_m28 + 0x40)) >= 0) goto loc_0027C9E1;
loc_0027C971:
loc_0027C97B:
    goto loc_0027C6D6;
loc_0027C985:
    if (5 < (*(uint64_t *)(0 + 0x10))) goto loc_0027C6A6;
    goto loc_0027C674;
loc_0027C998:
    goto loc_0027C573;
loc_0027C9A4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC914AE))) != 0) goto loc_0027C8FC;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_stack_p30 + 32, 255, *(uint64_t *)(v_stack_m28 + 0x40), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p30 + 0x20)))) + 1);
    goto loc_0027C7FE;
loc_0027C9C1:
    Arg1 = ((uint32_t)((uint32_t)(v_stack_m28))) >> (4);
    Arg1 = (Arg1) * (255);
    result = MiSearchChannelTable(Arg1, 255, *(uint64_t *)(v_stack_m28 + 0x40), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p30 + 0x20)))) + 1);
    goto loc_0027C6E6;
loc_0027C9DA:
    Arg1 = 0;
    goto loc_0027C5CD;
loc_0027C9E1:
    Arg1 = (*(uint64_t *)(v_rip + 0xBB12F8) + *(uint64_t *)(v_rip + 0xBB12F8) * 2) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xBB12F8));
    if ((*(uint64_t *)(v_stack_m28 + 0x40)) >= Arg1) goto loc_0027C97B;
    Arg1 = ((uint32_t)((uint32_t)(v_stack_m28))) >> (4);
    Arg1 = (Arg1) * (255);
    if (Arg1 < (*(uint64_t *)(v_rip + 0xBB91E9))) goto loc_0027CA36;
    result = (*(uint64_t *)(v_rip + 0xBB91E9)) + (0x800ULL);
    if (Arg1 < result) goto loc_0027C97B;
loc_0027CA36:
    result = (uint32_t)((5) >> (16));
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 6) goto loc_0027C6D0;
    if ((*(uint8_t *)(v_rip + 0xBC019A)) == 0) goto loc_0027C97B;
    Arg1 = (Arg1) >> (9);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xBC07E7) + arg1 * 2)) == 0) goto loc_0027C971;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xBC07E7) + arg1 * 2))) != 10) goto loc_0027C6D0;
    goto loc_0027C97B;
loc_0027CA81:
    if ((uint32_t)(Arg1) != 0) goto loc_0027CBD7;
    v_stack_m40 = Arg5;
    result = KeBugCheckEx(26, (uint32_t)(0x5180ULL), 5, *(uint64_t *)(v_rip + 0xBC07E7));
loc_0027CAA4:
    if (condition_is_below) goto loc_0027C81E;
    *(uint64_t *)(v_stack_p30 + 0x20 + 0x40) = v_stack_p30;
    *(uint64_t *)(v_stack_p30 + 0x20 + 0x38) = 5;
    *(uint8_t *)(v_stack_p30 + 0x20 + 0x48) = 1;
    goto loc_0027C7FE;
loc_0027CAC2:
    if (condition_is_below) goto loc_0027C81E;
    *(uint8_t *)(v_stack_p30 + 0x20 + 0x60) = 1;
    goto loc_0027C7CE;
loc_0027CAD8:
    if (((uint32_t)((int32_t)(Arg3))) == 8) goto loc_0027CBAC;
    Arg1 = 0;
loc_0027CAE4:
    v_stack_m8 = 0;
    Arg4 = (*(uint64_t *)(v_rip + 0xBC07E7)) * (5 + 0 * 8);
    Arg1 = (5 + 0 * 8) * ((int32_t)(Arg3));
    Arg4 = (Arg4) + (*(uint64_t *)(arg1 + (uint32_t)(0x5180ULL) * 1 + 0x3D98));
    goto loc_0027C71B;
loc_0027CB09:
    if ((*(uint32_t *)(v_stack_p30 + 0xC)) != 2) goto loc_0027C4E0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(0x5180ULL) + 0x20))) >> (24));
    local_r12 = 0;
    if ((((uint8_t)(result)) & (8)) != 0) { local_r12 = (uint32_t)(Arg1); }
    goto loc_0027C4E0;
loc_0027CB25:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_p30 + 32, (uint32_t)(0x5180ULL), 5, Arg4);
    local_r11 = 0;
    goto loc_0027C8A7;
loc_0027CB3E:
    local_r10 = (v_stack_m20) + (40);
    goto loc_0027C7A7;
loc_0027CB4C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD49F66)))) & (64)) == 0) goto loc_0027C949;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p30 + 32, (uint32_t)(0x5180ULL), 5, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0027C949;
    result = HvlNotifyLongSpinWait((uint32_t)(Arg5), (uint32_t)(0x5180ULL), 5, Arg4);
    goto loc_0027C94B;
loc_0027CB78:
    Arg4 = (Arg4) + (40);
    goto loc_0027C771;
loc_0027CB81:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC912D1))) != 0) goto loc_0027C89D;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented((uint32_t)(Arg5), v_stack_p28, 5, Arg4);
    local_r11 = 0;
    goto loc_0027C8A7;
loc_0027CBAC:
    local_r15 = ((uint32_t)((uint32_t)(v_stack_m28))) >> (4);
    local_r15 = (local_r15) * (result);
    local_r15 = (local_r15) >> (9);
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0xBC067B) + local_r15 * 2 + 0x1)) & (127));
    goto loc_0027CAE4;
loc_0027CBD7:
    goto loc_0027C674;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `32` | `R` |
| `Arg2` | `+ 0x24` | `32` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg5` | `+ 0x0` | `8` | `R` |
| `Arg5` | `+ 0x0` | `8` | `W` |
| `Arg5` | `+ 0x0` | `64` | `R` |
| `Arg5` | `+ 0x0 + rax*1` | `8` | `W` |
| `Arg5` | `+ 0x8` | `8` | `R` |
| `Arg5` | `+ 0x8` | `64` | `W` |
| `Arg5` | `+ 0x10` | `64` | `R` |
| `Arg5` | `+ 0x10` | `64` | `W` |
| `Arg5` | `+ 0x18` | `8` | `R` |
| `Arg5` | `+ 0x18` | `8` | `W` |
| `Arg5` | `+ 0x20` | `64` | `W` |
| `Arg5` | `+ 0x28` | `64` | `R` |
| `Arg5` | `+ 0x28` | `64` | `W` |
| `Arg5` | `+ 0x30` | `8` | `R` |
| `Arg5` | `+ 0x30` | `8` | `W` |
| `Arg5` | `+ 0x38` | `64` | `W` |
| `Arg5` | `+ 0x40` | `64` | `R` |
| `Arg5` | `+ 0x40` | `64` | `W` |
| `Arg5` | `+ 0x48` | `8` | `R` |
| `Arg5` | `+ 0x48` | `8` | `W` |
| `Arg5` | `+ 0x50` | `64` | `W` |
| `Arg5` | `+ 0x58` | `64` | `R` |
| `Arg5` | `+ 0x58` | `64` | `W` |

추가 오프셋 2개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0027C450&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
