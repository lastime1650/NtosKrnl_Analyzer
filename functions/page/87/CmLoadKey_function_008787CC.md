# CmLoadKey

- RVA: `0x008787CC`–`0x0087908D` (길이 `2,241` bytes)
- VA: `0x00000001408787CC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006CC90`
- 디코드: `476`개 명령, `2,241/2,241` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x008788A8` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x008788CF` → [CmpQueryHiveRedirectionFileList](CmpQueryHiveRedirectionFileList_function_00879094.md) (function, `0x00879094`)
- `0x008788DC` → [CmpAcquireHiveLoadUnloadRundown](../../pagecmrc/BC/CmpAcquireHiveLoadUnloadRundown_function_00BC9C6C.md) (function, `0x00BC9C6C`)
- `0x0087891A` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x0087899F` → [CmpCmdHiveOpen](CmpCmdHiveOpen_function_00878404.md) (function, `0x00878404`)
- `0x00878A16` → [CmpLoadKeyCommon](../../text/46/CmpLoadKeyCommon_function_0046E9F8.md) (function, `0x0046E9F8`)
- `0x00878A37` → [CmpReleaseHiveLoadUnloadRundown](../../pagecmrc/BC/CmpReleaseHiveLoadUnloadRundown_function_00BC9CAC.md) (function, `0x00BC9CAC`)
- `0x00878A40` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00878A5E` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00878A6F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00878C65` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (function, `0x002F0F7C`)
- `0x00878DB3` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00878E5F` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (function, `0x002F0F7C`)
- `0x00878E84` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00878ED4` → [CmpOpenHiveFile](CmpOpenHiveFile_function_0087A71C.md) (function, `0x0087A71C`)
- `0x00878F08` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00878F13` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00878F59` → [CmpResolveHiveLoadConflict](../A9/CmpResolveHiveLoadConflict_function_00A9E78C.md) (function, `0x00A9E78C`)
- `0x00878F65` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00878F8E` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00879047` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x00879055` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x0087905D` → [CmpDestroyHive](../9B/CmpDestroyHive_function_009B1708.md) (function, `0x009B1708`)
- `0x00879066` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)

### Direct callers
- [CmLoadDifferencingKey](CmLoadDifferencingKey_function_00875670.md) at `0x00876192`

### Static image references
- `0x008787EB` → RVA `0x00E0A740` (`.data`; read)
- `0x00878A49` → RVA `0x00E09F58` (`.data`; read)
- `0x00878AE8` → RVA `0x00E09F70` (`.data`; read)
- `0x00878B03` → RVA `0x00E09F68` (`.data`; read)
- `0x00878BCB` → RVA `0x0005670B` (`.rdata`; read)
- `0x00878D1B` → RVA `0x0005696E` (`.rdata`; read)
- `0x00878DFF` → RVA `0x0005691B` (`.rdata`; read)
- `0x00878EE3` → RVA `0x00EF7C68` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x008788A8` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x008788DC` → [CmpAcquireHiveLoadUnloadRundown](../../pagecmrc/BC/CmpAcquireHiveLoadUnloadRundown_function_00BC9C6C.md) (`PAGE` → `PAGECMRC`)
  - `0x0087891A` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x00878A16` → [CmpLoadKeyCommon](../../text/46/CmpLoadKeyCommon_function_0046E9F8.md) (`PAGE` → `.text`)
  - `0x00878A37` → [CmpReleaseHiveLoadUnloadRundown](../../pagecmrc/BC/CmpReleaseHiveLoadUnloadRundown_function_00BC9CAC.md) (`PAGE` → `PAGECMRC`)
  - `0x00878A40` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00878A5E` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00878A6F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00878C65` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (`PAGE` → `.text`)
  - `0x00878DB3` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00878E5F` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (`PAGE` → `.text`)
  - `0x00878E84` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00878F13` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00878F65` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00878F8E` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00879047` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x00879055` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x00879066` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x008789B6` → [sub_00B17DB0](../B1/Unknown_function_00B17DB0.md) (`tail-transfer`)
  - `0x00878AC9` → [sub_00B17DB0 + 0xD6](../B1/Unknown_function_00B17DB0.md) (`tail-transfer`)
  - `0x00878FEC` → [sub_00B17DB0 + 0xD6](../B1/Unknown_function_00B17DB0.md) (`tail-transfer`)
  - `0x00878FF6` → [sub_00B17DB0 + 0xD6](../B1/Unknown_function_00B17DB0.md) (`tail-transfer`)
  - `0x00879082` → [sub_00B17DB0 + 0xD6](../B1/Unknown_function_00B17DB0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008787CC  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
008787D1  55                              push rbp
008787D2  56                              push rsi
008787D3  57                              push rdi
008787D4  41 54                           push r12
008787D6  41 55                           push r13
008787D8  41 56                           push r14
008787DA  41 57                           push r15
008787DC  48 8D AC 24 C0 FE FF FF         lea rbp, [rsp - 0x140]
008787E4  48 81 EC 40 02 00 00            sub rsp, 0x240
008787EB  48 8B 05 4E 1F 59 00            mov rax, qword ptr [rip + 0x591f4e]
008787F2  48 33 C4                        xor rax, rsp
008787F5  48 89 85 30 01 00 00            mov qword ptr [rbp + 0x130], rax
008787FC  48 8B 85 A0 01 00 00            mov rax, qword ptr [rbp + 0x1a0]
00878803  45 33 ED                        xor r13d, r13d
00878806  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0087880A  0F 57 C0                        xorps xmm0, xmm0
0087880D  48 8B 85 A8 01 00 00            mov rax, qword ptr [rbp + 0x1a8]
00878814  4C 8B F9                        mov r15, rcx
00878817  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0087881B  45 8B E0                        mov r12d, r8d
0087881E  48 8B 85 B8 01 00 00            mov rax, qword ptr [rbp + 0x1b8]
00878825  41 8D 5D 02                     lea ebx, [r13 + 2]
00878829  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0087882D  48 8B F2                        mov rsi, rdx
00878830  48 8B 85 C0 01 00 00            mov rax, qword ptr [rbp + 0x1c0]
00878837  41 8B FD                        mov edi, r13d
0087883A  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0087883E  48 8B 85 D0 01 00 00            mov rax, qword ptr [rbp + 0x1d0]
00878845  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00878849  48 8B 85 D8 01 00 00            mov rax, qword ptr [rbp + 0x1d8]
00878850  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00878854  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00878858  44 88 6C 24 64                  mov byte ptr [rsp + 0x64], r13b
0087885D  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00878861  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
00878866  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0087886A  4C 89 6D 80                     mov qword ptr [rbp - 0x80], r13
0087886E  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00878872  44 89 6C 24 78                  mov dword ptr [rsp + 0x78], r13d
00878877  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0087887B  0F B7 08                        movzx ecx, word ptr [rax]
0087887E  66 3B CB                        cmp cx, bx
00878881  0F 83 09 02 00 00               jae 0x140878a90
00878887  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
0087888B  41 BE 01 00 00 00               mov r14d, 1
00878891  66 39 18                        cmp word ptr [rax], bx
00878894  0F 82 4D 07 00 00               jb 0x140878fe7
0087889A  BA 04 01 00 00                  mov edx, 0x104
0087889F  41 B8 43 4D 53 62               mov r8d, 0x62534d43
008788A5  8D 4A FC                        lea ecx, [rdx - 4]
008788A8  E8 57 4C B5 FF                  call 0x1403cd504
008788AD  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
008788B1  48 85 C0                        test rax, rax
008788B4  0F 84 37 07 00 00               je 0x140878ff1
008788BA  B9 04 01 00 00                  mov ecx, 0x104
008788BF  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
008788C3  66 89 4D C2                     mov word ptr [rbp - 0x3e], cx
008788C7  48 8D 55 C0                     lea rdx, [rbp - 0x40]
008788CB  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
008788CF  E8 C0 07 00 00                  call 0x140879094
008788D4  84 C0                           test al, al
008788D6  0F 85 1F 07 00 00               jne 0x140878ffb
008788DC  E8 8B 13 35 00                  call 0x140bc9c6c
008788E1  84 C0                           test al, al
008788E3  0F 84 AD 05 00 00               je 0x140878e96
008788E9  45 8B EC                        mov r13d, r12d
008788EC  BA B0 01 00 00                  mov edx, 0x1b0
008788F1  41 81 E5 00 20 00 00            and r13d, 0x2000
008788F8  41 B8 43 4D 39 33               mov r8d, 0x33394d43
008788FE  41 8B C5                        mov eax, r13d
00878901  F7 D8                           neg eax
00878903  1B C9                           sbb ecx, ecx
00878905  83 E1 03                        and ecx, 3
00878908  8B D9                           mov ebx, ecx
0087890A  83 CB 08                        or ebx, 8
0087890D  41 0F BA E4 0E                  bt r12d, 0xe
00878912  0F 43 D9                        cmovae ebx, ecx
00878915  B9 00 01 00 00                  mov ecx, 0x100
0087891A  E8 E5 4B B5 FF                  call 0x1403cd504
0087891F  48 8B F8                        mov rdi, rax
00878922  48 85 C0                        test rax, rax
00878925  0F 84 92 04 00 00               je 0x140878dbd
0087892B  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00878930  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
00878935  8B D3                           mov edx, ebx
00878937  44 88 74 24 60                  mov byte ptr [rsp + 0x60], r14b
0087893C  83 CA 04                        or edx, 4
0087893F  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00878944  48 83 7D 90 00                  cmp qword ptr [rbp - 0x70], 0
00878949  41 8B CC                        mov ecx, r12d
0087894C  41 8B C4                        mov eax, r12d
0087894F  0F 44 D3                        cmove edx, ebx
00878952  83 E1 04                        and ecx, 4
00878955  C1 E1 06                        shl ecx, 6
00878958  83 E0 20                        and eax, 0x20
0087895B  0B C8                           or ecx, eax
0087895D  41 8B C4                        mov eax, r12d
00878960  03 C9                           add ecx, ecx
00878962  25 80 04 00 00                  and eax, 0x480
00878967  0B C8                           or ecx, eax
00878969  41 8B C4                        mov eax, r12d
0087896C  03 C9                           add ecx, ecx
0087896E  25 23 F2 FF FF                  and eax, 0xfffff223
00878973  0B C8                           or ecx, eax
00878975  48 8D 44 24 64                  lea rax, [rsp + 0x64]
0087897A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0087897F  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00878983  C1 E1 13                        shl ecx, 0x13
00878986  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0087898B  81 C9 01 00 19 01               or ecx, 0x1190001
00878991  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00878995  41 8A D6                        mov dl, r14b
00878998  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
0087899C  48 8B CE                        mov rcx, rsi
0087899F  E8 60 FA FF FF                  call 0x140878404
008789A4  8B D8                           mov ebx, eax
008789A6  85 C0                           test eax, eax
008789A8  0F 88 BB 04 00 00               js 0x140878e69
008789AE  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
008789B3  45 85 ED                        test r13d, r13d
008789B6  0F 85 F4 F3 29 00               jne 0x140b17db0
008789BC  44 8A AD C8 01 00 00            mov r13b, byte ptr [rbp + 0x1c8]
008789C3  80 BD B0 01 00 00 00            cmp byte ptr [rbp + 0x1b0], 0
008789CA  74 08                           je 0x1408789d4
008789CC  0F BA AE 10 10 00 00 0D         bts dword ptr [rsi + 0x1010], 0xd
008789D4  8A 44 24 64                     mov al, byte ptr [rsp + 0x64]
008789D8  45 8B C4                        mov r8d, r12d
008789DB  4C 8B 4D A8                     mov r9, qword ptr [rbp - 0x58]
008789DF  49 8B D7                        mov rdx, r15
008789E2  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
008789E7  48 8B CE                        mov rcx, rsi
008789EA  88 44 24 48                     mov byte ptr [rsp + 0x48], al
008789EE  8A 44 24 60                     mov al, byte ptr [rsp + 0x60]
008789F2  88 44 24 40                     mov byte ptr [rsp + 0x40], al
008789F6  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
008789FA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008789FF  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00878A03  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
00878A08  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00878A0D  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00878A11  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00878A16  E8 DD 5F BF FF                  call 0x14046e9f8
00878A1B  45 33 ED                        xor r13d, r13d
00878A1E  8B D8                           mov ebx, eax
00878A20  41 8B F5                        mov esi, r13d
00878A23  85 C0                           test eax, eax
00878A25  0F 88 08 06 00 00               js 0x140879033
00878A2B  41 8B DD                        mov ebx, r13d
00878A2E  48 85 F6                        test rsi, rsi
00878A31  0F 85 1A 06 00 00               jne 0x140879051
00878A37  E8 70 12 35 00                  call 0x140bc9cac
00878A3C  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
00878A40  E8 3B D3 BF FF                  call 0x140475d80
00878A45  85 DB                           test ebx, ebx
00878A47  78 7D                           js 0x140878ac6
00878A49  83 3D 08 15 59 00 05            cmp dword ptr [rip + 0x591508], 5
00878A50  0F 87 74 03 00 00               ja 0x140878dca
00878A56  48 85 FF                        test rdi, rdi
00878A59  74 08                           je 0x140878a63
00878A5B  48 8B CF                        mov rcx, rdi
00878A5E  E8 1D D3 BF FF                  call 0x140475d80
00878A63  8B C3                           mov eax, ebx
00878A65  48 8B 8D 30 01 00 00            mov rcx, qword ptr [rbp + 0x130]
00878A6C  48 33 CC                        xor rcx, rsp
00878A6F  E8 CC 3B E3 FF                  call 0x1406ac640
00878A74  48 8B 9C 24 98 02 00 00         mov rbx, qword ptr [rsp + 0x298]
00878A7C  48 81 C4 40 02 00 00            add rsp, 0x240
00878A83  41 5F                           pop r15
00878A85  41 5E                           pop r14
00878A87  41 5D                           pop r13
00878A89  41 5C                           pop r12
00878A8B  5F                              pop rdi
00878A8C  5E                              pop rsi
00878A8D  5D                              pop rbp
00878A8E  C3                              ret
00878A8F  CC                              int3
00878A90  8B D1                           mov edx, ecx
00878A92  D1 EA                           shr edx, 1
00878A94  0F 84 ED FD FF FF               je 0x140878887
00878A9A  4D 8B 47 10                     mov r8, qword ptr [r15 + 0x10]
00878A9E  8D 42 FF                        lea eax, [rdx - 1]
00878AA1  8B C8                           mov ecx, eax
00878AA3  8B D0                           mov edx, eax
00878AA5  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
00878AA9  66 83 3C 48 5C                  cmp word ptr [rax + rcx*2], 0x5c
00878AAE  0F 85 D3 FD FF FF               jne 0x140878887
00878AB4  B8 FE FF 00 00                  mov eax, 0xfffe
00878AB9  66 41 01 00                     add word ptr [r8], ax
00878ABD  85 D2                           test edx, edx
00878ABF  75 D9                           jne 0x140878a9a
00878AC1  E9 C1 FD FF FF                  jmp 0x140878887
00878AC6  48 85 FF                        test rdi, rdi
00878AC9  0F 84 B7 F3 29 00               je 0x140b17e86
00878ACF  48 8D 77 08                     lea rsi, [rdi + 8]
00878AD3  44 0F B7 1E                     movzx r11d, word ptr [rsi]
00878AD7  66 45 85 DB                     test r11w, r11w
00878ADB  0F 84 8F 05 00 00               je 0x140879070
00878AE1  44 8B 05 70 14 59 00            mov r8d, dword ptr [rip + 0x591470]
00878AE8  48 8B 0D 81 14 59 00            mov rcx, qword ptr [rip + 0x591481]
00878AEF  41 83 F8 05                     cmp r8d, 5
00878AF3  0F 86 62 FF FF FF               jbe 0x140878a5b
00878AF9  48 BA 08 00 00 00 00 40 00 00   movabs rdx, 0x400000000008
00878B03  48 85 15 5E 14 59 00            test qword ptr [rip + 0x59145e], rdx
00878B0A  0F 85 8D 04 00 00               jne 0x140878f9d
00878B10  41 8A C5                        mov al, r13b
00878B13  84 C0                           test al, al
00878B15  0F 84 5D 01 00 00               je 0x140878c78
00878B1B  48 8D 57 0A                     lea rdx, [rdi + 0xa]
00878B1F  4C 89 75 88                     mov qword ptr [rbp - 0x78], r14
00878B23  44 0F B7 0A                     movzx r9d, word ptr [rdx]
00878B27  4C 8D 87 8A 01 00 00            lea r8, [rdi + 0x18a]
00878B2E  45 0F B6 10                     movzx r10d, byte ptr [r8]
00878B32  43 8D 0C 5B                     lea ecx, [r11 + r11*2]
00878B36  C1 E1 02                        shl ecx, 2
00878B39  48 8D 45 88                     lea rax, [rbp - 0x78]
00878B3D  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00878B41  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00878B46  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00878B4A  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00878B4F  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00878B53  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00878B58  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00878B5C  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00878B61  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00878B65  48 8D 47 0C                     lea rax, [rdi + 0xc]
00878B69  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00878B70  48 8D 47 6C                     lea rax, [rdi + 0x6c]
00878B74  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
00878B7B  43 8D 04 49                     lea eax, [r9 + r9*2]
00878B7F  C1 E0 02                        shl eax, 2
00878B82  89 85 A8 00 00 00               mov dword ptr [rbp + 0xa8], eax
00878B88  48 8D 87 8C 01 00 00            lea rax, [rdi + 0x18c]
00878B8F  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00878B96  48 8D 45 90                     lea rax, [rbp - 0x70]
00878B9A  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00878BA1  48 8D 45 00                     lea rax, [rbp]
00878BA5  66 44 89 54 24 78               mov word ptr [rsp + 0x78], r10w
00878BAB  66 44 89 4C 24 68               mov word ptr [rsp + 0x68], r9w
00878BB1  41 B9 0E 00 00 00               mov r9d, 0xe
00878BB7  89 8D 88 00 00 00               mov dword ptr [rbp + 0x88], ecx
00878BBD  48 8D 0D 94 13 59 00            lea rcx, [rip + 0x591394]
00878BC4  48 89 95 90 00 00 00            mov qword ptr [rbp + 0x90], rdx
00878BCB  48 8D 15 39 DB 7D FF            lea rdx, [rip - 0x8224c7]
00878BD2  41 C1 E2 03                     shl r10d, 3
00878BD6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00878BDB  48 C7 45 28 08 00 00 00         mov qword ptr [rbp + 0x28], 8
00878BE3  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
00878BE7  48 C7 45 38 04 00 00 00         mov qword ptr [rbp + 0x38], 4
00878BEF  66 44 89 5C 24 60               mov word ptr [rsp + 0x60], r11w
00878BF5  48 C7 45 48 02 00 00 00         mov qword ptr [rbp + 0x48], 2
00878BFD  48 C7 45 58 02 00 00 00         mov qword ptr [rbp + 0x58], 2
00878C05  48 C7 45 68 02 00 00 00         mov qword ptr [rbp + 0x68], 2
00878C0D  48 89 75 70                     mov qword ptr [rbp + 0x70], rsi
00878C11  48 C7 45 78 02 00 00 00         mov qword ptr [rbp + 0x78], 2
00878C19  44 89 AD 8C 00 00 00            mov dword ptr [rbp + 0x8c], r13d
00878C20  48 C7 85 98 00 00 00 02 00 00 00  mov qword ptr [rbp + 0x98], 2
00878C2B  44 89 AD AC 00 00 00            mov dword ptr [rbp + 0xac], r13d
00878C32  4C 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], r8
00878C39  48 C7 85 B8 00 00 00 02 00 00 00  mov qword ptr [rbp + 0xb8], 2
00878C44  44 89 95 C8 00 00 00            mov dword ptr [rbp + 0xc8], r10d
00878C4B  44 89 AD CC 00 00 00            mov dword ptr [rbp + 0xcc], r13d
00878C52  48 C7 45 90 00 00 00 01         mov qword ptr [rbp - 0x70], 0x1000000
00878C5A  48 C7 85 D8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xd8], 8
00878C65  E8 12 83 A7 FF                  call 0x1402f0f7c
00878C6A  48 8B 0D FF 12 59 00            mov rcx, qword ptr [rip + 0x5912ff]
00878C71  44 8B 05 E0 12 59 00            mov r8d, dword ptr [rip + 0x5912e0]
00878C78  41 83 F8 05                     cmp r8d, 5
00878C7C  0F 86 D9 FD FF FF               jbe 0x140878a5b
00878C82  F6 05 DF 12 59 00 08            test byte ptr [rip + 0x5912df], 8
00878C89  0F 85 44 03 00 00               jne 0x140878fd3
00878C8F  45 8A F5                        mov r14b, r13b
00878C92  45 84 F6                        test r14b, r14b
00878C95  0F 84 C0 FD FF FF               je 0x140878a5b
00878C9B  0F B7 16                        movzx edx, word ptr [rsi]
00878C9E  48 8D 4F 0A                     lea rcx, [rdi + 0xa]
00878CA2  44 0F B7 09                     movzx r9d, word ptr [rcx]
00878CA6  4C 8D 87 8A 01 00 00            lea r8, [rdi + 0x18a]
00878CAD  45 0F B6 10                     movzx r10d, byte ptr [r8]
00878CB1  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00878CB6  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00878CBA  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00878CBF  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00878CC3  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00878CC8  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00878CCC  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00878CD1  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00878CD5  48 8D 47 0C                     lea rax, [rdi + 0xc]
00878CD9  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00878CDD  8D 04 52                        lea eax, [rdx + rdx*2]
00878CE0  C1 E0 02                        shl eax, 2
00878CE3  89 45 78                        mov dword ptr [rbp + 0x78], eax
00878CE6  48 8D 47 6C                     lea rax, [rdi + 0x6c]
00878CEA  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
00878CF1  43 8D 04 49                     lea eax, [r9 + r9*2]
00878CF5  C1 E0 02                        shl eax, 2
00878CF8  89 85 98 00 00 00               mov dword ptr [rbp + 0x98], eax
00878CFE  48 8D 87 8C 01 00 00            lea rax, [rdi + 0x18c]
00878D05  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00878D0C  48 8D 45 00                     lea rax, [rbp]
00878D10  66 44 89 54 24 60               mov word ptr [rsp + 0x60], r10w
00878D16  66 89 54 24 78                  mov word ptr [rsp + 0x78], dx
00878D1B  48 8D 15 4C DC 7D FF            lea rdx, [rip - 0x8223b4]
00878D22  66 44 89 4C 24 68               mov word ptr [rsp + 0x68], r9w
00878D28  45 33 C9                        xor r9d, r9d
00878D2B  48 89 8D 80 00 00 00            mov qword ptr [rbp + 0x80], rcx
00878D32  48 8D 0D 1F 12 59 00            lea rcx, [rip + 0x59121f]
00878D39  4C 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], r8
00878D40  45 33 C0                        xor r8d, r8d
00878D43  41 C1 E2 03                     shl r10d, 3
00878D47  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00878D4C  C7 44 24 20 0C 00 00 00         mov dword ptr [rsp + 0x20], 0xc
00878D54  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
00878D58  48 C7 45 28 04 00 00 00         mov qword ptr [rbp + 0x28], 4
00878D60  48 C7 45 38 02 00 00 00         mov qword ptr [rbp + 0x38], 2
00878D68  48 C7 45 48 02 00 00 00         mov qword ptr [rbp + 0x48], 2
00878D70  48 C7 45 58 02 00 00 00         mov qword ptr [rbp + 0x58], 2
00878D78  48 89 75 60                     mov qword ptr [rbp + 0x60], rsi
00878D7C  48 C7 45 68 02 00 00 00         mov qword ptr [rbp + 0x68], 2
00878D84  44 89 6D 7C                     mov dword ptr [rbp + 0x7c], r13d
00878D88  48 C7 85 88 00 00 00 02 00 00 00  mov qword ptr [rbp + 0x88], 2
00878D93  44 89 AD 9C 00 00 00            mov dword ptr [rbp + 0x9c], r13d
00878D9A  48 C7 85 A8 00 00 00 02 00 00 00  mov qword ptr [rbp + 0xa8], 2
00878DA5  44 89 95 B8 00 00 00            mov dword ptr [rbp + 0xb8], r10d
00878DAC  44 89 AD BC 00 00 00            mov dword ptr [rbp + 0xbc], r13d
00878DB3  E8 28 D3 BA FF                  call 0x1404260e0
00878DB8  E9 9E FC FF FF                  jmp 0x140878a5b
00878DBD  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00878DC2  45 33 ED                        xor r13d, r13d
00878DC5  E9 6D FC FF FF                  jmp 0x140878a37
00878DCA  48 BA 08 00 00 00 00 40 00 00   movabs rdx, 0x400000000008
00878DD4  48 85 15 8D 11 59 00            test qword ptr [rip + 0x59118d], rdx
00878DDB  0F 85 D3 01 00 00               jne 0x140878fb4
00878DE1  41 8A C5                        mov al, r13b
00878DE4  84 C0                           test al, al
00878DE6  0F 84 6A FC FF FF               je 0x140878a56
00878DEC  48 8D 45 88                     lea rax, [rbp - 0x78]
00878DF0  48 C7 45 90 00 00 00 01         mov qword ptr [rbp - 0x70], 0x1000000
00878DF8  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
00878DFF  48 8D 15 15 DB 7D FF            lea rdx, [rip - 0x8224eb]
00878E06  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00878E0B  48 C7 85 28 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x128], 8
00878E16  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
00878E1D  41 B9 05 00 00 00               mov r9d, 5
00878E23  48 8D 45 90                     lea rax, [rbp - 0x70]
00878E27  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
00878E2E  48 8D 85 E0 00 00 00            lea rax, [rbp + 0xe0]
00878E35  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00878E3A  48 8D 0D 17 11 59 00            lea rcx, [rip + 0x591117]
00878E41  4C 89 75 88                     mov qword ptr [rbp - 0x78], r14
00878E45  48 C7 85 08 01 00 00 08 00 00 00  mov qword ptr [rbp + 0x108], 8
00878E50  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
00878E54  48 C7 85 18 01 00 00 04 00 00 00  mov qword ptr [rbp + 0x118], 4
00878E5F  E8 18 81 A7 FF                  call 0x1402f0f7c
00878E64  E9 ED FB FF FF                  jmp 0x140878a56
00878E69  33 D2                           xor edx, edx
00878E6B  3D 43 00 00 C0                  cmp eax, 0xc0000043
00878E70  74 2E                           je 0x140878ea0
00878E72  44 8B C8                        mov r9d, eax
00878E75  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
00878E7D  44 8D 42 1F                     lea r8d, [rdx + 0x1f]
00878E81  48 8B CF                        mov rcx, rdi
00878E84  E8 CB 60 BF FF                  call 0x14046ef54
00878E89  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00878E8E  45 33 ED                        xor r13d, r13d
00878E91  E9 98 FB FF FF                  jmp 0x140878a2e
00878E96  BB 89 01 00 C0                  mov ebx, 0xc0000189
00878E9B  E9 9C FB FF FF                  jmp 0x140878a3c
00878EA0  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00878EA4  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
00878EA9  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00878EAE  4C 8D 45 80                     lea r8, [rbp - 0x80]
00878EB2  45 33 ED                        xor r13d, r13d
00878EB5  48 8B CE                        mov rcx, rsi
00878EB8  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00878EBD  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00878EC2  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
00878EC7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00878ECC  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
00878ED4  E8 43 18 00 00                  call 0x14087a71c
00878ED9  33 D2                           xor edx, edx
00878EDB  85 C0                           test eax, eax
00878EDD  0F 88 2C 01 00 00               js 0x14087900f
00878EE3  48 8B 05 7E ED 67 00            mov rax, qword ptr [rip + 0x67ed7e]
00878EEA  45 33 C9                        xor r9d, r9d
00878EED  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00878EF1  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00878EF6  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
00878EFB  4C 8B 00                        mov r8, qword ptr [rax]
00878EFE  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00878F03  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00878F08  E8 A3 FE FE FF                  call 0x140868db0
00878F0D  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00878F11  8B D8                           mov ebx, eax
00878F13  E8 98 43 E3 FF                  call 0x1406ad2b0
00878F18  85 DB                           test ebx, ebx
00878F1A  0F 88 FC 00 00 00               js 0x14087901c
00878F20  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
00878F24  45 8B C4                        mov r8d, r12d
00878F27  4C 8B 4D A8                     mov r9, qword ptr [rbp - 0x58]
00878F2B  49 8B CF                        mov rcx, r15
00878F2E  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00878F33  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00878F38  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00878F3C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00878F41  8A 85 C8 01 00 00               mov al, byte ptr [rbp + 0x1c8]
00878F47  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00878F4B  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00878F4F  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00878F54  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00878F59  E8 2E 58 22 00                  call 0x140a9e78c
00878F5E  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00878F63  8B D8                           mov ebx, eax
00878F65  E8 E6 03 A8 FF                  call 0x1402f9350
00878F6A  85 DB                           test ebx, ebx
00878F6C  0F 89 B7 00 00 00               jns 0x140879029
00878F72  C7 44 24 20 40 00 00 00         mov dword ptr [rsp + 0x20], 0x40
00878F7A  33 D2                           xor edx, edx
00878F7C  41 B9 43 00 00 C0               mov r9d, 0xc0000043
00878F82  41 B8 1F 00 00 00               mov r8d, 0x1f
00878F88  48 8B CF                        mov rcx, rdi
00878F8B  41 8B D9                        mov ebx, r9d
00878F8E  E8 C1 5F BF FF                  call 0x14046ef54
00878F93  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00878F98  E9 91 FA FF FF                  jmp 0x140878a2e
00878F9D  48 8B C1                        mov rax, rcx
00878FA0  48 23 C2                        and rax, rdx
00878FA3  48 3B C1                        cmp rax, rcx
00878FA6  41 8A C6                        mov al, r14b
00878FA9  0F 85 61 FB FF FF               jne 0x140878b10
00878FAF  E9 5F FB FF FF                  jmp 0x140878b13
00878FB4  48 8B 05 B5 0F 59 00            mov rax, qword ptr [rip + 0x590fb5]
00878FBB  48 23 C2                        and rax, rdx
00878FBE  48 3B 05 AB 0F 59 00            cmp rax, qword ptr [rip + 0x590fab]
00878FC5  41 8A C6                        mov al, r14b
00878FC8  0F 85 13 FE FF FF               jne 0x140878de1
00878FCE  E9 11 FE FF FF                  jmp 0x140878de4
00878FD3  48 8B C1                        mov rax, rcx
00878FD6  83 E0 08                        and eax, 8
00878FD9  48 3B C1                        cmp rax, rcx
00878FDC  0F 85 AD FC FF FF               jne 0x140878c8f
00878FE2  E9 AB FC FF FF                  jmp 0x140878c92
00878FE7  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00878FEC  E9 95 EE 29 00                  jmp 0x140b17e86
00878FF1  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00878FF6  E9 8B EE 29 00                  jmp 0x140b17e86
00878FFB  66 39 5D C0                     cmp word ptr [rbp - 0x40], bx
00878FFF  48 8D 45 C0                     lea rax, [rbp - 0x40]
00879003  48 0F 44 C6                     cmove rax, rsi
00879007  48 8B F0                        mov rsi, rax
0087900A  E9 CD F8 FF FF                  jmp 0x1408788dc
0087900F  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
00879017  E9 60 FF FF FF                  jmp 0x140878f7c
0087901C  C7 44 24 20 30 00 00 00         mov dword ptr [rsp + 0x20], 0x30
00879024  E9 51 FF FF FF                  jmp 0x140878f7a
00879029  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0087902E  E9 F8 F9 FF FF                  jmp 0x140878a2b
00879033  33 D2                           xor edx, edx
00879035  C7 44 24 20 70 00 00 00         mov dword ptr [rsp + 0x20], 0x70
0087903D  44 8B C8                        mov r9d, eax
00879040  48 8B CF                        mov rcx, rdi
00879043  44 8D 42 1F                     lea r8d, [rdx + 0x1f]
00879047  E8 08 5F BF FF                  call 0x14046ef54
0087904C  E9 E6 F9 FF FF                  jmp 0x140878a37
00879051  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00879055  E8 86 08 35 00                  call 0x140bc98e0
0087905A  48 8B CE                        mov rcx, rsi
0087905D  E8 A6 86 13 00                  call 0x1409b1708
00879062  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00879066  E8 B5 08 35 00                  call 0x140bc9920
0087906B  E9 C7 F9 FF FF                  jmp 0x140878a37
00879070  66 44 39 6F 0A                  cmp word ptr [rdi + 0xa], r13w
00879075  0F 85 66 FA FF FF               jne 0x140878ae1
0087907B  44 38 AF 8A 01 00 00            cmp byte ptr [rdi + 0x18a], r13b
00879082  0F 84 FE ED 29 00               je 0x140b17e86
00879088  E9 54 FA FF FF                  jmp 0x140878ae1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmLoadKey(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, unsigned __int8 a7, __int64 a8, __int64 a9, unsigned __int8 a10, __int64 a11, __int64 a12)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int16 v_stack_m1B6;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned int v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int8 v_stack_m214;
    unsigned __int8 v_stack_m218;
    unsigned __int64 v_stack_m228;
    unsigned __int8 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m250;
    unsigned int v_stack_m258;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (576);
    result = (*(unsigned __int64 *)(v_rip + 5840718)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r13 = 0;
    v_stack_m1D0 = a5;
    v_stack_m1E8 = a6;
    v_stack_m1D8 = a8;
    v_stack_m1C8 = a9;
    v_stack_m1C0 = a11;
    v_stack_m1E0 = a12;
    v_stack_m214 = 0;
    v_stack_m1B8 = v_xmm0;
    v_stack_m208 = 0;
    v_stack_m1A8 = v_xmm0;
    v_stack_m1F8 = 0;
    v_stack_m198 = v_xmm0;
    v_stack_m200 = 0;
    v_stack_m188 = v_xmm0;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 16)))) >= ((unsigned __int16)(v_r13 + 2))) goto loc_00878A90;
