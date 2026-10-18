# MiGetPageChain

- RVA: `0x00330130`–`0x003308C0` (길이 `1,936` bytes)
- VA: `0x0000000140330130`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076530`
- 디코드: `479`개 명령, `1,936/1,936` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x0033027F` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x00330339` → [MiZeroPhysicalPage](MiZeroPhysicalPage_function_00332590.md) (function, `0x00332590`)
- `0x00330354` → [MiSetPfnTbFlushStamp](../2B/MiSetPfnTbFlushStamp_function_002B7A70.md) (function, `0x002B7A70`)
- `0x00330470` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00330513` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x0033052D` → [MiGetPageChainSmallPageProcess](../2B/MiGetPageChainSmallPageProcess_function_002B7850.md) (function, `0x002B7850`)
- `0x0033054A` → [MiGetPageChainYield](../46/MiGetPageChainYield_function_00466C3C.md) (function, `0x00466C3C`)
- `0x0033058E` → [MiGetLargePagesForChain](../31/MiGetLargePagesForChain_function_0031DF88.md) (function, `0x0031DF88`)
- `0x003305AD` → [MiGetPageChainYield](../46/MiGetPageChainYield_function_00466C3C.md) (function, `0x00466C3C`)
- `0x003305D6` → [MiPageAvailable](../2A/MiPageAvailable_function_002A3138.md) (function, `0x002A3138`)
- `0x0033061E` → [MiGetSlabPage](../37/MiGetSlabPage_function_00376FBC.md) (function, `0x00376FBC`)
- `0x0033065E` → [MiMakeLinkedListPte](../2C/MiMakeLinkedListPte_function_002C98C0.md) (function, `0x002C98C0`)
- `0x0033068F` → [MiPerformFinalZeroing](../4F/MiPerformFinalZeroing_function_004F9594.md) (function, `0x004F9594`)
- `0x00330703` → [MiZeroPhysicalPage](MiZeroPhysicalPage_function_00332590.md) (function, `0x00332590`)
- `0x0033070D` → [MiMakeLinkedListPte](../2C/MiMakeLinkedListPte_function_002C98C0.md) (function, `0x002C98C0`)
- `0x00330736` → [MiTbFlushTimeStampMayNeedFlush](../45/MiTbFlushTimeStampMayNeedFlush_function_004584B8.md) (function, `0x004584B8`)
- `0x0033074C` → [MiChangePageAttribute](MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x0033076B` → [MiWorkingSetIsContended](../2A/MiWorkingSetIsContended_function_002AE520.md) (function, `0x002AE520`)
- `0x00330778` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x003307AB` → [MiChangePageAttributeBatch](../2A/MiChangePageAttributeBatch_function_002A06E0.md) (function, `0x002A06E0`)
- `0x003307D8` → [MiChangePageAttributeBatch](../2A/MiChangePageAttributeBatch_function_002A06E0.md) (function, `0x002A06E0`)
- `0x003307FB` → [MiPageToNode](MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x0033081D` → [MiSwapNumaStandbyPage](../38/MiSwapNumaStandbyPage_function_00385144.md) (function, `0x00385144`)
- `0x00330877` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x003308A9` → [MiPerformFinalZeroing](../4F/MiPerformFinalZeroing_function_004F9594.md) (function, `0x004F9594`)
- `0x003308B6` → [MiPerformFinalZeroing](../4F/MiPerformFinalZeroing_function_004F9594.md) (function, `0x004F9594`)

### Direct callers
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B3B06`
- [MiCreateSharedZeroPages](../2B/MiCreateSharedZeroPages_function_002B6318.md) at `0x002B6440`
- [MiGetPoolPages](../32/MiGetPoolPages_function_00327D3C.md) at `0x00327E7D`
- [sub_0032FBA9](../32/Unknown_function_0032FBA9.md) at `0x0032FDF0`
- [MiGetHardFaultPages](../36/MiGetHardFaultPages_function_0036200C.md) at `0x0036212F`
- [MiResolvePageFileFault](../36/MiResolvePageFileFault_function_0036D968.md) at `0x0036E59C`
- [MiGetClusterPage](../4D/MiGetClusterPage_function_004DC57C.md) at `0x004DC9EE`
- [MiPfPrepareSequentialReadList](../../page/93/MiPfPrepareSequentialReadList_function_0093D8E8.md) at `0x0093DA6D`

