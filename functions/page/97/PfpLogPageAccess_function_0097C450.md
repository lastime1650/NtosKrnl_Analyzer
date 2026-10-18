# PfpLogPageAccess

- RVA: `0x0097C450`–`0x0097CB0E` (길이 `1,726` bytes)
- VA: `0x000000014097C450`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00096EC4`
- 디코드: `426`개 명령, `1,726/1,726` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0097CA06` → [PfTReplaceCurrentBuffer](PfTReplaceCurrentBuffer_function_0097CB14.md) (function, `0x0097CB14`)
- `0x0097CA32` → [PfTReplaceCurrentBuffer](PfTReplaceCurrentBuffer_function_0097CB14.md) (function, `0x0097CB14`)
- `0x0097CAA9` → [PfTReplaceCurrentBuffer](PfTReplaceCurrentBuffer_function_0097CB14.md) (function, `0x0097CB14`)

### Direct callers
- [PfpCopyEvent](PfpCopyEvent_function_0097BE5C.md) at `0x0097BF8C`
- [sub_0097C0F8](Unknown_function_0097C0F8.md) at `0x0097C276`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0097C450  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0097C455  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0097C45A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0097C45F  57                              push rdi
0097C460  41 54                           push r12
0097C462  41 55                           push r13
0097C464  41 56                           push r14
0097C466  41 57                           push r15
0097C468  48 83 EC 50                     sub rsp, 0x50
0097C46C  45 8B 10                        mov r10d, dword ptr [r8]
0097C46F  33 FF                           xor edi, edi
0097C471  BD FF FF 00 00                  mov ebp, 0xffff
0097C476  4D 8B F9                        mov r15, r9
0097C479  49 8B F0                        mov rsi, r8
0097C47C  4C 8B F2                        mov r14, rdx
0097C47F  4C 8B E9                        mov r13, rcx
0097C482  44 0F B7 E5                     movzx r12d, bp
0097C486  41 F7 C2 FF 01 00 00            test r10d, 0x1ff
0097C48D  0F 85 1C 02 00 00               jne 0x14097c6af
0097C493  4D 85 F6                        test r14, r14
0097C496  0F 84 F9 01 00 00               je 0x14097c695
0097C49C  39 BC 24 A8 00 00 00            cmp dword ptr [rsp + 0xa8], edi
0097C4A3  0F 85 DD 02 00 00               jne 0x14097c786
0097C4A9  49 8B 9E F8 01 00 00            mov rbx, qword ptr [r14 + 0x1f8]
0097C4B0  48 B8 FF FF FF FF FF FF FF 1F   movabs rax, 0x1fffffffffffffff
0097C4BA  49 33 9E D0 01 00 00            xor rbx, qword ptr [r14 + 0x1d0]
0097C4C1  48 23 D8                        and rbx, rax
0097C4C4  48 83 E3 FD                     and rbx, 0xfffffffffffffffd
0097C4C8  66 89 7C 24 24                  mov word ptr [rsp + 0x24], di
0097C4CD  48 83 CB 01                     or rbx, 1
0097C4D1  48 8B C3                        mov rax, rbx
0097C4D4  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
0097C4D9  83 E0 03                        and eax, 3
0097C4DC  4C 8D 1C 85 10 00 00 00         lea r11, [rax*4 + 0x10]
0097C4E4  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
0097C4E9  4D 8D 95 80 00 00 00            lea r10, [r13 + 0x80]
0097C4F0  4D 8B 42 18                     mov r8, qword ptr [r10 + 0x18]
0097C4F4  43 8B 0C 03                     mov ecx, dword ptr [r11 + r8]
0097C4F8  4D 8D 48 2F                     lea r9, [r8 + 0x2f]
0097C4FC  49 83 E1 F8                     and r9, 0xfffffffffffffff8
0097C500  48 8D 04 89                     lea rax, [rcx + rcx*4]
0097C504  49 39 1C C1                     cmp qword ptr [r9 + rax*8], rbx
0097C508  0F 85 82 02 00 00               jne 0x14097c790
0097C50E  49 8D 50 20                     lea rdx, [r8 + 0x20]
0097C512  66 3B CD                        cmp cx, bp
0097C515  0F 84 47 04 00 00               je 0x14097c962
0097C51B  45 32 D2                        xor r10b, r10b
0097C51E  4D 85 C0                        test r8, r8
0097C521  0F 84 4C 01 00 00               je 0x14097c673
0097C527  0F B7 C1                        movzx eax, cx
0097C52A  0F B7 E9                        movzx ebp, cx
0097C52D  66 41 03 68 24                  add bp, word ptr [r8 + 0x24]
0097C532  48 C7 84 24 90 00 00 00 02 00 00 00  mov qword ptr [rsp + 0x90], 2
0097C53E  48 8D 0C 80                     lea rcx, [rax + rax*4]
0097C542  49 8D 40 2F                     lea rax, [r8 + 0x2f]
0097C546  48 83 E0 F8                     and rax, 0xfffffffffffffff8
0097C54A  48 8D 14 C8                     lea rdx, [rax + rcx*8]
0097C54E  45 84 D2                        test r10b, r10b
0097C551  0F 85 F5 04 00 00               jne 0x14097ca4c
0097C557  F6 42 08 04                     test byte ptr [rdx + 8], 4
0097C55B  0F 85 EB 04 00 00               jne 0x14097ca4c
0097C561  41 0F B6 07                     movzx eax, byte ptr [r15]
0097C565  8B DF                           mov ebx, edi
0097C567  24 03                           and al, 3
0097C569  3C 02                           cmp al, 2
0097C56B  0F 94 C3                        sete bl
0097C56E  FF C3                           inc ebx
0097C570  49 8B 45 70                     mov rax, qword ptr [r13 + 0x70]
0097C574  8B 50 10                        mov edx, dword ptr [rax + 0x10]
0097C577  8D 0C 13                        lea ecx, [rbx + rdx]
0097C57A  3B 48 14                        cmp ecx, dword ptr [rax + 0x14]
0097C57D  0F 87 7C 04 00 00               ja 0x14097c9ff
0097C583  89 48 10                        mov dword ptr [rax + 0x10], ecx
0097C586  48 85 C0                        test rax, rax
0097C589  0F 84 E4 00 00 00               je 0x14097c673
0097C58F  48 83 C0 1F                     add rax, 0x1f
0097C593  8B FA                           mov edi, edx
0097C595  48 83 E0 F8                     and rax, 0xfffffffffffffff8
0097C599  48 C1 E7 04                     shl rdi, 4
0097C59D  48 03 F8                        add rdi, rax
0097C5A0  41 0F B6 07                     movzx eax, byte ptr [r15]
0097C5A4  24 03                           and al, 3
0097C5A6  3C 02                           cmp al, 2
0097C5A8  75 1B                           jne 0x14097c5c5
0097C5AA  41 0F 10 07                     movups xmm0, xmmword ptr [r15]
0097C5AE  0F 11 07                        movups xmmword ptr [rdi], xmm0
0097C5B1  48 8B 07                        mov rax, qword ptr [rdi]
0097C5B4  48 25 0B F0 FF FF               and rax, 0xfffffffffffff00b
0097C5BA  48 83 C8 08                     or rax, 8
0097C5BE  48 89 07                        mov qword ptr [rdi], rax
0097C5C1  48 83 C7 10                     add rdi, 0x10
0097C5C5  F7 06 FF 01 00 00               test dword ptr [rsi], 0x1ff
0097C5CB  48 8B 17                        mov rdx, qword ptr [rdi]
0097C5CE  75 57                           jne 0x14097c627
0097C5D0  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
0097C5D8  48 83 E2 FD                     and rdx, 0xfffffffffffffffd
0097C5DC  48 83 CA 01                     or rdx, 1
0097C5E0  48 89 17                        mov qword ptr [rdi], rdx
0097C5E3  8B 06                           mov eax, dword ptr [rsi]
0097C5E5  48 C1 E8 07                     shr rax, 7
0097C5E9  48 33 D0                        xor rdx, rax
0097C5EC  48 83 E2 FB                     and rdx, 0xfffffffffffffffb
0097C5F0  48 33 D0                        xor rdx, rax
0097C5F3  4A 8D 04 CD 00 00 00 00         lea rax, [r9*8]
0097C5FB  48 83 E2 E7                     and rdx, 0xffffffffffffffe7
0097C5FF  48 0B D0                        or rdx, rax
0097C602  48 89 17                        mov qword ptr [rdi], rdx
0097C605  48 8B C2                        mov rax, rdx
0097C608  48 33 06                        xor rax, qword ptr [rsi]
0097C60B  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0097C611  48 33 C2                        xor rax, rdx
0097C614  48 89 07                        mov qword ptr [rdi], rax
0097C617  49 83 F9 02                     cmp r9, 2
0097C61B  0F 85 59 01 00 00               jne 0x14097c77a
0097C621  66 89 6F 0A                     mov word ptr [rdi + 0xa], bp
0097C625  EB 4C                           jmp 0x14097c673
0097C627  48 83 E2 FC                     and rdx, 0xfffffffffffffffc
0097C62B  48 89 17                        mov qword ptr [rdi], rdx
0097C62E  8B 06                           mov eax, dword ptr [rsi]
0097C630  48 C1 E8 07                     shr rax, 7
0097C634  48 33 D0                        xor rdx, rax
0097C637  48 83 E2 FB                     and rdx, 0xfffffffffffffffb
0097C63B  48 33 D0                        xor rdx, rax
0097C63E  48 89 17                        mov qword ptr [rdi], rdx
0097C641  8B 06                           mov eax, dword ptr [rsi]
0097C643  48 C1 E8 07                     shr rax, 7
0097C647  48 33 D0                        xor rdx, rax
0097C64A  48 83 E2 F7                     and rdx, 0xfffffffffffffff7
0097C64E  48 33 D0                        xor rdx, rax
0097C651  48 89 17                        mov qword ptr [rdi], rdx
0097C654  83 E2 0F                        and edx, 0xf
0097C657  48 8B 0E                        mov rcx, qword ptr [rsi]
0097C65A  48 C1 E9 0C                     shr rcx, 0xc
0097C65E  8B C9                           mov ecx, ecx
0097C660  48 C1 E1 04                     shl rcx, 4
0097C664  48 0B CA                        or rcx, rdx
0097C667  66 89 6F 0A                     mov word ptr [rdi + 0xa], bp
0097C66B  48 89 0F                        mov qword ptr [rdi], rcx
0097C66E  66 44 89 67 08                  mov word ptr [rdi + 8], r12w
0097C673  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0097C678  48 8B C7                        mov rax, rdi
0097C67B  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0097C67F  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
0097C683  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
0097C687  49 8B E3                        mov rsp, r11
0097C68A  41 5F                           pop r15
0097C68C  41 5E                           pop r14
0097C68E  41 5D                           pop r13
0097C690  41 5C                           pop r12
0097C692  5F                              pop rdi
0097C693  C3                              ret
0097C694  CC                              int3
0097C695  39 BC 24 A8 00 00 00            cmp dword ptr [rsp + 0xa8], edi
0097C69C  0F 85 E4 00 00 00               jne 0x14097c786
0097C6A2  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
0097C6AA  E9 B2 FE FF FF                  jmp 0x14097c561
0097C6AF  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
0097C6B7  41 81 E2 FF 01 00 00            and r10d, 0x1ff
0097C6BE  49 C1 E2 03                     shl r10, 3
0097C6C2  49 2B C2                        sub rax, r10
0097C6C5  66 89 BC 24 90 00 00 00         mov word ptr [rsp + 0x90], di
0097C6CD  48 8B 18                        mov rbx, qword ptr [rax]
0097C6D0  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
0097C6D5  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
0097C6D9  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
0097C6DE  4D 8B 85 98 00 00 00            mov r8, qword ptr [r13 + 0x98]
0097C6E5  41 8B 48 10                     mov ecx, dword ptr [r8 + 0x10]
0097C6E9  4D 8D 48 2F                     lea r9, [r8 + 0x2f]
0097C6ED  49 83 E1 F8                     and r9, 0xfffffffffffffff8
0097C6F1  48 8D 04 89                     lea rax, [rcx + rcx*4]
0097C6F5  49 39 1C C1                     cmp qword ptr [r9 + rax*8], rbx
0097C6F9  0F 85 21 01 00 00               jne 0x14097c820
0097C6FF  49 8D 50 20                     lea rdx, [r8 + 0x20]
0097C703  66 3B CD                        cmp cx, bp
0097C706  0F 84 A6 02 00 00               je 0x14097c9b2
0097C70C  45 32 D2                        xor r10b, r10b
0097C70F  4D 85 C0                        test r8, r8
0097C712  0F 84 5B FF FF FF               je 0x14097c673
0097C718  44 0F B7 E1                     movzx r12d, cx
0097C71C  66 45 03 60 24                  add r12w, word ptr [r8 + 0x24]
0097C721  45 84 D2                        test r10b, r10b
0097C724  0F 84 69 FD FF FF               je 0x14097c493
0097C72A  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0097C72F  49 8D 50 2F                     lea rdx, [r8 + 0x2f]
0097C733  0F B7 C1                        movzx eax, cx
0097C736  48 83 E2 F8                     and rdx, 0xfffffffffffffff8
0097C73A  48 8D 0C 80                     lea rcx, [rax + rax*4]
0097C73E  49 8B C1                        mov rax, r9
0097C741  4C 8D 04 CA                     lea r8, [rdx + rcx*8]
0097C745  48 C1 E0 04                     shl rax, 4
0097C749  41 8B 48 08                     mov ecx, dword ptr [r8 + 8]
0097C74D  83 E1 08                        and ecx, 8
0097C750  49 C1 E9 3C                     shr r9, 0x3c
0097C754  48 0B C8                        or rcx, rax
0097C757  41 0F B7 40 10                  movzx eax, word ptr [r8 + 0x10]
0097C75C  48 83 C9 04                     or rcx, 4
0097C760  49 89 48 08                     mov qword ptr [r8 + 8], rcx
0097C764  B9 F0 FF 00 00                  mov ecx, 0xfff0
0097C769  66 23 C1                        and ax, cx
0097C76C  66 44 0B C8                     or r9w, ax
0097C770  66 45 89 48 10                  mov word ptr [r8 + 0x10], r9w
0097C775  E9 19 FD FF FF                  jmp 0x14097c493
0097C77A  C7 47 08 FF FF FF FF            mov dword ptr [rdi + 8], 0xffffffff
0097C781  E9 ED FE FF FF                  jmp 0x14097c673
0097C786  49 8B DE                        mov rbx, r14
0097C789  E9 36 FD FF FF                  jmp 0x14097c4c4
0097C78E  66 90                           nop
0097C790  0F B6 C3                        movzx eax, bl
0097C793  48 05 CB 5D B1 00               add rax, 0xb15dcb
0097C799  48 6B C8 25                     imul rcx, rax, 0x25
0097C79D  0F B6 44 24 39                  movzx eax, byte ptr [rsp + 0x39]
0097C7A2  48 03 C8                        add rcx, rax
0097C7A5  0F B6 44 24 3A                  movzx eax, byte ptr [rsp + 0x3a]
0097C7AA  48 6B D1 25                     imul rdx, rcx, 0x25
0097C7AE  48 03 D0                        add rdx, rax
0097C7B1  0F B6 44 24 3B                  movzx eax, byte ptr [rsp + 0x3b]
0097C7B6  48 6B CA 25                     imul rcx, rdx, 0x25
0097C7BA  48 03 C8                        add rcx, rax
0097C7BD  0F B6 44 24 3C                  movzx eax, byte ptr [rsp + 0x3c]
0097C7C2  48 6B D1 25                     imul rdx, rcx, 0x25
0097C7C6  48 03 D0                        add rdx, rax
0097C7C9  0F B6 44 24 3D                  movzx eax, byte ptr [rsp + 0x3d]
0097C7CE  48 6B CA 25                     imul rcx, rdx, 0x25
0097C7D2  48 03 C8                        add rcx, rax
0097C7D5  0F B6 44 24 3E                  movzx eax, byte ptr [rsp + 0x3e]
0097C7DA  48 6B D1 25                     imul rdx, rcx, 0x25
0097C7DE  48 03 D0                        add rdx, rax
0097C7E1  0F B6 44 24 3F                  movzx eax, byte ptr [rsp + 0x3f]
0097C7E6  48 6B CA 25                     imul rcx, rdx, 0x25
0097C7EA  49 8D 50 20                     lea rdx, [r8 + 0x20]
0097C7EE  48 03 C8                        add rcx, rax
0097C7F1  8B 02                           mov eax, dword ptr [rdx]
0097C7F3  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0097C7F7  FF C8                           dec eax
0097C7F9  23 C1                           and eax, ecx
0097C7FB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0097C7FF  48 8D 0C 80                     lea rcx, [rax + rax*4]
0097C803  49 8B 04 C9                     mov rax, qword ptr [r9 + rcx*8]
0097C807  48 3B C3                        cmp rax, rbx
0097C80A  0F 85 97 00 00 00               jne 0x14097c8a7
0097C810  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
0097C814  8B C8                           mov ecx, eax
0097C816  43 89 04 03                     mov dword ptr [r11 + r8], eax
0097C81A  E9 F3 FC FF FF                  jmp 0x14097c512
0097C81F  90                              nop
0097C820  0F B6 C3                        movzx eax, bl
0097C823  48 05 CB 5D B1 00               add rax, 0xb15dcb
0097C829  48 6B C8 25                     imul rcx, rax, 0x25
0097C82D  0F B6 44 24 31                  movzx eax, byte ptr [rsp + 0x31]
0097C832  48 03 C8                        add rcx, rax
0097C835  0F B6 44 24 32                  movzx eax, byte ptr [rsp + 0x32]
0097C83A  48 6B D1 25                     imul rdx, rcx, 0x25
0097C83E  48 03 D0                        add rdx, rax
0097C841  0F B6 44 24 33                  movzx eax, byte ptr [rsp + 0x33]
0097C846  48 6B CA 25                     imul rcx, rdx, 0x25
0097C84A  48 03 C8                        add rcx, rax
0097C84D  0F B6 44 24 34                  movzx eax, byte ptr [rsp + 0x34]
0097C852  48 6B D1 25                     imul rdx, rcx, 0x25
0097C856  48 03 D0                        add rdx, rax
0097C859  0F B6 44 24 35                  movzx eax, byte ptr [rsp + 0x35]
0097C85E  48 6B CA 25                     imul rcx, rdx, 0x25
0097C862  48 03 C8                        add rcx, rax
0097C865  0F B6 44 24 36                  movzx eax, byte ptr [rsp + 0x36]
0097C86A  48 6B D1 25                     imul rdx, rcx, 0x25
0097C86E  48 03 D0                        add rdx, rax
0097C871  0F B6 44 24 37                  movzx eax, byte ptr [rsp + 0x37]
0097C876  48 6B CA 25                     imul rcx, rdx, 0x25
0097C87A  49 8D 50 20                     lea rdx, [r8 + 0x20]
0097C87E  48 03 C8                        add rcx, rax
0097C881  8B 02                           mov eax, dword ptr [rdx]
0097C883  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
0097C887  44 8D 58 FF                     lea r11d, [rax - 1]
0097C88B  44 23 D9                        and r11d, ecx
0097C88E  4B 8D 0C 9B                     lea rcx, [r11 + r11*4]
0097C892  49 8B 04 C9                     mov rax, qword ptr [r9 + rcx*8]
0097C896  48 3B C3                        cmp rax, rbx
0097C899  75 73                           jne 0x14097c90e
0097C89B  45 89 58 10                     mov dword ptr [r8 + 0x10], r11d
0097C89F  41 8B CB                        mov ecx, r11d
0097C8A2  E9 5C FE FF FF                  jmp 0x14097c703
0097C8A7  48 85 C0                        test rax, rax
0097C8AA  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
0097C8AE  0F 84 A5 00 00 00               je 0x14097c959
0097C8B4  FF C0                           inc eax
0097C8B6  8B CF                           mov ecx, edi
0097C8B8  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0097C8BC  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
0097C8C3  83 F9 02                        cmp ecx, 2
0097C8C6  0F 83 07 02 00 00               jae 0x14097cad3
0097C8CC  3B 44 24 28                     cmp eax, dword ptr [rsp + 0x28]
0097C8D0  0F 83 E8 01 00 00               jae 0x14097cabe
0097C8D6  48 8D 0C 80                     lea rcx, [rax + rax*4]
0097C8DA  49 8B 04 C9                     mov rax, qword ptr [r9 + rcx*8]
0097C8DE  48 3B C3                        cmp rax, rbx
0097C8E1  74 1B                           je 0x14097c8fe
0097C8E3  48 85 C0                        test rax, rax
0097C8E6  0F 84 FE 00 00 00               je 0x14097c9ea
0097C8EC  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
0097C8F3  FF C0                           inc eax
0097C8F5  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
0097C8FC  EB CE                           jmp 0x14097c8cc
0097C8FE  8B 8C 24 90 00 00 00            mov ecx, dword ptr [rsp + 0x90]
0097C905  43 89 0C 03                     mov dword ptr [r11 + r8], ecx
0097C909  E9 04 FC FF FF                  jmp 0x14097c512
0097C90E  48 85 C0                        test rax, rax
0097C911  0F 84 8C 00 00 00               je 0x14097c9a3
0097C917  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
0097C91B  45 8D 53 01                     lea r10d, [r11 + 1]
0097C91F  8B CF                           mov ecx, edi
0097C921  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
0097C925  83 F9 02                        cmp ecx, 2
0097C928  0F 83 C3 01 00 00               jae 0x14097caf1
0097C92E  44 3B D0                        cmp r10d, eax
0097C931  0F 83 A5 01 00 00               jae 0x14097cadc
0097C937  41 8B C2                        mov eax, r10d
0097C93A  48 8D 0C 80                     lea rcx, [rax + rax*4]
0097C93E  49 8B 04 C9                     mov rax, qword ptr [r9 + rcx*8]
0097C942  48 3B C3                        cmp rax, rbx
0097C945  74 50                           je 0x14097c997
0097C947  48 85 C0                        test rax, rax
0097C94A  0F 84 CB 00 00 00               je 0x14097ca1b
0097C950  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
0097C954  41 FF C2                        inc r10d
0097C957  EB D5                           jmp 0x14097c92e
0097C959  43 89 04 03                     mov dword ptr [r11 + r8], eax
0097C95D  66 89 44 24 24                  mov word ptr [rsp + 0x24], ax
0097C962  8B 02                           mov eax, dword ptr [rdx]
0097C964  41 8B 48 1C                     mov ecx, dword ptr [r8 + 0x1c]
0097C968  C1 E8 02                        shr eax, 2
0097C96B  8D 04 40                        lea eax, [rax + rax*2]
0097C96E  3B C8                           cmp ecx, eax
0097C970  0F 83 B6 00 00 00               jae 0x14097ca2c
0097C976  8B 54 24 24                     mov edx, dword ptr [rsp + 0x24]
0097C97A  8D 41 01                        lea eax, [rcx + 1]
0097C97D  41 89 40 1C                     mov dword ptr [r8 + 0x1c], eax
0097C981  41 B2 01                        mov r10b, 1
0097C984  0F B7 C2                        movzx eax, dx
0097C987  48 8D 0C 80                     lea rcx, [rax + rax*4]
0097C98B  49 89 1C C9                     mov qword ptr [r9 + rcx*8], rbx
0097C98F  0F B7 CA                        movzx ecx, dx
0097C992  E9 87 FB FF FF                  jmp 0x14097c51e
0097C997  45 89 50 10                     mov dword ptr [r8 + 0x10], r10d
0097C99B  41 8B CA                        mov ecx, r10d
0097C99E  E9 60 FD FF FF                  jmp 0x14097c703
0097C9A3  41 0F B7 C3                     movzx eax, r11w
0097C9A7  45 89 58 10                     mov dword ptr [r8 + 0x10], r11d
0097C9AB  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
0097C9B2  8B 02                           mov eax, dword ptr [rdx]
0097C9B4  41 8B 48 1C                     mov ecx, dword ptr [r8 + 0x1c]
0097C9B8  C1 E8 02                        shr eax, 2
0097C9BB  8D 04 40                        lea eax, [rax + rax*2]
0097C9BE  3B C8                           cmp ecx, eax
0097C9C0  0F 83 D9 00 00 00               jae 0x14097ca9f
0097C9C6  8B 94 24 90 00 00 00            mov edx, dword ptr [rsp + 0x90]
0097C9CD  8D 41 01                        lea eax, [rcx + 1]
0097C9D0  41 89 40 1C                     mov dword ptr [r8 + 0x1c], eax
0097C9D4  41 B2 01                        mov r10b, 1
0097C9D7  0F B7 C2                        movzx eax, dx
0097C9DA  48 8D 0C 80                     lea rcx, [rax + rax*4]
0097C9DE  49 89 1C C9                     mov qword ptr [r9 + rcx*8], rbx
0097C9E2  0F B7 CA                        movzx ecx, dx
0097C9E5  E9 25 FD FF FF                  jmp 0x14097c70f
0097C9EA  8B 8C 24 90 00 00 00            mov ecx, dword ptr [rsp + 0x90]
0097C9F1  43 89 0C 03                     mov dword ptr [r11 + r8], ecx
0097C9F5  66 89 4C 24 24                  mov word ptr [rsp + 0x24], cx
0097C9FA  E9 63 FF FF FF                  jmp 0x14097c962
0097C9FF  49 8D 55 58                     lea rdx, [r13 + 0x58]
0097CA03  49 8B CD                        mov rcx, r13
0097CA06  E8 09 01 00 00                  call 0x14097cb14
0097CA0B  3D 01 00 00 C0                  cmp eax, 0xc0000001
0097CA10  0F 85 5A FB FF FF               jne 0x14097c570
0097CA16  E9 58 FC FF FF                  jmp 0x14097c673
0097CA1B  41 0F B7 C2                     movzx eax, r10w
0097CA1F  45 89 50 10                     mov dword ptr [r8 + 0x10], r10d
0097CA23  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
0097CA2A  EB 86                           jmp 0x14097c9b2
0097CA2C  49 8B D2                        mov rdx, r10
0097CA2F  49 8B CD                        mov rcx, r13
0097CA32  E8 DD 00 00 00                  call 0x14097cb14
0097CA37  3D 01 00 00 C0                  cmp eax, 0xc0000001
0097CA3C  0F 84 31 FC FF FF               je 0x14097c673
0097CA42  4C 8B 5C 24 40                  mov r11, qword ptr [rsp + 0x40]
0097CA47  E9 9D FA FF FF                  jmp 0x14097c4e9
0097CA4C  4C 8B 42 08                     mov r8, qword ptr [rdx + 8]
0097CA50  39 BC 24 A8 00 00 00            cmp dword ptr [rsp + 0xa8], edi
0097CA57  0F 85 A0 00 00 00               jne 0x14097cafd
0097CA5D  49 83 E0 F9                     and r8, 0xfffffffffffffff9
0097CA61  49 83 C8 01                     or r8, 1
0097CA65  4C 89 42 08                     mov qword ptr [rdx + 8], r8
0097CA69  41 83 E0 07                     and r8d, 7
0097CA6D  49 8B 8E F8 01 00 00            mov rcx, qword ptr [r14 + 0x1f8]
0097CA74  49 33 8E D0 01 00 00            xor rcx, qword ptr [r14 + 0x1d0]
0097CA7B  48 C1 E1 03                     shl rcx, 3
0097CA7F  49 0B C8                        or rcx, r8
0097CA82  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0097CA86  41 8B 86 84 03 00 00            mov eax, dword ptr [r14 + 0x384]
0097CA8D  89 42 14                        mov dword ptr [rdx + 0x14], eax
0097CA90  41 8B 86 D0 01 00 00            mov eax, dword ptr [r14 + 0x1d0]
0097CA97  89 42 10                        mov dword ptr [rdx + 0x10], eax
0097CA9A  E9 C2 FA FF FF                  jmp 0x14097c561
0097CA9F  49 8D 95 80 00 00 00            lea rdx, [r13 + 0x80]
0097CAA6  49 8B CD                        mov rcx, r13
0097CAA9  E8 66 00 00 00                  call 0x14097cb14
0097CAAE  3D 01 00 00 C0                  cmp eax, 0xc0000001
0097CAB3  0F 85 25 FC FF FF               jne 0x14097c6de
0097CAB9  E9 B5 FB FF FF                  jmp 0x14097c673
0097CABE  8B 4C 24 20                     mov ecx, dword ptr [rsp + 0x20]
0097CAC2  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0097CAC6  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
0097CACA  FF C1                           inc ecx
0097CACC  8B C7                           mov eax, edi
0097CACE  E9 E5 FD FF FF                  jmp 0x14097c8b8
0097CAD3  89 6C 24 24                     mov dword ptr [rsp + 0x24], ebp
0097CAD7  E9 86 FE FF FF                  jmp 0x14097c962
0097CADC  8B 4C 24 20                     mov ecx, dword ptr [rsp + 0x20]
0097CAE0  41 8B C3                        mov eax, r11d
0097CAE3  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
0097CAE7  FF C1                           inc ecx
0097CAE9  44 8B D7                        mov r10d, edi
0097CAEC  E9 30 FE FF FF                  jmp 0x14097c921
0097CAF1  89 AC 24 90 00 00 00            mov dword ptr [rsp + 0x90], ebp
0097CAF8  E9 B5 FE FF FF                  jmp 0x14097c9b2
0097CAFD  49 83 E0 FD                     and r8, 0xfffffffffffffffd
0097CB01  49 83 C8 05                     or r8, 5
0097CB05  4C 89 42 08                     mov qword ptr [rdx + 8], r8
0097CB09  E9 53 FA FF FF                  jmp 0x14097c561
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpLogPageAccess(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int8 v_stack_m11;
    unsigned __int8 v_stack_m12;
    unsigned __int8 v_stack_m13;
    unsigned __int8 v_stack_m14;
    unsigned __int8 v_stack_m15;
    unsigned __int8 v_stack_m16;
    unsigned __int8 v_stack_m17;
    unsigned __int64 v_stack_m18;
    unsigned __int8 v_stack_m19;
    unsigned __int8 v_stack_m1A;
    unsigned __int8 v_stack_m1B;
    unsigned __int8 v_stack_m1C;
    unsigned __int8 v_stack_m1D;
    unsigned __int8 v_stack_m1E;
    unsigned __int8 v_stack_m1F;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int16 v_stack_m54;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (80);
    v_rdi = 0;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) & (511)) != 0) goto loc_0097C6AF;
