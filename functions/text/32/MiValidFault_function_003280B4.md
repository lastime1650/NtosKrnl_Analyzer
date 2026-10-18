# MiValidFault

- RVA: `0x003280B4`–`0x00328560` (길이 `1,196` bytes)
- VA: `0x00000001403280B4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00075EB4`
- 디코드: `279`개 명령, `1,196/1,196` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00328176` → [MI_IS_PTE_SHADOW_STACK](../44/MI_IS_PTE_SHADOW_STACK_function_0044B110.md) (function, `0x0044B110`)
- `0x003281FE` → [MiNoFaultFound](../41/MiNoFaultFound_function_0041BB20.md) (function, `0x0041BB20`)
- `0x0032823A` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x0032824A` → [MiGetPagingFileOffset](../36/MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x00328272` → [MiCheckAndUpdateIoAttribution](../3C/MiCheckAndUpdateIoAttribution_function_003CB3C4.md) (function, `0x003CB3C4`)
- `0x00328293` → [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) (function, `0x00362A0C`)
- `0x00328328` → [MiCheckSystemNxFault](../4A/MiCheckSystemNxFault_function_004A44C0.md) (function, `0x004A44C0`)
- `0x00328398` → [MiValidVirtualizationFault](../46/MiValidVirtualizationFault_function_00466EC0.md) (function, `0x00466EC0`)
- `0x003283C1` → [KeIsUserVaAccessAllowed](../21/KeIsUserVaAccessAllowed_function_0021D740.md) (function, `0x0021D740`)
- `0x003283E3` → [MiUpdatePrefetchPriority](../40/MiUpdatePrefetchPriority_function_00402CB0.md) (function, `0x00402CB0`)
- `0x003283F0` → [MiPfnIsPageTable](../4F/MiPfnIsPageTable_function_004F2D90.md) (function, `0x004F2D90`)
- `0x00328403` → [MiLockPageAndSetDirty](../28/MiLockPageAndSetDirty_function_002857A0.md) (function, `0x002857A0`)
- `0x00328412` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x0032841A` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x00328429` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x003284EE` → [KeInvalidAccessAllowed](../34/KeInvalidAccessAllowed_function_0034B3F0.md) (function, `0x0034B3F0`)
- `0x00328512` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00328522` → [MiSetFaultPacketDirectives](../46/MiSetFaultPacketDirectives_function_004673D8.md) (function, `0x004673D8`)
- `0x0032853A` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x00328542` → [MiPfnIsActivePageTable](../4A/MiPfnIsActivePageTable_function_004AFFAC.md) (function, `0x004AFFAC`)
- `0x00328555` → [MiLockPageAndSetDirty](../28/MiLockPageAndSetDirty_function_002857A0.md) (function, `0x002857A0`)

### Direct callers
- [MiUserFault](MiUserFault_function_00329840.md) at `0x00329E7D`

### Static image references
- `0x003281BD` → RVA `0x00E2DCE0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x00328308` → [sub_006E1C8E + 0xAB](../6E/Unknown_function_006E1C8E.md) (`tail-transfer`)
  - `0x00328365` → [sub_006E1C8E + 0x69](../6E/Unknown_function_006E1C8E.md) (`tail-transfer`)
  - `0x0032845E` → [sub_006E1C8E](../6E/Unknown_function_006E1C8E.md) (`tail-transfer`)
  - `0x00328480` → [sub_006E1C8E](../6E/Unknown_function_006E1C8E.md) (`tail-transfer`)
  - `0x003284A4` → [sub_006E1C8E + 0x3C](../6E/Unknown_function_006E1C8E.md) (`tail-transfer`)
  - `0x003284CC` → [sub_006E1C8E + 0x4C](../6E/Unknown_function_006E1C8E.md) (`tail-transfer`)
  - `0x00328549` → [sub_006E1C8E + 0x93](../6E/Unknown_function_006E1C8E.md) (`tail-transfer`)
  - `0x0032855B` → [sub_006E1C8E + 0x93](../6E/Unknown_function_006E1C8E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003280B4  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003280B9  55                              push rbp
003280BA  56                              push rsi
003280BB  57                              push rdi
003280BC  41 54                           push r12
003280BE  41 55                           push r13
003280C0  41 56                           push r14
003280C2  41 57                           push r15
003280C4  48 83 EC 30                     sub rsp, 0x30
003280C8  48 8B 29                        mov rbp, qword ptr [rcx]
003280CB  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003280D5  4C 8B 71 08                     mov r14, qword ptr [rcx + 8]
003280D9  4C 8B E5                        mov r12, rbp
003280DC  48 8B 71 10                     mov rsi, qword ptr [rcx + 0x10]
003280E0  48 8B FA                        mov rdi, rdx
003280E3  49 C1 EC 09                     shr r12, 9
003280E7  4C 8B F9                        mov r15, rcx
003280EA  4C 23 E0                        and r12, rax
003280ED  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
003280F7  49 8B C0                        mov rax, r8
003280FA  4C 03 E0                        add r12, rax
003280FD  48 8B D6                        mov rdx, rsi
00328100  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00328109  48 8B CE                        mov rcx, rsi
0032810C  83 E2 01                        and edx, 1
0032810F  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
00328117  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0032811B  4C 8B A8 B8 00 00 00            mov r13, qword ptr [rax + 0xb8]
00328122  48 85 D2                        test rdx, rdx
00328125  0F 85 81 01 00 00               jne 0x1403282ac
0032812B  49 8B C0                        mov rax, r8
0032812E  48 3B E8                        cmp rbp, rax
00328131  0F 83 4E 03 00 00               jae 0x140328485
00328137  33 DB                           xor ebx, ebx
00328139  40 F6 C7 04                     test dil, 4
0032813D  0F 84 8E 03 00 00               je 0x1403284d1
00328143  41 F7 47 50 00 01 00 00         test dword ptr [r15 + 0x50], 0x100
0032814B  48 B9 00 00 00 00 00 80 FF FF   movabs rcx, 0xffff800000000000
00328155  0F 84 47 02 00 00               je 0x1403283a2
0032815B  41 F6 C6 02                     test r14b, 2
0032815F  75 28                           jne 0x140328189
00328161  41 F6 C6 10                     test r14b, 0x10
00328165  0F 85 9A 01 00 00               jne 0x140328305
0032816B  41 8B 47 50                     mov eax, dword ptr [r15 + 0x50]
0032816F  84 C0                           test al, al
00328171  79 75                           jns 0x1403281e8
00328173  48 8B CF                        mov rcx, rdi
00328176  E8 95 2F 12 00                  call 0x14044b110
0032817B  85 C0                           test eax, eax
0032817D  75 69                           jne 0x1403281e8
0032817F  BB 05 00 00 C0                  mov ebx, 0xc0000005
00328184  E9 84 00 00 00                  jmp 0x14032820d
00328189  48 21 5C 24 70                  and qword ptr [rsp + 0x70], rbx
0032818E  48 0F BA E7 09                  bt rdi, 9
00328193  0F 82 E3 00 00 00               jb 0x14032827c
00328199  48 0F BA E7 0B                  bt rdi, 0xb
0032819E  73 DF                           jae 0x14032817f
003281A0  48 85 FF                        test rdi, rdi
003281A3  0F 89 89 01 00 00               jns 0x140328332
003281A9  48 8B C7                        mov rax, rdi
003281AC  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
003281B6  48 C1 E8 0C                     shr rax, 0xc
003281BA  48 23 C1                        and rax, rcx
003281BD  48 3B 05 1C 5B B0 00            cmp rax, qword ptr [rip + 0xb05b1c]
003281C4  77 22                           ja 0x1403281e8
003281C6  48 8D 0C 40                     lea rcx, [rax + rax*2]
003281CA  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
003281D4  48 03 C9                        add rcx, rcx
003281D7  48 8B C0                        mov rax, rax
003281DA  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
003281DE  48 C1 E8 36                     shr rax, 0x36
003281E2  0F BA E0 00                     bt eax, 0
003281E6  72 3D                           jb 0x140328225
003281E8  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
003281ED  4C 8B CE                        mov r9, rsi
003281F0  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
003281F5  4C 8B C5                        mov r8, rbp
003281F8  49 8B D4                        mov rdx, r12
003281FB  49 8B CF                        mov rcx, r15
003281FE  E8 1D 39 0F 00                  call 0x14041bb20
00328203  40 F6 C6 01                     test sil, 1
00328207  0F 85 75 01 00 00               jne 0x140328382
0032820D  8B C3                           mov eax, ebx
0032820F  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00328214  48 83 C4 30                     add rsp, 0x30
00328218  41 5F                           pop r15
0032821A  41 5E                           pop r14
0032821C  41 5D                           pop r13
0032821E  41 5C                           pop r12
00328220  5F                              pop rdi
00328221  5E                              pop rsi
00328222  5D                              pop rbp
00328223  C3                              ret
00328224  CC                              int3
00328225  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0032822F  48 8B C0                        mov rax, rax
00328232  4C 8D 34 C8                     lea r14, [rax + rcx*8]
00328236  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
0032823A  E8 D1 A7 04 00                  call 0x140372a10
0032823F  85 C0                           test eax, eax
00328241  74 14                           je 0x140328257
00328243  48 0F BA E1 0A                  bt rcx, 0xa
00328248  72 0D                           jb 0x140328257
0032824A  E8 E1 72 04 00                  call 0x14036f530
0032824F  85 C0                           test eax, eax
00328251  0F 85 96 01 00 00               jne 0x1403283ed
00328257  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
0032825B  48 85 C0                        test rax, rax
0032825E  79 88                           jns 0x1403281e8
00328260  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00328264  48 0F BA E0 0A                  bt rax, 0xa
00328269  0F 83 79 FF FF FF               jae 0x1403281e8
0032826F  49 8B CE                        mov rcx, r14
00328272  E8 4D 31 0A 00                  call 0x1403cb3c4
00328277  E9 6C FF FF FF                  jmp 0x1403281e8
0032827C  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00328281  45 33 C9                        xor r9d, r9d
00328284  49 83 C8 FF                     or r8, 0xffffffffffffffff
00328288  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0032828D  49 8B D4                        mov rdx, r12
00328290  48 8B CD                        mov rcx, rbp
00328293  E8 74 A7 03 00                  call 0x140362a0c
00328298  8B D8                           mov ebx, eax
0032829A  85 C0                           test eax, eax
0032829C  0F 88 76 02 00 00               js 0x140328518
003282A2  BB 12 01 00 00                  mov ebx, 0x112
003282A7  E9 57 FF FF FF                  jmp 0x140328203
003282AC  8A 01                           mov al, byte ptr [rcx]
003282AE  3C 01                           cmp al, 1
003282B0  0F 84 27 01 00 00               je 0x1403283dd
003282B6  3C 03                           cmp al, 3
003282B8  0F 85 6D FE FF FF               jne 0x14032812b
003282BE  48 C1 EF 0C                     shr rdi, 0xc
003282C2  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
003282CC  48 23 F9                        and rdi, rcx
003282CF  48 3B 3D 0A 5A B0 00            cmp rdi, qword ptr [rip + 0xb05a0a]
003282D6  77 26                           ja 0x1403282fe
003282D8  48 8D 1C 7F                     lea rbx, [rdi + rdi*2]
003282DC  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
003282E6  48 03 DB                        add rbx, rbx
003282E9  48 8B C0                        mov rax, rax
003282EC  48 8B 04 D8                     mov rax, qword ptr [rax + rbx*8]
003282F0  48 C1 E8 36                     shr rax, 0x36
003282F4  0F BA E0 00                     bt eax, 0
003282F8  0F 82 0F 01 00 00               jb 0x14032840d
003282FE  33 C0                           xor eax, eax
00328300  E9 0A FF FF FF                  jmp 0x14032820f
00328305  48 85 FF                        test rdi, rdi
00328308  0F 88 2B 9A 3B 00               js 0x1406e1d39
0032830E  41 F7 47 50 00 01 00 00         test dword ptr [r15 + 0x50], 0x100
00328316  0F 85 4F FE FF FF               jne 0x14032816b
0032831C  41 B8 05 00 00 00               mov r8d, 5
00328322  48 8B D7                        mov rdx, rdi
00328325  49 8B CF                        mov rcx, r15
00328328  E8 93 C1 17 00                  call 0x1404a44c0
0032832D  E9 39 FE FF FF                  jmp 0x14032816b
00328332  40 F6 C7 42                     test dil, 0x42
00328336  0F 85 6D FE FF FF               jne 0x1403281a9
0032833C  41 8B 85 F4 01 00 00            mov eax, dword ptr [r13 + 0x1f4]
00328343  A8 10                           test al, 0x10
00328345  0F 84 5E FE FF FF               je 0x1403281a9
0032834B  48 3B E9                        cmp rbp, rcx
0032834E  0F 83 55 FE FF FF               jae 0x1403281a9
00328354  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0032835D  41 F7 47 50 00 01 00 00         test dword ptr [r15 + 0x50], 0x100
00328365  0F 84 8C 99 3B 00               je 0x1406e1cf7
0032836B  F6 81 A9 05 00 00 10            test byte ptr [rcx + 0x5a9], 0x10
00328372  0F 85 31 FE FF FF               jne 0x1403281a9
00328378  BB 23 07 00 C0                  mov ebx, 0xc0000723
0032837D  E9 8B FE FF FF                  jmp 0x14032820d
00328382  48 83 E6 FE                     and rsi, 0xfffffffffffffffe
00328386  80 3E 05                        cmp byte ptr [rsi], 5
00328389  0F 85 7E FE FF FF               jne 0x14032820d
0032838F  4D 8B C4                        mov r8, r12
00328392  48 8B D6                        mov rdx, rsi
00328395  49 8B CF                        mov rcx, r15
00328398  E8 23 EB 13 00                  call 0x140466ec0
0032839D  E9 6B FE FF FF                  jmp 0x14032820d
003283A2  48 85 F6                        test rsi, rsi
003283A5  0F 84 B0 FD FF FF               je 0x14032815b
003283AB  48 3B E9                        cmp rbp, rcx
003283AE  0F 83 A7 FD FF FF               jae 0x14032815b
003283B4  40 F6 C6 01                     test sil, 1
003283B8  0F 85 9D FD FF FF               jne 0x14032815b
003283BE  48 8B CE                        mov rcx, rsi
003283C1  E8 7A 53 EF FF                  call 0x14021d740
003283C6  84 C0                           test al, al
003283C8  0F 84 1B 01 00 00               je 0x1403284e9
003283CE  48 B9 00 00 00 00 00 80 FF FF   movabs rcx, 0xffff800000000000
003283D8  E9 7E FD FF FF                  jmp 0x14032815b
003283DD  45 33 C0                        xor r8d, r8d
003283E0  48 8B D5                        mov rdx, rbp
003283E3  E8 C8 A8 0D 00                  call 0x140402cb0
003283E8  E9 11 FF FF FF                  jmp 0x1403282fe
003283ED  49 8B CE                        mov rcx, r14
003283F0  E8 9B A9 1C 00                  call 0x1404f2d90
003283F5  85 C0                           test eax, eax
003283F7  0F 85 2F 01 00 00               jne 0x14032852c
003283FD  8D 50 01                        lea edx, [rax + 1]
00328400  49 8B CE                        mov rcx, r14
00328403  E8 98 D3 F5 FF                  call 0x1402857a0
00328408  E9 4A FE FF FF                  jmp 0x140328257
0032840D  B9 01 00 00 00                  mov ecx, 1
00328412  E8 D9 3C F5 FF                  call 0x14027c0f0
00328417  48 8B CD                        mov rcx, rbp
0032841A  E8 B1 E4 FE FF                  call 0x1403168d0
0032841F  B2 11                           mov dl, 0x11
00328421  B9 01 00 00 00                  mov ecx, 1
00328426  48 8B F8                        mov rdi, rax
00328429  E8 F2 EB F6 FF                  call 0x140297020
0032842E  48 85 FF                        test rdi, rdi
00328431  0F 84 C7 FE FF FF               je 0x1403282fe
00328437  8B 57 30                        mov edx, dword ptr [rdi + 0x30]
0032843A  44 8B C2                        mov r8d, edx
0032843D  41 83 E0 70                     and r8d, 0x70
00328441  41 83 F8 30                     cmp r8d, 0x30
00328445  0F 84 B3 FE FF FF               je 0x1403282fe
0032844B  41 8D 40 F0                     lea eax, [r8 - 0x10]
0032844F  A9 BF FF FF FF                  test eax, 0xffffffbf
00328454  0F 84 A4 FE FF FF               je 0x1403282fe
0032845A  0F BA E2 15                     bt edx, 0x15
0032845E  0F 83 2A 98 3B 00               jae 0x1406e1c8e
00328464  0F BA E2 17                     bt edx, 0x17
00328468  0F 82 90 FE FF FF               jb 0x1403282fe
0032846E  81 E2 00 00 18 00               and edx, 0x180000
00328474  81 FA 00 00 10 00               cmp edx, 0x100000
0032847A  0F 83 7E FE FF FF               jae 0x1403282fe
00328480  E9 09 98 3B 00                  jmp 0x1406e1c8e
00328485  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
0032848F  48 3B E8                        cmp rbp, rax
00328492  0F 87 9F FC FF FF               ja 0x140328137
00328498  40 84 FF                        test dil, dil
0032849B  0F 89 96 FC FF FF               jns 0x140328137
003284A1  48 85 D2                        test rdx, rdx
003284A4  0F 84 20 98 3B 00               je 0x1406e1cca
003284AA  80 39 01                        cmp byte ptr [rcx], 1
003284AD  0F 84 CC FC FF FF               je 0x14032817f
003284B3  80 39 03                        cmp byte ptr [rcx], 3
003284B6  0F 84 C3 FC FF FF               je 0x14032817f
003284BC  48 8B C6                        mov rax, rsi
003284BF  48 83 E0 FE                     and rax, 0xfffffffffffffffe
003284C3  80 38 06                        cmp byte ptr [rax], 6
003284C6  0F 84 B3 FC FF FF               je 0x14032817f
003284CC  E9 09 98 3B 00                  jmp 0x1406e1cda
003284D1  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
003284DB  48 3B E8                        cmp rbp, rax
003284DE  0F 86 9B FC FF FF               jbe 0x14032817f
003284E4  E9 5A FC FF FF                  jmp 0x140328143
003284E9  33 D2                           xor edx, edx
003284EB  48 8B CE                        mov rcx, rsi
003284EE  E8 FD 2E 02 00                  call 0x14034b3f0
003284F3  84 C0                           test al, al
003284F5  0F 85 D3 FE FF FF               jne 0x1403283ce
003284FB  4C 8B CE                        mov r9, rsi
003284FE  48 C7 44 24 20 0F 00 00 00      mov qword ptr [rsp + 0x20], 0xf
00328507  4D 8B C6                        mov r8, r14
0032850A  48 8B D5                        mov rdx, rbp
0032850D  B9 50 00 00 00                  mov ecx, 0x50
00328512  E8 49 51 1D 00                  call 0x1404fd660
00328517  CC                              int3
00328518  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
0032851D  8B D0                           mov edx, eax
0032851F  49 8B CF                        mov rcx, r15
00328522  E8 B1 EE 13 00                  call 0x1404673d8
00328527  E9 E1 FC FF FF                  jmp 0x14032820d
0032852C  4D 8B 67 38                     mov r12, qword ptr [r15 + 0x38]
00328530  4D 8B 6E 08                     mov r13, qword ptr [r14 + 8]
00328534  49 8B CC                        mov rcx, r12
00328537  49 8B D5                        mov rdx, r13
0032853A  E8 51 63 F1 FF                  call 0x14023e890
0032853F  49 8B CE                        mov rcx, r14
00328542  E8 65 7A 18 00                  call 0x1404affac
00328547  85 C0                           test eax, eax
00328549  0F 85 D2 97 3B 00               jne 0x1406e1d21
0032854F  8D 50 01                        lea edx, [rax + 1]
00328552  49 8B CE                        mov rcx, r14
00328555  E8 46 D2 F5 FF                  call 0x1402857a0
0032855A  90                              nop
0032855B  E9 C1 97 3B 00                  jmp 0x1406e1d21
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiValidFault(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_r12 = (*(unsigned __int64 *)(a1)) >> (9);
    v_r12 = (v_r12) & (result);
    v_r12 = (v_r12) + (a3);
    a2 = (unsigned int)((*(unsigned __int64 *)(a1 + 16)) & (1));
    v_stack_p18 = v_r12;
    a1 = (*(unsigned __int64 *)(a1 + 16)) & (-2);
    if (a2 != 0) goto loc_003282AC;
loc_0032812B:
    if ((*(unsigned __int64 *)(a1)) >= a3) goto loc_00328485;
loc_00328137:
    v_rbx = 0;
    if ((((unsigned __int8)(a2)) & (4)) == 0) goto loc_003284D1;
loc_00328143:
    if (((*(unsigned int *)(a1 + 80)) & (256)) == 0) goto loc_003283A2;
loc_0032815B:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 8))) & (2)) != 0) goto loc_00328189;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 8))) & (16)) != 0) goto loc_00328305;
loc_0032816B:
    if (!sign_flag) goto loc_003281E8;
    result = MI_IS_PTE_SHADOW_STACK(a2, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_003281E8;
loc_0032817F:
    goto loc_0032820D;
loc_00328189:
    if (condition_is_below) goto loc_0032827C;
    if (condition_is_above_or_equal) goto loc_0032817F;
    if (!sign_flag) goto loc_00328332;
loc_003281A9:
    result = (a2) >> (12);
    result = (result) & (a2);
    if (result > (*(unsigned __int64 *)(v_rip + 11557660))) goto loc_003281E8;
    a1 = (result + result * 2) + (result + result * 2);
    result = (*(unsigned __int64 *)(result + a1 * 8)) >> (54);
    if (condition_is_below) goto loc_00328225;
loc_003281E8:
    v_stack_m40 = a2;
    result = MiNoFaultFound(a1, v_r12, *(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 16));
loc_00328203:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (1)) != 0) goto loc_00328382;
loc_0032820D:
loc_0032820F:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL)));
loc_00328225:
    result = MiInvalidPteConforms(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL))) + a1 * 8 + 16), v_r12, *(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 16));
    if ((unsigned int)(result) == 0) goto loc_00328257;
    if (condition_is_below) goto loc_00328257;
    result = MiGetPagingFileOffset(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL))) + a1 * 8 + 16), v_r12, *(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 16));
    if ((unsigned int)(result) != 0) goto loc_003283ED;
