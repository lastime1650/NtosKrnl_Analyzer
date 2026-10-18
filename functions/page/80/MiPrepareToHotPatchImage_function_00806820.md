# MiPrepareToHotPatchImage

- RVA: `0x00806820`–`0x00806DB8` (길이 `1,432` bytes)
- VA: `0x0000000140806820`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D84DC`
- 디코드: `365`개 명령, `1,432/1,432` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00806869` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008068C3` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x008068F4` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (function, `0x00362490`)
- `0x0080693F` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00806963` → [RtlClearAllBits](../../text/45/RtlClearAllBits_function_00450230.md) (function, `0x00450230`)
- `0x0080696E` → [MiProcessHotPatchUndoTable](MiProcessHotPatchUndoTable_function_00806F20.md) (function, `0x00806F20`)
- `0x00806985` → [RtlFindHotPatchBaseMachine](../84/RtlFindHotPatchBaseMachine_function_00840EBC.md) (function, `0x00840EBC`)
- `0x008069CE` → [RtlCountRequiredHotPatchAddressTableEntries](../84/RtlCountRequiredHotPatchAddressTableEntries_function_00840BF8.md) (function, `0x00840BF8`)
- `0x00806A96` → [MiCommitHotPatchTable](../../text/68/MiCommitHotPatchTable_function_00683420.md) (function, `0x00683420`)
- `0x00806AED` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00806B16` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00806B21` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00806B56` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00806B7C` → [RtlClearAllBits](../../text/45/RtlClearAllBits_function_00450230.md) (function, `0x00450230`)
- `0x00806B87` → [MiProcessHotPatchUndoTable](MiProcessHotPatchUndoTable_function_00806F20.md) (function, `0x00806F20`)
- `0x00806BAA` → [MiPrepareImagePagesForHotPatch](../../text/68/MiPrepareImagePagesForHotPatch_function_00683800.md) (function, `0x00683800`)
- `0x00806BF5` → [RtlEnumerateHotPatchPatches](../84/RtlEnumerateHotPatchPatches_function_00840DE8.md) (function, `0x00840DE8`)
- `0x00806C2D` → [RtlAreBitsSet](../../text/45/RtlAreBitsSet_function_00450EF0.md) (function, `0x00450EF0`)
- `0x00806C93` → [RtlpCheckFunctionPatchApplied](../../pagelk/B7/RtlpCheckFunctionPatchApplied_function_00B75828.md) (function, `0x00B75828`)
- `0x00806CED` → [RtlHotPatchSynchronizationRequired](../../text/6A/RtlHotPatchSynchronizationRequired_function_006AA21C.md) (function, `0x006AA21C`)
- `0x00806CF7` → [RtlClearAllBits](../../text/45/RtlClearAllBits_function_00450230.md) (function, `0x00450230`)
- `0x00806D3A` → [RtlFindNextForwardRunClear](../../text/3C/RtlFindNextForwardRunClear_function_003CF6A0.md) (function, `0x003CF6A0`)
- `0x00806D62` → [MiPrepareImagePagesForHotPatch](../../text/68/MiPrepareImagePagesForHotPatch_function_00683800.md) (function, `0x00683800`)
- `0x00806D7A` → [MiMapHotPatchImageInSystemSpace](MiMapHotPatchImageInSystemSpace_function_00806438.md) (function, `0x00806438`)

### Direct callers
- [MiPrepareToHotPatchVad](MiPrepareToHotPatchVad_function_00806E70.md) at `0x00806EE8`

### Static image references
- `0x00806A72` → RVA `0x00E375AC` (`.data`; read)
- `0x00806BDB` → RVA `0x00806DC0` (`MiPrepareToHotPatchImagePatchCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x00806869` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008068C3` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x008068F4` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (`PAGE` → `.text`)
  - `0x0080693F` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00806963` → [RtlClearAllBits](../../text/45/RtlClearAllBits_function_00450230.md) (`PAGE` → `.text`)
  - `0x00806A96` → [MiCommitHotPatchTable](../../text/68/MiCommitHotPatchTable_function_00683420.md) (`PAGE` → `.text`)
  - `0x00806AED` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00806B16` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00806B21` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00806B56` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00806B7C` → [RtlClearAllBits](../../text/45/RtlClearAllBits_function_00450230.md) (`PAGE` → `.text`)
  - `0x00806BAA` → [MiPrepareImagePagesForHotPatch](../../text/68/MiPrepareImagePagesForHotPatch_function_00683800.md) (`PAGE` → `.text`)
  - `0x00806C2D` → [RtlAreBitsSet](../../text/45/RtlAreBitsSet_function_00450EF0.md) (`PAGE` → `.text`)
  - `0x00806C93` → [RtlpCheckFunctionPatchApplied](../../pagelk/B7/RtlpCheckFunctionPatchApplied_function_00B75828.md) (`PAGE` → `PAGELK`)
  - `0x00806CED` → [RtlHotPatchSynchronizationRequired](../../text/6A/RtlHotPatchSynchronizationRequired_function_006AA21C.md) (`PAGE` → `.text`)
  - `0x00806CF7` → [RtlClearAllBits](../../text/45/RtlClearAllBits_function_00450230.md) (`PAGE` → `.text`)
  - `0x00806D3A` → [RtlFindNextForwardRunClear](../../text/3C/RtlFindNextForwardRunClear_function_003CF6A0.md) (`PAGE` → `.text`)
  - `0x00806D62` → [MiPrepareImagePagesForHotPatch](../../text/68/MiPrepareImagePagesForHotPatch_function_00683800.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00806820  48 8B C4                        mov rax, rsp
00806823  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00806827  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0080682B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0080682F  53                              push rbx
00806830  56                              push rsi
00806831  57                              push rdi
00806832  41 54                           push r12
00806834  41 55                           push r13
00806836  41 56                           push r14
00806838  41 57                           push r15
0080683A  48 81 EC 10 01 00 00            sub rsp, 0x110
00806841  4D 8B F0                        mov r14, r8
00806844  48 8B F2                        mov rsi, rdx
00806847  48 8B F9                        mov rdi, rcx
0080684A  48 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rcx
00806852  0F 57 C0                        xorps xmm0, xmm0
00806855  0F 11 80 50 FF FF FF            movups xmmword ptr [rax - 0xb0], xmm0
0080685C  33 D2                           xor edx, edx
0080685E  44 8D 42 48                     lea r8d, [rdx + 0x48]
00806862  48 8D 88 78 FF FF FF            lea rcx, [rax - 0x88]
00806869  E8 D2 03 EC FF                  call 0x1406c6c40
0080686E  33 DB                           xor ebx, ebx
00806870  4D 85 F6                        test r14, r14
00806873  75 15                           jne 0x14080688a
00806875  4C 8D B4 24 C0 00 00 00         lea r14, [rsp + 0xc0]
0080687D  4C 89 B4 24 60 01 00 00         mov qword ptr [rsp + 0x160], r14
00806885  41 B4 01                        mov r12b, 1
00806888  EB 03                           jmp 0x14080688d
0080688A  44 8A E3                        mov r12b, bl
0080688D  44 88 A4 24 68 01 00 00         mov byte ptr [rsp + 0x168], r12b
00806895  4C 89 B4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r14
0080689D  8B 57 20                        mov edx, dword ptr [rdi + 0x20]
008068A0  8B C2                           mov eax, edx
008068A2  25 00 F0 03 00                  and eax, 0x3f000
008068A7  F7 D8                           neg eax
008068A9  1B C9                           sbb ecx, ecx
008068AB  F7 D9                           neg ecx
008068AD  83 C1 02                        add ecx, 2
008068B0  C1 EA 12                        shr edx, 0x12
008068B3  03 D1                           add edx, ecx
008068B5  C1 E2 03                        shl edx, 3
008068B8  B9 00 01 00 00                  mov ecx, 0x100
008068BD  41 B8 4D 6D 20 20               mov r8d, 0x20206d4d
008068C3  E8 78 4C B5 FF                  call 0x14035b540
008068C8  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
008068CC  48 85 C0                        test rax, rax
008068CF  74 10                           je 0x1408068e1
008068D1  8B 57 20                        mov edx, dword ptr [rdi + 0x20]
008068D4  C1 EA 0C                        shr edx, 0xc
008068D7  48 8D 48 10                     lea rcx, [rax + 0x10]
008068DB  89 10                           mov dword ptr [rax], edx
008068DD  48 89 48 08                     mov qword ptr [rax + 8], rcx
008068E1  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008068E5  48 85 C9                        test rcx, rcx
008068E8  75 0A                           jne 0x1408068f4
008068EA  BE 9A 00 00 C0                  mov esi, 0xc000009a
008068EF  E9 AE 04 00 00                  jmp 0x140806da2
008068F4  E8 97 BB B5 FF                  call 0x140362490
008068F9  4D 8D 7E 10                     lea r15, [r14 + 0x10]
008068FD  4C 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r15
00806905  48 8D 4F 24                     lea rcx, [rdi + 0x24]
00806909  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
00806911  41 8B 07                        mov eax, dword ptr [r15]
00806914  C1 E0 04                        shl eax, 4
00806917  89 01                           mov dword ptr [rcx], eax
00806919  48 85 F6                        test rsi, rsi
0080691C  75 5D                           jne 0x14080697b
0080691E  41 8B 17                        mov edx, dword ptr [r15]
00806921  8B C2                           mov eax, edx
00806923  24 3F                           and al, 0x3f
00806925  F6 D8                           neg al
00806927  1B C9                           sbb ecx, ecx
00806929  F7 D9                           neg ecx
0080692B  83 C1 02                        add ecx, 2
0080692E  C1 EA 06                        shr edx, 6
00806931  03 D1                           add edx, ecx
00806933  C1 E2 03                        shl edx, 3
00806936  8D 4E 40                        lea ecx, [rsi + 0x40]
00806939  41 B8 4D 6D 20 20               mov r8d, 0x20206d4d
0080693F  E8 FC 4B B5 FF                  call 0x14035b540
00806944  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
00806948  48 85 C0                        test rax, rax
0080694B  74 0D                           je 0x14080695a
0080694D  41 8B 0F                        mov ecx, dword ptr [r15]
00806950  48 8D 50 10                     lea rdx, [rax + 0x10]
00806954  89 08                           mov dword ptr [rax], ecx
00806956  48 89 50 08                     mov qword ptr [rax + 8], rdx
0080695A  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
0080695E  48 85 C9                        test rcx, rcx
00806961  74 87                           je 0x1408068ea
00806963  E8 C8 98 C4 FF                  call 0x140450230
00806968  49 8B D6                        mov rdx, r14
0080696B  48 8B CF                        mov rcx, rdi
0080696E  E8 AD 05 00 00                  call 0x140806f20
00806973  4C 8B EB                        mov r13, rbx
00806976  E9 DE 02 00 00                  jmp 0x140806c59
0080697B  0F B7 97 88 00 00 00            movzx edx, word ptr [rdi + 0x88]
00806982  48 8B CE                        mov rcx, rsi
00806985  E8 32 A5 03 00                  call 0x140840ebc
0080698A  44 8B 68 18                     mov r13d, dword ptr [rax + 0x18]
0080698E  4C 03 EE                        add r13, rsi
00806991  4C 89 AC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r13
00806999  89 9C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ebx
008069A0  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008069A8  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008069AD  44 88 64 24 38                  mov byte ptr [rsp + 0x38], r12b
008069B2  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
008069B7  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008069BC  41 8B 07                        mov eax, dword ptr [r15]
008069BF  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008069C3  4C 8B 4F 18                     mov r9, qword ptr [rdi + 0x18]
008069C7  8B 57 20                        mov edx, dword ptr [rdi + 0x20]
008069CA  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
008069CE  E8 25 A2 03 00                  call 0x140840bf8
008069D3  8B F0                           mov esi, eax
008069D5  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
008069DC  EB 2B                           jmp 0x140806a09
008069DE  8B F0                           mov esi, eax
008069E0  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
008069E7  33 DB                           xor ebx, ebx
008069E9  4C 8B B4 24 60 01 00 00         mov r14, qword ptr [rsp + 0x160]
008069F1  48 8B BC 24 50 01 00 00         mov rdi, qword ptr [rsp + 0x150]
008069F9  44 8A A4 24 68 01 00 00         mov r12b, byte ptr [rsp + 0x168]
00806A01  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
00806A09  85 F6                           test esi, esi
00806A0B  0F 88 91 03 00 00               js 0x140806da2
00806A11  41 8B 07                        mov eax, dword ptr [r15]
00806A14  44 8B AC 24 80 00 00 00         mov r13d, dword ptr [rsp + 0x80]
00806A1C  45 85 ED                        test r13d, r13d
00806A1F  0F 84 90 00 00 00               je 0x140806ab5
00806A25  44 03 E8                        add r13d, eax
00806A28  41 8B CD                        mov ecx, r13d
00806A2B  41 8B C5                        mov eax, r13d
00806A2E  C1 E0 04                        shl eax, 4
00806A31  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00806A39  89 02                           mov dword ptr [rdx], eax
00806A3B  48 C1 E1 03                     shl rcx, 3
00806A3F  48 F7 C1 FF 0F 00 00            test rcx, 0xfff
00806A46  8B D3                           mov edx, ebx
00806A48  0F 95 C2                        setne dl
00806A4B  48 C1 E9 0C                     shr rcx, 0xc
00806A4F  03 D1                           add edx, ecx
00806A51  03 D2                           add edx, edx
00806A53  89 94 24 60 01 00 00            mov dword ptr [rsp + 0x160], edx
00806A5A  4D 8D 46 14                     lea r8, [r14 + 0x14]
00806A5E  4C 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], r8
00806A66  41 8B 08                        mov ecx, dword ptr [r8]
00806A69  3B D1                           cmp edx, ecx
00806A6B  76 5F                           jbe 0x140806acc
00806A6D  8B C2                           mov eax, edx
00806A6F  C1 E0 0C                        shl eax, 0xc
00806A72  3B 05 34 0B 63 00               cmp eax, dword ptr [rip + 0x630b34]
00806A78  76 0A                           jbe 0x140806a84
00806A7A  BE 99 00 00 C0                  mov esi, 0xc0000099
00806A7F  E9 1E 03 00 00                  jmp 0x140806da2
00806A84  44 8B C2                        mov r8d, edx
00806A87  44 2B C1                        sub r8d, ecx
00806A8A  C1 E1 0C                        shl ecx, 0xc
00806A8D  8B D1                           mov edx, ecx
00806A8F  48 03 57 18                     add rdx, qword ptr [rdi + 0x18]
00806A93  48 8B 0F                        mov rcx, qword ptr [rdi]
00806A96  E8 85 C9 E7 FF                  call 0x140683420
00806A9B  8B F0                           mov esi, eax
00806A9D  85 C0                           test eax, eax
00806A9F  0F 88 FD 02 00 00               js 0x140806da2
00806AA5  8B 84 24 60 01 00 00            mov eax, dword ptr [rsp + 0x160]
00806AAC  4D 8D 46 14                     lea r8, [r14 + 0x14]
00806AB0  41 89 00                        mov dword ptr [r8], eax
00806AB3  EB 17                           jmp 0x140806acc
00806AB5  44 8B E8                        mov r13d, eax
00806AB8  4C 8B 84 24 B0 00 00 00         mov r8, qword ptr [rsp + 0xb0]
00806AC0  49 83 C0 14                     add r8, 0x14
00806AC4  4C 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], r8
00806ACC  45 84 E4                        test r12b, r12b
00806ACF  0F 85 BF 00 00 00               jne 0x140806b94
00806AD5  45 3B 2F                        cmp r13d, dword ptr [r15]
00806AD8  76 58                           jbe 0x140806b32
00806ADA  42 8D 14 ED 00 00 00 00         lea edx, [r13*8]
00806AE2  B9 00 01 00 00                  mov ecx, 0x100
00806AE7  41 B8 48 50 55 48               mov r8d, 0x48555048
00806AED  E8 4E 4A B5 FF                  call 0x14035b540
00806AF2  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
00806AFA  48 85 C0                        test rax, rax
00806AFD  0F 84 9F 02 00 00               je 0x140806da2
00806B03  49 8B 56 18                     mov rdx, qword ptr [r14 + 0x18]
00806B07  48 85 D2                        test rdx, rdx
00806B0A  74 22                           je 0x140806b2e
00806B0C  45 8B 07                        mov r8d, dword ptr [r15]
00806B0F  41 C1 E0 03                     shl r8d, 3
00806B13  48 8B C8                        mov rcx, rax
00806B16  E8 25 FD EB FF                  call 0x1406c6840
00806B1B  33 D2                           xor edx, edx
00806B1D  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
00806B21  E8 4A BD 37 00                  call 0x140b82870
00806B26  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
00806B2E  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
00806B32  41 8B C5                        mov eax, r13d
00806B35  24 3F                           and al, 0x3f
00806B37  F6 D8                           neg al
00806B39  1B C9                           sbb ecx, ecx
00806B3B  F7 D9                           neg ecx
00806B3D  8D 51 02                        lea edx, [rcx + 2]
00806B40  41 8B C5                        mov eax, r13d
00806B43  C1 E8 06                        shr eax, 6
00806B46  03 D0                           add edx, eax
00806B48  C1 E2 03                        shl edx, 3
00806B4B  B9 40 00 00 00                  mov ecx, 0x40
00806B50  41 B8 4D 6D 20 20               mov r8d, 0x20206d4d
00806B56  E8 E5 49 B5 FF                  call 0x14035b540
00806B5B  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
00806B5F  48 85 C0                        test rax, rax
00806B62  74 0B                           je 0x140806b6f
00806B64  48 8D 48 10                     lea rcx, [rax + 0x10]
00806B68  44 89 28                        mov dword ptr [rax], r13d
00806B6B  48 89 48 08                     mov qword ptr [rax + 8], rcx
00806B6F  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
00806B73  48 85 C9                        test rcx, rcx
00806B76  0F 84 6E FD FF FF               je 0x1408068ea
00806B7C  E8 AF 96 C4 FF                  call 0x140450230
00806B81  49 8B D6                        mov rdx, r14
00806B84  48 8B CF                        mov rcx, rdi
00806B87  E8 94 03 00 00                  call 0x140806f20
00806B8C  4C 8B 84 24 50 01 00 00         mov r8, qword ptr [rsp + 0x150]
00806B94  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00806B9C  39 18                           cmp dword ptr [rax], ebx
00806B9E  74 19                           je 0x140806bb9
00806BA0  45 8B 00                        mov r8d, dword ptr [r8]
00806BA3  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
00806BA7  48 8B CF                        mov rcx, rdi
00806BAA  E8 51 CC E7 FF                  call 0x140683800
00806BAF  8B F0                           mov esi, eax
00806BB1  85 C0                           test eax, eax
00806BB3  0F 88 E9 01 00 00               js 0x140806da2
00806BB9  89 9C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ebx
00806BC0  48 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdi
00806BC8  41 0F B6 C4                     movzx eax, r12b
00806BCC  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00806BD3  4C 8D 8C 24 98 00 00 00         lea r9, [rsp + 0x98]
00806BDB  4C 8D 05 DE 01 00 00            lea r8, [rip + 0x1de]
00806BE2  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
00806BEA  49 8B D5                        mov rdx, r13
00806BED  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
00806BF5  E8 EE A1 03 00                  call 0x140840de8
00806BFA  48 8B 07                        mov rax, qword ptr [rdi]
00806BFD  48 8B 48 48                     mov rcx, qword ptr [rax + 0x48]
00806C01  48 8B 31                        mov rsi, qword ptr [rcx]
00806C04  F7 46 38 00 00 02 00            test dword ptr [rsi + 0x38], 0x20000
00806C0B  74 3A                           je 0x140806c47
00806C0D  44 8B FB                        mov r15d, ebx
00806C10  48 83 EE 80                     sub rsi, -0x80
00806C14  48 85 F6                        test rsi, rsi
00806C17  74 2E                           je 0x140806c47
00806C19  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00806C1C  0F BA E0 11                     bt eax, 0x11
00806C20  73 14                           jae 0x140806c36
00806C22  44 8B 46 2C                     mov r8d, dword ptr [rsi + 0x2c]
00806C26  41 8B D7                        mov edx, r15d
00806C29  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00806C2D  E8 BE A2 C4 FF                  call 0x140450ef0
00806C32  84 C0                           test al, al
00806C34  74 0A                           je 0x140806c40
00806C36  44 03 7E 2C                     add r15d, dword ptr [rsi + 0x2c]
00806C3A  48 8B 76 10                     mov rsi, qword ptr [rsi + 0x10]
00806C3E  EB D4                           jmp 0x140806c14
00806C40  BE 4E 00 00 C0                  mov esi, 0xc000004e
00806C45  EB 02                           jmp 0x140806c49
00806C47  8B F3                           mov esi, ebx
00806C49  85 F6                           test esi, esi
00806C4B  0F 88 51 01 00 00               js 0x140806da2
00806C51  48 8B B4 24 58 01 00 00         mov rsi, qword ptr [rsp + 0x158]
00806C59  45 84 E4                        test r12b, r12b
00806C5C  0F 85 B3 00 00 00               jne 0x140806d15
00806C62  45 8B 5E 10                     mov r11d, dword ptr [r14 + 0x10]
00806C66  4D 8B 7E 18                     mov r15, qword ptr [r14 + 0x18]
00806C6A  4C 8B 67 18                     mov r12, qword ptr [rdi + 0x18]
00806C6E  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00806C72  48 89 94 24 60 01 00 00         mov qword ptr [rsp + 0x160], rdx
00806C7A  44 8B D3                        mov r10d, ebx
00806C7D  45 3B D3                        cmp r10d, r11d
00806C80  73 32                           jae 0x140806cb4
00806C82  41 8B C2                        mov eax, r10d
00806C85  41 8B 0C C7                     mov ecx, dword ptr [r15 + rax*8]
00806C89  85 C9                           test ecx, ecx
00806C8B  74 18                           je 0x140806ca5
00806C8D  48 03 CA                        add rcx, rdx
00806C90  4D 8B CC                        mov r9, r12
00806C93  E8 90 EB 36 00                  call 0x140b75828
00806C98  41 3B C2                        cmp eax, r10d
00806C9B  75 0D                           jne 0x140806caa
00806C9D  48 8B 94 24 60 01 00 00         mov rdx, qword ptr [rsp + 0x160]
00806CA5  41 FF C2                        inc r10d
00806CA8  EB D3                           jmp 0x140806c7d
00806CAA  BE AC 04 00 C0                  mov esi, 0xc00004ac
00806CAF  E9 EE 00 00 00                  jmp 0x140806da2
00806CB4  88 9C 24 60 01 00 00            mov byte ptr [rsp + 0x160], bl
00806CBB  48 8D 84 24 60 01 00 00         lea rax, [rsp + 0x160]
00806CC3  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00806CC8  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00806CCC  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00806CD1  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00806CD5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00806CDA  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00806CDE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00806CE3  4D 8B C5                        mov r8, r13
00806CE6  48 8B D6                        mov rdx, rsi
00806CE9  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00806CED  E8 2A 35 EA FF                  call 0x1406aa21c
00806CF2  90                              nop
00806CF3  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
00806CF7  E8 34 95 C4 FF                  call 0x140450230
00806CFC  38 9C 24 60 01 00 00            cmp byte ptr [rsp + 0x160], bl
00806D03  74 10                           je 0x140806d15
00806D05  83 8F 9C 00 00 00 01            or dword ptr [rdi + 0x9c], 1
00806D0C  EB 07                           jmp 0x140806d15
00806D0E  8B F0                           mov esi, eax
00806D10  E9 8D 00 00 00                  jmp 0x140806da2
00806D15  44 8B F3                        mov r14d, ebx
00806D18  89 9C 24 60 01 00 00            mov dword ptr [rsp + 0x160], ebx
00806D1F  4C 8B A4 24 B8 00 00 00         mov r12, qword ptr [rsp + 0xb8]
00806D27  49 83 C4 08                     add r12, 8
00806D2B  4C 8D 84 24 60 01 00 00         lea r8, [rsp + 0x160]
00806D33  41 8B D6                        mov edx, r14d
00806D36  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00806D3A  E8 61 89 BC FF                  call 0x1403cf6a0
00806D3F  44 8B F8                        mov r15d, eax
00806D42  48 8B CF                        mov rcx, rdi
00806D45  85 C0                           test eax, eax
00806D47  74 31                           je 0x140806d7a
00806D49  4C 8D 67 08                     lea r12, [rdi + 8]
00806D4D  45 8B C7                        mov r8d, r15d
00806D50  44 8B B4 24 60 01 00 00         mov r14d, dword ptr [rsp + 0x160]
00806D58  41 8B D6                        mov edx, r14d
00806D5B  C1 E2 0C                        shl edx, 0xc
00806D5E  49 03 14 24                     add rdx, qword ptr [r12]
00806D62  E8 99 CA E7 FF                  call 0x140683800
00806D67  8B F0                           mov esi, eax
00806D69  85 C0                           test eax, eax
00806D6B  78 35                           js 0x140806da2
00806D6D  45 03 F7                        add r14d, r15d
00806D70  44 89 B4 24 60 01 00 00         mov dword ptr [rsp + 0x160], r14d
00806D78  EB B1                           jmp 0x140806d2b
00806D7A  E8 B9 F6 FF FF                  call 0x140806438
00806D7F  8B F0                           mov esi, eax
00806D81  85 C0                           test eax, eax
00806D83  78 1D                           js 0x140806da2
00806D85  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
00806D89  48 8B 50 18                     mov rdx, qword ptr [rax + 0x18]
00806D8D  48 89 57 48                     mov qword ptr [rdi + 0x48], rdx
00806D91  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
00806D95  49 2B 0C 24                     sub rcx, qword ptr [r12]
00806D99  48 03 CA                        add rcx, rdx
00806D9C  48 89 4F 50                     mov qword ptr [rdi + 0x50], rcx
00806DA0  8B F3                           mov esi, ebx
00806DA2  8B C6                           mov eax, esi
00806DA4  48 81 C4 10 01 00 00            add rsp, 0x110
00806DAB  41 5F                           pop r15
00806DAD  41 5E                           pop r14
00806DAF  41 5D                           pop r13
00806DB1  41 5C                           pop r12
00806DB3  5F                              pop rdi
00806DB4  5E                              pop rsi
00806DB5  5B                              pop rbx
00806DB6  C3                              ret
00806DB7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPrepareToHotPatchImage(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (272);
    v_stack_m90 = a1;
    *(unsigned __int64 *)(v_rsp - 176) = v_xmm0;
    a2 = 0;
    result = memset(v_rsp - 136, a2, a2 + 72, a4);
    v_rbx = 0;
    if (a3 != 0) goto loc_0080688A;
    v_stack_p18 = v_stack_m88;
    goto loc_0080688D;
loc_0080688A:
loc_0080688D:
    v_stack_p20 = 0;
    v_stack_m98 = v_stack_m88;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))) & (0x3F000ULL));
    result = (unsigned int)(-(result));
    a1 = (unsigned int)(-(v_rsp - 136));
    a1 = (unsigned int)((a1) + (2));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (18));
    a2 = (unsigned int)((a2) + ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) << (3));
    result = MiAllocatePool(256, a2, (unsigned int)(0x20206D4DULL), a4);
    *(unsigned __int64 *)(a1 + 48) = result;
    if (result != 0) {
        a2 = *(unsigned int *)(a1 + 32);
        a2 = (unsigned int)((a2) >> (12));
        a1 = result + 16;
        *(unsigned int *)(result) = (unsigned int)(a2);
        *(unsigned __int64 *)(result + 8) = a1;
    }
    if (*(unsigned __int64 *)(a1 + 48) != 0) goto loc_008068F4;
