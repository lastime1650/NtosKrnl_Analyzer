# PopDiagTracePolicyChange

- RVA: `0x00705718`–`0x00705819` (길이 `257` bytes)
- VA: `0x0000000140705718`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BAEE4`
- 디코드: `61`개 명령, `257/257` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00705774` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x007057FE` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x0070580A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopAdaptivePowerSettingCallback](../76/PopAdaptivePowerSettingCallback_function_0076B7A0.md) at `0x0076B95C`

### Static image references
- `0x00705726` → RVA `0x00E0A740` (`.data`; read)
- `0x00705734` → RVA `0x00F081C0` (`.data`; read)
- `0x0070573E` → RVA `0x00E67858` (`.data`; read)
- `0x00705748` → RVA `0x00F081AC` (`.data`; read)
- `0x00705754` → RVA `0x00F081A8` (`.data`; read)
- `0x00705766` → RVA `0x00F0B408` (`.data`; read)
- `0x0070576D` → RVA `0x0001EEC0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00705774` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x007057FE` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x0070580A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00705718  40 55                           push rbp
0070571A  48 8D 6C 24 B9                  lea rbp, [rsp - 0x47]
0070571F  48 81 EC D0 00 00 00            sub rsp, 0xd0
00705726  48 8B 05 13 50 70 00            mov rax, qword ptr [rip + 0x705013]
0070572D  48 33 C4                        xor rax, rsp
00705730  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00705734  8B 05 86 2A 80 00               mov eax, dword ptr [rip + 0x802a86]
0070573A  83 65 CF 00                     and dword ptr [rbp - 0x31], 0
0070573E  80 3D 13 21 76 00 00            cmp byte ptr [rip + 0x762113], 0
00705745  89 45 C7                        mov dword ptr [rbp - 0x39], eax
00705748  8B 05 5E 2A 80 00               mov eax, dword ptr [rip + 0x802a5e]
0070574E  89 45 BF                        mov dword ptr [rbp - 0x41], eax
00705751  89 45 B7                        mov dword ptr [rbp - 0x49], eax
00705754  8B 05 4E 2A 80 00               mov eax, dword ptr [rip + 0x802a4e]
0070575A  89 45 AF                        mov dword ptr [rbp - 0x51], eax
0070575D  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00705760  0F 84 9D 00 00 00               je 0x140705803
00705766  48 8B 0D 9B 5C 80 00            mov rcx, qword ptr [rip + 0x805c9b]
0070576D  48 8D 15 4C 97 91 FF            lea rdx, [rip - 0x6e68b4]
00705774  E8 D7 CC C8 FF                  call 0x140392450
00705779  84 C0                           test al, al
0070577B  0F 84 82 00 00 00               je 0x140705803
00705781  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
00705785  48 8D 45 A7                     lea rax, [rbp - 0x59]
00705789  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
0070578D  48 8D 15 2C 97 91 FF            lea rdx, [rip - 0x6e68d4]
00705794  83 65 03 00                     and dword ptr [rbp + 3], 0
00705798  B9 04 00 00 00                  mov ecx, 4
0070579D  83 65 13 00                     and dword ptr [rbp + 0x13], 0
007057A1  45 33 C0                        xor r8d, r8d
007057A4  83 65 23 00                     and dword ptr [rbp + 0x23], 0
007057A8  83 65 33 00                     and dword ptr [rbp + 0x33], 0
007057AC  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
007057B0  44 8D 49 02                     lea r9d, [rcx + 2]
007057B4  48 8D 45 AF                     lea rax, [rbp - 0x51]
007057B8  89 4D DF                        mov dword ptr [rbp - 0x21], ecx
007057BB  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
007057BF  48 8D 45 B7                     lea rax, [rbp - 0x49]
007057C3  48 89 45 F7                     mov qword ptr [rbp - 9], rax
007057C7  48 8D 45 BF                     lea rax, [rbp - 0x41]
007057CB  48 89 45 07                     mov qword ptr [rbp + 7], rax
007057CF  48 8D 45 C7                     lea rax, [rbp - 0x39]
007057D3  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
007057D7  48 8D 45 CF                     lea rax, [rbp - 0x31]
007057DB  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
007057DF  48 8D 45 D7                     lea rax, [rbp - 0x29]
007057E3  89 4D EF                        mov dword ptr [rbp - 0x11], ecx
007057E6  89 4D FF                        mov dword ptr [rbp - 1], ecx
007057E9  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
007057EC  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
007057EF  89 4D 2F                        mov dword ptr [rbp + 0x2f], ecx
007057F2  48 8B 0D 0F 5C 80 00            mov rcx, qword ptr [rip + 0x805c0f]
007057F9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007057FE  E8 1D 6F D1 FF                  call 0x14041c720
00705803  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
00705807  48 33 CC                        xor rcx, rsp
0070580A  E8 31 6E FA FF                  call 0x1406ac640
0070580F  48 81 C4 D0 00 00 00            add rsp, 0xd0
00705816  5D                              pop rbp
00705817  C3                              ret
00705818  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTracePolicyChange(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned __int64 v_stack_m4F;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB8;

    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 7360531)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m88 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8399494)));
    v_stack_m90 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8399454)));
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8399454)));
    v_stack_mA0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8399438)));
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8399438)));
    if ((*(unsigned __int8 *)(v_rip + 7741715)) == 0) goto loc_00705803;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8412315), v_rip - 7235764, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_mA8;
        a2 = v_rip - 7235796;
        a1 = 4;
        a3 = 0;
        v_stack_m78 = result;
        a4 = a1 + 2;
        result = v_stack_mA0;
        v_stack_m70 = (unsigned int)(a1);
        v_stack_m68 = result;
        result = v_stack_m98;
        v_stack_m58 = result;
        result = v_stack_m90;
        v_stack_m48 = result;
        result = v_stack_m88;
        v_stack_m38 = result;
        result = v_stack_m80;
        v_stack_m28 = result;
        result = v_stack_m78;
        v_stack_m60 = (unsigned int)(a1);
        v_stack_m50 = (unsigned int)(a1);
        v_stack_m40 = (unsigned int)(a1);
        v_stack_m30 = (unsigned int)(a1);
        v_stack_m20 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 8412175);
        v_stack_mB8 = result;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (208);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTracePolicyChange(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint64_t v_stack_m4F;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB8;

    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x705013)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m88 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x802A86)));
    v_stack_m90 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x802A5E)));
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x802A5E)));
    v_stack_mA0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x802A4E)));
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x802A4E)));
    if ((*(uint8_t *)(v_rip + 0x762113)) == 0) goto loc_00705803;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x805C9B), v_rip - 7235764, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_mA8;
        Arg2 = v_rip - 7235796;
        Arg1 = 4;
        Arg3 = 0;
        v_stack_m78 = result;
        a4 = Arg1 + 2;
        result = v_stack_mA0;
        v_stack_m70 = (uint32_t)(Arg1);
        v_stack_m68 = result;
        result = v_stack_m98;
        v_stack_m58 = result;
        result = v_stack_m90;
        v_stack_m48 = result;
        result = v_stack_m88;
        v_stack_m38 = result;
        result = v_stack_m80;
        v_stack_m28 = result;
        result = v_stack_m78;
        v_stack_m60 = (uint32_t)(Arg1);
        v_stack_m50 = (uint32_t)(Arg1);
        v_stack_m40 = (uint32_t)(Arg1);
        v_stack_m30 = (uint32_t)(Arg1);
        v_stack_m20 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x805C0F);
        v_stack_mB8 = result;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (208);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00705718&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00705718[BB_00705718]
  bb_00705766[BB_00705766]
  bb_00705781[BB_00705781]
  bb_00705803[BB_00705803]
  bb_00705818[BB_00705818]
  bb_00705718 -->|branch| bb_00705803
  bb_00705718 -->|fallthrough| bb_00705766
  bb_00705766 -->|branch| bb_00705803
  bb_00705766 -->|fallthrough| bb_00705781
  bb_00705781 -->|flow| bb_00705803
```
