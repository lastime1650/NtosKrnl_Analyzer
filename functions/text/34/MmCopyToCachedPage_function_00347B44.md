# MmCopyToCachedPage

- RVA: `0x00347B44`–`0x003481F1` (길이 `1,709` bytes)
- VA: `0x0000000140347B44`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00078144`
- 디코드: `392`개 명령, `1,709/1,709` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00347B92` → [MiSystemCacheVaControlArea](MiSystemCacheVaControlArea_function_00348200.md) (function, `0x00348200`)
- `0x00347C57` → [MiGetContainingPageTable](MiGetContainingPageTable_function_003467F0.md) (function, `0x003467F0`)
- `0x00347D01` → [MiMakePageAvoidRead](../2B/MiMakePageAvoidRead_function_002B7DE0.md) (function, `0x002B7DE0`)
- `0x00347D71` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00347D78` → [RtlCopyMemoryNonTemporal](../6B/RtlCopyMemoryNonTemporal_function_006BA720.md) (function, `0x006BA720`)
- `0x00347DC7` → [MiMapSystemCachePage](../4D/MiMapSystemCachePage_function_004D3588.md) (function, `0x004D3588`)
- `0x00347E04` → [MiLockProtoPoolPageForce](../32/MiLockProtoPoolPageForce_function_00320E10.md) (function, `0x00320E10`)
- `0x00347E14` → [MiLockLeafPage](../36/MiLockLeafPage_function_003658C0.md) (function, `0x003658C0`)
- `0x00347E8F` → [MiUnlinkStandbyPfn](../2C/MiUnlinkStandbyPfn_function_002C3510.md) (function, `0x002C3510`)
- `0x00347EC6` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00347F37` → [MiMakeSystemCachePteValid](../2A/MiMakeSystemCachePteValid_function_002A35D8.md) (function, `0x002A35D8`)
- `0x00347F44` → [MiDirtyPte](../23/MiDirtyPte_function_00237C5C.md) (function, `0x00237C5C`)
- `0x00347F9E` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x00347FD2` → [MiMakeTransitionHeatBatch](../40/MiMakeTransitionHeatBatch_function_00409A94.md) (function, `0x00409A94`)
- `0x00347FFC` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00348001` → [MiReplenishTransitionPageHeatList](../4E/MiReplenishTransitionPageHeatList_function_004E131C.md) (function, `0x004E131C`)
- `0x00348022` → [MiMapSystemCachePage](../4D/MiMapSystemCachePage_function_004D3588.md) (function, `0x004D3588`)
- `0x0034804D` → [MiReleasePtes](../24/MiReleasePtes_function_00247240.md) (function, `0x00247240`)
- `0x0034807A` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x00348084` → [MiRemoveLockedPageChargeAndDecRef](../24/MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)
- `0x0034808E` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x003480B1` → [MiReservePtes](../31/MiReservePtes_function_00318D20.md) (function, `0x00318D20`)
- `0x003480F8` → [MiHandleSpecialPurposeMemoryCachedFault](../44/MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) (function, `0x0044C740`)
- `0x00348110` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00348141` → [MiAddLockedPageCharge](../28/MiAddLockedPageCharge_function_0028B550.md) (function, `0x0028B550`)
- `0x0034815D` → [MiIssuePageHeatList](../44/MiIssuePageHeatList_function_0044615C.md) (function, `0x0044615C`)
- `0x00348167` → [MiFreeTransitionPageHeatList](../4E/MiFreeTransitionPageHeatList_function_004E2B08.md) (function, `0x004E2B08`)
- `0x0034818B` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x003481A8` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x003481C1` → [MiMapFrame](../2C/MiMapFrame_function_002C7190.md) (function, `0x002C7190`)
- `0x003481EB` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [CcWrapperMmCopyToCachedPage](CcWrapperMmCopyToCachedPage_function_00347AB0.md) at `0x00347AEE`

### Static image references
- `0x00347BAB` → RVA `0x00E30088` (`.data`; read)
- `0x00347C68` → RVA `0x00E2DC80` (`.data`; read)
- `0x00348046` → RVA `0x00E37668` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003480C1` → [sub_006E20F8](../6E/Unknown_function_006E20F8.md) (`tail-transfer`)
  - `0x00348103` → [sub_006E20F8 + 0xA](../6E/Unknown_function_006E20F8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00347B44  48 8B C4                        mov rax, rsp
00347B47  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00347B4B  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00347B4F  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00347B53  48 89 48 08                     mov qword ptr [rax + 8], rcx
00347B57  53                              push rbx
00347B58  56                              push rsi
00347B59  57                              push rdi
00347B5A  41 54                           push r12
00347B5C  41 55                           push r13
00347B5E  41 56                           push r14
00347B60  41 57                           push r15
00347B62  48 81 EC 80 00 00 00            sub rsp, 0x80
00347B69  4D 8B E9                        mov r13, r9
00347B6C  45 8B C8                        mov r9d, r8d
00347B6F  48 8B DA                        mov rbx, rdx
00347B72  4C 8B C1                        mov r8, rcx
00347B75  48 83 60 90 00                  and qword ptr [rax - 0x70], 0
00347B7A  83 60 8C 00                     and dword ptr [rax - 0x74], 0
00347B7E  45 33 E4                        xor r12d, r12d
00347B81  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00347B86  33 C0                           xor eax, eax
00347B88  45 8D 7C 24 01                  lea r15d, [r12 + 1]
00347B8D  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00347B92  E8 69 06 00 00                  call 0x140348200
00347B97  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00347B9C  0F B7 40 3C                     movzx eax, word ptr [rax + 0x3c]
00347BA0  B9 FF 03 00 00                  mov ecx, 0x3ff
00347BA5  66 23 C1                        and ax, cx
00347BA8  0F B7 C8                        movzx ecx, ax
00347BAB  48 8B 05 D6 84 AE 00            mov rax, qword ptr [rip + 0xae84d6]
00347BB2  4C 8B 14 C8                     mov r10, qword ptr [rax + rcx*8]
00347BB6  49 81 C2 80 49 00 00            add r10, 0x4980
00347BBD  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
00347BC2  4B 8D 04 29                     lea rax, [r9 + r13]
00347BC6  48 3D 00 10 00 00               cmp rax, 0x1000
00347BCC  0F 87 07 06 00 00               ja 0x1403481d9
00347BD2  49 3B C5                        cmp rax, r13
00347BD5  0F 82 FE 05 00 00               jb 0x1403481d9
00347BDB  4D 8B F0                        mov r14, r8
00347BDE  49 C1 EE 09                     shr r14, 9
00347BE2  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00347BEC  4C 23 F0                        and r14, rax
00347BEF  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00347BF9  48 8B C0                        mov rax, rax
00347BFC  4C 03 F0                        add r14, rax
00347BFF  8B BC 24 E0 00 00 00            mov edi, dword ptr [rsp + 0xe0]
00347C06  8B C7                           mov eax, edi
00347C08  83 E0 04                        and eax, 4
00347C0B  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00347C0F  0F 85 D6 01 00 00               jne 0x140347deb
00347C15  40 F6 C7 08                     test dil, 8
00347C19  0F 85 88 04 00 00               jne 0x1403480a7
00347C1F  33 F6                           xor esi, esi
00347C21  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
00347C26  4D 8B 06                        mov r8, qword ptr [r14]
00347C29  45 84 C7                        test r15b, r8b
00347C2C  0F 85 83 01 00 00               jne 0x140347db5
00347C32  8A 03                           mov al, byte ptr [rbx]
00347C34  EB 1E                           jmp 0x140347c54
00347C36  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00347C3A  48 BF FF FF FF FF FF 00 00 00   movabs rdi, 0xffffffffff
00347C44  41 BF 01 00 00 00               mov r15d, 1
00347C4A  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00347C4F  E9 40 01 00 00                  jmp 0x140347d94
00347C54  49 8B CE                        mov rcx, r14
00347C57  E8 94 EB FF FF                  call 0x1403467f0
00347C5C  49 8B 1E                        mov rbx, qword ptr [r14]
00347C5F  41 84 DF                        test r15b, bl
00347C62  0F 85 C9 00 00 00               jne 0x140347d31
00347C68  48 8B 05 11 60 AE 00            mov rax, qword ptr [rip + 0xae6011]
00347C6F  48 85 C0                        test rax, rax
00347C72  74 0F                           je 0x140347c83
00347C74  F6 C3 10                        test bl, 0x10
00347C77  0F 85 65 01 00 00               jne 0x140347de2
00347C7D  48 F7 D0                        not rax
00347C80  48 23 D8                        and rbx, rax
00347C83  48 C1 FB 10                     sar rbx, 0x10
00347C87  4C 8B A4 24 C0 00 00 00         mov r12, qword ptr [rsp + 0xc0]
00347C8F  45 33 ED                        xor r13d, r13d
00347C92  C6 44 24 40 11                  mov byte ptr [rsp + 0x40], 0x11
00347C97  48 8B 03                        mov rax, qword ptr [rbx]
00347C9A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00347C9F  41 84 C7                        test r15b, al
00347CA2  0F 85 54 01 00 00               jne 0x140347dfc
00347CA8  48 0F BA E0 0A                  bt rax, 0xa
00347CAD  0F 83 49 01 00 00               jae 0x140347dfc
00347CB3  4D 85 ED                        test r13, r13
00347CB6  0F 85 E5 04 00 00               jne 0x1403481a1
00347CBC  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00347CC1  F6 40 3E 0C                     test byte ptr [rax + 0x3e], 0xc
00347CC5  0F 85 C8 02 00 00               jne 0x140347f93
00347CCB  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00347CD0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00347CD5  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00347CDA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00347CDF  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00347CE3  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
00347CEB  4D 8B CD                        mov r9, r13
00347CEE  44 8B 84 24 D0 00 00 00         mov r8d, dword ptr [rsp + 0xd0]
00347CF6  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
00347CFE  48 8B CB                        mov rcx, rbx
00347D01  E8 DA 00 F7 FF                  call 0x1402b7de0
00347D06  85 C0                           test eax, eax
00347D08  0F 84 8F 00 00 00               je 0x140347d9d
00347D0E  83 E8 01                        sub eax, 1
00347D11  0F 84 78 FF FF FF               je 0x140347c8f
00347D17  48 BF FF FF FF FF FF 00 00 00   movabs rdi, 0xffffffffff
00347D21  83 F8 01                        cmp eax, 1
00347D24  0F 85 E8 01 00 00               jne 0x140347f12
00347D2A  33 C0                           xor eax, eax
00347D2C  E9 E4 01 00 00                  jmp 0x140347f15
00347D31  48 85 F6                        test rsi, rsi
00347D34  0F 85 DF 02 00 00               jne 0x140348019
00347D3A  48 BF FF FF FF FF FF 00 00 00   movabs rdi, 0xffffffffff
00347D44  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
00347D49  4D 85 E4                        test r12, r12
00347D4C  4C 0F 44 A4 24 C0 00 00 00      cmove r12, qword ptr [rsp + 0xc0]
00347D55  8B 8C 24 D0 00 00 00            mov ecx, dword ptr [rsp + 0xd0]
00347D5C  49 03 CC                        add rcx, r12
00347D5F  4D 8B C5                        mov r8, r13
00347D62  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
00347D6A  83 7C 24 60 00                  cmp dword ptr [rsp + 0x60], 0
00347D6F  75 07                           jne 0x140347d78
00347D71  E8 CA EA 37 00                  call 0x1406c6840
00347D76  EB 05                           jmp 0x140347d7d
00347D78  E8 A3 29 37 00                  call 0x1406ba720
00347D7D  EB 15                           jmp 0x140347d94
00347D7F  48 BF FF FF FF FF FF 00 00 00   movabs rdi, 0xffffffffff
00347D89  41 BF 01 00 00 00               mov r15d, 1
00347D8F  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00347D94  48 85 F6                        test rsi, rsi
00347D97  0F 85 A0 02 00 00               jne 0x14034803d
00347D9D  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
00347DA1  48 81 C4 80 00 00 00            add rsp, 0x80
00347DA8  41 5F                           pop r15
00347DAA  41 5E                           pop r14
00347DAC  41 5D                           pop r13
00347DAE  41 5C                           pop r12
00347DB0  5F                              pop rdi
00347DB1  5E                              pop rsi
00347DB2  5B                              pop rbx
00347DB3  C3                              ret
00347DB4  CC                              int3
00347DB5  49 8B D6                        mov rdx, r14
00347DB8  48 85 F6                        test rsi, rsi
00347DBB  0F 84 80 01 00 00               je 0x140347f41
00347DC1  44 8B C7                        mov r8d, edi
00347DC4  48 8B CE                        mov rcx, rsi
00347DC7  E8 BC B7 18 00                  call 0x1404d3588
00347DCC  4C 8B E0                        mov r12, rax
00347DCF  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00347DD4  48 85 C0                        test rax, rax
00347DD7  0F 84 55 FE FF FF               je 0x140347c32
00347DDD  E9 58 FF FF FF                  jmp 0x140347d3a
00347DE2  48 83 E3 EF                     and rbx, 0xffffffffffffffef
00347DE6  E9 98 FE FF FF                  jmp 0x140347c83
00347DEB  41 F6 C1 3F                     test r9b, 0x3f
00347DEF  0F 84 A3 02 00 00               je 0x140348098
00347DF5  B8 74 04 00 C0                  mov eax, 0xc0000474
00347DFA  EB A5                           jmp 0x140347da1
00347DFC  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00347E01  48 8B CB                        mov rcx, rbx
00347E04  E8 07 90 FD FF                  call 0x140320e10
00347E09  4C 8B E8                        mov r13, rax
00347E0C  BA 02 00 00 00                  mov edx, 2
00347E11  48 8B CB                        mov rcx, rbx
00347E14  E8 A7 DA 01 00                  call 0x1403658c0
00347E19  48 8B F8                        mov rdi, rax
00347E1C  48 8B 03                        mov rax, qword ptr [rbx]
00347E1F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00347E24  48 85 FF                        test rdi, rdi
00347E27  0F 84 21 01 00 00               je 0x140347f4e
00347E2D  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
00347E32  41 84 C7                        test r15b, al
00347E35  0F 85 1F 01 00 00               jne 0x140347f5a
00347E3B  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00347E3F  48 C1 E8 2B                     shr rax, 0x2b
00347E43  25 FF 03 00 00                  and eax, 0x3ff
00347E48  48 8B 0D 39 82 AE 00            mov rcx, qword ptr [rip + 0xae8239]
00347E4F  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00347E53  8B 40 04                        mov eax, dword ptr [rax + 4]
00347E56  84 C0                           test al, al
00347E58  0F 88 73 02 00 00               js 0x1403480d1
00347E5E  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00347E62  48 8B D0                        mov rdx, rax
00347E65  81 E2 00 04 00 00               and edx, 0x400
00347E6B  48 8B C8                        mov rcx, rax
00347E6E  48 C1 E9 0B                     shr rcx, 0xb
00347E72  48 C1 E8 03                     shr rax, 3
00347E76  48 85 D2                        test rdx, rdx
00347E79  0F 45 C1                        cmovne eax, ecx
00347E7C  41 84 C7                        test r15b, al
00347E7F  0F 85 45 01 00 00               jne 0x140347fca
00347E85  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
00347E8C  48 8B CB                        mov rcx, rbx
00347E8F  E8 7C B6 F7 FF                  call 0x1402c3510
00347E94  44 8B E0                        mov r12d, eax
00347E97  85 C0                           test eax, eax
00347E99  0F 85 7B 02 00 00               jne 0x14034811a
00347E9F  48 8B 0B                        mov rcx, qword ptr [rbx]
00347EA2  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00347EA7  48 85 F6                        test rsi, rsi
00347EAA  0F 85 83 02 00 00               jne 0x140348133
00347EB0  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00347EBA  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
00347EBF  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
00347EC3  49 8B CD                        mov rcx, r13
00347EC6  E8 C5 E1 EF FF                  call 0x140246090
00347ECB  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00347ED0  48 85 C9                        test rcx, rcx
00347ED3  0F 85 84 02 00 00               jne 0x14034815d
00347ED9  83 7C 24 44 00                  cmp dword ptr [rsp + 0x44], 0
00347EDE  0F 8C CB 00 00 00               jl 0x140347faf
00347EE4  45 3B E7                        cmp r12d, r15d
00347EE7  0F 84 D1 00 00 00               je 0x140347fbe
00347EED  41 83 FC 02                     cmp r12d, 2
00347EF1  0F 84 81 02 00 00               je 0x140348178
00347EF7  48 BF FF FF FF FF FF 00 00 00   movabs rdi, 0xffffffffff
00347F01  48 85 F6                        test rsi, rsi
00347F04  0F 85 A8 02 00 00               jne 0x1403481b2
00347F0A  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
00347F12  41 8B C7                        mov eax, r15d
00347F15  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
00347F1A  85 C0                           test eax, eax
00347F1C  0F 84 22 FE FF FF               je 0x140347d44
00347F22  44 8B 8C 24 E0 00 00 00         mov r9d, dword ptr [rsp + 0xe0]
00347F2A  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00347F2F  49 8B D6                        mov rdx, r14
00347F32  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00347F37  E8 9C B6 F5 FF                  call 0x1402a35d8
00347F3C  E9 03 FE FF FF                  jmp 0x140347d44
00347F41  49 8B CA                        mov rcx, r10
00347F44  E8 13 FD EE FF                  call 0x140237c5c
00347F49  E9 EC FD FF FF                  jmp 0x140347d3a
00347F4E  8B BC 24 E0 00 00 00            mov edi, dword ptr [rsp + 0xe0]
00347F55  E9 59 FD FF FF                  jmp 0x140347cb3
00347F5A  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
00347F5E  48 8B D1                        mov rdx, rcx
00347F61  48 B8 FF FF FF FF FF FF FF 3F   movabs rax, 0x3fffffffffffffff
00347F6B  48 23 D0                        and rdx, rax
00347F6E  48 FF C2                        inc rdx
00347F71  48 8B C2                        mov rax, rdx
00347F74  48 33 C1                        xor rax, rcx
00347F77  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
00347F81  48 23 C1                        and rax, rcx
00347F84  48 33 C2                        xor rax, rdx
00347F87  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00347F8B  45 33 E4                        xor r12d, r12d
00347F8E  E9 14 FF FF FF                  jmp 0x140347ea7
00347F93  45 33 C9                        xor r9d, r9d
00347F96  45 33 C0                        xor r8d, r8d
00347F99  49 8B D4                        mov rdx, r12
00347F9C  33 C9                           xor ecx, ecx
00347F9E  E8 DD 6E F3 FF                  call 0x14027ee80
00347FA3  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00347FA7  85 C0                           test eax, eax
00347FA9  0F 89 E0 FC FF FF               jns 0x140347c8f
00347FAF  48 BF FF FF FF FF FF 00 00 00   movabs rdi, 0xffffffffff
00347FB9  E9 D6 FD FF FF                  jmp 0x140347d94
00347FBE  8B BC 24 E0 00 00 00            mov edi, dword ptr [rsp + 0xe0]
00347FC5  E9 BD FC FF FF                  jmp 0x140347c87
00347FCA  45 33 C0                        xor r8d, r8d
00347FCD  33 D2                           xor edx, edx
00347FCF  48 8B CF                        mov rcx, rdi
00347FD2  E8 BD 1A 0C 00                  call 0x140409a94
00347FD7  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00347FDC  48 83 F8 FF                     cmp rax, -1
00347FE0  0F 85 9F FE FF FF               jne 0x140347e85
00347FE6  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00347FF0  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
00347FF5  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
00347FF9  49 8B CD                        mov rcx, r13
00347FFC  E8 8F E0 EF FF                  call 0x140246090
00348001  E8 16 93 19 00                  call 0x1404e131c
00348006  33 C9                           xor ecx, ecx
00348008  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0034800D  8B BC 24 E0 00 00 00            mov edi, dword ptr [rsp + 0xe0]
00348014  E9 76 FC FF FF                  jmp 0x140347c8f
00348019  44 8B C7                        mov r8d, edi
0034801C  49 8B D6                        mov rdx, r14
0034801F  48 8B CE                        mov rcx, rsi
00348022  E8 61 B5 18 00                  call 0x1404d3588
00348027  4C 8B E0                        mov r12, rax
0034802A  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0034802F  48 85 C0                        test rax, rax
00348032  0F 85 02 FD FF FF               jne 0x140347d3a
00348038  E9 2B FC FF FF                  jmp 0x140347c68
0034803D  48 8B 1E                        mov rbx, qword ptr [rsi]
00348040  45 8B C7                        mov r8d, r15d
00348043  48 8B D6                        mov rdx, rsi
00348046  48 8D 0D 1B F6 AE 00            lea rcx, [rip + 0xaef61b]
0034804D  E8 EE F1 EF FF                  call 0x140247240
00348052  41 84 DF                        test r15b, bl
00348055  0F 84 42 FD FF FF               je 0x140347d9d
0034805B  48 C1 EB 0C                     shr rbx, 0xc
0034805F  48 23 DF                        and rbx, rdi
00348062  48 8D 3C 5B                     lea rdi, [rbx + rbx*2]
00348066  48 C1 E7 04                     shl rdi, 4
0034806A  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00348074  48 03 F8                        add rdi, rax
00348077  48 8B CF                        mov rcx, rdi
0034807A  E8 C1 22 FD FF                  call 0x14031a340
0034807F  8A D8                           mov bl, al
00348081  48 8B CF                        mov rcx, rdi
00348084  E8 47 D9 EF FF                  call 0x1402459d0
00348089  8A D3                           mov dl, bl
0034808B  48 8B CF                        mov rcx, rdi
0034808E  E8 4D 23 FD FF                  call 0x14031a3e0
00348093  E9 05 FD FF FF                  jmp 0x140347d9d
00348098  41 F6 C5 3F                     test r13b, 0x3f
0034809C  0F 84 73 FB FF FF               je 0x140347c15
003480A2  E9 4E FD FF FF                  jmp 0x140347df5
003480A7  41 8B D7                        mov edx, r15d
003480AA  48 8D 0D B7 F5 AE 00            lea rcx, [rip + 0xaef5b7]
003480B1  E8 6A 0C FD FF                  call 0x140318d20
003480B6  48 8B F0                        mov rsi, rax
003480B9  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
003480BE  48 85 C0                        test rax, rax
003480C1  0F 85 31 A0 39 00               jne 0x1406e20f8
003480C7  B8 9A 00 00 C0                  mov eax, 0xc000009a
003480CC  E9 D0 FC FF FF                  jmp 0x140347da1
003480D1  49 8B D6                        mov rdx, r14
003480D4  48 C1 E2 19                     shl rdx, 0x19
003480D8  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003480E2  48 8B C0                        mov rax, rax
003480E5  48 C1 E0 19                     shl rax, 0x19
003480E9  48 2B D0                        sub rdx, rax
003480EC  48 C1 FA 10                     sar rdx, 0x10
003480F0  4C 8B CF                        mov r9, rdi
003480F3  4C 8B C3                        mov r8, rbx
003480F6  33 C9                           xor ecx, ecx
003480F8  E8 43 46 10 00                  call 0x14044c740
003480FD  48 8B F8                        mov rdi, rax
00348100  48 85 C0                        test rax, rax
00348103  0F 85 F9 9F 39 00               jne 0x1406e2102
00348109  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
0034810D  49 8B CD                        mov rcx, r13
00348110  E8 7B DF EF FF                  call 0x140246090
00348115  E9 F3 FE FF FF                  jmp 0x14034800d
0034811A  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
0034811E  B9 09 07 00 C0                  mov ecx, 0xc0000709
00348123  41 83 FC 03                     cmp r12d, 3
00348127  0F 44 C1                        cmove eax, ecx
0034812A  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0034812E  E9 74 FD FF FF                  jmp 0x140347ea7
00348133  45 85 E4                        test r12d, r12d
00348136  0F 85 74 FD FF FF               jne 0x140347eb0
0034813C  33 D2                           xor edx, edx
0034813E  48 8B CF                        mov rcx, rdi
00348141  E8 0A 34 F4 FF                  call 0x14028b550
00348146  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
0034814A  85 C0                           test eax, eax
0034814C  B8 9A 00 00 C0                  mov eax, 0xc000009a
00348151  0F 44 C8                        cmove ecx, eax
00348154  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
00348158  E9 53 FD FF FF                  jmp 0x140347eb0
0034815D  E8 FA DF 0F 00                  call 0x14044615c
00348162  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00348167  E8 9C A9 19 00                  call 0x1404e2b08
0034816C  33 C0                           xor eax, eax
0034816E  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00348173  E9 61 FD FF FF                  jmp 0x140347ed9
00348178  45 33 C9                        xor r9d, r9d
0034817B  45 33 C0                        xor r8d, r8d
0034817E  4C 8B A4 24 C0 00 00 00         mov r12, qword ptr [rsp + 0xc0]
00348186  49 8B D4                        mov rdx, r12
00348189  33 C9                           xor ecx, ecx
0034818B  E8 F0 6C F3 FF                  call 0x14027ee80
00348190  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00348194  85 C0                           test eax, eax
00348196  0F 88 13 FE FF FF               js 0x140347faf
0034819C  E9 6C FE FF FF                  jmp 0x14034800d
003481A1  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
003481A5  49 8B CD                        mov rcx, r13
003481A8  E8 E3 DE EF FF                  call 0x140246090
003481AD  E9 0A FB FF FF                  jmp 0x140347cbc
003481B2  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
003481B7  48 C1 EA 0C                     shr rdx, 0xc
003481BB  48 23 D7                        and rdx, rdi
003481BE  48 8B CE                        mov rcx, rsi
003481C1  E8 CA EF F7 FF                  call 0x1402c7190
003481C6  4C 8B E0                        mov r12, rax
003481C9  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
003481D1  41 8B C7                        mov eax, r15d
003481D4  E9 41 FD FF FF                  jmp 0x140347f1a
003481D9  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
003481DE  4D 8B CD                        mov r9, r13
003481E1  BA 86 07 00 00                  mov edx, 0x786
003481E6  B9 1A 00 00 00                  mov ecx, 0x1a
003481EB  E8 70 54 1B 00                  call 0x1404fd660
003481F0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmCopyToCachedPage(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pD8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (128);
    v_r12 = 0;
    v_stack_m60 = 0;
    result = 0;
    v_stack_m68 = 0;
    result = MiSystemCacheVaControlArea(a1, a2, a1, (unsigned int)(a3));
    v_stack_m40 = result;
    result = (unsigned __int16)((*(unsigned __int16 *)(result + 60)) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    v_r10 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11437270) + (unsigned __int16)(result) * 8)) + (0x4980ULL);
    v_stack_m48 = v_r10;
    if (((unsigned int)(a3) + a4 * 1) > 0x1000ULL) goto loc_003481D9;
    if (((unsigned int)(a3) + a4 * 1) < a4) goto loc_003481D9;
    v_r14 = (a1) >> (9);
    v_r14 = (v_r14) & ((unsigned int)(a3) + a4 * 1);
    v_r14 = (v_r14) + ((unsigned int)(a3) + a4 * 1);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (4));
    v_stack_m58 = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_00347DEB;