loc_008068EA:
    goto loc_00806DA2;
loc_008068F4:
    result = RtlSetAllBits(*(unsigned __int64 *)(a1 + 48), a2, (unsigned int)(0x20206D4DULL), a4);
    v_stack_mA0 = v_stack_m88 + 16;
    v_stack_mC0 = a1 + 36;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m88 + 16))) << (4));
    *(unsigned int *)(a1 + 36) = (unsigned int)(result);
    if ((unsigned int)(0xC000009AULL) != 0) goto loc_0080697B;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 16))))) & (63));
    result = (unsigned __int8)(-(result));
    a1 = (unsigned int)(-(a1 + 36));
    a1 = (unsigned int)((a1) + (2));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m88 + 16))) >> (6));
    a2 = (unsigned int)((a2) + ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) << (3));
    result = MiAllocatePool((unsigned int)(0xC000009AULL) + 64, a2, (unsigned int)(0x20206D4DULL), a4);
    *(unsigned __int64 *)(a1 + 40) = result;
    if (result != 0) {
        a1 = *(unsigned int *)(v_stack_m88 + 16);
        a2 = result + 16;
        *(unsigned int *)(result) = (unsigned int)(a1);
        *(unsigned __int64 *)(result + 8) = a2;
    }
    if (*(unsigned __int64 *)(a1 + 40) == 0) goto loc_008068EA;
    result = RtlClearAllBits(*(unsigned __int64 *)(a1 + 40), a2, (unsigned int)(0x20206D4DULL), a4);
    result = MiProcessHotPatchUndoTable(a1, v_stack_m88, (unsigned int)(0x20206D4DULL), a4);
    goto loc_00806C59;
