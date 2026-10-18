# MiQueryAddressState

- RVA: `0x0032C380`–`0x0032D675` (길이 `4,853` bytes)
- VA: `0x000000014032C380`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000761E8`
- 디코드: `1,124`개 명령, `4,853/4,853` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x0032C48B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0032C4A8` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x0032C4E0` → [MiFastLockLeafPageTable](../27/MiFastLockLeafPageTable_function_00276340.md) (function, `0x00276340`)
- `0x0032C6D6` → [MiGetProtoPteAddress](MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x0032C7D3` → [MiPureAweVad](MiPureAweVad_function_0032B9D0.md) (function, `0x0032B9D0`)
- `0x0032C81B` → [MiGetPageProtection](MiGetPageProtection_function_0032BA10.md) (function, `0x0032BA10`)
- `0x0032CA43` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0032CAA4` → [MI_GET_GRAPHICS_PROTECTION_FROM_VAD](../43/MI_GET_GRAPHICS_PROTECTION_FROM_VAD_function_00438CA0.md) (function, `0x00438CA0`)
- `0x0032CAEA` → [PsReferencePartitionSafe](../3B/PsReferencePartitionSafe_function_003BA6C0.md) (function, `0x003BA6C0`)
- `0x0032CB0C` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x0032CB8C` → [MiPteHasShadow](MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x0032CBE1` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0032CBF7` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x0032CC01` → [MiFaultInPagedPool](../4B/MiFaultInPagedPool_function_004B3BC0.md) (function, `0x004B3BC0`)
- `0x0032CC09` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0032CC63` → [MiVadPureReserve](../2C/MiVadPureReserve_function_002C34C0.md) (function, `0x002C34C0`)
- `0x0032CD2F` → [EtwTraceShouldYieldProcessor](../27/EtwTraceShouldYieldProcessor_function_00279088.md) (function, `0x00279088`)
- `0x0032CE68` → [PsGetProcessSessionIdEx](../22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0032CE75` → [MiGetSharedProtos](../34/MiGetSharedProtos_function_00348D58.md) (function, `0x00348D58`)
- `0x0032CF9F` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0032CFB9` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x0032D10D` → [MiGetAweVadPartition](../2A/MiGetAweVadPartition_function_002A94E8.md) (function, `0x002A94E8`)
- `0x0032D16E` → [MiWalkPageTables](../2C/MiWalkPageTables_function_002C2710.md) (function, `0x002C2710`)
- `0x0032D213` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0032D2AE` → [MiVadPureReserve](../2C/MiVadPureReserve_function_002C34C0.md) (function, `0x002C34C0`)
- `0x0032D2C8` → [MiSkipFractionalPagefileRegion](../47/MiSkipFractionalPagefileRegion_function_00474628.md) (function, `0x00474628`)
- `0x0032D311` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0032D345` → [MiSkipEntirePagefileRegions](../36/MiSkipEntirePagefileRegions_function_00367B70.md) (function, `0x00367B70`)
- `0x0032D3D4` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0032D40F` → [MiGetAnyMultiplexedVm](../44/MiGetAnyMultiplexedVm_function_00448BD0.md) (function, `0x00448BD0`)
- `0x0032D433` → [MiQueryStateMatches](../43/MiQueryStateMatches_function_00439700.md) (function, `0x00439700`)
- `0x0032D454` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0032D549` → [MiGetProtectionFromPte](../2A/MiGetProtectionFromPte_function_002AEE78.md) (function, `0x002AEE78`)
- `0x0032D56C` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0032D593` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x0032D5AF` → [MiIsLazyStampedPte](../22/MiIsLazyStampedPte_function_00227B10.md) (function, `0x00227B10`)
- `0x0032D5CA` → [MiIsLazyStampedPte](../22/MiIsLazyStampedPte_function_00227B10.md) (function, `0x00227B10`)

### Direct callers
- [sub_002C37D9](../2C/Unknown_function_002C37D9.md) at `0x002C3959`
- [MiAllowProtectionChange](../44/MiAllowProtectionChange_function_00448834.md) at `0x004488F7`
- [MiComparePteProtections](../44/MiComparePteProtections_function_0044F4FC.md) at `0x0044F588`
- [MiQueryAddressSpan](../45/MiQueryAddressSpan_function_0045CF14.md) at `0x0045CFD4`
- [MiQueryAddressSpan](../45/MiQueryAddressSpan_function_0045CF14.md) at `0x0045D061`
- [MiObtainRotateProtectionRanges](../4A/MiObtainRotateProtectionRanges_function_004A4768.md) at `0x004A47FA`

### Static image references
- `0x0032C3ED` → RVA `0x00E30088` (`.data`; read)
- `0x0032C8D9` → RVA `0x00E38840` (`.data`; read)
- `0x0032C9DC` → RVA `0x00E2DC80` (`.data`; read)
- `0x0032CD1C` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0032CE28` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0032D155` → RVA `0x00313710` (`MiGetNextPageTableTail`; read)
- `0x0032D3F4` → RVA `0x00E2F380` (`.data`; read)
- `0x0032D3FD` → RVA `0x00E2F390` (`.data`; read)
- `0x0032D4E1` → RVA `0x00E2DCE0` (`.data`; read)
- `0x0032D50D` → RVA `0x00E300C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0032C380  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0032C385  44 88 44 24 18                  mov byte ptr [rsp + 0x18], r8b
0032C38A  55                              push rbp
0032C38B  53                              push rbx
0032C38C  56                              push rsi
0032C38D  57                              push rdi
0032C38E  41 54                           push r12
0032C390  41 55                           push r13
0032C392  41 56                           push r14
0032C394  41 57                           push r15
0032C396  48 8D 6C 24 88                  lea rbp, [rsp - 0x78]
0032C39B  48 81 EC 78 01 00 00            sub rsp, 0x178
0032C3A2  48 8B F9                        mov rdi, rcx
0032C3A5  45 33 C0                        xor r8d, r8d
0032C3A8  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
0032C3AD  4C 8B FF                        mov r15, rdi
0032C3B0  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
0032C3B5  49 B9 F8 FF FF FF 7F 00 00 00   movabs r9, 0x7ffffffff8
0032C3BF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032C3C8  49 C1 EF 09                     shr r15, 9
0032C3CC  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
0032C3D1  4D 23 F9                        and r15, r9
0032C3D4  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
0032C3DB  48 05 00 04 00 00               add rax, 0x400
0032C3E1  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0032C3E6  0F B7 88 AE 00 00 00            movzx ecx, word ptr [rax + 0xae]
0032C3ED  48 8B 05 94 3C B0 00            mov rax, qword ptr [rip + 0xb03c94]
0032C3F4  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0032C3F8  0F B7 01                        movzx eax, word ptr [rcx]
0032C3FB  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
0032C400  66 89 85 C0 00 00 00            mov word ptr [rbp + 0xc0], ax
0032C407  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
0032C411  48 8B C1                        mov rax, rcx
0032C414  4C 03 F8                        add r15, rax
0032C417  48 C1 EA 09                     shr rdx, 9
0032C41B  4C 89 7D A0                     mov qword ptr [rbp - 0x60], r15
0032C41F  49 23 D1                        and rdx, r9
0032C422  48 8B C1                        mov rax, rcx
0032C425  48 03 D0                        add rdx, rax
0032C428  44 89 44 24 78                  mov dword ptr [rsp + 0x78], r8d
0032C42D  B8 00 20 00 00                  mov eax, 0x2000
0032C432  48 89 95 C8 00 00 00            mov qword ptr [rbp + 0xc8], rdx
0032C439  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
0032C43D  44 89 44 24 70                  mov dword ptr [rsp + 0x70], r8d
0032C442  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
0032C447  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
0032C44C  48 8B F1                        mov rsi, rcx
0032C44F  48 C1 E6 19                     shl rsi, 0x19
0032C453  4C 8B EA                        mov r13, rdx
0032C456  49 C1 E5 19                     shl r13, 0x19
0032C45A  4C 2B EE                        sub r13, rsi
0032C45D  48 89 75 88                     mov qword ptr [rbp - 0x78], rsi
0032C461  49 C1 FD 10                     sar r13, 0x10
0032C465  4C 89 6D A8                     mov qword ptr [rbp - 0x58], r13
0032C469  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
0032C46D  48 8D 4D B4                     lea rcx, [rbp - 0x4c]
0032C471  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
0032C476  45 8B F0                        mov r14d, r8d
0032C479  49 8B D8                        mov rbx, r8
0032C47C  0F 57 C0                        xorps xmm0, xmm0
0032C47F  33 D2                           xor edx, edx
0032C481  41 B8 BC 00 00 00               mov r8d, 0xbc
0032C487  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
0032C48B  E8 B0 A7 39 00                  call 0x1406c6c40
0032C490  4D 8B E7                        mov r12, r15
0032C493  C7 45 B0 61 20 00 00            mov dword ptr [rbp - 0x50], 0x2061
0032C49A  49 C1 E4 19                     shl r12, 0x19
0032C49E  4C 2B E6                        sub r12, rsi
0032C4A1  49 C1 FC 10                     sar r12, 0x10
0032C4A5  49 8B CC                        mov rcx, r12
0032C4A8  E8 F3 FB F4 FF                  call 0x14027c0a0
0032C4AD  48 B9 00 00 00 00 00 80 FF FF   movabs rcx, 0xffff800000000000
0032C4B7  48 3B C1                        cmp rax, rcx
0032C4BA  0F 83 34 0F 00 00               jae 0x14032d3f4
0032C4C0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032C4C9  48 8B B0 B8 00 00 00            mov rsi, qword ptr [rax + 0xb8]
0032C4D0  48 81 C6 00 04 00 00            add rsi, 0x400
0032C4D7  45 33 C0                        xor r8d, r8d
0032C4DA  49 8B D4                        mov rdx, r12
0032C4DD  48 8B CE                        mov rcx, rsi
0032C4E0  E8 5B 9E F4 FF                  call 0x140276340
0032C4E5  85 C0                           test eax, eax
0032C4E7  0F 84 42 0C 00 00               je 0x14032d12f
0032C4ED  8D 50 FF                        lea edx, [rax - 1]
0032C4F0  49 C1 EC 09                     shr r12, 9
0032C4F4  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0032C4FE  89 55 90                        mov dword ptr [rbp - 0x70], edx
0032C501  4C 23 E0                        and r12, rax
0032C504  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0032C50E  48 8B C0                        mov rax, rax
0032C511  4C 03 E0                        add r12, rax
0032C514  4C 89 65 98                     mov qword ptr [rbp - 0x68], r12
0032C518  4D 85 E4                        test r12, r12
0032C51B  0F 84 89 08 00 00               je 0x14032cdaa
0032C521  4D 8B EC                        mov r13, r12
0032C524  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
0032C52E  49 C1 ED 09                     shr r13, 9
0032C532  49 B9 F8 FF FF FF 7F 00 00 00   movabs r9, 0x7ffffffff8
0032C53C  4D 23 E9                        and r13, r9
0032C53F  49 8B C0                        mov rax, r8
0032C542  4C 03 E8                        add r13, rax
0032C545  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
0032C54A  85 D2                           test edx, edx
0032C54C  0F 85 15 0E 00 00               jne 0x14032d367
0032C552  4D 3B FC                        cmp r15, r12
0032C555  0F 85 71 0E 00 00               jne 0x14032d3cc
0032C55B  49 8B 1F                        mov rbx, qword ptr [r15]
0032C55E  4D 8D 67 08                     lea r12, [r15 + 8]
0032C562  45 33 D2                        xor r10d, r10d
0032C565  C7 44 24 60 01 00 00 00         mov dword ptr [rsp + 0x60], 1
0032C56D  4D 8B EF                        mov r13, r15
0032C570  45 8B F2                        mov r14d, r10d
0032C573  49 81 E5 00 F0 FF FF            and r13, 0xfffffffffffff000
0032C57A  49 81 C5 F8 0F 00 00            add r13, 0xff8
0032C581  48 85 DB                        test rbx, rbx
0032C584  41 0F 94 C6                     sete r14b
0032C588  4C 3B AD C8 00 00 00            cmp r13, qword ptr [rbp + 0xc8]
0032C58F  4C 0F 47 AD C8 00 00 00         cmova r13, qword ptr [rbp + 0xc8]
0032C597  4C 89 6D 80                     mov qword ptr [rbp - 0x80], r13
0032C59B  E9 A6 00 00 00                  jmp 0x14032c646
0032C5A0  48 8B 95 E0 00 00 00            mov rdx, qword ptr [rbp + 0xe0]
0032C5A7  0F B7 85 C0 00 00 00            movzx eax, word ptr [rbp + 0xc0]
0032C5AE  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
0032C5B2  44 89 44 24 74                  mov dword ptr [rsp + 0x74], r8d
0032C5B7  89 74 24 78                     mov dword ptr [rsp + 0x78], esi
0032C5BB  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
0032C5BF  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
0032C5C4  48 85 D2                        test rdx, rdx
0032C5C7  0F 85 5F 09 00 00               jne 0x14032cf2c
0032C5CD  48 8B 85 E8 00 00 00            mov rax, qword ptr [rbp + 0xe8]
0032C5D4  48 8B 8D F0 00 00 00            mov rcx, qword ptr [rbp + 0xf0]
0032C5DB  89 30                           mov dword ptr [rax], esi
0032C5DD  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
0032C5E1  89 01                           mov dword ptr [rcx], eax
0032C5E3  48 8B 8D F8 00 00 00            mov rcx, qword ptr [rbp + 0xf8]
0032C5EA  0F B7 85 C0 00 00 00            movzx eax, word ptr [rbp + 0xc0]
0032C5F1  66 89 01                        mov word ptr [rcx], ax
0032C5F4  45 85 ED                        test r13d, r13d
0032C5F7  0F 85 1C 03 00 00               jne 0x14032c919
0032C5FD  48 83 7C 24 48 00               cmp qword ptr [rsp + 0x48], 0
0032C603  0F 85 10 03 00 00               jne 0x14032c919
0032C609  49 8D 47 08                     lea rax, [r15 + 8]
0032C60D  4C 8B F8                        mov r15, rax
0032C610  4C 3B E0                        cmp r12, rax
0032C613  0F 85 00 03 00 00               jne 0x14032c919
0032C619  4C 3B 65 80                     cmp r12, qword ptr [rbp - 0x80]
0032C61D  0F 87 F6 02 00 00               ja 0x14032c919
0032C623  83 7C 24 60 00                  cmp dword ptr [rsp + 0x60], 0
0032C628  74 03                           je 0x14032c62d
0032C62A  48 8B 18                        mov rbx, qword ptr [rax]
0032C62D  48 8B F8                        mov rdi, rax
0032C630  49 83 C4 08                     add r12, 8
0032C634  48 C1 E7 19                     shl rdi, 0x19
0032C638  48 2B 7D 88                     sub rdi, qword ptr [rbp - 0x78]
0032C63C  48 C1 FF 10                     sar rdi, 0x10
0032C640  45 33 D2                        xor r10d, r10d
0032C643  45 8B F2                        mov r14d, r10d
0032C646  4C 8B 9D D8 00 00 00            mov r11, qword ptr [rbp + 0xd8]
0032C64D  44 89 54 24 34                  mov dword ptr [rsp + 0x34], r10d
0032C652  41 B8 00 20 00 00               mov r8d, 0x2000
0032C658  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
0032C65D  41 8B F2                        mov esi, r10d
0032C660  45 8B EA                        mov r13d, r10d
0032C663  48 85 DB                        test rbx, rbx
0032C666  0F 85 64 01 00 00               jne 0x14032c7d0
0032C66C  45 8B 43 30                     mov r8d, dword ptr [r11 + 0x30]
0032C670  41 8B C0                        mov eax, r8d
0032C673  83 E0 70                        and eax, 0x70
0032C676  3C 30                           cmp al, 0x30
0032C678  0F 84 8C 0A 00 00               je 0x14032d10a
0032C67E  41 8B C0                        mov eax, r8d
0032C681  24 70                           and al, 0x70
0032C683  3C 10                           cmp al, 0x10
0032C685  0F 84 AB 01 00 00               je 0x14032c836
0032C68B  41 0F BA E0 15                  bt r8d, 0x15
0032C690  0F 82 F0 03 00 00               jb 0x14032ca86
0032C696  49 8B 43 48                     mov rax, qword ptr [r11 + 0x48]
0032C69A  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
0032C69F  48 C1 EF 0C                     shr rdi, 0xc
0032C6A3  41 B8 0C 00 00 00               mov r8d, 0xc
0032C6A9  48 8B D7                        mov rdx, rdi
0032C6AC  48 8B 08                        mov rcx, qword ptr [rax]
0032C6AF  0F B7 41 3C                     movzx eax, word ptr [rcx + 0x3c]
0032C6B3  B9 FF 03 00 00                  mov ecx, 0x3ff
0032C6B8  66 23 C1                        and ax, cx
0032C6BB  0F B7 C8                        movzx ecx, ax
0032C6BE  48 8B 05 C3 39 B0 00            mov rax, qword ptr [rip + 0xb039c3]
0032C6C5  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0032C6C9  0F B7 01                        movzx eax, word ptr [rcx]
0032C6CC  49 8B CB                        mov rcx, r11
0032C6CF  66 89 85 C0 00 00 00            mov word ptr [rbp + 0xc0], ax
0032C6D6  E8 95 22 00 00                  call 0x14032e970
0032C6DB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0032C6E0  48 85 C0                        test rax, rax
0032C6E3  0F 84 3C 05 00 00               je 0x14032cc25
0032C6E9  45 85 F6                        test r14d, r14d
0032C6EC  0F 85 91 07 00 00               jne 0x14032ce83
0032C6F2  44 39 74 24 60                  cmp dword ptr [rsp + 0x60], r14d
0032C6F7  0F 84 44 0B 00 00               je 0x14032d241
0032C6FD  4C 8B 9D D8 00 00 00            mov r11, qword ptr [rbp + 0xd8]
0032C704  45 33 D2                        xor r10d, r10d
0032C707  49 8B 43 78                     mov rax, qword ptr [r11 + 0x78]
0032C70B  48 85 C0                        test rax, rax
0032C70E  0F 88 4A 0D 00 00               js 0x14032d45e
0032C714  45 8B C2                        mov r8d, r10d
0032C717  49 C7 C1 FF FF FF FF            mov r9, 0xffffffffffffffff
0032C71E  48 83 7C 24 38 00               cmp qword ptr [rsp + 0x38], 0
0032C724  0F 84 0C 01 00 00               je 0x14032c836
0032C72A  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0032C72F  8B 40 20                        mov eax, dword ptr [rax + 0x20]
0032C732  41 8B 53 30                     mov edx, dword ptr [r11 + 0x30]
0032C736  8B C2                           mov eax, edx
0032C738  24 70                           and al, 0x70
0032C73A  3C 20                           cmp al, 0x20
0032C73C  0F 85 2B 08 00 00               jne 0x14032cf6d
0032C742  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0032C746  49 8B D2                        mov rdx, r10
0032C749  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0032C74E  48 85 FF                        test rdi, rdi
0032C751  74 35                           je 0x14032c788
0032C753  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
0032C756  0F BA E0 11                     bt eax, 0x11
0032C75A  0F 82 E7 06 00 00               jb 0x14032ce47
0032C760  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
0032C764  48 3B F2                        cmp rsi, rdx
0032C767  72 0C                           jb 0x14032c775
0032C769  8B 47 2C                        mov eax, dword ptr [rdi + 0x2c]
0032C76C  48 8D 0C C2                     lea rcx, [rdx + rax*8]
0032C770  48 3B F1                        cmp rsi, rcx
0032C773  72 09                           jb 0x14032c77e
0032C775  48 8B 7F 10                     mov rdi, qword ptr [rdi + 0x10]
0032C779  48 85 FF                        test rdi, rdi
0032C77C  75 D5                           jne 0x14032c753
0032C77E  4C 8B 9D D8 00 00 00            mov r11, qword ptr [rbp + 0xd8]
0032C785  45 33 D2                        xor r10d, r10d
0032C788  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
0032C78B  48 2B F2                        sub rsi, rdx
0032C78E  8B 47 2C                        mov eax, dword ptr [rdi + 0x2c]
0032C791  81 E1 FF FF FF 3F               and ecx, 0x3fffffff
0032C797  2B C1                           sub eax, ecx
0032C799  48 C1 FE 03                     sar rsi, 3
0032C79D  8B C8                           mov ecx, eax
0032C79F  48 3B F1                        cmp rsi, rcx
0032C7A2  0F 83 5A 06 00 00               jae 0x14032ce02
0032C7A8  41 8B 73 30                     mov esi, dword ptr [r11 + 0x30]
0032C7AC  C1 EE 07                        shr esi, 7
0032C7AF  83 E6 1F                        and esi, 0x1f
0032C7B2  83 FE 07                        cmp esi, 7
0032C7B5  75 08                           jne 0x14032c7bf
0032C7B7  8B 77 20                        mov esi, dword ptr [rdi + 0x20]
0032C7BA  D1 EE                           shr esi, 1
0032C7BC  83 E6 1F                        and esi, 0x1f
0032C7BF  85 F6                           test esi, esi
0032C7C1  74 73                           je 0x14032c836
0032C7C3  41 B8 00 10 00 00               mov r8d, 0x1000
0032C7C9  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
0032C7CE  EB 6B                           jmp 0x14032c83b
0032C7D0  49 8B CB                        mov rcx, r11
0032C7D3  E8 F8 F1 FF FF                  call 0x14032b9d0
0032C7D8  85 C0                           test eax, eax
0032C7DA  0F 85 E7 0D 00 00               jne 0x14032d5c7
0032C7E0  48 8B C3                        mov rax, rbx
0032C7E3  25 E0 03 00 00                  and eax, 0x3e0
0032C7E8  48 3D 00 02 00 00               cmp rax, 0x200
0032C7EE  0F 84 D4 01 00 00               je 0x14032c9c8
0032C7F4  48 8D 85 C0 00 00 00            lea rax, [rbp + 0xc0]
0032C7FB  41 BE 00 10 00 00               mov r14d, 0x1000
0032C801  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
0032C806  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
0032C80B  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
0032C810  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0032C815  49 8B D7                        mov rdx, r15
0032C818  49 8B CB                        mov rcx, r11
0032C81B  E8 F0 F1 FF FF                  call 0x14032ba10
0032C820  48 83 7C 24 38 00               cmp qword ptr [rsp + 0x38], 0
0032C826  8B F0                           mov esi, eax
0032C828  0F 85 A6 03 00 00               jne 0x14032cbd4
0032C82E  85 C0                           test eax, eax
0032C830  0F 84 49 09 00 00               je 0x14032d17f
0032C836  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
0032C83B  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
0032C83F  4C 3B F9                        cmp r15, rcx
0032C842  0F 84 58 FD FF FF               je 0x14032c5a0
0032C848  8B 54 24 74                     mov edx, dword ptr [rsp + 0x74]
0032C84C  44 3B C2                        cmp r8d, edx
0032C84F  0F 85 C2 01 00 00               jne 0x14032ca17
0032C855  0F B7 44 24 40                  movzx eax, word ptr [rsp + 0x40]
0032C85A  66 39 85 C0 00 00 00            cmp word ptr [rbp + 0xc0], ax
0032C861  0F 85 B0 01 00 00               jne 0x14032ca17
0032C867  3B 74 24 78                     cmp esi, dword ptr [rsp + 0x78]
0032C86B  0F 85 A6 01 00 00               jne 0x14032ca17
0032C871  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
0032C875  39 44 24 34                     cmp dword ptr [rsp + 0x34], eax
0032C879  0F 85 98 01 00 00               jne 0x14032ca17
0032C87F  48 83 7C 24 48 00               cmp qword ptr [rsp + 0x48], 0
0032C885  0F 85 69 FD FF FF               jne 0x14032c5f4
0032C88B  45 85 ED                        test r13d, r13d
0032C88E  0F 85 85 00 00 00               jne 0x14032c919
0032C894  49 8B C7                        mov rax, r15
0032C897  48 2B C1                        sub rax, rcx
0032C89A  48 83 E0 F8                     and rax, 0xfffffffffffffff8
0032C89E  48 3D 00 01 00 00               cmp rax, 0x100
0032C8A4  0F 8C 5F FD FF FF               jl 0x14032c609
0032C8AA  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
0032C8AF  4D 85 C0                        test r8, r8
0032C8B2  75 6F                           jne 0x14032c923
0032C8B4  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032C8B9  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
0032C8BF  24 0F                           and al, 0xf
0032C8C1  3C 05                           cmp al, 5
0032C8C3  0F 87 B0 03 00 00               ja 0x14032cc79
0032C8C9  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
0032C8CF  24 0F                           and al, 0xf
0032C8D1  3C 01                           cmp al, 1
0032C8D3  0F 85 82 0A 00 00               jne 0x14032d35b
0032C8D9  48 8D 0D 60 BF B0 00            lea rcx, [rip + 0xb0bf60]
0032C8E0  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0032C8E9  48 8B 09                        mov rcx, qword ptr [rcx]
0032C8EC  48 8B 90 38 88 00 00            mov rdx, qword ptr [rax + 0x8838]
0032C8F3  48 85 D2                        test rdx, rdx
0032C8F6  0F 84 14 01 00 00               je 0x14032ca10
0032C8FC  8B 82 44 01 00 00               mov eax, dword ptr [rdx + 0x144]
0032C902  8B C0                           mov eax, eax
0032C904  48 C1 E0 06                     shl rax, 6
0032C908  8B 04 01                        mov eax, dword ptr [rcx + rax]
0032C90B  0F BA E0 1E                     bt eax, 0x1e
0032C90F  0F 83 64 03 00 00               jae 0x14032cc79
0032C915  4D 8D 67 08                     lea r12, [r15 + 8]
0032C919  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
0032C91E  E9 0E 01 00 00                  jmp 0x14032ca31
0032C923  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
0032C92D  48 8B C0                        mov rax, rax
0032C930  4C 3B C0                        cmp r8, rax
0032C933  0F 84 98 04 00 00               je 0x14032cdd1
0032C939  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0032C93E  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
0032C944  A8 0F                           test al, 0xf
0032C946  0F 84 CA 01 00 00               je 0x14032cb16
0032C94C  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
0032C952  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
0032C95C  A8 0F                           test al, 0xf
0032C95E  74 1E                           je 0x14032c97e
0032C960  48 8B C1                        mov rax, rcx
0032C963  4C 3B C0                        cmp r8, rax
0032C966  72 16                           jb 0x14032c97e
0032C968  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0032C972  48 8B C0                        mov rax, rax
0032C975  4C 3B C0                        cmp r8, rax
0032C978  0F 86 8C 04 00 00               jbe 0x14032ce0a
0032C97E  49 8B 10                        mov rdx, qword ptr [r8]
0032C981  48 8B C1                        mov rax, rcx
0032C984  4C 3B C0                        cmp r8, rax
0032C987  72 2B                           jb 0x14032c9b4
0032C989  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
0032C993  48 8B C0                        mov rax, rax
0032C996  4C 3B C0                        cmp r8, rax
0032C999  77 19                           ja 0x14032c9b4
0032C99B  F6 C2 01                        test dl, 1
0032C99E  74 14                           je 0x14032c9b4
0032C9A0  F6 C2 42                        test dl, 0x42
0032C9A3  0F 95 C1                        setne cl
0032C9A6  F6 C2 20                        test dl, 0x20
0032C9A9  0F 95 C0                        setne al
0032C9AC  84 C8                           test al, cl
0032C9AE  0F 84 D8 01 00 00               je 0x14032cb8c
0032C9B4  48 C1 EA 3C                     shr rdx, 0x3c
0032C9B8  83 E2 02                        and edx, 2
0032C9BB  85 D2                           test edx, edx
0032C9BD  0F 84 F1 FE FF FF               je 0x14032c8b4
0032C9C3  E9 4D FF FF FF                  jmp 0x14032c915
0032C9C8  F6 C3 01                        test bl, 1
0032C9CB  0F 85 23 FE FF FF               jne 0x14032c7f4
0032C9D1  48 0F BA E3 0A                  bt rbx, 0xa
0032C9D6  0F 83 5F FE FF FF               jae 0x14032c83b
0032C9DC  48 8B 0D 9D 12 B0 00            mov rcx, qword ptr [rip + 0xb0129d]
0032C9E3  48 8B C3                        mov rax, rbx
0032C9E6  48 85 C9                        test rcx, rcx
0032C9E9  74 0E                           je 0x14032c9f9
0032C9EB  F6 C3 10                        test bl, 0x10
0032C9EE  75 09                           jne 0x14032c9f9
0032C9F0  48 8B C1                        mov rax, rcx
0032C9F3  48 F7 D0                        not rax
0032C9F6  48 23 C3                        and rax, rbx
0032C9F9  48 C1 E8 20                     shr rax, 0x20
0032C9FD  B9 FF FF FF FF                  mov ecx, 0xffffffff
0032CA02  48 3B C1                        cmp rax, rcx
0032CA05  0F 85 E9 FD FF FF               jne 0x14032c7f4
0032CA0B  E9 2B FE FF FF                  jmp 0x14032c83b
0032CA10  33 C0                           xor eax, eax
0032CA12  E9 EB FE FF FF                  jmp 0x14032c902
0032CA17  0F B7 4C 24 40                  movzx ecx, word ptr [rsp + 0x40]
0032CA1C  44 8B F2                        mov r14d, edx
0032CA1F  66 89 8D C0 00 00 00            mov word ptr [rbp + 0xc0], cx
0032CA26  4D 8B E7                        mov r12, r15
0032CA29  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
0032CA2D  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
0032CA31  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0032CA36  48 85 C0                        test rax, rax
0032CA39  74 0D                           je 0x14032ca48
0032CA3B  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032CA40  48 8B D0                        mov rdx, rax
0032CA43  E8 78 A4 EE FF                  call 0x140216ec0
0032CA48  49 C1 E4 19                     shl r12, 0x19
0032CA4C  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0032CA56  48 8B C8                        mov rcx, rax
0032CA59  48 C1 E1 19                     shl rcx, 0x19
0032CA5D  41 8B C6                        mov eax, r14d
0032CA60  4C 2B E1                        sub r12, rcx
0032CA63  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
0032CA6A  49 C1 FC 10                     sar r12, 0x10
0032CA6E  4C 89 21                        mov qword ptr [rcx], r12
0032CA71  48 81 C4 78 01 00 00            add rsp, 0x178
0032CA78  41 5F                           pop r15
0032CA7A  41 5E                           pop r14
0032CA7C  41 5D                           pop r13
0032CA7E  41 5C                           pop r12
0032CA80  5F                              pop rdi
0032CA81  5E                              pop rsi
0032CA82  5B                              pop rbx
0032CA83  5D                              pop rbp
0032CA84  C3                              ret
0032CA85  CC                              int3
0032CA86  41 0F BA E0 19                  bt r8d, 0x19
0032CA8B  73 20                           jae 0x14032caad
0032CA8D  41 8B F0                        mov esi, r8d
0032CA90  41 BE 00 10 00 00               mov r14d, 0x1000
0032CA96  C1 EE 07                        shr esi, 7
0032CA99  49 8B CB                        mov rcx, r11
0032CA9C  83 E6 1F                        and esi, 0x1f
0032CA9F  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
0032CAA4  E8 F7 C1 10 00                  call 0x140438ca0
0032CAA9  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0032CAAD  41 81 E0 00 00 A0 00            and r8d, 0xa00000
0032CAB4  41 81 F8 00 00 A0 00            cmp r8d, 0xa00000
0032CABB  0F 85 75 FD FF FF               jne 0x14032c836
0032CAC1  49 8B 4B 38                     mov rcx, qword ptr [r11 + 0x38]
0032CAC5  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0032CAC9  0F 84 67 FD FF FF               je 0x14032c836
0032CACF  8B 41 50                        mov eax, dword ptr [rcx + 0x50]
0032CAD2  A8 10                           test al, 0x10
0032CAD4  0F 84 99 09 00 00               je 0x14032d473
0032CADA  4C 8B 41 18                     mov r8, qword ptr [rcx + 0x18]
0032CADE  4D 85 C0                        test r8, r8
0032CAE1  0F 84 4F FD FF FF               je 0x14032c836
0032CAE7  49 8B C8                        mov rcx, r8
0032CAEA  E8 D1 DB 08 00                  call 0x1403ba6c0
0032CAEF  84 C0                           test al, al
0032CAF1  0F 84 3F FD FF FF               je 0x14032c836
0032CAF7  49 8B 00                        mov rax, qword ptr [r8]
0032CAFA  49 8B C8                        mov rcx, r8
0032CAFD  0F B7 10                        movzx edx, word ptr [rax]
0032CB00  66 89 95 C0 00 00 00            mov word ptr [rbp + 0xc0], dx
0032CB07  BA 4D 6D 51 75                  mov edx, 0x75516d4d
0032CB0C  E8 5F 63 01 00                  call 0x140342e70
0032CB11  E9 20 FD FF FF                  jmp 0x14032c836
0032CB16  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
0032CB20  48 8B C0                        mov rax, rax
0032CB23  4C 3B C0                        cmp r8, rax
0032CB26  0F 82 20 FE FF FF               jb 0x14032c94c
0032CB2C  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0032CB36  48 8B C0                        mov rax, rax
0032CB39  4C 3B C0                        cmp r8, rax
0032CB3C  0F 87 0A FE FF FF               ja 0x14032c94c
0032CB42  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032CB4B  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0032CB52  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
0032CB59  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
0032CB60  48 85 C9                        test rcx, rcx
0032CB63  0F 84 E3 FD FF FF               je 0x14032c94c
0032CB69  41 8B C0                        mov eax, r8d
0032CB6C  C1 E8 03                        shr eax, 3
0032CB6F  25 FF 01 00 00                  and eax, 0x1ff
0032CB74  8B 0C 81                        mov ecx, dword ptr [rcx + rax*4]
0032CB77  33 C0                           xor eax, eax
0032CB79  8B D0                           mov edx, eax
0032CB7B  0F BA E1 1E                     bt ecx, 0x1e
0032CB7F  B8 01 00 00 00                  mov eax, 1
0032CB84  0F 42 D0                        cmovb edx, eax
0032CB87  E9 2F FE FF FF                  jmp 0x14032c9bb
0032CB8C  E8 07 EE FF FF                  call 0x14032b998
0032CB91  48 85 C0                        test rax, rax
0032CB94  0F 84 1A FE FF FF               je 0x14032c9b4
0032CB9A  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
0032CBA1  48 85 C9                        test rcx, rcx
0032CBA4  0F 84 0A FE FF FF               je 0x14032c9b4
0032CBAA  49 8B C0                        mov rax, r8
0032CBAD  48 C1 E8 03                     shr rax, 3
0032CBB1  25 FF 01 00 00                  and eax, 0x1ff
0032CBB6  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0032CBBA  A8 20                           test al, 0x20
0032CBBC  74 04                           je 0x14032cbc2
0032CBBE  48 83 CA 20                     or rdx, 0x20
0032CBC2  48 8B CA                        mov rcx, rdx
0032CBC5  48 83 CA 42                     or rdx, 0x42
0032CBC9  A8 42                           test al, 0x42
0032CBCB  48 0F 44 D1                     cmove rdx, rcx
0032CBCF  E9 E0 FD FF FF                  jmp 0x14032c9b4
0032CBD4  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0032CBD9  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0032CBDE  48 8B CB                        mov rcx, rbx
0032CBE1  E8 DA A2 EE FF                  call 0x140216ec0
0032CBE6  0F B6 95 D0 00 00 00            movzx edx, byte ptr [rbp + 0xd0]
0032CBED  33 C0                           xor eax, eax
0032CBEF  48 8B CB                        mov rcx, rbx
0032CBF2  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0032CBF7  E8 94 0A F5 FF                  call 0x14027d690
0032CBFC  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0032CC01  E8 BA 6F 18 00                  call 0x1404b3bc0
0032CC06  48 8B CB                        mov rcx, rbx
0032CC09  E8 E2 FF F4 FF                  call 0x14027cbf0
0032CC0E  48 8B 95 C8 00 00 00            mov rdx, qword ptr [rbp + 0xc8]
0032CC15  45 33 C0                        xor r8d, r8d
0032CC18  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0032CC1C  4C 8B 6D A8                     mov r13, qword ptr [rbp - 0x58]
0032CC20  E9 44 F8 FF FF                  jmp 0x14032c469
0032CC25  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
0032CC2C  48 85 C0                        test rax, rax
0032CC2F  74 28                           je 0x14032cc59
0032CC31  81 78 20 00 20 00 00            cmp dword ptr [rax + 0x20], 0x2000
0032CC38  0F 85 E3 04 00 00               jne 0x14032d121
0032CC3E  83 78 24 00                     cmp dword ptr [rax + 0x24], 0
0032CC42  0F 85 D9 04 00 00               jne 0x14032d121
0032CC48  0F B7 40 14                     movzx eax, word ptr [rax + 0x14]
0032CC4C  66 39 85 C0 00 00 00            cmp word ptr [rbp + 0xc0], ax
0032CC53  0F 85 C8 04 00 00               jne 0x14032d121
0032CC59  4C 8B 95 D8 00 00 00            mov r10, qword ptr [rbp + 0xd8]
0032CC60  49 8B CA                        mov rcx, r10
0032CC63  E8 58 68 F9 FF                  call 0x1402c34c0
0032CC68  85 C0                           test eax, eax
0032CC6A  0F 85 AB 06 00 00               jne 0x14032d31b
0032CC70  4D 8D 67 08                     lea r12, [r15 + 8]
0032CC74  E9 BD FB FF FF                  jmp 0x14032c836
0032CC79  80 BD D0 00 00 00 02            cmp byte ptr [rbp + 0xd0], 2
0032CC80  0F 83 83 F9 FF FF               jae 0x14032c609
0032CC86  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0032CC8F  33 FF                           xor edi, edi
0032CC91  44 8B C7                        mov r8d, edi
0032CC94  44 8B CF                        mov r9d, edi
0032CC97  8B 91 BC 38 00 00               mov edx, dword ptr [rcx + 0x38bc]
0032CC9D  8B B1 AC 83 00 00               mov esi, dword ptr [rcx + 0x83ac]
0032CCA3  44 8B B1 5C 86 00 00            mov r14d, dword ptr [rcx + 0x865c]
0032CCAA  F6 C2 01                        test dl, 1
0032CCAD  75 49                           jne 0x14032ccf8
0032CCAF  40 38 79 20                     cmp byte ptr [rcx + 0x20], dil
0032CCB3  0F 85 95 00 00 00               jne 0x14032cd4e
0032CCB9  F6 C2 1E                        test dl, 0x1e
0032CCBC  75 59                           jne 0x14032cd17
0032CCBE  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
0032CCC5  84 C0                           test al, al
0032CCC7  0F 85 A1 00 00 00               jne 0x14032cd6e
0032CCCD  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
0032CCD1  48 85 C0                        test rax, rax
0032CCD4  75 6B                           jne 0x14032cd41
0032CCD6  83 FE 07                        cmp esi, 7
0032CCD9  0F 86 2A F9 FF FF               jbe 0x14032c609
0032CCDF  45 85 C0                        test r8d, r8d
0032CCE2  0F 84 8D 00 00 00               je 0x14032cd75
0032CCE8  F6 C2 1E                        test dl, 0x1e
0032CCEB  0F 84 CC 00 00 00               je 0x14032cdbd
0032CCF1  BF 05 00 00 00                  mov edi, 5
0032CCF6  EB 24                           jmp 0x14032cd1c
0032CCF8  41 BA 01 00 00 00               mov r10d, 1
0032CCFE  45 8B C2                        mov r8d, r10d
0032CD01  41 83 FE 07                     cmp r14d, 7
0032CD05  76 CF                           jbe 0x14032ccd6
0032CD07  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
0032CD0E  84 C0                           test al, al
0032CD10  74 D6                           je 0x14032cce8
0032CD12  41 8B FA                        mov edi, r10d
0032CD15  EB 05                           jmp 0x14032cd1c
0032CD17  BF 02 00 00 00                  mov edi, 2
0032CD1C  F7 05 DE 9D C9 00 00 00 00 04   test dword ptr [rip + 0xc99dde], 0x4000000
0032CD26  74 0C                           je 0x14032cd34
0032CD28  45 8B C6                        mov r8d, r14d
0032CD2B  8B D6                           mov edx, esi
0032CD2D  8B CF                           mov ecx, edi
0032CD2F  E8 54 C3 F4 FF                  call 0x140279088
0032CD34  85 FF                           test edi, edi
0032CD36  0F 85 D9 FB FF FF               jne 0x14032c915
0032CD3C  E9 C8 F8 FF FF                  jmp 0x14032c609
0032CD41  48 3B 41 08                     cmp rax, qword ptr [rcx + 8]
0032CD45  74 8F                           je 0x14032ccd6
0032CD47  BF 04 00 00 00                  mov edi, 4
0032CD4C  EB CE                           jmp 0x14032cd1c
0032CD4E  41 B9 01 00 00 00               mov r9d, 1
0032CD54  83 FE 07                        cmp esi, 7
0032CD57  0F 86 AC F8 FF FF               jbe 0x14032c609
0032CD5D  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
0032CD64  84 C0                           test al, al
0032CD66  74 80                           je 0x14032cce8
0032CD68  41 8D 79 06                     lea edi, [r9 + 6]
0032CD6C  EB AE                           jmp 0x14032cd1c
0032CD6E  BF 03 00 00 00                  mov edi, 3
0032CD73  EB A7                           jmp 0x14032cd1c
0032CD75  45 85 C9                        test r9d, r9d
0032CD78  0F 85 6A FF FF FF               jne 0x14032cce8
0032CD7E  FA                              cli
0032CD7F  89 B9 AC 83 00 00               mov dword ptr [rcx + 0x83ac], edi
0032CD85  89 B9 5C 86 00 00               mov dword ptr [rcx + 0x865c], edi
0032CD8B  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0032CD94  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0032CD9B  4D 85 C0                        test r8, r8
0032CD9E  0F 85 4F 05 00 00               jne 0x14032d2f3
0032CDA4  FB                              sti
0032CDA5  E9 72 FF FF FF                  jmp 0x14032cd1c
0032CDAA  4C 8B A5 C8 00 00 00            mov r12, qword ptr [rbp + 0xc8]
0032CDB1  49 83 C4 08                     add r12, 8
0032CDB5  45 33 D2                        xor r10d, r10d
0032CDB8  E9 89 F8 FF FF                  jmp 0x14032c646
0032CDBD  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0032CDC1  48 39 41 08                     cmp qword ptr [rcx + 8], rax
0032CDC5  74 B7                           je 0x14032cd7e
0032CDC7  BF 06 00 00 00                  mov edi, 6
0032CDCC  E9 4B FF FF FF                  jmp 0x14032cd1c
0032CDD1  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0032CDD6  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0032CDDF  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
0032CDE5  24 0F                           and al, 0xf
0032CDE7  0F 85 01 03 00 00               jne 0x14032d0ee
0032CDED  B9 30 00 00 00                  mov ecx, 0x30
0032CDF2  48 8B 84 0A 40 9C 00 00         mov rax, qword ptr [rdx + rcx + 0x9c40]
0032CDFA  48 85 C0                        test rax, rax
0032CDFD  E9 BB FB FF FF                  jmp 0x14032c9bd
0032CE02  41 8B F2                        mov esi, r10d
0032CE05  E9 2C FA FF FF                  jmp 0x14032c836
0032CE0A  48 8B C1                        mov rax, rcx
0032CE0D  49 8B C8                        mov rcx, r8
0032CE10  48 2B C8                        sub rcx, rax
0032CE13  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
0032CE19  48 C1 F9 03                     sar rcx, 3
0032CE1D  03 C9                           add ecx, ecx
0032CE1F  8B C1                           mov eax, ecx
0032CE21  44 8B C1                        mov r8d, ecx
0032CE24  48 C1 E8 05                     shr rax, 5
0032CE28  48 8D 0D D1 31 CD FF            lea rcx, [rip - 0x32ce2f]
0032CE2F  41 83 E0 1F                     and r8d, 0x1f
0032CE33  8B 94 81 AC F1 E2 00            mov edx, dword ptr [rcx + rax*4 + 0xe2f1ac]
0032CE3A  41 8B C8                        mov ecx, r8d
0032CE3D  D3 EA                           shr edx, cl
0032CE3F  F6 C2 02                        test dl, 2
0032CE42  E9 76 FB FF FF                  jmp 0x14032c9bd
0032CE47  4C 8B 37                        mov r14, qword ptr [rdi]
0032CE4A  41 F7 46 38 00 00 00 08         test dword ptr [r14 + 0x38], 0x8000000
0032CE52  0F 84 08 F9 FF FF               je 0x14032c760
0032CE58  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032CE61  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0032CE68  E8 83 2A F0 FF                  call 0x14022f8f0
0032CE6D  4C 8B C7                        mov r8, rdi
0032CE70  8B D0                           mov edx, eax
0032CE72  49 8B CE                        mov rcx, r14
0032CE75  E8 DE BE 01 00                  call 0x140348d58
0032CE7A  48 8B 50 48                     mov rdx, qword ptr [rax + 0x48]
0032CE7E  E9 E1 F8 FF FF                  jmp 0x14032c764
0032CE83  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
0032CE88  B8 20 00 00 00                  mov eax, 0x20
0032CE8D  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
0032CE91  4D 2B C7                        sub r8, r15
0032CE94  49 C1 F8 03                     sar r8, 3
0032CE98  8B 4A 2C                        mov ecx, dword ptr [rdx + 0x2c]
0032CE9B  49 FF C0                        inc r8
0032CE9E  49 83 F8 20                     cmp r8, 0x20
0032CEA2  4C 0F 4F C0                     cmovg r8, rax
0032CEA6  8B 42 34                        mov eax, dword ptr [rdx + 0x34]
0032CEA9  25 FF FF FF 3F                  and eax, 0x3fffffff
0032CEAE  48 2B C8                        sub rcx, rax
0032CEB1  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0032CEB5  4C 8D 14 C8                     lea r10, [rax + rcx*8]
0032CEB9  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
0032CEBC  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0032CEC1  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
0032CEC6  0F BA E0 11                     bt eax, 0x11
0032CECA  72 20                           jb 0x14032ceec
0032CECC  4D 3B CA                        cmp r9, r10
0032CECF  73 1B                           jae 0x14032ceec
0032CED1  4C 3B 4A 08                     cmp r9, qword ptr [rdx + 8]
0032CED5  72 15                           jb 0x14032ceec
0032CED7  4B 8D 04 C1                     lea rax, [r9 + r8*8]
0032CEDB  49 3B C2                        cmp rax, r10
0032CEDE  76 0F                           jbe 0x14032ceef
0032CEE0  4D 8B C2                        mov r8, r10
0032CEE3  4D 2B C1                        sub r8, r9
0032CEE6  49 C1 F8 03                     sar r8, 3
0032CEEA  EB 03                           jmp 0x14032ceef
0032CEEC  45 33 C0                        xor r8d, r8d
0032CEEF  49 8D 48 FF                     lea rcx, [r8 - 1]
0032CEF3  49 8D 0C CF                     lea rcx, [r15 + rcx*8]
0032CEF7  4D 8D 67 08                     lea r12, [r15 + 8]
0032CEFB  4C 3B E1                        cmp r12, rcx
0032CEFE  77 1C                           ja 0x14032cf1c
0032CF00  49 8B 04 24                     mov rax, qword ptr [r12]
0032CF04  48 85 C0                        test rax, rax
0032CF07  75 09                           jne 0x14032cf12
0032CF09  49 83 C4 08                     add r12, 8
0032CF0D  4C 3B E1                        cmp r12, rcx
0032CF10  76 EE                           jbe 0x14032cf00
0032CF12  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0032CF17  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
0032CF1C  83 7C 24 60 00                  cmp dword ptr [rsp + 0x60], 0
0032CF21  0F 85 D6 F7 FF FF               jne 0x14032c6fd
0032CF27  E9 78 03 00 00                  jmp 0x14032d2a4
0032CF2C  44 3B 42 20                     cmp r8d, dword ptr [rdx + 0x20]
0032CF30  75 2D                           jne 0x14032cf5f
0032CF32  85 F6                           test esi, esi
0032CF34  0F 84 B7 02 00 00               je 0x14032d1f1
0032CF3A  8B C6                           mov eax, esi
0032CF3C  4C 8D 05 BD 30 CD FF            lea r8, [rip - 0x32cf43]
0032CF43  41 0B 8C 80 30 46 01 00         or ecx, dword ptr [r8 + rax*4 + 0x14630]
0032CF4B  0F B7 44 24 40                  movzx eax, word ptr [rsp + 0x40]
0032CF50  3B 4A 24                        cmp ecx, dword ptr [rdx + 0x24]
0032CF53  75 0A                           jne 0x14032cf5f
0032CF55  66 3B 42 14                     cmp ax, word ptr [rdx + 0x14]
0032CF59  0F 84 6E F6 FF FF               je 0x14032c5cd
0032CF5F  41 BD 01 00 00 00               mov r13d, 1
0032CF65  4D 8B E7                        mov r12, r15
0032CF68  E9 60 F6 FF FF                  jmp 0x14032c5cd
0032CF6D  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
0032CF72  49 8B 06                        mov rax, qword ptr [r14]
0032CF75  48 83 78 40 00                  cmp qword ptr [rax + 0x40], 0
0032CF7A  0F 85 0F 02 00 00               jne 0x14032d18f
0032CF80  F7 40 38 00 20 00 00            test dword ptr [rax + 0x38], 0x2000
0032CF87  0F 85 02 02 00 00               jne 0x14032d18f
0032CF8D  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0032CF92  48 85 C0                        test rax, rax
0032CF95  74 16                           je 0x14032cfad
0032CF97  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032CF9C  48 8B D0                        mov rdx, rax
0032CF9F  E8 1C 9F EE FF                  call 0x140216ec0
0032CFA4  48 C7 44 24 50 00 00 00 00      mov qword ptr [rsp + 0x50], 0
0032CFAD  0F B6 95 D0 00 00 00            movzx edx, byte ptr [rbp + 0xd0]
0032CFB4  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032CFB9  E8 D2 06 F5 FF                  call 0x14027d690
0032CFBE  41 8B 46 34                     mov eax, dword ptr [r14 + 0x34]
0032CFC2  4D 2B E7                        sub r12, r15
0032CFC5  41 8B 4E 2C                     mov ecx, dword ptr [r14 + 0x2c]
0032CFC9  25 FF FF FF 3F                  and eax, 0x3fffffff
0032CFCE  48 2B C8                        sub rcx, rax
0032CFD1  49 C1 FC 03                     sar r12, 3
0032CFD5  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0032CFD9  48 8D 3C C8                     lea rdi, [rax + rcx*8]
0032CFDD  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0032CFE2  48 2B F8                        sub rdi, rax
0032CFE5  48 C1 FF 03                     sar rdi, 3
0032CFE9  49 3B FC                        cmp rdi, r12
0032CFEC  48 8B 00                        mov rax, qword ptr [rax]
0032CFEF  49 0F 47 FC                     cmova rdi, r12
0032CFF3  48 85 C0                        test rax, rax
0032CFF6  0F 84 25 06 00 00               je 0x14032d621
0032CFFC  4C 8B 95 D8 00 00 00            mov r10, qword ptr [rbp + 0xd8]
0032D003  41 BE 00 10 00 00               mov r14d, 0x1000
0032D009  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
0032D00E  41 8B 72 30                     mov esi, dword ptr [r10 + 0x30]
0032D012  C1 EE 07                        shr esi, 7
0032D015  83 E6 1F                        and esi, 0x1f
0032D018  48 8B 8D E0 00 00 00            mov rcx, qword ptr [rbp + 0xe0]
0032D01F  48 85 C9                        test rcx, rcx
0032D022  0F 85 F4 03 00 00               jne 0x14032d41c
0032D028  48 85 FF                        test rdi, rdi
0032D02B  0F 84 D4 01 00 00               je 0x14032d205
0032D031  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0032D036  48 8B 00                        mov rax, qword ptr [rax]
0032D039  48 85 C0                        test rax, rax
0032D03C  0F 84 DB 01 00 00               je 0x14032d21d
0032D042  41 81 FE 00 10 00 00            cmp r14d, 0x1000
0032D049  0F 85 B6 01 00 00               jne 0x14032d205
0032D04F  48 FF 44 24 48                  inc qword ptr [rsp + 0x48]
0032D054  48 FF CF                        dec rdi
0032D057  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0032D05C  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
0032D061  48 83 C0 08                     add rax, 8
0032D065  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0032D06A  48 8B C8                        mov rcx, rax
0032D06D  48 85 FF                        test rdi, rdi
0032D070  0F 84 8F 01 00 00               je 0x14032d205
0032D076  48 A9 FF 0F 00 00               test rax, 0xfff
0032D07C  75 B3                           jne 0x14032d031
0032D07E  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0032D088  48 C1 E9 09                     shr rcx, 9
0032D08C  48 23 C8                        and rcx, rax
0032D08F  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0032D099  48 8B C0                        mov rax, rax
0032D09C  48 8B 04 01                     mov rax, qword ptr [rcx + rax]
0032D0A0  A8 01                           test al, 1
0032D0A2  0F 85 50 01 00 00               jne 0x14032d1f8
0032D0A8  48 A9 E0 03 00 00               test rax, 0x3e0
0032D0AE  0F 85 44 01 00 00               jne 0x14032d1f8
0032D0B4  41 81 FE 00 10 00 00            cmp r14d, 0x1000
0032D0BB  0F 84 44 01 00 00               je 0x14032d205
0032D0C1  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0032D0C6  48 81 FF 00 02 00 00            cmp rdi, 0x200
0032D0CD  0F 86 61 05 00 00               jbe 0x14032d634
0032D0D3  48 81 44 24 48 00 02 00 00      add qword ptr [rsp + 0x48], 0x200
0032D0DC  48 05 00 10 00 00               add rax, 0x1000
0032D0E2  48 81 EF 00 02 00 00            sub rdi, 0x200
0032D0E9  E9 77 FF FF FF                  jmp 0x14032d065
0032D0EE  3C 07                           cmp al, 7
0032D0F0  0F 84 36 01 00 00               je 0x14032d22c
0032D0F6  3C 05                           cmp al, 5
0032D0F8  B9 48 00 00 00                  mov ecx, 0x48
0032D0FD  B8 00 00 00 00                  mov eax, 0
0032D102  0F 44 C8                        cmove ecx, eax
0032D105  E9 E8 FC FF FF                  jmp 0x14032cdf2
0032D10A  49 8B CB                        mov rcx, r11
0032D10D  E8 D6 C3 F7 FF                  call 0x1402a94e8
0032D112  0F B7 08                        movzx ecx, word ptr [rax]
0032D115  66 89 8D C0 00 00 00            mov word ptr [rbp + 0xc0], cx
0032D11C  E9 15 F7 FF FF                  jmp 0x14032c836
0032D121  41 BD 01 00 00 00               mov r13d, 1
0032D127  4D 8B E7                        mov r12, r15
0032D12A  E9 07 F7 FF FF                  jmp 0x14032c836
0032D12F  83 4D B0 04                     or dword ptr [rbp - 0x50], 4
0032D133  48 8D 45 90                     lea rax, [rbp - 0x70]
0032D137  48 89 45 68                     mov qword ptr [rbp + 0x68], rax
0032D13B  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0032D13F  8B 45 B4                        mov eax, dword ptr [rbp - 0x4c]
0032D142  25 7F FE FF FF                  and eax, 0xfffffe7f
0032D147  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
0032D14B  83 C8 40                        or eax, 0x40
0032D14E  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
0032D152  89 45 B4                        mov dword ptr [rbp - 0x4c], eax
0032D155  48 8D 05 B4 65 FE FF            lea rax, [rip - 0x19a4c]
0032D15C  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
0032D160  0F B6 85 D0 00 00 00            movzx eax, byte ptr [rbp + 0xd0]
0032D167  88 45 B9                        mov byte ptr [rbp - 0x47], al
0032D16A  4C 89 6D E0                     mov qword ptr [rbp - 0x20], r13
0032D16E  E8 9D 55 F9 FF                  call 0x1402c2710
0032D173  8B 55 90                        mov edx, dword ptr [rbp - 0x70]
0032D176  4C 8B 65 98                     mov r12, qword ptr [rbp - 0x68]
0032D17A  E9 99 F3 FF FF                  jmp 0x14032c518
0032D17F  41 B8 00 20 00 00               mov r8d, 0x2000
0032D185  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
0032D18A  E9 AC F6 FF FF                  jmp 0x14032c83b
0032D18F  41 8B 46 34                     mov eax, dword ptr [r14 + 0x34]
0032D193  4D 2B E7                        sub r12, r15
0032D196  41 8B 4E 2C                     mov ecx, dword ptr [r14 + 0x2c]
0032D19A  25 FF FF FF 3F                  and eax, 0x3fffffff
0032D19F  48 2B C8                        sub rcx, rax
0032D1A2  49 C1 FC 03                     sar r12, 3
0032D1A6  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0032D1AA  4C 8D 14 C8                     lea r10, [rax + rcx*8]
0032D1AE  4C 2B 54 24 38                  sub r10, qword ptr [rsp + 0x38]
0032D1B3  49 C1 FA 03                     sar r10, 3
0032D1B7  4D 3B D4                        cmp r10, r12
0032D1BA  4D 0F 47 D4                     cmova r10, r12
0032D1BE  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
0032D1C3  45 85 C0                        test r8d, r8d
0032D1C6  0F 85 B8 02 00 00               jne 0x14032d484
0032D1CC  4F 8D 24 D7                     lea r12, [r15 + r10*8]
0032D1D0  45 85 C0                        test r8d, r8d
0032D1D3  0F 85 5D F6 FF FF               jne 0x14032c836
0032D1D9  8B F2                           mov esi, edx
0032D1DB  41 B8 00 10 00 00               mov r8d, 0x1000
0032D1E1  C1 EE 07                        shr esi, 7
0032D1E4  83 E6 1F                        and esi, 0x1f
0032D1E7  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
0032D1EC  E9 4A F6 FF FF                  jmp 0x14032c83b
0032D1F1  33 C9                           xor ecx, ecx
0032D1F3  E9 58 FD FF FF                  jmp 0x14032cf50
0032D1F8  41 81 FE 00 10 00 00            cmp r14d, 0x1000
0032D1FF  0F 84 2C FE FF FF               je 0x14032d031
0032D205  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0032D20A  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032D20F  4D 8D 24 C7                     lea r12, [r15 + rax*8]
0032D213  E8 D8 F9 F4 FF                  call 0x14027cbf0
0032D218  E9 19 F6 FF FF                  jmp 0x14032c836
0032D21D  41 81 FE 00 10 00 00            cmp r14d, 0x1000
0032D224  0F 85 25 FE FF FF               jne 0x14032d04f
0032D22A  EB D9                           jmp 0x14032d205
0032D22C  B9 18 00 00 00                  mov ecx, 0x18
0032D231  48 8B 84 0A 40 9C 00 00         mov rax, qword ptr [rdx + rcx + 0x9c40]
0032D239  48 85 C0                        test rax, rax
0032D23C  E9 7C F7 FF FF                  jmp 0x14032c9bd
0032D241  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
0032D246  4D 2B E7                        sub r12, r15
0032D249  49 C1 FC 03                     sar r12, 3
0032D24D  8B 42 34                        mov eax, dword ptr [rdx + 0x34]
0032D250  8B 4A 2C                        mov ecx, dword ptr [rdx + 0x2c]
0032D253  25 FF FF FF 3F                  and eax, 0x3fffffff
0032D258  48 2B C8                        sub rcx, rax
0032D25B  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0032D25F  4C 8D 04 C8                     lea r8, [rax + rcx*8]
0032D263  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
0032D266  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0032D26B  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
0032D270  0F BA E0 11                     bt eax, 0x11
0032D274  0F 82 48 02 00 00               jb 0x14032d4c2
0032D27A  4D 3B C8                        cmp r9, r8
0032D27D  0F 83 3F 02 00 00               jae 0x14032d4c2
0032D283  4C 3B 4A 08                     cmp r9, qword ptr [rdx + 8]
0032D287  0F 82 35 02 00 00               jb 0x14032d4c2
0032D28D  4B 8D 04 E1                     lea rax, [r9 + r12*8]
0032D291  49 3B C0                        cmp rax, r8
0032D294  76 0A                           jbe 0x14032d2a0
0032D296  4D 8B E0                        mov r12, r8
0032D299  4D 2B E1                        sub r12, r9
0032D29C  49 C1 FC 03                     sar r12, 3
0032D2A0  4F 8D 24 E7                     lea r12, [r15 + r12*8]
0032D2A4  4C 8B 9D D8 00 00 00            mov r11, qword ptr [rbp + 0xd8]
0032D2AB  49 8B CB                        mov rcx, r11
0032D2AE  E8 0D 62 F9 FF                  call 0x1402c34c0
0032D2B3  85 C0                           test eax, eax
0032D2B5  0F 84 49 F4 FF FF               je 0x14032c704
0032D2BB  4D 8B C4                        mov r8, r12
0032D2BE  49 8B C9                        mov rcx, r9
0032D2C1  4D 2B C7                        sub r8, r15
0032D2C4  49 C1 F8 03                     sar r8, 3
0032D2C8  E8 5B 73 14 00                  call 0x140474628
0032D2CD  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0032D2D2  48 3B C1                        cmp rax, rcx
0032D2D5  0F 84 29 F4 FF FF               je 0x14032c704
0032D2DB  48 2B C1                        sub rax, rcx
0032D2DE  48 C1 F8 03                     sar rax, 3
0032D2E2  45 33 D2                        xor r10d, r10d
0032D2E5  4C 89 54 24 38                  mov qword ptr [rsp + 0x38], r10
0032D2EA  4D 8D 24 C7                     lea r12, [r15 + rax*8]
0032D2EE  E9 14 F4 FF FF                  jmp 0x14032c707
0032D2F3  41 0F 0D 08                     prefetchw byte ptr [r8]
0032D2F7  41 8B 00                        mov eax, dword ptr [r8]
0032D2FA  8B D0                           mov edx, eax
0032D2FC  0F BA F2 15                     btr edx, 0x15
0032D300  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0032D305  75 F3                           jne 0x14032d2fa
0032D307  0F BA E0 15                     bt eax, 0x15
0032D30B  0F 83 93 FA FF FF               jae 0x14032cda4
0032D311  E8 BA 5E F3 FF                  call 0x1402631d0
0032D316  E9 89 FA FF FF                  jmp 0x14032cda4
0032D31B  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0032D320  48 85 C0                        test rax, rax
0032D323  0F 84 47 F9 FF FF               je 0x14032cc70
0032D329  48 83 78 08 00                  cmp qword ptr [rax + 8], 0
0032D32E  0F 85 3C F9 FF FF               jne 0x14032cc70
0032D334  4D 8B CC                        mov r9, r12
0032D337  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0032D33C  4D 8B C7                        mov r8, r15
0032D33F  48 8B D7                        mov rdx, rdi
0032D342  49 8B CA                        mov rcx, r10
0032D345  E8 26 A8 03 00                  call 0x140367b70
0032D34A  4C 8B E0                        mov r12, rax
0032D34D  49 3B C7                        cmp rax, r15
0032D350  0F 84 1A F9 FF FF               je 0x14032cc70
0032D356  E9 DB F4 FF FF                  jmp 0x14032c836
0032D35B  48 81 C1 C0 00 00 00            add rcx, 0xc0
0032D362  E9 79 F5 FF FF                  jmp 0x14032c8e0
0032D367  49 8B F5                        mov rsi, r13
0032D36A  83 FA 01                        cmp edx, 1
0032D36D  0F 87 92 02 00 00               ja 0x14032d605
0032D373  4C 8B EE                        mov r13, rsi
0032D376  49 C1 ED 09                     shr r13, 9
0032D37A  4D 23 E9                        and r13, r9
0032D37D  49 8B C0                        mov rax, r8
0032D380  4C 03 E8                        add r13, rax
0032D383  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
0032D388  4D 3B E7                        cmp r12, r15
0032D38B  75 3F                           jne 0x14032d3cc
0032D38D  48 8B 16                        mov rdx, qword ptr [rsi]
0032D390  F6 C2 01                        test dl, 1
0032D393  0F 85 34 01 00 00               jne 0x14032d4cd
0032D399  48 0F BA E2 0B                  bt rdx, 0xb
0032D39E  0F 82 3B 02 00 00               jb 0x14032d5df
0032D3A4  4C 8B 9D D8 00 00 00            mov r11, qword ptr [rbp + 0xd8]
0032D3AB  41 8B 43 30                     mov eax, dword ptr [r11 + 0x30]
0032D3AF  83 E0 70                        and eax, 0x70
0032D3B2  3C 30                           cmp al, 0x30
0032D3B4  0F 84 F2 01 00 00               je 0x14032d5ac
0032D3BA  48 8B 85 E8 00 00 00            mov rax, qword ptr [rbp + 0xe8]
0032D3C1  C7 00 10 00 00 00               mov dword ptr [rax], 0x10
0032D3C7  E9 92 01 00 00                  jmp 0x14032d55e
0032D3CC  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032D3D1  49 8B D5                        mov rdx, r13
0032D3D4  E8 E7 9A EE FF                  call 0x140216ec0
0032D3D9  45 33 D2                        xor r10d, r10d
0032D3DC  4D 8B EC                        mov r13, r12
0032D3DF  49 81 E5 00 F0 FF FF            and r13, 0xfffffffffffff000
0032D3E6  4C 89 54 24 50                  mov qword ptr [rsp + 0x50], r10
0032D3EB  49 83 ED 08                     sub r13, 8
0032D3EF  E9 94 F1 FF FF                  jmp 0x14032c588
0032D3F4  48 3B 05 85 1F B0 00            cmp rax, qword ptr [rip + 0xb01f85]
0032D3FB  72 0D                           jb 0x14032d40a
0032D3FD  48 3B 05 8C 1F B0 00            cmp rax, qword ptr [rip + 0xb01f8c]
0032D404  0F 86 B6 F0 FF FF               jbe 0x14032c4c0
0032D40A  B9 02 00 00 00                  mov ecx, 2
0032D40F  E8 BC B7 11 00                  call 0x140448bd0
0032D414  48 8B F0                        mov rsi, rax
0032D417  E9 BB F0 FF FF                  jmp 0x14032c4d7
0032D41C  0F B7 85 C0 00 00 00            movzx eax, word ptr [rbp + 0xc0]
0032D423  44 8B C6                        mov r8d, esi
0032D426  44 8B 4C 24 34                  mov r9d, dword ptr [rsp + 0x34]
0032D42B  41 8B D6                        mov edx, r14d
0032D42E  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
0032D433  E8 C8 C2 10 00                  call 0x140439700
0032D438  85 C0                           test eax, eax
0032D43A  0F 85 E8 FB FF FF               jne 0x14032d028
0032D440  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032D445  33 C0                           xor eax, eax
0032D447  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0032D44C  44 8D 68 01                     lea r13d, [rax + 1]
0032D450  4D 8D 24 C7                     lea r12, [r15 + rax*8]
0032D454  E8 97 F7 F4 FF                  call 0x14027cbf0
0032D459  E9 D8 F3 FF FF                  jmp 0x14032c836
0032D45E  4C 8B 08                        mov r9, qword ptr [rax]
0032D461  41 B8 01 00 00 00               mov r8d, 1
0032D467  49 FF C9                        dec r9
0032D46A  49 C1 E9 0C                     shr r9, 0xc
0032D46E  E9 AB F2 FF FF                  jmp 0x14032c71e
0032D473  48 8B 09                        mov rcx, qword ptr [rcx]
0032D476  48 85 C9                        test rcx, rcx
0032D479  0F 84 B7 F3 FF FF               je 0x14032c836
0032D47F  E9 4B F6 FF FF                  jmp 0x14032cacf
0032D484  41 8B 43 18                     mov eax, dword ptr [r11 + 0x18]
0032D488  41 0F B6 4B 20                  movzx ecx, byte ptr [r11 + 0x20]
0032D48D  48 C1 E1 20                     shl rcx, 0x20
0032D491  48 0B C8                        or rcx, rax
0032D494  48 8B C7                        mov rax, rdi
0032D497  48 2B C1                        sub rax, rcx
0032D49A  49 3B C1                        cmp rax, r9
0032D49D  0F 87 29 FD FF FF               ja 0x14032d1cc
0032D4A3  48 2B CF                        sub rcx, rdi
0032D4A6  48 8D 41 01                     lea rax, [rcx + 1]
0032D4AA  49 03 C1                        add rax, r9
0032D4AD  4C 3B D0                        cmp r10, rax
0032D4B0  4C 0F 47 D0                     cmova r10, rax
0032D4B4  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
0032D4B9  4F 8D 24 D7                     lea r12, [r15 + r10*8]
0032D4BD  E9 17 FD FF FF                  jmp 0x14032d1d9
0032D4C2  41 BC 01 00 00 00               mov r12d, 1
0032D4C8  E9 D3 FD FF FF                  jmp 0x14032d2a0
0032D4CD  48 8B CA                        mov rcx, rdx
0032D4D0  48 C1 E9 0C                     shr rcx, 0xc
0032D4D4  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0032D4DE  48 23 C8                        and rcx, rax
0032D4E1  48 3B 0D F8 07 B0 00            cmp rcx, qword ptr [rip + 0xb007f8]
0032D4E8  77 23                           ja 0x14032d50d
0032D4EA  48 8D 04 49                     lea rax, [rcx + rcx*2]
0032D4EE  48 C1 E0 04                     shl rax, 4
0032D4F2  49 B8 28 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000028
0032D4FC  4C 03 C0                        add r8, rax
0032D4FF  49 8B 00                        mov rax, qword ptr [r8]
0032D502  48 0F BA E0 36                  bt rax, 0x36
0032D507  0F 82 57 01 00 00               jb 0x14032d664
0032D50D  48 8B 05 AC 2B B0 00            mov rax, qword ptr [rip + 0xb02bac]
0032D514  48 C1 E9 12                     shr rcx, 0x12
0032D518  8B 04 C8                        mov eax, dword ptr [rax + rcx*8]
0032D51B  B9 FF 07 00 00                  mov ecx, 0x7ff
0032D520  48 C1 E8 04                     shr rax, 4
0032D524  4C 8B AD D8 00 00 00            mov r13, qword ptr [rbp + 0xd8]
0032D52B  66 23 C1                        and ax, cx
0032D52E  66 89 85 C0 00 00 00            mov word ptr [rbp + 0xc0], ax
0032D535  41 8B 4D 30                     mov ecx, dword ptr [r13 + 0x30]
0032D539  8B C1                           mov eax, ecx
0032D53B  83 E0 70                        and eax, 0x70
0032D53E  3C 30                           cmp al, 0x30
0032D540  0F 85 01 01 00 00               jne 0x14032d647
0032D546  49 8B CD                        mov rcx, r13
0032D549  E8 2A 19 F8 FF                  call 0x1402aee78
0032D54E  8B C8                           mov ecx, eax
0032D550  48 8B 85 E8 00 00 00            mov rax, qword ptr [rbp + 0xe8]
0032D557  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
0032D55C  89 08                           mov dword ptr [rax], ecx
0032D55E  33 C0                           xor eax, eax
0032D560  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0032D564  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032D569  49 8B D5                        mov rdx, r13
0032D56C  E8 4F 99 EE FF                  call 0x140216ec0
0032D571  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
0032D575  48 8B 85 F0 00 00 00            mov rax, qword ptr [rbp + 0xf0]
0032D57C  89 08                           mov dword ptr [rax], ecx
0032D57E  48 8B 85 F8 00 00 00            mov rax, qword ptr [rbp + 0xf8]
0032D585  0F B7 8D C0 00 00 00            movzx ecx, word ptr [rbp + 0xc0]
0032D58C  66 89 08                        mov word ptr [rax], cx
0032D58F  48 8D 4E 08                     lea rcx, [rsi + 8]
0032D593  E8 08 EB F4 FF                  call 0x14027c0a0
0032D598  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
0032D59F  48 89 01                        mov qword ptr [rcx], rax
0032D5A2  B8 00 10 00 00                  mov eax, 0x1000
0032D5A7  E9 C5 F4 FF FF                  jmp 0x14032ca71
0032D5AC  48 8B CA                        mov rcx, rdx
0032D5AF  E8 5C A5 EF FF                  call 0x140227b10
0032D5B4  85 C0                           test eax, eax
0032D5B6  0F 84 FE FD FF FF               je 0x14032d3ba
0032D5BC  45 33 D2                        xor r10d, r10d
0032D5BF  41 8B DA                        mov ebx, r10d
0032D5C2  E9 86 F0 FF FF                  jmp 0x14032c64d
0032D5C7  48 8B CB                        mov rcx, rbx
0032D5CA  E8 41 A5 EF FF                  call 0x140227b10
0032D5CF  85 C0                           test eax, eax
0032D5D1  0F 84 09 F2 FF FF               je 0x14032c7e0
0032D5D7  49 8B DA                        mov rbx, r10
0032D5DA  E9 8D F0 FF FF                  jmp 0x14032c66c
0032D5DF  48 8B 05 9A 06 B0 00            mov rax, qword ptr [rip + 0xb0069a]
0032D5E6  48 8B CA                        mov rcx, rdx
0032D5E9  48 85 C0                        test rax, rax
0032D5EC  0F 84 DE FE FF FF               je 0x14032d4d0
0032D5F2  F6 C2 10                        test dl, 0x10
0032D5F5  75 34                           jne 0x14032d62b
0032D5F7  48 8B C8                        mov rcx, rax
0032D5FA  48 F7 D1                        not rcx
0032D5FD  48 23 CA                        and rcx, rdx
0032D600  E9 CB FE FF FF                  jmp 0x14032d4d0
0032D605  8D 4A FF                        lea ecx, [rdx - 1]
0032D608  48 C1 EE 09                     shr rsi, 9
0032D60C  49 23 F1                        and rsi, r9
0032D60F  49 8B C0                        mov rax, r8
0032D612  48 03 F0                        add rsi, rax
0032D615  48 83 E9 01                     sub rcx, 1
0032D619  0F 84 54 FD FF FF               je 0x14032d373
0032D61F  EB E7                           jmp 0x14032d608
0032D621  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
0032D626  E9 ED F9 FF FF                  jmp 0x14032d018
0032D62B  48 83 E1 EF                     and rcx, 0xffffffffffffffef
0032D62F  E9 9C FE FF FF                  jmp 0x14032d4d0
0032D634  48 01 7C 24 48                  add qword ptr [rsp + 0x48], rdi
0032D639  48 8D 0C F8                     lea rcx, [rax + rdi*8]
0032D63D  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0032D642  E9 BE FB FF FF                  jmp 0x14032d205
0032D647  8B C1                           mov eax, ecx
0032D649  25 00 00 A0 00                  and eax, 0xa00000
0032D64E  3D 00 00 A0 00                  cmp eax, 0xa00000
0032D653  0F 84 ED FE FF FF               je 0x14032d546
0032D659  C1 E9 07                        shr ecx, 7
0032D65C  83 E1 1F                        and ecx, 0x1f
0032D65F  E9 EC FE FF FF                  jmp 0x14032d550
0032D664  49 8B 00                        mov rax, qword ptr [r8]
0032D667  B9 FF 03 00 00                  mov ecx, 0x3ff
0032D66C  48 C1 E8 2B                     shr rax, 0x2b
0032D670  E9 AF FE FF FF                  jmp 0x14032d524
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiQueryAddressState(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m140;
    unsigned int v_stack_m144;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int16 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m184;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int8 v_stack_mFF;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p38;
    unsigned __int16 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int16 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = (unsigned __int8)(a3);
    v_rsp = (v_rsp) - (376);
    a3 = 0;
    v_stack_m180 = 0;
    v_stack_m184 = 0;
    v_r15 = (a1) >> (9);
    v_stack_m150 = 0;
    v_r15 = (v_r15) & (a4);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    v_stack_m160 = result;
    v_stack_m178 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11549844) + *(unsigned __int16 *)(result + 174) * 8)));
    v_stack_p8 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11549844) + *(unsigned __int16 *)(result + 174) * 8)));
    v_r15 = (v_r15) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11549844) + *(unsigned __int16 *)(result + 174) * 8));
    a2 = (a2) >> (9);
    v_stack_m118 = v_r15;
    a2 = (a2) & (a4);
    a2 = (a2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11549844) + *(unsigned __int16 *)(result + 174) * 8));
    v_stack_m140 = 0;
    v_stack_p10 = a2;
    v_stack_m144 = (unsigned int)((unsigned int)(0x2000ULL));
    v_stack_m148 = 0;
    v_stack_m168 = 0;
    v_stack_m170 = 0;
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11549844) + *(unsigned __int16 *)(result + 174) * 8)) << (25);
    v_r13 = (a2) << (25);
    v_r13 = (v_r13) - (v_rsi);
    v_stack_m130 = v_rsi;
    v_r13 = (v_r13) >> (16);
    v_stack_m110 = v_r13;
