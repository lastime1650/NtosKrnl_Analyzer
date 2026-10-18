# MiUpdateSystemProtoPtesTree

- RVA: `0x00295F0C`–`0x002962F5` (길이 `1,001` bytes)
- VA: `0x0000000140295F0C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006789C`
- 디코드: `256`개 명령, `1,001/1,001` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00295F5B` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x00296046` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0029608B` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x002960DE` → [RtlAvlRemoveNode](RtlAvlRemoveNode_function_00296650.md) (function, `0x00296650`)
- `0x00296126` → [RtlpTreeDoubleRotateNodes](RtlpTreeDoubleRotateNodes_function_00296C74.md) (function, `0x00296C74`)
- `0x002961C7` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x002961EB` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)

### Direct callers
- [MiCreatePrototypePtes](MiCreatePrototypePtes_function_002950FC.md) at `0x00295343`
- [MiDeleteCachedSubsection](MiDeleteCachedSubsection_function_00297888.md) at `0x00297B29`
- [MiEntireSubsectionIsPurged](MiEntireSubsectionIsPurged_function_00297C04.md) at `0x00297C77`
- [MiDeleteSubsectionPages](../32/MiDeleteSubsectionPages_function_00326340.md) at `0x003263F5`
- [MiDeletePerSessionProtos](../4A/MiDeletePerSessionProtos_function_004A0840.md) at `0x004A08FA`
- [MiDeleteEmptySubsections](../4E/MiDeleteEmptySubsections_function_004ED818.md) at `0x004ED8EF`
- [MiExtendSection](../../page/98/MiExtendSection_function_00982FDC.md) at `0x00983332`
- [MiCreatePagingFileMap](../../page/98/MiCreatePagingFileMap_function_009852F8.md) at `0x0098570E`
- [MiCreatePagingFileMap](../../page/98/MiCreatePagingFileMap_function_009852F8.md) at `0x00985941`
- [MiCreateImageFileMap](../../page/98/MiCreateImageFileMap_function_00986830.md) at `0x00986E59`
- [MiBuildImageControlArea](../../page/98/MiBuildImageControlArea_function_009878A4.md) at `0x00987C1F`
- [MiSegmentDelete](../../page/A1/MiSegmentDelete_function_00A1FBB4.md) at `0x00A1FCBA`
- [MiDeletePageFileSectionNodes](../../page/A1/MiDeletePageFileSectionNodes_function_00A1FD50.md) at `0x00A1FD78`
- [MiAllocatePerSessionProtos](../../page/A6/MiAllocatePerSessionProtos_function_00A66830.md) at `0x00A66935`
- [MiAllocateFileExtents](../../page/AB/MiAllocateFileExtents_function_00ABDF54.md) at `0x00ABE3BD`
- [MiAllocateFileExtents](../../page/AB/MiAllocateFileExtents_function_00ABDF54.md) at `0x00ABE44A`
- [sub_00B2A916](../../page/B2/Unknown_function_00B2A916.md) at `0x00B2A96F`

### Static image references
- `0x00295F47` → RVA `0x00E2D710` (`.data`; read)
- `0x00295F6A` → RVA `0x00E2D708` (`.data`; read)
- `0x0029601F` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0029602C` → RVA `0x00E2D710` (`.data`; write)
- `0x00296036` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0029618C` → RVA `0x00E2D708` (`.data`; write)
- `0x002961AD` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002962D5` → [sub_006DA6D2](../6D/Unknown_function_006DA6D2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00295F0C  48 8B C4                        mov rax, rsp
00295F0F  48 89 58 08                     mov qword ptr [rax + 8], rbx
00295F13  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00295F17  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00295F1B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00295F1F  41 54                           push r12
00295F21  41 56                           push r14
00295F23  41 57                           push r15
00295F25  48 83 EC 30                     sub rsp, 0x30
00295F29  48 8D 79 18                     lea rdi, [rcx + 0x18]
00295F2D  8B EA                           mov ebp, edx
00295F2F  8B 07                           mov eax, dword ptr [rdi]
00295F31  48 8B D9                        mov rbx, rcx
00295F34  41 BE 80 00 00 00               mov r14d, 0x80
00295F3A  83 E0 07                        and eax, 7
00295F3D  0F 85 82 01 00 00               jne 0x1402960c5
00295F43  48 8B 71 90                     mov rsi, qword ptr [rcx - 0x70]
00295F47  48 8D 0D C2 77 B9 00            lea rcx, [rip + 0xb977c2]
00295F4E  40 F6 C5 02                     test bpl, 2
00295F52  0F 84 33 01 00 00               je 0x14029608b
00295F58  41 B7 11                        mov r15b, 0x11
00295F5B  E8 20 2F FB FF                  call 0x140248e80
00295F60  40 F6 C5 01                     test bpl, 1
00295F64  0F 84 6A 01 00 00               je 0x1402960d4
00295F6A  48 8B 15 97 77 B9 00            mov rdx, qword ptr [rip + 0xb97797]
00295F71  32 C9                           xor cl, cl
00295F73  48 85 D2                        test rdx, rdx
00295F76  74 24                           je 0x140295f9c
00295F78  8B 42 18                        mov eax, dword ptr [rdx + 0x18]
00295F7B  83 E0 07                        and eax, 7
00295F7E  75 78                           jne 0x140295ff8
00295F80  48 8B 42 90                     mov rax, qword ptr [rdx - 0x70]
00295F84  48 3B F0                        cmp rsi, rax
00295F87  0F 82 24 01 00 00               jb 0x1402960b1
00295F8D  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00295F91  48 85 C0                        test rax, rax
00295F94  0F 85 23 01 00 00               jne 0x1402960bd
00295F9A  B1 01                           mov cl, 1
00295F9C  48 83 23 00                     and qword ptr [rbx], 0
00295FA0  48 8B FB                        mov rdi, rbx
00295FA3  48 83 63 08 00                  and qword ptr [rbx + 8], 0
00295FA8  48 89 53 10                     mov qword ptr [rbx + 0x10], rdx
00295FAC  48 85 D2                        test rdx, rdx
00295FAF  0F 84 D7 01 00 00               je 0x14029618c
00295FB5  0F B6 C1                        movzx eax, cl
00295FB8  48 89 1C C2                     mov qword ptr [rdx + rax*8], rbx
00295FBC  8A C1                           mov al, cl
00295FBE  4C 8D 72 10                     lea r14, [rdx + 0x10]
00295FC2  41 8A 36                        mov sil, byte ptr [r14]
00295FC5  02 C0                           add al, al
00295FC7  FE C8                           dec al
00295FC9  40 8A EE                        mov bpl, sil
00295FCC  44 8A C0                        mov r8b, al
00295FCF  41 80 E0 03                     and r8b, 3
00295FD3  40 80 E5 03                     and bpl, 3
00295FD7  75 2B                           jne 0x140296004
00295FD9  40 32 C6                        xor al, sil
00295FDC  48 8B FA                        mov rdi, rdx
00295FDF  24 03                           and al, 3
00295FE1  40 32 C6                        xor al, sil
00295FE4  41 88 06                        mov byte ptr [r14], al
00295FE7  49 8B 16                        mov rdx, qword ptr [r14]
00295FEA  48 83 E2 FC                     and rdx, 0xfffffffffffffffc
00295FEE  74 24                           je 0x140296014
00295FF0  48 39 3A                        cmp qword ptr [rdx], rdi
00295FF3  0F 95 C1                        setne cl
00295FF6  EB C4                           jmp 0x140295fbc
00295FF8  48 83 E8 01                     sub rax, 1
00295FFC  75 75                           jne 0x140296073
00295FFE  48 8B 42 D0                     mov rax, qword ptr [rdx - 0x30]
00296002  EB 80                           jmp 0x140295f84
00296004  41 3A E8                        cmp bpl, r8b
00296007  0F 84 FB 00 00 00               je 0x140296108
0029600D  40 80 E6 FC                     and sil, 0xfc
00296011  41 88 36                        mov byte ptr [r14], sil
00296014  48 83 4B 18 08                  or qword ptr [rbx + 0x18], 8
00296019  41 80 FF 11                     cmp r15b, 0x11
0029601D  74 79                           je 0x140296098
0029601F  F6 05 E0 0A D3 00 01            test byte ptr [rip + 0xd30ae0], 1
00296026  0F 85 81 01 00 00               jne 0x1402961ad
0029602C  C7 05 DA 76 B9 00 00 00 00 00   mov dword ptr [rip + 0xb976da], 0
00296036  83 3D E3 0C D3 00 00            cmp dword ptr [rip + 0xd30ce3], 0
0029603D  74 0C                           je 0x14029604b
0029603F  44 0F 20 C1                     mov rcx, cr8
00296043  41 8A D7                        mov dl, r15b
00296046  E8 4D F6 25 00                  call 0x1404f5698
0029604B  41 0F B6 C7                     movzx eax, r15b
0029604F  44 0F 22 C0                     mov cr8, rax
00296053  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00296058  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0029605D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00296062  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00296067  48 83 C4 30                     add rsp, 0x30
0029606B  41 5F                           pop r15
0029606D  41 5E                           pop r14
0029606F  41 5C                           pop r12
00296071  C3                              ret
00296072  CC                              int3
00296073  48 83 E8 01                     sub rax, 1
00296077  0F 85 78 01 00 00               jne 0x1402961f5
0029607D  48 8B 42 C8                     mov rax, qword ptr [rdx - 0x38]
00296081  4A 8B 44 30 08                  mov rax, qword ptr [rax + r14 + 8]
00296086  E9 F9 FE FF FF                  jmp 0x140295f84
0029608B  E8 00 26 FB FF                  call 0x140248690
00296090  44 8A F8                        mov r15b, al
00296093  E9 C8 FE FF FF                  jmp 0x140295f60
00296098  F6 05 67 0A D3 00 01            test byte ptr [rip + 0xd30a67], 1
0029609F  0F 85 2C 01 00 00               jne 0x1402961d1
002960A5  C7 05 61 76 B9 00 00 00 00 00   mov dword ptr [rip + 0xb97661], 0
002960AF  EB A2                           jmp 0x140296053
002960B1  48 8B 02                        mov rax, qword ptr [rdx]
002960B4  48 85 C0                        test rax, rax
002960B7  0F 84 DF FE FF FF               je 0x140295f9c
002960BD  48 8B D0                        mov rdx, rax
002960C0  E9 B3 FE FF FF                  jmp 0x140295f78
002960C5  48 83 E8 01                     sub rax, 1
002960C9  75 21                           jne 0x1402960ec
002960CB  48 8B 71 D0                     mov rsi, qword ptr [rcx - 0x30]
002960CF  E9 73 FE FF FF                  jmp 0x140295f47
002960D4  48 8B D3                        mov rdx, rbx
002960D7  48 8D 0D 2A 76 B9 00            lea rcx, [rip + 0xb9762a]
002960DE  E8 6D 05 00 00                  call 0x140296650
002960E3  48 83 27 F7                     and qword ptr [rdi], 0xfffffffffffffff7
002960E7  E9 2D FF FF FF                  jmp 0x140296019
002960EC  48 83 E8 01                     sub rax, 1
002960F0  0F 85 12 01 00 00               jne 0x140296208
002960F6  48 8B 41 C8                     mov rax, qword ptr [rcx - 0x38]
002960FA  48 8D 79 18                     lea rdi, [rcx + 0x18]
002960FE  4A 8B 74 30 08                  mov rsi, qword ptr [rax + r14 + 8]
00296103  E9 3F FE FF FF                  jmp 0x140295f47
00296108  0F B6 47 10                     movzx eax, byte ptr [rdi + 0x10]
0029610C  83 E0 03                        and eax, 3
0029610F  44 0F B6 E5                     movzx r12d, bpl
00296113  44 0F B6 C9                     movzx r9d, cl
00296117  41 3B C4                        cmp eax, r12d
0029611A  74 54                           je 0x140296170
0029611C  4C 8B C7                        mov r8, rdi
0029611F  48 8D 0D E2 75 B9 00            lea rcx, [rip + 0xb975e2]
00296126  E8 49 0B 00 00                  call 0x140296c74
0029612B  41 80 26 FC                     and byte ptr [r14], 0xfc
0029612F  4C 8B C0                        mov r8, rax
00296132  44 8A 4F 10                     mov r9b, byte ptr [rdi + 0x10]
00296136  41 8A C9                        mov cl, r9b
00296139  80 E1 FC                        and cl, 0xfc
0029613C  88 4F 10                        mov byte ptr [rdi + 0x10], cl
0029613F  0F B6 50 10                     movzx edx, byte ptr [rax + 0x10]
00296143  8B CA                           mov ecx, edx
00296145  83 E1 03                        and ecx, 3
00296148  44 3B E1                        cmp r12d, ecx
0029614B  74 4B                           je 0x140296198
0029614D  83 F2 FE                        xor edx, 0xfffffffe
00296150  83 E2 03                        and edx, 3
00296153  44 3B E2                        cmp r12d, edx
00296156  75 0E                           jne 0x140296166
00296158  41 8A C1                        mov al, r9b
0029615B  40 32 C6                        xor al, sil
0029615E  24 03                           and al, 3
00296160  41 32 C1                        xor al, r9b
00296163  88 47 10                        mov byte ptr [rdi + 0x10], al
00296166  41 80 60 10 FC                  and byte ptr [r8 + 0x10], 0xfc
0029616B  E9 A4 FE FF FF                  jmp 0x140296014
00296170  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00296174  41 83 F1 01                     xor r9d, 1
00296178  48 83 E0 FC                     and rax, 0xfffffffffffffffc
0029617C  48 3B C2                        cmp rax, rdx
0029617F  0F 84 96 00 00 00               je 0x14029621b
00296185  B9 1D 00 00 00                  mov ecx, 0x1d
0029618A  CD 29                           int 0x29
0029618C  48 89 1D 75 75 B9 00            mov qword ptr [rip + 0xb97575], rbx
00296193  E9 7C FE FF FF                  jmp 0x140296014
00296198  41 8A 06                        mov al, byte ptr [r14]
0029619B  8A C8                           mov cl, al
0029619D  40 32 CD                        xor cl, bpl
002961A0  80 F1 FE                        xor cl, 0xfe
002961A3  80 E1 03                        and cl, 3
002961A6  32 C8                           xor cl, al
002961A8  41 88 0E                        mov byte ptr [r14], cl
002961AB  EB B9                           jmp 0x140296166
002961AD  8B 05 A5 7C C7 00               mov eax, dword ptr [rip + 0xc77ca5]
002961B3  85 C0                           test eax, eax
002961B5  0F 85 71 FE FF FF               jne 0x14029602c
002961BB  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002961C0  48 8D 0D 49 75 B9 00            lea rcx, [rip + 0xb97549]
002961C7  E8 78 AD 02 00                  call 0x1402c0f44
002961CC  E9 65 FE FF FF                  jmp 0x140296036
002961D1  8B 05 81 7C C7 00               mov eax, dword ptr [rip + 0xc77c81]
002961D7  85 C0                           test eax, eax
002961D9  0F 85 C6 FE FF FF               jne 0x1402960a5
002961DF  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002961E4  48 8D 0D 25 75 B9 00            lea rcx, [rip + 0xb97525]
002961EB  E8 54 AD 02 00                  call 0x1402c0f44
002961F0  E9 5E FE FF FF                  jmp 0x140296053
002961F5  48 83 E8 01                     sub rax, 1
002961F9  0F 85 E3 00 00 00               jne 0x1402962e2
002961FF  48 8B 42 30                     mov rax, qword ptr [rdx + 0x30]
00296203  E9 7C FD FF FF                  jmp 0x140295f84
00296208  48 83 E8 01                     sub rax, 1
0029620C  0F 85 BF 00 00 00               jne 0x1402962d1
00296212  48 8B 71 30                     mov rsi, qword ptr [rcx + 0x30]
00296216  E9 2C FD FF FF                  jmp 0x140295f47
0029621B  41 8B C1                        mov eax, r9d
0029621E  48 83 F0 01                     xor rax, 1
00296222  48 39 3C C2                     cmp qword ptr [rdx + rax*8], rdi
00296226  0F 85 59 FF FF FF               jne 0x140296185
0029622C  4C 8B 42 10                     mov r8, qword ptr [rdx + 0x10]
00296230  49 8B C8                        mov rcx, r8
00296233  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
00296237  74 7F                           je 0x1402962b8
00296239  48 39 51 08                     cmp qword ptr [rcx + 8], rdx
0029623D  75 6B                           jne 0x1402962aa
0029623F  48 89 79 08                     mov qword ptr [rcx + 8], rdi
00296243  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00296247  48 8B C8                        mov rcx, rax
0029624A  49 33 C8                        xor rcx, r8
0029624D  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
00296251  48 33 C8                        xor rcx, rax
00296254  48 89 4F 10                     mov qword ptr [rdi + 0x10], rcx
00296258  4E 8B 04 CF                     mov r8, qword ptr [rdi + r9*8]
0029625C  4D 85 C0                        test r8, r8
0029625F  75 29                           jne 0x14029628a
00296261  41 8B C1                        mov eax, r9d
00296264  48 83 F0 01                     xor rax, 1
00296268  4C 89 04 C2                     mov qword ptr [rdx + rax*8], r8
0029626C  4A 89 14 CF                     mov qword ptr [rdi + r9*8], rdx
00296270  8B 42 10                        mov eax, dword ptr [rdx + 0x10]
00296273  83 E0 03                        and eax, 3
00296276  48 0B C7                        or rax, rdi
00296279  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
0029627D  80 67 10 FC                     and byte ptr [rdi + 0x10], 0xfc
00296281  80 62 10 FC                     and byte ptr [rdx + 0x10], 0xfc
00296285  E9 8A FD FF FF                  jmp 0x140296014
0029628A  49 8B 48 10                     mov rcx, qword ptr [r8 + 0x10]
0029628E  48 8B C1                        mov rax, rcx
00296291  48 83 E0 FC                     and rax, 0xfffffffffffffffc
00296295  48 3B C7                        cmp rax, rdi
00296298  0F 85 E7 FE FF FF               jne 0x140296185
0029629E  83 E1 03                        and ecx, 3
002962A1  48 0B CA                        or rcx, rdx
002962A4  49 89 48 10                     mov qword ptr [r8 + 0x10], rcx
002962A8  EB B7                           jmp 0x140296261
002962AA  48 39 11                        cmp qword ptr [rcx], rdx
002962AD  0F 85 D2 FE FF FF               jne 0x140296185
002962B3  48 89 39                        mov qword ptr [rcx], rdi
002962B6  EB 8B                           jmp 0x140296243
002962B8  48 39 15 49 74 B9 00            cmp qword ptr [rip + 0xb97449], rdx
002962BF  0F 85 C0 FE FF FF               jne 0x140296185
002962C5  48 89 3D 3C 74 B9 00            mov qword ptr [rip + 0xb9743c], rdi
002962CC  E9 72 FF FF FF                  jmp 0x140296243
002962D1  48 83 F8 01                     cmp rax, 1
002962D5  0F 84 F7 43 44 00               je 0x1406da6d2
002962DB  33 F6                           xor esi, esi
002962DD  E9 65 FC FF FF                  jmp 0x140295f47
002962E2  48 83 F8 01                     cmp rax, 1
002962E6  0F 85 A1 FC FF FF               jne 0x140295f8d
002962EC  48 8B 42 20                     mov rax, qword ptr [rdx + 0x20]
002962F0  E9 8F FC FF FF                  jmp 0x140295f84
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUpdateSystemProtoPtesTree(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 24))) & (7));
    if (condition_is_not_equal) goto loc_002960C5;