loc_00878887:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 16))) < ((unsigned __int16)(v_r13 + 2))) goto loc_00878FE7;
    result = CmpAllocatePool(260 - 4, 260, (unsigned int)(0x62534D43ULL), a4);
    v_stack_m1F0 = result;
    if (result == 0) goto loc_00878FF1;
    v_stack_m1B0 = result;
    v_stack_m1B6 = 260;
    result = CmpQueryHiveRedirectionFileList(*(unsigned __int64 *)(a1 + 16), v_stack_m1B8, (unsigned int)(0x62534D43ULL), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00878FFB;
loc_008788DC:
    result = CmpAcquireHiveLoadUnloadRundown(*(unsigned __int64 *)(a1 + 16), v_stack_m1B8, (unsigned int)(0x62534D43ULL), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00878E96;
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (0x2000ULL));
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_r13))));
    a1 = (unsigned int)((*(unsigned __int64 *)(a1 + 16)) & (3));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (8));
    if (condition_is_above_or_equal) { v_rbx = (unsigned int)(a1); }
    result = CmpAllocatePool(256, 432, (unsigned int)(0x33394D43ULL), a4);
    if (result == 0) goto loc_00878DBD;
    v_stack_m238 = result;
    v_stack_m218 = 1;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) | (4));
    if (v_stack_m1E8 == 0) { a2 = (unsigned int)(v_rbx); }
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (4));
    a1 = (unsigned int)((a1) << (6));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (32));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    a1 = (unsigned int)((a1) + ((unsigned int)(a1)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (0x480ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    a1 = (unsigned int)((a1) + ((unsigned int)(a1)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (0xFFFFF223ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    v_stack_m240 = v_stack_m214;
    a1 = (unsigned int)((a1) << (19));
    v_stack_m248 = v_stack_m1C8;
    a1 = (unsigned int)((a1) | (0x1190001ULL));
    v_stack_m250 = (unsigned int)(a2);
    v_stack_m258 = (unsigned int)(a1);
    result = CmpCmdHiveOpen(a2, 1, v_stack_m218, v_stack_m208);
    if (sign_flag) goto loc_00878E69;
    if (a7 != 0) {
    }
    v_stack_m228 = result;
    v_stack_m230 = (unsigned __int8)(v_stack_m214);
    v_stack_m238 = (unsigned __int8)(v_stack_m218);
    v_stack_m240 = v_stack_m1E0;
    v_stack_m248 = a10;
    v_stack_m250 = v_stack_m1D8;
    v_stack_m258 = v_stack_m1E8;
    result = CmpLoadKeyCommon(v_stack_m208, a1, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m1D0);
    v_r13 = 0;
    if (sign_flag) goto loc_00879033;
loc_00878A2B:
loc_00878A2E:
    if (0 != 0) goto loc_00879051;
loc_00878A37:
    result = CmpReleaseHiveLoadUnloadRundown(v_stack_m208, a1, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m1D0);
loc_00878A3C:
    result = CmSiFreeMemory(v_stack_m1F0, a1, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m1D0);
    if (sign_flag) goto loc_00878AC6;
    if ((*(unsigned int *)(v_rip + 5838088)) > 5) goto loc_00878DCA;
loc_00878A56:
    if (result != 0) {
        a1 = result;
        result = CmSiFreeMemory(a1, a1, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m1D0);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a1, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m1D0);
    v_rsp = (v_rsp) + (576);
    return result;
loc_00878A90:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) >> (1));
    if (condition_is_equal) goto loc_00878887;
loc_00878A9A:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + (unsigned int)((unsigned int)(a2 - 1)) * 2)) != 92) goto loc_00878887;
    if ((unsigned int)((unsigned int)((unsigned int)(a2 - 1))) != 0) goto loc_00878A9A;
    goto loc_00878887;
loc_00878AC6:
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 8)) == 0) goto loc_00879070;
loc_00878AE1:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5837936)))) <= 5) goto loc_00878A5B;
    if (((*(unsigned __int64 *)(v_rip + 5837918)) & ((unsigned int)((unsigned int)(a2 - 1)))) != 0) goto loc_00878F9D;