loc_0032C469:
    v_stack_m138 = a2;
    v_stack_m158 = 0;
    a2 = 0;
    v_stack_m128 = v_xmm0;
    result = memset(v_stack_m104, a2, 188, a4);
    v_stack_m108 = 0x2061ULL;
    v_r12 = (v_r15) << (25);
    v_r12 = (v_r12) - (v_rsi);
    v_r12 = (v_r12) >> (16);
    result = MiGetLeafVa(v_r12, a2, 188, a4);
    if (result >= v_r12) goto loc_0032D3F4;
loc_0032C4C0:
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
loc_0032C4D7:
    a3 = 0;
    result = MiFastLockLeafPageTable(v_rsi, v_r12, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0032D12F;
    v_r12 = (v_r12) >> (9);
    v_stack_m128 = (unsigned int)(result - 1);
    v_r12 = (v_r12) & (result);
    v_r12 = (v_r12) + (result);
    v_stack_m120 = v_r12;
loc_0032C518:
    if (v_r12 == 0) goto loc_0032CDAA;
    v_r13 = (v_r12) >> (9);
    v_r13 = (v_r13) & (a4);
    v_r13 = (v_r13) + (0);
    v_stack_m168 = v_r13;
    if ((unsigned int)(result - 1) != 0) goto loc_0032D367;
    if (v_r15 != v_r12) goto loc_0032D3CC;
    v_r10 = 0;
    v_stack_m158 = 1;
    v_r13 = (v_r15) & (0xFFFFFFFFFFFFF000ULL);
    v_r13 = (v_r13) + (0xFF8ULL);
    v_r14 = (*(unsigned __int64 *)(v_r15) == 0) ? 1 : 0;
loc_0032C588:
    if (v_r13 > v_stack_p10) { v_r13 = v_stack_p10; }
    v_stack_m138 = v_r13;
    goto loc_0032C646;
loc_0032C5A0:
    v_stack_m144 = 0;
    v_stack_m140 = (unsigned int)(v_rsi);
    v_stack_m148 = (unsigned int)((unsigned int)(v_stack_m184));
    v_stack_m178 = (unsigned __int16)(v_stack_p8);
    if (a5 != 0) goto loc_0032CF2C;
loc_0032C5CD:
    *(unsigned int *)(a6) = (unsigned int)(v_rsi);
    *(unsigned int *)(a7) = (unsigned int)((unsigned int)(v_stack_m184));
    *(unsigned __int16 *)(a8) = (unsigned __int16)(v_stack_p8);
loc_0032C5F4:
    if ((unsigned int)(v_r13) != 0) goto loc_0032C919;
    if (v_stack_m170 != 0) goto loc_0032C919;
loc_0032C609:
    if ((v_r15 + 8) != (v_r15 + 8)) goto loc_0032C919;
    if ((v_r15 + 8) > v_stack_m138) goto loc_0032C919;
    v_rbx = *(unsigned __int64 *)(v_r15);
    if (v_stack_m158 != 0) {
        v_rbx = *(unsigned __int64 *)(v_r15 + 8);
    }
    v_r12 = (v_r15 + 8) + (8);
    v_rdi = (v_r15 + 8) << (25);
    v_rdi = (v_rdi) - (v_stack_m130);
    v_rdi = (v_rdi) >> (16);
    v_r10 = 0;
loc_0032C646:
loc_0032C64D:
    v_stack_m184 = 0;
    v_stack_m188 = (unsigned int)((unsigned int)(0x2000ULL));
    if (v_rbx != 0) goto loc_0032C7D0;
loc_0032C66C:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 48))))) & (112));
    if (((unsigned __int8)(result)) == 48) goto loc_0032D10A;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 48))))) & (112));
    if (((unsigned __int8)(result)) == 16) goto loc_0032C836;
    if (((unsigned __int8)(result)) < 16) goto loc_0032CA86;
    v_rdi = (v_rdi) >> (12);
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 72)) + 60)) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    v_stack_p8 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11549123) + (unsigned __int16)(result) * 8)));
    result = MiGetProtoPteAddress(v_stack_p20, v_rdi, 12, v_stack_m150);
    v_stack_m180 = result;
    if (result == 0) goto loc_0032CC25;
    if (0 != 0) goto loc_0032CE83;
    if (v_stack_m158 == 0) goto loc_0032D241;