loc_00328257:
    if (!sign_flag) goto loc_003281E8;
    if (condition_is_above_or_equal) goto loc_003281E8;
    result = MiCheckAndUpdateIoAttribution((unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL))) + a1 * 8, v_r12, *(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1 + 16));
    goto loc_003281E8;
loc_0032827C:
    a4 = 0;
    a3 = (*(unsigned __int64 *)(a1)) | (-1);
    v_stack_p20 = v_stack_p70;
    result = MiCopyOnWrite(*(unsigned __int64 *)(a1), v_r12, a3, a4);
    if (sign_flag) goto loc_00328518;
    goto loc_00328203;
loc_003282AC:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1)))) == 1) goto loc_003283DD;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1)))) != 3) goto loc_0032812B;
    v_rdi = (a2) >> (12);
    v_rdi = (v_rdi) & (*(unsigned __int64 *)(a1));
    if (v_rdi > (*(unsigned __int64 *)(v_rip + 11557386))) goto loc_003282FE;
    v_rbx = (v_rdi + v_rdi * 2) + (v_rdi + v_rdi * 2);
    result = (*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1)) + v_rbx * 8)) >> (54);
    if (condition_is_below) goto loc_0032840D;
loc_003282FE:
    result = 0;
    goto loc_0032820F;