loc_00347C15:
    if ((((unsigned __int8)((unsigned int)(a5))) & (8)) != 0) goto loc_003480A7;
    v_rsi = 0;
    v_stack_m50 = 0;
    if ((((unsigned __int8)(v_r12 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(v_r14)))) != 0) goto loc_00347DB5;
loc_00347C32:
    goto loc_00347C54;
loc_00347C54:
    result = MiGetContainingPageTable(v_r14, a2, *(unsigned __int64 *)(v_r14), (unsigned int)(a3));
    if ((((unsigned __int8)(v_r12 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(v_r14)))) != 0) goto loc_00347D31;
loc_00347C68:
    if (*(unsigned __int64 *)(v_rip + 11427857) == 0) goto loc_00347C83;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (16)) != 0) goto loc_00347DE2;
    result = ~(*(unsigned __int64 *)(v_rip + 11427857));
    v_rbx = (*(unsigned __int64 *)(v_r14)) & (result);
loc_00347C83:
    v_rbx = (v_rbx) >> (16);
loc_00347C87:
loc_00347C8F:
    v_r13 = 0;
    v_stack_m78 = 17;
    v_stack_m70 = *(unsigned __int64 *)(v_rbx);
    if ((((unsigned __int8)(v_r12 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rbx)))) != 0) goto loc_00347DFC;
    if (condition_is_above_or_equal) goto loc_00347DFC;
