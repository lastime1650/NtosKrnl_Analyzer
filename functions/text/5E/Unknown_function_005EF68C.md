# sub_005EF68C

- RVA: `0x005EF68C`–`0x005EFC62` (길이 `1,494` bytes)
- VA: `0x00000001405EF68C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D00B8`
- 디코드: `398`개 명령, `1,494/1,494` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005EF71F` → [XpressBuildHuffmanDecodingTable](../3C/XpressBuildHuffmanDecodingTable_function_003C8DA0.md) (function, `0x003C8DA0`)
- `0x005EF801` → [RtlpMakeXpressCallback](../41/RtlpMakeXpressCallback_function_0041A7F0.md) (function, `0x0041A7F0`)
- `0x005EF9E7` → [RtlpMakeXpressCallback](../41/RtlpMakeXpressCallback_function_0041A7F0.md) (function, `0x0041A7F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x005EF851` → [sub_005EFC6A](Unknown_function_005EFC6A.md) (`tail-transfer`)
  - `0x005EFB0F` → [sub_005EFC6A + 0x8](Unknown_function_005EFC6A.md) (`tail-transfer`)
  - `0x005EFC34` → [sub_005EFC6A + 0x8](Unknown_function_005EFC6A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
005EF68C  48 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], rsi
005EF694  48 8D 70 07                     lea rsi, [rax + 7]
005EF698  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
005EF6A0  48 83 E6 F8                     and rsi, 0xfffffffffffffff8
005EF6A4  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
005EF6AC  48 8B F9                        mov rdi, rcx
005EF6AF  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
005EF6B7  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
005EF6BC  45 8B E1                        mov r12d, r9d
005EF6BF  44 8B D2                        mov r10d, edx
005EF6C2  4D 03 E0                        add r12, r8
005EF6C5  4C 03 D1                        add r10, rcx
005EF6C8  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
005EF6CD  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
005EF6D2  48 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rsi
005EF6DA  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
005EF6DF  48 85 C0                        test rax, rax
005EF6E2  74 04                           je 0x1405ef6e8
005EF6E4  3B D3                           cmp edx, ebx
005EF6E6  73 09                           jae 0x1405ef6f1
005EF6E8  8B DA                           mov ebx, edx
005EF6EA  89 94 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], edx
005EF6F1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
005EF6F6  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
005EF6FE  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005EF703  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
005EF707  49 8B C4                        mov rax, r12
005EF70A  48 2B C5                        sub rax, rbp
005EF70D  48 3D 04 01 00 00               cmp rax, 0x104
005EF713  0F 8C 18 05 00 00               jl 0x1405efc31
005EF719  48 8B D5                        mov rdx, rbp
005EF71C  48 8B CE                        mov rcx, rsi
005EF71F  E8 7C 96 DD FF                  call 0x1403c8da0
005EF724  85 C0                           test eax, eax
005EF726  0F 85 0A 05 00 00               jne 0x1405efc36
005EF72C  4C 8B 54 24 20                  mov r10, qword ptr [rsp + 0x20]
005EF731  44 8D 78 10                     lea r15d, [rax + 0x10]
005EF735  BA 00 01 00 00                  mov edx, 0x100
005EF73A  49 8B CA                        mov rcx, r10
005EF73D  48 03 EA                        add rbp, rdx
005EF740  0F B7 45 02                     movzx eax, word ptr [rbp + 2]
005EF744  44 0F B7 75 00                  movzx r14d, word ptr [rbp]
005EF749  48 83 C5 04                     add rbp, 4
005EF74D  41 C1 E6 10                     shl r14d, 0x10
005EF751  44 03 F0                        add r14d, eax
005EF754  48 8D 87 00 00 01 00            lea rax, [rdi + 0x10000]
005EF75B  49 3B C2                        cmp rax, r10
005EF75E  48 0F 46 C8                     cmovbe rcx, rax
005EF762  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
005EF767  4C 8D A9 44 FF FF FF            lea r13, [rcx - 0xbc]
005EF76E  49 3B FD                        cmp rdi, r13
005EF771  0F 83 CE 02 00 00               jae 0x1405efa45
005EF777  44 8B CB                        mov r9d, ebx
005EF77A  4C 03 CF                        add r9, rdi
005EF77D  4D 3B E9                        cmp r13, r9
005EF780  4D 0F 42 CD                     cmovb r9, r13
005EF784  EB 08                           jmp 0x1405ef78e
005EF786  48 8B B4 24 A8 00 00 00         mov rsi, qword ptr [rsp + 0xa8]
005EF78E  41 8B C6                        mov eax, r14d
005EF791  48 C1 E8 16                     shr rax, 0x16
005EF795  48 0F BF 9C 46 20 04 00 00      movsx rbx, word ptr [rsi + rax*2 + 0x420]
005EF79E  66 85 DB                        test bx, bx
005EF7A1  7F 2A                           jg 0x1405ef7cd
005EF7A3  41 C1 E6 0A                     shl r14d, 0xa
005EF7A7  49 83 EF 0A                     sub r15, 0xa
005EF7AB  41 8B C6                        mov eax, r14d
005EF7AE  49 FF CF                        dec r15
005EF7B1  C1 E8 1F                        shr eax, 0x1f
005EF7B4  45 03 F6                        add r14d, r14d
005EF7B7  66 2B C3                        sub ax, bx
005EF7BA  48 0F BF C0                     movsx rax, ax
005EF7BE  0F B7 9C 46 20 0C 00 00         movzx ebx, word ptr [rsi + rax*2 + 0xc20]
005EF7C6  66 85 DB                        test bx, bx
005EF7C9  7E E0                           jle 0x1405ef7ab
005EF7CB  EB 0C                           jmp 0x1405ef7d9
005EF7CD  48 8B CB                        mov rcx, rbx
005EF7D0  83 E1 0F                        and ecx, 0xf
005EF7D3  41 D3 E6                        shl r14d, cl
005EF7D6  4C 2B F9                        sub r15, rcx
005EF7D9  66 C1 EB 04                     shr bx, 4
005EF7DD  0F B7 F3                        movzx esi, bx
005EF7E0  66 2B F2                        sub si, dx
005EF7E3  4D 85 FF                        test r15, r15
005EF7E6  79 4A                           jns 0x1405ef832
005EF7E8  49 3B F9                        cmp rdi, r9
005EF7EB  72 1C                           jb 0x1405ef809
005EF7ED  49 3B FD                        cmp rdi, r13
005EF7F0  0F 83 C1 02 00 00               jae 0x1405efab7
005EF7F6  4C 8B C7                        mov r8, rdi
005EF7F9  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
005EF7FE  49 8B D5                        mov rdx, r13
005EF801  E8 EA AF E2 FF                  call 0x14041a7f0
005EF806  4C 8B C8                        mov r9, rax
005EF809  48 8D 4D 01                     lea rcx, [rbp + 1]
005EF80D  49 3B CC                        cmp rcx, r12
005EF810  0F 83 20 04 00 00               jae 0x1405efc36
005EF816  0F B7 55 00                     movzx edx, word ptr [rbp]
005EF81A  41 0F B6 CF                     movzx ecx, r15b
005EF81E  F6 D9                           neg cl
005EF820  48 83 C5 02                     add rbp, 2
005EF824  D3 E2                           shl edx, cl
005EF826  44 03 F2                        add r14d, edx
005EF829  BA 00 01 00 00                  mov edx, 0x100
005EF82E  49 83 C7 10                     add r15, 0x10
005EF832  66 85 F6                        test si, si
005EF835  79 0B                           jns 0x1405ef842
005EF837  40 88 37                        mov byte ptr [rdi], sil
005EF83A  48 FF C7                        inc rdi
005EF83D  E9 44 FF FF FF                  jmp 0x1405ef786
005EF842  4C 8B 54 24 20                  mov r10, qword ptr [rsp + 0x20]
005EF847  75 0E                           jne 0x1405ef857
005EF849  49 3B EC                        cmp rbp, r12
005EF84C  72 09                           jb 0x1405ef857
005EF84E  49 3B FA                        cmp rdi, r10
005EF851  0F 84 13 04 00 00               je 0x1405efc6a
005EF857  0F B7 CB                        movzx ecx, bx
005EF85A  2B CA                           sub ecx, edx
005EF85C  8B C1                           mov eax, ecx
005EF85E  99                              cdq
005EF85F  83 E2 0F                        and edx, 0xf
005EF862  03 C2                           add eax, edx
005EF864  C1 F8 04                        sar eax, 4
005EF867  48 63 F0                        movsxd rsi, eax
005EF86A  81 E1 0F 00 00 80               and ecx, 0x8000000f
005EF870  7D 07                           jge 0x1405ef879
005EF872  FF C9                           dec ecx
005EF874  83 C9 F0                        or ecx, 0xfffffff0
005EF877  FF C1                           inc ecx
005EF879  48 63 D9                        movsxd rbx, ecx
005EF87C  48 83 FB 0F                     cmp rbx, 0xf
005EF880  75 69                           jne 0x1405ef8eb
005EF882  49 3B EC                        cmp rbp, r12
005EF885  0F 83 AB 03 00 00               jae 0x1405efc36
005EF88B  0F B6 5D 00                     movzx ebx, byte ptr [rbp]
005EF88F  48 FF C5                        inc rbp
005EF892  48 81 FB FF 00 00 00            cmp rbx, 0xff
005EF899  75 4C                           jne 0x1405ef8e7
005EF89B  48 8D 45 01                     lea rax, [rbp + 1]
005EF89F  49 3B C4                        cmp rax, r12
005EF8A2  0F 83 8E 03 00 00               jae 0x1405efc36
005EF8A8  0F B7 5D 00                     movzx ebx, word ptr [rbp]
005EF8AC  48 83 C5 02                     add rbp, 2
005EF8B0  48 85 DB                        test rbx, rbx
005EF8B3  75 14                           jne 0x1405ef8c9
005EF8B5  48 8D 45 03                     lea rax, [rbp + 3]
005EF8B9  49 3B C4                        cmp rax, r12
005EF8BC  0F 83 74 03 00 00               jae 0x1405efc36
005EF8C2  8B 5D 00                        mov ebx, dword ptr [rbp]
005EF8C5  48 83 C5 04                     add rbp, 4
005EF8C9  48 83 FB 0F                     cmp rbx, 0xf
005EF8CD  0F 82 63 03 00 00               jb 0x1405efc36
005EF8D3  48 8D 47 03                     lea rax, [rdi + 3]
005EF8D7  48 03 C3                        add rax, rbx
005EF8DA  48 3B C7                        cmp rax, rdi
005EF8DD  0F 82 53 03 00 00               jb 0x1405efc36
005EF8E3  48 83 EB 0F                     sub rbx, 0xf
005EF8E7  48 83 C3 0F                     add rbx, 0xf
005EF8EB  B9 1F 00 00 00                  mov ecx, 0x1f
005EF8F0  41 8B D6                        mov edx, r14d
005EF8F3  40 2A CE                        sub cl, sil
005EF8F6  B8 01 00 00 00                  mov eax, 1
005EF8FB  48 D3 EA                        shr rdx, cl
005EF8FE  4C 8B C3                        mov r8, rbx
005EF901  48 8B CE                        mov rcx, rsi
005EF904  48 D1 EA                        shr rdx, 1
005EF907  48 D3 E0                        shl rax, cl
005EF90A  48 83 C3 03                     add rbx, 3
005EF90E  48 03 D0                        add rdx, rax
005EF911  41 D3 E6                        shl r14d, cl
005EF914  4C 2B FE                        sub r15, rsi
005EF917  79 2D                           jns 0x1405ef946
005EF919  49 3B FD                        cmp rdi, r13
005EF91C  0F 83 A8 02 00 00               jae 0x1405efbca
005EF922  48 8D 45 01                     lea rax, [rbp + 1]
005EF926  49 3B C4                        cmp rax, r12
005EF929  0F 83 07 03 00 00               jae 0x1405efc36
005EF92F  0F B7 45 00                     movzx eax, word ptr [rbp]
005EF933  41 0F B6 CF                     movzx ecx, r15b
005EF937  F6 D9                           neg cl
005EF939  48 83 C5 02                     add rbp, 2
005EF93D  D3 E0                           shl eax, cl
005EF93F  44 03 F0                        add r14d, eax
005EF942  49 83 C7 10                     add r15, 0x10
005EF946  48 8B F7                        mov rsi, rdi
005EF949  48 2B F2                        sub rsi, rdx
005EF94C  48 3B B4 24 80 00 00 00         cmp rsi, qword ptr [rsp + 0x80]
005EF954  0F 82 DC 02 00 00               jb 0x1405efc36
005EF95A  48 83 FA 04                     cmp rdx, 4
005EF95E  73 49                           jae 0x1405ef9a9
005EF960  0F B6 06                        movzx eax, byte ptr [rsi]
005EF963  88 07                           mov byte ptr [rdi], al
005EF965  48 83 EA 01                     sub rdx, 1
005EF969  74 1D                           je 0x1405ef988
005EF96B  0F B6 46 01                     movzx eax, byte ptr [rsi + 1]
005EF96F  88 47 01                        mov byte ptr [rdi + 1], al
005EF972  48 83 FA 01                     cmp rdx, 1
005EF976  74 06                           je 0x1405ef97e
005EF978  0F B6 46 02                     movzx eax, byte ptr [rsi + 2]
005EF97C  EB 13                           jmp 0x1405ef991
005EF97E  48 83 EB 02                     sub rbx, 2
005EF982  48 83 C7 02                     add rdi, 2
005EF986  EB 13                           jmp 0x1405ef99b
005EF988  0F B6 06                        movzx eax, byte ptr [rsi]
005EF98B  88 47 01                        mov byte ptr [rdi + 1], al
005EF98E  0F B6 06                        movzx eax, byte ptr [rsi]
005EF991  88 47 02                        mov byte ptr [rdi + 2], al
005EF994  49 8B D8                        mov rbx, r8
005EF997  48 83 C7 03                     add rdi, 3
005EF99B  BA 00 01 00 00                  mov edx, 0x100
005EF9A0  48 85 DB                        test rbx, rbx
005EF9A3  0F 84 DD FD FF FF               je 0x1405ef786
005EF9A9  8B 06                           mov eax, dword ptr [rsi]
005EF9AB  89 07                           mov dword ptr [rdi], eax
005EF9AD  8B 46 04                        mov eax, dword ptr [rsi + 4]
005EF9B0  89 47 04                        mov dword ptr [rdi + 4], eax
005EF9B3  48 83 FB 09                     cmp rbx, 9
005EF9B7  73 0D                           jae 0x1405ef9c6
005EF9B9  48 03 FB                        add rdi, rbx
005EF9BC  BA 00 01 00 00                  mov edx, 0x100
005EF9C1  E9 C0 FD FF FF                  jmp 0x1405ef786
005EF9C6  48 83 C7 08                     add rdi, 8
005EF9CA  48 83 C6 08                     add rsi, 8
005EF9CE  48 83 EB 08                     sub rbx, 8
005EF9D2  49 3B F9                        cmp rdi, r9
005EF9D5  72 18                           jb 0x1405ef9ef
005EF9D7  49 3B FD                        cmp rdi, r13
005EF9DA  73 3D                           jae 0x1405efa19
005EF9DC  4C 8B C7                        mov r8, rdi
005EF9DF  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
005EF9E4  49 8B D5                        mov rdx, r13
005EF9E7  E8 04 AE E2 FF                  call 0x14041a7f0
005EF9EC  4C 8B C8                        mov r9, rax
005EF9EF  8B 06                           mov eax, dword ptr [rsi]
005EF9F1  89 07                           mov dword ptr [rdi], eax
005EF9F3  8B 46 04                        mov eax, dword ptr [rsi + 4]
005EF9F6  89 47 04                        mov dword ptr [rdi + 4], eax
005EF9F9  8B 46 08                        mov eax, dword ptr [rsi + 8]
005EF9FC  89 47 08                        mov dword ptr [rdi + 8], eax
005EF9FF  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
005EFA02  89 47 0C                        mov dword ptr [rdi + 0xc], eax
005EFA05  48 83 FB 11                     cmp rbx, 0x11
005EFA09  72 AE                           jb 0x1405ef9b9
005EFA0B  48 83 C7 10                     add rdi, 0x10
005EFA0F  48 83 C6 10                     add rsi, 0x10
005EFA13  48 83 EB 10                     sub rbx, 0x10
005EFA17  EB B9                           jmp 0x1405ef9d2
005EFA19  4C 8B 54 24 20                  mov r10, qword ptr [rsp + 0x20]
005EFA1E  48 8D 04 3B                     lea rax, [rbx + rdi]
005EFA22  49 3B C2                        cmp rax, r10
005EFA25  0F 87 0B 02 00 00               ja 0x1405efc36
005EFA2B  48 8B CB                        mov rcx, rbx
005EFA2E  BA 00 01 00 00                  mov edx, 0x100
005EFA33  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
005EFA35  48 8B B4 24 A8 00 00 00         mov rsi, qword ptr [rsp + 0xa8]
005EFA3D  48 8B F8                        mov rdi, rax
005EFA40  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
005EFA45  4C 8B 9C 24 80 00 00 00         mov r11, qword ptr [rsp + 0x80]
005EFA4D  48 3B F9                        cmp rdi, rcx
005EFA50  0F 83 CF 01 00 00               jae 0x1405efc25
005EFA56  41 8B C6                        mov eax, r14d
005EFA59  48 C1 E8 16                     shr rax, 0x16
005EFA5D  48 0F BF B4 46 20 04 00 00      movsx rsi, word ptr [rsi + rax*2 + 0x420]
005EFA66  66 85 F6                        test si, si
005EFA69  7F 32                           jg 0x1405efa9d
005EFA6B  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
005EFA73  41 C1 E6 0A                     shl r14d, 0xa
005EFA77  49 83 EF 0A                     sub r15, 0xa
005EFA7B  41 8B C6                        mov eax, r14d
005EFA7E  49 FF CF                        dec r15
005EFA81  C1 E8 1F                        shr eax, 0x1f
005EFA84  45 03 F6                        add r14d, r14d
005EFA87  66 2B C6                        sub ax, si
005EFA8A  48 0F BF C0                     movsx rax, ax
005EFA8E  0F B7 B4 41 20 0C 00 00         movzx esi, word ptr [rcx + rax*2 + 0xc20]
005EFA96  66 85 F6                        test si, si
005EFA99  7E E0                           jle 0x1405efa7b
005EFA9B  EB 0C                           jmp 0x1405efaa9
005EFA9D  48 8B CE                        mov rcx, rsi
005EFAA0  83 E1 0F                        and ecx, 0xf
005EFAA3  41 D3 E6                        shl r14d, cl
005EFAA6  4C 2B F9                        sub r15, rcx
005EFAA9  66 C1 EE 04                     shr si, 4
005EFAAD  66 2B F2                        sub si, dx
005EFAB0  4D 85 FF                        test r15, r15
005EFAB3  79 33                           jns 0x1405efae8
005EFAB5  EB 0D                           jmp 0x1405efac4
005EFAB7  4C 8B 54 24 20                  mov r10, qword ptr [rsp + 0x20]
005EFABC  4C 8B 9C 24 80 00 00 00         mov r11, qword ptr [rsp + 0x80]
005EFAC4  48 8D 45 01                     lea rax, [rbp + 1]
005EFAC8  49 3B C4                        cmp rax, r12
005EFACB  0F 83 65 01 00 00               jae 0x1405efc36
005EFAD1  0F B7 45 00                     movzx eax, word ptr [rbp]
005EFAD5  41 0F B6 CF                     movzx ecx, r15b
005EFAD9  F6 D9                           neg cl
005EFADB  48 83 C5 02                     add rbp, 2
005EFADF  D3 E0                           shl eax, cl
005EFAE1  44 03 F0                        add r14d, eax
005EFAE4  49 83 C7 10                     add r15, 0x10
005EFAE8  66 85 F6                        test si, si
005EFAEB  79 18                           jns 0x1405efb05
005EFAED  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
005EFAF2  40 88 37                        mov byte ptr [rdi], sil
005EFAF5  48 FF C7                        inc rdi
005EFAF8  48 8B B4 24 A8 00 00 00         mov rsi, qword ptr [rsp + 0xa8]
005EFB00  E9 48 FF FF FF                  jmp 0x1405efa4d
005EFB05  75 0E                           jne 0x1405efb15
005EFB07  49 3B EC                        cmp rbp, r12
005EFB0A  72 09                           jb 0x1405efb15
005EFB0C  49 3B FA                        cmp rdi, r10
005EFB0F  0F 84 5D 01 00 00               je 0x1405efc72
005EFB15  0F BF C6                        movsx eax, si
005EFB18  99                              cdq
005EFB19  83 E2 0F                        and edx, 0xf
005EFB1C  03 C2                           add eax, edx
005EFB1E  8B C8                           mov ecx, eax
005EFB20  83 E0 0F                        and eax, 0xf
005EFB23  2B C2                           sub eax, edx
005EFB25  C1 F9 04                        sar ecx, 4
005EFB28  48 63 D8                        movsxd rbx, eax
005EFB2B  48 63 F1                        movsxd rsi, ecx
005EFB2E  48 83 FB 0F                     cmp rbx, 0xf
005EFB32  75 69                           jne 0x1405efb9d
005EFB34  49 3B EC                        cmp rbp, r12
005EFB37  0F 83 F9 00 00 00               jae 0x1405efc36
005EFB3D  0F B6 5D 00                     movzx ebx, byte ptr [rbp]
005EFB41  48 FF C5                        inc rbp
005EFB44  48 81 FB FF 00 00 00            cmp rbx, 0xff
005EFB4B  75 4C                           jne 0x1405efb99
005EFB4D  48 8D 45 01                     lea rax, [rbp + 1]
005EFB51  49 3B C4                        cmp rax, r12
005EFB54  0F 83 DC 00 00 00               jae 0x1405efc36
005EFB5A  0F B7 5D 00                     movzx ebx, word ptr [rbp]
005EFB5E  48 83 C5 02                     add rbp, 2
005EFB62  48 85 DB                        test rbx, rbx
005EFB65  75 14                           jne 0x1405efb7b
005EFB67  48 8D 45 03                     lea rax, [rbp + 3]
005EFB6B  49 3B C4                        cmp rax, r12
005EFB6E  0F 83 C2 00 00 00               jae 0x1405efc36
005EFB74  8B 5D 00                        mov ebx, dword ptr [rbp]
005EFB77  48 83 C5 04                     add rbp, 4
005EFB7B  48 83 FB 0F                     cmp rbx, 0xf
005EFB7F  0F 82 B1 00 00 00               jb 0x1405efc36
005EFB85  48 8D 47 03                     lea rax, [rdi + 3]
005EFB89  48 03 C3                        add rax, rbx
005EFB8C  48 3B C7                        cmp rax, rdi
005EFB8F  0F 82 A1 00 00 00               jb 0x1405efc36
005EFB95  48 83 EB 0F                     sub rbx, 0xf
005EFB99  48 83 C3 0F                     add rbx, 0xf
005EFB9D  B9 1F 00 00 00                  mov ecx, 0x1f
005EFBA2  41 8B D6                        mov edx, r14d
005EFBA5  40 2A CE                        sub cl, sil
005EFBA8  B8 01 00 00 00                  mov eax, 1
005EFBAD  48 D3 EA                        shr rdx, cl
005EFBB0  48 83 C3 03                     add rbx, 3
005EFBB4  48 8B CE                        mov rcx, rsi
005EFBB7  48 D1 EA                        shr rdx, 1
005EFBBA  48 D3 E0                        shl rax, cl
005EFBBD  48 03 D0                        add rdx, rax
005EFBC0  41 D3 E6                        shl r14d, cl
005EFBC3  4C 2B FE                        sub r15, rsi
005EFBC6  79 2A                           jns 0x1405efbf2
005EFBC8  EB 08                           jmp 0x1405efbd2
005EFBCA  4C 8B 9C 24 80 00 00 00         mov r11, qword ptr [rsp + 0x80]
005EFBD2  48 8D 45 01                     lea rax, [rbp + 1]
005EFBD6  49 3B C4                        cmp rax, r12
005EFBD9  73 5B                           jae 0x1405efc36
005EFBDB  0F B7 45 00                     movzx eax, word ptr [rbp]
005EFBDF  41 0F B6 CF                     movzx ecx, r15b
005EFBE3  F6 D9                           neg cl
005EFBE5  48 83 C5 02                     add rbp, 2
005EFBE9  D3 E0                           shl eax, cl
005EFBEB  44 03 F0                        add r14d, eax
005EFBEE  49 83 C7 10                     add r15, 0x10
005EFBF2  48 8B F7                        mov rsi, rdi
005EFBF5  48 2B F2                        sub rsi, rdx
005EFBF8  49 3B F3                        cmp rsi, r11
005EFBFB  72 39                           jb 0x1405efc36
005EFBFD  48 8D 04 3B                     lea rax, [rbx + rdi]
005EFC01  49 3B C2                        cmp rax, r10
005EFC04  77 30                           ja 0x1405efc36
005EFC06  48 8B CB                        mov rcx, rbx
005EFC09  BA 00 01 00 00                  mov edx, 0x100
005EFC0E  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
005EFC10  48 8B B4 24 A8 00 00 00         mov rsi, qword ptr [rsp + 0xa8]
005EFC18  48 8B F8                        mov rdi, rax
005EFC1B  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
005EFC20  E9 28 FE FF FF                  jmp 0x1405efa4d
005EFC25  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
005EFC2C  E9 D6 FA FF FF                  jmp 0x1405ef707
005EFC31  49 3B FA                        cmp rdi, r10
005EFC34  74 3C                           je 0x1405efc72
005EFC36  B8 42 02 00 C0                  mov eax, 0xc0000242
005EFC3B  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
005EFC40  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
005EFC45  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
005EFC4D  48 8B BC 24 90 00 00 00         mov rdi, qword ptr [rsp + 0x90]
005EFC55  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
005EFC5D  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_005EF68C(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, unsigned int a24)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;
    unsigned int v_stack_pC0;

    v_stack_p88 = v_rsi;
    v_rsi = (result + 7) & (-8);
    v_stack_p90 = v_rdi;
    v_stack_p98 = v_r12;
    v_stack_p60 = v_r13;
    v_r12 = ((unsigned int)(a4)) + (a3);
    v_r10 = ((unsigned int)(a2)) + (a1);
    v_stack_p58 = v_r14;
    v_stack_p50 = v_r15;
    v_stack_pA8 = v_rsi;
    v_stack_p20 = v_r10;
    if (a22 == 0) goto loc_005EF6E8;
    if (a2 < ((unsigned int)(v_rbx))) {
        v_rbx = a2;
        v_stack_pC0 = a2;
    }
    v_stack_p30 = a22;
    v_stack_p38 = a23;
    v_stack_p40 = (unsigned int)(v_rbx);
loc_005EF707:
    result = (v_r12) - (v_rbp);
    if (result < 260) goto loc_005EFC31;
    result = XpressBuildHuffmanDecodingTable(v_rsi, v_rbp, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_005EFC36;
    v_rbp = (v_rbp) + (256);
    v_rbp = (v_rbp) + (4);
    v_r14 = (unsigned int)((*(unsigned __int16 *)(v_rbp)) << (16));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(*(unsigned __int16 *)(v_rbp + 2))));
    a1 = v_stack_p20;
    if ((a1 + 65536) <= v_stack_p20) { a1 = a1 + 65536; }
    v_stack_p28 = a1;
    if (a1 >= (a1 - 188)) goto loc_005EFA45;
    a4 = ((unsigned int)((unsigned int)(v_rbx))) + (a1);
    if ((a1 - 188) < a4) { a4 = a1 - 188; }
    goto loc_005EF78E;
loc_005EF786:
loc_005EF78E:
    result = ((unsigned int)((unsigned int)(v_r14))) >> (22);
    if (condition_is_greater) goto loc_005EF7CD;
    v_r14 = (unsigned int)((v_r14) << (10));
    v_r15 = (result + 16) - (10);
loc_005EF7AB:
    v_r15 = (v_r15) - 1;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> (31));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    result = (unsigned __int16)((result) - ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a21 + result * 2 + 1056)))));
    if (condition_is_less_or_equal) goto loc_005EF7AB;
    goto loc_005EF7D9;
loc_005EF7CD:
    a1 = (unsigned int)((*(unsigned __int16 *)(a21 + (__int16)((unsigned __int16)(result)) * 2 + 3104)) & (15));
    v_r14 = (unsigned int)((v_r14) << ((unsigned __int8)(a1)));
    v_r15 = (v_r15) - (a1);
loc_005EF7D9:
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(a21 + (__int16)((unsigned __int16)(result)) * 2 + 3104)) >> (4));
    v_rsi = (unsigned __int16)(((unsigned __int16)(v_rbx)) - (256));
    if (!sign_flag) goto loc_005EF832;
    if (a1 < a4) goto loc_005EF809;
    if (a1 >= (a1 - 188)) goto loc_005EFAB7;
    result = RtlpMakeXpressCallback(a6, a1 - 188, a1, a4);
loc_005EF809:
    if ((v_rbp + 1) >= v_r12) goto loc_005EFC36;
    a1 = (unsigned __int8)(-((unsigned __int8)(v_r15)));
    v_rbp = (v_rbp) + (2);
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rbp)) << ((unsigned __int8)(a1)));
    v_r14 = (unsigned int)((v_r14) + (a2));
    v_r15 = (v_r15) + (16);
loc_005EF832:
    if (!sign_flag) goto loc_005EF842;
    *(unsigned __int8 *)(a1) = (unsigned __int8)(v_rsi);
    v_rdi = (a1) + 1;
    goto loc_005EF786;
loc_005EF842:
    if ((unsigned __int16)(v_rsi) != 0) goto loc_005EF857;
    if (v_rbp < v_r12) goto loc_005EF857;
loc_005EF857:
    a1 = (unsigned int)(((unsigned __int16)(v_rbx)) - (256));
    a2 = (unsigned int)((256) & (15));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) + (a2));
    result = (unsigned int)((result) >> (4));
    a1 = (unsigned int)((a1) & (0x8000000FULL));
    if (!(condition_is_greater_or_equal)) {
        a1 = (unsigned int)((a1) - 1);
        a1 = (unsigned int)((a1) | (0xFFFFFFF0ULL));
        a1 = (unsigned int)((a1) + 1);
    }
    if (((int)((unsigned int)(a1))) != 15) goto loc_005EF8EB;
    if (v_rbp >= v_r12) goto loc_005EFC36;
    v_rbp = (v_rbp) + 1;
    if ((*(unsigned __int8 *)(v_rbp)) != 255) goto loc_005EF8E7;
    if ((v_rbp + 1) >= v_r12) goto loc_005EFC36;
    v_rbp = (v_rbp) + (2);
    if (*(unsigned __int16 *)(v_rbp) != 0) goto loc_005EF8C9;
    if ((v_rbp + 3) >= v_r12) goto loc_005EFC36;
    v_rbp = (v_rbp) + (4);
loc_005EF8C9:
    if (((unsigned int)(*(unsigned int *)(v_rbp))) < 15) goto loc_005EFC36;
    result = (v_rdi + 3) + ((unsigned int)(*(unsigned int *)(v_rbp)));
    if (result < v_rdi) goto loc_005EFC36;
    v_rbx = ((unsigned int)(*(unsigned int *)(v_rbp))) - (15);
loc_005EF8E7:
    v_rbx = (v_rbx) + (15);
loc_005EF8EB:
    a1 = (unsigned __int8)((31) - ((unsigned __int8)((int)((unsigned int)(result)))));
    a2 = ((unsigned int)((unsigned int)(v_r14))) >> ((unsigned __int8)(a1));
    a2 = (a2) >> (1);
    result = (1) << ((unsigned __int8)((int)((unsigned int)(result))));
    v_rbx = (v_rbx) + (3);
    a2 = (a2) + (result);
    v_r14 = (unsigned int)((v_r14) << ((unsigned __int8)((int)((unsigned int)(result)))));
    v_r15 = (v_r15) - ((int)((unsigned int)(result)));
    if (!sign_flag) goto loc_005EF946;
    if (v_rdi >= (a1 - 188)) goto loc_005EFBCA;
    if ((v_rbp + 1) >= v_r12) goto loc_005EFC36;
    a1 = (unsigned __int8)(-((unsigned __int8)(v_r15)));
    v_rbp = (v_rbp) + (2);
    result = (unsigned int)((*(unsigned __int16 *)(v_rbp)) << ((unsigned __int8)(a1)));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
    v_r15 = (v_r15) + (16);
loc_005EF946:
    v_rsi = (v_rdi) - (a2);
    if (v_rsi < a16) goto loc_005EFC36;
    if (a2 >= 4) goto loc_005EF9A9;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi));
    a2 = (a2) - (1);
    if (condition_is_equal) goto loc_005EF988;
    *(unsigned __int8 *)(v_rdi + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1));
    if (a2 == 1) goto loc_005EF97E;
    goto loc_005EF991;
loc_005EF97E:
    v_rbx = (v_rbx) - (2);
    v_rdi = (v_rdi) + (2);
    goto loc_005EF99B;
loc_005EF988:
    *(unsigned __int8 *)(v_rdi + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi));
loc_005EF991:
    *(unsigned __int8 *)(v_rdi + 2) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi));
    v_rdi = (v_rdi) + (3);
loc_005EF99B:
    if (v_rbx == 0) goto loc_005EF786;
loc_005EF9A9:
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)));
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4)));
    if (v_rbx >= 9) goto loc_005EF9C6;
loc_005EF9B9:
    v_rdi = (v_rdi) + (v_rbx);
    goto loc_005EF786;
loc_005EF9C6:
    v_rdi = (v_rdi) + (8);
    v_rsi = (v_rsi) + (8);
    v_rbx = (v_rbx) - (8);
loc_005EF9D2:
    if (v_rdi < result) goto loc_005EF9EF;
    if (v_rdi >= (a1 - 188)) goto loc_005EFA19;
    result = RtlpMakeXpressCallback(a6, a1 - 188, v_rdi, result);
loc_005EF9EF:
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)));
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4)));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 8)));
    *(unsigned int *)(v_rdi + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 12)));
    if (v_rbx < 17) goto loc_005EF9B9;
    v_rdi = (v_rdi) + (16);
    v_rsi = (v_rsi) + (16);
    v_rbx = (v_rbx) - (16);
    goto loc_005EF9D2;
loc_005EFA19:
    if ((v_rbx + v_rdi * 1) > v_stack_p20) goto loc_005EFC36;
loc_005EFA45:
loc_005EFA4D:
    if ((v_rbx + v_rdi * 1) >= a5) goto loc_005EFC25;
    result = ((unsigned int)((unsigned int)(v_r14))) >> (22);
    if (condition_is_greater) goto loc_005EFA9D;
    v_r14 = (unsigned int)((v_r14) << (10));
    v_r15 = (v_r15) - (10);
loc_005EFA7B:
    v_r15 = (v_r15) - 1;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> (31));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    result = (unsigned __int16)((result) - ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a21 + result * 2 + 1056)))));
    if (condition_is_less_or_equal) goto loc_005EFA7B;
    goto loc_005EFAA9;
loc_005EFA9D:
    a1 = (unsigned int)((*(unsigned __int16 *)(a21 + (__int16)((unsigned __int16)(result)) * 2 + 3104)) & (15));
    v_r14 = (unsigned int)((v_r14) << ((unsigned __int8)(a1)));
    v_r15 = (v_r15) - (a1);
loc_005EFAA9:
    v_rsi = (unsigned __int16)((*(unsigned __int16 *)(a21 + (__int16)((unsigned __int16)(result)) * 2 + 3104)) >> (4));
    v_rsi = (unsigned __int16)((v_rsi) - (256));
    if (!sign_flag) goto loc_005EFAE8;
    goto loc_005EFAC4;
loc_005EFAB7:
loc_005EFAC4:
    if ((v_rbp + 1) >= v_r12) goto loc_005EFC36;
    a1 = (unsigned __int8)(-((unsigned __int8)(v_r15)));
    v_rbp = (v_rbp) + (2);
    result = (unsigned int)((*(unsigned __int16 *)(v_rbp)) << ((unsigned __int8)(a1)));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
    v_r15 = (v_r15) + (16);
loc_005EFAE8:
    if (!sign_flag) goto loc_005EFB05;
    *(unsigned __int8 *)(v_rbx + v_rdi * 1) = (unsigned __int8)(v_rsi);
    v_rdi = (v_rbx + v_rdi * 1) + 1;
    goto loc_005EFA4D;
loc_005EFB05:
    if ((unsigned __int16)(v_rsi) != 0) goto loc_005EFB15;
    if (v_rbp < v_r12) goto loc_005EFB15;
loc_005EFB15:
    a2 = (unsigned int)((256) & (15));
    result = (unsigned int)(((__int16)((unsigned __int16)(a21))) + (a2));
    result = (unsigned int)((result) & (15));
    result = (unsigned int)((result) - (a2));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (4));
    if (((int)((unsigned int)(result))) != 15) goto loc_005EFB9D;
    if (v_rbp >= v_r12) goto loc_005EFC36;
    v_rbp = (v_rbp) + 1;
    if ((*(unsigned __int8 *)(v_rbp)) != 255) goto loc_005EFB99;
    if ((v_rbp + 1) >= v_r12) goto loc_005EFC36;
    v_rbp = (v_rbp) + (2);
    if (*(unsigned __int16 *)(v_rbp) != 0) goto loc_005EFB7B;
    if ((v_rbp + 3) >= v_r12) goto loc_005EFC36;
    v_rbp = (v_rbp) + (4);
loc_005EFB7B:
    if (((unsigned int)(*(unsigned int *)(v_rbp))) < 15) goto loc_005EFC36;
    result = (v_rdi + 3) + ((unsigned int)(*(unsigned int *)(v_rbp)));
    if (result < v_rdi) goto loc_005EFC36;
    v_rbx = ((unsigned int)(*(unsigned int *)(v_rbp))) - (15);
loc_005EFB99:
    v_rbx = (v_rbx) + (15);
loc_005EFB9D:
    a1 = (unsigned __int8)((31) - ((unsigned __int8)((int)((unsigned int)(a1)))));
    a2 = ((unsigned int)((unsigned int)(v_r14))) >> ((unsigned __int8)(a1));
    v_rbx = (v_rbx) + (3);
    a2 = (a2) >> (1);
    result = (1) << ((unsigned __int8)((int)((unsigned int)(a1))));
    a2 = (a2) + (result);
    v_r14 = (unsigned int)((v_r14) << ((unsigned __int8)((int)((unsigned int)(a1)))));
    v_r15 = (v_r15) - ((int)((unsigned int)(a1)));
    if (!sign_flag) goto loc_005EFBF2;
    goto loc_005EFBD2;
loc_005EFBCA:
loc_005EFBD2:
    if ((v_rbp + 1) >= v_r12) goto loc_005EFC36;
    a1 = (unsigned __int8)(-((unsigned __int8)(v_r15)));
    v_rbp = (v_rbp) + (2);
    result = (unsigned int)((*(unsigned __int16 *)(v_rbp)) << ((unsigned __int8)(a1)));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
    v_r15 = (v_r15) + (16);
loc_005EFBF2:
    v_rsi = (v_rdi) - (a2);
    if (v_rsi < a16) goto loc_005EFC36;
    if ((v_rbx + v_rdi * 1) > v_stack_p20) goto loc_005EFC36;
    goto loc_005EFA4D;
loc_005EFC25:
    goto loc_005EF707;
loc_005EFC31:
loc_005EFC36:
    return (unsigned int)(0xC0000242ULL);
}
```