loc_00328305:
    if (((*(unsigned int *)(a1 + 80)) & (256)) != 0) goto loc_0032816B;
    result = MiCheckSystemNxFault(a1, v_rdi, 5, a4);
    goto loc_0032816B;
loc_00328332:
    if ((((unsigned __int8)(v_rdi)) & (66)) != 0) goto loc_003281A9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 500)))) & (16)) == 0) goto loc_003281A9;
    if ((*(unsigned __int64 *)(a1)) >= a1) goto loc_003281A9;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1449)) & (16)) != 0) goto loc_003281A9;
    goto loc_0032820D;
loc_00328382:
    v_rsi = (*(unsigned __int64 *)(a1 + 16)) & (-2);
    if ((*(unsigned __int8 *)(v_rsi)) != 5) goto loc_0032820D;
    result = MiValidVirtualizationFault(a1, v_rsi, v_r12, a4);
    goto loc_0032820D;
loc_003283A2:
    if (v_rsi == 0) goto loc_0032815B;
    if ((*(unsigned __int64 *)(a1)) >= a1) goto loc_0032815B;
    if ((((unsigned __int8)(v_rsi)) & (1)) != 0) goto loc_0032815B;
    result = KeIsUserVaAccessAllowed(v_rsi, v_rsi, v_r12, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003284E9;
loc_003283CE:
    goto loc_0032815B;
loc_003283DD:
    a3 = 0;
    result = MiUpdatePrefetchPriority(v_rsi, *(unsigned __int64 *)(a1), a3, a4);
    goto loc_003282FE;
loc_003283ED:
    result = MiPfnIsPageTable((unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL))) + a1 * 8, *(unsigned __int64 *)(a1), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0032852C;
    result = MiLockPageAndSetDirty((unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL))) + a1 * 8, result + 1, a3, a4);
    goto loc_00328257;