loc_0097C493:
    if (a2 == 0) goto loc_0097C695;
    if (a6 != 0) goto loc_0097C786;
    v_rbx = (*(unsigned __int64 *)(a2 + 504)) ^ (*(unsigned __int64 *)(a2 + 464));
    v_rbx = (v_rbx) & (result);
loc_0097C4C4:
    v_rbx = (v_rbx) & (-3);
    v_stack_m54 = 0;
    v_rbx = (v_rbx) | (1);
    v_stack_m40 = v_rbx;
    result = (unsigned int)((v_rbx) & (3));
    v_stack_m38 = result * 4 + 16;
loc_0097C4E9:
    a4 = (*(unsigned __int64 *)(a1 + 128 + 24) + 47) & (-8);
    if ((*(unsigned __int64 *)(a4 + (unsigned int)(*(unsigned int *)(result * 4 + 16 + *(unsigned __int64 *)(a1 + 128 + 24) * 1)) + (unsigned int)(*(unsigned int *)(result * 4 + 16 + *(unsigned __int64 *)(a1 + 128 + 24) * 1)) * 4 * 8)) != v_rbx) goto loc_0097C790;
loc_0097C512:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(result * 4 + 16 + *(unsigned __int64 *)(a1 + 128 + 24) * 1)))) == ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_0097C962;
    v_r10 = 0;