loc_00878B10:
loc_00878B13:
    result = 0;
    if (0 != 0) {
        a2 = result + 10;
        v_stack_m1F0 = 1;
        a4 = *(unsigned __int16 *)(a2);
        a3 = result + 394;
        v_r10 = *(unsigned __int8 *)(a3);
        a1 = *(unsigned __int16 *)(result + 8) + *(unsigned __int16 *)(result + 8) * 2;
        a1 = (unsigned int)((a1) << (2));
        result = v_stack_m1F0;
        v_stack_m158 = result;
        result = v_stack_p70;
        v_stack_m148 = result;
        result = v_stack_p60;
        v_stack_m138 = result;
        result = v_stack_p68;
        v_stack_m128 = result;
        result = v_stack_p78;
        v_stack_m118 = result;
        result = result + 12;
        v_stack_mF8 = result;
        result = result + 108;
        v_stack_mD8 = result;
        result = a4 + a4 * 2;
        result = (unsigned int)((result) << (2));
        v_stack_mD0 = (unsigned int)(result);
        result = result + 396;
        v_stack_mB8 = result;
        result = v_stack_m1E8;
        v_stack_mA8 = result;
        result = v_stack_m178;
        v_stack_p78 = (unsigned __int16)(v_r10);
        v_stack_p68 = (unsigned __int16)(a4);
        a4 = 14;
        v_stack_mF0 = (unsigned int)(a1);
        a1 = v_rip + 5837716;
        v_stack_mE8 = a2;
        a2 = v_rip - 8529095;
        v_r10 = (unsigned int)((v_r10) << (3));
        v_stack_p20 = result;
        v_stack_m150 = 8;
        v_stack_p70 = (unsigned int)(v_stack_p20);
        v_stack_m140 = 4;
        v_stack_p60 = (unsigned __int16)(*(unsigned __int16 *)(result + 8));
        v_stack_m130 = 2;
        v_stack_m120 = 2;
        v_stack_m110 = 2;
        v_stack_m108 = result + 8;
        v_stack_m100 = 2;
        v_stack_mEC = 0;
        v_stack_mE0 = 2;
        v_stack_mCC = 0;
        v_stack_mC8 = a3;
        v_stack_mC0 = 2;
        v_stack_mB0 = (unsigned int)(v_r10);
        v_stack_mAC = 0;
        v_stack_m1E8 = 0x1000000ULL;
        v_stack_mA0 = 8;
        result = tlgWriteAgg(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rip + 5837567);
        a3 = *(unsigned int *)(v_rip + 5837536);
    }
    if (a3 <= 5) goto loc_00878A5B;
    if (((*(unsigned __int8 *)(v_rip + 5837535)) & (8)) != 0) goto loc_00878FD3;
