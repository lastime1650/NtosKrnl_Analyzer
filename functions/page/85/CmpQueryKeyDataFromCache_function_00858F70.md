# CmpQueryKeyDataFromCache

- RVA: `0x00858F70`–`0x008593B6` (길이 `1,094` bytes)
- VA: `0x0000000140858F70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006A944`
- 디코드: `255`개 명령, `1,094/1,094` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008590C2` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008590FE` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085917B` → [CmEqualTrans](../84/CmEqualTrans_function_0084BF60.md) (function, `0x0084BF60`)
- `0x008591E0` → [CmGetVisibleSubkeyCount](../84/CmGetVisibleSubkeyCount_function_00849D74.md) (function, `0x00849D74`)
- `0x008591FB` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00859202` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00859242` → [CmListGetNextElement](../../pagecmrc/BC/CmListGetNextElement_function_00BC9940.md) (function, `0x00BC9940`)
- `0x0085925C` → [CmEqualTrans](../84/CmEqualTrans_function_0084BF60.md) (function, `0x0084BF60`)
- `0x00859286` → [CmpIsKeyDeleted](../84/CmpIsKeyDeleted_function_0084BDB0.md) (function, `0x0084BDB0`)
- `0x008592B5` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008592FA` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085935C` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00859382` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085938C` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00859393` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)

