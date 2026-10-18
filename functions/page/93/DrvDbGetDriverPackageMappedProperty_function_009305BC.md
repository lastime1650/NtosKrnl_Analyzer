# DrvDbGetDriverPackageMappedProperty

- RVA: `0x009305BC`–`0x00930D3D` (길이 `1,921` bytes)
- VA: `0x00000001409305BC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008EB90`
- 디코드: `460`개 명령, `1,921/1,921` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **31**

### Outgoing calls
- `0x0093073C` → [DrvDbOpenObjectRegKey](DrvDbOpenObjectRegKey_function_00931060.md) (function, `0x00931060`)
- `0x00930785` → [DrvDbGetRegValueMappedProperty](../92/DrvDbGetRegValueMappedProperty_function_0092FB80.md) (function, `0x0092FB80`)
- `0x009307C5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x009307FD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00930832` → [PnpCtxRegQueryValue](../99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x0093088A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009308E3` → [DrvDbOpenObjectRegKey](DrvDbOpenObjectRegKey_function_00931060.md) (function, `0x00931060`)
- `0x00930904` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00930945` → [DrvDbGetDriverPackageMappedProperty](DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (function, `0x009305BC`)
- `0x0093099D` → [DrvDbGetObjectDatabaseNodeName](../92/DrvDbGetObjectDatabaseNodeName_function_0092FAC4.md) (function, `0x0092FAC4`)
- `0x00930A4F` → [DrvDbGetDriverPackageMappedProperty](DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (function, `0x009305BC`)
- `0x00930B80` → [DrvDbGetDriverPackageMappedProperty](DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (function, `0x009305BC`)
- `0x00930D33` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [DrvDbGetDriverPackageMappedPropertyKeys](../83/DrvDbGetDriverPackageMappedPropertyKeys_function_00833B34.md) at `0x00833C49`
- [DrvDbGetDriverPackageSignerScore](../92/DrvDbGetDriverPackageSignerScore_function_0092F428.md) at `0x0092F45C`
- [DrvDbDispatchDriverPackage](DrvDbDispatchDriverPackage_function_009303A0.md) at `0x00930449`
- [DrvDbGetDriverPackageMappedProperty](DrvDbGetDriverPackageMappedProperty_function_009305BC.md) at `0x00930945`
- [DrvDbGetDriverPackageMappedProperty](DrvDbGetDriverPackageMappedProperty_function_009305BC.md) at `0x00930A4F`
- [DrvDbGetDriverPackageMappedProperty](DrvDbGetDriverPackageMappedProperty_function_009305BC.md) at `0x00930B80`
- [sub_00B23888](../B2/Unknown_function_00B23888.md) at `0x00B238FD`
- [sub_00B23888](../B2/Unknown_function_00B23888.md) at `0x00B23955`
- [sub_00B23888](../B2/Unknown_function_00B23888.md) at `0x00B23C64`
- [sub_00B23888](../B2/Unknown_function_00B23888.md) at `0x00B23D97`
- [sub_00B23888](../B2/Unknown_function_00B23888.md) at `0x00B23E43`
- [sub_00B23888](../B2/Unknown_function_00B23888.md) at `0x00B23E9E`
- [sub_00B23888](../B2/Unknown_function_00B23888.md) at `0x00B23EE4`
- [sub_00B23888](../B2/Unknown_function_00B23888.md) at `0x00B23FBA`

### Static image references
- `0x009306D3` → RVA `0x0000C670` (`.rdata`; read)
- `0x00930827` → RVA `0x00B0D9A0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00930897` → RVA `0x00011F78` (`.rdata`; read)
- `0x009308A4` → RVA `0x00011F80` (`.rdata`; read)
- `0x0093091D` → RVA `0x00011F90` (`.rdata`; read)
- `0x00930962` → RVA `0x00011F10` (`.rdata`; read)
- `0x0093096F` → RVA `0x00011F18` (`.rdata`; read)
- `0x00930A0C` → RVA `0x00022D18` (`.rdata`; read)
- `0x00930B27` → RVA `0x00023630` (`.rdata`; read)
- `0x00930B38` → RVA `0x00023638` (`.rdata`; read)
- `0x00930B51` → RVA `0x00023420` (`.rdata`; read)
- `0x00930BA8` → RVA `0x00021938` (`.rdata`; read)
- `0x00930BB9` → RVA `0x00021940` (`.rdata`; read)
- `0x00930BC8` → RVA `0x00023258` (`.rdata`; read)
- `0x00930BD9` → RVA `0x00023260` (`.rdata`; read)
- `0x00930BE8` → RVA `0x000232C0` (`.rdata`; read)
- `0x00930BF9` → RVA `0x000232C8` (`.rdata`; read)
- `0x00930C08` → RVA `0x00022F80` (`.rdata`; read)
- `0x00930C19` → RVA `0x00022F88` (`.rdata`; read)
- `0x00930C28` → RVA `0x00022778` (`.rdata`; read)
- `0x00930C39` → RVA `0x00022780` (`.rdata`; read)
- `0x00930C48` → RVA `0x00020F18` (`.rdata`; read)
- `0x00930C59` → RVA `0x00020F20` (`.rdata`; read)
- `0x00930C68` → RVA `0x00021950` (`.rdata`; read)
- `0x00930C79` → RVA `0x00021958` (`.rdata`; read)
- `0x00930C88` → RVA `0x00022528` (`.rdata`; read)
- `0x00930C99` → RVA `0x00022530` (`.rdata`; read)
- `0x00930CA8` → RVA `0x000218C8` (`.rdata`; read)
- `0x00930CB9` → RVA `0x000218D0` (`.rdata`; read)
- `0x00930D16` → RVA `0x00022AA0` (`.rdata`; read)
- `0x00930D27` → RVA `0x00022AA8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x009307C5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x009307FD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0093088A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00930904` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00930D33` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **26**
  - `0x009309AE` → [sub_00B23888](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x009309C1` → [sub_00B23888](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930B1F` → [sub_00B23888 + 0x7BA](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930B2E` → [sub_00B23888 + 0xD](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930B3F` → [sub_00B23888 + 0xD](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930BAF` → [sub_00B23888 + 0x14A](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930BC0` → [sub_00B23888 + 0x14A](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930BCF` → [sub_00B23888 + 0x1BC](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930BE0` → [sub_00B23888 + 0x1BC](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930BEF` → [sub_00B23888 + 0x1C6](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930C00` → [sub_00B23888 + 0x1C6](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930C0F` → [sub_00B23888 + 0x314](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930C20` → [sub_00B23888 + 0x314](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930C2F` → [sub_00B23888 + 0x362](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930C40` → [sub_00B23888 + 0x362](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930C4F` → [sub_00B23888 + 0x4A8](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930C60` → [sub_00B23888 + 0x4A8](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930C6F` → [sub_00B23888 + 0x553](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930C80` → [sub_00B23888 + 0x553](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930C8F` → [sub_00B23888 + 0x6BF](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930CA0` → [sub_00B23888 + 0x6BF](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930CAF` → [sub_00B23888 + 0x6C9](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930CC0` → [sub_00B23888 + 0x6C9](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930CE2` → [sub_00B23888 + 0x7BA](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930D1D` → [sub_00B23888 + 0x7C5](../B2/Unknown_function_00B23888.md) (`tail-transfer`)
  - `0x00930D2E` → [sub_00B23888 + 0x7C5](../B2/Unknown_function_00B23888.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009305BC  48 8B C4                        mov rax, rsp
009305BF  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
009305C3  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
009305C7  48 89 48 08                     mov qword ptr [rax + 8], rcx
009305CB  55                              push rbp
009305CC  56                              push rsi
009305CD  57                              push rdi
009305CE  41 54                           push r12
009305D0  41 55                           push r13
009305D2  41 56                           push r14
009305D4  41 57                           push r15
009305D6  48 8D 68 C1                     lea rbp, [rax - 0x3f]
009305DA  48 81 EC B0 00 00 00            sub rsp, 0xb0
009305E1  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
009305E5  4D 8B F1                        mov r14, r9
009305E8  4C 8B 7D 7F                     mov r15, qword ptr [rbp + 0x7f]
009305EC  45 33 C9                        xor r9d, r9d
009305EF  41 8B C1                        mov eax, r9d
009305F2  4C 89 4D EF                     mov qword ptr [rbp - 0x11], r9
009305F6  4C 8B D1                        mov r10, rcx
009305F9  48 89 45 F7                     mov qword ptr [rbp - 9], rax
009305FD  45 89 4D 00                     mov dword ptr [r13], r9d
00930601  4D 8B E0                        mov r12, r8
00930604  41 8D 71 12                     lea esi, [r9 + 0x12]
00930608  45 89 0F                        mov dword ptr [r15], r9d
0093060B  45 8B 46 10                     mov r8d, dword ptr [r14 + 0x10]
0093060F  8D 4E F0                        lea ecx, [rsi - 0x10]
00930612  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00930616  0F 57 C0                        xorps xmm0, xmm0
00930619  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0093061D  48 8B FA                        mov rdi, rdx
00930620  44 89 4D BF                     mov dword ptr [rbp - 0x41], r9d
00930624  41 8B D9                        mov ebx, r9d
00930627  44 89 4D B7                     mov dword ptr [rbp - 0x49], r9d
0093062B  44 89 4D AF                     mov dword ptr [rbp - 0x51], r9d
0093062F  44 89 4D B3                     mov dword ptr [rbp - 0x4d], r9d
00930633  44 89 4D BB                     mov dword ptr [rbp - 0x45], r9d
00930637  44 89 4D C7                     mov dword ptr [rbp - 0x39], r9d
0093063B  4C 89 4D CF                     mov qword ptr [rbp - 0x31], r9
0093063F  44 88 4D 5F                     mov byte ptr [rbp + 0x5f], r9b
00930643  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
00930647  44 3B C1                        cmp r8d, ecx
0093064A  0F 84 0F 03 00 00               je 0x14093095f
00930650  44 3B C6                        cmp r8d, esi
00930653  0F 84 CB 04 00 00               je 0x140930b24
00930659  41 83 F8 21                     cmp r8d, 0x21
0093065D  0F 84 31 02 00 00               je 0x140930894
00930663  41 83 F8 2A                     cmp r8d, 0x2a
00930667  0F 84 38 05 00 00               je 0x140930ba5
0093066D  41 83 F8 1D                     cmp r8d, 0x1d
00930671  0F 84 4E 05 00 00               je 0x140930bc5
00930677  41 83 F8 1E                     cmp r8d, 0x1e
0093067B  0F 84 64 05 00 00               je 0x140930be5
00930681  41 83 F8 20                     cmp r8d, 0x20
00930685  0F 84 7A 05 00 00               je 0x140930c05
0093068B  41 83 F8 26                     cmp r8d, 0x26
0093068F  0F 84 90 05 00 00               je 0x140930c25
00930695  41 83 F8 28                     cmp r8d, 0x28
00930699  0F 84 A6 05 00 00               je 0x140930c45
0093069F  41 83 F8 2E                     cmp r8d, 0x2e
009306A3  0F 84 BC 05 00 00               je 0x140930c65
009306A9  41 83 F8 35                     cmp r8d, 0x35
009306AD  0F 84 D2 05 00 00               je 0x140930c85
009306B3  41 83 F8 36                     cmp r8d, 0x36
009306B7  0F 84 E8 05 00 00               je 0x140930ca5
009306BD  BE 01 00 00 00                  mov esi, 1
009306C2  41 83 F9 29                     cmp r9d, 0x29
009306C6  0F 83 A7 03 00 00               jae 0x140930a73
009306CC  41 8B C1                        mov eax, r9d
009306CF  48 8D 0C 80                     lea rcx, [rax + rax*4]
009306D3  48 8D 05 96 BF 6D FF            lea rax, [rip - 0x92406a]
009306DA  48 8D 14 C8                     lea rdx, [rax + rcx*8]
009306DE  4C 8B 1A                        mov r11, qword ptr [rdx]
009306E1  48 89 55 67                     mov qword ptr [rbp + 0x67], rdx
009306E5  45 39 43 10                     cmp dword ptr [r11 + 0x10], r8d
009306E9  74 05                           je 0x1409306f0
009306EB  44 03 CE                        add r9d, esi
009306EE  EB D2                           jmp 0x1409306c2
009306F0  49 8B 0B                        mov rcx, qword ptr [r11]
009306F3  49 2B 0E                        sub rcx, qword ptr [r14]
009306F6  75 08                           jne 0x140930700
009306F8  49 8B 4B 08                     mov rcx, qword ptr [r11 + 8]
009306FC  49 2B 4E 08                     sub rcx, qword ptr [r14 + 8]
00930700  33 DB                           xor ebx, ebx
00930702  48 85 C9                        test rcx, rcx
00930705  75 E4                           jne 0x1409306eb
00930707  48 85 D2                        test rdx, rdx
0093070A  0F 84 63 03 00 00               je 0x140930a73
00930710  4D 85 E4                        test r12, r12
00930713  75 3A                           jne 0x14093074f
00930715  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0093071A  48 8D 45 A7                     lea rax, [rbp - 0x59]
0093071E  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00930723  44 8D 43 02                     lea r8d, [rbx + 2]
00930727  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0093072C  4C 8B CF                        mov r9, rdi
0093072F  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
00930733  33 D2                           xor edx, edx
00930735  49 8B CA                        mov rcx, r10
00930738  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
0093073C  E8 1F 09 00 00                  call 0x140931060
00930741  8B D8                           mov ebx, eax
00930743  85 C0                           test eax, eax
00930745  78 68                           js 0x1409307af
00930747  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
0093074B  33 DB                           xor ebx, ebx
0093074D  EB 04                           jmp 0x140930753
0093074F  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
00930753  48 8B 75 67                     mov rsi, qword ptr [rbp + 0x67]
00930757  39 5E 20                        cmp dword ptr [rsi + 0x20], ebx
0093075A  0F 85 88 00 00 00               jne 0x1409307e8
00930760  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00930763  4D 85 E4                        test r12, r12
00930766  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0093076B  4D 8B CD                        mov r9, r13
0093076E  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00930772  49 0F 45 CC                     cmovne rcx, r12
00930776  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
0093077A  48 8B D1                        mov rdx, rcx
0093077D  4C 8B C6                        mov r8, rsi
00930780  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00930785  E8 F6 F3 FF FF                  call 0x14092fb80
0093078A  8B D8                           mov ebx, eax
0093078C  BF 23 00 00 C0                  mov edi, 0xc0000023
00930791  3D 25 02 00 C0                  cmp eax, 0xc0000225
00930796  0F 84 6C 05 00 00               je 0x140930d08
0093079C  85 C0                           test eax, eax
0093079E  0F 85 4D 05 00 00               jne 0x140930cf1
009307A4  41 83 7D 00 12                  cmp dword ptr [r13], 0x12
009307A9  0F 84 4F 05 00 00               je 0x140930cfe
009307AF  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
009307B3  48 85 C9                        test rcx, rcx
009307B6  0F 85 77 05 00 00               jne 0x140930d33
009307BC  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
009307C0  48 85 C9                        test rcx, rcx
009307C3  74 05                           je 0x1409307ca
009307C5  E8 E6 CA D7 FF                  call 0x1406ad2b0
009307CA  8B C3                           mov eax, ebx
009307CC  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
009307D4  48 81 C4 B0 00 00 00            add rsp, 0xb0
009307DB  41 5F                           pop r15
009307DD  41 5E                           pop r14
009307DF  41 5D                           pop r13
009307E1  41 5C                           pop r12
009307E3  5F                              pop rdi
009307E4  5E                              pop rsi
009307E5  5D                              pop rbp
009307E6  C3                              ret
009307E7  CC                              int3
009307E8  B8 30 00 00 00                  mov eax, 0x30
009307ED  41 B8 50 44 44 42               mov r8d, 0x42444450
009307F3  8B D0                           mov edx, eax
009307F5  89 45 67                        mov dword ptr [rbp + 0x67], eax
009307F8  B9 00 01 00 00                  mov ecx, 0x100
009307FD  E8 EE 18 25 00                  call 0x140b820f0
00930802  4C 8B F0                        mov r14, rax
00930805  48 85 C0                        test rax, rax
00930808  0F 84 36 03 00 00               je 0x140930b44
0093080E  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00930812  48 8D 45 67                     lea rax, [rbp + 0x67]
00930816  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0093081B  4C 8D 4D BF                     lea r9, [rbp - 0x41]
0093081F  4D 85 E4                        test r12, r12
00930822  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00930827  4C 8D 05 72 D1 1D 00            lea r8, [rip + 0x1dd172]
0093082E  49 0F 45 D4                     cmovne rdx, r12
00930832  E8 C5 38 06 00                  call 0x1409940fc
00930837  8B D8                           mov ebx, eax
00930839  3D 34 00 00 C0                  cmp eax, 0xc0000034
0093083E  0F 84 81 04 00 00               je 0x140930cc5
00930844  BF 23 00 00 C0                  mov edi, 0xc0000023
00930849  3B C7                           cmp eax, edi
0093084B  0F 84 04 01 00 00               je 0x140930955
00930851  85 C0                           test eax, eax
00930853  78 30                           js 0x140930885
00930855  83 7D BF 03                     cmp dword ptr [rbp - 0x41], 3
00930859  0F 85 88 04 00 00               jne 0x140930ce7
0093085F  83 7D 67 30                     cmp dword ptr [rbp + 0x67], 0x30
00930863  0F 85 7E 04 00 00               jne 0x140930ce7
00930869  8B 46 08                        mov eax, dword ptr [rsi + 8]
0093086C  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00930870  41 89 45 00                     mov dword ptr [r13], eax
00930874  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00930877  41 89 07                        mov dword ptr [r15], eax
0093087A  48 85 C9                        test rcx, rcx
0093087D  0F 85 4C 04 00 00               jne 0x140930ccf
00930883  8B DF                           mov ebx, edi
00930885  33 D2                           xor edx, edx
00930887  49 8B CE                        mov rcx, r14
0093088A  E8 E1 1F 25 00                  call 0x140b82870
0093088F  E9 1B FF FF FF                  jmp 0x1409307af
00930894  49 8B 06                        mov rax, qword ptr [r14]
00930897  48 2B 05 DA 16 6E FF            sub rax, qword ptr [rip - 0x91e926]
0093089E  75 0B                           jne 0x1409308ab
009308A0  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
009308A4  48 2B 05 D5 16 6E FF            sub rax, qword ptr [rip - 0x91e92b]
009308AB  48 85 C0                        test rax, rax
009308AE  0F 85 09 FE FF FF               jne 0x1409306bd
009308B4  8D 70 01                        lea esi, [rax + 1]
009308B7  4D 85 E4                        test r12, r12
009308BA  75 36                           jne 0x1409308f2
009308BC  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
009308C1  48 8D 45 A7                     lea rax, [rbp - 0x59]
009308C5  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
009308CA  44 8B C1                        mov r8d, ecx
009308CD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009308D2  33 D2                           xor edx, edx
009308D4  44 88 4C 24 28                  mov byte ptr [rsp + 0x28], r9b
009308D9  49 8B CA                        mov rcx, r10
009308DC  4C 8B CF                        mov r9, rdi
009308DF  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
009308E3  E8 78 07 00 00                  call 0x140931060
009308E8  8B D8                           mov ebx, eax
009308EA  85 C0                           test eax, eax
009308EC  0F 88 BD FE FF FF               js 0x1409307af
009308F2  BB 12 04 00 00                  mov ebx, 0x412
009308F7  41 B8 50 44 44 42               mov r8d, 0x42444450
009308FD  8B D3                           mov edx, ebx
009308FF  B9 00 01 00 00                  mov ecx, 0x100
00930904  E8 E7 17 25 00                  call 0x140b820f0
00930909  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0093090D  4C 8B F0                        mov r14, rax
00930910  48 85 C0                        test rax, rax
00930913  0F 84 2B 02 00 00               je 0x140930b44
00930919  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
0093091D  4C 8D 0D 6C 16 6E FF            lea r9, [rip - 0x91e994]
00930924  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00930928  4D 85 E4                        test r12, r12
0093092B  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00930930  48 8B D7                        mov rdx, rdi
00930933  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00930937  4D 0F 45 C4                     cmovne r8, r12
0093093B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00930940  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00930945  E8 72 FC FF FF                  call 0x1409305bc
0093094A  BF 23 00 00 C0                  mov edi, 0xc0000023
0093094F  8B D8                           mov ebx, eax
00930951  3B C7                           cmp eax, edi
00930953  75 71                           jne 0x1409309c6
00930955  BB E5 00 00 C0                  mov ebx, 0xc00000e5
0093095A  E9 26 FF FF FF                  jmp 0x140930885
0093095F  49 8B 06                        mov rax, qword ptr [r14]
00930962  48 2B 05 A7 15 6E FF            sub rax, qword ptr [rip - 0x91ea59]
00930969  75 0B                           jne 0x140930976
0093096B  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0093096F  48 2B 05 A2 15 6E FF            sub rax, qword ptr [rip - 0x91ea5e]
00930976  48 85 C0                        test rax, rax
00930979  0F 85 3E FD FF FF               jne 0x1409306bd
0093097F  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00930982  8B D1                           mov edx, ecx
00930984  4C 8B 4D 6F                     mov r9, qword ptr [rbp + 0x6f]
00930988  4C 8B C7                        mov r8, rdi
0093098B  D1 E8                           shr eax, 1
0093098D  49 8B CA                        mov rcx, r10
00930990  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00930995  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00930999  41 89 75 00                     mov dword ptr [r13], esi
0093099D  E8 22 F1 FF FF                  call 0x14092fac4
009309A2  BA 00 00 00 80                  mov edx, 0x80000000
009309A7  8B D8                           mov ebx, eax
009309A9  8D 0C 10                        lea ecx, [rax + rdx]
009309AC  85 CA                           test edx, ecx
009309AE  0F 85 D4 2E 1F 00               jne 0x140b23888
009309B4  BF 23 00 00 C0                  mov edi, 0xc0000023
009309B9  3B C7                           cmp eax, edi
009309BB  0F 85 EE FD FF FF               jne 0x1409307af
009309C1  E9 C2 2E 1F 00                  jmp 0x140b23888
009309C6  85 DB                           test ebx, ebx
009309C8  0F 88 B7 FE FF FF               js 0x140930885
009309CE  41 83 7D 00 12                  cmp dword ptr [r13], 0x12
009309D3  0F 85 0E 03 00 00               jne 0x140930ce7
009309D9  41 8B 0F                        mov ecx, dword ptr [r15]
009309DC  8D 41 FE                        lea eax, [rcx - 2]
009309DF  3D 06 02 00 00                  cmp eax, 0x206
009309E4  0F 87 FD 02 00 00               ja 0x140930ce7
009309EA  D1 E9                           shr ecx, 1
009309EC  2B CE                           sub ecx, esi
009309EE  33 F6                           xor esi, esi
009309F0  8B C1                           mov eax, ecx
009309F2  48 89 45 F7                     mov qword ptr [rbp - 9], rax
009309F6  66 41 39 34 4E                  cmp word ptr [r14 + rcx*2], si
009309FB  0F 85 E6 02 00 00               jne 0x140930ce7
00930A01  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
00930A05  8D 14 09                        lea edx, [rcx + rcx]
00930A08  48 8B 75 47                     mov rsi, qword ptr [rbp + 0x47]
00930A0C  4C 8D 0D 05 23 6F FF            lea r9, [rip - 0x90dcfb]
00930A13  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00930A18  B9 10 04 00 00                  mov ecx, 0x410
00930A1D  89 55 7F                        mov dword ptr [rbp + 0x7f], edx
00930A20  4D 85 E4                        test r12, r12
00930A23  4D 0F 45 C4                     cmovne r8, r12
00930A27  2B CA                           sub ecx, edx
00930A29  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00930A2D  48 FF C0                        inc rax
00930A30  89 4D 67                        mov dword ptr [rbp + 0x67], ecx
00930A33  48 8B CE                        mov rcx, rsi
00930A36  49 8D 04 46                     lea rax, [r14 + rax*2]
00930A3A  4C 8B 75 4F                     mov r14, qword ptr [rbp + 0x4f]
00930A3E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00930A43  49 8B D6                        mov rdx, r14
00930A46  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00930A4A  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00930A4F  E8 68 FB FF FF                  call 0x1409305bc
00930A54  8B D8                           mov ebx, eax
00930A56  3D 25 02 00 C0                  cmp eax, 0xc0000225
00930A5B  0F 84 ED 00 00 00               je 0x140930b4e
00930A61  3B DF                           cmp ebx, edi
00930A63  75 18                           jne 0x140930a7d
00930A65  BB E5 00 00 C0                  mov ebx, 0xc00000e5
00930A6A  4C 8B 75 BF                     mov r14, qword ptr [rbp - 0x41]
00930A6E  E9 12 FE FF FF                  jmp 0x140930885
00930A73  BB 16 00 00 C0                  mov ebx, 0xc0000016
00930A78  E9 4D FD FF FF                  jmp 0x1409307ca
00930A7D  85 DB                           test ebx, ebx
00930A7F  78 E9                           js 0x140930a6a
00930A81  41 83 7D 00 12                  cmp dword ptr [r13], 0x12
00930A86  0F 85 0F 01 00 00               jne 0x140930b9b
00930A8C  41 8B 07                        mov eax, dword ptr [r15]
00930A8F  83 E8 02                        sub eax, 2
00930A92  3D 06 02 00 00                  cmp eax, 0x206
00930A97  0F 87 FE 00 00 00               ja 0x140930b9b
00930A9D  4C 8B 75 BF                     mov r14, qword ptr [rbp - 0x41]
00930AA1  41 BB 2D 00 00 00               mov r11d, 0x2d
00930AA7  4C 8B 4D F7                     mov r9, qword ptr [rbp - 9]
00930AAB  49 8B D6                        mov rdx, r14
00930AAE  66 47 89 1C 4E                  mov word ptr [r14 + r9*2], r11w
00930AB3  41 0F B7 0E                     movzx ecx, word ptr [r14]
00930AB7  66 85 C9                        test cx, cx
00930ABA  74 2C                           je 0x140930ae8
00930ABC  66 83 F9 3A                     cmp cx, 0x3a
00930AC0  0F 87 C6 00 00 00               ja 0x140930b8c
00930AC6  49 BA 00 00 00 00 01 20 00 04   movabs r10, 0x400200100000000
00930AD0  49 0F A3 CA                     bt r10, rcx
00930AD4  0F 83 B2 00 00 00               jae 0x140930b8c
00930ADA  66 C7 02 5F 00                  mov word ptr [rdx], 0x5f
00930ADF  48 83 C2 02                     add rdx, 2
00930AE3  0F B7 0A                        movzx ecx, word ptr [rdx]
00930AE6  EB CF                           jmp 0x140930ab7
00930AE8  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
00930AEB  83 C1 02                        add ecx, 2
00930AEE  66 47 89 1C 4E                  mov word ptr [r14 + r9*2], r11w
00930AF3  41 C7 45 00 12 00 00 00         mov dword ptr [r13], 0x12
00930AFB  41 03 0F                        add ecx, dword ptr [r15]
00930AFE  8B C1                           mov eax, ecx
00930B00  41 89 0F                        mov dword ptr [r15], ecx
00930B03  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00930B07  48 85 C9                        test rcx, rcx
00930B0A  0F 84 73 FD FF FF               je 0x140930883
00930B10  39 45 77                        cmp dword ptr [rbp + 0x77], eax
00930B13  0F 82 6A FD FF FF               jb 0x140930883
00930B19  44 8B C0                        mov r8d, eax
00930B1C  49 8B D6                        mov rdx, r14
00930B1F  E9 1E 35 1F 00                  jmp 0x140b24042
00930B24  49 8B 06                        mov rax, qword ptr [r14]
00930B27  48 2B 05 02 2B 6F FF            sub rax, qword ptr [rip - 0x90d4fe]
00930B2E  0F 85 61 2D 1F 00               jne 0x140b23895
00930B34  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00930B38  48 2B 05 F9 2A 6F FF            sub rax, qword ptr [rip - 0x90d507]
00930B3F  E9 51 2D 1F 00                  jmp 0x140b23895
00930B44  BB 17 00 00 C0                  mov ebx, 0xc0000017
00930B49  E9 61 FC FF FF                  jmp 0x1409307af
00930B4E  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
00930B51  4C 8D 0D C8 28 6F FF            lea r9, [rip - 0x90d738]
00930B58  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
00930B5C  4D 85 E4                        test r12, r12
00930B5F  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00930B64  49 8B D6                        mov rdx, r14
00930B67  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00930B6B  4D 0F 45 C4                     cmovne r8, r12
00930B6F  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00930B73  48 8B CE                        mov rcx, rsi
00930B76  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00930B7B  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00930B80  E8 37 FA FF FF                  call 0x1409305bc
00930B85  8B D8                           mov ebx, eax
00930B87  E9 D5 FE FF FF                  jmp 0x140930a61
00930B8C  66 83 F9 7E                     cmp cx, 0x7e
00930B90  0F 85 49 FF FF FF               jne 0x140930adf
00930B96  E9 3F FF FF FF                  jmp 0x140930ada
00930B9B  BB 01 00 00 C0                  mov ebx, 0xc0000001
00930BA0  E9 C5 FE FF FF                  jmp 0x140930a6a
00930BA5  49 8B 06                        mov rax, qword ptr [r14]
00930BA8  48 2B 05 89 0D 6F FF            sub rax, qword ptr [rip - 0x90f277]
00930BAF  0F 85 1D 2E 1F 00               jne 0x140b239d2
00930BB5  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00930BB9  48 2B 05 80 0D 6F FF            sub rax, qword ptr [rip - 0x90f280]
00930BC0  E9 0D 2E 1F 00                  jmp 0x140b239d2
00930BC5  49 8B 06                        mov rax, qword ptr [r14]
00930BC8  48 2B 05 89 26 6F FF            sub rax, qword ptr [rip - 0x90d977]
00930BCF  0F 85 6F 2E 1F 00               jne 0x140b23a44
00930BD5  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00930BD9  48 2B 05 80 26 6F FF            sub rax, qword ptr [rip - 0x90d980]
00930BE0  E9 5F 2E 1F 00                  jmp 0x140b23a44
00930BE5  49 8B 06                        mov rax, qword ptr [r14]
00930BE8  48 2B 05 D1 26 6F FF            sub rax, qword ptr [rip - 0x90d92f]
00930BEF  0F 85 59 2E 1F 00               jne 0x140b23a4e
00930BF5  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00930BF9  48 2B 05 C8 26 6F FF            sub rax, qword ptr [rip - 0x90d938]
00930C00  E9 49 2E 1F 00                  jmp 0x140b23a4e
00930C05  49 8B 06                        mov rax, qword ptr [r14]
00930C08  48 2B 05 71 23 6F FF            sub rax, qword ptr [rip - 0x90dc8f]
00930C0F  0F 85 87 2F 1F 00               jne 0x140b23b9c
00930C15  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00930C19  48 2B 05 68 23 6F FF            sub rax, qword ptr [rip - 0x90dc98]
00930C20  E9 77 2F 1F 00                  jmp 0x140b23b9c
00930C25  49 8B 06                        mov rax, qword ptr [r14]
00930C28  48 2B 05 49 1B 6F FF            sub rax, qword ptr [rip - 0x90e4b7]
00930C2F  0F 85 B5 2F 1F 00               jne 0x140b23bea
00930C35  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00930C39  48 2B 05 40 1B 6F FF            sub rax, qword ptr [rip - 0x90e4c0]
00930C40  E9 A5 2F 1F 00                  jmp 0x140b23bea
00930C45  49 8B 06                        mov rax, qword ptr [r14]
00930C48  48 2B 05 C9 02 6F FF            sub rax, qword ptr [rip - 0x90fd37]
00930C4F  0F 85 DB 30 1F 00               jne 0x140b23d30
00930C55  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00930C59  48 2B 05 C0 02 6F FF            sub rax, qword ptr [rip - 0x90fd40]
00930C60  E9 CB 30 1F 00                  jmp 0x140b23d30
00930C65  49 8B 06                        mov rax, qword ptr [r14]
00930C68  48 2B 05 E1 0C 6F FF            sub rax, qword ptr [rip - 0x90f31f]
00930C6F  0F 85 66 31 1F 00               jne 0x140b23ddb
00930C75  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00930C79  48 2B 05 D8 0C 6F FF            sub rax, qword ptr [rip - 0x90f328]
00930C80  E9 56 31 1F 00                  jmp 0x140b23ddb
00930C85  49 8B 06                        mov rax, qword ptr [r14]
00930C88  48 2B 05 99 18 6F FF            sub rax, qword ptr [rip - 0x90e767]
00930C8F  0F 85 B2 32 1F 00               jne 0x140b23f47
00930C95  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00930C99  48 2B 05 90 18 6F FF            sub rax, qword ptr [rip - 0x90e770]
00930CA0  E9 A2 32 1F 00                  jmp 0x140b23f47
00930CA5  49 8B 06                        mov rax, qword ptr [r14]
00930CA8  48 2B 05 19 0C 6F FF            sub rax, qword ptr [rip - 0x90f3e7]
00930CAF  0F 85 9C 32 1F 00               jne 0x140b23f51
00930CB5  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00930CB9  48 2B 05 10 0C 6F FF            sub rax, qword ptr [rip - 0x90f3f0]
00930CC0  E9 8C 32 1F 00                  jmp 0x140b23f51
00930CC5  BB 25 02 00 C0                  mov ebx, 0xc0000225
00930CCA  E9 B6 FB FF FF                  jmp 0x140930885
00930CCF  39 45 77                        cmp dword ptr [rbp + 0x77], eax
00930CD2  0F 82 AB FB FF FF               jb 0x140930883
00930CD8  8B 56 1C                        mov edx, dword ptr [rsi + 0x1c]
00930CDB  44 8B 46 20                     mov r8d, dword ptr [rsi + 0x20]
00930CDF  49 03 D6                        add rdx, r14
00930CE2  E9 5B 33 1F 00                  jmp 0x140b24042
00930CE7  BB 01 00 00 C0                  mov ebx, 0xc0000001
00930CEC  E9 94 FB FF FF                  jmp 0x140930885
00930CF1  3B C7                           cmp eax, edi
00930CF3  0F 85 B6 FA FF FF               jne 0x1409307af
00930CF9  E9 A6 FA FF FF                  jmp 0x1409307a4
00930CFE  41 83 3F 02                     cmp dword ptr [r15], 2
00930D02  0F 85 A7 FA FF FF               jne 0x1409307af
00930D08  41 83 7E 10 07                  cmp dword ptr [r14 + 0x10], 7
00930D0D  0F 85 9C FA FF FF               jne 0x1409307af
00930D13  49 8B 06                        mov rax, qword ptr [r14]
00930D16  48 2B 05 83 1D 6F FF            sub rax, qword ptr [rip - 0x90e27d]
00930D1D  0F 85 2A 33 1F 00               jne 0x140b2404d
00930D23  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00930D27  48 2B 05 7A 1D 6F FF            sub rax, qword ptr [rip - 0x90e286]
00930D2E  E9 1A 33 1F 00                  jmp 0x140b2404d
00930D33  E8 78 C5 D7 FF                  call 0x1406ad2b0
00930D38  E9 7F FA FF FF                  jmp 0x1409307bc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DrvDbGetDriverPackageMappedProperty(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int8 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (176);
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 17) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 9) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103)) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127)) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 89) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 25) = 0;
    *(unsigned int *)(v_rsp - 63 - 65) = 0;
    *(unsigned int *)(v_rsp - 63 - 73) = 0;
    *(unsigned int *)(v_rsp - 63 - 81) = 0;
    *(unsigned int *)(v_rsp - 63 - 77) = 0;
    *(unsigned int *)(v_rsp - 63 - 69) = 0;
    *(unsigned int *)(v_rsp - 63 - 57) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 49) = 0;
    *(unsigned __int8 *)(v_rsp - 63 + 95) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 41) = v_xmm0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == ((unsigned int)(a4 + 18 - 16))) goto loc_0093095F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == ((unsigned int)(a4 + 18))) goto loc_00930B24;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 33) goto loc_00930894;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 42) goto loc_00930BA5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 29) goto loc_00930BC5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 30) goto loc_00930BE5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 32) goto loc_00930C05;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 38) goto loc_00930C25;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 40) goto loc_00930C45;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 46) goto loc_00930C65;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 53) goto loc_00930C85;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) == 54) goto loc_00930CA5;
loc_009306BD:
loc_009306C2:
    if (0 >= 41) goto loc_00930A73;
    *(unsigned __int64 *)(v_rsp - 63 + 103) = v_rip - 9584746 + 0 + 0 * 4 * 8;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip - 9584746 + 0 + 0 * 4 * 8) + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16))))) goto loc_009306F0;
loc_009306EB:
    a4 = (unsigned int)((a4) + (1));
    goto loc_009306C2;
loc_009306F0:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9584746 + 0 + 0 * 4 * 8))) - (*(unsigned __int64 *)(a4));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9584746 + 0 + 0 * 4 * 8) + 8);
        a1 = (a1) - (*(unsigned __int64 *)(a4 + 8));
    }
    v_rbx = 0;
    if (a1 != 0) goto loc_009306EB;
    if (v_rip - 9584746 + 0 + 0 * 4 * 8 == 0) goto loc_00930A73;
    if (a3 != 0) goto loc_0093074F;
    v_stack_mA8 = 0;
    v_stack_mB0 = 0;
    v_stack_mB8 = v_rsp - 63 - 89;
    v_stack_mC0 = 0;
    a2 = 0;
    v_stack_mC8 = 1;
    result = DrvDbOpenObjectRegKey(a1, a2, v_rbx + 2, a2);
    if (sign_flag) goto loc_009307AF;
    v_rbx = 0;
    goto loc_00930753;
loc_0093074F:
loc_00930753:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103) + 32)) != 0) goto loc_009307E8;
    v_stack_mB8 = *(unsigned __int64 *)(v_rsp - 63 + 127);
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 119)));
    a1 = *(unsigned __int64 *)(v_rsp - 63 - 9);
    if (a3 != 0) { a1 = a3; }
    v_stack_mC8 = *(unsigned __int64 *)(v_rsp - 63 + 111);
    result = DrvDbGetRegValueMappedProperty(a1, a1, *(unsigned __int64 *)(v_rsp - 63 + 103), *(unsigned __int64 *)(v_rsp - 63 + 103));
    if (((unsigned int)(result)) == 0xC0000225ULL) goto loc_00930D08;
    if ((unsigned int)(result) != 0) goto loc_00930CF1;
loc_009307A4:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103))) == 18) goto loc_00930CFE;
loc_009307AF:
    if (*(unsigned __int64 *)(v_rsp - 63 - 17) != 0) goto loc_00930D33;
loc_009307BC:
    if (*(unsigned __int64 *)(v_rsp - 63 - 89) != 0) {
        result = ZwClose(*(unsigned __int64 *)(v_rsp - 63 - 89), a1, *(unsigned __int64 *)(v_rsp - 63 + 103), *(unsigned __int64 *)(v_rsp - 63 + 103));
    }
    v_rsp = (v_rsp) + (176);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_009307E8:
    *(unsigned int *)(v_rsp - 63 + 103) = 48;
    result = ExAllocatePool2(256, 48, (unsigned int)(0x42444450ULL), *(unsigned __int64 *)(v_rsp - 63 + 103));
    if (result == 0) goto loc_00930B44;
    v_stack_p28 = v_rsp - 63 + 103;
    v_stack_p20 = result;
    a2 = *(unsigned __int64 *)(v_rsp - 63 - 89);
    if (a3 != 0) { a2 = a3; }
    result = PnpCtxRegQueryValue(256, a2, v_rip + 1954162, v_rsp - 63 - 65);
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_00930CC5;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_00930955;
    if (sign_flag) goto loc_00930885;
    if ((*(unsigned int *)(v_rsp - 63 - 65)) != 3) goto loc_00930CE7;
    if ((*(unsigned int *)(v_rsp - 63 + 103)) != 48) goto loc_00930CE7;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103)) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103) + 8)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127)) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103) + 32)));
    if (*(unsigned __int64 *)(v_rsp - 63 + 111) != 0) goto loc_00930CCF;
loc_00930883:
loc_00930885:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_rip + 1954162, v_rsp - 63 - 65);
    goto loc_009307AF;
loc_00930894:
    result = (*(unsigned __int64 *)(result)) - (*(unsigned __int64 *)(v_rip - 9562406));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(result + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9562411));
    }
    if (result != 0) goto loc_009306BD;
    if (a3 != 0) goto loc_009308F2;
    v_stack_p40 = v_rsp - 63 - 65;
    v_stack_p38 = v_rsp - 63 - 65;
    v_stack_p30 = v_rsp - 63 - 89;
    a2 = 0;
    v_stack_p28 = (unsigned __int8)(v_rsp - 63 - 65);
    v_stack_p20 = (unsigned int)(result + 1);
    result = DrvDbOpenObjectRegKey(a1, a2, (unsigned int)((unsigned int)(result)), (unsigned int)(0xC0000023ULL));
    if (sign_flag) goto loc_009307AF;
loc_009308F2:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(0x412ULL))), (unsigned int)(0x42444450ULL), (unsigned int)(0xC0000023ULL));
    *(unsigned __int64 *)(v_rsp - 63 - 65) = result;
    if (result == 0) goto loc_00930B44;
    v_stack_p38 = *(unsigned __int64 *)(v_rsp - 63 + 127);
    v_stack_p30 = (unsigned int)((unsigned int)(0x412ULL));
    a3 = *(unsigned __int64 *)(v_rsp - 63 - 89);
    if (a3 != 0) { a3 = a3; }
    v_stack_p28 = result;
    v_stack_p20 = *(unsigned __int64 *)(v_rsp - 63 + 103);
    result = DrvDbGetDriverPackageMappedProperty(*(unsigned __int64 *)(v_rsp - 63 + 71), (unsigned int)(0xC0000023ULL), a3, v_rip - 9562516);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_009309C6;
loc_00930955:
    goto loc_00930885;
loc_0093095F:
    result = (*(unsigned __int64 *)(result)) - (*(unsigned __int64 *)(v_rip - 9562713));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(result + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 9562718));
    }
    if (result != 0) goto loc_009306BD;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 63 + 119))) >> (1));
    v_stack_p28 = *(unsigned __int64 *)(v_rsp - 63 + 127);
    v_stack_p20 = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103)) = (unsigned int)(result + 1);
    result = DrvDbGetObjectDatabaseNodeName(a1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 63 + 71))), (unsigned int)(0xC0000023ULL), *(unsigned __int64 *)(v_rsp - 63 + 111));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_009307AF;
loc_009309C6:
    if (sign_flag) goto loc_00930885;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103))) != 18) goto loc_00930CE7;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127))) - 2)) > 518) goto loc_00930CE7;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127)))) >> (1));
    a1 = (unsigned int)((a1) - ((unsigned int)(result + 1)));
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 9) = (unsigned int)((unsigned int)(a1));
    if ((*(unsigned __int16 *)(result + a1 * 2)) != 0) goto loc_00930CE7;
    v_stack_p38 = *(unsigned __int64 *)(v_rsp - 63 + 127);
    *(unsigned int *)(v_rsp - 63 + 127) = (unsigned int)(a1 + a1 * 1);
    a3 = *(unsigned __int64 *)(v_rsp - 63 - 89);
    if (a3 != 0) { a3 = a3; }
    a1 = (unsigned int)(((unsigned int)(0x410ULL)) - ((unsigned int)(a1 + a1 * 1)));
    v_stack_p30 = (unsigned int)(a1);
    result = ((unsigned int)((unsigned int)(a1))) + 1;
    *(unsigned int *)(v_rsp - 63 + 103) = (unsigned int)(a1);
    v_stack_p28 = result + result * 2;
    *(unsigned __int64 *)(v_rsp - 63 - 49) = result + result * 2;
    v_stack_p20 = *(unsigned __int64 *)(v_rsp - 63 + 103);
    result = DrvDbGetDriverPackageMappedProperty(*(unsigned __int64 *)(v_rsp - 63 + 71), *(unsigned __int64 *)(v_rsp - 63 + 79), a3, v_rip - 9493755);
    if (((unsigned int)(result)) == 0xC0000225ULL) goto loc_00930B4E;
loc_00930A61:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_00930A7D;
loc_00930A6A:
    goto loc_00930885;
loc_00930A73:
    goto loc_009307CA;
loc_00930A7D:
    if (sign_flag) goto loc_00930A6A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103))) != 18) goto loc_00930B9B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127)))) - (2));
    if (((unsigned int)(result)) > 518) goto loc_00930B9B;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + *(unsigned __int64 *)(v_rsp - 63 - 9) * 2) = 45;
loc_00930AB7:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 - 65))) == 0) goto loc_00930AE8;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 - 65)))) > 58) goto loc_00930B8C;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 - 65)))) >= 58) goto loc_00930B8C;
loc_00930ADA:
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 - 65)) = 95;
loc_00930ADF:
    a2 = (*(unsigned __int64 *)(v_rsp - 63 - 65)) + (2);
    goto loc_00930AB7;
loc_00930AE8:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 63 + 127))) + (2));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + *(unsigned __int64 *)(v_rsp - 63 - 9) * 2) = 45;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103)) = 18;
    a1 = (unsigned int)((a1) + (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127))));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127)) = (unsigned int)(a1);
    if (*(unsigned __int64 *)(v_rsp - 63 + 111) == 0) goto loc_00930883;
    if ((*(unsigned int *)(v_rsp - 63 + 119)) < ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_00930883;
loc_00930B24:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65))) - (*(unsigned __int64 *)(v_rip - 9491710));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + 8)) - (*(unsigned __int64 *)(v_rip - 9491719));
loc_00930B44:
    goto loc_009307AF;
loc_00930B4E:
    v_stack_p38 = *(unsigned __int64 *)(v_rsp - 63 + 127);
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 + 103)));
    a3 = *(unsigned __int64 *)(v_rsp - 63 - 89);
    if (a3 != 0) { a3 = a3; }
    v_stack_p28 = *(unsigned __int64 *)(v_rsp - 63 - 49);
    v_stack_p20 = *(unsigned __int64 *)(v_rsp - 63 + 103);
    result = DrvDbGetDriverPackageMappedProperty(*(unsigned __int64 *)(v_rsp - 63 + 71), *(unsigned __int64 *)(v_rsp - 63 - 65), a3, v_rip - 9492280);
    goto loc_00930A61;
loc_00930B8C:
    if (((unsigned __int16)(*(unsigned __int64 *)(v_rsp - 63 + 71))) != 126) goto loc_00930ADF;
    goto loc_00930ADA;
loc_00930B9B:
    goto loc_00930A6A;
loc_00930BA5:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65))) - (*(unsigned __int64 *)(v_rip - 9499255));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + 8)) - (*(unsigned __int64 *)(v_rip - 9499264));
loc_00930BC5:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65))) - (*(unsigned __int64 *)(v_rip - 9492855));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + 8)) - (*(unsigned __int64 *)(v_rip - 9492864));
loc_00930BE5:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65))) - (*(unsigned __int64 *)(v_rip - 9492783));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + 8)) - (*(unsigned __int64 *)(v_rip - 9492792));
loc_00930C05:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65))) - (*(unsigned __int64 *)(v_rip - 9493647));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + 8)) - (*(unsigned __int64 *)(v_rip - 9493656));
loc_00930C25:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65))) - (*(unsigned __int64 *)(v_rip - 9495735));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + 8)) - (*(unsigned __int64 *)(v_rip - 9495744));
loc_00930C45:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65))) - (*(unsigned __int64 *)(v_rip - 9502007));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + 8)) - (*(unsigned __int64 *)(v_rip - 9502016));
loc_00930C65:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65))) - (*(unsigned __int64 *)(v_rip - 9499423));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + 8)) - (*(unsigned __int64 *)(v_rip - 9499432));
loc_00930C85:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65))) - (*(unsigned __int64 *)(v_rip - 9496423));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + 8)) - (*(unsigned __int64 *)(v_rip - 9496432));
loc_00930CA5:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65))) - (*(unsigned __int64 *)(v_rip - 9499623));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + 8)) - (*(unsigned __int64 *)(v_rip - 9499632));
loc_00930CC5:
    goto loc_00930885;
loc_00930CCF:
    if ((*(unsigned int *)(v_rsp - 63 + 119)) < ((unsigned int)(result))) goto loc_00930883;
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 71) + 28))) + (*(unsigned __int64 *)(v_rsp - 63 - 65));
loc_00930CE7:
    goto loc_00930885;
loc_00930CF1:
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_009307AF;
    goto loc_009307A4;
loc_00930CFE:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 127))) != 2) goto loc_009307AF;
loc_00930D08:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + 16)) != 7) goto loc_009307AF;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65))) - (*(unsigned __int64 *)(v_rip - 9495165));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 65) + 8)) - (*(unsigned __int64 *)(v_rip - 9495174));
loc_00930D33:
    result = ZwClose(*(unsigned __int64 *)(v_rsp - 63 + 71), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 71) + 32)), v_rip - 9492280);
    goto loc_009307BC;
}
```

## 5. (Beta) C Style

```c
int64_t DrvDbGetDriverPackageMappedProperty(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint8_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (176);
    Arg4 = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x11) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x9) = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67)) = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F)) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x59) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x19) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x41) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x49) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x51) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x4D) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x45) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x39) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x31) = 0;
    *(uint8_t *)(local_rsp - 0x3F + 0x5F) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x29) = v_xmm0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == ((uint32_t)(Arg4 + 18 - 16))) goto loc_0093095F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == ((uint32_t)(Arg4 + 18))) goto loc_00930B24;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 33) goto loc_00930894;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 42) goto loc_00930BA5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 29) goto loc_00930BC5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 30) goto loc_00930BE5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 32) goto loc_00930C05;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 38) goto loc_00930C25;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 40) goto loc_00930C45;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 46) goto loc_00930C65;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 53) goto loc_00930C85;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) == 54) goto loc_00930CA5;
loc_009306BD:
loc_009306C2:
    if (0 >= 41) goto loc_00930A73;
    *(uint64_t *)(local_rsp - 0x3F + 0x67) = v_rip - 9584746 + 0 + 0 * 4 * 8;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip - 0x92406A + 0x0 + 0x0 * 4 * 8) + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10))))) goto loc_009306F0;
loc_009306EB:
    Arg4 = (uint32_t)((Arg4) + (1));
    goto loc_009306C2;
loc_009306F0:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x92406A + 0x0 + 0x0 * 4 * 8))) - (*(uint64_t *)(arg4));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip - 0x92406A + 0x0 + 0x0 * 4 * 8) + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(arg4 + 0x8));
    }
    local_rbx = 0;
    if (Arg1 != 0) goto loc_009306EB;
    if (v_rip - 9584746 + 0 + 0 * 4 * 8 == 0) goto loc_00930A73;
    if (Arg3 != 0) goto loc_0093074F;
    v_stack_mA8 = 0;
    v_stack_mB0 = 0;
    v_stack_mB8 = local_rsp - 63 - 89;
    v_stack_mC0 = 0;
    Arg2 = 0;
    v_stack_mC8 = 1;
    result = DrvDbOpenObjectRegKey(Arg1, Arg2, local_rbx + 2, Arg2);
    if (sign_flag) goto loc_009307AF;
    local_rbx = 0;
    goto loc_00930753;
loc_0093074F:
loc_00930753:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67) + 0x20)) != 0) goto loc_009307E8;
    v_stack_mB8 = *(uint64_t *)(local_rsp - 0x3F + 0x7F);
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x77)));
    Arg1 = *(uint64_t *)(local_rsp - 0x3F - 0x9);
    if (Arg3 != 0) { Arg1 = Arg3; }
    v_stack_mC8 = *(uint64_t *)(local_rsp - 0x3F + 0x6F);
    result = DrvDbGetRegValueMappedProperty(Arg1, Arg1, *(uint64_t *)(local_rsp - 0x3F + 0x67), *(uint64_t *)(local_rsp - 0x3F + 0x67));
    if (((uint32_t)(result)) == 0xC0000225ULL) goto loc_00930D08;
    if ((uint32_t)(result) != 0) goto loc_00930CF1;
loc_009307A4:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67))) == 18) goto loc_00930CFE;
loc_009307AF:
    if (*(uint64_t *)(local_rsp - 0x3F - 0x11) != 0) goto loc_00930D33;
loc_009307BC:
    if (*(uint64_t *)(local_rsp - 0x3F - 0x59) != 0) {
        result = ZwClose(*(uint64_t *)(local_rsp - 0x3F - 0x59), Arg1, *(uint64_t *)(local_rsp - 0x3F + 0x67), *(uint64_t *)(local_rsp - 0x3F + 0x67));
    }
    local_rsp = (local_rsp) + (176);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_009307E8:
    *(uint32_t *)(local_rsp - 0x3F + 0x67) = 48;
    result = ExAllocatePool2(256, 48, (uint32_t)(0x42444450ULL), *(uint64_t *)(local_rsp - 0x3F + 0x67));
    if (result == 0) goto loc_00930B44;
    v_stack_p28 = local_rsp - 63 + 103;
    v_stack_p20 = result;
    Arg2 = *(uint64_t *)(local_rsp - 0x3F - 0x59);
    if (Arg3 != 0) { Arg2 = Arg3; }
    result = PnpCtxRegQueryValue(256, Arg2, v_rip + 1954162, local_rsp - 63 - 65);
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_00930CC5;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_00930955;
    if (sign_flag) goto loc_00930885;
    if ((*(uint32_t *)(local_rsp - 0x3F - 0x41)) != 3) goto loc_00930CE7;
    if ((*(uint32_t *)(local_rsp - 0x3F + 0x67)) != 48) goto loc_00930CE7;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67)) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67) + 0x8)));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F)) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67) + 0x20)));
    if (*(uint64_t *)(local_rsp - 0x3F + 0x6F) != 0) goto loc_00930CCF;
loc_00930883:
loc_00930885:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_rip + 1954162, local_rsp - 63 - 65);
    goto loc_009307AF;
loc_00930894:
    result = (*(uint64_t *)(result)) - (*(uint64_t *)(v_rip - 0x91E926));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(result + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x91E92B));
    }
    if (result != 0) goto loc_009306BD;
    if (Arg3 != 0) goto loc_009308F2;
    v_stack_p40 = local_rsp - 63 - 65;
    v_stack_p38 = local_rsp - 63 - 65;
    v_stack_p30 = local_rsp - 63 - 89;
    Arg2 = 0;
    v_stack_p28 = (uint8_t)(local_rsp - 63 - 65);
    v_stack_p20 = (uint32_t)(result + 1);
    result = DrvDbOpenObjectRegKey(Arg1, Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)(0xC0000023ULL));
    if (sign_flag) goto loc_009307AF;
loc_009308F2:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(0x412ULL))), (uint32_t)(0x42444450ULL), (uint32_t)(0xC0000023ULL));
    *(uint64_t *)(local_rsp - 0x3F - 0x41) = result;
    if (result == 0) goto loc_00930B44;
    v_stack_p38 = *(uint64_t *)(local_rsp - 0x3F + 0x7F);
    v_stack_p30 = (uint32_t)((uint32_t)(0x412ULL));
    Arg3 = *(uint64_t *)(local_rsp - 0x3F - 0x59);
    if (Arg3 != 0) { Arg3 = Arg3; }
    v_stack_p28 = result;
    v_stack_p20 = *(uint64_t *)(local_rsp - 0x3F + 0x67);
    result = DrvDbGetDriverPackageMappedProperty(*(uint64_t *)(local_rsp - 0x3F + 0x47), (uint32_t)(0xC0000023ULL), Arg3, v_rip - 9562516);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_009309C6;
loc_00930955:
    goto loc_00930885;
loc_0093095F:
    result = (*(uint64_t *)(result)) - (*(uint64_t *)(v_rip - 0x91EA59));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(result + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x91EA5E));
    }
    if (result != 0) goto loc_009306BD;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x77))) >> (1));
    v_stack_p28 = *(uint64_t *)(local_rsp - 0x3F + 0x7F);
    v_stack_p20 = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67)) = (uint32_t)(result + 1);
    result = DrvDbGetObjectDatabaseNodeName(Arg1, (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x3F + 0x47))), (uint32_t)(0xC0000023ULL), *(uint64_t *)(local_rsp - 0x3F + 0x6F));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_009307AF;
loc_009309C6:
    if (sign_flag) goto loc_00930885;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67))) != 18) goto loc_00930CE7;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F))) - 2)) > 518) goto loc_00930CE7;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F)))) >> (1));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result + 1)));
    local_rsi = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x9) = (uint32_t)((uint32_t)(Arg1));
    if ((*(uint16_t *)(result + Arg1 * 2)) != 0) goto loc_00930CE7;
    v_stack_p38 = *(uint64_t *)(local_rsp - 0x3F + 0x7F);
    *(uint32_t *)(local_rsp - 0x3F + 0x7F) = (uint32_t)(Arg1 + Arg1 * 1);
    Arg3 = *(uint64_t *)(local_rsp - 0x3F - 0x59);
    if (Arg3 != 0) { Arg3 = Arg3; }
    Arg1 = (uint32_t)(((uint32_t)(0x410ULL)) - ((uint32_t)(Arg1 + Arg1 * 1)));
    v_stack_p30 = (uint32_t)(Arg1);
    result = ((uint32_t)((uint32_t)(Arg1))) + 1;
    *(uint32_t *)(local_rsp - 0x3F + 0x67) = (uint32_t)(Arg1);
    v_stack_p28 = result + result * 2;
    *(uint64_t *)(local_rsp - 0x3F - 0x31) = result + result * 2;
    v_stack_p20 = *(uint64_t *)(local_rsp - 0x3F + 0x67);
    result = DrvDbGetDriverPackageMappedProperty(*(uint64_t *)(local_rsp - 0x3F + 0x47), *(uint64_t *)(local_rsp - 0x3F + 0x4F), Arg3, v_rip - 9493755);
    if (((uint32_t)(result)) == 0xC0000225ULL) goto loc_00930B4E;
loc_00930A61:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_00930A7D;
loc_00930A6A:
    goto loc_00930885;
loc_00930A73:
    goto loc_009307CA;
loc_00930A7D:
    if (sign_flag) goto loc_00930A6A;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67))) != 18) goto loc_00930B9B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F)))) - (2));
    if (((uint32_t)(result)) > 518) goto loc_00930B9B;
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + *(uint64_t *)(local_rsp - 0x3F - 0x9) * 2) = 45;
loc_00930AB7:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41))) == 0) goto loc_00930AE8;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41)))) > 58) goto loc_00930B8C;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41)))) >= 58) goto loc_00930B8C;
loc_00930ADA:
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41)) = 95;
loc_00930ADF:
    Arg2 = (*(uint64_t *)(local_rsp - 0x3F - 0x41)) + (2);
    goto loc_00930AB7;
loc_00930AE8:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x7F))) + (2));
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + *(uint64_t *)(local_rsp - 0x3F - 0x9) * 2) = 45;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67)) = 18;
    Arg1 = (uint32_t)((Arg1) + (*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F))));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F)) = (uint32_t)(Arg1);
    if (*(uint64_t *)(local_rsp - 0x3F + 0x6F) == 0) goto loc_00930883;
    if ((*(uint32_t *)(local_rsp - 0x3F + 0x77)) < ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_00930883;
loc_00930B24:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41))) - (*(uint64_t *)(v_rip - 0x90D4FE));
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + 0x8)) - (*(uint64_t *)(v_rip - 0x90D507));
loc_00930B44:
    goto loc_009307AF;
loc_00930B4E:
    v_stack_p38 = *(uint64_t *)(local_rsp - 0x3F + 0x7F);
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F + 0x67)));
    Arg3 = *(uint64_t *)(local_rsp - 0x3F - 0x59);
    if (Arg3 != 0) { Arg3 = Arg3; }
    v_stack_p28 = *(uint64_t *)(local_rsp - 0x3F - 0x31);
    v_stack_p20 = *(uint64_t *)(local_rsp - 0x3F + 0x67);
    result = DrvDbGetDriverPackageMappedProperty(*(uint64_t *)(local_rsp - 0x3F + 0x47), *(uint64_t *)(local_rsp - 0x3F - 0x41), Arg3, v_rip - 9492280);
    goto loc_00930A61;
loc_00930B8C:
    if (((uint16_t)(*(uint64_t *)(local_rsp - 0x3F + 0x47))) != 126) goto loc_00930ADF;
    goto loc_00930ADA;
loc_00930B9B:
    goto loc_00930A6A;
loc_00930BA5:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41))) - (*(uint64_t *)(v_rip - 0x90F277));
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + 0x8)) - (*(uint64_t *)(v_rip - 0x90F280));
loc_00930BC5:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41))) - (*(uint64_t *)(v_rip - 0x90D977));
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + 0x8)) - (*(uint64_t *)(v_rip - 0x90D980));
loc_00930BE5:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41))) - (*(uint64_t *)(v_rip - 0x90D92F));
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + 0x8)) - (*(uint64_t *)(v_rip - 0x90D938));
loc_00930C05:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41))) - (*(uint64_t *)(v_rip - 0x90DC8F));
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + 0x8)) - (*(uint64_t *)(v_rip - 0x90DC98));
loc_00930C25:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41))) - (*(uint64_t *)(v_rip - 0x90E4B7));
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + 0x8)) - (*(uint64_t *)(v_rip - 0x90E4C0));
loc_00930C45:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41))) - (*(uint64_t *)(v_rip - 0x90FD37));
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + 0x8)) - (*(uint64_t *)(v_rip - 0x90FD40));
loc_00930C65:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41))) - (*(uint64_t *)(v_rip - 0x90F31F));
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + 0x8)) - (*(uint64_t *)(v_rip - 0x90F328));
loc_00930C85:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41))) - (*(uint64_t *)(v_rip - 0x90E767));
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + 0x8)) - (*(uint64_t *)(v_rip - 0x90E770));
loc_00930CA5:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41))) - (*(uint64_t *)(v_rip - 0x90F3E7));
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + 0x8)) - (*(uint64_t *)(v_rip - 0x90F3F0));
loc_00930CC5:
    goto loc_00930885;
loc_00930CCF:
    if ((*(uint32_t *)(local_rsp - 0x3F + 0x77)) < ((uint32_t)(result))) goto loc_00930883;
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 0x1C))) + (*(uint64_t *)(local_rsp - 0x3F - 0x41));
loc_00930CE7:
    goto loc_00930885;
loc_00930CF1:
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_009307AF;
    goto loc_009307A4;
loc_00930CFE:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x7F))) != 2) goto loc_009307AF;
loc_00930D08:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + 0x10)) != 7) goto loc_009307AF;
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41))) - (*(uint64_t *)(v_rip - 0x90E27D));
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x41) + 0x8)) - (*(uint64_t *)(v_rip - 0x90E286));
loc_00930D33:
    result = ZwClose(*(uint64_t *)(local_rsp - 0x3F + 0x47), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x47) + 0x20)), v_rip - 9492280);
    goto loc_009307BC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009305BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