loc_00347CB3:
    if (0 != 0) goto loc_003481A1;
loc_00347CBC:
    if (((*(unsigned __int8 *)(v_stack_m40 + 62)) & (12)) != 0) goto loc_00347F93;
    v_stack_m88 = v_stack_m74;
    v_stack_m90 = v_stack_m70;
    v_stack_m98 = (unsigned int)((unsigned int)(a5));
    result = MiMakePageAvoidRead(v_rbx, v_stack_p10, (unsigned int)(v_stack_p18), v_stack_p20);
    if ((unsigned int)(result) == 0) goto loc_00347D9D;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00347C8F;
    if (((unsigned int)(result)) != 1) goto loc_00347F12;
    result = 0;
    goto loc_00347F15;
loc_00347D31:
    if (0 != 0) goto loc_00348019;
loc_00347D3A:
loc_00347D44:
    v_r12 = v_stack_p8;
    if (v_stack_p8 == 0) { v_r12 = v_stack_p8; }
    a1 = ((unsigned int)(v_stack_p18)) + (v_r12);
    if (v_stack_m58 != 0) goto loc_00347D78;
    result = memcpy(a1, v_stack_p10, v_stack_p20, v_stack_p20);
    goto loc_00347D7D;
loc_00347D78:
    result = RtlCopyMemoryNonTemporal(a1, v_stack_p10, v_stack_p20, v_stack_p20);
