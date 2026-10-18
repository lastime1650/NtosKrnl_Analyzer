# DifObReferenceObjectByPointerWithTagWrapper

- RVA: `0x00638210`–`0x006383A2` (길이 `402` bytes)
- VA: `0x0000000140638210`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `116`개 명령, `402/402` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00638250` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00638276` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006382B8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006382DE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006382F7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00638310` → [ObReferenceObjectByPointerWithTag](../41/ObReferenceObjectByPointerWithTag_function_00419870.md) (function, `0x00419870`)
- `0x0063833C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00638362` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063837B` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00638286` → RVA `0x00F048B8` (`.data`; read)
- `0x006382A5` → RVA `0x00F04980` (`.data`; read)
- `0x006382B1` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00638210  48 8B C4                        mov rax, rsp
00638213  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00638217  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063821B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0063821F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00638223  55                              push rbp
00638224  41 54                           push r12
00638226  41 55                           push r13
00638228  41 56                           push r14
0063822A  41 57                           push r15
0063822C  48 8B EC                        mov rbp, rsp
0063822F  48 83 EC 60                     sub rsp, 0x60
00638233  0F 57 C0                        xorps xmm0, xmm0
00638236  B9 C8 00 00 00                  mov ecx, 0xc8
0063823B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063823F  45 8A F9                        mov r15b, r9b
00638242  4D 8B E0                        mov r12, r8
00638245  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00638249  44 8B EA                        mov r13d, edx
0063824C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00638250  E8 DF D7 E5 FF                  call 0x140495a34
00638255  48 8B F0                        mov rsi, rax
00638258  48 85 C0                        test rax, rax
0063825B  0F 84 9B 00 00 00               je 0x1406382fc
00638261  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00638264  A8 18                           test al, 0x18
00638266  74 0A                           je 0x140638272
00638268  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063826C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00638270  EB 0D                           jmp 0x14063827f
00638272  A8 04                           test al, 4
00638274  74 09                           je 0x14063827f
00638276  E8 8D B9 E9 FF                  call 0x1404d3c08
0063827B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063827F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00638283  45 32 F6                        xor r14b, r14b
00638286  44 38 35 2B C6 8C 00            cmp byte ptr [rip + 0x8cc62b], r14b
0063828D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00638291  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00638294  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00638297  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
0063829B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063829F  44 88 7D DC                     mov byte ptr [rbp - 0x24], r15b
006382A3  75 0C                           jne 0x1406382b1
006382A5  F7 05 D1 C6 8C 00 00 08 00 00   test dword ptr [rip + 0x8cc6d1], 0x800
006382AF  74 13                           je 0x1406382c4
006382B1  48 8D 0D C8 BB 8C 00            lea rcx, [rip + 0x8cbbc8]
006382B8  E8 63 E3 BD FF                  call 0x140216620
006382BD  44 8A F0                        mov r14b, al
006382C0  84 C0                           test al, al
006382C2  74 38                           je 0x1406382fc
006382C4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006382C8  48 8B 1F                        mov rbx, qword ptr [rdi]
006382CB  EB 19                           jmp 0x1406382e6
006382CD  48 8D 43 F0                     lea rax, [rbx - 0x10]
006382D1  48 85 C0                        test rax, rax
006382D4  74 0D                           je 0x1406382e3
006382D6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006382DA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006382DE  E8 ED 27 08 00                  call 0x1406baad0
006382E3  48 8B 1B                        mov rbx, qword ptr [rbx]
006382E6  48 3B DF                        cmp rbx, rdi
006382E9  75 E2                           jne 0x1406382cd
006382EB  45 84 F6                        test r14b, r14b
006382EE  74 0C                           je 0x1406382fc
006382F0  48 8D 0D 89 BB 8C 00            lea rcx, [rip + 0x8cbb89]
006382F7  E8 84 1B D1 FF                  call 0x140349e80
006382FC  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
006382FF  45 8A CF                        mov r9b, r15b
00638302  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00638306  4D 8B C4                        mov r8, r12
00638309  41 8B D5                        mov edx, r13d
0063830C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00638310  E8 5B 15 DE FF                  call 0x140419870
00638315  89 45 F8                        mov dword ptr [rbp - 8], eax
00638318  48 85 F6                        test rsi, rsi
0063831B  74 63                           je 0x140638380
0063831D  40 32 FF                        xor dil, dil
00638320  40 38 3D 91 C5 8C 00            cmp byte ptr [rip + 0x8cc591], dil
00638327  75 0C                           jne 0x140638335
00638329  F7 05 4D C6 8C 00 00 08 00 00   test dword ptr [rip + 0x8cc64d], 0x800
00638333  74 13                           je 0x140638348
00638335  48 8D 0D 44 BB 8C 00            lea rcx, [rip + 0x8cbb44]
0063833C  E8 DF E2 BD FF                  call 0x140216620
00638341  40 8A F8                        mov dil, al
00638344  84 C0                           test al, al
00638346  74 38                           je 0x140638380
00638348  48 83 C6 30                     add rsi, 0x30
0063834C  48 8B 1E                        mov rbx, qword ptr [rsi]
0063834F  EB 19                           jmp 0x14063836a
00638351  48 8D 43 F0                     lea rax, [rbx - 0x10]
00638355  48 85 C0                        test rax, rax
00638358  74 0D                           je 0x140638367
0063835A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063835E  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00638362  E8 69 27 08 00                  call 0x1406baad0
00638367  48 8B 1B                        mov rbx, qword ptr [rbx]
0063836A  48 3B DE                        cmp rbx, rsi
0063836D  75 E2                           jne 0x140638351
0063836F  40 84 FF                        test dil, dil
00638372  74 0C                           je 0x140638380
00638374  48 8D 0D 05 BB 8C 00            lea rcx, [rip + 0x8cbb05]
0063837B  E8 00 1B D1 FF                  call 0x140349e80
00638380  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00638383  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00638388  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0063838C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00638390  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00638394  49 8B E3                        mov rsp, r11
00638397  41 5F                           pop r15
00638399  41 5E                           pop r14
0063839B  41 5D                           pop r13
0063839D  41 5C                           pop r12
0063839F  5D                              pop rbp
006383A0  C3                              ret
006383A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifObReferenceObjectByPointerWithTagWrapper(__int64 a1, int a2, __int64 a3, unsigned __int8 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(200, a2, a3, a4);
    if (result == 0) goto loc_006382FC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00638272;
    v_stack_m58 = v_stack_p0;
    goto loc_0063827F;
loc_00638272:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = (unsigned int)((unsigned int)(a5));
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m4C = a4;
    if ((*(unsigned __int8 *)(v_rip + 9225771)) != 0) goto loc_006382B1;
    if (((*(unsigned int *)(v_rip + 9225937)) & (0x800ULL)) == 0) goto loc_006382C4;
loc_006382B1:
    result = ExAcquireRundownProtection(v_rip + 9223112, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006382FC;
loc_006382C4:
    goto loc_006382E6;
loc_006382CD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006382E6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006382CD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9223049;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = ObReferenceObjectByPointerWithTag(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_00638380;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9225617)) != 0) goto loc_00638335;
    if (((*(unsigned int *)(v_rip + 9225805)) & (0x800ULL)) == 0) goto loc_00638348;
loc_00638335:
    result = ExAcquireRundownProtection(v_rip + 9222980, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00638380;
loc_00638348:
    v_rsi = (result) + (48);
    goto loc_0063836A;
loc_00638351:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0063836A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00638351;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9222917;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifObReferenceObjectByPointerWithTagWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, uint8_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint8_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(200, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006382FC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00638272;
    v_stack_m58 = v_stack_p0;
    goto loc_0063827F;
loc_00638272:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m4C = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8CC62B)) != 0) goto loc_006382B1;
    if (((*(uint32_t *)(v_rip + 0x8CC6D1)) & (0x800ULL)) == 0) goto loc_006382C4;
loc_006382B1:
    result = ExAcquireRundownProtection(v_rip + 9223112, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006382FC;
loc_006382C4:
    goto loc_006382E6;
loc_006382CD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006382E6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006382CD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9223049;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = ObReferenceObjectByPointerWithTag(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_00638380;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CC591)) != 0) goto loc_00638335;
    if (((*(uint32_t *)(v_rip + 0x8CC64D)) & (0x800ULL)) == 0) goto loc_00638348;
loc_00638335:
    result = ExAcquireRundownProtection(v_rip + 9222980, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00638380;
loc_00638348:
    local_rsi = (result) + (48);
    goto loc_0063836A;
loc_00638351:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_0063836A:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00638351;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9222917;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00638210&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00638210[BB_00638210]
  bb_00638261[BB_00638261]
  bb_00638268[BB_00638268]
  bb_00638272[BB_00638272]
  bb_00638276[BB_00638276]
  bb_0063827F[BB_0063827F]
  bb_006382A5[BB_006382A5]
  bb_006382B1[BB_006382B1]
  bb_006382C4[BB_006382C4]
  bb_006382CD[BB_006382CD]
  bb_006382D6[BB_006382D6]
  bb_006382E3[BB_006382E3]
  bb_006382E6[BB_006382E6]
  bb_006382EB[BB_006382EB]
  bb_006382F0[BB_006382F0]
  bb_006382FC[BB_006382FC]
  bb_0063831D[BB_0063831D]
  bb_00638329[BB_00638329]
  bb_00638335[BB_00638335]
  bb_00638348[BB_00638348]
  bb_00638351[BB_00638351]
  bb_0063835A[BB_0063835A]
  bb_00638367[BB_00638367]
  bb_0063836A[BB_0063836A]
  bb_0063836F[BB_0063836F]
  bb_00638374[BB_00638374]
  bb_00638380[BB_00638380]
  bb_006383A1[BB_006383A1]
  bb_00638210 -->|branch| bb_006382FC
  bb_00638210 -->|fallthrough| bb_00638261
  bb_00638261 -->|branch| bb_00638272
  bb_00638261 -->|fallthrough| bb_00638268
  bb_00638268 -->|branch| bb_0063827F
  bb_00638272 -->|branch| bb_0063827F
  bb_00638272 -->|fallthrough| bb_00638276
  bb_00638276 -->|flow| bb_0063827F
  bb_0063827F -->|branch| bb_006382B1
  bb_0063827F -->|fallthrough| bb_006382A5
  bb_006382A5 -->|branch| bb_006382C4
  bb_006382A5 -->|fallthrough| bb_006382B1
  bb_006382B1 -->|branch| bb_006382FC
  bb_006382B1 -->|fallthrough| bb_006382C4
  bb_006382C4 -->|branch| bb_006382E6
  bb_006382CD -->|branch| bb_006382E3
  bb_006382CD -->|fallthrough| bb_006382D6
  bb_006382D6 -->|flow| bb_006382E3
  bb_006382E3 -->|flow| bb_006382E6
  bb_006382E6 -->|branch| bb_006382CD
  bb_006382E6 -->|fallthrough| bb_006382EB
  bb_006382EB -->|branch| bb_006382FC
  bb_006382EB -->|fallthrough| bb_006382F0
  bb_006382F0 -->|flow| bb_006382FC
  bb_006382FC -->|branch| bb_00638380
  bb_006382FC -->|fallthrough| bb_0063831D
  bb_0063831D -->|branch| bb_00638335
  bb_0063831D -->|fallthrough| bb_00638329
  bb_00638329 -->|branch| bb_00638348
  bb_00638329 -->|fallthrough| bb_00638335
  bb_00638335 -->|branch| bb_00638380
  bb_00638335 -->|fallthrough| bb_00638348
  bb_00638348 -->|branch| bb_0063836A
  bb_00638351 -->|branch| bb_00638367
  bb_00638351 -->|fallthrough| bb_0063835A
  bb_0063835A -->|flow| bb_00638367
  bb_00638367 -->|flow| bb_0063836A
  bb_0063836A -->|branch| bb_00638351
  bb_0063836A -->|fallthrough| bb_0063836F
  bb_0063836F -->|branch| bb_00638380
  bb_0063836F -->|fallthrough| bb_00638374
  bb_00638374 -->|flow| bb_00638380
```