loc_0097C51E:
    if (*(unsigned __int64 *)(a1 + 128 + 24) == 0) goto loc_0097C673;
    v_rbp = (unsigned __int16)(((unsigned __int16)((unsigned int)(*(unsigned int *)(result * 4 + 16 + *(unsigned __int64 *)(a1 + 128 + 24) * 1)))) + (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 128 + 24) + 36)));
    v_stack_p18 = 2;
    result = (*(unsigned __int64 *)(a1 + 128 + 24) + 47) & (-8);
    if (0 != 0) goto loc_0097CA4C;
    if (((*(unsigned __int8 *)(result + (unsigned __int16)((unsigned int)(*(unsigned int *)(result * 4 + 16 + *(unsigned __int64 *)(a1 + 128 + 24) * 1))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(result * 4 + 16 + *(unsigned __int64 *)(a1 + 128 + 24) * 1))) * 4 * 8 + 8)) & (4)) != 0) goto loc_0097CA4C;
loc_0097C561:
    result = (unsigned __int8)((*(unsigned __int8 *)(a4)) & (3));
    v_rbx = (((unsigned __int8)(result)) == 2) ? 1 : 0;
    v_rbx = (unsigned int)((v_rbx) + 1);
loc_0097C570:
    if (((unsigned int)(v_rbx + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 112) + 16)) * 1)) > (*(unsigned int *)(*(unsigned __int64 *)(a1 + 112) + 20))) goto loc_0097C9FF;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 112) + 16) = (unsigned int)(v_rbx + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 112) + 16)) * 1);
    if (*(unsigned __int64 *)(a1 + 112) == 0) goto loc_0097C673;
    result = (*(unsigned __int64 *)(a1 + 112)) + (31);
    result = (result) & (-8);
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 112) + 16))))) << (4);
    v_rdi = (v_rdi) + (result);
    result = (unsigned __int8)((*(unsigned __int8 *)(a4)) & (3));
    if (((unsigned __int8)(result)) == 2) {
        *(unsigned __int64 *)(v_rdi) = v_xmm0;
        result = *(unsigned __int64 *)(v_rdi);
        result = (result) & (0xFFFFFFFFFFFFF00BULL);
        result = (result) | (8);
        *(unsigned __int64 *)(v_rdi) = result;
        v_rdi = (v_rdi) + (16);
    }
    if (((*(unsigned int *)(a3)) & (511)) != 0) goto loc_0097C627;
    a2 = (*(unsigned __int64 *)(v_rdi)) & (-3);
    a2 = (a2) | (1);
    *(unsigned __int64 *)(v_rdi) = a2;
    result = ((unsigned int)(*(unsigned int *)(a3))) >> (7);
    a2 = (a2) ^ (result);
    a2 = (a2) & (-5);
    a2 = (a2) ^ (result);
    a2 = (a2) & (-25);
    a2 = (a2) | (v_stack_p18 * 8);
    *(unsigned __int64 *)(v_rdi) = a2;
    result = (a2) ^ (*(unsigned __int64 *)(a3));
    result = (result) & (0xFFFFFFFFFFFFF000ULL);
    result = (result) ^ (a2);
    *(unsigned __int64 *)(v_rdi) = result;
    if (v_stack_p18 != 2) goto loc_0097C77A;
    *(unsigned __int16 *)(v_rdi + 10) = (unsigned __int16)(v_rbp);
    goto loc_0097C673;