loc_00347D7D:
    goto loc_00347D94;
loc_00347D94:
    if (0 != 0) goto loc_0034803D;
loc_00347D9D:
loc_00347DA1:
    v_rsp = (v_rsp) + (128);
    return (unsigned int)(v_stack_m74);
loc_00347DB5:
    if (0 == 0) goto loc_00347F41;
    result = MiMapSystemCachePage(0, v_r14, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_p20);
    v_stack_p58 = result;
    if (result == 0) goto loc_00347C32;
    goto loc_00347D3A;
loc_00347DE2:
    v_rbx = (v_rbx) & (-17);
    goto loc_00347C83;
loc_00347DEB:
    if ((((unsigned __int8)(v_stack_p20)) & (63)) == 0) goto loc_00348098;
loc_00347DF5:
    goto loc_00347DA1;
loc_00347DFC:
    result = MiLockProtoPoolPageForce(v_rbx, v_stack_p40, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_p20);
    result = MiLockLeafPage(v_rbx, 2, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_p20);
    v_stack_p48 = *(unsigned __int64 *)(v_rbx);
    if (result == 0) goto loc_00347F4E;
    if ((((unsigned __int8)(v_r12 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rbx)))) != 0) goto loc_00347F5A;
    result = (*(unsigned __int64 *)(result + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_003480D1;
    a2 = (unsigned int)((*(unsigned __int64 *)(result + 16)) & (0x400ULL));
    a1 = (*(unsigned __int64 *)(result + 16)) >> (11);
    result = (*(unsigned __int64 *)(result + 16)) >> (3);
    if (a2 != 0) { result = (unsigned int)(a1); }
    if ((((unsigned __int8)(v_r12 + 1)) & ((unsigned __int8)(result))) != 0) goto loc_00347FCA;
loc_00347E85:
    result = MiUnlinkStandbyPfn(v_rbx, (unsigned int)(a5), (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_p20);
    if ((unsigned int)(result) != 0) goto loc_0034811A;
    v_stack_p48 = *(unsigned __int64 *)(v_rbx);
loc_00347EA7:
    if (0 != 0) goto loc_00348133;
loc_00347EB0:
    result = MiUnlockProtoPoolPage(result, v_stack_p40, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_p20);
    if (v_stack_p50 != 0) goto loc_0034815D;
loc_00347ED9:
    if (v_stack_p44 < 0) goto loc_00347FAF;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(v_r12 + 1))) goto loc_00347FBE;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 2) goto loc_00348178;
    if (0 != 0) goto loc_003481B2;