loc_0032840D:
    result = MiLockVadTree(1, result + 1, a3, a4);
    result = MiLocateAddress(*(unsigned __int64 *)(a1), result + 1, a3, a4);
    result = MiUnlockVadTree(1, 17, a3, a4);
    if (result == 0) goto loc_003282FE;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) & (112));
    if (((unsigned int)(a3)) == 48) goto loc_003282FE;
    if ((((unsigned int)(a3 - 16)) & (0xFFFFFFBFULL)) == 0) goto loc_003282FE;
    if (condition_is_below) goto loc_003282FE;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0x180000ULL));
    if (((unsigned int)(a2)) >= 0x100000ULL) goto loc_003282FE;
loc_00328485:
    if ((*(unsigned __int64 *)(a1)) > (a3 - 16)) goto loc_00328137;
    if (!sign_flag) goto loc_00328137;
    if ((*(unsigned __int8 *)(1)) == 1) goto loc_0032817F;
    if ((*(unsigned __int8 *)(1)) == 3) goto loc_0032817F;
    result = (v_rsi) & (-2);
    if ((*(unsigned __int8 *)(result)) == 6) goto loc_0032817F;
loc_003284D1:
    if ((*(unsigned __int64 *)(a1)) <= result) goto loc_0032817F;
    goto loc_00328143;