loc_0097C627:
    a2 = (a2) & (-4);
    *(unsigned __int64 *)(v_rdi) = a2;
    result = ((unsigned int)(*(unsigned int *)(a3))) >> (7);
    a2 = (a2) ^ (result);
    a2 = (a2) & (-5);
    a2 = (a2) ^ (result);
    *(unsigned __int64 *)(v_rdi) = a2;
    result = ((unsigned int)(*(unsigned int *)(a3))) >> (7);
    a2 = (a2) ^ (result);
    a2 = (a2) & (-9);
    a2 = (a2) ^ (result);
    *(unsigned __int64 *)(v_rdi) = a2;
    a2 = (unsigned int)((a2) & (15));
    a1 = (*(unsigned __int64 *)(a3)) >> (12);
    a1 = ((unsigned int)((unsigned int)(a1))) << (4);
    a1 = (a1) | (a2);
    *(unsigned __int16 *)(v_rdi + 10) = (unsigned __int16)(v_rbp);
    *(unsigned __int64 *)(v_rdi) = a1;
    *(unsigned __int16 *)(v_rdi + 8) = (unsigned __int16)((unsigned __int16)((unsigned int)(0xFFFFULL)));
loc_0097C673:
    return v_rdi;
loc_0097C695:
    if (a6 != ((unsigned int)(v_rdi))) goto loc_0097C786;
    v_stack_p40 = v_rdi;
    goto loc_0097C561;