### Static image references
- `0x0033014F` → RVA `0x00E0A740` (`.data`; read)
- `0x003301AD` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x003301B4` → RVA `0x00E2CB40` (`.data`; read)
- `0x003301C9` → RVA `0x00E2DBD0` (`.data`; read)
- `0x0033064D` → RVA `0x00E2DCD8` (`.data`; reference)
- `0x0033072A` → RVA `0x00FCF080` (`CACHEALI`; read)
- `0x003307A4` → RVA `0x00010880` (`.rdata`; read)
- `0x00330836` → RVA `0x00E2DCCC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00330130  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00330135  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
0033013A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0033013F  57                              push rdi
00330140  41 54                           push r12
00330142  41 55                           push r13
00330144  41 56                           push r14
00330146  41 57                           push r15
00330148  48 81 EC 80 00 00 00            sub rsp, 0x80
0033014F  48 8B 05 EA A5 AD 00            mov rax, qword ptr [rip + 0xada5ea]
00330156  48 33 C4                        xor rax, rsp
00330159  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0033015E  48 8B 41 48                     mov rax, qword ptr [rcx + 0x48]
00330162  45 33 ED                        xor r13d, r13d
00330165  4C 8B E1                        mov r12, rcx
00330168  48 85 C0                        test rax, rax
0033016B  74 03                           je 0x140330170
0033016D  4C 89 28                        mov qword ptr [rax], r13
00330170  8B 49 30                        mov ecx, dword ptr [rcx + 0x30]
00330173  4D 8D 7C 24 38                  lea r15, [r12 + 0x38]
00330178  41 8B 5C 24 20                  mov ebx, dword ptr [r12 + 0x20]
0033017D  48 B8 FF FF FF FF 7F 00 00 00   movabs rax, 0x7fffffffff
00330187  C1 E9 09                        shr ecx, 9
0033018A  41 8B F5                        mov esi, r13d
0033018D  8B E9                           mov ebp, ecx
0033018F  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00330194  83 E5 3F                        and ebp, 0x3f
00330197  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
0033019C  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003301A1  45 8B F5                        mov r14d, r13d
003301A4  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
003301A9  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
003301AD  0F B7 05 4C 4E C9 00            movzx eax, word ptr [rip + 0xc94e4c]
003301B4  4C 8D 0D 85 C9 AF 00            lea r9, [rip + 0xafc985]
003301BB  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
003301C0  44 3B F0                        cmp r14d, eax
003301C3  0F 83 E7 02 00 00               jae 0x1403304b0
003301C9  48 8B 15 00 DA AF 00            mov rdx, qword ptr [rip + 0xafda00]
003301D0  83 E6 FE                        and esi, 0xfffffffe
003301D3  0F AF C5                        imul eax, ebp
003301D6  41 03 C6                        add eax, r14d
003301D9  8B 14 82                        mov edx, dword ptr [rdx + rax*4]
003301DC  8B CA                           mov ecx, edx
003301DE  41 8B 44 24 30                  mov eax, dword ptr [r12 + 0x30]
003301E3  C1 E1 09                        shl ecx, 9
003301E6  33 C8                           xor ecx, eax
003301E8  81 E1 00 7E 00 00               and ecx, 0x7e00
003301EE  33 C8                           xor ecx, eax
003301F0  41 89 4C 24 30                  mov dword ptr [r12 + 0x30], ecx
003301F5  41 8B 44 24 1C                  mov eax, dword ptr [r12 + 0x1c]
003301FA  83 E0 0F                        and eax, 0xf
003301FD  3C 09                           cmp al, 9
003301FF  75 1E                           jne 0x14033021f
00330201  49 83 3F FF                     cmp qword ptr [r15], -1
00330205  0F 85 E5 05 00 00               jne 0x1403307f0
0033020B  49 8B 4C 24 50                  mov rcx, qword ptr [r12 + 0x50]
00330210  49 2B 4C 24 68                  sub rcx, qword ptr [r12 + 0x68]
00330215  48 83 F9 10                     cmp rcx, 0x10
00330219  0F 83 69 03 00 00               jae 0x140330588
0033021F  40 F6 C6 01                     test sil, 1
00330223  0F 85 70 04 00 00               jne 0x140330699
00330229  41 8B 4C 24 30                  mov ecx, dword ptr [r12 + 0x30]
0033022E  B8 01 00 00 00                  mov eax, 1
00330233  49 8B 54 24 28                  mov rdx, qword ptr [r12 + 0x28]
00330238  F0 0F C1 02                     lock xadd dword ptr [rdx], eax
0033023C  33 D2                           xor edx, edx
0033023E  44 8B C1                        mov r8d, ecx
00330241  49 C1 E8 10                     shr r8, 0x10
00330245  41 83 E0 03                     and r8d, 3
00330249  43 F7 B4 81 80 11 00 00         div dword ptr [r9 + r8*4 + 0x1180]
00330251  49 8B 07                        mov rax, qword ptr [r15]
00330254  33 D1                           xor edx, ecx
00330256  0F B6 FA                        movzx edi, dl
00330259  33 F9                           xor edi, ecx
0033025B  48 83 F8 FF                     cmp rax, -1
0033025F  0F 85 D1 05 00 00               jne 0x140330836
00330265  41 8B 54 24 1C                  mov edx, dword ptr [r12 + 0x1c]
0033026A  83 E2 0F                        and edx, 0xf
0033026D  83 FA 09                        cmp edx, 9
00330270  0F 85 7C 03 00 00               jne 0x1403305f2
00330276  49 8B 0C 24                     mov rcx, qword ptr [r12]
0033027A  44 8B C3                        mov r8d, ebx
0033027D  8B D7                           mov edx, edi
0033027F  E8 3C 82 F5 FF                  call 0x1402884c0
00330284  4C 8B E8                        mov r13, rax
00330287  48 83 F8 FF                     cmp rax, -1
0033028B  0F 84 06 02 00 00               je 0x140330497
00330291  8B CB                           mov ecx, ebx
00330293  83 CB 40                        or ebx, 0x40
00330296  49 83 3F FF                     cmp qword ptr [r15], -1
0033029A  0F 44 D9                        cmove ebx, ecx
0033029D  0F BA E3 11                     bt ebx, 0x11
003302A1  0F 92 C1                        setb cl
003302A4  40 F6 C6 02                     test sil, 2
003302A8  0F 94 C0                        sete al
003302AB  84 C8                           test al, cl
003302AD  0F 85 45 05 00 00               jne 0x1403307f8
003302B3  45 8B 7C 24 30                  mov r15d, dword ptr [r12 + 0x30]
003302B8  4A 8D 3C 6D 00 00 00 00         lea rdi, [r13*2]
003302C0  45 8B 44 24 20                  mov r8d, dword ptr [r12 + 0x20]
003302C5  49 03 FD                        add rdi, r13
003302C8  41 C1 EF 12                     shr r15d, 0x12
003302CC  41 83 E7 03                     and r15d, 3
003302D0  48 C1 E7 04                     shl rdi, 4
003302D4  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003302DE  48 8B C0                        mov rax, rax
003302E1  48 03 F8                        add rdi, rax
003302E4  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
003302E7  C1 E8 10                        shr eax, 0x10
003302EA  0F B6 C8                        movzx ecx, al
003302ED  C1 E9 06                        shr ecx, 6
003302F0  41 3B CF                        cmp ecx, r15d
003302F3  0F 85 46 03 00 00               jne 0x14033063f
003302F9  41 8B C0                        mov eax, r8d
003302FC  C7 44 24 30 00 00 00 00         mov dword ptr [rsp + 0x30], 0
00330304  83 E0 01                        and eax, 1
00330307  44 8B C8                        mov r9d, eax
0033030A  41 C1 E1 04                     shl r9d, 4
0033030E  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
00330313  44 8D 14 00                     lea r10d, [rax + rax]
00330317  44 89 54 24 44                  mov dword ptr [rsp + 0x44], r10d
0033031C  41 F6 C0 20                     test r8b, 0x20
00330320  74 49                           je 0x14033036b
00330322  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00330326  48 A9 E0 03 00 00               test rax, 0x3e0
0033032C  74 3D                           je 0x14033036b
0033032E  45 8B CF                        mov r9d, r15d
00330331  45 8B C2                        mov r8d, r10d
00330334  49 8B D5                        mov rdx, r13
00330337  33 C9                           xor ecx, ecx
00330339  E8 52 22 00 00                  call 0x140332590
0033033E  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00330342  45 33 C0                        xor r8d, r8d
00330345  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
0033034B  33 D2                           xor edx, edx
0033034D  48 8B CF                        mov rcx, rdi
00330350  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00330354  E8 17 77 F8 FF                  call 0x1402b7a70
00330359  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
0033035E  44 8B 54 24 44                  mov r10d, dword ptr [rsp + 0x44]
00330363  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
0033036B  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
0033036E  C1 E8 10                        shr eax, 0x10
00330371  0F B6 C8                        movzx ecx, al
00330374  C1 E9 06                        shr ecx, 6
00330377  41 3B CF                        cmp ecx, r15d
0033037A  0F 85 55 03 00 00               jne 0x1403306d5
00330380  83 7C 24 30 00                  cmp dword ptr [rsp + 0x30], 0
00330385  75 40                           jne 0x1403303c7
00330387  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0033038B  49 B9 FF FF FF FF FF FF FF C7   movabs r9, 0xc7ffffffffffffff
00330395  48 8B CA                        mov rcx, rdx
00330398  48 8B C2                        mov rax, rdx
0033039B  49 23 C9                        and rcx, r9
0033039E  F0 48 0F B1 4F 18               lock cmpxchg qword ptr [rdi + 0x18], rcx
003303A4  4C 8B C0                        mov r8, rax
003303A7  48 3B D0                        cmp rdx, rax
003303AA  74 1B                           je 0x1403303c7
003303AC  0F 1F 40 00                     nop dword ptr [rax]
003303B0  49 8B C8                        mov rcx, r8
003303B3  4D 23 C1                        and r8, r9
003303B6  48 8B C1                        mov rax, rcx
003303B9  F0 4C 0F B1 47 18               lock cmpxchg qword ptr [rdi + 0x18], r8
003303BF  4C 8B C0                        mov r8, rax
003303C2  48 3B C8                        cmp rcx, rax
003303C5  75 E9                           jne 0x1403303b0
003303C7  49 8B 44 24 58                  mov rax, qword ptr [r12 + 0x58]
003303CC  48 89 07                        mov qword ptr [rdi], rax
003303CF  49 83 7C 24 60 00               cmp qword ptr [r12 + 0x60], 0
003303D5  49 89 7C 24 58                  mov qword ptr [r12 + 0x58], rdi
003303DA  75 05                           jne 0x1403303e1
003303DC  49 89 7C 24 60                  mov qword ptr [r12 + 0x60], rdi
003303E1  49 FF 44 24 68                  inc qword ptr [r12 + 0x68]
003303E6  49 8B 44 24 68                  mov rax, qword ptr [r12 + 0x68]
003303EB  49 3B 44 24 50                  cmp rax, qword ptr [r12 + 0x50]
003303F0  0F 85 6D 01 00 00               jne 0x140330563
003303F6  45 33 ED                        xor r13d, r13d
003303F9  41 8B FD                        mov edi, r13d
003303FC  48 BE FF FF FF FF 7F 00 00 00   movabs rsi, 0x7fffffffff
00330406  8B C7                           mov eax, edi
00330408  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0033040D  48 C1 E0 04                     shl rax, 4
00330411  48 03 C8                        add rcx, rax
00330414  48 39 31                        cmp qword ptr [rcx], rsi
00330417  0F 85 6D 03 00 00               jne 0x14033078a
0033041D  44 8D 4F 01                     lea r9d, [rdi + 1]
00330421  41 8B C1                        mov eax, r9d
00330424  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00330429  48 C1 E0 04                     shl rax, 4
0033042D  48 03 C8                        add rcx, rax
00330430  48 39 31                        cmp qword ptr [rcx], rsi
00330433  0F 85 7C 03 00 00               jne 0x1403307b5
00330439  83 C7 02                        add edi, 2
0033043C  83 FF 02                        cmp edi, 2
0033043F  72 C5                           jb 0x140330406
00330441  49 8B 54 24 58                  mov rdx, qword ptr [r12 + 0x58]
00330446  48 85 D2                        test rdx, rdx
00330449  74 1D                           je 0x140330468
0033044B  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
0033044F  41 8B CD                        mov ecx, r13d
00330452  48 0F BA E0 28                  bt rax, 0x28
00330457  0F 82 85 03 00 00               jb 0x1403307e2
0033045D  89 4A 24                        mov dword ptr [rdx + 0x24], ecx
00330460  48 8B 12                        mov rdx, qword ptr [rdx]
00330463  48 85 D2                        test rdx, rdx
00330466  75 E3                           jne 0x14033044b
00330468  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0033046D  48 33 CC                        xor rcx, rsp
00330470  E8 CB C1 37 00                  call 0x1406ac640
00330475  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
0033047D  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00330481  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
00330485  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00330489  49 8B E3                        mov rsp, r11
0033048C  41 5F                           pop r15
0033048E  41 5E                           pop r14
00330490  41 5D                           pop r13
00330492  41 5C                           pop r12
00330494  5F                              pop rdi
00330495  C3                              ret
00330496  CC                              int3
00330497  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
0033049C  0F BA E0 0C                     bt eax, 0xc
003304A0  0F 83 20 01 00 00               jae 0x1403305c6
003304A6  4C 8D 0D 93 C6 AF 00            lea r9, [rip + 0xafc693]
003304AD  45 33 ED                        xor r13d, r13d
003304B0  0F BA E3 10                     bt ebx, 0x10
003304B4  0F 83 3F FF FF FF               jae 0x1403303f9
003304BA  41 8B 44 24 30                  mov eax, dword ptr [r12 + 0x30]
003304BF  0F BA F3 10                     btr ebx, 0x10
003304C3  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
003304C7  0F BA EB 12                     bts ebx, 0x12
003304CB  C1 E1 09                        shl ecx, 9
003304CE  33 C8                           xor ecx, eax
003304D0  81 E1 00 7E 00 00               and ecx, 0x7e00
003304D6  33 C8                           xor ecx, eax
003304D8  41 89 4C 24 30                  mov dword ptr [r12 + 0x30], ecx
003304DD  41 8B 4C 24 30                  mov ecx, dword ptr [r12 + 0x30]
003304E2  B8 01 00 00 00                  mov eax, 1
003304E7  49 8B 54 24 28                  mov rdx, qword ptr [r12 + 0x28]
003304EC  F0 0F C1 02                     lock xadd dword ptr [rdx], eax
003304F0  33 D2                           xor edx, edx
003304F2  44 8B C1                        mov r8d, ecx
003304F5  49 C1 E8 10                     shr r8, 0x10
003304F9  41 83 E0 03                     and r8d, 3
003304FD  43 F7 B4 81 80 11 00 00         div dword ptr [r9 + r8*4 + 0x1180]
00330505  44 8B C3                        mov r8d, ebx
00330508  33 D1                           xor edx, ecx
0033050A  0F B6 D2                        movzx edx, dl
0033050D  33 D1                           xor edx, ecx
0033050F  49 8B 0C 24                     mov rcx, qword ptr [r12]
00330513  E8 A8 7F F5 FF                  call 0x1402884c0
00330518  48 83 F8 FF                     cmp rax, -1
0033051C  0F 84 D7 FE FF FF               je 0x1403303f9
00330522  4C 8B C0                        mov r8, rax
00330525  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
0033052A  49 8B CC                        mov rcx, r12
0033052D  E8 1E 73 F8 FF                  call 0x1402b7850
00330532  49 8B 44 24 50                  mov rax, qword ptr [r12 + 0x50]
00330537  49 39 44 24 68                  cmp qword ptr [r12 + 0x68], rax
0033053C  0F 84 B7 FE FF FF               je 0x1403303f9
00330542  BA 10 00 00 00                  mov edx, 0x10
00330547  49 8B CC                        mov rcx, r12
0033054A  E8 ED 66 13 00                  call 0x140466c3c
0033054F  4C 8D 0D EA C5 AF 00            lea r9, [rip + 0xafc5ea]
00330556  85 C0                           test eax, eax
00330558  0F 85 9B FE FF FF               jne 0x1403303f9
0033055E  E9 7A FF FF FF                  jmp 0x1403304dd
00330563  A8 0F                           test al, 0xf
00330565  75 0D                           jne 0x140330574
00330567  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
0033056C  A8 01                           test al, 1
0033056E  0F 85 E2 01 00 00               jne 0x140330756
00330574  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
00330579  4C 8D 0D C0 C5 AF 00            lea r9, [rip + 0xafc5c0]
00330580  45 33 ED                        xor r13d, r13d
00330583  E9 A1 FC FF FF                  jmp 0x140330229
00330588  49 8B CC                        mov rcx, r12
0033058B  83 CE 01                        or esi, 1
0033058E  E8 F5 D9 FE FF                  call 0x14031df88
00330593  49 8B 44 24 68                  mov rax, qword ptr [r12 + 0x68]
00330598  48 85 C0                        test rax, rax
0033059B  74 1D                           je 0x1403305ba
0033059D  49 3B 44 24 50                  cmp rax, qword ptr [r12 + 0x50]
003305A2  0F 84 51 FE FF FF               je 0x1403303f9
003305A8  33 D2                           xor edx, edx
003305AA  49 8B CC                        mov rcx, r12
003305AD  E8 8A 66 13 00                  call 0x140466c3c
003305B2  85 C0                           test eax, eax
003305B4  0F 85 3F FE FF FF               jne 0x1403303f9
003305BA  4C 8D 0D 7F C5 AF 00            lea r9, [rip + 0xafc57f]
003305C1  E9 59 FC FF FF                  jmp 0x14033021f
003305C6  0F BA E3 0C                     bt ebx, 0xc
003305CA  0F 83 D6 FE FF FF               jae 0x1403304a6
003305D0  49 8B 0C 24                     mov rcx, qword ptr [r12]
003305D4  8B D0                           mov edx, eax
003305D6  E8 5D 2B F7 FF                  call 0x1402a3138
003305DB  85 C0                           test eax, eax
003305DD  0F 84 13 FE FF FF               je 0x1403303f6
003305E3  0F BA F3 0C                     btr ebx, 0xc
003305E7  41 FF C6                        inc r14d
003305EA  45 33 ED                        xor r13d, r13d
003305ED  E9 BB FB FF FF                  jmp 0x1403301ad
003305F2  49 8B 44 24 48                  mov rax, qword ptr [r12 + 0x48]
003305F7  8B CB                           mov ecx, ebx
003305F9  C1 E9 0C                        shr ecx, 0xc
003305FC  44 8B C7                        mov r8d, edi
003305FF  83 E1 01                        and ecx, 1
00330602  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
00330607  44 8B C9                        mov r9d, ecx
0033060A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0033060F  41 83 C9 10                     or r9d, 0x10
00330613  F6 C3 01                        test bl, 1
00330616  44 0F 44 C9                     cmove r9d, ecx
0033061A  49 8B 0C 24                     mov rcx, qword ptr [r12]
0033061E  E8 99 69 04 00                  call 0x140376fbc
00330623  4C 8B E8                        mov r13, rax
00330626  48 83 F8 FF                     cmp rax, -1
0033062A  0F 84 C6 FD FF FF               je 0x1403303f6
00330630  49 83 FD FF                     cmp r13, -1
00330634  0F 84 3C FC FF FF               je 0x140330276
0033063A  E9 52 FC FF FF                  jmp 0x140330291
0033063F  B8 01 00 00 00                  mov eax, 1
00330644  D2 E0                           shl al, cl
00330646  0F B6 C8                        movzx ecx, al
00330649  44 0F AB F9                     bts ecx, r15d
0033064D  84 0D 85 D6 AF 00               test byte ptr [rip + 0xafd685], cl
00330653  0F 84 A0 FC FF FF               je 0x1403302f9
00330659  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0033065E  E8 5D 92 F9 FF                  call 0x1402c98c0
00330663  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00330667  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0033066C  48 FF C0                        inc rax
0033066F  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
00330674  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00330679  48 83 F8 10                     cmp rax, 0x10
0033067D  0F 85 44 FD FF FF               jne 0x1403303c7
00330683  41 83 E0 01                     and r8d, 1
00330687  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0033068C  41 8B D7                        mov edx, r15d
0033068F  E8 00 8F 1C 00                  call 0x1404f9594
00330694  E9 2E FD FF FF                  jmp 0x1403303c7
00330699  49 8B 4C 24 50                  mov rcx, qword ptr [r12 + 0x50]
0033069E  49 2B 4C 24 68                  sub rcx, qword ptr [r12 + 0x68]
003306A3  48 83 F9 10                     cmp rcx, 0x10
003306A7  0F 82 7C FB FF FF               jb 0x140330229
003306AD  41 F7 44 24 20 00 30 00 00      test dword ptr [r12 + 0x20], 0x3000
003306B6  0F 85 6D FB FF FF               jne 0x140330229
003306BC  66 83 3D 3C 49 C9 00 01         cmp word ptr [rip + 0xc9493c], 1
003306C4  0F 86 5F FB FF FF               jbe 0x140330229
003306CA  81 CB 00 10 03 00               or ebx, 0x31000
003306D0  E9 54 FB FF FF                  jmp 0x140330229
003306D5  83 F9 01                        cmp ecx, 1
003306D8  74 12                           je 0x1403306ec
003306DA  83 F9 03                        cmp ecx, 3
003306DD  74 64                           je 0x140330743
003306DF  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
003306E3  48 C1 E9 3B                     shr rcx, 0x3b
003306E7  83 E1 07                        and ecx, 7
003306EA  75 39                           jne 0x140330725
003306EC  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003306F0  48 A9 E0 03 00 00               test rax, 0x3e0
003306F6  74 10                           je 0x140330708
003306F8  45 8B CF                        mov r9d, r15d
003306FB  45 8B C2                        mov r8d, r10d
003306FE  49 8B D5                        mov rdx, r13
00330701  33 C9                           xor ecx, ecx
00330703  E8 88 1E 00 00                  call 0x140332590
00330708  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0033070D  E8 AE 91 F9 FF                  call 0x1402c98c0
00330712  48 FF 44 24 68                  inc qword ptr [rsp + 0x68]
00330717  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
0033071B  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
00330720  E9 A2 FC FF FF                  jmp 0x1403303c7
00330725  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0033072A  8B 15 50 E9 C9 00               mov edx, dword ptr [rip + 0xc9e950]
00330730  41 B8 07 00 00 00               mov r8d, 7
00330736  E8 7D 7D 12 00                  call 0x1404584b8
0033073B  84 C0                           test al, al
0033073D  75 AD                           jne 0x1403306ec
0033073F  41 83 C9 04                     or r9d, 4
00330743  45 8B C1                        mov r8d, r9d
00330746  41 8B D7                        mov edx, r15d
00330749  48 8B CF                        mov rcx, rdi
0033074C  E8 7B 27 00 00                  call 0x140332ecc
00330751  E9 2A FC FF FF                  jmp 0x140330380
00330756  41 8B 54 24 1C                  mov edx, dword ptr [r12 + 0x1c]
0033075B  C1 EA 04                        shr edx, 4
0033075E  83 E2 03                        and edx, 3
00330761  83 FA 02                        cmp edx, 2
00330764  74 12                           je 0x140330778
00330766  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
0033076B  E8 B0 DD F7 FF                  call 0x1402ae520
00330770  85 C0                           test eax, eax
00330772  0F 85 7E FC FF FF               jne 0x1403303f6
00330778  E8 63 6C F4 FF                  call 0x1402773e0
0033077D  85 C0                           test eax, eax
0033077F  0F 84 EF FD FF FF               je 0x140330574
00330785  E9 6C FC FF FF                  jmp 0x1403303f6
0033078A  41 8B 54 24 30                  mov edx, dword ptr [r12 + 0x30]
0033078F  44 8B CB                        mov r9d, ebx
00330792  C1 EA 12                        shr edx, 0x12
00330795  41 83 E1 01                     and r9d, 1
00330799  83 E2 03                        and edx, 3
0033079C  85 FF                           test edi, edi
0033079E  0F 84 02 01 00 00               je 0x1403308a6
003307A4  4C 8B 05 D5 00 CE FF            mov r8, qword ptr [rip - 0x31ff2b]
003307AB  E8 30 FF F6 FF                  call 0x1402a06e0
003307B0  E9 68 FC FF FF                  jmp 0x14033041d
003307B5  41 8B 54 24 30                  mov edx, dword ptr [r12 + 0x30]
003307BA  8B C3                           mov eax, ebx
003307BC  C1 EA 12                        shr edx, 0x12
003307BF  83 E0 01                        and eax, 1
003307C2  83 E2 03                        and edx, 3
003307C5  45 85 C9                        test r9d, r9d
003307C8  0F 84 E5 00 00 00               je 0x1403308b3
003307CE  4C 8B 05 AB 00 CE FF            mov r8, qword ptr [rip - 0x31ff55]
003307D5  44 8B C8                        mov r9d, eax
003307D8  E8 03 FF F6 FF                  call 0x1402a06e0
003307DD  E9 57 FC FF FF                  jmp 0x140330439
003307E2  8B 4A 24                        mov ecx, dword ptr [rdx + 0x24]
003307E5  81 E1 00 00 00 18               and ecx, 0x18000000
003307EB  E9 6D FC FF FF                  jmp 0x14033045d
003307F0  83 CB 40                        or ebx, 0x40
003307F3  E9 27 FA FF FF                  jmp 0x14033021f
003307F8  49 8B CD                        mov rcx, r13
003307FB  E8 D0 84 00 00                  call 0x140338cd0
00330800  3B C5                           cmp eax, ebp
00330802  0F 84 AB FA FF FF               je 0x1403302b3
00330808  45 8B 4C 24 20                  mov r9d, dword ptr [r12 + 0x20]
0033080D  45 33 C0                        xor r8d, r8d
00330810  41 0F BA E9 0C                  bts r9d, 0xc
00330815  8B D5                           mov edx, ebp
00330817  49 8B CD                        mov rcx, r13
0033081A  49 8B FD                        mov rdi, r13
0033081D  E8 22 49 05 00                  call 0x140385144
00330822  4C 8B E8                        mov r13, rax
00330825  48 3B C7                        cmp rax, rdi
00330828  0F 85 85 FA FF FF               jne 0x1403302b3
0033082E  83 CE 02                        or esi, 2
00330831  E9 7D FA FF FF                  jmp 0x1403302b3
00330836  8B 0D 90 D4 AF 00               mov ecx, dword ptr [rip + 0xafd490]
0033083C  41 BF 0F 00 00 00               mov r15d, 0xf
00330842  49 3B CF                        cmp rcx, r15
00330845  44 8B C3                        mov r8d, ebx
00330848  44 0F 42 F9                     cmovb r15d, ecx
0033084C  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00330851  49 23 C7                        and rax, r15
00330854  33 D2                           xor edx, edx
00330856  48 89 01                        mov qword ptr [rcx], rax
00330859  8B CF                           mov ecx, edi
0033085B  48 C1 E9 10                     shr rcx, 0x10
0033085F  83 E1 03                        and ecx, 3
00330862  41 F7 B4 89 80 11 00 00         div dword ptr [r9 + rcx*4 + 0x1180]
0033086A  49 8B 0C 24                     mov rcx, qword ptr [r12]
0033086E  33 D7                           xor edx, edi
00330870  0F B6 C2                        movzx eax, dl
00330873  33 F8                           xor edi, eax
00330875  8B D7                           mov edx, edi
00330877  E8 44 7C F5 FF                  call 0x1402884c0
0033087C  4C 8B E8                        mov r13, rax
0033087F  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00330884  48 8B 08                        mov rcx, qword ptr [rax]
00330887  48 FF C1                        inc rcx
0033088A  49 23 CF                        and rcx, r15
0033088D  4C 8B F8                        mov r15, rax
00330890  48 89 08                        mov qword ptr [rax], rcx
00330893  8B CB                           mov ecx, ebx
00330895  83 E1 BF                        and ecx, 0xffffffbf
00330898  49 83 FD FF                     cmp r13, -1
0033089C  0F 45 CB                        cmovne ecx, ebx
0033089F  8B D9                           mov ebx, ecx
003308A1  E9 8A FD FF FF                  jmp 0x140330630
003308A6  45 8B C1                        mov r8d, r9d
003308A9  E8 E6 8C 1C 00                  call 0x1404f9594
003308AE  E9 6A FB FF FF                  jmp 0x14033041d
003308B3  44 8B C0                        mov r8d, eax
003308B6  E8 D9 8C 1C 00                  call 0x1404f9594
003308BB  E9 79 FB FF FF                  jmp 0x140330439
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetPageChain(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 11380202)) ^ (v_rsp);
    v_stack_m38 = result;
    v_r13 = 0;
    if (*(unsigned __int64 *)(a1 + 72) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) = 0;
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) >> (9));
    v_stack_m58 = *(unsigned __int64 *)(a1 + 72);
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (63));
    v_stack_m50 = 0;
    v_stack_m48 = *(unsigned __int64 *)(a1 + 72);
    v_stack_m40 = 0;
    v_stack_m60 = (unsigned int)(a1);