loc_00347F12:
loc_00347F15:
loc_00347F1A:
    if ((unsigned int)((unsigned int)((unsigned int)(v_r12 + 1))) == 0) goto loc_00347D44;
    result = MiMakeSystemCachePteValid(v_stack_p70, v_r14, v_stack_p48, (unsigned int)(a5));
    goto loc_00347D44;
loc_00347F41:
    result = MiDirtyPte(v_r10, v_r14, v_stack_p48, (unsigned int)(a5));
    goto loc_00347D3A;
loc_00347F4E:
    goto loc_00347CB3;
loc_00347F5A:
    a2 = (*(unsigned __int64 *)((unsigned int)(a5) + 24)) & (result);
    a2 = (a2) + 1;
    result = (a2) ^ (*(unsigned __int64 *)((unsigned int)(a5) + 24));
    result = (result) & (*(unsigned __int64 *)((unsigned int)(a5) + 24));
    result = (result) ^ (a2);
    *(unsigned __int64 *)((unsigned int)(a5) + 24) = result;
    v_r12 = 0;
    goto loc_00347EA7;
loc_00347F93:
    a4 = 0;
    a3 = 0;
    a1 = 0;
    result = MmAccessFault(a1, 0, a3, a4);
    v_stack_p44 = (unsigned int)(result);
    if (!sign_flag) goto loc_00347C8F;