loc_0097C6AF:
    v_r10 = (unsigned int)((v_r10) & (511));
    v_r10 = (v_r10) << (3);
    result = (a5) - (v_r10);
    v_stack_p40 = (unsigned __int16)(v_rdi);
    v_stack_m18 = *(unsigned __int64 *)(result);
    v_rbx = (*(unsigned __int64 *)(result)) & (-4);
    v_stack_m20 = v_rbx;
loc_0097C6DE:
    a4 = (*(unsigned __int64 *)(a1 + 152) + 47) & (-8);
    if ((*(unsigned __int64 *)(a4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16)) * 4 * 8)) != v_rbx) goto loc_0097C820;
loc_0097C703:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16)))) == ((unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 56)))) goto loc_0097C9B2;
    v_r10 = 0;
loc_0097C70F:
    if (*(unsigned __int64 *)(a1 + 152) == 0) goto loc_0097C673;
    v_r12 = (unsigned __int16)(((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16)))) + (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 152) + 36)));
    if (0 == 0) goto loc_0097C493;
    a2 = (*(unsigned __int64 *)(a1 + 152) + 47) & (-8);
    result = (v_stack_m18) << (4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 8))) & (8));
    a4 = (v_stack_m18) >> (60);
    a1 = (a1) | (result);
    a1 = (a1) | (4);
    *(unsigned __int64 *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 8) = a1;
    result = (unsigned __int16)((*(unsigned __int16 *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 16)) & ((unsigned __int16)((unsigned int)(0xFFF0ULL))));
    a4 = (unsigned __int16)((a4) | ((unsigned __int16)(result)));
    *(unsigned __int16 *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 16) = (unsigned __int16)(a4);
    goto loc_0097C493;
loc_0097C77A:
    *(unsigned int *)(v_rdi + 8) = 0xFFFFFFFFULL;
    goto loc_0097C673;
loc_0097C786:
    goto loc_0097C4C4;
loc_0097C790:
    result = ((unsigned __int8)(a2)) + (0xB15DCBULL);
    a1 = ((unsigned int)(0xFFF0ULL)) * (result);
    a1 = (a1) + (v_stack_m17);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_m16);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_m15);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_m14);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_m13);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_m12);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_m11);
    v_stack_m28 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 32))) - 1);
    result = (unsigned int)((result) & ((unsigned int)(a1)));
    v_stack_m30 = (unsigned int)(result);
    if ((*(unsigned __int64 *)(a4 + result + result * 4 * 8)) != a2) goto loc_0097C8A7;
    *(unsigned int *)(v_stack_m28 + a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 * 1) = (unsigned int)((unsigned int)(v_stack_m30));
    goto loc_0097C512;
