# DifIofCallDriverWrapper

- RVA: `0x0062DCF0`–`0x0062DE71` (길이 `385` bytes)
- VA: `0x000000014062DCF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2C68`
- 디코드: `111`개 명령, `385/385` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062DD32` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062DD5A` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062DD8E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062DDB4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062DDCD` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062DDDF` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062DE0B` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062DE31` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062DE4A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062DD6A` → RVA `0x00F048B8` (`.data`; read)
- `0x0062DD7B` → RVA `0x00F04980` (`.data`; read)
- `0x0062DD87` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062DCF0  48 8B C4                        mov rax, rsp
0062DCF3  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062DCF7  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0062DCFB  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0062DCFF  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
0062DD03  55                              push rbp
0062DD04  41 54                           push r12
0062DD06  41 55                           push r13
0062DD08  41 56                           push r14
0062DD0A  41 57                           push r15
0062DD0C  48 8B EC                        mov rbp, rsp
0062DD0F  48 83 EC 50                     sub rsp, 0x50
0062DD13  0F 57 C0                        xorps xmm0, xmm0
0062DD16  33 C0                           xor eax, eax
0062DD18  4C 8B E9                        mov r13, rcx
0062DD1B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0062DD1F  B9 2E 01 00 00                  mov ecx, 0x12e
0062DD24  4D 8B F8                        mov r15, r8
0062DD27  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0062DD2B  4C 8B E2                        mov r12, rdx
0062DD2E  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0062DD32  E8 FD 7C E6 FF                  call 0x140495a34
0062DD37  4C 8B F0                        mov r14, rax
0062DD3A  48 85 C0                        test rax, rax
0062DD3D  0F 84 8F 00 00 00               je 0x14062ddd2
0062DD43  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
0062DD46  F6 C1 18                        test cl, 0x18
0062DD49  74 0A                           je 0x14062dd55
0062DD4B  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0062DD4F  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0062DD53  EB 0E                           jmp 0x14062dd63
0062DD55  F6 C1 04                        test cl, 4
0062DD58  74 09                           je 0x14062dd63
0062DD5A  E8 A9 5E EA FF                  call 0x1404d3c08
0062DD5F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0062DD63  40 32 F6                        xor sil, sil
0062DD66  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0062DD6A  40 38 35 47 6B 8D 00            cmp byte ptr [rip + 0x8d6b47], sil
0062DD71  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0062DD75  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0062DD79  75 0C                           jne 0x14062dd87
0062DD7B  F7 05 FB 6B 8D 00 00 08 00 00   test dword ptr [rip + 0x8d6bfb], 0x800
0062DD85  74 13                           je 0x14062dd9a
0062DD87  48 8D 0D F2 60 8D 00            lea rcx, [rip + 0x8d60f2]
0062DD8E  E8 8D 88 BE FF                  call 0x140216620
0062DD93  40 8A F0                        mov sil, al
0062DD96  84 C0                           test al, al
0062DD98  74 38                           je 0x14062ddd2
0062DD9A  49 8D 7E 20                     lea rdi, [r14 + 0x20]
0062DD9E  48 8B 1F                        mov rbx, qword ptr [rdi]
0062DDA1  EB 19                           jmp 0x14062ddbc
0062DDA3  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062DDA7  48 85 C0                        test rax, rax
0062DDAA  74 0D                           je 0x14062ddb9
0062DDAC  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062DDB0  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062DDB4  E8 17 CD 08 00                  call 0x1406baad0
0062DDB9  48 8B 1B                        mov rbx, qword ptr [rbx]
0062DDBC  48 3B DF                        cmp rbx, rdi
0062DDBF  75 E2                           jne 0x14062dda3
0062DDC1  40 84 F6                        test sil, sil
0062DDC4  74 0C                           je 0x14062ddd2
0062DDC6  48 8D 0D B3 60 8D 00            lea rcx, [rip + 0x8d60b3]
0062DDCD  E8 AE C0 D1 FF                  call 0x140349e80
0062DDD2  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0062DDD6  4D 8B C7                        mov r8, r15
0062DDD9  49 8B D4                        mov rdx, r12
0062DDDC  49 8B CD                        mov rcx, r13
0062DDDF  E8 EC CC 08 00                  call 0x1406baad0
0062DDE4  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0062DDE7  4D 85 F6                        test r14, r14
0062DDEA  74 63                           je 0x14062de4f
0062DDEC  40 32 FF                        xor dil, dil
0062DDEF  40 38 3D C2 6A 8D 00            cmp byte ptr [rip + 0x8d6ac2], dil
0062DDF6  75 0C                           jne 0x14062de04
0062DDF8  F7 05 7E 6B 8D 00 00 08 00 00   test dword ptr [rip + 0x8d6b7e], 0x800
0062DE02  74 13                           je 0x14062de17
0062DE04  48 8D 0D 75 60 8D 00            lea rcx, [rip + 0x8d6075]
0062DE0B  E8 10 88 BE FF                  call 0x140216620
0062DE10  40 8A F8                        mov dil, al
0062DE13  84 C0                           test al, al
0062DE15  74 38                           je 0x14062de4f
0062DE17  49 8D 76 30                     lea rsi, [r14 + 0x30]
0062DE1B  48 8B 1E                        mov rbx, qword ptr [rsi]
0062DE1E  EB 19                           jmp 0x14062de39
0062DE20  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062DE24  48 85 C0                        test rax, rax
0062DE27  74 0D                           je 0x14062de36
0062DE29  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062DE2D  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062DE31  E8 9A CC 08 00                  call 0x1406baad0
0062DE36  48 8B 1B                        mov rbx, qword ptr [rbx]
0062DE39  48 3B DE                        cmp rbx, rsi
0062DE3C  75 E2                           jne 0x14062de20
0062DE3E  40 84 FF                        test dil, dil
0062DE41  74 0C                           je 0x14062de4f
0062DE43  48 8D 0D 36 60 8D 00            lea rcx, [rip + 0x8d6036]
0062DE4A  E8 31 C0 D1 FF                  call 0x140349e80
0062DE4F  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0062DE52  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0062DE57  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0062DE5B  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0062DE5F  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0062DE63  49 8B E3                        mov rsp, r11
0062DE66  41 5F                           pop r15
0062DE68  41 5E                           pop r14
0062DE6A  41 5D                           pop r13
0062DE6C  41 5C                           pop r12
0062DE6E  5D                              pop rbp
0062DE6F  C3                              ret
0062DE70  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIofCallDriverWrapper(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(302, a2, a3, a4);
    if (result == 0) goto loc_0062DDD2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062DD55;
    v_stack_m58 = v_stack_p0;
    goto loc_0062DD63;
loc_0062DD55:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_rsi = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9268039)) != 0) goto loc_0062DD87;
    if (((*(unsigned int *)(v_rip + 9268219)) & (0x800ULL)) == 0) goto loc_0062DD9A;
loc_0062DD87:
    result = ExAcquireRundownProtection(v_rip + 9265394, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062DDD2;
loc_0062DD9A:
    goto loc_0062DDBC;
loc_0062DDA3:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062DDBC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062DDA3;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9265331;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0062DE4F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9267906)) != 0) goto loc_0062DE04;
    if (((*(unsigned int *)(v_rip + 9268094)) & (0x800ULL)) == 0) goto loc_0062DE17;
loc_0062DE04:
    result = ExAcquireRundownProtection(v_rip + 9265269, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062DE4F;
loc_0062DE17:
    goto loc_0062DE39;
loc_0062DE20:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062DE39:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_0062DE20;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9265206;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifIofCallDriverWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(302, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062DDD2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062DD55;
    v_stack_m58 = v_stack_p0;
    goto loc_0062DD63;
loc_0062DD55:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_rsi = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8D6B47)) != 0) goto loc_0062DD87;
    if (((*(uint32_t *)(v_rip + 0x8D6BFB)) & (0x800ULL)) == 0) goto loc_0062DD9A;
loc_0062DD87:
    result = ExAcquireRundownProtection(v_rip + 9265394, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062DDD2;
loc_0062DD9A:
    goto loc_0062DDBC;
loc_0062DDA3:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062DDBC:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062DDA3;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9265331;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0062DE4F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D6AC2)) != 0) goto loc_0062DE04;
    if (((*(uint32_t *)(v_rip + 0x8D6B7E)) & (0x800ULL)) == 0) goto loc_0062DE17;
loc_0062DE04:
    result = ExAcquireRundownProtection(v_rip + 9265269, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062DE4F;
loc_0062DE17:
    goto loc_0062DE39;
loc_0062DE20:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062DE39:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_0062DE20;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9265206;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062DCF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062DCF0[BB_0062DCF0]
  bb_0062DD43[BB_0062DD43]
  bb_0062DD4B[BB_0062DD4B]
  bb_0062DD55[BB_0062DD55]
  bb_0062DD5A[BB_0062DD5A]
  bb_0062DD63[BB_0062DD63]
  bb_0062DD7B[BB_0062DD7B]
  bb_0062DD87[BB_0062DD87]
  bb_0062DD9A[BB_0062DD9A]
  bb_0062DDA3[BB_0062DDA3]
  bb_0062DDAC[BB_0062DDAC]
  bb_0062DDB9[BB_0062DDB9]
  bb_0062DDBC[BB_0062DDBC]
  bb_0062DDC1[BB_0062DDC1]
  bb_0062DDC6[BB_0062DDC6]
  bb_0062DDD2[BB_0062DDD2]
  bb_0062DDEC[BB_0062DDEC]
  bb_0062DDF8[BB_0062DDF8]
  bb_0062DE04[BB_0062DE04]
  bb_0062DE17[BB_0062DE17]
  bb_0062DE20[BB_0062DE20]
  bb_0062DE29[BB_0062DE29]
  bb_0062DE36[BB_0062DE36]
  bb_0062DE39[BB_0062DE39]
  bb_0062DE3E[BB_0062DE3E]
  bb_0062DE43[BB_0062DE43]
  bb_0062DE4F[BB_0062DE4F]
  bb_0062DE70[BB_0062DE70]
  bb_0062DCF0 -->|branch| bb_0062DDD2
  bb_0062DCF0 -->|fallthrough| bb_0062DD43
  bb_0062DD43 -->|branch| bb_0062DD55
  bb_0062DD43 -->|fallthrough| bb_0062DD4B
  bb_0062DD4B -->|branch| bb_0062DD63
  bb_0062DD55 -->|branch| bb_0062DD63
  bb_0062DD55 -->|fallthrough| bb_0062DD5A
  bb_0062DD5A -->|flow| bb_0062DD63
  bb_0062DD63 -->|branch| bb_0062DD87
  bb_0062DD63 -->|fallthrough| bb_0062DD7B
  bb_0062DD7B -->|branch| bb_0062DD9A
  bb_0062DD7B -->|fallthrough| bb_0062DD87
  bb_0062DD87 -->|branch| bb_0062DDD2
  bb_0062DD87 -->|fallthrough| bb_0062DD9A
  bb_0062DD9A -->|branch| bb_0062DDBC
  bb_0062DDA3 -->|branch| bb_0062DDB9
  bb_0062DDA3 -->|fallthrough| bb_0062DDAC
  bb_0062DDAC -->|flow| bb_0062DDB9
  bb_0062DDB9 -->|flow| bb_0062DDBC
  bb_0062DDBC -->|branch| bb_0062DDA3
  bb_0062DDBC -->|fallthrough| bb_0062DDC1
  bb_0062DDC1 -->|branch| bb_0062DDD2
  bb_0062DDC1 -->|fallthrough| bb_0062DDC6
  bb_0062DDC6 -->|flow| bb_0062DDD2
  bb_0062DDD2 -->|branch| bb_0062DE4F
  bb_0062DDD2 -->|fallthrough| bb_0062DDEC
  bb_0062DDEC -->|branch| bb_0062DE04
  bb_0062DDEC -->|fallthrough| bb_0062DDF8
  bb_0062DDF8 -->|branch| bb_0062DE17
  bb_0062DDF8 -->|fallthrough| bb_0062DE04
  bb_0062DE04 -->|branch| bb_0062DE4F
  bb_0062DE04 -->|fallthrough| bb_0062DE17
  bb_0062DE17 -->|branch| bb_0062DE39
  bb_0062DE20 -->|branch| bb_0062DE36
  bb_0062DE20 -->|fallthrough| bb_0062DE29
  bb_0062DE29 -->|flow| bb_0062DE36
  bb_0062DE36 -->|flow| bb_0062DE39
  bb_0062DE39 -->|branch| bb_0062DE20
  bb_0062DE39 -->|fallthrough| bb_0062DE3E
  bb_0062DE3E -->|branch| bb_0062DE4F
  bb_0062DE3E -->|fallthrough| bb_0062DE43
  bb_0062DE43 -->|flow| bb_0062DE4F
```