loc_00878C8F:
loc_00878C92:
    if (0 == 0) goto loc_00878A5B;
    v_stack_m158 = v_stack_p70;
    v_stack_m148 = v_stack_p78;
    v_stack_m138 = v_stack_p68;
    v_stack_m128 = v_stack_p60;
    v_stack_m108 = result + 12;
    result = (unsigned int)((*(unsigned __int16 *)(result + 8) + *(unsigned __int16 *)(result + 8) * 2) << (2));
    v_stack_m100 = (unsigned int)(result);
    v_stack_mE8 = result + 108;
    result = (unsigned int)((*(unsigned __int16 *)(result + 10) + *(unsigned __int16 *)(result + 10) * 2) << (2));
    v_stack_mE0 = (unsigned int)(result);
    v_stack_mC8 = result + 396;
    v_stack_p60 = (unsigned __int16)(*(unsigned __int8 *)(result + 394));
    v_stack_p78 = (unsigned __int16)(*(unsigned __int16 *)(result + 8));
    v_stack_p68 = (unsigned __int16)(*(unsigned __int16 *)(result + 10));
    a4 = 0;
    v_stack_mF8 = result + 10;
    v_stack_mD8 = result + 394;
    a3 = 0;
    v_r10 = (unsigned int)((*(unsigned __int8 *)(result + 394)) << (3));
    v_stack_p28 = v_stack_m178;
    v_stack_p20 = 12;
    v_stack_p70 = (unsigned int)(v_stack_p20);
    v_stack_m150 = 4;
    v_stack_m140 = 2;
    v_stack_m130 = 2;
    v_stack_m120 = 2;
    v_stack_m118 = result + 8;
    v_stack_m110 = 2;
    v_stack_mFC = 0;
    v_stack_mF0 = 2;
    v_stack_mDC = 0;
    v_stack_mD0 = 2;
    v_stack_mC0 = (unsigned int)(v_r10);
    v_stack_mBC = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 5837343, v_rip - 8528820, a3, a4);
    goto loc_00878A5B;