loc_00295F47:
    if ((((unsigned __int8)((unsigned int)(a2))) & (2)) == 0) goto loc_0029608B;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12154818, a2, a3, a4);
loc_00295F60:
    if ((((unsigned __int8)((unsigned int)(a2))) & (1)) == 0) goto loc_002960D4;
    a1 = 0;
    if (*(unsigned __int64 *)(v_rip + 12154775) == 0) goto loc_00295F9C;
loc_00295F78:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12154775) + 24))) & (7));
    if (condition_is_not_equal) goto loc_00295FF8;
loc_00295F84:
    if ((*(unsigned __int64 *)(a1 - 112)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12154775) - 112))) goto loc_002960B1;
loc_00295F8D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12154775) + 8) != 0) goto loc_002960BD;
loc_00295F9C:
    *(unsigned __int64 *)(a1 + 16) = *(unsigned __int64 *)(v_rip + 12154775);
    if (*(unsigned __int64 *)(v_rip + 12154775) == 0) goto loc_0029618C;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12154775) + 1 * 8) = 0;
loc_00295FBC:
    result = (unsigned __int8)((1) + (1));
    result = (unsigned __int8)((result) - 1);
    a3 = (unsigned __int8)(((unsigned __int8)(result)) & (3));
    v_rbp = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12154775) + 16))) & (3));
    if (condition_is_not_equal) goto loc_00296004;
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12154775) + 16))));
    result = (unsigned __int8)((result) & (3));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12154775) + 16))));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12154775) + 16) = (unsigned __int8)(result);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12154775) + 16)) & (-4);
    if (condition_is_equal) goto loc_00296014;
    a1 = ((*(unsigned __int64 *)(a2)) != (*(unsigned __int64 *)(v_rip + 12154775))) ? 1 : 0;
    goto loc_00295FBC;