loc_003301AD:
    v_stack_m70 = a1 + 56;
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 13192780)))) goto loc_003304B0;
    v_rsi = (unsigned int)((0) & (0xFFFFFFFEULL));
    result = (unsigned int)((*(unsigned __int16 *)(v_rip + 13192780)) * ((unsigned int)(v_rbp)));
    result = (unsigned int)((result) + (0));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11524608) + result * 4))))) << (9));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))));
    a1 = (unsigned int)((a1) & (0x7E00ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))));
    *(unsigned int *)(a1 + 48) = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 28))) & (15));
    if (((unsigned __int8)(result)) != 9) goto loc_0033021F;
    if ((*(unsigned __int64 *)(a1 + 56)) != -1) goto loc_003307F0;
    a1 = (*(unsigned __int64 *)(a1 + 80)) - (*(unsigned __int64 *)(a1 + 104));
    if (a1 >= 16) goto loc_00330588;
loc_0033021F:
    if ((((unsigned __int8)(v_rsi)) & (1)) != 0) goto loc_00330699;
loc_00330229:
    a2 = 0;
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) >> (16);
    a3 = (unsigned int)((a3) & (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))));
    v_rdi = (unsigned int)(((unsigned __int8)(a2)) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))));
    if ((*(unsigned __int64 *)(a1 + 56)) != -1) goto loc_00330836;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 28))) & (15));
    if (((unsigned int)(a2)) != 9) goto loc_003305F2;