loc_0032C6FD:
loc_0032C704:
    v_r10 = 0;
loc_0032C707:
    if (sign_flag) goto loc_0032D45E;
loc_0032C71E:
    if (v_stack_m180 == 0) goto loc_0032C836;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 48))))) & (112));
    if (((unsigned __int8)(result)) != 32) goto loc_0032CF6D;
    if (*(unsigned __int64 *)(v_stack_p20 + 72) == 0) goto loc_0032C788;
loc_0032C753:
    if (condition_is_below) goto loc_0032CE47;
loc_0032C760:
loc_0032C764:
    if (v_stack_m180 < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 72) + 8))) goto loc_0032C775;
    if (v_stack_m180 < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 72) + 8) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 72) + 44)) * 8)) goto loc_0032C77E;
loc_0032C775:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 72) + 16) != 0) goto loc_0032C753;
loc_0032C77E:
    v_r10 = 0;
loc_0032C788:
    v_rsi = (v_stack_m180) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 72) + 8));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 72) + 16) + 52))) & (0x3FFFFFFFULL));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 72) + 16) + 44))) - ((unsigned int)(a1)));
    v_rsi = (v_rsi) >> (3);
    if (v_rsi >= ((unsigned int)((unsigned int)(result)))) goto loc_0032CE02;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 48))) >> (7));
    v_rsi = (unsigned int)((v_rsi) & (31));
    if (((unsigned int)(v_rsi)) == 7) {
        v_rsi = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 72) + 16) + 32);
        v_rsi = (unsigned int)((v_rsi) >> (1));
        v_rsi = (unsigned int)((v_rsi) & (31));
    }
    if ((unsigned int)(v_rsi) == 0) goto loc_0032C836;
    v_stack_m188 = (unsigned int)((unsigned int)(0x1000ULL));
    goto loc_0032C83B;