loc_00295FF8:
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00296073;
    goto loc_00295F84;
loc_00296004:
    if (((unsigned __int8)(v_rbp)) == ((unsigned __int8)(a3))) goto loc_00296108;
    v_rsi = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12154775) + 16)) & (252));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12154775) + 16) = (unsigned __int8)(v_rsi);
loc_00296014:
loc_00296019:
    if (17 == 17) goto loc_00296098;
    if (((*(unsigned __int8 *)(v_rip + 13830880)) & (1)) != 0) goto loc_002961AD;
loc_0029602C:
    *(unsigned int *)(v_rip + 12154586) = 0;
loc_00296036:
    result = *(unsigned __int64 *)(a2 - 48);
    if ((*(unsigned int *)(v_rip + 13831395)) != 0) {
        a1 = v_cr8;
        a2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_00296053:
    v_rsp = (v_rsp) + (48);
    return 17;
loc_00296073:
    result = (17) - (1);
    if (condition_is_not_equal) goto loc_002961F5;
    goto loc_00295F84;
loc_0029608B:
    result = ExAcquireSpinLockExclusive(a1, a2, a3, a4);
    goto loc_00295F60;
loc_00296098:
    if (((*(unsigned __int8 *)(v_rip + 13830759)) & (1)) != 0) goto loc_002961D1;
loc_002960A5:
    *(unsigned int *)(v_rip + 12154465) = 0;
    goto loc_00296053;
loc_002960B1:
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00295F9C;
loc_002960BD:
    goto loc_00295F78;
loc_002960C5:
    result = (*(unsigned __int64 *)(a2)) - (1);
    if (condition_is_not_equal) goto loc_002960EC;
    goto loc_00295F47;
loc_002960D4:
    result = RtlAvlRemoveNode(v_rip + 12154410, v_stack_p8, a3, a4);
    goto loc_00296019;
loc_002960EC:
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00296208;
    goto loc_00295F47;
loc_00296108:
    result = (unsigned int)((*(unsigned __int8 *)(v_rip + 12154410 + 24 + 16)) & (3));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned __int8)(v_stack_p10)))) goto loc_00296170;
    result = RtlpTreeDoubleRotateNodes(v_rip + 12154338, v_stack_p8, v_rip + 12154410 + 24, (unsigned __int8)(v_rip + 12154410));
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12154410 + 24 + 16))) & (252));
    *(unsigned __int8 *)(v_rip + 12154410 + 24 + 16) = (unsigned __int8)(a1);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(result + 16)))) & (3));
    if (((unsigned int)((unsigned __int8)(v_stack_p10))) == ((unsigned int)(a1))) goto loc_00296198;
    a2 = (unsigned int)((*(unsigned __int8 *)(result + 16)) ^ (0xFFFFFFFEULL));
    a2 = (unsigned int)((a2) & (3));
    if (((unsigned int)((unsigned __int8)(v_stack_p10))) == a2) {
        result = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 12154410 + 24 + 16));
        result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12154410 - 56) + *(unsigned __int64 *)(v_rip + 12154775) + 16 * 1 + 8))));
        result = (unsigned __int8)((result) & (3));
        result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12154410 + 24 + 16))));
        *(unsigned __int8 *)(v_rip + 12154410 + 24 + 16) = (unsigned __int8)(result);
    }
    goto loc_00296014;