loc_00330276:
    result = MiGetPage(*(unsigned __int64 *)(a1), (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))), v_rip + 11520389);
    if (result == -1) goto loc_00330497;
loc_00330291:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) | (64));
    if ((*(unsigned __int64 *)(a1 + 56)) == -1) { v_rbx = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))); }
    a1 = ((*(unsigned __int64 *)(a1 + 56)) < -1) ? 1 : 0;
    result = ((((unsigned __int8)(v_rsi)) & (2)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_003307F8;
loc_003302B3:
    v_rdi = (result * 2) + (result);
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) >> (18));
    v_r15 = (unsigned int)((v_r15) & (3));
    v_rdi = (v_rdi) << (4);
    v_rdi = (v_rdi) + (result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(a1)) != ((unsigned int)(v_r15))) goto loc_0033063F;
loc_003302F9:
    v_stack_m78 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))) & (1));
    a4 = (unsigned int)(((unsigned int)((unsigned int)(result))) << (4));
    v_stack_m68 = (unsigned int)(a4);
    v_stack_m64 = (unsigned int)(result + result * 1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 32)))) & (32)) == 0) goto loc_0033036B;
    result = *(unsigned __int64 *)(v_rdi + 16);
    v_r10 = result + result * 1;
    if (((*(unsigned __int64 *)(v_rdi + 16)) & (992)) != 0) {
        a4 = (unsigned int)(v_r15);
        a3 = (unsigned int)(result + result * 1);
        a2 = result;
        a1 = 0;
        result = MiZeroPhysicalPage(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(v_rdi + 16);
        a3 = 0;
        result = (result) & (-993);
        a2 = 0;
        a1 = v_rdi;
        *(unsigned __int64 *)(v_rdi + 16) = result;
        result = MiSetPfnTbFlushStamp(a1, a2, a3, a4);
        a4 = v_stack_m68;
        v_r10 = v_stack_m64;
        v_stack_m78 = 1;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(a1)) != ((unsigned int)(v_r15))) goto loc_003306D5;