loc_003284E9:
    a2 = 0;
    result = KeInvalidAccessAllowed(v_rsi, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_003283CE;
    v_stack_p20 = 15;
    result = KeBugCheckEx(80, *(unsigned __int64 *)(a1), (unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL))) + a1 * 8, v_rsi);
loc_00328518:
    result = MiSetFaultPacketDirectives(a1, (unsigned int)((unsigned int)(result)), v_stack_p70, v_rsi);
    goto loc_0032820D;
loc_0032852C:
    result = MiLockNestedPageTable(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL))) + a1 * 8 + 8), v_stack_p70, v_rsi);
    result = MiPfnIsActivePageTable((unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL))) + a1 * 8, *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL))) + a1 * 8 + 8), v_stack_p70, v_rsi);
    result = MiLockPageAndSetDirty((unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL))) + a1 * 8, result + 1, v_stack_p70, v_rsi);
}
```

## 5. (Beta) C Style

```c
int64_t MiValidFault(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (48);
    local_r12 = (*(uint64_t *)(arg1)) >> (9);
    local_r12 = (local_r12) & (result);
    local_r12 = (local_r12) + (a3);
    Arg2 = (uint32_t)((*(uint64_t *)(arg1 + 0x10)) & (1));
    v_stack_p18 = local_r12;
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) & (-2);
    if (Arg2 != 0) goto loc_003282AC;