loc_0080697B:
    result = RtlFindHotPatchBaseMachine((unsigned int)(0xC000009AULL), *(unsigned __int16 *)(a1 + 136), (unsigned int)(0x20206D4DULL), a4);
    v_r13 = ((unsigned int)(*(unsigned int *)(result + 24))) + ((unsigned int)(0xC000009AULL));
    v_stack_mB8 = v_r13;
    v_stack_mC8 = 0;
    v_stack_mD8 = v_stack_mC8;
    v_stack_m110 = 0;
    v_stack_m118 = v_r13;
    v_stack_m120 = (unsigned int)(0xC000009AULL);
    v_stack_m128 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 16)));
    result = RtlCountRequiredHotPatchAddressTableEntries(*(unsigned __int64 *)(a1 + 8), (unsigned int)(*(unsigned int *)(a1 + 32)), (unsigned int)(0x20206D4DULL), *(unsigned __int64 *)(a1 + 24));
    v_stack_mC4 = (unsigned int)(result);
    goto loc_00806A09;
loc_00806A09:
    if (sign_flag) goto loc_00806DA2;
    if ((unsigned int)((unsigned int)(v_stack_mC8)) == 0) goto loc_00806AB5;
    v_r13 = (unsigned int)(((unsigned int)(v_stack_mC8)) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 16)))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) << (4));
    *(unsigned int *)(v_stack_mC0) = (unsigned int)(result);
    a1 = ((unsigned int)((unsigned int)(v_r13))) << (3);
    a2 = (((a1) & (0xFFFULL)) != 0) ? 1 : 0;
    a1 = (a1) >> (12);
    a2 = (unsigned int)((a2) + ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) + ((unsigned int)(a2)));
    v_stack_p18 = (unsigned int)(a2);
    v_stack_p8 = v_stack_m88 + 20;
    if (((unsigned int)(a2)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 20))))) goto loc_00806ACC;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) << (12));
    if (((unsigned int)(result)) <= (*(unsigned int *)(v_rip + 6490932))) goto loc_00806A84;
    goto loc_00806DA2;