loc_0097C820:
    result = ((unsigned __int8)(a2)) + (0xB15DCBULL);
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m30)))) * (result);
    a1 = (a1) + (v_stack_m1F);
    a2 = (a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 32) * (a1);
    a2 = (a2) + (v_stack_m1E);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_m1D);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_m1C);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_m1B);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_m1A);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_m19);
    v_stack_m2C = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 32)));
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 32)) - 1) & ((unsigned int)(a1)));
    if ((*(unsigned __int64 *)(a4 + v_r11 + v_r11 * 4 * 8)) != a2) goto loc_0097C90E;
    *(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 16) = (unsigned int)(v_r11);
    goto loc_0097C703;
loc_0097C8A7:
    if (*(unsigned __int64 *)(a4 + v_r11 + v_r11 * 4 * 8) == 0) goto loc_0097C959;
    result = (unsigned int)(((unsigned int)(v_stack_m30)) + 1);
loc_0097C8B8:
    v_stack_m20 = (unsigned int)((unsigned int)((unsigned int)(v_rdi)));
    v_stack_p40 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= 2) goto loc_0097CAD3;
loc_0097C8CC:
    if (((unsigned int)(result)) >= v_stack_m28) goto loc_0097CABE;
    if ((*(unsigned __int64 *)(a4 + result + result * 4 * 8)) == a2) goto loc_0097C8FE;
    if (*(unsigned __int64 *)(a4 + result + result * 4 * 8) == 0) goto loc_0097C9EA;
    result = (unsigned int)(((unsigned int)(v_stack_p40)) + 1);
    v_stack_p40 = (unsigned int)(result);
    goto loc_0097C8CC;
loc_0097C8FE:
    *(unsigned int *)(v_r11 + a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 * 1) = (unsigned int)((unsigned int)(v_stack_p40));
    goto loc_0097C512;
loc_0097C90E:
    if (result == 0) goto loc_0097C9A3;
loc_0097C921:
    v_stack_m30 = (unsigned int)((unsigned int)((unsigned int)(v_rdi)));
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= 2) goto loc_0097CAF1;
loc_0097C92E:
    if (((unsigned int)(v_r11 + 1)) >= ((unsigned int)((unsigned int)(v_stack_m2C)))) goto loc_0097CADC;
    if ((*(unsigned __int64 *)(a4 + (unsigned int)((unsigned int)(v_r11 + 1)) + (unsigned int)((unsigned int)(v_r11 + 1)) * 4 * 8)) == a2) goto loc_0097C997;
    if (*(unsigned __int64 *)(a4 + (unsigned int)((unsigned int)(v_r11 + 1)) + (unsigned int)((unsigned int)(v_r11 + 1)) * 4 * 8) == 0) goto loc_0097CA1B;
    v_r10 = (unsigned int)((v_r11 + 1) + 1);
    goto loc_0097C92E;
loc_0097C959:
    *(unsigned int *)(v_r11 + a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 * 1) = (unsigned int)((unsigned int)(v_stack_m2C));
    v_stack_m2C = (unsigned __int16)((unsigned int)(v_stack_m2C));
loc_0097C962:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 32))) >> (2));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 28)))) >= ((unsigned int)(result + result * 2))) goto loc_0097CA2C;
    *(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 28)) + 1);
    *(unsigned __int64 *)(a4 + (unsigned __int16)((unsigned int)(v_stack_m2C)) + (unsigned __int16)((unsigned int)(v_stack_m2C)) * 4 * 8) = a2;
    goto loc_0097C51E;
loc_0097C997:
    *(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 16) = 1;
    goto loc_0097C703;
loc_0097C9A3:
    *(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 16) = (unsigned int)(v_r11);
    v_stack_p40 = (unsigned int)((unsigned __int16)(v_r11));
loc_0097C9B2:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m2C)))) >> (2));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 28)))) >= ((unsigned int)(result + result * 2))) goto loc_0097CA9F;
    *(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 28)) + 1);
    *(unsigned __int64 *)(a4 + (unsigned __int16)((unsigned int)(v_stack_p40)) + (unsigned __int16)((unsigned int)(v_stack_p40)) * 4 * 8) = a2;
    goto loc_0097C70F;
loc_0097C9EA:
    *(unsigned int *)(v_r11 + a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 * 1) = (unsigned int)((unsigned int)(v_stack_p40));
    v_stack_m2C = (unsigned __int16)((unsigned int)(v_stack_p40));
    goto loc_0097C962;
loc_0097C9FF:
    result = PfTReplaceCurrentBuffer(a1, a1 + 88, a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8, a4);
    if (((unsigned int)(result)) != 0xC0000001ULL) goto loc_0097C570;
    goto loc_0097C673;
loc_0097CA1B:
    *(unsigned int *)(a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8 + 16) = 1;
    v_stack_p40 = 1;
    goto loc_0097C9B2;
loc_0097CA2C:
    result = PfTReplaceCurrentBuffer(a1, 1, a2 + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 152) + 16))) * 4 * 8, a4);
    if (((unsigned int)(result)) == 0xC0000001ULL) goto loc_0097C673;
    goto loc_0097C4E9;
loc_0097CA4C:
    if (a6 != ((unsigned int)(v_rdi))) goto loc_0097CAFD;
    a3 = (*(unsigned __int64 *)(1 + 8)) & (-7);
    a3 = (a3) | (1);
    *(unsigned __int64 *)(1 + 8) = a3;
    a3 = (unsigned int)((a3) & (7));
    a1 = (*(unsigned __int64 *)(a2 + 504)) ^ (*(unsigned __int64 *)(a2 + 464));
    a1 = (a1) << (3);
    a1 = (a1) | (a3);
    *(unsigned __int64 *)(1 + 8) = a1;
    *(unsigned int *)(1 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 900)));
    *(unsigned int *)(1 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 464)));
    goto loc_0097C561;
loc_0097CA9F:
    result = PfTReplaceCurrentBuffer(a1, a1 + 128, a3, a4);
    if (((unsigned int)(result)) != 0xC0000001ULL) goto loc_0097C6DE;
    goto loc_0097C673;
loc_0097CABE:
    v_stack_m28 = (unsigned int)((unsigned int)(v_stack_m30));
    a1 = (unsigned int)(((unsigned int)(v_stack_m20)) + 1);
    goto loc_0097C8B8;
loc_0097CAD3:
    v_stack_m2C = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_0097C962;
loc_0097CADC:
    v_stack_m2C = (unsigned int)((unsigned int)((unsigned int)(v_stack_m10)));
    a1 = (unsigned int)(((unsigned int)(v_stack_m30)) + 1);
    goto loc_0097C921;
loc_0097CAF1:
    v_stack_p40 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_0097C9B2;
loc_0097CAFD:
    a3 = (a3) & (-3);
    a3 = (a3) | (5);
    *(unsigned __int64 *)(a1 + 128 + 8) = a3;
    goto loc_0097C561;
}
```

## 5. (Beta) C Style

```c
int64_t PfpLogPageAccess(void *Arg1, int64_t Arg2, void *Arg3, void *Arg4, void *Arg5, uint32_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint8_t v_stack_m11;
    uint8_t v_stack_m12;
    uint8_t v_stack_m13;
    uint8_t v_stack_m14;
    uint8_t v_stack_m15;
    uint8_t v_stack_m16;
    uint8_t v_stack_m17;
    uint64_t v_stack_m18;
    uint8_t v_stack_m19;
    uint8_t v_stack_m1A;
    uint8_t v_stack_m1B;
    uint8_t v_stack_m1C;
    uint8_t v_stack_m1D;
    uint8_t v_stack_m1E;
    uint8_t v_stack_m1F;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint16_t v_stack_m54;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (80);
    local_rdi = 0;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg3)))) & (511)) != 0) goto loc_0097C6AF;
