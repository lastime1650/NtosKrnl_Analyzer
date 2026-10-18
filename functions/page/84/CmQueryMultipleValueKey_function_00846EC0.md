# CmQueryMultipleValueKey

- RVA: `0x00846EC0`–`0x00847609` (길이 `1,865` bytes)
- VA: `0x0000000140846EC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00069294`
- 디코드: `406`개 명령, `1,865/1,865` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00846F57` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x00846F96` → [CmpLockTwoKcbsShared](CmpLockTwoKcbsShared_function_008485B4.md) (function, `0x008485B4`)
- `0x00846FA1` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x00846FC6` → [HvLockHiveFlusherShared](HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x00846FF4` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00847014` → [CmpUpdateKeyNodeAccessBits](CmpUpdateKeyNodeAccessBits_function_0084864C.md) (function, `0x0084864C`)
- `0x0084701C` → [HvUnlockHiveFlusherShared](HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x008470E3` → [CmpFindNameInListWithStatus](CmpFindNameInListWithStatus_function_00846B80.md) (function, `0x00846B80`)
- `0x00847111` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008471D1` → [CmpGetValueData](../85/CmpGetValueData_function_00856DB0.md) (function, `0x00856DB0`)
- `0x008471FD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00847296` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008472CE` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008472EE` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0084733E` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00847349` → [CmpUnlockTwoKcbs](CmpUnlockTwoKcbs_function_0084869C.md) (function, `0x0084869C`)
- `0x0084734E` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00847394` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x008473DD` → [CmQueryMultipleValueForLayeredKey](../A8/CmQueryMultipleValueForLayeredKey_function_00A8DE80.md) (function, `0x00A8DE80`)
- `0x008473E4` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00847402` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x0084740C` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x0084741C` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00847429` → [CmpTransSearchAddTransFromKeyBody](../87/CmpTransSearchAddTransFromKeyBody_function_008736B8.md) (function, `0x008736B8`)
- `0x00847442` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0084744C` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00847456` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00847475` → [CmpUnlockTwoKcbs](CmpUnlockTwoKcbs_function_0084869C.md) (function, `0x0084869C`)
- `0x0084747A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x0084748A` → [HvUnlockHiveFlusherShared](HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x00847495` → [CmpUnlockTwoKcbs](CmpUnlockTwoKcbs_function_0084869C.md) (function, `0x0084869C`)
- `0x0084749A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x008474B8` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008474D6` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x00847528` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00847568` → [CmpFindValueByName](CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00847592` → [CmpFindNameInList](CmpFindNameInList_function_00844E54.md) (function, `0x00844E54`)
- `0x008475B4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008475DB` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008475FF` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)

### Direct callers
- [NtQueryMultipleValueKey](../8B/NtQueryMultipleValueKey_function_008B13B0.md) at `0x008B175C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x00846F57` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x00846FA1` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x008471FD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0084734E` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x008473E4` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00847402` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x0084740C` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x0084741C` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x0084747A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x0084749A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x008474B8` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008474D6` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x008475B4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00847522` → [sub_00B16338](../B1/Unknown_function_00B16338.md) (`tail-transfer`)
  - `0x0084752E` → [sub_00B16338 + 0x5](../B1/Unknown_function_00B16338.md) (`tail-transfer`)
  - `0x0084755C` → [sub_00B16338 + 0x67](../B1/Unknown_function_00B16338.md) (`tail-transfer`)
  - `0x00847577` → [sub_00B16338 + 0x90](../B1/Unknown_function_00B16338.md) (`tail-transfer`)
  - `0x008475D5` → [sub_00B16338 + 0x9A](../B1/Unknown_function_00B16338.md) (`tail-transfer`)
  - `0x008475F9` → [sub_00B16338 + 0xA5](../B1/Unknown_function_00B16338.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00846EC0  48 8B C4                        mov rax, rsp
00846EC3  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00846EC7  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00846ECB  53                              push rbx
00846ECC  56                              push rsi
00846ECD  57                              push rdi
00846ECE  41 54                           push r12
00846ED0  41 55                           push r13
00846ED2  41 56                           push r14
00846ED4  41 57                           push r15
00846ED6  48 81 EC F0 00 00 00            sub rsp, 0xf0
00846EDD  4C 8B FA                        mov r15, rdx
00846EE0  48 8B F9                        mov rdi, rcx
00846EE3  33 DB                           xor ebx, ebx
00846EE5  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
00846EED  44 8B E3                        mov r12d, ebx
00846EF0  48 89 9C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rbx
00846EF8  83 C9 FF                        or ecx, 0xffffffff
00846EFB  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00846EFF  89 5C 24 64                     mov dword ptr [rsp + 0x64], ebx
00846F03  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00846F07  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
00846F0B  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
00846F0F  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
00846F13  89 5C 24 6C                     mov dword ptr [rsp + 0x6c], ebx
00846F17  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
00846F1F  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
00846F23  89 5C 24 7C                     mov dword ptr [rsp + 0x7c], ebx
00846F27  44 8B EB                        mov r13d, ebx
00846F2A  48 89 9C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rbx
00846F32  8B F3                           mov esi, ebx
00846F34  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00846F39  88 5C 24 70                     mov byte ptr [rsp + 0x70], bl
00846F3D  88 5C 24 54                     mov byte ptr [rsp + 0x54], bl
00846F41  48 89 98 70 FF FF FF            mov qword ptr [rax - 0x90], rbx
00846F48  88 58 08                        mov byte ptr [rax + 8], bl
00846F4B  89 88 60 FF FF FF               mov dword ptr [rax - 0xa0], ecx
00846F51  89 98 64 FF FF FF               mov dword ptr [rax - 0x9c], ebx
00846F57  E8 D8 2B 38 00                  call 0x140bc9b34
00846F5C  4C 8B 77 08                     mov r14, qword ptr [rdi + 8]
00846F60  4C 89 B4 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r14
00846F68  66 41 39 5E 42                  cmp word ptr [r14 + 0x42], bx
00846F6D  0F 85 35 04 00 00               jne 0x1408473a8
00846F73  48 39 5F 38                     cmp qword ptr [rdi + 0x38], rbx
00846F77  0F 85 82 04 00 00               jne 0x1408473ff
00846F7D  48 39 5F 40                     cmp qword ptr [rdi + 0x40], rbx
00846F81  0F 85 78 04 00 00               jne 0x1408473ff
00846F87  4D 85 FF                        test r15, r15
00846F8A  0F 85 2F 05 00 00               jne 0x1408474bf
00846F90  49 8B D6                        mov rdx, r14
00846F93  49 8B CD                        mov rcx, r13
00846F96  E8 19 16 00 00                  call 0x1408485b4
00846F9B  48 8B D6                        mov rdx, rsi
00846F9E  48 8B CF                        mov rcx, rdi
00846FA1  E8 DA 24 38 00                  call 0x140bc9480
00846FA6  84 C0                           test al, al
00846FA8  0F 85 B2 04 00 00               jne 0x140847460
00846FAE  4D 85 FF                        test r15, r15
00846FB1  0F 85 19 05 00 00               jne 0x1408474d0
00846FB7  4D 8B 7E 20                     mov r15, qword ptr [r14 + 0x20]
00846FBB  4C 89 BC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r15
00846FC3  49 8B CF                        mov rcx, r15
00846FC6  E8 91 89 00 00                  call 0x14084f95c
00846FCB  41 8B 56 28                     mov edx, dword ptr [r14 + 0x28]
00846FCF  49 8D 87 8C 00 00 00            lea rax, [r15 + 0x8c]
00846FD6  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
00846FDE  BF 01 00 00 00                  mov edi, 1
00846FE3  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00846FE8  49 8B CF                        mov rcx, r15
00846FEB  40 84 38                        test byte ptr [rax], dil
00846FEE  0F 84 A0 03 00 00               je 0x140847394
00846FF4  E8 67 DC 00 00                  call 0x140854c60
00846FF9  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00847001  49 8B CF                        mov rcx, r15
00847004  48 85 C0                        test rax, rax
00847007  0F 84 7D 04 00 00               je 0x14084748a
0084700D  45 8B 46 28                     mov r8d, dword ptr [r14 + 0x28]
00847011  48 8B D0                        mov rdx, rax
00847014  E8 33 16 00 00                  call 0x14084864c
00847019  49 8B CF                        mov rcx, r15
0084701C  E8 17 17 00 00                  call 0x140848738
00847021  48 85 F6                        test rsi, rsi
00847024  0F 85 C2 04 00 00               jne 0x1408474ec
0084702A  4D 85 ED                        test r13, r13
0084702D  0F 85 D3 04 00 00               jne 0x140847506
00847033  4C 8B CB                        mov r9, rbx
00847036  44 8B 54 24 54                  mov r10d, dword ptr [rsp + 0x54]
0084703B  8B F3                           mov esi, ebx
0084703D  8B CB                           mov ecx, ebx
0084703F  89 8C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ecx
00847046  3B 8C 24 48 01 00 00            cmp ecx, dword ptr [rsp + 0x148]
0084704D  0F 83 AA 02 00 00               jae 0x1408472fd
00847053  8B C1                           mov eax, ecx
00847055  48 8D 04 40                     lea rax, [rax + rax*2]
00847059  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00847061  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
00847069  4C 8B 04 C1                     mov r8, qword ptr [rcx + rax*8]
0084706D  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00847072  41 0F B7 08                     movzx ecx, word ptr [r8]
00847076  66 85 C9                        test cx, cx
00847079  74 15                           je 0x140847090
0084707B  49 8B 50 08                     mov rdx, qword ptr [r8 + 8]
0084707F  0F B7 C1                        movzx eax, cx
00847082  48 D1 E8                        shr rax, 1
00847085  66 39 5C 42 FE                  cmp word ptr [rdx + rax*2 - 2], bx
0084708A  0F 84 A3 04 00 00               je 0x140847533
00847090  83 C9 FF                        or ecx, 0xffffffff
00847093  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
00847097  89 4C 24 4C                     mov dword ptr [rsp + 0x4c], ecx
0084709B  4D 85 ED                        test r13, r13
0084709E  0F 85 A2 04 00 00               jne 0x140847546
008470A4  83 F9 FF                        cmp ecx, -1
008470A7  75 50                           jne 0x1408470f9
008470A9  4D 8B E7                        mov r12, r15
008470AC  4C 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r15
008470B4  45 33 C9                        xor r9d, r9d
008470B7  49 8B CF                        mov rcx, r15
008470BA  38 5C 24 70                     cmp byte ptr [rsp + 0x70], bl
008470BE  0F 85 B8 04 00 00               jne 0x14084757c
008470C4  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
008470C8  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
008470D0  48 83 C2 24                     add rdx, 0x24
008470D4  48 8D 44 24 44                  lea rax, [rsp + 0x44]
008470D9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008470DE  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
008470E3  E8 98 FA FF FF                  call 0x140846b80
008470E8  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
008470EC  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
008470F0  83 F9 FF                        cmp ecx, -1
008470F3  0F 84 FF 01 00 00               je 0x1408472f8
008470F9  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
008470FE  8B D1                           mov edx, ecx
00847100  49 8B CC                        mov rcx, r12
00847103  41 84 BC 24 8C 00 00 00         test byte ptr [r12 + 0x8c], dil
0084710B  0F 84 DD 01 00 00               je 0x1408472ee
00847111  E8 4A DB 00 00                  call 0x140854c60
00847116  48 8B C8                        mov rcx, rax
00847119  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0084711E  48 85 C0                        test rax, rax
00847121  0F 84 79 04 00 00               je 0x1408475a0
00847127  8B 40 04                        mov eax, dword ptr [rax + 4]
0084712A  8D 90 00 00 00 80               lea edx, [rax - 0x80000000]
00847130  3D 00 00 00 80                  cmp eax, 0x80000000
00847135  0F 42 D0                        cmovb edx, eax
00847138  89 54 24 4C                     mov dword ptr [rsp + 0x4c], edx
0084713C  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
00847141  41 83 C0 03                     add r8d, 3
00847145  B8 FC FF FF FF                  mov eax, 0xfffffffc
0084714A  44 23 C0                        and r8d, eax
0084714D  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
00847152  44 89 84 24 A4 00 00 00         mov dword ptr [rsp + 0xa4], r8d
0084715A  44 8B 54 24 50                  mov r10d, dword ptr [rsp + 0x50]
0084715F  41 83 C2 03                     add r10d, 3
00847163  44 23 D0                        and r10d, eax
00847166  44 89 54 24 50                  mov dword ptr [rsp + 0x50], r10d
0084716B  44 89 94 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r10d
00847173  42 8D 04 02                     lea eax, [rdx + r8]
00847177  4C 8B 8C 24 58 01 00 00         mov r9, qword ptr [rsp + 0x158]
0084717F  41 3B 01                        cmp eax, dword ptr [r9]
00847182  0F 87 16 02 00 00               ja 0x14084739e
00847188  41 3B C0                        cmp eax, r8d
0084718B  0F 82 0D 02 00 00               jb 0x14084739e
00847191  38 5C 24 40                     cmp byte ptr [rsp + 0x40], bl
00847195  0F 85 03 02 00 00               jne 0x14084739e
0084719B  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
008471A3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008471A8  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
008471B0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008471B5  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
008471BD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008471C2  4C 8D 4C 24 4C                  lea r9, [rsp + 0x4c]
008471C7  4C 8B C1                        mov r8, rcx
008471CA  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
008471CE  49 8B CC                        mov rcx, r12
008471D1  E8 DA FB 00 00                  call 0x140856db0
008471D6  84 C0                           test al, al
008471D8  0F 84 12 02 00 00               je 0x1408473f0
008471DE  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
008471E2  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
008471E6  44 8B C0                        mov r8d, eax
008471E9  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
008471ED  48 03 8C 24 50 01 00 00         add rcx, qword ptr [rsp + 0x150]
008471F5  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
008471FD  E8 3E F6 E7 FF                  call 0x1406c6840
00847202  EB 40                           jmp 0x140847244
00847204  8B F0                           mov esi, eax
00847206  33 DB                           xor ebx, ebx
00847208  8D 7B 01                        lea edi, [rbx + 1]
0084720B  4C 8B BC 24 D8 00 00 00         mov r15, qword ptr [rsp + 0xd8]
00847213  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
0084721B  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00847220  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
00847228  8B 84 24 A4 00 00 00            mov eax, dword ptr [rsp + 0xa4]
0084722F  4C 8B B4 24 E0 00 00 00         mov r14, qword ptr [rsp + 0xe0]
00847237  4C 8B AC 24 C0 00 00 00         mov r13, qword ptr [rsp + 0xc0]
0084723F  E9 C5 00 00 00                  jmp 0x140847309
00847244  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00847249  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0084724C  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00847254  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
0084725C  89 44 CA 10                     mov dword ptr [rdx + rcx*8 + 0x10], eax
00847260  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
00847264  89 44 CA 08                     mov dword ptr [rdx + rcx*8 + 8], eax
00847268  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0084726C  89 44 CA 0C                     mov dword ptr [rdx + rcx*8 + 0xc], eax
00847270  38 9C 24 30 01 00 00            cmp byte ptr [rsp + 0x130], bl
00847277  0F 85 2D 03 00 00               jne 0x1408475aa
0084727D  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
00847285  49 8B CC                        mov rcx, r12
00847288  41 84 BC 24 8C 00 00 00         test byte ptr [r12 + 0x8c], dil
00847290  0F 85 B6 01 00 00               jne 0x14084744c
00847296  E8 A5 EC 00 00                  call 0x140855f40
0084729B  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
008472A3  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
008472A7  01 54 24 48                     add dword ptr [rsp + 0x48], edx
008472AB  44 8B 54 24 50                  mov r10d, dword ptr [rsp + 0x50]
008472B0  44 03 D2                        add r10d, edx
008472B3  44 89 54 24 50                  mov dword ptr [rsp + 0x50], r10d
008472B8  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
008472BD  49 8B CC                        mov rcx, r12
008472C0  41 84 BC 24 8C 00 00 00         test byte ptr [r12 + 0x8c], dil
008472C8  0F 85 74 01 00 00               jne 0x140847442
008472CE  E8 6D EC 00 00                  call 0x140855f40
008472D3  8B 8C 24 80 00 00 00            mov ecx, dword ptr [rsp + 0x80]
008472DA  03 CF                           add ecx, edi
008472DC  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
008472E4  44 8B 54 24 54                  mov r10d, dword ptr [rsp + 0x54]
008472E9  E9 51 FD FF FF                  jmp 0x14084703f
008472EE  E8 BD D9 00 00                  call 0x140854cb0
008472F3  E9 1E FE FF FF                  jmp 0x140847116
008472F8  BE 34 00 00 C0                  mov esi, 0xc0000034
008472FD  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
00847302  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
00847306  48 8B CB                        mov rcx, rbx
00847309  85 F6                           test esi, esi
0084730B  79 5C                           jns 0x140847369
0084730D  48 85 C9                        test rcx, rcx
00847310  0F 85 AF 02 00 00               jne 0x1408475c5
00847316  48 83 BC 24 90 00 00 00 00      cmp qword ptr [rsp + 0x90], 0
0084731F  0F 85 C0 02 00 00               jne 0x1408475e5
00847325  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
0084732D  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00847332  49 8B CF                        mov rcx, r15
00847335  40 84 38                        test byte ptr [rax], dil
00847338  0F 85 18 01 00 00               jne 0x140847456
0084733E  E8 FD EB 00 00                  call 0x140855f40
00847343  49 8B D6                        mov rdx, r14
00847346  49 8B CD                        mov rcx, r13
00847349  E8 4E 13 00 00                  call 0x14084869c
0084734E  E8 31 27 38 00                  call 0x140bc9a84
00847353  8B C6                           mov eax, esi
00847355  48 81 C4 F0 00 00 00            add rsp, 0xf0
0084735C  41 5F                           pop r15
0084735E  41 5E                           pop r14
00847360  41 5D                           pop r13
00847362  41 5C                           pop r12
00847364  5F                              pop rdi
00847365  5E                              pop rsi
00847366  5B                              pop rbx
00847367  C3                              ret
00847368  CC                              int3
00847369  BA 05 00 00 80                  mov edx, 0x80000005
0084736E  38 5C 24 40                     cmp byte ptr [rsp + 0x40], bl
00847372  0F 45 F2                        cmovne esi, edx
00847375  48 8B 94 24 58 01 00 00         mov rdx, qword ptr [rsp + 0x158]
0084737D  89 02                           mov dword ptr [rdx], eax
0084737F  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
00847387  48 85 C0                        test rax, rax
0084738A  74 81                           je 0x14084730d
0084738C  44 89 00                        mov dword ptr [rax], r8d
0084738F  E9 79 FF FF FF                  jmp 0x14084730d
00847394  E8 17 D9 00 00                  call 0x140854cb0
00847399  E9 5B FC FF FF                  jmp 0x140846ff9
0084739E  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
008473A3  E9 08 FF FF FF                  jmp 0x1408472b0
008473A8  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
008473B0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008473B5  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
008473BD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008473C2  4C 8B 8C 24 50 01 00 00         mov r9, qword ptr [rsp + 0x150]
008473CA  44 8B 84 24 48 01 00 00         mov r8d, dword ptr [rsp + 0x148]
008473D2  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
008473DA  48 8B CF                        mov rcx, rdi
008473DD  E8 9E 6A 24 00                  call 0x140a8de80
008473E2  8B D8                           mov ebx, eax
008473E4  E8 9B 26 38 00                  call 0x140bc9a84
008473E9  8B C3                           mov eax, ebx
008473EB  E9 65 FF FF FF                  jmp 0x140847355
008473F0  BE 9A 00 00 C0                  mov esi, 0xc000009a
008473F5  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008473FA  E9 0E FF FF FF                  jmp 0x14084730d
008473FF  49 8B CE                        mov rcx, r14
00847402  E8 15 26 38 00                  call 0x140bc9a1c
00847407  33 D2                           xor edx, edx
00847409  48 8B CF                        mov rcx, rdi
0084740C  E8 6F 20 38 00                  call 0x140bc9480
00847411  49 8B CE                        mov rcx, r14
00847414  84 C0                           test al, al
00847416  0F 85 8D 00 00 00               jne 0x1408474a9
0084741C  E8 9F 1E 38 00                  call 0x140bc92c0
00847421  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00847426  48 8B CF                        mov rcx, rdi
00847429  E8 8A C2 02 00                  call 0x1408736b8
0084742E  8B F0                           mov esi, eax
00847430  85 C0                           test eax, eax
00847432  0F 88 16 FF FF FF               js 0x14084734e
00847438  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0084743D  E9 45 FB FF FF                  jmp 0x140846f87
00847442  E8 D9 57 01 00                  call 0x14085cc20
00847447  E9 87 FE FF FF                  jmp 0x1408472d3
0084744C  E8 CF 57 01 00                  call 0x14085cc20
00847451  E9 45 FE FF FF                  jmp 0x14084729b
00847456  E8 C5 57 01 00                  call 0x14085cc20
0084745B  E9 E3 FE FF FF                  jmp 0x140847343
00847460  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00847463  24 01                           and al, 1
00847465  F6 D8                           neg al
00847467  1B DB                           sbb ebx, ebx
00847469  81 E3 A9 02 00 00               and ebx, 0x2a9
0084746F  49 8B D6                        mov rdx, r14
00847472  49 8B CD                        mov rcx, r13
00847475  E8 22 12 00 00                  call 0x14084869c
0084747A  E8 05 26 38 00                  call 0x140bc9a84
0084747F  8D 83 7C 01 00 C0               lea eax, [rbx - 0x3ffffe84]
00847485  E9 CB FE FF FF                  jmp 0x140847355
0084748A  E8 A9 12 00 00                  call 0x140848738
0084748F  49 8B D6                        mov rdx, r14
00847492  49 8B CD                        mov rcx, r13
00847495  E8 02 12 00 00                  call 0x14084869c
0084749A  E8 E5 25 38 00                  call 0x140bc9a84
0084749F  B8 9A 00 00 C0                  mov eax, 0xc000009a
008474A4  E9 AC FE FF FF                  jmp 0x140847355
008474A9  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
008474AC  24 01                           and al, 1
008474AE  F6 D8                           neg al
008474B0  1B DB                           sbb ebx, ebx
008474B2  81 E3 A9 02 00 00               and ebx, 0x2a9
008474B8  E8 03 1E 38 00                  call 0x140bc92c0
008474BD  EB BB                           jmp 0x14084747a
008474BF  4D 8B 6F 08                     mov r13, qword ptr [r15 + 8]
008474C3  4C 89 AC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r13
008474CB  E9 C0 FA FF FF                  jmp 0x140846f90
008474D0  48 8B D6                        mov rdx, rsi
008474D3  49 8B CF                        mov rcx, r15
008474D6  E8 A5 1F 38 00                  call 0x140bc9480
008474DB  84 C0                           test al, al
008474DD  0F 84 D4 FA FF FF               je 0x140846fb7
008474E3  41 8B 47 30                     mov eax, dword ptr [r15 + 0x30]
008474E7  E9 77 FF FF FF                  jmp 0x140847463
008474EC  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
008474F0  0F B6 C0                        movzx eax, al
008474F3  49 39 B6 20 01 00 00            cmp qword ptr [r14 + 0x120], rsi
008474FA  0F 44 C7                        cmove eax, edi
008474FD  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00847501  E9 24 FB FF FF                  jmp 0x14084702a
00847506  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
0084750A  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
00847512  41 8B 55 28                     mov edx, dword ptr [r13 + 0x28]
00847516  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
0084751B  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
00847522  0F 84 10 EE 2C 00               je 0x140b16338
00847528  E8 33 D7 00 00                  call 0x140854c60
0084752D  90                              nop
0084752E  E9 0A EE 2C 00                  jmp 0x140b1633d
00847533  66 83 E9 02                     sub cx, 2
00847537  66 41 89 08                     mov word ptr [r8], cx
0084753B  0F 85 3E FB FF FF               jne 0x14084707f
00847541  E9 4A FB FF FF                  jmp 0x140847090
00847546  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0084754E  4C 8B E0                        mov r12, rax
00847551  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00847559  45 84 D2                        test r10b, r10b
0084755C  0F 85 3D EE 2C 00               jne 0x140b1639f
00847562  49 8B D1                        mov rdx, r9
00847565  48 8B C8                        mov rcx, rax
00847568  E8 AF D8 FF FF                  call 0x140844e1c
0084756D  8B C8                           mov ecx, eax
0084756F  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00847573  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
00847577  E9 4C EE 2C 00                  jmp 0x140b163c8
0084757C  49 8D 96 18 01 00 00            lea rdx, [r14 + 0x118]
00847583  48 8D 44 24 4C                  lea rax, [rsp + 0x4c]
00847588  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0084758D  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00847592  E8 BD D8 FF FF                  call 0x140844e54
00847597  8B 4C 24 4C                     mov ecx, dword ptr [rsp + 0x4c]
0084759B  E9 4C FB FF FF                  jmp 0x1408470ec
008475A0  BE 9A 00 00 C0                  mov esi, 0xc000009a
008475A5  E9 63 FD FF FF                  jmp 0x14084730d
008475AA  33 D2                           xor edx, edx
008475AC  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
008475B4  E8 B7 B2 33 00                  call 0x140b82870
008475B9  88 9C 24 30 01 00 00            mov byte ptr [rsp + 0x130], bl
008475C0  E9 D6 FC FF FF                  jmp 0x14084729b
008475C5  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
008475CA  49 8B CC                        mov rcx, r12
008475CD  41 84 BC 24 8C 00 00 00         test byte ptr [r12 + 0x8c], dil
008475D5  0F 84 F7 ED 2C 00               je 0x140b163d2
008475DB  E8 40 56 01 00                  call 0x14085cc20
008475E0  E9 31 FD FF FF                  jmp 0x140847316
008475E5  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
008475ED  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
008475F2  40 84 B9 8C 00 00 00            test byte ptr [rcx + 0x8c], dil
008475F9  0F 84 DE ED 2C 00               je 0x140b163dd
008475FF  E8 1C 56 01 00                  call 0x14085cc20
00847604  E9 1C FD FF FF                  jmp 0x140847325
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmQueryMultipleValueKey(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned __int8 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int8 v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int8 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int8 v_stack_p130;
    unsigned __int64 v_stack_p140;
    unsigned int v_stack_p148;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p4C;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pC0;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (240);
    v_rbx = 0;
    v_stack_m78 = 0;
    v_stack_m80 = 0;
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    v_stack_mC8 = (unsigned int)(a1);
    v_stack_mC4 = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = 0;
    v_stack_mE8 = 0;
    v_stack_mC0 = (unsigned int)(a1);
    v_stack_mBC = 0;
    v_stack_m98 = 0;
    v_stack_mB0 = (unsigned int)(a1);
    v_stack_mAC = 0;
    v_stack_m68 = 0;
    v_stack_mD0 = 0;
    v_stack_mB8 = 0;
    v_stack_mD4 = 0;
    *(unsigned __int64 *)(v_rsp - 144) = 0;
    *(unsigned __int8 *)(v_rsp + 8) = 0;
    *(unsigned int *)(v_rsp - 160) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 156) = 0;
    result = CmpLockRegistry(a1, a2, a3, a4);
    v_stack_m48 = *(unsigned __int64 *)(a1 + 8);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) != 0) goto loc_008473A8;
    if ((*(unsigned __int64 *)(a1 + 56)) != 0) goto loc_008473FF;
    if ((*(unsigned __int64 *)(a1 + 64)) != 0) goto loc_008473FF;
loc_00846F87:
    if (a2 != 0) goto loc_008474BF;
loc_00846F90:
    result = CmpLockTwoKcbsShared(0, *(unsigned __int64 *)(a1 + 8), a3, a4);
    result = CmpIsKeyDeletedForKeyBody(a1, 0, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00847460;
    if (a2 != 0) goto loc_008474D0;
loc_00846FB7:
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32);
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), 0, a3, a4);
    v_stack_m60 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_00847394;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), v_stack_mC0, a4);
loc_00846FF9:
    v_stack_m70 = result;
    if (result == 0) goto loc_0084748A;
    result = CmpUpdateKeyNodeAccessBits(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), a4);
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), a4);
    if (0 != 0) goto loc_008474EC;
loc_0084702A:
    if (0 != 0) goto loc_00847506;
loc_0084703F:
    v_stack_mA8 = 0;
    if (0 >= v_stack_p20) goto loc_008472FD;
    v_stack_m58 = 0 + 0 * 2;
    v_stack_mD0 = *(unsigned __int64 *)(v_stack_p18 + 0 + 0 * 2 * 8);
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 0 + 0 * 2 * 8))) == 0) goto loc_00847090;
loc_0084707F:
    result = ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 0 + 0 * 2 * 8)))) >> (1);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 0 + 0 * 2 * 8) + 8) + result * 2 - 2)) == 0) goto loc_00847533;
loc_00847090:
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p18 + 0 + 0 * 2 * 8))) | (0xFFFFFFFFULL));
    v_stack_mE4 = (unsigned int)(a1);
    v_stack_mDC = (unsigned int)(a1);
    if (0 != 0) goto loc_00847546;
    if (((unsigned int)(a1)) != -1) goto loc_008470F9;
    v_stack_m80 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32);
    a4 = 0;
    if (v_stack_mB8 != 0) goto loc_0084757C;
    v_stack_mE4 = 0;
    a2 = (v_stack_m70) + (36);
    v_stack_m100 = v_stack_mE4;
    v_stack_m108 = 0;
    result = CmpFindNameInListWithStatus(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a2, *(unsigned __int64 *)(v_stack_p18 + 0 + 0 * 2 * 8), a4);
loc_008470EC:
    v_stack_mE4 = (unsigned int)((unsigned int)(v_stack_mE4));
    if (((unsigned int)((unsigned int)(v_stack_mE4))) == -1) goto loc_008472F8;
loc_008470F9:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_008472EE;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_mE4))), v_stack_mC8, a4);
loc_00847116:
    v_stack_mD0 = result;
    if (result == 0) goto loc_008475A0;
    a2 = (unsigned int)(*(unsigned int *)(result + 4)) - 2147483648;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) < 0x80000000ULL) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4))); }
    v_stack_mDC = (unsigned int)(a2);
    a3 = (unsigned int)(((unsigned int)(v_stack_mE0)) + (3));
    a3 = (unsigned int)((a3) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    v_stack_mE0 = (unsigned int)(a3);
    v_stack_m84 = (unsigned int)(a3);
    v_r10 = (unsigned int)(((unsigned int)(v_stack_mD8)) + (3));
    v_r10 = (unsigned int)((v_r10) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    v_stack_mD8 = (unsigned int)(v_r10);
    v_stack_m88 = (unsigned int)(v_r10);
    if (((unsigned int)(a2 + a3 * 1)) > (*(unsigned int *)(a6))) goto loc_0084739E;
    if (((unsigned int)(a2 + a3 * 1)) < ((unsigned int)(a3))) goto loc_0084739E;
    if (v_stack_mE8 != 0) goto loc_0084739E;
    v_stack_mF8 = v_stack_mA0;
    v_stack_m100 = v_stack_p8;
    v_stack_m108 = v_stack_m90;
    result = CmpGetValueData(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(v_stack_mE4), result, v_stack_mDC);
    if ((unsigned __int8)(result) == 0) goto loc_008473F0;
    v_stack_mE4 = (unsigned int)((unsigned int)(v_stack_mDC));
    a1 = ((unsigned int)(v_stack_mE0)) + (a5);
    result = memcpy(a1, v_stack_m90, (unsigned int)((unsigned int)((unsigned int)(v_stack_mDC))), v_stack_mDC);
    goto loc_00847244;
loc_00847244:
    *(unsigned int *)(v_stack_p18 + v_stack_m58 * 8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD0 + 12)));
    *(unsigned int *)(v_stack_p18 + v_stack_m58 * 8 + 8) = (unsigned int)((unsigned int)(v_stack_mE4));
    *(unsigned int *)(v_stack_p18 + v_stack_m58 * 8 + 12) = (unsigned int)((unsigned int)(v_stack_mE0));
    if (v_stack_p8 != 0) goto loc_008475AA;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) != 0) goto loc_0084744C;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_mA0, (unsigned int)((unsigned int)((unsigned int)(v_stack_mDC))), v_stack_mDC);
loc_0084729B:
    v_stack_m90 = 0;
loc_008472B0:
    v_r10 = (unsigned int)(((unsigned int)(v_stack_mD8)) + ((unsigned int)((unsigned int)(v_stack_mE4))));
    v_stack_mD8 = (unsigned int)(v_r10);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) != 0) goto loc_00847442;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_mC8, (unsigned int)((unsigned int)((unsigned int)(v_stack_mDC))), v_stack_mDC);
loc_008472D3:
    a1 = (unsigned int)(((unsigned int)(v_stack_mA8)) + (1));
    goto loc_0084703F;
loc_008472EE:
    result = HvpGetCellPaged(a1, v_stack_mC8, (unsigned int)((unsigned int)((unsigned int)(v_stack_mDC))), v_stack_m98);
    goto loc_00847116;
loc_008472F8:
loc_008472FD:
loc_00847309:
    if (!sign_flag) goto loc_00847369;
loc_0084730D:
    if (0 != 0) goto loc_008475C5;
loc_00847316:
    if (v_stack_m98 != 0) goto loc_008475E5;
loc_00847325:
    if (((*(unsigned __int8 *)(v_stack_m60)) & (1)) != 0) goto loc_00847456;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_mC0, (unsigned int)(v_stack_mD8), v_stack_m98);
loc_00847343:
    result = CmpUnlockTwoKcbs(0, *(unsigned __int64 *)(a1 + 8), (unsigned int)(v_stack_mD8), v_stack_m98);
loc_0084734E:
    result = CmpUnlockRegistry(0, *(unsigned __int64 *)(a1 + 8), (unsigned int)(v_stack_mD8), v_stack_m98);
loc_00847355:
    v_rsp = (v_rsp) + (240);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000034ULL)));
loc_00847369:
    v_rsi = (unsigned int)(0xC0000034ULL);
    if (v_stack_p40 != 0) { v_rsi = (unsigned int)((unsigned int)(0x80000005ULL)); }
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000034ULL))));
    if (a7 == 0) goto loc_0084730D;
    *(unsigned int *)(a7) = (unsigned int)((unsigned int)(v_stack_mD8));
    goto loc_0084730D;
loc_00847394:
    result = HvpGetCellPaged(0, a6, (unsigned int)(v_stack_mD8), v_stack_m98);
    goto loc_00846FF9;
loc_0084739E:
    v_stack_p40 = 1;
    goto loc_008472B0;
loc_008473A8:
    v_stack_p28 = a7;
    v_stack_p20 = a6;
    result = CmQueryMultipleValueForLayeredKey(1, v_stack_p140, (unsigned int)(v_stack_p148), a5);
    result = CmpUnlockRegistry(1, v_stack_p140, (unsigned int)(v_stack_p148), a5);
    goto loc_00847355;
loc_008473F0:
    goto loc_0084730D;
loc_008473FF:
    result = CmpLockKcbShared(*(unsigned __int64 *)(a1 + 8), v_stack_p140, (unsigned int)(v_stack_p148), a5);
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(1, a2, (unsigned int)(v_stack_p148), a5);
    if ((unsigned __int8)(result) != 0) goto loc_008474A9;
    result = CmpUnlockKcb(*(unsigned __int64 *)(a1 + 8), a2, (unsigned int)(v_stack_p148), a5);
    result = CmpTransSearchAddTransFromKeyBody(1, v_stack_p58, (unsigned int)(v_stack_p148), a5);
    if (sign_flag) goto loc_0084734E;
    goto loc_00846F87;
loc_00847442:
    result = HvpReleaseCellFlat(1, v_stack_p58, (unsigned int)(v_stack_p148), a5);
    goto loc_008472D3;
loc_0084744C:
    result = HvpReleaseCellFlat(1, v_stack_p58, (unsigned int)(v_stack_p148), a5);
    goto loc_0084729B;
loc_00847456:
    result = HvpReleaseCellFlat(1, v_stack_p58, (unsigned int)(v_stack_p148), a5);
    goto loc_00847343;
loc_00847460:
loc_00847463:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(1 + 48))) & (1));
    result = (unsigned __int8)(-(result));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) & (681));
    result = CmpUnlockTwoKcbs(0, *(unsigned __int64 *)(a1 + 8), (unsigned int)(v_stack_p148), a5);
loc_0084747A:
    result = CmpUnlockRegistry(0, *(unsigned __int64 *)(a1 + 8), (unsigned int)(v_stack_p148), a5);
    goto loc_00847355;
loc_0084748A:
    result = HvUnlockHiveFlusherShared(0, *(unsigned __int64 *)(a1 + 8), (unsigned int)(v_stack_p148), a5);
    result = CmpUnlockTwoKcbs(0, *(unsigned __int64 *)(a1 + 8), (unsigned int)(v_stack_p148), a5);
    result = CmpUnlockRegistry(0, *(unsigned __int64 *)(a1 + 8), (unsigned int)(v_stack_p148), a5);
    goto loc_00847355;
loc_008474A9:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(1 + 48))) & (1));
    result = (unsigned __int8)(-(result));
    v_rbx = (unsigned int)((v_rbx) & (681));
    result = CmpUnlockKcb(0, *(unsigned __int64 *)(a1 + 8), (unsigned int)(v_stack_p148), a5);
    goto loc_0084747A;
loc_008474BF:
    v_stack_pC0 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 8);
    goto loc_00846F90;
loc_008474D0:
    result = CmpIsKeyDeletedForKeyBody(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_p58, (unsigned int)(v_stack_p148), a5);
    if ((unsigned __int8)(result) == 0) goto loc_00846FB7;
    goto loc_00847463;
loc_008474EC:
    result = (unsigned __int8)((unsigned int)(v_stack_p70));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 288)) == v_stack_p58) { result = 1; }
    v_stack_p70 = (unsigned int)(result);
    goto loc_0084702A;
loc_00847506:
    v_stack_pB0 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 8) + 32);
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 8) + 40)), v_stack_p78, a5);
loc_00847533:
    a1 = (unsigned __int16)((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 8) + 32)) - (2));
    *(unsigned __int16 *)(v_stack_p78) = (unsigned __int16)(a1);
    if (condition_is_not_equal) goto loc_0084707F;
    goto loc_00847090;
loc_00847546:
    v_stack_pA8 = v_stack_pB0;
    result = CmpFindValueByName(v_stack_pB0, a5, v_stack_p78, a5);
    v_stack_p44 = (unsigned int)(result);
    v_stack_p4C = (unsigned int)(result);
loc_0084757C:
    v_stack_p28 = v_stack_p4C;
    v_stack_p20 = v_rbx;
    result = CmpFindNameInList((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(a1 + 8) + 280, v_stack_p78, a5);
    goto loc_008470EC;
loc_008475A0:
    goto loc_0084730D;
loc_008475AA:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p98, a2, v_stack_p78, a5);
    v_stack_p130 = (unsigned __int8)(v_rbx);
    goto loc_0084729B;
loc_008475C5:
    result = HvpReleaseCellFlat(v_stack_pB0, v_stack_p60, v_stack_p78, a5);
    goto loc_00847316;
loc_008475E5:
    result = HvpReleaseCellFlat(v_stack_pB0, v_stack_p78, v_stack_p78, a5);
    goto loc_00847325;
}
```

## 5. (Beta) C Style

```c
int64_t CmQueryMultipleValueKey(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, void *Arg6, int64_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint8_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint8_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint8_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint8_t v_stack_p130;
    uint64_t v_stack_p140;
    uint32_t v_stack_p148;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p4C;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pC0;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (240);
    local_rbx = 0;
    v_stack_m78 = 0;
    v_stack_m80 = 0;
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    v_stack_mC8 = (uint32_t)(Arg1);
    v_stack_mC4 = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = 0;
    v_stack_mE8 = 0;
    v_stack_mC0 = (uint32_t)(Arg1);
    v_stack_mBC = 0;
    v_stack_m98 = 0;
    v_stack_mB0 = (uint32_t)(Arg1);
    v_stack_mAC = 0;
    v_stack_m68 = 0;
    v_stack_mD0 = 0;
    v_stack_mB8 = 0;
    v_stack_mD4 = 0;
    *(uint64_t *)(local_rsp - 0x90) = 0;
    *(uint8_t *)(local_rsp + 0x8) = 0;
    *(uint32_t *)(local_rsp - 0xA0) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x9C) = 0;
    result = CmpLockRegistry(Arg1, Arg2, Arg3, Arg4);
    v_stack_m48 = *(uint64_t *)(arg1 + 0x8);
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x42)) != 0) goto loc_008473A8;
    if ((*(uint64_t *)(arg1 + 0x38)) != 0) goto loc_008473FF;
    if ((*(uint64_t *)(arg1 + 0x40)) != 0) goto loc_008473FF;
loc_00846F87:
    if (Arg2 != 0) goto loc_008474BF;
loc_00846F90:
    result = CmpLockTwoKcbsShared(0, *(uint64_t *)(arg1 + 0x8), Arg3, Arg4);
    result = CmpIsKeyDeletedForKeyBody(Arg1, 0, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00847460;
    if (Arg2 != 0) goto loc_008474D0;
loc_00846FB7:
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20);
    result = HvLockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), 0, Arg3, Arg4);
    v_stack_m60 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 140;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_00847394;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28)), v_stack_mC0, Arg4);
loc_00846FF9:
    v_stack_m70 = result;
    if (result == 0) goto loc_0084748A;
    result = CmpUpdateKeyNodeAccessBits(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28)), Arg4);
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28)), Arg4);
    if (0 != 0) goto loc_008474EC;
loc_0084702A:
    if (0 != 0) goto loc_00847506;
loc_0084703F:
    v_stack_mA8 = 0;
    if (0 >= v_stack_p20) goto loc_008472FD;
    v_stack_m58 = 0 + 0 * 2;
    v_stack_mD0 = *(uint64_t *)(v_stack_p18 + 0x0 + 0x0 * 2 * 8);
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x0 + 0x0 * 2 * 8))) == 0) goto loc_00847090;
loc_0084707F:
    result = ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x0 + 0x0 * 2 * 8)))) >> (1);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x0 + 0x0 * 2 * 8) + 0x8) + result * 2 - 0x2)) == 0) goto loc_00847533;
loc_00847090:
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_p18 + 0x0 + 0x0 * 2 * 8))) | (0xFFFFFFFFULL));
    v_stack_mE4 = (uint32_t)(Arg1);
    v_stack_mDC = (uint32_t)(Arg1);
    if (0 != 0) goto loc_00847546;
    if (((uint32_t)(Arg1)) != -1) goto loc_008470F9;
    v_stack_m80 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20);
    Arg4 = 0;
    if (v_stack_mB8 != 0) goto loc_0084757C;
    v_stack_mE4 = 0;
    Arg2 = (v_stack_m70) + (36);
    v_stack_m100 = v_stack_mE4;
    v_stack_m108 = 0;
    result = CmpFindNameInListWithStatus(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg2, *(uint64_t *)(v_stack_p18 + 0x0 + 0x0 * 2 * 8), Arg4);
loc_008470EC:
    v_stack_mE4 = (uint32_t)((uint32_t)(v_stack_mE4));
    if (((uint32_t)((uint32_t)(v_stack_mE4))) == -1) goto loc_008472F8;
loc_008470F9:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_008472EE;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_mE4))), v_stack_mC8, Arg4);
loc_00847116:
    v_stack_mD0 = result;
    if (result == 0) goto loc_008475A0;
    Arg2 = (uint32_t)(*(uint32_t *)(result + 0x4)) - 2147483648;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) < 0x80000000ULL) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))); }
    v_stack_mDC = (uint32_t)(Arg2);
    Arg3 = (uint32_t)(((uint32_t)(v_stack_mE0)) + (3));
    Arg3 = (uint32_t)((Arg3) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    v_stack_mE0 = (uint32_t)(Arg3);
    v_stack_m84 = (uint32_t)(Arg3);
    local_r10 = (uint32_t)(((uint32_t)(v_stack_mD8)) + (3));
    local_r10 = (uint32_t)((local_r10) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    v_stack_mD8 = (uint32_t)(local_r10);
    v_stack_m88 = (uint32_t)(local_r10);
    if (((uint32_t)(Arg2 + Arg3 * 1)) > (*(uint32_t *)(arg6))) goto loc_0084739E;
    if (((uint32_t)(Arg2 + Arg3 * 1)) < ((uint32_t)(Arg3))) goto loc_0084739E;
    if (v_stack_mE8 != 0) goto loc_0084739E;
    v_stack_mF8 = v_stack_mA0;
    v_stack_m100 = v_stack_p8;
    v_stack_m108 = v_stack_m90;
    result = CmpGetValueData(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(v_stack_mE4), result, v_stack_mDC);
    if ((uint8_t)(result) == 0) goto loc_008473F0;
    v_stack_mE4 = (uint32_t)((uint32_t)(v_stack_mDC));
    Arg1 = ((uint32_t)(v_stack_mE0)) + (Arg5);
    result = memcpy(Arg1, v_stack_m90, (uint32_t)((uint32_t)((uint32_t)(v_stack_mDC))), v_stack_mDC);
    goto loc_00847244;
loc_00847244:
    *(uint32_t *)(v_stack_p18 + v_stack_m58 * 8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0xC)));
    *(uint32_t *)(v_stack_p18 + v_stack_m58 * 8 + 0x8) = (uint32_t)((uint32_t)(v_stack_mE4));
    *(uint32_t *)(v_stack_p18 + v_stack_m58 * 8 + 0xC) = (uint32_t)((uint32_t)(v_stack_mE0));
    if (v_stack_p8 != 0) goto loc_008475AA;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) != 0) goto loc_0084744C;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_mA0, (uint32_t)((uint32_t)((uint32_t)(v_stack_mDC))), v_stack_mDC);
loc_0084729B:
    v_stack_m90 = 0;
loc_008472B0:
    local_r10 = (uint32_t)(((uint32_t)(v_stack_mD8)) + ((uint32_t)((uint32_t)(v_stack_mE4))));
    v_stack_mD8 = (uint32_t)(local_r10);
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) != 0) goto loc_00847442;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_mC8, (uint32_t)((uint32_t)((uint32_t)(v_stack_mDC))), v_stack_mDC);
loc_008472D3:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_mA8)) + (1));
    goto loc_0084703F;
loc_008472EE:
    result = HvpGetCellPaged(Arg1, v_stack_mC8, (uint32_t)((uint32_t)((uint32_t)(v_stack_mDC))), v_stack_m98);
    goto loc_00847116;
loc_008472F8:
loc_008472FD:
loc_00847309:
    if (!sign_flag) goto loc_00847369;
loc_0084730D:
    if (0 != 0) goto loc_008475C5;
loc_00847316:
    if (v_stack_m98 != 0) goto loc_008475E5;
loc_00847325:
    if (((*(uint8_t *)(v_stack_m60)) & (1)) != 0) goto loc_00847456;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_mC0, (uint32_t)(v_stack_mD8), v_stack_m98);
loc_00847343:
    result = CmpUnlockTwoKcbs(0, *(uint64_t *)(arg1 + 0x8), (uint32_t)(v_stack_mD8), v_stack_m98);
loc_0084734E:
    result = CmpUnlockRegistry(0, *(uint64_t *)(arg1 + 0x8), (uint32_t)(v_stack_mD8), v_stack_m98);
loc_00847355:
    local_rsp = (local_rsp) + (240);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000034ULL)));
loc_00847369:
    local_rsi = (uint32_t)(0xC0000034ULL);
    if (v_stack_p40 != 0) { local_rsi = (uint32_t)((uint32_t)(0x80000005ULL)); }
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000034ULL))));
    if (Arg7 == 0) goto loc_0084730D;
    *(uint32_t *)(Arg7) = (uint32_t)((uint32_t)(v_stack_mD8));
    goto loc_0084730D;
loc_00847394:
    result = HvpGetCellPaged(0, Arg6, (uint32_t)(v_stack_mD8), v_stack_m98);
    goto loc_00846FF9;
loc_0084739E:
    v_stack_p40 = 1;
    goto loc_008472B0;
loc_008473A8:
    v_stack_p28 = Arg7;
    v_stack_p20 = Arg6;
    result = CmQueryMultipleValueForLayeredKey(1, v_stack_p140, (uint32_t)(v_stack_p148), Arg5);
    result = CmpUnlockRegistry(1, v_stack_p140, (uint32_t)(v_stack_p148), Arg5);
    goto loc_00847355;
loc_008473F0:
    goto loc_0084730D;
loc_008473FF:
    result = CmpLockKcbShared(*(uint64_t *)(arg1 + 0x8), v_stack_p140, (uint32_t)(v_stack_p148), Arg5);
    Arg2 = 0;
    result = CmpIsKeyDeletedForKeyBody(1, Arg2, (uint32_t)(v_stack_p148), Arg5);
    if ((uint8_t)(result) != 0) goto loc_008474A9;
    result = CmpUnlockKcb(*(uint64_t *)(arg1 + 0x8), Arg2, (uint32_t)(v_stack_p148), Arg5);
    result = CmpTransSearchAddTransFromKeyBody(1, v_stack_p58, (uint32_t)(v_stack_p148), Arg5);
    if (sign_flag) goto loc_0084734E;
    goto loc_00846F87;
loc_00847442:
    result = HvpReleaseCellFlat(1, v_stack_p58, (uint32_t)(v_stack_p148), Arg5);
    goto loc_008472D3;
loc_0084744C:
    result = HvpReleaseCellFlat(1, v_stack_p58, (uint32_t)(v_stack_p148), Arg5);
    goto loc_0084729B;
loc_00847456:
    result = HvpReleaseCellFlat(1, v_stack_p58, (uint32_t)(v_stack_p148), Arg5);
    goto loc_00847343;
loc_00847460:
loc_00847463:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(1 + 0x30))) & (1));
    result = (uint8_t)(-(result));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) & (681));
    result = CmpUnlockTwoKcbs(0, *(uint64_t *)(arg1 + 0x8), (uint32_t)(v_stack_p148), Arg5);
loc_0084747A:
    result = CmpUnlockRegistry(0, *(uint64_t *)(arg1 + 0x8), (uint32_t)(v_stack_p148), Arg5);
    goto loc_00847355;
loc_0084748A:
    result = HvUnlockHiveFlusherShared(0, *(uint64_t *)(arg1 + 0x8), (uint32_t)(v_stack_p148), Arg5);
    result = CmpUnlockTwoKcbs(0, *(uint64_t *)(arg1 + 0x8), (uint32_t)(v_stack_p148), Arg5);
    result = CmpUnlockRegistry(0, *(uint64_t *)(arg1 + 0x8), (uint32_t)(v_stack_p148), Arg5);
    goto loc_00847355;
loc_008474A9:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(1 + 0x30))) & (1));
    result = (uint8_t)(-(result));
    local_rbx = (uint32_t)((local_rbx) & (681));
    result = CmpUnlockKcb(0, *(uint64_t *)(arg1 + 0x8), (uint32_t)(v_stack_p148), Arg5);
    goto loc_0084747A;
loc_008474BF:
    v_stack_pC0 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8);
    goto loc_00846F90;
loc_008474D0:
    result = CmpIsKeyDeletedForKeyBody(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_p58, (uint32_t)(v_stack_p148), Arg5);
    if ((uint8_t)(result) == 0) goto loc_00846FB7;
    goto loc_00847463;
loc_008474EC:
    result = (uint8_t)((uint32_t)(v_stack_p70));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x120)) == v_stack_p58) { result = 1; }
    v_stack_p70 = (uint32_t)(result);
    goto loc_0084702A;
loc_00847506:
    v_stack_pB0 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8) + 0x20);
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8) + 0x28)), v_stack_p78, Arg5);
loc_00847533:
    Arg1 = (uint16_t)((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8) + 0x20)) - (2));
    *(uint16_t *)(v_stack_p78) = (uint16_t)(Arg1);
    if (condition_is_not_equal) goto loc_0084707F;
    goto loc_00847090;
loc_00847546:
    v_stack_pA8 = v_stack_pB0;
    result = CmpFindValueByName(v_stack_pB0, Arg5, v_stack_p78, Arg5);
    v_stack_p44 = (uint32_t)(result);
    v_stack_p4C = (uint32_t)(result);
loc_0084757C:
    v_stack_p28 = v_stack_p4C;
    v_stack_p20 = local_rbx;
    result = CmpFindNameInList((uint32_t)((uint32_t)(result)), *(uint64_t *)(arg1 + 0x8) + 280, v_stack_p78, Arg5);
    goto loc_008470EC;
loc_008475A0:
    goto loc_0084730D;
loc_008475AA:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p98, Arg2, v_stack_p78, Arg5);
    v_stack_p130 = (uint8_t)(local_rbx);
    goto loc_0084729B;
loc_008475C5:
    result = HvpReleaseCellFlat(v_stack_pB0, v_stack_p60, v_stack_p78, Arg5);
    goto loc_00847316;
loc_008475E5:
    result = HvpReleaseCellFlat(v_stack_pB0, v_stack_p78, v_stack_p78, Arg5);
    goto loc_00847325;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg6` | `+ 0x0` | `32` | `R` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00846EC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