loc_00806A84:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 20)))));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m88 + 20))) << (12));
    a2 = ((unsigned int)((unsigned int)(a1))) + (*(unsigned __int64 *)(a1 + 24));
    result = MiCommitHotPatchTable(*(unsigned __int64 *)(a1), a2, a3, *(unsigned __int64 *)(a1 + 24));
    if (sign_flag) goto loc_00806DA2;
    *(unsigned int *)(v_stack_m88 + 20) = (unsigned int)((unsigned int)(v_stack_p18));
    goto loc_00806ACC;
loc_00806AB5:
    a3 = (v_stack_m98) + (20);
    v_stack_p8 = a3;
loc_00806ACC:
    if (0 != 0) goto loc_00806B94;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) <= (*(unsigned int *)(v_stack_m88 + 16))) goto loc_00806B32;
    result = MiAllocatePool(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))) * 8, (unsigned int)(0x48555048ULL), *(unsigned __int64 *)(a1 + 24));
    v_stack_p18 = result;
    if (result == 0) goto loc_00806DA2;
    if (*(unsigned __int64 *)(v_stack_m88 + 24) != 0) {
        a3 = *(unsigned int *)(v_stack_m88 + 16);
        a3 = (unsigned int)((a3) << (3));
        a1 = result;
        result = memcpy(a1, *(unsigned __int64 *)(v_stack_m88 + 24), a3, *(unsigned __int64 *)(a1 + 24));
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_stack_m88 + 24);
        result = ExFreePoolWithTag(a1, a2, a3, *(unsigned __int64 *)(a1 + 24));
        result = v_stack_p18;
    }
    *(unsigned __int64 *)(v_stack_m88 + 24) = result;