loc_00330380:
    if (v_stack_m78 != 0) goto loc_003303C7;
    a1 = (*(unsigned __int64 *)(v_rdi + 24)) & (a4);
    if ((*(unsigned __int64 *)(v_rdi + 24)) == (*(unsigned __int64 *)(v_rdi + 24))) goto loc_003303C7;
loc_003303B0:
    a3 = (*(unsigned __int64 *)(v_rdi + 24)) & (a4);
    if ((*(unsigned __int64 *)(v_rdi + 24)) != (*(unsigned __int64 *)(v_rdi + 24))) goto loc_003303B0;
loc_003303C7:
    *(unsigned __int64 *)(v_rdi) = *(unsigned __int64 *)(a1 + 88);
    *(unsigned __int64 *)(a1 + 88) = v_rdi;
    if ((*(unsigned __int64 *)(a1 + 96)) == 0) {
        *(unsigned __int64 *)(a1 + 96) = v_rdi;
    }
    if ((*(unsigned __int64 *)(a1 + 104)) != (*(unsigned __int64 *)(a1 + 80))) goto loc_00330563;
loc_003303F6:
    v_r13 = 0;
loc_003303F9:
loc_00330406:
    result = (0) << (4);
    a1 = (v_stack_m58) + (result);
    if ((*(unsigned __int64 *)(a1)) != v_rsi) goto loc_0033078A;
loc_0033041D:
    result = ((unsigned int)((unsigned int)(0 + 1))) << (4);
    a1 = (v_stack_m58) + (result);
    if ((*(unsigned __int64 *)(a1)) != v_rsi) goto loc_003307B5;
loc_00330439:
    v_rdi = (unsigned int)((0) + (2));
    if (((unsigned int)(v_rdi)) < 2) goto loc_00330406;
    if (*(unsigned __int64 *)(a1 + 88) == 0) goto loc_00330468;
loc_0033044B:
    if (condition_is_below) goto loc_003307E2;
loc_0033045D:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 88) + 36) = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88)) != 0) goto loc_0033044B;
loc_00330468:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88)), *(unsigned __int64 *)(v_rdi + 24), 0 + 1);
    return result;
loc_00330497:
    if (condition_is_above_or_equal) goto loc_003305C6;
loc_003304A6:
    v_r13 = 0;
loc_003304B0:
    if (condition_is_above_or_equal) goto loc_003303F9;
    a1 = (unsigned int)(((unsigned int)(v_stack_m38)) << (9));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))));
    a1 = (unsigned int)((a1) & (0x7E00ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))));
    *(unsigned int *)(a1 + 48) = (unsigned int)(a1);
loc_003304DD:
    a2 = 0;
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) >> (16);
    a3 = (unsigned int)((a3) & (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))));
    a2 = (unsigned int)(((unsigned __int8)(a2)) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))));
    result = MiGetPage(*(unsigned __int64 *)(a1), a2, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56))), v_rip + 11519635);
    if (result == -1) goto loc_003303F9;
    result = MiGetPageChainSmallPageProcess(a1, v_stack_m30, result, v_rip + 11519635);
    if ((*(unsigned __int64 *)(a1 + 104)) == (*(unsigned __int64 *)(a1 + 80))) goto loc_003303F9;
    result = MiGetPageChainYield(a1, 16, result, v_rip + 11519635);
    if ((unsigned int)(result) != 0) goto loc_003303F9;
    goto loc_003304DD;