loc_0032C7D0:
    result = MiPureAweVad(v_stack_p20, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 72) + 8), (unsigned int)(0x1000ULL), -1);
    if ((unsigned int)(result) != 0) goto loc_0032D5C7;
loc_0032C7E0:
    result = (unsigned int)((v_rbx) & (992));
    if (result == 512) goto loc_0032C9C8;
loc_0032C7F4:
    v_stack_m188 = (unsigned int)((unsigned int)(0x1000ULL));
    v_stack_m198 = v_stack_p8;
    result = MiGetPageProtection(v_stack_p20, v_r15 + 8, v_stack_m180, v_stack_m184);
    if (v_stack_m180 != 0) goto loc_0032CBD4;
    if ((unsigned int)(result) == 0) goto loc_0032D17F;
loc_0032C836:
loc_0032C83B:
    if ((v_r15 + 8) == v_stack_m118) goto loc_0032C5A0;
    if (((unsigned int)((unsigned int)(v_stack_m188))) != ((unsigned int)((unsigned int)(v_stack_m144)))) goto loc_0032CA17;
    if (v_stack_p8 != ((unsigned __int16)(v_stack_m178))) goto loc_0032CA17;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != v_stack_m140) goto loc_0032CA17;
    if (v_stack_m184 != ((unsigned int)((unsigned int)(v_stack_m148)))) goto loc_0032CA17;
    if (v_stack_m170 != 0) goto loc_0032C5F4;
    if (0 != 0) goto loc_0032C919;
    result = (v_r15 + 8) - (v_stack_m118);
    result = (result) & (-8);
    if (result < 256) goto loc_0032C609;
    if (v_stack_m168 != 0) goto loc_0032C923;