loc_00806B32:
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))))) & (63));
    result = (unsigned __int8)(-(result));
    a1 = (unsigned int)(-(a1));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))))) >> (6));
    a2 = (unsigned int)((a1 + 2) + ((unsigned int)(result)));
    a2 = (unsigned int)((a2) << (3));
    result = MiAllocatePool(64, a2, (unsigned int)(0x20206D4DULL), *(unsigned __int64 *)(a1 + 24));
    *(unsigned __int64 *)(a1 + 40) = result;
    if (result != 0) {
        a1 = result + 16;
        *(unsigned int *)(result) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))));
        *(unsigned __int64 *)(result + 8) = a1;
    }
    if (*(unsigned __int64 *)(a1 + 40) == 0) goto loc_008068EA;
    result = RtlClearAllBits(*(unsigned __int64 *)(a1 + 40), a2, (unsigned int)(0x20206D4DULL), *(unsigned __int64 *)(a1 + 24));
    result = MiProcessHotPatchUndoTable(a1, v_stack_m88, (unsigned int)(0x20206D4DULL), *(unsigned __int64 *)(a1 + 24));
loc_00806B94:
    if ((*(unsigned int *)(v_stack_mC0)) == 0) goto loc_00806BB9;
    result = MiPrepareImagePagesForHotPatch(a1, *(unsigned __int64 *)(a1 + 24), (unsigned int)(*(unsigned int *)(v_stack_p8)), *(unsigned __int64 *)(a1 + 24));
    if (sign_flag) goto loc_00806DA2;