loc_00878DBD:
    v_r13 = 0;
    goto loc_00878A37;
loc_00878DCA:
    if (((*(unsigned __int64 *)(v_rip + 5837197)) & (v_rip - 8528820)) != 0) goto loc_00878FB4;
loc_00878DE1:
loc_00878DE4:
    if (0 == 0) goto loc_00878A56;
    v_stack_m1E8 = 0x1000000ULL;
    v_stack_m78 = v_stack_m1F0;
    v_stack_m50 = 8;
    v_stack_m68 = v_stack_p70;
    v_stack_m58 = v_stack_m1E8;
    v_stack_p20 = v_stack_m98;
    v_stack_m1F0 = 0;
    v_stack_m70 = 8;
    v_stack_p70 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_m60 = 4;
    result = tlgWriteAgg(v_rip + 5837079, v_rip - 8529131, a3, 5);
    goto loc_00878A56;
loc_00878E69:
    a2 = 0;
    if (((unsigned int)(result)) == 0xC0000043ULL) goto loc_00878EA0;
    v_stack_p20 = 16;
    result = SetFailureLocation(result, a2, a2 + 31, (unsigned int)((unsigned int)(result)));
    v_r13 = 0;
    goto loc_00878A2E;
loc_00878E96:
    goto loc_00878A3C;