loc_00296170:
    a4 = (unsigned int)((*(unsigned __int8 *)(v_rip + 12154410 + 24 + 16)) ^ (1));
    result = (*(unsigned __int64 *)(v_rip + 12154410 + 24 + 16)) & (-4);
    if (result == a2) goto loc_0029621B;
loc_00296185:
loc_0029618C:
    *(unsigned __int64 *)(v_rip + 12154229) = v_stack_p8;
    goto loc_00296014;
loc_00296198:
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12154775) + 16))) ^ ((unsigned __int8)(v_stack_p10)));
    a1 = (unsigned __int8)((a1) ^ (254));
    a1 = (unsigned __int8)((a1) & (3));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12154775) + 16))));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12154775) + 16) = (unsigned __int8)(a1);
    goto loc_00296166;
loc_002961AD:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13073573))) != 0) goto loc_0029602C;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rip + 12154185, v_stack_p48, result, a4);
    goto loc_00296036;
loc_002961D1:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13073537))) != 0) goto loc_002960A5;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rip + 12154149, v_stack_p48, result, a4);
    goto loc_00296053;
loc_002961F5:
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_002962E2;
    goto loc_00295F84;
loc_00296208:
    result = (*(unsigned __int64 *)(v_stack_p48 + 48)) - (1);
    if (condition_is_not_equal) goto loc_002962D1;
    goto loc_00295F47;