loc_0032C8B4:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_m160 + 184))) & (15));
    if (((unsigned __int8)(result)) > 5) goto loc_0032CC79;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_m160 + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_0032D35B;
loc_0032C8E0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) == 0) goto loc_0032CA10;
loc_0032C902:
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 324))))) << (6);
    if (condition_is_above_or_equal) goto loc_0032CC79;
loc_0032C915:
loc_0032C919:
    goto loc_0032CA31;
loc_0032C923:
    if (v_stack_m168 == ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11583328) + result * 1)))) goto loc_0032CDD1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m160 + 184)))) & (15)) == 0) goto loc_0032CB16;
loc_0032C94C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m160 + 184)))) & (15)) == 0) goto loc_0032C97E;
    if (v_stack_m168 < (*(unsigned __int64 *)(v_rip + 11583328))) goto loc_0032C97E;
    if (v_stack_m168 <= (*(unsigned __int64 *)(v_rip + 11583328))) goto loc_0032CE0A;
loc_0032C97E:
    if (v_stack_m168 < (*(unsigned __int64 *)(v_rip + 11583328))) goto loc_0032C9B4;
    if (v_stack_m168 > (*(unsigned __int64 *)(v_rip + 11583328))) goto loc_0032C9B4;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m168))) & (1)) == 0) goto loc_0032C9B4;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m168))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m168))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0032CB8C;
loc_0032C9B4:
    a2 = (*(unsigned __int64 *)(v_stack_m168)) >> (60);
    a2 = (unsigned int)((a2) & (2));
loc_0032C9BB:
loc_0032C9BD:
    if ((unsigned int)(a2) == 0) goto loc_0032C8B4;
    goto loc_0032C915;
loc_0032C9C8:
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) goto loc_0032C7F4;
    if (condition_is_above_or_equal) goto loc_0032C83B;
    if (*(unsigned __int64 *)(v_rip + 11539101) == 0) goto loc_0032C9F9;
    result = v_rbx;
    if ((((unsigned __int8)(v_rbx)) & (16)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 11539101);
        result = ~(result);
        result = (result) & (v_rbx);
    }
    result = (result) >> (32);
    if (result != ((unsigned int)(0xFFFFFFFFULL))) goto loc_0032C7F4;
    goto loc_0032C83B;
loc_0032CA10:
    result = 0;
    goto loc_0032C902;
loc_0032CA17:
    v_stack_p8 = (unsigned __int16)(v_stack_m178);
    v_stack_m184 = (unsigned int)((unsigned int)(v_stack_m148));
loc_0032CA31:
    result = v_stack_m168;
    if (v_stack_m168 != 0) {
        a1 = v_stack_m160;
        a2 = v_stack_m168;
        result = MiUnlockPageTable(a1, a2, v_stack_m168, v_stack_m184);
    }
    v_r12 = (v_r15 + 8) << (25);
    a1 = (result) << (25);
    v_r12 = (v_r12) - (a1);
    v_r12 = (v_r12) >> (16);
    *(unsigned __int64 *)(a9) = v_r12;
loc_0032CA71:
    v_rsp = (v_rsp) + (376);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))));
loc_0032CA86:
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))));
    v_rsi = (unsigned int)((unsigned int)(result));
    v_r14 = (unsigned int)((unsigned int)(a2));
    if (!(condition_is_above_or_equal)) {
        v_rsi = (unsigned int)(v_stack_m168);
        v_r14 = 0x1000ULL;
        v_rsi = (unsigned int)((v_rsi) >> (7));
        a1 = v_stack_p20;
        v_rsi = (unsigned int)((v_rsi) & (31));
        v_stack_p30 = (unsigned int)(v_r14);
        result = MI_GET_GRAPHICS_PROTECTION_FROM_VAD(a1, a2, v_stack_m168, v_stack_m184);
        v_stack_p34 = (unsigned int)(result);
    }
    a3 = (unsigned int)((v_stack_m168) & (0xA00000ULL));
    if (a3 != 0xA00000ULL) goto loc_0032C836;
    a1 = (*(unsigned __int64 *)(v_stack_p20 + 56)) & (-16);
    if (condition_is_equal) goto loc_0032C836;
loc_0032CACF:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (16)) == 0) goto loc_0032D473;
    if (*(unsigned __int64 *)(a1 + 24) == 0) goto loc_0032C836;
    result = PsReferencePartitionSafe(*(unsigned __int64 *)(a1 + 24), a2, *(unsigned __int64 *)(a1 + 24), v_stack_m184);
    if ((unsigned __int8)(result) == 0) goto loc_0032C836;
    v_stack_p8 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24))));
    result = PsDereferencePartition(*(unsigned __int64 *)(a1 + 24), (unsigned int)(0x75516D4DULL), *(unsigned __int64 *)(a1 + 24), v_stack_m184);
    goto loc_0032C836;
loc_0032CB16:
    if ((*(unsigned __int64 *)(a1 + 24)) < result) goto loc_0032C94C;
    if ((*(unsigned __int64 *)(a1 + 24)) > result) goto loc_0032C94C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_0032C94C;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 24)))) >> (3));
    result = (unsigned int)((result) & (511));
    result = 0;
    a2 = 0;
    if (condition_is_below) { a2 = 1; }
    goto loc_0032C9BB;
loc_0032CB8C:
    result = MiPteHasShadow((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + result * 4)), a2, *(unsigned __int64 *)(a1 + 24), v_stack_m184);
    if (result == 0) goto loc_0032C9B4;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_0032C9B4;
    result = (*(unsigned __int64 *)(a1 + 24)) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (32)) != 0) {
        a2 = (a2) | (32);
    }
    a2 = (a2) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (66)) == 0) { a2 = a2; }
    goto loc_0032C9B4;
loc_0032CBD4:
    result = MiUnlockPageTable(v_stack_p58, v_stack_p50, *(unsigned __int64 *)(a1 + 24), v_stack_m184);
    result = 0;
    v_stack_p50 = 0;
    result = MiUnlockWorkingSetShared(v_stack_p58, v_stack_p18, *(unsigned __int64 *)(a1 + 24), v_stack_m184);
    result = MiFaultInPagedPool(v_stack_p38, v_stack_p18, *(unsigned __int64 *)(a1 + 24), v_stack_m184);
    result = MiLockWorkingSetShared(v_stack_p58, v_stack_p18, *(unsigned __int64 *)(a1 + 24), v_stack_m184);
    a3 = 0;
    goto loc_0032C469;
loc_0032CC25:
    if (a5 == 0) goto loc_0032CC59;
    if ((*(unsigned int *)(a5 + 32)) != 0x2000ULL) goto loc_0032D121;
    if ((*(unsigned int *)(a5 + 36)) != 0) goto loc_0032D121;
    if (v_stack_p8 != ((unsigned __int16)(*(unsigned __int16 *)(a5 + 20)))) goto loc_0032D121;
loc_0032CC59:
    result = MiVadPureReserve(v_stack_p20, v_stack_p10, a3, v_stack_m184);
    if ((unsigned int)(result) != 0) goto loc_0032D31B;
loc_0032CC70:
    goto loc_0032C836;
loc_0032CC79:
    if (v_stack_p18 >= 2) goto loc_0032C609;
    v_rdi = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (1)) != 0) goto loc_0032CCF8;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) != 0) goto loc_0032CD4E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (30)) != 0) goto loc_0032CD17;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14521)) != 0) goto loc_0032CD6E;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16) != 0) goto loc_0032CD41;
loc_0032CCD6:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33708)))) <= 7) goto loc_0032C609;
    if (0 == 0) goto loc_0032CD75;
loc_0032CCE8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (30)) == 0) goto loc_0032CDBD;
    goto loc_0032CD1C;
loc_0032CCF8:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34396)))) <= 7) goto loc_0032CCD6;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14521)) == 0) goto loc_0032CCE8;
    goto loc_0032CD1C;
loc_0032CD17:
loc_0032CD1C:
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14521);
    if (((*(unsigned int *)(v_rip + 13213150)) & (0x4000000ULL)) != 0) {
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34396)));
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33708)));
        a1 = 2;
        result = EtwTraceShouldYieldProcessor(a1, a2, a3, 0);
    }
    if (2 != 0) goto loc_0032C915;
    goto loc_0032C609;