loc_00878EA0:
    v_stack_p48 = result;
    v_r13 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_m1C8;
    v_stack_p20 = 8;
    result = CmpOpenHiveFile(v_stack_p70, a2, v_stack_m1F8, v_stack_p78);
    a2 = 0;
    if (sign_flag) goto loc_0087900F;
    a4 = 0;
    v_stack_p28 = 0;
    v_stack_p78 = 0;
    v_stack_p20 = v_stack_p78;
    result = ObReferenceObjectByHandle(v_stack_m1F8, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6811006)), a4);
    result = ZwClose(v_stack_m1F8, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6811006)), a4);
    if (sign_flag) goto loc_0087901C;
    v_stack_p40 = v_stack_m1E0;
    v_stack_p38 = v_stack_m1C0;
    v_stack_p30 = a10;
    v_stack_p28 = result;
    v_stack_p20 = v_stack_m1D8;
    result = CmpResolveHiveLoadConflict(a1, v_stack_p78, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m1D0);
    result = ObfDereferenceObject(v_stack_p78, v_stack_p78, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m1D0);
    if (!sign_flag) goto loc_00879029;
    v_stack_p20 = 64;
loc_00878F7A:
    a2 = 0;
loc_00878F7C:
    result = SetFailureLocation(result, a2, 31, (unsigned int)(0xC0000043ULL));
    goto loc_00878A2E;
loc_00878F9D:
    result = (result) & (0);
    if (result != result) goto loc_00878B10;
    goto loc_00878B13;
loc_00878FB4:
    result = (*(unsigned __int64 *)(v_rip + 5836725)) & (0);
    if (result != (*(unsigned __int64 *)(v_rip + 5836715))) goto loc_00878DE1;
    goto loc_00878DE4;
loc_00878FD3:
    result = (unsigned int)((result) & (8));
    if (result != result) goto loc_00878C8F;
    goto loc_00878C92;
loc_00878FE7:
loc_00878FF1:
loc_00878FFB:
    result = v_stack_m1B8;
    if (v_stack_m1B8 == ((unsigned __int16)((unsigned int)(0xC000009AULL)))) { result = v_stack_p70; }
    goto loc_008788DC;
loc_0087900F:
    v_stack_p20 = 32;
    goto loc_00878F7C;