loc_0097C493:
    if (Arg2 == 0) goto loc_0097C695;
    if (Arg6 != 0) goto loc_0097C786;
    local_rbx = (*(uint64_t *)(Arg2 + 0x1F8)) ^ (*(uint64_t *)(Arg2 + 0x1D0));
    local_rbx = (local_rbx) & (result);
loc_0097C4C4:
    local_rbx = (local_rbx) & (-3);
    v_stack_m54 = 0;
    local_rbx = (local_rbx) | (1);
    v_stack_m40 = local_rbx;
    result = (uint32_t)((local_rbx) & (3));
    v_stack_m38 = result * 4 + 16;
loc_0097C4E9:
    Arg4 = (*(uint64_t *)(arg1 + 0x80 + 0x18) + 47) & (-8);
    if ((*(uint64_t *)(arg4 + (uint32_t)(*(uint32_t *)(result * 4 + 0x10 + *(uint64_t *)(arg1 + 0x80 + 0x18) * 1)) + (uint32_t)(*(uint32_t *)(result * 4 + 0x10 + *(uint64_t *)(arg1 + 0x80 + 0x18) * 1)) * 4 * 8)) != local_rbx) goto loc_0097C790;
loc_0097C512:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(result * 4 + 0x10 + *(uint64_t *)(arg1 + 0x80 + 0x18) * 1)))) == ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_0097C962;
    local_r10 = 0;
loc_0097C51E:
    if (*(uint64_t *)(arg1 + 0x80 + 0x18) == 0) goto loc_0097C673;
    local_rbp = (uint16_t)(((uint16_t)((uint32_t)(*(uint32_t *)(result * 4 + 0x10 + *(uint64_t *)(arg1 + 0x80 + 0x18) * 1)))) + (*(uint16_t *)(*(uint64_t *)(arg1 + 0x80 + 0x18) + 0x24)));
    v_stack_p18 = 2;
    result = (*(uint64_t *)(arg1 + 0x80 + 0x18) + 47) & (-8);
    if (0 != 0) goto loc_0097CA4C;
    if (((*(uint8_t *)(result + (uint16_t)((uint32_t)(*(uint32_t *)(result * 4 + 0x10 + *(uint64_t *)(arg1 + 0x80 + 0x18) * 1))) + (uint16_t)((uint32_t)(*(uint32_t *)(result * 4 + 0x10 + *(uint64_t *)(arg1 + 0x80 + 0x18) * 1))) * 4 * 8 + 0x8)) & (4)) != 0) goto loc_0097CA4C;
loc_0097C561:
    result = (uint8_t)((*(uint8_t *)(arg4)) & (3));
    local_rbx = (((uint8_t)(result)) == 2) ? 1 : 0;
    local_rbx = (uint32_t)((local_rbx) + 1);
loc_0097C570:
    if (((uint32_t)(local_rbx + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x70) + 0x10)) * 1)) > (*(uint32_t *)(*(uint64_t *)(arg1 + 0x70) + 0x14))) goto loc_0097C9FF;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x70) + 0x10) = (uint32_t)(local_rbx + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x70) + 0x10)) * 1);
    if (*(uint64_t *)(arg1 + 0x70) == 0) goto loc_0097C673;
    result = (*(uint64_t *)(arg1 + 0x70)) + (31);
    result = (result) & (-8);
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x70) + 0x10))))) << (4);
    local_rdi = (local_rdi) + (result);
    result = (uint8_t)((*(uint8_t *)(arg4)) & (3));
    if (((uint8_t)(result)) == 2) {
        *(uint64_t *)(local_rdi) = v_xmm0;
        result = *(uint64_t *)(local_rdi);
        result = (result) & (0xFFFFFFFFFFFFF00BULL);
        result = (result) | (8);
        *(uint64_t *)(local_rdi) = result;
        local_rdi = (local_rdi) + (16);
    }
    if (((*(uint32_t *)(arg3)) & (511)) != 0) goto loc_0097C627;
    Arg2 = (*(uint64_t *)(local_rdi)) & (-3);
    Arg2 = (Arg2) | (1);
    *(uint64_t *)(local_rdi) = Arg2;
    result = ((uint32_t)(*(uint32_t *)(arg3))) >> (7);
    Arg2 = (Arg2) ^ (result);
    Arg2 = (Arg2) & (-5);
    Arg2 = (Arg2) ^ (result);
    Arg2 = (Arg2) & (-25);
    Arg2 = (Arg2) | (v_stack_p18 * 8);
    *(uint64_t *)(local_rdi) = Arg2;
    result = (Arg2) ^ (*(uint64_t *)(arg3));
    result = (result) & (0xFFFFFFFFFFFFF000ULL);
    result = (result) ^ (Arg2);
    *(uint64_t *)(local_rdi) = result;
    if (v_stack_p18 != 2) goto loc_0097C77A;
    *(uint16_t *)(local_rdi + 0xA) = (uint16_t)(local_rbp);
    goto loc_0097C673;
loc_0097C627:
    Arg2 = (Arg2) & (-4);
    *(uint64_t *)(local_rdi) = Arg2;
    result = ((uint32_t)(*(uint32_t *)(arg3))) >> (7);
    Arg2 = (Arg2) ^ (result);
    Arg2 = (Arg2) & (-5);
    Arg2 = (Arg2) ^ (result);
    *(uint64_t *)(local_rdi) = Arg2;
    result = ((uint32_t)(*(uint32_t *)(arg3))) >> (7);
    Arg2 = (Arg2) ^ (result);
    Arg2 = (Arg2) & (-9);
    Arg2 = (Arg2) ^ (result);
    *(uint64_t *)(local_rdi) = Arg2;
    Arg2 = (uint32_t)((Arg2) & (15));
    Arg1 = (*(uint64_t *)(arg3)) >> (12);
    Arg1 = ((uint32_t)((uint32_t)(Arg1))) << (4);
    Arg1 = (Arg1) | (Arg2);
    *(uint16_t *)(local_rdi + 0xA) = (uint16_t)(local_rbp);
    *(void **)(local_rdi) = Arg1;
    *(uint16_t *)(local_rdi + 0x8) = (uint16_t)((uint16_t)((uint32_t)(0xFFFFULL)));
loc_0097C673:
    return local_rdi;
loc_0097C695:
    if (Arg6 != ((uint32_t)(local_rdi))) goto loc_0097C786;
    v_stack_p40 = local_rdi;
    goto loc_0097C561;
loc_0097C6AF:
    local_r10 = (uint32_t)((local_r10) & (511));
    local_r10 = (local_r10) << (3);
    result = (Arg5) - (local_r10);
    v_stack_p40 = (uint16_t)(local_rdi);
    v_stack_m18 = *(uint64_t *)(result);
    local_rbx = (*(uint64_t *)(result)) & (-4);
    v_stack_m20 = local_rbx;
loc_0097C6DE:
    Arg4 = (*(uint64_t *)(arg1 + 0x98) + 47) & (-8);
    if ((*(uint64_t *)(arg4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10)) * 4 * 8)) != local_rbx) goto loc_0097C820;
loc_0097C703:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10)))) == ((uint16_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) goto loc_0097C9B2;
    local_r10 = 0;
loc_0097C70F:
    if (*(uint64_t *)(arg1 + 0x98) == 0) goto loc_0097C673;
    local_r12 = (uint16_t)(((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10)))) + (*(uint16_t *)(*(uint64_t *)(arg1 + 0x98) + 0x24)));
    if (0 == 0) goto loc_0097C493;
    Arg2 = (*(uint64_t *)(arg1 + 0x98) + 47) & (-8);
    result = (v_stack_m18) << (4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x8))) & (8));
    Arg4 = (v_stack_m18) >> (60);
    Arg1 = (Arg1) | (result);
    Arg1 = (Arg1) | (4);
    *(void **)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x8) = Arg1;
    result = (uint16_t)((*(uint16_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x10)) & ((uint16_t)((uint32_t)(0xFFF0ULL))));
    Arg4 = (uint16_t)((Arg4) | ((uint16_t)(result)));
    *(uint16_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x10) = (uint16_t)(Arg4);
    goto loc_0097C493;