loc_00347FAF:
    goto loc_00347D94;
loc_00347FBE:
    goto loc_00347C87;
loc_00347FCA:
    a3 = 0;
    a2 = 0;
    result = MiMakeTransitionHeatBatch((unsigned int)(a5), a2, a3, a4);
    v_stack_p50 = result;
    if (result != -1) goto loc_00347E85;
    result = MiUnlockProtoPoolPage(v_stack_pD8, v_stack_p40, a3, a4);
    result = MiReplenishTransitionPageHeatList(v_stack_pD8, v_stack_p40, a3, a4);
    a1 = 0;
    v_stack_p50 = 0;
loc_0034800D:
    goto loc_00347C8F;
loc_00348019:
    result = MiMapSystemCachePage(0, v_r14, (unsigned int)((unsigned int)((unsigned int)(a5))), a4);
    v_stack_p58 = result;
    if (result != 0) goto loc_00347D3A;
    goto loc_00347C68;
loc_0034803D:
    result = MiReleasePtes(v_rip + 11466267, 0, (unsigned int)((unsigned int)(v_r12 + 1)), a4);
    if ((((unsigned __int8)(v_r12 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rsi)))) == 0) goto loc_00347D9D;
    v_rbx = (*(unsigned __int64 *)(v_rsi)) >> (12);
    v_rbx = (v_rbx) & ((unsigned int)(a5));
    v_rdi = (v_rbx + v_rbx * 2) << (4);
    v_rdi = (v_rdi) + (result);
    result = MiLockPageInline(v_rdi, 0, (unsigned int)((unsigned int)(v_r12 + 1)), a4);
    result = MiRemoveLockedPageChargeAndDecRef(v_rdi, 0, (unsigned int)((unsigned int)(v_r12 + 1)), a4);
    result = MiUnlockPage(v_rdi, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)((unsigned int)(v_r12 + 1)), a4);
    goto loc_00347D9D;
loc_00348098:
    if ((((unsigned __int8)(v_stack_pD8)) & (63)) == 0) goto loc_00347C15;
    goto loc_00347DF5;
loc_003480A7:
    result = MiReservePtes(v_rip + 11466167, (unsigned int)((unsigned int)(v_r12 + 1)), (unsigned int)((unsigned int)(v_r12 + 1)), a4);
    v_stack_p68 = result;
    goto loc_00347DA1;
loc_003480D1:
    a2 = (v_r14) << (25);
    result = ((unsigned int)(0xC000009AULL)) << (25);
    a2 = (a2) - (result);
    a2 = (a2) >> (16);
    a1 = 0;
    result = MiHandleSpecialPurposeMemoryCachedFault(a1, a2, (unsigned __int8)(result), v_rdi);
    result = MiUnlockProtoPoolPage(v_stack_pD8, v_stack_p40, (unsigned __int8)(result), v_rdi);
    goto loc_0034800D;
loc_0034811A:
    result = (unsigned int)(v_stack_p44);
    if (((unsigned int)(result)) == 3) { result = (unsigned int)((unsigned int)(0xC0000709ULL)); }
    v_stack_p44 = (unsigned int)(result);
    goto loc_00347EA7;
loc_00348133:
    if ((unsigned int)(result) != 0) goto loc_00347EB0;
    a2 = 0;
    result = MiAddLockedPageCharge(result, a2, (unsigned __int8)(result), v_rdi);
    a1 = (unsigned int)(v_stack_p44);
    if ((unsigned int)(result) == 0) { a1 = (unsigned int)((unsigned int)(0xC000009AULL)); }
    v_stack_p44 = (unsigned int)(a1);
    goto loc_00347EB0;
loc_0034815D:
    result = MiIssuePageHeatList(a1, a2, (unsigned __int8)(result), v_rdi);
    result = MiFreeTransitionPageHeatList(v_stack_p50, a2, (unsigned __int8)(result), v_rdi);
    result = 0;
    v_stack_p50 = 0;
    goto loc_00347ED9;
loc_00348178:
    a4 = 0;
    a3 = 0;
    a1 = 0;
    result = MmAccessFault(a1, v_stack_pC0, a3, a4);
    v_stack_p44 = (unsigned int)(result);
    if (sign_flag) goto loc_00347FAF;
    goto loc_0034800D;
loc_003481A1:
    result = MiUnlockProtoPoolPage(v_stack_pD8, v_stack_p40, a3, a4);
    goto loc_00347CBC;
loc_003481B2:
    a2 = (v_stack_p48) >> (12);
    a2 = (a2) & (result);
    result = MiMapFrame(result, a2, a3, a4);
    goto loc_00347F1A;