loc_00330563:
    if ((((unsigned __int8)(result)) & (15)) != 0) goto loc_00330574;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 32)))) & (1)) != 0) goto loc_00330756;
loc_00330574:
    v_r13 = 0;
    goto loc_00330229;
loc_00330588:
    v_rsi = (unsigned int)((*(unsigned __int64 *)(v_stack_m28 + 72)) | (1));
    result = MiGetLargePagesForChain(a1, 16, result, v_rip + 11519424);
    if (*(unsigned __int64 *)(a1 + 104) == 0) goto loc_003305BA;
    if ((*(unsigned __int64 *)(a1 + 104)) == (*(unsigned __int64 *)(a1 + 80))) goto loc_003303F9;
    a2 = 0;
    result = MiGetPageChainYield(a1, a2, result, v_rip + 11519424);
    if ((unsigned int)(result) != 0) goto loc_003303F9;
loc_003305BA:
    goto loc_0033021F;
loc_003305C6:
    if (condition_is_above_or_equal) goto loc_003304A6;
    result = MiPageAvailable(*(unsigned __int64 *)(a1), (unsigned int)((unsigned int)(result)), result, v_rip + 11519359);
    if ((unsigned int)(result) == 0) goto loc_003303F6;
    v_r14 = (unsigned int)((0) + 1);
    v_r13 = 0;
    goto loc_003301AD;
loc_003305F2:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) >> (12));
    a1 = (unsigned int)((a1) & (1));
    v_stack_m58 = 0;
    v_stack_m60 = *(unsigned __int64 *)(a1 + 72);
    a4 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (16));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 56))) & (1)) == 0) { a4 = (unsigned int)(a1); }
    result = MiGetSlabPage(*(unsigned __int64 *)(a1), (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_rdi)), a4);
    if (result == -1) goto loc_003303F6;
loc_00330630:
    if (result == -1) goto loc_00330276;
    goto loc_00330291;
loc_0033063F:
    result = (unsigned __int8)((1) << ((unsigned __int8)(*(unsigned __int64 *)(a1))));
    if (((*(unsigned __int8 *)(v_rip + 11523717)) & ((unsigned __int8)((unsigned __int8)(result)))) == 0) goto loc_003302F9;
    result = MiMakeLinkedListPte(v_stack_m30, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_rdi)), a4);
    *(unsigned __int64 *)(v_rdi + 16) = result;
    result = (v_stack_m28) + 1;
    v_stack_m30 = result;
    v_stack_m28 = result;
    if (result != 16) goto loc_003303C7;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (1));
    result = MiPerformFinalZeroing(v_stack_m30, (unsigned int)((unsigned int)(v_stack_m48)), a3, a4);
    goto loc_003303C7;
loc_00330699:
    a1 = (*(unsigned __int64 *)(a1 + 80)) - (*(unsigned __int64 *)(a1 + 104));
    if (a1 < 16) goto loc_00330229;
    if (((*(unsigned int *)(a1 + 32)) & (0x3000ULL)) != 0) goto loc_00330229;
    if ((*(unsigned __int16 *)(v_rip + 13191484)) <= 1) goto loc_00330229;
    v_rbx = (unsigned int)((*(unsigned __int64 *)(v_stack_m28 + 56)) | (0x31000ULL));
    goto loc_00330229;
loc_003306D5:
    if (((unsigned int)(a1)) == 1) goto loc_003306EC;
    if (((unsigned int)(a1)) == 3) goto loc_00330743;
    a1 = (*(unsigned __int64 *)(v_rdi + 24)) >> (59);
    a1 = (unsigned int)((a1) & (7));
    if (condition_is_not_equal) goto loc_00330725;
loc_003306EC:
    result = *(unsigned __int64 *)(v_rdi + 16);
    if (((*(unsigned __int64 *)(v_rdi + 16)) & (992)) != 0) {
        a4 = (unsigned int)(v_stack_m48);
        a3 = (unsigned int)(v_r10);
        a2 = result;
        a1 = 0;
        result = MiZeroPhysicalPage(a1, a2, a3, a4);
    }
    result = MiMakeLinkedListPte(v_stack_m20, a2, a3, a4);
    *(unsigned __int64 *)(v_rdi + 16) = result;
    v_stack_m20 = result;
    goto loc_003303C7;
loc_00330725:
    result = MiTbFlushTimeStampMayNeedFlush(v_stack_m20, (unsigned int)(*(unsigned int *)(v_rip + 13232464)), 7, a4);
    if ((unsigned __int8)(result) != 0) goto loc_003306EC;
    a4 = (unsigned int)((a4) | (4));
loc_00330743:
    result = MiChangePageAttribute(v_rdi, (unsigned int)((unsigned int)(v_stack_m48)), (unsigned int)((unsigned int)(a4)), a4);
    goto loc_00330380;
loc_00330756:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 28))) >> (4));
    a2 = (unsigned int)((a2) & (3));
    if (((unsigned int)(a2)) == 2) goto loc_00330778;
    result = MiWorkingSetIsContended(*(unsigned __int64 *)(a1 + 8), a2, (unsigned int)((unsigned int)(a4)), a4);
    if ((unsigned int)(result) != 0) goto loc_003303F6;
loc_00330778:
    result = KeShouldYieldProcessor(*(unsigned __int64 *)(a1 + 8), a2, (unsigned int)((unsigned int)(a4)), a4);
    if ((unsigned int)(result) == 0) goto loc_00330574;
    goto loc_003303F6;
loc_0033078A:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) >> (18));
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (1));
    a2 = (unsigned int)((a2) & (3));
    if ((unsigned int)(v_rdi) == 0) goto loc_003308A6;
    result = MiChangePageAttributeBatch(*(unsigned __int64 *)(a1 + 8), a2, *(unsigned __int64 *)(v_rip - 3276587), a4);
    goto loc_0033041D;
loc_003307B5:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) >> (18));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (1));
    a2 = (unsigned int)((a2) & (3));
    if ((unsigned int)(a4) == 0) goto loc_003308B3;
    result = MiChangePageAttributeBatch(*(unsigned __int64 *)(a1 + 8), a2, *(unsigned __int64 *)(v_rip - 3276629), (unsigned int)((unsigned int)(result)));
    goto loc_00330439;
loc_003307E2:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 36))) & (0x18000000ULL));
    goto loc_0033045D;
loc_003307F0:
    v_rbx = (unsigned int)((v_rbx) | (64));
    goto loc_0033021F;
loc_003307F8:
    result = MiPageToNode(result, a2, *(unsigned __int64 *)(v_rip - 3276629), (unsigned int)((unsigned int)(result)));
    if (((unsigned int)(result)) == ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)))) goto loc_003302B3;
    a3 = 0;
    result = MiSwapNumaStandbyPage(result, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), a3, (unsigned int)(*(unsigned int *)(a1 + 32)));
    if (result != result) goto loc_003302B3;
    v_rsi = (unsigned int)((v_rsi) | (2));
    goto loc_003302B3;
loc_00330836:
    v_r15 = 15;
    if (((unsigned int)(*(unsigned int *)(v_rip + 11523216))) < 15) { v_r15 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11523216))); }
    result = (result) & (v_r15);
    a2 = 0;
    *(unsigned __int64 *)(v_stack_m48) = result;
    a1 = ((unsigned int)((unsigned int)(result))) >> (16);
    a1 = (unsigned int)((a1) & (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(result)));
    v_rdi = (unsigned int)((result) ^ ((unsigned int)((unsigned __int8)(a2))));
    result = MiGetPage(*(unsigned __int64 *)(a1), (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(*(unsigned int *)(a1 + 32)));
    a1 = (*(unsigned __int64 *)(v_stack_m48)) + 1;
    a1 = (a1) & (v_r15);
    *(unsigned __int64 *)(v_stack_m48) = a1;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (0xFFFFFFBFULL));
    if (result != -1) { a1 = (unsigned int)(v_rbx); }
    goto loc_00330630;