loc_00806BB9:
    v_stack_mA4 = 0;
    v_stack_mB0 = a1;
    v_stack_mA8 = 0;
    result = RtlEnumerateHotPatchPatches(v_stack_p10, v_stack_mB8, v_rip + 478, v_stack_mB0);
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 72)) + 56)) & (0x20000ULL)) == 0) goto loc_00806C47;
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 72))) - (-128);
loc_00806C14:
    if (v_rsi == 0) goto loc_00806C47;
    if (condition_is_above_or_equal) goto loc_00806C36;
    result = RtlAreBitsSet(*(unsigned __int64 *)(a1 + 48), 0, (unsigned int)(*(unsigned int *)(v_rsi + 44)), v_stack_mB0);
    if ((unsigned __int8)(result) == 0) goto loc_00806C40;
loc_00806C36:
    v_r15 = (unsigned int)((0) + (*(unsigned int *)(v_rsi + 44)));
    goto loc_00806C14;
loc_00806C40:
    goto loc_00806C49;
loc_00806C47:
loc_00806C49:
    if (sign_flag) goto loc_00806DA2;
loc_00806C59:
    if (0 != 0) goto loc_00806D15;
    v_stack_p18 = *(unsigned __int64 *)(a1 + 8);
loc_00806C7D:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 16))))) goto loc_00806CB4;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m88 + 24) + 0 * 8))) == 0) goto loc_00806CA5;
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m88 + 24) + 0 * 8))) + (*(unsigned __int64 *)(a1 + 8));
    result = RtlpCheckFunctionPatchApplied(a1, *(unsigned __int64 *)(a1 + 8), (unsigned int)(*(unsigned int *)(v_rsi + 44)), *(unsigned __int64 *)(a1 + 24));
    if (((unsigned int)(result)) != 0) goto loc_00806CAA;
loc_00806CA5:
    v_r10 = (unsigned int)((0) + 1);
    goto loc_00806C7D;
loc_00806CAA:
    goto loc_00806DA2;
loc_00806CB4:
    v_stack_p18 = 0;
    v_stack_mE0 = v_stack_p18;
    v_stack_m110 = *(unsigned __int64 *)(a1 + 40);
    v_stack_m118 = *(unsigned __int64 *)(v_stack_m88 + 24);
    v_stack_m120 = *(unsigned __int64 *)(a1 + 24);
    result = RtlHotPatchSynchronizationRequired(*(unsigned __int64 *)(a1 + 8), (unsigned int)(0xC00004ACULL), v_stack_mB8, *(unsigned __int64 *)(a1 + 24));
    result = RtlClearAllBits(*(unsigned __int64 *)(a1 + 40), (unsigned int)(0xC00004ACULL), v_stack_mB8, *(unsigned __int64 *)(a1 + 24));
    if (v_stack_p18 == 0) goto loc_00806D15;
    goto loc_00806D15;
loc_00806D15:
    v_stack_p18 = 0;
    v_r12 = (v_stack_m90) + (8);