loc_0097C77A:
    *(uint32_t *)(local_rdi + 0x8) = 0xFFFFFFFFULL;
    goto loc_0097C673;
loc_0097C786:
    goto loc_0097C4C4;
loc_0097C790:
    result = ((uint8_t)(Arg2)) + (0xB15DCBULL);
    Arg1 = ((uint32_t)(0xFFF0ULL)) * (result);
    Arg1 = (Arg1) + (v_stack_m17);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m16);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_m15);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m14);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_m13);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m12);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_m11);
    v_stack_m28 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x20))) - 1);
    result = (uint32_t)((result) & ((uint32_t)(Arg1)));
    v_stack_m30 = (uint32_t)(result);
    if ((*(uint64_t *)(arg4 + result + result * 4 * 8)) != Arg2) goto loc_0097C8A7;
    *(uint32_t *)(v_stack_m28 + Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 * 1) = (uint32_t)((uint32_t)(v_stack_m30));
    goto loc_0097C512;
loc_0097C820:
    result = ((uint8_t)(Arg2)) + (0xB15DCBULL);
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m30)))) * (result);
    Arg1 = (Arg1) + (v_stack_m1F);
    Arg2 = (Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 32) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m1E);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_m1D);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m1C);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_m1B);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m1A);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_m19);
    v_stack_m2C = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x20)));
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x20)) - 1) & ((uint32_t)(Arg1)));
    if ((*(uint64_t *)(arg4 + local_r11 + local_r11 * 4 * 8)) != Arg2) goto loc_0097C90E;
    *(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x10) = (uint32_t)(local_r11);
    goto loc_0097C703;
loc_0097C8A7:
    if (*(uint64_t *)(arg4 + local_r11 + local_r11 * 4 * 8) == 0) goto loc_0097C959;
    result = (uint32_t)(((uint32_t)(v_stack_m30)) + 1);
loc_0097C8B8:
    v_stack_m20 = (uint32_t)((uint32_t)((uint32_t)(local_rdi)));
    v_stack_p40 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= 2) goto loc_0097CAD3;
loc_0097C8CC:
    if (((uint32_t)(result)) >= v_stack_m28) goto loc_0097CABE;
    if ((*(uint64_t *)(arg4 + result + result * 4 * 8)) == Arg2) goto loc_0097C8FE;
    if (*(uint64_t *)(arg4 + result + result * 4 * 8) == 0) goto loc_0097C9EA;
    result = (uint32_t)(((uint32_t)(v_stack_p40)) + 1);
    v_stack_p40 = (uint32_t)(result);
    goto loc_0097C8CC;
loc_0097C8FE:
    *(uint32_t *)(local_r11 + Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 * 1) = (uint32_t)((uint32_t)(v_stack_p40));
    goto loc_0097C512;
loc_0097C90E:
    if (result == 0) goto loc_0097C9A3;
loc_0097C921:
    v_stack_m30 = (uint32_t)((uint32_t)((uint32_t)(local_rdi)));
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= 2) goto loc_0097CAF1;
loc_0097C92E:
    if (((uint32_t)(local_r11 + 1)) >= ((uint32_t)((uint32_t)(v_stack_m2C)))) goto loc_0097CADC;
    if ((*(uint64_t *)(arg4 + (uint32_t)((uint32_t)(local_r11 + 0x1)) + (uint32_t)((uint32_t)(local_r11 + 0x1)) * 4 * 8)) == Arg2) goto loc_0097C997;
    if (*(uint64_t *)(arg4 + (uint32_t)((uint32_t)(local_r11 + 0x1)) + (uint32_t)((uint32_t)(local_r11 + 0x1)) * 4 * 8) == 0) goto loc_0097CA1B;
    local_r10 = (uint32_t)((local_r11 + 1) + 1);
    goto loc_0097C92E;
loc_0097C959:
    *(uint32_t *)(local_r11 + Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 * 1) = (uint32_t)((uint32_t)(v_stack_m2C));
    v_stack_m2C = (uint16_t)((uint32_t)(v_stack_m2C));
loc_0097C962:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x20))) >> (2));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x1C)))) >= ((uint32_t)(result + result * 2))) goto loc_0097CA2C;
    *(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x1C)) + 1);
    *(uint64_t *)(arg4 + (uint16_t)((uint32_t)(v_stack_m2C)) + (uint16_t)((uint32_t)(v_stack_m2C)) * 4 * 8) = Arg2;
    goto loc_0097C51E;
loc_0097C997:
    *(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x10) = 1;
    goto loc_0097C703;
loc_0097C9A3:
    *(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x10) = (uint32_t)(local_r11);
    v_stack_p40 = (uint32_t)((uint16_t)(local_r11));
loc_0097C9B2:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m2C)))) >> (2));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x1C)))) >= ((uint32_t)(result + result * 2))) goto loc_0097CA9F;
    *(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x1C)) + 1);
    *(uint64_t *)(arg4 + (uint16_t)((uint32_t)(v_stack_p40)) + (uint16_t)((uint32_t)(v_stack_p40)) * 4 * 8) = Arg2;
    goto loc_0097C70F;
loc_0097C9EA:
    *(uint32_t *)(local_r11 + Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 * 1) = (uint32_t)((uint32_t)(v_stack_p40));
    v_stack_m2C = (uint16_t)((uint32_t)(v_stack_p40));
    goto loc_0097C962;
loc_0097C9FF:
    result = PfTReplaceCurrentBuffer(Arg1, Arg1 + 88, Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8, Arg4);
    if (((uint32_t)(result)) != 0xC0000001ULL) goto loc_0097C570;
    goto loc_0097C673;
loc_0097CA1B:
    *(uint32_t *)(Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8 + 0x10) = 1;
    v_stack_p40 = 1;
    goto loc_0097C9B2;
loc_0097CA2C:
    result = PfTReplaceCurrentBuffer(Arg1, 1, Arg2 + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x98) + 0x10))) * 4 * 8, Arg4);
    if (((uint32_t)(result)) == 0xC0000001ULL) goto loc_0097C673;
    goto loc_0097C4E9;
loc_0097CA4C:
    if (Arg6 != ((uint32_t)(local_rdi))) goto loc_0097CAFD;
    Arg3 = (*(uint64_t *)(1 + 0x8)) & (-7);
    Arg3 = (Arg3) | (1);
    *(void **)(1 + 0x8) = Arg3;
    Arg3 = (uint32_t)((Arg3) & (7));
    Arg1 = (*(uint64_t *)(Arg2 + 0x1F8)) ^ (*(uint64_t *)(Arg2 + 0x1D0));
    Arg1 = (Arg1) << (3);
    Arg1 = (Arg1) | (Arg3);
    *(void **)(1 + 0x8) = Arg1;
    *(uint32_t *)(1 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x384)));
    *(uint32_t *)(1 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1D0)));
    goto loc_0097C561;
loc_0097CA9F:
    result = PfTReplaceCurrentBuffer(Arg1, Arg1 + 128, Arg3, Arg4);
    if (((uint32_t)(result)) != 0xC0000001ULL) goto loc_0097C6DE;
    goto loc_0097C673;
loc_0097CABE:
    v_stack_m28 = (uint32_t)((uint32_t)(v_stack_m30));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m20)) + 1);
    goto loc_0097C8B8;
loc_0097CAD3:
    v_stack_m2C = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_0097C962;
loc_0097CADC:
    v_stack_m2C = (uint32_t)((uint32_t)((uint32_t)(v_stack_m10)));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m30)) + 1);
    goto loc_0097C921;
loc_0097CAF1:
    v_stack_p40 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_0097C9B2;
loc_0097CAFD:
    Arg3 = (Arg3) & (-3);
    Arg3 = (Arg3) | (5);
    *(void **)(arg1 + 0x80 + 0x8) = Arg3;
    goto loc_0097C561;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `8` | `R` |
| `Arg4` | `+ 0x0` | `128` | `R` |
| `Arg5` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0097C450&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
