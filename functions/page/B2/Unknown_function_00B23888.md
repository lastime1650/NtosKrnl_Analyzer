# sub_00B23888

- RVA: `0x00B23888`–`0x00B240D7` (길이 `2,127` bytes)
- VA: `0x0000000140B23888`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008EBB0`
- 디코드: `560`개 명령, `2,127/2,127` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x00B238BA` → [DrvDbOpenDriverPackageRegKey](../93/DrvDbOpenDriverPackageRegKey_function_00931014.md) (function, `0x00931014`)
- `0x00B238FD` → [DrvDbGetDriverPackageMappedProperty](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (function, `0x009305BC`)
- `0x00B23955` → [DrvDbGetDriverPackageMappedProperty](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (function, `0x009305BC`)
- `0x00B239E1` → [wcsrchr](../../text/50/wcsrchr_function_00501E50.md) (function, `0x00501E50`)
- `0x00B23A2F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B23A75` → [DrvDbOpenDriverPackageRegKey](../93/DrvDbOpenDriverPackageRegKey_function_00931014.md) (function, `0x00931014`)
- `0x00B23AAD` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x00B23B30` → [PnpCtxRegEnumKeyWithCallback](../AA/PnpCtxRegEnumKeyWithCallback_function_00AA146C.md) (function, `0x00AA146C`)
- `0x00B23BD5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B23C26` → [DrvDbOpenObjectRegKey](../93/DrvDbOpenObjectRegKey_function_00931060.md) (function, `0x00931060`)
- `0x00B23C64` → [DrvDbGetDriverPackageMappedProperty](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (function, `0x009305BC`)
- `0x00B23CE3` → [DrvDbOpenObjectRegKey](../93/DrvDbOpenObjectRegKey_function_00931060.md) (function, `0x00931060`)
- `0x00B23D55` → [DrvDbOpenDriverPackageRegKey](../93/DrvDbOpenDriverPackageRegKey_function_00931014.md) (function, `0x00931014`)
- `0x00B23D97` → [DrvDbGetDriverPackageMappedProperty](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (function, `0x009305BC`)
- `0x00B23E00` → [DrvDbOpenDriverPackageRegKey](../93/DrvDbOpenDriverPackageRegKey_function_00931014.md) (function, `0x00931014`)
- `0x00B23E43` → [DrvDbGetDriverPackageMappedProperty](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (function, `0x009305BC`)
- `0x00B23E9E` → [DrvDbGetDriverPackageMappedProperty](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (function, `0x009305BC`)
- `0x00B23EE4` → [DrvDbGetDriverPackageMappedProperty](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (function, `0x009305BC`)
- `0x00B23F78` → [DrvDbOpenDriverPackageRegKey](../93/DrvDbOpenDriverPackageRegKey_function_00931014.md) (function, `0x00931014`)
- `0x00B23FBA` → [DrvDbGetDriverPackageMappedProperty](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (function, `0x009305BC`)
- `0x00B24042` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B2406D` → [DrvDbGetDriverPackageSignerScore](../92/DrvDbGetDriverPackageSignerScore_function_0092F428.md) (function, `0x0092F428`)
- `0x00B240C5` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (function, `0x0041E1C0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B238D9` → RVA `0x00022938` (`.rdata`; read)
- `0x00B2392C` → RVA `0x00021428` (`.rdata`; read)
- `0x00B23A98` → RVA `0x00AFEEB0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B23AE8` → RVA `0x000232C0` (`.rdata`; read)
- `0x00B23AF5` → RVA `0x000232C8` (`.rdata`; read)
- `0x00B23B26` → RVA `0x006A2E40` (`DrvDbGetConfigurationSubKeyCallback`; read)
- `0x00B23C4A` → RVA `0x00021398` (`.rdata`; read)
- `0x00B23D7D` → RVA `0x00021A70` (`.rdata`; read)
- `0x00B23E1F` → RVA `0x000214D0` (`.rdata`; read)
- `0x00B23E72` → RVA `0x000216C8` (`.rdata`; read)
- `0x00B23EBC` → RVA `0x00021CC8` (`.rdata`; read)
- `0x00B23FA0` → RVA `0x00022FB0` (`.rdata`; read)
- `0x00B24018` → RVA `0x00022528` (`.rdata`; read)
- `0x00B24025` → RVA `0x00022530` (`.rdata`; read)
- `0x00B240B6` → RVA `0x00B0D9B0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00B239E1` → [wcsrchr](../../text/50/wcsrchr_function_00501E50.md) (`PAGE` → `.text`)
  - `0x00B23A2F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B23BD5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B24042` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B240C5` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **46**
  - `0x00B23890` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23898` → [DrvDbGetDriverPackageMappedProperty + 0x101](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B238C3` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B2390D` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B2391A` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B2396E` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B239CD` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B239D5` → [DrvDbGetDriverPackageMappedProperty + 0x101](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B239F5` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23A35` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23A3F` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23A49` → [DrvDbGetDriverPackageMappedProperty + 0xBB](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23A51` → [DrvDbGetDriverPackageMappedProperty + 0x101](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23A7E` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23AC1` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23B40` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23B48` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23B97` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23B9F` → [DrvDbGetDriverPackageMappedProperty + 0x101](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23BDB` → [DrvDbGetDriverPackageMappedProperty + 0x20E](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23BE5` → [DrvDbGetDriverPackageMappedProperty + 0x20E](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23BED` → [DrvDbGetDriverPackageMappedProperty + 0x101](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23C2F` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23C8E` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23CEC` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23D2B` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23D33` → [DrvDbGetDriverPackageMappedProperty + 0x101](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23D5E` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23DB8` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23DDE` → [DrvDbGetDriverPackageMappedProperty + 0x101](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23E09` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23E53` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23E60` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23F0D` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23F2C` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23F4C` → [DrvDbGetDriverPackageMappedProperty + 0xF7](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23F54` → [DrvDbGetDriverPackageMappedProperty + 0x101](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23F81` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23FCC` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B23FD7` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B24048` → [DrvDbGetDriverPackageMappedProperty + 0x2C9](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B24050` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B24074` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B24081` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B240CB` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)
  - `0x00B240D2` → [DrvDbGetDriverPackageMappedProperty + 0x1F3](../93/DrvDbGetDriverPackageMappedProperty_function_009305BC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B23888  41 8B 0F                        mov ecx, dword ptr [r15]
00B2388B  03 C9                           add ecx, ecx
00B2388D  41 89 0F                        mov dword ptr [r15], ecx
00B23890  E9 1A CF E0 FF                  jmp 0x1409307af
00B23895  48 85 C0                        test rax, rax
00B23898  0F 85 1F CE E0 FF               jne 0x1409306bd
00B2389E  8D 70 01                        lea esi, [rax + 1]
00B238A1  4D 85 E4                        test r12, r12
00B238A4  75 2D                           jne 0x140b238d3
00B238A6  48 8D 45 A7                     lea rax, [rbp - 0x59]
00B238AA  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
00B238AF  44 8B C6                        mov r8d, esi
00B238B2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B238B7  49 8B CA                        mov rcx, r10
00B238BA  E8 55 D7 E0 FF                  call 0x140931014
00B238BF  8B D8                           mov ebx, eax
00B238C1  85 C0                           test eax, eax
00B238C3  0F 88 E6 CE E0 FF               js 0x1409307af
00B238C9  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
00B238CD  4C 8B 55 47                     mov r10, qword ptr [rbp + 0x47]
00B238D1  EB 03                           jmp 0x140b238d6
00B238D3  4D 8B C4                        mov r8, r12
00B238D6  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00B238D9  4C 8D 0D 58 F0 4F FF            lea r9, [rip - 0xb00fa8]
00B238E0  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00B238E5  48 8B D7                        mov rdx, rdi
00B238E8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B238EC  49 8B CA                        mov rcx, r10
00B238EF  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00B238F3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B238F8  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00B238FD  E8 BA CC E0 FF                  call 0x1409305bc
00B23902  BA 00 00 00 80                  mov edx, 0x80000000
00B23907  8B D8                           mov ebx, eax
00B23909  03 C2                           add eax, edx
00B2390B  85 C2                           test edx, eax
00B2390D  0F 85 9C CE E0 FF               jne 0x1409307af
00B23913  BF 23 00 00 C0                  mov edi, 0xc0000023
00B23918  3B DF                           cmp ebx, edi
00B2391A  0F 84 8F CE E0 FF               je 0x1409307af
00B23920  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
00B23924  48 8D 45 B7                     lea rax, [rbp - 0x49]
00B23928  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
00B2392C  4C 8D 0D F5 DA 4F FF            lea r9, [rip - 0xb0250b]
00B23933  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00B23937  4D 85 E4                        test r12, r12
00B2393A  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00B2393F  C7 44 24 30 04 00 00 00         mov dword ptr [rsp + 0x30], 4
00B23947  4D 0F 45 C4                     cmovne r8, r12
00B2394B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B23950  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00B23955  E8 62 CC E0 FF                  call 0x1409305bc
00B2395A  8B D8                           mov ebx, eax
00B2395C  3B C7                           cmp eax, edi
00B2395E  75 0C                           jne 0x140b2396c
00B23960  33 C0                           xor eax, eax
00B23962  8B D8                           mov ebx, eax
00B23964  83 C8 FF                        or eax, 0xffffffff
00B23967  89 45 B7                        mov dword ptr [rbp - 0x49], eax
00B2396A  EB 24                           jmp 0x140b23990
00B2396C  85 C0                           test eax, eax
00B2396E  0F 88 3B CE E0 FF               js 0x1409307af
00B23974  41 83 7D 00 07                  cmp dword ptr [r13], 7
00B23979  75 E9                           jne 0x140b23964
00B2397B  41 83 3F 04                     cmp dword ptr [r15], 4
00B2397F  75 E3                           jne 0x140b23964
00B23981  8B 45 B7                        mov eax, dword ptr [rbp - 0x49]
00B23984  EB 0A                           jmp 0x140b23990
00B23986  33 C0                           xor eax, eax
00B23988  8B D8                           mov ebx, eax
00B2398A  83 C8 FF                        or eax, 0xffffffff
00B2398D  89 45 B3                        mov dword ptr [rbp - 0x4d], eax
00B23990  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00B23994  41 C7 45 00 11 00 00 00         mov dword ptr [r13], 0x11
00B2399C  41 89 37                        mov dword ptr [r15], esi
00B2399F  48 85 C9                        test rcx, rcx
00B239A2  0F 84 28 07 00 00               je 0x140b240d0
00B239A8  39 75 77                        cmp dword ptr [rbp + 0x77], esi
00B239AB  0F 82 1F 07 00 00               jb 0x140b240d0
00B239B1  F7 D8                           neg eax
00B239B3  1A C0                           sbb al, al
00B239B5  F6 D8                           neg al
00B239B7  40 2A C6                        sub al, sil
00B239BA  EB 0F                           jmp 0x140b239cb
00B239BC  8B 45 BB                        mov eax, dword ptr [rbp - 0x45]
00B239BF  25 00 F0 FF 00                  and eax, 0xfff000
00B239C4  89 45 BB                        mov dword ptr [rbp - 0x45], eax
00B239C7  F7 D8                           neg eax
00B239C9  1A C0                           sbb al, al
00B239CB  88 01                           mov byte ptr [rcx], al
00B239CD  E9 DD CD E0 FF                  jmp 0x1409307af
00B239D2  48 85 C0                        test rax, rax
00B239D5  0F 85 E2 CC E0 FF               jne 0x1409306bd
00B239DB  8D 50 5F                        lea edx, [rax + 0x5f]
00B239DE  48 8B CF                        mov rcx, rdi
00B239E1  E8 6A E4 9D FF                  call 0x140501e50
00B239E6  33 C9                           xor ecx, ecx
00B239E8  4C 8B C8                        mov r9, rax
00B239EB  48 85 C0                        test rax, rax
00B239EE  75 0A                           jne 0x140b239fa
00B239F0  BB 33 00 00 C0                  mov ebx, 0xc0000033
00B239F5  E9 B5 CD E0 FF                  jmp 0x1409307af
00B239FA  48 83 CA FF                     or rdx, 0xffffffffffffffff
00B239FE  48 FF C2                        inc rdx
00B23A01  66 39 4C 50 02                  cmp word ptr [rax + rdx*2 + 2], cx
00B23A06  75 F6                           jne 0x140b239fe
00B23A08  41 89 75 00                     mov dword ptr [r13], esi
00B23A0C  41 8B 0F                        mov ecx, dword ptr [r15]
00B23A0F  83 C1 02                        add ecx, 2
00B23A12  8D 0C 51                        lea ecx, [rcx + rdx*2]
00B23A15  8B C1                           mov eax, ecx
00B23A17  41 89 0F                        mov dword ptr [r15], ecx
00B23A1A  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00B23A1E  48 85 C9                        test rcx, rcx
00B23A21  74 17                           je 0x140b23a3a
00B23A23  39 45 77                        cmp dword ptr [rbp + 0x77], eax
00B23A26  72 12                           jb 0x140b23a3a
00B23A28  44 8B C0                        mov r8d, eax
00B23A2B  49 8D 51 02                     lea rdx, [r9 + 2]
00B23A2F  E8 0C 2E BA FF                  call 0x1406c6840
00B23A34  90                              nop
00B23A35  E9 75 CD E0 FF                  jmp 0x1409307af
00B23A3A  BB 23 00 00 C0                  mov ebx, 0xc0000023
00B23A3F  E9 6B CD E0 FF                  jmp 0x1409307af
00B23A44  48 85 C0                        test rax, rax
00B23A47  74 0E                           je 0x140b23a57
00B23A49  E9 29 CC E0 FF                  jmp 0x140930677
00B23A4E  48 85 C0                        test rax, rax
00B23A51  0F 85 66 CC E0 FF               jne 0x1409306bd
00B23A57  BE 01 00 00 00                  mov esi, 1
00B23A5C  4D 85 E4                        test r12, r12
00B23A5F  75 2B                           jne 0x140b23a8c
00B23A61  48 8D 45 A7                     lea rax, [rbp - 0x59]
00B23A65  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
00B23A6A  44 8B C6                        mov r8d, esi
00B23A6D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B23A72  49 8B CA                        mov rcx, r10
00B23A75  E8 9A D5 E0 FF                  call 0x140931014
00B23A7A  8B D8                           mov ebx, eax
00B23A7C  85 C0                           test eax, eax
00B23A7E  0F 88 2B CD E0 FF               js 0x1409307af
00B23A84  4C 8B 65 A7                     mov r12, qword ptr [rbp - 0x59]
00B23A88  4C 8B 55 47                     mov r10, qword ptr [rbp + 0x47]
00B23A8C  49 8B 0A                        mov rcx, qword ptr [r10]
00B23A8F  48 8D 45 EF                     lea rax, [rbp - 0x11]
00B23A93  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B23A98  4C 8D 05 11 B4 FD FF            lea r8, [rip - 0x24bef]
00B23A9F  45 33 C9                        xor r9d, r9d
00B23AA2  C7 44 24 20 09 00 00 00         mov dword ptr [rsp + 0x20], 9
00B23AAA  49 8B D4                        mov rdx, r12
00B23AAD  E8 06 BD DC FF                  call 0x1408ef7b8
00B23AB2  8B D8                           mov ebx, eax
00B23AB4  3D 34 00 00 C0                  cmp eax, 0xc0000034
00B23AB9  0F 84 13 05 00 00               je 0x140b23fd2
00B23ABF  85 C0                           test eax, eax
00B23AC1  0F 88 E8 CC E0 FF               js 0x1409307af
00B23AC7  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00B23ACB  33 DB                           xor ebx, ebx
00B23ACD  41 83 7E 10 1E                  cmp dword ptr [r14 + 0x10], 0x1e
00B23AD2  66 89 5D E8                     mov word ptr [rbp - 0x18], bx
00B23AD6  88 5D EA                        mov byte ptr [rbp - 0x16], bl
00B23AD9  48 89 4D D7                     mov qword ptr [rbp - 0x29], rcx
00B23ADD  89 5D E3                        mov dword ptr [rbp - 0x1d], ebx
00B23AE0  89 5D EB                        mov dword ptr [rbp - 0x15], ebx
00B23AE3  75 20                           jne 0x140b23b05
00B23AE5  49 8B 06                        mov rax, qword ptr [r14]
00B23AE8  48 2B 05 D1 F7 4F FF            sub rax, qword ptr [rip - 0xb0082f]
00B23AEF  75 0B                           jne 0x140b23afc
00B23AF1  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00B23AF5  48 2B 05 CC F7 4F FF            sub rax, qword ptr [rip - 0xb00834]
00B23AFC  40 88 75 E7                     mov byte ptr [rbp - 0x19], sil
00B23B00  48 85 C0                        test rax, rax
00B23B03  74 03                           je 0x140b23b08
00B23B05  88 5D E7                        mov byte ptr [rbp - 0x19], bl
00B23B08  48 85 C9                        test rcx, rcx
00B23B0B  74 0A                           je 0x140b23b17
00B23B0D  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00B23B10  D1 E8                           shr eax, 1
00B23B12  89 45 DF                        mov dword ptr [rbp - 0x21], eax
00B23B15  EB 03                           jmp 0x140b23b1a
00B23B17  89 5D DF                        mov dword ptr [rbp - 0x21], ebx
00B23B1A  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00B23B1E  4C 8D 4D D7                     lea r9, [rbp - 0x29]
00B23B22  48 8B 55 EF                     mov rdx, qword ptr [rbp - 0x11]
00B23B26  4C 8D 05 13 F3 B7 FF            lea r8, [rip - 0x480ced]
00B23B2D  48 8B 09                        mov rcx, qword ptr [rcx]
00B23B30  E8 37 D9 F7 FF                  call 0x140aa146c
00B23B35  8B D8                           mov ebx, eax
00B23B37  85 C0                           test eax, eax
00B23B39  79 12                           jns 0x140b23b4d
00B23B3B  8B 45 EB                        mov eax, dword ptr [rbp - 0x15]
00B23B3E  85 C0                           test eax, eax
00B23B40  0F 89 69 CC E0 FF               jns 0x1409307af
00B23B46  8B D8                           mov ebx, eax
00B23B48  E9 62 CC E0 FF                  jmp 0x1409307af
00B23B4D  8B 55 E3                        mov edx, dword ptr [rbp - 0x1d]
00B23B50  85 D2                           test edx, edx
00B23B52  0F 84 7A 04 00 00               je 0x140b23fd2
00B23B58  4C 8B 45 D7                     mov r8, qword ptr [rbp - 0x29]
00B23B5C  FF C2                           inc edx
00B23B5E  8B 5D EB                        mov ebx, dword ptr [rbp - 0x15]
00B23B61  41 C7 45 00 12 20 00 00         mov dword ptr [r13], 0x2012
00B23B69  89 55 E3                        mov dword ptr [rbp - 0x1d], edx
00B23B6C  8D 04 12                        lea eax, [rdx + rdx]
00B23B6F  41 89 07                        mov dword ptr [r15], eax
00B23B72  4D 85 C0                        test r8, r8
00B23B75  0F 84 BF FE FF FF               je 0x140b23a3a
00B23B7B  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00B23B7E  8B CA                           mov ecx, edx
00B23B80  48 03 C9                        add rcx, rcx
00B23B83  48 3B C8                        cmp rcx, rax
00B23B86  0F 87 AE FE FF FF               ja 0x140b23a3a
00B23B8C  8D 42 FF                        lea eax, [rdx - 1]
00B23B8F  45 33 E4                        xor r12d, r12d
00B23B92  66 45 89 24 40                  mov word ptr [r8 + rax*2], r12w
00B23B97  E9 13 CC E0 FF                  jmp 0x1409307af
00B23B9C  48 85 C0                        test rax, rax
00B23B9F  0F 85 18 CB E0 FF               jne 0x1409306bd
00B23BA5  41 89 75 00                     mov dword ptr [r13], esi
00B23BA9  48 83 CA FF                     or rdx, 0xffffffffffffffff
00B23BAD  48 FF C2                        inc rdx
00B23BB0  66 44 39 0C 57                  cmp word ptr [rdi + rdx*2], r9w
00B23BB5  75 F6                           jne 0x140b23bad
00B23BB7  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00B23BBB  8D 14 55 02 00 00 00            lea edx, [rdx*2 + 2]
00B23BC2  41 89 17                        mov dword ptr [r15], edx
00B23BC5  48 85 C9                        test rcx, rcx
00B23BC8  74 16                           je 0x140b23be0
00B23BCA  39 55 77                        cmp dword ptr [rbp + 0x77], edx
00B23BCD  72 11                           jb 0x140b23be0
00B23BCF  44 8B C2                        mov r8d, edx
00B23BD2  48 8B D7                        mov rdx, rdi
00B23BD5  E8 66 2C BA FF                  call 0x1406c6840
00B23BDA  90                              nop
00B23BDB  E9 EA CB E0 FF                  jmp 0x1409307ca
00B23BE0  BB 23 00 00 C0                  mov ebx, 0xc0000023
00B23BE5  E9 E0 CB E0 FF                  jmp 0x1409307ca
00B23BEA  48 85 C0                        test rax, rax
00B23BED  0F 85 CA CA E0 FF               jne 0x1409306bd
00B23BF3  8D 70 01                        lea esi, [rax + 1]
00B23BF6  4D 85 E4                        test r12, r12
00B23BF9  75 42                           jne 0x140b23c3d
00B23BFB  48 8D 45 CF                     lea rax, [rbp - 0x31]
00B23BFF  44 8B C1                        mov r8d, ecx
00B23C02  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00B23C07  33 D2                           xor edx, edx
00B23C09  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
00B23C0E  48 8D 45 A7                     lea rax, [rbp - 0x59]
00B23C12  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B23C17  49 8B CA                        mov rcx, r10
00B23C1A  44 88 4C 24 28                  mov byte ptr [rsp + 0x28], r9b
00B23C1F  4C 8B CF                        mov r9, rdi
00B23C22  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00B23C26  E8 35 D4 E0 FF                  call 0x140931060
00B23C2B  8B D8                           mov ebx, eax
00B23C2D  85 C0                           test eax, eax
00B23C2F  0F 88 7A CB E0 FF               js 0x1409307af
00B23C35  4C 8B 65 A7                     mov r12, qword ptr [rbp - 0x59]
00B23C39  4C 8B 55 47                     mov r10, qword ptr [rbp + 0x47]
00B23C3D  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00B23C42  48 8D 45 5F                     lea rax, [rbp + 0x5f]
00B23C46  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00B23C4A  4C 8D 0D 47 D7 4F FF            lea r9, [rip - 0xb028b9]
00B23C51  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B23C56  4D 8B C4                        mov r8, r12
00B23C59  48 8B D7                        mov rdx, rdi
00B23C5C  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00B23C61  49 8B CA                        mov rcx, r10
00B23C64  E8 53 C9 E0 FF                  call 0x1409305bc
00B23C69  33 C9                           xor ecx, ecx
00B23C6B  BF 23 00 00 C0                  mov edi, 0xc0000023
00B23C70  8B D8                           mov ebx, eax
00B23C72  3B C7                           cmp eax, edi
00B23C74  75 0B                           jne 0x140b23c81
00B23C76  48 83 CA FF                     or rdx, 0xffffffffffffffff
00B23C7A  8B D9                           mov ebx, ecx
00B23C7C  88 55 5F                        mov byte ptr [rbp + 0x5f], dl
00B23C7F  EB 2F                           jmp 0x140b23cb0
00B23C81  3D 25 02 00 C0                  cmp eax, 0xc0000225
00B23C86  75 04                           jne 0x140b23c8c
00B23C88  8B D9                           mov ebx, ecx
00B23C8A  EB 77                           jmp 0x140b23d03
00B23C8C  85 C0                           test eax, eax
00B23C8E  0F 88 1B CB E0 FF               js 0x1409307af
00B23C94  41 83 7D 00 11                  cmp dword ptr [r13], 0x11
00B23C99  75 0A                           jne 0x140b23ca5
00B23C9B  41 39 37                        cmp dword ptr [r15], esi
00B23C9E  75 05                           jne 0x140b23ca5
00B23CA0  8A 55 5F                        mov dl, byte ptr [rbp + 0x5f]
00B23CA3  EB 07                           jmp 0x140b23cac
00B23CA5  48 83 CA FF                     or rdx, 0xffffffffffffffff
00B23CA9  88 55 5F                        mov byte ptr [rbp + 0x5f], dl
00B23CAC  84 D2                           test dl, dl
00B23CAE  74 58                           je 0x140b23d08
00B23CB0  48 39 4D A7                     cmp qword ptr [rbp - 0x59], rcx
00B23CB4  75 3F                           jne 0x140b23cf5
00B23CB6  4C 8B 4D 4F                     mov r9, qword ptr [rbp + 0x4f]
00B23CBA  48 8D 45 CF                     lea rax, [rbp - 0x31]
00B23CBE  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00B23CC3  33 D2                           xor edx, edx
00B23CC5  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00B23CCA  48 8D 45 A7                     lea rax, [rbp - 0x59]
00B23CCE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B23CD3  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
00B23CD7  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00B23CDB  44 8D 42 02                     lea r8d, [rdx + 2]
00B23CDF  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00B23CE3  E8 78 D3 E0 FF                  call 0x140931060
00B23CE8  8B D8                           mov ebx, eax
00B23CEA  85 C0                           test eax, eax
00B23CEC  0F 88 BD CA E0 FF               js 0x1409307af
00B23CF2  8A 55 5F                        mov dl, byte ptr [rbp + 0x5f]
00B23CF5  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00B23CF9  8B 48 40                        mov ecx, dword ptr [rax + 0x40]
00B23CFC  F6 C1 10                        test cl, 0x10
00B23CFF  74 07                           je 0x140b23d08
00B23D01  33 C9                           xor ecx, ecx
00B23D03  88 4D 5F                        mov byte ptr [rbp + 0x5f], cl
00B23D06  8A D1                           mov dl, cl
00B23D08  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00B23D0C  41 C7 45 00 11 00 00 00         mov dword ptr [r13], 0x11
00B23D14  41 89 37                        mov dword ptr [r15], esi
00B23D17  48 85 C0                        test rax, rax
00B23D1A  0F 84 B0 03 00 00               je 0x140b240d0
00B23D20  39 75 77                        cmp dword ptr [rbp + 0x77], esi
00B23D23  0F 82 A7 03 00 00               jb 0x140b240d0
00B23D29  88 10                           mov byte ptr [rax], dl
00B23D2B  E9 7F CA E0 FF                  jmp 0x1409307af
00B23D30  48 85 C0                        test rax, rax
00B23D33  0F 85 84 C9 E0 FF               jne 0x1409306bd
00B23D39  8D 70 01                        lea esi, [rax + 1]
00B23D3C  4D 85 E4                        test r12, r12
00B23D3F  75 2B                           jne 0x140b23d6c
00B23D41  48 8D 45 A7                     lea rax, [rbp - 0x59]
00B23D45  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
00B23D4A  44 8B C6                        mov r8d, esi
00B23D4D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B23D52  49 8B CA                        mov rcx, r10
00B23D55  E8 BA D2 E0 FF                  call 0x140931014
00B23D5A  8B D8                           mov ebx, eax
00B23D5C  85 C0                           test eax, eax
00B23D5E  0F 88 4B CA E0 FF               js 0x1409307af
00B23D64  4C 8B 65 A7                     mov r12, qword ptr [rbp - 0x59]
00B23D68  4C 8B 55 47                     mov r10, qword ptr [rbp + 0x47]
00B23D6C  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00B23D71  48 8D 45 B3                     lea rax, [rbp - 0x4d]
00B23D75  C7 44 24 30 04 00 00 00         mov dword ptr [rsp + 0x30], 4
00B23D7D  4C 8D 0D EC DC 4F FF            lea r9, [rip - 0xb02314]
00B23D84  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B23D89  4D 8B C4                        mov r8, r12
00B23D8C  48 8B D7                        mov rdx, rdi
00B23D8F  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00B23D94  49 8B CA                        mov rcx, r10
00B23D97  E8 20 C8 E0 FF                  call 0x1409305bc
00B23D9C  BF 23 00 00 C0                  mov edi, 0xc0000023
00B23DA1  8B D8                           mov ebx, eax
00B23DA3  3B C7                           cmp eax, edi
00B23DA5  0F 84 DB FB FF FF               je 0x140b23986
00B23DAB  3D 25 02 00 C0                  cmp eax, 0xc0000225
00B23DB0  0F 84 D0 FB FF FF               je 0x140b23986
00B23DB6  85 C0                           test eax, eax
00B23DB8  0F 88 F1 C9 E0 FF               js 0x1409307af
00B23DBE  41 83 7D 00 07                  cmp dword ptr [r13], 7
00B23DC3  0F 85 C1 FB FF FF               jne 0x140b2398a
00B23DC9  41 83 3F 04                     cmp dword ptr [r15], 4
00B23DCD  0F 85 B7 FB FF FF               jne 0x140b2398a
00B23DD3  8B 45 B3                        mov eax, dword ptr [rbp - 0x4d]
00B23DD6  E9 B5 FB FF FF                  jmp 0x140b23990
00B23DDB  48 85 C0                        test rax, rax
00B23DDE  0F 85 D9 C8 E0 FF               jne 0x1409306bd
00B23DE4  8D 70 01                        lea esi, [rax + 1]
00B23DE7  4D 85 E4                        test r12, r12
00B23DEA  75 2D                           jne 0x140b23e19
00B23DEC  48 8D 45 A7                     lea rax, [rbp - 0x59]
00B23DF0  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
00B23DF5  44 8B C6                        mov r8d, esi
00B23DF8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B23DFD  49 8B CA                        mov rcx, r10
00B23E00  E8 0F D2 E0 FF                  call 0x140931014
00B23E05  8B D8                           mov ebx, eax
00B23E07  85 C0                           test eax, eax
00B23E09  0F 88 A0 C9 E0 FF               js 0x1409307af
00B23E0F  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
00B23E13  4C 8B 55 47                     mov r10, qword ptr [rbp + 0x47]
00B23E17  EB 03                           jmp 0x140b23e1c
00B23E19  4D 8B C4                        mov r8, r12
00B23E1C  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00B23E1F  4C 8D 0D AA D6 4F FF            lea r9, [rip - 0xb02956]
00B23E26  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00B23E2B  48 8B D7                        mov rdx, rdi
00B23E2E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B23E32  49 8B CA                        mov rcx, r10
00B23E35  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00B23E39  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B23E3E  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00B23E43  E8 74 C7 E0 FF                  call 0x1409305bc
00B23E48  BA 00 00 00 80                  mov edx, 0x80000000
00B23E4D  8B D8                           mov ebx, eax
00B23E4F  03 C2                           add eax, edx
00B23E51  85 C2                           test edx, eax
00B23E53  0F 85 56 C9 E0 FF               jne 0x1409307af
00B23E59  BF 23 00 00 C0                  mov edi, 0xc0000023
00B23E5E  3B DF                           cmp ebx, edi
00B23E60  0F 84 49 C9 E0 FF               je 0x1409307af
00B23E66  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
00B23E6A  48 8D 45 AF                     lea rax, [rbp - 0x51]
00B23E6E  4C 8B 75 4F                     mov r14, qword ptr [rbp + 0x4f]
00B23E72  4C 8D 0D 4F D8 4F FF            lea r9, [rip - 0xb027b1]
00B23E79  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00B23E7D  4D 85 E4                        test r12, r12
00B23E80  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00B23E85  49 8B D6                        mov rdx, r14
00B23E88  C7 44 24 30 04 00 00 00         mov dword ptr [rsp + 0x30], 4
00B23E90  4D 0F 45 C4                     cmovne r8, r12
00B23E94  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B23E99  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00B23E9E  E8 19 C7 E0 FF                  call 0x1409305bc
00B23EA3  8B D8                           mov ebx, eax
00B23EA5  3B C7                           cmp eax, edi
00B23EA7  74 53                           je 0x140b23efc
00B23EA9  3D 25 02 00 C0                  cmp eax, 0xc0000225
00B23EAE  75 7A                           jne 0x140b23f2a
00B23EB0  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
00B23EB4  48 8D 45 AF                     lea rax, [rbp - 0x51]
00B23EB8  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00B23EBC  4C 8D 0D 05 DE 4F FF            lea r9, [rip - 0xb021fb]
00B23EC3  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00B23EC8  4D 85 E4                        test r12, r12
00B23ECB  C7 44 24 30 04 00 00 00         mov dword ptr [rsp + 0x30], 4
00B23ED3  49 8B D6                        mov rdx, r14
00B23ED6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B23EDB  4D 0F 45 C4                     cmovne r8, r12
00B23EDF  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00B23EE4  E8 D3 C6 E0 FF                  call 0x1409305bc
00B23EE9  8B D8                           mov ebx, eax
00B23EEB  3B C7                           cmp eax, edi
00B23EED  74 0D                           je 0x140b23efc
00B23EEF  3D 25 02 00 C0                  cmp eax, 0xc0000225
00B23EF4  75 15                           jne 0x140b23f0b
00B23EF6  33 C0                           xor eax, eax
00B23EF8  8B D8                           mov ebx, eax
00B23EFA  EB 07                           jmp 0x140b23f03
00B23EFC  33 C0                           xor eax, eax
00B23EFE  8B D8                           mov ebx, eax
00B23F00  83 C8 FF                        or eax, 0xffffffff
00B23F03  89 45 AF                        mov dword ptr [rbp - 0x51], eax
00B23F06  E9 85 FA FF FF                  jmp 0x140b23990
00B23F0B  85 C0                           test eax, eax
00B23F0D  0F 88 9C C8 E0 FF               js 0x1409307af
00B23F13  41 83 7D 00 07                  cmp dword ptr [r13], 7
00B23F18  75 E6                           jne 0x140b23f00
00B23F1A  41 83 3F 04                     cmp dword ptr [r15], 4
00B23F1E  75 E0                           jne 0x140b23f00
00B23F20  8B 45 AF                        mov eax, dword ptr [rbp - 0x51]
00B23F23  25 0F 10 00 80                  and eax, 0x8000100f
00B23F28  EB D9                           jmp 0x140b23f03
00B23F2A  85 C0                           test eax, eax
00B23F2C  0F 88 7D C8 E0 FF               js 0x1409307af
00B23F32  41 83 7D 00 07                  cmp dword ptr [r13], 7
00B23F37  75 C7                           jne 0x140b23f00
00B23F39  41 83 3F 04                     cmp dword ptr [r15], 4
00B23F3D  75 C1                           jne 0x140b23f00
00B23F3F  8B 45 AF                        mov eax, dword ptr [rbp - 0x51]
00B23F42  E9 49 FA FF FF                  jmp 0x140b23990
00B23F47  48 85 C0                        test rax, rax
00B23F4A  74 0E                           je 0x140b23f5a
00B23F4C  E9 62 C7 E0 FF                  jmp 0x1409306b3
00B23F51  48 85 C0                        test rax, rax
00B23F54  0F 85 63 C7 E0 FF               jne 0x1409306bd
00B23F5A  BE 01 00 00 00                  mov esi, 1
00B23F5F  4D 85 E4                        test r12, r12
00B23F62  75 2B                           jne 0x140b23f8f
00B23F64  48 8D 45 A7                     lea rax, [rbp - 0x59]
00B23F68  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
00B23F6D  44 8B C6                        mov r8d, esi
00B23F70  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B23F75  49 8B CA                        mov rcx, r10
00B23F78  E8 97 D0 E0 FF                  call 0x140931014
00B23F7D  8B D8                           mov ebx, eax
00B23F7F  85 C0                           test eax, eax
00B23F81  0F 88 28 C8 E0 FF               js 0x1409307af
00B23F87  4C 8B 65 A7                     mov r12, qword ptr [rbp - 0x59]
00B23F8B  4C 8B 55 47                     mov r10, qword ptr [rbp + 0x47]
00B23F8F  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00B23F94  48 8D 45 BB                     lea rax, [rbp - 0x45]
00B23F98  C7 44 24 30 04 00 00 00         mov dword ptr [rsp + 0x30], 4
00B23FA0  4C 8D 0D 09 F0 4F FF            lea r9, [rip - 0xb00ff7]
00B23FA7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B23FAC  4D 8B C4                        mov r8, r12
00B23FAF  48 8B D7                        mov rdx, rdi
00B23FB2  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00B23FB7  49 8B CA                        mov rcx, r10
00B23FBA  E8 FD C5 E0 FF                  call 0x1409305bc
00B23FBF  8B D8                           mov ebx, eax
00B23FC1  85 C0                           test eax, eax
00B23FC3  79 17                           jns 0x140b23fdc
00B23FC5  BF 23 00 00 C0                  mov edi, 0xc0000023
00B23FCA  3B C7                           cmp eax, edi
00B23FCC  0F 85 DD C7 E0 FF               jne 0x1409307af
00B23FD2  BB 25 02 00 C0                  mov ebx, 0xc0000225
00B23FD7  E9 D3 C7 E0 FF                  jmp 0x1409307af
00B23FDC  41 83 7D 00 07                  cmp dword ptr [r13], 7
00B23FE1  75 EF                           jne 0x140b23fd2
00B23FE3  41 83 3F 04                     cmp dword ptr [r15], 4
00B23FE7  75 E9                           jne 0x140b23fd2
00B23FE9  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00B23FED  41 C7 45 00 11 00 00 00         mov dword ptr [r13], 0x11
00B23FF5  41 89 37                        mov dword ptr [r15], esi
00B23FF8  48 85 C9                        test rcx, rcx
00B23FFB  0F 84 39 FA FF FF               je 0x140b23a3a
00B24001  39 75 77                        cmp dword ptr [rbp + 0x77], esi
00B24004  0F 82 30 FA FF FF               jb 0x140b23a3a
00B2400A  41 83 7E 10 35                  cmp dword ptr [r14 + 0x10], 0x35
00B2400F  0F 85 A7 F9 FF FF               jne 0x140b239bc
00B24015  49 8B 06                        mov rax, qword ptr [r14]
00B24018  48 2B 05 09 E5 4F FF            sub rax, qword ptr [rip - 0xb01af7]
00B2401F  75 0B                           jne 0x140b2402c
00B24021  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00B24025  48 2B 05 04 E5 4F FF            sub rax, qword ptr [rip - 0xb01afc]
00B2402C  48 85 C0                        test rax, rax
00B2402F  0F 85 87 F9 FF FF               jne 0x140b239bc
00B24035  8B 45 BB                        mov eax, dword ptr [rbp - 0x45]
00B24038  25 F0 0F 00 00                  and eax, 0xff0
00B2403D  E9 82 F9 FF FF                  jmp 0x140b239c4
00B24042  E8 F9 27 BA FF                  call 0x1406c6840
00B24047  90                              nop
00B24048  E9 38 C8 E0 FF                  jmp 0x140930885
00B2404D  48 85 C0                        test rax, rax
00B24050  0F 85 59 C7 E0 FF               jne 0x1409307af
00B24056  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
00B2405A  4C 8D 4D C7                     lea r9, [rbp - 0x39]
00B2405E  48 8B 55 4F                     mov rdx, qword ptr [rbp + 0x4f]
00B24062  4D 85 E4                        test r12, r12
00B24065  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00B24069  4D 0F 45 C4                     cmovne r8, r12
00B2406D  E8 B6 B3 E0 FF                  call 0x14092f428
00B24072  85 C0                           test eax, eax
00B24074  0F 88 35 C7 E0 FF               js 0x1409307af
00B2407A  81 7D C7 03 00 00 0D            cmp dword ptr [rbp - 0x39], 0xd000003
00B24081  0F 85 28 C7 E0 FF               jne 0x1409307af
00B24087  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
00B2408B  33 DB                           xor ebx, ebx
00B2408D  41 C7 45 00 12 00 00 00         mov dword ptr [r13], 0x12
00B24095  41 C7 07 24 00 00 00            mov dword ptr [r15], 0x24
00B2409C  48 85 C9                        test rcx, rcx
00B2409F  74 2F                           je 0x140b240d0
00B240A1  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00B240A4  83 F8 24                        cmp eax, 0x24
00B240A7  72 27                           jb 0x140b240d0
00B240A9  8B D0                           mov edx, eax
00B240AB  C7 44 24 28 00 08 00 00         mov dword ptr [rsp + 0x28], 0x800
00B240B3  48 D1 EA                        shr rdx, 1
00B240B6  4C 8D 05 F3 98 FE FF            lea r8, [rip - 0x1670d]
00B240BD  45 33 C9                        xor r9d, r9d
00B240C0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00B240C5  E8 F6 A0 8F FF                  call 0x14041e1c0
00B240CA  90                              nop
00B240CB  E9 DF C6 E0 FF                  jmp 0x1409307af
00B240D0  8B DF                           mov ebx, edi
00B240D2  E9 D8 C6 E0 FF                  jmp 0x1409307af
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B23888(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;

    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15))) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15)))));
    *(unsigned int *)(v_r15) = (unsigned int)(a1);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B23888(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;

    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15))) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15)))));
    *(uint32_t *)(local_r15) = (uint32_t)(Arg1);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B23888&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