loc_003481D9:
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (unsigned int)(0x786ULL), a3, v_stack_pD8);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmCopyToCachedPage(int64_t Arg1, void *Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint8_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pD8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (128);
    local_r12 = 0;
    v_stack_m60 = 0;
    result = 0;
    v_stack_m68 = 0;
    result = MiSystemCacheVaControlArea(Arg1, Arg2, Arg1, (uint32_t)(Arg3));
    v_stack_m40 = result;
    result = (uint16_t)((*(uint16_t *)(result + 0x3C)) & ((uint16_t)((uint32_t)(0x3FFULL))));
    local_r10 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAE84D6) + (uint16_t)(result) * 8)) + (0x4980ULL);
    v_stack_m48 = local_r10;
    if (((uint32_t)(Arg3) + Arg4 * 1) > 0x1000ULL) goto loc_003481D9;
    if (((uint32_t)(Arg3) + Arg4 * 1) < Arg4) goto loc_003481D9;
    local_r14 = (Arg1) >> (9);
    local_r14 = (local_r14) & ((uint32_t)(Arg3) + Arg4 * 1);
    local_r14 = (local_r14) + ((uint32_t)(Arg3) + Arg4 * 1);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (4));
    v_stack_m58 = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_00347DEB;
loc_00347C15:
    if ((((uint8_t)((uint32_t)(Arg5))) & (8)) != 0) goto loc_003480A7;
    local_rsi = 0;
    v_stack_m50 = 0;
    if ((((uint8_t)(local_r12 + 1)) & ((uint8_t)(*(uint64_t *)(local_r14)))) != 0) goto loc_00347DB5;
loc_00347C32:
    goto loc_00347C54;
loc_00347C54:
    result = MiGetContainingPageTable(local_r14, Arg2, *(uint64_t *)(local_r14), (uint32_t)(Arg3));
    if ((((uint8_t)(local_r12 + 1)) & ((uint8_t)(*(uint64_t *)(local_r14)))) != 0) goto loc_00347D31;
loc_00347C68:
    if (*(uint64_t *)(v_rip + 0xAE6011) == 0) goto loc_00347C83;
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (16)) != 0) goto loc_00347DE2;
    result = ~(*(uint64_t *)(v_rip + 0xAE6011));
    local_rbx = (*(uint64_t *)(local_r14)) & (result);
loc_00347C83:
    local_rbx = (local_rbx) >> (16);
loc_00347C87:
loc_00347C8F:
    local_r13 = 0;
    v_stack_m78 = 17;
    v_stack_m70 = *(uint64_t *)(local_rbx);
    if ((((uint8_t)(local_r12 + 1)) & ((uint8_t)(*(uint64_t *)(local_rbx)))) != 0) goto loc_00347DFC;
    if (condition_is_above_or_equal) goto loc_00347DFC;
loc_00347CB3:
    if (0 != 0) goto loc_003481A1;
loc_00347CBC:
    if (((*(uint8_t *)(v_stack_m40 + 0x3E)) & (12)) != 0) goto loc_00347F93;
    v_stack_m88 = v_stack_m74;
    v_stack_m90 = v_stack_m70;
    v_stack_m98 = (uint32_t)((uint32_t)(Arg5));
    result = MiMakePageAvoidRead(local_rbx, v_stack_p10, (uint32_t)(v_stack_p18), v_stack_p20);
    if ((uint32_t)(result) == 0) goto loc_00347D9D;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00347C8F;
    if (((uint32_t)(result)) != 1) goto loc_00347F12;
    result = 0;
    goto loc_00347F15;
loc_00347D31:
    if (0 != 0) goto loc_00348019;
loc_00347D3A:
loc_00347D44:
    local_r12 = v_stack_p8;
    if (v_stack_p8 == 0) { local_r12 = v_stack_p8; }
    Arg1 = ((uint32_t)(v_stack_p18)) + (local_r12);
    if (v_stack_m58 != 0) goto loc_00347D78;
    result = memcpy(Arg1, v_stack_p10, v_stack_p20, v_stack_p20);
    goto loc_00347D7D;
loc_00347D78:
    result = RtlCopyMemoryNonTemporal(Arg1, v_stack_p10, v_stack_p20, v_stack_p20);
loc_00347D7D:
    goto loc_00347D94;
loc_00347D94:
    if (0 != 0) goto loc_0034803D;
loc_00347D9D:
loc_00347DA1:
    local_rsp = (local_rsp) + (128);
    return (uint32_t)(v_stack_m74);
loc_00347DB5:
    if (0 == 0) goto loc_00347F41;
    result = MiMapSystemCachePage(0, local_r14, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_p20);
    v_stack_p58 = result;
    if (result == 0) goto loc_00347C32;
    goto loc_00347D3A;
loc_00347DE2:
    local_rbx = (local_rbx) & (-17);
    goto loc_00347C83;
loc_00347DEB:
    if ((((uint8_t)(v_stack_p20)) & (63)) == 0) goto loc_00348098;
loc_00347DF5:
    goto loc_00347DA1;
loc_00347DFC:
    result = MiLockProtoPoolPageForce(local_rbx, v_stack_p40, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_p20);
    result = MiLockLeafPage(local_rbx, 2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_p20);
    v_stack_p48 = *(uint64_t *)(local_rbx);
    if (result == 0) goto loc_00347F4E;
    if ((((uint8_t)(local_r12 + 1)) & ((uint8_t)(*(uint64_t *)(local_rbx)))) != 0) goto loc_00347F5A;
    result = (*(uint64_t *)(result + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_003480D1;
    Arg2 = (uint32_t)((*(uint64_t *)(result + 0x10)) & (0x400ULL));
    Arg1 = (*(uint64_t *)(result + 0x10)) >> (11);
    result = (*(uint64_t *)(result + 0x10)) >> (3);
    if (Arg2 != NULL) { result = (uint32_t)(Arg1); }
    if ((((uint8_t)(local_r12 + 1)) & ((uint8_t)(result))) != 0) goto loc_00347FCA;
loc_00347E85:
    result = MiUnlinkStandbyPfn(local_rbx, (uint32_t)(Arg5), (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_p20);
    if ((uint32_t)(result) != 0) goto loc_0034811A;
    v_stack_p48 = *(uint64_t *)(local_rbx);
loc_00347EA7:
    if (0 != 0) goto loc_00348133;
loc_00347EB0:
    result = MiUnlockProtoPoolPage(result, v_stack_p40, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_p20);
    if (v_stack_p50 != 0) goto loc_0034815D;
loc_00347ED9:
    if (v_stack_p44 < 0) goto loc_00347FAF;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(local_r12 + 1))) goto loc_00347FBE;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 2) goto loc_00348178;
    if (0 != 0) goto loc_003481B2;