loc_0029621B:
    result = ((unsigned int)((unsigned int)(a4))) ^ (1);
    if ((*(unsigned __int64 *)(v_stack_p48 + result * 8)) != (v_rip + 12154410 + 24)) goto loc_00296185;
    a1 = (*(unsigned __int64 *)(v_stack_p48 + 16)) & (-4);
    if (condition_is_equal) goto loc_002962B8;
    if ((*(unsigned __int64 *)(a1 + 8)) != v_stack_p48) goto loc_002962AA;
    *(unsigned __int64 *)(a1 + 8) = v_rip + 12154410 + 24;
loc_00296243:
    a1 = (*(unsigned __int64 *)(v_rip + 12154410 + 24 + 16)) ^ (*(unsigned __int64 *)(v_stack_p48 + 16));
    a1 = (a1) & (-4);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_rip + 12154410 + 24 + 16));
    *(unsigned __int64 *)(v_rip + 12154410 + 24 + 16) = a1;
    if (*(unsigned __int64 *)(v_rip + 12154410 + 24 + a4 * 8) != 0) goto loc_0029628A;
loc_00296261:
    result = ((unsigned int)((unsigned int)(a4))) ^ (1);
    *(unsigned __int64 *)(v_stack_p48 + result * 8) = *(unsigned __int64 *)(v_rip + 12154410 + 24 + a4 * 8);
    *(unsigned __int64 *)(v_rip + 12154410 + 24 + a4 * 8) = v_stack_p48;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p48 + 16))) & (3));
    result = (result) | (v_rip + 12154410 + 24);
    *(unsigned __int64 *)(v_stack_p48 + 16) = result;
    goto loc_00296014;