loc_003308A6:
    result = MiPerformFinalZeroing(a1, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))), (unsigned int)(*(unsigned int *)(a1 + 32)));
    goto loc_0033041D;
loc_003308B3:
    result = MiPerformFinalZeroing(a1, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(a1 + 32)));
    goto loc_00330439;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetPageChain(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0xADA5EA)) ^ (local_rsp);
    v_stack_m38 = result;
    local_r13 = 0;
    if (*(uint64_t *)(arg1 + 0x48) != 0) {
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) = 0;
    }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) >> (9));
    v_stack_m58 = *(uint64_t *)(arg1 + 0x48);
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (63));
    v_stack_m50 = 0;
    v_stack_m48 = *(uint64_t *)(arg1 + 0x48);
    v_stack_m40 = 0;
    v_stack_m60 = (uint32_t)(Arg1);
loc_003301AD:
    v_stack_m70 = Arg1 + 56;
    if (0 >= ((uint32_t)(*(uint16_t *)(v_rip + 0xC94E4C)))) goto loc_003304B0;
    local_rsi = (uint32_t)((0) & (0xFFFFFFFEULL));
    result = (uint32_t)((*(uint16_t *)(v_rip + 0xC94E4C)) * ((uint32_t)(local_rbp)));
    result = (uint32_t)((result) + (0));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xAFDA00) + result * 4))))) << (9));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))));
    Arg1 = (uint32_t)((Arg1) & (0x7E00ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))));
    *(uint32_t *)(arg1 + 0x30) = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1C))) & (15));
    if (((uint8_t)(result)) != 9) goto loc_0033021F;
    if ((*(uint64_t *)(arg1 + 0x38)) != -1) goto loc_003307F0;
    Arg1 = (*(uint64_t *)(arg1 + 0x50)) - (*(uint64_t *)(arg1 + 0x68));
    if (Arg1 >= 16) goto loc_00330588;
loc_0033021F:
    if ((((uint8_t)(local_rsi)) & (1)) != 0) goto loc_00330699;
loc_00330229:
    a2 = 0;
    a3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) >> (16);
    a3 = (uint32_t)((a3) & (3));
    a2 = (uint32_t)((a2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))));
    local_rdi = (uint32_t)(((uint8_t)(a2)) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))));
    if ((*(uint64_t *)(arg1 + 0x38)) != -1) goto loc_00330836;
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1C))) & (15));
    if (((uint32_t)(a2)) != 9) goto loc_003305F2;
loc_00330276:
    result = MiGetPage(*(uint64_t *)(arg1), (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))), v_rip + 11520389);
    if (result == -1) goto loc_00330497;
loc_00330291:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) | (64));
    if ((*(uint64_t *)(arg1 + 0x38)) == -1) { local_rbx = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))); }
    Arg1 = ((*(uint64_t *)(arg1 + 0x38)) < -1) ? 1 : 0;
    result = ((((uint8_t)(local_rsi)) & (2)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_003307F8;
loc_003302B3:
    local_rdi = (result * 2) + (result);
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) >> (18));
    local_r15 = (uint32_t)((local_r15) & (3));
    local_rdi = (local_rdi) << (4);
    local_rdi = (local_rdi) + (result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(Arg1)) != ((uint32_t)(local_r15))) goto loc_0033063F;
loc_003302F9:
    v_stack_m78 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) & (1));
    a4 = (uint32_t)(((uint32_t)((uint32_t)(result))) << (4));
    v_stack_m68 = (uint32_t)(a4);
    v_stack_m64 = (uint32_t)(result + result * 1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) & (32)) == 0) goto loc_0033036B;
    result = *(uint64_t *)(local_rdi + 0x10);
    local_r10 = result + result * 1;
    if (((*(uint64_t *)(local_rdi + 0x10)) & (992)) != 0) {
        a4 = (uint32_t)(local_r15);
        a3 = (uint32_t)(result + result * 1);
        a2 = result;
        Arg1 = 0;
        result = MiZeroPhysicalPage(Arg1, a2, a3, a4);
        result = *(uint64_t *)(local_rdi + 0x10);
        a3 = 0;
        result = (result) & (-993);
        a2 = 0;
        Arg1 = local_rdi;
        *(uint64_t *)(local_rdi + 0x10) = result;
        result = MiSetPfnTbFlushStamp(Arg1, a2, a3, a4);
        a4 = v_stack_m68;
        local_r10 = v_stack_m64;
        v_stack_m78 = 1;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(Arg1)) != ((uint32_t)(local_r15))) goto loc_003306D5;
loc_00330380:
    if (v_stack_m78 != 0) goto loc_003303C7;
    Arg1 = (*(uint64_t *)(local_rdi + 0x18)) & (a4);
    if ((*(uint64_t *)(local_rdi + 0x18)) == (*(uint64_t *)(local_rdi + 0x18))) goto loc_003303C7;
loc_003303B0:
    a3 = (*(uint64_t *)(local_rdi + 0x18)) & (a4);
    if ((*(uint64_t *)(local_rdi + 0x18)) != (*(uint64_t *)(local_rdi + 0x18))) goto loc_003303B0;
loc_003303C7:
    *(uint64_t *)(local_rdi) = *(uint64_t *)(arg1 + 0x58);
    *(uint64_t *)(arg1 + 0x58) = local_rdi;
    if ((*(uint64_t *)(arg1 + 0x60)) == 0) {
        *(uint64_t *)(arg1 + 0x60) = local_rdi;
    }
    if ((*(uint64_t *)(arg1 + 0x68)) != (*(uint64_t *)(arg1 + 0x50))) goto loc_00330563;
loc_003303F6:
    local_r13 = 0;
loc_003303F9:
loc_00330406:
    result = (0) << (4);
    Arg1 = (v_stack_m58) + (result);
    if ((*(uint64_t *)(arg1)) != local_rsi) goto loc_0033078A;
loc_0033041D:
    result = ((uint32_t)((uint32_t)(0 + 1))) << (4);
    Arg1 = (v_stack_m58) + (result);
    if ((*(uint64_t *)(arg1)) != local_rsi) goto loc_003307B5;
loc_00330439:
    local_rdi = (uint32_t)((0) + (2));
    if (((uint32_t)(local_rdi)) < 2) goto loc_00330406;
    if (*(uint64_t *)(arg1 + 0x58) == 0) goto loc_00330468;
loc_0033044B:
    if (condition_is_below) goto loc_003307E2;
loc_0033045D:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x58) + 0x24) = 0;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58)) != 0) goto loc_0033044B;
loc_00330468:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x58)), *(uint64_t *)(local_rdi + 0x18), 0 + 1);
    return result;
loc_00330497:
    if (condition_is_above_or_equal) goto loc_003305C6;
loc_003304A6:
    local_r13 = 0;
loc_003304B0:
    if (condition_is_above_or_equal) goto loc_003303F9;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m38)) << (9));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))));
    Arg1 = (uint32_t)((Arg1) & (0x7E00ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))));
    *(uint32_t *)(arg1 + 0x30) = (uint32_t)(Arg1);
loc_003304DD:
    a2 = 0;
    a3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) >> (16);
    a3 = (uint32_t)((a3) & (3));
    a2 = (uint32_t)((a2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))));
    a2 = (uint32_t)(((uint8_t)(a2)) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))));
    result = MiGetPage(*(uint64_t *)(arg1), a2, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38))), v_rip + 11519635);
    if (result == -1) goto loc_003303F9;
    result = MiGetPageChainSmallPageProcess(Arg1, v_stack_m30, result, v_rip + 11519635);
    if ((*(uint64_t *)(arg1 + 0x68)) == (*(uint64_t *)(arg1 + 0x50))) goto loc_003303F9;
    result = MiGetPageChainYield(Arg1, 16, result, v_rip + 11519635);
    if ((uint32_t)(result) != 0) goto loc_003303F9;
    goto loc_003304DD;