loc_0087901C:
    v_stack_p20 = 48;
    goto loc_00878F7A;
loc_00879029:
    goto loc_00878A2B;
loc_00879033:
    a2 = 0;
    v_stack_p20 = 112;
    result = SetFailureLocation(result, a2, a2 + 31, (unsigned int)((unsigned int)(result)));
    goto loc_00878A37;
loc_00879051:
    result = CmpAttachToRegistryProcess(v_stack_m1A8, a2, a2 + 31, (unsigned int)((unsigned int)(result)));
    result = CmpDestroyHive(v_stack_p70, a2, a2 + 31, (unsigned int)((unsigned int)(result)));
    result = CmpDetachFromRegistryProcess(v_stack_m1A8, a2, a2 + 31, (unsigned int)((unsigned int)(result)));
    goto loc_00878A37;
loc_00879070:
    if ((*(unsigned __int16 *)(result + 10)) != 0) goto loc_00878AE1;
    goto loc_00878AE1;
}
```

## 5. (Beta) C Style

```c
int64_t CmLoadKey(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint8_t Arg7, int64_t Arg8, int64_t Arg9, uint8_t Arg10, int64_t Arg11, int64_t Arg12)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m178;
    uint64_t v_stack_m188;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint16_t v_stack_m1B6;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint32_t v_stack_m200;
    uint64_t v_stack_m208;
    uint8_t v_stack_m214;
    uint8_t v_stack_m218;
    uint64_t v_stack_m228;
    uint8_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint32_t v_stack_m250;
    uint32_t v_stack_m258;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (576);
    result = (*(uint64_t *)(v_rip + 0x591F4E)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r13 = 0;
    v_stack_m1D0 = Arg5;
    v_stack_m1E8 = Arg6;
    v_stack_m1D8 = Arg8;
    v_stack_m1C8 = Arg9;
    v_stack_m1C0 = Arg11;
    v_stack_m1E0 = Arg12;
    v_stack_m214 = 0;
    v_stack_m1B8 = v_xmm0;
    v_stack_m208 = 0;
    v_stack_m1A8 = v_xmm0;
    v_stack_m1F8 = 0;
    v_stack_m198 = v_xmm0;
    v_stack_m200 = 0;
    v_stack_m188 = v_xmm0;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x10)))) >= ((uint16_t)(local_r13 + 2))) goto loc_00878A90;
loc_00878887:
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x10))) < ((uint16_t)(local_r13 + 2))) goto loc_00878FE7;
    result = CmpAllocatePool(260 - 4, 260, (uint32_t)(0x62534D43ULL), Arg4);
    v_stack_m1F0 = result;
    if (result == 0) goto loc_00878FF1;
    v_stack_m1B0 = result;
    v_stack_m1B6 = 260;
    result = CmpQueryHiveRedirectionFileList(*(uint64_t *)(arg1 + 0x10), v_stack_m1B8, (uint32_t)(0x62534D43ULL), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00878FFB;
loc_008788DC:
    result = CmpAcquireHiveLoadUnloadRundown(*(uint64_t *)(arg1 + 0x10), v_stack_m1B8, (uint32_t)(0x62534D43ULL), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00878E96;
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (0x2000ULL));
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_r13))));
    Arg1 = (uint32_t)((*(uint64_t *)(arg1 + 0x10)) & (3));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (8));
    if (condition_is_above_or_equal) { local_rbx = (uint32_t)(Arg1); }
    result = CmpAllocatePool(256, 432, (uint32_t)(0x33394D43ULL), Arg4);
    if (result == 0) goto loc_00878DBD;
    v_stack_m238 = result;
    v_stack_m218 = 1;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) | (4));
    if (v_stack_m1E8 == 0) { Arg2 = (uint32_t)(local_rbx); }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (4));
    Arg1 = (uint32_t)((Arg1) << (6));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (32));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (0x480ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (0xFFFFF223ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    v_stack_m240 = v_stack_m214;
    Arg1 = (uint32_t)((Arg1) << (19));
    v_stack_m248 = v_stack_m1C8;
    Arg1 = (uint32_t)((Arg1) | (0x1190001ULL));
    v_stack_m250 = (uint32_t)(Arg2);
    v_stack_m258 = (uint32_t)(Arg1);
    result = CmpCmdHiveOpen(Arg2, 1, v_stack_m218, v_stack_m208);
    if (sign_flag) goto loc_00878E69;
    if (Arg7 != 0) {
    }
    v_stack_m228 = result;
    v_stack_m230 = (uint8_t)(v_stack_m214);
    v_stack_m238 = (uint8_t)(v_stack_m218);
    v_stack_m240 = v_stack_m1E0;
    v_stack_m248 = Arg10;
    v_stack_m250 = v_stack_m1D8;
    v_stack_m258 = v_stack_m1E8;
    result = CmpLoadKeyCommon(v_stack_m208, Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m1D0);
    local_r13 = 0;
    if (sign_flag) goto loc_00879033;
loc_00878A2B:
loc_00878A2E:
    if (0 != 0) goto loc_00879051;
loc_00878A37:
    result = CmpReleaseHiveLoadUnloadRundown(v_stack_m208, Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m1D0);
loc_00878A3C:
    result = CmSiFreeMemory(v_stack_m1F0, Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m1D0);
    if (sign_flag) goto loc_00878AC6;
    if ((*(uint32_t *)(v_rip + 0x591508)) > 5) goto loc_00878DCA;
loc_00878A56:
    if (result != 0) {
        Arg1 = result;
        result = CmSiFreeMemory(Arg1, Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m1D0);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m1D0);
    local_rsp = (local_rsp) + (576);
    return result;
loc_00878A90:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) >> (1));
    if (condition_is_equal) goto loc_00878887;
loc_00878A9A:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + (uint32_t)((uint32_t)(Arg2 - 0x1)) * 2)) != 92) goto loc_00878887;
    if ((uint32_t)((uint32_t)((uint32_t)(Arg2 - 1))) != 0) goto loc_00878A9A;
    goto loc_00878887;
loc_00878AC6:
    if ((uint16_t)(*(uint16_t *)(result + 0x8)) == 0) goto loc_00879070;
loc_00878AE1:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x591470)))) <= 5) goto loc_00878A5B;
    if (((*(uint64_t *)(v_rip + 0x59145E)) & ((uint32_t)((uint32_t)(Arg2 - 1)))) != 0) goto loc_00878F9D;