## 5. (Beta) C Style

```c
int64_t sub_005EF68C(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, int64_t Arg16, int64_t Arg17, int64_t Arg18, int64_t Arg19, uint64_t Arg20, void *Arg21, int64_t Arg22, int64_t Arg23, uint32_t Arg24)
{
    uint8_t *arg21 = (uint8_t *)Arg21;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;
    uint32_t v_stack_pC0;

    v_stack_p88 = local_rsi;
    local_rsi = (result + 7) & (-8);
    v_stack_p90 = local_rdi;
    v_stack_p98 = local_r12;
    v_stack_p60 = local_r13;
    local_r12 = ((uint32_t)(Arg4)) + (Arg3);
    local_r10 = ((uint32_t)(Arg2)) + (Arg1);
    v_stack_p58 = local_r14;
    v_stack_p50 = local_r15;
    v_stack_pA8 = local_rsi;
    v_stack_p20 = local_r10;
    if (Arg22 == 0) goto loc_005EF6E8;
    if (Arg2 < ((uint32_t)(local_rbx))) {
        local_rbx = Arg2;
        v_stack_pC0 = Arg2;
    }
    v_stack_p30 = Arg22;
    v_stack_p38 = Arg23;
    v_stack_p40 = (uint32_t)(local_rbx);
loc_005EF707:
    result = (local_r12) - (local_rbp);
    if (result < 260) goto loc_005EFC31;
    result = XpressBuildHuffmanDecodingTable(local_rsi, local_rbp, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_005EFC36;
    local_rbp = (local_rbp) + (256);
    local_rbp = (local_rbp) + (4);
    local_r14 = (uint32_t)((*(uint16_t *)(local_rbp)) << (16));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(*(uint16_t *)(local_rbp + 0x2))));
    Arg1 = v_stack_p20;
    if ((Arg1 + 65536) <= v_stack_p20) { Arg1 = Arg1 + 65536; }
    v_stack_p28 = Arg1;
    if (Arg1 >= (Arg1 - 188)) goto loc_005EFA45;
    Arg4 = ((uint32_t)((uint32_t)(local_rbx))) + (Arg1);
    if ((Arg1 - 188) < Arg4) { Arg4 = Arg1 - 188; }
    goto loc_005EF78E;
loc_005EF786:
loc_005EF78E:
    result = ((uint32_t)((uint32_t)(local_r14))) >> (22);
    if (condition_is_greater) goto loc_005EF7CD;
    local_r14 = (uint32_t)((local_r14) << (10));
    local_r15 = (result + 16) - (10);
loc_005EF7AB:
    local_r15 = (local_r15) - 1;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> (31));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    result = (uint16_t)((result) - ((uint16_t)((int16_t)(*(uint16_t *)(arg21 + result * 2 + 0x420)))));
    if (condition_is_less_or_equal) goto loc_005EF7AB;
    goto loc_005EF7D9;
loc_005EF7CD:
    Arg1 = (uint32_t)((*(uint16_t *)(arg21 + (int16_t)((uint16_t)(result)) * 2 + 0xC20)) & (15));
    local_r14 = (uint32_t)((local_r14) << ((uint8_t)(Arg1)));
    local_r15 = (local_r15) - (Arg1);
loc_005EF7D9:
    local_rbx = (uint16_t)((*(uint16_t *)(arg21 + (int16_t)((uint16_t)(result)) * 2 + 0xC20)) >> (4));
    local_rsi = (uint16_t)(((uint16_t)(local_rbx)) - (256));
    if (!sign_flag) goto loc_005EF832;
    if (Arg1 < Arg4) goto loc_005EF809;
    if (Arg1 >= (Arg1 - 188)) goto loc_005EFAB7;
    result = RtlpMakeXpressCallback(Arg6, Arg1 - 188, Arg1, Arg4);
loc_005EF809:
    if ((local_rbp + 1) >= local_r12) goto loc_005EFC36;
    Arg1 = (uint8_t)(-((uint8_t)(local_r15)));
    local_rbp = (local_rbp) + (2);
    Arg2 = (uint32_t)((*(uint16_t *)(local_rbp)) << ((uint8_t)(Arg1)));
    local_r14 = (uint32_t)((local_r14) + (Arg2));
    local_r15 = (local_r15) + (16);
loc_005EF832:
    if (!sign_flag) goto loc_005EF842;
    *(uint8_t *)(Arg1) = (uint8_t)(local_rsi);
    local_rdi = (Arg1) + 1;
    goto loc_005EF786;
loc_005EF842:
    if ((uint16_t)(local_rsi) != 0) goto loc_005EF857;
    if (local_rbp < local_r12) goto loc_005EF857;
loc_005EF857:
    Arg1 = (uint32_t)(((uint16_t)(local_rbx)) - (256));
    Arg2 = (uint32_t)((256) & (15));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) + (Arg2));
    result = (uint32_t)((result) >> (4));
    Arg1 = (uint32_t)((Arg1) & (0x8000000FULL));
    if (!(condition_is_greater_or_equal)) {
        Arg1 = (uint32_t)((Arg1) - 1);
        Arg1 = (uint32_t)((Arg1) | (0xFFFFFFF0ULL));
        Arg1 = (uint32_t)((Arg1) + 1);
    }
    if (((int32_t)((uint32_t)(Arg1))) != 15) goto loc_005EF8EB;
    if (local_rbp >= local_r12) goto loc_005EFC36;
    local_rbp = (local_rbp) + 1;
    if ((*(uint8_t *)(local_rbp)) != 255) goto loc_005EF8E7;
    if ((local_rbp + 1) >= local_r12) goto loc_005EFC36;
    local_rbp = (local_rbp) + (2);
    if (*(uint16_t *)(local_rbp) != 0) goto loc_005EF8C9;
    if ((local_rbp + 3) >= local_r12) goto loc_005EFC36;
    local_rbp = (local_rbp) + (4);
loc_005EF8C9:
    if (((uint32_t)(*(uint32_t *)(local_rbp))) < 15) goto loc_005EFC36;
    result = (local_rdi + 3) + ((uint32_t)(*(uint32_t *)(local_rbp)));
    if (result < local_rdi) goto loc_005EFC36;
    local_rbx = ((uint32_t)(*(uint32_t *)(local_rbp))) - (15);
loc_005EF8E7:
    local_rbx = (local_rbx) + (15);
loc_005EF8EB:
    Arg1 = (uint8_t)((31) - ((uint8_t)((int32_t)((uint32_t)(result)))));
    Arg2 = ((uint32_t)((uint32_t)(local_r14))) >> ((uint8_t)(Arg1));
    Arg2 = (Arg2) >> (1);
    result = (1) << ((uint8_t)((int32_t)((uint32_t)(result))));
    local_rbx = (local_rbx) + (3);
    Arg2 = (Arg2) + (result);
    local_r14 = (uint32_t)((local_r14) << ((uint8_t)((int32_t)((uint32_t)(result)))));
    local_r15 = (local_r15) - ((int32_t)((uint32_t)(result)));
    if (!sign_flag) goto loc_005EF946;
    if (local_rdi >= (Arg1 - 188)) goto loc_005EFBCA;
    if ((local_rbp + 1) >= local_r12) goto loc_005EFC36;
    Arg1 = (uint8_t)(-((uint8_t)(local_r15)));
    local_rbp = (local_rbp) + (2);
    result = (uint32_t)((*(uint16_t *)(local_rbp)) << ((uint8_t)(Arg1)));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
    local_r15 = (local_r15) + (16);
loc_005EF946:
    local_rsi = (local_rdi) - (Arg2);
    if (local_rsi < Arg16) goto loc_005EFC36;
    if (Arg2 >= 4) goto loc_005EF9A9;
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rsi));
    Arg2 = (Arg2) - (1);
    if (condition_is_equal) goto loc_005EF988;
    *(uint8_t *)(local_rdi + 0x1) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1));
    if (Arg2 == 1) goto loc_005EF97E;
    goto loc_005EF991;
loc_005EF97E:
    local_rbx = (local_rbx) - (2);
    local_rdi = (local_rdi) + (2);
    goto loc_005EF99B;
loc_005EF988:
    *(uint8_t *)(local_rdi + 0x1) = (uint8_t)(*(uint8_t *)(local_rsi));
loc_005EF991:
    *(uint8_t *)(local_rdi + 0x2) = (uint8_t)(*(uint8_t *)(local_rsi));
    local_rdi = (local_rdi) + (3);
loc_005EF99B:
    if (local_rbx == 0) goto loc_005EF786;
loc_005EF9A9:
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)));
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)));
    if (local_rbx >= 9) goto loc_005EF9C6;
loc_005EF9B9:
    local_rdi = (local_rdi) + (local_rbx);
    goto loc_005EF786;
loc_005EF9C6:
    local_rdi = (local_rdi) + (8);
    local_rsi = (local_rsi) + (8);
    local_rbx = (local_rbx) - (8);
loc_005EF9D2:
    if (local_rdi < result) goto loc_005EF9EF;
    if (local_rdi >= (Arg1 - 188)) goto loc_005EFA19;
    result = RtlpMakeXpressCallback(Arg6, Arg1 - 188, local_rdi, result);
loc_005EF9EF:
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)));
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x8)));
    *(uint32_t *)(local_rdi + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0xC)));
    if (local_rbx < 17) goto loc_005EF9B9;
    local_rdi = (local_rdi) + (16);
    local_rsi = (local_rsi) + (16);
    local_rbx = (local_rbx) - (16);
    goto loc_005EF9D2;
loc_005EFA19:
    if ((local_rbx + local_rdi * 1) > v_stack_p20) goto loc_005EFC36;
loc_005EFA45:
loc_005EFA4D:
    if ((local_rbx + local_rdi * 1) >= Arg5) goto loc_005EFC25;
    result = ((uint32_t)((uint32_t)(local_r14))) >> (22);
    if (condition_is_greater) goto loc_005EFA9D;
    local_r14 = (uint32_t)((local_r14) << (10));
    local_r15 = (local_r15) - (10);
loc_005EFA7B:
    local_r15 = (local_r15) - 1;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> (31));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    result = (uint16_t)((result) - ((uint16_t)((int16_t)(*(uint16_t *)(arg21 + result * 2 + 0x420)))));
    if (condition_is_less_or_equal) goto loc_005EFA7B;
    goto loc_005EFAA9;
loc_005EFA9D:
    Arg1 = (uint32_t)((*(uint16_t *)(arg21 + (int16_t)((uint16_t)(result)) * 2 + 0xC20)) & (15));
    local_r14 = (uint32_t)((local_r14) << ((uint8_t)(Arg1)));
    local_r15 = (local_r15) - (Arg1);
loc_005EFAA9:
    local_rsi = (uint16_t)((*(uint16_t *)(arg21 + (int16_t)((uint16_t)(result)) * 2 + 0xC20)) >> (4));
    local_rsi = (uint16_t)((local_rsi) - (256));
    if (!sign_flag) goto loc_005EFAE8;
    goto loc_005EFAC4;
loc_005EFAB7:
loc_005EFAC4:
    if ((local_rbp + 1) >= local_r12) goto loc_005EFC36;
    Arg1 = (uint8_t)(-((uint8_t)(local_r15)));
    local_rbp = (local_rbp) + (2);
    result = (uint32_t)((*(uint16_t *)(local_rbp)) << ((uint8_t)(Arg1)));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
    local_r15 = (local_r15) + (16);
loc_005EFAE8:
    if (!sign_flag) goto loc_005EFB05;
    *(uint8_t *)(local_rbx + local_rdi * 1) = (uint8_t)(local_rsi);
    local_rdi = (local_rbx + local_rdi * 1) + 1;
    goto loc_005EFA4D;
loc_005EFB05:
    if ((uint16_t)(local_rsi) != 0) goto loc_005EFB15;
    if (local_rbp < local_r12) goto loc_005EFB15;
loc_005EFB15:
    Arg2 = (uint32_t)((256) & (15));
    result = (uint32_t)(((int16_t)((uint16_t)(Arg21))) + (Arg2));
    result = (uint32_t)((result) & (15));
    result = (uint32_t)((result) - (Arg2));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (4));
    if (((int32_t)((uint32_t)(result))) != 15) goto loc_005EFB9D;
    if (local_rbp >= local_r12) goto loc_005EFC36;
    local_rbp = (local_rbp) + 1;
    if ((*(uint8_t *)(local_rbp)) != 255) goto loc_005EFB99;
    if ((local_rbp + 1) >= local_r12) goto loc_005EFC36;
    local_rbp = (local_rbp) + (2);
    if (*(uint16_t *)(local_rbp) != 0) goto loc_005EFB7B;
    if ((local_rbp + 3) >= local_r12) goto loc_005EFC36;
    local_rbp = (local_rbp) + (4);
loc_005EFB7B:
    if (((uint32_t)(*(uint32_t *)(local_rbp))) < 15) goto loc_005EFC36;
    result = (local_rdi + 3) + ((uint32_t)(*(uint32_t *)(local_rbp)));
    if (result < local_rdi) goto loc_005EFC36;
    local_rbx = ((uint32_t)(*(uint32_t *)(local_rbp))) - (15);
loc_005EFB99:
    local_rbx = (local_rbx) + (15);
loc_005EFB9D:
    Arg1 = (uint8_t)((31) - ((uint8_t)((int32_t)((uint32_t)(Arg1)))));
    Arg2 = ((uint32_t)((uint32_t)(local_r14))) >> ((uint8_t)(Arg1));
    local_rbx = (local_rbx) + (3);
    Arg2 = (Arg2) >> (1);
    result = (1) << ((uint8_t)((int32_t)((uint32_t)(Arg1))));
    Arg2 = (Arg2) + (result);
    local_r14 = (uint32_t)((local_r14) << ((uint8_t)((int32_t)((uint32_t)(Arg1)))));
    local_r15 = (local_r15) - ((int32_t)((uint32_t)(Arg1)));
    if (!sign_flag) goto loc_005EFBF2;
    goto loc_005EFBD2;
loc_005EFBCA:
loc_005EFBD2:
    if ((local_rbp + 1) >= local_r12) goto loc_005EFC36;
    Arg1 = (uint8_t)(-((uint8_t)(local_r15)));
    local_rbp = (local_rbp) + (2);
    result = (uint32_t)((*(uint16_t *)(local_rbp)) << ((uint8_t)(Arg1)));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
    local_r15 = (local_r15) + (16);
loc_005EFBF2:
    local_rsi = (local_rdi) - (Arg2);
    if (local_rsi < Arg16) goto loc_005EFC36;
    if ((local_rbx + local_rdi * 1) > v_stack_p20) goto loc_005EFC36;
    goto loc_005EFA4D;
loc_005EFC25:
    goto loc_005EF707;
loc_005EFC31:
loc_005EFC36:
    return (uint32_t)(0xC0000242ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg21` | `+ 0xC20 + rax*2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005EF68C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