loc_00330563:
    if ((((uint8_t)(result)) & (15)) != 0) goto loc_00330574;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) & (1)) != 0) goto loc_00330756;
loc_00330574:
    local_r13 = 0;
    goto loc_00330229;
loc_00330588:
    local_rsi = (uint32_t)((*(uint64_t *)(v_stack_m28 + 0x48)) | (1));
    result = MiGetLargePagesForChain(Arg1, 16, result, v_rip + 11519424);
    if (*(uint64_t *)(arg1 + 0x68) == 0) goto loc_003305BA;
    if ((*(uint64_t *)(arg1 + 0x68)) == (*(uint64_t *)(arg1 + 0x50))) goto loc_003303F9;
    a2 = 0;
    result = MiGetPageChainYield(Arg1, a2, result, v_rip + 11519424);
    if ((uint32_t)(result) != 0) goto loc_003303F9;
loc_003305BA:
    goto loc_0033021F;
loc_003305C6:
    if (condition_is_above_or_equal) goto loc_003304A6;
    result = MiPageAvailable(*(uint64_t *)(arg1), (uint32_t)((uint32_t)(result)), result, v_rip + 11519359);
    if ((uint32_t)(result) == 0) goto loc_003303F6;
    local_r14 = (uint32_t)((0) + 1);
    local_r13 = 0;
    goto loc_003301AD;
loc_003305F2:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) >> (12));
    Arg1 = (uint32_t)((Arg1) & (1));
    v_stack_m58 = 0;
    v_stack_m60 = *(uint64_t *)(arg1 + 0x48);
    a4 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (16));
    if ((((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x38))) & (1)) == 0) { a4 = (uint32_t)(Arg1); }
    result = MiGetSlabPage(*(uint64_t *)(arg1), (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_rdi)), a4);
    if (result == -1) goto loc_003303F6;
loc_00330630:
    if (result == -1) goto loc_00330276;
    goto loc_00330291;
loc_0033063F:
    result = (uint8_t)((1) << ((uint8_t)(*(uint64_t *)(arg1))));
    if (((*(uint8_t *)(v_rip + 0xAFD685)) & ((uint8_t)((uint8_t)(result)))) == 0) goto loc_003302F9;
    result = MiMakeLinkedListPte(v_stack_m30, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_rdi)), a4);
    *(uint64_t *)(local_rdi + 0x10) = result;
    result = (v_stack_m28) + 1;
    v_stack_m30 = result;
    v_stack_m28 = result;
    if (result != 16) goto loc_003303C7;
    a3 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (1));
    result = MiPerformFinalZeroing(v_stack_m30, (uint32_t)((uint32_t)(v_stack_m48)), a3, a4);
    goto loc_003303C7;
loc_00330699:
    Arg1 = (*(uint64_t *)(arg1 + 0x50)) - (*(uint64_t *)(arg1 + 0x68));
    if (Arg1 < 16) goto loc_00330229;
    if (((*(uint32_t *)(arg1 + 0x20)) & (0x3000ULL)) != 0) goto loc_00330229;
    if ((*(uint16_t *)(v_rip + 0xC9493C)) <= 1) goto loc_00330229;
    local_rbx = (uint32_t)((*(uint64_t *)(v_stack_m28 + 0x38)) | (0x31000ULL));
    goto loc_00330229;
loc_003306D5:
    if (((uint32_t)(Arg1)) == 1) goto loc_003306EC;
    if (((uint32_t)(Arg1)) == 3) goto loc_00330743;
    Arg1 = (*(uint64_t *)(local_rdi + 0x18)) >> (59);
    Arg1 = (uint32_t)((Arg1) & (7));
    if (condition_is_not_equal) goto loc_00330725;
loc_003306EC:
    result = *(uint64_t *)(local_rdi + 0x10);
    if (((*(uint64_t *)(local_rdi + 0x10)) & (992)) != 0) {
        a4 = (uint32_t)(v_stack_m48);
        a3 = (uint32_t)(local_r10);
        a2 = result;
        Arg1 = 0;
        result = MiZeroPhysicalPage(Arg1, a2, a3, a4);
    }
    result = MiMakeLinkedListPte(v_stack_m20, a2, a3, a4);
    *(uint64_t *)(local_rdi + 0x10) = result;
    v_stack_m20 = result;
    goto loc_003303C7;
loc_00330725:
    result = MiTbFlushTimeStampMayNeedFlush(v_stack_m20, (uint32_t)(*(uint32_t *)(v_rip + 0xC9E950)), 7, a4);
    if ((uint8_t)(result) != 0) goto loc_003306EC;
    a4 = (uint32_t)((a4) | (4));
loc_00330743:
    result = MiChangePageAttribute(local_rdi, (uint32_t)((uint32_t)(v_stack_m48)), (uint32_t)((uint32_t)(a4)), a4);
    goto loc_00330380;
loc_00330756:
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1C))) >> (4));
    a2 = (uint32_t)((a2) & (3));
    if (((uint32_t)(a2)) == 2) goto loc_00330778;
    result = MiWorkingSetIsContended(*(uint64_t *)(arg1 + 0x8), a2, (uint32_t)((uint32_t)(a4)), a4);
    if ((uint32_t)(result) != 0) goto loc_003303F6;
loc_00330778:
    result = KeShouldYieldProcessor(*(uint64_t *)(arg1 + 0x8), a2, (uint32_t)((uint32_t)(a4)), a4);
    if ((uint32_t)(result) == 0) goto loc_00330574;
    goto loc_003303F6;
loc_0033078A:
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) >> (18));
    a4 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (1));
    a2 = (uint32_t)((a2) & (3));
    if ((uint32_t)(local_rdi) == 0) goto loc_003308A6;
    result = MiChangePageAttributeBatch(*(uint64_t *)(arg1 + 0x8), a2, *(uint64_t *)(v_rip - 0x31FF2B), a4);
    goto loc_0033041D;
loc_003307B5:
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) >> (18));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (1));
    a2 = (uint32_t)((a2) & (3));
    if ((uint32_t)(a4) == 0) goto loc_003308B3;
    result = MiChangePageAttributeBatch(*(uint64_t *)(arg1 + 0x8), a2, *(uint64_t *)(v_rip - 0x31FF55), (uint32_t)((uint32_t)(result)));
    goto loc_00330439;
loc_003307E2:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(a2 + 0x24))) & (0x18000000ULL));
    goto loc_0033045D;
loc_003307F0:
    local_rbx = (uint32_t)((local_rbx) | (64));
    goto loc_0033021F;
loc_003307F8:
    result = MiPageToNode(result, a2, *(uint64_t *)(v_rip - 0x31FF55), (uint32_t)((uint32_t)(result)));
    if (((uint32_t)(result)) == ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)))) goto loc_003302B3;
    a3 = 0;
    result = MiSwapNumaStandbyPage(result, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), a3, (uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    if (result != result) goto loc_003302B3;
    local_rsi = (uint32_t)((local_rsi) | (2));
    goto loc_003302B3;
loc_00330836:
    local_r15 = 15;
    if (((uint32_t)(*(uint32_t *)(v_rip + 0xAFD490))) < 15) { local_r15 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAFD490))); }
    result = (result) & (local_r15);
    a2 = 0;
    *(uint64_t *)(v_stack_m48) = result;
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (16);
    Arg1 = (uint32_t)((Arg1) & (3));
    a2 = (uint32_t)((a2) ^ ((uint32_t)(result)));
    local_rdi = (uint32_t)((result) ^ ((uint32_t)((uint8_t)(a2))));
    result = MiGetPage(*(uint64_t *)(arg1), (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    Arg1 = (*(uint64_t *)(v_stack_m48)) + 1;
    Arg1 = (Arg1) & (local_r15);
    *(void **)(v_stack_m48) = Arg1;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (0xFFFFFFBFULL));
    if (result != -1) { Arg1 = (uint32_t)(local_rbx); }
    goto loc_00330630;
loc_003308A6:
    result = MiPerformFinalZeroing(Arg1, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))), (uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    goto loc_0033041D;
loc_003308B3:
    result = MiPerformFinalZeroing(Arg1, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    goto loc_00330439;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `W` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `W` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `W` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00330130&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