loc_00878B10:
loc_00878B13:
    result = 0;
    if (0 != 0) {
        Arg2 = result + 10;
        v_stack_m1F0 = 1;
        Arg4 = *(uint16_t *)(Arg2);
        Arg3 = result + 394;
        local_r10 = *(uint8_t *)(Arg3);
        Arg1 = *(uint16_t *)(result + 0x8) + *(uint16_t *)(result + 0x8) * 2;
        Arg1 = (uint32_t)((Arg1) << (2));
        result = v_stack_m1F0;
        v_stack_m158 = result;
        result = v_stack_p70;
        v_stack_m148 = result;
        result = v_stack_p60;
        v_stack_m138 = result;
        result = v_stack_p68;
        v_stack_m128 = result;
        result = v_stack_p78;
        v_stack_m118 = result;
        result = result + 12;
        v_stack_mF8 = result;
        result = result + 108;
        v_stack_mD8 = result;
        result = Arg4 + Arg4 * 2;
        result = (uint32_t)((result) << (2));
        v_stack_mD0 = (uint32_t)(result);
        result = result + 396;
        v_stack_mB8 = result;
        result = v_stack_m1E8;
        v_stack_mA8 = result;
        result = v_stack_m178;
        v_stack_p78 = (uint16_t)(local_r10);
        v_stack_p68 = (uint16_t)(Arg4);
        Arg4 = 14;
        v_stack_mF0 = (uint32_t)(Arg1);
        Arg1 = v_rip + 5837716;
        v_stack_mE8 = Arg2;
        Arg2 = v_rip - 8529095;
        local_r10 = (uint32_t)((local_r10) << (3));
        v_stack_p20 = result;
        v_stack_m150 = 8;
        v_stack_p70 = (uint32_t)(v_stack_p20);
        v_stack_m140 = 4;
        v_stack_p60 = (uint16_t)(*(uint16_t *)(result + 0x8));
        v_stack_m130 = 2;
        v_stack_m120 = 2;
        v_stack_m110 = 2;
        v_stack_m108 = result + 8;
        v_stack_m100 = 2;
        v_stack_mEC = 0;
        v_stack_mE0 = 2;
        v_stack_mCC = 0;
        v_stack_mC8 = Arg3;
        v_stack_mC0 = 2;
        v_stack_mB0 = (uint32_t)(local_r10);
        v_stack_mAC = 0;
        v_stack_m1E8 = 0x1000000ULL;
        v_stack_mA0 = 8;
        result = tlgWriteAgg(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(v_rip + 0x5912FF);
        Arg3 = *(uint32_t *)(v_rip + 0x5912E0);
    }
    if (Arg3 <= 5) goto loc_00878A5B;
    if (((*(uint8_t *)(v_rip + 0x5912DF)) & (8)) != 0) goto loc_00878FD3;
loc_00878C8F:
loc_00878C92:
    if (0 == 0) goto loc_00878A5B;
    v_stack_m158 = v_stack_p70;
    v_stack_m148 = v_stack_p78;
    v_stack_m138 = v_stack_p68;
    v_stack_m128 = v_stack_p60;
    v_stack_m108 = result + 12;
    result = (uint32_t)((*(uint16_t *)(result + 0x8) + *(uint16_t *)(result + 0x8) * 2) << (2));
    v_stack_m100 = (uint32_t)(result);
    v_stack_mE8 = result + 108;
    result = (uint32_t)((*(uint16_t *)(result + 0xA) + *(uint16_t *)(result + 0xA) * 2) << (2));
    v_stack_mE0 = (uint32_t)(result);
    v_stack_mC8 = result + 396;
    v_stack_p60 = (uint16_t)(*(uint8_t *)(result + 0x18A));
    v_stack_p78 = (uint16_t)(*(uint16_t *)(result + 0x8));
    v_stack_p68 = (uint16_t)(*(uint16_t *)(result + 0xA));
    Arg4 = 0;
    v_stack_mF8 = result + 10;
    v_stack_mD8 = result + 394;
    Arg3 = 0;
    local_r10 = (uint32_t)((*(uint8_t *)(result + 0x18A)) << (3));
    v_stack_p28 = v_stack_m178;
    v_stack_p20 = 12;
    v_stack_p70 = (uint32_t)(v_stack_p20);
    v_stack_m150 = 4;
    v_stack_m140 = 2;
    v_stack_m130 = 2;
    v_stack_m120 = 2;
    v_stack_m118 = result + 8;
    v_stack_m110 = 2;
    v_stack_mFC = 0;
    v_stack_mF0 = 2;
    v_stack_mDC = 0;
    v_stack_mD0 = 2;
    v_stack_mC0 = (uint32_t)(local_r10);
    v_stack_mBC = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 5837343, v_rip - 8528820, Arg3, Arg4);
    goto loc_00878A5B;
loc_00878DBD:
    local_r13 = 0;
    goto loc_00878A37;
loc_00878DCA:
    if (((*(uint64_t *)(v_rip + 0x59118D)) & (v_rip - 8528820)) != 0) goto loc_00878FB4;
loc_00878DE1:
loc_00878DE4:
    if (0 == 0) goto loc_00878A56;
    v_stack_m1E8 = 0x1000000ULL;
    v_stack_m78 = v_stack_m1F0;
    v_stack_m50 = 8;
    v_stack_m68 = v_stack_p70;
    v_stack_m58 = v_stack_m1E8;
    v_stack_p20 = v_stack_m98;
    v_stack_m1F0 = 0;
    v_stack_m70 = 8;
    v_stack_p70 = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_m60 = 4;
    result = tlgWriteAgg(v_rip + 5837079, v_rip - 8529131, Arg3, 5);
    goto loc_00878A56;
loc_00878E69:
    Arg2 = 0;
    if (((uint32_t)(result)) == 0xC0000043ULL) goto loc_00878EA0;
    v_stack_p20 = 16;
    result = SetFailureLocation(result, Arg2, Arg2 + 31, (uint32_t)((uint32_t)(result)));
    local_r13 = 0;
    goto loc_00878A2E;
loc_00878E96:
    goto loc_00878A3C;
loc_00878EA0:
    v_stack_p48 = result;
    local_r13 = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_m1C8;
    v_stack_p20 = 8;
    result = CmpOpenHiveFile(v_stack_p70, Arg2, v_stack_m1F8, v_stack_p78);
    Arg2 = 0;
    if (sign_flag) goto loc_0087900F;
    Arg4 = 0;
    v_stack_p28 = 0;
    v_stack_p78 = 0;
    v_stack_p20 = v_stack_p78;
    result = ObReferenceObjectByHandle(v_stack_m1F8, Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0x67ED7E)), Arg4);
    result = ZwClose(v_stack_m1F8, Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0x67ED7E)), Arg4);
    if (sign_flag) goto loc_0087901C;
    v_stack_p40 = v_stack_m1E0;
    v_stack_p38 = v_stack_m1C0;
    v_stack_p30 = Arg10;
    v_stack_p28 = result;
    v_stack_p20 = v_stack_m1D8;
    result = CmpResolveHiveLoadConflict(Arg1, v_stack_p78, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m1D0);
    result = ObfDereferenceObject(v_stack_p78, v_stack_p78, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m1D0);
    if (!sign_flag) goto loc_00879029;
    v_stack_p20 = 64;
loc_00878F7A:
    Arg2 = 0;
loc_00878F7C:
    result = SetFailureLocation(result, Arg2, 31, (uint32_t)(0xC0000043ULL));
    goto loc_00878A2E;
loc_00878F9D:
    result = (result) & (0);
    if (result != result) goto loc_00878B10;
    goto loc_00878B13;
loc_00878FB4:
    result = (*(uint64_t *)(v_rip + 0x590FB5)) & (0);
    if (result != (*(uint64_t *)(v_rip + 0x590FAB))) goto loc_00878DE1;
    goto loc_00878DE4;
loc_00878FD3:
    result = (uint32_t)((result) & (8));
    if (result != result) goto loc_00878C8F;
    goto loc_00878C92;
loc_00878FE7:
loc_00878FF1:
loc_00878FFB:
    result = v_stack_m1B8;
    if (v_stack_m1B8 == ((uint16_t)((uint32_t)(0xC000009AULL)))) { result = v_stack_p70; }
    goto loc_008788DC;
loc_0087900F:
    v_stack_p20 = 32;
    goto loc_00878F7C;
loc_0087901C:
    v_stack_p20 = 48;
    goto loc_00878F7A;
loc_00879029:
    goto loc_00878A2B;
loc_00879033:
    Arg2 = 0;
    v_stack_p20 = 112;
    result = SetFailureLocation(result, Arg2, Arg2 + 31, (uint32_t)((uint32_t)(result)));
    goto loc_00878A37;
loc_00879051:
    result = CmpAttachToRegistryProcess(v_stack_m1A8, Arg2, Arg2 + 31, (uint32_t)((uint32_t)(result)));
    result = CmpDestroyHive(v_stack_p70, Arg2, Arg2 + 31, (uint32_t)((uint32_t)(result)));
    result = CmpDetachFromRegistryProcess(v_stack_m1A8, Arg2, Arg2 + 31, (uint32_t)((uint32_t)(result)));
    goto loc_00878A37;
loc_00879070:
    if ((*(uint16_t *)(result + 0xA)) != 0) goto loc_00878AE1;
    goto loc_00878AE1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008787CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
