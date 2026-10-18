# sub_00B444BA

- RVA: `0x00B444BA`–`0x00B44AC4` (길이 `1,546` bytes)
- VA: `0x0000000140B444BA`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B7B0C`
- 디코드: `409`개 명령, `1,546/1,546` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00B445E5` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (function, `0x0045488C`)
- `0x00B44676` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x00B446A7` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x00B44718` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (function, `0x0026E9A4`)
- `0x00B44879` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x00B44A5B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B445CF` → RVA `0x00B03E60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B4465A` → RVA `0x00B05530` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B44683` → RVA `0x00B05550` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B44700` → RVA `0x00B05520` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B44709` → RVA `0x00B05510` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00B445E5` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (`PAGE` → `.text`)
  - `0x00B44676` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
  - `0x00B446A7` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
  - `0x00B44718` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (`PAGE` → `.text`)
  - `0x00B44879` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
  - `0x00B44A5B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **17**
  - `0x00B44880` → [RtlFormatMessageEx + 0x1A5](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B44894` → [RtlFormatMessageEx + 0x1A5](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B448CF` → [RtlFormatMessageEx + 0x12D](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B448E7` → [RtlFormatMessageEx + 0x1A5](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B44904` → [RtlFormatMessageEx + 0xFF](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B44911` → [RtlFormatMessageEx + 0x1A5](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B44939` → [RtlFormatMessageEx + 0x1A5](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B44963` → [RtlFormatMessageEx + 0x1A5](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B4497B` → [RtlFormatMessageEx + 0x1A5](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B44995` → [RtlFormatMessageEx + 0x1A5](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B449C0` → [RtlFormatMessageEx + 0xFF](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B449CB` → [RtlFormatMessageEx + 0x173](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B449D9` → [RtlFormatMessageEx + 0xE5](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B44A31` → [RtlFormatMessageEx + 0x1A5](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B44A8C` → [RtlFormatMessageEx + 0x1A5](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B44AB5` → [RtlFormatMessageEx + 0xBA](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)
  - `0x00B44ABF` → [RtlFormatMessageEx + 0x142](../A8/RtlFormatMessageEx_function_00A860E0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B444BA  0F B7 0F                        movzx ecx, word ptr [rdi]
00B444BD  48 8B D3                        mov rdx, rbx
00B444C0  48 89 5D 98                     mov qword ptr [rbp - 0x68], rbx
00B444C4  8D 41 CF                        lea eax, [rcx - 0x31]
00B444C7  66 3B 45 90                     cmp ax, word ptr [rbp - 0x70]
00B444CB  0F 87 F6 03 00 00               ja 0x140b448c7
00B444D1  49 03 FF                        add rdi, r15
00B444D4  41 B8 30 00 00 00               mov r8d, 0x30
00B444DA  8B F1                           mov esi, ecx
00B444DC  41 2B F0                        sub esi, r8d
00B444DF  0F B7 17                        movzx edx, word ptr [rdi]
00B444E2  0F B7 C2                        movzx eax, dx
00B444E5  66 41 3B D0                     cmp dx, r8w
00B444E9  72 44                           jb 0x140b4452f
00B444EB  83 FA 39                        cmp edx, 0x39
00B444EE  77 3F                           ja 0x140b4452f
00B444F0  8D 34 B6                        lea esi, [rsi + rsi*4]
00B444F3  49 03 FF                        add rdi, r15
00B444F6  8D 76 E8                        lea esi, [rsi - 0x18]
00B444F9  8D 34 72                        lea esi, [rdx + rsi*2]
00B444FC  0F B7 17                        movzx edx, word ptr [rdi]
00B444FF  0F B7 C2                        movzx eax, dx
00B44502  66 41 3B D0                     cmp dx, r8w
00B44506  72 27                           jb 0x140b4452f
00B44508  83 FA 39                        cmp edx, 0x39
00B4450B  77 22                           ja 0x140b4452f
00B4450D  49 03 FF                        add rdi, r15
00B44510  8D 34 B6                        lea esi, [rsi + rsi*4]
00B44513  8D 76 E8                        lea esi, [rsi - 0x18]
00B44516  8D 34 72                        lea esi, [rdx + rsi*2]
00B44519  0F B7 0F                        movzx ecx, word ptr [rdi]
00B4451C  0F B7 C1                        movzx eax, cx
00B4451F  66 41 3B C8                     cmp cx, r8w
00B44523  72 0A                           jb 0x140b4452f
00B44525  66 83 F9 39                     cmp cx, 0x39
00B44529  0F 86 8B 05 00 00               jbe 0x140b44aba
00B4452F  44 8B FE                        mov r15d, esi
00B44532  44 89 64 24 68                  mov dword ptr [rsp + 0x68], r12d
00B44537  FF CE                           dec esi
00B44539  66 83 F8 21                     cmp ax, 0x21
00B4453D  0F 85 81 00 00 00               jne 0x140b445c4
00B44543  45 33 C9                        xor r9d, r9d
00B44546  48 8D 8D F2 05 00 00            lea rcx, [rbp + 0x5f2]
00B4454D  45 8A C1                        mov r8b, r9b
00B44550  48 83 C7 02                     add rdi, 2
00B44554  41 8D 41 25                     lea eax, [r9 + 0x25]
00B44558  66 89 85 F0 05 00 00            mov word ptr [rbp + 0x5f0], ax
00B4455F  48 8D 85 F2 05 00 00            lea rax, [rbp + 0x5f2]
00B44566  0F B7 17                        movzx edx, word ptr [rdi]
00B44569  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00B4456E  66 83 FA 21                     cmp dx, 0x21
00B44572  74 46                           je 0x140b445ba
00B44574  66 85 D2                        test dx, dx
00B44577  0F 84 3D 05 00 00               je 0x140b44aba
00B4457D  4C 8D 8D 2E 06 00 00            lea r9, [rbp + 0x62e]
00B44584  49 3B C1                        cmp rax, r9
00B44587  0F 83 2D 05 00 00               jae 0x140b44aba
00B4458D  66 83 FA 2A                     cmp dx, 0x2a
00B44591  75 14                           jne 0x140b445a7
00B44593  41 8B C4                        mov eax, r12d
00B44596  41 FF C4                        inc r12d
00B44599  44 89 64 24 68                  mov dword ptr [rsp + 0x68], r12d
00B4459E  83 F8 01                        cmp eax, 1
00B445A1  0F 87 13 05 00 00               ja 0x140b44aba
00B445A7  66 89 11                        mov word ptr [rcx], dx
00B445AA  48 83 C7 02                     add rdi, 2
00B445AE  48 83 C1 02                     add rcx, 2
00B445B2  48 8B C1                        mov rax, rcx
00B445B5  45 33 C9                        xor r9d, r9d
00B445B8  EB AC                           jmp 0x140b44566
00B445BA  48 83 C7 02                     add rdi, 2
00B445BE  66 44 89 09                     mov word ptr [rcx], r9w
00B445C2  EB 3B                           jmp 0x140b445ff
00B445C4  33 C0                           xor eax, eax
00B445C6  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
00B445CB  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00B445CF  4C 8D 05 8A F8 FB FF            lea r8, [rip - 0x40776]
00B445D6  48 8D 8D F0 05 00 00            lea rcx, [rbp + 0x5f0]
00B445DD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B445E2  8D 50 40                        lea edx, [rax + 0x40]
00B445E5  E8 A2 02 91 FF                  call 0x14045488c
00B445EA  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00B445EF  41 B0 01                        mov r8b, 1
00B445F2  4C 8B 5C 24 60                  mov r11, qword ptr [rsp + 0x60]
00B445F7  45 33 C9                        xor r9d, r9d
00B445FA  44 8A 54 24 50                  mov r10b, byte ptr [rsp + 0x50]
00B445FF  45 84 D2                        test r10b, r10b
00B44602  0F 84 A9 00 00 00               je 0x140b446b1
00B44608  41 80 F8 01                     cmp r8b, 1
00B4460C  74 72                           je 0x140b44680
00B4460E  0F B7 8D F0 05 00 00            movzx ecx, word ptr [rbp + 0x5f0]
00B44615  B8 25 00 00 00                  mov eax, 0x25
00B4461A  0F B7 C0                        movzx eax, ax
00B4461D  2B C8                           sub ecx, eax
00B4461F  75 1E                           jne 0x140b4463f
00B44621  0F B7 8D F2 05 00 00            movzx ecx, word ptr [rbp + 0x5f2]
00B44628  83 E9 73                        sub ecx, 0x73
00B4462B  75 12                           jne 0x140b4463f
00B4462D  0F B7 8D F4 05 00 00            movzx ecx, word ptr [rbp + 0x5f4]
00B44634  45 33 E4                        xor r12d, r12d
00B44637  41 0F B7 C4                     movzx eax, r12w
00B4463B  2B C8                           sub ecx, eax
00B4463D  EB 03                           jmp 0x140b44642
00B4463F  45 33 E4                        xor r12d, r12d
00B44642  85 C9                           test ecx, ecx
00B44644  74 3D                           je 0x140b44683
00B44646  48 8D 85 F2 05 00 00            lea rax, [rbp + 0x5f2]
00B4464D  49 63 D6                        movsxd rdx, r14d
00B44650  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B44655  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00B4465A  48 8D 05 CF 0E FC FF            lea rax, [rip - 0x3f131]
00B44661  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00B44666  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B4466B  45 33 C9                        xor r9d, r9d
00B4466E  48 8B CB                        mov rcx, rbx
00B44671  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00B44676  E8 15 6D 8E FF                  call 0x14042b390
00B4467B  E9 FE 01 00 00                  jmp 0x140b4487e
00B44680  45 33 E4                        xor r12d, r12d
00B44683  48 8D 05 C6 0E FC FF            lea rax, [rip - 0x3f13a]
00B4468A  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00B4468F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B44694  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00B44699  49 63 D6                        movsxd rdx, r14d
00B4469C  45 33 C9                        xor r9d, r9d
00B4469F  48 8B CB                        mov rcx, rbx
00B446A2  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00B446A7  E8 E4 6C 8E FF                  call 0x14042b390
00B446AC  E9 CD 01 00 00                  jmp 0x140b4487e
00B446B1  4D 85 DB                        test r11, r11
00B446B4  0F 84 00 04 00 00               je 0x140b44aba
00B446BA  41 8D 04 34                     lea eax, [r12 + rsi]
00B446BE  3D C8 00 00 00                  cmp eax, 0xc8
00B446C3  0F 83 F1 03 00 00               jae 0x140b44aba
00B446C9  44 38 4C 24 51                  cmp byte ptr [rsp + 0x51], r9b
00B446CE  0F 84 88 00 00 00               je 0x140b4475c
00B446D4  4C 8D 49 FE                     lea r9, [rcx - 2]
00B446D8  41 B8 63 00 00 00               mov r8d, 0x63
00B446DE  41 0F B7 01                     movzx eax, word ptr [r9]
00B446E2  66 41 3B C0                     cmp ax, r8w
00B446E6  75 37                           jne 0x140b4471f
00B446E8  0F B7 41 FC                     movzx eax, word ptr [rcx - 4]
00B446EC  66 83 E8 68                     sub ax, 0x68
00B446F0  66 83 F8 0F                     cmp ax, 0xf
00B446F4  77 0A                           ja 0x140b44700
00B446F6  B9 11 80 00 00                  mov ecx, 0x8011
00B446FB  0F A3 C1                        bt ecx, eax
00B446FE  72 59                           jb 0x140b44759
00B44700  4C 8D 05 19 0E FC FF            lea r8, [rip - 0x3f1e7]
00B44707  EB 07                           jmp 0x140b44710
00B44709  4C 8D 05 00 0E FC FF            lea r8, [rip - 0x3f200]
00B44710  BA 03 00 00 00                  mov edx, 3
00B44715  49 8B C9                        mov rcx, r9
00B44718  E8 87 A2 72 FF                  call 0x14026e9a4
00B4471D  EB 3A                           jmp 0x140b44759
00B4471F  BA 73 00 00 00                  mov edx, 0x73
00B44724  66 3B C2                        cmp ax, dx
00B44727  75 1A                           jne 0x140b44743
00B44729  0F B7 41 FC                     movzx eax, word ptr [rcx - 4]
00B4472D  66 83 E8 68                     sub ax, 0x68
00B44731  66 83 F8 0F                     cmp ax, 0xf
00B44735  77 D2                           ja 0x140b44709
00B44737  B9 11 80 00 00                  mov ecx, 0x8011
00B4473C  0F A3 C1                        bt ecx, eax
00B4473F  72 18                           jb 0x140b44759
00B44741  EB C6                           jmp 0x140b44709
00B44743  66 83 F8 53                     cmp ax, 0x53
00B44747  75 06                           jne 0x140b4474f
00B44749  66 41 89 11                     mov word ptr [r9], dx
00B4474D  EB 0A                           jmp 0x140b44759
00B4474F  66 83 F8 43                     cmp ax, 0x43
00B44753  75 04                           jne 0x140b44759
00B44755  66 45 89 01                     mov word ptr [r9], r8w
00B44759  45 33 C9                        xor r9d, r9d
00B4475C  44 8B 7C 24 54                  mov r15d, dword ptr [rsp + 0x54]
00B44761  41 3B F7                        cmp esi, r15d
00B44764  72 47                           jb 0x140b447ad
00B44766  41 BC 08 00 00 00               mov r12d, 8
00B4476C  45 8D 47 01                     lea r8d, [r15 + 1]
00B44770  41 8B D7                        mov edx, r15d
00B44773  44 38 8D A0 06 00 00            cmp byte ptr [rbp + 0x6a0], r9b
00B4477A  74 08                           je 0x140b44784
00B4477C  49 8B 03                        mov rax, qword ptr [r11]
00B4477F  4D 03 DC                        add r11, r12
00B44782  EB 0D                           jmp 0x140b44791
00B44784  49 8B 0B                        mov rcx, qword ptr [r11]
00B44787  48 8D 41 08                     lea rax, [rcx + 8]
00B4478B  49 89 03                        mov qword ptr [r11], rax
00B4478E  48 8B 01                        mov rax, qword ptr [rcx]
00B44791  48 89 44 D5 B0                  mov qword ptr [rbp + rdx*8 - 0x50], rax
00B44796  45 8B F8                        mov r15d, r8d
00B44799  44 3B C6                        cmp r8d, esi
00B4479C  76 CE                           jbe 0x140b4476c
00B4479E  44 8B 64 24 68                  mov r12d, dword ptr [rsp + 0x68]
00B447A3  4C 89 5C 24 60                  mov qword ptr [rsp + 0x60], r11
00B447A8  44 89 44 24 54                  mov dword ptr [rsp + 0x54], r8d
00B447AD  4C 8B 54 F5 B0                  mov r10, qword ptr [rbp + rsi*8 - 0x50]
00B447B2  33 C0                           xor eax, eax
00B447B4  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
00B447B9  44 8B C0                        mov r8d, eax
00B447BC  45 85 E4                        test r12d, r12d
00B447BF  0F 84 83 00 00 00               je 0x140b44848
00B447C5  38 85 A0 06 00 00               cmp byte ptr [rbp + 0x6a0], al
00B447CB  74 21                           je 0x140b447ee
00B447CD  4D 8B 0B                        mov r9, qword ptr [r11]
00B447D0  41 8B C7                        mov eax, r15d
00B447D3  41 FF C7                        inc r15d
00B447D6  44 89 7C 24 54                  mov dword ptr [rsp + 0x54], r15d
00B447DB  4C 89 4C C5 B0                  mov qword ptr [rbp + rax*8 - 0x50], r9
00B447E0  41 8D 40 08                     lea eax, [r8 + 8]
00B447E4  4C 03 D8                        add r11, rax
00B447E7  4C 89 5C 24 60                  mov qword ptr [rsp + 0x60], r11
00B447EC  EB 12                           jmp 0x140b44800
00B447EE  49 8B 0B                        mov rcx, qword ptr [r11]
00B447F1  48 8D 41 08                     lea rax, [rcx + 8]
00B447F5  49 89 03                        mov qword ptr [r11], rax
00B447F8  B8 08 00 00 00                  mov eax, 8
00B447FD  4C 8B 09                        mov r9, qword ptr [rcx]
00B44800  41 83 FC 01                     cmp r12d, 1
00B44804  76 42                           jbe 0x140b44848
00B44806  41 8B D7                        mov edx, r15d
00B44809  45 33 E4                        xor r12d, r12d
00B4480C  41 FF C7                        inc r15d
00B4480F  44 89 7C 24 54                  mov dword ptr [rsp + 0x54], r15d
00B44814  44 38 A5 A0 06 00 00            cmp byte ptr [rbp + 0x6a0], r12b
00B4481B  74 12                           je 0x140b4482f
00B4481D  4D 8B 03                        mov r8, qword ptr [r11]
00B44820  4C 03 D8                        add r11, rax
00B44823  4C 89 5C 24 60                  mov qword ptr [rsp + 0x60], r11
00B44828  4C 89 44 D5 B0                  mov qword ptr [rbp + rdx*8 - 0x50], r8
00B4482D  EB 1C                           jmp 0x140b4484b
00B4482F  49 8B 0B                        mov rcx, qword ptr [r11]
00B44832  44 89 7C 24 54                  mov dword ptr [rsp + 0x54], r15d
00B44837  48 8D 41 08                     lea rax, [rcx + 8]
00B4483B  49 89 03                        mov qword ptr [r11], rax
00B4483E  4C 8B 01                        mov r8, qword ptr [rcx]
00B44841  4C 89 44 D5 B0                  mov qword ptr [rbp + rdx*8 - 0x50], r8
00B44846  EB 03                           jmp 0x140b4484b
00B44848  45 33 E4                        xor r12d, r12d
00B4484B  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00B44850  48 8D 85 F0 05 00 00            lea rax, [rbp + 0x5f0]
00B44857  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
00B4485C  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00B44861  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
00B44866  45 33 C9                        xor r9d, r9d
00B44869  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B4486E  48 8B CB                        mov rcx, rbx
00B44871  49 63 D6                        movsxd rdx, r14d
00B44874  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00B44879  E8 12 6B 8E FF                  call 0x14042b390
00B4487E  85 C0                           test eax, eax
00B44880  0F 88 FF 19 F4 FF               js 0x140a86285
00B44886  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00B4488B  48 2B C3                        sub rax, rbx
00B4488E  48 D1 F8                        sar rax, 1
00B44891  44 2B F0                        sub r14d, eax
00B44894  0F 88 EB 19 F4 FF               js 0x140a86285
00B4489A  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00B4489F  41 BF 02 00 00 00               mov r15d, 2
00B448A5  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
00B448A9  4C 8B 5C 24 60                  mov r11, qword ptr [rsp + 0x60]
00B448AE  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
00B448B2  44 8B 4C 24 6C                  mov r9d, dword ptr [rsp + 0x6c]
00B448B7  44 8A 54 24 50                  mov r10b, byte ptr [rsp + 0x50]
00B448BC  48 98                           cdqe
00B448BE  48 8D 1C 43                     lea rbx, [rbx + rax*2]
00B448C2  E9 DD 00 00 00                  jmp 0x140b449a4
00B448C7  B8 30 00 00 00                  mov eax, 0x30
00B448CC  66 3B C8                        cmp cx, ax
00B448CF  0F 84 38 19 F4 FF               je 0x140a8620d
00B448D5  66 85 C9                        test cx, cx
00B448D8  0F 84 DC 01 00 00               je 0x140b44aba
00B448DE  83 F9 72                        cmp ecx, 0x72
00B448E1  75 26                           jne 0x140b44909
00B448E3  41 83 EE 01                     sub r14d, 1
00B448E7  0F 88 98 19 F4 FF               js 0x140a86285
00B448ED  8D 48 DD                        lea ecx, [rax - 0x23]
00B448F0  66 89 0B                        mov word ptr [rbx], cx
00B448F3  49 03 DF                        add rbx, r15
00B448F6  49 03 FF                        add rdi, r15
00B448F9  BA 0A 00 00 00                  mov edx, 0xa
00B448FE  4D 8B EC                        mov r13, r12
00B44901  41 8B F4                        mov esi, r12d
00B44904  E9 D6 18 F4 FF                  jmp 0x140a861df
00B44909  83 F9 6E                        cmp ecx, 0x6e
00B4490C  75 22                           jne 0x140b44930
00B4490E  45 2B F7                        sub r14d, r15d
00B44911  0F 88 6E 19 F4 FF               js 0x140a86285
00B44917  B9 0D 00 00 00                  mov ecx, 0xd
00B4491C  66 89 0B                        mov word ptr [rbx], cx
00B4491F  49 03 DF                        add rbx, r15
00B44922  8D 51 FD                        lea edx, [rcx - 3]
00B44925  66 89 13                        mov word ptr [rbx], dx
00B44928  49 03 DF                        add rbx, r15
00B4492B  49 03 FF                        add rdi, r15
00B4492E  EB CE                           jmp 0x140b448fe
00B44930  83 F9 74                        cmp ecx, 0x74
00B44933  75 25                           jne 0x140b4495a
00B44935  41 83 EE 01                     sub r14d, 1
00B44939  0F 88 46 19 F4 FF               js 0x140a86285
00B4493F  40 F6 C6 07                     test sil, 7
00B44943  74 08                           je 0x140b4494d
00B44945  83 C6 07                        add esi, 7
00B44948  83 E6 F8                        and esi, 0xfffffff8
00B4494B  EB 03                           jmp 0x140b44950
00B4494D  83 C6 08                        add esi, 8
00B44950  4C 8B EB                        mov r13, rbx
00B44953  66 C7 03 09 00                  mov word ptr [rbx], 9
00B44958  EB 44                           jmp 0x140b4499e
00B4495A  83 F9 62                        cmp ecx, 0x62
00B4495D  75 14                           jne 0x140b44973
00B4495F  41 83 EE 01                     sub r14d, 1
00B44963  0F 88 1C 19 F4 FF               js 0x140a86285
00B44969  4C 8B EB                        mov r13, rbx
00B4496C  66 C7 03 20 00                  mov word ptr [rbx], 0x20
00B44971  EB 2B                           jmp 0x140b4499e
00B44973  45 84 D2                        test r10b, r10b
00B44976  74 19                           je 0x140b44991
00B44978  45 2B F7                        sub r14d, r15d
00B4497B  0F 88 04 19 F4 FF               js 0x140a86285
00B44981  66 C7 03 25 00                  mov word ptr [rbx], 0x25
00B44986  49 03 DF                        add rbx, r15
00B44989  0F B7 07                        movzx eax, word ptr [rdi]
00B4498C  66 89 03                        mov word ptr [rbx], ax
00B4498F  EB 0D                           jmp 0x140b4499e
00B44991  41 83 EE 01                     sub r14d, 1
00B44995  0F 88 EA 18 F4 FF               js 0x140a86285
00B4499B  66 89 0B                        mov word ptr [rbx], cx
00B4499E  49 03 DF                        add rbx, r15
00B449A1  49 03 FF                        add rdi, r15
00B449A4  B9 0D 00 00 00                  mov ecx, 0xd
00B449A9  48 85 D2                        test rdx, rdx
00B449AC  0F 84 47 FF FF FF               je 0x140b448f9
00B449B2  48 8B C3                        mov rax, rbx
00B449B5  48 2B C2                        sub rax, rdx
00B449B8  8D 51 FD                        lea edx, [rcx - 3]
00B449BB  48 D1 F8                        sar rax, 1
00B449BE  03 F0                           add esi, eax
00B449C0  E9 1A 18 F4 FF                  jmp 0x140a861df
00B449C5  49 03 FF                        add rdi, r15
00B449C8  45 85 C9                        test r9d, r9d
00B449CB  0F 84 82 18 F4 FF               je 0x140a86253
00B449D1  4C 8B EB                        mov r13, rbx
00B449D4  B8 20 00 00 00                  mov eax, 0x20
00B449D9  E9 E7 17 F4 FF                  jmp 0x140a861c5
00B449DE  0F B7 02                        movzx eax, word ptr [rdx]
00B449E1  66 41 3B C1                     cmp ax, r9w
00B449E5  74 06                           je 0x140b449ed
00B449E7  66 41 3B C4                     cmp ax, r12w
00B449EB  75 08                           jne 0x140b449f5
00B449ED  49 03 D7                        add rdx, r15
00B449F0  48 3B D3                        cmp rdx, rbx
00B449F3  75 E9                           jne 0x140b449de
00B449F5  41 BC 00 00 00 00               mov r12d, 0
00B449FB  4D 3B E8                        cmp r13, r8
00B449FE  76 20                           jbe 0x140b44a20
00B44A00  45 8D 54 24 09                  lea r10d, [r12 + 9]
00B44A05  49 8D 4D FE                     lea rcx, [r13 - 2]
00B44A09  0F B7 01                        movzx eax, word ptr [rcx]
00B44A0C  66 41 3B C1                     cmp ax, r9w
00B44A10  74 06                           je 0x140b44a18
00B44A12  66 41 3B C2                     cmp ax, r10w
00B44A16  75 08                           jne 0x140b44a20
00B44A18  4C 8B E9                        mov r13, rcx
00B44A1B  49 3B C8                        cmp rcx, r8
00B44A1E  77 E5                           ja 0x140b44a05
00B44A20  48 8B C2                        mov rax, rdx
00B44A23  49 2B C5                        sub rax, r13
00B44A26  48 D1 F8                        sar rax, 1
00B44A29  83 F8 01                        cmp eax, 1
00B44A2C  75 0B                           jne 0x140b44a39
00B44A2E  44 2B F0                        sub r14d, eax
00B44A31  0F 88 4E 18 F4 FF               js 0x140a86285
00B44A37  EB 0C                           jmp 0x140b44a45
00B44A39  41 3B C7                        cmp eax, r15d
00B44A3C  76 07                           jbe 0x140b44a45
00B44A3E  41 83 C6 FE                     add r14d, -2
00B44A42  44 03 F0                        add r14d, eax
00B44A45  48 2B DA                        sub rbx, rdx
00B44A48  49 8D 4D 04                     lea rcx, [r13 + 4]
00B44A4C  48 D1 FB                        sar rbx, 1
00B44A4F  48 8B F3                        mov rsi, rbx
00B44A52  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00B44A57  4C 8D 04 1B                     lea r8, [rbx + rbx]
00B44A5B  E8 E0 1D B8 FF                  call 0x1406c6840
00B44A60  44 8B 4C 24 6C                  mov r9d, dword ptr [rsp + 0x6c]
00B44A65  B9 0D 00 00 00                  mov ecx, 0xd
00B44A6A  8B C3                           mov eax, ebx
00B44A6C  66 41 89 4D 00                  mov word ptr [r13], cx
00B44A71  4D 03 EF                        add r13, r15
00B44A74  8D 51 FD                        lea edx, [rcx - 3]
00B44A77  48 8D 1C 45 00 00 00 00         lea rbx, [rax*2]
00B44A7F  66 41 89 55 00                  mov word ptr [r13], dx
00B44A84  49 03 DD                        add rbx, r13
00B44A87  EB 1A                           jmp 0x140b44aa3
00B44A89  45 2B F7                        sub r14d, r15d
00B44A8C  0F 88 F3 17 F4 FF               js 0x140a86285
00B44A92  66 89 0B                        mov word ptr [rbx], cx
00B44A95  41 8B F4                        mov esi, r12d
00B44A98  49 03 DF                        add rbx, r15
00B44A9B  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00B44AA0  66 89 13                        mov word ptr [rbx], dx
00B44AA3  4C 8B 5C 24 60                  mov r11, qword ptr [rsp + 0x60]
00B44AA8  48 83 C3 02                     add rbx, 2
00B44AAC  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
00B44AB0  44 8A 54 24 50                  mov r10b, byte ptr [rsp + 0x50]
00B44AB5  E9 E0 16 F4 FF                  jmp 0x140a8619a
00B44ABA  B8 0D 00 00 C0                  mov eax, 0xc000000d
00B44ABF  E9 5E 17 F4 FF                  jmp 0x140a86222
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B444BA(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, unsigned __int8 a10, __int64 a11, __int64 a12, unsigned int a13, __int64 a14, __int64 a15)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p50;
    unsigned __int8 v_stack_p51;
    unsigned int v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned __int64 v_stack_p70;

    *(unsigned __int64 *)(v_rbp - 104) = v_rbx;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi) - 49)) > (*(unsigned __int16 *)(v_rbp - 112))) goto loc_00B448C7;
    v_rdi = (v_rdi) + (v_r15);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rdi)))) - (48));
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi))) < 48) goto loc_00B4452F;
    if (((unsigned int)(*(unsigned __int16 *)(v_rdi))) > 57) goto loc_00B4452F;
    v_rdi = (v_rdi) + (v_r15);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi))) < 48) goto loc_00B4452F;
    if (((unsigned int)(*(unsigned __int16 *)(v_rdi))) > 57) goto loc_00B4452F;
    v_rdi = (v_rdi) + (v_r15);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi))) < 48) goto loc_00B4452F;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi))) <= 57) goto loc_00B44ABA;
loc_00B4452F:
    v_stack_p68 = (unsigned int)(v_r12);
    v_rsi = (unsigned int)((*(unsigned __int16 *)(v_rdi) + *(unsigned __int16 *)(v_rdi) + v_rsi + v_rsi * 4 - 24 * 2 + *(unsigned __int16 *)(v_rdi) + v_rsi + v_rsi * 4 - 24 * 2 * 4 - 24 * 2) - 1);
    if (((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rdi)))) != 33) goto loc_00B445C4;
    a4 = 0;
    v_rdi = (v_rdi) + (2);
    *(unsigned __int16 *)(v_rbp + 1520) = (unsigned __int16)(a4 + 37);
loc_00B44566:
    v_stack_p70 = v_rbp + 1522;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi))) == 33) goto loc_00B445BA;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rdi)) == 0) goto loc_00B44ABA;
    if ((v_rbp + 1522) >= (v_rbp + 1582)) goto loc_00B44ABA;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi))) != 42) goto loc_00B445A7;
    v_r12 = (unsigned int)((v_r12) + 1);
    v_stack_p68 = (unsigned int)(v_r12);
    if (((unsigned int)((unsigned int)((unsigned int)(v_r12)))) > 1) goto loc_00B44ABA;
loc_00B445A7:
    *(unsigned __int16 *)(v_rbp + 1522) = (unsigned __int16)(*(unsigned __int16 *)(v_rdi));
    v_rdi = (v_rdi) + (2);
    a1 = (v_rbp + 1522) + (2);
    a4 = 0;
    goto loc_00B44566;
loc_00B445BA:
    v_rdi = (v_rdi) + (2);
    *(unsigned __int16 *)(a1) = 0;
    goto loc_00B445FF;
loc_00B445C4:
    result = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = RtlStringCbCopyExW(v_rbp + 1520, result + 64, v_rip - 264054, a14);
    a4 = 0;
loc_00B445FF:
    if (a10 == 0) goto loc_00B446B1;
    if (1 == 1) goto loc_00B44680;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rbp + 1520)) - (37));
    if (condition_is_not_equal) goto loc_00B4463F;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rbp + 1522)) - (115));
    if (condition_is_not_equal) goto loc_00B4463F;
    v_r12 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rbp + 1524)) - (0));
    goto loc_00B44642;
loc_00B4463F:
    v_r12 = 0;
loc_00B44642:
    if ((unsigned int)(a1) == 0) goto loc_00B44683;
    v_stack_p38 = v_rbp + 1522;
    v_stack_p30 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rdi) + *(unsigned __int16 *)(v_rdi) + v_rsi + v_rsi * 4 - 24 * 2 + *(unsigned __int16 *)(v_rdi) + v_rsi + v_rsi * 4 - 24 * 2 * 4 - 24 * 2)));
    v_stack_p28 = v_rip - 258353;
    a4 = 0;
    v_stack_p20 = 0;
    result = RtlStringCchPrintfExW(v_rbx, (int)((unsigned int)(v_r14)), a15, a4);
    goto loc_00B4487E;
loc_00B44680:
    v_r12 = 0;
loc_00B44683:
    v_stack_p30 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rdi) + *(unsigned __int16 *)(v_rdi) + v_rsi + v_rsi * 4 - 24 * 2 + *(unsigned __int16 *)(v_rdi) + v_rsi + v_rsi * 4 - 24 * 2 * 4 - 24 * 2)));
    v_stack_p28 = v_rip - 258362;
    a4 = 0;
    v_stack_p20 = 0;
    result = RtlStringCchPrintfExW(v_rbx, (int)((unsigned int)(v_r14)), a15, a4);
    goto loc_00B4487E;
loc_00B446B1:
    if (a12 == 0) goto loc_00B44ABA;
    if (((unsigned int)(v_r12 + v_rsi * 1)) >= 200) goto loc_00B44ABA;
    if (v_stack_p51 == 0) goto loc_00B4475C;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx - 2))) != 99) goto loc_00B4471F;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rbx - 4)) - (104));
    if (((unsigned __int16)(result)) > 15) goto loc_00B44700;
    if (((unsigned __int16)(result)) < 15) goto loc_00B44759;
loc_00B44700:
    goto loc_00B44710;
loc_00B44709:
loc_00B44710:
    result = RtlStringCchCopyW(v_rbx - 2, 3, v_rip - 258560, v_rbx - 2);
    goto loc_00B44759;
loc_00B4471F:
    if (((unsigned __int16)(result)) != 115) goto loc_00B44743;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rbx - 2 - 4)) - (104));
    if (((unsigned __int16)(result)) > 15) goto loc_00B44709;
    if (((unsigned __int16)(result)) < 15) goto loc_00B44759;
    goto loc_00B44709;
loc_00B44743:
    if (((unsigned __int16)(result)) != 83) goto loc_00B4474F;
    *(unsigned __int16 *)(v_rbx - 2) = 115;
    goto loc_00B44759;
loc_00B4474F:
    if (((unsigned __int16)(result)) == 67) {
        *(unsigned __int16 *)(v_rbx - 2) = (unsigned __int16)(v_rip - 258560);
    }
    a4 = 0;
loc_00B4475C:
    if (((unsigned int)(v_rsi)) < ((unsigned int)((unsigned int)(v_stack_p54)))) goto loc_00B447AD;
loc_00B4476C:
    if ((*(unsigned __int8 *)(v_rbp + 1696)) == 0) goto loc_00B44784;
    v_r11 = (a12) + (8);
    goto loc_00B44791;
loc_00B44784:
    *(unsigned __int64 *)(v_r11) = *(unsigned __int64 *)(v_r11) + 8;
loc_00B44791:
    *(unsigned __int64 *)(v_rbp + (unsigned int)((unsigned int)((unsigned int)(v_stack_p54))) * 8 - 80) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11));
    if (((unsigned int)((unsigned int)(v_stack_p54) + 1)) <= ((unsigned int)(v_rsi))) goto loc_00B4476C;
    v_stack_p60 = v_r11;
    v_stack_p54 = (unsigned int)((unsigned int)(v_stack_p54) + 1);
loc_00B447AD:
    result = 0;
    v_stack_p70 = *(unsigned __int64 *)(v_rbp + v_rsi * 8 - 80);
    if ((unsigned int)((unsigned int)(a13)) == 0) goto loc_00B44848;
    if ((*(unsigned __int8 *)(v_rbp + 1696)) == 0) goto loc_00B447EE;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p54) + 1))) + 1);
    v_stack_p54 = (unsigned int)(v_r15);
    *(unsigned __int64 *)(v_rbp + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p54) + 1)))) * 8 - 80) = *(unsigned __int64 *)(v_r11);
    v_r11 = (v_r11) + (0 + 8);
    v_stack_p60 = v_r11;
    goto loc_00B44800;
loc_00B447EE:
    *(unsigned __int64 *)(v_r11) = *(unsigned __int64 *)(v_r11) + 8;
loc_00B44800:
    if (((unsigned int)((unsigned int)(a13))) <= 1) goto loc_00B44848;
    v_r12 = 0;
    v_r15 = (unsigned int)((v_r15) + 1);
    v_stack_p54 = (unsigned int)(v_r15);
    if ((*(unsigned __int8 *)(v_rbp + 1696)) == 0) goto loc_00B4482F;
    v_r11 = (v_r11) + (8);
    v_stack_p60 = v_r11;
    *(unsigned __int64 *)(v_rbp + (unsigned int)((unsigned int)(v_r15)) * 8 - 80) = *(unsigned __int64 *)(v_r11);
    goto loc_00B4484B;
loc_00B4482F:
    v_stack_p54 = (unsigned int)(v_r15);
    *(unsigned __int64 *)(v_r11) = *(unsigned __int64 *)(v_r11) + 8;
    *(unsigned __int64 *)(v_rbp + (unsigned int)((unsigned int)(v_r15)) * 8 - 80) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11));
    goto loc_00B4484B;
loc_00B44848:
    v_r12 = 0;
loc_00B4484B:
    v_stack_p40 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11));
    v_stack_p38 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11));
    v_stack_p30 = *(unsigned __int64 *)(v_rbp + v_rsi * 8 - 80);
    a4 = 0;
    v_stack_p28 = v_rbp + 1520;
    v_stack_p20 = 0;
    result = RtlStringCchPrintfExW(v_rbx, (int)((unsigned int)(v_r14)), a15, a4);
loc_00B4487E:
    result = (a15) - (v_rbx);
    result = (result) >> (1);
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)(result)));
    goto loc_00B449A4;
loc_00B448C7:
    if ((unsigned __int16)(v_rbx) == 0) goto loc_00B44ABA;
    if (((unsigned int)(v_rbx)) != 114) goto loc_00B44909;
    v_r14 = (unsigned int)((v_r14) - (1));
    *(unsigned __int16 *)(v_rbx + result * 2) = (unsigned __int16)(48 - 35);
    v_rbx = (v_rbx + result * 2) + (2);
    v_rdi = (v_rdi) + (2);
loc_00B448F9:
loc_00B448FE:
loc_00B44909:
    if (((unsigned int)(48 - 35)) != 110) goto loc_00B44930;
    v_r14 = (unsigned int)((v_r14) - (2));
    *(unsigned __int16 *)(v_rbx) = 13;
    v_rbx = (v_rbx) + (2);
    *(unsigned __int16 *)(v_rbx) = (unsigned __int16)(13 - 3);
    v_rbx = (v_rbx) + (2);
    v_rdi = (v_rdi) + (2);
    goto loc_00B448FE;
loc_00B44930:
    if (13 != 116) goto loc_00B4495A;
    v_r14 = (unsigned int)((v_r14) - (1));
    if (((0) & (7)) == 0) goto loc_00B4494D;
    v_rsi = (unsigned int)((0) + (7));
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFF8ULL));
    goto loc_00B44950;
loc_00B4494D:
    v_rsi = (unsigned int)((v_rsi) + (8));
loc_00B44950:
    *(unsigned __int16 *)(v_rbx) = 9;
    goto loc_00B4499E;
loc_00B4495A:
    if (13 != 98) goto loc_00B44973;
    v_r14 = (unsigned int)((v_r14) - (1));
    *(unsigned __int16 *)(v_rbx) = 32;
    goto loc_00B4499E;
loc_00B44973:
    if (a10 == 0) goto loc_00B44991;
    v_r14 = (unsigned int)((v_r14) - (2));
    *(unsigned __int16 *)(v_rbx) = 37;
    v_rbx = (v_rbx) + (2);
    *(unsigned __int16 *)(v_rbx) = (unsigned __int16)(*(unsigned __int16 *)(v_rdi));
    goto loc_00B4499E;
loc_00B44991:
    v_r14 = (unsigned int)((v_r14) - (1));
    *(unsigned __int16 *)(v_rbx) = 13;
loc_00B4499E:
    v_rbx = (v_rbx) + (2);
    v_rdi = (v_rdi) + (2);
loc_00B449A4:
    if (13 - 3 == 0) goto loc_00B448F9;
    result = (v_rbx) - (13 - 3);
    result = (result) >> (1);
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(result)));
loc_00B44ABA:
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B444BA(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint8_t Arg10, int64_t Arg11, int64_t Arg12, uint32_t Arg13, int64_t Arg14, int64_t Arg15)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p50;
    uint8_t v_stack_p51;
    uint32_t v_stack_p54;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint64_t v_stack_p70;

    *(uint64_t *)(local_rbp - 0x68) = local_rbx;
    if (((uint16_t)(*(uint16_t *)(local_rdi) - 49)) > (*(uint16_t *)(local_rbp - 0x70))) goto loc_00B448C7;
    local_rdi = (local_rdi) + (local_r15);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rdi)))) - (48));
    if (((uint16_t)(*(uint16_t *)(local_rdi))) < 48) goto loc_00B4452F;
    if (((uint32_t)(*(uint16_t *)(local_rdi))) > 57) goto loc_00B4452F;
    local_rdi = (local_rdi) + (local_r15);
    if (((uint16_t)(*(uint16_t *)(local_rdi))) < 48) goto loc_00B4452F;
    if (((uint32_t)(*(uint16_t *)(local_rdi))) > 57) goto loc_00B4452F;
    local_rdi = (local_rdi) + (local_r15);
    if (((uint16_t)(*(uint16_t *)(local_rdi))) < 48) goto loc_00B4452F;
    if (((uint16_t)(*(uint16_t *)(local_rdi))) <= 57) goto loc_00B44ABA;
loc_00B4452F:
    v_stack_p68 = (uint32_t)(local_r12);
    local_rsi = (uint32_t)((*(uint16_t *)(local_rdi) + *(uint16_t *)(local_rdi) + local_rsi + local_rsi * 4 - 24 * 2 + *(uint16_t *)(local_rdi) + local_rsi + local_rsi * 4 - 24 * 2 * 4 - 24 * 2) - 1);
    if (((uint16_t)((uint16_t)(*(uint16_t *)(local_rdi)))) != 33) goto loc_00B445C4;
    Arg4 = 0;
    local_rdi = (local_rdi) + (2);
    *(uint16_t *)(local_rbp + 0x5F0) = (uint16_t)(Arg4 + 37);
loc_00B44566:
    v_stack_p70 = local_rbp + 1522;
    if (((uint16_t)(*(uint16_t *)(local_rdi))) == 33) goto loc_00B445BA;
    if ((uint16_t)(*(uint16_t *)(local_rdi)) == 0) goto loc_00B44ABA;
    if ((local_rbp + 1522) >= (local_rbp + 1582)) goto loc_00B44ABA;
    if (((uint16_t)(*(uint16_t *)(local_rdi))) != 42) goto loc_00B445A7;
    local_r12 = (uint32_t)((local_r12) + 1);
    v_stack_p68 = (uint32_t)(local_r12);
    if (((uint32_t)((uint32_t)((uint32_t)(local_r12)))) > 1) goto loc_00B44ABA;
loc_00B445A7:
    *(uint16_t *)(local_rbp + 0x5F2) = (uint16_t)(*(uint16_t *)(local_rdi));
    local_rdi = (local_rdi) + (2);
    Arg1 = (local_rbp + 1522) + (2);
    Arg4 = 0;
    goto loc_00B44566;
loc_00B445BA:
    local_rdi = (local_rdi) + (2);
    *(uint16_t *)(Arg1) = 0;
    goto loc_00B445FF;
loc_00B445C4:
    result = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = RtlStringCbCopyExW(local_rbp + 1520, result + 64, v_rip - 264054, Arg14);
    Arg4 = 0;
loc_00B445FF:
    if (Arg10 == 0) goto loc_00B446B1;
    if (1 == 1) goto loc_00B44680;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rbp + 0x5F0)) - (37));
    if (condition_is_not_equal) goto loc_00B4463F;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rbp + 0x5F2)) - (115));
    if (condition_is_not_equal) goto loc_00B4463F;
    local_r12 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rbp + 0x5F4)) - (0));
    goto loc_00B44642;
loc_00B4463F:
    local_r12 = 0;
loc_00B44642:
    if ((uint32_t)(Arg1) == 0) goto loc_00B44683;
    v_stack_p38 = local_rbp + 1522;
    v_stack_p30 = (uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(local_rdi) + *(uint16_t *)(local_rdi) + local_rsi + local_rsi * 4 - 24 * 2 + *(uint16_t *)(local_rdi) + local_rsi + local_rsi * 4 - 24 * 2 * 4 - 24 * 2)));
    v_stack_p28 = v_rip - 258353;
    Arg4 = 0;
    v_stack_p20 = 0;
    result = RtlStringCchPrintfExW(local_rbx, (int32_t)((uint32_t)(local_r14)), Arg15, Arg4);
    goto loc_00B4487E;
loc_00B44680:
    local_r12 = 0;
loc_00B44683:
    v_stack_p30 = (uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(local_rdi) + *(uint16_t *)(local_rdi) + local_rsi + local_rsi * 4 - 24 * 2 + *(uint16_t *)(local_rdi) + local_rsi + local_rsi * 4 - 24 * 2 * 4 - 24 * 2)));
    v_stack_p28 = v_rip - 258362;
    Arg4 = 0;
    v_stack_p20 = 0;
    result = RtlStringCchPrintfExW(local_rbx, (int32_t)((uint32_t)(local_r14)), Arg15, Arg4);
    goto loc_00B4487E;
loc_00B446B1:
    if (Arg12 == 0) goto loc_00B44ABA;
    if (((uint32_t)(local_r12 + local_rsi * 1)) >= 200) goto loc_00B44ABA;
    if (v_stack_p51 == 0) goto loc_00B4475C;
    if (((uint16_t)(*(uint16_t *)(local_rbx - 0x2))) != 99) goto loc_00B4471F;
    result = (uint16_t)((*(uint16_t *)(local_rbx - 0x4)) - (104));
    if (((uint16_t)(result)) > 15) goto loc_00B44700;
    if (((uint16_t)(result)) < 15) goto loc_00B44759;
loc_00B44700:
    goto loc_00B44710;
loc_00B44709:
loc_00B44710:
    result = RtlStringCchCopyW(local_rbx - 2, 3, v_rip - 258560, local_rbx - 2);
    goto loc_00B44759;
loc_00B4471F:
    if (((uint16_t)(result)) != 115) goto loc_00B44743;
    result = (uint16_t)((*(uint16_t *)(local_rbx - 0x2 - 0x4)) - (104));
    if (((uint16_t)(result)) > 15) goto loc_00B44709;
    if (((uint16_t)(result)) < 15) goto loc_00B44759;
    goto loc_00B44709;
loc_00B44743:
    if (((uint16_t)(result)) != 83) goto loc_00B4474F;
    *(uint16_t *)(local_rbx - 0x2) = 115;
    goto loc_00B44759;
loc_00B4474F:
    if (((uint16_t)(result)) == 67) {
        *(uint16_t *)(local_rbx - 0x2) = (uint16_t)(v_rip - 258560);
    }
    Arg4 = 0;
loc_00B4475C:
    if (((uint32_t)(local_rsi)) < ((uint32_t)((uint32_t)(v_stack_p54)))) goto loc_00B447AD;
loc_00B4476C:
    if ((*(uint8_t *)(local_rbp + 0x6A0)) == 0) goto loc_00B44784;
    local_r11 = (Arg12) + (8);
    goto loc_00B44791;
loc_00B44784:
    *(uint64_t *)(local_r11) = *(uint64_t *)(local_r11) + 8;
loc_00B44791:
    *(uint64_t *)(local_rbp + (uint32_t)((uint32_t)((uint32_t)(v_stack_p54))) * 8 - 0x50) = *(uint64_t *)(*(uint64_t *)(local_r11));
    if (((uint32_t)((uint32_t)(v_stack_p54) + 1)) <= ((uint32_t)(local_rsi))) goto loc_00B4476C;
    v_stack_p60 = local_r11;
    v_stack_p54 = (uint32_t)((uint32_t)(v_stack_p54) + 1);
loc_00B447AD:
    result = 0;
    v_stack_p70 = *(uint64_t *)(local_rbp + local_rsi * 8 - 0x50);
    if ((uint32_t)((uint32_t)(Arg13)) == 0) goto loc_00B44848;
    if ((*(uint8_t *)(local_rbp + 0x6A0)) == 0) goto loc_00B447EE;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p54) + 1))) + 1);
    v_stack_p54 = (uint32_t)(local_r15);
    *(uint64_t *)(local_rbp + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p54) + 0x1)))) * 8 - 0x50) = *(uint64_t *)(local_r11);
    local_r11 = (local_r11) + (0 + 8);
    v_stack_p60 = local_r11;
    goto loc_00B44800;
loc_00B447EE:
    *(uint64_t *)(local_r11) = *(uint64_t *)(local_r11) + 8;
loc_00B44800:
    if (((uint32_t)((uint32_t)(Arg13))) <= 1) goto loc_00B44848;
    local_r12 = 0;
    local_r15 = (uint32_t)((local_r15) + 1);
    v_stack_p54 = (uint32_t)(local_r15);
    if ((*(uint8_t *)(local_rbp + 0x6A0)) == 0) goto loc_00B4482F;
    local_r11 = (local_r11) + (8);
    v_stack_p60 = local_r11;
    *(uint64_t *)(local_rbp + (uint32_t)((uint32_t)(local_r15)) * 8 - 0x50) = *(uint64_t *)(local_r11);
    goto loc_00B4484B;
loc_00B4482F:
    v_stack_p54 = (uint32_t)(local_r15);
    *(uint64_t *)(local_r11) = *(uint64_t *)(local_r11) + 8;
    *(uint64_t *)(local_rbp + (uint32_t)((uint32_t)(local_r15)) * 8 - 0x50) = *(uint64_t *)(*(uint64_t *)(local_r11));
    goto loc_00B4484B;
loc_00B44848:
    local_r12 = 0;
loc_00B4484B:
    v_stack_p40 = *(uint64_t *)(*(uint64_t *)(local_r11));
    v_stack_p38 = *(uint64_t *)(*(uint64_t *)(local_r11));
    v_stack_p30 = *(uint64_t *)(local_rbp + local_rsi * 8 - 0x50);
    Arg4 = 0;
    v_stack_p28 = local_rbp + 1520;
    v_stack_p20 = 0;
    result = RtlStringCchPrintfExW(local_rbx, (int32_t)((uint32_t)(local_r14)), Arg15, Arg4);
loc_00B4487E:
    result = (Arg15) - (local_rbx);
    result = (result) >> (1);
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)(result)));
    goto loc_00B449A4;
loc_00B448C7:
    if ((uint16_t)(local_rbx) == 0) goto loc_00B44ABA;
    if (((uint32_t)(local_rbx)) != 114) goto loc_00B44909;
    local_r14 = (uint32_t)((local_r14) - (1));
    *(uint16_t *)(local_rbx + result * 2) = (uint16_t)(48 - 35);
    local_rbx = (local_rbx + result * 2) + (2);
    local_rdi = (local_rdi) + (2);
loc_00B448F9:
loc_00B448FE:
loc_00B44909:
    if (((uint32_t)(48 - 35)) != 110) goto loc_00B44930;
    local_r14 = (uint32_t)((local_r14) - (2));
    *(uint16_t *)(local_rbx) = 13;
    local_rbx = (local_rbx) + (2);
    *(uint16_t *)(local_rbx) = (uint16_t)(13 - 3);
    local_rbx = (local_rbx) + (2);
    local_rdi = (local_rdi) + (2);
    goto loc_00B448FE;
loc_00B44930:
    if (13 != 116) goto loc_00B4495A;
    local_r14 = (uint32_t)((local_r14) - (1));
    if (((0) & (7)) == 0) goto loc_00B4494D;
    local_rsi = (uint32_t)((0) + (7));
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFF8ULL));
    goto loc_00B44950;
loc_00B4494D:
    local_rsi = (uint32_t)((local_rsi) + (8));
loc_00B44950:
    *(uint16_t *)(local_rbx) = 9;
    goto loc_00B4499E;
loc_00B4495A:
    if (13 != 98) goto loc_00B44973;
    local_r14 = (uint32_t)((local_r14) - (1));
    *(uint16_t *)(local_rbx) = 32;
    goto loc_00B4499E;
loc_00B44973:
    if (Arg10 == 0) goto loc_00B44991;
    local_r14 = (uint32_t)((local_r14) - (2));
    *(uint16_t *)(local_rbx) = 37;
    local_rbx = (local_rbx) + (2);
    *(uint16_t *)(local_rbx) = (uint16_t)(*(uint16_t *)(local_rdi));
    goto loc_00B4499E;
loc_00B44991:
    local_r14 = (uint32_t)((local_r14) - (1));
    *(uint16_t *)(local_rbx) = 13;
loc_00B4499E:
    local_rbx = (local_rbx) + (2);
    local_rdi = (local_rdi) + (2);
loc_00B449A4:
    if (13 - 3 == 0) goto loc_00B448F9;
    result = (local_rbx) - (13 - 3);
    result = (result) >> (1);
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(result)));
loc_00B44ABA:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B444BA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