loc_00347F12:
loc_00347F15:
loc_00347F1A:
    if ((uint32_t)((uint32_t)((uint32_t)(local_r12 + 1))) == 0) goto loc_00347D44;
    result = MiMakeSystemCachePteValid(v_stack_p70, local_r14, v_stack_p48, (uint32_t)(Arg5));
    goto loc_00347D44;
loc_00347F41:
    result = MiDirtyPte(local_r10, local_r14, v_stack_p48, (uint32_t)(Arg5));
    goto loc_00347D3A;
loc_00347F4E:
    goto loc_00347CB3;
loc_00347F5A:
    Arg2 = (*(uint64_t *)((uint32_t)(Arg5) + 0x18)) & (result);
    Arg2 = (Arg2) + 1;
    result = (Arg2) ^ (*(uint64_t *)((uint32_t)(Arg5) + 0x18));
    result = (result) & (*(uint64_t *)((uint32_t)(Arg5) + 0x18));
    result = (result) ^ (Arg2);
    *(uint64_t *)((uint32_t)(Arg5) + 0x18) = result;
    local_r12 = 0;
    goto loc_00347EA7;
loc_00347F93:
    Arg4 = 0;
    Arg3 = 0;
    Arg1 = 0;
    result = MmAccessFault(Arg1, 0, Arg3, Arg4);
    v_stack_p44 = (uint32_t)(result);
    if (!sign_flag) goto loc_00347C8F;
loc_00347FAF:
    goto loc_00347D94;
loc_00347FBE:
    goto loc_00347C87;
loc_00347FCA:
    Arg3 = 0;
    Arg2 = 0;
    result = MiMakeTransitionHeatBatch((uint32_t)(Arg5), Arg2, Arg3, Arg4);
    v_stack_p50 = result;
    if (result != -1) goto loc_00347E85;
    result = MiUnlockProtoPoolPage(v_stack_pD8, v_stack_p40, Arg3, Arg4);
    result = MiReplenishTransitionPageHeatList(v_stack_pD8, v_stack_p40, Arg3, Arg4);
    Arg1 = 0;
    v_stack_p50 = 0;
loc_0034800D:
    goto loc_00347C8F;
loc_00348019:
    result = MiMapSystemCachePage(0, local_r14, (uint32_t)((uint32_t)((uint32_t)(Arg5))), Arg4);
    v_stack_p58 = result;
    if (result != 0) goto loc_00347D3A;
    goto loc_00347C68;
loc_0034803D:
    result = MiReleasePtes(v_rip + 11466267, 0, (uint32_t)((uint32_t)(local_r12 + 1)), Arg4);
    if ((((uint8_t)(local_r12 + 1)) & ((uint8_t)(*(uint64_t *)(local_rsi)))) == 0) goto loc_00347D9D;
    local_rbx = (*(uint64_t *)(local_rsi)) >> (12);
    local_rbx = (local_rbx) & ((uint32_t)(Arg5));
    local_rdi = (local_rbx + local_rbx * 2) << (4);
    local_rdi = (local_rdi) + (result);
    result = MiLockPageInline(local_rdi, 0, (uint32_t)((uint32_t)(local_r12 + 1)), Arg4);
    result = MiRemoveLockedPageChargeAndDecRef(local_rdi, 0, (uint32_t)((uint32_t)(local_r12 + 1)), Arg4);
    result = MiUnlockPage(local_rdi, (uint8_t)((uint8_t)(result)), (uint32_t)((uint32_t)(local_r12 + 1)), Arg4);
    goto loc_00347D9D;
loc_00348098:
    if ((((uint8_t)(v_stack_pD8)) & (63)) == 0) goto loc_00347C15;
    goto loc_00347DF5;
loc_003480A7:
    result = MiReservePtes(v_rip + 11466167, (uint32_t)((uint32_t)(local_r12 + 1)), (uint32_t)((uint32_t)(local_r12 + 1)), Arg4);
    v_stack_p68 = result;
    goto loc_00347DA1;
loc_003480D1:
    Arg2 = (local_r14) << (25);
    result = ((uint32_t)(0xC000009AULL)) << (25);
    Arg2 = (Arg2) - (result);
    Arg2 = (Arg2) >> (16);
    Arg1 = 0;
    result = MiHandleSpecialPurposeMemoryCachedFault(Arg1, Arg2, (uint8_t)(result), local_rdi);
    result = MiUnlockProtoPoolPage(v_stack_pD8, v_stack_p40, (uint8_t)(result), local_rdi);
    goto loc_0034800D;
loc_0034811A:
    result = (uint32_t)(v_stack_p44);
    if (((uint32_t)(result)) == 3) { result = (uint32_t)((uint32_t)(0xC0000709ULL)); }
    v_stack_p44 = (uint32_t)(result);
    goto loc_00347EA7;
loc_00348133:
    if ((uint32_t)(result) != 0) goto loc_00347EB0;
    Arg2 = 0;
    result = MiAddLockedPageCharge(result, Arg2, (uint8_t)(result), local_rdi);
    Arg1 = (uint32_t)(v_stack_p44);
    if ((uint32_t)(result) == 0) { Arg1 = (uint32_t)((uint32_t)(0xC000009AULL)); }
    v_stack_p44 = (uint32_t)(Arg1);
    goto loc_00347EB0;
loc_0034815D:
    result = MiIssuePageHeatList(Arg1, Arg2, (uint8_t)(result), local_rdi);
    result = MiFreeTransitionPageHeatList(v_stack_p50, Arg2, (uint8_t)(result), local_rdi);
    result = 0;
    v_stack_p50 = 0;
    goto loc_00347ED9;
loc_00348178:
    Arg4 = 0;
    Arg3 = 0;
    Arg1 = 0;
    result = MmAccessFault(Arg1, v_stack_pC0, Arg3, Arg4);
    v_stack_p44 = (uint32_t)(result);
    if (sign_flag) goto loc_00347FAF;
    goto loc_0034800D;
loc_003481A1:
    result = MiUnlockProtoPoolPage(v_stack_pD8, v_stack_p40, Arg3, Arg4);
    goto loc_00347CBC;
loc_003481B2:
    Arg2 = (v_stack_p48) >> (12);
    Arg2 = (Arg2) & (result);
    result = MiMapFrame(result, Arg2, Arg3, Arg4);
    goto loc_00347F1A;
loc_003481D9:
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (uint32_t)(0x786ULL), Arg3, v_stack_pD8);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00347B44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