loc_0032812B:
    if ((*(uint64_t *)(arg1)) >= a3) goto loc_00328485;
loc_00328137:
    local_rbx = 0;
    if ((((uint8_t)(Arg2)) & (4)) == 0) goto loc_003284D1;
loc_00328143:
    if (((*(uint32_t *)(arg1 + 0x50)) & (256)) == 0) goto loc_003283A2;
loc_0032815B:
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x8))) & (2)) != 0) goto loc_00328189;
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x8))) & (16)) != 0) goto loc_00328305;
loc_0032816B:
    if (!sign_flag) goto loc_003281E8;
    result = MI_IS_PTE_SHADOW_STACK(Arg2, Arg2, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_003281E8;
loc_0032817F:
    goto loc_0032820D;
loc_00328189:
    if (condition_is_below) goto loc_0032827C;
    if (condition_is_above_or_equal) goto loc_0032817F;
    if (!sign_flag) goto loc_00328332;
loc_003281A9:
    result = (Arg2) >> (12);
    result = (result) & (Arg2);
    if (result > (*(uint64_t *)(v_rip + 0xB05B1C))) goto loc_003281E8;
    Arg1 = (result + result * 2) + (result + result * 2);
    result = (*(uint64_t *)(result + arg1 * 8)) >> (54);
    if (condition_is_below) goto loc_00328225;
loc_003281E8:
    v_stack_m40 = Arg2;
    result = MiNoFaultFound(Arg1, local_r12, *(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x10));
loc_00328203:
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (1)) != 0) goto loc_00328382;
loc_0032820D:
loc_0032820F:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL)));
loc_00328225:
    result = MiInvalidPteConforms(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL))) + arg1 * 8 + 0x10), local_r12, *(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x10));
    if ((uint32_t)(result) == 0) goto loc_00328257;
    if (condition_is_below) goto loc_00328257;
    result = MiGetPagingFileOffset(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL))) + arg1 * 8 + 0x10), local_r12, *(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x10));
    if ((uint32_t)(result) != 0) goto loc_003283ED;