loc_0029628A:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12154410 + 24 + a4 * 8) + 16)) & (-4);
    if (result != (v_rip + 12154410 + 24)) goto loc_00296185;
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12154410 + 24 + a4 * 8) + 16)) & (3));
    a1 = (a1) | (v_stack_p48);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12154410 + 24 + a4 * 8) + 16) = a1;
    goto loc_00296261;
loc_002962AA:
    if ((*(unsigned __int64 *)(a1)) != v_stack_p48) goto loc_00296185;
    *(unsigned __int64 *)(a1) = v_rip + 12154410 + 24;
    goto loc_00296243;
loc_002962B8:
    if ((*(unsigned __int64 *)(v_rip + 12153929)) != v_stack_p48) goto loc_00296185;
    *(unsigned __int64 *)(v_rip + 12153916) = v_rip + 12154410 + 24;
    goto loc_00296243;
loc_002962D1:
    v_rsi = 0;
    goto loc_00295F47;
loc_002962E2:
    if (result != 1) goto loc_00295F8D;
    goto loc_00295F84;
}
```

## 5. (Beta) C Style

```c
int64_t MiUpdateSystemProtoPtesTree(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x18))) & (7));
    if (condition_is_not_equal) goto loc_002960C5;
loc_00295F47:
    if ((((uint8_t)((uint32_t)(Arg2))) & (2)) == 0) goto loc_0029608B;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12154818, Arg2, a3, a4);
