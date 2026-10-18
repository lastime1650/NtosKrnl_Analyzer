# DifZwOpenProcessTokenExWrapper

- RVA: `0x00644200`–`0x00644387` (길이 `391` bytes)
- VA: `0x0000000140644200`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2B7C`
- 디코드: `113`개 명령, `391/391` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00644240` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00644268` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006442A4` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006442CA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006442E3` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006442F5` → [ZwOpenProcessTokenEx](../6A/ZwOpenProcessTokenEx_function_006AD6D0.md) (function, `0x006AD6D0`)
- `0x00644321` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00644347` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00644360` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00644278` → RVA `0x00F048B8` (`.data`; read)
- `0x00644291` → RVA `0x00F04980` (`.data`; read)
- `0x0064429D` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00644200  48 8B C4                        mov rax, rsp
00644203  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00644207  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064420B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064420F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00644213  55                              push rbp
00644214  41 54                           push r12
00644216  41 55                           push r13
00644218  41 56                           push r14
0064421A  41 57                           push r15
0064421C  48 8B EC                        mov rbp, rsp
0064421F  48 83 EC 50                     sub rsp, 0x50
00644223  33 C0                           xor eax, eax
00644225  0F 57 C0                        xorps xmm0, xmm0
00644228  4D 8B F9                        mov r15, r9
0064422B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064422F  45 8B E0                        mov r12d, r8d
00644232  44 8B EA                        mov r13d, edx
00644235  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00644239  8D 48 4D                        lea ecx, [rax + 0x4d]
0064423C  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00644240  E8 EF 17 E5 FF                  call 0x140495a34
00644245  4C 8B F0                        mov r14, rax
00644248  48 85 C0                        test rax, rax
0064424B  0F 84 97 00 00 00               je 0x1406442e8
00644251  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00644254  F6 C1 18                        test cl, 0x18
00644257  74 0A                           je 0x140644263
00644259  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0064425D  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00644261  EB 0E                           jmp 0x140644271
00644263  F6 C1 04                        test cl, 4
00644266  74 09                           je 0x140644271
00644268  E8 9B F9 E8 FF                  call 0x1404d3c08
0064426D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00644271  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00644275  40 32 F6                        xor sil, sil
00644278  40 38 35 39 06 8C 00            cmp byte ptr [rip + 0x8c0639], sil
0064427F  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00644283  44 89 6D E4                     mov dword ptr [rbp - 0x1c], r13d
00644287  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
0064428B  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0064428F  75 0C                           jne 0x14064429d
00644291  F7 05 E5 06 8C 00 00 08 00 00   test dword ptr [rip + 0x8c06e5], 0x800
0064429B  74 13                           je 0x1406442b0
0064429D  48 8D 0D DC FB 8B 00            lea rcx, [rip + 0x8bfbdc]
006442A4  E8 77 23 BD FF                  call 0x140216620
006442A9  40 8A F0                        mov sil, al
006442AC  84 C0                           test al, al
006442AE  74 38                           je 0x1406442e8
006442B0  49 8D 7E 20                     lea rdi, [r14 + 0x20]
006442B4  48 8B 1F                        mov rbx, qword ptr [rdi]
006442B7  EB 19                           jmp 0x1406442d2
006442B9  48 8D 43 F0                     lea rax, [rbx - 0x10]
006442BD  48 85 C0                        test rax, rax
006442C0  74 0D                           je 0x1406442cf
006442C2  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006442C6  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006442CA  E8 01 68 07 00                  call 0x1406baad0
006442CF  48 8B 1B                        mov rbx, qword ptr [rbx]
006442D2  48 3B DF                        cmp rbx, rdi
006442D5  75 E2                           jne 0x1406442b9
006442D7  40 84 F6                        test sil, sil
006442DA  74 0C                           je 0x1406442e8
006442DC  48 8D 0D 9D FB 8B 00            lea rcx, [rip + 0x8bfb9d]
006442E3  E8 98 5B D0 FF                  call 0x140349e80
006442E8  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
006442EC  4D 8B CF                        mov r9, r15
006442EF  45 8B C4                        mov r8d, r12d
006442F2  41 8B D5                        mov edx, r13d
006442F5  E8 D6 93 06 00                  call 0x1406ad6d0
006442FA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
006442FD  4D 85 F6                        test r14, r14
00644300  74 63                           je 0x140644365
00644302  40 32 FF                        xor dil, dil
00644305  40 38 3D AC 05 8C 00            cmp byte ptr [rip + 0x8c05ac], dil
0064430C  75 0C                           jne 0x14064431a
0064430E  F7 05 68 06 8C 00 00 08 00 00   test dword ptr [rip + 0x8c0668], 0x800
00644318  74 13                           je 0x14064432d
0064431A  48 8D 0D 5F FB 8B 00            lea rcx, [rip + 0x8bfb5f]
00644321  E8 FA 22 BD FF                  call 0x140216620
00644326  40 8A F8                        mov dil, al
00644329  84 C0                           test al, al
0064432B  74 38                           je 0x140644365
0064432D  49 8D 76 30                     lea rsi, [r14 + 0x30]
00644331  48 8B 1E                        mov rbx, qword ptr [rsi]
00644334  EB 19                           jmp 0x14064434f
00644336  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064433A  48 85 C0                        test rax, rax
0064433D  74 0D                           je 0x14064434c
0064433F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00644343  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00644347  E8 84 67 07 00                  call 0x1406baad0
0064434C  48 8B 1B                        mov rbx, qword ptr [rbx]
0064434F  48 3B DE                        cmp rbx, rsi
00644352  75 E2                           jne 0x140644336
00644354  40 84 FF                        test dil, dil
00644357  74 0C                           je 0x140644365
00644359  48 8D 0D 20 FB 8B 00            lea rcx, [rip + 0x8bfb20]
00644360  E8 1B 5B D0 FF                  call 0x140349e80
00644365  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00644368  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064436D  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00644371  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00644375  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00644379  49 8B E3                        mov rsp, r11
0064437C  41 5F                           pop r15
0064437E  41 5E                           pop r14
00644380  41 5D                           pop r13
00644382  41 5C                           pop r12
00644384  5D                              pop rbp
00644385  C3                              ret
00644386  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenProcessTokenExWrapper(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 77, a2, a3, a4);
    if (result == 0) goto loc_006442E8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00644263;
    v_stack_m58 = v_stack_p0;
    goto loc_00644271;
loc_00644263:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m44 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = (unsigned int)((unsigned int)(a3));
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9176633)) != 0) goto loc_0064429D;
    if (((*(unsigned int *)(v_rip + 9176805)) & (0x800ULL)) == 0) goto loc_006442B0;
loc_0064429D:
    result = ExAcquireRundownProtection(v_rip + 9173980, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006442E8;
loc_006442B0:
    goto loc_006442D2;
loc_006442B9:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006442D2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006442B9;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9173917;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwOpenProcessTokenEx(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00644365;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9176492)) != 0) goto loc_0064431A;
    if (((*(unsigned int *)(v_rip + 9176680)) & (0x800ULL)) == 0) goto loc_0064432D;
loc_0064431A:
    result = ExAcquireRundownProtection(v_rip + 9173855, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00644365;
loc_0064432D:
    goto loc_0064434F;
loc_00644336:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0064434F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00644336;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9173792;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenProcessTokenExWrapper(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 77, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006442E8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00644263;
    v_stack_m58 = v_stack_p0;
    goto loc_00644271;
loc_00644263:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m44 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8C0639)) != 0) goto loc_0064429D;
    if (((*(uint32_t *)(v_rip + 0x8C06E5)) & (0x800ULL)) == 0) goto loc_006442B0;
loc_0064429D:
    result = ExAcquireRundownProtection(v_rip + 9173980, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006442E8;
loc_006442B0:
    goto loc_006442D2;
loc_006442B9:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006442D2:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006442B9;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9173917;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwOpenProcessTokenEx(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00644365;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C05AC)) != 0) goto loc_0064431A;
    if (((*(uint32_t *)(v_rip + 0x8C0668)) & (0x800ULL)) == 0) goto loc_0064432D;
loc_0064431A:
    result = ExAcquireRundownProtection(v_rip + 9173855, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00644365;
loc_0064432D:
    goto loc_0064434F;
loc_00644336:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_0064434F:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00644336;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9173792;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00644200&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00644200[BB_00644200]
  bb_00644251[BB_00644251]
  bb_00644259[BB_00644259]
  bb_00644263[BB_00644263]
  bb_00644268[BB_00644268]
  bb_00644271[BB_00644271]
  bb_00644291[BB_00644291]
  bb_0064429D[BB_0064429D]
  bb_006442B0[BB_006442B0]
  bb_006442B9[BB_006442B9]
  bb_006442C2[BB_006442C2]
  bb_006442CF[BB_006442CF]
  bb_006442D2[BB_006442D2]
  bb_006442D7[BB_006442D7]
  bb_006442DC[BB_006442DC]
  bb_006442E8[BB_006442E8]
  bb_00644302[BB_00644302]
  bb_0064430E[BB_0064430E]
  bb_0064431A[BB_0064431A]
  bb_0064432D[BB_0064432D]
  bb_00644336[BB_00644336]
  bb_0064433F[BB_0064433F]
  bb_0064434C[BB_0064434C]
  bb_0064434F[BB_0064434F]
  bb_00644354[BB_00644354]
  bb_00644359[BB_00644359]
  bb_00644365[BB_00644365]
  bb_00644386[BB_00644386]
  bb_00644200 -->|branch| bb_006442E8
  bb_00644200 -->|fallthrough| bb_00644251
  bb_00644251 -->|branch| bb_00644263
  bb_00644251 -->|fallthrough| bb_00644259
  bb_00644259 -->|branch| bb_00644271
  bb_00644263 -->|branch| bb_00644271
  bb_00644263 -->|fallthrough| bb_00644268
  bb_00644268 -->|flow| bb_00644271
  bb_00644271 -->|branch| bb_0064429D
  bb_00644271 -->|fallthrough| bb_00644291
  bb_00644291 -->|branch| bb_006442B0
  bb_00644291 -->|fallthrough| bb_0064429D
  bb_0064429D -->|branch| bb_006442E8
  bb_0064429D -->|fallthrough| bb_006442B0
  bb_006442B0 -->|branch| bb_006442D2
  bb_006442B9 -->|branch| bb_006442CF
  bb_006442B9 -->|fallthrough| bb_006442C2
  bb_006442C2 -->|flow| bb_006442CF
  bb_006442CF -->|flow| bb_006442D2
  bb_006442D2 -->|branch| bb_006442B9
  bb_006442D2 -->|fallthrough| bb_006442D7
  bb_006442D7 -->|branch| bb_006442E8
  bb_006442D7 -->|fallthrough| bb_006442DC
  bb_006442DC -->|flow| bb_006442E8
  bb_006442E8 -->|branch| bb_00644365
  bb_006442E8 -->|fallthrough| bb_00644302
  bb_00644302 -->|branch| bb_0064431A
  bb_00644302 -->|fallthrough| bb_0064430E
  bb_0064430E -->|branch| bb_0064432D
  bb_0064430E -->|fallthrough| bb_0064431A
  bb_0064431A -->|branch| bb_00644365
  bb_0064431A -->|fallthrough| bb_0064432D
  bb_0064432D -->|branch| bb_0064434F
  bb_00644336 -->|branch| bb_0064434C
  bb_00644336 -->|fallthrough| bb_0064433F
  bb_0064433F -->|flow| bb_0064434C
  bb_0064434C -->|flow| bb_0064434F
  bb_0064434F -->|branch| bb_00644336
  bb_0064434F -->|fallthrough| bb_00644354
  bb_00644354 -->|branch| bb_00644365
  bb_00644354 -->|fallthrough| bb_00644359
  bb_00644359 -->|flow| bb_00644365
```