loc_00328257:
    if (!sign_flag) goto loc_003281E8;
    if (condition_is_above_or_equal) goto loc_003281E8;
    result = MiCheckAndUpdateIoAttribution((uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL))) + Arg1 * 8, local_r12, *(uint64_t *)(arg1), *(uint64_t *)(arg1 + 0x10));
    goto loc_003281E8;
loc_0032827C:
    a4 = 0;
    a3 = (*(uint64_t *)(arg1)) | (-1);
    v_stack_p20 = v_stack_p70;
    result = MiCopyOnWrite(*(uint64_t *)(arg1), local_r12, a3, a4);
    if (sign_flag) goto loc_00328518;
    goto loc_00328203;
loc_003282AC:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1)))) == 1) goto loc_003283DD;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1)))) != 3) goto loc_0032812B;
    local_rdi = (Arg2) >> (12);
    local_rdi = (local_rdi) & (*(uint64_t *)(arg1));
    if (local_rdi > (*(uint64_t *)(v_rip + 0xB05A0A))) goto loc_003282FE;
    local_rbx = (local_rdi + local_rdi * 2) + (local_rdi + local_rdi * 2);
    result = (*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(arg1)) + local_rbx * 8)) >> (54);
    if (condition_is_below) goto loc_0032840D;
loc_003282FE:
    result = 0;
    goto loc_0032820F;
