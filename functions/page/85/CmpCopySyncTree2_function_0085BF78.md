# CmpCopySyncTree2

- RVA: `0x0085BF78`–`0x0085C925` (길이 `2,477` bytes)
- VA: `0x000000014085BF78`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006AE94`
- 디코드: `600`개 명령, `2,477/2,477` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **55**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0085C05F` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085C07D` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085C098` → [CmpFindSubKeyByNumber](CmpFindSubKeyByNumber_function_0085C930.md) (function, `0x0085C930`)
- `0x0085C0F2` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085C13C` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085C16A` → [CmpCopyKeyPartial](CmpCopyKeyPartial_function_0085AFF4.md) (function, `0x0085AFF4`)
- `0x0085C1A9` → [CmpAddSubKeyEx](../84/CmpAddSubKeyEx_function_0084C940.md) (function, `0x0084C940`)
- `0x0085C1E5` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085C204` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085C251` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085C26A` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085C32E` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085C348` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085C352` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085C35C` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085C381` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085C38F` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C426` → [CmpMarkKeyParentDirty](../A7/CmpMarkKeyParentDirty_function_00A749E8.md) (function, `0x00A749E8`)
- `0x0085C45C` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085C46F` → [CmpInitializeKeyNameString](../A8/CmpInitializeKeyNameString_function_00A8B734.md) (function, `0x00A8B734`)
- `0x0085C48D` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085C4A7` → [CmpFindSubKeyByNameWithStatus](CmpFindSubKeyByNameWithStatus_function_00852770.md) (function, `0x00852770`)
- `0x0085C4CA` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085C4EE` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085C547` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0085C571` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0085C580` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0085C5D6` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C5E0` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C60D` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085C647` → [CmpSyncSubKeysAfterDelete](../AC/CmpSyncSubKeysAfterDelete_function_00AC5980.md) (function, `0x00AC5980`)
- `0x0085C660` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085C66D` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C677` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085C681` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085C6A1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0085C6C5` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085C6D9` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C6F6` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085C726` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085C73C` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085C74F` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085C756` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C760` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C76A` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C774` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C77B` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C7ED` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0085C832` → [HvpMarkCellDirty](HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0085C85A` → [HvpMarkCellDirty](HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0085C8C0` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C8DF` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C8FD` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085C90C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0085C91B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [CmpCopySyncTree](../7F/CmpCopySyncTree_function_007F21A0.md) at `0x007F221C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x0085C547` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0085C571` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0085C580` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0085C6A1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0085C7ED` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0085C90C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0085C91B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **9**
  - `0x0085C80F` → [sub_00B16DFE](../B1/Unknown_function_00B16DFE.md) (`tail-transfer`)
  - `0x0085C81E` → [sub_00B16DFE](../B1/Unknown_function_00B16DFE.md) (`tail-transfer`)
  - `0x0085C84A` → [sub_00B16DFE](../B1/Unknown_function_00B16DFE.md) (`tail-transfer`)
  - `0x0085C897` → [sub_00B16DFE + 0x98](../B1/Unknown_function_00B16DFE.md) (`tail-transfer`)
  - `0x0085C8A0` → [sub_00B16DFE + 0x89](../B1/Unknown_function_00B16DFE.md) (`tail-transfer`)
  - `0x0085C8A6` → [sub_00B16DFE + 0x95](../B1/Unknown_function_00B16DFE.md) (`tail-transfer`)
  - `0x0085C8BA` → [sub_00B16DFE + 0xA3](../B1/Unknown_function_00B16DFE.md) (`tail-transfer`)
  - `0x0085C8D9` → [sub_00B16DFE + 0xAE](../B1/Unknown_function_00B16DFE.md) (`tail-transfer`)
  - `0x0085C8F7` → [sub_00B16DFE + 0xB9](../B1/Unknown_function_00B16DFE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085BF78  48 8B C4                        mov rax, rsp
0085BF7B  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
0085BF7F  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
0085BF83  89 50 10                        mov dword ptr [rax + 0x10], edx
0085BF86  48 89 48 08                     mov qword ptr [rax + 8], rcx
0085BF8A  55                              push rbp
0085BF8B  56                              push rsi
0085BF8C  57                              push rdi
0085BF8D  41 54                           push r12
0085BF8F  41 55                           push r13
0085BF91  41 56                           push r14
0085BF93  41 57                           push r15
0085BF95  48 8D 68 B9                     lea rbp, [rax - 0x47]
0085BF99  48 81 EC E0 00 00 00            sub rsp, 0xe0
0085BFA0  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
0085BFA3  4D 8B F9                        mov r15, r9
0085BFA6  48 8B 5D 6F                     mov rbx, qword ptr [rbp + 0x6f]
0085BFAA  45 33 C9                        xor r9d, r9d
0085BFAD  83 E0 01                        and eax, 1
0085BFB0  44 89 4D A3                     mov dword ptr [rbp - 0x5d], r9d
0085BFB4  89 45 E7                        mov dword ptr [rbp - 0x19], eax
0085BFB7  48 8B F9                        mov rdi, rcx
0085BFBA  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
0085BFBD  83 C9 FF                        or ecx, 0xffffffff
0085BFC0  FF C8                           dec eax
0085BFC2  44 89 4D A7                     mov dword ptr [rbp - 0x59], r9d
0085BFC6  83 F8 01                        cmp eax, 1
0085BFC9  44 89 4C 24 50                  mov dword ptr [rsp + 0x50], r9d
0085BFCE  0F 57 C0                        xorps xmm0, xmm0
0085BFD1  44 88 4D 57                     mov byte ptr [rbp + 0x57], r9b
0085BFD5  41 0F 96 C0                     setbe r8b
0085BFD9  89 4D 97                        mov dword ptr [rbp - 0x69], ecx
0085BFDC  44 89 4D 9B                     mov dword ptr [rbp - 0x65], r9d
0085BFE0  45 8B F1                        mov r14d, r9d
0085BFE3  89 4D B7                        mov dword ptr [rbp - 0x49], ecx
0085BFE6  45 8B E9                        mov r13d, r9d
0085BFE9  44 89 4D BB                     mov dword ptr [rbp - 0x45], r9d
0085BFED  89 4D AF                        mov dword ptr [rbp - 0x51], ecx
0085BFF0  44 89 4D B3                     mov dword ptr [rbp - 0x4d], r9d
0085BFF4  89 4D 87                        mov dword ptr [rbp - 0x79], ecx
0085BFF7  44 89 4D 8B                     mov dword ptr [rbp - 0x75], r9d
0085BFFB  89 4D CF                        mov dword ptr [rbp - 0x31], ecx
0085BFFE  44 89 4D D3                     mov dword ptr [rbp - 0x2d], r9d
0085C002  89 4D EB                        mov dword ptr [rbp - 0x15], ecx
0085C005  4C 89 4D EF                     mov qword ptr [rbp - 0x11], r9
0085C009  44 88 45 5F                     mov byte ptr [rbp + 0x5f], r8b
0085C00D  89 4D 8F                        mov dword ptr [rbp - 0x71], ecx
0085C010  44 89 4D 93                     mov dword ptr [rbp - 0x6d], r9d
0085C014  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
0085C019  44 89 4D BF                     mov dword ptr [rbp - 0x41], r9d
0085C01D  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
0085C021  C7 45 9F 01 00 00 00            mov dword ptr [rbp - 0x61], 1
0085C028  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
0085C02C  45 84 C0                        test r8b, r8b
0085C02F  0F 85 A8 07 00 00               jne 0x14085c7dd
0085C035  41 8B C6                        mov eax, r14d
0085C038  48 8D 0C 80                     lea rcx, [rax + rax*4]
0085C03C  4C 8D 24 8F                     lea r12, [rdi + rcx*4]
0085C040  45 89 4C 24 08                  mov dword ptr [r12 + 8], r9d
0085C045  4D 85 ED                        test r13, r13
0085C048  74 1A                           je 0x14085c064
0085C04A  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
0085C052  48 8D 55 AF                     lea rdx, [rbp - 0x51]
0085C056  49 8B CF                        mov rcx, r15
0085C059  0F 85 30 03 00 00               jne 0x14085c38f
0085C05F  E8 DC 9E FF FF                  call 0x140855f40
0085C064  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
0085C06C  4C 8D 45 AF                     lea r8, [rbp - 0x51]
0085C070  41 8B 14 24                     mov edx, dword ptr [r12]
0085C074  49 8B CF                        mov rcx, r15
0085C077  0F 84 B1 02 00 00               je 0x14085c32e
0085C07D  E8 DE 8B FF FF                  call 0x140854c60
0085C082  45 8B 44 24 08                  mov r8d, dword ptr [r12 + 8]
0085C087  4C 8D 4D A7                     lea r9, [rbp - 0x59]
0085C08B  48 8B D0                        mov rdx, rax
0085C08E  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0085C092  49 8B CF                        mov rcx, r15
0085C095  4C 8B E8                        mov r13, rax
0085C098  E8 93 08 00 00                  call 0x14085c930
0085C09D  45 33 C9                        xor r9d, r9d
0085C0A0  8B F8                           mov edi, eax
0085C0A2  85 C0                           test eax, eax
0085C0A4  0F 88 D8 06 00 00               js 0x14085c782
0085C0AA  41 FF 44 24 08                  inc dword ptr [r12 + 8]
0085C0AF  8B 75 A7                        mov esi, dword ptr [rbp - 0x59]
0085C0B2  8B 7D E7                        mov edi, dword ptr [rbp - 0x19]
0085C0B5  83 FE FF                        cmp esi, -1
0085C0B8  0F 84 0D 02 00 00               je 0x14085c2cb
0085C0BE  40 84 FF                        test dil, dil
0085C0C1  75 08                           jne 0x14085c0cb
0085C0C3  85 F6                           test esi, esi
0085C0C5  0F 88 00 02 00 00               js 0x14085c2cb
0085C0CB  44 38 4D 5F                     cmp byte ptr [rbp + 0x5f], r9b
0085C0CF  0F 85 70 03 00 00               jne 0x14085c445
0085C0D5  F6 45 77 40                     test byte ptr [rbp + 0x77], 0x40
0085C0D9  74 66                           je 0x14085c141
0085C0DB  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
0085C0E3  4C 8D 45 8F                     lea r8, [rbp - 0x71]
0085C0E7  8B D6                           mov edx, esi
0085C0E9  49 8B CF                        mov rcx, r15
0085C0EC  0F 84 6A 02 00 00               je 0x14085c35c
0085C0F2  E8 69 8B FF FF                  call 0x140854c60
0085C0F7  8A 40 0C                        mov al, byte ptr [rax + 0xc]
0085C0FA  A8 02                           test al, 2
0085C0FC  0F 84 36 02 00 00               je 0x14085c338
0085C102  B9 01 00 00 00                  mov ecx, 1
0085C107  3B 4D 9F                        cmp ecx, dword ptr [rbp - 0x61]
0085C10A  0F 8F 56 02 00 00               jg 0x14085c366
0085C110  41 8B 44 24 0C                  mov eax, dword ptr [r12 + 0xc]
0085C115  41 8A 97 8C 00 00 00            mov dl, byte ptr [r15 + 0x8c]
0085C11C  C1 E0 1D                        shl eax, 0x1d
0085C11F  80 E2 01                        and dl, 1
0085C122  C1 F8 1D                        sar eax, 0x1d
0085C125  3B C8                           cmp ecx, eax
0085C127  0F 8E 5E 02 00 00               jle 0x14085c38b
0085C12D  84 D2                           test dl, dl
0085C12F  49 8B CF                        mov rcx, r15
0085C132  48 8D 55 8F                     lea rdx, [rbp - 0x71]
0085C136  0F 85 31 05 00 00               jne 0x14085c66d
0085C13C  E8 FF 9D FF FF                  call 0x140855f40
0085C141  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
0085C144  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0085C149  45 8B 4C 24 04                  mov r9d, dword ptr [r12 + 4]
0085C14E  83 C8 04                        or eax, 4
0085C151  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0085C156  4C 8B C3                        mov r8, rbx
0085C159  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
0085C161  49 8B CF                        mov rcx, r15
0085C164  8B D6                           mov edx, esi
0085C166  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0085C16A  E8 85 EE FF FF                  call 0x14085aff4
0085C16F  45 33 C9                        xor r9d, r9d
0085C172  8B F8                           mov edi, eax
0085C174  85 C0                           test eax, eax
0085C176  0F 88 06 06 00 00               js 0x14085c782
0085C17C  41 F6 44 24 10 02               test byte ptr [r12 + 0x10], 2
0085C182  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
0085C187  0F 84 C2 06 00 00               je 0x14085c84f
0085C18D  41 8B 54 24 04                  mov edx, dword ptr [r12 + 4]
0085C192  48 8B CB                        mov rcx, rbx
0085C195  44 8B CE                        mov r9d, esi
0085C198  49 C1 E9 1F                     shr r9, 0x1f
0085C19C  47 8B 4C 8D 14                  mov r9d, dword ptr [r13 + r9*4 + 0x14]
0085C1A1  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
0085C1A6  45 8B C5                        mov r8d, r13d
0085C1A9  E8 92 07 FF FF                  call 0x14084c940
0085C1AE  45 33 C9                        xor r9d, r9d
0085C1B1  8B F8                           mov edi, eax
0085C1B3  85 C0                           test eax, eax
0085C1B5  0F 88 C7 05 00 00               js 0x14085c782
0085C1BB  41 8B 54 24 04                  mov edx, dword ptr [r12 + 4]
0085C1C0  4C 8D 45 DF                     lea r8, [rbp - 0x21]
0085C1C4  83 C9 FF                        or ecx, 0xffffffff
0085C1C7  44 89 4D E3                     mov dword ptr [rbp - 0x1d], r9d
0085C1CB  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085C1D2  89 4D DF                        mov dword ptr [rbp - 0x21], ecx
0085C1D5  89 4D D7                        mov dword ptr [rbp - 0x29], ecx
0085C1D8  48 8B CB                        mov rcx, rbx
0085C1DB  44 89 4D DB                     mov dword ptr [rbp - 0x25], r9d
0085C1DF  0F 84 63 01 00 00               je 0x14085c348
0085C1E5  E8 76 8A FF FF                  call 0x140854c60
0085C1EA  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085C1F1  4C 8D 45 D7                     lea r8, [rbp - 0x29]
0085C1F5  48 8B F8                        mov rdi, rax
0085C1F8  41 8B D5                        mov edx, r13d
0085C1FB  48 8B CB                        mov rcx, rbx
0085C1FE  0F 84 4E 01 00 00               je 0x14085c352
0085C204  E8 57 8A FF FF                  call 0x140854c60
0085C209  0F B7 50 48                     movzx edx, word ptr [rax + 0x48]
0085C20D  4C 8B C0                        mov r8, rax
0085C210  0F B7 CA                        movzx ecx, dx
0085C213  66 03 C9                        add cx, cx
0085C216  F6 40 02 20                     test byte ptr [rax + 2], 0x20
0085C21A  8B 47 34                        mov eax, dword ptr [rdi + 0x34]
0085C21D  66 0F 44 CA                     cmove cx, dx
0085C221  0F B7 D1                        movzx edx, cx
0085C224  0F B7 C8                        movzx ecx, ax
0085C227  3B CA                           cmp ecx, edx
0085C229  0F 82 48 06 00 00               jb 0x14085c877
0085C22F  41 0F B7 40 4A                  movzx eax, word ptr [r8 + 0x4a]
0085C234  39 47 38                        cmp dword ptr [rdi + 0x38], eax
0085C237  0F 82 43 06 00 00               jb 0x14085c880
0085C23D  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085C244  48 8D 55 D7                     lea rdx, [rbp - 0x29]
0085C248  48 8B CB                        mov rcx, rbx
0085C24B  0F 85 85 03 00 00               jne 0x14085c5d6
0085C251  E8 EA 9C FF FF                  call 0x140855f40
0085C256  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085C25D  48 8D 55 DF                     lea rdx, [rbp - 0x21]
0085C261  48 8B CB                        mov rcx, rbx
0085C264  0F 85 76 03 00 00               jne 0x14085c5e0
0085C26A  E8 D1 9C FF FF                  call 0x140855f40
0085C26F  45 33 C9                        xor r9d, r9d
0085C272  41 8B F1                        mov esi, r9d
0085C275  44 38 4D 5F                     cmp byte ptr [rbp + 0x5f], r9b
0085C279  0F 85 97 01 00 00               jne 0x14085c416
0085C27F  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
0085C283  8B 45 A3                        mov eax, dword ptr [rbp - 0x5d]
0085C286  4C 8B F6                        mov r14, rsi
0085C289  FF C0                           inc eax
0085C28B  89 45 A3                        mov dword ptr [rbp - 0x5d], eax
0085C28E  3D 00 02 00 00                  cmp eax, 0x200
0085C293  0F 83 EF 05 00 00               jae 0x14085c888
0085C299  48 8B 7D 4F                     mov rdi, qword ptr [rbp + 0x4f]
0085C29D  48 8D 0C 80                     lea rcx, [rax + rax*4]
0085C2A1  44 8B F0                        mov r14d, eax
0085C2A4  02 D2                           add dl, dl
0085C2A6  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
0085C2A9  83 64 8F 0C F8                  and dword ptr [rdi + rcx*4 + 0xc], 0xfffffff8
0085C2AE  89 04 8F                        mov dword ptr [rdi + rcx*4], eax
0085C2B1  8A 44 8F 10                     mov al, byte ptr [rdi + rcx*4 + 0x10]
0085C2B5  24 FC                           and al, 0xfc
0085C2B7  44 89 6C 8F 04                  mov dword ptr [rdi + rcx*4 + 4], r13d
0085C2BC  4C 8B 6D C7                     mov r13, qword ptr [rbp - 0x39]
0085C2C0  0A C2                           or al, dl
0085C2C2  88 44 8F 10                     mov byte ptr [rdi + rcx*4 + 0x10], al
0085C2C6  E9 6A FD FF FF                  jmp 0x14085c035
0085C2CB  44 38 4D 5F                     cmp byte ptr [rbp + 0x5f], r9b
0085C2CF  0F 85 15 03 00 00               jne 0x14085c5ea
0085C2D5  41 F6 44 24 10 01               test byte ptr [r12 + 0x10], 1
0085C2DB  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
0085C2DF  0F 85 1E 02 00 00               jne 0x14085c503
0085C2E5  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0085C2EA  8B 75 9F                        mov esi, dword ptr [rbp - 0x61]
0085C2ED  45 85 F6                        test r14d, r14d
0085C2F0  0F 84 A3 00 00 00               je 0x14085c399
0085C2F6  48 8B 7D 4F                     mov rdi, qword ptr [rbp + 0x4f]
0085C2FA  4C 8B 6D C7                     mov r13, qword ptr [rbp - 0x39]
0085C2FE  41 FF CE                        dec r14d
0085C301  44 89 75 A3                     mov dword ptr [rbp - 0x5d], r14d
0085C305  4B 8D 0C B6                     lea rcx, [r14 + r14*4]
0085C309  4C 8D 24 8F                     lea r12, [rdi + rcx*4]
0085C30D  44 38 4D 57                     cmp byte ptr [rbp + 0x57], r9b
0085C311  0F 84 2E FD FF FF               je 0x14085c045
0085C317  44 3B 75 EB                     cmp r14d, dword ptr [rbp - 0x15]
0085C31B  0F 85 24 FD FF FF               jne 0x14085c045
0085C321  C6 45 5F 01                     mov byte ptr [rbp + 0x5f], 1
0085C325  44 88 4D 57                     mov byte ptr [rbp + 0x57], r9b
0085C329  E9 17 FD FF FF                  jmp 0x14085c045
0085C32E  E8 7D 89 FF FF                  call 0x140854cb0
0085C333  E9 4A FD FF FF                  jmp 0x14085c082
0085C338  F6 D0                           not al
0085C33A  0F B6 C8                        movzx ecx, al
0085C33D  83 E1 01                        and ecx, 1
0085C340  83 C9 02                        or ecx, 2
0085C343  E9 BF FD FF FF                  jmp 0x14085c107
0085C348  E8 63 89 FF FF                  call 0x140854cb0
0085C34D  E9 98 FE FF FF                  jmp 0x14085c1ea
0085C352  E8 59 89 FF FF                  call 0x140854cb0
0085C357  E9 AD FE FF FF                  jmp 0x14085c209
0085C35C  E8 4F 89 FF FF                  call 0x140854cb0
0085C361  E9 91 FD FF FF                  jmp 0x14085c0f7
0085C366  41 80 4C 24 10 01               or byte ptr [r12 + 0x10], 1
0085C36C  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
0085C374  48 8D 55 8F                     lea rdx, [rbp - 0x71]
0085C378  49 8B CF                        mov rcx, r15
0085C37B  0F 85 58 03 00 00               jne 0x14085c6d9
0085C381  E8 BA 9B FF FF                  call 0x140855f40
0085C386  E9 BA FC FF FF                  jmp 0x14085c045
0085C38B  84 D2                           test dl, dl
0085C38D  EB E5                           jmp 0x14085c374
0085C38F  E8 8C 08 00 00                  call 0x14085cc20
0085C394  E9 CB FC FF FF                  jmp 0x14085c064
0085C399  83 FA FF                        cmp edx, -1
0085C39C  0F 84 FA 04 00 00               je 0x14085c89c
0085C3A2  48 8B 7D 4F                     mov rdi, qword ptr [rbp + 0x4f]
0085C3A6  8B C2                           mov eax, edx
0085C3A8  FF CA                           dec edx
0085C3AA  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
0085C3AE  48 8D 0C 80                     lea rcx, [rax + rax*4]
0085C3B2  4C 8D 04 8D 00 00 00 00         lea r8, [rcx*4]
0085C3BA  43 8B 4C 28 0C                  mov ecx, dword ptr [r8 + r13 + 0xc]
0085C3BF  41 33 4D 0C                     xor ecx, dword ptr [r13 + 0xc]
0085C3C3  F6 C1 07                        test cl, 7
0085C3C6  0F 85 BF 02 00 00               jne 0x14085c68b
0085C3CC  43 0F 10 04 28                  movups xmm0, xmmword ptr [r8 + r13]
0085C3D1  0F 11 07                        movups xmmword ptr [rdi], xmm0
0085C3D4  43 8B 44 28 10                  mov eax, dword ptr [r8 + r13 + 0x10]
0085C3D9  89 47 10                        mov dword ptr [rdi + 0x10], eax
0085C3DC  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
0085C3DF  41 BE 01 00 00 00               mov r14d, 1
0085C3E5  C1 E0 1D                        shl eax, 0x1d
0085C3E8  C1 F8 1D                        sar eax, 0x1d
0085C3EB  3B F0                           cmp esi, eax
0085C3ED  0F 85 07 FF FF FF               jne 0x14085c2fa
0085C3F3  8B 83 18 01 00 00               mov eax, dword ptr [rbx + 0x118]
0085C3F9  FF C6                           inc esi
0085C3FB  89 75 9F                        mov dword ptr [rbp - 0x61], esi
0085C3FE  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
0085C402  83 FE 02                        cmp esi, 2
0085C405  0F 84 AF 02 00 00               je 0x14085c6ba
0085C40B  89 83 94 12 00 00               mov dword ptr [rbx + 0x1294], eax
0085C411  E9 E4 FE FF FF                  jmp 0x14085c2fa
0085C416  44 38 4D 57                     cmp byte ptr [rbp + 0x57], r9b
0085C41A  0F 84 5F FE FF FF               je 0x14085c27f
0085C420  41 8B D5                        mov edx, r13d
0085C423  48 8B CB                        mov rcx, rbx
0085C426  E8 BD 85 21 00                  call 0x140a749e8
0085C42B  45 33 C9                        xor r9d, r9d
0085C42E  8B F8                           mov edi, eax
0085C430  85 C0                           test eax, eax
0085C432  0F 88 4D 03 00 00               js 0x14085c785
0085C438  44 89 75 EB                     mov dword ptr [rbp - 0x15], r14d
0085C43C  44 88 4D 5F                     mov byte ptr [rbp + 0x5f], r9b
0085C440  E9 3A FE FF FF                  jmp 0x14085c27f
0085C445  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
0085C44D  4C 8D 45 97                     lea r8, [rbp - 0x69]
0085C451  8B D6                           mov edx, esi
0085C453  49 8B CF                        mov rcx, r15
0085C456  0F 84 1B 02 00 00               je 0x14085c677
0085C45C  E8 FF 87 FF FF                  call 0x140854c60
0085C461  4C 8B 45 EF                     mov r8, qword ptr [rbp - 0x11]
0085C465  48 8D 55 F7                     lea rdx, [rbp - 9]
0085C469  48 8B C8                        mov rcx, rax
0085C46C  48 8B F0                        mov rsi, rax
0085C46F  E8 C0 F2 22 00                  call 0x140a8b734
0085C474  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085C47B  4C 8D 45 CF                     lea r8, [rbp - 0x31]
0085C47F  41 8B 54 24 04                  mov edx, dword ptr [r12 + 4]
0085C484  48 8B CB                        mov rcx, rbx
0085C487  0F 84 F4 01 00 00               je 0x14085c681
0085C48D  E8 CE 87 FF FF                  call 0x140854c60
0085C492  33 FF                           xor edi, edi
0085C494  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
0085C499  4C 8D 45 F7                     lea r8, [rbp - 9]
0085C49D  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
0085C4A1  48 8B D0                        mov rdx, rax
0085C4A4  48 8B CB                        mov rcx, rbx
0085C4A7  E8 C4 62 FF FF                  call 0x140852770
0085C4AC  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085C4B3  48 8D 55 CF                     lea rdx, [rbp - 0x31]
0085C4B7  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
0085C4BC  48 8B CB                        mov rcx, rbx
0085C4BF  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
0085C4C4  0F 85 8C 02 00 00               jne 0x14085c756
0085C4CA  E8 71 9A FF FF                  call 0x140855f40
0085C4CF  41 83 FD FF                     cmp r13d, -1
0085C4D3  0F 85 0A 02 00 00               jne 0x14085c6e3
0085C4D9  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
0085C4E1  48 8D 55 97                     lea rdx, [rbp - 0x69]
0085C4E5  49 8B CF                        mov rcx, r15
0085C4E8  0F 85 72 02 00 00               jne 0x14085c760
0085C4EE  E8 4D 9A FF FF                  call 0x140855f40
0085C4F3  8B 75 A7                        mov esi, dword ptr [rbp - 0x59]
0085C4F6  4C 8B 6D C7                     mov r13, qword ptr [rbp - 0x39]
0085C4FA  C6 45 57 01                     mov byte ptr [rbp + 0x57], 1
0085C4FE  E9 D2 FB FF FF                  jmp 0x14085c0d5
0085C503  44 8B 4D BF                     mov r9d, dword ptr [rbp - 0x41]
0085C507  FF C2                           inc edx
0085C509  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
0085C50D  41 3B D1                        cmp edx, r9d
0085C510  0F 82 B9 01 00 00               jb 0x14085c6cf
0085C516  45 8B C1                        mov r8d, r9d
0085C519  41 8D 41 01                     lea eax, [r9 + 1]
0085C51D  41 D1 E8                        shr r8d, 1
0085C520  BA 01 00 00 00                  mov edx, 1
0085C525  43 8D 0C 08                     lea ecx, [r8 + r9]
0085C529  3B C1                           cmp eax, ecx
0085C52B  B9 00 01 00 00                  mov ecx, 0x100
0085C530  41 0F 46 D0                     cmovbe edx, r8d
0085C534  41 B8 43 4D 20 20               mov r8d, 0x20204d43
0085C53A  41 03 D1                        add edx, r9d
0085C53D  8B F2                           mov esi, edx
0085C53F  48 8D 14 92                     lea rdx, [rdx + rdx*4]
0085C543  48 C1 E2 02                     shl rdx, 2
0085C547  E8 A4 5B 32 00                  call 0x140b820f0
0085C54C  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0085C551  45 33 C9                        xor r9d, r9d
0085C554  48 8B F8                        mov rdi, rax
0085C557  48 85 C0                        test rax, rax
0085C55A  0F 84 32 03 00 00               je 0x14085c892
0085C560  8B 45 BF                        mov eax, dword ptr [rbp - 0x41]
0085C563  49 8B D5                        mov rdx, r13
0085C566  48 8B CF                        mov rcx, rdi
0085C569  4C 8D 04 80                     lea r8, [rax + rax*4]
0085C56D  49 C1 E0 02                     shl r8, 2
0085C571  E8 CA A2 E6 FF                  call 0x1406c6840
0085C576  4D 85 ED                        test r13, r13
0085C579  74 0A                           je 0x14085c585
0085C57B  33 D2                           xor edx, edx
0085C57D  49 8B CD                        mov rcx, r13
0085C580  E8 EB 62 32 00                  call 0x140b82870
0085C585  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
0085C589  4C 8B EF                        mov r13, rdi
0085C58C  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
0085C591  89 75 BF                        mov dword ptr [rbp - 0x41], esi
0085C594  8B 75 9F                        mov esi, dword ptr [rbp - 0x61]
0085C597  45 33 C9                        xor r9d, r9d
0085C59A  45 89 4C 24 08                  mov dword ptr [r12 + 8], r9d
0085C59F  8B C6                           mov eax, esi
0085C5A1  41 33 44 24 0C                  xor eax, dword ptr [r12 + 0xc]
0085C5A6  83 E0 F8                        and eax, 0xfffffff8
0085C5A9  33 C6                           xor eax, esi
0085C5AB  41 80 64 24 10 FE               and byte ptr [r12 + 0x10], 0xfe
0085C5B1  41 89 44 24 0C                  mov dword ptr [r12 + 0xc], eax
0085C5B6  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
0085C5BB  8B C2                           mov eax, edx
0085C5BD  48 8D 0C 80                     lea rcx, [rax + rax*4]
0085C5C1  41 0F 11 44 8D 00               movups xmmword ptr [r13 + rcx*4], xmm0
0085C5C7  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
0085C5CC  41 89 44 8D 10                  mov dword ptr [r13 + rcx*4 + 0x10], eax
0085C5D1  E9 17 FD FF FF                  jmp 0x14085c2ed
0085C5D6  E8 45 06 00 00                  call 0x14085cc20
0085C5DB  E9 76 FC FF FF                  jmp 0x14085c256
0085C5E0  E8 3B 06 00 00                  call 0x14085cc20
0085C5E5  E9 85 FC FF FF                  jmp 0x14085c26f
0085C5EA  83 7D 7F 02                     cmp dword ptr [rbp + 0x7f], 2
0085C5EE  0F 84 E1 FC FF FF               je 0x14085c2d5
0085C5F4  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085C5FB  4C 8D 45 87                     lea r8, [rbp - 0x79]
0085C5FF  41 8B 54 24 04                  mov edx, dword ptr [r12 + 4]
0085C604  48 8B CB                        mov rcx, rbx
0085C607  0F 84 B8 00 00 00               je 0x14085c6c5
0085C60D  E8 4E 86 FF FF                  call 0x140854c60
0085C612  45 33 D2                        xor r10d, r10d
0085C615  4C 8B C8                        mov r9, rax
0085C618  40 84 FF                        test dil, dil
0085C61B  0F 84 91 00 00 00               je 0x14085c6b2
0085C621  41 8B 4D 18                     mov ecx, dword ptr [r13 + 0x18]
0085C625  41 8B 51 18                     mov edx, dword ptr [r9 + 0x18]
0085C629  41 03 51 14                     add edx, dword ptr [r9 + 0x14]
0085C62D  41 03 4D 14                     add ecx, dword ptr [r13 + 0x14]
0085C631  3B D1                           cmp edx, ecx
0085C633  76 17                           jbe 0x14085c64c
0085C635  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
0085C639  4C 8B C3                        mov r8, rbx
0085C63C  49 8B D5                        mov rdx, r13
0085C63F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0085C644  49 8B CF                        mov rcx, r15
0085C647  E8 34 93 26 00                  call 0x140ac5980
0085C64C  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085C653  48 8D 55 87                     lea rdx, [rbp - 0x79]
0085C657  48 8B CB                        mov rcx, rbx
0085C65A  0F 85 0A 01 00 00               jne 0x14085c76a
0085C660  E8 DB 98 FF FF                  call 0x140855f40
0085C665  45 33 C9                        xor r9d, r9d
0085C668  E9 68 FC FF FF                  jmp 0x14085c2d5
0085C66D  E8 AE 05 00 00                  call 0x14085cc20
0085C672  E9 CA FA FF FF                  jmp 0x14085c141
0085C677  E8 34 86 FF FF                  call 0x140854cb0
0085C67C  E9 E0 FD FF FF                  jmp 0x14085c461
0085C681  E8 2A 86 FF FF                  call 0x140854cb0
0085C686  E9 07 FE FF FF                  jmp 0x14085c492
0085C68B  41 0F 10 45 00                  movups xmm0, xmmword ptr [r13]
0085C690  49 8D 55 14                     lea rdx, [r13 + 0x14]
0085C694  49 8B CD                        mov rcx, r13
0085C697  0F 11 07                        movups xmmword ptr [rdi], xmm0
0085C69A  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
0085C69E  89 47 10                        mov dword ptr [rdi + 0x10], eax
0085C6A1  E8 9A A1 E6 FF                  call 0x1406c6840
0085C6A6  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
0085C6AA  45 33 C9                        xor r9d, r9d
0085C6AD  E9 2A FD FF FF                  jmp 0x14085c3dc
0085C6B2  41 8B CA                        mov ecx, r10d
0085C6B5  E9 6B FF FF FF                  jmp 0x14085c625
0085C6BA  89 83 90 12 00 00               mov dword ptr [rbx + 0x1290], eax
0085C6C0  E9 35 FC FF FF                  jmp 0x14085c2fa
0085C6C5  E8 E6 85 FF FF                  call 0x140854cb0
0085C6CA  E9 43 FF FF FF                  jmp 0x14085c612
0085C6CF  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0085C6D4  E9 BB FE FF FF                  jmp 0x14085c594
0085C6D9  E8 42 05 00 00                  call 0x14085cc20
0085C6DE  E9 62 F9 FF FF                  jmp 0x14085c045
0085C6E3  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085C6EA  4C 8D 45 B7                     lea r8, [rbp - 0x49]
0085C6EE  41 8B D5                        mov edx, r13d
0085C6F1  48 8B CB                        mov rcx, rbx
0085C6F4  74 59                           je 0x14085c74f
0085C6F6  E8 65 85 FF FF                  call 0x140854c60
0085C6FB  83 7D 7F 02                     cmp dword ptr [rbp + 0x7f], 2
0085C6FF  4C 8B F0                        mov r14, rax
0085C702  0F 84 01 01 00 00               je 0x14085c809
0085C708  48 8B 46 04                     mov rax, qword ptr [rsi + 4]
0085C70C  49 39 46 04                     cmp qword ptr [r14 + 4], rax
0085C710  0F 8C F3 00 00 00               jl 0x14085c809
0085C716  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085C71D  48 8D 55 B7                     lea rdx, [rbp - 0x49]
0085C721  48 8B CB                        mov rcx, rbx
0085C724  75 4E                           jne 0x14085c774
0085C726  E8 15 98 FF FF                  call 0x140855f40
0085C72B  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
0085C733  48 8D 55 97                     lea rdx, [rbp - 0x69]
0085C737  49 8B CF                        mov rcx, r15
0085C73A  75 3F                           jne 0x14085c77b
0085C73C  E8 FF 97 FF FF                  call 0x140855f40
0085C741  45 33 C9                        xor r9d, r9d
0085C744  41 8B F1                        mov esi, r9d
0085C747  41 8A D1                        mov dl, r9b
0085C74A  E9 34 FB FF FF                  jmp 0x14085c283
0085C74F  E8 5C 85 FF FF                  call 0x140854cb0
0085C754  EB A5                           jmp 0x14085c6fb
0085C756  E8 C5 04 00 00                  call 0x14085cc20
0085C75B  E9 6F FD FF FF                  jmp 0x14085c4cf
0085C760  E8 BB 04 00 00                  call 0x14085cc20
0085C765  E9 89 FD FF FF                  jmp 0x14085c4f3
0085C76A  E8 B1 04 00 00                  call 0x14085cc20
0085C76F  E9 F1 FE FF FF                  jmp 0x14085c665
0085C774  E8 A7 04 00 00                  call 0x14085cc20
0085C779  EB B0                           jmp 0x14085c72b
0085C77B  E8 A0 04 00 00                  call 0x14085cc20
0085C780  EB BF                           jmp 0x14085c741
0085C782  49 8B F1                        mov rsi, r9
0085C785  4D 8B F1                        mov r14, r9
0085C788  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0085C78D  4C 39 4D C7                     cmp qword ptr [rbp - 0x39], r9
0085C791  0F 85 14 01 00 00               jne 0x14085c8ab
0085C797  48 85 F6                        test rsi, rsi
0085C79A  0F 85 2A 01 00 00               jne 0x14085c8ca
0085C7A0  4D 85 F6                        test r14, r14
0085C7A3  0F 85 40 01 00 00               jne 0x14085c8e9
0085C7A9  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
0085C7AD  48 85 C0                        test rax, rax
0085C7B0  0F 85 51 01 00 00               jne 0x14085c907
0085C7B6  4D 85 ED                        test r13, r13
0085C7B9  0F 85 57 01 00 00               jne 0x14085c916
0085C7BF  8B C7                           mov eax, edi
0085C7C1  48 8B 9C 24 38 01 00 00         mov rbx, qword ptr [rsp + 0x138]
0085C7C9  48 81 C4 E0 00 00 00            add rsp, 0xe0
0085C7D0  41 5F                           pop r15
0085C7D2  41 5E                           pop r14
0085C7D4  41 5D                           pop r13
0085C7D6  41 5C                           pop r12
0085C7D8  5F                              pop rdi
0085C7D9  5E                              pop rsi
0085C7DA  5D                              pop rbp
0085C7DB  C3                              ret
0085C7DC  CC                              int3
0085C7DD  BA 00 02 00 00                  mov edx, 0x200
0085C7E2  B9 00 01 00 00                  mov ecx, 0x100
0085C7E7  41 B8 43 6D 5A 6E               mov r8d, 0x6e5a6d43
0085C7ED  E8 FE 58 32 00                  call 0x140b820f0
0085C7F2  45 33 C9                        xor r9d, r9d
0085C7F5  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
0085C7F9  48 85 C0                        test rax, rax
0085C7FC  0F 85 33 F8 FF FF               jne 0x14085c035
0085C802  B8 9A 00 00 C0                  mov eax, 0xc000009a
0085C807  EB B8                           jmp 0x14085c7c1
0085C809  41 F6 44 24 10 02               test byte ptr [r12 + 0x10], 2
0085C80F  0F 85 E9 A5 2B 00               jne 0x140b16dfe
0085C815  41 0F B7 46 4A                  movzx eax, word ptr [r14 + 0x4a]
0085C81A  66 39 46 4A                     cmp word ptr [rsi + 0x4a], ax
0085C81E  0F 86 DA A5 2B 00               jbe 0x140b16dfe
0085C824  41 8B 54 24 04                  mov edx, dword ptr [r12 + 4]
0085C829  45 33 C9                        xor r9d, r9d
0085C82C  45 33 C0                        xor r8d, r8d
0085C82F  48 8B CB                        mov rcx, rbx
0085C832  E8 49 B8 FF FF                  call 0x140858080
0085C837  45 33 C9                        xor r9d, r9d
0085C83A  8B F8                           mov edi, eax
0085C83C  85 C0                           test eax, eax
0085C83E  0F 88 44 FF FF FF               js 0x14085c788
0085C844  41 80 4C 24 10 02               or byte ptr [r12 + 0x10], 2
0085C84A  E9 AF A5 2B 00                  jmp 0x140b16dfe
0085C84F  41 8B 54 24 04                  mov edx, dword ptr [r12 + 4]
0085C854  45 33 C0                        xor r8d, r8d
0085C857  48 8B CB                        mov rcx, rbx
0085C85A  E8 21 B8 FF FF                  call 0x140858080
0085C85F  45 33 C9                        xor r9d, r9d
0085C862  8B F8                           mov edi, eax
0085C864  85 C0                           test eax, eax
0085C866  0F 88 16 FF FF FF               js 0x14085c782
0085C86C  41 80 4C 24 10 02               or byte ptr [r12 + 0x10], 2
0085C872  E9 16 F9 FF FF                  jmp 0x14085c18d
0085C877  66 89 57 34                     mov word ptr [rdi + 0x34], dx
0085C87B  E9 AF F9 FF FF                  jmp 0x14085c22f
0085C880  89 47 38                        mov dword ptr [rdi + 0x38], eax
0085C883  E9 B5 F9 FF FF                  jmp 0x14085c23d
0085C888  BF 9A 00 00 C0                  mov edi, 0xc000009a
0085C88D  E9 F6 FE FF FF                  jmp 0x14085c788
0085C892  BF 9A 00 00 C0                  mov edi, 0xc000009a
0085C897  E9 FA A5 2B 00                  jmp 0x140b16e96
0085C89C  F6 45 77 40                     test byte ptr [rbp + 0x77], 0x40
0085C8A0  0F 85 E1 A5 2B 00               jne 0x140b16e87
0085C8A6  E9 E8 A5 2B 00                  jmp 0x140b16e93
0085C8AB  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
0085C8B3  48 8D 55 AF                     lea rdx, [rbp - 0x51]
0085C8B7  49 8B CF                        mov rcx, r15
0085C8BA  0F 84 E1 A5 2B 00               je 0x140b16ea1
0085C8C0  E8 5B 03 00 00                  call 0x14085cc20
0085C8C5  E9 CD FE FF FF                  jmp 0x14085c797
0085C8CA  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
0085C8D2  48 8D 55 97                     lea rdx, [rbp - 0x69]
0085C8D6  49 8B CF                        mov rcx, r15
0085C8D9  0F 84 CD A5 2B 00               je 0x140b16eac
0085C8DF  E8 3C 03 00 00                  call 0x14085cc20
0085C8E4  E9 B7 FE FF FF                  jmp 0x14085c7a0
0085C8E9  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0085C8F0  48 8D 55 B7                     lea rdx, [rbp - 0x49]
0085C8F4  48 8B CB                        mov rcx, rbx
0085C8F7  0F 84 BA A5 2B 00               je 0x140b16eb7
0085C8FD  E8 1E 03 00 00                  call 0x14085cc20
0085C902  E9 A2 FE FF FF                  jmp 0x14085c7a9
0085C907  33 D2                           xor edx, edx
0085C909  48 8B C8                        mov rcx, rax
0085C90C  E8 5F 5F 32 00                  call 0x140b82870
0085C911  E9 A0 FE FF FF                  jmp 0x14085c7b6
0085C916  33 D2                           xor edx, edx
0085C918  49 8B CD                        mov rcx, r13
0085C91B  E8 50 5F 32 00                  call 0x140b82870
0085C920  E9 9A FE FF FF                  jmp 0x14085c7bf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCopySyncTree2(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (224);
    a4 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 + 119))) & (1));
    *(unsigned int *)(v_rsp - 71 - 93) = 0;
    *(unsigned int *)(v_rsp - 71 - 25) = (unsigned int)(result);
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 + 127))) - 1);
    *(unsigned int *)(v_rsp - 71 - 89) = 0;
    v_stack_mC8 = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 87) = 0;
    a3 = (((unsigned int)(result)) <= 1) ? 1 : 0;
    *(unsigned int *)(v_rsp - 71 - 105) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 71 - 101) = 0;
    *(unsigned int *)(v_rsp - 71 - 73) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 71 - 69) = 0;
    *(unsigned int *)(v_rsp - 71 - 81) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 71 - 77) = 0;
    *(unsigned int *)(v_rsp - 71 - 121) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 71 - 117) = 0;
    *(unsigned int *)(v_rsp - 71 - 49) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 71 - 45) = 0;
    *(unsigned int *)(v_rsp - 71 - 21) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_rsp - 71 - 17) = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 95) = (unsigned __int8)(a3);
    *(unsigned int *)(v_rsp - 71 - 113) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 71 - 109) = 0;
    v_stack_mD0 = 0;
    *(unsigned int *)(v_rsp - 71 - 65) = 0;
    v_stack_mD4 = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 71 - 97) = 1;
    *(unsigned __int64 *)(v_rsp - 71 - 9) = v_xmm0;
    if ((unsigned __int8)(a3) != 0) goto loc_0085C7DD;
loc_0085C035:
    *(unsigned int *)(a1 + 0 + 0 * 4 * 4 + 8) = 0;
loc_0085C045:
    if (0 == 0) goto loc_0085C064;
    if (((*(unsigned __int8 *)(a4 + 140)) & (1)) != 0) goto loc_0085C38F;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 81, a3, a4);
loc_0085C064:
    if (((*(unsigned __int8 *)(a4 + 140)) & (1)) == 0) goto loc_0085C32E;
    result = HvpGetCellFlat(0, (unsigned int)(*(unsigned int *)(a1 + 0 + 0 * 4 * 4)), v_rsp - 71 - 81, a4);
loc_0085C082:
    *(unsigned __int64 *)(v_rsp - 71 - 57) = result;
    result = CmpFindSubKeyByNumber(0, result, (unsigned int)(*(unsigned int *)(a1 + 0 + 0 * 4 * 4 + 8)), v_rsp - 71 - 89);
    a4 = 0;
    if (sign_flag) goto loc_0085C782;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 89)))) == -1) goto loc_0085C2CB;
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 25))) != 0) goto loc_0085C0CB;
    if (sign_flag) goto loc_0085C2CB;
loc_0085C0CB:
    if ((*(unsigned __int8 *)(v_rsp - 71 + 95)) != 0) goto loc_0085C445;
loc_0085C0D5:
    if (((*(unsigned __int8 *)(v_rsp - 71 + 119)) & (64)) == 0) goto loc_0085C141;
    if (((*(unsigned __int8 *)(a4 + 140)) & (1)) == 0) goto loc_0085C35C;
    result = HvpGetCellFlat(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 89)))), v_rsp - 71 - 113, a4);
loc_0085C0F7:
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 12))) & (2)) == 0) goto loc_0085C338;
loc_0085C107:
    if (1 > (*(unsigned int *)(v_rsp - 71 - 97))) goto loc_0085C366;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 0 + 0 * 4 * 4 + 12))) << (29));
    a2 = (unsigned __int8)((*(unsigned __int8 *)(a4 + 140)) & (1));
    result = (unsigned int)((result) >> (29));
    if (1 <= ((unsigned int)(result))) goto loc_0085C38B;
    if ((unsigned __int8)(a2) != 0) goto loc_0085C66D;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 113, v_rsp - 71 - 113, a4);
loc_0085C141:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 + 119))) | (4));
    v_stack_mE0 = v_stack_mC8;
    v_stack_mE8 = 2;
    v_stack_mF8 = (unsigned int)(result);
    result = CmpCopyKeyPartial(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 89)))), *(unsigned __int64 *)(v_rsp - 71 + 111), (unsigned int)(*(unsigned int *)(a1 + 0 + 0 * 4 * 4 + 4)));
    a4 = 0;
    if (sign_flag) goto loc_0085C782;
    v_stack_mD8 = 1;
    if (((*(unsigned __int8 *)(a1 + 0 + 0 * 4 * 4 + 16)) & (2)) == 0) goto loc_0085C84F;
loc_0085C18D:
    a4 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 89))))) >> (31);
    result = CmpAddSubKeyEx(*(unsigned __int64 *)(v_rsp - 71 + 111), (unsigned int)(*(unsigned int *)(a1 + 0 + 0 * 4 * 4 + 4)), (unsigned int)((unsigned int)((unsigned int)(v_stack_mC8))), (unsigned int)(*(unsigned int *)(result + a4 * 4 + 20)));
    a4 = 0;
    if (sign_flag) goto loc_0085C782;
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 71 + 111)) | (0xFFFFFFFFULL));
    *(unsigned int *)(v_rsp - 71 - 29) = 0;
    *(unsigned int *)(v_rsp - 71 - 33) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 71 - 41) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 71 - 37) = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 140)) & (1)) == 0) goto loc_0085C348;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_rsp - 71 + 111), (unsigned int)(*(unsigned int *)(a1 + 0 + 0 * 4 * 4 + 4)), v_rsp - 71 - 33, a4);
loc_0085C1EA:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 140)) & (1)) == 0) goto loc_0085C352;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_rsp - 71 + 111), (unsigned int)((unsigned int)((unsigned int)(v_stack_mC8))), v_rsp - 71 - 41, a4);
loc_0085C209:
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(result + 72))) + ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(result + 72)))));
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) { a1 = (unsigned __int16)(*(unsigned __int16 *)(result + 72)); }
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 52))))) < ((unsigned int)((unsigned __int16)(a1)))) goto loc_0085C877;
loc_0085C22F:
    if ((*(unsigned int *)(result + 56)) < ((unsigned int)(*(unsigned __int16 *)(result + 74)))) goto loc_0085C880;
loc_0085C23D:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 140)) & (1)) != 0) goto loc_0085C5D6;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_rsp - 71 + 111), v_rsp - 71 - 41, result, a4);
loc_0085C256:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 140)) & (1)) != 0) goto loc_0085C5E0;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_rsp - 71 + 111), v_rsp - 71 - 33, result, a4);
loc_0085C26F:
    a4 = 0;
    if ((*(unsigned __int8 *)(v_rsp - 71 + 95)) != 0) goto loc_0085C416;
loc_0085C27F:
loc_0085C283:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 - 93))) + 1);
    *(unsigned int *)(v_rsp - 71 - 93) = (unsigned int)(result);
    if (((unsigned int)(result)) >= 512) goto loc_0085C888;
    a2 = (unsigned __int8)((v_stack_mD8) + ((unsigned __int8)(v_stack_mD8)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + result + result * 4 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 89)));
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + result + result * 4 * 4 + 16)) & (252));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + result + result * 4 * 4 + 4) = (unsigned int)((unsigned int)(v_stack_mC8));
    result = (unsigned __int8)((result) | ((unsigned __int8)(a2)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + result + result * 4 * 4 + 16) = (unsigned __int8)(result);
    goto loc_0085C035;
loc_0085C2CB:
    if ((*(unsigned __int8 *)(v_rsp - 71 + 95)) != 0) goto loc_0085C5EA;
loc_0085C2D5:
    if (((*(unsigned __int8 *)(a1 + 0 + 0 * 4 * 4 + 16)) & (1)) != 0) goto loc_0085C503;
loc_0085C2ED:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_0085C399;
loc_0085C2FA:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(result))) - 1);
    *(unsigned int *)(v_rsp - 71 - 93) = (unsigned int)(v_r14);
    if ((*(unsigned __int8 *)(v_rsp - 71 + 87)) == 0) goto loc_0085C045;
    if (((unsigned int)(v_r14)) != (*(unsigned int *)(v_rsp - 71 - 21))) goto loc_0085C045;
    *(unsigned __int8 *)(v_rsp - 71 + 95) = 1;
    *(unsigned __int8 *)(v_rsp - 71 + 87) = 0;
    goto loc_0085C045;
loc_0085C32E:
    result = HvpGetCellPaged(v_r14 + v_r14 * 4, (unsigned int)(v_stack_mD4), result, a4);
    goto loc_0085C082;
loc_0085C338:
    result = (unsigned __int8)(~(result));
    a1 = (unsigned int)(((unsigned __int8)(result)) & (1));
    a1 = (unsigned int)((a1) | (2));
    goto loc_0085C107;
loc_0085C348:
    result = HvpGetCellPaged(a1, (unsigned int)(v_stack_mD4), result, a4);
    goto loc_0085C1EA;
loc_0085C352:
    result = HvpGetCellPaged(a1, (unsigned int)(v_stack_mD4), result, a4);
    goto loc_0085C209;
loc_0085C35C:
    result = HvpGetCellPaged(a1, (unsigned int)(v_stack_mD4), result, a4);
    goto loc_0085C0F7;
loc_0085C366:
loc_0085C374:
    if (((*(unsigned __int8 *)(a4 + 140)) & (1)) != 0) goto loc_0085C6D9;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 113, result, a4);
    goto loc_0085C045;
loc_0085C38B:
    goto loc_0085C374;
loc_0085C38F:
    result = HvpReleaseCellFlat(0, v_rsp - 71 - 113, result, a4);
    goto loc_0085C064;
loc_0085C399:
    if (((unsigned int)(v_rsp - 71 - 113)) == -1) goto loc_0085C89C;
    a2 = (unsigned int)((v_rsp - 71 - 113) - 1);
    v_stack_mD4 = a2;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_rsp - 71 - 113)) + (unsigned int)((unsigned int)(v_rsp - 71 - 113)) * 4 * 4 + *(unsigned __int64 *)(v_rsp - 71 - 57) * 1 + 12))) ^ (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 57) + 12)));
    if ((((unsigned __int8)(a1)) & (7)) != 0) goto loc_0085C68B;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79)) = v_xmm0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_rsp - 71 - 113)) + (unsigned int)((unsigned int)(v_rsp - 71 - 113)) * 4 * 4 + *(unsigned __int64 *)(v_rsp - 71 - 57) * 1 + 16)));
loc_0085C3DC:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 12))) << (29));
    result = (unsigned int)((result) >> (29));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 97)))) != ((unsigned int)(result))) goto loc_0085C2FA;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 - 97))) + 1);
    *(unsigned int *)(v_rsp - 71 - 97) = (unsigned int)(v_rsi);
    v_stack_mD4 = a2;
    if (((unsigned int)(v_rsi)) == 2) goto loc_0085C6BA;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 4756) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 280)));
    goto loc_0085C2FA;
loc_0085C416:
    if ((*(unsigned __int8 *)(v_rsp - 71 + 87)) == 0) goto loc_0085C27F;
    result = CmpMarkKeyParentDirty(*(unsigned __int64 *)(v_rsp - 71 + 111), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 - 57))), (unsigned int)((unsigned int)(v_rsp - 71 - 113)) + (unsigned int)((unsigned int)(v_rsp - 71 - 113)) * 4 * 4, a4);
    a4 = 0;
    if (sign_flag) goto loc_0085C785;
    *(unsigned int *)(v_rsp - 71 - 21) = 1;
    *(unsigned __int8 *)(v_rsp - 71 + 95) = 0;
    goto loc_0085C27F;
loc_0085C445:
    if (((*(unsigned __int8 *)(a4 + 140)) & (1)) == 0) goto loc_0085C677;
    result = HvpGetCellFlat(0, (unsigned int)((unsigned int)(v_rsi)), v_rsp - 71 - 105, a4);
loc_0085C461:
    result = CmpInitializeKeyNameString(result, v_rsp - 71 - 9, *(unsigned __int64 *)(v_rsp - 71 - 17), a4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 140)) & (1)) == 0) goto loc_0085C681;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_rsp - 71 + 111), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + v_r14 + v_r14 * 4 * 4 + 4)), v_rsp - 71 - 49, a4);
loc_0085C492:
    v_rdi = 0;
    v_stack_mC8 = 0;
    result = CmpFindSubKeyByNameWithStatus(*(unsigned __int64 *)(v_rsp - 71 + 111), result, v_rsp - 71 - 9, v_stack_mC8);
    v_stack_mC8 = (unsigned int)((unsigned int)(v_stack_mC8));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 140)) & (1)) != 0) goto loc_0085C756;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_rsp - 71 + 111), v_rsp - 71 - 49, v_rsp - 71 - 9, v_stack_mC8);
loc_0085C4CF:
    if (((unsigned int)((unsigned int)(v_stack_mC8))) != -1) goto loc_0085C6E3;
    if (((*(unsigned __int8 *)(a4 + 140)) & (1)) != 0) goto loc_0085C760;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 105, v_rsp - 71 - 9, v_stack_mC8);
loc_0085C4F3:
    *(unsigned __int8 *)(v_rsp - 71 + 87) = 1;
    goto loc_0085C0D5;
loc_0085C503:
    a2 = (unsigned int)((v_rsp - 71 - 105) + 1);
    v_stack_mD4 = a2;
    if (a2 < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 65))))) goto loc_0085C6CF;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 65))))) >> (1));
    a2 = 1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 65)) + 1)) <= ((unsigned int)(a3 + (unsigned int)(*(unsigned int *)(v_rsp - 71 - 65)) * 1))) { a2 = a3; }
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 65)))));
    a2 = (a2 + a2 * 4) << (2);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x20204D43ULL), (unsigned int)(*(unsigned int *)(v_rsp - 71 - 65)));
    a4 = 0;
    if (result == 0) goto loc_0085C892;
    a3 = ((unsigned int)(*(unsigned int *)(v_rsp - 71 - 65)) + (unsigned int)(*(unsigned int *)(v_rsp - 71 - 65)) * 4) << (2);
    result = memcpy(result, v_stack_mD0, a3, a4);
    if (v_stack_mD0 != 0) {
        a2 = 0;
        a1 = v_stack_mD0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_stack_mD0 = result;
    *(unsigned int *)(v_rsp - 71 - 65) = (unsigned int)((unsigned int)(a2));
loc_0085C594:
    a4 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + v_r14 + v_r14 * 4 * 4 + 8) = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 97))))) ^ (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + v_r14 + v_r14 * 4 * 4 + 12)));
    result = (unsigned int)((result) & (0xFFFFFFF8ULL));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 97)))));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + v_r14 + v_r14 * 4 * 4 + 12) = (unsigned int)(result);
    *(unsigned __int64 *)(result + (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))) + (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))) * 4 * 4) = v_xmm0;
    *(unsigned int *)(result + (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))) + (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))) * 4 * 4 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + v_r14 + v_r14 * 4 * 4 + 16)));
    goto loc_0085C2ED;
loc_0085C5D6:
    result = HvpReleaseCellFlat((unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))) + (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))) * 4, (unsigned int)(v_stack_mD4), a3, a4);
    goto loc_0085C256;
loc_0085C5E0:
    result = HvpReleaseCellFlat((unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))) + (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))) * 4, (unsigned int)(v_stack_mD4), a3, a4);
    goto loc_0085C26F;
loc_0085C5EA:
    if ((*(unsigned int *)(v_rsp - 71 + 127)) == 2) goto loc_0085C2D5;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 140)) & (1)) == 0) goto loc_0085C6C5;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_rsp - 71 + 111), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + v_r14 + v_r14 * 4 * 4 + 4)), v_rsp - 71 - 121, a4);
loc_0085C612:
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0085C6B2;
loc_0085C625:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 24))) + (*(unsigned int *)(result + 20)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 24))) + (*(unsigned int *)(result + 20)));
    if (a2 >= = ((unsigned int)(a1))) {
        result = *(unsigned __int64 *)(v_rsp - 71 - 17);
        a3 = *(unsigned __int64 *)(v_rsp - 71 + 111);
        a2 = result;
        v_stack_mF8 = result;
        a1 = 0;
        result = CmpSyncSubKeysAfterDelete(a1, a2, a3, result);
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 140)) & (1)) != 0) goto loc_0085C76A;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_rsp - 71 + 111), v_rsp - 71 - 121, a3, result);
loc_0085C665:
    a4 = 0;
    goto loc_0085C2D5;
loc_0085C66D:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_rsp - 71 + 111), v_rsp - 71 - 121, a3, a4);
    goto loc_0085C141;
loc_0085C677:
    result = HvpGetCellPaged(*(unsigned __int64 *)(v_rsp - 71 + 111), v_rsp - 71 - 121, a3, a4);
    goto loc_0085C461;
loc_0085C681:
    result = HvpGetCellPaged(*(unsigned __int64 *)(v_rsp - 71 + 111), v_rsp - 71 - 121, a3, a4);
    goto loc_0085C492;
loc_0085C68B:
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 16)));
    result = memcpy(result, result + 20, a3, a4);
    a4 = 0;
    goto loc_0085C3DC;
loc_0085C6B2:
    goto loc_0085C625;
loc_0085C6BA:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 4752) = (unsigned int)(result);
    goto loc_0085C2FA;
loc_0085C6C5:
    result = HvpGetCellPaged(0, (unsigned int)(v_stack_mD4), a3, a4);
    goto loc_0085C612;
loc_0085C6CF:
    goto loc_0085C594;
loc_0085C6D9:
    result = HvpReleaseCellFlat(0, (unsigned int)(v_stack_mD4), a3, a4);
    goto loc_0085C045;
loc_0085C6E3:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 140)) & (1)) == 0) goto loc_0085C74F;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_rsp - 71 + 111), (unsigned int)((unsigned int)(v_stack_mD0)), v_rsp - 71 - 73, a4);
loc_0085C6FB:
    if ((*(unsigned int *)(v_rsp - 71 + 127)) == 2) goto loc_0085C809;
    if ((*(unsigned __int64 *)(result + 4)) < (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 97)) + 4))) goto loc_0085C809;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 111) + 140)) & (1)) != 0) goto loc_0085C774;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_rsp - 71 + 111), v_rsp - 71 - 73, v_rsp - 71 - 73, a4);
loc_0085C72B:
    if (((*(unsigned __int8 *)(a4 + 140)) & (1)) != 0) goto loc_0085C77B;
    result = HvpReleaseCellPaged(0, v_rsp - 71 - 105, v_rsp - 71 - 73, a4);
loc_0085C741:
    a4 = 0;
    goto loc_0085C283;
loc_0085C74F:
    result = HvpGetCellPaged(0, 0, v_rsp - 71 - 73, a4);
    goto loc_0085C6FB;
loc_0085C756:
    result = HvpReleaseCellFlat(0, 0, v_rsp - 71 - 73, a4);
    goto loc_0085C4CF;
loc_0085C760:
    result = HvpReleaseCellFlat(0, 0, v_rsp - 71 - 73, a4);
    goto loc_0085C4F3;
loc_0085C76A:
    result = HvpReleaseCellFlat(0, 0, v_rsp - 71 - 73, a4);
    goto loc_0085C665;
loc_0085C774:
    result = HvpReleaseCellFlat(0, 0, v_rsp - 71 - 73, a4);
    goto loc_0085C72B;
loc_0085C77B:
    result = HvpReleaseCellFlat(0, 0, v_rsp - 71 - 73, a4);
    goto loc_0085C741;
loc_0085C782:
loc_0085C785:
loc_0085C788:
    if ((*(unsigned __int64 *)(v_rsp - 71 - 57)) != 0) goto loc_0085C8AB;
loc_0085C797:
    if (0 != 0) goto loc_0085C8CA;
loc_0085C7A0:
    if (0 != 0) goto loc_0085C8E9;
loc_0085C7A9:
    if (*(unsigned __int64 *)(v_rsp - 71 - 17) != 0) goto loc_0085C907;
loc_0085C7B6:
    if (v_stack_mD0 != 0) goto loc_0085C916;
loc_0085C7BF:
loc_0085C7C1:
    v_rsp = (v_rsp) + (224);
    return (unsigned int)((unsigned int)(result));
loc_0085C7DD:
    result = ExAllocatePool2(256, 512, (unsigned int)(0x6E5A6D43ULL), a4);
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 17) = result;
    if (result != 0) goto loc_0085C035;
    goto loc_0085C7C1;
loc_0085C809:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(v_stack_p20, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + v_r14 + v_r14 * 4 * 4 + 4)), a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_0085C788;
loc_0085C84F:
    a3 = 0;
    result = HvpMarkCellDirty(v_stack_p20, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + v_r14 + v_r14 * 4 * 4 + 4)), a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_0085C782;
    goto loc_0085C18D;
loc_0085C877:
    *(unsigned __int16 *)((unsigned int)((unsigned int)(result)) + 52) = (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + v_r14 + v_r14 * 4 * 4 + 4)));
    goto loc_0085C22F;
loc_0085C880:
    *(unsigned int *)((unsigned int)((unsigned int)(result)) + 56) = (unsigned int)(result);
    goto loc_0085C23D;
loc_0085C888:
    goto loc_0085C788;
loc_0085C892:
loc_0085C89C:
loc_0085C8AB:
    result = HvpReleaseCellFlat(0, v_rsp - 71 - 81, a3, a4);
    goto loc_0085C797;
loc_0085C8CA:
    result = HvpReleaseCellFlat(0, v_rsp - 71 - 105, a3, a4);
    goto loc_0085C7A0;
loc_0085C8E9:
    result = HvpReleaseCellFlat(v_stack_p20, v_rsp - 71 - 73, a3, a4);
    goto loc_0085C7A9;
loc_0085C907:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    goto loc_0085C7B6;
loc_0085C916:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mD0, a2, a3, a4);
    goto loc_0085C7BF;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCopySyncTree2(int64_t Arg1, int32_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (224);
    Arg4 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x77))) & (1));
    *(uint32_t *)(local_rsp - 0x47 - 0x5D) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x19) = (uint32_t)(result);
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x7F))) - 1);
    *(uint32_t *)(local_rsp - 0x47 - 0x59) = 0;
    v_stack_mC8 = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x57) = 0;
    Arg3 = (((uint32_t)(result)) <= 1) ? 1 : 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x69) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x65) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x49) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x45) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x51) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x4D) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x79) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x75) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x31) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x2D) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x15) = (uint32_t)(Arg1);
    *(uint64_t *)(local_rsp - 0x47 - 0x11) = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x5F) = (uint8_t)(Arg3);
    *(uint32_t *)(local_rsp - 0x47 - 0x71) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x6D) = 0;
    v_stack_mD0 = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x41) = 0;
    v_stack_mD4 = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x61) = 1;
    *(uint64_t *)(local_rsp - 0x47 - 0x9) = v_xmm0;
    if ((uint8_t)(Arg3) != 0) goto loc_0085C7DD;
loc_0085C035:
    *(uint32_t *)(Arg1 + 0x0 + 0x0 * 4 * 4 + 0x8) = 0;
loc_0085C045:
    if (0 == 0) goto loc_0085C064;
    if (((*(uint8_t *)(arg4 + 0x8C)) & (1)) != 0) goto loc_0085C38F;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 81, Arg3, Arg4);
loc_0085C064:
    if (((*(uint8_t *)(arg4 + 0x8C)) & (1)) == 0) goto loc_0085C32E;
    result = HvpGetCellFlat(0, (uint32_t)(*(uint32_t *)(Arg1 + 0x0 + 0x0 * 4 * 4)), local_rsp - 71 - 81, Arg4);
loc_0085C082:
    *(uint64_t *)(local_rsp - 0x47 - 0x39) = result;
    result = CmpFindSubKeyByNumber(0, result, (uint32_t)(*(uint32_t *)(Arg1 + 0x0 + 0x0 * 4 * 4 + 0x8)), local_rsp - 71 - 89);
    Arg4 = 0;
    if (sign_flag) goto loc_0085C782;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x59)))) == -1) goto loc_0085C2CB;
    if ((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x19))) != 0) goto loc_0085C0CB;
    if (sign_flag) goto loc_0085C2CB;
loc_0085C0CB:
    if ((*(uint8_t *)(local_rsp - 0x47 + 0x5F)) != 0) goto loc_0085C445;
loc_0085C0D5:
    if (((*(uint8_t *)(local_rsp - 0x47 + 0x77)) & (64)) == 0) goto loc_0085C141;
    if (((*(uint8_t *)(arg4 + 0x8C)) & (1)) == 0) goto loc_0085C35C;
    result = HvpGetCellFlat(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x59)))), local_rsp - 71 - 113, Arg4);
loc_0085C0F7:
    if ((((uint8_t)(*(uint8_t *)(result + 0xC))) & (2)) == 0) goto loc_0085C338;
loc_0085C107:
    if (1 > (*(uint32_t *)(local_rsp - 0x47 - 0x61))) goto loc_0085C366;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x0 + 0x0 * 4 * 4 + 0xC))) << (29));
    Arg2 = (uint8_t)((*(uint8_t *)(arg4 + 0x8C)) & (1));
    result = (uint32_t)((result) >> (29));
    if (1 <= ((uint32_t)(result))) goto loc_0085C38B;
    if ((uint8_t)(Arg2) != 0) goto loc_0085C66D;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 113, local_rsp - 71 - 113, Arg4);
loc_0085C141:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x77))) | (4));
    v_stack_mE0 = v_stack_mC8;
    v_stack_mE8 = 2;
    v_stack_mF8 = (uint32_t)(result);
    result = CmpCopyKeyPartial(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x59)))), *(uint64_t *)(local_rsp - 0x47 + 0x6F), (uint32_t)(*(uint32_t *)(Arg1 + 0x0 + 0x0 * 4 * 4 + 0x4)));
    Arg4 = 0;
    if (sign_flag) goto loc_0085C782;
    v_stack_mD8 = 1;
    if (((*(uint8_t *)(Arg1 + 0x0 + 0x0 * 4 * 4 + 0x10)) & (2)) == 0) goto loc_0085C84F;
loc_0085C18D:
    Arg4 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x59))))) >> (31);
    result = CmpAddSubKeyEx(*(uint64_t *)(local_rsp - 0x47 + 0x6F), (uint32_t)(*(uint32_t *)(Arg1 + 0x0 + 0x0 * 4 * 4 + 0x4)), (uint32_t)((uint32_t)((uint32_t)(v_stack_mC8))), (uint32_t)(*(uint32_t *)(result + arg4 * 4 + 0x14)));
    Arg4 = 0;
    if (sign_flag) goto loc_0085C782;
    Arg1 = (uint32_t)((*(uint64_t *)(local_rsp - 0x47 + 0x6F)) | (0xFFFFFFFFULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x1D) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x21) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x29) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x25) = 0;
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x8C)) & (1)) == 0) goto loc_0085C348;
    result = HvpGetCellFlat(*(uint64_t *)(local_rsp - 0x47 + 0x6F), (uint32_t)(*(uint32_t *)(Arg1 + 0x0 + 0x0 * 4 * 4 + 0x4)), local_rsp - 71 - 33, Arg4);
loc_0085C1EA:
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x8C)) & (1)) == 0) goto loc_0085C352;
    result = HvpGetCellFlat(*(uint64_t *)(local_rsp - 0x47 + 0x6F), (uint32_t)((uint32_t)((uint32_t)(v_stack_mC8))), local_rsp - 71 - 41, Arg4);
loc_0085C209:
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(result + 0x48))) + ((uint16_t)((uint16_t)(*(uint16_t *)(result + 0x48)))));
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) { Arg1 = (uint16_t)(*(uint16_t *)(result + 0x48)); }
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x34))))) < ((uint32_t)((uint16_t)(Arg1)))) goto loc_0085C877;
loc_0085C22F:
    if ((*(uint32_t *)(result + 0x38)) < ((uint32_t)(*(uint16_t *)(result + 0x4A)))) goto loc_0085C880;
loc_0085C23D:
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x8C)) & (1)) != 0) goto loc_0085C5D6;
    result = HvpReleaseCellPaged(*(uint64_t *)(local_rsp - 0x47 + 0x6F), local_rsp - 71 - 41, result, Arg4);
loc_0085C256:
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x8C)) & (1)) != 0) goto loc_0085C5E0;
    result = HvpReleaseCellPaged(*(uint64_t *)(local_rsp - 0x47 + 0x6F), local_rsp - 71 - 33, result, Arg4);
loc_0085C26F:
    Arg4 = 0;
    if ((*(uint8_t *)(local_rsp - 0x47 + 0x5F)) != 0) goto loc_0085C416;
loc_0085C27F:
loc_0085C283:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x5D))) + 1);
    *(uint32_t *)(local_rsp - 0x47 - 0x5D) = (uint32_t)(result);
    if (((uint32_t)(result)) >= 512) goto loc_0085C888;
    Arg2 = (uint8_t)((v_stack_mD8) + ((uint8_t)(v_stack_mD8)));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + result + result * 4 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x59)));
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + result + result * 4 * 4 + 0x10)) & (252));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + result + result * 4 * 4 + 0x4) = (uint32_t)((uint32_t)(v_stack_mC8));
    result = (uint8_t)((result) | ((uint8_t)(Arg2)));
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + result + result * 4 * 4 + 0x10) = (uint8_t)(result);
    goto loc_0085C035;
loc_0085C2CB:
    if ((*(uint8_t *)(local_rsp - 0x47 + 0x5F)) != 0) goto loc_0085C5EA;
loc_0085C2D5:
    if (((*(uint8_t *)(Arg1 + 0x0 + 0x0 * 4 * 4 + 0x10)) & (1)) != 0) goto loc_0085C503;
loc_0085C2ED:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_0085C399;
loc_0085C2FA:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(result))) - 1);
    *(uint32_t *)(local_rsp - 0x47 - 0x5D) = (uint32_t)(local_r14);
    if ((*(uint8_t *)(local_rsp - 0x47 + 0x57)) == 0) goto loc_0085C045;
    if (((uint32_t)(local_r14)) != (*(uint32_t *)(local_rsp - 0x47 - 0x15))) goto loc_0085C045;
    *(uint8_t *)(local_rsp - 0x47 + 0x5F) = 1;
    *(uint8_t *)(local_rsp - 0x47 + 0x57) = 0;
    goto loc_0085C045;
loc_0085C32E:
    result = HvpGetCellPaged(local_r14 + local_r14 * 4, (uint32_t)(v_stack_mD4), result, Arg4);
    goto loc_0085C082;
loc_0085C338:
    result = (uint8_t)(~(result));
    Arg1 = (uint32_t)(((uint8_t)(result)) & (1));
    Arg1 = (uint32_t)((Arg1) | (2));
    goto loc_0085C107;
loc_0085C348:
    result = HvpGetCellPaged(Arg1, (uint32_t)(v_stack_mD4), result, Arg4);
    goto loc_0085C1EA;
loc_0085C352:
    result = HvpGetCellPaged(Arg1, (uint32_t)(v_stack_mD4), result, Arg4);
    goto loc_0085C209;
loc_0085C35C:
    result = HvpGetCellPaged(Arg1, (uint32_t)(v_stack_mD4), result, Arg4);
    goto loc_0085C0F7;
loc_0085C366:
loc_0085C374:
    if (((*(uint8_t *)(arg4 + 0x8C)) & (1)) != 0) goto loc_0085C6D9;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 113, result, Arg4);
    goto loc_0085C045;
loc_0085C38B:
    goto loc_0085C374;
loc_0085C38F:
    result = HvpReleaseCellFlat(0, local_rsp - 71 - 113, result, Arg4);
    goto loc_0085C064;
loc_0085C399:
    if (((uint32_t)(local_rsp - 71 - 113)) == -1) goto loc_0085C89C;
    Arg2 = (uint32_t)((local_rsp - 71 - 113) - 1);
    v_stack_mD4 = Arg2;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_rsp - 0x47 - 0x71)) + (uint32_t)((uint32_t)(local_rsp - 0x47 - 0x71)) * 4 * 4 + *(uint64_t *)(local_rsp - 0x47 - 0x39) * 1 + 0xC))) ^ (*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x39) + 0xC)));
    if ((((uint8_t)(Arg1)) & (7)) != 0) goto loc_0085C68B;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F)) = v_xmm0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_rsp - 0x47 - 0x71)) + (uint32_t)((uint32_t)(local_rsp - 0x47 - 0x71)) * 4 * 4 + *(uint64_t *)(local_rsp - 0x47 - 0x39) * 1 + 0x10)));
loc_0085C3DC:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0xC))) << (29));
    result = (uint32_t)((result) >> (29));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61)))) != ((uint32_t)(result))) goto loc_0085C2FA;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61))) + 1);
    *(uint32_t *)(local_rsp - 0x47 - 0x61) = (uint32_t)(local_rsi);
    v_stack_mD4 = Arg2;
    if (((uint32_t)(local_rsi)) == 2) goto loc_0085C6BA;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x1294) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x118)));
    goto loc_0085C2FA;
loc_0085C416:
    if ((*(uint8_t *)(local_rsp - 0x47 + 0x57)) == 0) goto loc_0085C27F;
    result = CmpMarkKeyParentDirty(*(uint64_t *)(local_rsp - 0x47 + 0x6F), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 - 0x39))), (uint32_t)((uint32_t)(local_rsp - 71 - 113)) + (uint32_t)((uint32_t)(local_rsp - 71 - 113)) * 4 * 4, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_0085C785;
    *(uint32_t *)(local_rsp - 0x47 - 0x15) = 1;
    *(uint8_t *)(local_rsp - 0x47 + 0x5F) = 0;
    goto loc_0085C27F;
loc_0085C445:
    if (((*(uint8_t *)(arg4 + 0x8C)) & (1)) == 0) goto loc_0085C677;
    result = HvpGetCellFlat(0, (uint32_t)((uint32_t)(local_rsi)), local_rsp - 71 - 105, Arg4);
loc_0085C461:
    result = CmpInitializeKeyNameString(result, local_rsp - 71 - 9, *(uint64_t *)(local_rsp - 0x47 - 0x11), Arg4);
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x8C)) & (1)) == 0) goto loc_0085C681;
    result = HvpGetCellFlat(*(uint64_t *)(local_rsp - 0x47 + 0x6F), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + local_r14 + local_r14 * 4 * 4 + 0x4)), local_rsp - 71 - 49, Arg4);
loc_0085C492:
    local_rdi = 0;
    v_stack_mC8 = 0;
    result = CmpFindSubKeyByNameWithStatus(*(uint64_t *)(local_rsp - 0x47 + 0x6F), result, local_rsp - 71 - 9, v_stack_mC8);
    v_stack_mC8 = (uint32_t)((uint32_t)(v_stack_mC8));
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x8C)) & (1)) != 0) goto loc_0085C756;
    result = HvpReleaseCellPaged(*(uint64_t *)(local_rsp - 0x47 + 0x6F), local_rsp - 71 - 49, local_rsp - 71 - 9, v_stack_mC8);
loc_0085C4CF:
    if (((uint32_t)((uint32_t)(v_stack_mC8))) != -1) goto loc_0085C6E3;
    if (((*(uint8_t *)(arg4 + 0x8C)) & (1)) != 0) goto loc_0085C760;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 105, local_rsp - 71 - 9, v_stack_mC8);
loc_0085C4F3:
    *(uint8_t *)(local_rsp - 0x47 + 0x57) = 1;
    goto loc_0085C0D5;
loc_0085C503:
    Arg2 = (uint32_t)((local_rsp - 71 - 105) + 1);
    v_stack_mD4 = Arg2;
    if (Arg2 < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x41))))) goto loc_0085C6CF;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x41))))) >> (1));
    Arg2 = 1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x41)) + 1)) <= ((uint32_t)(Arg3 + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x41)) * 1))) { Arg2 = Arg3; }
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x41)))));
    Arg2 = (Arg2 + Arg2 * 4) << (2);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x20204D43ULL), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x41)));
    Arg4 = 0;
    if (result == 0) goto loc_0085C892;
    Arg3 = ((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x41)) + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x41)) * 4) << (2);
    result = memcpy(result, v_stack_mD0, Arg3, Arg4);
    if (v_stack_mD0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mD0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_mD0 = result;
    *(uint32_t *)(local_rsp - 0x47 - 0x41) = (uint32_t)((uint32_t)(Arg2));
loc_0085C594:
    Arg4 = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + local_r14 + local_r14 * 4 * 4 + 0x8) = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61))))) ^ (*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + local_r14 + local_r14 * 4 * 4 + 0xC)));
    result = (uint32_t)((result) & (0xFFFFFFF8ULL));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61)))));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + local_r14 + local_r14 * 4 * 4 + 0xC) = (uint32_t)(result);
    *(uint64_t *)(result + (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))) + (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))) * 4 * 4) = v_xmm0;
    *(uint32_t *)(result + (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))) + (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))) * 4 * 4 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + local_r14 + local_r14 * 4 * 4 + 0x10)));
    goto loc_0085C2ED;
loc_0085C5D6:
    result = HvpReleaseCellFlat((uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))) + (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))) * 4, (uint32_t)(v_stack_mD4), Arg3, Arg4);
    goto loc_0085C256;
loc_0085C5E0:
    result = HvpReleaseCellFlat((uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))) + (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))) * 4, (uint32_t)(v_stack_mD4), Arg3, Arg4);
    goto loc_0085C26F;
loc_0085C5EA:
    if ((*(uint32_t *)(local_rsp - 0x47 + 0x7F)) == 2) goto loc_0085C2D5;
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x8C)) & (1)) == 0) goto loc_0085C6C5;
    result = HvpGetCellFlat(*(uint64_t *)(local_rsp - 0x47 + 0x6F), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + local_r14 + local_r14 * 4 * 4 + 0x4)), local_rsp - 71 - 121, Arg4);
loc_0085C612:
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_0085C6B2;
loc_0085C625:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x18))) + (*(uint32_t *)(result + 0x14)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x18))) + (*(uint32_t *)(result + 0x14)));
    if (Arg2 >= = ((uint32_t)(Arg1))) {
        result = *(uint64_t *)(local_rsp - 0x47 - 0x11);
        Arg3 = *(uint64_t *)(local_rsp - 0x47 + 0x6F);
        Arg2 = result;
        v_stack_mF8 = result;
        Arg1 = 0;
        result = CmpSyncSubKeysAfterDelete(Arg1, Arg2, Arg3, result);
    }
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x8C)) & (1)) != 0) goto loc_0085C76A;
    result = HvpReleaseCellPaged(*(uint64_t *)(local_rsp - 0x47 + 0x6F), local_rsp - 71 - 121, Arg3, result);
loc_0085C665:
    Arg4 = 0;
    goto loc_0085C2D5;
loc_0085C66D:
    result = HvpReleaseCellFlat(*(uint64_t *)(local_rsp - 0x47 + 0x6F), local_rsp - 71 - 121, Arg3, Arg4);
    goto loc_0085C141;
loc_0085C677:
    result = HvpGetCellPaged(*(uint64_t *)(local_rsp - 0x47 + 0x6F), local_rsp - 71 - 121, Arg3, Arg4);
    goto loc_0085C461;
loc_0085C681:
    result = HvpGetCellPaged(*(uint64_t *)(local_rsp - 0x47 + 0x6F), local_rsp - 71 - 121, Arg3, Arg4);
    goto loc_0085C492;
loc_0085C68B:
    *(uint64_t *)(result) = v_xmm0;
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)));
    result = memcpy(result, result + 20, Arg3, Arg4);
    Arg4 = 0;
    goto loc_0085C3DC;
loc_0085C6B2:
    goto loc_0085C625;
loc_0085C6BA:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x1290) = (uint32_t)(result);
    goto loc_0085C2FA;
loc_0085C6C5:
    result = HvpGetCellPaged(0, (uint32_t)(v_stack_mD4), Arg3, Arg4);
    goto loc_0085C612;
loc_0085C6CF:
    goto loc_0085C594;
loc_0085C6D9:
    result = HvpReleaseCellFlat(0, (uint32_t)(v_stack_mD4), Arg3, Arg4);
    goto loc_0085C045;
loc_0085C6E3:
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x8C)) & (1)) == 0) goto loc_0085C74F;
    result = HvpGetCellFlat(*(uint64_t *)(local_rsp - 0x47 + 0x6F), (uint32_t)((uint32_t)(v_stack_mD0)), local_rsp - 71 - 73, Arg4);
loc_0085C6FB:
    if ((*(uint32_t *)(local_rsp - 0x47 + 0x7F)) == 2) goto loc_0085C809;
    if ((*(uint64_t *)(result + 0x4)) < (*(uint64_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x61)) + 0x4))) goto loc_0085C809;
    if (((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x6F) + 0x8C)) & (1)) != 0) goto loc_0085C774;
    result = HvpReleaseCellPaged(*(uint64_t *)(local_rsp - 0x47 + 0x6F), local_rsp - 71 - 73, local_rsp - 71 - 73, Arg4);
loc_0085C72B:
    if (((*(uint8_t *)(arg4 + 0x8C)) & (1)) != 0) goto loc_0085C77B;
    result = HvpReleaseCellPaged(0, local_rsp - 71 - 105, local_rsp - 71 - 73, Arg4);
loc_0085C741:
    Arg4 = 0;
    goto loc_0085C283;
loc_0085C74F:
    result = HvpGetCellPaged(0, 0, local_rsp - 71 - 73, Arg4);
    goto loc_0085C6FB;
loc_0085C756:
    result = HvpReleaseCellFlat(0, 0, local_rsp - 71 - 73, Arg4);
    goto loc_0085C4CF;
loc_0085C760:
    result = HvpReleaseCellFlat(0, 0, local_rsp - 71 - 73, Arg4);
    goto loc_0085C4F3;
loc_0085C76A:
    result = HvpReleaseCellFlat(0, 0, local_rsp - 71 - 73, Arg4);
    goto loc_0085C665;
loc_0085C774:
    result = HvpReleaseCellFlat(0, 0, local_rsp - 71 - 73, Arg4);
    goto loc_0085C72B;
loc_0085C77B:
    result = HvpReleaseCellFlat(0, 0, local_rsp - 71 - 73, Arg4);
    goto loc_0085C741;
loc_0085C782:
loc_0085C785:
loc_0085C788:
    if ((*(uint64_t *)(local_rsp - 0x47 - 0x39)) != 0) goto loc_0085C8AB;
loc_0085C797:
    if (0 != 0) goto loc_0085C8CA;
loc_0085C7A0:
    if (0 != 0) goto loc_0085C8E9;
loc_0085C7A9:
    if (*(uint64_t *)(local_rsp - 0x47 - 0x11) != 0) goto loc_0085C907;
loc_0085C7B6:
    if (v_stack_mD0 != 0) goto loc_0085C916;
loc_0085C7BF:
loc_0085C7C1:
    local_rsp = (local_rsp) + (224);
    return (uint32_t)((uint32_t)(result));
loc_0085C7DD:
    result = ExAllocatePool2(256, 512, (uint32_t)(0x6E5A6D43ULL), Arg4);
    Arg4 = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x11) = result;
    if (result != 0) goto loc_0085C035;
    goto loc_0085C7C1;
loc_0085C809:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(v_stack_p20, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + local_r14 + local_r14 * 4 * 4 + 0x4)), Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_0085C788;
loc_0085C84F:
    Arg3 = 0;
    result = HvpMarkCellDirty(v_stack_p20, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + local_r14 + local_r14 * 4 * 4 + 0x4)), Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_0085C782;
    goto loc_0085C18D;
loc_0085C877:
    *(uint16_t *)((uint32_t)((uint32_t)(result)) + 0x34) = (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + local_r14 + local_r14 * 4 * 4 + 0x4)));
    goto loc_0085C22F;
loc_0085C880:
    *(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x38) = (uint32_t)(result);
    goto loc_0085C23D;
loc_0085C888:
    goto loc_0085C788;
loc_0085C892:
loc_0085C89C:
loc_0085C8AB:
    result = HvpReleaseCellFlat(0, local_rsp - 71 - 81, Arg3, Arg4);
    goto loc_0085C797;
loc_0085C8CA:
    result = HvpReleaseCellFlat(0, local_rsp - 71 - 105, Arg3, Arg4);
    goto loc_0085C7A0;
loc_0085C8E9:
    result = HvpReleaseCellFlat(v_stack_p20, local_rsp - 71 - 73, Arg3, Arg4);
    goto loc_0085C7A9;
loc_0085C907:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    goto loc_0085C7B6;
loc_0085C916:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mD0, Arg2, Arg3, Arg4);
    goto loc_0085C7BF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x8C` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085BF78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