loc_00295F60:
    if ((((uint8_t)((uint32_t)(Arg2))) & (1)) == 0) goto loc_002960D4;
    Arg1 = 0;
    if (*(uint64_t *)(v_rip + 0xB97797) == 0) goto loc_00295F9C;
loc_00295F78:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x18))) & (7));
    if (condition_is_not_equal) goto loc_00295FF8;
loc_00295F84:
    if ((*(uint64_t *)(arg1 - 0x70)) < (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB97797) - 0x70))) goto loc_002960B1;
loc_00295F8D:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x8) != 0) goto loc_002960BD;
loc_00295F9C:
    *(uint64_t *)(arg1 + 0x10) = *(uint64_t *)(v_rip + 0xB97797);
    if (*(uint64_t *)(v_rip + 0xB97797) == 0) goto loc_0029618C;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x1 * 8) = 0;
loc_00295FBC:
    result = (uint8_t)((1) + (1));
    result = (uint8_t)((result) - 1);
    a3 = (uint8_t)(((uint8_t)(result)) & (3));
    local_rbp = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x10))) & (3));
    if (condition_is_not_equal) goto loc_00296004;
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x10))));
    result = (uint8_t)((result) & (3));
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x10))));
    *(uint8_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x10) = (uint8_t)(result);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x10)) & (-4);
    if (condition_is_equal) goto loc_00296014;
    Arg1 = ((*(uint64_t *)(Arg2)) != (*(uint64_t *)(v_rip + 0xB97797))) ? 1 : 0;
    goto loc_00295FBC;
loc_00295FF8:
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00296073;
    goto loc_00295F84;
loc_00296004:
    if (((uint8_t)(local_rbp)) == ((uint8_t)(a3))) goto loc_00296108;
    local_rsi = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x10)) & (252));
    *(uint8_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x10) = (uint8_t)(local_rsi);
loc_00296014:
loc_00296019:
    if (17 == 17) goto loc_00296098;
    if (((*(uint8_t *)(v_rip + 0xD30AE0)) & (1)) != 0) goto loc_002961AD;
loc_0029602C:
    *(uint32_t *)(v_rip + 0xB976DA) = 0;
loc_00296036:
    result = *(uint64_t *)(Arg2 - 0x30);
    if ((*(uint32_t *)(v_rip + 0xD30CE3)) != 0) {
        Arg1 = v_cr8;
        Arg2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, a3, a4);
    }
loc_00296053:
    local_rsp = (local_rsp) + (48);
    return 17;
loc_00296073:
    result = (17) - (1);
    if (condition_is_not_equal) goto loc_002961F5;
    goto loc_00295F84;
loc_0029608B:
    result = ExAcquireSpinLockExclusive(Arg1, Arg2, a3, a4);
    goto loc_00295F60;
loc_00296098:
    if (((*(uint8_t *)(v_rip + 0xD30A67)) & (1)) != 0) goto loc_002961D1;
loc_002960A5:
    *(uint32_t *)(v_rip + 0xB97661) = 0;
    goto loc_00296053;
loc_002960B1:
    if (*(uint64_t *)(Arg2) == 0) goto loc_00295F9C;
loc_002960BD:
    goto loc_00295F78;
loc_002960C5:
    result = (*(uint64_t *)(Arg2)) - (1);
    if (condition_is_not_equal) goto loc_002960EC;
    goto loc_00295F47;
loc_002960D4:
    result = RtlAvlRemoveNode(v_rip + 12154410, v_stack_p8, a3, a4);
    goto loc_00296019;
loc_002960EC:
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00296208;
    goto loc_00295F47;
loc_00296108:
    result = (uint32_t)((*(uint8_t *)(v_rip + 0xB9762A + 0x18 + 0x10)) & (3));
    if (((uint32_t)(result)) == ((uint32_t)((uint8_t)(v_stack_p10)))) goto loc_00296170;
    result = RtlpTreeDoubleRotateNodes(v_rip + 12154338, v_stack_p8, v_rip + 12154410 + 24, (uint8_t)(v_rip + 12154410));
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(v_rip + 0xB9762A + 0x18 + 0x10))) & (252));
    *(uint8_t *)(v_rip + 0xB9762A + 0x18 + 0x10) = (uint8_t)(Arg1);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(result + 0x10)))) & (3));
    if (((uint32_t)((uint8_t)(v_stack_p10))) == ((uint32_t)(Arg1))) goto loc_00296198;
    Arg2 = (uint32_t)((*(uint8_t *)(result + 0x10)) ^ (0xFFFFFFFEULL));
    Arg2 = (uint32_t)((Arg2) & (3));
    if (((uint32_t)((uint8_t)(v_stack_p10))) == Arg2) {
        result = (uint8_t)(*(uint8_t *)(v_rip + 0xB9762A + 0x18 + 0x10));
        result = (uint8_t)((result) ^ ((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9762A - 0x38) + *(uint64_t *)(v_rip + 0xB97797) + 0x10 * 1 + 0x8))));
        result = (uint8_t)((result) & (3));
        result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(v_rip + 0xB9762A + 0x18 + 0x10))));
        *(uint8_t *)(v_rip + 0xB9762A + 0x18 + 0x10) = (uint8_t)(result);
    }
    goto loc_00296014;
