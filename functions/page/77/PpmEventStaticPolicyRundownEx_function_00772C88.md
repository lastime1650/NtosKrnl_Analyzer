# PpmEventStaticPolicyRundownEx

- RVA: `0x00772C88`–`0x00772E55` (길이 `461` bytes)
- VA: `0x0000000140772C88`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD570`
- 디코드: `82`개 명령, `461/461` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **19**

### Outgoing calls
- `0x00772CC4` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00772E32` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00772E3E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmEventStaticPolicyRundown](../76/PpmEventStaticPolicyRundown_function_0076A528.md) at `0x0076A553`

### Static image references
- `0x00772C9A` → RVA `0x00E0A740` (`.data`; read)
- `0x00772CAA` → RVA `0x00E67A39` (`.data`; read)
- `0x00772CB6` → RVA `0x00F083E8` (`.data`; read)
- `0x00772CBD` → RVA `0x00021B28` (`.rdata`; read)
- `0x00772CD1` → RVA `0x00FC5050` (`ALMOSTRO`; read)
- `0x00772CD7` → RVA `0x00FC6CC8` (`ALMOSTRO`; read)
- `0x00772CE7` → RVA `0x00FC5178` (`ALMOSTRO`; read)
- `0x00772CFE` → RVA `0x00FC50E0` (`ALMOSTRO`; read)
- `0x00772D16` → RVA `0x00FC517C` (`ALMOSTRO`; read)
- `0x00772D26` → RVA `0x00FC506C` (`ALMOSTRO`; read)
- `0x00772D35` → RVA `0x00FC6CD4` (`ALMOSTRO`; read)
- `0x00772D49` → RVA `0x00E0B978` (`.data`; read)
- `0x00772D54` → RVA `0x00FC5100` (`ALMOSTRO`; read)
- `0x00772D5F` → RVA `0x00FC50B0` (`ALMOSTRO`; read)
- `0x00772D73` → RVA `0x00FC50B8` (`ALMOSTRO`; read)
- `0x00772D7E` → RVA `0x00F083A2` (`.data`; read)
- `0x00772D89` → RVA `0x00F083A0` (`.data`; read)
- `0x00772D9D` → RVA `0x00FC6C34` (`ALMOSTRO`; read)
- `0x00772DA8` → RVA `0x00FC6C88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00772CC4` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00772E32` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00772E3E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00772C88  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00772C8D  55                              push rbp
00772C8E  48 8D 6C 24 C0                  lea rbp, [rsp - 0x40]
00772C93  48 81 EC 40 01 00 00            sub rsp, 0x140
00772C9A  48 8B 05 9F 7A 69 00            mov rax, qword ptr [rip + 0x697a9f]
00772CA1  48 33 C4                        xor rax, rsp
00772CA4  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00772CA8  33 DB                           xor ebx, ebx
00772CAA  38 1D 89 4D 6F 00               cmp byte ptr [rip + 0x6f4d89], bl
00772CB0  0F 84 81 01 00 00               je 0x140772e37
00772CB6  48 8B 0D 2B 57 79 00            mov rcx, qword ptr [rip + 0x79572b]
00772CBD  48 8D 15 64 EE 8A FF            lea rdx, [rip - 0x75119c]
00772CC4  E8 87 F7 C1 FF                  call 0x140392450
00772CC9  84 C0                           test al, al
00772CCB  0F 84 66 01 00 00               je 0x140772e37
00772CD1  8B 0D 79 23 85 00               mov ecx, dword ptr [rip + 0x852379]
00772CD7  48 8D 05 EA 3F 85 00            lea rax, [rip + 0x853fea]
00772CDE  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00772CE3  44 8D 4B 0F                     lea r9d, [rbx + 0xf]
00772CE7  48 8D 05 8A 24 85 00            lea rax, [rip + 0x85248a]
00772CEE  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00772CF2  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00772CF7  48 8D 15 2A EE 8A FF            lea rdx, [rip - 0x7511d6]
00772CFE  48 8D 05 DB 23 85 00            lea rax, [rip + 0x8523db]
00772D05  48 C7 44 24 48 04 00 00 00      mov qword ptr [rsp + 0x48], 4
00772D0E  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00772D13  83 F9 FF                        cmp ecx, -1
00772D16  48 8D 05 5F 24 85 00            lea rax, [rip + 0x85245f]
00772D1D  48 C7 44 24 58 04 00 00 00      mov qword ptr [rsp + 0x58], 4
00772D26  0F 44 0D 3F 23 85 00            cmove ecx, dword ptr [rip + 0x85233f]
00772D2D  45 33 C0                        xor r8d, r8d
00772D30  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00772D35  48 8D 05 98 3F 85 00            lea rax, [rip + 0x853f98]
00772D3C  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00772D40  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00772D45  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00772D49  48 8D 05 28 8C 69 00            lea rax, [rip + 0x698c28]
00772D50  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00772D54  48 8D 05 A5 23 85 00            lea rax, [rip + 0x8523a5]
00772D5B  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00772D5F  48 8D 05 4A 23 85 00            lea rax, [rip + 0x85234a]
00772D66  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00772D6A  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00772D6F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00772D73  48 8D 05 3E 23 85 00            lea rax, [rip + 0x85233e]
00772D7A  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00772D7E  48 8D 05 1D 56 79 00            lea rax, [rip + 0x79561d]
00772D85  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00772D89  0F B6 05 10 56 79 00            movzx eax, byte ptr [rip + 0x795610]
00772D90  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00772D94  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00772D99  48 89 45 00                     mov qword ptr [rbp], rax
00772D9D  48 8D 05 90 3E 85 00            lea rax, [rip + 0x853e90]
00772DA4  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00772DA8  48 8D 05 D9 3E 85 00            lea rax, [rip + 0x853ed9]
00772DAF  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00772DB3  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00772DB8  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
00772DBC  48 8B 0D 25 56 79 00            mov rcx, qword ptr [rip + 0x795625]
00772DC3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00772DC8  48 C7 44 24 68 04 00 00 00      mov qword ptr [rsp + 0x68], 4
00772DD1  48 C7 44 24 78 04 00 00 00      mov qword ptr [rsp + 0x78], 4
00772DDA  48 C7 45 88 04 00 00 00         mov qword ptr [rbp - 0x78], 4
00772DE2  48 C7 45 98 04 00 00 00         mov qword ptr [rbp - 0x68], 4
00772DEA  48 C7 45 A8 04 00 00 00         mov qword ptr [rbp - 0x58], 4
00772DF2  48 C7 45 B8 04 00 00 00         mov qword ptr [rbp - 0x48], 4
00772DFA  48 C7 45 C8 04 00 00 00         mov qword ptr [rbp - 0x38], 4
00772E02  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
00772E0A  48 C7 45 E8 04 00 00 00         mov qword ptr [rbp - 0x18], 4
00772E12  48 C7 45 F8 02 00 00 00         mov qword ptr [rbp - 8], 2
00772E1A  48 C7 45 08 04 00 00 00         mov qword ptr [rbp + 8], 4
00772E22  48 C7 45 18 04 00 00 00         mov qword ptr [rbp + 0x18], 4
00772E2A  48 C7 45 28 04 00 00 00         mov qword ptr [rbp + 0x28], 4
00772E32  E8 E9 98 CA FF                  call 0x14041c720
00772E37  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00772E3B  48 33 CC                        xor rcx, rsp
00772E3E  E8 FD 97 F3 FF                  call 0x1406ac640
00772E43  48 8B 9C 24 50 01 00 00         mov rbx, qword ptr [rsp + 0x150]
00772E4B  48 81 C4 40 01 00 00            add rsp, 0x140
00772E52  5D                              pop rbp
00772E53  C3                              ret
00772E54  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmEventStaticPolicyRundownEx(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m114;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 6912671)) ^ (v_rsp);
    v_stack_m18 = result;
    v_rbx = 0;
    if ((*(unsigned __int8 *)(v_rip + 7294345)) == 0) goto loc_00772E37;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 7952171), v_rip - 7672220, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned int *)(v_rip + 8725369);
        result = v_rip + 8732650;
        v_stack_m108 = result;
        a4 = v_rbx + 15;
        result = v_rip + 8725642;
        v_stack_m118 = 0;
        v_stack_mF8 = result;
        a2 = v_rip - 7672278;
        result = v_rip + 8725467;
        v_stack_m100 = 4;
        v_stack_mE8 = result;
        result = v_rip + 8725599;
        v_stack_mF0 = 4;
        if (((unsigned int)(a1)) == -1) { a1 = *(unsigned int *)(v_rip + 8725311); }
        a3 = 0;
        v_stack_mD8 = result;
        result = v_rip + 8732568;
        v_stack_mC8 = result;
        result = v_stack_m118;
        v_stack_mB8 = result;
        result = v_rip + 6917160;
        v_stack_mA8 = result;
        result = v_rip + 8725413;
        v_stack_m98 = result;
        result = v_rip + 8725322;
        v_stack_m88 = result;
        result = v_stack_m114;
        v_stack_m78 = result;
        result = v_rip + 8725310;
        v_stack_m68 = result;
        result = v_rip + 7951901;
        v_stack_m58 = result;
        result = *(unsigned __int8 *)(v_rip + 7951888);
        v_stack_m110 = (unsigned int)(result);
        result = v_stack_m110;
        v_stack_m48 = result;
        result = v_rip + 8732304;
        v_stack_m38 = result;
        result = v_rip + 8732377;
        v_stack_m28 = result;
        result = v_stack_m108;
        v_stack_m114 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 7951909);
        v_stack_m128 = result;
        v_stack_mE0 = 4;
        v_stack_mD0 = 4;
        v_stack_mC0 = 4;
        v_stack_mB0 = 4;
        v_stack_mA0 = 4;
        v_stack_m90 = 4;
        v_stack_m80 = 4;
        v_stack_m70 = 4;
        v_stack_m60 = 4;
        v_stack_m50 = 2;
        v_stack_m40 = 4;
        v_stack_m30 = 4;
        v_stack_m20 = 4;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (320);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmEventStaticPolicyRundownEx(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m114;
    uint32_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0x697A9F)) ^ (local_rsp);
    v_stack_m18 = result;
    local_rbx = 0;
    if ((*(uint8_t *)(v_rip + 0x6F4D89)) == 0) goto loc_00772E37;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x79572B), v_rip - 7672220, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint32_t *)(v_rip + 0x852379);
        result = v_rip + 8732650;
        v_stack_m108 = result;
        a4 = local_rbx + 15;
        result = v_rip + 8725642;
        v_stack_m118 = 0;
        v_stack_mF8 = result;
        Arg2 = v_rip - 7672278;
        result = v_rip + 8725467;
        v_stack_m100 = 4;
        v_stack_mE8 = result;
        result = v_rip + 8725599;
        v_stack_mF0 = 4;
        if (((uint32_t)(Arg1)) == -1) { Arg1 = *(uint32_t *)(v_rip + 0x85233F); }
        Arg3 = 0;
        v_stack_mD8 = result;
        result = v_rip + 8732568;
        v_stack_mC8 = result;
        result = v_stack_m118;
        v_stack_mB8 = result;
        result = v_rip + 6917160;
        v_stack_mA8 = result;
        result = v_rip + 8725413;
        v_stack_m98 = result;
        result = v_rip + 8725322;
        v_stack_m88 = result;
        result = v_stack_m114;
        v_stack_m78 = result;
        result = v_rip + 8725310;
        v_stack_m68 = result;
        result = v_rip + 7951901;
        v_stack_m58 = result;
        result = *(uint8_t *)(v_rip + 0x795610);
        v_stack_m110 = (uint32_t)(result);
        result = v_stack_m110;
        v_stack_m48 = result;
        result = v_rip + 8732304;
        v_stack_m38 = result;
        result = v_rip + 8732377;
        v_stack_m28 = result;
        result = v_stack_m108;
        v_stack_m114 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x795625);
        v_stack_m128 = result;
        v_stack_mE0 = 4;
        v_stack_mD0 = 4;
        v_stack_mC0 = 4;
        v_stack_mB0 = 4;
        v_stack_mA0 = 4;
        v_stack_m90 = 4;
        v_stack_m80 = 4;
        v_stack_m70 = 4;
        v_stack_m60 = 4;
        v_stack_m50 = 2;
        v_stack_m40 = 4;
        v_stack_m30 = 4;
        v_stack_m20 = 4;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (320);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00772C88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00772C88[BB_00772C88]
  bb_00772CB6[BB_00772CB6]
  bb_00772CD1[BB_00772CD1]
  bb_00772E37[BB_00772E37]
  bb_00772E54[BB_00772E54]
  bb_00772C88 -->|branch| bb_00772E37
  bb_00772C88 -->|fallthrough| bb_00772CB6
  bb_00772CB6 -->|branch| bb_00772E37
  bb_00772CB6 -->|fallthrough| bb_00772CD1
  bb_00772CD1 -->|flow| bb_00772E37
```