loc_0032CD41:
    if (result == (*(unsigned __int64 *)(a1 + 8))) goto loc_0032CCD6;
    goto loc_0032CD1C;
loc_0032CD4E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33708)))) <= 7) goto loc_0032C609;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 14521)) == 0) goto loc_0032CCE8;
    goto loc_0032CD1C;
loc_0032CD6E:
    goto loc_0032CD1C;
loc_0032CD75:
    if (1 != 0) goto loc_0032CCE8;
loc_0032CD7E:
    *(unsigned int *)(a1 + 33708) = 3;
    *(unsigned int *)(a1 + 34396) = 3;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0032D2F3;
loc_0032CDA4:
    goto loc_0032CD1C;
loc_0032CDAA:
    v_r12 = (v_stack_p10) + (8);
    v_r10 = 0;
    goto loc_0032C646;
loc_0032CDBD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) goto loc_0032CD7E;
    goto loc_0032CD1C;
loc_0032CDD1:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p58 + 184))) & (15));
    if (condition_is_not_equal) goto loc_0032D0EE;
loc_0032CDF2:
    goto loc_0032C9BD;
loc_0032CE02:
    goto loc_0032C836;
loc_0032CE0A:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536)) - (48);
    a1 = (a1) >> (3);
    a1 = (unsigned int)((a1) + ((unsigned int)(a1)));
    result = ((unsigned int)((unsigned int)(a1))) >> (5);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (31));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 3329583 + result * 4 + 14873004))) >> ((unsigned __int8)((unsigned int)(a3))));
    goto loc_0032C9BD;
loc_0032CE47:
    if (((*(unsigned int *)(*(unsigned __int64 *)(6) + 56)) & (0x8000000ULL)) == 0) goto loc_0032C760;
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, a3, 1);
    result = MiGetSharedProtos(*(unsigned __int64 *)(6), (unsigned int)((unsigned int)(result)), 6, 1);
    goto loc_0032C764;
loc_0032CE83:
    a3 = (v_stack_m138) - (v_r15 + 8);
    a3 = (a3) >> (3);
    a3 = (a3) + 1;
    if (a3 > 32) { a3 = 32; }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p68 + 52))) & (0x3FFFFFFFULL));
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_p68 + 44))) - (result);
    if (condition_is_below) goto loc_0032CEEC;
    if (v_stack_p38 >= (*(unsigned __int64 *)(v_stack_p68 + 8) + a1 * 8)) goto loc_0032CEEC;
    if (v_stack_p38 < (*(unsigned __int64 *)(v_stack_p68 + 8))) goto loc_0032CEEC;
    if ((v_stack_p38 + a3 * 8) <= (*(unsigned __int64 *)(v_stack_p68 + 8) + a1 * 8)) goto loc_0032CEEF;
    a3 = (*(unsigned __int64 *)(v_stack_p68 + 8) + a1 * 8) - (v_stack_p38);
    a3 = (a3) >> (3);
    goto loc_0032CEEF;
loc_0032CEEC:
    a3 = 0;
loc_0032CEEF:
    if ((v_r15 + 8 + 8) > (v_r15 + 8 + a3 - 1 * 8)) goto loc_0032CF1C;
loc_0032CF00:
    if (*(unsigned __int64 *)(v_r15 + 8 + 8) != 0) goto loc_0032CF12;
    v_r12 = (v_r15 + 8 + 8) + (8);
    if (v_r12 <= (v_r15 + 8 + a3 - 1 * 8)) goto loc_0032CF00;
loc_0032CF12:
loc_0032CF1C:
    if (v_stack_p60 != 0) goto loc_0032C6FD;
    goto loc_0032D2A4;
loc_0032CF2C:
    if (0 != (*(unsigned int *)(v_stack_p68 + 32))) goto loc_0032CF5F;
    if (0 == 0) goto loc_0032D1F1;
    a1 = (unsigned int)((v_r15 + 8 + a3 - 1 * 8) | (*(unsigned int *)(v_rip - 3329859 + 0 * 4 + 83504)));
loc_0032CF50:
    if (((unsigned int)(a1)) != (*(unsigned int *)(v_stack_p68 + 36))) goto loc_0032CF5F;
    if (((unsigned __int16)(v_stack_p40)) == (*(unsigned __int16 *)(v_stack_p68 + 20))) goto loc_0032C5CD;
loc_0032CF5F:
    goto loc_0032C5CD;
loc_0032CF6D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p68) + 64)) != 0) goto loc_0032D18F;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p68) + 56)) & (0x2000ULL)) != 0) goto loc_0032D18F;
    result = v_stack_p50;
    if (v_stack_p50 != 0) {
        a1 = v_stack_p58;
        a2 = v_stack_p50;
        result = MiUnlockPageTable(a1, a2, v_rip - 3329859, v_stack_p38);
        v_stack_p50 = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_p58, v_stack_p18, v_rip - 3329859, v_stack_p38);
    v_r12 = (v_r15 + 8) - (v_r15 + 8);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p68 + 52))) & (0x3FFFFFFFULL));
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_p68 + 44))) - (result);
    v_r12 = (v_r12) >> (3);
    v_rdi = (*(unsigned __int64 *)(v_stack_p68 + 8) + a1 * 8) - (v_stack_p38);
    v_rdi = (v_rdi) >> (3);
    if (v_rdi > v_r12) { v_rdi = v_r12; }
    if (*(unsigned __int64 *)(v_stack_p38) == 0) goto loc_0032D621;
    v_stack_p30 = (unsigned int)((unsigned int)(0x1000ULL));
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 48))) >> (7));
    v_rsi = (unsigned int)((v_rsi) & (31));
loc_0032D018:
    if (a5 != 0) goto loc_0032D41C;
loc_0032D028:
    if (v_rdi == 0) goto loc_0032D205;
loc_0032D031:
    if (*(unsigned __int64 *)(v_stack_p38) == 0) goto loc_0032D21D;
    if (((unsigned int)((unsigned int)(0x1000ULL))) != 0x1000ULL) goto loc_0032D205;
loc_0032D04F:
    v_rdi = (v_rdi) - 1;
    result = (v_stack_p38) + (8);
loc_0032D065:
    v_stack_p38 = result;
    if (v_rdi == 0) goto loc_0032D205;
    if (((result) & (0xFFFULL)) != 0) goto loc_0032D031;
    a1 = (result) >> (9);
    a1 = (a1) & (result);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + result * 1))) & (1)) != 0) goto loc_0032D1F8;
    if (((*(unsigned __int64 *)(a1 + result * 1)) & (992)) != 0) goto loc_0032D1F8;
    if (((unsigned int)((unsigned int)(v_stack_p30))) == 0x1000ULL) goto loc_0032D205;
    if (v_rdi <= 512) goto loc_0032D634;
    result = (v_stack_p38) + (0x1000ULL);
    v_rdi = (v_rdi) - (512);
    goto loc_0032D065;
loc_0032D0EE:
    if (((unsigned __int8)(result)) == 7) goto loc_0032D22C;
    a1 = 72;
    if (((unsigned __int8)(result)) == 5) { a1 = 0; }
    goto loc_0032CDF2;
loc_0032D10A:
    result = MiGetAweVadPartition(v_stack_p20, v_stack_p18, v_rip - 3329859, v_stack_p38);
    v_stack_p8 = (unsigned __int16)(*(unsigned __int16 *)(result));
    goto loc_0032C836;
loc_0032D121:
    goto loc_0032C836;
loc_0032D12F:
    v_stack_m50 = v_stack_m128;
    result = (unsigned int)(((unsigned int)(v_stack_m104)) & (0xFFFFFE7FULL));
    v_stack_mE8 = v_rsi;
    result = (unsigned int)((result) | (64));
    v_stack_mE0 = v_r15 + 8;
    v_stack_m104 = (unsigned int)(result);
    v_stack_m58 = v_rip - 105036;
    v_stack_mFF = (unsigned __int8)(v_stack_p18);
    v_stack_mD8 = 1;
    result = MiWalkPageTables(v_stack_m108, v_stack_p18, v_rip - 3329859, v_stack_p38);
    goto loc_0032C518;
loc_0032D17F:
    v_stack_p30 = (unsigned int)((unsigned int)(0x2000ULL));
    goto loc_0032C83B;
loc_0032D18F:
    v_r12 = (v_stack_m120) - (v_r15 + 8);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p30) + 52))) & (0x3FFFFFFFULL));
    a1 = ((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p30) + 44))) - (result);
    v_r12 = (v_r12) >> (3);
    v_r10 = (*(unsigned __int64 *)((unsigned int)(v_stack_p30) + 8) + a1 * 8) - (v_stack_p38);
    v_r10 = (v_r10) >> (3);
    if (v_r10 > v_r12) { v_r10 = v_r12; }
    v_stack_p48 = v_r10;
    if ((unsigned int)((unsigned int)(0x2000ULL)) != 0) goto loc_0032D484;
loc_0032D1CC:
    if ((unsigned int)((unsigned int)(0x2000ULL)) != 0) goto loc_0032C836;
loc_0032D1D9:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m128)))) >> (7));
    v_rsi = (unsigned int)((v_rsi) & (31));
    v_stack_p30 = (unsigned int)((unsigned int)(0x1000ULL));
    goto loc_0032C83B;
loc_0032D1F1:
    a1 = 0;
    goto loc_0032CF50;
loc_0032D1F8:
    if (((unsigned int)((unsigned int)(v_stack_p30))) == 0x1000ULL) goto loc_0032D031;
loc_0032D205:
    result = MiLockWorkingSetShared(v_stack_p58, (unsigned int)(v_stack_m128), (unsigned int)(0x1000ULL), v_stack_p38);
    goto loc_0032C836;
loc_0032D21D:
    if (((unsigned int)((unsigned int)(v_stack_p30))) != 0x1000ULL) goto loc_0032D04F;
    goto loc_0032D205;
loc_0032D22C:
    goto loc_0032C9BD;
loc_0032D241:
    v_r12 = (v_r15 + 8 + v_stack_p48 * 8) - (v_r15 + 8);
    v_r12 = (v_r12) >> (3);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p68 + 52))) & (0x3FFFFFFFULL));
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_p68 + 44))) - (result);
    if (condition_is_below) goto loc_0032D4C2;
    if (v_stack_p38 >= (*(unsigned __int64 *)(v_stack_p68 + 8) + a1 * 8)) goto loc_0032D4C2;
    if (v_stack_p38 < (*(unsigned __int64 *)(v_stack_p68 + 8))) goto loc_0032D4C2;
    if ((v_stack_p38 + v_r12 * 8) >= = (*(unsigned __int64 *)(v_stack_p68 + 8) + a1 * 8)) {
        v_r12 = *(unsigned __int64 *)(v_stack_p68 + 8) + a1 * 8;
        v_r12 = (v_r12) - (v_stack_p38);
        v_r12 = (v_r12) >> (3);
    }
loc_0032D2A4:
    result = MiVadPureReserve(v_stack_p20, v_stack_p68, *(unsigned __int64 *)(v_stack_p68 + 8) + a1 * 8, v_stack_p38);
    if ((unsigned int)(result) == 0) goto loc_0032C704;
    a3 = (v_r15 + 8 + v_r12 * 8) - (v_r15 + 8);
    a3 = (a3) >> (3);
    result = MiSkipFractionalPagefileRegion(v_stack_p38, v_stack_p68, a3, v_stack_p38);
    if (result == v_stack_p38) goto loc_0032C704;
    result = (result) - (v_stack_p38);
    result = (result) >> (3);
    v_r10 = 0;
    v_stack_p38 = 0;
    goto loc_0032C707;
loc_0032D2F3:
loc_0032D2FA:
    if (condition_is_not_equal) goto loc_0032D2FA;
    if (condition_is_above_or_equal) goto loc_0032CDA4;
    result = KiRemoveSystemWorkPriorityKick(v_stack_p38, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, v_stack_p38);
    goto loc_0032CDA4;
loc_0032D31B:
    if (v_stack_p68 == 0) goto loc_0032CC70;
    if ((*(unsigned __int64 *)(v_stack_p68 + 8)) != 0) goto loc_0032CC70;
    v_stack_p20 = v_stack_p68;
    result = MiSkipEntirePagefileRegions(0, v_rdi, v_r15 + 8, v_r15 + 8 + result * 8);
    if (result == (v_r15 + 8)) goto loc_0032CC70;
    goto loc_0032C836;
loc_0032D35B:
    a1 = (0) + (192);
    goto loc_0032C8E0;
loc_0032D367:
    if (((unsigned int)(v_rdi)) > 1) goto loc_0032D605;
loc_0032D373:
    v_r13 = (1) >> (9);
    v_r13 = (v_r13) & (v_r15 + 8 + result * 8);
    v_r13 = (v_r13) + (v_r15 + 8);
    v_stack_p50 = v_r13;
    if (result != (v_r15 + 8)) goto loc_0032D3CC;
    if ((((unsigned __int8)(*(unsigned __int64 *)(1))) & (1)) != 0) goto loc_0032D4CD;
    if (condition_is_below) goto loc_0032D5DF;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 48))) & (112));
    if (((unsigned __int8)(result)) == 48) goto loc_0032D5AC;
loc_0032D3BA:
    *(unsigned int *)(a6) = 16;
    goto loc_0032D55E;
loc_0032D3CC:
    result = MiUnlockPageTable(v_stack_p58, v_r13, v_r15 + 8, v_r15 + 8 + result * 8);
    v_r10 = 0;
    v_r13 = (result) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p50 = 0;
    v_r13 = (v_r13) - (8);
    goto loc_0032C588;
loc_0032D3F4:
    if (result < (*(unsigned __int64 *)(v_rip + 11542405))) goto loc_0032D40A;
    if (result <= (*(unsigned __int64 *)(v_rip + 11542412))) goto loc_0032C4C0;
loc_0032D40A:
    result = MiGetAnyMultiplexedVm(2, v_r13, v_r15 + 8, v_r15 + 8 + result * 8);
    goto loc_0032C4D7;
loc_0032D41C:
    v_stack_p20 = (unsigned __int16)(v_stack_p8);
    result = MiQueryStateMatches(2, (unsigned int)((unsigned int)((unsigned int)(v_stack_p30))), (unsigned int)((unsigned int)(result)), (unsigned int)(v_stack_p34));
    if ((unsigned int)(result) != 0) goto loc_0032D028;
    result = 0;
    v_stack_p48 = 0;
    result = MiLockWorkingSetShared(v_stack_p58, (unsigned int)((unsigned int)((unsigned int)(v_stack_p30))), (unsigned int)((unsigned int)(result)), (unsigned int)(v_stack_p34));
    goto loc_0032C836;
loc_0032D45E:
    a4 = (*(unsigned __int64 *)(result)) - 1;
    a4 = (a4) >> (12);
    goto loc_0032C71E;
loc_0032D473:
    if (*(unsigned __int64 *)(v_stack_p58) == 0) goto loc_0032C836;
    goto loc_0032CACF;
loc_0032D484:
    a1 = (*(unsigned __int8 *)(v_stack_p20 + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(v_stack_p20 + 24)));
    result = (v_rdi) - (a1);
    if (result > a4) goto loc_0032D1CC;
    a1 = (a1) - (v_rdi);
    result = (a1 + 1) + (a4);
    if (0 > result) { v_r10 = result; }
    v_stack_p48 = v_r10;
    goto loc_0032D1D9;
loc_0032D4C2:
    goto loc_0032D2A0;
loc_0032D4CD:
loc_0032D4D0:
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p30)))) >> (12);
    a1 = (a1) & (result);
    if (a1 > (*(unsigned __int64 *)(v_rip + 11536376))) goto loc_0032D50D;
    result = (a1 + a1 * 2) << (4);
    a3 = (1) + (result);
    if (condition_is_below) goto loc_0032D664;
loc_0032D50D:
    a1 = (a1) >> (18);
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11545516) + a1 * 8))) >> (4);
loc_0032D524:
    result = (unsigned __int16)((result) & ((unsigned __int16)((unsigned int)(0x7FFULL))));
    v_stack_p8 = (unsigned __int16)(result);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 48))))) & (112));
    if (((unsigned __int8)(result)) != 48) goto loc_0032D647;
loc_0032D546:
    result = MiGetProtectionFromPte(v_stack_p20, (unsigned int)((unsigned int)((unsigned int)(v_stack_p30))), a3, a4);
loc_0032D550:
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)((unsigned int)(result)));
loc_0032D55E:
    result = 0;
    v_stack_p34 = 0;
    result = MiUnlockPageTable(v_stack_p58, v_stack_p50, a3, a4);
    *(unsigned int *)(a7) = (unsigned int)((unsigned int)(v_stack_p34));
    *(unsigned __int16 *)(a8) = (unsigned __int16)(v_stack_p8);
    result = MiGetLeafVa(result + 8, v_stack_p50, a3, a4);
    *(unsigned __int64 *)(a9) = result;
    goto loc_0032CA71;
loc_0032D5AC:
    result = MiIsLazyStampedPte(v_stack_p50, v_stack_p50, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0032D3BA;
    v_r10 = 0;
    goto loc_0032C64D;
loc_0032D5C7:
    result = MiIsLazyStampedPte(0, v_stack_p50, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0032C7E0;
    goto loc_0032C66C;
loc_0032D5DF:
    if (*(unsigned __int64 *)(v_rip + 11536026) == 0) goto loc_0032D4D0;
    if ((((unsigned __int8)(v_stack_p50)) & (16)) != 0) goto loc_0032D62B;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11536026));
    a1 = (a1) & (v_stack_p50);
    goto loc_0032D4D0;
loc_0032D605:
loc_0032D608:
    v_rsi = (result) >> (9);
    v_rsi = (v_rsi) & (a4);
    v_rsi = (v_rsi) + (a3);
    a1 = (v_stack_p50 - 1) - (1);
    if (condition_is_equal) goto loc_0032D373;
    goto loc_0032D608;
loc_0032D621:
    goto loc_0032D018;
loc_0032D62B:
    a1 = (a1) & (-17);
    goto loc_0032D4D0;
loc_0032D634:
    v_stack_p38 = a3 + v_rdi * 8;
    goto loc_0032D205;
loc_0032D647:
    result = (unsigned int)(((unsigned int)((unsigned int)(a3 + v_rdi * 8))) & (0xA00000ULL));
    if (((unsigned int)(result)) == 0xA00000ULL) goto loc_0032D546;
    a1 = (unsigned int)((a3 + v_rdi * 8) >> (7));
    a1 = (unsigned int)((a1) & (31));
    goto loc_0032D550;