loc_00296170:
    a4 = (uint32_t)((*(uint8_t *)(v_rip + 0xB9762A + 0x18 + 0x10)) ^ (1));
    result = (*(uint64_t *)(v_rip + 0xB9762A + 0x18 + 0x10)) & (-4);
    if (result == Arg2) goto loc_0029621B;
loc_00296185:
loc_0029618C:
    *(uint64_t *)(v_rip + 0xB97575) = v_stack_p8;
    goto loc_00296014;
loc_00296198:
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x10))) ^ ((uint8_t)(v_stack_p10)));
    Arg1 = (uint8_t)((Arg1) ^ (254));
    Arg1 = (uint8_t)((Arg1) & (3));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x10))));
    *(uint8_t *)(*(uint64_t *)(v_rip + 0xB97797) + 0x10) = (uint8_t)(Arg1);
    goto loc_00296166;
loc_002961AD:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC77CA5))) != 0) goto loc_0029602C;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rip + 12154185, v_stack_p48, result, a4);
    goto loc_00296036;
loc_002961D1:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC77C81))) != 0) goto loc_002960A5;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rip + 12154149, v_stack_p48, result, a4);
    goto loc_00296053;
loc_002961F5:
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_002962E2;
    goto loc_00295F84;
loc_00296208:
    result = (*(uint64_t *)(v_stack_p48 + 0x30)) - (1);
    if (condition_is_not_equal) goto loc_002962D1;
    goto loc_00295F47;
loc_0029621B:
    result = ((uint32_t)((uint32_t)(a4))) ^ (1);
    if ((*(uint64_t *)(v_stack_p48 + result * 8)) != (v_rip + 12154410 + 24)) goto loc_00296185;
    Arg1 = (*(uint64_t *)(v_stack_p48 + 0x10)) & (-4);
    if (condition_is_equal) goto loc_002962B8;
    if ((*(uint64_t *)(arg1 + 0x8)) != v_stack_p48) goto loc_002962AA;
    *(uint64_t *)(arg1 + 0x8) = v_rip + 12154410 + 24;
loc_00296243:
    Arg1 = (*(uint64_t *)(v_rip + 0xB9762A + 0x18 + 0x10)) ^ (*(uint64_t *)(v_stack_p48 + 0x10));
    Arg1 = (Arg1) & (-4);
    Arg1 = (Arg1) ^ (*(uint64_t *)(v_rip + 0xB9762A + 0x18 + 0x10));
    *(void **)(v_rip + 0xB9762A + 0x18 + 0x10) = Arg1;
    if (*(uint64_t *)(v_rip + 0xB9762A + 0x18 + a4 * 8) != 0) goto loc_0029628A;
loc_00296261:
    result = ((uint32_t)((uint32_t)(a4))) ^ (1);
    *(uint64_t *)(v_stack_p48 + result * 8) = *(uint64_t *)(v_rip + 0xB9762A + 0x18 + a4 * 8);
    *(uint64_t *)(v_rip + 0xB9762A + 0x18 + a4 * 8) = v_stack_p48;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p48 + 0x10))) & (3));
    result = (result) | (v_rip + 12154410 + 24);
    *(uint64_t *)(v_stack_p48 + 0x10) = result;
    goto loc_00296014;
loc_0029628A:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9762A + 0x18 + a4 * 8) + 0x10)) & (-4);
    if (result != (v_rip + 12154410 + 24)) goto loc_00296185;
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9762A + 0x18 + a4 * 8) + 0x10)) & (3));
    Arg1 = (Arg1) | (v_stack_p48);
    *(void **)(*(uint64_t *)(v_rip + 0xB9762A + 0x18 + a4 * 8) + 0x10) = Arg1;
    goto loc_00296261;
loc_002962AA:
    if ((*(uint64_t *)(arg1)) != v_stack_p48) goto loc_00296185;
    *(uint64_t *)(arg1) = v_rip + 12154410 + 24;
    goto loc_00296243;
loc_002962B8:
    if ((*(uint64_t *)(v_rip + 0xB97449)) != v_stack_p48) goto loc_00296185;
    *(uint64_t *)(v_rip + 0xB9743C) = v_rip + 12154410 + 24;
    goto loc_00296243;
loc_002962D1:
    local_rsi = 0;
    goto loc_00295F47;
loc_002962E2:
    if (result != 1) goto loc_00295F8D;
    goto loc_00295F84;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x70` | `64` | `R` |
| `Arg1` | `- 0x38` | `64` | `R` |
| `Arg1` | `- 0x30` | `64` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x8` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R/W` |
| `Arg1` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00295F0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