loc_00806D2B:
    result = RtlFindNextForwardRunClear(*(unsigned __int64 *)(a1 + 48), 0, v_stack_p18, *(unsigned __int64 *)(a1 + 24));
    if ((unsigned int)(result) == 0) goto loc_00806D7A;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))) << (12));
    a2 = (a2) + (*(unsigned __int64 *)(a1 + 8));
    result = MiPrepareImagePagesForHotPatch(a1, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(a1 + 24));
    if (sign_flag) goto loc_00806DA2;
    v_r14 = (unsigned int)(((unsigned int)(v_stack_p18)) + ((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_stack_p18 = (unsigned int)(v_r14);
    goto loc_00806D2B;
loc_00806D7A:
    result = MiMapHotPatchImageInSystemSpace(a1, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(a1 + 24));
    v_rsi = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        result = *(unsigned __int64 *)(a1 + 64);
        a2 = *(unsigned __int64 *)(result + 24);
        *(unsigned __int64 *)(a1 + 72) = a2;
        a1 = *(unsigned __int64 *)(a1 + 24);
        a1 = (a1) - (*(unsigned __int64 *)(a1 + 8));
        a1 = (a1) + (a2);
        *(unsigned __int64 *)(a1 + 80) = a1;
        v_rsi = 0;
    }
    v_rsp = (v_rsp) + (272);
    return (unsigned int)((unsigned int)(v_rsi));
}
```

## 5. (Beta) C Style

```c
int64_t MiPrepareToHotPatchImage(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m128;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (272);
    v_stack_m90 = Arg1;
    *(uint64_t *)(local_rsp - 0xB0) = v_xmm0;
    Arg2 = 0;
    result = memset(local_rsp - 136, Arg2, Arg2 + 72, a4);
    local_rbx = 0;
    if (Arg3 != 0) goto loc_0080688A;
    v_stack_p18 = v_stack_m88;
    goto loc_0080688D;
loc_0080688A:
loc_0080688D:
    v_stack_p20 = 0;
    v_stack_m98 = v_stack_m88;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) & (0x3F000ULL));
    result = (uint32_t)(-(result));
    Arg1 = (uint32_t)(-(local_rsp - 136));
    Arg1 = (uint32_t)((Arg1) + (2));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (18));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) << (3));
    result = MiAllocatePool(256, Arg2, (uint32_t)(0x20206D4DULL), a4);
    *(uint64_t *)(arg1 + 0x30) = result;
    if (result != 0) {
        Arg2 = *(uint32_t *)(arg1 + 0x20);
        Arg2 = (uint32_t)((Arg2) >> (12));
        Arg1 = result + 16;
        *(uint32_t *)(result) = (uint32_t)(Arg2);
        *(void **)(result + 0x8) = Arg1;
    }
    if (*(uint64_t *)(arg1 + 0x30) != 0) goto loc_008068F4;
loc_008068EA:
    goto loc_00806DA2;
loc_008068F4:
    result = RtlSetAllBits(*(uint64_t *)(arg1 + 0x30), Arg2, (uint32_t)(0x20206D4DULL), a4);
    v_stack_mA0 = v_stack_m88 + 16;
    v_stack_mC0 = Arg1 + 36;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x10))) << (4));
    *(uint32_t *)(arg1 + 0x24) = (uint32_t)(result);
    if ((uint32_t)(0xC000009AULL) != 0) goto loc_0080697B;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x10))))) & (63));
    result = (uint8_t)(-(result));
    Arg1 = (uint32_t)(-(Arg1 + 36));
    Arg1 = (uint32_t)((Arg1) + (2));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x10))) >> (6));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) << (3));
    result = MiAllocatePool((uint32_t)(0xC000009AULL) + 64, Arg2, (uint32_t)(0x20206D4DULL), a4);
    *(uint64_t *)(arg1 + 0x28) = result;
    if (result != 0) {
        Arg1 = *(uint32_t *)(v_stack_m88 + 0x10);
        Arg2 = result + 16;
        *(uint32_t *)(result) = (uint32_t)(Arg1);
        *(uint64_t *)(result + 0x8) = Arg2;
    }
    if (*(uint64_t *)(arg1 + 0x28) == 0) goto loc_008068EA;
    result = RtlClearAllBits(*(uint64_t *)(arg1 + 0x28), Arg2, (uint32_t)(0x20206D4DULL), a4);
    result = MiProcessHotPatchUndoTable(Arg1, v_stack_m88, (uint32_t)(0x20206D4DULL), a4);
    goto loc_00806C59;
loc_0080697B:
    result = RtlFindHotPatchBaseMachine((uint32_t)(0xC000009AULL), *(uint16_t *)(arg1 + 0x88), (uint32_t)(0x20206D4DULL), a4);
    local_r13 = ((uint32_t)(*(uint32_t *)(result + 0x18))) + ((uint32_t)(0xC000009AULL));
    v_stack_mB8 = local_r13;
    v_stack_mC8 = 0;
    v_stack_mD8 = v_stack_mC8;
    v_stack_m110 = 0;
    v_stack_m118 = local_r13;
    v_stack_m120 = (uint32_t)(0xC000009AULL);
    v_stack_m128 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x10)));
    result = RtlCountRequiredHotPatchAddressTableEntries(*(uint64_t *)(arg1 + 0x8), (uint32_t)(*(uint32_t *)(arg1 + 0x20)), (uint32_t)(0x20206D4DULL), *(uint64_t *)(arg1 + 0x18));
    v_stack_mC4 = (uint32_t)(result);
    goto loc_00806A09;
loc_00806A09:
    if (sign_flag) goto loc_00806DA2;
    if ((uint32_t)((uint32_t)(v_stack_mC8)) == 0) goto loc_00806AB5;
    local_r13 = (uint32_t)(((uint32_t)(v_stack_mC8)) + ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x10)))));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) << (4));
    *(uint32_t *)(v_stack_mC0) = (uint32_t)(result);
    Arg1 = ((uint32_t)((uint32_t)(local_r13))) << (3);
    Arg2 = (((Arg1) & (0xFFFULL)) != 0) ? 1 : 0;
    Arg1 = (Arg1) >> (12);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg2)));
    v_stack_p18 = (uint32_t)(Arg2);
    v_stack_p8 = v_stack_m88 + 20;
    if (((uint32_t)(Arg2)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x14))))) goto loc_00806ACC;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) << (12));
    if (((uint32_t)(result)) <= (*(uint32_t *)(v_rip + 0x630B34))) goto loc_00806A84;
    goto loc_00806DA2;
loc_00806A84:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x14)))));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x14))) << (12));
    Arg2 = ((uint32_t)((uint32_t)(Arg1))) + (*(uint64_t *)(arg1 + 0x18));
    result = MiCommitHotPatchTable(*(uint64_t *)(arg1), Arg2, Arg3, *(uint64_t *)(arg1 + 0x18));
    if (sign_flag) goto loc_00806DA2;
    *(uint32_t *)(v_stack_m88 + 0x14) = (uint32_t)((uint32_t)(v_stack_p18));
    goto loc_00806ACC;
loc_00806AB5:
    Arg3 = (v_stack_m98) + (20);
    v_stack_p8 = Arg3;
loc_00806ACC:
    if (0 != 0) goto loc_00806B94;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) <= (*(uint32_t *)(v_stack_m88 + 0x10))) goto loc_00806B32;
    result = MiAllocatePool(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))) * 8, (uint32_t)(0x48555048ULL), *(uint64_t *)(arg1 + 0x18));
    v_stack_p18 = result;
    if (result == 0) goto loc_00806DA2;
    if (*(uint64_t *)(v_stack_m88 + 0x18) != 0) {
        Arg3 = *(uint32_t *)(v_stack_m88 + 0x10);
        Arg3 = (uint32_t)((Arg3) << (3));
        Arg1 = result;
        result = memcpy(Arg1, *(uint64_t *)(v_stack_m88 + 0x18), Arg3, *(uint64_t *)(arg1 + 0x18));
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_stack_m88 + 0x18);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, *(uint64_t *)(arg1 + 0x18));
        result = v_stack_p18;
    }
    *(uint64_t *)(v_stack_m88 + 0x18) = result;