loc_0032D664:
    result = (*(unsigned __int64 *)(a3)) >> (43);
    goto loc_0032D524;
}
```

## 5. (Beta) C Style

```c
int64_t MiQueryAddressState(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, void *Arg6, void *Arg7, void *Arg8, void *Arg9)
{
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m140;
    uint32_t v_stack_m144;
    uint32_t v_stack_m148;
    uint64_t v_stack_m150;
    uint32_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint16_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m184;
    uint32_t v_stack_m188;
    uint64_t v_stack_m198;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint8_t v_stack_mFF;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint64_t v_stack_p38;
    uint16_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint16_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = (uint8_t)(Arg3);
    local_rsp = (local_rsp) - (376);
    Arg3 = 0;
    v_stack_m180 = 0;
    v_stack_m184 = 0;
    local_r15 = (Arg1) >> (9);
    v_stack_m150 = 0;
    local_r15 = (local_r15) & (Arg4);
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    v_stack_m160 = result;
    v_stack_m178 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB03C94) + *(uint16_t *)(result + 0xAE) * 8)));
    v_stack_p8 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB03C94) + *(uint16_t *)(result + 0xAE) * 8)));
    local_r15 = (local_r15) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB03C94) + *(uint16_t *)(result + 0xAE) * 8));
    Arg2 = (Arg2) >> (9);
    v_stack_m118 = local_r15;
    Arg2 = (Arg2) & (Arg4);
    Arg2 = (Arg2) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB03C94) + *(uint16_t *)(result + 0xAE) * 8));
    v_stack_m140 = 0;
    v_stack_p10 = Arg2;
    v_stack_m144 = (uint32_t)((uint32_t)(0x2000ULL));
    v_stack_m148 = 0;
    v_stack_m168 = 0;
    v_stack_m170 = 0;
    local_rsi = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB03C94) + *(uint16_t *)(result + 0xAE) * 8)) << (25);
    local_r13 = (Arg2) << (25);
    local_r13 = (local_r13) - (local_rsi);
    v_stack_m130 = local_rsi;
    local_r13 = (local_r13) >> (16);
    v_stack_m110 = local_r13;
loc_0032C469:
    v_stack_m138 = Arg2;
    v_stack_m158 = 0;
    Arg2 = 0;
    v_stack_m128 = v_xmm0;
    result = memset(v_stack_m104, Arg2, 188, Arg4);
    v_stack_m108 = 0x2061ULL;
    local_r12 = (local_r15) << (25);
    local_r12 = (local_r12) - (local_rsi);
    local_r12 = (local_r12) >> (16);
    result = MiGetLeafVa(local_r12, Arg2, 188, Arg4);
    if (result >= local_r12) goto loc_0032D3F4;
loc_0032C4C0:
    local_rsi = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
loc_0032C4D7:
    Arg3 = 0;
    result = MiFastLockLeafPageTable(local_rsi, local_r12, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0032D12F;
    local_r12 = (local_r12) >> (9);
    v_stack_m128 = (uint32_t)(result - 1);
    local_r12 = (local_r12) & (result);
    local_r12 = (local_r12) + (result);
    v_stack_m120 = local_r12;
loc_0032C518:
    if (local_r12 == 0) goto loc_0032CDAA;
    local_r13 = (local_r12) >> (9);
    local_r13 = (local_r13) & (Arg4);
    local_r13 = (local_r13) + (0);
    v_stack_m168 = local_r13;
    if ((uint32_t)(result - 1) != 0) goto loc_0032D367;
    if (local_r15 != local_r12) goto loc_0032D3CC;
    local_r10 = 0;
    v_stack_m158 = 1;
    local_r13 = (local_r15) & (0xFFFFFFFFFFFFF000ULL);
    local_r13 = (local_r13) + (0xFF8ULL);
    local_r14 = (*(uint64_t *)(local_r15) == 0) ? 1 : 0;
loc_0032C588:
    if (local_r13 > v_stack_p10) { local_r13 = v_stack_p10; }
    v_stack_m138 = local_r13;
    goto loc_0032C646;
loc_0032C5A0:
    v_stack_m144 = 0;
    v_stack_m140 = (uint32_t)(local_rsi);
    v_stack_m148 = (uint32_t)((uint32_t)(v_stack_m184));
    v_stack_m178 = (uint16_t)(v_stack_p8);
    if (Arg5 != 0) goto loc_0032CF2C;
loc_0032C5CD:
    *(uint32_t *)(arg6) = (uint32_t)(local_rsi);
    *(uint32_t *)(arg7) = (uint32_t)((uint32_t)(v_stack_m184));
    *(uint16_t *)(arg8) = (uint16_t)(v_stack_p8);
loc_0032C5F4:
    if ((uint32_t)(local_r13) != 0) goto loc_0032C919;
    if (v_stack_m170 != 0) goto loc_0032C919;
loc_0032C609:
    if ((local_r15 + 8) != (local_r15 + 8)) goto loc_0032C919;
    if ((local_r15 + 8) > v_stack_m138) goto loc_0032C919;
    local_rbx = *(uint64_t *)(local_r15);
    if (v_stack_m158 != 0) {
        local_rbx = *(uint64_t *)(local_r15 + 0x8);
    }
    local_r12 = (local_r15 + 8) + (8);
    local_rdi = (local_r15 + 8) << (25);
    local_rdi = (local_rdi) - (v_stack_m130);
    local_rdi = (local_rdi) >> (16);
    local_r10 = 0;
loc_0032C646:
loc_0032C64D:
    v_stack_m184 = 0;
    v_stack_m188 = (uint32_t)((uint32_t)(0x2000ULL));
    if (local_rbx != 0) goto loc_0032C7D0;
loc_0032C66C:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x30))))) & (112));
    if (((uint8_t)(result)) == 48) goto loc_0032D10A;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x30))))) & (112));
    if (((uint8_t)(result)) == 16) goto loc_0032C836;
    if (((uint8_t)(result)) < 16) goto loc_0032CA86;
    local_rdi = (local_rdi) >> (12);
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x48)) + 0x3C)) & ((uint16_t)((uint32_t)(0x3FFULL))));
    v_stack_p8 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB039C3) + (uint16_t)(result) * 8)));
    result = MiGetProtoPteAddress(v_stack_p20, local_rdi, 12, v_stack_m150);
    v_stack_m180 = result;
    if (result == 0) goto loc_0032CC25;
    if (0 != 0) goto loc_0032CE83;
    if (v_stack_m158 == 0) goto loc_0032D241;
loc_0032C6FD:
loc_0032C704:
    local_r10 = 0;
loc_0032C707:
    if (sign_flag) goto loc_0032D45E;
loc_0032C71E:
    if (v_stack_m180 == 0) goto loc_0032C836;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x30))))) & (112));
    if (((uint8_t)(result)) != 32) goto loc_0032CF6D;
    if (*(uint64_t *)(v_stack_p20 + 0x48) == 0) goto loc_0032C788;
loc_0032C753:
    if (condition_is_below) goto loc_0032CE47;
loc_0032C760:
loc_0032C764:
    if (v_stack_m180 < (*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x48) + 0x8))) goto loc_0032C775;
    if (v_stack_m180 < (*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x48) + 0x8) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x48) + 0x2C)) * 8)) goto loc_0032C77E;
loc_0032C775:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x48) + 0x10) != 0) goto loc_0032C753;
loc_0032C77E:
    local_r10 = 0;
loc_0032C788:
    local_rsi = (v_stack_m180) - (*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x48) + 0x8));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x48) + 0x10) + 0x34))) & (0x3FFFFFFFULL));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x48) + 0x10) + 0x2C))) - ((uint32_t)(Arg1)));
    local_rsi = (local_rsi) >> (3);
    if (local_rsi >= ((uint32_t)((uint32_t)(result)))) goto loc_0032CE02;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x30))) >> (7));
    local_rsi = (uint32_t)((local_rsi) & (31));
    if (((uint32_t)(local_rsi)) == 7) {
        local_rsi = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x48) + 0x10) + 0x20);
        local_rsi = (uint32_t)((local_rsi) >> (1));
        local_rsi = (uint32_t)((local_rsi) & (31));
    }
    if ((uint32_t)(local_rsi) == 0) goto loc_0032C836;
    v_stack_m188 = (uint32_t)((uint32_t)(0x1000ULL));
    goto loc_0032C83B;
loc_0032C7D0:
    result = MiPureAweVad(v_stack_p20, *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x48) + 0x8), (uint32_t)(0x1000ULL), -1);
    if ((uint32_t)(result) != 0) goto loc_0032D5C7;
loc_0032C7E0:
    result = (uint32_t)((local_rbx) & (992));
    if (result == 512) goto loc_0032C9C8;
loc_0032C7F4:
    v_stack_m188 = (uint32_t)((uint32_t)(0x1000ULL));
    v_stack_m198 = v_stack_p8;
    result = MiGetPageProtection(v_stack_p20, local_r15 + 8, v_stack_m180, v_stack_m184);
    if (v_stack_m180 != 0) goto loc_0032CBD4;
    if ((uint32_t)(result) == 0) goto loc_0032D17F;
loc_0032C836:
loc_0032C83B:
    if ((local_r15 + 8) == v_stack_m118) goto loc_0032C5A0;
    if (((uint32_t)((uint32_t)(v_stack_m188))) != ((uint32_t)((uint32_t)(v_stack_m144)))) goto loc_0032CA17;
    if (v_stack_p8 != ((uint16_t)(v_stack_m178))) goto loc_0032CA17;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != v_stack_m140) goto loc_0032CA17;
    if (v_stack_m184 != ((uint32_t)((uint32_t)(v_stack_m148)))) goto loc_0032CA17;
    if (v_stack_m170 != 0) goto loc_0032C5F4;
    if (0 != 0) goto loc_0032C919;
    result = (local_r15 + 8) - (v_stack_m118);
    result = (result) & (-8);
    if (result < 256) goto loc_0032C609;
    if (v_stack_m168 != 0) goto loc_0032C923;
loc_0032C8B4:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_m160 + 0xB8))) & (15));
    if (((uint8_t)(result)) > 5) goto loc_0032CC79;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_m160 + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_0032D35B;
loc_0032C8E0:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) == 0) goto loc_0032CA10;
loc_0032C902:
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x144))))) << (6);
    if (condition_is_above_or_equal) goto loc_0032CC79;
loc_0032C915:
loc_0032C919:
    goto loc_0032CA31;
loc_0032C923:
    if (v_stack_m168 == ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB0BF60) + result * 1)))) goto loc_0032CDD1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m160 + 0xB8)))) & (15)) == 0) goto loc_0032CB16;
loc_0032C94C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m160 + 0xB8)))) & (15)) == 0) goto loc_0032C97E;
    if (v_stack_m168 < (*(uint64_t *)(v_rip + 0xB0BF60))) goto loc_0032C97E;
    if (v_stack_m168 <= (*(uint64_t *)(v_rip + 0xB0BF60))) goto loc_0032CE0A;
loc_0032C97E:
    if (v_stack_m168 < (*(uint64_t *)(v_rip + 0xB0BF60))) goto loc_0032C9B4;
    if (v_stack_m168 > (*(uint64_t *)(v_rip + 0xB0BF60))) goto loc_0032C9B4;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m168))) & (1)) == 0) goto loc_0032C9B4;
    Arg1 = ((((uint8_t)(*(uint64_t *)(v_stack_m168))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(v_stack_m168))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0032CB8C;
loc_0032C9B4:
    Arg2 = (*(uint64_t *)(v_stack_m168)) >> (60);
    Arg2 = (uint32_t)((Arg2) & (2));
loc_0032C9BB:
loc_0032C9BD:
    if ((uint32_t)(Arg2) == 0) goto loc_0032C8B4;
    goto loc_0032C915;
loc_0032C9C8:
    if ((((uint8_t)(local_rbx)) & (1)) != 0) goto loc_0032C7F4;
    if (condition_is_above_or_equal) goto loc_0032C83B;
    if (*(uint64_t *)(v_rip + 0xB0129D) == 0) goto loc_0032C9F9;
    result = local_rbx;
    if ((((uint8_t)(local_rbx)) & (16)) == 0) {
        result = *(uint64_t *)(v_rip + 0xB0129D);
        result = ~(result);
        result = (result) & (local_rbx);
    }
    result = (result) >> (32);
    if (result != ((uint32_t)(0xFFFFFFFFULL))) goto loc_0032C7F4;
    goto loc_0032C83B;
loc_0032CA10:
    result = 0;
    goto loc_0032C902;
loc_0032CA17:
    v_stack_p8 = (uint16_t)(v_stack_m178);
    v_stack_m184 = (uint32_t)((uint32_t)(v_stack_m148));
loc_0032CA31:
    result = v_stack_m168;
    if (v_stack_m168 != 0) {
        Arg1 = v_stack_m160;
        Arg2 = v_stack_m168;
        result = MiUnlockPageTable(Arg1, Arg2, v_stack_m168, v_stack_m184);
    }
    local_r12 = (local_r15 + 8) << (25);
    Arg1 = (result) << (25);
    local_r12 = (local_r12) - (Arg1);
    local_r12 = (local_r12) >> (16);
    *(uint64_t *)(arg9) = local_r12;
loc_0032CA71:
    local_rsp = (local_rsp) + (376);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))));
loc_0032CA86:
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))));
    local_rsi = (uint32_t)((uint32_t)(result));
    local_r14 = (uint32_t)((uint32_t)(Arg2));
    if (!(condition_is_above_or_equal)) {
        local_rsi = (uint32_t)(v_stack_m168);
        local_r14 = 0x1000ULL;
        local_rsi = (uint32_t)((local_rsi) >> (7));
        Arg1 = v_stack_p20;
        local_rsi = (uint32_t)((local_rsi) & (31));
        v_stack_p30 = (uint32_t)(local_r14);
        result = MI_GET_GRAPHICS_PROTECTION_FROM_VAD(Arg1, Arg2, v_stack_m168, v_stack_m184);
        v_stack_p34 = (uint32_t)(result);
    }
    Arg3 = (uint32_t)((v_stack_m168) & (0xA00000ULL));
    if (Arg3 != 0xA00000ULL) goto loc_0032C836;
    Arg1 = (*(uint64_t *)(v_stack_p20 + 0x38)) & (-16);
    if (condition_is_equal) goto loc_0032C836;
loc_0032CACF:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x50)))) & (16)) == 0) goto loc_0032D473;
    if (*(uint64_t *)(Arg1 + 0x18) == 0) goto loc_0032C836;
    result = PsReferencePartitionSafe(*(uint64_t *)(Arg1 + 0x18), Arg2, *(uint64_t *)(Arg1 + 0x18), v_stack_m184);
    if ((uint8_t)(result) == 0) goto loc_0032C836;
    v_stack_p8 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x18))));
    result = PsDereferencePartition(*(uint64_t *)(Arg1 + 0x18), (uint32_t)(0x75516D4DULL), *(uint64_t *)(Arg1 + 0x18), v_stack_m184);
    goto loc_0032C836;
loc_0032CB16:
    if ((*(uint64_t *)(Arg1 + 0x18)) < result) goto loc_0032C94C;
    if ((*(uint64_t *)(Arg1 + 0x18)) > result) goto loc_0032C94C;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_0032C94C;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(Arg1 + 0x18)))) >> (3));
    result = (uint32_t)((result) & (511));
    result = 0;
    Arg2 = 0;
    if (condition_is_below) { Arg2 = 1; }
    goto loc_0032C9BB;
loc_0032CB8C:
    result = MiPteHasShadow((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + result * 4)), Arg2, *(uint64_t *)(Arg1 + 0x18), v_stack_m184);
    if (result == 0) goto loc_0032C9B4;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_0032C9B4;
    result = (*(uint64_t *)(Arg1 + 0x18)) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (32)) != 0) {
        Arg2 = (Arg2) | (32);
    }
    Arg2 = (Arg2) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (66)) == 0) { Arg2 = Arg2; }
    goto loc_0032C9B4;
loc_0032CBD4:
    result = MiUnlockPageTable(v_stack_p58, v_stack_p50, *(uint64_t *)(Arg1 + 0x18), v_stack_m184);
    result = 0;
    v_stack_p50 = 0;
    result = MiUnlockWorkingSetShared(v_stack_p58, v_stack_p18, *(uint64_t *)(Arg1 + 0x18), v_stack_m184);
    result = MiFaultInPagedPool(v_stack_p38, v_stack_p18, *(uint64_t *)(Arg1 + 0x18), v_stack_m184);
    result = MiLockWorkingSetShared(v_stack_p58, v_stack_p18, *(uint64_t *)(Arg1 + 0x18), v_stack_m184);
    Arg3 = 0;
    goto loc_0032C469;
loc_0032CC25:
    if (Arg5 == 0) goto loc_0032CC59;
    if ((*(uint32_t *)(Arg5 + 0x20)) != 0x2000ULL) goto loc_0032D121;
    if ((*(uint32_t *)(Arg5 + 0x24)) != 0) goto loc_0032D121;
    if (v_stack_p8 != ((uint16_t)(*(uint16_t *)(Arg5 + 0x14)))) goto loc_0032D121;
loc_0032CC59:
    result = MiVadPureReserve(v_stack_p20, v_stack_p10, Arg3, v_stack_m184);
    if ((uint32_t)(result) != 0) goto loc_0032D31B;
loc_0032CC70:
    goto loc_0032C836;
loc_0032CC79:
    if (v_stack_p18 >= 2) goto loc_0032C609;
    local_rdi = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (1)) != 0) goto loc_0032CCF8;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) != 0) goto loc_0032CD4E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (30)) != 0) goto loc_0032CD17;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38B9)) != 0) goto loc_0032CD6E;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10) != 0) goto loc_0032CD41;
loc_0032CCD6:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83AC)))) <= 7) goto loc_0032C609;
    if (0 == 0) goto loc_0032CD75;
loc_0032CCE8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (30)) == 0) goto loc_0032CDBD;
    goto loc_0032CD1C;
loc_0032CCF8:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x865C)))) <= 7) goto loc_0032CCD6;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38B9)) == 0) goto loc_0032CCE8;
    goto loc_0032CD1C;
loc_0032CD17:
loc_0032CD1C:
    result = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38B9);
    if (((*(uint32_t *)(v_rip + 0xC99DDE)) & (0x4000000ULL)) != 0) {
        Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x865C)));
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83AC)));
        Arg1 = 2;
        result = EtwTraceShouldYieldProcessor(Arg1, Arg2, Arg3, 0);
    }
    if (2 != 0) goto loc_0032C915;
    goto loc_0032C609;
loc_0032CD41:
    if (result == (*(uint64_t *)(Arg1 + 0x8))) goto loc_0032CCD6;
    goto loc_0032CD1C;
loc_0032CD4E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83AC)))) <= 7) goto loc_0032C609;
    if ((uint8_t)(*(uint8_t *)(Arg1 + 0x38B9)) == 0) goto loc_0032CCE8;
    goto loc_0032CD1C;