### Direct callers
- [CmQueryKey](CmQueryKey_function_00858240.md) at `0x008583CD`
- [CmpQueryKeyData](CmpQueryKeyData_function_00858E70.md) at `0x00858EBC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00859242` → [CmListGetNextElement](../../pagecmrc/BC/CmListGetNextElement_function_00BC9940.md) (`PAGE` → `PAGECMRC`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008593B1` → [sub_00B16C30](../B1/Unknown_function_00B16C30.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00858F70  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00858F75  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00858F7A  57                              push rdi
00858F7B  41 54                           push r12
00858F7D  41 55                           push r13
00858F7F  41 56                           push r14
00858F81  41 57                           push r15
00858F83  48 83 EC 60                     sub rsp, 0x60
00858F87  41 8B D9                        mov ebx, r9d
00858F8A  4D 8B F8                        mov r15, r8
00858F8D  48 8B F9                        mov rdi, rcx
00858F90  C7 44 24 38 FF FF FF FF         mov dword ptr [rsp + 0x38], 0xffffffff
00858F98  33 F6                           xor esi, esi
00858F9A  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
00858F9E  48 8B 41 50                     mov rax, qword ptr [rcx + 0x50]
00858FA2  48 85 C0                        test rax, rax
00858FA5  0F 84 CD 03 00 00               je 0x140859378
00858FAB  44 0F B7 70 18                  movzx r14d, word ptr [rax + 0x18]
00858FB0  8B 00                           mov eax, dword ptr [rax]
00858FB2  A8 01                           test al, 1
00858FB4  74 04                           je 0x140858fba
00858FB6  66 45 03 F6                     add r14w, r14w
00858FBA  83 FA 04                        cmp edx, 4
00858FBD  0F 85 E2 03 00 00               jne 0x1408593a5
00858FC3  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
00858FC8  C7 44 24 20 FF FF FF FF         mov dword ptr [rsp + 0x20], 0xffffffff
00858FD0  89 74 24 24                     mov dword ptr [rsp + 0x24], esi
00858FD4  44 0F B7 89 B0 00 00 00         movzx r9d, word ptr [rcx + 0xb0]
00858FDC  44 89 8C 24 90 00 00 00         mov dword ptr [rsp + 0x90], r9d
00858FE4  4C 8B A4 24 B8 00 00 00         mov r12, qword ptr [rsp + 0xb8]
00858FEC  4D 85 E4                        test r12, r12
00858FEF  0F 85 3B 02 00 00               jne 0x140859230
00858FF5  C7 44 24 20 FF FF FF FF         mov dword ptr [rsp + 0x20], 0xffffffff
00858FFD  89 74 24 24                     mov dword ptr [rsp + 0x24], esi
00859001  C7 44 24 28 FF FF FF FF         mov dword ptr [rsp + 0x28], 0xffffffff
00859009  89 74 24 2C                     mov dword ptr [rsp + 0x2c], esi
0085900D  0F B7 87 B2 00 00 00            movzx eax, word ptr [rdi + 0xb2]
00859014  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00859018  44 8B AF B4 00 00 00            mov r13d, dword ptr [rdi + 0xb4]
0085901F  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
00859024  4D 85 E4                        test r12, r12
00859027  0F 85 E7 02 00 00               jne 0x140859314
0085902D  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00859035  C7 00 28 00 00 00               mov dword ptr [rax], 0x28
0085903B  83 FB 28                        cmp ebx, 0x28
0085903E  0F 82 6D 01 00 00               jb 0x1408591b1
00859044  48 8B C6                        mov rax, rsi
00859047  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0085904C  48 8B 9F A8 00 00 00            mov rbx, qword ptr [rdi + 0xa8]
00859053  4D 85 E4                        test r12, r12
00859056  0F 85 B4 00 00 00               jne 0x140859110
0085905C  4C 8D AF D0 00 00 00            lea r13, [rdi + 0xd0]
00859063  49 89 1F                        mov qword ptr [r15], rbx
00859066  41 89 77 08                     mov dword ptr [r15 + 8], esi
0085906A  41 0F B7 C6                     movzx eax, r14w
0085906E  41 89 47 20                     mov dword ptr [r15 + 0x20], eax
00859072  B8 FF FF FF FF                  mov eax, 0xffffffff
00859077  48 85 FF                        test rdi, rdi
0085907A  74 0C                           je 0x140859088
0085907C  4D 85 E4                        test r12, r12
0085907F  0F 85 D2 00 00 00               jne 0x140859157
00859085  8B 47 60                        mov eax, dword ptr [rdi + 0x60]
00859088  41 89 47 14                     mov dword ptr [r15 + 0x14], eax
0085908C  45 89 4F 10                     mov dword ptr [r15 + 0x10], r9d
00859090  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00859094  41 89 47 18                     mov dword ptr [r15 + 0x18], eax
00859098  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
0085909C  41 89 47 1C                     mov dword ptr [r15 + 0x1c], eax
008590A0  8B 47 08                        mov eax, dword ptr [rdi + 8]
008590A3  A8 40                           test al, 0x40
008590A5  75 06                           jne 0x1408590ad
008590A7  4D 39 6D 00                     cmp qword ptr [r13], r13
008590AB  74 31                           je 0x1408590de
008590AD  8B 57 28                        mov edx, dword ptr [rdi + 0x28]
008590B0  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
008590B4  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
008590B9  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008590C0  74 3C                           je 0x1408590fe
008590C2  E8 99 BB FF FF                  call 0x140854c60
008590C7  48 85 C0                        test rax, rax
008590CA  0F 85 07 01 00 00               jne 0x1408591d7
008590D0  BE 9A 00 00 C0                  mov esi, 0xc000009a
008590D5  89 74 24 4C                     mov dword ptr [rsp + 0x4c], esi
008590D9  E9 31 01 00 00                  jmp 0x14085920f
008590DE  A8 01                           test al, 1
008590E0  75 6C                           jne 0x14085914e
008590E2  A8 02                           test al, 2
008590E4  0F 85 A1 00 00 00               jne 0x14085918b
008590EA  A8 04                           test al, 4
008590EC  0F 85 D9 00 00 00               jne 0x1408591cb
008590F2  8B 47 70                        mov eax, dword ptr [rdi + 0x70]
008590F5  41 89 47 0C                     mov dword ptr [r15 + 0xc], eax
008590F9  E9 09 01 00 00                  jmp 0x140859207
008590FE  E8 AD BB FF FF                  call 0x140854cb0
00859103  EB C2                           jmp 0x1408590c7
00859105  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
00859110  4C 8D AF D0 00 00 00            lea r13, [rdi + 0xd0]
00859117  48 85 C0                        test rax, rax
0085911A  75 09                           jne 0x140859125
0085911C  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
00859120  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00859125  4C 3B E8                        cmp r13, rax
00859128  74 17                           je 0x140859141
0085912A  48 8D 48 E0                     lea rcx, [rax - 0x20]
0085912E  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00859133  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00859137  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0085913C  48 85 C9                        test rcx, rcx
0085913F  75 33                           jne 0x140859174
00859141  44 8B 8C 24 90 00 00 00         mov r9d, dword ptr [rsp + 0x90]
00859149  E9 15 FF FF FF                  jmp 0x140859063
0085914E  41 89 77 0C                     mov dword ptr [r15 + 0xc], esi
00859152  E9 B0 00 00 00                  jmp 0x140859207
00859157  48 8B 87 20 01 00 00            mov rax, qword ptr [rdi + 0x120]
0085915E  48 85 C0                        test rax, rax
00859161  0F 84 1E FF FF FF               je 0x140859085
00859167  49 3B C4                        cmp rax, r12
0085916A  75 50                           jne 0x1408591bc
0085916C  8B 87 18 01 00 00               mov eax, dword ptr [rdi + 0x118]
00859172  EB 4B                           jmp 0x1408591bf
00859174  49 8B D4                        mov rdx, r12
00859177  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
0085917B  E8 E0 2D FF FF                  call 0x14084bf60
00859180  84 C0                           test al, al
00859182  75 11                           jne 0x140859195
00859184  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00859189  EB 85                           jmp 0x140859110
0085918B  41 C7 47 0C 01 00 00 00         mov dword ptr [r15 + 0xc], 1
00859193  EB 72                           jmp 0x140859207
00859195  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0085919A  83 78 44 08                     cmp dword ptr [rax + 0x44], 8
0085919E  75 E4                           jne 0x140859184
008591A0  48 8B 58 58                     mov rbx, qword ptr [rax + 0x58]
008591A4  44 8B 8C 24 90 00 00 00         mov r9d, dword ptr [rsp + 0x90]
008591AC  E9 B2 FE FF FF                  jmp 0x140859063
008591B1  BE 23 00 00 C0                  mov esi, 0xc0000023
008591B6  89 74 24 4C                     mov dword ptr [rsp + 0x4c], esi
008591BA  EB 4B                           jmp 0x140859207
008591BC  8B 47 60                        mov eax, dword ptr [rdi + 0x60]
008591BF  4C 8D AF D0 00 00 00            lea r13, [rdi + 0xd0]
008591C6  E9 BD FE FF FF                  jmp 0x140859088
008591CB  48 8B 47 70                     mov rax, qword ptr [rdi + 0x70]
008591CF  8B 08                           mov ecx, dword ptr [rax]
008591D1  41 89 4F 0C                     mov dword ptr [r15 + 0xc], ecx
008591D5  EB 30                           jmp 0x140859207
008591D7  4D 8B C4                        mov r8, r12
008591DA  48 8B D0                        mov rdx, rax
008591DD  48 8B CF                        mov rcx, rdi
008591E0  E8 8F 0B FF FF                  call 0x140849d74
008591E5  41 89 47 0C                     mov dword ptr [r15 + 0xc], eax
008591E9  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
008591ED  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
008591F2  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008591F9  74 07                           je 0x140859202
008591FB  E8 20 3A 00 00                  call 0x14085cc20
00859200  EB 05                           jmp 0x140859207
00859202  E8 39 CD FF FF                  call 0x140855f40
00859207  EB 06                           jmp 0x14085920f
00859209  8B F0                           mov esi, eax
0085920B  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
0085920F  8B C6                           mov eax, esi
00859211  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00859216  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0085921A  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0085921E  49 8B E3                        mov rsp, r11
00859221  41 5F                           pop r15
00859223  41 5E                           pop r14
00859225  41 5D                           pop r13
00859227  41 5C                           pop r12
00859229  5F                              pop rdi
0085922A  C3                              ret
0085922B  CC                              int3
0085922C  0F 1F 40 00                     nop dword ptr [rax]
00859230  41 B8 20 00 00 00               mov r8d, 0x20
00859236  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
0085923B  48 8D 8F D0 00 00 00            lea rcx, [rdi + 0xd0]
00859242  E8 F9 06 37 00                  call 0x140bc9940
00859247  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0085924C  48 85 C0                        test rax, rax
0085924F  0F 84 A0 FD FF FF               je 0x140858ff5
00859255  49 8B D4                        mov rdx, r12
00859258  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
0085925C  E8 FF 2C FF FF                  call 0x14084bf60
00859261  84 C0                           test al, al
00859263  44 8B 8C 24 90 00 00 00         mov r9d, dword ptr [rsp + 0x90]
0085926B  74 C3                           je 0x140859230
0085926D  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
00859272  83 78 44 01                     cmp dword ptr [rax + 0x44], 1
00859276  75 B8                           jne 0x140859230
00859278  48 8B 40 58                     mov rax, qword ptr [rax + 0x58]
0085927C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00859281  33 D2                           xor edx, edx
00859283  48 8B C8                        mov rcx, rax
00859286  E8 25 2B FF FF                  call 0x14084bdb0
0085928B  84 C0                           test al, al
0085928D  44 8B 8C 24 90 00 00 00         mov r9d, dword ptr [rsp + 0x90]
00859295  75 99                           jne 0x140859230
00859297  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
0085929C  8B 50 28                        mov edx, dword ptr [rax + 0x28]
0085929F  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
008592A3  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
008592A8  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008592AF  0F 84 CD 00 00 00               je 0x140859382
008592B5  E8 A6 B9 FF FF                  call 0x140854c60
008592BA  48 85 C0                        test rax, rax
008592BD  0F 84 AB 00 00 00               je 0x14085936e
008592C3  8B 40 34                        mov eax, dword ptr [rax + 0x34]
008592C6  0F B7 C0                        movzx eax, ax
008592C9  39 84 24 90 00 00 00            cmp dword ptr [rsp + 0x90], eax
008592D0  0F 43 84 24 90 00 00 00         cmovae eax, dword ptr [rsp + 0x90]
008592D8  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
008592DF  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
008592E4  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
008592E8  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
008592ED  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008592F4  0F 85 99 00 00 00               jne 0x140859393
008592FA  E8 41 CC FF FF                  call 0x140855f40
008592FF  44 8B 8C 24 90 00 00 00         mov r9d, dword ptr [rsp + 0x90]
00859307  44 89 8C 24 90 00 00 00         mov dword ptr [rsp + 0x90], r9d
0085930F  E9 1C FF FF FF                  jmp 0x140859230
00859314  48 8B 87 20 01 00 00            mov rax, qword ptr [rdi + 0x120]
0085931B  48 85 C0                        test rax, rax
0085931E  0F 84 09 FD FF FF               je 0x14085902d
00859324  49 3B C4                        cmp rax, r12
00859327  0F 85 00 FD FF FF               jne 0x14085902d
0085932D  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00859331  44 8B EE                        mov r13d, esi
00859334  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
00859338  39 B7 18 01 00 00               cmp dword ptr [rdi + 0x118], esi
0085933E  0F 84 E9 FC FF FF               je 0x14085902d
00859344  8B 97 1C 01 00 00               mov edx, dword ptr [rdi + 0x11c]
0085934A  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0085934E  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
00859353  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
0085935A  74 30                           je 0x14085938c
0085935C  E8 FF B8 FF FF                  call 0x140854c60
00859361  48 8B C8                        mov rcx, rax
00859364  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00859369  48 85 C0                        test rax, rax
0085936C  75 41                           jne 0x1408593af
0085936E  BE 9A 00 00 C0                  mov esi, 0xc000009a
00859373  E9 97 FE FF FF                  jmp 0x14085920f
00859378  B8 9A 00 00 C0                  mov eax, 0xc000009a
0085937D  E9 8F FE FF FF                  jmp 0x140859211
00859382  E8 29 B9 FF FF                  call 0x140854cb0
00859387  E9 2E FF FF FF                  jmp 0x1408592ba
0085938C  E8 1F B9 FF FF                  call 0x140854cb0
00859391  EB CE                           jmp 0x140859361
00859393  E8 88 38 00 00                  call 0x14085cc20
00859398  44 8B 8C 24 90 00 00 00         mov r9d, dword ptr [rsp + 0x90]
008593A0  E9 8B FE FF FF                  jmp 0x140859230
008593A5  BE 0D 00 00 C0                  mov esi, 0xc000000d
008593AA  E9 60 FE FF FF                  jmp 0x14085920f
008593AF  8B C6                           mov eax, esi
008593B1  E9 7A D8 2B 00                  jmp 0x140b16c30
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpQueryKeyDataFromCache(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p30;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (96);
    v_stack_m50 = 0xFFFFFFFFULL;
    v_rsi = 0;
    v_stack_m4C = 0;
    if (*(unsigned __int64 *)(a1 + 80) == 0) goto loc_00859378;
    v_r14 = *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 80) + 24);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 80))))) & (1)) != 0) {
        v_r14 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 80) + 24)) + ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 80) + 24))));
    }
    if (a2 != 4) goto loc_008593A5;
    v_stack_m48 = 0;
    v_stack_m68 = 0xFFFFFFFFULL;
    v_stack_m64 = 0;
    v_stack_p8 = (unsigned int)(*(unsigned __int16 *)(a1 + 176));
    if (a6 != 0) goto loc_00859230;
loc_00858FF5:
    v_stack_m68 = 0xFFFFFFFFULL;
    v_stack_m64 = 0;
    v_stack_m60 = 0xFFFFFFFFULL;
    v_stack_m5C = 0;
    v_stack_m58 = (unsigned int)(*(unsigned __int16 *)(a1 + 178));
    v_stack_m54 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 180)));
    if (a6 != 0) goto loc_00859314;
loc_0085902D:
    *(unsigned int *)(a5) = 40;
    if (((unsigned int)((unsigned int)(a4))) < 40) goto loc_008591B1;
    v_stack_m38 = 0;
    if (a6 != 0) goto loc_00859110;
loc_00859063:
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(a1 + 168);
    *(unsigned int *)(a3 + 8) = 0;
    *(unsigned int *)(a3 + 32) = (unsigned int)((unsigned __int16)(v_r14));
    if (a1 == 0) goto loc_00859088;
    if (a6 != 0) goto loc_00859157;
loc_00859085:
loc_00859088:
    *(unsigned int *)(a3 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96)));
    *(unsigned int *)(a3 + 16) = (unsigned int)(*(unsigned __int16 *)(a1 + 176));
    *(unsigned int *)(a3 + 24) = (unsigned int)((unsigned int)(v_stack_m58));
    *(unsigned int *)(a3 + 28) = (unsigned int)((unsigned int)(v_stack_m54));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 8)))) & (64)) != 0) goto loc_008590AD;
    if ((*(unsigned __int64 *)(a1 + 208)) == (a1 + 208)) goto loc_008590DE;
loc_008590AD:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) == 0) goto loc_008590FE;
    result = HvpGetCellFlat(*(unsigned __int64 *)(a1 + 32), (unsigned int)(*(unsigned int *)(a1 + 40)), v_stack_m50, *(unsigned __int16 *)(a1 + 176));
loc_008590C7:
    if (result != 0) goto loc_008591D7;
    v_stack_m3C = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_0085920F;
loc_008590DE:
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0085914E;
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_0085918B;
    if ((((unsigned __int8)(result)) & (4)) != 0) goto loc_008591CB;
    *(unsigned int *)(a3 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 112)));
    goto loc_00859207;
loc_008590FE:
    result = HvpGetCellPaged(*(unsigned __int64 *)(a1 + 32), (unsigned int)(*(unsigned int *)(a1 + 40)), v_stack_m50, *(unsigned __int16 *)(a1 + 176));
    goto loc_008590C7;
loc_00859110:
    if (result == 0) {
        result = *(unsigned __int64 *)(a1 + 208 + 8);
        v_stack_m38 = result;
    }
    if ((a1 + 208) == result) goto loc_00859141;
    v_stack_m48 = result - 32;
    v_stack_m38 = *(unsigned __int64 *)(result + 8);
    if (result - 32 != 0) goto loc_00859174;
loc_00859141:
    goto loc_00859063;
loc_0085914E:
    *(unsigned int *)(a3 + 12) = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_00859207;
loc_00859157:
    if (*(unsigned __int64 *)(a1 + 288) == 0) goto loc_00859085;
    if ((*(unsigned __int64 *)(a1 + 288)) != a6) goto loc_008591BC;
    goto loc_008591BF;
loc_00859174:
    result = CmEqualTrans(*(unsigned __int64 *)(result - 32 + 56), a6, v_stack_m50, (unsigned int)(v_stack_p8));
    if ((unsigned __int8)(result) != 0) goto loc_00859195;
loc_00859184:
    goto loc_00859110;
loc_0085918B:
    *(unsigned int *)(a3 + 12) = 1;
    goto loc_00859207;
loc_00859195:
    if ((*(unsigned int *)(v_stack_m48 + 68)) != 8) goto loc_00859184;
    goto loc_00859063;
loc_008591B1:
    v_stack_m3C = (unsigned int)((unsigned int)(0xC0000023ULL));
    goto loc_00859207;
loc_008591BC:
loc_008591BF:
    goto loc_00859088;
loc_008591CB:
    *(unsigned int *)(a3 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 112))));
    goto loc_00859207;
loc_008591D7:
    result = CmGetVisibleSubkeyCount(a1, *(unsigned __int64 *)(a1 + 112), a6, (unsigned int)(v_stack_p8));
    *(unsigned int *)(a3 + 12) = (unsigned int)(result);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) == 0) goto loc_00859202;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(a1 + 32), v_stack_m50, a6, (unsigned int)(v_stack_p8));
    goto loc_00859207;
loc_00859202:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(a1 + 32), v_stack_m50, a6, (unsigned int)(v_stack_p8));
loc_00859207:
    goto loc_0085920F;
loc_0085920F:
loc_00859211:
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000023ULL)));
loc_00859230:
    result = CmListGetNextElement(a1 + 208, v_stack_m20, 32, (unsigned int)(v_stack_p8));
    v_stack_m38 = result;
    if (result == 0) goto loc_00858FF5;
    result = CmEqualTrans(*(unsigned __int64 *)(result + 56), a6, 32, (unsigned int)(v_stack_p8));
    if ((unsigned __int8)(result) == 0) goto loc_00859230;
    if ((*(unsigned int *)(v_stack_m38 + 68)) != 1) goto loc_00859230;
    v_stack_m38 = *(unsigned __int64 *)(v_stack_m38 + 88);
    a2 = 0;
    result = CmpIsKeyDeleted(*(unsigned __int64 *)(v_stack_m38 + 88), a2, 32, (unsigned int)(v_stack_p30));
    if ((unsigned __int8)(result) != 0) goto loc_00859230;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m38 + 32) + 140)) & (1)) == 0) goto loc_00859382;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_stack_m38 + 32), (unsigned int)(*(unsigned int *)(v_stack_m38 + 40)), v_stack_m40, (unsigned int)(v_stack_p30));
loc_008592BA:
    if (result == 0) goto loc_0085936E;
    result = (unsigned __int16)((unsigned int)(*(unsigned int *)(result + 52)));
    if (v_stack_p30 >= ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 52)))))) { result = v_stack_p30; }
    v_stack_p30 = (unsigned int)(result);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m38 + 32) + 140)) & (1)) != 0) goto loc_00859393;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_stack_m38 + 32), v_stack_m40, v_stack_m40, (unsigned int)(v_stack_p30));
    v_stack_p30 = (unsigned int)((unsigned int)(v_stack_p30));
    goto loc_00859230;
loc_00859314:
    if (*(unsigned __int64 *)(a1 + 288) == 0) goto loc_0085902D;
    if ((*(unsigned __int64 *)(a1 + 288)) != a6) goto loc_0085902D;
    v_stack_m30 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64));
    v_stack_m2C = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64));
    if ((*(unsigned int *)(a1 + 280)) == ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)))) goto loc_0085902D;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) == 0) goto loc_0085938C;
    result = HvpGetCellFlat(*(unsigned __int64 *)(a1 + 32), (unsigned int)(*(unsigned int *)(a1 + 284)), v_stack_m40, (unsigned int)(v_stack_p30));
loc_00859361:
    v_stack_m20 = result;
    if (result != 0) goto loc_008593AF;
loc_0085936E:
    goto loc_0085920F;
loc_00859378:
    goto loc_00859211;
loc_00859382:
    result = HvpGetCellPaged(result, (unsigned int)(*(unsigned int *)(a1 + 284)), v_stack_m40, (unsigned int)(v_stack_p30));
    goto loc_008592BA;
loc_0085938C:
    result = HvpGetCellPaged(result, (unsigned int)(*(unsigned int *)(a1 + 284)), v_stack_m40, (unsigned int)(v_stack_p30));
    goto loc_00859361;
loc_00859393:
    result = HvpReleaseCellFlat(result, (unsigned int)(*(unsigned int *)(a1 + 284)), v_stack_m40, (unsigned int)(v_stack_p30));
    goto loc_00859230;
loc_008593A5:
    goto loc_0085920F;
loc_008593AF:
}
```

## 5. (Beta) C Style

```c
int64_t CmpQueryKeyDataFromCache(void *Arg1, int32_t Arg2, void *Arg3, int32_t Arg4, void *Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r14;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p30;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (96);
    v_stack_m50 = 0xFFFFFFFFULL;
    local_rsi = 0;
    v_stack_m4C = 0;
    if (*(uint64_t *)(arg1 + 0x50) == 0) goto loc_00859378;
    local_r14 = *(uint16_t *)(*(uint64_t *)(arg1 + 0x50) + 0x18);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x50))))) & (1)) != 0) {
        local_r14 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x50) + 0x18)) + ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x50) + 0x18))));
    }
    if (Arg2 != 4) goto loc_008593A5;
    v_stack_m48 = 0;
    v_stack_m68 = 0xFFFFFFFFULL;
    v_stack_m64 = 0;
    v_stack_p8 = (uint32_t)(*(uint16_t *)(arg1 + 0xB0));
    if (Arg6 != 0) goto loc_00859230;
loc_00858FF5:
    v_stack_m68 = 0xFFFFFFFFULL;
    v_stack_m64 = 0;
    v_stack_m60 = 0xFFFFFFFFULL;
    v_stack_m5C = 0;
    v_stack_m58 = (uint32_t)(*(uint16_t *)(arg1 + 0xB2));
    v_stack_m54 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB4)));
    if (Arg6 != 0) goto loc_00859314;
loc_0085902D:
    *(uint32_t *)(arg5) = 40;
    if (((uint32_t)((uint32_t)(Arg4))) < 40) goto loc_008591B1;
    v_stack_m38 = 0;
    if (Arg6 != 0) goto loc_00859110;
loc_00859063:
    *(uint64_t *)(arg3) = *(uint64_t *)(arg1 + 0xA8);
    *(uint32_t *)(arg3 + 0x8) = 0;
    *(uint32_t *)(arg3 + 0x20) = (uint32_t)((uint16_t)(local_r14));
    if (Arg1 == NULL) goto loc_00859088;
    if (Arg6 != 0) goto loc_00859157;
loc_00859085:
loc_00859088:
    *(uint32_t *)(arg3 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60)));
    *(uint32_t *)(arg3 + 0x10) = (uint32_t)(*(uint16_t *)(arg1 + 0xB0));
    *(uint32_t *)(arg3 + 0x18) = (uint32_t)((uint32_t)(v_stack_m58));
    *(uint32_t *)(arg3 + 0x1C) = (uint32_t)((uint32_t)(v_stack_m54));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) & (64)) != 0) goto loc_008590AD;
    if ((*(uint64_t *)(arg1 + 0xD0)) == (Arg1 + 208)) goto loc_008590DE;
loc_008590AD:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) == 0) goto loc_008590FE;
    result = HvpGetCellFlat(*(uint64_t *)(arg1 + 0x20), (uint32_t)(*(uint32_t *)(arg1 + 0x28)), v_stack_m50, *(uint16_t *)(arg1 + 0xB0));
loc_008590C7:
    if (result != 0) goto loc_008591D7;
    v_stack_m3C = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_0085920F;
loc_008590DE:
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0085914E;
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_0085918B;
    if ((((uint8_t)(result)) & (4)) != 0) goto loc_008591CB;
    *(uint32_t *)(arg3 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x70)));
    goto loc_00859207;
loc_008590FE:
    result = HvpGetCellPaged(*(uint64_t *)(arg1 + 0x20), (uint32_t)(*(uint32_t *)(arg1 + 0x28)), v_stack_m50, *(uint16_t *)(arg1 + 0xB0));
    goto loc_008590C7;
loc_00859110:
    if (result == 0) {
        result = *(uint64_t *)(arg1 + 0xD0 + 0x8);
        v_stack_m38 = result;
    }
    if ((Arg1 + 208) == result) goto loc_00859141;
    v_stack_m48 = result - 32;
    v_stack_m38 = *(uint64_t *)(result + 0x8);
    if (result - 32 != 0) goto loc_00859174;
loc_00859141:
    goto loc_00859063;
loc_0085914E:
    *(uint32_t *)(arg3 + 0xC) = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_00859207;
loc_00859157:
    if (*(uint64_t *)(arg1 + 0x120) == 0) goto loc_00859085;
    if ((*(uint64_t *)(arg1 + 0x120)) != Arg6) goto loc_008591BC;
    goto loc_008591BF;
loc_00859174:
    result = CmEqualTrans(*(uint64_t *)(result - 0x20 + 0x38), Arg6, v_stack_m50, (uint32_t)(v_stack_p8));
    if ((uint8_t)(result) != 0) goto loc_00859195;
loc_00859184:
    goto loc_00859110;
loc_0085918B:
    *(uint32_t *)(arg3 + 0xC) = 1;
    goto loc_00859207;
loc_00859195:
    if ((*(uint32_t *)(v_stack_m48 + 0x44)) != 8) goto loc_00859184;
    goto loc_00859063;
loc_008591B1:
    v_stack_m3C = (uint32_t)((uint32_t)(0xC0000023ULL));
    goto loc_00859207;
loc_008591BC:
loc_008591BF:
    goto loc_00859088;
loc_008591CB:
    *(uint32_t *)(arg3 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x70))));
    goto loc_00859207;
loc_008591D7:
    result = CmGetVisibleSubkeyCount(Arg1, *(uint64_t *)(arg1 + 0x70), Arg6, (uint32_t)(v_stack_p8));
    *(uint32_t *)(arg3 + 0xC) = (uint32_t)(result);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) == 0) goto loc_00859202;
    result = HvpReleaseCellFlat(*(uint64_t *)(arg1 + 0x20), v_stack_m50, Arg6, (uint32_t)(v_stack_p8));
    goto loc_00859207;
loc_00859202:
    result = HvpReleaseCellPaged(*(uint64_t *)(arg1 + 0x20), v_stack_m50, Arg6, (uint32_t)(v_stack_p8));
loc_00859207:
    goto loc_0085920F;
loc_0085920F:
loc_00859211:
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000023ULL)));
loc_00859230:
    result = CmListGetNextElement(Arg1 + 208, v_stack_m20, 32, (uint32_t)(v_stack_p8));
    v_stack_m38 = result;
    if (result == 0) goto loc_00858FF5;
    result = CmEqualTrans(*(uint64_t *)(result + 0x38), Arg6, 32, (uint32_t)(v_stack_p8));
    if ((uint8_t)(result) == 0) goto loc_00859230;
    if ((*(uint32_t *)(v_stack_m38 + 0x44)) != 1) goto loc_00859230;
    v_stack_m38 = *(uint64_t *)(v_stack_m38 + 0x58);
    Arg2 = 0;
    result = CmpIsKeyDeleted(*(uint64_t *)(v_stack_m38 + 0x58), Arg2, 32, (uint32_t)(v_stack_p30));
    if ((uint8_t)(result) != 0) goto loc_00859230;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m38 + 0x20) + 0x8C)) & (1)) == 0) goto loc_00859382;
    result = HvpGetCellFlat(*(uint64_t *)(v_stack_m38 + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m38 + 0x28)), v_stack_m40, (uint32_t)(v_stack_p30));
loc_008592BA:
    if (result == 0) goto loc_0085936E;
    result = (uint16_t)((uint32_t)(*(uint32_t *)(result + 0x34)));
    if (v_stack_p30 >= ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x34)))))) { result = v_stack_p30; }
    v_stack_p30 = (uint32_t)(result);
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m38 + 0x20) + 0x8C)) & (1)) != 0) goto loc_00859393;
    result = HvpReleaseCellPaged(*(uint64_t *)(v_stack_m38 + 0x20), v_stack_m40, v_stack_m40, (uint32_t)(v_stack_p30));
    v_stack_p30 = (uint32_t)((uint32_t)(v_stack_p30));
    goto loc_00859230;
loc_00859314:
    if (*(uint64_t *)(arg1 + 0x120) == 0) goto loc_0085902D;
    if ((*(uint64_t *)(arg1 + 0x120)) != Arg6) goto loc_0085902D;
    v_stack_m30 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    v_stack_m2C = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    if ((*(uint32_t *)(arg1 + 0x118)) == ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)))) goto loc_0085902D;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) == 0) goto loc_0085938C;
    result = HvpGetCellFlat(*(uint64_t *)(arg1 + 0x20), (uint32_t)(*(uint32_t *)(arg1 + 0x11C)), v_stack_m40, (uint32_t)(v_stack_p30));
loc_00859361:
    v_stack_m20 = result;
    if (result != 0) goto loc_008593AF;
loc_0085936E:
    goto loc_0085920F;
loc_00859378:
    goto loc_00859211;
loc_00859382:
    result = HvpGetCellPaged(result, (uint32_t)(*(uint32_t *)(arg1 + 0x11C)), v_stack_m40, (uint32_t)(v_stack_p30));
    goto loc_008592BA;
loc_0085938C:
    result = HvpGetCellPaged(result, (uint32_t)(*(uint32_t *)(arg1 + 0x11C)), v_stack_m40, (uint32_t)(v_stack_p30));
    goto loc_00859361;
loc_00859393:
    result = HvpReleaseCellFlat(result, (uint32_t)(*(uint32_t *)(arg1 + 0x11C)), v_stack_m40, (uint32_t)(v_stack_p30));
    goto loc_00859230;
loc_008593A5:
    goto loc_0085920F;
loc_008593AF:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `16` | `R` |
| `Arg1` | `+ 0xB2` | `16` | `R` |
| `Arg1` | `+ 0xB4` | `32` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `R` |
| `Arg1` | `+ 0x118` | `32` | `R` |
| `Arg1` | `+ 0x11C` | `32` | `R` |
| `Arg1` | `+ 0x120` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x8` | `32` | `W` |
| `Arg3` | `+ 0xC` | `32` | `W` |
| `Arg3` | `+ 0x10` | `32` | `W` |
| `Arg3` | `+ 0x14` | `32` | `W` |
| `Arg3` | `+ 0x18` | `32` | `W` |
| `Arg3` | `+ 0x1C` | `32` | `W` |
| `Arg3` | `+ 0x20` | `32` | `W` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00858F70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