loc_00806B32:
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))))) & (63));
    result = (uint8_t)(-(result));
    Arg1 = (uint32_t)(-(Arg1));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))))) >> (6));
    Arg2 = (uint32_t)((Arg1 + 2) + ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) << (3));
    result = MiAllocatePool(64, Arg2, (uint32_t)(0x20206D4DULL), *(uint64_t *)(arg1 + 0x18));
    *(uint64_t *)(arg1 + 0x28) = result;
    if (result != 0) {
        Arg1 = result + 16;
        *(uint32_t *)(result) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))));
        *(void **)(result + 0x8) = Arg1;
    }
    if (*(uint64_t *)(arg1 + 0x28) == 0) goto loc_008068EA;
    result = RtlClearAllBits(*(uint64_t *)(arg1 + 0x28), Arg2, (uint32_t)(0x20206D4DULL), *(uint64_t *)(arg1 + 0x18));
    result = MiProcessHotPatchUndoTable(Arg1, v_stack_m88, (uint32_t)(0x20206D4DULL), *(uint64_t *)(arg1 + 0x18));
loc_00806B94:
    if ((*(uint32_t *)(v_stack_mC0)) == 0) goto loc_00806BB9;
    result = MiPrepareImagePagesForHotPatch(Arg1, *(uint64_t *)(arg1 + 0x18), (uint32_t)(*(uint32_t *)(v_stack_p8)), *(uint64_t *)(arg1 + 0x18));
    if (sign_flag) goto loc_00806DA2;
loc_00806BB9:
    v_stack_mA4 = 0;
    v_stack_mB0 = Arg1;
    v_stack_mA8 = 0;
    result = RtlEnumerateHotPatchPatches(v_stack_p10, v_stack_mB8, v_rip + 478, v_stack_mB0);
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x48)) + 0x38)) & (0x20000ULL)) == 0) goto loc_00806C47;
    local_rsi = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x48))) - (-128);
loc_00806C14:
    if (local_rsi == 0) goto loc_00806C47;
    if (condition_is_above_or_equal) goto loc_00806C36;
    result = RtlAreBitsSet(*(uint64_t *)(arg1 + 0x30), 0, (uint32_t)(*(uint32_t *)(local_rsi + 0x2C)), v_stack_mB0);
    if ((uint8_t)(result) == 0) goto loc_00806C40;
loc_00806C36:
    local_r15 = (uint32_t)((0) + (*(uint32_t *)(local_rsi + 0x2C)));
    goto loc_00806C14;
loc_00806C40:
    goto loc_00806C49;
loc_00806C47:
loc_00806C49:
    if (sign_flag) goto loc_00806DA2;
loc_00806C59:
    if (0 != 0) goto loc_00806D15;
    v_stack_p18 = *(uint64_t *)(arg1 + 0x8);
loc_00806C7D:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x10))))) goto loc_00806CB4;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m88 + 0x18) + 0x0 * 8))) == 0) goto loc_00806CA5;
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m88 + 0x18) + 0x0 * 8))) + (*(uint64_t *)(arg1 + 0x8));
    result = RtlpCheckFunctionPatchApplied(Arg1, *(uint64_t *)(arg1 + 0x8), (uint32_t)(*(uint32_t *)(local_rsi + 0x2C)), *(uint64_t *)(arg1 + 0x18));
    if (((uint32_t)(result)) != 0) goto loc_00806CAA;
loc_00806CA5:
    local_r10 = (uint32_t)((0) + 1);
    goto loc_00806C7D;
loc_00806CAA:
    goto loc_00806DA2;
loc_00806CB4:
    v_stack_p18 = 0;
    v_stack_mE0 = v_stack_p18;
    v_stack_m110 = *(uint64_t *)(arg1 + 0x28);
    v_stack_m118 = *(uint64_t *)(v_stack_m88 + 0x18);
    v_stack_m120 = *(uint64_t *)(arg1 + 0x18);
    result = RtlHotPatchSynchronizationRequired(*(uint64_t *)(arg1 + 0x8), (uint32_t)(0xC00004ACULL), v_stack_mB8, *(uint64_t *)(arg1 + 0x18));
    result = RtlClearAllBits(*(uint64_t *)(arg1 + 0x28), (uint32_t)(0xC00004ACULL), v_stack_mB8, *(uint64_t *)(arg1 + 0x18));
    if (v_stack_p18 == 0) goto loc_00806D15;
    goto loc_00806D15;
loc_00806D15:
    v_stack_p18 = 0;
    local_r12 = (v_stack_m90) + (8);
loc_00806D2B:
    result = RtlFindNextForwardRunClear(*(uint64_t *)(arg1 + 0x30), 0, v_stack_p18, *(uint64_t *)(arg1 + 0x18));
    if ((uint32_t)(result) == 0) goto loc_00806D7A;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))) << (12));
    Arg2 = (Arg2) + (*(uint64_t *)(arg1 + 0x8));
    result = MiPrepareImagePagesForHotPatch(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(arg1 + 0x18));
    if (sign_flag) goto loc_00806DA2;
    local_r14 = (uint32_t)(((uint32_t)(v_stack_p18)) + ((uint32_t)((uint32_t)((uint32_t)(result)))));
    v_stack_p18 = (uint32_t)(local_r14);
    goto loc_00806D2B;
loc_00806D7A:
    result = MiMapHotPatchImageInSystemSpace(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(arg1 + 0x18));
    local_rsi = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        result = *(uint64_t *)(arg1 + 0x40);
        Arg2 = *(uint64_t *)(result + 0x18);
        *(uint64_t *)(arg1 + 0x48) = Arg2;
        Arg1 = *(uint64_t *)(arg1 + 0x18);
        Arg1 = (Arg1) - (*(uint64_t *)(arg1 + 0x8));
        Arg1 = (Arg1) + (Arg2);
        *(void **)(arg1 + 0x50) = Arg1;
        local_rsi = 0;
    }
    local_rsp = (local_rsp) + (272);
    return (uint32_t)((uint32_t)(local_rsi));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x24` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `W` |
| `Arg1` | `+ 0x50` | `64` | `W` |
| `Arg1` | `+ 0x88` | `16` | `R` |
| `Arg1` | `+ 0x9C` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00806820&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