loc_0032CD6E:
    goto loc_0032CD1C;
loc_0032CD75:
    if (1 != 0) goto loc_0032CCE8;
loc_0032CD7E:
    *(uint32_t *)(Arg1 + 0x83AC) = 3;
    *(uint32_t *)(Arg1 + 0x865C) = 3;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0032D2F3;
loc_0032CDA4:
    goto loc_0032CD1C;
loc_0032CDAA:
    local_r12 = (v_stack_p10) + (8);
    local_r10 = 0;
    goto loc_0032C646;
loc_0032CDBD:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) goto loc_0032CD7E;
    goto loc_0032CD1C;
loc_0032CDD1:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p58 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_0032D0EE;
loc_0032CDF2:
    goto loc_0032C9BD;
loc_0032CE02:
    goto loc_0032C836;
loc_0032CE0A:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8)) - (48);
    Arg1 = (Arg1) >> (3);
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1)));
    result = ((uint32_t)((uint32_t)(Arg1))) >> (5);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (31));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x32CE2F + result * 4 + 0xE2F1AC))) >> ((uint8_t)((uint32_t)(Arg3))));
    goto loc_0032C9BD;
loc_0032CE47:
    if (((*(uint32_t *)(*(uint64_t *)(6) + 0x38)) & (0x8000000ULL)) == 0) goto loc_0032C760;
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, Arg3, 1);
    result = MiGetSharedProtos(*(uint64_t *)(6), (uint32_t)((uint32_t)(result)), 6, 1);
    goto loc_0032C764;
loc_0032CE83:
    Arg3 = (v_stack_m138) - (local_r15 + 8);
    Arg3 = (Arg3) >> (3);
    Arg3 = (Arg3) + 1;
    if (Arg3 > 32) { Arg3 = 32; }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x34))) & (0x3FFFFFFFULL));
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x2C))) - (result);
    if (condition_is_below) goto loc_0032CEEC;
    if (v_stack_p38 >= (*(uint64_t *)(v_stack_p68 + 0x8) + Arg1 * 8)) goto loc_0032CEEC;
    if (v_stack_p38 < (*(uint64_t *)(v_stack_p68 + 0x8))) goto loc_0032CEEC;
    if ((v_stack_p38 + Arg3 * 8) <= (*(uint64_t *)(v_stack_p68 + 0x8) + Arg1 * 8)) goto loc_0032CEEF;
    Arg3 = (*(uint64_t *)(v_stack_p68 + 0x8) + Arg1 * 8) - (v_stack_p38);
    Arg3 = (Arg3) >> (3);
    goto loc_0032CEEF;
loc_0032CEEC:
    Arg3 = 0;
loc_0032CEEF:
    if ((local_r15 + 8 + 8) > (local_r15 + 8 + Arg3 - 1 * 8)) goto loc_0032CF1C;
loc_0032CF00:
    if (*(uint64_t *)(local_r15 + 0x8 + 0x8) != 0) goto loc_0032CF12;
    local_r12 = (local_r15 + 8 + 8) + (8);
    if (local_r12 <= (local_r15 + 8 + Arg3 - 1 * 8)) goto loc_0032CF00;
loc_0032CF12:
loc_0032CF1C:
    if (v_stack_p60 != 0) goto loc_0032C6FD;
    goto loc_0032D2A4;
loc_0032CF2C:
    if (0 != (*(uint32_t *)(v_stack_p68 + 0x20))) goto loc_0032CF5F;
    if (0 == 0) goto loc_0032D1F1;
    Arg1 = (uint32_t)((local_r15 + 8 + Arg3 - 1 * 8) | (*(uint32_t *)(v_rip - 0x32CF43 + 0x0 * 4 + 0x14630)));
loc_0032CF50:
    if (((uint32_t)(Arg1)) != (*(uint32_t *)(v_stack_p68 + 0x24))) goto loc_0032CF5F;
    if (((uint16_t)(v_stack_p40)) == (*(uint16_t *)(v_stack_p68 + 0x14))) goto loc_0032C5CD;
loc_0032CF5F:
    goto loc_0032C5CD;
loc_0032CF6D:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p68) + 0x40)) != 0) goto loc_0032D18F;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p68) + 0x38)) & (0x2000ULL)) != 0) goto loc_0032D18F;
    result = v_stack_p50;
    if (v_stack_p50 != 0) {
        Arg1 = v_stack_p58;
        Arg2 = v_stack_p50;
        result = MiUnlockPageTable(Arg1, Arg2, v_rip - 3329859, v_stack_p38);
        v_stack_p50 = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_p58, v_stack_p18, v_rip - 3329859, v_stack_p38);
    local_r12 = (local_r15 + 8) - (local_r15 + 8);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x34))) & (0x3FFFFFFFULL));
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x2C))) - (result);
    local_r12 = (local_r12) >> (3);
    local_rdi = (*(uint64_t *)(v_stack_p68 + 0x8) + Arg1 * 8) - (v_stack_p38);
    local_rdi = (local_rdi) >> (3);
    if (local_rdi > local_r12) { local_rdi = local_r12; }
    if (*(uint64_t *)(v_stack_p38) == 0) goto loc_0032D621;
    v_stack_p30 = (uint32_t)((uint32_t)(0x1000ULL));
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x30))) >> (7));
    local_rsi = (uint32_t)((local_rsi) & (31));
loc_0032D018:
    if (Arg5 != 0) goto loc_0032D41C;
loc_0032D028:
    if (local_rdi == 0) goto loc_0032D205;
loc_0032D031:
    if (*(uint64_t *)(v_stack_p38) == 0) goto loc_0032D21D;
    if (((uint32_t)((uint32_t)(0x1000ULL))) != 0x1000ULL) goto loc_0032D205;
loc_0032D04F:
    local_rdi = (local_rdi) - 1;
    result = (v_stack_p38) + (8);
loc_0032D065:
    v_stack_p38 = result;
    if (local_rdi == 0) goto loc_0032D205;
    if (((result) & (0xFFFULL)) != 0) goto loc_0032D031;
    Arg1 = (result) >> (9);
    Arg1 = (Arg1) & (result);
    if ((((uint8_t)(*(uint64_t *)(Arg1 + result * 1))) & (1)) != 0) goto loc_0032D1F8;
    if (((*(uint64_t *)(Arg1 + result * 1)) & (992)) != 0) goto loc_0032D1F8;
    if (((uint32_t)((uint32_t)(v_stack_p30))) == 0x1000ULL) goto loc_0032D205;
    if (local_rdi <= 512) goto loc_0032D634;
    result = (v_stack_p38) + (0x1000ULL);
    local_rdi = (local_rdi) - (512);
    goto loc_0032D065;
loc_0032D0EE:
    if (((uint8_t)(result)) == 7) goto loc_0032D22C;
    Arg1 = 72;
    if (((uint8_t)(result)) == 5) { Arg1 = 0; }
    goto loc_0032CDF2;
loc_0032D10A:
    result = MiGetAweVadPartition(v_stack_p20, v_stack_p18, v_rip - 3329859, v_stack_p38);
    v_stack_p8 = (uint16_t)(*(uint16_t *)(result));
    goto loc_0032C836;
loc_0032D121:
    goto loc_0032C836;
loc_0032D12F:
    v_stack_m50 = v_stack_m128;
    result = (uint32_t)(((uint32_t)(v_stack_m104)) & (0xFFFFFE7FULL));
    v_stack_mE8 = local_rsi;
    result = (uint32_t)((result) | (64));
    v_stack_mE0 = local_r15 + 8;
    v_stack_m104 = (uint32_t)(result);
    v_stack_m58 = v_rip - 105036;
    v_stack_mFF = (uint8_t)(v_stack_p18);
    v_stack_mD8 = 1;
    result = MiWalkPageTables(v_stack_m108, v_stack_p18, v_rip - 3329859, v_stack_p38);
    goto loc_0032C518;
loc_0032D17F:
    v_stack_p30 = (uint32_t)((uint32_t)(0x2000ULL));
    goto loc_0032C83B;
loc_0032D18F:
    local_r12 = (v_stack_m120) - (local_r15 + 8);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p30) + 0x34))) & (0x3FFFFFFFULL));
    Arg1 = ((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p30) + 0x2C))) - (result);
    local_r12 = (local_r12) >> (3);
    local_r10 = (*(uint64_t *)((uint32_t)(v_stack_p30) + 0x8) + Arg1 * 8) - (v_stack_p38);
    local_r10 = (local_r10) >> (3);
    if (local_r10 > local_r12) { local_r10 = local_r12; }
    v_stack_p48 = local_r10;
    if ((uint32_t)((uint32_t)(0x2000ULL)) != 0) goto loc_0032D484;
loc_0032D1CC:
    if ((uint32_t)((uint32_t)(0x2000ULL)) != 0) goto loc_0032C836;
loc_0032D1D9:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m128)))) >> (7));
    local_rsi = (uint32_t)((local_rsi) & (31));
    v_stack_p30 = (uint32_t)((uint32_t)(0x1000ULL));
    goto loc_0032C83B;
loc_0032D1F1:
    Arg1 = 0;
    goto loc_0032CF50;
loc_0032D1F8:
    if (((uint32_t)((uint32_t)(v_stack_p30))) == 0x1000ULL) goto loc_0032D031;
loc_0032D205:
    result = MiLockWorkingSetShared(v_stack_p58, (uint32_t)(v_stack_m128), (uint32_t)(0x1000ULL), v_stack_p38);
    goto loc_0032C836;
loc_0032D21D:
    if (((uint32_t)((uint32_t)(v_stack_p30))) != 0x1000ULL) goto loc_0032D04F;
    goto loc_0032D205;
loc_0032D22C:
    goto loc_0032C9BD;
loc_0032D241:
    local_r12 = (local_r15 + 8 + v_stack_p48 * 8) - (local_r15 + 8);
    local_r12 = (local_r12) >> (3);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x34))) & (0x3FFFFFFFULL));
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_p68 + 0x2C))) - (result);
    if (condition_is_below) goto loc_0032D4C2;
    if (v_stack_p38 >= (*(uint64_t *)(v_stack_p68 + 0x8) + Arg1 * 8)) goto loc_0032D4C2;
    if (v_stack_p38 < (*(uint64_t *)(v_stack_p68 + 0x8))) goto loc_0032D4C2;
    if ((v_stack_p38 + local_r12 * 8) >= = (*(uint64_t *)(v_stack_p68 + 0x8) + Arg1 * 8)) {
        local_r12 = *(uint64_t *)(v_stack_p68 + 0x8) + Arg1 * 8;
        local_r12 = (local_r12) - (v_stack_p38);
        local_r12 = (local_r12) >> (3);
    }
loc_0032D2A4:
    result = MiVadPureReserve(v_stack_p20, v_stack_p68, *(uint64_t *)(v_stack_p68 + 0x8) + Arg1 * 8, v_stack_p38);
    if ((uint32_t)(result) == 0) goto loc_0032C704;
    Arg3 = (local_r15 + 8 + local_r12 * 8) - (local_r15 + 8);
    Arg3 = (Arg3) >> (3);
    result = MiSkipFractionalPagefileRegion(v_stack_p38, v_stack_p68, Arg3, v_stack_p38);
    if (result == v_stack_p38) goto loc_0032C704;
    result = (result) - (v_stack_p38);
    result = (result) >> (3);
    local_r10 = 0;
    v_stack_p38 = 0;
    goto loc_0032C707;
loc_0032D2F3:
loc_0032D2FA:
    if (condition_is_not_equal) goto loc_0032D2FA;
    if (condition_is_above_or_equal) goto loc_0032CDA4;
    result = KiRemoveSystemWorkPriorityKick(v_stack_p38, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))), Arg3, v_stack_p38);
    goto loc_0032CDA4;
loc_0032D31B:
    if (v_stack_p68 == 0) goto loc_0032CC70;
    if ((*(uint64_t *)(v_stack_p68 + 0x8)) != 0) goto loc_0032CC70;
    v_stack_p20 = v_stack_p68;
    result = MiSkipEntirePagefileRegions(0, local_rdi, local_r15 + 8, local_r15 + 8 + result * 8);
    if (result == (local_r15 + 8)) goto loc_0032CC70;
    goto loc_0032C836;
loc_0032D35B:
    Arg1 = (0) + (192);
    goto loc_0032C8E0;
loc_0032D367:
    if (((uint32_t)(local_rdi)) > 1) goto loc_0032D605;
loc_0032D373:
    local_r13 = (1) >> (9);
    local_r13 = (local_r13) & (local_r15 + 8 + result * 8);
    local_r13 = (local_r13) + (local_r15 + 8);
    v_stack_p50 = local_r13;
    if (result != (local_r15 + 8)) goto loc_0032D3CC;
    if ((((uint8_t)(*(uint64_t *)(1))) & (1)) != 0) goto loc_0032D4CD;
    if (condition_is_below) goto loc_0032D5DF;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x30))) & (112));
    if (((uint8_t)(result)) == 48) goto loc_0032D5AC;
loc_0032D3BA:
    *(uint32_t *)(arg6) = 16;
    goto loc_0032D55E;
loc_0032D3CC:
    result = MiUnlockPageTable(v_stack_p58, local_r13, local_r15 + 8, local_r15 + 8 + result * 8);
    local_r10 = 0;
    local_r13 = (result) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p50 = 0;
    local_r13 = (local_r13) - (8);
    goto loc_0032C588;
loc_0032D3F4:
    if (result < (*(uint64_t *)(v_rip + 0xB01F85))) goto loc_0032D40A;
    if (result <= (*(uint64_t *)(v_rip + 0xB01F8C))) goto loc_0032C4C0;
loc_0032D40A:
    result = MiGetAnyMultiplexedVm(2, local_r13, local_r15 + 8, local_r15 + 8 + result * 8);
    goto loc_0032C4D7;
loc_0032D41C:
    v_stack_p20 = (uint16_t)(v_stack_p8);
    result = MiQueryStateMatches(2, (uint32_t)((uint32_t)((uint32_t)(v_stack_p30))), (uint32_t)((uint32_t)(result)), (uint32_t)(v_stack_p34));
    if ((uint32_t)(result) != 0) goto loc_0032D028;
    result = 0;
    v_stack_p48 = 0;
    result = MiLockWorkingSetShared(v_stack_p58, (uint32_t)((uint32_t)((uint32_t)(v_stack_p30))), (uint32_t)((uint32_t)(result)), (uint32_t)(v_stack_p34));
    goto loc_0032C836;
loc_0032D45E:
    Arg4 = (*(uint64_t *)(result)) - 1;
    Arg4 = (Arg4) >> (12);
    goto loc_0032C71E;
loc_0032D473:
    if (*(uint64_t *)(v_stack_p58) == 0) goto loc_0032C836;
    goto loc_0032CACF;
loc_0032D484:
    Arg1 = (*(uint8_t *)(v_stack_p20 + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x18)));
    result = (local_rdi) - (Arg1);
    if (result > Arg4) goto loc_0032D1CC;
    Arg1 = (Arg1) - (local_rdi);
    result = (Arg1 + 1) + (Arg4);
    if (0 > result) { local_r10 = result; }
    v_stack_p48 = local_r10;
    goto loc_0032D1D9;
loc_0032D4C2:
    goto loc_0032D2A0;
loc_0032D4CD:
loc_0032D4D0:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p30)))) >> (12);
    Arg1 = (Arg1) & (result);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xB007F8))) goto loc_0032D50D;
    result = (Arg1 + Arg1 * 2) << (4);
    Arg3 = (1) + (result);
    if (condition_is_below) goto loc_0032D664;
loc_0032D50D:
    Arg1 = (Arg1) >> (18);
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB02BAC) + Arg1 * 8))) >> (4);
loc_0032D524:
    result = (uint16_t)((result) & ((uint16_t)((uint32_t)(0x7FFULL))));
    v_stack_p8 = (uint16_t)(result);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x30))))) & (112));
    if (((uint8_t)(result)) != 48) goto loc_0032D647;
loc_0032D546:
    result = MiGetProtectionFromPte(v_stack_p20, (uint32_t)((uint32_t)((uint32_t)(v_stack_p30))), Arg3, Arg4);
loc_0032D550:
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)((uint32_t)(result)));
loc_0032D55E:
    result = 0;
    v_stack_p34 = 0;
    result = MiUnlockPageTable(v_stack_p58, v_stack_p50, Arg3, Arg4);
    *(uint32_t *)(arg7) = (uint32_t)((uint32_t)(v_stack_p34));
    *(uint16_t *)(arg8) = (uint16_t)(v_stack_p8);
    result = MiGetLeafVa(result + 8, v_stack_p50, Arg3, Arg4);
    *(uint64_t *)(arg9) = result;
    goto loc_0032CA71;
loc_0032D5AC:
    result = MiIsLazyStampedPte(v_stack_p50, v_stack_p50, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0032D3BA;
    local_r10 = 0;
    goto loc_0032C64D;
loc_0032D5C7:
    result = MiIsLazyStampedPte(0, v_stack_p50, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0032C7E0;
    goto loc_0032C66C;
loc_0032D5DF:
    if (*(uint64_t *)(v_rip + 0xB0069A) == 0) goto loc_0032D4D0;
    if ((((uint8_t)(v_stack_p50)) & (16)) != 0) goto loc_0032D62B;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xB0069A));
    Arg1 = (Arg1) & (v_stack_p50);
    goto loc_0032D4D0;
loc_0032D605:
loc_0032D608:
    local_rsi = (result) >> (9);
    local_rsi = (local_rsi) & (Arg4);
    local_rsi = (local_rsi) + (Arg3);
    Arg1 = (v_stack_p50 - 1) - (1);
    if (condition_is_equal) goto loc_0032D373;
    goto loc_0032D608;
loc_0032D621:
    goto loc_0032D018;
loc_0032D62B:
    Arg1 = (Arg1) & (-17);
    goto loc_0032D4D0;
loc_0032D634:
    v_stack_p38 = Arg3 + local_rdi * 8;
    goto loc_0032D205;
loc_0032D647:
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg3 + local_rdi * 8))) & (0xA00000ULL));
    if (((uint32_t)(result)) == 0xA00000ULL) goto loc_0032D546;
    Arg1 = (uint32_t)((Arg3 + local_rdi * 8) >> (7));
    Arg1 = (uint32_t)((Arg1) & (31));
    goto loc_0032D550;
loc_0032D664:
    result = (*(uint64_t *)(Arg3)) >> (43);
    goto loc_0032D524;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `32` | `W` |
| `Arg7` | `+ 0x0` | `32` | `W` |
| `Arg8` | `+ 0x0` | `16` | `W` |
| `Arg9` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0032C380&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