loc_00328305:
    if (((*(uint32_t *)(arg1 + 0x50)) & (256)) != 0) goto loc_0032816B;
    result = MiCheckSystemNxFault(Arg1, local_rdi, 5, a4);
    goto loc_0032816B;
loc_00328332:
    if ((((uint8_t)(local_rdi)) & (66)) != 0) goto loc_003281A9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1F4)))) & (16)) == 0) goto loc_003281A9;
    if ((*(uint64_t *)(arg1)) >= Arg1) goto loc_003281A9;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A9)) & (16)) != 0) goto loc_003281A9;
    goto loc_0032820D;
loc_00328382:
    local_rsi = (*(uint64_t *)(arg1 + 0x10)) & (-2);
    if ((*(uint8_t *)(local_rsi)) != 5) goto loc_0032820D;
    result = MiValidVirtualizationFault(Arg1, local_rsi, local_r12, a4);
    goto loc_0032820D;
loc_003283A2:
    if (local_rsi == 0) goto loc_0032815B;
    if ((*(uint64_t *)(arg1)) >= Arg1) goto loc_0032815B;
    if ((((uint8_t)(local_rsi)) & (1)) != 0) goto loc_0032815B;
    result = KeIsUserVaAccessAllowed(local_rsi, local_rsi, local_r12, a4);
    if ((uint8_t)(result) == 0) goto loc_003284E9;
loc_003283CE:
    goto loc_0032815B;
loc_003283DD:
    a3 = 0;
    result = MiUpdatePrefetchPriority(local_rsi, *(uint64_t *)(arg1), a3, a4);
    goto loc_003282FE;
loc_003283ED:
    result = MiPfnIsPageTable((uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL))) + Arg1 * 8, *(uint64_t *)(arg1), a3, a4);
    if ((uint32_t)(result) != 0) goto loc_0032852C;
    result = MiLockPageAndSetDirty((uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL))) + Arg1 * 8, result + 1, a3, a4);
    goto loc_00328257;
loc_0032840D:
    result = MiLockVadTree(1, result + 1, a3, a4);
    result = MiLocateAddress(*(uint64_t *)(arg1), result + 1, a3, a4);
    result = MiUnlockVadTree(1, 17, a3, a4);
    if (result == 0) goto loc_003282FE;
    a3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) & (112));
    if (((uint32_t)(a3)) == 48) goto loc_003282FE;
    if ((((uint32_t)(a3 - 16)) & (0xFFFFFFBFULL)) == 0) goto loc_003282FE;
    if (condition_is_below) goto loc_003282FE;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0x180000ULL));
    if (((uint32_t)(Arg2)) >= 0x100000ULL) goto loc_003282FE;
loc_00328485:
    if ((*(uint64_t *)(arg1)) > (a3 - 16)) goto loc_00328137;
    if (!sign_flag) goto loc_00328137;
    if ((*(uint8_t *)(1)) == 1) goto loc_0032817F;
    if ((*(uint8_t *)(1)) == 3) goto loc_0032817F;
    result = (local_rsi) & (-2);
    if ((*(uint8_t *)(result)) == 6) goto loc_0032817F;
loc_003284D1:
    if ((*(uint64_t *)(arg1)) <= result) goto loc_0032817F;
    goto loc_00328143;
loc_003284E9:
    Arg2 = 0;
    result = KeInvalidAccessAllowed(local_rsi, Arg2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_003283CE;
    v_stack_p20 = 15;
    result = KeBugCheckEx(80, *(uint64_t *)(arg1), (uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL))) + Arg1 * 8, local_rsi);
loc_00328518:
    result = MiSetFaultPacketDirectives(Arg1, (uint32_t)((uint32_t)(result)), v_stack_p70, local_rsi);
    goto loc_0032820D;
loc_0032852C:
    result = MiLockNestedPageTable(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL))) + arg1 * 8 + 0x8), v_stack_p70, local_rsi);
    result = MiPfnIsActivePageTable((uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL))) + Arg1 * 8, *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL))) + arg1 * 8 + 0x8), v_stack_p70, local_rsi);
    result = MiLockPageAndSetDirty((uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL))) + Arg1 * 8, result + 1, v_stack_p70, local_rsi);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003280B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
